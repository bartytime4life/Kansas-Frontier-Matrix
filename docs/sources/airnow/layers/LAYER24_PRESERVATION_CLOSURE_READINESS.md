# AirNow Layer 24 Preservation Closure Readiness

Layer 24 is a **local-only, non-executing closure-readiness planning layer**. It reads Layer 23 artifacts, produces deterministic readiness/candidate/governance planning outputs, and never executes closure or preservation actions.

## Boundaries and denials
- No downloads, web services, ZIP loop usage, or live ingestion.
- No command execution, task closure, audit closure, or governance closure.
- No preservation execution/copy/transfer, snapshot export/copy/transfer/publication/release.
- No deletion, destruction, chmod/chattr, legal holds, archive certification, final accession, legal advice.
- No GitHub issue/PR creation, no git push.
- Not publication, dashboard, tiles, UI, or public API.
- No emergency alerts and no regulatory analysis.

## AirNow caveats
- AirNow data are preliminary and subject to change.
- Official regulatory data must come from EPA AQS/AirData.
- AirNow web services must not be used as bulk ZIP-code loops.

## Models and outputs
Resolved manifest, input inventory, readiness matrix, candidate ledger, unresolved issue register, governance gate, receipt verification, evidence summary, policy continuity, caveat continuity, non-execution attestation, decision candidate, rerun plan, status board/report, and receipt.

## Optional packet
If `closure_policy.include_packet=true`, Layer 24 creates deterministic `preservation_closure_packet.tar.gz` with only Layer 24 outputs and stores packet hash in receipt.

## CLI
```bash
python tools/air_quality/airnow_layer24_preservation_closure_readiness.py --manifest ... --out-dir ... --created-at 2026-01-01T00:00:00Z
```

## Tests
Run pytest files under `tests/air_quality/test_airnow_layer24_*.py`.

## NEEDS_VERIFICATION
Any unresolved blockers/exceptions should be tracked and rerun planned; no auto-remediation.

## Next layer proposal
Layer 25 should add offline manual closure-review intake and acceptance determination, while retaining all Layer 24 non-execution/non-publication/non-transfer constraints.
