<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/redactionreceipt.flora
title: Flora protective-transform receipt review
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Flora protective-transform receipt review; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/redaction_receipt.md
  - schemas/contracts/v1/domains/flora/redaction_receipt.schema.json
  - docs/domains/flora/OBJECT_FAMILIES.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Redactionreceipt Flora

This retained CamelCase path is a draft compatibility and review guide for
`RedactionReceipt`. The existing [redaction_receipt semantic contract](redaction_receipt.md)
is the detailed semantic home. Keep future meaning changes there and link them
here; this guide does not create a second writable contract or adopt an alias.

## Meaning and identity

A Flora RedactionReceipt records a protective transformation and its evidence: what changed, which input/output it binds, why it was required, what method was used and how correction can reach the derivative.

Source-native identity and source/version evidence must survive normalization.
A candidate identifier or hash does not resolve the source, approve review or
create canonical identity. Preserve the original record and any supersession
relationship through correction.

## Required semantic review

The table summarizes proposed review requirements from the existing contract.
These are not field-level rules enforced by the current permissive schema.

| Dimension | Review requirement |
|---|---|
| Input identity | Reference protected source object and selected fields through appropriate access controls. |
| Output identity | Identify the exact derivative or explicit suppression/withholding result. |
| Transformation | Bind class, method/version, parameters and before/after support. |
| Decision basis | Reference rights, sensitivity, policy and review requirements without becoming those decisions. |
| Integrity and validation | Preserve input/output digest binding and validation evidence. |
| Correction | Identify transform supersession, affected release and rollback target. |

## Illustrative valid and invalid cases

**Semantically coherent review candidate:** A synthetic receipt describes exact-to-county generalization using protected input references, a derivative digest and review links, without exposing the original point.

**Invalid claim:** A receipt copies original coordinates or a restricted locator into public metadata, or claims the existence of a receipt alone authorizes release.

These are synthetic prose examples, not released records or executable fixtures.
The invalid claim must remain denied, held or subject to abstention under the
appropriate future profile; a shape-only JSON pass cannot make it valid.

## Invariants and lifecycle

The receipt is evidence of a transform, not the transformation policy or release decision. An opaque input reference still needs access review; a reversible transform may remain sensitive.

Retain source and evidence lineage during candidate work. A public derivative
needs its own rights, sensitivity, policy, review, release and correction
support. Neither this guide nor an accepted intake recommendation performs any
lifecycle transition, source activation, transformation or publication.

## Current schema and validation posture

The [paired schema](../../../schemas/contracts/v1/domains/flora/redaction_receipt.schema.json)
has `properties: {}`, no required field list and `additionalProperties: true`
at the evidence snapshot. It does not enforce the semantic dimensions above.
The [bounded Flora smoke suite](../../../tests/domains/flora/test_flora_smoke.py)
proves only its own public-safe fixture profile, not complete coverage of this
object family.

Reconcile the .flora schema with the existing lowercase receipt contract/schema and define a public projection. Test input/output binding, unsafe metadata, unknown parameters and withdrawal propagation.

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
