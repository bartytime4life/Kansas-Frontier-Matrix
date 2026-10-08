<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy/sensitivity/flora/README
title: "Flora sensitivity review boundary"
type: policy-review-guide
version: v1.0-draft
status: draft; review-guidance; evaluator-unbound
owners: ["@bartytime4life via CODEOWNERS; specialist review unassigned"]
created: 2026-10-08
created_note: First substantive guide edition; the path predates this update.
updated: 2026-10-08
policy_label: public; review-guidance
owning_root: policy/
responsibility: "Explain the review packet and evidence boundaries for flora sensitivity review boundary."
truth_posture: PROPOSED guidance; repository-grounded guidance at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no terms approval, active rule or release decision.
related:
  - docs/domains/flora/CANONICAL_PATHS.md
  - policy/README.md
[/KFM_META_BLOCK_V2] -->

# Flora sensitivity review boundary

Draft review guidance, 2026-10-08. Source terms, individual decisions and enforcement must be established for the exact candidate.

## Current lane

The four local Rego files cover cultural sensitivity, exact geometry, join-induced sensitivity and rare-plant geoprivacy. At the pinned source snapshot they contain `default allow := false` without substantive decision bodies. This guide explains review work; it does not turn those rule declarations into an implemented policy service.

## What a packet must describe

Identify the selected taxon/record, source rights, location representation, proposed audience and intended action. Include map, detail view, export, citation, media and join behavior. Keep taxonomic confidence, observation quality and sensitivity as separate dimensions.

Use [rare-plant geoprivacy](rare_plant_geoprivacy.md) for exact-location handling and [join sensitivity](plants_join_sensitivity.md) when combining records. Preserve source privacy flags and transformation lineage instead of replacing them with a generic public label.

## Review outcomes

A reviewer may require omission, restriction, generalization or further evidence under the owning policy. Record the actual disposition and its scope; do not invent a numeric privacy radius or assign an unverified sensitivity tier. No live sensitive coordinates belong in public examples or fixtures.

## Implementation acceptance

Before reporting enforcement, establish the accepted inputs/outcomes, rule tests with meaningful negative cases, bundle identity, evaluator binding and the consumer path that applies the result. Then verify every output representation. A default declaration, passing parser, synthetic helper or this completed guide cannot establish that chain alone.

## Owning references

- [CANONICAL_PATHS.md](../../../docs/domains/flora/CANONICAL_PATHS.md)
- [README.md](../../README.md)
- [README.md](../README.md)
- [SENSITIVITY_ESCALATION.md](../../../docs/runbooks/SENSITIVITY_ESCALATION.md)
