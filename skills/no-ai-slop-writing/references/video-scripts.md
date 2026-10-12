# Video scripts (Shorts, Reels, TikTok, YouTube)

Scripts are written to be *said*. Read every line out loud in your head; if it's something nobody would say to a friend, rewrite it. Voice comes from the speaker's own material; for Will, use the "How he talks on camera" section of writer-voice-profile.md.

A script here is a recording guide, not a teleprompter essay. Creators usually record in chunks and re-take lines, and the `make-my-video-awesome` skill picks the best takes afterwards, so short, separable lines make the edit better.

## Short (30–75 seconds)

| Beat | Time | Job |
|---|---|---|
| Hook | 0–3 s | A verdict, a number, or a genuine question the video then answers. No greeting, no "in this video". |
| Thesis | 3–8 s | The one idea, in one sentence ("Bigger, smarter models don't mean better results."), then a short signpost into the story (Will's: "Here's what I mean.") |
| Story / proof | 8–45 s | What the speaker tried, what they said to the AI, what happened, with the numbers. One concrete moment beats three vague ones. |
| Lessons | 45–65 s | Numbered lessons the speaker actually drew (often 2–3; fewer if that's all the source supports), each one sentence + one specific reason. |
| CTA | last 3–5 s | The creator's sign-off (Will's: "Follow along for more builds and more AI tips."). Lead straight into it; no "this is the kind of stuff…" warm-up. |

Rules:

- One idea per Short. If there are two, write two Shorts.
- Lines of 5–12 words. Each line should survive being cut on its own.
- Say numbers the way you'd say them: "three hours", "ten more hours", "a whole month of tokens in one weekend".
- Mark visuals for the editor in brackets on their own line: `[ON SCREEN: usage chart, highlight the spike]`, `[MEME: everyone's job is safe]`, `[CARD: Lesson 1]`. Only reference screenshots or data that exist or that the creator will capture.
- Sarcasm needs a beat: give the joke line its own line so the edit can land a meme on it.

Return format:

```text
TITLE (for the upload): …
HOOK
<line>
<line>
[ON SCREEN: …]
THESIS
…
STORY
…
LESSONS
…
CTA
…
```

Then: estimated length at ~150 spoken words per minute, the visuals the creator needs to capture, and any line that depends on a fact they haven't confirmed.

## Long-form YouTube (8–20 minutes)

1. **Cold open** (0–30 s): the most interesting moment or result, before any intro.
2. **Intro** (≤20 s): who the creator is in one line, what this video will show, why it's worth the time.
3. **Chapters**: each with a plain title (it becomes a YouTube chapter and an on-screen chapter card), a setup line, the demo/story, and a takeaway line.
4. **Recap** of decisions or tips, only if the video is long enough that viewers need it.
5. **End screen** (last 20 s): what to watch next + follow.

Write long-form as segments the creator can record separately. For screen-recorded demos, script the talking points and the clicks, not every word. Mark B-roll and screenshots in brackets. Include the chapter list with rough timestamps for the description.

## Shared rules

- Never invent results, numbers, quotes, or reactions. If the story needs one the creator hasn't given, ask or mark `[NEED: …]`.
- Don't fabricate posts, tweets, or quotes for on-screen proof. Mark `[NEED: screenshot of …]`.
- Keep the no-AI-slop check: no "In today's video", "Let's dive in", "game changer", "unlock", fake suspense, or recap endings.
