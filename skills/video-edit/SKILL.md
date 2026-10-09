---
name: video-edit
description: Edit raw talking-head footage (phone or camera clips of someone speaking to camera) into a finished, scroll-stopping video — YouTube Shorts, TikTok, Reels, or long-form YouTube. Picks the best takes from the transcript, removes mistakes and dead air with tight jump cuts, fixes iPhone HDR color, then adds punch-in zooms, word-by-word captions, kinetic cards, screenshot takeovers, and meme beats with HyperFrames, and renders an MP4. Use this whenever the user points at a folder of raw clips, says "edit this", "cut this into a short", "make this a YouTube video", gives timestamped notes on an edit ("at 0:19 the stamp covers my face"), or wants their video editing style applied, even if they never say "skill" or "HyperFrames".
---

# Video Edit

Turn raw talking-head clips into an edited video, the way a human editor would: find the story, cut the takes, then dress it. The user directs; you edit. They record and give notes; everything else is yours.

The pipeline has two layers, and keeping them separate is what makes revisions cheap:

1. **The cut** (`scripts/cut.py`, FFmpeg): which takes, in what order, with dead air removed and color fixed. Output: `assets/cut.mp4` + `cuts.json`.
2. **The dress** (HyperFrames composition): zooms, captions, cards, takeovers, timed to a transcript *of the cut*. Output: the rendered MP4.

Re-cutting never breaks the dress as long as you re-sync (`scripts/sync_data.py`) and shift overlay times by the amount the cut moved.

Read these as you reach each stage, not all up front:

| When | Read |
|---|---|
| Before planning the edit | [references/style.md](references/style.md) — the visual and pacing rules |
| Deciding Short vs long-form | [references/formats.md](references/formats.md) |
| Footage is iPhone HDR, or color looks washed out/off | [references/color.md](references/color.md) |
| Before writing any brand element (handle, colors, end card) | [references/brand-profile.md](references/brand-profile.md) — only for its owner; ask other users for theirs |
| Every time, before building | [references/lessons.md](references/lessons.md) — general lessons from past edits; obey them. The owner's personal preferences live in brand-profile.md. |

Before writing composition HTML, load the `hyperframes` skill and follow its composition contract. This skill decides *what* goes on screen; HyperFrames decides *how* a composition must be built.

## Workflow

### 1. Inspect the footage

For each clip: duration, orientation (a `rotation=-90` side-data tag means a landscape-coded file is really portrait), and `color_transfer` (`arib-std-b67` = iPhone HDR/HLG). Look at a few frames per clip (`python3 scripts/verify.py --source --out WORK_DIR CLIP` writes a contact sheet into WORK_DIR, never into the footage folder) so you know who is on camera and where their face sits. Check free disk space (`df -h ~`): a render needs several GB of temp space, and HDR renders far more.

### 2. Transcribe each clip separately

```bash
python3 scripts/transcribe.py clips RAW_DIR WORK_DIR/t
```

`hyperframes transcribe` writes `transcript.json` into whatever directory it runs in, so batch-transcribing into one folder silently keeps only the last clip. The script gives each clip its own folder and prints word timings.

### 3. Find the story and write the edit plan

Read every transcript before choosing anything. Raw talking-head footage has retakes, false starts, asides, and the same line said three ways. Pick:

- **Hook first.** The most tension-creating line goes at 0:00, even if it was recorded in the middle. The hook earns the next 3 seconds; the thesis earns the rest.
- **One take per beat.** When a line was recorded twice, keep the cleaner, more energetic one.
- **Cut asides that don't serve the arc** (a coffee run, a detail only the speaker cares about). Mention what you dropped so the user can veto.
- **Keep the speaker's words.** You choose and order; you never paraphrase or invent lines.

Scaffold the project first, into a new folder (`init` refuses a folder that already has files):

```bash
npx hyperframes init PROJECT_DIR --non-interactive
```

Then write `PROJECT_DIR/edit.json` (format in the `cut.py` docstring): `[label, clip, start, end]` per segment, in viewing order, plus `raw_dir` and, for the creator's own videos, `handle`. Everything after this reads and writes inside `PROJECT_DIR`.

### 4. Cut, then verify the cut by ear

```bash
python3 scripts/cut.py PROJECT_DIR/edit.json
python3 scripts/transcribe.py cut PROJECT_DIR
```

Read the cut's transcript start to finish. Look for stray fragments at segment seams ("and, but if…", a half "during"). Whisper word times drift 0.4–0.6 s, so when a seam is dirty, find real silence with `python3 scripts/energy.py CLIP FROM TO` and move the boundary into it. Trust the energy bars over the transcript. Re-cut until the transcript reads clean.

### 5. Build the dress

Copy [templates/short-example.html](templates/short-example.html) to `PROJECT_DIR/index.html`: a complete, working Short (camera engine, caption engine, card/stamp/counter/takeover/meme components) with `__WORDS__`/`__CUTS__`/`__HANDLE__` placeholders. Its overlays are the worked example's content; they reference `assets/usage.png`, which isn't bundled, so swap in this video's proof or delete that section. Replace its overlay content with this video's beats; keep the engines. Then:

```bash
python3 scripts/sync_data.py PROJECT_DIR
```

Plan overlays from the cut transcript's word times: each overlay lands on the word that motivates it (a "3 HOURS" timer starts on "three hours"; a stamp slams on "terrible"). See style.md for which beat gets which treatment.

### 6. Check, snapshot, preview

Run `npm run check` (fix every error; resolve contrast warnings), snapshot the moment each overlay lands (`npx hyperframes snapshot --at t1,t2,…`) and actually look at the contact sheet, then open the Studio preview (`npx hyperframes preview --background`) for the user.

### 7. Take notes, revise, learn

The user reviews and gives notes, often with timestamps. Apply them. For any note that reflects a *preference* rather than a one-off fix ("I don't use sound", "captions too big", "my handle is…"), add it to the skill (dated, one line, with why): general lessons go in `references/lessons.md`; one creator's taste goes in their profile (the owner's is `references/brand-profile.md`). This feedback loop is the point of the skill: the same note should never be needed twice.

### 8. Render and verify

```bash
npm run render -- --output renders/NAME.mp4
python3 scripts/verify.py renders/NAME.mp4
```

Render only after the user approves the preview. Then check the verify output: bt709 tags (an HDR tag means players will wash it out), zero frozen spans, sensible luma levels. Look at the contact sheet before saying it's done.

## Things that went wrong before (and why the scripts exist)

- **Washed-out color.** iPhone HDR footage labelled HDR got tone-mapped twice; then a hand grade overshot. `cut.py` now converts HLG with a LUT fitted to HyperFrames' own preview and labels output SDR. Details in color.md.
- **Stray words at seams.** Trusting Whisper's timestamps. Use `energy.py`.
- **Disk full mid-project.** The user freed space by deleting files, including a raw clip and `cut.mp4`. Before telling someone to free space, name what is safe to delete; if raw clips vanish, ask where the originals live (camera roll, external drive) instead of guessing.
- **Studio edits the HTML.** The preview stamps `data-hf-id` attributes onto elements. Any regex edit must tolerate extra attributes, and should assert it matched.
- **Face-tracked props drift.** People move their heads a lot while talking. Without face tracking, put meme gags on the full frame (top/bottom text, vignette, punch-in), not on the face.

## Honesty rules

- Don't fabricate posts, tweets, or quotes and present them as real. Illustrative reactions are fine only when obviously generic, and say so to the user. Prefer real screenshots the user provides or you capture.
- Numbers on screen must come from the footage or the user's data. If you derive one (like "~9× a normal day" measured from a chart's bar heights), say how.
- Report what you verified and what you didn't. If a render had warnings, mention them.
