# Layer 32 Closure Archive Index Preservation

Layer 32 creates local-only, deterministic planning artifacts from Layer 31 audit outputs. It does not execute preservation/index/publication actions.

## Inputs and outputs
- Inputs: Layer 31 audit artifacts listed in manifest `layer31_inputs`.
- Outputs: resolved manifest, inventory, scope/classification/fixity/layout/access/minimization/hold/risk plans, blockers, caveats, readiness, rerun, status, report, receipt, and optional packet.

## Safety and boundary
Layer 32 is planning-only and local-only. It does not download files, call web services, run ZIP web-service loops, execute commands, write databases, create search services, create public catalogs, copy prior-layer artifacts, transfer/publish/release snapshots, delete files, transfer to external storage, set immutable flags, create legal holds, certify official archive status, execute final accession, provide legal advice, create GitHub issues/PRs, provide emergency alerts, or provide regulatory analysis.

AirNow caveats:
- AirNow data are preliminary and subject to change.
- Regulatory data must come from EPA AQS/AirData.
- AirNow web services are not for bulk ZIP-code looping.

## Workflow outcomes
- PASS/ANSWER: internal plan complete.
- FAIL/DENY: blockers or denied capabilities detected.

## Models
Includes: Layer 31 intake, input inventory, scope plan, classification matrix, fixity plan, layout plan, access review plan, minimization review plan, hold candidate plan, risk register, blocker, non-execution attestation, policy continuity matrix, caveat register, readiness summary, rerun plan, status board.

## CLI
```bash
python tools/air_quality/airnow_layer32_closure_archive_index_preservation.py --manifest tests/fixtures/air_quality/airnow/layer32/manifests/closure_archive_index_preservation_valid_manifest.json --out-dir /tmp/airnow_layer32 --created-at 2026-01-01T00:00:00Z
```

## Tests
Run the `tests/air_quality/test_airnow_layer32_*.py` suite.

## NEEDS_VERIFICATION
Any manual preservation review evidence remains `NEEDS_VERIFICATION` until a future layer consumes offline reviewer artifacts.

## Next layer proposal
Layer 33 should add offline review intake and acceptance determination for manual internal preservation review, while still prohibiting execution/publishing/networking/automation actions.
