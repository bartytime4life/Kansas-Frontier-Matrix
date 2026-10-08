<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/invasiveplantrecord
title: Invasive plant record review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Invasive plant record review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/invasive_plant_record.md
  - schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Invasiveplantrecord

This retained CamelCase path is a draft compatibility and review guide for
`InvasivePlantRecord`. The existing [invasive_plant_record semantic contract](invasive_plant_record.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

An InvasivePlantRecord captures a source-qualified occurrence, infestation, survey result, treatment record, regulatory status, aggregate report or modeled risk concerning an invasive or potentially invasive plant.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Subject | Retain source taxon name and versioned taxon/crosswalk support. |
| Record class | Separate observed occurrence, non-detection, treatment, status and modeled risk. |
| Status authority | Identify the list or source behind invasive/noxious/watch-list status and effective time. |
| Extent and method | Keep survey effort, geometry support, abundance/extent and uncertainty where evidenced. |
| Management context | Record treatment/management observations without inferring success or prescribing action. |
| Governance | Bind rights, private-land precision, evidence, review, release and correction separately. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic administrative status record names the relevant source/list edition and makes no assertion that the plant occurs at a particular site.

**Invalid claim:** A regulatory list entry is converted into an exact infestation point or a treatment record is treated as confirmed eradication.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

Public benefit does not erase private-land or source restrictions. Status, occurrence, risk and treatment outcome must remain distinct, including through map filters and exports.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Implement class-specific shape, effective-time checks and negatives for list-as-occurrence, modeled-as-observed, stale restrictions and private precision before broadening runtime use.

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
