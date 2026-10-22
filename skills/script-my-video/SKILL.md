---
name: script-my-video
description: Plan and script a talking-head video before it's filmed — YouTube Shorts, TikTok, Reels, or long-form YouTube. Interviews the creator for their real story, numbers and receipts, writes 2–3 provocative-but-true hook variants, sources every claim, and produces a shoot sheet (numbered clips with a word-for-word hook, bridge lines, questions with talking points, written punchlines, and a word-for-word close) plus a storyboard and a shot list of screens to capture. Runs a hook check before filming. Use whenever someone wants to plan, script, outline, or storyboard a video, asks "what should I say on camera?", "write me a shoot sheet", "turn this idea into a Short", "plan the YouTube video", or "what do I film?", even if they never say "script" or "skill". Not for editing footage that already exists (that's make-my-video-awesome).
---

# Script My Video

Plan a talking-head video so the footage can actually be edited into something good. Most problems that sink an edit are made before filming: a hook that starts with a wind-up, clips recorded as isolated one-liners that don't flow, a claim nobody can prove on screen, a moment that needed a screen recording nobody captured. The edit can't fix those. This skill fixes them on paper.

The output is a **plan** with a **shoot sheet** in it: what the creator says (hook and close word for word, everything else as questions they answer in their own words), what's on screen at each beat, and what to capture before the camera rolls.

## Pick the format first

| Video | Read | Depth |
|---|---|---|
| Short (TikTok, Reels, YouTube Shorts), personal story | [references/shorts.md](references/shorts.md) | Light: brief, hooks, shoot sheet, captures |
| Short, explainer or news | [references/shorts.md](references/shorts.md) | Medium: light + sources table + an on-screen note on every beat |
| Long-form YouTube | [references/youtube.md](references/youtube.md) | Full: medium + chapters, research notes, a still of the biggest visual |
| A build: one shoot → a long video **and** Shorts | both | Full for the long video; each Short gets its own hook takes in the same session ([youtube.md](references/youtube.md#shorts-from-a-long-video)) |

Depth follows what the video *does*, not its length: any claim stated as fact on screen needs a source, even in a 40-second Short.

## Before you start

- **Read [references/lessons.md](references/lessons.md).** General lessons from past scripts; obey them.
- **Voice.** Spoken lines come from the creator's own material. Use the `no-ai-slop-writing` skill for anything written word for word. If the creator is that skill's profiled writer, load its `references/writer-voice-profile.md`, including the "How he talks on camera" and "Video scripts" sections (they set the humor level for scripts).
- **The creator's own setup.** Look in their project instructions (`AGENTS.md`/`CLAUDE.md`) for where plans are saved, their tracker (ideas, status, results log), and their benchmarks. Use those paths; don't invent them. With no setup, save `plans/<video-name>.md` next to their notes and say where it went.

## Where ideas come from

When the creator asks what to make (not how to script a given idea), source ideas from the audience before brainstorming:

- **Earned the right to explain:** only topics they've actually done or are a few steps ahead on. The test: could they talk 30 minutes about it with zero prep? That's also what makes the video impossible for a generic creator to copy.
- **A swipe file:** the top posts in their niche on the platform they care most about. Note each hook and topic. Borrow the hook's *shape*, never the content, and fill it with the creator's own receipt.
- **Unanswered comments:** read the comments under popular videos in the niche (and the creator's own) for questions nobody answered. Those are next videos.
- **The creator's own winners:** transcribe their best-performing past videos and read them next to their comments. That shows how their hooks, timing and jokes actually work, which beats guessing at their style, and the comments become the next ideas.
- **The viewer's words:** keep a list of problems in the exact words viewers use ("I don't have the money and I'm scared I'll look stupid"), and use those words in hooks and titles instead of the creator's jargon.
- **Repeatable formats:** a creator who repeats a few named formats and a recurring phrase gets recognized faster than one who invents a new shape every time. Prefer an idea that fits one of their existing formats.

## Workflow

### 1. Interview (one round, before writing anything)

Ask 3–5 short questions, only what their notes, posts and tracker can't answer. Look at anything public yourself first (their site, dashboards, repos, past posts). Aim for:

- **The before:** a real moment the old way failed. What they tried, what went wrong.
- **The proof moment:** one specific time the thing did something they wouldn't have caught or done.
- **Their take:** an opinion they'd defend in the comments.
- **Numbers** they'd say on camera: cost, time, counts. Ask where each one comes from.
- **What they can show:** screens, recordings, live pages, objects. The shot list only asks for things that exist.

Their answers are source material. Never fill a gap with a plausible invention; mark it `[NEED: …]` and keep going.

### 2. Brief (five lines)

Who it's for · the one idea · what the viewer walks away with · the main receipt (the single best piece of proof) · what's *not* in this one (the idea that belongs in a different video).

One idea per video. If the brief needs two ideas, it's two videos.

**Three idea tests before writing anything.** If one fails, fix the idea or pick another; scripting won't rescue it.
1. **Zero context:** a stranger scrolling past gets it without knowing the niche, the tool, or the news. Insider ideas can still work as search-led YouTube titles, but they rarely travel in a swipe feed.
2. **A setback and a comeback:** something goes wrong before the payoff (it failed, it got the message wrong, the number looked bad), then the recovery. Hook → build-up → payoff alone is predictable, and predictable is when people leave.
3. **An open loop:** the hook can leave a question the video answers.

### 3. Title and hooks

Write **2–3 hook variants, word for word**, and the creator films all of them.

- **The first spoken words are the claim.** No greeting, no "so I tried…", no "in this video". A viewer decides in the first two seconds.
- **Each variant is a different shape**, so the takes test something: an outcome or number, a failure, a contrarian claim. Fill each shape with one of the creator's specific facts; a shape with no fact is filler.
- **Provocative, even controversial, and true.** A cautious hook is the failure mode. But never claim more than the receipt shows, and never put words in someone's mouth.
- **Opinions can be absolute; facts stay exact.** A take about the world can be as sweeping as the creator believes ("anyone can build anything with AI", "software an agent can do for you is dead"): viewers argue with it in the comments, and that helps the video. Don't soften a take into "almost" or "might." A fact about the creator's own story, a number, a date, a quote or a result stays exactly true ("months", not "immediately", if it took months), because a checkably wrong fact makes the top comment a correction instead of the debate. When the two sit side by side, let the absolute take come first and the exact receipt prove it ("AI can make it obsolete overnight. Mine got made pointless in one weekend.").
- **Lead with the human stakes; name the tool second.** "My AI works while I sleep" needs no context; a product name does.
- **Open a loop, don't close it.** The hook plants a question the video answers ("why would you kill it?", "how did it do that?"). It doesn't have to be phrased as a question; a statement with an obvious "why?" works as well. A hook that gives away the result ("This YouTuber turned 100 cans into powder") leaves no reason to stay.
- **Each hook names its first frame:** what's on screen besides the face, and the 3–6 word cover text. Line, visual and text land together in the first second.

Add the cover text and **one title or caption per platform**: the same video is found differently on each. Swipe feeds (TikTok, Reels) rank on watch behavior, so the caption and cover carry the human stakes. YouTube also surfaces Shorts through search and topic, so the YouTube title leads with the words people actually search for (the tool, the topic), then the stakes. Pull those words from YouTube Studio's search insights when the creator has them. For long-form, the thumbnail text must add to the title, not repeat it.

### 4. Sources

| # | Claim as said | Source (publisher, date, link) | Highlight to show | Strength |
|---|---|---|---|---|

- **Original sources:** the company's own post or docs, a filing, the reporter who broke it. Aggregators are leads, not sources.
- **Strength:** `primary` (original source, or the creator's own data), `secondary` (credible outlet reporting it), `weak` (one second-hand blog). Weak claims get cut or said as "reportedly", never shown as fact.
- **The creator's own data is the best receipt:** usage charts, logs, dashboards, bills. A number with no known origin gets verified or re-measured before filming, not after.
- **Capture web receipts now,** during planning (screenshot, crop to headline + the one line), so the edit isn't hunting for them later.

### 5. One story, in order

Before writing clips, decide the spine: what happens first, what it causes, where it lands. Then:

- **Every clip opens with a bridge line, word for word,** that hands off from the clip before ("So when I wake up…", "That's why…"). This is what makes the cut flow instead of feeling like random scenes strung together.
- **Pick one visual thread** that runs the whole video (an object, a clock, a running count) and changes from beat to beat, instead of a new card on every beat.
- **Plan the transition out of each beat** (a match cut, the object transforming, a real B-roll action). Hard card swaps reset the viewer.
- **Have them film the clips in order, in one continuous recording.** A flubbed clip restarts from its bridge line.

### 6. The shoot sheet

Use [templates/shoot-sheet.md](templates/shoot-sheet.md). Numbered clips: A1, A2… (one letter per video when a session feeds several).

- **First clip: the hook variants, word for word.** 2–3 takes each.
- **Middle clips:** the bridge line (word for word) → a **question** the creator answers to camera → 2–4 talking-point bullets from their own words and sourced facts → **1–2 punchlines, word for word**, marked **Line:**. Jokes depend on wording, so write them out; the creator can say them as written or riff. Optional riffs are marked *Optional*.
- **Last clip: the close and CTA, word for word.** End on the payoff or a callback, then straight into the CTA with no warm-up.
- **On screen** for each clip: what the viewer sees, concretely (the real screen, what's highlighted, roughly how long). Use the editing skill's treatments where they fit (`make-my-video-awesome`'s `references/style.md`).

Talking points, not lines to read: the edit only uses what the creator actually says, so sounding natural beats reciting. Write a full teleprompter script only when they ask for one.

Length check: about 2.5 spoken words per second (≈150 a minute).

### 7. Shot list

- **Screen captures before filming.** They decide what's true. Each one: what to show, how (screen recording, screenshot, slow scroll), roughly how long, which clip it serves. Note anything to blur (names, balances, card numbers, other people's handles).
- **Real B-roll:** 1–3 short phone shots of real actions (closing a laptop, a notification lighting up). Real beats generated.
- **Face-cam notes:** framing room the on-screen plan needs (space at the top for a card, etc.).
- **What you'll capture yourself:** public pages, articles, docs.
- **Questions before filming:** every `[NEED]` in one list.

### 8. Hook check, then approval

For a Short, run the `roast-my-short` skill in hook-check mode on the shoot sheet (pass the creator's tracker so it scores against their real benchmarks) and fold its hook and length notes in. Then the creator approves or leaves notes. Then they film.

When footage arrives, the edit follows the plan, and **what the creator actually said on camera wins over the plan's wording.**

## Learn from every round

When the creator gives a note on a script that reflects a preference, not a one-off fix, save it (dated, one line, with why):

- **General lessons** (they'd help anyone's script) → [references/lessons.md](references/lessons.md). Write the why as a general reason; per-video stats, titles and view counts stay in the creator's private tracker.
- **One creator's taste** (their sign-off, humor level, banned words) → their voice profile in `no-ai-slop-writing`.

After a video publishes and its stats come in, ask what the plan got wrong (hook, length, a beat that lost people) and save the general lesson. The same note should never be needed twice.

## Guardrails

- Never invent results, numbers, quotes, reactions or personal details. Ask, or mark `[NEED: …]`.
- Never fabricate posts, tweets or screenshots for on-screen proof.
- Hyperbole is for jokes, feelings, comparisons and opinions (takes can be absolute). Numbers, quotes, dates and results, including the creator's own story, stay exact and sourced.
- Roast up (big tech, hype, benchmarks, the creator themselves), not the viewer and not private people. Blur private people's names.
- Not financial, medical or legal advice: if a video touches those, the plan says it's the creator's own experience.
