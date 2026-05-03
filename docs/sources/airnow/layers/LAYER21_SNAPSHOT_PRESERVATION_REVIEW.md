# Layer 21 Snapshot Preservation Review

Layer 21 performs local-only, internal snapshot-preservation review intake and produces candidate-only review artifacts. It does not execute commands or preservation actions.

## Inputs/Outputs
- Inputs: Layer 20 JSON/JSONL/MD artifacts plus local manual review notes.
- Outputs: manifest resolution, evidence inventory, assessment matrix, satisfaction matrix, candidates/blockers, validation/readiness/rerun/policy/caveats/status/report, receipt, and optional packet archive.

## Guardrails
Layer 21 is local-only and denies network/web-service use, ZIP loop usage, command execution, preservation execution/copy/transfer, snapshot export/copy/transfer/publication/release, deletion/destruction/chmod/chattr, legal hold creation, official archive certification, final accession, legal advice, GitHub issue/PR creation, task closure, and external storage/archive transfer.

It is not publication, not a dashboard, not tiles, not UI, and not a public API. It does not provide emergency alerts or regulatory analysis.

AirNow caveats:
- AirNow data are preliminary and subject to change.
- Regulatory data must come from EPA AQS/AirData.
- AirNow web services must not be used as bulk ZIP-code loops.

## Models
Includes Layer 20 intake, evidence inventory, review assessment, item satisfaction, acceptance candidate, residual blocker, validation result, readiness summary, rerun plan, policy attestation, caveat register, and status board models.

## CLI
`python tools/air_quality/airnow_layer21_snapshot_preservation_review.py --manifest <manifest.json> --out-dir <outdir> --created-at 2026-01-01T00:00:00Z`

## Tests
Run the Layer 21 pytest suite under `tests/air_quality/test_airnow_layer21_*.py`.

## NEEDS_VERIFICATION
If evidence is missing or policy checks fail, Layer 21 emits denied receipt outcomes for manual rerun/remediation.

## Next Layer
Layer 22 should add offline snapshot-preservation finalization planning and may consolidate Layer 21 candidates/blockers/evidence into an internal ledger while preserving all no-execution/no-publication/no-transfer constraints.
