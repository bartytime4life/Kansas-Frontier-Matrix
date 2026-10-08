<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/rangepolygon
title: Plant range geometry review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Plant range geometry review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/range_polygon.md
  - schemas/contracts/v1/domains/flora/range_polygon.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Rangepolygon

This retained CamelCase path is a draft compatibility and review guide for
`RangePolygon`. The existing [range_polygon semantic contract](range_polygon.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A RangePolygon carries a bounded spatial claim about a Flora subject. It may be compiled, observed-supported, modeled, historical, administrative, aggregate or a public derivative.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Subject | Bind taxon/Flora subject and source-native name through reviewed mapping. |
| Range class and role | Keep observed support, modeled range and administrative extent distinct. |
| Geometry | Reference internal geometry and any public derivative separately; preserve CRS, scale and topology method. |
| Evidence | Bind supporting occurrences, specimens, surveys, models or lists and their versions. |
| Time/uncertainty | Retain historical/current interval, coverage limits and uncertainty. |
| Exposure and correction | Review sensitive inference, release audience, supersession and rollback. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic modeled range is shown at its declared support scale with source/model version and uncertainty, without claiming every location is occupied.

**Invalid claim:** A polygon boundary is treated as surveyed presence at each point or outside the polygon is presented as biological absence.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

A polygon is a claim carrier, not direct occurrence evidence. Masking or clipping does not automatically settle sensitivity or source rights.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/range_polygon.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

The architecture retains RangePolygon/DistributionSurface naming conflict and additional .flora schema lineage. Resolve exact binding and compatibility before activating a renderer or validator.

## Review and maintenance handoff

For a proposed implementation, pin this guide, the detailed contract, schema and
consumer revisions. Record exact source support, proposed shape, positive and
negative cases, failure outcomes, reviewer roles and rollback before wiring
runtime use. Names remain `OWNER_TBD`; documentation cannot supply approval.

Preserve this path and heading while inbound references remain. Any consolidation
or migration must update consumers and retain lineage under the adopted
[Directory Rules](../../../docs/doctrine/directory-rules.md). Related context:
[Flora object families](../../../docs/domains/flora/OBJECT_FAMILIES.md) and
[verification backlog](../../../docs/domains/flora/VERIFICATION_BACKLOG.md).
