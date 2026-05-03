# Layer 20 Snapshot Preservation

Layer 20 produces local-only preservation planning artifacts from Layer 19 audit outputs. It does not download data, call web services, execute commands, execute preservation actions, copy prior-layer artifacts, publish/release/transfer snapshots, delete files, set chmod/chattr, create legal holds, certify archive status, perform final accession, give legal advice, create GitHub issues/PRs, or provide UI/API/dashboard/tiles/emergency/regulatory outputs.

AirNow caveats: data are preliminary; regulatory data must come from EPA AQS/AirData; AirNow web services are not for ZIP-loop bulk extraction.

## Inputs/Outputs
- Inputs: Layer 19 receipt, inventory, ledgers, hash chain, policy ledger, caveat registry, non-execution ledger, final summary.
- Outputs: resolved manifest, inventories/plans/matrices/registers, markdown status/report, receipt, optional deterministic packet.

## Models
Includes intake, inventory, scope, classification, fixity, layout, access review, minimization review, hold candidate, risk register, blocker, non-execution attestation, policy continuity, caveat register, readiness, rerun, status board.

## CLI
`python tools/air_quality/airnow_layer20_snapshot_preservation.py --manifest <path> --out-dir <dir> --created-at 2026-01-01T00:00:00Z`

## Tests
Run `pytest tests/air_quality/test_airnow_layer20_*.py`.

## NEEDS_VERIFICATION
Treat unresolved/manual evidence as NEEDS_MANUAL_REVIEW; no automated execution.

## Layer 21 proposal
Layer 21 should intake offline manual review evidence and decide whether Layer 20 planning is accepted for manual internal preservation review, while preserving all current non-execution/non-publication constraints.
