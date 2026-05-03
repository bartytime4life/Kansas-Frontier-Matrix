# Layer 27 Preservation Closure Audit

Layer 27 generates internal-only audit ledgers from Layer 24/25/26 closure artifacts and never executes closure/preservation/publication actions.

## Boundary and caveats
- Local-only input processing.
- No downloads, no web services, no ZIP loop usage.
- No command execution, no task/audit/governance closure.
- No preservation execution/copy/transfer.
- No snapshot export/copy/transfer/publish/release.
- No deletion/destruction/chmod/chattr/legal hold/archive certification/final accession/legal advice.
- Not publication, not dashboard, not tiles, not UI, not public API.
- No emergency alerts and no regulatory analysis.
- AirNow data caveats: preliminary; regulatory data must come from EPA AQS/AirData; no bulk ZIP web-service loops.

## Inputs/outputs
Inputs: Layer 24, 25, 26 manifests/receipts/supporting ledgers from fixture manifest paths.
Outputs: resolved manifest, input inventory, receipt/decision/evidence ledgers, lineage graph, hash chain, policy/caveat/non-execution ledgers, completeness/consistency matrices, exception register, final summary, rerun plan, status board/report, receipt, optional deterministic packet.

## Models
Includes Layer24/25/26 intake model plus input inventory, receipt ledger, decision ledger, evidence ledger, lineage graph, hash chain, policy ledger, caveat registry, non-execution ledger, completeness matrix, consistency matrix, exception register, final summary, rerun plan, status board.

## CLI
`python tools/air_quality/airnow_layer27_preservation_closure_audit.py --manifest <manifest> --out-dir <dir> --created-at 2026-01-01T00:00:00Z`

## Tests
Run `pytest tests/air_quality/test_airnow_layer27_*.py`

## NEEDS_VERIFICATION
If required intake files are missing or forbidden capabilities are requested, receipt is denied and rerun is required with corrected manifest.

## Layer 28 proposal
Layer 28 should plan an offline closure archive index for Layer 27 outputs and deterministic hashes while keeping all non-execution constraints in force.
