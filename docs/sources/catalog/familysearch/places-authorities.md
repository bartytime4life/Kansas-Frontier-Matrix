<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-familysearch-places-authorities
title: FamilySearch Places
type: product-page
version: v0.1
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for familysearch>
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/sources/catalog/familysearch/README.md
  - docs/sources/catalog/README.md
  - docs/doctrine/directory-rules.md
tags: [kfm, docs, sources, catalog, familysearch]
notes:
  - "PROPOSED product-page scaffold; sibling-link presence verified in Claude Code session."
[/KFM_META_BLOCK_V2] -->

# FamilySearch Places

> FamilySearch place IDs and authorities used as context anchors.

**Status:** PROPOSED — scaffold only · **Family:** [`familysearch`](./README.md) · **Last reviewed:** 2026-05-20

---

## Overview
PROPOSED scaffold. NEEDS VERIFICATION: scope, cadence, geographic coverage, current endpoint URL, rights status, license terms.

## Source authority
See [`data/registry/sources/`](../../../../data/registry/sources/) for the authoritative SourceDescriptor. **Do not duplicate** descriptor fields here.

## Catalog profiles used
| Profile | Lane | Used by this product? |
|---|---|---|
| STAC | `data/catalog/stac/` | PROPOSED — Yes / No (NEEDS VERIFICATION) |
| DCAT | `data/catalog/dcat/` | PROPOSED — Yes / No (NEEDS VERIFICATION) |
| PROV-O | `data/catalog/prov/` | PROPOSED — Yes / No (NEEDS VERIFICATION) |
| Domain projection | `data/catalog/domain/<domain>/` | PROPOSED — Yes / No (NEEDS VERIFICATION) |

## Collection identity
- PROPOSED Collection id pattern: `kfm-<org>-<product>` (see [`IDENTITY.md`](../IDENTITY.md)).
- PROPOSED namespace: `kfm:` *(see OPEN-DSC-03)*.
- Asset roles: NEEDS VERIFICATION — confirm against `schemas/contracts/v1/source/`.

## Provenance fields
STAC `properties.kfm:provenance` block (PROPOSED — Pass-10 C4-01):
- `spec_hash` — sha256 of the canonical record.
- `evidence_bundle_ref` — `kfm://evidence/<digest>`.
- `run_record_ref` — `kfm://run/<run-id>`.
- `audit_ref` — `kfm://audit/<attestation-id>`.
- `policy_digest` — sha256 of the policy bundle.
Per-asset integrity: `file:checksum`.

## Temporal handling
PROPOSED — distinct source / observed / valid / retrieval / release / correction times where material. NEEDS VERIFICATION per product.

## Geometry and projection
PROPOSED — confirm CRS, generalization rules, and scale support against `data/catalog/` artifacts. NEEDS VERIFICATION.

## Rights and sensitivity
NEEDS VERIFICATION — see [`policy/sensitivity/`](../../../../policy/sensitivity/) and [`RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md). **Do not restate policy here.**

## Validation and catalog closure
- Catalog closure required before public release (Pass-10 / KFM-P1-IDEA-0020).
- STAC Projection lint (KFM-P27-FEAT-0003) — PROPOSED.
- STAC checksum closure against the ReleaseManifest digest (KFM-P22-PROG-0037) — PROPOSED.

## Related contracts and schemas
- `contracts/` — NEEDS VERIFICATION.
- `schemas/contracts/v1/source/` — per ADR-0001.

## Related connectors and pipelines
- `connectors/familysearch/`.
- `pipelines/ingest/`, `pipelines/normalize/`, `pipelines/validate/`, `pipelines/catalog/`.
- `pipeline_specs/<domain>/`.

## Examples
*(Illustrative only — do not treat as authoritative.)*
See [`_examples/stac-item-example.json`](../_examples/stac-item-example.json) for the minimal STAC + `kfm:provenance` shape.

## Open questions
- OPEN — confirm cadence and current endpoint URL.
- OPEN — confirm rights status and CARE applicability.
- OPEN — confirm whether this product warrants its own STAC Collection or shares one with sibling products.

## Last reviewed
2026-05-20 *(Claude Code product-page scaffold session).*
