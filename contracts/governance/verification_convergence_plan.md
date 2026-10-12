<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/verification-convergence-plan
title: VerificationConvergencePlan Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — governance steward · research steward · validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; fixture-only; non-authoritative
related:
  - ./verification_backlog_item.md
  - ../../schemas/contracts/v1/governance/verification_convergence_plan.schema.json
  - ../../fixtures/contracts/v1/governance/verification_convergence_plan/
  - ../../tools/validators/governance/validate_verification_convergence_plan.py
  - ../../tests/validators/governance/test_verification_convergence_plan.py
tags: [kfm, governance, verification, research, convergence, prioritization]
[/KFM_META_BLOCK_V2] -->

# VerificationConvergencePlan Contract

`VerificationConvergencePlan` is a deterministic, fixture-only proposal for selecting at most two unresolved verification items for one bounded convergence review. It preserves priority, research mode, dependency, blocker, constraint, deferral, correction, and rollback posture without becoming a scheduler, source of evidence, governance decision, or repository authority.

## Status and boundary

| Field | Value |
|---|---|
| Profile | `kfm.governance.verification-convergence-plan.v1` |
| Execution | `FIXTURE_ONLY_NO_NETWORK` |
| Outcomes | `READY`, `HOLD`, `ERROR` |
| Capacity | one or two selected items |
| Authority | `NONE` |

`READY` means only that the proposed packet is internally coherent. It does not authorize research, assign an owner, accept an ADR, mutate the repository, activate a source, approve a release, or publish a result.

## Candidate semantics

Each candidate carries a stable `item_id`, `P0`–`P3` priority, one or more research modes (`EXT`, `REPO`, `DEC`, `STW`, `TST`), dependency IDs, blocker reason codes, a constraint state, and explicit selection or deferral reasons.

An item is selectable only when it is `OPEN` or `IN_PROGRESS`, has no blockers, has `CLEAR` or `RESTRICTED` constraints, and all dependencies are already satisfied or selected earlier in the same plan. Candidate order is deterministic: priority first, then stable ID.

## Invariants

- selected and deferred IDs are an exact, ordered partition of candidate IDs;
- selection never exceeds `capacity` or two items;
- selected items require at least one selection reason;
- every deferred item requires at least one deferral reason;
- an actionable higher-priority item cannot be skipped without an explicit reason;
- the plan digest and plan ID bind the complete record except their own fields;
- all authority, mutation, release, publication, and public-use flags remain false.

## Directory Rules basis

Semantic meaning belongs in `contracts/governance/`; machine shape in `schemas/contracts/v1/governance/`; synthetic examples in `fixtures/contracts/v1/governance/`; executable validation in `tools/validators/governance/`; enforceability in `tests/validators/governance/`; source adaptation in `docs/intake/exploratory/`; and AI authoring provenance in `data/receipts/generated/`. No new root, registry, lifecycle phase, policy home, release home, or proof home is introduced.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q tests/validators/governance/test_verification_convergence_plan.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_verification_convergence_plan.py \
  fixtures/contracts/v1/governance/verification_convergence_plan/valid/*.json
```

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the bounded feature commit. This inactive profile creates no source, data, issue, release, cache, deployment, or public state requiring operational cleanup.
