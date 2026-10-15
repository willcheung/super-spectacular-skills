#!/usr/bin/env python3
"""Build a swipe-review packet and the exact prompt for a fresh reviewer.

Usage:
  python3 prepare.py PROJECT_DIR   [options]   # HyperFrames project (edit mode)
  python3 prepare.py VIDEO.mp4     [options]   # finished render (render mode)
  python3 prepare.py SCRIPT.md     [options]   # script / shoot sheet (hook check)

Options:
  --tracker PATH   creator's private tracker; its "## Results log" section becomes
                   the benchmarks (the predictions table is left out)
  --profile PATH   creator profile for the reviewer (default: make-my-video-awesome's
                   brand-profile.md, which is the repo owner's; pass "none" for anyone else)
  --label NAME     version label, e.g. v3 (default: review)
  --every SECS     frame interval (default 1.5)
  --out DIR        packet folder (default: PROJECT/snapshots/review, or <video>-review/)

Prints the packet folder and PROMPT.md. PROMPT.md goes to the temp dir, not the
project, so private benchmarks and doc paths aren't copied onto the footage drive.
Pass its contents verbatim to a fresh subagent; add nothing about the edit.
"""
import argparse, json, re, subprocess, sys, tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
VIDEO_EXTS = {".mp4", ".mov", ".m4v"}


def find_mmva():
    for p in (SKILL.parent / "make-my-video-awesome",
              Path.home() / ".claude/skills/make-my-video-awesome",
              Path.home() / ".agents/skills/make-my-video-awesome"):
        if (p / "scripts/transcribe.py").exists():
            return p.resolve()
    sys.exit("make-my-video-awesome not found next to this skill or in ~/.claude/skills")


def sh(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        sys.exit(f"failed: {' '.join(map(str, cmd))}\n{(r.stderr or r.stdout)[-2000:]}")
    return r.stdout


def probe_duration(path):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-of", "csv=p=0", str(path)]).strip())


def times(duration, every):
    """Every `every` s from 0, plus the last moment (the ending is where the payoff lands)."""
    n = int(duration / every - 1e-6) + 1
    ts = [round(i * every, 2) for i in range(n) if i * every < duration - 0.05]
    end = round(duration - 0.1, 2)
    return ts + [end] if end - ts[-1] > 0.5 else ts


def fmt_t(t):
    return f"{t:g}"


def words_txt(mmva, transcript):
    return sh([sys.executable, str(mmva / "scripts/transcribe.py"), "words", str(transcript)])


def benchmarks(tracker):
    if not tracker:
        return None
    text = Path(tracker).expanduser().read_text()
    m = re.search(r"^## Results log\b.*?(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return None
    sec = re.sub(r"^### Swipe-review predictions\b.*?(?=^### |\Z)", "", m.group(0), flags=re.S | re.M)
    return sec.strip().rstrip("-").strip()


def edit_mode(proj, mmva, out, every):
    html = (proj / "index.html").read_text()
    root = re.search(r"<[^>]*data-composition-id=\"[^\"]*\"[^>]*>", html)
    dur = re.search(r'data-duration="([\d.]+)"', root.group(0)) if root else None
    duration = float(dur.group(1)) if dur else probe_duration(proj / "assets/cut.mp4")

    transcript = next((p for p in (proj / "transcript.json", proj / "assets/transcript.json") if p.exists()), None)
    if not transcript:
        sys.exit(f"no transcript.json in {proj}; run make-my-video-awesome's transcribe.py cut {proj}")
    cut = proj / "assets/cut.mp4"
    if cut.exists() and transcript.stat().st_mtime < cut.stat().st_mtime - 1:
        sys.exit(f"{transcript} is older than {cut}: the cut changed since it was transcribed.\n"
                 f"Run: python3 {mmva}/scripts/transcribe.py cut '{proj}'")

    ts = times(duration, every)
    for attempt in (1, 2):
        print(f"snapshotting {len(ts)} frames of {duration:.2f} s …", file=sys.stderr)
        sh(["npx", "hyperframes", "snapshot", str(proj), "-o", str(out), "--describe", "false",
            "--no-end", "--at", ",".join(fmt_t(t) for t in ts)], cwd=proj)
        # A snapshot can come back with the overlays on black when the footage didn't load in time
        # (seen once, fine on retry). Real footage frames are ~1 MB+; overlays on black are ~50 KB.
        sizes = sorted(f.stat().st_size for f in out.glob("frame-*.png"))
        if sizes and sizes[len(sizes) // 2] > 150_000:
            break
        print("frames look empty (footage didn't load); retrying once", file=sys.stderr)
    else:
        sys.exit(f"snapshot frames in {out} have no footage. Open contact-sheet-1.jpg, then check the "
                 "video loads in the Studio preview before reviewing.")
    (out / "transcript.txt").write_text(words_txt(mmva, transcript))
    return duration


def render_mode(video, mmva, out, every):
    duration = probe_duration(video)
    out.mkdir(parents=True, exist_ok=True)
    for old in list(out.glob("frame-*.png")) + list(out.glob("contact-sheet-*.jpg")):
        old.unlink()
    ts = times(duration, every)
    pad = max(2, len(str(len(ts) - 1)))
    print(f"extracting {len(ts)} frames of {duration:.2f} s …", file=sys.stderr)
    for i, t in enumerate(ts):
        sh(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(video), "-frames:v", "1",
            str(out / f"frame-{i:0{pad}d}-at-{fmt_t(t)}s.png")])
    sh(["ffmpeg", "-v", "error", "-y", "-pattern_type", "glob", "-framerate", "1",
        "-i", str(out / "frame-*.png"), "-vf", "scale=270:-2,tile=4x2:padding=6:color=white",
        "-q:v", "3", str(out / "contact-sheet-%d.jpg")])
    tdir = out / "t"
    sh(["npx", "hyperframes", "transcribe", str(video), "-d", str(tdir)])
    (out / "transcript.txt").write_text(words_txt(mmva, tdir / "transcript.json"))
    return duration


def prompt(mode, target, packet, duration, mmva, profile, bench, every):
    lines = [
        "You are reviewing a short-form video you have never seen, for a creator you have never met.",
        "Read your brief first and follow it exactly, including its deliverable format and word limit.",
        "",
        f"- Brief: {SKILL / 'references/reviewer-brief.md'}",
        f"- Your calibration notes: {SKILL / 'references/calibration.md'}",
        f"- Creator's lessons: {mmva / 'references/lessons.md'}",
    ]
    if profile:
        lines.append(f"- Creator's profile: {profile}")
    lines.append("")
    if mode == "hook":
        lines += ["Mode: hook check (pre-filming). Nothing is filmed yet.",
                  f"- Script / shoot sheet: {target}"]
    else:
        lines += [f"Mode: {mode}. A {duration:.1f} s vertical Short (1080x1920).",
                  f"- Word-timed transcript (seconds): {packet / 'transcript.txt'}",
                  f"- Frames every {every:g} s, named frame-NN-at-Xs.png, plus contact sheets "
                  f"(contact-sheet-N.jpg, in time order left to right, top to bottom): {packet}/"]
    lines.append("")
    if bench:
        lines += ["Creator's benchmarks (their own results log; predict against these):",
                  "<benchmarks>", bench, "</benchmarks>"]
    else:
        lines.append("No creator benchmarks were provided. Say so, and predict against general short-form norms.")
    lines += ["",
              "Open only the files listed above. Don't read anything else in or around the project "
              "(HTML, edit plans, notes, other reviews): you're judging what a viewer sees and hears.",
              "Reply with the report only, ending with the PREDICTION line."]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("--tracker")
    ap.add_argument("--profile")
    ap.add_argument("--label", default="review")
    ap.add_argument("--every", type=float, default=1.5)
    ap.add_argument("--out")
    a = ap.parse_args()

    mmva = find_mmva()
    src = Path(a.input).expanduser().resolve()
    profile = None if (a.profile or "").lower() == "none" else \
        Path(a.profile).expanduser().resolve() if a.profile else mmva / "references/brand-profile.md"

    if src.is_dir() and (src / "index.html").exists():
        mode, packet = "edit", Path(a.out).resolve() if a.out else src / "snapshots/review"
        duration = edit_mode(src, mmva, packet, a.every)
    elif src.suffix.lower() in VIDEO_EXTS:
        mode, packet = "render", Path(a.out).resolve() if a.out else src.parent / f"{src.stem}-review"
        duration = render_mode(src, mmva, packet, a.every)
    elif src.suffix.lower() in {".md", ".txt"}:
        mode, packet, duration = "hook", None, 0.0
    else:
        sys.exit(f"don't know how to review {src}: pass a HyperFrames project dir, a video, or a .md script")

    name = src.stem if src.is_file() else src.name
    pdir = Path(tempfile.gettempdir()) / "swipe-review" / f"{name}-{a.label}"
    pdir.mkdir(parents=True, exist_ok=True)
    pfile = pdir / "PROMPT.md"
    pfile.write_text(prompt(mode, src, packet, duration, mmva, profile, benchmarks(a.tracker), a.every))

    info = {"mode": mode, "duration": round(duration, 2), "packet": str(packet) if packet else None,
            "prompt": str(pfile), "benchmarks": bool(a.tracker)}
    if packet:
        info["frames"] = len(list(packet.glob("frame-*.png")))
    print(json.dumps(info, indent=1))


if __name__ == "__main__":
    main()
