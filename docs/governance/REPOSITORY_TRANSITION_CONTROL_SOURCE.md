<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/governance/repository-transition-control-source
title: Repository transition control-source binding
type: governance binding and enforcement-candidate note
version: v1.3.6
status: current-main workflow-active advisory; three-helper bounded capture integrated; declared Content-Length completeness correction validated branch-only; required-status-check authorization expired
owner: OWNER_TBD — governance steward and repository-control steward
created: 2026-09-03
updated: 2026-09-03
policy_label: repository-facing; governance; fail-closed; non-authoritative
truth_posture: CONFIRMED current-main issue-#4024 binding and strict bounded-EOF capture / CONFIRMED silent-short declared-length gap on main / VALIDATED_BRANCH_ONLY completeness correction / EXPIRED_UNAPPLIED required-check authorization
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
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5532535765
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5532579086
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5532649271
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5533558088
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5533902911
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5534073715
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/fix/repository-control-content-length-completeness-20260903
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
`main@7d9eda78f7da0aee0a2396d31780aaafb5694c7b`. PR #4238 advanced bounded
capture failure handling as current
`main@7c5d4125c277536258be6345e366efae59dbe5d6`, tree
`0a9aaac391d9c8a101234fc9cee8facbe1c4e5c6`.

The current protected-main workflow uses three trusted-base helpers:

1. `fetch_bounded_issue_comments.py` captures the source page by page under
   strict transport-byte, parser, structure, pagination, and serialization
   ceilings, with bounded reads to EOF.
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

## Declared Content-Length completeness gap and branch-only correction

Fresh review of the exact current-main helper found that it does not inspect or
compare a declared `Content-Length`. It reads under the page and aggregate byte
budgets until the response returns EOF, then parses the bytes it received. A
peer can therefore declare a longer body, end the transfer after a complete
valid-JSON prefix such as `[]`, and have that prefix classified as an
`AVAILABLE` source.

Issue #4024 comment `5533902911` records the bounded reproduction and the
branch-only correction. Comment `5534073715` records a same-session second-pass
technical review; it is not independent human or capability-separated review.

The preserved correction is:

- branch: `fix/repository-control-content-length-completeness-20260903`;
- exact head: `5fe7ca322c838f5de3d677977a12302ba3c9e6f6`;
- exact tree from fresh GitHub branch readback:
  `841ce3565e297e2a4778dd56cd4a4ef3e9e6b78f`;
- helper blob: `9047c59d2ba91618078713ebffc2989ac282ab9b`;
- direct-regression blob: `174733cb47d00ed688c168d3deee5015ba316e3e`;
- permanent net paths: the capture helper and
  `tests/validators/test_repository_control_content_length.py`.

The two issue comments transcribed the final tree as
`841ce7988aabc4b864a275e61c7253003848f082`. That value is not the tree of exact
head `5fe7ca322c838f5de3d677977a12302ba3c9e6f6` and must not be used as its
identity.

The correction collects all visible `Content-Length` values, rejects malformed
or conflicting declarations, rejects a declared size above the applicable
budget before reading, and requires the received byte count to equal a valid
declared length after EOF. A missing `Content-Length` remains permissible and
uses the existing bounded-EOF behavior.

That correction is validated branch-only. It is not integrated into protected
main, and no pull request exists for it. This note records the distinction; it
does not authorize delivery or integration.

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

### Current-main bounded-capture merge — PR #4238

PR #4238 was restored to draft after one unauthorized ready event, then marked
ready again at `2026-09-03T21:29:33Z` and merged four seconds later. The owner
account is the recorded actor for both final transitions and neither event names
a performing GitHub App. The repository-control run captured the live source
and correctly classified the exact head as
`TRANSITION_AUTHORIZATION_MISSING`, but it was created one second after merge.
The later declared-length completeness finding does not change that incident
timeline or classification.

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
  wrong-base, wrong-head, wrong-issue, duplicate-key, non-owner, or over-limit
  material fails closed within the admitted capture semantics.
- Malformed-JSON truncation fails closed. Silent transport truncation that ends
  on complete valid JSON is a known current-main gap when a longer
  `Content-Length` is declared; the exact branch-only correction above detects
  that mismatch.
- Raw response bodies, comments, numeric tokens, and transport exceptions are
  not copied into bounded decision output.

## Current bounded source capture

The capture helper requests at most 100 records per page and admits at most
100 pages. A bounded sentinel page is used when page 100 is full so the source
is never silently truncated at the pagination limit.

The fixed limits are:

- 8 MiB of transferred input per page;
- 16 MiB of aggregate transferred and reserialized input;
- 10,000 admitted comment records;
- JSON depth of 32;
- 100,000 JSON nodes per page;
- 1,000,000 JSON nodes across the capture;
- 128 digits in an integer token; and
- 128 characters in a floating-point token.

Each current-main response read receives only the remaining byte allowance plus
one overflow probe byte. The reader stops at EOF but does not currently verify
that EOF agrees with a declared `Content-Length`. Exact declared-length
verification remains in the branch-only correction identified above.

The current-main helper rejects non-standard `NaN`, `Infinity`, and
`-Infinity`, rejects non-finite parsed floats and overlong integer tokens,
rejects duplicate object keys, and normalizes parser `ValueError`,
`OverflowError`, and `RecursionError` into a finite invalid-page result. Output
serialization uses `allow_nan=false`.

On current main, any detected fetch, token, page, byte, node, depth, UTF-8, JSON,
shape, or serialization failure produces only:

1. an empty comments array; and
2. the four-field source status with `status=UNAVAILABLE`.

The branch-only correction additionally classifies malformed or conflicting
declared lengths as `CONTROL_SOURCE_CONTENT_LENGTH_INVALID` and declared versus
received mismatches as `CONTROL_SOURCE_CONTENT_LENGTH_MISMATCH`, while
preserving the same bounded failure artifacts.

The helper returns control to the trusted-base availability validator, which
emits the nonzero blocking classification for an `UNAVAILABLE` source.

## Pull-request lifecycle behavior

The current workflow listens to `opened`, `reopened`, `synchronize`,
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

## Expired authorization; server-side packet remains unapplied

The smallest reviewed addition remains:

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

The required-check addition remains **proposed and not applied**. Its bounded
owner authorization expired at `2026-09-03T23:30:00Z`.

The packet remains **unapplied**. `REQUIRED-STATUS-CHECK AUTHORIZED BUT NOT APPLIED`
was the bounded status through `2026-09-03T23:30:00Z`; that authorization has
expired. Issue #4024 comment `5532535765` preserves the rollback-bound operator
commands, comment `5532579086` records the expired owner authorization, and
comment `5532649271` confirms that the connected GitHub capability exposes
ruleset reads but no Administration-write operation. Comment `5533558088`
records the validated, Drive-published operator package; publishing that package
did not renew authority or apply the setting. No ruleset mutation was attempted
through the connected surface.

No settings operation may reuse the expired authorization. A new owner decision
must be bound to the exact current main, tree, ruleset preimage, check context,
GitHub Actions integration identity, operation, rollback, and validity window
before a separately authenticated settings mutation.

This document does not authorize a ruleset mutation; preservation of the packet
does not itself authorize a ruleset mutation. It also does not authorize branch
protection, permissions, bypass, approval, ready, merge, release, deployment,
promotion, publication, or source-state change.

## Remaining proof order

1. **CONFIRMED on current main:** issue #4024 source binding, three-helper
   resource-bounded capture, strict parser and serialization behavior, bounded
   pagination, and bounded reads to EOF.
2. **CONFIRMED branch-only:** exact correction
   `fix/repository-control-content-length-completeness-20260903@5fe7ca322c838f5de3d677977a12302ba3c9e6f6`
   detects malformed, conflicting, oversized, and mismatched declared lengths.
3. Obtain genuinely independent exact-final-head review and a separately
   authorized delivery decision before opening or integrating that correction.
4. Re-read the exact current workflow, check-run name, GitHub Actions App
   identity, current ruleset, and current main immediately before requesting a
   new settings authorization.
5. After a new exact owner authorization, use a separately authenticated,
   abort-on-drift repository-settings operation to add one reviewed strict
   required-status-check rule without weakening deletion, non-fast-forward,
   pull-request, or thread-resolution protections.
6. Use a genuinely capability-separated operator or account for all canaries.
7. Create a draft canary and prove its first `opened` event produces
   `PULL_REQUEST_IS_DRAFT`, not skipped success.
8. Prove a born-ready pull request with no exact record cannot merge while
   `TRANSITION_AUTHORIZATION_MISSING` is outstanding.
9. Prove a draft changed to ready without an exact record cannot merge under
   the same hold.
10. Prove one exact, unedited, unexpired owner record for the current base and
    head allows only that authorization check to pass.
11. Prove stale, edited, malformed, duplicate-key, wrong-base, wrong-head,
    wrong-issue, non-owner, expired, unavailable, oversized, incomplete, and
    truncated source states remain blocked after the completeness correction is
    integrated.
12. Push a new head and prove strict currentness requires a fresh record and
    rerun.
13. Record platform rejection before merge; a check that starts after merge is
    not prevention evidence.

Reusing the owner-authenticated path implicated by PRs #4234, #4235, #4238,
and #4239 would not prove capability separation.

## Explicit residual limits

A public commenter can consume the issue-wide capture budget and cause a safe
availability denial. That is a denial-of-service exposure, not an authorization
bypass.

Current main can treat a silently short response as complete when the received
prefix is valid JSON because it does not compare EOF with a declared
`Content-Length`. The exact branch-only correction closes that signal only when
a valid length is declared. A missing `Content-Length` remains permissible and
therefore proves neither transport completeness nor cryptographic source
authenticity.

Authorization expiry, comment edit, and comment deletion are evaluated when the
job runs. GitHub does not automatically invalidate an already successful check
later. The control must not be described as continuous revocation or real-time
expiry enforcement.

A successful record identifies an owner-account decision, not the initiating
browser, app, token, or client. Capability separation and audit evidence remain
separate obligations.

## Enforcement boundary

The live source binding and current-main bounded capture prevent silent issue
lookup, unbounded resource consumption, and admitted malformed-input failure
modes. They do not yet prevent every incomplete-response case. Integrating the
exact declared-length correction would make a present, valid `Content-Length`
a checked completeness signal; it would not make absent-length responses,
source authenticity, or continuous revocation proven.

Requiring the authorization check would make its current outcome a server-side
merge prerequisite. Neither the workflow nor a future ruleset rule creates
independent review, resolves client attribution, or grants source admission,
Stage 1B, Stage 2, release, deployment, promotion, or publication authority.

## Migration and rollback

Historical records retain the issue identity and bytes they actually observed.
Do not rewrite receipts merely because the live control source moved from
deleted issue #1675 to issue #4024.

The three-helper resource-bounded capture is on main. Strict declared-length
completeness remains on the exact validated branch identified above. Any later
integration or correction should be a focused reviewed forward change. If a
required-check rule is later installed, remove or replace that rule through a
separately authorized settings operation before reverting or renaming its
workflow, so the protected branch is not deadlocked.

Never repoint the workflow to a missing issue, weaken negative outcomes to make
a canary green, treat a branch-only repair as integrated, or treat this document
as merge authority.
