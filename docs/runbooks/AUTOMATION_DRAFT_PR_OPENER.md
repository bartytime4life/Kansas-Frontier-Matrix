# Automation Draft PR Opener

**Status:** PROPOSED_INACTIVE · trusted-base · draft-only · non-publisher

This runbook describes the bounded `automation-draft-pr-opener` workflow. The workflow is intentionally narrower than a repository writer: it cannot create or modify branches or repository contents. It can only inspect an already-existing `automation/` branch and, when every declared guard passes, open one draft pull request against `main`.

## Purpose

The opener closes the next Pass 12 prerequisite after `AutomationPrProposal`: convert a validated proposal plus an already-existing candidate branch into reviewable GitHub state without granting merge, release, deployment, promotion, publication, or repository-content write authority.

The workflow is triggered only by the `automation-pr-proposal-v1` `repository_dispatch` event. `repository_dispatch` uses the workflow definition from the repository default branch, so candidate branch workflow bytes are not the execution authority. Candidate refs and blobs are fetched as data and are never executed.

## Required proposal

The dispatch `client_payload` must be exactly one `kfm.automation.pr-proposal.v1` object. The existing proposal validator must return:

```text
outcome = PASS
write_eligible = true
```

The proposal therefore binds:

- `main` and its exact 40-character base SHA;
- one existing `automation/` head branch;
- one to eight candidate paths confined to `data/work/automation/`;
- exact SHA-256 digests for every candidate blob;
- a receipt reference;
- `policy_outcome = PASS`;
- `draft = true`; and
- merge, release, deploy, promote, and publish authority all set to `false`.

## Live binding gate

Before any pull-request mutation, `validate_automation_pr_live_binding.py` verifies the locally fetched refs and bytes.

It requires:

1. the current fetched `main` commit to equal the proposal `base_sha`;
2. the proposed head to remain based on that exact current base;
3. the complete live diff to equal the proposal `changed_paths` set;
4. every live change to be an add or modify operation;
5. every live path to remain below `data/work/automation/`;
6. every candidate to be a normal non-executable `100644` Git blob; and
7. every live blob SHA-256 digest to equal the proposal artifact binding.

Any base drift, head drift, undeclared path, deletion, rename/type-change effect, path escape, unreadable blob, unsafe mode, or digest mismatch denies the write.

## Mutation boundary

The privileged job has exactly:

```yaml
permissions:
  contents: read
  pull-requests: write
```

It does not have `contents: write`, Actions write, issue write, deployment write, package write, OIDC, secret, or administrative authority.

After the deterministic local binding passes, the workflow re-reads the remote `main` and head branch SHAs through the GitHub API immediately before mutation. If either moved, it fails closed.

The workflow then:

- checks whether an open pull request already exists for the declared head/base pair;
- opens at most one **draft** pull request when none exists;
- re-reads the created pull request;
- requires the PR head SHA, base SHA, and `draft=true` state to match the validated values; and
- closes the newly created pull request fail-safe if that post-create binding does not match.

The GitHub pull-request API does not provide an atomic expected-head-SHA precondition for creation, so the pre-create ref recheck plus post-create verification bounds, but does not mathematically eliminate, the final network race window. The fail-safe close is the rollback for detected drift.

## What the opener does not do

The opener does not:

- create an `automation/` branch;
- write or modify candidate bytes;
- run candidate code;
- resolve evidence or authenticate a receipt;
- evaluate policy beyond consuming the already-declared proposal outcome;
- approve review;
- mark a pull request ready;
- merge or enable auto-merge;
- create a release or deployment;
- promote lifecycle state;
- publish or expose candidate data; or
- change repository settings, branch protection, rulesets, secrets, environments, or permissions.

A successful run proves only that the declared branch/diff/blob state matched the proposal at the bounded checks and that a draft review surface was created or already existed.

## Validation

The separate `automation-draft-pr-opener-test` workflow is deliberately read-only. It runs deterministic temporary-Git-repository tests for live binding and statically checks that the privileged workflow retains its repository-dispatch-only trigger and narrow permission set.

The privileged workflow itself cannot be meaningfully exercised by a pull-request run because doing so would collapse trusted-base and untrusted-branch execution. Live PR creation remains a post-merge, explicit repository-dispatch operation.

## Directory Rules basis

- proposal meaning remains under `contracts/governance/`;
- machine shape remains under `schemas/contracts/v1/governance/`;
- reusable validation remains under `tools/validators/governance/`;
- deterministic proof remains under `tests/validators/`;
- GitHub orchestration remains under `.github/workflows/`; and
- this operator guidance remains under `docs/runbooks/`.

No new responsibility root or parallel policy, contract, schema, receipt, proof, release, or publication home is created.

## Rollback

Before merge, close the implementation pull request and abandon its feature branch. After an authorized merge, revert the opener workflow, test workflow, live-binding validator/tests, contract reference, and this runbook through a reviewed pull request.

If a live opener run detects post-create drift, the workflow closes only the draft PR it just created. It does not delete or rewrite the candidate branch. Any candidate-branch cleanup remains a separate authorized action.
