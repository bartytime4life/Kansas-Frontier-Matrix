# Layer 31 Closure Archive Index Audit

Layer 31 performs a **local-only internal audit** over Layer 28/29/30 artifacts and emits deterministic ledgers, matrices, summaries, and a receipt.

## Boundary and Denials
This layer does not download files, call web services, run ZIP-code bulk loops, execute commands, create database indexes, create search services, create public catalogs, close tasks/audits/governance, execute preservation/copy/transfer, export/publish/release snapshots, delete/destroy files, set chmod/chattr flags, create legal holds, certify official archive status, execute final accession, provide legal advice, or create GitHub issues/PRs.

It is not publication, dashboard, tiles, UI, search API, public API, emergency alerts, or regulatory analysis.

AirNow caveats:
- AirNow data are preliminary and can change.
- Regulatory air quality must come from EPA AQS/AirData.
- AirNow web services are not permitted as bulk ZIP-code loops.

## Inputs/Outputs
Inputs: Layer 28/29/30 receipts and related indexes/ledgers/attestations. Outputs include resolved manifest, input inventory, receipt/decision/evidence ledgers, lineage graph, hash chain, policy/caveat/non-execution ledgers, completeness/consistency matrices, exception register, final summary, rerun plan, status board, report, and audit receipt.

## Intake models
- Layer 28 intake model: receipt + archive index artifacts.
- Layer 29 intake model: review receipt + acceptance/blocker evidence.
- Layer 30 intake model: finalization receipt + decision/policy/caveat continuity.

## Workflow outcomes
- `CLOSURE_ARCHIVE_INDEX_INTERNAL_AUDIT_COMPLETE`
- `CLOSURE_ARCHIVE_INDEX_INTERNAL_AUDIT_NEEDS_MORE_INPUT`
- Policy-denied outcome on any forbidden request.

## CLI
```bash
python tools/air_quality/airnow_layer31_closure_archive_index_audit.py --manifest tests/fixtures/air_quality/airnow/layer31/manifests/closure_archive_index_audit_valid_manifest.json --out-dir /tmp/airnow_layer31 --created-at 2026-01-01T00:00:00Z
```

## Tests
Run Layer 31 pytest modules under `tests/air_quality/test_airnow_layer31_*.py`.

## NEEDS_VERIFICATION
If intake is incomplete or blockers remain, Layer 31 records exceptions and emits rerun guidance with internal-only ceiling.

## Next layer proposal
Layer 32 should add offline closure archive index preservation planning for Layer 31 output hashes, while still denying all execution/publication/networking/governance-closure actions listed above.
