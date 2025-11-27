---
title: "🛰️ Kansas Frontier Matrix — STAC Mission Catalog (Diamond⁹ Ω / Crown∞Ω)"
path: "data/stac/missions/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · EO Working Group · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/stac-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/stac-missions-index-v11.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active"
doc_kind: "Index"
intent: "stac-mission-catalog-index"
semantic_document_id: "kfm-stac-missions-index"
doc_uuid: "urn:kfm:data:stac:missions:index:v11.2.2"

fair_category: "FAIR-Aligned"
care_label: "CARE Screened (Earth Observation Generally Low Risk)"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🛰️ **KFM STAC Mission Catalog**  
`data/stac/missions/`

**Purpose:**  
Provide the **canonical index** for all **Earth Observation (EO) missions**, sensors, and orbital data sources integrated into KFM’s **STAC v11.2** collections.  
This directory contains **mission-level namespaces**, each with their own STAC Collections, Items, QA telemetry, and ingestion scaffolding under LangGraph v11.

[![STAC v1.1.0](https://img.shields.io/badge/STAC-v1.1.0-blue)]() ·  
[![KFM-STAC v11.2](https://img.shields.io/badge/KFM–STAC-v11.2-purple)]() ·  
[![OpenLineage v2.5](https://img.shields.io/badge/Lineage-OpenLineage_v2.5-orange)]()  

</div>

---

## 📘 Overview

The **missions module** defines mission-scoped STAC structures for:

- SAR platforms (Sentinel-1A/1B/1C/1D, NISAR, RADARSAT)  
- Optical platforms (Landsat, Sentinel-2, NAIP)  
- Thermal & atmospheric missions (ECOSTRESS, AIRS/OMI, MODIS/VIIRS)  
- Hydrology & altimetry missions (SWOT, ICESat-2, CryoSat)  

Each mission folder contains:

- A **STAC Collection** (`collection.json`)  
- An **items/** subtree for:
  - commissioning previews  
  - operational SLC/GRD/Level-2 products  
- A **metadata/** subdirectory for JSON-LD, DCAT, PROV-O  
- A **qa/** subdirectory for validation and sustainability telemetry

All missions conform to:

- **KFM-STAC v11.2 profile**  
- **SAR/EO/STAC extensions**  
- **FAIR+CARE screening**  
- **KFM metadata and provenance rules**

---

## 🗂️ Directory Layout

```text
📁 data/
└── 📁 stac/
    └── 📁 missions/                        — Mission-scoped STAC namespaces
        ├── 📄 README.md                    — ← This index
        │
        ├── 📁 sentinel-1d/                 — Sentinel-1D (SAR · C-Band · Commissioning)
        │   ├── 📄 README.md
        │   ├── 📄 collection.json
        │   ├── 📁 items/
        │   ├── 📁 metadata/
        │   └── 📁 qa/
        │
        ├── 📁 sentinel-1c/                 — Sentinel-1C (SAR · C-Band · Operational)
        │   ├── 📄 README.md
        │   ├── 📄 collection.json
        │   ├── 📁 items/
        │   ├── 📁 metadata/
        │   └── 📁 qa/
        │
        ├── 📁 landsat-9/                   — Landsat-9 OLI/TIRS (optical + thermal)
        │   ├── 📄 README.md
        │   ├── 📄 collection.json
        │   ├── 📁 items/
        │   ├── 📁 metadata/
        │   └── 📁 qa/
        │
        ├── 📁 sentinel-2/                  — Sentinel-2 MSI (optical)
        │   ├── 📄 README.md
        │   ├── 📄 collection.json
        │   ├── 📁 items/
        │   ├── 📁 metadata/
        │   └── 📁 qa/
        │
        ├── 📁 naip/                        — NAIP high-resolution aerial imagery (USDA)
        │   ├── 📄 README.md
        │   ├── 📄 collection.json
        │   ├── 📁 items/
        │   ├── 📁 metadata/
        │   └── 📁 qa/
        │
        └── 📁 swot/                        — Surface Water and Ocean Topography (altimetry)
            ├── 📄 README.md
            ├── 📄 collection.json
            ├── 📁 items/
            ├── 📁 metadata/
            └── 📁 qa/
```

This layout is **universal across all KFM STAC mission directories**.

---

## 🧭 Mission Role in KFM Architecture

Mission-level STAC directories form the **core ingestion surface** for KFM:

### 1. **STAC → LangGraph v11**
Each mission has a pre-configured ingestion DAG that:

- Detects new EO/SAR products  
- Converts SAFE/GRD/SLC products → GeoTIFF/COG  
- Emits OpenLineage v2.5 provenance  
- Generates mission-specific STAC Items  
- Inserts graph nodes:
  - `Acquisition`
  - `SatelliteMission`
  - `SensorMode`
  - `DerivedProduct`
  - `HazardLayer`

### 2. **Graph → Story Nodes / Focus Mode**
EO missions provide:

- Upstream signal for hazard narratives (flooding, drought, subsidence)  
- Timeline-driven visualizations  
- Contextual overlays in Focus Mode v3

### 3. **UI → MapLibre / Cesium**
Mission outputs drive:

- Layer selectors  
- Historical time sliders  
- Hazard overlays  
- Before/After comparisons  
- InSAR deformation maps

---

## 🛰️ Currently Active Mission Namespaces

### **Sentinel-1D (Commissioning)**  
`data/stac/missions/sentinel-1d/`  
- C-band SAR  
- Commissioning pseudo-items available  
- Operational data expected Q1–Q2 2026  

### **Sentinel-2 MSI**  
`data/stac/missions/sentinel-2/`  
- High-resolution optical imagery  
- True-color basemaps for UI  

### **Landsat-9 OLI/TIRS**  
`data/stac/missions/landsat-9/`  
- Multi-decadal continuity  
- Temperature and vegetation analyses  

### **NAIP**  
`data/stac/missions/naip/`  
- High-resolution aerial photography  
- Supports parcel- and site-scale investigations  

### **SWOT**  
`data/stac/missions/swot/`  
- Water surface elevation + hydrology models  
- Relevant to Kansas river basins indirectly  

More missions can be added following the exact directory template.

---

## 🧪 Validation & QA

Each mission directory MUST include:

- **STAC validation logs**
- **Energy telemetry**
- **Carbon telemetry**
- **Provenance emission checks**
- **Collection + items schema validation**

CI checks:

- `stac-lint`  
- `schema-lint`  
- `telemetry-validate`  
- `openlineage-emit-test`

Any failure blocks ingestion.

---

## 🧭 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-27 | STAC mission index upgraded to v11.2.2; canonical directory layout applied; telemetry + governance updated. |
| v11.0.0 | 2025-11-20 | Initial mission index created. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Mission Catalog**  
Earth Observation as a first-class citizen of the knowledge graph.

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[⬅ Back to STAC Root](../README.md) ·  
[⚖ Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

