<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/terminal-state-assessment
title: TerminalStateAssessment Contract
type: semantic-contract; repository-control incident assessment
version: v0.1.0
status: proposed; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Repository steward · Security steward · Release steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; repository-control; incident-evidence; non-authorizing
related:
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../schemas/contracts/v1/governance/terminal_state_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/terminal_state_assessment/cases.json
  - ../../tools/validators/governance/validate_terminal_state_assessment.py
[/KFM_META_BLOCK_V2] -->

# TerminalStateAssessment

`TerminalStateAssessment` is a deterministic, fixture-only repository-control record that compares an explicitly authorized pull-request terminal ceiling with observed host state. It records divergence; it does not grant permissions, change settings, convert a draft, close or merge a pull request, or normalize an unexpected transition.

## Source basis

The briefing-integration architecture names `TerminalStateDivergence` as incident evidence and calls for deterministic regression fixtures for known unexpected-merge patterns. It explicitly states that mergeability is not authorization and that a draft state is not approval.

## Semantics

- `DRAFT_PR` admits only `OPEN_DRAFT`.
- `READY_PR` admits `OPEN_DRAFT`, `OPEN_READY`, and `CLOSED_UNMERGED`; `MERGED` exceeds the ceiling.
- missing, expired, or unknown host evidence yields `HOLD`/`ABSTAIN` rather than guessed authorization.
- head identity, timeline order, merge-commit presence, deterministic identity, and result reduction fail closed.

A validator `PASS` proves only local fixture coherence inside the authorized ceiling. A `DENY` for divergence is incident classification, not a repository mutation or rollback execution.

## Finite outcomes

| Validator outcome | Meaning |
|---|---|
| `PASS` | Observed fixture state remains within the declared ceiling. |
| `ABSTAIN` | Authorization or host state is missing, expired, or unknown. |
| `DENY` | The host state exceeds the ceiling or an integrity invariant fails. |
| `ERROR` | Input cannot be read safely or the fixture explicitly records assessment error. |

## Directory Rules basis

Semantic meaning belongs in `contracts/governance/`; machine shape in `schemas/contracts/v1/governance/`; synthetic incident timelines in `fixtures/contracts/v1/governance/`; reusable validation in `tools/validators/governance/`; executable proof in `tests/validators/`; orchestration in `.github/workflows/`; and authoring accountability in `data/receipts/generated/`. No settings, permission, release, proof, or publication authority is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_terminal_state_assessment -v
python tools/validators/governance/validate_terminal_state_assessment.py --fixtures
```

## Rollback

Close the draft pull request or revert the additive packet. No branch protection, ruleset, pull-request state, release, deployment, or public artifact is changed by this profile.
