<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-catalog-readme
title: data/catalog/README.md — Catalog-Stage Data README
version: v0.1
type: readme; data-lifecycle-stage; catalog-stage-guide
status: draft; PROPOSED; data-root; catalog-stage; implementation-bounded; release-gated
owners: OWNER_TBD — Data steward · Catalog steward · Evidence steward · Policy steward · Release steward · Schema steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-06-24
policy_label: public-doc; data; catalog; lifecycle; release-gated; no-raw-public
tags: [kfm, data, catalog, lifecycle, CATALOG, TRIPLET, STAC, DCAT, PROV, EvidenceBundle, ReleaseManifest, CatalogBuildReceipt]
related:
  - ../README.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../contracts/data/README.md
  - ../../contracts/data/catalog_matrix.md
  - ../../schemas/
  - ../../policy/
  - ../../tests/
  - ../../tools/validators/
  - ../../release/
  - ../triplets/
  - ../published/
  - ../proofs/
  - ../receipts/
notes:
  - "Expanded from a greenfield stub at `data/catalog/README.md`."
  - "The data root is the canonical lifecycle data root and includes catalog, triplets, receipts, proofs, published, registry, and related data lanes."
  - "Lifecycle Law defines `data/catalog` as RELEASED ONLY exposure with required `CatalogBuildReceipt` and withdraw/supersede failure disposition."
  - "Catalog records are not release decisions; release authority lives under `release/` and public-safe materialization belongs under `data/published/` after governance gates."
  - "Rollback target for this expansion is previous stub blob SHA `617d8c10c5424f7c463491ef168ce8c6c608cd09`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/catalog

> Catalog-stage data lane for governed catalog records and indexes. `data/catalog/` may hold catalog projections such as STAC, DCAT, PROV, and domain catalog records after processed candidates are promoted into catalog form. It is not RAW, WORK, QUARANTINE, PROCESSED, PUBLISHED, proof storage, release authority, schema authority, policy code, or implementation code.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data/catalog" src="https://img.shields.io/badge/root-data%2Fcatalog-blue">
  <img alt="Lifecycle: CATALOG" src="https://img.shields.io/badge/lifecycle-CATALOG-purple">
  <img alt="Exposure: released only" src="https://img.shields.io/badge/exposure-RELEASED__ONLY-critical">
  <img alt="Truth: evidence first" src="https://img.shields.io/badge/truth-evidence__first-green">
</p>

**Status:** draft / PROPOSED  
**Path:** `data/catalog/README.md`  
**Owning root:** `data/`  
**Lifecycle stage:** `CATALOG / TRIPLET`  
**Exposure posture:** RELEASED ONLY — only records tied to an approved release may be public  
**Truth posture:** CONFIRMED target was a greenfield stub · CONFIRMED `data/README.md` defines `data/` as lifecycle data root including `catalog` · CONFIRMED Lifecycle Law defines `data/catalog` as RELEASED ONLY with `CatalogBuildReceipt` · NEEDS VERIFICATION for concrete catalog inventory, schemas, validators, receipts, policy gates, release manifests, and public route behavior.

## Quick jumps

[Purpose](#purpose) · [Lifecycle boundary](#lifecycle-boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Recommended layout](#recommended-layout) · [Catalog guardrails](#catalog-guardrails) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/catalog/` materializes the `CATALOG` side of the `CATALOG / TRIPLET` lifecycle stage.

It may hold governed catalog records and indexes that describe datasets, layers, sources, provenance, domains, rights, sensitivity, publication candidates, or released public records.

A catalog record can help users and systems discover governed data. It does not make the underlying claim true, does not replace EvidenceBundle support, and does not approve publication.

## Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

`data/catalog/` receives normalized candidates from `data/processed/` after validation and catalog-building steps. Public exposure is allowed only for the subset of catalog records that belongs to an approved release.

The paired graph projection lane is `data/triplets/`. The slash in `CATALOG / TRIPLET` is doctrinal: catalog records and graph triplets are paired projections of the same lifecycle stage.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Catalog-stage data records | `data/catalog/` | This lane. |
| Source-native captures | `data/raw/` | Do not store here. |
| Transform workspace | `data/work/` | Do not store here. |
| Failed/unsafe holds | `data/quarantine/` | Do not store here. |
| Normalized candidates | `data/processed/` | Upstream of catalog. |
| Graph/triplet projection | `data/triplets/` | Paired CATALOG/TRIPLET stage. |
| Public-safe materialization | `data/published/` | Downstream after release. |
| Evidence/proof | `data/proofs/` | EvidenceBundle and proof records. |
| Receipts | `data/receipts/` | CatalogBuildReceipt and related receipts. |
| Release decisions | `release/` | Publication authority. |
| Schemas/policy/tests/code | `schemas/`, `policy/`, `tests/`, implementation roots | Separate responsibility roots. |

## Accepted contents

| Content | Purpose |
|---|---|
| STAC catalog records | Spatial/temporal asset catalog metadata. |
| DCAT catalog records | Data catalog interoperability metadata. |
| PROV catalog records | Provenance-oriented catalog projections. |
| Domain catalog records | Domain-scoped catalog entries under `domain/<domain>/`. |
| Catalog indexes | Public-safe or steward-only lookup indexes. |
| Release-linked catalog manifests | Pointers to release-approved catalog subsets. |
| Catalog quality summaries | Summaries that point to validation reports and receipts. |

## Exclusions

| Do not put here | Correct home |
|---|---|
| RAW source files | `data/raw/` |
| WORK/intermediate data | `data/work/` |
| Quarantined data | `data/quarantine/` |
| Processed normalized datasets | `data/processed/` |
| Triplets/graph edges | `data/triplets/` |
| Public materialized outputs | `data/published/` |
| EvidenceBundle/proof records | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions | `release/` |
| Source registry records | `data/registry/` or accepted source registry roots |
| Schemas | `schemas/` |
| Policy rules | `policy/` |
| Tests, validators, or code | `tests/`, `tools/validators/`, implementation roots |

## Recommended layout

PROPOSED until verified against concrete files:

```text
data/catalog/
├── README.md
├── stac/
├── dcat/
├── prov/
├── domain/
│   └── <domain>/
├── indexes/
├── quality/
└── release_refs/
```

This layout may be revised by ADR, schema, or data-lifecycle steward decision.

## Catalog guardrails

- Catalog records are discoverability and provenance projections, not source truth.
- Catalog records must point to source descriptors, EvidenceBundle/proof context, validation reports, policy posture, and release state when those are material.
- Unreleased catalog records are not public, even if they live under `data/catalog/`.
- Public routes must enforce release state; directory location alone is not publication.
- Catalog entries that expose sensitive locations, rights-restricted data, archaeology, rare species, living-person data, or infrastructure risk must be redacted, generalized, quarantined, or denied through policy.
- Failed or superseded catalog records must preserve correction and rollback paths rather than being silently overwritten.

## Validation checklist

- [ ] Confirm actual child directories under `data/catalog/`.
- [ ] Confirm catalog record schemas for STAC/DCAT/PROV/domain entries.
- [ ] Confirm `CatalogBuildReceipt` shape and storage home.
- [ ] Confirm validation reports and evidence/proof links.
- [ ] Confirm release linkage for any public catalog record.
- [ ] Confirm policy checks for sensitivity, rights, and source-role posture.
- [ ] Confirm route-level enforcement for RELEASED ONLY exposure.
- [ ] Confirm withdrawal/supersession behavior for failed or stale catalog records.

## Rollback

Rollback is required if this lane becomes a raw data root, work area, quarantine store, processed-data store, proof store, source registry, release-decision root, public-published root, schema root, policy root, validator root, implementation root, or public route bypass.

Rollback target for this expansion: previous stub blob SHA `617d8c10c5424f7c463491ef168ce8c6c608cd09`.

<p align="right"><a href="#top">Back to top</a></p>
