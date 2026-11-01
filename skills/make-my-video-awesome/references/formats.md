# Short vs long-form

One skill, two formats. Decide from what the user asks for; if they don't say, infer from the footage: portrait clips with a story under ~90 s → Short; landscape, or more than ~3 minutes of usable material → long-form. When it's genuinely ambiguous, ask once.

| | Short (Shorts / TikTok / Reels) | Long-form YouTube |
|---|---|---|
| Canvas | 1080×1920 | 1920×1080 (shoot 4K so you can punch in) |
| Target length | Start around 35–50 s when useful; let the complete story earn its length | Match the promised experience; preserve meaningful pauses |
| Zoom rhythm | Deliberate emphasis, with amplitude and cadence from the profile | Calm framing; motivated, restrained changes |
| Graphics density | Proof, explanation, orientation or a joke when needed | Large proof and concept takeovers; a calm face between them |
| Captions | Readable phrase or word captions, with platform-safe placement | Follow the creator's preference; the owner's are native captions, without burned-in text |
| Structure | hook → thesis → story → lessons → CTA | cold open (20–30 s: event, stakes, roadmap) → intro → chapters (with chapter cards and a re-hook at each break) → recap only if viewers need it → end screen |
| Extra deliverables | Platform package when requested | Upload package and corrected native captions; see the packaging owner below |
| Sound | Read the creator's existing audio preference | Read the creator's existing audio preference; a long duration does not imply music |

## How long-form is built differently

A 64 s Short rendered in ~2 minutes in one project; long-form can take much longer per revision. The current starting path is chunked A-roll with one HyperFrames composition, described below. The following per-piece approach is an optional alternative, not the required pipeline:

1. `cut.py` builds the A-roll at 1920×1080 exactly as for Shorts.
2. Apply the camera rhythm (zooms/punches) in the same pass or as FFmpeg crops on the cut.
3. Build each graphic moment (title, chapter cards, annotated screenshots, lower thirds, end screen) as its own short HyperFrames composition and render it — with alpha if it overlays footage, opaque if it's a takeover.
4. Composite them onto the A-roll at their timestamps with FFmpeg `overlay` / concat.

A note then re-renders only the piece that changed. This path is described, not yet battle-tested: verify the first long-form edit carefully (sync, alpha edges, color match between A-roll and takeovers) and record what you learn in lessons.md.

What actually worked on a 12-minute edit (2026-10-26): one HyperFrames composition over the chunked A-roll (cut and transcribe in chapter-sized chunks, then join), about 100 clips. A full render took about 25 minutes, so iterate in the Studio preview and `snapshot`, render once after approval, and budget one re-render for what `verify.py` finds. The per-piece overlay path above wasn't needed.

**Packaging owner:** use [video-director's packaging method](../../video-director/references/packaging.md) for titles, paired covers, description, final chapters, corrected captions, source links, next watch and relevant settings. This editor produces and verifies the media; the package must reflect the actual cut. Choose audience settings from the real content, not from a blanket template.

## Separate screen and face recordings

When the creator records the screen silently and the face-cam separately, the face-cam audio is the master track. Cut the A-roll from the face-cam transcript first, then place each screen clip on the words that describe it (the creator usually filmed while watching the recording, so the spoken cue tells you which file and which moment). Layouts, in order of preference: full-screen takeover with the face in a small corner bubble during demos; straight cuts between face and screen for short proofs. Trim dead cursor time inside a screen clip instead of speeding up the whole clip, and match the screen clip's length to the line, not the other way round. Ask for a re-record rather than stretching a clip that's too short.
