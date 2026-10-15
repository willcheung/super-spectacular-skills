---
name: roast-my-short
description: Independent, blunt short-form strategist review of a Short (TikTok, Reels, YouTube Shorts) that predicts where viewers swipe away. Snapshots the edit every 1.5 s, exports the cut's word-timed transcript, and hands only those files to a fresh subagent that never saw the edit being made, so it judges the video instead of defending it. Returns a hook verdict with predicted 2 s / 5 s retention against the creator's own benchmarks, a second-by-second swipe map, exact cuts quoted from the creator's words, a top-5 change list, a score /10, and post-as-is yes/no. Also checks a script or shoot sheet's hook before filming, and calibrates its predictions against real stats after publishing. Use whenever an edit is ready for a first watch, the user asks "roast my short", "would people swipe?", "review this short", "is the hook strong enough?", "rate this video", or wants a second opinion on a cut or a script, even if they never say "roast-my-short".
---

# Roast My Short

A second pair of eyes that has never seen the edit being made. The editor knows why every beat is there, so they forgive it; a viewer doesn't. This skill builds a review packet from files only, gives it to a fresh reviewer with no edit context, and gets back a blunt prediction of where people swipe.

Three modes, picked from the input:

| Input | Mode | What the reviewer gets |
|---|---|---|
| HyperFrames project dir (has `index.html`) | **edit** | a frame every 1.5 s of the dressed composition + the cut's word-timed transcript |
| `.mp4` / `.mov` | **render** | a frame every 1.5 s extracted with FFmpeg + a fresh word-timed transcript |
| `.md` script or shoot sheet | **hook check** (before filming) | the script itself |

## 1. Build the packet

```bash
python3 scripts/prepare.py INPUT [--tracker PRIVATE_TRACKER.md] [--label v3]
```

It prints the packet folder and the path of `PROMPT.md`, the exact message for the reviewer. What it does:

- **edit:** `npx hyperframes snapshot DIR -o DIR/snapshots/review --describe false --at 0,1.5,3,…` up to the root composition's `data-duration`, then `transcribe.py words DIR/transcript.json` (from make-my-video-awesome) into `transcript.txt`. It stops if the transcript is older than `assets/cut.mp4`: re-run `transcribe.py cut DIR` first, since a stale transcript gives a wrong swipe map.
- **render:** FFmpeg frames at the same interval plus contact sheets into `<name>-review/`, and a Parakeet/Whisper transcript via `npx hyperframes transcribe`.
- **hook check:** no frames; the prompt points at the script.

**Benchmarks are the creator's, never hardcoded.** With `--tracker`, the script copies only the tracker's `## Results log` section (minus the predictions table) into the prompt, so the reviewer sees the creator's real 2 s / 5 s / full-watch numbers without the rest of the tracker, whose idea and edit notes would leak the editor's intent. Without a tracker, the reviewer says it has no benchmark and predicts against general short-form norms. Find the tracker in the creator's own instructions (a project `AGENTS.md`/`CLAUDE.md`) or ask; never guess a path.

The prompt also points the reviewer at make-my-video-awesome's `references/lessons.md` and `references/brand-profile.md` (so it doesn't recommend something the creator has already ruled out, like music; the brand profile is the repo owner's, so for anyone else pass `--profile THEIR_PROFILE.md` or `--profile none`), at [references/reviewer-brief.md](references/reviewer-brief.md) (role and the fixed deliverable), and at [references/calibration.md](references/calibration.md) (its own past prediction errors).

## 2. Run the reviewer in a fresh subagent

Independence is the point. The reviewer must not share the session that made the edit.

- **Claude Code:** `Agent` tool, `general-purpose`, prompt = the contents of `PROMPT.md` verbatim, or just "Your full instructions are in PROMPT_PATH. Read it first and follow it exactly." Don't add a word about what the edit is going for, what changed since last version, or what you're worried about. If you want a second opinion on a specific worry, leave it out anyway; a good reviewer finds it, and if it doesn't, viewers might not either.
- **No subagent tool** (Codex, others): start a fresh headless session with the same prompt, e.g. `claude -p "$(cat PROMPT.md)"` or `codex exec "$(cat PROMPT.md)"`.
- Don't resume or message an earlier reviewer for a new version. Each version gets a new reviewer, so it isn't anchored on its last score.

Save the reviewer's report verbatim to `PROJECT/reviews/YYYY-MM-DD-<label>.md` (render mode: next to the packet). Not inside `snapshots/review/`: the next snapshot run clears that folder.

## 3. Log the prediction

The report ends with a `PREDICTION:` line. Log it in the creator's private tracker:

```bash
python3 scripts/predictions.py log TRACKER --video "My hook title" --version v3 --report PROJECT/reviews/YYYY-MM-DD-v3.md
```

This adds a row to a `### Roast predictions` table inside the tracker's Results log (creating it the first time). Per-video numbers live there and nowhere else: never in this public skill. Hook checks log too (version `script`), so the pre-filming call can be scored later.

## 4. Act on it

Sort the report's changes into two piles:

- **No-brainers: just fix them.** Text colliding with captions, the face, or platform UI; empty, half-loaded, or unreadable cards; a stray fragment at a seam; a frame that's black or frozen. Re-snapshot the spot to confirm.
- **Judgment calls: take them to the creator** with your own recommendation (agree, disagree, or partly). Reorders, cutting the creator's lines, dropping a gag, changing length, a different hook. The creator decides.

**Creator notes override the reviewer.** If the creator already asked for something the reviewer pushes against (they wanted the article excerpt full-size; the reviewer wants it smaller), keep the creator's version and say so in one line. The reviewer never saw those notes, by design.

Don't chase the score. A re-review after fixes is worth it when the hook or the order changed, not for polish.

## 5. Calibrate after publishing

When the video's real 24 h stats are pulled (kept-at-2 s and 5 s from TikTok Studio or similar):

```bash
python3 scripts/predictions.py actual TRACKER --video "My hook" --actual 61/44
python3 scripts/predictions.py pending TRACKER   # rows still waiting for stats
```

`actual` fills the latest pre-publish row for that video and prints the miss in points. Then reread that review and ask why it missed: what did the reviewer overrate or underrate? Append one dated line to [references/calibration.md](references/calibration.md): the pattern, the direction, and a size band (within 5 pts / 5–15 / over 15). Generic only: no title, no view counts, no actual percentages, because this file is public and per-video stats stay private. A miss within 5 points on both numbers still gets a line ("on target for an opens-on-the-claim hook") so the reviewer learns what it's good at, not only what it's bad at.

## Scripts

| Script | Does |
|---|---|
| `scripts/prepare.py` | builds the review packet and `PROMPT.md` for any of the three modes |
| `scripts/predictions.py` | `log` / `actual` / `pending` against the predictions table in the creator's tracker |

Requires: Python 3 (standard library), FFmpeg, Node (`npx hyperframes`), and the make-my-video-awesome skill installed alongside (for `transcribe.py` and the lessons files).
