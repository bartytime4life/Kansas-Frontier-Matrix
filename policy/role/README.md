<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-role-readme
title: policy/role/ — Unresolved Role-Policy Routing Boundary
type: readme
version: v0.1.0
status: draft; repository-grounded; routing-and-hold boundary; scope-unresolved; inactive; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy/ to @bartytime4life; no accepted role-policy steward or independent approver was established
created: 2026-08-28
updated: 2026-08-28
current_path: policy/role/README.md
owning_root: policy/
policy_label: internal; policy; role; routing; hold; non-release; non-publication
responsibility: Route the unresolved role-policy namespace and its sensitivity child without defining role semantics, assigning authority, evaluating policy, approving release, or publishing.
base_commit: e52165e820b07e65c54830fde519a9c90df8eb1c
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED one direct sensitivity child with a substantive hold README and no executable rule, contract binding, schema, fixture, test, validator, bundle, evaluator, consumer, decision record, or release integration / PROPOSED narrow routing boundary only / HOLD role-family meaning, canonical scope, owner, package, evaluator, consumer, and path-retention decisions / UNKNOWN whether role means actor, reviewer, source, service capability, or another governed family
related:
  - ../README.md
  - ./sensitivity/README.md
  - ../sensitivity/README.md
  - ../decision/README.md
  - ../review/README.md
  - ../decision/reviewer_roles.v1.json
  - ../../contracts/governance/review_authority_binding.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../release/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: role

> **One-line purpose.** `policy/role/` is a routing-and-hold boundary for an
> unresolved policy namespace; it documents the existing
> [`sensitivity/` child](./sensitivity/README.md) without defining a role,
> granting authority, or activating policy.

> [!IMPORTANT]
> **Safe current conclusion at `main@e52165e820b0`:** this directory
> contains only this README and the `sensitivity/` child. The child contains
> only `.gitkeep` and its hold README. No executable rule, accepted role
> contract, schema binding, fixture, test, validator, bundle, evaluator,
> consumer, decision record, release integration, or publication path is
> established.

> [!CAUTION]
> The path name does not identify which role family it means. KFM separately
> discusses actors, reviewers, sources, services or capabilities, and evidence
> roles. These families must not be collapsed or treated as interchangeable
> authority.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-scope) · [Inventory](#current-inventory) · [Belongs](#what-belongs-here) · [Prohibited](#what-does-not-belong-here) · [Validation](#validation) · [Correction](#correction-and-rollback) · [Open work](#open-verification-register)

## Purpose

This README makes the current boundary navigable and prevents a blank parent
from being mistaken for an implemented role-policy family. The only current
child is a documented hold around a possible composition of an already-defined
role with an independently determined sensitivity posture.

That prospective composition remains **PROPOSED**. The repository does not
establish which role family belongs here, whether this path should remain, or
which governed consumer could rely on it.

## Authority and scope

| Field | Current boundary |
|---|---|
| Parent authority | [`policy/`](../README.md), the canonical admissibility-rule root under accepted Directory Rules placement. |
| Local authority | Routing and documentation only. This README does not create role semantics, assignments, reviewer authority, or access rights. |
| Current child | [`sensitivity/`](./sensitivity/README.md), an inactive `HOLD_UNRESOLVED` leaf. |
| Related sensitivity policy | [`policy/sensitivity/`](../sensitivity/README.md) owns sensitivity admissibility rules; this lane must not redefine labels or classification. |
| Related decisions and review | [`policy/decision/`](../decision/README.md) and [`policy/review/`](../review/README.md) document separate decision and review boundaries. |
| Placement basis | [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../docs/doctrine/directory-rules.md) place policy source under `policy/`; they do not accept this lane's meaning. |
| Owner and scope ID | **NEEDS VERIFICATION.** CODEOWNERS routing is not accepted stewardship or approval authority. |
| Current placement outcome | **HOLD_UNRESOLVED.** Preserve the tracked path and document it; do not add authority-bearing rules until classification is accepted. |
| Release/publication authority | None. Role membership or a policy result cannot approve release or publication. |

The proposed [reviewer-role registry](../decision/reviewer_roles.v1.json) assigns
no people and records no approval. The
[review-authority binding contract](../../contracts/governance/review_authority_binding.md)
is related evidence, not proof that this namespace owns reviewer roles.

## Current inventory

Verified from the tracked tree at the pinned base:

```text
policy/role/
├── README.md
└── sensitivity/
    ├── .gitkeep
    └── README.md
```

| Surface | Confirmed state | Safe interpretation |
|---|---|---|
| Parent README | This routing-and-hold boundary | Documentation only; no rule activation. |
| Direct child | One substantive hold README under `sensitivity/` | The child records uncertainty rather than implementing a control. |
| Rule source and package | Absent | No engine-native behavior exists. |
| Contracts and schemas | No accepted binding to this path | Role meaning, authority, sensitivity, and outcomes remain external and unresolved. |
| Fixtures, tests, validator, workflow | Absent for this lane | Validation maturity remains placeholder-level. |
| Runtime consumer | Not established | Dependent operations must use another accepted governed control or remain held. |

Directory presence and a substantive README prove navigation and boundary
documentation only. They do not prove implementation maturity.

## What belongs here

Until scope is accepted, only the following belongs here:

- this routing boundary and repository-grounded corrections;
- documentation for the existing child hold;
- an evidence-backed decision that identifies one role family, owner, scope ID,
  canonical path, consumers, and migration or retirement outcome; and
- explicitly authorized compatibility or rollback material.

If a later accepted decision retains the lane, policy source here must consume
accepted role and authority references. It must not define identities,
memberships, reviewer assignments, source roles, or sensitivity labels.

## What does not belong here

| Prohibited material or inference | Owning surface or response |
|---|---|
| Role definitions, memberships, assignments, credentials, or authority intervals | Accepted contracts, schemas, identity or authority registries, and authenticated runtime systems. |
| Sensitivity labels, classifications, protected payloads, or transform evidence | Sensitivity contracts, registries, evidence, and [`policy/sensitivity/`](../sensitivity/README.md) for admissibility. |
| Reviewer approval or separation-of-duties evidence | Governed review records and authority bindings; a role code is not approval. |
| Source-role or evidence-role truth | Source and evidence authority lanes; do not collapse them into actor or reviewer roles. |
| General RBAC implementation, evaluator, API, UI, cache, or identity-provider code | `packages/`, `apps/`, `runtime/`, or infrastructure by responsibility. |
| Decisions, receipts, proofs, lifecycle instances, release records, or public artifacts | Their accepted process and accountability roots. |
| Real identities, access tokens, group membership, personal data, exact sensitive locations, or protected infrastructure details | Keep out of Git, fixtures, reasons, logs, and receipts. |

## Inputs, outputs, and failure posture

This lane currently has no executable inputs or outputs. It creates no role
assignment, access grant, `PolicyDecision`, review approval, receipt, release,
or public artifact.

A future accepted rule would need explicit, versioned context for the bounded
operation, authenticated subject or source reference, role-family identity,
authority binding and validity interval, audience, purpose, sensitivity and
transform state, rights, consent, evidence, lifecycle, review, release
candidate, policy bundle, evaluator, effective time, revocation, and correction.
Missing, stale, conflicting, revoked, or unverifiable context must fail closed
to hold, deny, restrict, abstain, or error as the accepted policy specifies.

## Validation

Current validation can prove only documentation and topology:

```bash
python tools/validators/docs/link-check/check_links.py policy/role/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required policy/role/README.md
python tools/validators/docs/fragments/check_fragments.py policy/role/README.md
```

These commands do not prove role resolution, authority binding, sensitivity
composition, reviewer separation, runtime enforcement, release, or publication.
The repository-wide `make policy` target remains TODO-only and is not a general
policy evaluator.

## Contributor guidance

1. Classify `role` explicitly before adding policy source.
2. Identify exactly one authority owner and stable scope ID.
3. Reconcile existing actor, reviewer, source, service-capability, and evidence
   role surfaces before choosing `PLACE`, `SPLIT`, `MIGRATE`, or `DENY`.
4. Require accepted contracts, schemas, public-safe fixtures, positive and
   negative tests, evaluator and bundle identity, authenticated consumers,
   revocation and correction behavior, and rollback before activation.
5. Never use plausible real identities or authority assignments in examples.

## Correction and rollback

For a documentation defect, revert or forward-fix this file and the directly
affected parent or child navigation. The prior blank blob is
`8b137891791fe96927ad78e64b0aad7bded08bdc`; restoring it removes documentation only and does not change
runtime behavior.

A future defective role rule or binding must be held and corrected through its
owning authority system. Preserve prior identities and audit evidence, revoke
stale authority, re-evaluate dependent decisions, and route release correction
through [`release/`](../../release/README.md). Do not rewrite Git history or
create parallel writable role authorities.

## Open verification register

| ID | Open item | Posture |
|---|---|---|
| `ROLE-001` | Intended role family and accepted local scope ID | **HOLD_UNRESOLVED** |
| `ROLE-002` | Canonical role-definition and authority-binding homes | **NEEDS DECISION** |
| `ROLE-003` | Relationship to reviewer, source, service-capability, evidence, access, identity, and sensitivity policy | **NEEDS POLICY/DIRECTORY REVIEW** |
| `ROLE-004` | Rule package, outcomes, reasons, obligations, evaluator, bundle, and consumer | **NOT ESTABLISHED** |
| `ROLE-005` | Revocation, stale-authority, separation-of-duties, correction, and rollback proof | **UNKNOWN / FAIL CLOSED** |
| `ROLE-006` | Required checks and independent qualified review | **UNKNOWN** |

<p align="right"><a href="#top">Back to top</a></p>
