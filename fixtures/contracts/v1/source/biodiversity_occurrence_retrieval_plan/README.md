# Biodiversity occurrence retrieval-plan fixtures

**Status:** PROPOSED · synthetic · no-network · no source activation.

This fixture family exercises the closed `BiodiversityOccurrenceRetrievalPlanCandidate` profile for eBird EBD/SED and GBIF predicate/SQL retrieval planning.

- `valid/` contains four schema-valid, semantically valid process candidates.
- `invalid/invalid_*.json` contains thirteen schema-invalid canary records that also trigger exact reviewed semantic findings.
- `invalid/expected_findings_manifest.json` is the exact finding-code oracle used by the validator and tests.

No fixture contains real credentials, notification addresses, source bytes, occurrence records, observer identifiers, precise coordinates, sensitive species locations, or release authority. A valid fixture is process-memory only and remains `HOLD` for rights, sensitivity, review, release, and public use.
