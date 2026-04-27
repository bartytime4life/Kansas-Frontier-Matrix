# Atmosphere / Air Runbook

Execution checklist for safe offline atmosphere-air work.

## Minimal flow

1. Verify branch and working tree.
2. Run lane-local docs checks (if configured).
3. Run schema/fixture validators (when implemented).
4. Run lane tests.
5. Record receipts and validation outcomes.

## Failure triage

- Schema failures -> quarantine candidate and fix fixtures/schema.
- Policy denials -> resolve rights/role/evidence issues.
- Evidence gaps -> attach missing refs before promotion attempts.
