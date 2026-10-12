<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-hifld-readme
title: HIFLD source family
type: readme
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for hifld>
created: 2026-05-21
updated: 2026-05-21
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/catalog/PROFILES.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md
  - docs/sources/catalog/hifld/hifld.md
  - docs/doctrine/directory-rules.md
  - docs/domains/roads-rail-trade/SOURCE_REGISTRY.md
  - docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md
  - docs/domains/hazards/SOURCE_REGISTRY.md
tags: [kfm, docs, sources, catalog, hifld, infrastructure, cross-domain, deny-default]
notes:
  - "Family scaffolded from connectors/ inventory; descriptions grounded in docs/domains SOURCE_REGISTRY files (NEEDS VERIFICATION). Beyond directory-rules.md §7.3 — see OPEN-DSC-14."
  - "v0.2: applied KFM presentation standard; added directory tree, Mermaid family-flow diagram, cross-domain landing map, and critical-infrastructure sensitivity callout grounded in C10-05 / KFM-P2-PROG-0008."
[/KFM_META_BLOCK_V2] -->

# 🏛️ `hifld` source family

> Source-oriented catalog documentation for the **HIFLD** (Homeland Infrastructure Foundation-Level Data) family — a cross-domain federal aggregator that lands in rail, settlements/infrastructure, and hazards lanes.

[![Status: draft](https://img.shields.io/badge/status-draft-blue)](#) [![Type: source--family README](https://img.shields.io/badge/type-source--family%20README-informational)](#) [![Family status: PROPOSED (beyond §7.3)](https://img.shields.io/badge/family-PROPOSED%20%28beyond%20%C2%A77.3%29-yellow)](#4-family-status) [![Scope: cross-domain](https://img.shields.io/badge/scope-cross--domain-9a6700)](#11-cross-domain-landing-map) [![Sensitivity: critical-infrastructure deny-default](https://img.shields.io/badge/sensitivity-critical--infrastructure%20deny--default-b00020)](#10-rights--sensitivity) [![Truth: receipt%E2%89%A0proof%E2%89%A0catalog%E2%89%A0publication](https://img.shields.io/badge/truth-receipt%E2%89%A0proof%E2%89%A0catalog%E2%89%A0publication-lightgrey)](#) [![ADR: pending](https://img.shields.io/badge/ADR-pending%20(OPEN--DSC--14)-yellow)](#16-open-questions)

**Status:** draft — **PROPOSED** (beyond `directory-rules.md` §7.3) · **Owners:** `<PLACEHOLDER — Docs steward + Source steward for hifld>` · **Last reviewed:** 2026-05-21

> [!IMPORTANT]
> The HIFLD family is **not** one of the nine canonical source families enumerated in `directory-rules.md` §7.3 (`usgs, fema, noaa, nrcs, kansas, gbif, inaturalist, census, local_upload`). Promotion to a canonical family is **ADR-class** per §2.4(2) and is tracked as **OPEN-DSC-14** in [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md). Until then, this folder is a documentation scaffold paired with the `connectors/hifld/` stub; nothing under this family carries canonical-family authority.

---

## Mini-TOC

- [1. Overview](#1-overview)
- [2. Scope and boundary](#2-scope-and-boundary)
- [3. Repo fit](#3-repo-fit)
- [4. Family status](#4-family-status)
- [5. Product pages](#5-product-pages)
- [6. Directory tree](#6-directory-tree)
- [7. Source authority](#7-source-authority)
- [8. Catalog profiles](#8-catalog-profiles)
- [9. Identity & namespaces](#9-identity--namespaces)
- [10. Rights & sensitivity](#10-rights--sensitivity)
- [11. Cross-domain landing map](#11-cross-domain-landing-map)
- [12. Lifecycle diagram](#12-lifecycle-diagram)
- [13. Validation](#13-validation)
- [14. Related contracts & schemas](#14-related-contracts--schemas)
- [15. Related connectors & pipelines](#15-related-connectors--pipelines)
- [16. Open questions](#16-open-questions)
- [17. Related docs](#17-related-docs)

---

## 1. Overview

**CONFIRMED (doctrine, C10-05 Rail Stack):** HIFLD (Homeland Infrastructure Foundation-Level Data) is recognized in the KFM corpus as a U.S. national geospatial program publishing foundation-level critical-infrastructure layers, paired with NTAD (National Transportation Atlas Database) for rail-infrastructure geometry (rail lines, yards, structures).

**INFERRED (from corpus context):** HIFLD's catalog reaches far beyond rail — it covers energy, communications, emergency services, education, water, and other critical-infrastructure sectors. Per-product scope, license, cadence, and Kansas-relevant subsets remain **NEEDS VERIFICATION** until inspected against the mounted SourceDescriptors in [`data/registry/sources/`](../../../../data/registry/sources/).

**PROPOSED (this family folder):** the folder was scaffolded on 2026-05-21 because a `connectors/hifld/` companion exists. The product pages below describe the **documentation surface**, not the descriptor — the descriptor is owned by `data/registry/sources/` per `directory-rules.md §7.3` and **ADR-0001**.

[Back to top](#-hifld-source-family)

---

## 2. Scope and boundary

> [!NOTE]
> **What this folder is:** a documentation lane explaining HIFLD-family sources as KFM admits them. **What it is not:** a source descriptor home, a schema home, a policy home, or a connector implementation. Those live elsewhere.

| Belongs here | Does **not** belong here | Where it goes instead |
|---|---|---|
| Per-product product-pages following [`_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md) | Source descriptors (identity, role, endpoints, cadence, terms) | [`data/registry/sources/`](../../../../data/registry/sources/) — schema home `schemas/contracts/v1/source/source-descriptor.json` per **ADR-0001** |
| Family-level overview, status, cross-domain mapping | Machine schemas for HIFLD object shapes | [`schemas/contracts/v1/`](../../../../schemas/contracts/v1/) per **ADR-0001** |
| Pointers to sibling lane docs (`IDENTITY.md`, `PROFILES.md`, etc.) | Policy / sensitivity rules | [`policy/sensitivity/`](../../../../policy/sensitivity/) — never restate policy here |
| Open-questions discussion that ripples across the family | Connector code / fetch logic | [`connectors/hifld/`](../../../../connectors/hifld/) per `directory-rules.md §7.3` |
| Cross-references to upstream `docs/domains/` SOURCE_REGISTRY entries | Pipeline orchestration | [`pipelines/`](../../../../pipelines/) per `directory-rules.md §7.4` |
| Truth-label discipline for every claim about HIFLD | Release decisions, ReleaseManifests | [`release/`](../../../../release/) |

**Authority boundary:** `docs/` **explains**; `control_plane/` **indexes**; `contracts/` **defines meaning**; `schemas/` **defines shape**; `policy/` **decides admissibility** (`directory-rules.md §6.1`). This folder is `docs/` — it carries no decision authority.

[Back to top](#-hifld-source-family)

---

## 3. Repo fit

- **Path:** `docs/sources/catalog/hifld/`
- **Parent lane:** [`docs/sources/catalog/`](../README.md) — the source-pages index across all families.
- **Connector companion:** [`connectors/hifld/`](../../../../connectors/hifld/) — **CONFIRMED this session: empty stub directory** (NEEDS VERIFICATION against mounted-repo commit).
- **Domain landings:** see §[11. Cross-domain landing map](#11-cross-domain-landing-map). HIFLD lands in **multiple** responsibility-root lanes, not one.
- **Sibling family folders:** organized one folder per source family under `docs/sources/catalog/<family>/`. Other family folders include `gbif/`, `usgs/`, `fema/`, etc. — *(NEEDS VERIFICATION of which exist in the mounted repo)*.

[Back to top](#-hifld-source-family)

---

## 4. Family status

| Aspect | Status | Basis |
|---|---|---|
| Recognition in KFM corpus | **CONFIRMED** | C10-05 Rail Stack names HIFLD explicitly alongside NTAD. |
| Listed in `directory-rules.md §7.3` canonical families | **No** | §7.3 enumerates: `usgs, fema, noaa, nrcs, kansas, gbif, inaturalist, census, local_upload`. HIFLD is not among them. |
| Connector folder presence | **CONFIRMED this session (empty stub)** | `connectors/hifld/` observed in connector inventory; **NEEDS VERIFICATION** of current commit state. |
| ADR ratifying canonical-family promotion | **Pending** | Tracked as **OPEN-DSC-14** in [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md). |
| Source descriptor in `data/registry/sources/` | **NEEDS VERIFICATION** | Folder existence and HIFLD-specific descriptor file not confirmed this session. |
| Sensitivity posture | **CONFIRMED doctrine — critical-infrastructure deny-default** | KFM-P2-PROG-0008: *"sensitive infrastructure (pump stations, gate controls) generalized or marked restricted in line with policy agreements"*. Applies family-wide. |

> [!WARNING]
> Until **OPEN-DSC-14** is closed by ADR, do not promote HIFLD-derived artifacts to PUBLISHED via the §7.3 path. Use a quarantine + steward-review route, or run through the `local_upload/` connector lane as a temporary accommodation if ADR cycles are slow.

[Back to top](#-hifld-source-family)

---

## 5. Product pages

| Page | Product | Status | Notes |
|---|---|---|---|
| [`hifld.md`](./hifld.md) | HIFLD Infrastructure Layers | PROPOSED — scaffold | Will likely fork into per-sector product pages (rail, energy, communications, water/wastewater, emergency services, etc.) as scope clarifies. **NEEDS VERIFICATION** of which sectors KFM admits. |

> [!TIP]
> When per-sector product pages are added, follow the parallel pattern from `docs/sources/catalog/gbif/` — one page per surface (e.g., `hifld-rail.md`, `hifld-energy.md`), each linking back to this README via the family badge.

[Back to top](#-hifld-source-family)

---

## 6. Directory tree

```text
docs/sources/catalog/hifld/
├── README.md                    # this file
├── hifld.md                     # PROPOSED — HIFLD Infrastructure Layers product page (scaffold)
└── _examples/                   # NEEDS VERIFICATION — sibling examples folder (PROPOSED)
    └── stac-item-example.json   # PROPOSED — shared minimal STAC + kfm:provenance example
```

**Lane-wide siblings (one level up, in `docs/sources/catalog/`):**

```text
docs/sources/catalog/
├── README.md                                       # catalog source-pages index
├── IDENTITY.md                                     # Collection-id + namespace conventions
├── PROFILES.md                                     # catalog profile lanes (STAC, DCAT, PROV-O, domain)
├── RIGHTS-AND-SENSITIVITY-MAP.md                   # per-license + per-taxon/feature sensitivity map
├── OPEN-QUESTIONS.md                               # lane-wide OPEN-DSC-* register
├── _template/
│   └── SOURCE_PRODUCT_TEMPLATE.md                  # template every product page follows
├── hifld/                                          # ← this folder
└── <other family folders>/                         # gbif/, usgs/, fema/, … (NEEDS VERIFICATION)
```

**NEEDS VERIFICATION** of every sibling and child path above against the mounted repo. The tree reflects the original draft's sibling references plus the standard `_examples/` convention from `gbif/`.

[Back to top](#-hifld-source-family)

---

## 7. Source authority

Authoritative SourceDescriptors live in [`data/registry/sources/`](../../../../data/registry/sources/) — schema home `schemas/contracts/v1/source/source-descriptor.json` per **ADR-0001** *(PROPOSED in mounted-repo evidence; NEEDS VERIFICATION)*.

**Do not duplicate descriptor fields here.** This folder explains HIFLD as a family; the descriptor is the single source of truth for identity, role, endpoints, cadence, and terms per product.

| Field | Authority home | Status here |
|---|---|---|
| SourceDescriptor (per HIFLD product) | `data/registry/sources/.../hifld/...` | **PROPOSED — Do not duplicate**; NEEDS VERIFICATION of path |
| Source role | Source-role registry (PROPOSED, KFM-P20-IDEA-0001). HIFLD role: **`aggregator`** (federal compilation) — PROPOSED | PROPOSED |
| Rights matrix | [`policy/sensitivity/`](../../../../policy/sensitivity/) + license-map JSON | See §[10](#10-rights--sensitivity) |
| Place / feature anchoring | GNIS for places (C7-09); HIFLD-specific feature IDs preserved through normalization | PROPOSED |

[Back to top](#-hifld-source-family)

---

## 8. Catalog profiles

**PROPOSED — see [`PROFILES.md`](../PROFILES.md).** Confirm per product which of the following lanes each HIFLD product lands in:

| Profile | Lane | Default for HIFLD products (PROPOSED) | Notes |
|---|---|---|---|
| **STAC** | [`data/catalog/stac/`](../../../../data/catalog/stac/) | **Yes** (vector features as STAC Items) | C4-01 `kfm:provenance` block required. |
| **DCAT Distribution** | [`data/catalog/dcat/`](../../../../data/catalog/dcat/) | **Yes** (dataset-level distribution metadata) | C4-05 — non-spatial dataset metadata. |
| **PROV-O** | [`data/catalog/prov/`](../../../../data/catalog/prov/) | **Yes** | Required when promotion edges must be inspectable. |
| **Domain projection** | [`data/catalog/domain/<domain>/`](../../../../data/catalog/domain/) | **Multiple** — see §[11](#11-cross-domain-landing-map) | HIFLD spans `roads-rail-trade`, `settlements-infrastructure`, `hazards`. |

[Back to top](#-hifld-source-family)

---

## 9. Identity & namespaces

Collection-id and namespace conventions follow [`IDENTITY.md`](../IDENTITY.md).

- **PROPOSED Collection id pattern:** `kfm-<org>-<product>` (C4-02 expansion direction). Illustrative shape for the family: `kfm-hifld-<sector>-<scope>` (e.g., `kfm-hifld-rail-kansas`). Not authoritative until [`IDENTITY.md`](../IDENTITY.md) pins it.
- **PROPOSED KFM namespace:** `kfm:` — **OPEN-DSC-03** (corpus C4-01 records `kfm:` vs `ks-kfm:` as unresolved). See [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md).
- **Authority anchoring (PROPOSED):** HIFLD feature IDs are preserved as carrier identifiers; KFM canonical IDs follow the deterministic basis *source id + object role + temporal scope + normalized digest* per the Fauna/Settlements domain-dossier identity rule. **NEEDS VERIFICATION** against `schemas/contracts/v1/` per-domain shapes.

[Back to top](#-hifld-source-family)

---

## 10. Rights & sensitivity

> [!CAUTION]
> **Critical-infrastructure deny-default.** Several HIFLD layers carry sensitivity that survives the layer's "public" label: pump stations, gate controls, dam-failure inundation, and similar features must be generalized, withheld, or routed through a steward-review path before any KFM-published derivative ships. Source: **KFM-P2-PROG-0008** (FEMA NFHL + USACE NLD/NID ingest doctrine, which generalizes to HIFLD by family analogy).

**NEEDS VERIFICATION per product** — see [`RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) and [`policy/sensitivity/`](../../../../policy/sensitivity/). **Do not restate policy here.**

| Posture | Source of doctrine | Applies to (PROPOSED) |
|---|---|---|
| Generalize at publication | KFM-P2-PROG-0008 | Geometry of sensitive control points; per-zoom generalization rules. |
| Restrict / hold for steward review | C6-01 Sensitivity Rubric 0–5 + critical-infrastructure annex | Energy switchyards, dam inundation footprints, communications cores. |
| Deny by default | Default-deny promotion (C5-02) | Any HIFLD layer where rights, license, or sensitivity posture is unknown. |
| Public-safe with attribution | (per-product, after policy resolution) | Layers with confirmed public-safe terms and no restricted features. |

[Back to top](#-hifld-source-family)

---

## 11. Cross-domain landing map

> [!NOTE]
> HIFLD is unusual: a **single source family** landing in **multiple responsibility-root domain lanes**. The corpus places HIFLD in the rail stack (C10-05); a general infrastructure / hazards landing follows by analogy with KFM-P2-PROG-0008 (FEMA NFHL + USACE NLD/NID). Per-sector ownership is **NEEDS VERIFICATION**.

| HIFLD sector (illustrative) | Primary domain lane (PROPOSED) | Domain SOURCE_REGISTRY pointer | Sensitivity posture |
|---|---|---|---|
| Rail lines, yards, structures | `roads-rail-trade` | [`docs/domains/roads-rail-trade/SOURCE_REGISTRY.md`](../../../domains/roads-rail-trade/SOURCE_REGISTRY.md) | Public-safe (geometry); generalize where it abuts security-sensitive sites |
| Pipelines, electric substations, transmission | `settlements-infrastructure` | [`docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md`](../../../domains/settlements-infrastructure/SOURCE_REGISTRY.md) | **Critical-infrastructure deny-default**; per-feature steward review |
| Dams, levees, flood-control structures | `hazards` (and overlap with `hydrology`) | [`docs/domains/hazards/SOURCE_REGISTRY.md`](../../../domains/hazards/SOURCE_REGISTRY.md) | High-stakes; KFM-P2-PROG-0008 generalization rules apply |
| Communications towers, broadcast | `settlements-infrastructure` | (as above) | Public-safe with attribution; precise coords gated |
| Emergency services (fire, EMS, hospitals) | `settlements-infrastructure` | (as above) | Public-safe; per-facility privacy review |

> [!IMPORTANT]
> When ADR closes **OPEN-DSC-14**, this table should be hardened into a per-sector registry with explicit owners and policy_label per row. Until then, treat every row as **PROPOSED** even when the doctrinal posture is CONFIRMED.

[Back to top](#-hifld-source-family)

---

## 12. Lifecycle diagram

> [!NOTE]
> The diagram below shows the **expected lifecycle** of a HIFLD-derived artifact through the KFM trust membrane. It reflects corpus doctrine (C4-01 STAC `kfm:provenance`, C5-02 default-deny promotion, KFM-P2-PROG-0008 sensitive-infrastructure generalization, watcher-as-non-publisher). **Implementation maturity remains UNKNOWN** until the `connectors/hifld/` stub gains content and OPEN-DSC-14 is resolved.

```mermaid
flowchart LR
    H["HIFLD endpoints<br/>(external — REST / ArcGIS / bulk)"] -->|connectors/hifld/<br/>(empty stub — PROPOSED)| R["data/raw/&lt;domain&gt;/hifld/&lt;run_id&gt;/<br/>RAW"]
    R -->|sector classification<br/>+ license parse| C{"license known &<br/>parseable?"}
    C -- no --> Q["data/quarantine/<br/>&lt;domain&gt;/&lt;reason&gt;/<br/>QUARANTINE"]
    C -- yes --> S{"critical-infrastructure<br/>feature?<br/>(pump, gate, switchyard,<br/>dam, levee, ...)"}
    S -- yes --> SR["Steward review<br/>+ generalization /<br/>restriction profile<br/>(KFM-P2-PROG-0008)"]
    SR -->|approved| N["pipelines/normalize<br/>EPSG:4326 + JCS spec_hash"]
    SR -->|denied| Q
    S -- no --> N
    N --> V["pipelines/validate<br/>+ sensitivity policy"]
    V -- fail closed --> Q
    V -- pass --> P["data/processed/&lt;domain&gt;/<br/>PROCESSED"]
    P --> CAT["pipelines/catalog<br/>STAC + DCAT + PROV<br/>+ domain projection"]
    CAT --> CL["data/catalog/{stac,dcat,prov,domain/...}/<br/>CATALOG"]
    CL --> EB["EvidenceBundle +<br/>RunReceipt + ProofPack"]
    EB --> J{"PromotionDecision<br/>(gates A–G)<br/>default-deny (C5-02)"}
    J -- deny / hold --> RB["RollbackCard /<br/>steward review"]
    J -- allow --> REL["release/<br/>ReleaseManifest"]
    REL --> PUB["data/published/...<br/>PUBLISHED (public-safe only)"]

    classDef quar fill:#fde0e0,stroke:#b00020,color:#000;
    classDef sens fill:#fff3e0,stroke:#c25e00,color:#000;
    classDef gate fill:#fff8e1,stroke:#9a6700,color:#000;
    classDef pub fill:#e7f5ee,stroke:#2e7d32,color:#000;
    class Q,RB quar;
    class S,SR sens;
    class C,V,J gate;
    class REL,PUB pub;
```

[Back to top](#-hifld-source-family)

---

## 13. Validation

| Check | Tool / lane | Status |
|---|---|---|
| Markdown lint | `docs/`-wide workflow | **NEEDS VERIFICATION** — workflow not yet wired |
| Link integrity (repo-relative targets) | CI workflow (PROPOSED) | NEEDS VERIFICATION |
| Per-product page conformance to [`_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md) | manual + lint (PROPOSED) | PROPOSED |
| KFM Meta Block v2 presence & validity | manual + parser (PROPOSED) | PROPOSED |
| Sibling-file presence (`IDENTITY.md`, `PROFILES.md`, `RIGHTS-AND-SENSITIVITY-MAP.md`, `OPEN-QUESTIONS.md`, `_template/`) | manual | **NEEDS VERIFICATION** — confirmed in prior session, not re-confirmed this session |
| Truth-label discipline (no fabricated paths / owners / dates) | reviewer | enforced by review |

[Back to top](#-hifld-source-family)

---

## 14. Related contracts & schemas

- [`schemas/contracts/v1/source/`](../../../../schemas/contracts/v1/source/) — machine SourceDescriptor shape per **ADR-0001**.
- [`contracts/`](../../../../contracts/) — object families. NEEDS VERIFICATION of HIFLD-relevant subtrees: `contracts/domains/roads-rail-trade/`, `contracts/domains/settlements-infrastructure/`, `contracts/domains/hazards/`.
- [`contracts/evidence/`](../../../../contracts/evidence/) — EvidenceBundle / EvidenceRef contracts (KFM-P26-PROG-0004 / -0005).

[Back to top](#-hifld-source-family)

---

## 15. Related connectors & pipelines

- **Connector folder:** [`connectors/hifld/`](../../../../connectors/hifld/) — **all currently empty stubs (CONFIRMED this session; NEEDS VERIFICATION against mounted repo commit).** Per `directory-rules.md §7.3`, this folder's output MUST go to `data/raw/<domain>/hifld/<run_id>/` or `data/quarantine/...`, with source descriptors, checksums, and ingest receipts — never directly to `data/processed/`, `data/catalog/`, or `data/published/`.
- **Pipeline lanes:** [`pipelines/ingest/`](../../../../pipelines/ingest/), [`pipelines/normalize/`](../../../../pipelines/normalize/), [`pipelines/validate/`](../../../../pipelines/validate/), [`pipelines/catalog/`](../../../../pipelines/catalog/).
- **Declarative specs:** [`pipeline_specs/roads-rail-trade/`](../../../../pipeline_specs/roads-rail-trade/), [`pipeline_specs/settlements-infrastructure/`](../../../../pipeline_specs/settlements-infrastructure/), [`pipeline_specs/hazards/`](../../../../pipeline_specs/hazards/) — per-domain declarative specs (NEEDS VERIFICATION).

[Back to top](#-hifld-source-family)

---

## 16. Open questions

| ID | Question | Class | Status |
|---|---|---|---|
| **OPEN-DSC-14** | Should the HIFLD family be promoted to a canonical `directory-rules.md §7.3` family via ADR? If yes, which §7.3 family does it sit alongside (e.g., as a tenth slot), and what is its primary domain lane? | governance / ADR | **OPEN** — promotion is ADR-class per §2.4(2). |
| OPEN-HIFLD-01 | Confirm per-product **rights, license, cadence, and endpoints** (REST / ArcGIS FeatureService / bulk download). | ops | **NEEDS VERIFICATION** |
| OPEN-HIFLD-02 | Confirm the **per-sector domain-landing map** (§[11](#11-cross-domain-landing-map)) against `docs/domains/*/SOURCE_REGISTRY.md` files; harden into a registry with owners and policy_labels. | catalog | **OPEN** |
| OPEN-HIFLD-03 | Confirm the **critical-infrastructure feature list** that triggers steward review under the KFM-P2-PROG-0008 generalization doctrine. | policy | **OPEN** — must be codified in `policy/sensitivity/`, not here. |
| OPEN-HIFLD-04 | Confirm the **HIFLD ↔ GCIS coordinate-disagreement policy** for shared rail-crossing features (corpus open question, C10-05). | catalog / authority | **OPEN** |
| OPEN-DSC-03 | KFM namespace token (`kfm:` vs `ks-kfm:`) for STAC Collection summaries. | identity | **OPEN** — corpus C4-01 records this as unresolved. |
| OPEN-DSC-* | Lane-wide open items — see [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md). | various | various |

[Back to top](#-hifld-source-family)

---

## 17. Related docs

- [`docs/sources/catalog/README.md`](../README.md) — catalog source-pages index
- [`docs/sources/catalog/OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) — lane-wide `OPEN-DSC-*` register
- [`docs/sources/catalog/PROFILES.md`](../PROFILES.md) — catalog profile lanes
- [`docs/sources/catalog/IDENTITY.md`](../IDENTITY.md) — Collection-id + namespace conventions
- [`docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) — per-license + per-feature sensitivity map
- [`docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md) — template for product pages under this folder
- [`docs/sources/catalog/hifld/hifld.md`](./hifld.md) — HIFLD Infrastructure Layers product page
- [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — placement, lifecycle, and naming authority
- [`docs/domains/roads-rail-trade/SOURCE_REGISTRY.md`](../../../domains/roads-rail-trade/SOURCE_REGISTRY.md), [`settlements-infrastructure/SOURCE_REGISTRY.md`](../../../domains/settlements-infrastructure/SOURCE_REGISTRY.md), [`hazards/SOURCE_REGISTRY.md`](../../../domains/hazards/SOURCE_REGISTRY.md) — per-domain source registries (NEEDS VERIFICATION)

<details>
<summary>📎 Appendix — corpus citations grounding this README</summary>

- **C10-05 Rail Stack** (CONFIRMED) — "HIFLD (Homeland Infrastructure Foundation-Level Data) and NTAD (National Transportation Atlas Database) provide the geospatial layers for rail lines, yards, and structures."
- **KFM-P2-PROG-0008** (PROPOSED, Pass 32) — sensitive infrastructure (pump stations, gate controls) generalized or marked restricted in line with policy agreements; doctrine generalized by analogy to the HIFLD family.
- **C4-01 STAC `kfm:provenance`** (CONFIRMED) — `spec_hash`, `evidence_bundle_ref`, `run_record_ref`, `audit_ref`, `policy_digest`; per-asset `file:checksum`.
- **C4-02 STAC Collection identity** (CONFIRMED expansion direction) — `kfm-<org>-<product>` Collection id pattern.
- **C4-05 DCAT Distribution** (CONFIRMED) — dataset-level metadata for non-spatial / non-spatiotemporal data.
- **C5-02 Default-deny promotion** (CONFIRMED) — promotion fails closed; explicit allow-rule required.
- **C6-01 Sensitivity Rubric 0–5** (CONFIRMED) — six-level rubric from public to highest-restricted.
- **C7-09 GNIS** (CONFIRMED) — USGS Geographic Names Information System as the federal authority for U.S. place names; relevant for HIFLD feature anchoring.
- **`directory-rules.md §7.3`** (CONFIRMED) — nine canonical connector families: `usgs, fema, noaa, nrcs, kansas, gbif, inaturalist, census, local_upload`.
- **`directory-rules.md §2.4(2)`** (CONFIRMED) — adding a canonical root or family is ADR-class.
- **ADR-0001** (PROPOSED in mounted-repo evidence) — schemas/contracts/v1/ as schema home.

</details>

---

<sub>**Last reviewed:** 2026-05-21 *(Claude Code source-family README polish session; KFM presentation standard v2 applied)* · **Version:** v0.2 (draft) · **Doc ID:** `kfm://doc/docs-sources-catalog-hifld-readme` · [Back to top ↑](#-hifld-source-family)</sub>
