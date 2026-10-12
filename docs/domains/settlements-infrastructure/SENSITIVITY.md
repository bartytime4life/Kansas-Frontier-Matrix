<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/settlements-infrastructure/sensitivity
title: Settlements and Infrastructure - Sensitivity Review Guide
type: domain-guide
version: v0.1
status: draft; repository-grounded; documentation-only; review-required
owners: NEEDS VERIFICATION - domain and documentation stewardship
created: 2026-10-08
created_note: Date of this substantive documentation edition; the tracked path existed earlier.
updated: 2026-10-08
policy_label: repository-facing; cite-or-abstain; no-operational-approval
owning_root: docs/
responsibility: Explain sensitivity-review prerequisites and safe handoff boundaries for settlements and infrastructure without deciding policy, choosing transforms, or approving release.
truth_posture: CONFIRMED pinned repository inventory and source inspection; PROPOSED review-required documentation guide; NEEDS VERIFICATION accountable stewardship and operational acceptance
evidence_snapshot: main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
related:
  - docs/domains/settlements-infrastructure/README.md
  - docs/domains/settlements-infrastructure/DENY_BY_DEFAULT.md
  - policy/release/settlements-infrastructure/asset_clustering.rego
  - docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Settlements and Infrastructure — Sensitivity Review Guide

Use this guide to decide what evidence and accountable review a proposed settlement or infrastructure representation needs before it can be considered for public use. It explains the lane's existing [deny-by-default guidance](DENY_BY_DEFAULT.md); it does not make a policy decision or choose a supposedly safe generalization distance.

## Current implementation boundary

At `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`:

- The [asset-clustering policy file](../../../policy/release/settlements-infrastructure/asset_clustering.rego) contains only its package declaration, explanatory comment and `default allow := false`. It is not a completed clustering or geoprivacy implementation.
- The [restricted-geometry test](../../../tests/domains/settlements-infrastructure/test_restricted_geometry_no_leak.py) is a comment-only test placeholder; its path is not executable no-leak proof.
- The [validator index](../../../tools/validators/domains/settlements-infrastructure/README.md) describes a bounded identity-envelope candidate. Identity conformance does not establish source rights, infrastructure sensitivity, public geometry or release eligibility.
- The draft deny register records competing policy-home proposals. This documentation edition does not resolve that placement question or accept an ADR.

These findings leave operational sensitivity clearance **HOLD** wherever a material policy or review requirement is unresolved.

## Review the representation, not just the dataset name

| Proposed information | Review question | Retained boundary |
|---|---|---|
| Census place geometry and counts | Which vintage and statistical unit are represented? Could small-area joins identify protected people or assets? | Census geography is not municipal legal-status authority. |
| Municipality, townsite or historical place | What source supports the name, identity and valid interval? Does the record expose culturally sensitive context? | A historical location hypothesis is not a current legal boundary. |
| Facility or service-area outline | Is the geometry public-safe at the proposed scale and for this audience? | Public availability alone does not approve KFM reuse or precision. |
| Operator or condition observation | Are identity, observation time, use rights and exposure authorized? | Condition data cannot be presented as current without applicable evidence. |
| Asset dependency or network relation | Can the combination expose critical nodes, vulnerabilities or continuity-sensitive relationships? | Hold unresolved sensitive dependencies out of public carriers. |
| Cross-domain join | Does a parcel, access route, date or neighboring layer reconstruct withheld detail? | A generalized single layer may still reveal too much after joining. |

The [source guide](SOURCE_FAMILIES.md) and [identity model](IDENTITY_MODEL.md) supply the domain distinctions. Do not copy protected coordinates, vulnerability details, access routes, credentials or private-person identifiers into public review artifacts.

## Review procedure

1. Pin the candidate's source/version, opaque identity, intended audience, output fields, map scale and use case.
2. Record source role, rights, provenance and time semantics separately. Retain the provider's restrictions and unknowns.
3. Identify the relevant sensitivity question without reproducing protected values in the handoff.
4. Trace the owning policy, policy version, reviewer authority and required evidence. If a rule or owner is missing, retain a hold and name the missing prerequisite.
5. Evaluate the proposed representation together with its likely joins, exports, search results and map inspection behavior.
6. Where a transformation is proposed, require its approved method, reproducibility, source linkage and accountable review. Do not invent a threshold in documentation.
7. Route any eligible successor through the owning evidence and release process. Preserve the original and restricted material in its authorized lane.

## Finite handoff outcomes

**Ready for accountable review** means the packet can be reviewed; it is not release approval. **HOLD** means a required authority or fact is missing. **DENY** records a supported prohibited representation. **ABSTAIN** means the available evidence cannot support the requested claim. **ERROR** records a processing or validation failure. Use the owning contract's exact machine vocabulary when emitting machine objects.

The public-safe handoff should include repository pin, opaque candidate identity, role and sensitivity labels, relevant policy references, bounded validation result, unresolved items, reviewer role still required, and correction route. Omit the protected value that motivated the review.

## Validation and correction

A future executable no-leak test should exercise geometry, attributes, joins, logs, errors and exports with synthetic protected values and positive/negative expectations. This guide records no new test run and grants no test waiver.

If sensitive material has already reached a public carrier, use the owning incident, withdrawal and correction procedures; changing this Markdown file does not withdraw data. A documentation rollback restores the prior file while preserving subsequent legitimate source and review records.

Related: [domain overview](README.md), [API boundary](API_CONTRACTS.md), [source registry](SOURCE_REGISTRY.md), [release root](../../../release/README.md).
