#!/usr/bin/env python3
"""Check a rendered video before handing it over.

Usage: python3 verify.py VIDEO [T1 T2 ...]

Reports duration, size, color tags (must be bt709), frozen-frame spans, luma levels,
and writes VIDEO-check.jpg: frames at the given times (default: 6 evenly spaced).
"""
import subprocess, sys
from pathlib import Path


def probe(v, entries):
    return subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", entries,
                           "-of", "default=nw=1", v], capture_output=True, text=True).stdout.strip()


v = sys.argv[1]
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v],
                           capture_output=True, text=True).stdout)
print(f"duration {dur:.2f}s, {Path(v).stat().st_size / 1e6:.1f} MB")
tags = probe(v, "stream=width,height,color_transfer,color_primaries")
print(tags.replace("\n", "  "))
if "arib-std-b67" in tags or "smpte2084" in tags:
    print("WARNING: output is tagged HDR; players will tone-map it (usually washed out)")

fz = subprocess.run(["ffmpeg", "-v", "info", "-i", v, "-vf", "freezedetect=n=0.001:d=0.6", "-an", "-f", "null", "-"],
                    capture_output=True, text=True).stderr
starts = [float(l.split("freeze_start: ")[1]) for l in fz.splitlines() if "freeze_start" in l]
lens = [float(l.split("freeze_duration: ")[1]) for l in fz.splitlines() if "freeze_duration" in l]
print(f"still spans >0.6s: {len(starts)}")
for a, d in zip(starts, lens + [None] * len(starts)):
    print(f"  {a:7.2f}s  {'%.2fs' % d if d else 'to end'}")
if starts:
    print("  (fine if they fall on intentional still graphics like takeovers; a stuck camera shot is a bug)")

st = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(dur / 2), "-i", v, "-frames:v", "1", "-vf",
                     "signalstats,metadata=print:file=-", "-f", "null", "-"], capture_output=True, text=True).stdout
vals = {l.split("=")[0].split(".")[-1]: l.split("=")[1] for l in st.splitlines() if "signalstats" in l}
print("mid-frame luma low/avg/high: {} / {} / {}  saturation {}".format(
    vals.get("YLOW"), vals.get("YAVG"), vals.get("YHIGH"), vals.get("SATAVG")))

times = [float(x) for x in sys.argv[2:]] or [dur * (i + 0.5) / 6 for i in range(6)]
out = str(Path(v).with_name(Path(v).stem + "-check.jpg"))
inputs, filt = [], []
for i, t in enumerate(times):
    inputs += ["-ss", f"{t:.2f}", "-i", v]
    filt.append(f"[{i}:v]trim=end_frame=1,scale=270:-1[f{i}]")
filt.append("".join(f"[f{i}]" for i in range(len(times))) + f"hstack={len(times)}")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-frames:v", "1", out],
               check=True)
print(f"contact sheet: {out}")
