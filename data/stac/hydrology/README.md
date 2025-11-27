---
title: "🛰️ Kansas Frontier Matrix — Hydrology STAC Domain Index (v11.2.2 Super-Edition)"
path: "data/stac/hydrology/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Hydrology & Hazards Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/stac-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-stac-hydrology-index-v11.2.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "STAC Domain Index"
intent: "stac-hydrology-domain-index"
semantic_document_id: "kfm-stac-hydrology-domain-index"
doc_uuid: "urn:kfm:stac:hydrology:index:v11.2.2"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
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

# 🛰️ **Hydrology STAC Domain Index (v11.2.2 Super-Edition)**  
`data/stac/hydrology/README.md`

**Purpose**  
Define the **STAC domain rules, directory structure, metadata requirements, and lineage model** for all **hydrology-related datasets** in KFM: reservoirs, rivers, sedimentation, bathymetry, WID, flood operations, water quality, downstream ecology, and statewide hydroclimate.

</div>

---

## 📘 Overview

Hydrology is one of the heaviest data domains in KFM. This document specifies:

- How hydrologic datasets are organized under `data/stac/hydrology/`  
- How they become **STAC 1.0+ Items and Collections**  
- How they align with:
  - **KFM-STAC v11.2**  
  - **DCAT 3.0**  
  - **PROV-O**  
  - **CIDOC-CRM + GeoSPARQL + OWL-Time**  
- How they feed:
  - The Neo4j graph  
  - Focus Mode v3  
  - Story Node v3  
  - MapLibre/3D UIs

This index is the root reference for **all hydrology STAC Collections** in KFM.

---

## 🗂️ Directory Layout (Canonical)

```text
📁 data/
└── 📁 stac/
    └── 📁 hydrology/
        ├── 📄 README.md                 — ← This file (domain index)
        ├── 📄 collection.json           — Optional overall hydrology collection
        ├── 📁 items/                    — Cross-collection Items (if needed)
        ├── 📁 tuttle-creek/             — Tuttle Creek hydrology collection
        ├── 📁 milford/                  — Milford Lake hydrology collection
        ├── 📁 perry/                    — Perry Lake hydrology collection
        ├── 📁 clinton/                  — Clinton Lake hydrology collection
        ├── 📁 kansas-river/             — Kansas River hydrology
        ├── 📁 statewide/                — Statewide hydrology & hydroclimate
        ├── 📁 sediment/                 — Sedimentation datasets
        ├── 📁 bathymetry/               — Bathymetry, reservoir DEMs, DoDs
        ├── 📁 wid/                      — Water Injection Dredging (WID) datasets
        └── 📁 ecology/                  — Hydrology-linked ecological datasets
```

This layout is stable and extendable for new reservoirs, rivers, and state programs.

---

## 🌎 Hydrology Domain Architecture

The hydrology STAC domain is structured as multiple **Collections**, each focused on a reservoir, river reach, or theme.

### Spatial Subdomains

- Tuttle Creek  
- Milford  
- Perry  
- Clinton  
- Kansas River  
- Statewide hydrology (all reservoirs + rivers + hydroclimate context)

### Thematic Subdomains

- **Hydrology** — inflows, outflows, stage, storage, hydrographs  
- **Sedimentation** — delta growth, volume, TSS, sediment cores  
- **Bathymetry** — historical and modern DEMs, difference-of-DEM (DoD)  
- **Water Quality** — turbidity, DO, nutrients, temperature, conductivity  
- **Flood Operations** — releases, gate operations, events  
- **Climate Drivers** — Mesonet, PRISM, NCEI climate drivers for flows  
- **Ecology** — hydrology → ecological response (fish, mussels, macroinvertebrates)  
- **WID** — Water Injection Dredging operations and environmental response (2025+)  

Each subdomain is implemented as one or more **STAC Collections** under the corresponding directory.

---

## 🛰️ STAC Item Requirements (Hydrology)

All hydrology Items MUST meet **STAC 1.0+** (or 1.1) minimums and hydrology-specific extensions.

### Core STAC Fields

- `stac_version`  
- `type` = `"Feature"`  
- `id` (globally unique in domain)  
- `collection`  
- `geometry` (GeoJSON)  
- `bbox`  
- `properties.datetime`  
- `properties.start_datetime` (if temporal extent)  
- `properties.end_datetime` (if temporal extent)  
- `assets` (≥1 asset)

### Hydrology-Specific Fields (Required)

| Field             | Purpose                                              |
|------------------|------------------------------------------------------|
| `kfm:parameter`  | Hydrologic variable (flow, stage, turbidity, etc.)   |
| `kfm:units`      | Units (SI / hydrology-standard)                      |
| `kfm:site`       | Canonical KFM site code (e.g., USGS station ID)      |
| `kfm:provider`   | Dataset owner/host (USACE, USGS, KWO, KDHE, etc.)    |
| `kfm:method`     | Sensor/survey/algorithm/methodology                  |
| `kfm:lineage`    | Short ETL → STAC provenance pointer                  |
| `kfm:quality`    | QA/QC flags or score                                 |
| `kfm:project`    | Project or initiative (e.g., `"WID-2025"`)           |

### Strongly Recommended

- `keywords`  
- `summaries` in collection metadata for common fields  
- `kfm:hydrologic_region` (e.g., `"Kansas River Basin"`)  
- `kfm:license_text` (if more detailed license text needed)  
- `kfm:processing_history` (summarized steps or version tags)

---

## 📐 Asset Standards (Hydrology)

### Allowed Formats

| Format                         | Use Case                                      |
|--------------------------------|-----------------------------------------------|
| COG (Cloud-Optimized GeoTIFF)  | Bathymetry, DEMs, DoDs, flood depth grids     |
| GeoJSON                        | Survey lines, plume polygons, station points  |
| CSV / CSVW                     | Time series from gauges and sensors           |
| NetCDF (CF-compliant)          | Gridded climate/hydrology fields              |
| Parquet                        | High-volume tabular hydrology data            |

Each asset MUST include:

- `href` — stable path or URL  
- `type` — MIME type (`"image/tiff; application=geotiff; profile=cloud-optimized"`, `"application/geo+json"`, `"text/csv"`, etc.)  
- `roles` — e.g. `["data"]`, `["metadata"]`, `["thumbnail"]`  
- `title` — human-readable label (recommended)  
- `description` — short description (recommended)

---

## 🧭 Collection Metadata Rules

Each hydrology Collection (e.g., `tuttle-creek/collection.json`) MUST include:

- `"type": "Collection"`  
- `"stac_version": "1.0.0"` or `"1.1.0"`  
- `"id"` — unique within KFM STAC domain  
- `"title"`  
- `"description"`  
- `"keywords"` — at least hydrology + location + parameter terms  
- `"extent"` — spatial + temporal extents  
- `"providers"` — including KFM and source agencies  
- `"license"`  
- `"links"` — including `root`, `parent`, `items`  

### Summaries

For faster search and filtering, `summaries` SHOULD include:

- `kfm:parameter`  
- `kfm:units`  
- `kfm:site`  
- `kfm:method`  
- `datetime` (range)  

---

## 🧬 Lineage & Ontology (PROV-O, DCAT, CIDOC, GeoSPARQL, OWL-Time)

Hydrology STAC Items are not just files—they are hooked into the KFM semantics and lineage graph.

### PROV-O

Each Item is a `prov:Entity` with:

- `prov:wasGeneratedBy` → ETL or analysis `prov:Activity`  
- `prov:wasDerivedFrom` → raw datasets (upstream sensors, grids, etc.)  
- `prov:wasAttributedTo` → `prov:Agent` (agency, KFM pipeline)  

### DCAT 3.0

Mapping from hydrology STAC to DCAT:

| STAC Field          | DCAT Field        |
|---------------------|-------------------|
| `id`                | `dct:identifier`  |
| `description`       | `dct:description` |
| `providers`         | `dcat:contactPoint` |
| `assets[].href`     | `dcat:downloadURL` |
| `extent.spatial`    | `dct:spatial`     |
| `extent.temporal`   | `dct:temporal`    |
| `keywords`          | `dcat:keyword`    |
| `license`           | `dct:license`     |

### CIDOC-CRM / GeoSPARQL / OWL-Time

- `E73 InformationObject` → the dataset  
- `E53 Place` → the basin/reservoir reach  
- `E7 Activity` → major hydrologic events (e.g., WID operations)  
- `geo:hasGeometry` → dataset geometry  
- `time:hasBeginning` / `time:hasEnd` → dataset temporal extent  

These mappings allow hydrology STAC Items to link directly into KFM’s historical narratives and Focus Mode.

---

## 🔁 STAC → ETL → Graph Pipeline Pattern

```text
Raw hydrology data (USGS/USACE/KWO/etc.)
    ↓ extract
Schema normalization + unit harmonization
    ↓ transform
Asset generation (COG, CSVW, GeoJSON, NetCDF)
    ↓ stac-annotate
STAC Items written under data/stac/hydrology/...
    ↓ validate (STAC + JSON Schema + FAIR+CARE)
Graph ingestion (Neo4j hydrology schema)
```

Each ETL run is logged under `mcp/experiments/hydrology/...` and emits OpenLineage v2.5 events with energy/carbon telemetry if configured.

---

## 🎯 Focus Mode & Story Nodes

Hydrology STAC Items power:

- **Focus Mode v3** views of:
  - Reservoir operations over time  
  - Flood events and downstream impacts  
  - Sediment accumulation and dredging operations  
  - Climate drivers and hydrologic response  

- **Story Node v3** narratives such as:
  - “A Reservoir Filling From the Bottom Up”  
  - “Downstream of the Dam”  
  - “The 2025 WID Demonstration”  
  - “Kansas Climate & Flow Regimes”  

Story Nodes refer to hydrology datasets via `relation.rel = "uses-dataset"` and `relation.target` set to the STAC Item or Collection IDs.

---

## 🛣 Roadmap

Planned hydrology STAC enhancements:

- Ingestion of full 3D hydrodynamic model outputs (NetCDF/CF-compliant)  
- Real-time streaming STAC Items for key gauges and reservoirs  
- Climate-projection-based hydrology layers for 2030–2100  
- Flood inundation maps based on combined SAR + gauge data  
- Integration of Sentinel-1D InSAR-derived hydrology products  
- Cross-reservoir sediment and nutrient transport datasets  

---

## 🕰 Version History

| Version  | Date       | Summary                                                                                  |
|---------:|------------|------------------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-27 | Upgraded to v11.2.2; canonical directory layout; PROV/DCAT/CIDOC mapping hardened; Focus Mode hooks clarified. |
| v11.0.0  | 2025-11-21 | Initial hydrology STAC domain index for v11; defined core layout and STAC metadata rules. |

---

<div align="center">

**Kansas Frontier Matrix — Hydrology STAC Domain (v11.2.2)**  
Hydrology as a first-class, semantically-governed STAC domain.

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[⬅ Back to STAC Root](../README.md) ·  
[📐 Data Architecture](../../../docs/ARCHITECTURE.md) ·  
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
