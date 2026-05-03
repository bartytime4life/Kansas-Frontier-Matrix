# Layer 16 Snapshot Export Plan

Layer 16 generates a **local-only, planning-only** snapshot export package plan for AirNow artifacts. It does not execute export, transfer, publication, deletion, legal actions, or command execution.

## Inputs and outputs
- Inputs: Layer 15 artifacts listed in manifest `layer15_inputs`.
- Outputs: resolved manifest, inventory, scope/member/layout plans, access/redaction/fixity plans, preview, blockers, continuity/caveat/readiness/rerun/status, report, receipt, optional deterministic planning packet.

## Boundary and denials
Layer 16 does not download files, call web services, run ZIP loop extraction, execute commands, execute snapshot export, copy prior-layer artifacts into snapshots, transfer/publish/release snapshots, delete files, transfer to external storage, set chmod/chattr immutable flags, create legal holds, certify official archive status, execute final accession, provide legal advice, create GitHub issues/PRs, or provide dashboard/tiles/UI/public API/emergency alerts/regulatory analysis.

AirNow caveats are preserved:
- Preliminary and subject to change.
- Regulatory decisions must use EPA AQS/AirData.
- AirNow services are not for bulk ZIP-code loops.

## Models
Covers: input inventory, scope plan, member plan, layout plan, access classification, redaction review plan (planned only), fixity plan (sha256 planning), manifest preview (preview only), blockers, non-execution attestation, policy continuity matrix, caveat continuity register, readiness summary, rerun plan, status board.

## CLI
`python tools/air_quality/airnow_layer16_snapshot_export_plan.py --manifest <manifest.json> --out-dir <dir> --created-at 2026-01-01T00:00:00Z`

## Tests
Run the Layer 16 pytest modules under `tests/air_quality/test_airnow_layer16_*.py`.

## NEEDS_VERIFICATION
If manual review evidence is unavailable, mark `NEEDS_VERIFICATION` for human validation of acceptance and governance interpretation.

## Next layer
Layer 17 should intake offline manual review outcomes and decide internal acceptance for manual export review, while still denying command execution, export/copy/transfer/release, deletion, legal hold/certification, live ingestion/downloads/publication/APIs/alerts/regulatory/legal claims, GitHub issue/PR automation, and automatic patching/task closure.
