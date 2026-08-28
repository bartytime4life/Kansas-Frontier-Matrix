# PolicyTransformPlanSimulation fixtures

This fixture family exercises the closed, fixture-only `PolicyTransformPlanSimulation` profile.

- `valid/valid_*.json` are schema-valid and semantically self-consistent simulation records.
- `SATISFIES` and `INSUFFICIENT` are both valid assessment outcomes.
- `invalid/invalid_*.json` are true JSON-Schema negatives.
- `invalid/semantic_invalid_*.json` remain schema-valid and fail only dedicated semantic validation.
- `expected_findings_manifest.json` binds every case to its exact validator outcome and stable finding-code set.
- Source snapshots reuse IDs, full-record hashes, and reduced results from landed `PolicyObligationReduction` fixtures, and bind the embedded result projection with its own RFC 8785/SHA-256 hash.

The fixtures are synthetic. They do not evaluate a policy bundle, apply a transform, expose geometry, mutate data, create release authority, or authorize public use.
