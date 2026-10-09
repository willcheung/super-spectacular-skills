# Style rules

These are the defaults that came out of real edits and real notes. They aim at one thing: a viewer who would otherwise scroll keeps watching. When a rule here conflicts with `lessons.md`, lessons win (they're newer and more specific). For the owner's own videos, `brand-profile.md` preferences win over both.

## Pacing

- **Tight jump cuts.** Pauses over 0.30 s shrink to 0.14 s (`cut.py` does this). Talking-head content dies in the gaps.
- **Change the framing on every cut.** Alternate scale 1.00 / 1.12 at each jump cut (skip cuts closer than 0.6 s together). The zoom change hides the jump.
- **Punch in on the word that matters.** A 0.16 s push to 1.18–1.38 on the emotional word ("disappointing", "terrible", "safe"). Five or six per minute, not more; punches lose force when everything punches.
- **Something new on screen every 2–4 seconds** in a Short: a card, a counter tick, a stamp, a caption keyword. Long-form relaxes this (see formats.md).

## Layout (9:16, 1080×1920)

- **Top band (y ≈ 110–500): cards.** The face lives in the middle; the shirt area below holds captions. Cards may overlap hair, never eyes.
- **Captions at y ≈ 1250–1510**, centered, over the chest. Shorts UI covers roughly the bottom 400 px and a strip on the right; keep key content inside the 80% title-safe box.
- **Full-screen takeovers** are allowed when a visual is the point (a chart, a screenshot, the thesis line). They may cover the face. Keep captions running over them unless the takeover already shows the words.

## Captions

- Word-by-word pop (0.12 s, slight overshoot), groups of up to 3 words / ~15 characters, break at punctuation or a 0.35 s gap.
- Uppercase, heavy weight (900), ~88 px, light text with a thick dark stroke.
- **Keywords in the accent color** (numbers, the product/model name, the emotional word). Accent text must pass contrast; on footage use a slightly brighter accent with a dark stroke.
- Hide captions during a takeover or meme that already shows the words.

## Beat treatments

| Beat in the script | Treatment |
|---|---|
| Hook line | Card at 0:00 restating the tension in fewer words ("I gave the 'AGI' model a 3-hour job.") — visible on the first frame |
| A duration or count ("three hours", "10 more hours") | Counter that ticks to the number (pre-rendered steps, not text tweens; seek-safe) |
| A verdict ("disappointing", "terrible") | Rubber stamp slams in, slightly rotated, plus a punch-in |
| The thesis / one-line takeaway | Full-screen notebook takeover, words stacked and revealed on their spoken times |
| A claim about data the user has (usage, revenue, analytics) | Full-screen takeover of their real screenshot, annotated in sync with speech: baseline line, highlight box, measured multiplier |
| The thing being asked ("I said: make me more money") | Prompt card with lines appearing as spoken |
| Numbered lessons/steps | "LESSON N" chip card per lesson |
| An obviously sarcastic/ironic line | Meme beat: full-frame top/bottom meme text, vignette, punch-in, a small flipping 🙃-style face. Caption off. Hold ~1 s past the line, delay the next card |
| Call to action | Handle card on the word "follow" |

## Things that read as AI slop on video

- Overlays that restate exactly what is being said with no added information. A card should compress, quantify, or show proof.
- Generic stock reactions presented as real posts.
- Every card entering the same way. Vary: drop-in, slide, stamp, typewriter lines.
- Neon gradients, glow on everything, emoji soup.
