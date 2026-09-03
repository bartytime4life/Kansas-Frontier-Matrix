<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/governance/repository-transition-control-source
title: Repository transition control-source binding
type: governance binding and enforcement-candidate note
version: v1.3.0
status: accepted; bootstrap-integrated; workflow-active; enforcement-pending
owner: OWNER_TBD — governance steward and repository-control steward
created: 2026-09-03
updated: 2026-09-03
policy_label: repository-facing; governance; fail-closed; non-authoritative
truth_posture: CONFIRMED selected GitHub issue, incident entry paths, skipped-check race, bootstrap integration at main@bd942b45493fa5f80e946ecfb3e810e413787394, exact check identity, current ruleset gap, and hosting non-effect / PROPOSED required-check packet and capability-separated canary
related:
  - ../../contracts/governance/repository_control_state.md
  - ../../tools/validators/repository_control/validate_control_source_availability.py
  - ../../tools/validators/repository_control/validate_transition_authorization.py
  - ../../tests/validators/test_repository_control_source.py
  - ../../tests/validators/test_repository_transition_authorization.py
  - ../../.github/workflows/repository-control.yml
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5529114880
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5530676972
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4234
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4235
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4237
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/bd942b45493fa5f80e946ecfb3e810e413787394
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/rules/15484585
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

## Bootstrap integration status

The five-file trusted-base repair was bootstrap-integrated by an explicit,
authorized squash merge of PR #4237 at `2026-09-03T18:56:08Z`.

The resulting authoritative revision is:

- main commit: `bd942b45493fa5f80e946ecfb3e810e413787394`;
- parent: `13e7114494ce5dfb5cb0495aef6127a1ee783a45`;
- tree: `73d31fda24c29185425ee87effe77c1125247b50`;
- exact bootstrap head: `50952c9d554ee366a22170d0ed86d09e7f5de77b`;
- recovery ref:
  `recovery/repository-control-bootstrap-pre-50952c9@13e7114494ce5dfb5cb0495aef6127a1ee783a45`.

The temporary read-only hosted-validation workflow is absent from the resulting
tree and main history. The integrated tree is the same permanent repair tree
validated by GitHub-hosted run `33790380138`, job `100765268087`.

The workflow is therefore active on the trusted default-branch base. It remains
advisory until ruleset `15484585` requires the exact
`authorize-ready-and-merge` check with strict currentness.

## Observed unauthorized entry paths

Two exact incidents show that repository control must cover both ways a
non-draft pull request can enter the mergeable lifecycle.

### Born ready — PR #4234

PR #4234 was created with `draft=false` at `2026-09-03T16:57:04Z` and merged at
`16:57:16Z`, twelve seconds later. There was no `ready_for_review` event because
the pull request entered the lifecycle already non-draft. The owner account is
the recorded merge actor and GitHub reports no performing GitHub App for that
merge event.

The advisory authorization job began after the merge, still used deleted issue
#1675, received HTTP 404, and never evaluated an exact transition record.

### Draft then ready — PR #4235

PR #4235 was created through a one-shot invocation with `draft=true` at
`2026-09-03T17:29:20Z`. GitHub later records `ready_for_review` at `17:44:37Z`
and merge at `17:44:41Z`, a four-second ready-to-merge interval. The owner
account is the recorded actor for both events and GitHub reports no performing
GitHub App for either event.

The advisory authorization job again began after merge and used the deleted
#1675 source from the trusted base. Terminating the draft-creation invocation
therefore established process separation but did not establish preventive
capability separation.

These records do not identify whether the later action came from a browser,
CLI, PAT, OAuth client, connector, or another owner-authenticated session. They
do prove that body warnings, draft creation, and asynchronous advisory checks
are not merge containment.

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

The workflow listens to `opened`, `ready_for_review`, and
`converted_to_draft`, among its bounded rerun events. Its authorization job
runs for both draft and non-draft pull requests:

- draft state returns
  `EXPECTED_READINESS_HOLD / PULL_REQUEST_IS_DRAFT / exit 3`;
- born-ready `opened` without a record returns
  `EXPECTED_READINESS_HOLD / TRANSITION_AUTHORIZATION_MISSING / exit 3`;
- later `ready_for_review` without a record returns the same missing-record
  hold.

The job must not use a draft-state `if` condition. GitHub reports a skipped job
as successful even when that job is required. Leaving a skipped-success result
on a draft head would create a race in which a later ready transition might be
merged before the replacement run registers its hold.

Running the job on the initial draft event leaves an explicit nonzero result on
that head. A later valid authorization and ready event must replace that result
with a fresh exact-head pass.

## Exact platform snapshot

Ruleset `15484585`, named `Protect`, was re-read active for the default branch
after the PR #4237 bootstrap on `2026-09-03`. Its registered rules are:

- deletion protection;
- non-fast-forward protection; and
- pull-request use with unresolved-thread resolution.

The pull-request rule currently requires zero approving reviews, does not
require code-owner review or last-push approval, and allows merge, squash, and
rebase. No bypass actor is registered. Most importantly, the ruleset contains
**no required-status-check rule**. A failing `authorize-ready-and-merge` result
or repository-topology result therefore does not presently block merge.

The exact GitHub Actions check-run name remains
`authorize-ready-and-merge`, and the observed GitHub Actions App identity
remains `15368`.

## Proposed server-side enforcement packet

The workflow repair is integrated. The smallest candidate addition to ruleset
`15484585` remains:

```json
{
  "type": "required_status_checks",
  "parameters": {
    "do_not_enforce_on_create": false,
    "required_status_checks": [
      {
        "context": "authorize-ready-and-merge",
        "integration_id": 15368
      }
    ],
    "strict_required_status_checks_policy": true
  }
}
```

The context is the observed GitHub Actions check-run name
`authorize-ready-and-merge`; `15368` is the observed GitHub Actions App ID. The
strict policy requires the pull-request head to be tested with the latest
protected-branch code before the check can satisfy the rule.

`do_not_enforce_on_create` concerns creation of a protected ref, not whether a
pull request is born draft or non-draft. It remains `false` to preserve normal
enforcement, but the born-ready guarantee comes from the required missing or
failing check context plus the always-running authorization job.

**This packet is proposed and not applied.** It is an exact settings candidate
for independent review and a separately authorized repository-settings
operation.

## Bootstrap and proof order

The dependency-bound bootstrap stages are complete:

1. The five-file trusted-base workflow repair is integrated on current main.
2. The integrated workflow, exact check-run name, and GitHub Actions App
   identity have been re-read.

The remaining order is:

3. Through a separately authorized repository-settings operation, add the
   reviewed required-status-check rule without weakening deletion,
   non-fast-forward, pull-request, or thread-resolution rules.
4. Re-read the complete ruleset and confirm the required check is active,
   strict, and bound to integration ID `15368`.
5. Create a draft canary and prove its first `opened` event produces
   `PULL_REQUEST_IS_DRAFT`, not a skipped-success check.
6. Prove a born-ready pull request with no record cannot merge while
   `TRANSITION_AUTHORIZATION_MISSING` is outstanding.
7. Prove a draft pull request changed to ready with no record cannot merge under
   the same hold.
8. Prove one exact, unedited, unexpired owner record for the current base and
   head allows only that transition check to pass.
9. Prove stale, edited, malformed, duplicate-key, wrong-base, wrong-head,
   wrong-issue, non-owner, expired, and unavailable-source cases remain blocked.
10. Push a new head and prove strict currentness invalidates the earlier result
    until a fresh exact-head record and rerun exist.
11. Confirm the platform rejected each negative merge attempt before merge;
    workflow failure after merge is not acceptance evidence.

The canary must use a capability-separated operator or account path whose sole
purpose is controlled test execution. Reusing the owner-authenticated path
implicated by PRs #4234, #4235, and #4236 would not prove separation.

A pre-enforcement canary may demonstrate workflow classification, but it cannot
prove server-side rejection. Because pull-request creation currently fans out
to more than one hundred checks, do not spend another canary run until the
required-check rule can be installed and read back or a narrower, separately
approved validation surface exists.

## Enforcement boundary

The exact check is commonly rendered as
`repository-control / authorize-ready-and-merge`, but the ruleset context
candidate is the check-run name `authorize-ready-and-merge`.

Repairing the lookup prevents a silent 404-and-skip failure. Requiring the check
would make its current outcome a server-side merge prerequisite. Neither action
proves the initiating client, creates independent review, or authorizes source
admission, proof construction, release, deployment, promotion, publication, or
sensitive-data handling.

This note does not authorize a ruleset, branch-protection, permission, bypass,
repository-setting, approval, ready, merge, release, deployment, promotion,
publication, or source-state change.

## Migration boundary

The workflow and this note now use issue #4024 while historical fixtures and
receipts may continue to retain the issue identity they actually observed. Any
authored instruction that still tells an operator to post a new authorization
to deleted issue #1675 is stale and needs separate reconciliation; that
documentation debt does not make historical receipts false.

The bootstrap integration is complete at
`main@bd942b45493fa5f80e946ecfb3e810e413787394`. Required-check enforcement,
capability-separated canaries, Stage 1B, and Stage 2 remain ungranted and
unproved.

## Rollback

The pre-bootstrap default-branch state is preserved at
`recovery/repository-control-bootstrap-pre-50952c9@13e7114494ce5dfb5cb0495aef6127a1ee783a45`.
No automatic rollback is authorized.

If the required-check rule is later installed, remove or replace that rule
through a separately authorized settings operation before reverting or
renaming its workflow, so the protected branch is not deadlocked. A reviewed
forward correction may instead bind a separately verified live successor
source and update the coupled tests.

Never repoint the workflow to a missing issue, weaken negative outcomes to make
a canary green, or rewrite historical evidence to make rollback appear
retroactive.
