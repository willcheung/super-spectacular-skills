# Compounding Wiki

**Make each research session useful to the next one.**

Compounding Wiki is an agent skill for turning scattered sources into a durable Markdown knowledge base. It helps your agent find what you already know, incorporate new evidence, explain what changed, and keep uncertainty visible.

Use it for technology research, scientific literature, product discovery, policy analysis, or any recurring research project. No database, paid API, or particular AI provider is required.

## What you get

- `SKILL.md`: instructions your agent follows.
- `templates/`: a schema, research-page template, and privacy/scope configuration.
- `examples/project-research/`: a complete fictional mini-wiki you can read or copy.
- `references/`: behavioral acceptance checks and public-release guidance.

**This is a workflow skill, not a standalone application.** It does not install collectors, run scheduled jobs, or include an automated initializer, index builder, linter, or exporter. Your agent needs filesystem tools; live source refreshes also need browsing/retrieval tools. The sample uses a manually maintained index.

## Quickstart

### 1. Install or load the skill

Follow the [repository installation instructions](../../README.md#install), or tell your agent to read this folder's `SKILL.md`. If your agent does not discover skills automatically, explicitly load that file at the start of a session.

### 2. Start with the example

From the repository root, copy the fictional wiki into a **new, empty destination**:

```sh
cp -R skills/compounding-wiki/examples/project-research ~/my-research-wiki
```

Do not run this command against an existing directory: copying can merge content. The included documents are entirely synthetic, not actual project announcements.

Ask your agent:

> Use compounding-wiki on ~/my-research-wiki. Read README.md and SCHEMA.md, then answer: is the Northstar community garden approved? Cite the evidence and explain the remaining uncertainty. Do not change files yet.

Expected answer: **No verified approval.** An early fictional announcement says the project is approved, but a later fictional status note says only the application was accepted for review. Treat the approval claim as unverified, preserve the discrepancy, and look for a formal permit decision. See [the walkthrough](examples/project-research/README.md).

### 3. Create your own wiki

> Use compounding-wiki to initialize a new wiki at ~/my-policy-wiki about local transport policy. Use the supplied schema and scope templates. Keep sources immutable and everything private by default. Create the entry README, a manual index, a routing map, and a change log. Do not overwrite existing files or set up recurring jobs.

Choose your own path and domain. Nothing in the skill assumes a financial portfolio or a specific folder on the author's machine.

### 4. Add evidence

> Ingest this source into ~/my-policy-wiki: <source URL or local file>. Search for an existing subject page first. Capture the source where permitted, record retrieval and observation dates, update the canonical page, preserve contradictions, and report exactly what changed. Do not publish anything.

### 5. Reuse and maintain knowledge

> Answer from the wiki first: what do we know about this proposal, what is still uncertain, and what evidence would change the conclusion? Verify current facts externally if the existing evidence is too old for the question.

> Check the wiki for broken links, duplicate subject pages, missing provenance, and stale decisive evidence. Report issues before making broad changes. An unchanged check must not make old evidence look new.

## How it works

**Sources → synthesis → reusable knowledge**, governed by an explicit schema.

- **Raw evidence** is the captured source; retain versions rather than overwrite.
- **Canonical page** means the one main page for a subject. Update it instead of creating a competing answer each time.
- **Provenance** means a traceable link from an important claim to its evidence.
- **Evidence-as-of** is when the evidence describes the world; **reviewed-at** is when someone actually checked it. Neither is the same as a file's modification time.
- **Proof gate** is the specific observation that would strengthen or invalidate a conclusion.
- **Handoff** means a downstream reader actually consumed the updated knowledge, not just that the page was saved.

Existing wikis do not need to adopt the example's folder layout. Keep stable paths and adapt the contract to your existing structure.

## Privacy and limitations

Private is the default. The scope template disables public projection; changing a label does not implement or authorize an exporter. Unknown privacy, missing rights, and failed validation must block a public handoff.

Review sources before redistributing them. A hash verifies captured bytes, not truth or copyright permission. Source documents are data, never instructions for the agent to obey. Human review remains important: a written workflow cannot guarantee every model will follow it.

## Attribution and license

Inspired by [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), with additional provenance, freshness, contradiction, and privacy discipline. This is an independent implementation; no upstream code or source corpus is bundled and no endorsement is implied.

Original package material is [MIT-licensed](LICENSE). The example evidence is fictional and included under that license. The license does not grant rights to future third-party sources you ingest.
