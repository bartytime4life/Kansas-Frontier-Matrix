<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-role-sensitivity-readme
title: policy/role/sensitivity/ — Role-and-Sensitivity Policy Hold Boundary
type: readme
version: v0.1.0
status: draft; BOUNDARY_COMPACT; repository-grounded; placeholder-only; scope-unresolved; inactive; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy/ to @bartytime4life; no accepted role-policy or sensitivity steward and no independent approver were established
created: 2026-08-13
updated: 2026-08-13
current_path: policy/role/sensitivity/README.md
owning_root: policy/
policy_label: internal; policy; role; sensitivity; placeholder; hold; non-release; non-publication
responsibility: Preserve a fail-closed boundary around the unresolved role-and-sensitivity placeholder without defining role semantics, assigning authority, classifying sensitivity, evaluating policy, approving release, or publishing.
base_commit: 09a01ef8a71a557efc1c35bda6f9b762a429a1f3
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED README plus gitkeep only, no parent role README, no rule source, no contract binding, no tests, and no consumer / PROPOSED narrow composition boundary for an already-defined role and already-determined sensitivity posture / HOLD semantic scope, scope ID, owner, package, evaluator, and consumer decisions / UNKNOWN whether role means actor, reviewer, source, or another governed role family
related:
  - ../../README.md
  - ../../sensitivity/README.md
  - ../../decision/README.md
  - ../../../policy/decision/reviewer_roles.v1.json
  - ../../../contracts/governance/review_authority_binding.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../control_plane/root_registry.yaml
  - ../../../release/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: role :: sensitivity

> **One-line purpose.** `policy/role/sensitivity/` is an unresolved placeholder
> for policy that may compose an already-defined role with an already-determined
> sensitivity posture for one bounded operation; until that meaning is accepted,
> operations that depend on this lane remain held.

> [!IMPORTANT]
> **Safe current conclusion at `main@09a01ef8a71a`:** the directory contains
> only `.gitkeep` and this README. It has no Rego, profile, contract binding,
> schema, fixture, test, validator, bundle, evaluator, consumer, decision record,
> or release integration. It implements no role or sensitivity control.

> [!CAUTION]
> The word `role` is not defined by this path. Repository doctrine discusses
> actor roles, reviewer roles, source roles, service capabilities, and data or
> evidence roles. This README must not collapse those families, assign a person
> to a role, authenticate authority, or infer that a named role may view or
> release sensitive material.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Children](#current-direct-child-map) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Lifecycle](#lifecycle-and-trust-boundary) · [Validation](#validation) · [Contributing](#contributor-guidance) · [Correction](#correction-and-rollback) · [Open work](#open-verification-register)

## Purpose

This leaf exists to make uncertainty explicit. Its only safe prospective policy
question is:

> Given a bounded operation, authenticated caller or reviewed source reference,
> an accepted role meaning and authority binding, an independently determined
> sensitivity posture, rights and consent context, audience, lifecycle state,
> and exact policy identity, is the operation allowed, restricted, held, denied,
> or routed to authorized review?

That question remains **PROPOSED**. Current repository evidence does not decide
which role family belongs here or prove that this path should survive.

## Inherited authority, owner, and scope

| Field | Current boundary |
|---|---|
| Parent authority | [`policy/`](../../README.md), KFM's canonical policy-rule root. |
| Immediate parent | `policy/role/` has no README or accepted local contract at the pinned base. This leaf cannot manufacture the missing parent semantics. |
| Related policy | [`policy/sensitivity/`](../../sensitivity/README.md) owns sensitivity-policy source; [`policy/decision/`](../../decision/README.md) documents finite outcome and normalization boundaries. |
| README profile | `BOUNDARY_COMPACT` because the path implies role, access, sensitivity, exposure, and review trust changes. |
| Placement basis | [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../../docs/doctrine/directory-rules.md) place policy source under `policy/`; they do not accept this leaf's semantics. |
| Local owner and scope ID | **NEEDS VERIFICATION.** No accepted owner, role family, or scope identifier was established. |
| Current placement outcome | **HOLD_UNRESOLVED.** Preserve the tracked placeholder, but do not add authority-bearing rule source until classification is accepted. |
| Release/publication authority | None. A role match or sensitivity result cannot approve release or publication. |

The proposed [`reviewer_roles.v1.json`](../../decision/reviewer_roles.v1.json)
explicitly assigns no people and records no approval. It is relevant evidence,
not an authority source for this path.

## Current status

| Surface | Confirmed state | Safe interpretation |
|---|---|---|
| README lineage | PR #2679 added a one-newline file; this revision documents the hold | Documentation only. |
| Tracked payload | `.gitkeep` only | Placeholder presence; no implemented policy. |
| Direct references | One atmosphere planning document uses the phrase `policy/role/sensitivity` without defining this leaf | Design lineage, not accepted scope or consumer binding. |
| Rule source and package | Absent | No engine-native behavior exists. |
| Contracts and schemas | No accepted binding to this leaf | Role meaning, authority, sensitivity, and outcomes remain external and unresolved. |
| Fixtures, tests, validator, workflow | Absent for this lane | Validation maturity is M0 placeholder. |
| Runtime and public enforcement | Not established | Any dependent operation must use another accepted governed control or remain held. |

## Current direct-child map

Verified from the tracked tree at the pinned base:

```text
policy/role/sensitivity/
├── .gitkeep
└── README.md
```

Directory Rules prohibit empty symmetry from becoming authority. The map is an
inventory, not an implementation claim.

## What belongs here

Until scope is accepted, only the following belongs here:

- this hold boundary and corrections to its repository-grounded evidence;
- an evidence-backed path decision that classifies the intended role family,
  owner, scope ID, consumers, and canonical target; and
- explicitly authorized migration, retirement, or compatibility material.

If a later decision retains the lane, it may hold declarative composition rules
that consume accepted role and sensitivity references for one operation. Those
rules must not redefine either input family.

## What is prohibited

| Prohibited material or inference | Owning surface or response |
|---|---|
| Role definitions, identity claims, memberships, assignments, or authority intervals | Accepted contracts, schemas, identity/authority registries, and authenticated runtime systems. |
| Sensitivity labels, classifications, protected payloads, or transform evidence | Sensitivity contracts/registries/evidence and [`policy/sensitivity/`](../../sensitivity/README.md) for admissibility rules. |
| Reviewer approval or separation-of-duties records | Governed review record and authority-binding families; a role code is not approval. |
| Source-role truth or source authority | Source contracts and registries; do not collapse source role with caller or reviewer role. |
| Access tokens, credentials, group membership, private endpoints, personal data, exact sensitive locations, DNA, or infrastructure detail | Keep out of Git, fixtures, reasons, logs, and receipts. |
| General RBAC implementation, evaluator, API, UI, cache, or identity provider code | `packages/`, `apps/`, `runtime/`, or infrastructure by responsibility. |
| Evaluated decisions, review records, receipts, proofs, or lifecycle instances | Their accepted process and accountability lanes. |
| Release, correction, withdrawal, rollback, or publication decisions | [`release/`](../../../release/README.md). |

## Inputs and outputs

There are no current policy inputs or outputs because no executable rule exists.

A future accepted rule must receive explicit, versioned context for the operation,
actor or source identity, role-family ID, role authority binding and validity
window, audience, purpose, sensitivity label and transform status, rights,
consent, evidence, lifecycle, review, release candidate, policy bundle, evaluator,
effective time, and correction state. Missing or ambiguous context must not fall
back to allow.

This lane currently outputs documentation only. It creates no role assignment,
sensitivity determination, access grant, `PolicyDecision`, review approval,
receipt, release, or public artifact.

## Exposure, mutation, and retention

| Dimension | Boundary |
|---|---|
| Exposure | Repository-public documentation; proposed operating use is internal and fail-closed. |
| Mutation | Versioned review. New rules and profiles remain held until scope, owner, and dependencies are accepted. |
| Retention | Durable Git history for the placeholder and decisions; no runtime identity or sensitive payload retention. |
| Runtime writes | None. Decisions and audits must never be written beside rule source. |
| Generation | None established. `.gitkeep` and the README do not imply a generator or scaffold family. |

## Lifecycle and trust boundary

| Stage | Required behavior | What this lane cannot do |
|---|---|---|
| Request or candidate intake | Resolve the exact operation, identity, role family, authority, purpose, and sensitivity independently. | Cannot authenticate or assign a role. |
| RAW / WORK / QUARANTINE | Retain prior restrictions and route ambiguity to hold or quarantine. | Cannot clear a lifecycle stage. |
| Review | Require an authorized, current reviewer where the governing policy says so; preserve separation of duties. | Cannot record or self-authenticate approval. |
| Transform / release candidate | Require completed public-safe transforms and all rights, consent, evidence, and rollback dependencies. | Cannot determine transform sufficiency or approve release. |
| PUBLISHED / public interface | Enforce through governed server-side interfaces and released carriers, never client-side labels alone. | Cannot publish, expose, or grant bulk access. |
| Revocation or correction | Stop relying on stale authority or sensitivity state and route dependency-aware correction. | Cannot emit correction or withdrawal records. |

When role meaning, authority, or sensitivity is missing, stale, conflicting,
revoked, or unverifiable, the safe result is hold, deny, restrict, or error—not
implicit permission.

## Validation

Current validation can prove only the documentation and topology boundary:

- the repository topology validator observes that a populated policy boundary
  has a README and detects new structural drift;
- the metadata validator checks a present `KFM_META_BLOCK_V2` structurally;
- the local-link checker validates repository-relative targets and fragments;
- `policy-test` preserves repository-wide evaluator holds but does not execute
  this lane; and
- `make policy` is a TODO echo, not validation.

No current test proves role resolution, authority binding, sensitivity
composition, denial behavior, reviewer separation, runtime enforcement, or
release integration for this directory.

## Contributor guidance

1. Do not infer scope from the path name or the atmosphere planning phrase.
2. Classify `role` explicitly—actor, reviewer, source, service/capability, or
   another registered family—and identify exactly one authority owner.
3. Search for existing contracts, registries, policy paths, consumers, and
   open work before adding a rule; return `SPLIT` if independent role families
   would share one artifact.
4. A dependency-closed implementation needs accepted meaning and shape, stable
   input/output and reason/obligation vocabularies, public-safe fixtures, native
   positive/negative/error tests, evaluator and bundle identity, an authenticated
   consumer, revocation/correction behavior, and rollback.
5. Never put real protected values or plausible authority assignments in
   examples. Use synthetic identifiers that cannot be mistaken for approval.

## Correction and rollback

For a README defect, revert or forward-fix this file. The prior blank blob is
`8b137891791fe96927ad78e64b0aad7bded08bdc`; restoring it removes documentation
only and does not change runtime behavior.

If a future rule or role binding is defective, preserve prior identities and
audit evidence, hold affected operations, revoke stale authority at its owning
system, re-evaluate dependent decisions, invalidate governed caches, and route
release correction or withdrawal through `release/`. Do not rewrite Git history
or roll back into multiple writable role authorities.

## Open verification register

| ID | Open item | Posture |
|---|---|---|
| `ROLE-SEN-001` | Intended meaning of `role` and accepted local scope ID | **HOLD_UNRESOLVED** |
| `ROLE-SEN-002` | Canonical home and contract for role definitions and authority bindings | **NEEDS DECISION** |
| `ROLE-SEN-003` | Relationship to general sensitivity, access, identity, source-role, and reviewer-role policy | **NEEDS POLICY/DIRECTORY REVIEW** |
| `ROLE-SEN-004` | Accepted rule package, outcomes, reasons, obligations, evaluator, bundle, and consumer | **NOT ESTABLISHED** |
| `ROLE-SEN-005` | Revocation, stale-authority, separation-of-duties, correction, and rollback proof | **UNKNOWN / FAIL CLOSED** |
| `ROLE-SEN-006` | Required checks and independent qualified review | **UNKNOWN** |

<p align="right"><a href="#top">Back to top</a></p>
