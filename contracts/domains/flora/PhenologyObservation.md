<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/phenologyobservation
title: Plant phenology observation review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Plant phenology observation review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/phenology_observation.md
  - schemas/contracts/v1/domains/flora/phenology_observation.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Phenologyobservation

This retained CamelCase path is a draft compatibility and review guide for
`PhenologyObservation`. The existing [phenology_observation semantic contract](phenology_observation.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A PhenologyObservation is a time- and support-bound claim about a plant seasonal phase. It may be observed, specimen-derived, surveyed, aggregated, modeled or administratively described.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Subject | Link the plant/taxon or occurrence, specimen, survey, community or restoration subject. |
| Phase | Retain source phase text/code and separately reviewed normalized phase. |
| Intensity and certainty | Record the supplied scale, count/percentage or categorical basis; missing values remain unknown. |
| Time | Preserve observation interval, precision, source timezone and retrieval clock distinctly. |
| Location/support | Retain site or generalized support and uncertainty without exposing restricted locality. |
| Evidence and correction | Bind method, role, evidence and supersession to the exact observation. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic historical specimen-derived flowering observation carries the collection date precision and does not claim flowering today.

**Invalid claim:** A retrieval date is substituted for observation date, or a modeled seasonal window is presented as an observed bloom at an exact site.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

No phase detected is not the same as not surveyed or unknown. A time-series point cannot support a population trend without a declared sampling and analysis method.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/phenology_observation.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Bind phase vocabulary and time precision to strict fixtures, including ambiguous dates, missing support, modeled-role collapse and sensitivity leakage. Current permissive shape cannot enforce them.

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
