---
title: "🗂️ ESA Sentinel-1 — STAC Ecosystem (GRD · GRDH · RTC · Coherence · Flood · Wetlands · Deformation)"
path: "docs/data/satellites/sentinel-1/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public Earth Observation (CC-BY-4.0)"
status: "Active / Enforced"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F2-A1-I2-R4"
care_label: "CARE-A / CARE-B (varies by product family)"
indigenous_rights_flag: true
sensitivity_level: "Low–High (product dependent)"
public_exposure_risk: "Low–Medium"
risk_category: "Low–High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/sentinel1-stac-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-stac-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon next ESA Sentinel-1 STAC reprocessing cycle"
---

<div align="center">

# 🗂️ **Sentinel-1 STAC Ecosystem**  
`docs/data/satellites/sentinel-1/stac/`

**Purpose**  
Define the **complete STAC layout and product registry** for Sentinel-1 within KFM v11.2.2, aligned with  
**STAC 1.0**, **DCAT 3.0**, **PROV-O**, **GeoSPARQL**, and **OWL-Time**, and wired for FAIR+CARE + sovereignty enforcement.

GRD · GRDH · RTC · 🔗 Coherence · 🌊 Flood · 🌿 Wetlands · 🌍 Deformation (InSAR)

</div>

---

## 📘 1. Overview

This directory hosts the **entire STAC ecosystem** for ESA Sentinel-1 inside the Kansas Frontier Matrix:

- **🛰️ GRD / GRDH** — calibrated σ⁰ VV/VH backscatter (standard and high-resolution)
- **🛰️ RTC** — γ⁰, radiometrically terrain-corrected backscatter
- **🔗 Coherence** — temporal coherence for disturbance, flood damage, agriculture, land-change
- **🌊 Flood** — flood-extent masks (binary, multi-class, probability surfaces)
- **🌿 Wetlands** — wetland / saturation / inundation indicators
- **🌍 Deformation (InSAR)** — LOS displacement, subsidence/uplift (H3 sovereignty-generalized)
- **📚 Metadata hubs** — DCAT / JSON-LD / PROV-O templates for all Sentinel-1 assets

Everything is expressed as:

- **Collections** — product-family catalogs (spatial/temporal extent, license, summaries)
- **Items** — scene-level or tile-level assets (COGs, NetCDF, GeoJSON, QA layers)
- **Metadata** — DCAT datasets, JSON-LD contexts, PROV-O templates

All products are:

- STAC **1.0.0** compliant
- JSON-LD compatible
- DCAT-aligned for dataset catalogs
- PROV-O annotated for ingestion + processing lineage
- Subject to **FAIR+CARE** + sovereignty masking (H3-aware generalization and CARE labels)

---

## 🗂️ 2. Directory Layout (Aligned to Current Repo State)

The `stac/` tree now mirrors the actual GitHub layout in your screenshot — including **per-family hubs**:

~~~text
docs/data/satellites/sentinel-1/stac/
├── 📄 README.md                          # This file (global STAC overview)
│
├── 🗂️ collections/                       # Global top-level Collections (all families)
│   ├── collection_grd.json              # GRD scenes
│   ├── collection_grdh.json             # GRDH high-res scenes
│   ├── collection_rtc.json              # RTC γ⁰ products
│   ├── collection_coherence.json        # Temporal coherence
│   ├── collection_deformation.json      # InSAR LOS deformation (generalized)
│   ├── collection_flood.json            # Flood detection products
│   └── collection_wetlands.json         # Wetlands / saturation / inundation
│
├── 🧩 items/                             # Global Items index (by family)
│   ├── grd/                             # GRD item JSONs (scene-level)
│   ├── grdh/                            # GRDH item JSONs
│   ├── rtc/                             # RTC item JSONs
│   ├── coherence/                       # Coherence item JSONs
│   ├── deformation/                     # Deformation item JSONs
│   ├── flood/                           # Flood item JSONs
│   └── wetlands/                        # Wetland item JSONs
│
├── 📁 metadata/                         # Global metadata scaffolding
│   ├── 📚 dcat/                         # DCAT Dataset & Distribution templates
│   ├── 🧩 jsonld/                       # JSON-LD contexts (SAR, governance, PROV-O)
│   └── 🔗 provenance/                   # PROV-O activity/entity/agent templates
│
├── 🛰️ grd/                             # GRD family hub (local README + collections/items)
│   ├── README.md
│   ├── collections/
│   └── items/
│
├── 🛰️ grdh/                            # GRDH family hub (local README + collections/items)
│   ├── README.md
│   ├── collections/
│   └── items/
│
├── 🔗 coherence/                       # Coherence family hub
│   ├── README.md
│   ├── collections/
│   └── items/
│
├── 🌍 deformation/                     # InSAR deformation family hub
│   ├── README.md
│   ├── collections/
│   └── items/
│
├── 🌊 flood/                           # Flood family hub
│   ├── README.md
│   ├── collections/
│   └── items/
│
└── 🌿 wetlands/                        # Wetland family hub
    ├── README.md
    ├── collections/
    └── items/
~~~

Notes:

- The **top-level `collections/` and `items/`** folders provide a **global index** by product family.
- The **family hubs** (`grd/`, `grdh/`, `coherence/`, `deformation/`, `flood/`, `wetlands/`) contain:
  - a **family-specific README.md** (you already created these)
  - **nested `collections/` and `items/`** for that family
- **RTC** currently lives only under `collections/collection_rtc.json` and `items/rtc/` (no separate `stac/rtc/` hub yet), matching the repo.

This layout block is now 1:1 with the GitHub view in your screenshot (no phantom directories).

---

## 🧩 3. Product Families & Where to Find Them

Each Sentinel-1 product family has:

- A **global Collection** in `collections/collection_<family>.json`
- A **global Items subtree** in `items/<family>/`
- For most families, a **local hub** (`stac/<family>/`) with its own README and nested collections/items

### 🛰 GRD — Ground Range Detected Backscatter

- **Collections:**
  - `collections/collection_grd.json`
  - `grd/collections/` (family-scoped view, if you want to keep per-hub collections)
- **Items:**
  - `items/grd/` — all GRD scenes
  - `grd/items/` — GRD items accessed via the family hub
- **Hub README:** `grd/README.md` (high-level design and governance for GRD)

### 🛰 GRDH — High-Resolution GRD

- **Collections:** `collections/collection_grdh.json`, `grdh/collections/`
- **Items:** `items/grdh/`, `grdh/items/`
- **Hub README:** `grdh/README.md`

### 🛰 RTC — Radiometrically Terrain Corrected (γ⁰)

- **Collections:** `collections/collection_rtc.json`
- **Items:** `items/rtc/`
- **Note:** No `stac/rtc/` hub yet — RTC is managed via the global `collections/` + `items/rtc/` layout.

### 🔗 Coherence — Temporal SAR Coherence

- **Collections:** `collections/collection_coherence.json`, `coherence/collections/`
- **Items:** `items/coherence/`, `coherence/items/`
- **Hub README:** `coherence/README.md`

### 🌍 Deformation — InSAR LOS Displacement

- **Collections:** `collections/collection_deformation.json`, `deformation/collections/`
- **Items:** `items/deformation/`, `deformation/items/`
- **Hub README:** `deformation/README.md`

### 🌊 Flood — Flood Mapping Layers

- **Collections:** `collections/collection_flood.json`, `flood/collections/`
- **Items:** `items/flood/`, `flood/items/`
- **Hub README:** `flood/README.md`

### 🌿 Wetlands — Wetness & Inundation Indicators

- **Collections:** `collections/collection_wetlands.json`, `wetlands/collections/`
- **Items:** `items/wetlands/`, `wetlands/items/`
- **Hub README:** `wetlands/README.md`

---

## 🔐 4. FAIR+CARE & Sovereignty Controls

All Sentinel-1 STAC content in this tree is **governed**:

- **CARE-B** applies to disturbance- and presence-revealing products:
  - GRDH, Coherence, Flood, Wetlands, Deformation
- **CARE-A** applies to lower-sensitivity baselines:
  - Many GRD/RTC products, depending on downstream use

Enforcement patterns reflected in STAC metadata:

- `properties["kfm:care_label"]`  
- `properties["kfm:h3_sensitive"]`  
- `properties["kfm:mask_required"]`  
- `properties["kfm:sovereignty_uncertainty_floor"]`  
- `properties["kfm:governance_notes"]`  

Sovereignty masking is implemented via:

- **H3-based geometry generalization** for Deformation, Flood, Wetlands, Coherence
- **Magnitude/uncertainty flooring** for displacement and probability products
- **Explicit provenance** in PROV-O (`prov:wasGeneratedBy`, `prov:used`) pointing to masking steps

---

## 🧪 5. CI & Validation

All files beneath `stac/` are validated via CI:

- **STAC validation** (`stac-validate.yml`)
- **JSON Schema & SHACL** checks against:
  - `json_schema_ref: sentinel1-stac-v11.json`
  - `shape_schema_ref: sentinel1-stac-v11-shape.ttl`
- **FAIR+CARE checks** to ensure:
  - Required `"kfm:*"` governance fields are present
  - Sovereignty flags line up with product type
- **Link graph sanity** (Collections ↔ Items ↔ metadata, no broken references)

Any structural mismatch (wrong directory, missing collection/item, or stale layout) is treated as a **CI failure**.

---

## 🔁 6. Sentinel-1 STAC in the ETL Pipeline

High-level SAR → STAC pipeline (for all families):

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → (optional) terrain correction (RTC γ⁰)
 → (optional) speckle filtering
 → derived products (coherence / deformation / flood / wetlands)
 → sovereignty masking & governance QA
 → STAC Item emissions (items/<family>/**.json)
 → Collection rollups (collections/collection_<family>.json)
 → metadata sync (metadata/dcat + metadata/jsonld + metadata/provenance)
~~~

The `stac/` tree is the **public, declarative index** of everything this pipeline produces for Sentinel-1.

---

## 🕰️ 7. Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Updated STAC README to match current repo directories (coherence/, deformation/, flood/, grd/, grdh/, items/, metadata/, wetlands/); documented family hubs and global collections/items. |
| v11.2.1 | 2025-11-28 | Initial v11 STAC ecosystem README (global collections/items/metadata) without per-family hubs.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🛰 Sentinel-1 Root](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
