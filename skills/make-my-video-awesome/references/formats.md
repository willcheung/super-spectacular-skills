# Short vs long-form

One skill, two formats. Decide from what the user asks for; if they don't say, infer from the footage: portrait clips with a story under ~90 s → Short; landscape, or more than ~3 minutes of usable material → long-form. When it's genuinely ambiguous, ask once.

| | Short (Shorts / TikTok / Reels) | Long-form YouTube |
|---|---|---|
| Canvas | 1080×1920 | 1920×1080 (shoot 4K so you can punch in) |
| Target length | 30–75 s | whatever the content needs; cut every dead second anyway |
| Zoom rhythm | every jump cut alternates; 5–6 punches/min | every 2–3 cuts; fewer punches |
| Graphics density | something new every 2–4 s | cards at chapter changes, proof moments, and lists |
| Captions | big word-by-word, center | smaller lower-third, or off (YouTube CC exists) |
| Structure | hook → thesis → story → lessons → CTA | cold open (20–30 s: event, stakes, roadmap) → intro → chapters (with chapter cards and a re-hook at each break) → recap only if viewers need it → end screen |
| Extra deliverables | — | the post package: a title plus an A/B title; two covers that test different ideas, paired so neither repeats its title; a description (below); chapter timestamps; a source link for every on-screen claim; the creator's links; a pinned comment that asks a question; an English .srt built from the cut's word timings with proper nouns corrected |
| Sound | per the creator's preference (ask; the owner's is in brand-profile.md) | consider a quiet bed; silence under 10+ minutes of talking feels empty — ask |

## How long-form is built differently

A 64 s Short renders in ~2 minutes through HyperFrames. A 15-minute video rendered the same way takes 30+ minutes per revision. So for long-form:

1. `cut.py` builds the A-roll at 1920×1080 exactly as for Shorts.
2. Apply the camera rhythm (zooms/punches) in the same pass or as FFmpeg crops on the cut.
3. Build each graphic moment (title, chapter cards, annotated screenshots, lower thirds, end screen) as its own short HyperFrames composition and render it — with alpha if it overlays footage, opaque if it's a takeover.
4. Composite them onto the A-roll at their timestamps with FFmpeg `overlay` / concat.

A note then re-renders only the piece that changed. This path is described, not yet battle-tested: verify the first long-form edit carefully (sync, alpha edges, color match between A-roll and takeovers) and record what you learn in lessons.md.

What actually worked on a 12-minute edit (2026-10-26): one HyperFrames composition over the chunked A-roll (cut and transcribe in chapter-sized chunks, then join), about 100 clips. A full render took about 25 minutes, so iterate in the Studio preview and `snapshot`, render once after approval, and budget one re-render for what `verify.py` finds. The per-piece overlay path above wasn't needed.

**Long-form description:** the first two lines carry the search phrases (the title is for the home feed) and the creator's credential. Don't answer the question the cover asks; list what the video covers instead. Then chapters, the creator's links, the sources, and disclosures (re-created chats, not investment advice, not sponsored). Set the video language (it turns on auto-captions), "not made for kids", and upload the .srt.

## Separate screen and face recordings

When the creator records the screen silently and the face-cam separately, the face-cam audio is the master track. Cut the A-roll from the face-cam transcript first, then place each screen clip on the words that describe it (the creator usually filmed while watching the recording, so the spoken cue tells you which file and which moment). Layouts, in order of preference: full-screen takeover with the face in a small corner bubble during demos; straight cuts between face and screen for short proofs. Trim dead cursor time inside a screen clip instead of speeding up the whole clip, and match the screen clip's length to the line, not the other way round. Ask for a re-record rather than stretching a clip that's too short.
