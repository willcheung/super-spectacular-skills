# No AI Slop Writing

A portable [Agent Skill](https://agentskills.io) for interviewing, drafting, developing, and editing blog posts, newsletters, and video scripts without flattening the writer's voice. It ships with the voice profile of its author, Will Cheung ([Vibe Coding Dad](https://blog.vibecodingdad.com)), and works for anyone else from their own material.

It catches the usual AI-writing habits: fake insights, tidy rhetorical formulas, corporate filler, repeated punchlines, and endings that try too hard to sound profound. When a real voice is present, it protects the facts, uncertainty, humor, and odd little details that make it recognizable.

## What it does

- Writes new copy from a brief, notes, source material, or task context
- Develops a ramble, voice transcript, or brain dump into a coherent piece
- Asks focused questions when an important blank requires the user's experience or opinion
- Uses a two-to-three-question shadow interview before substantial new long-form writing in Will's voice
- Expands supported ideas and keeps brainstormed possibilities clearly labeled
- Edits an existing draft without sanding away the writer's voice
- Protects supplied names, numbers, dates, results, and limitations
- Avoids inventing personal experiences, opinions, or endorsements
- Flags claims the supplied material does not support
- Writes video scripts for Shorts, Reels, TikTok, and long-form YouTube, with on-screen notes the `make-my-video-awesome` skill can use
- Shapes Substack-style build logs and takes: title, plain headings, pro tips, an honest verdict
- Works with essays, articles, newsletters, social posts, notes, emails, and similar copy

## Inputs

| Input | Required? | What it provides |
| --- | --- | --- |
| Ramble, transcript, or brain dump | No | Raw thoughts, unfinished connections, and natural voice |
| Draft | No | Existing meaning, structure, and voice to preserve |
| Brief or task | No | The goal, topic, or requested piece |
| Notes or sources | No | Facts and details the agent can safely use |
| Voice samples | No | Extra guidance on vocabulary, rhythm, humor, and point of view |

Provide at least one starting input: a ramble, draft, brief, notes, source material, or a clear task. The profile describes Will's recurring patterns from his public blog and video; it doesn't contain copies of his articles. Other users get the general workflow unless they explicitly ask for that profile.

## Install

This skill is part of [Super Spectacular Skills](../../README.md) and follows the open [Agent Skills specification](https://agentskills.io/specification). See the [repository README](../../README.md#install) to install it, or point an agent directly at `SKILL.md`.

## Use it

Create something from a brief:

```text
Use no-ai-slop-writing to write a short newsletter about why I stopped using daily productivity summaries. Keep it dry and conversational. I usually forgot the summaries within an hour.
```

Develop a rambling thought:

```text
Use no-ai-slop-writing to turn this ramble into an article. Fill in connections that are supported by what I said. If an important example, fact, or opinion is missing, ask me a few focused questions before drafting. Don't make it up.

[ramble or transcript]
```

Edit an existing draft:

```text
Use no-ai-slop-writing to edit this post. Preserve my uncertainty and don't invent stronger results.

[draft]
```

### A small before-and-after

The skill does not make writing more formal. It keeps the point and restores the kind of rhythm someone might use out loud.

> **Before:** The tool generated a daily summary. However, I forgot most of it almost immediately.
>
> **After:** The tool made me a daily summary. Great. But I forgot most of it like an hour later.

This example is also used in the bundled [conversational writing guide](references/conversational-guide.md); it demonstrates an editing choice, not a measured product result.

Write as Will (his voice profile):

```text
Use no-ai-slop-writing to develop this ramble in my voice. Preserve my small word choices and natural roughness. Ask me about any missing personal detail instead of inventing it.

[ramble]
```

Voice samples and source material are optional. If the ramble already contains enough information, the agent should proceed. If the missing material must come from the writer, it should ask instead of guessing.

### Interview-led long-form writing

For a substantial new essay, article, newsletter, or thought piece in Will's voice, the skill starts with one round of two or three probing questions. The questions combine Andrew Ross Sorkin-inspired analytical pressure-testing with David Marchese-inspired human curiosity. The skill uses those high-level interviewing qualities without imitating either person's prose or persona. It retrieves specific memories, decisions, tradeoffs, technical mechanisms, and opinions before writing the final piece, and does not produce the questions and final draft in the same response.

Will's profile includes tech leadership and founder-operator background, pragmatic “middle-aged dad energy,” and a perspective on vibe coding. It uses those details only when relevant and never invents a personal story or opinion. Finished writing with the profile avoids rhetorical or self-answered questions (a genuine hook or closing question is fine), named-company prestige signals, exact former titles, and assumptions about the reader's work or life situation.

For a piece equivalent to a 15–20 minute read or narration, the skill targets roughly 2,000–2,500 words unless another length is requested. A four-part shape—personal opening, industry insight, optional operator depth, and practical action—is available when it fits the material. It is not imposed on short posts, emails, ordinary edits, or topics that need a different structure.

Example:

```text
Use no-ai-slop-writing to help me write a long-form article in my voice about why learning to direct AI tools matters more than memorizing syntax for many practical projects. Interview me before drafting.
```

## Automatic use and persistent voice

Compatible agents may invoke the skill automatically when a request matches its description. The description names blog posts, newsletters, video scripts, rambles, and “write as me” to make that match more reliable. Because implicit skill selection is still an agent decision, use a persistent project or global instruction when the voice must always be applied.

For Will, use this instruction:

```text
Whenever I say I'm writing, drafting, or developing a post, article, newsletter, video script, or social copy, automatically use no-ai-slop-writing and load references/writer-voice-profile.md. For substantial new long-form writing, also load references/interview-led-writing.md and interview me before drafting. Treat the writer voice profile as mine unless I explicitly request another voice.
```

Put the instruction in the writing project's persistent instructions when it should apply only there. Put it in the agent's global user instructions when it should apply to every writing task. The skill remains portable: other users get the general workflow or can provide their own samples rather than inheriting the bundled profile.

## Compatibility

The core skill is vendor-neutral and has no scripts, external tools, or runtime dependencies. Any agent that supports the Agent Skills format can load `SKILL.md` and its reference files. Agents without native skill support can still follow `SKILL.md` as a prompt or instruction file.

The `agents/openai.yaml` file adds optional OpenAI interface metadata. It does not change the core workflow and other agents can ignore it.

## What's inside

- `SKILL.md` contains develop, edit, draft, script, and interview-led modes, plus the workflow, factual guardrails, and the no-AI-slop check.
- `references/conversational-guide.md` contains detailed voice guidance and examples.
- `references/writer-voice-profile.md` contains Will Cheung's voice profile: recurring language decisions from his blog and on-camera delivery, not copies of his articles.
- `references/blog-posts.md` contains the shape of a blog post or newsletter.
- `references/video-scripts.md` contains Short and long-form YouTube script formats.
- `references/interview-led-writing.md` contains the interview-first long-form workflow, background, voice constraints, and optional article architecture.
- `agents/openai.yaml` provides optional OpenAI display metadata.

## Contributing

Issues and pull requests are welcome. Keep changes focused on preserving a real person's voice instead of replacing it with a house style.

## License

MIT
