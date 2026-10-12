<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/identifier-precision-lineage-assessment-source-map
title: Identifier and Precision Lineage Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · Data steward · Geoprivacy steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded mapping from identifier and precision lineage candidates to bounded repository artifacts without treating proposal cards as implementation evidence or authority
truth_posture: CONFIRMED candidate transcription and repository comparison / PROPOSED bounded adaptation pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/common/identifier_precision_lineage_assessment.md
  - ../../kfm_full_atlas_seed_cards.md
  - ./new-ideas-4-16-source-map.md
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, atlas, identifier, precision, crosswalk, source-map]
[/KFM_META_BLOCK_V2] -->

# Identifier and Precision Lineage Assessment Source Map

## Source cards

| Card | Retained proposal | Bounded implementation |
|---|---|---|
| `KFM-TRIAD-034` | Preserve source identity, resolved identity, precision, and transform lineage without collapse. | One fixture-only declaration candidate joining digest-only assertions, a crosswalk outcome, and effective precision. |
| `KFM-CAND-0100` | Keep source identifiers and represent merge, split, surrogate, unresolved, and supersession decisions explicitly. | Source-native assertions remain distinct; the initial profile covers match, ambiguity, unresolved state, and internal supersession links. |
| `KFM-CAND-0101` | Expose source versus resolved identity and effective precision where interpretation changes. | Reviewer-readable summary and exact effective-precision field; no UI or public derivative. |
| `KFM-CAND-0102` | Define identifier, crosswalk, precision-profile, and transform-receipt objects. | One narrow assessment references method/profile/receipt authorities rather than duplicating them. |

The Full Atlas and Drive-derived `New Ideas 4-16-26` source map are candidate evidence, not implementation authority. Raw identifiers, coordinates, and public derivatives are deliberately excluded.

## Repository reconciliation

- `SourceDescriptor` remains source identity and source-role authority.
- Runtime `PrecisionActuallyUsed` remains runtime disclosure; this profile records fixture-declared lineage only.
- Domain identity, geoprivacy, redaction, and release families retain their existing responsibilities.
- Repository search at base `9e76413313b8529091d01be6132d6e987e3f9fae` found domain-specific identifier and precision artifacts but no common `IdentifierAssertion`, `CrosswalkResolution`, `PrecisionProfile`, or `PrecisionTransformReceipt` assessment family outside proposal material.

## Path decision

```yaml
path_decision:
  artifact: IdentifierPrecisionLineageAssessmentCandidate
  proposed_path: contracts/common/identifier_precision_lineage_assessment.md
  artifact_kind: semantic contract
  authority_owner: shared identifier and precision lineage declaration
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: object_family
  scope_id: identifier-precision-lineage
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/kfm_full_atlas_seed_cards.md
    - docs/intake/exploratory/new-ideas-4-16-source-map.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-AUTHROOT-001
    - DIR-SCOPELANE-004
    - DIR-DEP-001
  outcome: PLACE
```

## Non-effects

This packet does not store raw identifiers or coordinates, resolve identity, query sources, perform a geometry transform, authenticate evidence or review, change source roles, evaluate policy, approve redaction, promote, release, deploy, publish, or authorize public use.
