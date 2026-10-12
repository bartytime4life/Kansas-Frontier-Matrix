<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/domain-context-map-assessment
title: Domain Context Map Assessment Candidate
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-pending; non-authoritative
owners: OWNER_TBD — Architecture steward · Domain stewards · Evidence steward · Sensitivity steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; governance; domain-context-map; fixture-only
owning_root: contracts/
responsibility: Define the semantic meaning and fail-closed validation boundary of a fixture-only DDD context-map proposal bound to existing KFM domain-lane and cross-domain-seam projections.
truth_posture: CONFIRMED source and repository projection review / PROPOSED mapping candidate / UNKNOWN adopted relationship patterns / NEEDS VERIFICATION domain and architecture review
related:
  - ../../control_plane/domain_lane_register.yaml
  - ../../control_plane/cross_domain_seam_register.yaml
  - ../../schemas/contracts/v1/governance/domain_context_map_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/domain_context_map_assessment/cases.json
  - ../../tools/validators/governance/validate_domain_context_map_assessment.py
  - ../../tests/validators/governance/test_validate_domain_context_map_assessment.py
  - ../../docs/intake/exploratory/domain-context-map-assessment-source-map.md
tags: [kfm, governance, ddd, bounded-context, context-map, cross-domain, fixture-only]
notes:
  - "The profile validates a proposed interpretation only; it does not modify either control-plane register or authorize a cross-domain join."
  - "DDD relationship names are reference language adapted to KFM's stricter evidence, sensitivity, policy, and release boundaries."
[/KFM_META_BLOCK_V2] -->

# Domain Context Map Assessment Candidate

> A deterministic, fixture-only proposal for describing how two or more registered KFM domain lanes may relate at one already-declared cross-domain seam without collapsing their models, evidence, source roles, sensitivity, policy, or release authority.

## Purpose and status

The Full Atlas seed corpus proposes treating KFM domains as Domain-Driven Design bounded contexts and making their relationships explicit through a context map. The repository already has a `Domain Lane Register` and a partial `Cross-Domain Seam Register`; those projections remain the current repository evidence and are not replaced here.

This contract adds only a **candidate assessment shape**. A positive result means that one proposed DDD relationship label is internally coherent with the existing lane and seam projections. It does not establish that the label is architecturally correct, accepted, implemented, or permitted for runtime use.

| Field | Value |
|---|---|
| Profile | `kfm.governance.domain-context-map-assessment.fixture.v1` |
| Input posture | Synthetic, local, no-network |
| Positive outcome | `PASS` with `assessment_state: REVIEW_REQUIRED` |
| Unresolved outcome | `ABSTAIN` |
| Authority effect | None |

## Relationship vocabulary

The allowed labels are reference-language patterns from the attached Domain-Driven Design reference:

- `PARTNERSHIP`
- `SHARED_KERNEL`
- `CUSTOMER_SUPPLIER`
- `CONFORMIST`
- `ANTICORRUPTION_LAYER`
- `OPEN_HOST_SERVICE`
- `PUBLISHED_LANGUAGE`
- `SEPARATE_WAYS`
- `UNRESOLVED`

The label is descriptive and proposal-only. It does not create a shared kernel, API, translation layer, dependency, data flow, import, mutation right, or public join.

Directional patterns (`CUSTOMER_SUPPLIER`, `CONFORMIST`, `ANTICORRUPTION_LAYER`, and `OPEN_HOST_SERVICE`) require distinct upstream and downstream registered participants. Symmetric or non-directional patterns do not carry directional fields. `UNRESOLVED` returns `ABSTAIN` and preserves the seam's existing hold posture.

## Preserved KFM controls

Every candidate fixes these controls:

- each participating lane must retain its own EvidenceBundle support;
- source roles remain distinct;
- the most restrictive sensitivity and policy posture controls;
- every participant requires its own released state before any public composition;
- mutation, lifecycle writes, register writes, release, publication, and public use remain false; and
- the existing seam's participant set must match exactly.

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | Shape, identity, participant binding, relationship semantics, and KFM controls are locally coherent. | Still `REVIEW_REQUIRED`; no relationship is adopted. |
| `ABSTAIN` | The proposed DDD relationship remains explicitly unresolved. | No fallback relationship is inferred. |
| `DENY` | Participant, seam, direction, ordering, identity, or control semantics conflict. | No join or register mutation occurs. |
| `ERROR` | The candidate or required projection cannot be safely parsed. | No partial result is trusted. |

## Directory Rules basis

The candidate's semantic meaning is cross-domain governance, so it belongs under `contracts/governance/`. Its machine shape, synthetic cases, validator, tests, workflow, source adaptation, and authoring provenance remain in their established responsibility roots. The canonical machine projections remain under `control_plane/` and are read-only inputs.

No new root, domain lane, seam register, policy home, evidence home, lifecycle store, or release home is created.

## Non-effects and rollback

A green result does not:

- create, rename, remove, merge, or accept a domain lane;
- create or amend a cross-domain seam;
- authorize a join, import, mutation, inference, or shared storage model;
- lower sensitivity, precision, policy, evidence, or release requirements;
- resolve evidence or decide policy or review;
- promote, release, deploy, publish, or authorize public use.

Rollback is one additive commit revert. Because the profile is fixture-only, no register, source, data, release, deployment, or public state requires restoration.
