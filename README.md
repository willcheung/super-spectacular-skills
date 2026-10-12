# Super Spectacular Skills

A collection of portable [Agent Skills](https://agentskills.io) for writing, video editing, retirement planning, and compounding research. Each skill is a folder with a `SKILL.md` that any compatible agent (Claude Code, Codex, and others) can load.

## Skills

| Skill | What it does |
|---|---|
| [no-ai-slop-writing](skills/no-ai-slop-writing/) | Blog posts, newsletters, and video scripts (Shorts and YouTube) that sound like you, not AI. Ships with Will's (Vibe Coding Dad) voice profile |
| [video-edit](skills/video-edit/) | Turn raw talking-head clips into an edited Short or YouTube video: story, jump cuts, color, zooms, captions, cards, render |
| [retirement-dashboard](skills/retirement-dashboard/) | See when you could retire, how much you would need from savings each month, and what might remain after college and retirement. Compare spending, taxes, inflation, and market downturns in an editable dashboard. All examples are fictional. |
| [compounding-wiki](skills/compounding-wiki/) | Turn sources into reusable, evidence-backed research memory. Preserve provenance, contradictions, and honest freshness. Includes a fictional worked example. |

## Install

Clone once, then link the skills you want into your agent's skills directory. The loops below assume the clone lives at `~/super-spectacular-skills`; change the path if you clone elsewhere. If a skill folder with the same name already exists there as a real directory (not a link), remove or rename it first, or `ln` will put the link inside it.

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

Linking (instead of copying) means `git pull` updates every installed skill, and lessons a skill learns are saved back into the repo.

## Add a skill

1. Create `skills/<name>/SKILL.md` with `name` and `description` frontmatter. The description decides when an agent uses the skill, so say what it does and when to reach for it.
2. Put long guidance in `skills/<name>/references/`, code in `scripts/`, files the skill outputs in `assets/` or `templates/`.
3. Add a short `README.md` for humans and an `agents/openai.yaml` for Codex's display name.
4. Add a row to the table above.

## License

[MIT](LICENSE)
