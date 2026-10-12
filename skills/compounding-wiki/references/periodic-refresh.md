# Periodic news and source refresh

## Purpose
Keep existing research current without turning a wiki into a daily headline dump. Scan for developments that change an established fact, interpretation, uncertainty, or proof condition. This is an agent procedure; no executable scheduler or collector is bundled.

## Choose the coverage
Use existing canonical pages, explicit user exclusions, and open questions as the watchlist. For company research, look for filings, earnings releases, product launches, material contracts, and regulatory outcomes. For software evaluation, check official releases, pricing changes, deprecations, and security advisories. For scientific topics, look for primary papers, corrections, and replication evidence.

Resolve aliases and ambiguous names before attaching news to a subject. Cross-check secondary reporting against a primary source when available; label unverified reporting. Repeated syndication is not new corroboration. Do not send private wiki passages or sensitive watchlists to an external search/API without permission: use approved public subject names or a local source feed.

## Run a bounded one-off scan first
1. Read the wiki contract, canonical pages, relevant unresolved questions, and previous scan receipts. Respect privacy and source-redistribution rules.
2. Use the last successful subject/source checkpoint plus a configured overlap for delayed indexing. On the first run choose an explicit lookback. A late-discovered older source can still matter; record its real publication/observation date, not today's date.
3. Limit subjects, candidate sources, runtime, and paid usage. Reuse recent usable captures. State which feeds/searches were checked; no tool can prove exhaustive news coverage.
4. Capture lawful source bytes and metadata. Deduplicate by content and event identity without erasing distinct original documents. Retain previous captures and distinguish changed source versions from separate reports.
5. Compare against canonical knowledge. Update only material deltas; preserve contradictions and dated prior views. Update related themes only if supported. Missing proof remains missing; don't turn a product announcement into shipped revenue or a pilot into a confirmed contract.
6. Run existing checks or a documented manual check, read back affected pages, and verify configured consumers if any. Never invent maintenance tooling.
7. Save a lightweight receipt with attempted window, subjects/sources checked, evidence IDs/hashes, material deltas, coverage gaps, status, and last successful checkpoint. Keep private operational receipts outside public exports.

## Checkpoints and no-op behavior
Separate `last_attempted_at`, `last_successful_scan_at`, source observation/publication dates, and canonical evidence-as-of. A complete unchanged run may advance a successful scan checkpoint, but cannot make underlying evidence newer or create an editorial update. Advance checkpoints only for subjects/source families actually checked successfully. Retain previous checkpoints for partial or blocked coverage; retry with overlap rather than skip missing intervals.

Deduplicate retries and do not create new pages for an unchanged headline. Record no material change operationally; stay quiet by default. Persisted evidence may still need synthesis after an interrupted run—an existing raw capture alone is not completion proof.

## Enable recurrence only with approval
Propose and confirm:
- Exact wiki root and subject scope; coverage exclusions.
- Cadence or event triggers and explicit timezone. Prefer more frequent checks around meaningful events rather than blanket high-frequency polling.
- Page/source/runtime caps and paid-source budget (zero by default).
- Allowed local writes; no public publishing, trades, or unrelated automation changes.
- Delivery destination and material-change/coverage-failure notification policy.
- Existing job reuse, overlap/concurrency policy, and retry behavior.

Installing a skill is not scheduling authorization. Use the host agent's supported scheduler only after approval; if none exists, run manually. Do not claim a recurring monitor is active until its job configuration and an actual run are verified. This package contains no scheduler integration or background service.

## Schedule-ready prompt
Adapt placeholders and submit to your agent for review, not as executable configuration:

> Propose a weekly refresh for <wiki root> on <day/time/timezone>. Cover existing active pages only and prioritize primary sources relevant to their open questions. Check up to <page cap> pages and <source cap> candidate sources with <runtime limit>; paid-source budget is zero unless separately approved. Use the previous successful checkpoints with <overlap>, retaining failed coverage for retry. Capture/deduplicate evidence, update canonical pages only for material changes, preserve source clocks and contradictions, and validate/read back local changes. Keep private research out of external search payloads. Deliver only material deltas or actionable coverage failures to <destination>; no unchanged all-clears or external publishing. Show the proposed job and reuse any equivalent existing job. Do not enable it until I approve.

## Verification scenarios
- New decisive source: existing owner updated with traceable evidence; prior view retained.
- Duplicate/no material change: operational receipt only; no freshness reset or notification.
- Delayed source: overlapping window catches it with original source dates.
- Partial source outage: explicit coverage gap; failed checkpoint retained for retry.
- Interrupted synthesis: retained capture reconciled once, not falsely treated as a completed update.
- No scheduler available: honest manual workflow, not an invented running monitor.
