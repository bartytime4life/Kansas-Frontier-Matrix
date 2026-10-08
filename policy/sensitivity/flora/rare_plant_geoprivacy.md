<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy/sensitivity/flora/rare_plant_geoprivacy
title: "Rare-plant geoprivacy review"
type: policy-review-guide
version: v1.0-draft
status: draft; review-guidance; evaluator-unbound
owners: ["@bartytime4life via CODEOWNERS; specialist review unassigned"]
created: 2026-10-08
created_note: First substantive guide edition; the path predates this update.
updated: 2026-10-08
policy_label: public; review-guidance
owning_root: policy/
responsibility: "Explain the review packet and evidence boundaries for rare-plant geoprivacy review."
truth_posture: PROPOSED guidance; repository-grounded guidance at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no terms approval, active rule or release decision.
related:
  - docs/domains/flora/CANONICAL_PATHS.md
  - policy/README.md
[/KFM_META_BLOCK_V2] -->

# Rare-plant geoprivacy review

Draft review guidance, 2026-10-08. Source terms, individual decisions and enforcement must be established for the exact candidate.

## Preserve the original restriction

Treat the exact location and associated identifying context as a review boundary. Preserve provider privacy and uncertainty flags. Do not infer that a record is public-safe because a map marker can be drawn or because the source is accessible.

## Build the review packet

Record source/product identity, record class, observation/valid time, native spatial precision, intended audience and proposed representation. Identify all location-bearing fields, including locality text, media metadata and identifiers that can resolve to a precise external record. Describe the transform and how its lineage will remain inspectable without exposing the restricted original.

## Required checks

A permitted generalized representation must be evaluated across tiles, API/detail payloads, popup text, exports and generated explanation. Check joins that could reverse the intended coarsening. Use synthetic locations and labels in fixtures. Do not choose an arbitrary radius or public tier in place of a source- and purpose-specific decision.

## Current implementation boundary

The adjacent `rare_plant_geoprivacy.rego` and `exact_geometry_deny.rego` are default-only proposed files at the pinned source snapshot. Their presence is not evidence of an enforced transform. Completion requires accepted semantics, meaningful positive/negative cases, evaluator/consumer binding and the required review record. Changed precision, source restriction, audience or join purpose triggers renewed assessment.

## Owning references

- [CANONICAL_PATHS.md](../../../docs/domains/flora/CANONICAL_PATHS.md)
- [README.md](../../README.md)
- [README.md](../README.md)
- [SENSITIVITY_ESCALATION.md](../../../docs/runbooks/SENSITIVITY_ESCALATION.md)
