# AirNow Layer 7 Release Gate

Layer 7 is an **offline controlled-release gate simulation** for Layer 6 internal bundles.

- Internal review only.
- Not publication output.
- Not a public dashboard.
- Not a public API.
- Not a map tile product.
- Not an emergency alert product.
- Not regulatory analysis.
- AirNow data are preliminary and subject to change.
- Official regulatory air-quality data must come from EPA AQS/AirData.
- Layer 7 does not approve public release.

## Scope
Reads local Layer 6 artifacts, verifies governance/readiness checks, and emits deterministic decision + evidence + receipt outputs.

## Decision outcomes
- `ALLOW_INTERNAL_REVIEW_ONLY`
- `NEEDS_REMEDIATION`
- `DENY_PUBLICATION`
- `DENY_REQUESTED_CAPABILITY`
- `ABSTAIN_INSUFFICIENT_EVIDENCE`

Positive decision ceiling is `ALLOW_INTERNAL_REVIEW_ONLY`.

## Next layer
Layer 8 should add offline remediation-workflow scaffolding only.
