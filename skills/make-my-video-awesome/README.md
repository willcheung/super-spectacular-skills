# Video Edit

An [Agent Skill](https://agentskills.io) that edits raw talking-head footage into a finished video: YouTube Shorts, TikTok, Reels, or long-form YouTube.

You record and give notes. The agent does the rest:

- reads every clip's transcript and finds the story (hook first, best take of each line, asides dropped)
- cuts the takes together with tight jump cuts and no dead air
- fixes iPhone HDR footage so it doesn't look washed out
- adds punch-in zooms, word-by-word captions, kinetic cards, counters, stamps, full-screen screenshot takeovers, and meme beats with [HyperFrames](https://hyperframes.heygen.com)
- renders an MP4 and checks it (color tags, still/frozen spans, levels, contact sheet)
- shows you the beat plan before building, so changes land before anything is built
- writes every preference from your notes into `references/lessons.md`, so the next edit already knows

## Requirements

- FFmpeg + ffprobe
- Node.js (for `npx hyperframes`) and the HyperFrames agent skills (`npx skills add heygen-com/hyperframes`)
- Python 3 (scripts use the standard library; `fit_lut.py` also needs numpy + pillow)
- Several GB of free disk space for renders

## Use it

```text
Use make-my-video-awesome on the raw clips in ~/videos/astra. Make a scroll-stopping Short.
```

```text
Notes on the edit: cut "this is the kind of stuff I build" but keep "follow along".
At 0:50 I say "during" out of nowhere, cut it. When I say "everyone's job is safe", do a sarcastic meme.
```

```text
Use make-my-video-awesome to turn these 12 clips into a 10-minute YouTube video with chapters.
```

## What's inside

| Path | Purpose |
|---|---|
| `SKILL.md` | The workflow |
| `references/style.md` | Pacing, layout, captions, which beat gets which treatment |
| `references/formats.md` | Short vs long-form differences, long-form build strategy |
| `references/color.md` | iPhone HDR → SDR, refitting the LUT |
| `references/lessons.md` | Preferences learned from notes (grows over time) |
| `references/brand-profile.md` | The owner's brand (handle, palette); not applied to other users |
| `scripts/cut.py` | Edit plan (`edit.json`) → `assets/cut.mp4` + `cuts.json` |
| `scripts/transcribe.py` | Per-clip and per-cut transcripts |
| `scripts/energy.py` | Find real silence when transcript timings drift |
| `scripts/sync_data.py` | Push words/cut points/duration into the composition |
| `scripts/verify.py` | Post-render checks + contact sheet |
| `scripts/fit_lut.py` | Refit the HLG→SDR LUT for new lighting |
| `assets/iphone_hlg_to_sdr.cube` | The fitted LUT |
| `templates/short-example.html` | A complete working Short composition to start from |

Tip: turn off **Settings → Camera → Record Video → HDR Video** on iPhone for footage meant for this pipeline. Color then needs no conversion at all.

## Credits

The beat-plan check before building, the final check in step 9, and a few Shorts rules in `references/style.md` (the split layout, sound-off openings, moving off-camera visuals, captions clear of the mouth, whole lines of text, official logos, no subtitled clips under the captions) are adapted from [video-short](https://github.com/petergyang/video-short) by Peter Yang (MIT License).
