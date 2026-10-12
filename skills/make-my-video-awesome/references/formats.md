# Short vs long-form

One skill, two formats. Decide from what the user asks for; if they don't say, infer from the footage: portrait clips with a story under ~90 s → Short; landscape, or more than ~3 minutes of usable material → long-form. When it's genuinely ambiguous, ask once.

| | Short (Shorts / TikTok / Reels) | Long-form YouTube |
|---|---|---|
| Canvas | 1080×1920 | 1920×1080 (shoot 4K so you can punch in) |
| Target length | 30–75 s | whatever the content needs; cut every dead second anyway |
| Zoom rhythm | every jump cut alternates; 5–6 punches/min | every 2–3 cuts; fewer punches |
| Graphics density | something new every 2–4 s | cards at chapter changes, proof moments, and lists |
| Captions | big word-by-word, center | smaller lower-third, or off (YouTube CC exists) |
| Structure | hook → thesis → story → lessons → CTA | cold open → intro → chapters (with chapter cards) → recap → end screen |
| Extra deliverables | — | chapter timestamps for the description |
| Sound | per the creator's preference (ask; the owner's is in brand-profile.md) | consider a quiet bed; silence under 10+ minutes of talking feels empty — ask |

## How long-form is built differently

A 64 s Short renders in ~2 minutes through HyperFrames. A 15-minute video rendered the same way takes 30+ minutes per revision. So for long-form:

1. `cut.py` builds the A-roll at 1920×1080 exactly as for Shorts.
2. Apply the camera rhythm (zooms/punches) in the same pass or as FFmpeg crops on the cut.
3. Build each graphic moment (title, chapter cards, annotated screenshots, lower thirds, end screen) as its own short HyperFrames composition and render it — with alpha if it overlays footage, opaque if it's a takeover.
4. Composite them onto the A-roll at their timestamps with FFmpeg `overlay` / concat.

A note then re-renders only the piece that changed. This path is described, not yet battle-tested: verify the first long-form edit carefully (sync, alpha edges, color match between A-roll and takeovers) and record what you learn in lessons.md.
