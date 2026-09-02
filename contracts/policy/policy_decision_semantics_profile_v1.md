<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/policy-decision-semantics-profile-v1
title: PolicyDecision Semantics Profile v1
type: contract-profile
version: v0.1
status: draft; PROPOSED_INACTIVE; fixture-only; non-evaluator
owners: OWNER_TBD — Policy steward · Contracts steward · Schema steward · Runtime steward · Release steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; policy-decision; reason-codes; obligations; finite-outcomes; non-evaluator
related:
  - ./policy_decision.md
  - ./policy_decision_vocabulary.md
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../policy/decision/vocabulary.v1.json
  - ../../tools/validators/policy/validate_policy_decision_semantics_v1.py
truth_posture: CONFIRMED existing PolicyDecision shape and attached-corpus implementation pressure / PROPOSED inactive semantic binding / UNKNOWN accepted evaluator, authenticated decision emission, runtime enforcement, and release authority
[/KFM_META_BLOCK_V2] -->

# PolicyDecision semantics profile v1

> **Purpose.** Validate that the existing `PolicyDecision` shape uses the inactive v1 reason and obligation vocabulary coherently, without creating the held canonical policy evaluator or authenticating any decision.

## Status and relationship

This profile is **PROPOSED_INACTIVE** and validator-only. It consumes:

- the existing `schemas/contracts/v1/policy/policy_decision.schema.json` shape;
- the inactive `policy/decision/vocabulary.v1.json` registry;
- synthetic `PolicyDecision` fixtures.

It deliberately does not create `tools/validators/validate_policy_decision.py`, because the existing policy readiness hold reserves that path for a later accepted evaluator-bound implementation.

## Semantic rules

The dedicated validator enforces:

1. `reasons` and `obligations` are sorted and unique.
2. Every reason and obligation code exists in the inactive registry.
3. Every reason's canonical outcome matches the decision outcome.
4. Every reason and obligation admits the decision's policy family.
5. `ABSTAIN`, `DENY`, and `ERROR` require at least one reason and allow no obligations.
6. `ANSWER` requires at least one reason.
7. `OPERATION_ALLOWED_WITH_OBLIGATIONS` requires at least one obligation.
8. Findings are deterministic and do not echo untrusted values.

## Trust boundary

A passing record proves only shape plus vocabulary coherence. It does not prove:

- that a policy bundle ran;
- that evaluator inputs were complete;
- that the decision is authentic, current, reviewed, or binding;
- that evidence, rights, consent, sensitivity, promotion, release, or publication gates passed.

The validator emits explicit false authority flags and performs no network access, hidden fetch, lifecycle write, policy evaluation, or public mutation.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_policy_decision_semantics_v1.py' \
  --verbose

python tools/validators/policy/validate_policy_decision_semantics_v1.py \
  fixtures/contracts/v1/policy/policy_decision_semantics_v1/valid_answer.json
```

## Rollback

Close the stacked draft PR or revert its single commit. The existing PolicyDecision schema and held canonical validator path remain unchanged.
