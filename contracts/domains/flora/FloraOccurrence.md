<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/floraoccurrence
title: Plant occurrence records
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Plant occurrence records; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/flora_occurrence.md
  - schemas/contracts/v1/domains/flora/flora_occurrence.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Floraoccurrence

This retained CamelCase path is a draft compatibility and review guide for
`FloraOccurrence`. The existing [flora_occurrence semantic contract](flora_occurrence.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A FloraOccurrence is a source-bound assertion about a plant subject at a place and time. It can represent observed, specimen-supported, survey-derived, aggregate, modeled, administrative or synthetic material; those classes do not support the same claim.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Identity and source | Retain occurrence/candidate identity, source descriptor, native record, edition and source role. |
| Taxon support | Keep source taxon name and reviewed taxon/crosswalk references distinct. |
| Basis of record | Explain observation, specimen, survey, aggregate, model or administrative basis. |
| Place and time | Retain support scale, date precision, uncertainty and restricted/public geometry separation. |
| Evidence and governance | Bind evidence and validation; keep rights, sensitivity, review and release independent. |
| Correction | Retain supersession, source withdrawal and affected derivative references. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic county-supported historical observation retains its source date, taxon uncertainty and candidate status, with public release still held.

**Invalid claim:** A county checklist row is labeled an exact, current observed occurrence, or an obscured record is exposed with its original coordinates.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

An occurrence claim must not become current merely because it was retrieved today. Absence of a row is not an observed absence; location precision cannot be reconstructed from a public derivative.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/flora_occurrence.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Close occurrence-class and geometry/time semantics with exact positive and negative fixtures. The separate bounded occurrence-candidate and public-safe smoke profiles must be mapped deliberately before claiming umbrella coverage.

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
