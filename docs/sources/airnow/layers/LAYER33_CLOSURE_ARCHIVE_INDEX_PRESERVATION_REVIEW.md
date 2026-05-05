# Layer 33 Closure Archive Index Preservation Review

Layer 33 performs local-only, candidate-only review intake over Layer 32 artifacts and manual review notes. It does not execute preservation, indexing, publication, or command actions.

## Inputs and outputs
- Inputs: Layer 32 JSON/JSONL/Markdown artifacts and manual review notes under `tests/fixtures/air_quality/airnow/layer33/input/...`.
- Outputs: resolved manifest, evidence inventory, assessment matrix, item satisfaction, acceptance candidates, blockers, validation results, readiness summary, rerun plan, policy attestation, caveat register, status board/report, and receipt.

## Boundary and denials
Layer 33 is local-file only. It does not download files, call web services, run ZIP-code web-service loops, execute commands, create database indexes/search/public catalogs, execute preservation actions, copy prior-layer artifacts, transfer/publish/release snapshots, delete files, use external storage, set chmod/chattr immutability flags, create legal holds, certify official archive status, execute final accession, provide legal advice, create GitHub issues/PRs, provide emergency alerts, or provide regulatory analysis.

AirNow caveats:
- AirNow data are preliminary and can change.
- Regulatory determinations must come from EPA AQS/AirData.
- AirNow web services must not be used for bulk ZIP-code loops.

## Models
Layer 33 emits models for intake, evidence inventory, assessment, item satisfaction, acceptance candidates, residual blockers, validation, readiness, rerun planning, policy attestation, caveats, and status board.

## CLI examples
`python tools/air_quality/airnow_layer33_closure_archive_index_preservation_review.py --manifest tests/fixtures/air_quality/airnow/layer33/manifests/closure_archive_index_preservation_review_valid_manifest.json --out-dir /tmp/l33 --created-at 2026-01-01T00:00:00Z`

## Tests
Run the Layer 33 pytest modules under `tests/air_quality/test_airnow_layer33_*.py`.

## NEEDS_VERIFICATION
Flag unresolved or missing evidence as NEEDS_VERIFICATION and require rerun with corrected local artifacts.

## Next layer proposal
Layer 34 should add offline closure-archive-index-preservation finalization planning and may consolidate Layer 33 acceptance candidates, blockers, and evidence into an internal ledger. Layer 34 must keep all non-execution and non-publication denials.
