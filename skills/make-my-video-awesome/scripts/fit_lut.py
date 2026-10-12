#!/usr/bin/env python3
"""Refit the HLG->SDR LUT to HyperFrames' own preview of new footage.

Usage: python3 fit_lut.py WORK_DIR OUT.cube     (needs numpy + pillow)

WORK_DIR must contain pairs in_<n>.png / ref_<n>.png of the same frame:
  in_<n>.png  : ffmpeg -ss T -i hlg.mp4 -frames:v 1 \
                  -vf "scale=1080:1920:in_color_matrix=bt2020:in_range=tv:out_range=pc,format=rgb24" in_<n>.png
  ref_<n>.png : `npx hyperframes snapshot --at T` of a one-video composition playing hlg.mp4
See references/color.md for the full recipe. Fits per-channel curves plus a 3x3
matrix (out = M @ curve(in) + b), prints the error, writes a 33^3 .cube.
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image

work, out_cube = Path(sys.argv[1]), sys.argv[2]
X, Y = [], []
for p in sorted(work.glob("in_*.png")):
    ref = work / p.name.replace("in_", "ref_")
    a = np.asarray(Image.open(p).convert("RGB"), dtype=np.float64) / 255
    b = np.asarray(Image.open(ref).convert("RGB").resize(Image.open(p).size), dtype=np.float64) / 255
    X.append(a.reshape(-1, 3)); Y.append(b.reshape(-1, 3))
if not X:
    sys.exit("no in_*.png / ref_*.png pairs found")
X, Y = np.concatenate(X), np.concatenate(Y)

BINS, curves = 64, []
for c in range(3):
    idx = np.minimum((X[:, c] * BINS).astype(int), BINS - 1)
    xs, ys = [], []
    for k in range(BINS):
        m = idx == k
        if m.sum() > 200:
            xs.append(X[m, c].mean()); ys.append(np.median(Y[m, c]))
    xs = [0.0] + xs + [1.0]
    ys = [max(0.0, ys[0] - xs[1] * 0.5)] + ys + [min(1.0, ys[-1] + (1 - xs[-2]) * 0.8)]
    curves.append((np.array(xs), np.maximum.accumulate(np.array(ys))))


def apply_curves(rgb):
    return np.stack([np.interp(rgb[:, c], *curves[c]) for c in range(3)], axis=1)


C = apply_curves(X)
coef, *_ = np.linalg.lstsq(np.hstack([C, np.ones((len(C), 1))]), Y, rcond=None)


def model(rgb):
    c = apply_curves(rgb)
    return np.clip(np.hstack([c, np.ones((len(c), 1))]) @ coef, 0, 1)


print(f"mean abs error (0-255): naive {np.abs(X - Y).mean() * 255:.2f} -> fitted {np.abs(model(X) - Y).mean() * 255:.2f}")
g = np.linspace(0, 1, 33)
bb, gg, rr = np.meshgrid(g, g, g, indexing="ij")
vals = model(np.stack([rr.ravel(), gg.ravel(), bb.ravel()], axis=1))
with open(out_cube, "w") as f:
    f.write('TITLE "iPhone HLG to SDR (matched to HyperFrames preview)"\nLUT_3D_SIZE 33\n')
    for v in vals:
        f.write("%.6f %.6f %.6f\n" % tuple(v))
print(f"wrote {out_cube}")
