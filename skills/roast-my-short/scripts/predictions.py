#!/usr/bin/env python3
"""Log roast-my-short predictions in the creator's private tracker and score them later.

Usage:
  python3 predictions.py log TRACKER --video NAME --version V (--report REPORT.md | --pred 58/40 --score 6 --post no) [--len 56.7]
  python3 predictions.py actual TRACKER --video NAME --actual 61/44 [--version V]
  python3 predictions.py pending TRACKER

The table lives in a "### Roast predictions" subsection of the tracker's
"## Results log" (created on first use). Per-video numbers stay in that private
file; the skill's public calibration notes get only the generic pattern.

`actual` fills the latest non-script row for the video still waiting for stats
(or --version), plus any hook-check ("script") rows for it, and prints the miss:
positive = the reviewer predicted too high.
"""
import argparse, datetime, re, sys
from pathlib import Path

HEAD = "### Roast predictions"
INTRO = ("Logged by the roast-my-short skill before posting; actuals come from the 24 h pull. "
         "Misses become generic calibration notes in the skill's public references, never these numbers.")
COLS = ["Date", "Video", "Version", "Len", "Score", "Post as-is", "Pred 2s / 5s", "Actual 2s / 5s (24h)", "Miss 2s / 5s"]
EMPTY = {"", "–", "-"}


def row(cells):
    return "| " + " | ".join(cells) + " |"


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def section(lines):
    """(start, end) line indexes of the predictions table rows; creates the subsection if missing."""
    try:
        h = next(i for i, l in enumerate(lines) if l.strip() == HEAD)
    except StopIteration:
        try:
            rl = next(i for i, l in enumerate(lines) if re.match(r"## Results log\b", l))
        except StopIteration:
            sys.exit("tracker has no '## Results log' section")
        end = next((i for i in range(rl + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        while end > rl + 1 and lines[end - 1].strip() in {"", "---"}:
            end -= 1
        block = ["", HEAD, "", INTRO, "", row(COLS), row(["-"] * len(COLS))]
        lines[end:end] = block
        h = end + 1
    first = next(i for i in range(h, len(lines)) if lines[i].startswith("|")) + 2
    last = first
    while last < len(lines) and lines[last].startswith("|"):
        last += 1
    return first, last


def pct_pair(s):
    a, b = (int(round(float(x.strip().rstrip("%")))) for x in s.split("/"))
    return a, b


def from_report(path):
    m = re.search(r"PREDICTION:\s*2s=(\d+)%?\s+5s=(\d+)%?\s+score=([\d.]+)(?:/10)?\s+post=(\S+)",
                  Path(path).read_text())
    if not m:
        sys.exit(f"no PREDICTION line in {path}")
    return f"{m[1]}/{m[2]}", m[3], m[4]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["log", "actual", "pending"])
    ap.add_argument("tracker")
    ap.add_argument("--video"); ap.add_argument("--version")
    ap.add_argument("--report"); ap.add_argument("--pred"); ap.add_argument("--score"); ap.add_argument("--post")
    ap.add_argument("--len"); ap.add_argument("--actual")
    a = ap.parse_args()

    path = Path(a.tracker).expanduser()
    lines = path.read_text().split("\n")
    first, last = section(lines)

    if a.cmd == "pending":
        rows = [cells(l) for l in lines[first:last]]
        todo = [r for r in rows if len(r) == len(COLS) and r[7] in EMPTY]
        for r in todo:
            print(f"{r[0]}  {r[1]}  {r[2]}  pred {r[6]}")
        print(f"{len(todo)} waiting for stats" if todo else "nothing waiting for stats")
        return

    if not a.video:
        sys.exit("--video is required")

    if a.cmd == "log":
        if a.report:
            pred, score, post = from_report(a.report)
        elif a.pred:
            pred, score, post = a.pred, a.score or "–", a.post or "–"
        else:
            sys.exit("pass --report or --pred")
        p2, p5 = pct_pair(pred)
        new = row([datetime.date.today().isoformat(), a.video, a.version or "–",
                   f"{float(a.len):g}s" if a.len else "–", f"{score}/10", post,
                   f"{p2}% / {p5}%", "–", "–"])
        lines.insert(last, new)
        path.write_text("\n".join(lines))
        print(f"logged: {new}")
        return

    # actual
    if not a.actual:
        sys.exit("--actual 2s/5s is required")
    a2, a5 = pct_pair(a.actual)
    idx = [i for i in range(first, last)
           if len(cells(lines[i])) == len(COLS) and a.video.lower() in cells(lines[i])[1].lower()
           and cells(lines[i])[7] in EMPTY]
    if not idx:
        sys.exit(f"no row for '{a.video}' waiting for stats")
    edits = [i for i in idx if cells(lines[i])[2] == "script"]
    vid = [i for i in idx if cells(lines[i])[2] != "script" and (not a.version or cells(lines[i])[2] == a.version)]
    if vid:
        edits.append(vid[-1])
    for i in edits:
        c = cells(lines[i])
        p2, p5 = pct_pair(c[6])
        c[7], c[8] = f"{a2}% / {a5}%", f"{p2 - a2:+d} / {p5 - a5:+d}"
        lines[i] = row(c)
        print(f"{c[1]} {c[2]}: predicted {p2}/{p5}, actual {a2}/{a5}, miss {p2 - a2:+d} / {p5 - a5:+d} pts")
    path.write_text("\n".join(lines))
    print("Now reread that review, find why it missed, and add one generic dated line to "
          f"{Path(__file__).resolve().parent.parent / 'references/calibration.md'} (no titles or numbers).")


if __name__ == "__main__":
    main()
