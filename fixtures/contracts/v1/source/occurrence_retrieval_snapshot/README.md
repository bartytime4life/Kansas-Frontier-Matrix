# Occurrence retrieval snapshot fixtures

This folder contains synthetic, no-network examples for the proposed `OccurrenceRetrievalSnapshotCandidate` profile.

## Lanes

- `valid/` — three schema-valid and semantically valid snapshots: paired eBird EBD/SED success, GBIF async running, and GBIF async success.
- `semantic_invalid/` — schema-valid packets rejected by source-role, sampling-support, query, identity, or transfer semantics. `expected_findings_manifest.json` records the exact reviewed finding-code set.
- `schema_invalid/` — a packet that intentionally violates the closed governance shape. It is kept distinct from schema-valid semantic denials so repository-wide schema polarity remains non-vacuous.

## Important boundaries

- Fixture dates, thresholds, taxa, counties, digests, artifact references, and citation references are synthetic.
- eBird complete-checklist support is checklist-event non-detection, not county absence.
- GBIF transfer failure or an unfinished job is not a zero-record result.
- A successful zero-record result is `no_claim`, not absence.
- No fixture activates a source, contacts a network, resolves evidence, clears rights/sensitivity, releases, deploys, or publishes.

## Replay

```bash
python tools/validators/validate_occurrence_retrieval_snapshot.py --fixtures
python -m pytest -q -p no:cacheprovider tests/validators/test_validate_occurrence_retrieval_snapshot.py
```
