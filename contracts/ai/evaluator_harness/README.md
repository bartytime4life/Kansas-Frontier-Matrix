# AI Evaluator Harness Contract

Status: **PROPOSED** · execution posture: **fixture-only / no-network**.

This contract operationalizes model-output evaluation as a deterministic pre-review gate. It evaluates candidate artifacts; it does **not** promote, release, publish, approve, or convert model output into evidence.

## Required semantics

An evaluation record identifies the candidate, artifact family, evidence references, deterministic metric checks, policy outcome, and finite evaluator result.

- `PASS` requires `deterministic=true`, `network_access=false`, `policy_outcome=ALLOW`, at least one evidence reference, and every metric threshold to pass.
- `FAIL` records a deterministic metric failure. It remains a reviewable candidate outcome, never publication authority.
- `ERROR` records an explicit evaluator/tool failure and must not fall back to `PASS`.
- `HOLD` or `DENY` policy outcomes cannot produce `PASS`.
- Metrics are explicit `{name,value,threshold,comparison}` records; no hidden composite score is authoritative.

The evaluator intentionally stops before human review and before every KFM promotion gate.

## Pass 12 public-safe profiles

The optional `PUBLIC_SAFE_RASTER_V1` and `PUBLIC_SAFE_TEXT_V1` profiles derive declared metrics from bounded synthetic inputs and then require exact parity between the derived values and the evaluator record.

- Raster derivation computes comparable-cell coverage, RMSE, and maximum absolute error. Shape mismatch denies; insufficient coverage holds; threshold failure fails.
- Text derivation computes citation coverage, unsupported-claim count, sensitive-term hits, and character count. Missing citation registry holds; unsupported or overlong output fails; declared sensitive-term exposure denies.
- `profile_spec_hash` binds the profile, input, candidate reference, and evidence references through deterministic `spec_hash` computation.

Profiles do not fetch sources, open binary artifacts, call a model, resolve an `EvidenceBundle`, execute policy, or authenticate review. Their outputs remain evaluation evidence subordinate to evidence, policy, review, release, correction, and rollback state.

## Directory Rules basis

Per accepted ADR-0029 / Directory Rules v2, semantic meaning lives under `contracts/`, machine shape under `schemas/`, synthetic examples under `fixtures/`, enforcement under `tools/validators/`, tests under `tests/`, CI under `.github/workflows/`, and authoring accountability under `data/receipts/generated/`. No new responsibility root or parallel evaluator authority is introduced.

## Validation

```bash
python -m unittest tests.validators.test_validate_ai_evaluator_harness -v
python tools/validators/ai/validate_ai_evaluator_harness.py --fixtures
```

## Rollback

Revert the additive profile fields and fixture cases. No source, model, policy, release, route, or public state is mutated.
