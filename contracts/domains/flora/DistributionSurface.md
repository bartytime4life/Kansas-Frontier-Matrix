<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/distributionsurface
title: Flora distribution surface naming and review guide
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Flora distribution surface naming and review guide; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/range_polygon.md
  - contracts/domains/flora/usda_plants_distribution_snapshot.md
  - schemas/contracts/v1/domains/flora/distribution_surface.flora.schema.json
  - docs/domains/flora/ARCHITECTURE.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Distributionsurface

This retained path explains the `DistributionSurface` name and its relationship
to the existing [RangePolygon semantic contract](range_polygon.md). It is a
proposed review guide, not an accepted second range/distribution authority.

## Meaning and naming evidence

The [Flora architecture](../../../docs/domains/flora/ARCHITECTURE.md) records
`RangePolygon / DistributionSurface` as modeled or aggregated distribution
support, distinct from raw occurrences, and marks naming as conflicted pending
ADR reconciliation. The [object-family guide](../../../docs/domains/flora/OBJECT_FAMILIES.md)
proposes folding the earlier DistributionSurface family into RangePolygon.
Those statements are planning lineage, not evidence of a completed migration.

The [distribution schema](../../../schemas/contracts/v1/domains/flora/distribution_surface.flora.schema.json)
is a proposed open object with empty properties. Its metadata names
`contracts/domains/flora/distribution_surface.flora.md`, which is absent at the
pinned revision. This document preserves the observed gap without creating a
new path or modifying the schema binding.

## Required semantic review

A distribution representation must preserve:

| Dimension | Meaning |
|---|---|
| Subject | Taxon or other Flora subject plus source-name/crosswalk evidence |
| Role | Observed aggregation, administrative distribution, model or other qualified basis |
| Spatial support | Grid/county/polygon resolution, extent, projection and source method |
| Value semantics | Presence claim, suitability, probability, count or other exact quantity |
| Missingness | Not reported, not evaluated and reported absence remain distinct |
| Time | Source edition, represented period, model vintage and retrieval time |
| Uncertainty | Input gaps, model limitations, coverage and aggregation assumptions |
| Governance | Evidence, rights, sensitivity, review, correction and intended audience |

This table is proposed semantic review guidance. The permissive distribution
schema does not enforce it or define a safe public carrier.

## Existing bounded distribution profile

The [USDA PLANTS distribution snapshot contract](usda_plants_distribution_snapshot.md)
and [schema](../../../schemas/contracts/v1/domains/flora/usda_plants_distribution_snapshot.schema.json)
are a separate strict, fixture-only administrative county/taxon profile. They
separate `reported_present`, `reported_absent`, `not_reported` and `not_evaluated`.
The missing-row policy is `NO_SOURCE_ROW_IS_NO_CLAIM_NOT_ABSENCE`; `first_observed`
is null and release remains held. This implementation cannot be generalized to
all distribution surfaces merely because the names are related.

## Examples and invariants

**Coherent synthetic candidate:** a county/taxon distribution retains an explicit
administrative presence claim and source row, while unreported counties remain
no-claim. It makes no point occurrence or first-observation assertion.

**Invalid claim:** a missing source row becomes species absence, or a modeled
suitability raster is displayed as observed occurrence density without its method,
units and support being disclosed.

A range outline or raster cell cannot establish that a species occupies every
location inside it. Neither a fine display zoom nor resampling creates better
source resolution. Source and sensitivity reviews also apply to inferred range
for rare plants and to joins that could expose their locality.

## Completion and migration gaps

Before treating this name as an executable contract, resolve the RangePolygon
relationship, chosen schema and missing schema metadata target through reviewed
placement and compatibility work. Inventory consumers of both names, then bind
closed fields, quantity/missingness semantics, positive/negative fixtures and
validator outcomes. Preserve existing identifiers until a migration is accepted.

Revert a mistaken documentation change without claiming that datasets or public
surfaces were rolled back. Any source, catalog, release or public correction
remains a separately evidenced operation. This guide settles navigation and
review questions only; it does not accept the proposed consolidation.
