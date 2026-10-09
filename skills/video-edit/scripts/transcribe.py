#!/usr/bin/env python3
"""Transcribe raw clips (one folder each) or a finished cut, and print word timings.

Usage:
  python3 transcribe.py clips RAW_DIR OUT_DIR   # every clip -> OUT_DIR/<clip>/transcript.json
  python3 transcribe.py cut PROJECT_DIR         # assets/cut.mp4 -> assets/transcript.json
  python3 transcribe.py words TRANSCRIPT.json [FROM_S] [TO_S]

`hyperframes transcribe` always writes transcript.json into its project dir, so
transcribing several clips into one dir silently overwrites. This keeps them apart.
Uses Parakeet automatically when installed (`npx hyperframes models install parakeet`),
which has tighter word timings than Whisper.
"""
import json, subprocess, sys
from pathlib import Path

EXTS = {".mov", ".mp4", ".m4v"}


def run(src, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(["npx", "hyperframes", "transcribe", str(src), "-d", str(out_dir)],
                   check=True, capture_output=True)


def lines(path, a=0.0, b=1e9):
    w = json.loads(Path(path).read_text())
    w = w if isinstance(w, list) else w.get("words", [])
    sel = [x for x in w if a <= x["start"] <= b]
    out, cur, st = [], [], None
    for x in sel:
        st = x["start"] if st is None else st
        cur.append(f"{x['text'].strip()}({x['start']:.2f}-{x['end']:.2f})")
        if x["text"].strip().endswith((".", "?", "!")):
            out.append(f"[{st:6.2f}] " + " ".join(cur)); cur, st = [], None
    if cur:
        out.append(f"[{st:6.2f}] " + " ".join(cur))
    return "\n".join(out)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "clips":
        raw, out = Path(sys.argv[2]), Path(sys.argv[3])
        for clip in sorted(p for p in raw.iterdir() if p.suffix.lower() in EXTS):
            run(clip, out / clip.stem)
            print(f"=== {clip.stem}\n{lines(out / clip.stem / 'transcript.json')}")
    elif mode == "cut":
        proj = Path(sys.argv[2])
        run(proj / "assets" / "cut.mp4", proj)
        t = proj / "assets" / "transcript.json"
        if not t.exists():
            t = proj / "transcript.json"
        print(lines(t))
    elif mode == "words":
        print(lines(sys.argv[2], *(float(v) for v in sys.argv[3:5])))
    else:
        sys.exit(__doc__)
