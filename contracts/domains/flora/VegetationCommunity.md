<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/vegetationcommunity
title: Vegetation community classification review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Vegetation community classification review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/vegetation_community.md
  - schemas/contracts/v1/domains/flora/vegetation_community.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Vegetationcommunity

This retained CamelCase path is a draft compatibility and review guide for
`VegetationCommunity`. The existing [vegetation_community semantic contract](vegetation_community.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A VegetationCommunity records a source-bound community or plant-cover classification at a declared support. It can describe a mapped polygon, plot, transect, aggregate, remote-sensing class, model or restoration target.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Classification | Preserve source label, classification system and exact version. |
| Record class | Separate observed survey, remote-sensing/model class and proposed restoration target. |
| Composition support | Bind dominant/indicator taxa, structure or composition evidence where supplied. |
| Space and time | Retain plot/polygon scale, method, topology, vintage and uncertainty. |
| Cross-lane relation | Reference Habitat and Flora evidence without adopting either domain’s authority. |
| Exposure and correction | Review rare habitat, private stewardship, restrictions and supersession. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic survey-plot classification retains its vocabulary version and plot support; the broader mapped region remains an inference requiring its own method.

**Invalid claim:** A modeled land-cover class is treated as confirmed community composition or a restoration target is marked as an observed existing community.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

Community labels are not occurrence proof for every member species. Changing classification vocabulary can change derived counts and labels without new field observations.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/vegetation_community.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Bind a closed versioned schema and tests for role separation, topology, classification updates, missing composition evidence and sensitive habitat inference.

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
