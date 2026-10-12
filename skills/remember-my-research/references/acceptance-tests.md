# Acceptance checks

Use a disposable wiki, fictional subjects, and explicitly synthetic evidence. These are behavioral specifications, not bundled automated tests.

1. Orientation: a fresh agent given only root/question retrieves canonical view and uncertainty.
2. Deduplication: identical ingest adds no duplicate source version or subject.
3. Drift: changed bytes retain both versions, distinct computed hashes, and supersession metadata.
4. Contradiction: source A says approval; B says application only. Preserve discrepancy and attribution rather than silently overwrite.
5. Freshness: reviewing unchanged old evidence never changes observation time to today.
6. Missing evidence: remove a decisive synthetic source; report the missing input and degraded status, never fabricate.
7. Navigation: new page appears in catalog; new links resolve. Where implemented, builder is deterministic and stale-index check catches omissions.
8. Ownership: two producers for one concept/output fail validation.
9. Privacy: private, unknown, and unapproved candidate pages never enter public projection.
10. Handoff: canonical change is verified independently in derived consumer output; lint alone is insufficient.
11. No-op: unchanged check creates no new editorial story, promotion, or external action.
12. Recovery: archived page retains recovery copy, redirect, and raw provenance.

Record executed results separately from pending cases. Package-structure checks do not prove workflow behaviors.
