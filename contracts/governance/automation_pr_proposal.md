# Automation PR Proposal v1

**Status:** PROPOSED_INACTIVE · fixture-first · non-publisher

`AutomationPrProposal` is a pre-write declaration for automation that may open a **draft** pull request from a trusted base only after additional live-ref and artifact binding checks pass. It does not itself create a branch, write repository bytes, open a pull request, approve review, merge, release, deploy, promote, or publish.

## Purpose

Pass 12 calls for PR-first automation that can propose change without direct publish or merge power. KFM therefore requires a deterministic object that binds the intended base/head, bounded changed paths, candidate digest, receipt reference, policy outcome, and terminal limits before any pull-request mutation is attempted.

The proposed draft-PR opener is deliberately narrower than a repository writer: it accepts an already-existing `automation/` branch, revalidates the proposal and live Git state from trusted default-branch code, and may create only a draft pull request. It cannot create or modify branches or repository contents.

## Required invariants

- exact profile: `kfm.automation.pr-proposal.v1`;
- `base_ref` is `main` and `base_sha` is a full lowercase commit SHA;
- `head_branch` begins with `automation/` and contains only safe branch characters;
- every changed path is below `data/work/automation/` and contains no traversal or hidden path segment;
- each changed path is represented in `artifacts` with a lowercase SHA-256 digest;
- `draft` is always `true`;
- `merge_allowed`, `release_allowed`, `deploy_allowed`, `promote_allowed`, and `publish_allowed` are always `false`;
- `policy_outcome` is one of `PASS`, `HOLD`, `DENY`, or `ERROR`;
- a proposal is `write_eligible` only when policy outcome is `PASS`, the path/digest bindings are complete, and all terminal limits remain false;
- `receipt_ref` is required but is not proof or approval.

## Authority split

| Concern | Owner |
|---|---|
| proposal meaning | `contracts/governance/automation_pr_proposal.md` |
| machine shape | `schemas/contracts/v1/governance/automation_pr_proposal.schema.json` |
| deterministic examples | `fixtures/contracts/v1/governance/automation_pr_proposal/` |
| structural proposal validation | `tools/validators/governance/validate_automation_pr_proposal.py` |
| live Git/ref/blob binding | `tools/validators/governance/validate_automation_pr_live_binding.py` — PROPOSED_INACTIVE until reviewed/merged |
| draft-PR orchestration | `.github/workflows/automation-draft-pr-opener.yml` — PROPOSED_INACTIVE; PR creation only, no branch/content writes |
| read-only opener conformance | `.github/workflows/automation-draft-pr-opener-test.yml` and `tests/validators/test_validate_automation_pr_live_binding.py` |
| operator guidance | `docs/runbooks/AUTOMATION_DRAFT_PR_OPENER.md` |
| candidate bytes | `data/work/automation/` only |
| policy | `policy/` |
| merge/release/publication | separate repository and release authorities |

The proposal remains the declaration boundary. The live-binding validator and opener add stricter operational admission checks; they do not become semantic, policy, evidence, review, release, or publication authorities.

## Finite validator result

The structural validator emits JSON with `outcome` (`PASS`, `HOLD`, or `ERROR`), `write_eligible`, and stable `reason_codes`. A schema-valid object with `policy_outcome != PASS` remains a valid proposal record but is not write-eligible.

For a write-eligible proposal, the proposed live-binding validator additionally requires the fetched `main` and head refs, complete diff path set, candidate blob modes, and exact SHA-256 values to match the declaration. Any mismatch fails closed before pull-request mutation.

## Draft-PR opener boundary

The proposed opener is triggered only from trusted default-branch workflow code and has a job-level permission surface of:

```yaml
permissions:
  contents: read
  pull-requests: write
```

It may open at most one draft pull request for an already-existing declared head/base pair after structural validation, live binding, and immediate remote-ref rechecks. It does not have repository-content write permission and therefore cannot create the candidate branch or candidate bytes.

Because pull-request creation does not accept an atomic expected-head-SHA precondition, the opener rechecks remote refs immediately before creation and verifies the created PR's base SHA, head SHA, and draft state immediately afterward. A detected post-create mismatch closes only the newly created draft PR fail-safe.

## Non-effects

A passing proposal or live-binding check does not prove GitHub token safety, branch protection, human review, evidence closure, source rights, receipt authenticity, release safety, or publication authority. A draft pull request created by the opener remains a review surface only.

Neither the proposal nor the opener may:

- create or modify candidate branches;
- execute candidate code;
- approve review or mark a pull request ready;
- merge or enable auto-merge;
- release, deploy, or promote lifecycle state;
- publish or authorize public use; or
- change repository settings, rulesets, environments, secrets, or permissions.

## Rollback

Before merge, close the implementation pull request and abandon its feature branch. After an authorized merge, revert the bounded opener packet through a reviewed pull request. If a live opener run detects a post-create binding mismatch, its fail-safe is to close only the draft pull request it just created; candidate-branch cleanup remains a separate authorized action.
