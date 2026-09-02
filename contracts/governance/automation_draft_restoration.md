# Automation Draft Restoration v1

**Status:** PROPOSED / incident-scoped / non-merge / non-publisher

`AutomationDraftRestoration` is a short-lived, exact-event declaration for one
attempt to return one open KFM pull request to draft after an unauthorized
`ready_for_review` transition. It exists to implement the containment sequence
recorded by issue #4024 without relying on repository settings or executing pull
request code.

## Admission boundary

A restoration proposal is write-eligible only when all of the following remain
true immediately before mutation:

- the proposal profile is `kfm.automation.draft-restoration.v1`;
- `control_issue` is exactly `4024`;
- the target still exists as one open, unmerged, visibly non-draft pull request;
- base ref, base SHA, head branch, head SHA, repository, author, and pull-request
  number match the proposal exactly;
- the head is a same-repository `automation/` or `fix/` branch;
- the body contains exactly one
  `<!-- KFM_AUTOMATION_DRAFT_ONLY -->` marker;
- GitHub issue events contain exactly one matching `ready_for_review` event with
  the declared timestamp, owner actor, GitHub App attribution, and PR number;
- no later ready/draft/close/reopen/merge transition is present;
- the event is no more than four hours old and not materially in the future; and
- every terminal authority flag remains false.

Missing markers, an already-draft PR, or an already closed or merged PR produces
a bounded no-action result. Identity drift, stale or replayed event evidence,
fork ownership, duplicate markers, or malformed inputs fail closed without a
pull-request mutation.

## Trusted orchestration

`.github/workflows/automation-draft-pr-restorer.yml` is triggered only by the
trusted default-branch `repository_dispatch` event type
`automation-draft-restoration-v1`, or by an explicit trusted
`workflow_dispatch` carrying the same object in one `proposal_json` input. A
repository dispatch carries exactly one top-level `client_payload` property
named `proposal`; the bounded restoration declaration is nested beneath it so
the request remains inside GitHub's repository-dispatch top-level property
limit. The workflow has workflow-level `contents: read` and a single job-level
`pull-requests: write` grant. The workflow:

1. materializes and structurally validates the bounded dispatch proposal;
2. fetches the live PR and paginated issue-event records as untrusted data;
3. validates exact live/event binding with the trusted-base standalone
   validator;
4. repeats the read and binding immediately before mutation;
5. invokes GitHub's `convertPullRequestToDraft` mutation by PR node ID; and
6. verifies the exact restored state.

If restoration fails and the exact PR remains open, unmerged, non-draft, and
marker-bound, the same run closes that PR unmerged as the issue #4024 fallback.
If any binding changed, it stops without closing. The branch and head commit are
never deleted, force-pushed, rewritten, or executed.

## Authority split

| Concern | Owner |
|---|---|
| semantic boundary | `contracts/governance/automation_draft_restoration.md` |
| machine shape | `schemas/contracts/v1/governance/automation_draft_restoration.schema.json` |
| deterministic validation | `tools/validators/governance/validate_automation_draft_restoration.py` |
| focused regressions | `tests/validators/test_validate_automation_draft_restoration.py` |
| privileged orchestration | `.github/workflows/automation-draft-pr-restorer.yml` |
| read-only conformance | `.github/workflows/automation-draft-pr-restorer-test.yml` |
| incident and event evidence | GitHub issue #4024 and exact GitHub PR event records |

## Non-effects

A passing declaration is not independent review, approval, merge authority,
release authority, deployment authority, publication authority, source
admission, sensitive-data access, validator weakening, or repository-settings
permission. It cannot mark a PR ready, merge it, alter branch bytes, write to
`main`, create a release or deployment, publish data, or change a ruleset.

## Rollback

Before integration, abandon the feature branch. After an independently
authorized merge, revert this bounded workflow/validator/schema/test packet
through a reviewed pull request. A live restoration run is reversible by a
separately authorized ready transition; the restorer itself does not grant that
authority.
