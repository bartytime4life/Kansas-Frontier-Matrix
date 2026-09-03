<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/governance/repository-transition-control-source
title: Repository transition control-source binding
type: governance binding note
version: v1.0.0
status: proposed; branch-only; not workflow-active
owner: OWNER_TBD — governance steward and repository-control steward
created: 2026-09-03
updated: 2026-09-03
policy_label: repository-facing; governance; fail-closed; non-authoritative
truth_posture: CONFIRMED selected GitHub issue / PROPOSED branch implementation / UNKNOWN required-check enforcement
related:
  - ../../contracts/governance/repository_control_state.md
  - ../../tools/validators/repository_control/validate_control_source_availability.py
  - ../../tools/validators/repository_control/validate_transition_authorization.py
  - ../../tests/validators/test_repository_control_source.py
  - ../../.github/workflows/repository-control.yml
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5529114880
[/KFM_META_BLOCK_V2] -->

# Repository transition control-source binding

## Decision

Issue #4024 is the selected live comment source for exact
`KFM_REPOSITORY_TRANSITION_AUTHORIZATION_V1` records. The project-owner
selection is recorded in issue #4024 comment `5529114880`; this note projects
that decision and does not manufacture it.

Deleted issue #1675 is historical evidence only. It remains valid as a cited
past incident or fixture identity, but it is no longer a usable runtime lookup
target and must not be treated as live merely because older repository files or
receipts still name it.

This note binds one operational lookup identity. It does not replace the
`RepositoryControlState` semantic contract, create a second authorization
format, or make a workflow result authoritative.

## Live-source rules

- Keep issue #4024 available while a trusted-base workflow version references it.
- The issue body is descriptive and never authorizes a transition.
- Only an unedited owner-account comment containing one strict authorization
  marker can satisfy the existing transition validator.
- The record remains exact to repository, control issue, pull request, base
  SHA, head SHA, actor, finite decision, and expiry.
- Missing, unavailable, deleted, malformed, edited, stale, expired,
  future-dated, wrong-base, wrong-head, wrong-issue, and non-owner material
  fails closed.
- Retrieval errors are represented by a bounded local status object. Raw API
  response bodies and transport errors are not copied into reports.

## Trusted-base execution

The `pull_request_target` workflow fetches both standalone validators from the
exact pull-request base SHA and never checks out or executes pull-request head
code:

1. `validate_control_source_availability.py` confirms that comments for the
   designated issue were obtained and bound to the expected repository and
   issue number.
2. `validate_transition_authorization.py` evaluates the bounded comments only
   after the source-availability check passes.

The source validator emits `CONTROL_SOURCE_UNAVAILABLE` or another bounded
regression when the lookup cannot be trusted. This prevents deletion, outage,
or retrieval failure from skipping the substantive authorization
classification.

## Enforcement boundary

The exact check remains
`repository-control / authorize-ready-and-merge`. It is **advisory** until a
separately authorized GitHub ruleset or branch-protection change requires that
check with strict, up-to-date behavior.

Repairing the lookup prevents a silent 404-and-skip failure. It does not make a
post-transition workflow preventive, prove the initiating client, establish
independent review, or stop an owner-authenticated merge by itself. This note
does not authorize a ruleset, branch-protection, permission, bypass, repository
setting, release, deployment, promotion, publication, or source-state change.

## Migration boundary

The active workflow and this note may move to issue #4024 before historical
fixtures and receipts are rewritten. Historical records should retain the issue
identity they actually observed. Any authored instruction that still tells an
operator to post a new authorization to deleted issue #1675 is stale and needs
separate reconciliation; that documentation debt does not make historical
receipts false.

This branch stops at `VALIDATED_BRANCH_ONLY` under issue #4024. It does not
create a pull request or authorize ready, merge, Stage 1B, Stage 2, or a
repository-setting change.

## Rollback

Before integration, abandon the branch. After reviewed integration, rollback is
a focused forward change that restores a separately verified live successor
source and its tests. Never repoint the workflow to a missing issue or rewrite
historical evidence to make rollback appear retroactive.
