<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-profiles
title: Source catalog profiles register
type: register
version: v0.3
status: draft
owners: Docs steward · Source steward · Catalog profile owner
created: 2026-05-20
updated: 2026-06-12
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/sources/catalog/CROSSWALKS.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/GLOSSARY.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/catalog/CARE-COMPLIANCE.md
  - docs/standards/STAC.md
  - docs/standards/DCAT.md
  - docs/standards/PROV.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/contract-schema-policy-split.md
  - schemas/contracts/v1/source/
tags: [kfm, docs, sources, catalog, register, profiles, stac, dcat, prov, provenance, care, attestation]
notes:
  - "v0.3 — optimized authority boundary. This file is a pointer register and catalog-lane coordination surface, not the authoritative source for external standard profile content, object meaning, machine-checkable schema shape, policy decisions, or release decisions."
  - "External standards profile content belongs in docs/standards/. KFM object meaning belongs in contracts/. Machine-checkable shape belongs in schemas/. Policy/admissibility decisions belong in policy/ and release/."
  - "v0.3 downgrades unverified repo-path and sibling-link claims to NEEDS VERIFICATION unless supported by mounted-repo evidence, current repo scan, accepted ADR, or generated artifact."
  - "v0.3 retains the v0.2 doctrinal correction: type remains register, not profile."
  - "v0.3 keeps ADR-0014 for temporal vocabulary as NEEDS VERIFICATION. The six time-kinds vocabulary remains doctrine-supported; the specific ADR identifier must be reconciled against the active ADR ledger."
[/KFM_META_BLOCK_V2] -->

# Source Catalog Profiles Register

> Pointer register for the external metadata-standard profiles the source-catalog lane relies on — **STAC**, **DCAT**, and **PROV-O** — plus the KFM-namespaced extension obligations that must travel through catalog, evidence, policy, release, and UI surfaces.

![status](https://img.shields.io/badge/status-draft%20%C2%B7%20scaffold-yellow)
![type](https://img.shields.io/badge/type-register-blueviolet)
![profiles](https://img.shields.io/badge/external%20profiles-3-1f6feb)
![authority](https://img.shields.io/badge/profile%20content-docs%2Fstandards%2F-green)
![schema](https://img.shields.io/badge/schema%20shape-schemas%2Fcontracts%2Fv1-orange)
![policy](https://img.shields.io/badge/policy-policy%2F%20%2B%20release%2F-red)
![reviewed](https://img.shields.io/badge/last%20reviewed-2026--06--12-green)

**Status:** draft scaffold  
**Type:** register, not profile  
**Last reviewed:** 2026-06-12  
**Truth posture:** doctrine-supported register · implementation paths **NEEDS VERIFICATION** unless separately confirmed

---

## Contents

- [Purpose](#purpose)
- [Non-authority boundary](#non-authority-boundary)
- [Authority map](#authority-map)
- [Profiles register](#profiles-register)
  - [1. KFM-STAC profile](#1-kfm-stac-profile)
  - [2. KFM-DCAT profile](#2-kfm-dcat-profile)
  - [3. KFM-PROV profile](#3-kfm-prov-profile)
- [KFM-namespaced extension obligations](#kfm-namespaced-extension-obligations)
- [Temporal vocabulary: six time-kinds](#temporal-vocabulary-six-time-kinds)
- [Placement model](#placement-model)
- [Maintenance rules](#maintenance-rules)
- [Validation checklist](#validation-checklist)
- [Open questions](#open-questions)
- [Related docs](#related-docs)
- [Final status](#final-status)

---

## Purpose

This register answers one operational question:

> **For each external metadata standard used by the source-catalog lane, where is the authoritative KFM profile, and which KFM extension obligations must travel with catalog records, evidence references, receipts, policy decisions, release manifests, and public UI payloads?**

This file exists so catalog maintainers do not have to rediscover the same crosswalk every time a STAC Item, DCAT Dataset, PROV-O graph, EvidenceBundle, ReleaseManifest, or MapLibre layer payload is created.

It records:

1. Which external standards are in scope: **STAC**, **DCAT**, and **PROV-O**.
2. Where their authoritative KFM profile documents should live.
3. Which KFM extension obligations must be carried consistently.
4. Which claims are **CONFIRMED**, **PROPOSED**, **NEEDS VERIFICATION**, or **UNKNOWN**.
5. Which open questions block promotion from scaffold to stable register.

---

## Non-authority boundary

This register is deliberately narrow.

| This register does not… | Authority belongs in… |
|---|---|
| define external standards | `docs/standards/` |
| define KFM object meaning | `contracts/` |
| define machine-checkable JSON Schema shape | `schemas/contracts/v1/...` |
| decide allow, deny, restrict, redact, delay, or publish | `policy/` and `release/` |
| prove current implementation | mounted-repo evidence, receipts, logs, tests, CI, dashboards, or accepted ADRs |

This file is a coordination register. It keeps the catalog lane aligned with the standards lane, schema lane, policy lane, evidence lane, release lane, and public UI lane.

---

## Authority map

| Concern | Canonical owner | This file’s role | Status |
|---|---|---|---|
| External profile prose for STAC, DCAT, PROV-O | `docs/standards/` | Points to profile docs | CONFIRMED doctrine / file existence NEEDS VERIFICATION |
| KFM object meaning | `contracts/` | Points to contract owner | CONFIRMED doctrine |
| Machine-checkable object shape | `schemas/contracts/v1/...` | Points to schema owner | CONFIRMED doctrine |
| Source identity, rights, sensitivity | `data/registry/` + source descriptors + policy review | Records catalog dependency | CONFIRMED doctrine / specific paths NEEDS VERIFICATION |
| Policy decisions | `policy/` | Records required policy linkage | CONFIRMED doctrine |
| Release, rollback, correction | `release/` | Records required release linkage | CONFIRMED doctrine |
| STAC/DCAT/PROV catalog outputs | `data/catalog/...` lifecycle lane | Records expected catalog lanes | CONFIRMED lifecycle phase / specific folder shape NEEDS VERIFICATION |
| EvidenceBundle and receipts | evidence/proof/receipt homes per accepted repo convention | Records required references | CONFIRMED doctrine / exact homes NEEDS VERIFICATION |
| Public MapLibre/UI payloads | governed API + released artifacts | Records downstream obligations | CONFIRMED doctrine / implementation UNKNOWN |

> [!IMPORTANT]
> This document is a **register**, not a profile. External standards profile content belongs in `docs/standards/`. KFM object contracts and schemas remain under their own governance roots.

---

## Profiles register

The catalog lane relies on three external standards. Each entry below is a pointer entry, not a full profile definition.

### 1. KFM-STAC profile

| Field | Register value | Status |
|---|---|---|
| Base standard | STAC | CONFIRMED external standard dependency |
| Intended version pin | STAC 1.1.x | PROPOSED / NEEDS VERIFICATION |
| Authoritative KFM profile doc | `docs/standards/STAC.md` | PROPOSED file / placement doctrine-supported |
| Machine-readable schema home | `schemas/contracts/v1/catalog/stac/...` or accepted repo equivalent | PROPOSED / NEEDS ADR or repo verification |
| Catalog output lane | `data/catalog/stac/...` | PROPOSED path / lifecycle phase supported |
| Collection ID convention | `kfm-<org>-<product>` | PROPOSED / verify against `IDENTITY.md` |
| Item identity | deterministic identity from source identity + `spec_hash` | PROPOSED / doctrine-supported |
| Required external extensions | `projection`, `processing`, `file` | PROPOSED / verify against STAC profile |
| KFM extension obligations | `kfm:provenance`, `kfm:care` when applicable, attestation link | PROPOSED register obligation |
| Required public posture | STAC is catalog metadata, not publication approval | CONFIRMED doctrine |

Expected coverage in `docs/standards/STAC.md`:

- version pin and migration rule;
- conformance classes;
- extension list;
- Collection ID rules;
- Item identity and `spec_hash` rules;
- asset role vocabulary;
- MIME/media-type policy;
- `file:checksum` and per-asset integrity;
- `kfm:provenance` carriage;
- `kfm:care` carriage where applicable;
- attestation link relation posture;
- validation fixtures and expected failure cases.

---

### 2. KFM-DCAT profile

| Field | Register value | Status |
|---|---|---|
| Base standard | W3C DCAT | CONFIRMED external standard dependency |
| Intended version pin | DCAT 3 | PROPOSED / NEEDS VERIFICATION |
| Authoritative KFM profile doc | `docs/standards/DCAT.md` | PROPOSED file / placement doctrine-supported |
| Machine-readable schema home | `schemas/contracts/v1/catalog/dcat/...` or accepted repo equivalent | PROPOSED / NEEDS ADR or repo verification |
| Catalog output lane | `data/catalog/dcat/...` | PROPOSED path / lifecycle phase supported |
| Core model | Dataset → Distribution(s) | CONFIRMED standard pattern / KFM mapping PROPOSED |
| Distribution obligations | checksum, byte size, media type, version, license, rights holder, provenance links | PROPOSED |
| KFM extension obligations | `kfm:care` at Dataset level where applicable; provenance at Dataset or Distribution level per profile | PROPOSED / NEEDS VERIFICATION |
| Required public posture | DCAT is harvest/discovery metadata, not publication approval | CONFIRMED doctrine |

Expected coverage in `docs/standards/DCAT.md`:

- Dataset and Distribution mapping;
- version and release mapping;
- license and rights-holder rules;
- DOI or persistent identifier posture;
- EvidenceBundle and ReleaseManifest references;
- STAC → DCAT JSON-LD mapping;
- distribution checksums and byte sizes;
- `kfm:care` exposure rule;
- policy and sensitivity warning fields;
- harvest and correction timestamps.

---

### 3. KFM-PROV profile

| Field | Register value | Status |
|---|---|---|
| Base standard | W3C PROV-O | CONFIRMED external standard dependency |
| Adjacent vocabulary | PAV where useful | PROPOSED / NEEDS VERIFICATION |
| Intended version pin | PROV-O 1.0 | PROPOSED / NEEDS VERIFICATION |
| Authoritative KFM profile doc | `docs/standards/PROV.md` | PROPOSED file / placement doctrine-supported |
| Machine-readable schema home | `schemas/contracts/v1/catalog/prov/...` or accepted repo equivalent | PROPOSED / NEEDS ADR or repo verification |
| Catalog output lane | `data/catalog/prov/...` | PROPOSED path / lifecycle phase supported |
| Core mapping | `RunReceipt` → Activity; `EvidenceBundle` → Entity; tool/operator/system → Agent | PROPOSED / doctrine-supported |
| Key relations | `prov:used`, `prov:generated`, `prov:wasAssociatedWith`, `prov:wasAttributedTo`, `prov:wasGeneratedBy` | PROPOSED |
| Serialization | JSON-LD | PROPOSED |
| Canonicalization | JCS by default for KFM object hashing; URDNA2015 reserved for RDF semantic equivalence | PROPOSED / NEEDS ADR |
| Required public posture | PROV lineage explains evidence flow; it does not override policy or release state | CONFIRMED doctrine |

Expected coverage in `docs/standards/PROV.md`:

- KFM object-family mapping;
- activity/entity/agent identity;
- JSON-LD context strategy;
- canonicalization and hash discipline;
- relation vocabulary;
- time-kind mapping;
- EvidenceBundle, RunReceipt, AIReceipt, ReleaseManifest, and CorrectionNotice linkage;
- Neo4j/triplet projection constraints;
- round-trip checks between STAC/DCAT/PROV.

---

## KFM-namespaced extension obligations

The following are KFM-specific extension obligations. This register records their catalog-lane carriage requirements, but their meaning, schema, and policy effects must be defined in the appropriate authority roots.

### Extension ownership table

| Extension | Catalog carriage | Meaning owner | Shape owner | Policy owner | Status |
|---|---|---|---|---|---|
| `kfm:provenance` | STAC Item properties; DCAT Distribution or Dataset; PROV linkage | `contracts/` | `schemas/contracts/v1/...` | `policy/` + `release/` | PROPOSED / doctrine-supported |
| `kfm:care` | STAC properties and DCAT Dataset where applicable | `contracts/` | `schemas/contracts/v1/...` | `policy/sensitivity/` or accepted equivalent | PROPOSED / default-deny doctrine-supported |
| KFM attestation link relation | STAC `links[]`; DCAT distribution relation; release/proof linkage | `contracts/` | `schemas/contracts/v1/...` | `release/` + proof policy | PROPOSED / rel registration NEEDS VERIFICATION |

### `kfm:provenance` carriage obligation

When a catalog object depends on evidence or emitted artifacts, it should carry or resolve to the following provenance fields.

| Field | Expected value | Register posture |
|---|---|---|
| `spec_hash` | canonical hash of the record or governed artifact | PROPOSED |
| `evidence_bundle_ref` | resolvable EvidenceBundle URI | PROPOSED |
| `run_record_ref` | RunReceipt or pipeline run record URI | PROPOSED |
| `audit_ref` | audit/proof/attestation reference | PROPOSED |
| `policy_digest` | digest of policy bundle used for decision or promotion | PROPOSED |
| per-asset checksum | `file:checksum` or asset-specific checksum field | PROPOSED |

> [!IMPORTANT]
> A catalog record carrying `kfm:provenance` must not imply public release. It only records provenance linkage. Public release still depends on validation, policy, review, release manifest, correction path, and rollback target.

### `kfm:care` carriage obligation

When a source, dataset, feature, layer, or evidence bundle carries Indigenous, cultural, community, stewardship, consent, or authority-to-control concerns, catalog records must preserve that signal without exposing restricted details.

| Field | Meaning | Publication posture |
|---|---|---|
| `steward_org` | community, nation, organization, or steward body | restrict/redact if sensitive |
| `authority_to_control` | asserted authority/control interest | non-empty triggers default-deny review |
| `consent` | ConsentSidecar or consent record reference | never infer consent from absence |
| `obligations` | stewardship or use obligations | preserve through release |
| `benefit_commitments` | benefit-sharing or return obligations | preserve through release |
| `access_tier` | public, staged, restricted, denied, or steward-review | policy-owned |
| `redaction_reason` | reason exact data is withheld/generalized | required when transformed |

> [!CAUTION]
> `kfm:care` is not decorative metadata. If it indicates authority-to-control, cultural sensitivity, consent requirements, or community obligations, publication must fail closed until policy and review state permit release.

### KFM attestation link relation

A catalog object may include a KFM attestation link relation that points to an EvidenceBundle, proof bundle, DSSE/cosign-style attestation, or ReleaseManifest entry.

Proposed STAC link shape:

```json
{
  "rel": "kfm:attestation",
  "href": "kfm://evidence/<digest-or-id>",
  "type": "application/json",
  "title": "KFM attestation and evidence bundle"
}