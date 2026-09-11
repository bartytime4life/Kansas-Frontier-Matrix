<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/repository-issue-mutation-intent
title: RepositoryIssueMutationIntentCandidate Contract
type: semantic-contract; repository-control-profile; fixture-first
version: v0.1.0
status: proposed; inactive; no-network; non-mutating
owners: OWNER_TBD — repository-control steward · governance steward · validation steward
created: 2026-09-09
updated: 2026-09-09
policy_label: internal; fixture-only; no-authority
related:
  - ../../schemas/contracts/v1/governance/repository_issue_mutation_intent.schema.json
  - ../../tools/validators/repository_control/validate_issue_mutation_intent.py
  - ../../fixtures/contracts/v1/governance/repository_issue_mutation_intent/
  - ./repository_control_state.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, repository-control, mutation-intent, idempotency, readback, fixture-only]
[/KFM_META_BLOCK_V2] -->

# RepositoryIssueMutationIntentCandidate

> A `RepositoryIssueMutationIntentCandidate` is a fixture-only repository-control profile for one exact issue-maintenance action: add the existing `needs-review` label to one issue. It binds the repository, issue, expected state and revision, authority declaration, expiry, and idempotency key before evaluating a declared attempt and exact readback. The evaluator never contacts GitHub, emits a request, changes external state, changes pull-request lifecycle, changes repository settings, or grants mutation authority.

## Status and owning family

| Field | Value |
|---|---|
| Status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY_DECLARATION` |
| Owning contract family | Existing `contracts/governance/` repository-control family |
| Supported target | One GitHub issue |
| Supported action | Exactly `ADD_LABEL` with label `needs-review` |
| Live adapter | Absent |
| Network, credential, or external write effect | None |
| Lifecycle or settings authority | None |

This is a narrow profile of the existing repository-control boundary, not a generic mutation authority. It does not extend `RepositoryControlState` permissions, create a writer role, change a workflow, or alter issue, pull-request, branch, ruleset, release, deployment, promotion, or publication state.

## Placement

ADR-0029 adopted Directory Rules v2. Responsibilities remain split:

| Responsibility | Home |
|---|---|
| Intent and receipt meaning | `contracts/governance/` |
| Machine-checkable shape | `schemas/contracts/v1/governance/` |
| Synthetic cases | `fixtures/contracts/v1/governance/` |
| No-network evaluator | `tools/validators/repository_control/` |
| Executable negative controls | `tests/validators/` |

No workflow, policy bundle, platform setting, data receipt, live adapter, or new root is added by this slice.

## Intent boundary

One intent binds all of the following:

- exact repository `full_name` and numeric repository ID;
- issue number and GitHub node ID;
- expected issue state and expected revision (`updated_at`);
- an explicit `expected_head_sha: null`, because issue labels have no head SHA;
- exactly one action object, fixed to `ADD_LABEL` / `needs-review`;
- one authority reference, the capability-separated `ISSUE_MAINTAINER` actor class, and expiry;
- a bounded caller-supplied idempotency key; and
- a deterministic intent fingerprint and derived intent ID.

An array of actions is deliberately absent. Unknown action fields, a second action, or a different label are schema-invalid.

## Read-only preflight

The fixture supplies a closed preflight snapshot containing the observed repository and issue identities, open/closed state, revision, sorted unique labels, declared authority evidence, observation time, and any prior idempotency record. These are synthetic declarations. The evaluator does not authenticate them against GitHub.

Evaluation fails closed when any of these conditions is present:

- wrong repository name or ID;
- issue number or node-ID substitution;
- state or revision drift;
- missing, mismatched, denied, unknown, or expired authority;
- an unsupported actor class or action shape;
- a reused idempotency key bound to different parameters;
- incoherent replay evidence; or
- a declared attempt after a denied precondition.

## Retry convergence

The intent fingerprint binds every target, expected-state, action, authority, expiry, and idempotency parameter. The preflight replay record binds a previously seen key to its prior fingerprint and outcome.

- If the same intent is replayed and `needs-review` is already present, the result is `NO_OP` with `REPLAY_CONVERGED`.
- If the action is already satisfied without a replay record, the result is `NO_OP` with `ACTION_ALREADY_SATISFIED`.
- If the same key is associated with a different fingerprint, the result is `DENIED` with `IDEMPOTENCY_KEY_REUSED`.
- The evaluator never retries or repeats a write.

## Declared attempt and exact readback

The candidate may model a synthetic subject attempt so the receipt semantics are reviewable before a live adapter exists. `DECLARED_GITHUB_API` means only that fixture fields describe a hypothetical subject operation. It is not a network path in the evaluator and is not authenticated execution evidence.

An `APPLIED` result requires an exact post-action readback declaration:

- repository and issue identities match the intent;
- state remains `OPEN`;
- revision advances beyond the preflight revision and is not later than evaluation time; and
- labels equal the preflight labels plus exactly `needs-review`.

Any mismatch is `ERROR`, never `APPLIED`. A transport failure is explicit `ERROR` with unknown readback. A no-op requires exact readback of the already-satisfied preflight snapshot.

## Compact receipt outcomes

| Outcome | Meaning in this fixture-only profile |
|---|---|
| `ATTEMPTED` | The fixture declares one request attempt after all preconditions passed; no applied state is asserted. |
| `APPLIED` | The fixture declares success and an exact coherent readback. This is not authenticated live proof. |
| `NO_OP` | The requested label was already present, including a converged same-parameter replay. |
| `DENIED` | A target, state, authority, expiry, action, or replay precondition failed closed. |
| `ERROR` | Transport or readback evidence is incomplete or incoherent. |

The compact receipt records stable reason codes, whether an attempt was declared, whether application was modeled, and fingerprints for the intent, target, and readback. Its ID and top-level specification hash are deterministic.

## Fixed non-effects

The schema fixes these claims:

- deterministic evaluation is true;
- validator network access and external mutation are false;
- external state and authority authentication are false;
- a live mutation adapter is absent;
- mutation verification is false; and
- pull-request lifecycle, repository settings, releases, deployments, promotions, and publication are unchanged.

Passing validation proves only deterministic fixture coherence. It is not owner authorization, independent review, live readback, GitHub attribution, a write receipt, or permission to build a live adapter.

## Validation and rollback

The validator checks closed Draft 2020-12 shape, exact target/state/authority matching, expiry, one-action semantics, replay convergence, attempt coherence, exact readback, deterministic identity, and fixed non-effects. Negative fixtures cover stale state, wrong repository, target substitution, action chaining, unsupported action, missing/denied authority, expiry, replay mismatch, transport failure, and readback mismatch.

Before merge, rollback is branch or pull-request deletion. After an authorized merge, revert this additive contract slice. No external state cleanup is required because the implementation has no network or mutation path.
