<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/habitatassociation
title: Flora habitat association review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Flora habitat association review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/habitat_association.md
  - schemas/contracts/v1/domains/flora/habitat_association.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Habitatassociation

This retained CamelCase path is a draft compatibility and review guide for
`HabitatAssociation`. The existing [habitat_association semantic contract](habitat_association.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A HabitatAssociation links a Flora subject to a bounded habitat or environmental context. The relationship may come from observation, specimen text, literature, a model, a survey or a restoration plan.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Flora subject | Identify taxon, occurrence, community, range or restoration subject and its evidence state. |
| Habitat target | Identify the habitat object, classification or contextual source without replacing its owning domain. |
| Association type | Retain relation category, basis and any supported strength. |
| Support | Record spatial scale, temporal scope and uncertainty on both sides. |
| Sensitivity | Review whether the join reveals a rare plant, private site or sensitive habitat. |
| Lineage | Bind evidence, source roles, corrections and any public derivative separately. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic modeled association relates a candidate taxon to generalized soil/moisture context with model role and uncertain scope explicit.

**Invalid claim:** Modeled suitable habitat is relabeled an observed occupied location, or a public association reconstructs a restricted rare-plant site.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

A habitat relation does not create canonical Habitat-domain truth. Shared geography alone cannot establish occupancy or causation.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/habitat_association.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Reconcile the existing habitat_association schema with the separate .flora schema lineage, then bind cross-domain negatives and access controls. Neither permissive schema currently enforces these semantic requirements.

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
