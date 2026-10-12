<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/restorationplanting
title: Restoration planting record review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Restoration planting record review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/restoration_planting.md
  - schemas/contracts/v1/domains/flora/restoration_planting.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Restorationplanting

This retained CamelCase path is a draft compatibility and review guide for
`RestorationPlanting`. The existing [restoration_planting semantic contract](restoration_planting.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A RestorationPlanting records a project, seed mix, planting event, stock lot, site preparation, phase or monitoring visit. Planned work, work performed and ecological outcome remain distinct.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Project/event | Preserve source project/site and specific planting or monitoring event identity. |
| Flora subjects | Bind taxa, source names, seed/stock lots and crosswalk evidence. |
| Provenance | Retain supplied ecotype/cultivar/lot origin without inventing suitability. |
| Phase and time | Distinguish plan, planting, monitoring and establishment assessment with their clocks. |
| Site and evidence | Keep method, spatial support, habitat context and evidence references. |
| Sensitivity/correction | Review private land, steward and cultural information; retain supersession and withdrawal. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic planting event lists the recorded mix and date while establishment and survival remain unknown pending independent monitoring.

**Invalid claim:** A seed-mix plan is treated as successful establishment, or planted individuals are automatically published as wild occurrences.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

A project record is not a management recommendation or proof of ecological success. Source rights and location sensitivity remain relevant even for restoration intended to benefit habitat.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/restoration_planting.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Close event/phase and provenance schemas, then add tests for plan-versus-execution, establishment overclaims, wild-occurrence collapse and restricted project details.

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
