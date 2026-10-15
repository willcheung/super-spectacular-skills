# Swipe Review

An [Agent Skill](https://agentskills.io) that gives your Short a blunt, independent review and predicts where viewers swipe away.

The editor knows why every beat is there, so they forgive it. Viewers don't. This skill builds a review packet from files only (a frame every 1.5 s and the word-timed transcript) and hands it to a fresh reviewer that never saw the edit being made. You get back:

- a hook verdict for 0–5 s, with predicted kept-at-2 s and 5 s against *your* benchmarks
- a second-by-second swipe map (dead air, repetition, slow explanation, confusing jump, too-long takeover, unclear payoff) plus the strongest moments
- whether the length is earned, with exact cuts quoted from your own words
- payoff/ending, phone-size readability and collision checks
- the top 5 changes ranked by retention impact, a score /10, and post-as-is yes/no

It also checks a script's hook before you film, and after you publish it compares its prediction with your real 24 h stats and writes a generic calibration note, so it gets sharper over time.

## Requirements

- Python 3, FFmpeg, Node.js (`npx hyperframes`)
- [make-my-video-awesome](../make-my-video-awesome/) installed alongside (transcription and the lessons files)
- An agent that can start a subagent or a fresh headless session

## Use it

```text
Run swipe-review on ~/videos/my-short before I watch it.
```

```text
Swipe-review renders/final.mp4 against my results log in ~/notes/tracker.md.
```

```text
Hook-check my shoot sheet plans/my-shoot-sheet.md before I film.
```

```text
My last Short's 24-hour stats are in. Calibrate swipe-review.
```

## What's inside

| Path | Purpose |
|---|---|
| `SKILL.md` | The workflow: packet, independent reviewer, log, act, calibrate |
| `references/reviewer-brief.md` | The reviewer's role, what it reads, and its fixed deliverable |
| `references/calibration.md` | Generic notes on past prediction misses (grows over time) |
| `scripts/prepare.py` | Builds the packet (frames, transcript) and the reviewer's prompt |
| `scripts/predictions.py` | Logs predictions in your private tracker and scores them against real stats |

Your benchmarks and per-video numbers stay in your own tracker; only generic lessons land in this skill.
