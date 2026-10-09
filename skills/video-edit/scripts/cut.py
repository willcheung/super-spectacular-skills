#!/usr/bin/env python3
"""Assemble chosen takes from raw talking-head clips into one tight cut.

Usage: python3 cut.py edit.json

edit.json (paths relative to the file; the # comments are for illustration only, JSON has none):
{
  "raw_dir": "../raw",                 # folder with the source clips
  "out_dir": "assets",                 # writes cut.mp4 here
  "width": 1080, "height": 1920,       # 1080x1920 for Shorts, 1920x1080 for long-form
  "fps": 30,
  "warmth": "light",                   # none | light | medium (taste grade on top)
  "handle": "@yourhandle",             # optional; sync_data.py puts it on the end card
  "segments": [                        # [label, clip, start_s, end_s] on the source clip
    ["hook", "IMG_7825", 14.66, 25.70]
  ]
}

Per segment: boundaries snap to the quietest nearby audio frame, and pauses longer
than MAX_GAP shrink to KEEP_GAP (jump cuts). iPhone HDR (HLG) clips are converted
to SDR with the bundled LUT; SDR clips pass through. Output is labelled BT.709.
Writes <out_dir>/cut.mp4 and cuts.json (segment times + every cut point).
"""
import array, json, subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
LUT = SKILL / "assets" / "iphone_hlg_to_sdr.cube"
SR, HOP = 16000, 160              # 10ms analysis frames
MAX_GAP, KEEP_GAP = 0.30, 0.14    # pauses longer than MAX_GAP shrink to KEEP_GAP
MIN_PIECE = 0.25                  # shorter pieces flash on screen; merge them into a neighbour
SNAP = 0.15                       # search window (s) for snapping boundaries
WARMTH = {
    "none": "",
    "light": "colorbalance=rm=0.03:bm=-0.04:rh=0.01:bh=-0.015,eq=saturation=1.15:contrast=1.05",
    "medium": "colorbalance=rm=0.05:gm=-0.01:bm=-0.06:rh=0.02:bh=-0.03,eq=saturation=1.22:contrast=1.06",
}
SDR_TAGS = "setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv"


def ff_escape(path):
    """Quote a path for an FFmpeg filter option value."""
    return str(path).replace("\\", "\\\\").replace("'", "\\'").replace(":", "\\:")


def find_clip(raw, name):
    p = raw / name
    if p.exists():
        return p
    for ext in (".MOV", ".mov", ".MP4", ".mp4", ".m4v"):
        if (raw / f"{name}{ext}").exists():
            return raw / f"{name}{ext}"
    sys.exit(f"clip not found: {name} in {raw}")


def is_hlg(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=color_transfer", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True).stdout
    # csv output can carry a trailing comma from side data (e.g. iPhone rotation)
    return out.strip().split(",")[0] == "arib-std-b67"


def color_chain(path, w, h, warmth):
    if is_hlg(path):
        base = (f"scale={w}:{h}:in_color_matrix=bt2020:in_range=tv:out_range=pc,format=gbrp,"
                f"lut3d=file='{ff_escape(LUT)}':interp=tetrahedral,"
                f"scale=out_color_matrix=bt709:in_range=pc:out_range=tv,format=yuv420p,{SDR_TAGS}")
    else:
        base = f"scale={w}:{h},format=yuv420p,{SDR_TAGS}"
    return base + (f",{WARMTH[warmth]}" if WARMTH[warmth] else "")


def rms_frames(path):
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-vn", "-ac", "1",
                          "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
    a = array.array("h", pcm)
    return [(sum(x * x for x in a[i:i + HOP]) / HOP) ** 0.5 for i in range(0, len(a) - HOP, HOP)]


def snap(rms, t):
    lo, hi = max(0, int((t - SNAP) * 100)), min(len(rms) - 3, int((t + SNAP) * 100))
    best = min(range(lo, hi + 1), key=lambda i: (sum(rms[i:i + 3]), abs(i - t * 100)))
    return (best + 1) / 100


def keep_ranges(rms, start, end):
    s, e = int(start * 100), int(end * 100)
    seg = sorted(rms[s:e])
    thresh = max(seg[int(len(seg) * 0.9)] * 0.12, 60)
    ranges, cur, quiet = [], s, None
    for i in range(s, e):
        if rms[i] < thresh:
            quiet = i if quiet is None else quiet
        else:
            if quiet is not None and (i - quiet) / 100 > MAX_GAP:
                pad = KEEP_GAP / 2
                ranges.append((cur / 100, quiet / 100 + pad))
                cur = int((i / 100 - pad) * 100)
            quiet = None
    ranges.append((cur / 100, end))
    # Flash-length pieces (< MIN_PIECE) read as glitches. At a segment's edges they're
    # almost always a click or breath: drop them. In the middle, join one to its
    # neighbour only when the gap between them is short, so no dead air comes back;
    # otherwise keep it (it may be a real one-syllable word).
    short = lambda r: r[1] - r[0] < MIN_PIECE
    while len(ranges) > 1 and short(ranges[0]):
        ranges.pop(0)
    while len(ranges) > 1 and short(ranges[-1]):
        ranges.pop()
    merged = []
    for a, b in ranges:
        if merged and (short((a, b)) or short(merged[-1])) and a - merged[-1][1] <= MAX_GAP:
            merged[-1] = (merged[-1][0], b)
        else:
            merged.append((a, b))
    return merged


def main(cfg_path):
    cfg_path = Path(cfg_path).resolve()
    cfg = json.loads(cfg_path.read_text())
    base = cfg_path.parent
    raw = (base / cfg["raw_dir"]).resolve()
    out = (base / cfg.get("out_dir", "assets")).resolve()
    w, h, fps = cfg.get("width", 1080), cfg.get("height", 1920), cfg.get("fps", 30)
    warmth = cfg.get("warmth", "light")
    out.mkdir(parents=True, exist_ok=True)

    cache, pieces, timeline, t = {}, [], [], 0.0
    for label, clip, start, end in cfg["segments"]:
        path = find_clip(raw, clip)
        rms = cache.setdefault(path, rms_frames(path))
        start, end = snap(rms, start), snap(rms, end)
        rs = keep_ranges(rms, start, end)
        dur = sum(b - a for a, b in rs)
        timeline.append({"label": label, "clip": clip, "src": [start, end],
                         "start": round(t, 3), "end": round(t + dur, 3)})
        t += dur
        pieces += [(path, a, b) for a, b in rs]

    clips = sorted({p for p, _, _ in pieces})
    idx = {p: i for i, p in enumerate(clips)}
    chains = {p: color_chain(p, w, h, warmth) for p in clips}
    f = []
    for n, (p, a, b) in enumerate(pieces):
        i, d = idx[p], b - a
        f.append(f"[{i}:v]trim={a}:{b},setpts=PTS-STARTPTS,{chains[p]},fps={fps},setsar=1[v{n}]")
        f.append(f"[{i}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,"
                 f"afade=t=in:d=0.012,afade=t=out:st={max(0, d - 0.012):.3f}:d=0.012[a{n}]")
    f.append("".join(f"[v{n}][a{n}]" for n in range(len(pieces))) +
             f"concat=n={len(pieces)}:v=1:a=1[vc][ac]")
    f.append("[ac]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[ao]")
    cmd = ["ffmpeg", "-v", "error", "-y"]
    for p in clips:
        cmd += ["-i", str(p)]
    cmd += ["-filter_complex", ";".join(f), "-map", "[vc]", "-map", "[ao]",
            "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p",
            "-g", str(fps), "-color_primaries", "bt709", "-color_trc", "bt709",
            "-colorspace", "bt709", "-color_range", "tv",
            "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out / "cut.mp4")]
    subprocess.run(cmd, check=True)

    cut_points, acc = [], 0.0
    for _, a, b in pieces:
        cut_points.append(round(acc, 3))
        acc += b - a
    (base / "cuts.json").write_text(json.dumps({"segments": timeline, "cuts": cut_points}, indent=2))
    hdr = [p.name for p in clips if is_hlg(p)]
    print(f"{len(pieces)} pieces, {t:.1f}s total" + (f"  (HLG->SDR: {', '.join(hdr)})" if hdr else ""))
    for s in timeline:
        print(f"  {s['start']:7.2f}-{s['end']:7.2f}  {s['label']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
