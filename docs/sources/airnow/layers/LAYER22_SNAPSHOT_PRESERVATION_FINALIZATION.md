# Layer 22 Snapshot Preservation Finalization

Layer 22 finalizes an **internal-only** snapshot-preservation review package from Layer 21 inputs. It is local-only, deterministic, and non-executing.

## Boundaries and denials
- No downloads/web services/network calls.
- No ZIP-code bulk web-service loops.
- No command execution.
- No preservation action/copy/transfer execution.
- No transfer/publication/release.
- No deletion/destruction/chmod/chattr/legal hold/archive certification/final accession.
- No legal advice.
- No GitHub issue/PR creation.
- Not publication, dashboard, tiles, UI, or public API.
- Not emergency alerts or regulatory analysis.

## AirNow caveats
- AirNow data are preliminary and may change.
- Regulatory data must come from EPA AQS/AirData.
- AirNow services must not be used as bulk ZIP loops.

## Models
Resolved manifest, input inventory, finalization ledger, decision candidate, acceptance consolidation, blocker consolidation, non-execution attestation, policy continuity matrix, caveat continuity register, readiness summary, exception register, rerun plan, status board, receipt.

## CLI
```bash
python tools/air_quality/airnow_layer22_snapshot_preservation_finalization.py --manifest <manifest.json> --out-dir <dir> --created-at 2026-01-01T00:00:00Z
```

## Tests
Run the Layer 22 pytest modules under `tests/air_quality/test_airnow_layer22_*.py`.

## NEEDS_VERIFICATION
If intake is missing/unsafe/forbidden, receipt is DENY and rerun is required after corrected local artifacts.

## Next layer proposal
Layer 23 should add an offline final preservation audit ledger consolidating Layers 20–22; it must keep all non-execution and non-publication constraints.
