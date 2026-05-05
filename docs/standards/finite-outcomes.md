# Finite Outcomes Standard

Shared finite outcome wave lives under `schemas/contracts/v1/shared/`:
- `runtime_response_envelope.schema.json`
- `policy_decision.schema.json`
- `promotion_decision.schema.json`
- `validation_report.schema.json`
- `rollback_reference.schema.json`

`evidence_bundle.schema.json` is reused as-is (no duplicate shared definition).

Allowed finite decision/outcome values:
- `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` for runtime outcomes.
- `ALLOW`, `ABSTAIN`, `DENY`, `ERROR` for policy/promotion/rollback decisions.
- `PASS`, `FAIL`, `ABSTAIN`, `ERROR` for validation report status.
