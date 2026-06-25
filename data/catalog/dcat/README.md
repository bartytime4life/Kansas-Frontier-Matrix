<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-catalog-dcat-readme
title: data/catalog/dcat/README.md — DCAT Catalog Sublane README
version: v0.1
type: readme; data-lifecycle-sublane; dcat-catalog-guide
status: draft; PROPOSED; data-root; catalog-stage; dcat; release-gated
owners: OWNER_TBD — Data steward · Catalog steward · DCAT steward · Evidence steward · Policy steward · Release steward · Schema steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-06-24
policy_label: public-doc; data; catalog; dcat; lifecycle; release-gated
tags: [kfm, data, catalog, dcat, DCATv3, CATALOG, STAC, PROV, EvidenceBundle, SourceDescriptor, ReleaseManifest, CatalogBuildReceipt]
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/standards/DCAT.md
  - ../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../schemas/
  - ../../../policy/
  - ../../../release/
notes:
  - "Expanded from a greenfield stub at `data/catalog/dcat/README.md`."
  - "DCAT records are catalog carriers and do not replace SourceDescriptor, EvidenceBundle, RunReceipt, PolicyDecision, or ReleaseManifest."
  - "ADR-0022 requires STAC, DCAT, and PROV-O catalog records to agree by identifier, digest, and release reference for promoted releases."
  - "Rollback target for this expansion is previous stub blob SHA `47704f9c29000e8fbef71e334d21ce595f2f9ba0`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/catalog/dcat

> DCAT catalog sublane for governed `dcat:Dataset` and `dcat:Distribution` records inside the `CATALOG / TRIPLET` lifecycle stage. DCAT supports catalog discovery and interoperability. It is not source truth, proof storage, policy authority, schema authority, or release authority.

**Status:** draft / PROPOSED  
**Path:** `data/catalog/dcat/README.md`  
**Owning root:** `data/catalog/`  
**Lifecycle stage:** `CATALOG / TRIPLET`  
**External vocabulary:** W3C DCAT v3  
**Exposure posture:** RELEASED ONLY  
**Truth posture:** CONFIRMED target was a greenfield stub · CONFIRMED parent catalog lane is RELEASED ONLY · CONFIRMED DCAT profile targets W3C DCAT v3 and names `data/catalog/dcat/` as catalog data home · CONFIRMED ADR-0022 says STAC, DCAT, and PROV must agree for promoted releases · NEEDS VERIFICATION for concrete inventory, schemas, validators, policy gates, receipts, release manifests, and routed access behavior.

## Purpose

`data/catalog/dcat/` stores or stages governed DCAT catalog records for KFM datasets and distributions.

A DCAT record can help users and systems discover catalog metadata. It cannot make a dataset true, public, policy-admitted, evidence-supported, or released by itself.

## Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

`data/catalog/dcat/` is a CATALOG-stage sublane. Public exposure applies only to records tied to an approved release and governed access path.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| DCAT catalog records | `data/catalog/dcat/` | This lane. |
| Parent catalog stage | `data/catalog/` | Parent CATALOG-stage lane. |
| STAC catalog records | `data/catalog/stac/` | Spatiotemporal catalog records. |
| PROV catalog records | `data/catalog/prov/` | Provenance catalog projection. |
| Evidence/proof records | `data/proofs/` | EvidenceBundle and ProofPack. |
| Receipts | `data/receipts/` | CatalogBuildReceipt, RunReceipt, validation receipts. |
| Release decisions | `release/` | Publication authority. |
| Published outputs | `data/published/` | Public-safe materialization after release. |
| Schemas and policy | `schemas/`, `policy/` | Separate roots. |
| Validators and tests | `tools/validators/`, `tests/` | Separate roots. |

## Accepted contents

| Content | Purpose |
|---|---|
| `dcat:Dataset` records | Dataset-level catalog metadata. |
| `dcat:Distribution` records | Distribution metadata and references. |
| KFM extension fields | Source, evidence, release, policy, digest, rights, and sensitivity pointers. |
| Release-linked DCAT records | DCAT records tied to ReleaseManifest references. |
| DCAT validation summaries | Pointers to validation reports and receipts. |

## Exclusions

| Do not put here | Correct home |
|---|---|
| RAW source files | `data/raw/` |
| WORK/intermediate data | `data/work/` |
| Quarantined data | `data/quarantine/` |
| Processed datasets | `data/processed/` |
| STAC records | `data/catalog/stac/` |
| PROV records | `data/catalog/prov/` |
| Triplets/graph edges | `data/triplets/` |
| EvidenceBundle/proof records | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions | `release/` |
| Published public products | `data/published/` |
| JSON Schema | `schemas/` |
| Policy rules | `policy/` |
| Validators/tests/code | `tools/validators/`, `tests/`, implementation roots |

## DCAT record requirements

PROPOSED until schema and validator are verified:

| Requirement | Meaning |
|---|---|
| Stable identifier | Identifier matches the artifact identity used by catalog closure. |
| Distribution digest | Checksum matches the released artifact or referenced bundle digest. |
| Release reference | Public or release-linked records point to the immutable ReleaseManifest. |
| Evidence reference | EvidenceBundle/proof context is referenced when claims depend on evidence. |
| Source reference | SourceDescriptor/source catalog is referenced when source authority matters. |
| Policy reference | Policy/admissibility posture is available when release or sensitivity depends on it. |
| Closure compatibility | STAC ↔ DCAT ↔ PROV agreement holds for promoted releases. |

## Guardrails

- DCAT is a catalog vocabulary, not source truth.
- DCAT, STAC, and PROV records for the same released artifact must agree on identifier, digest, and release reference.
- EvidenceBundle, SourceDescriptor, RunReceipt, PolicyDecision, and ReleaseManifest remain separate authority objects.
- Unreleased DCAT records are not public merely because they exist under `data/catalog/dcat/`.

## Validation checklist

- [ ] Confirm actual child directories and DCAT record files.
- [ ] Confirm DCAT schema/profile location.
- [ ] Confirm DCAT validator and CI checks.
- [ ] Confirm STAC/DCAT/PROV catalog matrix closure.
- [ ] Confirm ReleaseManifest linkage for public DCAT records.
- [ ] Confirm EvidenceBundle, SourceDescriptor, RunReceipt, and PolicyDecision references.
- [ ] Confirm rights, sensitivity, and publication handling.
- [ ] Confirm withdrawal/supersession behavior for stale or failed DCAT records.

## Rollback

Rollback is required if this lane becomes a source-data root, proof store, release-decision root, published-output root, schema root, policy root, validator root, or implementation root.

Rollback target for this expansion: previous stub blob SHA `47704f9c29000e8fbef71e334d21ce595f2f9ba0`.

<p align="right"><a href="#top">Back to top</a></p>
