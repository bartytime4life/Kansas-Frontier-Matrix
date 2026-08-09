# AI Evaluator Harness Contract

Status: **PROPOSED** · execution posture: **fixture-only / no-network**.

This contract operationalizes the Pass 9 evaluator-harness idea as a deterministic pre-review gate for model-produced candidate artifacts. It evaluates candidate artifacts; it does **not** promote, release, publish, approve, or convert model output into evidence.

## Required semantics

An evaluation record identifies the candidate, artifact family, evidence references, deterministic metric checks, policy outcome, and finite evaluator result.

- `PASS` requires `deterministic=true`, `network_access=false`, `policy_outcome=ALLOW`, at least one evidence reference, and every metric threshold to pass.
- `FAIL` records a deterministic metric or policy failure. It remains a reviewable candidate outcome, never publication authority.
- `ERROR` records an explicit evaluator/tool failure and must not fall back to PASS.
- `HOLD` or `DENY` policy outcomes cannot produce `PASS`.
- Metrics are explicit `{name,value,threshold,comparison}` records; no hidden composite score is authoritative.

The evaluator intentionally stops before human review and before any KFM promotion gate.

## Directory Rules basis

Per adopted ADR-0029 / Directory Rules v2, semantic meaning lives under `contracts/`, machine shape under `schemas/`, synthetic examples under `fixtures/`, enforcement under `tools/validators/`, tests under `tests/`, and CI under `.github/workflows/`. No new responsibility root is introduced.

## Validation

```bash
python -m unittest tests.validators.test_validate_ai_evaluator_harness -v
python tools/validators/ai/validate_ai_evaluator_harness.py --fixtures
```
