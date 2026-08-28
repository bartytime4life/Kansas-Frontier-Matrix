<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/policy-input-bundle-profile-v1
title: PolicyInputBundle Explicit Context Profile v1
type: contract-profile
version: v0.1
status: draft; PROPOSED_INACTIVE; fixture-only; non-evaluator
owners: OWNER_TBD — Policy steward · Contracts steward · Schema steward · Evidence steward · Source steward · Release steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; policy-input; explicit-context; fail-closed; no-hidden-fetch
related:
  - ./policy_input_bundle.md
  - ./policy_decision_vocabulary.md
  - ../../schemas/contracts/v1/policy/policy_input_bundle_profile_v1.schema.json
  - ../../policy/decision/vocabulary.v1.json
  - ../../tools/validators/policy/validate_policy_input_bundle_profile_v1.py
truth_posture: CONFIRMED parent contract and attached-corpus pressure / PROPOSED inactive profile and semantic checks / UNKNOWN accepted evaluator, consumer binding, runtime enforcement, and release authority
[/KFM_META_BLOCK_V2] -->

# PolicyInputBundle explicit context profile v1

> **Purpose.** Make one bounded subset of the existing `PolicyInputBundle` semantic contract machine-checkable for exposure and release-adjacent review, without evaluating policy.

## Relationship to the parent contract

`contracts/policy/policy_input_bundle.md` remains the semantic parent. This file is a profile, not a competing object family. It selects the minimum explicit context needed to test whether an input is coherent enough to reach a future policy evaluator.

The profile requires:

- one bounded operation and audience;
- subject identity, domain, and lifecycle phase;
- evidence resolution and citation-validation state;
- source descriptor references and source roles;
- rights and sensitivity posture;
- review and release context;
- evaluator identity with fail-closed mode;
- explicit false authority flags.

## Finite scope

Version 1 admits `ANSWER`, `RENDER`, `EXPORT`, `PROMOTE`, and `RELEASE`. It does not model intake, source activation, correction execution, or rollback execution.

## Semantic coherence rules

The dedicated validator enforces, in addition to JSON Schema:

1. reference arrays and source-role arrays are sorted and unique;
2. `ANSWER`, `RENDER`, and `EXPORT` require resolved evidence and passing citation validation;
3. public audience requires clear rights, public-safe sensitivity, safe precision, and approved or not-required review;
4. `PROMOTE` and `RELEASE` require approved review, candidate state, and a rollback reference;
5. `RELEASE` also requires a release-manifest reference;
6. unknown rights or sensitivity fail closed;
7. all authority flags remain false.

These checks establish input coherence only. They do not decide allow/deny outcomes and do not run a policy bundle.

## Directory Rules basis

The profile stays within existing responsibility roots: semantic meaning in `contracts/`, shape in `schemas/`, fixtures in `fixtures/`, validator in `tools/`, tests in `tests/`, and CI in `.github/workflows/`.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_policy_input_bundle_profile_v1.py' \
  --verbose

python tools/validators/policy/validate_policy_input_bundle_profile_v1.py \
  fixtures/contracts/v1/policy/policy_input_bundle_profile_v1/valid/valid_1.json

python -m pytest tests/schemas/test_common_contracts.py \
  -q -k policy_input_bundle_profile_v1
```

## Trust boundary

A passing input:

- is not a `PolicyDecision`;
- does not prove source authority, evidence truth, consent, rights, review, release, or publication;
- does not activate the inactive vocabulary from the parent PR;
- does not authorize a hidden fetch or lifecycle write.

## Rollback

Close the stacked draft PR or revert its single profile commit. The parent contract and existing placeholder schema remain unchanged.
