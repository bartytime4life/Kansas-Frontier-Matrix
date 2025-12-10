---
title: "🟫 Kansas Frontier Matrix — Environmental Events & Pipelines Index"
path: "docs/events/environmental/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Environmental Systems Working Group"
content_stability: "stable"

doc_kind: "Events / Pipelines Index"
status: "Active / Canonical"
intent: "environmental-events-index"
semantic_document_id: "kfm-doc-events-environmental-index-v11.2.6"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

header_profile: "standard"
footer_profile: "standard"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"

telemetry_ref: "../../../releases/v11.2.6/environmental-events-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/environmental-events-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
---

# 🟫 Environmental Events & Pipelines Index  

Canonical index for **environmental event docs and pipelines** in KFM v11.2.6:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → Story Nodes → Focus Mode

This file organizes **soil**, **air-quality**, and related environmental ingestion & event flows under `docs/events/environmental/`.

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 events/
    ├── 📄 README.md                        # Global events index (Event→Action map)
    ├── 📁 environmental/
    │   ├── 📄 README.md                    # 🟫 This file — environmental events & pipelines index
    │   └── 📄 soil-air-ingestion-overview.md
    │                                        # SDA (SSURGO/STATSGO) + OpenAQ v3 + CAMS NRT ingestion
    └── 📁 remote-sensing/
        ├── 📄 README.md                    # Remote-sensing events index
        └── 📄 stac-telemetry-overview.md   # STAC telemetry spec (freshness, energy, SLO)
~~~

Implementation & data paths (documented in their own READMEs):

- `src/pipelines/environmental/` — environmental ETL (soil, air, joint harmonization)  
- `configs/pipelines/environmental/` — config files for environmental pipelines  
- `data/processed/environmental/` — harmonized soil & air products  
- `data/stac/environmental/` — STAC Collections & Items for environmental assets  
- `data/catalogs/environmental/` — DCAT datasets and distributions  
- `data/provenance/environmental/` — PROV bundles for environmental runs  

---

## 📘 Purpose & Scope

This index:

- lists **environmental event / pipeline docs** under `docs/events/environmental/`  
- explains how they fit the KFM pipeline:
  - **soil ingestion** (SDA / SSURGO / STATSGO)  
  - **air-quality ingestion** (OpenAQ v3 / CAMS NRT)  
  - future environmental channels (hydrology, land-surface, vegetation)  
- defines high-level **governance expectations**:
  - deterministic ETL and chunking  
  - catalog & graph alignment (STAC/DCAT/PROV + Neo4j)  
  - telemetry and SLO integration  
  - Story Node and Focus Mode readiness  

It is the **entry point** for environmental events and pipelines; all new environmental event docs must be linked here.

---

## 🧬 Relationship to the KFM Pipeline

Environmental events and pipelines are structured to follow:

> **Raw → Work → Processed → STAC/DCAT/PROV → Neo4j → API → Story Nodes → Focus Mode**

- **Raw** — direct pulls from SDA, OpenAQ v3, CAMS NRT, and future environmental APIs.  
- **Work** — normalized relational tables or gridded products (soil components/horizons, air observations).  
- **Processed** — harmonized, unit-aware environmental layers ready for cataloging and graph ingestion.  
- **STAC/DCAT/PROV** — collections, datasets, and provenance that describe:
  - sources
  - versions
  - coverage
  - transformations  
- **Neo4j** — graph representation of:
  - soil units and horizons  
  - air sensors and observations  
  - environmental regions and relationships  
- **API & Story Nodes** — narrative-ready surfaces:
  - environmental incidents and episodes  
  - cross-layer reasoning (soil ↔ air ↔ remote sensing)  

---

## 📚 Current Environmental Event Docs

### 🟫 Soil & Air Ingestion Overview

- **Doc:** `docs/events/environmental/soil-air-ingestion-overview.md`  
- **Scope:**
  - SDA (SSURGO/STATSGO) ingestion with deterministic chunking  
  - OpenAQ v3 + CAMS NRT air-quality ingestion and enrichment  
  - end-to-end flow into STAC/DCAT/PROV and Neo4j  
  - Story Node / Focus Mode integration for soil and air layers  

Key responsibilities:

- document constraints (SDA row/size limits, OpenAQ v3-only, CAMS cadence)  
- define soil graph schema (MapUnit → Component → Horizon)  
- define harmonized air-quality model (observations, sensors, model overlays)  
- specify telemetry outputs (`soil-air-telemetry.json`)

### 📡 Remote-Sensing Event Docs (Sibling Index)

While not under this directory, environmental pipelines frequently depend on:

- `docs/events/remote-sensing/README.md` — remote-sensing events index  
- `docs/events/remote-sensing/stac-telemetry-overview.md` — STAC telemetry integration for:
  - freshness  
  - energy & CO₂ intensity  
  - SLO state  

Environmental pipelines SHOULD:

- use STAC telemetry fields to describe environmental layers sourced from remote-sensing products.  

---

## 🧭 Event Families & Routing

Environmental events are grouped into families:

| Family          | Examples                                                | Primary Docs                                                        |
|-----------------|---------------------------------------------------------|----------------------------------------------------------------------|
| `soil-ingest`   | SDA chunk plans, SSURGO/STATSGO updates                 | `soil-air-ingestion-overview.md`                                    |
| `air-ingest`    | OpenAQ v3 window pulls, CAMS NRT forecast cycles        | `soil-air-ingestion-overview.md` and `docs/data/air-quality/README.md` |
| `env-telemetry` | soil-air ingestion telemetry & SLOs                     | `telemetry_ref` (environmental-events-telemetry.json)               |
| `env-story`     | soil/air event narratives and cross-layer episodes      | Story Node docs (future)                                            |

Event→Action routing (see global events index) MUST ensure environmental events:

- drive ETL behavior (pause/resume, reprocess, backfill)  
- update STAC/DCAT metadata (status flags, source versions, SLO states)  
- update graph nodes and Story Nodes (incident narratives, layers impacted)  

---

## 🧪 Telemetry & Provenance

Environmental event pipelines must emit:

- **Telemetry** (per `telemetry_schema`):
  - rows/bytes processed  
  - runtime, energy, and CO₂ estimates  
  - SLO states (freshness, latency, availability)  

- **PROV-O**:
  - Entities for raw pulls, normalized tables, harmonized products  
  - Activities for ingestion runs, conversions, model overlays  
  - Agents for pipeline services and maintainers  

Environmental telemetry is recorded in:

- `releases/v11.2.6/environmental-events-telemetry.json`

and may be aggregated with air-quality telemetry for source-wide views.

---

## 📖 Story Nodes & Focus Mode

Environmental event docs must be written so their content can be transformed into **Story Nodes** with:

- **title & description** — human-readable environmental narrative  
- **spatial extent** — affected regions (e.g., soil survey areas, air basins, counties)  
- **temporal extent** — time window of the episode or change  
- **links** — to:
  - STAC Collections/Items  
  - DCAT datasets  
  - Neo4j entities (soils, air observations, sensors, regions)  

Focus Mode uses these Story Nodes to support:

- soil–air cross reasoning (e.g., dust events over specific soil types)  
- environmental hazard or exposure stories  
- long-term trends and anomaly reporting  

---

## 🕰️ Version History

| Version  | Date       | Notes                                                                |
|----------|------------|----------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Initial environmental events & pipelines index for KFM v11.2.6.      |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **Environmental Systems Working Group**, with co-review by the FAIR+CARE Council and Governance Council  
- must be updated when new environmental event docs are added or when core environmental pipelines change

Edits require approval from the Environmental Systems WG and FAIR+CARE Council and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and environmental-events telemetry & ETL validation workflows.

<br/>

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🟫 **Kansas Frontier Matrix — Environmental Events & Pipelines Index v11.2.6**  
Soil & Air Pipelines · Catalog–Graph Harmony · FAIR+CARE Environmental Governance  

[📘 Docs Root](../../README.md) · [📡 Events Root](../README.md) · [📊 Data Docs Index](../../data/README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>