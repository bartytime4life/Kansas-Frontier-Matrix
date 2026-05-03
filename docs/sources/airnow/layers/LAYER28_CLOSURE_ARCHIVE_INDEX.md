# Layer 28 Closure Archive Index

Layer 28 creates a **local-only, internal planning index** from Layer 27 closure artifacts. It does not execute closure/preservation actions.

## Purpose
- Build deterministic inventories and planning indexes.
- Emit non-execution attestation and readiness/status artifacts.

## Boundaries
- No downloads, no web service calls, no ZIP loop usage.
- No command execution, database indexing, search-service creation, or public catalog publication.
- No task/audit/governance closure execution.
- No preservation action/copy/transfer execution.
- No snapshot export/copy/transfer/publication/release execution.
- No file deletion/destruction/chmod/chattr/legal hold/archive certification/final accession execution.
- No legal advice, no emergency alerts, no regulatory claims.

## AirNow caveats
- AirNow data are preliminary and subject to change.
- Regulatory data must come from EPA AQS/AirData.
- AirNow web services are not for bulk ZIP-code looping.

## Inputs/Outputs
Consumes Layer 27 receipt/ledger/hash/policy/caveat/lineage artifacts and produces:
manifest resolved, input inventory, scope/member/hash/receipt/decision/policy/caveat/lineage/access/search-key indexes, blockers, non-execution attestation, readiness summary, rerun plan, status board, report, and final receipt.

## Optional packet
If `index_policy.include_packet=true`, a deterministic `closure_archive_index_packet.tar.gz` is created with only Layer 28 generated outputs and receipt includes packet hash.

## CLI
```bash
python tools/air_quality/airnow_layer28_closure_archive_index.py --manifest <manifest.json> --out-dir <out> --created-at 2026-01-01T00:00:00Z
```

## Tests
Run pytest files under `tests/air_quality/test_airnow_layer28_*.py`.

## NEEDS_VERIFICATION
Any external-action request or prohibited capability must fail closed and appear in blockers/receipt errors.

## Next layer proposal
Layer 29 should add offline review intake for Layer 28 index plan acceptance while preserving all current non-execution constraints.
