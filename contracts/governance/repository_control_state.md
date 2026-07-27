<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/repository-control-state
title: RepositoryControlState semantic contract
version: v0.1.0
status: proposed
owner: OWNER_TBD — governance steward and repository-control steward
created: 2026-07-26
updated: 2026-07-26
policy_label: repository-facing; governance; fail-closed; non-authoritative
related:
  - ../../docs/doctrine/directory-rules.md
  - ../../control_plane/repository_control_state.yaml
  - ../../schemas/contracts/v1/governance/repository_control_state.schema.json
  - ../../schemas/contracts/v1/governance/ci_outcome.schema.json
  - ../../tools/validators/repository_control/validate_repository_control.py
  - ../../tests/validators/test_repository_control.py
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1675
[/KFM_META_BLOCK_V2] -->

# `RepositoryControlState`

> **One-line meaning.** `RepositoryControlState` is a reviewed machine projection of bounded repository-control evidence; it can describe authorization and detect divergence, but it cannot authorize itself or replace GitHub repository settings.

## Authority boundary

This contract defines semantic meaning under `contracts/governance/`. Machine shape belongs to the paired schema. The current projection belongs under `control_plane/`. GitHub rulesets and branch protection remain platform settings. A schema-valid state, a passing validator, a green workflow, an issue comment, or a pull request is not review, merge, release, deployment, or publication authority by itself.

## Required semantics

| Field family | Meaning |
|---|---|
| Identity | `schema_version`, `state_id`, and `repository` identify the projection and target repository. |
| Base snapshot | Records the default branch, pinned `main` SHA, observation time, and observed open pull-request set. |
| Claim | Records one finite state (`IDLE`, `ACTIVE`, `HELD`, or `TERMINAL`), exact branch, active PR set, allowed path patterns, allowed operations, expiry, and terminal condition. |
| Authorization evidence | Identifies the actor and evidence references outside the state file. An active claim requires external evidence; the file cannot cite itself as authority. |
| Permissions | Every consequential permission is explicit and defaults to `false`, including merge, source activation, proof construction, release, deployment, and publication. |
| Settings snapshot | Records only settings that were actually verified. Unobserved branch protection, rulesets, bypass actors, review requirements, and direct-push controls remain `NEEDS_VERIFICATION` or `null`. |
| Digest | `state_digest` covers every top-level field except itself under `KFM-REPOSITORY-CONTROL-1`. |
| Boundary | States what the projection and evaluator cannot do. |

## Finite claim states

| State | Meaning | Merge posture |
|---|---|---|
| `IDLE` | No active claim exists. | Held. |
| `ACTIVE` | One externally authorized branch/PR/path/operation packet is being evaluated. | Determined by explicit permission plus verified settings evidence. |
| `HELD` | Work is intentionally blocked pending a named condition. | Denied. |
| `TERMINAL` | The claim reached a terminal observation and requires reconciliation before reuse. | Denied. |

## Bounded exception rules

An active exception must pin the current base SHA, branch, PR number, allowed paths, allowed operations, expiry or terminal condition, actor, evidence references, and default-false permissions. Wildcards are allowed only when their review meaning is clear and testable. `modify_control_logic` is separately gated because a guard must not silently weaken itself.

## Failure behavior

Malformed, unavailable, digest-mismatched, stale, expired, branch-mismatched, PR-mismatched, path-out-of-scope, operation-out-of-scope, or unauthorized terminal state must fail closed. A merged terminal state observed while `merge=false` is a `REGRESSION`, not evidence that merge was authorized. Unverified repository settings produce `UNKNOWN` when a decision depends on them.

## Registered `CIOutcome` vocabulary

The paired `CIOutcome` schema records what a declared check established without collapsing distinct states into a generic red/green signal.

| Outcome | Meaning | Default merge posture |
|---|---|---|
| `PASS` | The declared executable assertions ran and passed. | Non-blocking for that check only. |
| `EXPECTED_READINESS_HOLD` | Permission, implementation, review, settings evidence, or another declared prerequisite is intentionally missing. | Blocking. |
| `REGRESSION` | Accepted behavior regressed, scope was violated, or terminal GitHub state advanced beyond the claim. | Blocking. |
| `NOT_APPLICABLE` | The check is outside the evaluated scope. | Non-blocking with a reason. |
| `SKIPPED_EXPLICIT` | A declared precondition prevented execution and the skip was recorded. | Consumer-dependent; never executable proof. |
| `UNKNOWN` | Available evidence cannot classify the result safely. | Blocking for trust-bearing decisions. |

`evidence_kind` remains separate: `EXECUTABLE_PROOF`, `READINESS_EVIDENCE`, or `NEITHER`. A green held job must not be represented as domain validation, proof construction, release readiness, or publication authority. `PASS` proves only the declared assertions.

## Placement basis

- `contracts/governance/` owns meaning.
- `schemas/contracts/v1/governance/` owns shape.
- `control_plane/` owns the machine projection of what governs what.
- `tools/validators/` owns the checker.
- `fixtures/` and `tests/` own reusable examples and executable conformance evidence.
- `.github/` may later orchestrate the checker, but it does not become authorization authority.

This split follows adopted Directory Rules v2 responsibility ownership and avoids a parallel policy, release, proof, or platform-settings authority.

## Rollback

Before merge, close the draft PR and abandon the branch. After merge, revert the scoped commit. Preserve issue history and incident fixtures; do not rewrite shared history or represent rollback as erasing the observed control incident.
