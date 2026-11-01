# Super Spectacular Skills

A collection of portable [Agent Skills](https://agentskills.io) for writing, video editing, retirement planning, and compounding research. Each skill is a folder with a `SKILL.md` that any compatible agent (Claude Code, Codex, and others) can load.

## Skills

| Skill | What it does |
|---|---|
| [video-director](skills/video-director/) | Choose viewer-first topics, route the existing production skills, prepare coherent upload packages, and learn from results |
| [no-ai-slop-writing](skills/no-ai-slop-writing/) | Blog posts, newsletters, and video scripts (Shorts and YouTube) that sound like you, not AI. Ships with Will's (Vibe Coding Dad) voice profile |
| [script-my-video](skills/script-my-video/) | Plan a Short or YouTube video before you film: interview, provocative-but-true hooks, sourced claims, a shoot sheet with bridge lines and punchlines, and the screens to capture |
| [make-my-video-awesome](skills/make-my-video-awesome/) | Turn raw talking-head clips into an edited Short or YouTube video: story, jump cuts, color, zooms, captions, cards, render |
| [roast-my-short](skills/roast-my-short/) | A blunt, independent review of a Short that predicts where viewers swipe away, from a reviewer that never saw the edit. Checks script hooks before filming and calibrates against your real stats |
| [when-can-i-retire](skills/when-can-i-retire/) | See when you could retire, how much you would need from savings each month, and what might remain after college and retirement. Compare spending, taxes, inflation, and market downturns in an editable dashboard. All examples are fictional. |
| [remember-my-research](skills/remember-my-research/) | Turn sources into reusable, evidence-backed research memory. Preserve provenance, contradictions, and honest freshness. Includes a fictional worked example. |
| [stock-thesis-to-ink](skills/stock-thesis-to-ink/) | Turn stock research into a readable, source-backed newsletter with a countercase and evidence appendix. |

## Install

Clone once, then link the skills you want into your agent's skills directory. The loops below assume the clone lives at `~/super-spectacular-skills`; change the path if you clone elsewhere. If a same-named real directory already exists, compare its contents, preserve unique changes and move it to a backup outside the skill-discovery directories before linking. Otherwise `ln` can put a link inside the old directory.

```sh
git clone https://github.com/willcheung/super-spectacular-skills.git ~/super-spectacular-skills
```

Claude Code:

```sh
mkdir -p ~/.claude/skills
for s in ~/super-spectacular-skills/skills/*/; do ln -sfn "${s%/}" ~/.claude/skills/"$(basename "$s")"; done
```

Codex:

```sh
mkdir -p ~/.agents/skills
for s in ~/super-spectacular-skills/skills/*/; do ln -sfn "${s%/}" ~/.agents/skills/"$(basename "$s")"; done
```

Linking (instead of copying) means both agents read the same files and lessons are saved back into the repo. Before replacing an existing real skill directory, compare it with the repository, preserve any unique changes, and move a recovery copy outside the agent's skill-discovery directories. Do not create nested links inside an existing directory. If Codex also has a copy under `~/.codex/skills`, reconcile that copy too so it cannot shadow the canonical skill. A running chat may need a fresh session to rediscover a new skill.

## Video workflow

Start with `video-director` when choosing the next step, packaging, or reviewing results. It uses `script-my-video` for planning, `make-my-video-awesome` for editing, and `roast-my-short` for independent Shorts review. These specialists remain directly usable. `no-ai-slop-writing` owns voice; each creator's project keeps its private tracker and research. All stages use the existing format and creator preferences rather than importing one pacing formula for every video.

## Add a skill

1. Create `skills/<name>/SKILL.md` with `name` and `description` frontmatter. The description decides when an agent uses the skill, so say what it does and when to reach for it.
2. Put long guidance in `skills/<name>/references/`, code in `scripts/`, files the skill outputs in `assets/` or `templates/`.
3. Add a short `README.md` for humans and an `agents/openai.yaml` for Codex's display name.
4. Add a row to the table above.

## License

[MIT](LICENSE)
