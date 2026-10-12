# Remember My Research

**Make each research session useful to the next one.**

Remember My Research is an agent skill for turning scattered sources into a durable Markdown knowledge base. It helps your agent find what you already know, incorporate new evidence, explain what changed, and keep uncertainty visible.

Use it for technology research, scientific literature, product discovery, policy analysis, or any recurring research project. No database, paid API, or particular AI provider is required.

## A real-world use case: keep company research current

Suppose you follow several companies and keep a page for each one. You have already read their reports, mapped their competitors, and written down the questions that matter. Instead of researching from scratch every week:

1. **Build the starting view:** capture public filings, earnings releases, product announcements, and other relevant sources. Each company gets one main page with the current interpretation, uncertainties, and evidence links.
2. **Check for developments:** use your agent's browsing tools to periodically scan selected companies and themes for earnings, contract announcements, product launches, and regulatory decisions. Prefer original filings and announcements over repeated headlines.
3. **Update only what changed:** a new release may show that a projected launch actually shipped, or that a reported deal is still only a pilot. Capture the evidence, revise the affected page, preserve the earlier view, and update related theme pages where justified.
4. **Reuse the accumulated knowledge:** ask “What changed since my last review, and does it resolve any open questions?” The answer starts with your existing research rather than a blank chat.

This is a realistic workflow, **not a claim about any particular company or current event**. The same pattern works for evaluating software tools (releases, pricing, security advisories), following scientific topics (new papers and replication results), or tracking public policy (proposals, amendments, and final decisions).

## What you get

- `SKILL.md`: instructions your agent follows.
- `templates/`: a schema, research-page template, and privacy/scope configuration.
- `examples/project-research/`: a complete fictional mini-wiki you can read or copy.
- `references/`: behavioral acceptance checks and public-release guidance.

**This is a workflow skill, not a standalone application.** It does not install collectors, run scheduled jobs, or include an automated initializer, index builder, linter, or exporter. Your agent needs filesystem tools; live source refreshes also need browsing/retrieval tools. The sample uses a manually maintained index.

## Quickstart

### 1. Install or load the skill

Follow the [repository installation instructions](../../README.md#install), or tell your agent to read this folder's `SKILL.md`. If your agent does not discover skills automatically, explicitly load that file at the start of a session.

### 2. Optional: try the small practice wiki

The included community-garden example is deliberately small and fictional: it demonstrates the difference between a claim and verified evidence without needing live sources. It is a practice exercise, not the main use case. You can skip it and create your own wiki in step 3.

From the repository root, copy the fictional wiki into a **new, empty destination**:

```sh
cp -R skills/remember-my-research/examples/project-research ~/my-research-wiki
```

Do not run this command against an existing directory: copying can merge content. The included documents are entirely synthetic, not actual project announcements.

Ask your agent:

> Use remember-my-research on ~/my-research-wiki. Read README.md and SCHEMA.md, then answer: is the Northstar community garden approved? Cite the evidence and explain the remaining uncertainty. Do not change files yet.

Expected answer: **No verified approval.** An early fictional announcement says the project is approved, but a later fictional status note says only the application was accepted for review. Treat the approval claim as unverified, preserve the discrepancy, and look for a formal permit decision. See [the walkthrough](examples/project-research/README.md).

### 3. Create your own wiki

> Use remember-my-research to initialize a new wiki at ~/my-policy-wiki about local transport policy. Use the supplied schema and scope templates. Keep sources immutable and everything private by default. Create the entry README, a manual index, a routing map, and a change log. Do not overwrite existing files or set up recurring jobs.

Choose your own path and domain. Nothing in the skill assumes a financial portfolio or a specific folder on the author's machine.

### 4. Add evidence

> Ingest this source into ~/my-policy-wiki: <source URL or local file>. Search for an existing subject page first. Capture the source where permitted, record retrieval and observation dates, update the canonical page, preserve contradictions, and report exactly what changed. Do not publish anything.

### 5. Reuse and maintain knowledge

> Answer from the wiki first: what do we know about this proposal, what is still uncertain, and what evidence would change the conclusion? Verify current facts externally if the existing evidence is too old for the question.

> Check the wiki for broken links, duplicate subject pages, missing provenance, and stale decisive evidence. Report issues before making broad changes. An unchanged check must not make old evidence look new.

## Periodically scan news and refresh existing pages

Yes: the wiki can be maintained through recurring news/source checks. **The skill defines the research workflow; your agent's scheduler and browsing tools run it.** Nothing is scheduled automatically by installing this package.

Start with a bounded, one-off run:

> Use remember-my-research on ~/my-company-wiki. Scan the companies already covered for material news since their last successful scan, with a small overlap to catch delayed stories. Prioritize official filings, earnings releases, company announcements, and regulator records. Check at most five pages and twenty candidate sources this run. Capture and deduplicate usable evidence, update existing pages only when it changes the facts, interpretation, or proof status, and preserve conflicting claims. Report material changes and coverage gaps. Do not add new companies, publish, trade, or create scheduled jobs.

Once the one-off run works, choose a cadence appropriate to the subject—for example, weekly for a software shortlist, or more frequent around earnings/product releases. Prefer specific event triggers over repeatedly scanning everything. Ask your agent to propose the schedule, timezone, source/budget limits, permitted local writes, and delivery destination **before enabling recurrence**.

- **New material evidence:** capture it, update the affected page and relevant links, and explain the delta.
- **Same evidence or repeated headline:** no new research conclusion or “fresh” evidence date. Keep a lightweight scan receipt, not another editorial summary.
- **Unavailable or incomplete sources:** report partial/blocked coverage; absence of retrieved news is not proof that nothing happened.
- **No material change:** stay quiet by default rather than send repetitive all-clear messages.

See [the refresh playbook](references/periodic-refresh.md) for checkpoints, failure handling, and a schedule-ready prompt. News commentary is a lead to investigate, not automatically proof.

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
