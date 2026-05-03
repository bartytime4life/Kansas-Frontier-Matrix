# Decision Log Governance Layer

This layer treats `decision_log` as an immutable audit artifact. It is not policy law, not a run log, and not standalone proof.

## What is validated

- JSON schema conformance (`schemas/governance/decision_log.schema.json`).
- Deterministic `spec_hash` over canonical JSON input fixture.
- Cross-link integrity between decision log and run receipt.
- Local fixture signature bundle presence (`fixtures://...`).
- Policy bundle hash integrity.
- Deterministic replay of the recorded decision.

## Replay and verification CLI

```bash
python tools/validators/governance/validate_decision_log.py \
  tests/fixtures/governance/decision_log/valid_allow.json \
  tests/fixtures/governance/run_receipts/valid_run_receipt_with_decision_log.json \
  tests/fixtures/governance/policy_bundles/promotion_bundle_v1.json \
  tests/fixtures/governance/policy_inputs/promotion_allow_input.json
```

```bash
python tools/validators/governance/replay_decision_log.py \
  tests/fixtures/governance/policy_bundles/promotion_bundle_v1.json \
  tests/fixtures/governance/policy_inputs/promotion_allow_input.json
```

## Promotion gate behavior

`policy/governance/decision_log_gate.rego` fails closed when:

- decision log is missing
- verification report is absent/failed

Promotion requires `decision_log_present=true` and `decision_log_verification_report.ok=true`.
