# Layer 23 Snapshot Preservation Audit

Layer 23 performs a **local-only internal audit** of Layer 20/21/22 artifacts and emits deterministic governance ledgers, matrices, summaries, and receipt outputs. It does not execute preservation, command, publication, transfer, deletion, legal hold, certification, accession, or external-storage actions.

## Inputs and outputs
- Inputs: Layer 20/21/22 manifests, receipts, policy/caveat/non-execution artifacts, acceptance/blocker evidence.
- Outputs: resolved manifest, inventories, ledgers, lineage graph, hash chain, matrices, summary, status board/report, receipt, optional packet.

## Security and boundary constraints
- No live ingestion, no downloads, no web-service calls, no ZIP-loop bulk polling.
- No command execution or preservation action execution.
- No copy/transfer/export/publish/release of snapshots.
- No deletion/destruction/chmod/chattr/legal-hold/certification/final accession.
- No legal advice, no GitHub issue/PR creation, no dashboard/UI/API/tiles/publication output.
- No emergency alerts or regulatory claims.

AirNow caveats: preliminary data, non-AQS regulatory source, and no bulk ZIP-code web-service loops.

## Models
Includes intake models (Layer 20/21/22), input inventory, receipt/decision/evidence ledgers, lineage graph, hash chain, policy ledger, caveat registry, non-execution ledger, completeness/consistency matrices, exception register, final summary, rerun plan, status board.

## CLI
`python tools/air_quality/airnow_layer23_snapshot_preservation_audit.py --manifest ... --out-dir ... --created-at 2026-01-01T00:00:00Z`

## Tests
Run `pytest tests/air_quality/test_airnow_layer23_*.py`.

## NEEDS_VERIFICATION
Use `SNAPSHOT_PRESERVATION_INTERNAL_AUDIT_NEEDS_MORE_INPUT` when blockers remain.

## Layer 24 proposal
Layer 24 should provide offline closure-readiness planning and governance-only candidate evaluation while keeping all non-execution/non-publication constraints.
