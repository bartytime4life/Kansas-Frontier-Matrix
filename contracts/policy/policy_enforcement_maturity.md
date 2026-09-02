<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/policy-enforcement-maturity
title: PolicyEnforcementMaturity Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — policy steward · repository-governance steward · runtime steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/policy/policy_enforcement_maturity.schema.json
  - ../../fixtures/contracts/v1/policy/policy_enforcement_maturity/cases.json
  - ../../tools/validators/policy/validate_policy_enforcement_maturity.py
  - ../../tests/validators/test_validate_policy_enforcement_maturity.py
tags: [kfm, policy, enforcement, maturity, ci, promotion, runtime]
[/KFM_META_BLOCK_V2] -->

# PolicyEnforcementMaturity Contract

`PolicyEnforcementMaturity` is a deterministic, fixture-only assessment of the evidence supporting one policy surface at one observed revision. It implements the Pass 11 maturity vocabulary without creating, amending, approving, activating, or enforcing policy.

## Status and boundary

| Field | Value |
|---|---|
| Profile | `kfm.policy.enforcement-maturity.v1` |
| Execution | `FIXTURE_ONLY_NO_NETWORK` |
| Validator outcomes | `PASS`, `DENY`, `ERROR` |
| Authority | `NONE` |

A `PASS` means only that the supplied evidence chain supports the declared stage locally. The assessment does not authenticate GitHub required-check configuration, PromotionGate execution, runtime behavior, reviewer authority, or release state.

## Ordered stages

1. `DESIGNED`
   - semantic contract or policy rule evidence exists;
   - evidence kind: `CONTRACT_OR_POLICY`.
2. `FIXTURE_TESTED`
   - deterministic positive and negative fixtures or tests exercise the rule;
   - evidence kind: `FIXTURE_OR_TEST`.
3. `MERGE_BLOCKING`
   - repository-required-check or ruleset evidence shows the check blocks merge;
   - evidence kind: `REQUIRED_CHECK`.
4. `PROMOTION_BLOCKING`
   - promotion-gate evidence shows the rule blocks a governed state transition;
   - evidence kind: `PROMOTION_GATE`.
5. `RUNTIME_ENFORCED`
   - runtime observation tied to the assessed revision shows enforcement at the governed service boundary;
   - evidence kind: `RUNTIME_OBSERVATION`.

Stages are cumulative. A record cannot claim a later stage without evidence for every preceding stage, and later-stage evidence cannot coexist with a deliberately lower maturity claim.

## Invariants

- assessments declare deterministic execution and no network access;
- the observed revision is a full 40-character commit SHA;
- evidence stages are unique, canonically ordered, and use the expected evidence kind;
- evidence references are nonempty, unique, and canonically ordered;
- a workflow file by itself does not prove `MERGE_BLOCKING`;
- a passing merge check does not prove `PROMOTION_BLOCKING` or `RUNTIME_ENFORCED`;
- `spec_hash` binds the complete assessment except the `spec_hash` field through the repository RFC 8785 JCS plus SHA-256 implementation;
- malformed shape or identity returns `ERROR`; maturity overclaim returns `DENY`.

## Directory Rules basis

Accepted ADR-0029 and Directory Rules v2 place policy semantics in `contracts/policy/`, machine shape in `schemas/contracts/v1/policy/`, synthetic examples in `fixtures/contracts/v1/policy/`, policy validation in `tools/validators/policy/`, enforceability in `tests/validators/policy/`, CI in `.github/workflows/`, source adaptation in `docs/intake/exploratory/`, and AI-authoring provenance in `data/receipts/generated/`. No new root or parallel policy, registry, release, proof, receipt, or publication home is introduced.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest \
  tests.validators.test_validate_policy_enforcement_maturity --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/policy/validate_policy_enforcement_maturity.py --fixtures
```

## Rollback

Before merge, close the draft pull request and abandon its feature branch. After an authorized merge, revert the additive commit. This inactive assessment creates no policy, repository setting, lifecycle, release, deployment, or public state requiring operational cleanup.
