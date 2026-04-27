<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-NEEDS-UUID
title: KFM STAC Extension Profile
type: standard
version: v1
status: draft
owners: TODO
created: TODO
updated: 2026-04-27
policy_label: public
related: [
  docs/adr/ADR-PROV-STAC-DCAT-CATALOG-MAPPING.md,
  contracts/v1/provenance/kfm_prov_sidecar.schema.json,
  docs/catalog/dcat/KFM_DCAT_EXPORT_PROFILE.md
]
tags: [kfm, stac, catalog, provenance, evidence, receipts]
notes: [Defines KFM-specific STAC fields and links for public-safe catalog artifacts.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM STAC Extension Profile

KFM-specific STAC fields for evidence-bound, provenance-linked, public-safe catalog exports.

---

## Purpose

This profile defines how KFM publishes STAC Items and Collections without losing:

- deterministic identity
- EvidenceBundle lineage
- run receipts
- redaction receipts
- attestation links
- rights and sensitivity posture

STAC is a discovery layer. It is **not** the source of truth.

---

## Required KFM Properties

| Property | Required | Type | Description |
|---------|----------|------|-------------|
| `kfm:spec_hash` | yes | string | Canonical deterministic artifact/spec identity |
| `kfm:evidence_ref` | yes | string | Reference to the governing EvidenceBundle |
| `kfm:run_receipt_url` | yes | string | URL or repo path to PROV/run receipt |
| `kfm:release_manifest_ref` | yes | string | Release manifest reference |
| `kfm:policy_label` | yes | string | Public policy posture |
| `kfm:review_state` | yes | string | Review state at publication |
| `kfm:source_role` | yes | string | Role of the underlying source |
| `kfm:redaction_receipt_url` | conditional | string | Required when geometry/fields were transformed |
| `kfm:ai_receipt_url` | conditional | string | Required when AI contributed interpretation |

---

## Allowed Policy Labels

```text
public
restricted
deny
TODO
