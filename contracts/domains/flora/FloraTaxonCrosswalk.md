<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/florataxoncrosswalk
title: Taxon crosswalk review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Taxon crosswalk review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/flora_taxon_crosswalk.md
  - schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Florataxoncrosswalk

This retained CamelCase path is a draft compatibility and review guide for
`FloraTaxonCrosswalk`. The existing [flora_taxon_crosswalk semantic contract](flora_taxon_crosswalk.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A FloraTaxonCrosswalk records how a source taxon concept, name or identifier relates to a target taxon or unresolved candidate. It supports normalization and audit while preserving the source concept and mapping uncertainty.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Source concept | Retain native identifier, spelling, rank, status and taxonomy/list version. |
| Target concept | Identify the proposed target and its accepted, candidate or unresolved state. |
| Relationship | Distinguish exact identifier, synonym, broader/narrower concept, ambiguous and rejected matches. |
| Basis and review | Record mapping evidence, method and the review scope; name similarity alone is candidate support. |
| Downstream effect | Identify occurrence groupings, public labels and sensitivity/list implications. |
| Correction lineage | Retain old mapping, supersession and revalidation requirements. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic source synonym maps to a versioned target with an explicit synonym relationship; the old spelling and source ID remain retrievable.

**Invalid claim:** An ambiguous common name is silently mapped to one accepted species and used to validate its occurrence or rare-plant status.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

A successful mapping is not a taxonomic authority decision or occurrence proof. A backbone split/merge requires consumer review; do not distribute historic observations across new concepts by convenience.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Pair a closed schema with mapping-specific negatives, version/compatibility rules and expert review. The taxonomy policy currently defaults deny; no automated backbone rotation is established by this guide.

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
