# Layer 29 Closure Archive Index Review

Layer 29 performs **local-only** closure archive index review intake. It validates Layer 28 artifacts and manual review evidence, then emits deterministic review outputs for internal candidate-only handling.

## Guardrails
Layer 29 does not download files, call web services, execute commands, create database indexes, create search services, create public catalogs, close tasks/audits/governance, execute preservation actions, copy prior-layer artifacts, transfer/publish/release snapshots, delete files, transfer to external storage, set chmod/chattr immutable flags, create legal holds, certify official archive status, execute final accession, provide legal advice, create GitHub issues/PRs, or provide emergency/regulatory outputs.

AirNow caveats include preliminary-data status, non-AQS regulatory status, and prohibition on bulk ZIP-code web-service loops.

## Inputs
- Layer 28 intake files listed in the manifest under `layer28_inputs`.
- Manual review evidence notes and attestation.

## Outputs
- Resolved manifest, evidence inventory (+jsonl), assessment matrix (+jsonl), item satisfaction (+jsonl), acceptance candidates, residual blockers, validation results (+jsonl), readiness summary, rerun plan, policy attestation, caveat register, status board (+md), report, receipt.
- Optional packet archive when `review_policy.include_packet=true`.

## Models
Includes: Layer 28 intake, evidence inventory, review assessment, item satisfaction, acceptance candidate, residual blocker, validation result, readiness summary, rerun plan, policy attestation, caveat register, status board.

## CLI
```bash
python tools/air_quality/airnow_layer29_closure_archive_index_review.py --manifest <manifest.json> --out-dir <out> --created-at 2026-01-01T00:00:00Z
```

## Tests
Run `pytest tests/air_quality/test_airnow_layer29_*.py`.

## NEEDS_VERIFICATION
Use blockers/validation outputs to mark unresolved manual evidence or denied content.

## Next Layer (30)
Layer 30 should add offline closure archive index finalization planning and may consolidate candidates/blockers/evidence into an internal ledger, while preserving all non-execution/no-publication/no-network guardrails.
