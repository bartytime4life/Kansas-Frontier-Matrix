<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/planttaxon
title: Plant taxon identity review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Plant taxon identity review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/plant_taxon.md
  - schemas/contracts/v1/domains/flora/plant_taxon.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Planttaxon

This retained CamelCase path is a draft compatibility and review guide for
`PlantTaxon`. The existing [plant_taxon semantic contract](plant_taxon.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A PlantTaxon is the Flora identity anchor for names, ranks, source identifiers, taxonomic status and correction lineage. It enables references without making KFM the source of botanical authority.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Identity | Keep candidate identity separate from accepted canonical identity. |
| Source name and ID | Preserve the source-native identifier, name and authorship/rank where supplied. |
| Backbone binding | Name the provider and exact taxonomy/list version. |
| Accepted/candidate label | Record review-supported display label and unresolved or deprecated status. |
| Crosswalks | Retain synonym, vernacular and external-ID mapping evidence. |
| Correction | Maintain concept split/merge, supersession and downstream revalidation lineage. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic taxon candidate preserves two conflicting source names and stays unresolved until a reviewed crosswalk supports a display label.

**Invalid claim:** A model-generated name is marked accepted without source support, or a taxon identity is used as proof that the species occurs in Kansas.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

Identity, list status, occurrence, sensitivity and range are separate concerns. A taxon label change may affect public projections and protected-status handling without changing observations.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/plant_taxon.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Choose canonical identity/version behavior through the existing contract review; add strict source/version and conflict cases. Do not adopt a new slug/hash algorithm in this compatibility document.

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
