# Fictional project research wiki

Every subject, source, and event here is synthetic. Source hashes are calculated from the actual included fixture bytes; timestamps describe the fictional scenario, not actual collection.

## Start here
Read [SCHEMA.md](SCHEMA.md), [the routing map](maps/project-map.md), [index.md](index.md), and [log.md](log.md). Then read the [canonical project page](entities/northstar-garden.md) and its two raw sources. The [evidence manifest](raw/evidence.json) records capture identity and hashes.

## Worked example: a claim gets qualified
1. An early announcement says a community garden is “approved.” The agent retains the source but treats approval as an attributed claim without direct proof.
2. A later status note says the application was accepted for review, with no permit decision issued.
3. The agent preserves both sources, explains the discrepancy, and updates the single canonical page. It does not interpret application acceptance as approval or missing approval as rejection.
4. The next researcher can see the current view, why it changed, and what formal evidence would resolve it without replaying an earlier conversation.

Expected query answer: **No verified approval; awaiting a formal permit decision.** Cite both documents, retain uncertainty, and do not present fictional dates as today's facts.

## Practice prompts
> What changed between the two sources, and which evidence would settle the disagreement? Do not edit files.

> In a disposable copy, review both unchanged sources. Keep evidence-as-of at January 15; distinguish actual review time from fictional source times. Do not create a new approval conclusion or publish anything.

> Draft a fictional new permit decision, clearly labeled synthetic. Save it as a new source, compute its actual bytes hash, and update the canonical page. Preserve the earlier sources and view. Never pass the draft off as a real authority record.

No maintenance commands, exporters, collectors, or schedules are installed. The index is manual. The scope configuration defaults to private with public projection disabled; the checked-in synthetic fixture is intentionally public under MIT, but that does not grant publication rights to future user research.
