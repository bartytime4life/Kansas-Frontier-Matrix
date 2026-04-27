# Fauna Release Dry-Run Runbook

Purpose: rehearse fauna publication safely with synthetic or previously approved public-safe fixtures.

## Preconditions

- Validation suite passes for touched fauna surfaces.
- No unresolved high-severity geoprivacy risks.
- Release candidate includes evidence and policy references.

## Steps

1. Build candidate artifacts from fixture or approved input set.
2. Execute schema, policy, and publication validators.
3. Verify no restricted geometry appears in public payloads/artifacts.
4. Produce release manifest and attach validation evidence.
5. Stage publish to non-public target and verify API/UI behavior.
6. Approve or hold release with explicit decision record.

## Exit criteria

- `PASS`: candidate may proceed to governed publish.
- `HOLD`: missing evidence, unresolved rights, or policy drift.
- `DENY`: geoprivacy/safety violation detected.

