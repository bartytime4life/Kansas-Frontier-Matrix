<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/rareplantrecord
title: Sensitive plant record review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Sensitive plant record review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/rare_plant_record.md
  - schemas/contracts/v1/domains/flora/rare_plant_record.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Rareplantrecord

This retained CamelCase path is a draft compatibility and review guide for
`RarePlantRecord`. The existing [rare_plant_record semantic contract](rare_plant_record.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A RarePlantRecord represents a rare, protected, tracked, culturally controlled or otherwise sensitive plant record. It can bind occurrence evidence, status, restricted geometry and a separately reviewed public derivative.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Taxon and status | Retain source name, taxon crosswalk, status authority and effective time. |
| Support | Identify occurrence, specimen, survey or status evidence without conflating them. |
| Restricted representation | Keep exact geometry and protected timing in authorized custody. |
| Public derivative | Name generalized, delayed, suppressed or withheld output only when separately justified. |
| Rights and review | Bind source restrictions, sensitivity and accountable stewardship decisions. |
| Correction and withdrawal | Trace affected map, export, evidence and answer dependents. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic sensitive record retains only opaque restricted references and declares no public projection while review is unresolved.

**Invalid claim:** High-quality specimen evidence is treated as permission to publish exact locality, or a citation reveals the protected location removed from map geometry.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

Strong evidence does not authorize exposure. Public labels, timestamps, links and cross-domain joins can reveal sensitive locality even without coordinates.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/rare_plant_record.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Close the schema, access-control and transformation receipt profiles before runtime use. Negative tests must cover hidden location aliases, restricted citations, missing review and stale permission.

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
