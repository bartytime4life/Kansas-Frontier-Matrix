<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/policy-decision-vocabulary
title: PolicyDecision Reason and Obligation Vocabulary
type: contract
version: v0.1
status: draft; PROPOSED_INACTIVE; fixture-only; non-evaluator; non-release
owners: OWNER_TBD — Policy steward · Contracts steward · Schema steward · Runtime steward · Release steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; policy; finite-outcomes; reason-codes; obligations; fail-closed
related:
  - ./policy_decision.md
  - ./policy_input_bundle.md
  - ../../policy/decision/README.md
  - ../../policy/decision/vocabulary.v1.json
  - ../../schemas/contracts/v1/policy/policy_decision_vocabulary.schema.json
  - ../../tools/validators/policy/validate_policy_decision_vocabulary.py
truth_posture: CONFIRMED attached-corpus implementation pressure and current repository gaps / PROPOSED inactive vocabulary and semantics / UNKNOWN accepted evaluator, runtime binding, release enforcement, and steward approval
[/KFM_META_BLOCK_V2] -->

# PolicyDecision reason and obligation vocabulary

> **Purpose.** Define one small, versioned, machine-checkable vocabulary for `PolicyDecision.reasons` and `PolicyDecision.obligations` without evaluating policy or granting authority.

## Status and boundary

This profile is **PROPOSED_INACTIVE**. The registry is fixture-first and reviewable. It does not:

- evaluate Rego or any policy bundle;
- emit or authenticate a `PolicyDecision`;
- create evidence, consent, rights clearance, review, promotion, release, or publication authority;
- replace `contracts/policy/policy_decision.md`;
- make a schema-valid decision correct.

The implementation follows the responsibility split adopted by KFM:

| Responsibility | Surface |
|---|---|
| Semantic meaning | `contracts/policy/policy_decision_vocabulary.md` |
| Machine shape | `schemas/contracts/v1/policy/policy_decision_vocabulary.schema.json` |
| Inactive reviewed candidate registry | `policy/decision/vocabulary.v1.json` |
| Synthetic fixtures | `fixtures/contracts/v1/policy/policy_decision_vocabulary/` |
| Deterministic validation | `tools/validators/policy/validate_policy_decision_vocabulary.py` |
| Focused CI | `.github/workflows/policy-decision-vocabulary.yml` |

## Evidence basis

The attached Pass 9, Pass 11, and Pass 12 dossiers repeatedly call for stable policy reasons, obligations, finite outcomes, fixture-backed gates, and a small real policy surface rather than free-text drift or a broad untested library. Current repository evidence also identifies reason and obligation registries as a missing decision-policy dependency.

These sources establish implementation pressure, not adoption. The registry remains inactive until a later accepted evaluator and consumer binding are reviewed.

## Vocabulary model

### Reason codes

Each reason code has:

- a stable uppercase `code`;
- exactly one canonical finite `outcome`: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- one or more schema-confirmed `policy_families`;
- a `public_safe` flag indicating whether the description may be shown without exposing restricted details;
- a bounded description.

A reason code explains a decision outcome. It does not contain raw evidence, precise sensitive values, credentials, or internal exception text.

### Obligation codes

Each obligation code has:

- a stable uppercase `code`;
- one or more `applicable_outcomes`;
- one or more policy families;
- a bounded description.

Version 1 deliberately allows obligations only on `ANSWER`. Negative outcomes may carry reasons, but a downstream system must not reinterpret an obligation as permission to bypass `ABSTAIN`, `DENY`, or `ERROR`.

## Deterministic rules

The validator enforces:

1. JSON Schema Draft 2020-12 shape.
2. Sorted and unique reason and obligation entries.
3. Sorted and unique policy-family arrays.
4. No code collision between reason and obligation namespaces.
5. Obligation applicability only to `ANSWER` in this first profile.
6. All governance authority flags remain `false`.
7. Deterministic, value-safe findings.

## Change discipline

Adding, renaming, or removing a code is a compatibility change. A future active profile must define:

- alias and deprecation handling;
- consumer compatibility;
- runtime normalization;
- bundle digest and evaluator identity;
- review authority;
- correction and rollback behavior.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_policy_decision_vocabulary.py' \
  --verbose

python tools/validators/policy/validate_policy_decision_vocabulary.py --registry

python -m pytest tests/schemas/test_common_contracts.py \
  -q -k policy_decision_vocabulary
```

## Rollback

Close the draft pull request or revert its single commit. No current evaluator, release, or public surface depends on this inactive profile.
