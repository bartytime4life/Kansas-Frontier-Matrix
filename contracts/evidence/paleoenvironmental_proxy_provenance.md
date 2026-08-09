<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/paleoenvironmental-proxy-provenance
title: PaleoenvironmentalProxyProvenanceRecord — fixture-only provenance contract
type: semantic-contract
version: v0.1.0
status: proposed-inactive; fixture-only; non-release; non-publication
owner: OWNER_TBD — evidence steward · paleoenvironment steward · spatial steward · sensitivity reviewer · Directory Rules reviewer
created: 2026-08-09
updated: 2026-08-09
policy_label: public; proposed; evidence; provenance; paleoenvironment; sensitivity-aware; non-authoritative
source_card: KFM-P30-PROG-0029
source_spec_hash: sha256:cd77280751f0bc76d55a2ecddff911b0b9f022b79bcad4ad90500320fdffc295
related:
  - README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/evidence/paleoenvironmental_proxy_provenance.schema.json
  - ../../fixtures/contracts/v1/evidence/paleoenvironmental_proxy_provenance/cases.json
[/KFM_META_BLOCK_V2] -->

# PaleoenvironmentalProxyProvenanceRecord

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This contract records provenance boundaries for a synthetic paleoenvironmental proxy and its reconstruction. It does not ingest observations, locate a real site, prove past or present conditions, evaluate policy, release data, or publish an output.

## Responsibility boundary

The record keeps four surfaces distinct: proxy-source provenance, reconstruction provenance, temporal interpretation, and spatial generalization. It is an evidence object under `contracts/evidence/`; machine shape, validation, fixtures, policies, lifecycle data, and publications remain in their owning roots.

## Required meaning

| Surface | Meaning | Anti-collapse rule |
|---|---|---|
| `proxy_source` | Opaque source record, sample/series reference, proxy kind, chronology, rights, and sensitivity posture. | A proxy observation is not a reconstructed environment or current-condition observation. |
| `reconstruction` | Versioned method, parameter hash, transformation receipts, uncertainty model, and output artifact identity. | Interpretive reconstruction cannot be relabeled as an observed proxy. |
| `temporal_scope` | Explicit timescale, bounded interval, epoch, resolution, uncertainty, and calibration reference. | Temporal coverage is not present-day equivalence or predictive authority. |
| `spatial_generalization` | Opaque source location, published extent, method, precision transition, generalization receipt, and sensitivity reason. | Published precision cannot exceed source precision; protected locations must remain withheld. |
| `evidence_refs` | Closure over the proxy source, transformations, and spatial-generalization receipt. | Missing support fails closed. |
| `claims` and `permissions` | Explicit non-authority and non-effect assertions. | Provenance completeness does not authorize interpretation, policy, release, or publication. |

## Identity

`spec_hash` is the repository hashing package's RFC 8785/JCS SHA-256 digest over the full record after removing `record_id` and `spec_hash`. `record_id` is `kfm:paleoenvironmental-proxy-provenance:` plus the first 24 hexadecimal digest characters. Set-like arrays are sorted and duplicate-free.

## Precision and evidence closure

Precision order is `EXACT` → `SITE` → `LOCALITY` → `COUNTY` → `REGION` → `STATE` → `WITHHELD`; movement may only remain level or generalize. When sensitivity is not `PUBLIC`, `exact_location_withheld` must be true and published precision cannot be `EXACT` or `SITE`. The evidence set must contain the proxy source reference, every transformation receipt, and the spatial-generalization receipt.

## Non-effects

A conforming record performs no source access, coordinate disclosure, proxy ingestion, reconstruction execution, current-condition inference, forecast, evidence mutation, policy decision, lifecycle promotion, release, or publication. A validator PASS proves only bounded shape, semantic consistency, evidence-reference closure, precision monotonicity, fixture polarity, and deterministic identity.

## Adoption and rollback

Activation requires reviewed real-source mappings, domain vocabulary, rights and sensitivity policy, temporal and spatial authorities, reconstruction method governance, lifecycle integration, and release gates. Rollback of this proposal is deletion of its contract packet; no source or output data is modified.
