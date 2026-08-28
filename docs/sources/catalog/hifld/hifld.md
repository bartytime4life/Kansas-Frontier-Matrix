<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-hifld-hifld
title: HIFLD Infrastructure Layers
type: product-page
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for hifld>
created: 2026-05-21
updated: 2026-05-21
policy_label: public
related:
  - docs/sources/catalog/hifld/README.md
  - docs/sources/catalog/hifld/_examples/stac-item-example.json
  - docs/sources/catalog/README.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/PROFILES.md
  - docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md
  - docs/doctrine/directory-rules.md
  - docs/standards/PROV.md
  - docs/domains/roads-rail-trade/SOURCE_REGISTRY.md
  - docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md
  - docs/domains/hazards/SOURCE_REGISTRY.md
tags: [kfm, docs, sources, catalog, hifld, infrastructure, cross-domain, deny-default, rail]
notes:
  - "PROPOSED product-page scaffold; description grounded in docs/domains SOURCE_REGISTRY files (NEEDS VERIFICATION)."
  - "v0.2: applied KFM presentation standard; added corpus-CONFIRMED C10-05 rail-stack anchoring, critical-infrastructure deny-default emphasis (KFM-P2-PROG-0008 analogy), HIFLD↔GCIS coordinate-disagreement open question, and cross-domain landing table."
[/KFM_META_BLOCK_V2] -->

# 🏗️ HIFLD Infrastructure Layers

> HIFLD geospatial critical-infrastructure layers — corpus-anchored in **rail** (C10-05) and extended by analogy to other infrastructure sectors, with **critical-infrastructure deny-default** as the operational posture.

[![Status: draft](https://img.shields.io/badge/status-draft-blue)](#) [![Type: product-page](https://img.shields.io/badge/type-product--page-informational)](#) [![Family: hifld](https://img.shields.io/badge/family-hifld-2e7d32)](./README.md) [![Family status: PROPOSED (beyond §7.3)](https://img.shields.io/badge/family-PROPOSED%20%28beyond%20%C2%A77.3%29-yellow)](./README.md#4-family-status) [![Corpus sector: rail (CONFIRMED)](https://img.shields.io/badge/corpus%20sector-rail%20(CONFIRMED%2C%20C10--05)-blueviolet)](#1-overview) [![Sensitivity: critical-infrastructure deny-default](https://img.shields.io/badge/sensitivity-critical--infrastructure%20deny--default-b00020)](#9-rights-and-sensitivity) [![Truth: receipt%E2%89%A0proof%E2%89%A0catalog%E2%89%A0publication](https://img.shields.io/badge/truth-receipt%E2%89%A0proof%E2%89%A0catalog%E2%89%A0publication-lightgrey)](#) [![ADR: pending (OPEN-DSC-14)](https://img.shields.io/badge/ADR-pending%20(OPEN--DSC--14)-yellow)](#15-open-questions)

**Status:** PROPOSED — scaffold + v0.2 polish · **Family:** [`hifld`](./README.md) · **Owners:** `<PLACEHOLDER — Docs steward + Source steward for hifld>` · **Last reviewed:** 2026-05-21

> [!IMPORTANT]
> The `hifld` family is **not** one of the nine canonical `directory-rules.md §7.3` source families. Promotion to canonical status is ADR-class and tracked as **OPEN-DSC-14**. Until the ADR closes, **do not promote HIFLD-derived artifacts to PUBLISHED via the standard §7.3 path** — use a quarantine + steward-review route, or run through the `local_upload/` connector lane as a temporary accommodation. See [`README.md`](./README.md#4-family-status) for the family-level status.

---

## Mini-TOC

- [1. Overview](#1-overview)
- [2. Source authority](#2-source-authority)
- [3. Catalog profiles used](#3-catalog-profiles-used)
- [4. Collection identity](#4-collection-identity)
- [5. Provenance fields](#5-provenance-fields)
- [6. Temporal handling](#6-temporal-handling)
- [7. Geometry and projection](#7-geometry-and-projection)
- [8. Cross-domain landing](#8-cross-domain-landing)
- [9. Rights and sensitivity](#9-rights-and-sensitivity)
- [10. Validation and catalog closure](#10-validation-and-catalog-closure)
- [11. Related contracts and schemas](#11-related-contracts-and-schemas)
- [12. Related connectors and pipelines](#12-related-connectors-and-pipelines)
- [13. Lifecycle diagram](#13-lifecycle-diagram)
- [14. Examples](#14-examples)
- [15. Open questions](#15-open-questions)
- [16. Related docs](#16-related-docs)

---

## 1. Overview

**CONFIRMED (doctrine, C10-05 Rail Stack):** HIFLD (Homeland Infrastructure Foundation-Level Data) is paired with NTAD (National Transportation Atlas Database) as the geospatial source for *"rail lines, yards, and structures"* in the KFM rail stack alongside FRA GCIS (grade-crossing inventory), FRA Form 57 (incident reports), and STB Class I weekly reports.

**INFERRED — sector breadth:** HIFLD publishes far beyond rail (energy, communications, water/wastewater, emergency services, dams/levees, transportation generally). Per-sector inclusion in KFM is **NEEDS VERIFICATION**; only the rail sector has explicit corpus grounding. The doctrine that *"sensitive infrastructure (pump stations, gate controls) generalized or marked restricted"* (KFM-P2-PROG-0008) generalizes by analogy and is the operational basis for §[9. Rights and sensitivity](#9-rights-and-sensitivity).

**PROPOSED — this product instance:** scope, refresh cadence, geographic filter (Kansas-anchored vs national), current endpoint URLs (REST FeatureService / ArcGIS Online / bulk download), license matrix snapshot, and rights status are all **NEEDS VERIFICATION** against the mounted SourceDescriptor in `data/registry/sources/`.

> [!TIP]
> Where HIFLD geometry **disagrees with FRA GCIS** coordinates for the same rail-crossing feature, the corpus flags this as an unresolved authority-tiebreak question (C10-05 Open Question, captured here as **OPEN-HIFLD-IL-04**).

[Back to top](#-hifld-infrastructure-layers)

---

## 2. Source authority

| Field | Authoritative home | Status here |
|---|---|---|
| SourceDescriptor (identity, role, endpoints, cadence, terms) | [`data/registry/sources/`](../../../../data/registry/sources/) — schema home `schemas/contracts/v1/source/source-descriptor.json` per **ADR-0001** | **Do not duplicate** here (PROPOSED; NEEDS VERIFICATION of descriptor file presence) |
| Source role | Source-role registry (PROPOSED, KFM-P20-IDEA-0001). HIFLD role: **`aggregator`** (federal compilation of agency / vendor source data) — PROPOSED | PROPOSED |
| Rights / license matrix | [`policy/sensitivity/`](../../../../policy/sensitivity/) + license-map JSON | See §[9. Rights and sensitivity](#9-rights-and-sensitivity) |
| Place / feature anchoring | GNIS for U.S. place names (**CONFIRMED, C7-09**); HIFLD-native feature IDs preserved as carrier identifiers | PROPOSED realization |
| Sister sources for join discipline | FRA GCIS, FRA Form 57, STB Class I, NTAD (C10-05) | CONFIRMED stack membership |

[Back to top](#-hifld-infrastructure-layers)

---

## 3. Catalog profiles used

**PROPOSED.** Per [`PROFILES.md`](../PROFILES.md), HIFLD products land in the four lanes below. Realization per sector is **NEEDS VERIFICATION**.

| Profile | Lane | Default for HIFLD Infrastructure Layers (PROPOSED) | Notes |
|---|---|---|---|
| **STAC** | [`data/catalog/stac/`](../../../../data/catalog/stac/) | **Yes** | Vector features as STAC `Feature` Items with `kfm:provenance` block (C4-01). |
| **DCAT Distribution** | [`data/catalog/dcat/`](../../../../data/catalog/dcat/) | **Yes** | Dataset-level metadata for sector layers (C4-05). |
| **PROV-O** | [`data/catalog/prov/`](../../../../data/catalog/prov/) | **Yes** | Required when promotion edges must be inspectable; especially for ADR-pending family. |
| **Domain projection** | [`data/catalog/domain/<domain>/`](../../../../data/catalog/domain/) | **Multiple** — see §[8. Cross-domain landing](#8-cross-domain-landing) | HIFLD spans `roads-rail-trade`, `settlements-infrastructure`, `hazards`. |

> [!NOTE]
> **Catalog closure must distinguish HIFLD from co-located federal sources.** A rail Item derived from HIFLD geometry should not silently merge with one derived from NTAD or GCIS; provenance `source_descriptor_ref` MUST disambiguate. See §[5. Provenance fields](#5-provenance-fields).

[Back to top](#-hifld-infrastructure-layers)

---

## 4. Collection identity

- **PROPOSED Collection id pattern:** `kfm-<org>-<product>` (corpus expansion direction, C4-02). Illustrative shape: `kfm-hifld-rail-kansas`, `kfm-hifld-pipelines-kansas`, `kfm-hifld-dams-kansas`. Not authoritative until [`IDENTITY.md`](../IDENTITY.md) pins.
- **PROPOSED KFM namespace:** `kfm:` — **OPEN-DSC-03** (corpus C4-01 records `kfm:` vs `ks-kfm:` as unresolved).
- **PROPOSED — one Collection per sector**, not one Collection for all HIFLD layers. Sectors carry distinct sensitivity postures (a rail-line Collection is public-safe; a pipeline / switchyard Collection is critical-infrastructure deny-default). Mixing them in one Collection collapses trust class.
- **Asset roles:** NEEDS VERIFICATION — confirm against `schemas/contracts/v1/source/` and any STAC asset-role conventions adopted by the catalog lane README.

[Back to top](#-hifld-infrastructure-layers)

---

## 5. Provenance fields

**CONFIRMED (C4-01):** STAC Items carry an `item.properties.kfm:provenance` block. Per-asset integrity is recorded as STAC `file:checksum`.

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "properties": {
    "datetime": "<observed/event ISO-8601>",
    "kfm:provenance": {
      "spec_hash": "sha256:<JCS-canonicalized record hash>",
      "evidence_bundle_ref": "kfm://evidence/<digest>",
      "run_record_ref": "kfm://run/<run-id>",
      "audit_ref": "kfm://audit/<attestation-id>",
      "policy_digest": "sha256:<policy bundle digest>",

      "source_descriptor_ref": "kfm://source/hifld/<sector>",
      "source_aggregator": "hifld",
      "source_original_publisher": "<agency or vendor as reported by HIFLD>",
      "hifld_layer_id": "<HIFLD-native layer identifier>",
      "hifld_feature_id": "<HIFLD-native feature id>",
      "sector": "rail | energy | water | communications | emergency_services | dams | ..."
    },
    "redaction_profile": "<public-safe profile id or null>"
  },
  "assets": {
    "data": { "href": "...", "file:checksum": "sha256:<asset-bytes>" }
  }
}
```

| Field | Required for HIFLD? | Source of authority |
|---|---|---|
| `spec_hash`, `evidence_bundle_ref`, `run_record_ref`, `audit_ref`, `policy_digest`, `file:checksum` | **Yes** (same as all KFM STAC Items) | **CONFIRMED (C4-01)** |
| `source_descriptor_ref` | **Yes** | PROPOSED extension — disambiguates HIFLD from co-located federal sources (NTAD, GCIS). |
| `source_aggregator: "hifld"` | **Yes** | PROPOSED — makes the aggregator role inspectable at the catalog level. |
| `source_original_publisher` | **Yes where known** | PROPOSED — HIFLD records often carry an upstream provenance string (agency or vendor); preserve it. |
| `hifld_layer_id`, `hifld_feature_id` | **Yes** | PROPOSED — carrier identifiers needed for the HIFLD↔GCIS reconciliation (see **OPEN-HIFLD-IL-04**). |
| `sector` | **Yes** | PROPOSED — drives Collection routing (§[4](#4-collection-identity)) and sensitivity policy (§[9](#9-rights-and-sensitivity)). |

[Back to top](#-hifld-infrastructure-layers)

---

## 6. Temporal handling

**CONFIRMED doctrine:** source, observed, valid, retrieval, release, and correction times stay **distinct** where material. For HIFLD layers, the dominant temporal facts are publish-time of the HIFLD release and retrieval-time of the KFM fetch.

| Time concept | Carrier (PROPOSED) | HIFLD-specific notes |
|---|---|---|
| **source time** | HIFLD layer attribute (e.g., `EFFECTIVE_DATE`, `LAST_UPDATE` — NEEDS VERIFICATION per layer) | HIFLD layers vary widely in how they report this. |
| **observed time** | Sector-specific; e.g., commissioning year for a dam, last-survey date for a rail crossing | NEEDS VERIFICATION per sector. |
| **valid time** | EvidenceBundle `valid_from` / `valid_to` (PROPOSED) | Default valid window: one HIFLD release cycle (NEEDS VERIFICATION of HIFLD cadence). |
| **retrieval time** | `RunReceipt.fetched_at` | Records when KFM pulled the layer. |
| **release time** | `ReleaseManifest.released_at` | When the KFM derivative was published. |
| **correction time** | `CorrectionNotice.corrected_at` | Common for HIFLD: feature geometry revisions across releases. |

> [!CAUTION]
> **HIFLD release cadence is not uniform across layers.** Some layers refresh annually; others irregularly. The retrieval-time anchor is operationally critical for HIFLD; do not assume "current" without inspecting the RunReceipt.

[Back to top](#-hifld-infrastructure-layers)

---

## 7. Geometry and projection

- **PROPOSED:** Normalize to **EPSG:4326** at admission, preserving original projection metadata in `kfm:provenance.source_native_crs` (PROPOSED extension). HIFLD layers historically have been served in Web Mercator / WGS84 variants — **NEEDS VERIFICATION** per layer.
- **PROPOSED:** STAC Projection fields (`proj:code`, `proj:bbox`, `proj:geometry`, `proj:shape`, `proj:transform`) lint-checked against **KFM-P27-FEAT-0003** ("STAC Projection lint report").
- **PROPOSED (KFM-P2-PROG-0008 analogy):** deliver derived public-safe layers as compact MVT/PMTiles with per-zoom generalization and minimal attributes; sensitive feature classes (control points, switchyards, gate structures, dam-failure inundation) are **generalized or restricted in line with policy agreements** — see §[9](#9-rights-and-sensitivity).
- **NEEDS VERIFICATION:** specific generalization parameters per sector and per zoom level.

[Back to top](#-hifld-infrastructure-layers)

---

## 8. Cross-domain landing

> [!NOTE]
> HIFLD is a **single source family** that lands in **multiple responsibility-root domain lanes**. Per-sector ownership is **NEEDS VERIFICATION**; the corpus only nails rail explicitly (C10-05). Other sectors are PROPOSED-by-analogy.

| HIFLD sector | Primary domain lane (PROPOSED) | Domain SOURCE_REGISTRY pointer | Sensitivity posture | Corpus grounding |
|---|---|---|---|---|
| Rail lines, yards, structures | `roads-rail-trade` | [`docs/domains/roads-rail-trade/SOURCE_REGISTRY.md`](../../../domains/roads-rail-trade/SOURCE_REGISTRY.md) | Public-safe (geometry); generalize near security-sensitive sites | **CONFIRMED, C10-05** |
| Pipelines, electric substations, transmission | `settlements-infrastructure` | [`docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md`](../../../domains/settlements-infrastructure/SOURCE_REGISTRY.md) | **Critical-infrastructure deny-default**; per-feature steward review | PROPOSED (KFM-P2-PROG-0008 analogy) |
| Dams, levees, flood-control structures | `hazards` (overlap with `hydrology`) | [`docs/domains/hazards/SOURCE_REGISTRY.md`](../../../domains/hazards/SOURCE_REGISTRY.md) | High-stakes; KFM-P2-PROG-0008 generalization rules apply | CONFIRMED doctrine generalized by analogy |
| Communications towers, broadcast | `settlements-infrastructure` | (as above) | Public-safe with attribution; precise coords gated | PROPOSED |
| Emergency services (fire, EMS, hospitals) | `settlements-infrastructure` | (as above) | Public-safe; per-facility privacy review | PROPOSED |
| Water / wastewater treatment, pump stations | `hydrology` (overlap with `settlements-infrastructure`) | NEEDS VERIFICATION | **Critical-infrastructure deny-default** (pump stations / gate controls explicitly named in KFM-P2-PROG-0008) | CONFIRMED doctrine, PROPOSED routing |

> [!IMPORTANT]
> When **OPEN-DSC-14** closes by ADR, this table should be hardened into a per-sector registry with explicit owners and `policy_label` per row. Until then, treat each row as **PROPOSED** even when the doctrinal posture is CONFIRMED.

[Back to top](#-hifld-infrastructure-layers)

---

## 9. Rights and sensitivity

> [!CAUTION]
> **Critical-infrastructure deny-default is the central operating constraint for this product.** Many HIFLD features carry sensitivity that survives the layer's nominal "public" label: pump stations, gate controls, dam-failure inundation, energy switchyards, communications cores, treatment-plant control points. Each must be **generalized, withheld, or routed through steward review** before any KFM-published derivative ships. Source: **KFM-P2-PROG-0008** (FEMA NFHL + USACE NLD/NID doctrine, generalized by analogy to the HIFLD family).

**NEEDS VERIFICATION per product / per sector** — see [`policy/sensitivity/`](../../../../policy/sensitivity/) and [`RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md). **Do not restate policy here.**

| Posture | Trigger (PROPOSED) | Doctrine source |
|---|---|---|
| **Generalize at publication** | Sensitive control-point features (pumps, gates, switchyards) within an otherwise-public layer | KFM-P2-PROG-0008 |
| **Restrict / hold for steward review** | Dam inundation footprints; energy switchyard inventories; communications cores | C6-01 Sensitivity Rubric 0–5 + critical-infrastructure annex |
| **Deny by default** | Any HIFLD layer where license, terms, or feature-class sensitivity is unknown / unparseable | Default-deny promotion (C5-02) |
| **Public-safe with attribution** | Layers with confirmed public-safe terms **and** no restricted feature classes | (per-product, after policy resolution) |

[Back to top](#-hifld-infrastructure-layers)

---

## 10. Validation and catalog closure

- **CONFIRMED doctrine (Pass-10 / KFM-P1-IDEA-0020):** Catalog closure is the final discoverability and accountability gate before public release.
- **PROPOSED HIFLD-specific gate:** an Item with `kfm:provenance.sector` in the critical-infrastructure set **AND** missing a `redaction_profile` is **denied promotion**.
- **PROPOSED HIFLD-specific gate:** an Item that shares a feature anchor (e.g., a rail crossing) with a corresponding FRA GCIS Item but with **coordinate disagreement** above a threshold is held for steward review — see **OPEN-HIFLD-IL-04**.
- **PROPOSED (KFM-P27-FEAT-0003):** STAC Projection lint as a fail-closed gate.
- **PROPOSED (KFM-P22-PROG-0037):** STAC checksum closure against the `ReleaseManifest` digest.
- **PROPOSED (KFM-P27-PROG-0012 / -0013):** `run_catalog_qa.py` + `catalog-qa` GitHub workflow. **NEEDS VERIFICATION** against `directory-rules.md §7.5.a` and OPEN-DR-07.

[Back to top](#-hifld-infrastructure-layers)

---

## 11. Related contracts and schemas

- `contracts/domains/roads-rail-trade/`, `contracts/domains/settlements-infrastructure/`, `contracts/domains/hazards/` — semantic contracts for the per-sector landings. **NEEDS VERIFICATION.**
- `schemas/contracts/v1/source/` — canonical SourceDescriptor home per **ADR-0001** (PROPOSED in mounted-repo evidence; **NEEDS VERIFICATION**).
- `contracts/evidence/` — EvidenceBundle / EvidenceRef contracts (KFM-P26-PROG-0004 / -0005).

[Back to top](#-hifld-infrastructure-layers)

---

## 12. Related connectors and pipelines

- [`connectors/hifld/`](../../../../connectors/hifld/) — source-specific fetch and admission per `directory-rules.md §7.3`. **CONFIRMED this session: empty stub** (NEEDS VERIFICATION against mounted-repo commit). Outputs must go to `data/raw/<domain>/hifld/<run_id>/` or `data/quarantine/...`; **does not publish**.
- `pipelines/ingest/`, `pipelines/normalize/`, `pipelines/validate/`, `pipelines/catalog/` — executable pipeline lanes per `directory-rules.md §7.4`.
- `pipeline_specs/roads-rail-trade/`, `pipeline_specs/settlements-infrastructure/`, `pipeline_specs/hazards/` — declarative pipeline specs (NEEDS VERIFICATION).

[Back to top](#-hifld-infrastructure-layers)

---

## 13. Lifecycle diagram

> [!NOTE]
> The diagram shows the **expected lifecycle** of a HIFLD Item through the KFM trust membrane. It reflects corpus doctrine (C4-01 `kfm:provenance`, C5-02 default-deny promotion, KFM-P2-PROG-0008 critical-infrastructure generalization, watcher-as-non-publisher). **Implementation maturity remains UNKNOWN** until `connectors/hifld/` gains content and OPEN-DSC-14 is resolved.

```mermaid
flowchart LR
    H["HIFLD endpoints<br/>(external — REST / ArcGIS / bulk)"] -->|connectors/hifld/<br/>(empty stub — PROPOSED)| R["data/raw/&lt;domain&gt;/hifld/&lt;run_id&gt;/<br/>RAW"]
    R -->|sector classification<br/>+ license parse| L{"license known &<br/>parseable?"}
    L -- no --> Q["data/quarantine/<br/>&lt;domain&gt;/&lt;reason&gt;/<br/>QUARANTINE"]
    L -- yes --> SEC["Tag sector<br/>(rail / energy / water /<br/>communications / dams / ...)"]
    SEC --> CI{"critical-infrastructure<br/>feature class?<br/>(pumps, gates, switchyards,<br/>dams, levees, ...)"}
    CI -- yes --> SR["Steward review<br/>+ generalization /<br/>restriction profile<br/>(KFM-P2-PROG-0008)"]
    SR -->|approved| N["pipelines/normalize<br/>EPSG:4326 + JCS spec_hash"]
    SR -->|denied| Q
    CI -- no --> N
    N --> CR{"HIFLD↔GCIS coord<br/>disagreement?<br/>(C10-05 open question)"}
    CR -- yes --> SR2["Hold for steward<br/>tiebreak<br/>(OPEN-HIFLD-IL-04)"]
    SR2 --> N2["normalize (continued)"]
    CR -- no --> N2
    N2 --> V["pipelines/validate<br/>+ sensitivity policy"]
    V -- fail closed --> Q
    V -- pass --> P["data/processed/&lt;domain&gt;/<br/>PROCESSED"]
    P --> CAT["pipelines/catalog<br/>STAC + DCAT + PROV<br/>+ domain projection"]
    CAT --> CL["data/catalog/{stac,dcat,prov,domain/...}/<br/>CATALOG"]
    CL --> EB["EvidenceBundle +<br/>RunReceipt + ProofPack"]
    EB --> J{"PromotionDecision<br/>(gates A–G)<br/>default-deny (C5-02)<br/>+ sector-aware gate"}
    J -- deny / hold --> RB["RollbackCard /<br/>steward review"]
    J -- allow --> REL["release/<br/>ReleaseManifest"]
    REL --> PUB["data/published/...<br/>PUBLISHED (public-safe only)"]

    classDef quar fill:#fde0e0,stroke:#b00020,color:#000;
    classDef sens fill:#fff3e0,stroke:#c25e00,color:#000;
    classDef gate fill:#fff8e1,stroke:#9a6700,color:#000;
    classDef pub fill:#e7f5ee,stroke:#2e7d32,color:#000;
    class Q,RB quar;
    class CI,SR,CR,SR2 sens;
    class L,V,J gate;
    class REL,PUB pub;
```

[Back to top](#-hifld-infrastructure-layers)

---

## 14. Examples

*Illustrative only — do not treat as authoritative.*

See [`_examples/stac-item-example.json`](../_examples/stac-item-example.json) for the family-shared minimal STAC + `kfm:provenance` shape *(PROPOSED sibling; NEEDS VERIFICATION)*.

<details>
<summary>📄 Illustrative STAC Item fragment for a HIFLD rail-line feature</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-hifld-rail-<uuid>",
  "collection": "kfm-hifld-rail-kansas",
  "geometry": { "type": "LineString", "coordinates": [[-98.0, 38.5], [-97.95, 38.51]] },
  "properties": {
    "datetime": "<HIFLD release date>",
    "proj:code": "EPSG:4326",
    "kfm:provenance": {
      "spec_hash": "sha256:abc…",
      "evidence_bundle_ref": "kfm://evidence/sha256:def…",
      "run_record_ref": "kfm://run/run-2026-05-21-001",
      "audit_ref": "kfm://audit/attest-…",
      "policy_digest": "sha256:ghi…",
      "source_descriptor_ref": "kfm://source/hifld/rail",
      "source_aggregator": "hifld",
      "source_original_publisher": "<as reported by HIFLD>",
      "hifld_layer_id": "<HIFLD layer id>",
      "hifld_feature_id": "<HIFLD feature id>",
      "sector": "rail",
      "source_native_crs": "EPSG:4326"
    },
    "redaction_profile": null
  },
  "assets": {
    "data": {
      "href": "../data.parquet",
      "type": "application/vnd.apache.parquet",
      "file:checksum": "sha256:jkl…"
    }
  },
  "links": [
    { "rel": "collection", "href": "../collection.json" },
    { "rel": "self", "href": "./item.json" }
  ]
}
```

</details>

<details>
<summary>⚠️ Illustrative <em>denied</em> Item fragment for a critical-infrastructure feature</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-hifld-pipelines-<uuid>",
  "collection": "kfm-hifld-pipelines-kansas",
  "geometry": "<REDACTED — generalization profile applied>",
  "properties": {
    "datetime": "<HIFLD release date>",
    "kfm:provenance": { "...": "..." },
    "sector": "energy",
    "redaction_profile": "critical-infrastructure-generalize-county",
    "policy_decision": "RESTRICT — steward review approved generalized derivative; precise geometry withheld"
  }
}
```

> Note: the `policy_decision` field shown here is illustrative; concrete carrier name and shape live in `contracts/`/`schemas/contracts/v1/` and are PROPOSED, not pinned.

</details>

[Back to top](#-hifld-infrastructure-layers)

---

## 15. Open questions

| ID | Question | Class | Status |
|---|---|---|---|
| **OPEN-DSC-14** | Should the `hifld` family be promoted to a canonical `directory-rules.md §7.3` family? | governance / ADR | **OPEN** (family-level; see [`README.md`](./README.md#4-family-status)) |
| OPEN-HIFLD-IL-01 | Confirm current **endpoint URLs** (REST FeatureService / ArcGIS Online / bulk) and **per-layer cadence**. | ops | **NEEDS VERIFICATION** |
| OPEN-HIFLD-IL-02 | Confirm **license matrix** per HIFLD layer (federal public-domain default; per-layer exceptions). | rights | **NEEDS VERIFICATION** |
| OPEN-HIFLD-IL-03 | Confirm the **critical-infrastructure feature-class list** that triggers steward review (KFM-P2-PROG-0008 generalization). | policy | **OPEN** — must be codified in `policy/sensitivity/`, not here. |
| **OPEN-HIFLD-IL-04** | **HIFLD ↔ GCIS coordinate-disagreement policy** for shared rail-crossing features (corpus-flagged open question, C10-05). Default tiebreaker direction (GCIS authoritative? HIFLD authoritative? steward review?) | catalog / authority | **OPEN — corpus-flagged** |
| OPEN-HIFLD-IL-05 | Should **each HIFLD sector** get its own STAC Collection, or share Collections with co-located federal sources (NTAD, GCIS, NFHL)? | catalog | **OPEN** — recommendation: per-sector HIFLD Collections (trust-class legibility argument). |
| OPEN-HIFLD-IL-06 | Should KFM publish **derived cross-source layers** (e.g., HIFLD rail × GCIS crossings × Form 57 incidents) as research-derived artifacts? | doctrine | **OPEN** — corpus expansion direction (C10-05 suggested future work). |
| OPEN-DSC-03 | KFM namespace token (`kfm:` vs `ks-kfm:`) for STAC Collection summaries. | identity | **OPEN** — corpus C4-01 unresolved. |
| OPEN-DSC-* | Lane-wide open items — see [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md). | various | various |

[Back to top](#-hifld-infrastructure-layers)

---

## 16. Related docs

- [`docs/sources/catalog/hifld/README.md`](./README.md) — family landing page (status, scope, cross-domain landing map)
- [`docs/sources/catalog/README.md`](../README.md) — catalog source-pages index
- [`docs/sources/catalog/IDENTITY.md`](../IDENTITY.md) — Collection-id + namespace conventions
- [`docs/sources/catalog/PROFILES.md`](../PROFILES.md) — catalog profile lanes
- [`docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) — per-license + per-feature sensitivity map
- [`docs/sources/catalog/OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) — lane-wide `OPEN-DSC-*` register
- [`docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md) — template every product page follows
- [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — placement, lifecycle, and naming authority
- [`docs/standards/PROV.md`](../../../standards/PROV.md) — W3C PROV-O profile (note: filename `PROV.md` vs corpus `PROVENANCE.md` is **OPEN-DR-01** in `directory-rules.md §18`)
- [`docs/domains/roads-rail-trade/SOURCE_REGISTRY.md`](../../../domains/roads-rail-trade/SOURCE_REGISTRY.md), [`settlements-infrastructure/SOURCE_REGISTRY.md`](../../../domains/settlements-infrastructure/SOURCE_REGISTRY.md), [`hazards/SOURCE_REGISTRY.md`](../../../domains/hazards/SOURCE_REGISTRY.md) — per-domain source registries (NEEDS VERIFICATION)

<details>
<summary>📎 Appendix — corpus citations grounding this product page</summary>

- **C10-05 Rail Stack** (CONFIRMED) — names HIFLD/NTAD explicitly as the geospatial layer source for rail lines, yards, and structures; flags the HIFLD↔GCIS coordinate-disagreement open question.
- **KFM-P2-PROG-0008** (PROPOSED, Pass 32) — FEMA NFHL + USACE NLD/NID ingest doctrine: sensitive infrastructure (pump stations, gate controls) generalized or marked restricted in line with policy agreements. **Generalized by analogy to the HIFLD family.**
- **C4-01 STAC `kfm:provenance`** (CONFIRMED) — `spec_hash`, `evidence_bundle_ref`, `run_record_ref`, `audit_ref`, `policy_digest`; per-asset `file:checksum`.
- **C4-02 STAC Collection identity** (CONFIRMED expansion direction) — `kfm-<org>-<product>` Collection id pattern.
- **C4-05 DCAT Distribution** (CONFIRMED) — dataset-level metadata for non-spatial / non-spatiotemporal data.
- **C5-02 Default-deny promotion** (CONFIRMED) — promotion fails closed; explicit allow-rule required.
- **C6-01 Sensitivity Rubric 0–5** (CONFIRMED) — six-level rubric from public to highest-restricted.
- **C7-09 GNIS** (CONFIRMED) — USGS Geographic Names Information System as the federal authority for U.S. place names.
- **KFM-P26-PROG-0025** (PROPOSED) — catalog writers should emit DCAT, STAC, and PROV entries with dataset DOI, harvest date, dataset version, license, rightsHolder, datasetID, and EvidenceBundle references.
- **KFM-P27-FEAT-0003** (PROPOSED) — STAC Projection lint report.
- **KFM-P22-PROG-0037** (PROPOSED) — STAC checksum closure against the ReleaseManifest digest.
- **`directory-rules.md §7.3`** (CONFIRMED) — nine canonical connector families do not include `hifld`.
- **`directory-rules.md §2.4(2)`** (CONFIRMED) — promotion to canonical family is ADR-class.
- **ADR-0001** (PROPOSED in mounted-repo evidence) — schemas/contracts/v1/ as schema home.

</details>

---

<sub>**Last reviewed:** 2026-05-21 *(Claude Code product-page polish session; KFM presentation standard v2 applied)* · **Version:** v0.2 (draft) · **Doc ID:** `kfm://doc/docs-sources-catalog-hifld-hifld` · [Back to top ↑](#-hifld-infrastructure-layers)</sub>
