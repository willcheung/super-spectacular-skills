# Compounding Wiki Schema

## Domain
Set domain, audience, excluded subjects, and coverage policy before ingesting.

## Layout
- raw/: immutable evidence and versioned metadata.
- entities/, topics/, comparisons/, queries/: canonical knowledge.
- maps/: routing pages; derived/: rebuildable artifacts.
- config/: shared registries; _archive/: retired pages/redirects.
- README.md: agent entry; SCHEMA.md: contract; index.md: catalog; log.md: append-only material receipts.

## Page fields
Require title, type, created, updated, tags, sources, lifecycle, privacy.
Optional: reviewed_at, evidence_as_of, confidence, contested, supersedes, canonical_owner.
Types: entity, topic, comparison, query, map.
The authoritative allowed-tags registry is `config/content-scope.json` (`allowed_tags`); this schema summary must mirror it. Initial tags: entity, topic, comparison, evidence, hypothesis, contested.
Use ISO dates and timezone-aware known clocks. Add tags to the contract before using them. Automated tooling must read one authoritative taxonomy rather than hardcoding duplicates.

## Evidence fields
Require source_id, source_url (nullable), retrieved_at, published_on (nullable), published_at (nullable), sha256, hash_scope, capture_path, privacy, redistribution_rights, supersedes (nullable).
Hash exact capture bytes or explicitly identified body bytes; never conflate them. For original/binary captures keep metadata separately. Corrections create versions; raw history is immutable.

## Lifecycle and freshness
Lifecycle: active, awaiting-proof, reference, dormant, archived.
Define per-subject windows and event triggers. Separate observation/review times. Unchanged checks do not freshen evidence. Confidence measures support, not popularity.

## Links and updates
The inline syntax `[[path/to/page|Display]]` is a non-resolving documentation placeholder, not a navigation link. Use real links with unique root-relative paths and meaningful existing links. Maintain backlinks. Generated indexes name their producer and freshness check; without a builder label the index manually maintained. Never claim regeneration before implementing it.
Check scope/owners; capture evidence; reconcile; retain prior views; update navigation/log; validate. Newer is not automatically better. Keep one canonical current view per subject.

## Privacy and maintenance
Private by default. Public-candidate is not approval. Unknown/private/failed inputs fail closed at public handoffs. Research writes authorize no external action.
List real tested maintenance commands here once implemented; until then use manual acceptance checks. Compare validation against baseline. Archive with redirects and recovery copies; preserve raw provenance.

## Example domain and checks
Domain: fictional community-project research. All dates are fictional scenario dates.
Index is manually maintained. Required claims cite raw source paths. Both example entity/map types use the base fields above. No automated exporter or validators are configured.
