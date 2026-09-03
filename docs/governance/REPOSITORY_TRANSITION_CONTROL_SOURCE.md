<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/governance/repository-transition-control-source
title: Repository transition control-source binding
type: governance binding and enforcement-candidate note
version: v1.3.0
status: implemented workflow-active advisory; bounded-input hardened; required-status-check not installed
owner: OWNER_TBD — governance steward and repository-control steward
created: 2026-09-03
updated: 2026-09-03
policy_label: repository-facing; governance; fail-closed; non-authoritative
truth_posture: CONFIRMED live issue source and #4237 workflow bootstrap / BOUNDED capture implementation / PROPOSED required-check packet
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
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4234
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4235
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4237
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

PR #4237 integrated the live-source workflow baseline into protected
`main@bd942b45493fa5f80e946ecfb3e810e413787394` on 2026-09-03. The workflow is
therefore **workflow-active** and reads issue #4024 from trusted-base code.

The check remains advisory. Ruleset `15484585`, named `Protect`, still has no
`required_status_checks` rule. A passing or failing
`authorize-ready-and-merge` result is not presently a server-side merge
prerequisite.

The active control uses three trusted-base helpers:

1. `fetch_bounded_issue_comments.py` captures the source page by page under
   strict transport, parser, structure, and serialization ceilings.
2. `validate_control_source_availability.py` requires the exact four-field
   `AVAILABLE` status for the expected repository and issue.
3. `validate_transition_authorization.py` evaluates only the captured bounded
   comments against the exact pull request, base, head, actor, decision, and
   expiry.

All three helpers are fetched from the exact pull-request base SHA. The workflow
never checks out or executes pull-request-head code and has read-only
`contents`, `issues`, and `pull-requests` permissions.

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

These incidents do not identify whether the initiating path was a browser, CLI,
PAT, OAuth client, connector, or another owner-authenticated session. They do
prove that body warnings, draft creation, and asynchronous advisory checks are
not preventive merge containment.

## Live-source rules

- Keep issue #4024 available while trusted-base workflow code references it.
- Only an unedited owner-account comment containing one strict authorization
  marker can satisfy the transition validator.
- Each record is exact to repository, control issue, pull request, base SHA,
  head SHA, actor, decision, and expiry.
- Missing, unavailable, malformed, edited, stale, expired, future-dated,
  wrong-base, wrong-head, wrong-issue, duplicate-key, non-owner, truncated, or
  over-limit material fails closed.
- Raw response bodies, comments, numeric tokens, and transport exceptions are
  not copied into bounded decision output.

## Bounded source capture

The capture helper requests at most 100 records per page and admits at most 100
pages. A bounded sentinel page is used when page 100 is full so the source is
never silently truncated.

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
probe byte. The helper rejects non-standard `NaN`, `Infinity`, and `-Infinity`,
rejects non-finite parsed floats and overlong integer tokens, rejects duplicate
object keys, and normalizes parser `ValueError`, `OverflowError`, and
`RecursionError` into a finite invalid-page result. Output serialization uses
`allow_nan=false`.

Any fetch, token, page, byte, node, depth, UTF-8, JSON, shape, completeness, or
serialization failure produces only:

1. an empty comments array; and
2. the four-field source status with `status=UNAVAILABLE`.

The helper then returns control to the trusted-base availability validator,
which emits the nonzero blocking classification.

## Pull-request lifecycle behavior

The workflow listens to `opened`, `reopened`, `synchronize`,
`ready_for_review`, `converted_to_draft`, `edited`, `labeled`, and `unlabeled`.

Its authorization job runs for draft and non-draft pull requests:

- draft state returns
  `EXPECTED_READINESS_HOLD / PULL_REQUEST_IS_DRAFT / exit 3`;
- born-ready `opened` without a record returns
  `EXPECTED_READINESS_HOLD / TRANSITION_AUTHORIZATION_MISSING / exit 3`;
- later `ready_for_review` without a record returns the same missing-record
  hold.

The job must not use a draft-state `if` predicate. GitHub treats a skipped job
as successful for required-check evaluation. Leaving a skipped-success result
on a draft head would reopen the ready-to-merge race.

## Exact platform snapshot

Ruleset `15484585` is active for the default branch. Its observed rules are:

- deletion protection;
- non-fast-forward protection; and
- pull-request use with unresolved-thread resolution.

It requires zero approving reviews and contains no required-status-check rule.
That is why an advisory failure can occur after a merge without preventing it.

## Proposed server-side enforcement packet

After the bounded workflow bytes are independently reviewed and integrated, the
smallest candidate addition is:

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

This packet is **proposed and not applied**. This document does not authorize a ruleset.
It also does not authorize branch-protection, permission, bypass, approval, ready, merge, release,
deployment, promotion, publication, or source-state change.

## Remaining proof order

1. Integrate the bounded-capture implementation through a separately authorized
   path.
2. Re-read the helper, workflow, check-run name, and GitHub Actions App identity
   on exact current main.
3. Run a fresh draft event and verify the active workflow emits
   `PULL_REQUEST_IS_DRAFT`, not skipped success.
4. Through a separately authorized settings operation, add the reviewed strict
   required-status-check rule without weakening existing protections.
5. Use a genuinely capability-separated operator for negative and positive
   canaries.
6. Prove born-ready and later-ready requests cannot merge without an exact
   current record.
7. Prove stale, edited, malformed, duplicate-key, wrong-base, wrong-head,
   wrong-issue, non-owner, expired, unavailable, oversized, and incomplete
   source states remain blocked.
8. Advance the head and prove strict currentness requires a fresh record and
   rerun.
9. Record platform rejection before merge; a check that starts after merge is
   not prevention evidence.

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

Repairing the source lookup and bounding capture prevent silent retrieval and
resource-exhaustion failure modes. Requiring the check would make its current
outcome a server-side merge prerequisite. Neither action creates independent
review, resolves client attribution, or grants source admission, Stage 1B,
Stage 2, release, deployment, promotion, or publication authority.

## Migration and rollback

Historical records retain the issue identity and bytes they actually observed.
Do not rewrite receipts merely because the live control source moved from
deleted issue #1675 to issue #4024.

Before integration, abandon the candidate branch. After integration, rollback
is a focused forward restoration of the previously reviewed helper/workflow
bytes. If a required-check rule is later installed, remove or replace that rule
through a separately authorized settings operation before reverting or renaming
its workflow, so the protected branch is not deadlocked.

Never repoint the workflow to a missing issue, weaken negative outcomes to make
a canary green, or treat this document as merge authority.
