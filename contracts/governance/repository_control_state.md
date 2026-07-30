<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/repository-control-state
title: RepositoryControlState semantic contract
version: v0.4.0
status: proposed
owner: OWNER_TBD — governance steward and repository-control steward
created: 2026-07-26
updated: 2026-07-30
policy_label: repository-facing; governance; fail-closed; non-authoritative
related:
  - ../../docs/doctrine/directory-rules.md
  - ../../control_plane/repository_control_state.yaml
  - ../../schemas/contracts/v1/governance/repository_control_state.schema.json
  - ../../schemas/contracts/v1/governance/repository_control_context.schema.json
  - ../../schemas/contracts/v1/governance/repository_transition_authorization.schema.json
  - ../../schemas/contracts/v1/governance/ci_outcome.schema.json
  - ../../tools/validators/repository_control/validate_repository_control.py
  - ../../tools/validators/repository_control/validate_transition_authorization.py
  - ../../tests/validators/test_repository_control.py
  - ../../tests/validators/test_repository_transition_authorization.py
  - ../../.github/workflows/repository-control.yml
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1675
[/KFM_META_BLOCK_V2] -->

# `RepositoryControlState`

> **One-line meaning.** `RepositoryControlState` is a reviewed, observation-time machine projection of bounded repository-control evidence; it can describe authorization and detect divergence, but it cannot authorize itself, self-refresh to the containing commit, or replace GitHub repository settings.

## Authority boundary

This contract defines semantic meaning under `contracts/governance/`. Machine shapes belong to the paired state, prepared-context, and outcome schemas. The current projection belongs under `control_plane/`. GitHub rulesets and branch protection remain platform settings. A schema-valid state, a passing validator, a green workflow, an issue comment, or a pull request is not review, merge, release, deployment, or publication authority by itself.

## Required semantics

| Field family | Meaning |
|---|---|
| Identity | `schema_version`, `state_id`, `repository`, and `projection_status` identify the projection and whether it is proposed, confirmed, or superseded. |
| Base snapshot | Records the default branch, the `main` SHA observed for the bounded snapshot, observation time, and open pull-request set observed at that time. It is a historical checkpoint and active-claim base pin, not a self-refreshing statement of live GitHub state. |
| Claim | Records one finite state (`IDLE`, `ACTIVE`, `HELD`, or `TERMINAL`), exact branch, active PR set, allowed path patterns, allowed operations, expiry, and terminal condition. |
| Authorization evidence | Identifies the actor and evidence references outside the state file. An active claim requires external evidence; the file cannot cite itself as authority. |
| Permissions | Every consequential permission is explicit and defaults to `false`, including ready transition, merge, source activation, proof construction, release, deployment, and publication. |
| Settings snapshot | Records only settings that were actually verified. A `CONFIRMED` snapshot must contain determinate review, status-check, bypass, direct-push, force-push, deletion, and draft-merge fields. |
| Prepared context | Carries the current base/head/branch/PR/path/operation/open-PR evidence and, when merge permission is true, a separately evidenced platform block for draft state, ready transition, approvals, conversations, normalized required checks, and mergeability. |
| Transition authorization | Records a short-lived Model B owner-account decision for one repository, control issue, PR, base SHA, head SHA, and expiry. It does not identify the initiating client or create independent review. |
| Digest | `state_digest` covers every top-level state field except itself under `KFM-REPOSITORY-CONTROL-2`. |
| Boundary | States what the projection and evaluator cannot do. |

## Finite claim states

| State | Meaning | Merge posture |
|---|---|---|
| `IDLE` | No active claim exists. | Held. |
| `ACTIVE` | One externally authorized branch/PR/path/operation packet is being evaluated. The projection itself must be `CONFIRMED`. | Determined by explicit permission, verified settings, and current platform evidence. |
| `HELD` | Work is intentionally blocked pending a named condition. | Denied. |
| `TERMINAL` | The claim reached a terminal observation and requires reconciliation before reuse. | Denied. |

## Version 2 observed-base semantics

Schema version `2.0.0` corrects the live-versus-observed ambiguity in the base snapshot. The registered JSON key `base.current_main_sha` is retained so existing incident fixtures and consumers do not gain a second alias or require an unsafe flag-day migration. In version 2 it has one exact meaning: **the default-branch SHA observed at `base.observed_at` for this snapshot**.

The field does not claim that its value is the commit containing the projection, and advancing `main` after the observation does not by itself make a non-active historical snapshot invalid. Git commit identity depends on the committed tree, so a tracked file must not be treated as a self-updating pointer to its own containing commit. Current live head evidence belongs in a freshly prepared context or an externally recorded control cursor.

For an `ACTIVE` claim, the evaluator still compares `context.base_sha` with this observed snapshot. A mismatch is `OBSERVED_BASE_SHA_MISMATCH` and fails closed because the authorized branch was prepared from a different base. For `IDLE`, `HELD`, or `TERMINAL` projections, later default-branch movement does not silently reactivate work or transform the historical observation into a regression; those states remain non-authorizing on their own terms.

## Bounded exception rules

An active exception must pin the observed base SHA, branch, PR number, observed open-PR set, allowed paths, allowed operations, expiry or terminal condition, actor, evidence references, and default-false permissions. Path scope supports only exact file paths or an explicit trailing `/**` recursive prefix. Other glob syntax, absolute paths, backslashes, control characters, dot segments, parent segments, and duplicate entries are invalid. `modify_control_logic` is separately gated because a guard must not silently weaken itself.

## Platform evidence rules

`settings_snapshot.status: CONFIRMED` means all registered settings fields were actually determined from durable platform evidence. It is invalid to mark the snapshot confirmed while leaving review, push, deletion, or draft behavior as `null` or `NEEDS_VERIFICATION`.

Merge permission alone never produces `PASS`. A normal open-PR pass also requires `platform_merge_evidence.status: CONFIRMED`, including:

- the evaluated PR number and exact head SHA;
- draft state and whether a ready transition was observed;
- current approving-review count;
- unresolved conversation count;
- normalized outcomes for every verified required check;
- current mergeability;
- evidence references and observation time.

Confirmed platform evidence is one atomic prepared-context snapshot: its PR number and head SHA must match the evaluated context, and its `observed_at` must equal `context.now`. A binding mismatch is a regression. A different observation time is not accepted as current evidence and produces `UNKNOWN`; adapters must prepare a new snapshot instead of reusing approvals, checks, or mergeability from another time.

A required check satisfies the merge-readiness evaluation only with `PASS`. `EXPECTED_READINESS_HOLD`, `SKIPPED_EXPLICIT`, and `NOT_APPLICABLE` remain holds for a required check; `UNKNOWN` remains unknown; `REGRESSION` remains a regression. The evaluator does not infer GitHub settings or convert raw workflow failures into a classification.

## Head-bound transition records

The proposed `RepositoryTransitionAuthorization` is a separate, short-lived record embedded as strict JSON in a comment intended to remain append-only on the repository-control issue. It exists to make a Model B ready-and-merge decision explicit and exact-head bound when independent review is unavailable.

An accepted record must match:

- the repository and designated control issue;
- the pull-request number;
- the current default-branch base SHA and pull-request head SHA;
- the repository-owner login recorded both in the record and by GitHub as the unedited comment author;
- the finite decision `ALLOW_READY_AND_MERGE`; and
- an expiry after comment creation and no more than four hours later.

The trusted-base workflow rejects draft PRs, edited comments, duplicate or unknown JSON fields, stale or overlong records, and base/head mismatches. Comment bodies are treated as untrusted bounded data and are never executed or echoed.

Post each authorization as a new comment on issue #1675 after the PR base and head are frozen. Do not edit it; post a replacement for any correction or new head. This synthetic example shows the exact marker and shape:

```html
<!-- KFM_REPOSITORY_TRANSITION_AUTHORIZATION_V1
{"schema_version":"1.0.0","authorization_id":"kfm-rta-pr-9001-head-222222222222","repository":"bartytime4life/Kansas-Frontier-Matrix","control_issue":1675,"pr_number":9001,"base_sha":"1111111111111111111111111111111111111111","head_sha":"2222222222222222222222222222222222222222","authorizing_actor":"bartytime4life","decision":"ALLOW_READY_AND_MERGE","expires_at":"2026-07-30T22:00:00Z","reason":"Synthetic exact-head transition example.","evidence_refs":["fixture://repository-control/pr/9001/head/222222222222"]}
-->
```

Keep the PR draft until that separate transition decision exists, then mark it ready to trigger the check. If an already-ready PR needs reevaluation, an `edited`, `labeled`, or `unlabeled` PR event can request a new run; none of those events supplies authority without a matching unedited #1675 record.

The expiry and unedited-comment condition are evaluated at workflow run time. GitHub does not automatically turn an already-recorded successful check into a failure when the timestamp later passes or the issue comment is later edited or deleted. Therefore the record is an exact-head point-in-time transition decision, not a continuously enforced time lease or immutable ledger: post it only when the ready-and-merge transition is actually intended, preserve it, and request a fresh run before relying on it after expiry or any comment mutation. A later head or base change invalidates the exact binding and causes a new run to hold.

This control closes an auditability gap, not an identity-separation gap. An owner login observed on a GitHub comment establishes the authenticated account identity exposed by the API. It does **not** establish whether a human browser, OAuth token, GitHub App, PAT, or another client initiated the action. If an app acts through the same owner identity, this record cannot distinguish it from the human owner. Security-log evidence, app/token restriction, and future Model A independent review remain separate controls.

The workflow check name is `repository-control / authorize-ready-and-merge`. It is advisory until GitHub ruleset `15484585` separately requires that exact check with strict/up-to-date behavior. A workflow file cannot make itself required, and this contract does not authorize a ruleset mutation.

## Failure behavior

Malformed, unavailable, digest-mismatched, observed-base-mismatched, expired, branch-mismatched, PR-mismatched, path-out-of-scope, operation-out-of-scope, control-self-modifying, or unauthorized terminal state fails closed. Later live-head movement alone is not an observed-base mismatch for a non-active historical snapshot. For a merged PR, terminal divergence is evaluated before applicability or explicit-skip handling: a merged state observed while the claim is not active or `merge=false` is a `REGRESSION`, not evidence that merge was authorized. An observed, confirmed, current ready transition without permission is also a regression in `IDLE`, `ACTIVE`, `HELD`, and `TERMINAL` claim states. Unverified settings or non-current platform state produce `UNKNOWN` when a decision depends on them. An explicit skip is otherwise recorded distinctly and remains merge-blocking by default.

## Registered `CIOutcome` vocabulary

The paired `CIOutcome` schema records what a declared check established without collapsing distinct states into a generic red/green signal.

| Outcome | Meaning | Default merge posture |
|---|---|---|
| `PASS` | The declared executable assertions ran and passed. | Non-blocking for that check only. |
| `EXPECTED_READINESS_HOLD` | Permission, implementation, review, settings evidence, or another declared prerequisite is intentionally missing. | Blocking. |
| `REGRESSION` | Accepted behavior regressed, scope was violated, or terminal GitHub state advanced beyond the claim. | Blocking. |
| `NOT_APPLICABLE` | The check is outside the evaluated scope. | Non-blocking with an explicit reason. |
| `SKIPPED_EXPLICIT` | A declared precondition prevented execution and the skip was recorded. | Blocking by default; never executable proof. |
| `UNKNOWN` | Available evidence cannot classify the result safely. | Blocking for trust-bearing decisions. |

`evidence_kind` remains separate: `EXECUTABLE_PROOF`, `READINESS_EVIDENCE`, or `NEITHER`. A green held job must not be represented as domain validation, proof construction, release readiness, or publication authority. `PASS` proves only the declared assertions. Every emitted outcome includes the state digest, detailed findings, and available state/context/platform evidence references.

## Placement basis

- `contracts/governance/` owns meaning.
- `schemas/contracts/v1/governance/` owns state, prepared-context, and outcome shape.
- `control_plane/` owns the machine projection of what governs what.
- `tools/validators/` owns the checker.
- `tests/fixtures/` and `tests/` own test-local examples and executable conformance evidence.
- `.github/` may orchestrate the trusted-base checker, but it does not become authorization authority and cannot make its own check required.

This split follows adopted Directory Rules v2 responsibility ownership and avoids a parallel policy, release, proof, or platform-settings authority.

## Rollback

Before merge, close the draft PR and abandon the branch. After merge, remove any required-check coupling before reverting or renaming the workflow so `main` is not deadlocked, then use a focused reviewed revert. Preserve issue history and incident fixtures; do not rewrite shared history or represent rollback as erasing the observed control incident.
