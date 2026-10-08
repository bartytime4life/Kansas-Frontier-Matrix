<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/settlements-infrastructure/source-families
title: Settlements and Infrastructure - Source Families
type: source-guide
version: v0.1
status: draft; repository-grounded; documentation-only; review-required
owners: NEEDS VERIFICATION - domain and documentation stewardship
created: 2026-10-08
created_note: Date of this substantive documentation edition; the tracked path existed earlier.
updated: 2026-10-08
policy_label: repository-facing; cite-or-abstain; no-operational-approval
owning_root: docs/
responsibility: Guide source-family selection and candidate intake while preserving source roles, vintage, rights, sensitivity, domain ownership, and admission boundaries.
truth_posture: CONFIRMED pinned repository inventory and source inspection; PROPOSED review-required documentation guide; NEEDS VERIFICATION accountable stewardship and operational acceptance
evidence_snapshot: main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
related:
  - docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md
  - docs/domains/settlements-infrastructure/EXPANSION_PLAN.md
  - docs/domains/settlements-infrastructure/SENSITIVITY.md
  - docs/sources/README.md
[/KFM_META_BLOCK_V2] -->

# Settlements and Infrastructure — Source Families

Use this page to select evidence appropriate to a settlement, municipality, historic place, facility, operator or service-area question. It organizes the families already described in the [domain source registry](SOURCE_REGISTRY.md). A family is a discovery aid; it does not admit every provider, establish current terms or activate a connector.

## Choose a family by the claim

| Source family | Useful questions | Required distinctions |
|---|---|---|
| Census TIGER and census-place products | Where is a statistical place in a named vintage, and which geography supports aggregate statistics? | Census place, municipality and community identity are separate; join counts to the declared vintage. |
| GNIS and other gazetteers | Which place name and feature identity does the source record? | A name record alone does not prove legal status, occupancy or current facility operation. |
| State and local GIS | What geometry or administrative attribute does the named publisher provide? | Record item/layer identity, publisher, edition, rights and scale; a portal is not blanket authority. |
| Municipal and local legal records | What incorporation, annexation, dissolution or status event is documented? | Administrative events need valid dates and exact source support, not inference from a map label. |
| Historical gazetteers and maps | What place or feature is represented in that source edition? | Preserve uncertainty, georeferencing and source age; a hypothesis remains a candidate. |
| Infrastructure operators and providers | What asset, operator, service or condition is recorded? | Preserve use restrictions, observation time and sensitive dependencies; do not expose precise critical detail by default. |
| KDOT, bridge and facility sources | How does a facility relate to a transport system? | Facility identity and route/network identity keep their owning lanes; a joined record does not transfer authority. |
| FEMA and hazard/resilience sources | What designated zone, declaration or hazard context relates to the place? | Regulatory designation, modeled risk, event observation and official warning are different roles. |

These are repository-documented families, not a fresh provider availability or license audit. Use exact provider records and current source terms for a real intake.

## Minimum candidate packet

Record the provider and dataset/item identifiers, exact source URL or original-file identity, requested Kansas extent, object family, source role, edition, observation/valid/publication/retrieval times, units, CRS and applicable vertical reference, declared size or selected maximum, rights, sensitivity, processing and exclusions.

Retain source-native names and IDs alongside any normalized identity. If a date, datum or license is unknown, say which field is unknown and what evidence would resolve it. Do not turn retrieval time into observation time or a selected transfer maximum into measured size.

Machine fields belong to the actual source-descriptor schema and contract. This checklist is a human review aid, not an alternate schema.

## Source-role checks

- An administrative record is not a direct observation merely because it has coordinates.
- An aggregate describes its stated geographic and temporal unit; it does not establish every individual facility's condition.
- A model needs its inputs, method/version and interpretation limits.
- A candidate stays pending until its governing review supports a later state.
- A synthetic reconstruction must be labeled as such and cannot substitute for surveyed or historical evidence.
- A regulatory layer retains its legal/designation role; it is not an observed event.

Refer to the source registry's role discussion, then use the current owning contract vocabulary for machine objects. A convenience display label cannot silently widen a source's role.

## Work a bounded intake

1. State one question and the smallest source slice that can answer it.
2. Choose an individual product from the appropriate family; pin its source edition and expected output.
3. Review rights and [sensitivity](SENSITIVITY.md), including risks introduced by joining otherwise public fields.
4. Preserve the original capture and record any normalization or generalization separately.
5. Validate identity, geometry and object-family constraints using the actual applicable checks. Named test files must be inspected: the current [Census-versus-municipality file](../../../tests/domains/settlements-infrastructure/test_census_vs_municipality.py) is comment-only, not a passing executable test.
6. Record the candidate's actual next gate. Source discovery, capture, conformance, review, activation and release remain separate.

## Domain handoffs

[Roads/Rail/Trade](../roads-rail-trade/README.md) owns transport-route meaning; [Hydrology](../hydrology/README.md) owns water observations; [Hazards](../hazards/README.md) owns hazard-event context; [People/DNA/Land](../people-dna-land/README.md) owns living-person and ownership concerns. Preserve each lane's source/evidence references when joining.

## Maintenance and open review

Revisit this guide when a family is added, a provider changes identity or access conditions, source roles change, or an actual candidate reveals a missing boundary. Accountable source and domain stewardship remain to be verified. This edition replaces an empty explanation at the same path; it creates no operational registry entry and changes no source status.
