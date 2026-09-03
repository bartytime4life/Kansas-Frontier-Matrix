<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/governance/repository-transition-control-source
title: Repository transition control-source binding
type: governance binding and enforcement-candidate note
version: v1.3.2
status: current-main workflow-active advisory; bounded capture and truncated-response hardening integrated; required-status-check not installed
owner: OWNER_TBD — governance steward and repository-control steward
created: 2026-09-03
updated: 2026-09-03
policy_label: repository-facing; governance; fail-closed; non-authoritative
truth_posture: CONFIRMED current-main issue-#4024 binding, three-helper bounded capture, and truncated-response handling / PROPOSED required-check packet
related:
  - ../../contracts/governance/repository_control_state.md
  - ../../tools/validators/repository_control/fetch_bounded_issue_comments.py
  - ../../tools/validators/repository_control/validate_control_source_availability.py
  - ../../tools/validators/repository_control/validate_transition_authorization.py
  - ../../tests/validators/test_repository_control_input_bounds.py
  - ../../tests/validators/test_repository_control_strict_input.py
  - ../../tests/validators/test_repository_control_source.py
  - ../../tests/validators/test_repository_transition_authorization.py
  - ../../.github/workflows/repository-control.yml
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5532519315
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4234
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4235
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4237
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4238
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4239
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/rules/15484585
[/KFM_META_BLOCK_V2] -->

# Repository transition control-source binding

## Decision

Issue #4024 is the selected live comment source for exact
`KFM_REPOSITORY_TRANSITION_AUTHORIZATION_V1` records. The issue body is
descriptive and never authorizes a transition.

Deleted issue #1675 is historical evidence only. It remains valid when cited by
a past receipt or test fixture, but it is not a live runtime lookup target.
Issue #4024 replaces that operational lookup without rewriting history.

This note binds one control-source identity and its capture boundary. It does
not replace the `RepositoryControlState` semantic contract, create a second
authorization format, or make a workflow result sovereign authority.

## Current implementation state

PR #4237 integrated the live issue-#4024 source binding and non-skipped
draft/readiness classification into protected
`main@bd942b45493fa5f80e946ecfb3e810e413787394` on 2026-09-03.

PR #4239 then integrated strict page-wise source capture as
`main@7d9eda78f7da0aee0a2396d31780aaafb5694c7b`. PR #4238 added finite
truncated-`Content-Length` handling and its direct regression as current
`main@7c5d4125c277536258be6345e366efae59dbe5d6`, tree
`0a9aaac391d9c8a101234fc9cee8facbe1c4e5c6`.

The current protected-main workflow uses three trusted-base helpers:

1. `fetch_bounded_issue_comments.py` captures the source page by page under
   strict transport, parser, structure, pagination, completeness, and
   serialization ceilings.
2. `validate_control_source_availability.py` requires the exact four-field
   `AVAILABLE` status for the expected repository and issue.
3. `validate_transition_authorization.py` evaluates only the captured bounded
   comments against the exact pull request, base, head, actor, decision, and
   expiry.

All three helpers are fetched from the exact pull-request base SHA. The
workflow never checks out or executes pull-request-head code and has read-only
`contents`, `issues`, and `pull-requests` permissions.

The control is workflow-active but remains advisory at the platform boundary.
Ruleset `15484585`, named `Protect`, still has no `required_status_checks` rule.
A passing or failing `authorize-ready-and-merge` result is therefore not
presently a server-side merge prerequisite.

## Incident entry paths

### Born ready — PR #4234

PR #4234 was created with `draft=false` at `2026-09-03T16:57:04Z` and merged
twelve seconds later. There was no `ready_for_review` event because it entered
the lifecycle non-draft. The owner account is the recorded merge actor and the
merge event has no performing GitHub App.

### Draft then ready — PR #4235

PR #4235 was created as a draft at `2026-09-03T17:29:20Z`, marked ready at
`17:44:37Z`, and merged at `17:44:41Z`. The owner account is the recorded actor
for both transitions and neither event names a performing GitHub App.

### Bounded-capture integration — PR #4239

PR #4239 was created with an explicit draft-only/no-merge boundary, marked ready
at `2026-09-03T21:22:33Z`, and merged three seconds later. The owner account is
the recorded actor for both transitions and neither event names a performing
GitHub App. The repository-control run correctly classified the exact head as
`TRANSITION_AUTHORIZATION_MISSING`, but the run began after the merge.

### Truncated-response correction — PR #4238

PR #4238 was restored to draft after one unauthorized ready event, then marked
ready again at `2026-09-03T21:29:33Z` and merged four seconds later. The owner
account is the recorded actor for both final transitions and neither event names
a performing GitHub App. The repository-control run captured the live source
and correctly classified the exact head as
`TRANSITION_AUTHORIZATION_MISSING`, but it was created one second after merge.

These incidents do not identify whether the initiating path was a browser, CLI,
PAT, OAuth client, connector, or another owner-authenticated session. They do
prove that body warnings, draft creation, and asynchronous advisory checks are
not preventive merge containment.

## Live-source rules

- Keep issue #4024 available while trusted-base workflow code references it.
- Only an undited owner-account comment containing one strict authorization
  marker can satisfy the transition validator.
- Each record is exact to repository, control issue, pull request, base SHA,
  head SHA, actor, decision, and expiry.
- Missing, unavailable, malformed, edited, stale, expired, future-dated,
  wrong-base, wrong-head, wrong-issue, duplicate-key, non-owner, truncated, or
  over-limit material fails closed.
- Raw response bodies, comments, numeric tokens, and transport exceptions are
  not copied into bounded decision output.

## Current bounded source capture

The capture helper requests at most 100 records per page and admits at most
100 pages. A bounded sentinel page is used when page 100 is full so the source
is never silently truncated.

The fixed limits are:

- 8 MiB of transferred input per page;
- 16 MiB of aggregate transferred and reserialized input;
- 10,000 admitted comment records;
- JSON depth of 32;
- 100,000 JSON nodes per page;
- 1,000,000 JSON nodes across the capture;
- 128 digits in an integer token; and
- 128 characters in a floating-point token.

Each response read receives only the remaining byte allowance plus one overflow
probe byte. A declared `Content-Length`, when present and valid, must equal the
actual bounded body length; premature end-of-body is a finite fetch failure.

The helper rejects non-standard `NaN`, `Infinity`, and `-Infinity`, rejects
non-finite parsed floats and overlong integer tokens, rejects duplicate object
keys, and normalizes parser `ValueError`, `OverflowError`, and `RecursionError`
into a finite invalid-page result. Output serialization uses
`allow_nan=false`.

Any fetch, token, page, byte, node, depth, UTF-8, JSON, shape, completeness, or
serialization failure produces only:

1. an empty comments array; and
2. the four-field source status with `status=UNAVAILABLE`.

The helper returns control to the trusted-base availability validator, which
emits the nonzero blocking classification.

## Pull-request lifecycle behavior

The current workflow listens to `opened`, `reopened`, `synchronized`,
`ready_for_review`, `converted_to_draft`, `edited`, `labeled`, and `unlabeled`.

The authorization job runs for draft and non-draft pull requests:

- draft state returns
  `EXPECTED_READINESS_HOLD / PULL_REQUEST_IS_DRAFT / exit 3`;
- born-ready `opened` without a record returns
  `EXPECTED_READINESS_HOLD / TRANSITION_AUTHORIZATION_MISSING / exit 3`;
- later `ready_for_review` without a record returns the same missing-record
  hold.

The job must not use a draft-state `if` predicate. GitHub treats a skipped job
as successful for required-check evaluation. Leaving a skipped-success result
on a draft head would reopen the ready-to-merge race.

A successful transition record is still bounded to the exact tested base and
head. It is not independent review, initiating-client attribution, source
admission, release authority, or publication authority.

## Exact platform snapshot

Ruleset `15484585` is active for the default branch. Its observed rules are:

- deletion protection;
- non-fast-forward protection; and
- pull-request use with unresolved-thread resolution.

It requires zero approving reviews, does not require code-owner or last-push
approval, and contains no required-status-check rule. No bypass actor is
registered. That is why a correct advisory failure can occur after a merge
without preventing it.

## Proposed server-side enforcement packet

The smallest current candidate addition is:

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

This packet is **proposed and not applied**. The check context is observed, but
the GitHub Actions App identity and integration ID must be re-read immediately
before any settings mutation. This document does not authorize a ruleset. It
also does not authorize branch protection, permissions, bypass, approval,
ready, merge, release, deployment, promotion, publication, or source-state
change.

## Remaining proof order

1. **CONFIRMED complete:** issue #4024 source binding, three-helper strict
   bounded capture, and truncated-response handling are present on current main.
2. Re-read the exact current workflow, check-run name, GitHub Actions App
   identity, current ruleset, and current main immediately before a settings
   decision.
3. Through a separately authorized repository-settings operation, add one
   reviewed strict required-status-check rule without weakening deletion,
   non-fast-forward, pull-request, or thread-resolution protections.
4. Use a genuinely capability-separated operator or account for all canaries.
5. Create a draft canary and prove its first `opened` event produces
   `PULL_REQUEST_IS_DRAFT`, not skipped success.
6. Prove a born-ready pull request with no exact record cannot merge while
   `TRANSITION_AUTHORIZATION_MISSING` is outstanding.
7. Prove a draft changed to ready without an exact record cannot merge under
   the same hold.
8. Prove one exact, unedited, unexpired owner record for the current base and
   head allows only that authorization check to pass.
9. Prove stale, edited, malformed, duplicate-key, wrong-base, wrong-head,
   wrong-issue, non-owner, expired, unavailable, oversized, incomplete, and
   truncated source states remain blocked.
10. Push a new head and prove strict currentness requires a fresh record and
    rerun.
11. Record platform rejection before merge; a check that starts after merge is
    not prevention evidence.

Reusing the owner-authenticated path implicated by PRs #4234, #4235, #4238,
and #4239 would not prove capability separation.

## Explicit residual limits

A public commenter can consume the issue-wide capture budget and cause a safe
availability denial. That is a denial-of-service exposure, not an authorization
bypass.

Authorization expiry, comment edit, and comment deletion are evaluated when the
job runs. GitHub does not automatically invalidate an already successful check
later. The control must not be described as continuous revocation or real-time
expiry enforcement.

A successful record identifies an owner-account decision, not the initiating
browser, app, token, or client. Capability separation and audit evidence remain
separate obligations.

## Enforcement boundary

The live source binding and bounded capture prevent silent lookup,
resource-exhaustion, malformed-input, and incomplete-response failure modes.
Requiring the check would make its current outcome a server-side merge
prerequisite. Neither the workflow nor a future ruleset rule creates independent
review, resolves client attribution, or grants source admission, Stage 1B,
Stage 2, release, deployment, promotion, or publication authority.

## Migration and rollback

Historical records retain the issue identity and bytes they actually observed.
Do not rewrite receipts merely because the live control source moved from
deleted issue #1675 to issue #4024.

The bounded-capture and truncated-response code is now on main. Any correction
should be a focused reviewed forward change. If a required-check rule is later
installed, remove or replace that rule through a separately authorized settings
operation before reverting or renaming its workflow, so the protected branch is
not deadlocked.

Never repoint the workflow to a missing issue, weaken negative outcomes to make
a canary green, or treat this document as merge authority.
