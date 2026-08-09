# Automation PR Proposal v1

**Status:** PROPOSED_INACTIVE · fixture-first · non-publisher

`AutomationPrProposal` is a pre-write declaration for automation that may eventually open a **draft** pull request from a trusted base. It does not itself create a branch, write repository bytes, open a pull request, approve review, merge, release, deploy, promote, or publish.

## Purpose

Pass 12 calls for PR-first automation that can propose change without direct publish or merge power. Before any write-capable workflow is admitted, KFM needs a deterministic object that binds the intended base/head, bounded changed paths, candidate digest, receipt reference, policy outcome, and terminal limits.

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
| validation | `tools/validators/governance/validate_automation_pr_proposal.py` |
| orchestration | future `.github/workflows/` implementation after this guard is proven |
| candidate bytes | `data/work/automation/` only |
| policy | `policy/` |
| merge/release/publication | separate repository and release authorities |

## Finite validator result

The validator emits JSON with `outcome` (`PASS`, `HOLD`, or `ERROR`), `write_eligible`, and stable `reason_codes`. A schema-valid object with `policy_outcome != PASS` remains a valid proposal record but is not write-eligible.

## Non-effects

A passing proposal does not prove GitHub token safety, branch protection, human review, evidence closure, source rights, release safety, or publication authority. A future write-capable workflow must consume this object from trusted-base code, validate it before mutation, use least-privilege permissions, create draft PRs only, and remain unable to merge or publish.

## Rollback

This is additive and fixture-only. Revert the change through a reviewed pull request; there is no data migration or external cleanup.
