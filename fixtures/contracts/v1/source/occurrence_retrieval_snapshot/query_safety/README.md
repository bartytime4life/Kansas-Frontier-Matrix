# Occurrence retrieval query-safety fixtures

**Status:** PROPOSED · synthetic · no-network · companion validation only.

This fixture subprofile enforces an existing boundary of the canonical
`OccurrenceRetrievalSnapshotCandidate`: normalized query predicates must not
carry notification addresses, authorization material, credentials, or
secret-like values.

- `valid/` contains one canonical-profile-shaped candidate with reviewed,
  non-sensitive predicate values.
- `semantic_invalid/` contains schema-shaped candidates whose predicate values
  include a synthetic email address or secret marker.
- `semantic_invalid/expected_findings_manifest.json` records exact non-echoing
  finding-code polarity.

The companion validator does not define a new retrieval object, replace the
canonical occurrence-retrieval validator, activate eBird or GBIF, inspect real
credentials, resolve evidence, or authorize release or publication.
