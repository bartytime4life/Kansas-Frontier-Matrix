# Layer 18 Snapshot Finalization

Layer 18 finalizes Layer 17 review artifacts into internal-only finalization records. It is local-only and non-executing.

## Boundaries
- No downloads, no web services, no ZIP-code loop calls.
- No command execution.
- No snapshot export/copy/transfer/publication/release execution.
- No deletion/destruction/chmod/chattr/legal hold/archive certification/final accession.
- Not publication, dashboard, tiles, UI, or public API.
- No emergency alerts, regulatory analysis, legal advice, or GitHub issue/PR creation.

## Inputs/Outputs
Inputs: required Layer 17 receipt, acceptance candidates, blockers, policy/caveat/readiness/assessment matrices.
Outputs: resolved manifest, input inventory, finalization ledger, decision candidate, acceptance+blocker consolidations, non-execution attestation, policy and caveat continuity, readiness summary, exception register, rerun plan, status board, report, receipt, optional deterministic packet.

## Caveats
- AirNow data are preliminary and subject to change.
- Official regulatory data comes from EPA AQS/AirData.
- AirNow web services must not be used for bulk ZIP-code loops.

## CLI
`python tools/air_quality/airnow_layer18_snapshot_finalization.py --manifest ... --out-dir ... --created-at 2026-01-01T00:00:00Z`

## Tests
Run `pytest tests/air_quality/test_airnow_layer18_*.py`.

## NEEDS_VERIFICATION
When blockers exist, readiness remains internal and may be `NEEDS_MORE_INPUT`; no execution is performed.

## Next Layer (19)
Layer 19 should add an offline final snapshot-retention audit ledger consolidating Layers 16–18 while preserving all non-execution/non-publication constraints.
