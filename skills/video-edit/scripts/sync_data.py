#!/usr/bin/env python3
"""Push the cut's word timings and cut points into the composition.

Usage: python3 sync_data.py PROJECT_DIR

Replaces `const WORDS = ...;` and `const CUTS = ...;` in PROJECT_DIR/index.html
(or the __WORDS__ / __CUTS__ placeholders in a fresh template) and updates the
root and a-roll data-duration to the cut length. Run it after every re-cut.
"""
import json, re, sys
from pathlib import Path

proj = Path(sys.argv[1])
html = proj / "index.html"
t = proj / "assets" / "transcript.json"
if not t.exists():
    t = proj / "transcript.json"
w = json.loads(t.read_text())
w = w if isinstance(w, list) else w["words"]
words = json.dumps([[x["text"].strip(), round(x["start"], 2), round(x["end"], 2)] for x in w])
cuts = json.dumps(json.loads((proj / "cuts.json").read_text())["cuts"])
# cuts.json is exact; the container duration includes audio padding
dur = json.loads((proj / "cuts.json").read_text())["segments"][-1]["end"]
dur = f"{dur:.2f}"

s = html.read_text()
s = s.replace("__WORDS__", words).replace("__CUTS__", cuts).replace("__DURATION__", dur)
s = re.sub(r"const WORDS = \[.*?\];", lambda m: f"const WORDS = {words};", s, flags=re.S)
s = re.sub(r"const CUTS = \[.*?\];", lambda m: f"const CUTS = {cuts};", s, flags=re.S)
s = re.sub(r"const D = [\d.]+;", f"const D = {dur};", s)
s = re.sub(r'(data-composition-id="main"[^>]*?data-duration=")[\d.]+"', rf'\g<1>{dur}"', s)
s = re.sub(r'(id="aroll"[^>]*?data-duration=")[\d.]+"', rf'\g<1>{dur}"', s)
html.write_text(s)
print(f"synced {len(w)} words, {len(json.loads(cuts))} cuts, duration {dur}s")
