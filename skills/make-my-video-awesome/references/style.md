# Style rules

These are the defaults that came out of real edits and real notes. They aim at one thing: a viewer who would otherwise scroll keeps watching. When a rule here conflicts with `lessons.md`, lessons win (they're newer and more specific). For the owner's own videos, `brand-profile.md` preferences win over both.

## Pacing

- **Tight jump cuts.** Pauses over 0.30 s shrink to 0.14 s (`cut.py` does this). Talking-head content dies in the gaps.
- **Change the framing on every cut.** Alternate scale 1.00 / 1.12 at each jump cut (skip cuts closer than 0.6 s together). The zoom change hides the jump.
- **Punch in on the word that matters.** A 0.16 s push to 1.18–1.38 on the emotional word ("disappointing", "terrible", "safe"). Five or six per minute, not more; punches lose force when everything punches.
- **Something new on screen every 2–4 seconds** in a Short: a card, a counter tick, a stamp, a caption keyword. Long-form relaxes this (see formats.md).
- **The opening makes sense with the sound off.** Most phone viewers start muted. In the first 3 seconds the hook card, the captions, and the face or the strongest visual must carry the claim on their own; if the first frame only works with audio, rework it.
- **Nothing off-camera sits dead.** When the face is off screen or shrunk, the visual moves: a slow push toward the line that matters, a slow drift down a page, rows building, outline boxes or highlights landing on the spoken words. Never a plain still held under captions. Lessons win on how: a full article excerpt stays whole and unzoomed, and its motion is the highlights landing as spoken; a receipt zooms slowly to its one line rather than fast-scrolling.

## Layout (9:16, 1080×1920)

- **Top band (y ≈ 165–500): cards.** Start top cards at y ≈ 165. In Instagram's feed the username + "Original audio" row sits over roughly y 90–195 of the 1080×1920 frame (after Instagram's own top crop), and Facebook's top UI is similar; a card at ≈ 120 put its chip under that row, and 140 still touched it. Much lower (≈ 250) covers the forehead. Measured from a real feed screenshot; keep chips and text below y ≈ 200. The face lives in the middle and the shirt area below holds captions. Cards may overlap hair, never eyes.
- **Captions at y ≈ 1250–1510**, centered, over the chest (inside the 3:4 grid crop too). Shorts UI covers roughly the bottom 400 px and a strip on the right; keep key content inside the 80% title-safe box.
- **Split (visual on top, speaker below)** is the middle ground between a top-band card and a full takeover: the visual fills roughly the top 45% (y 0–880) and the speaker fills the rest, face about 40% down their panel, captions on the seam. Use it when the visual needs more room than a card but the face should stay (the first 5 s, a demo the speaker reacts to, a receipt that supports rather than carries the beat). The template's camera fills the whole frame with the face about 36% down, so a panel laid on top would cover the eyes: for a split, move the camera wrapper down into the lower panel (and snapshot to check the face is whole) before the panel comes in.
- **Full-screen takeovers** are allowed when a visual is the point (a chart, a screenshot, the thesis line). They may cover the face. Keep captions running over them unless the takeover already shows the words. Receipts that carry a beat (an article, a screenshot, a pricing page) stay full-size and legible for as long as reading them takes. A common Shorts default caps full-screen B-roll at about 3.5 s to keep the face present; use it for generic B-roll (ambient screen footage, establishing shots) only, never to shrink or cut short a receipt, and keep the ~8–10 s cap on back-to-back takeovers from lessons.md.

## Captions

- Word-by-word pop (0.12 s, slight overshoot), groups of up to 3 words / ~15 characters, break at punctuation or a 0.35 s gap.
- **Never over the mouth or chin.** Check a snapshot on every framing (punch-ins and low-sitting speakers push the chin down into the caption band). If it collides, lower the captions for that beat (staying above y ≈ 1510) or ease the punch-in; on a split, they sit on the seam.
- Uppercase, heavy weight (900), ~88 px, light text with a thick dark stroke.
- **Keywords in the accent color** (numbers, the product/model name, the emotional word). Accent text must pass contrast; on footage use a slightly brighter accent with a dark stroke.
- Hide captions during a takeover or meme that already shows the words.
- **Never run a clip with its own burned-in subtitles under ours.** Two caption tracks fight and neither reads. Crop the clip's subtitles out, pick another moment, or hide ours for that beat.

## Beat treatments

| Beat in the script | Treatment |
|---|---|
| Hook line | Card at 0:00 restating the tension in fewer words ("I gave the 'AGI' model a 3-hour job.") — visible on the first frame |
| A duration or count ("three hours", "10 more hours") | Counter that ticks to the number (pre-rendered steps, not text tweens; seek-safe) |
| A verdict ("disappointing", "terrible") | Rubber stamp slams in, slightly rotated, plus a punch-in; over real proof of the failure when available (the agent's "done" + the creator's bug report) |
| The thesis / one-line takeaway | Full-screen notebook takeover, words stacked and revealed on their spoken times |
| A claim about data the user has (usage, revenue, analytics) | Full-screen takeover of their real screenshot, annotated in sync with speech: baseline line, highlight box, measured multiplier |
| A claim about a company or public fact ("they just raised $2B") | The original article as a full-screen takeover over the face: a real excerpt (headline, publisher/date, and the paragraph or list that holds the claim) with the backing phrases highlighted as they are spoken, no zoom (see "Articles and news") |
| The thing being asked ("I said: make me more money") | The real prompt/spec/chat message if it exists (zoomed); otherwise a prompt card with lines appearing as spoken |
| Numbered lessons/steps | One card that builds: lesson 1 alone, then 1 (dimmed) + 2, then 1 + 2 (dimmed) + 3, each row landing on its spoken line. Hide it during any meme beat in between and bring it back with the next row. Viewers see the whole list forming, which makes the final frame save-worthy |
| An obviously sarcastic/ironic line | Meme beat: full-frame top/bottom meme text, vignette, punch-in, a small flipping 🙃-style face. Caption off. Hold ~1 s past the line, delay the next card |
| Call to action | Handle card on the word "follow" |

## Real material first

Real screenshots and screen recordings beat generated graphics whenever they exist. They read as genuine, and TikTok/Instagram audiences scroll past things that look AI-made. Generated graphics are great for what has no real source: a thesis line, a counter, a stamp, a meme beat, a chart you build from real numbers.

Making real material work at phone size:

- **Screen recordings** are the best proof: full-screen takeover, cover the face. Speed up long scrolls (3–4×) so a wall of text reads as "a lot", play the key moment at 1–2×, then hold the last frame (`tpad=stop_mode=clone`) and push in on the line that matters with an outline box. Pre-cut the clip with FFmpeg to exactly the beat's length; mute it.
- **Screenshots** of chat threads or docs: show the whole thing for a beat (it proves it's real), then zoom into the one line. A full Slack message at phone width is unreadable; never just shrink it.
- **Size receipts to be seen.** A phone screenshot, a pricing page, an article: if it carries the beat, make it big (most of the frame width) and lay it over the face, with outline boxes landing on the spoken words. A small card in the top band reads as decoration.
- **Outline boxes** go inside the zoom wrapper so they scale with the image. Measure positions from the actual frame (character widths are a good guide) and snapshot to check; they're easy to land half a word off.
- **Keep every line of text whole.** A receipt, page or screenshot never shows words chopped at the frame edge; crop to whole lines or a whole card, or zoom less. Half a sentence reads as a crop mistake and makes viewers doubt the receipt.
- **Logos only from the brand's official file** (press kit, the site's own SVG), never redrawn or generated. Without one, write the name in text.
- **Posts on X** the creator embedded or referenced: show them as faithful cards (real name, handle, date, avatar, exact text, truncation marked with "…"). Highlight the phrase being talked about.
- **Articles and news** cited on camera: use the original source (the company's own post or docs, a filing, the outlet that broke the story), not an aggregator or summary blog. Capture the real page in a browser at about 1080 px wide (2x for sharpness). Show it as a full-screen takeover over the face (dim the footage behind it): a real excerpt the width of the frame, with the headline, publisher and date on top and the paragraph or bullet list that backs the claim below, stitched from the page if the two are far apart. Highlight the backing phrases (a marker-style fill behind the text) on the words that say them. Don't zoom into one line: the whole excerpt on screen is what proves it's a real article. Keep the body text large enough to read on a phone (crop side margins and sidebars, wrap the headline narrower if needed). If the page is paywalled or the backing sentence is buried, ask the creator for their own screenshot. Put the links in the caption or pinned comment.
- macOS names screen recordings with a narrow no-break space before AM/PM; glob the filename instead of typing it.

Ask the creator for real material at these moments, typically: the tool/agent saying it's done, the creator's own reaction or bug report, before/after of the result, dashboards or usage/billing pages, the post they're reacting to, the spec or prompt they used.

## Things that read as AI slop on video

- Overlays that restate exactly what is being said with no added information. A card should compress, quantify, or show proof.
- Generic stock reactions presented as real posts.
- Every card entering the same way. Vary: drop-in, slide, stamp, typewriter lines.
- Neon gradients, glow on everything, emoji soup.
