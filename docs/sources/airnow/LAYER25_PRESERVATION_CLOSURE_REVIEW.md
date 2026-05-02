# Layer 25 Preservation Closure Review

Layer 25 performs **local-only, internal manual preservation-closure review intake** and produces candidate-only review artifacts. It does not execute closure, preservation, publication, or command actions.

## Inputs / Outputs
- Inputs: Layer 24 receipt/readiness/candidate/governance/policy/caveat/non-execution artifacts plus manual review notes.
- Outputs: resolved manifest, evidence inventory, assessment matrix, item satisfaction, candidate/blocker JSONL, validation/readiness/rerun/policy/caveat/status/report, receipt, optional packet.

## Safety and Denied Capabilities
No downloads, no web services, no ZIP bulk loops, no command execution, no task/audit/governance closure, no preservation action/copy/transfer, no snapshot export/copy/transfer/publication/release, no deletion/destruction/chmod/chattr, no external storage/archive transfer/legal hold/final accession/official certification/legal advice, no GitHub issue/PR creation.

AirNow caveats:
- Data are preliminary and can change.
- Regulatory data must come from EPA AQS/AirData.
- AirNow web services are not for bulk ZIP loops.

## Models
Layer 24 intake, evidence inventory, review assessment, item satisfaction, acceptance candidate, residual blocker, validation result, readiness summary, rerun plan, policy attestation, caveat register, status board are emitted as deterministic local files.

## CLI
`python tools/air_quality/airnow_layer25_preservation_closure_review.py --manifest <manifest> --out-dir <out> --created-at 2026-01-01T00:00:00Z`

## Tests
Run `pytest tests/air_quality/test_airnow_layer25_*.py`

## NEEDS_VERIFICATION
Use blockers + DENY outcomes for missing/invalid evidence; rerun after local corrections.

## Next layer proposal
Layer 26 should add offline preservation-closure finalization planning and may consolidate candidates/blockers/review evidence into an internal ledger, while still forbidding execution/publication/API/dashboard/tiles/emergency/regulatory/legal/automation actions.
