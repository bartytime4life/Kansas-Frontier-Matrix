---
title: "🛰️ Kansas Frontier Matrix — Hydrology STAC Domain Index (v11 Super-Edition)"
path: "data/stac/hydrology/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-stac-hydrology-index-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Domain Index"
intent: "stac-hydrology-domain-index"
semantic_document_id: "kfm-stac-hydrology-domain-index"
doc_uuid: "urn:kfm:stac:hydrology:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **Hydrology STAC Domain Index (v11 Super-Edition)**  
`data/stac/hydrology/README.md`

**Purpose:**  
Serve as the **master STAC domain index** for all hydrology-related datasets in KFM, including  
reservoirs, rivers, sedimentation, bathymetry, flood operations, water quality, WID 2025,  
downstream ecology, and statewide hydroclimate. Defines STAC metadata rules, asset  
standards, ontology mapping, lineage protocols, and Focus Mode v3 integration for  
hydrology datasets across Kansas.

</div>

---

# 📘 0. Overview

Hydrology is one of the largest and most data-intensive domains in the Kansas Frontier Matrix.  
This README defines how hydrologic datasets must be cataloged using **STAC 1.0.0**,  
ensuring:

- FAIR+CARE compliance  
- DCAT 3.0 interoperability  
- PROV-O lineage tracking  
- Full GeoSPARQL spatial grounding  
- OWL-Time temporal grounding  
- CIDOC-CRM entity mapping  
- KFM v11 UI compatibility (MapLibre, timeline, Focus Mode v3)  
- Machine-readability and reproducible ETL pipelines  

This STAC domain index is the root reference for ALL hydrology STAC Collections.

---

# 🗂️ 1. Directory Layout (Canonical)

```text
data/
└── stac/
    └── hydrology/
        ├── collection.json                     # (optional global hydrology collection)
        ├── items/                              # cross-collection STAC Items
        ├── tuttle-creek/                       # Tuttle Creek hydrology collection
        ├── milford/                            # Milford Lake hydrology collection
        ├── perry/                              # Perry Lake hydrology collection
        ├── clinton/                            # Clinton Lake hydrology collection
        ├── kansas-river/                       # Kansas River hydrology
        ├── statewide/                          # statewide hydrology & hydroclimate
        ├── sediment/                           # sedimentation datasets
        ├── bathymetry/                         # statewide bathymetry & DEMs
        ├── wid/                                # any reservoir’s WID datasets
        └── ecology/                            # hydrology-linked ecological datasets
```

This directory layout is **fully extensible** for future reservoirs, rivers, and state programs.

---

# 🌎 2. Hydrology STAC Domain Architecture

The hydrology domain is composed of multiple **STAC Collections**, each organized by  
reservoir, region, or topic.

### ✔ Spatial Subdomains
- Tuttle Creek  
- Milford  
- Perry  
- Clinton  
- Kansas River  
- Blue River  
- Missouri Basin (lower Kansas context)  
- Statewide hydroclimate

### ✔ Thematic Subdomains
- Hydrology (inflows, outflows, stage, storage)  
- Sedimentation (delta growth, sediment volumes, TSS)  
- Bathymetry (1962–present)  
- Water Quality (NTU, DO, nutrients)  
- Flood Operations  
- Climate Drivers (Mesonet, PRISM, NOAA NCEI)  
- Ecological Responses  
- WID 2025 (water injection dredging)  

Each subdomain includes one or more STAC Collections.

---

# 🛰️ 3. Required STAC 1.0.0 Metadata (Domain Rules)

Every Item in this domain **must** include:

### ✔ Core Fields
- `stac_version`
- `type`
- `id`
- `collection`
- `geometry`
- `bbox`
- `properties.datetime`  
- `properties.start_datetime`  
- `properties.end_datetime`  
- `assets` (at least one)

### ✔ Hydrology-Specific Required Fields
| Field | Purpose |
|------|---------|
| `kfm:parameter` | Hydrologic variable (flow, turbidity, DO, depth, etc.) |
| `kfm:units` | SI or domain standard |
| `kfm:site` | Canonical KFM site code |
| `kfm:provider` | Dataset owner/host |
| `kfm:method` | Sensor/survey/algorithm |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | QA/QC flags |
| `kfm:project` | e.g., “Sedimentation-History” |

### ✔ Strongly Recommended
- `keywords`  
- `summaries`  
- `kfm:hydrologic_region`  
- `kfm:license_text`  
- `kfm:processing_history`

---

# 📐 4. Asset Standards for Hydrology

### ✔ Allowed Formats
| Format | Use Case |
|--------|-----------|
| **COG (Cloud-Optimized GeoTIFF)** | Bathymetry, DoD rasters, sediment extents |
| **GeoJSON** | Vector surveys, transects, plume polygons |
| **CSV / CSVW** | Timeseries |
| **NetCDF (CF-compliant)** | Climate, hydrodynamic rasters |
| **MP4 (optional)** | ADCP plume videos |

### ✔ Asset Fields
Each asset MUST include:
- `href`  
- `type`  
- `roles`  
- `title` (recommended)  
- `description` (recommended)  

---

# 🧭 5. Collection-Level Metadata Rules

### Required (in `collection.json`)
- `"type": "Collection"`
- `"stac_version": "1.0.0"`
- `"id"` unique across hydrology domain
- `"title"`
- `"description"`
- `"keywords"`
- `"extent"` (spatial + temporal)
- `"providers"`
- `"license"`
- `"assets"` (optional thumbnails, QA docs)
- `"links"` (root, parent, items)

### STAC Summaries
Collections should define summaries for:
- `kfm:parameter`  
- `kfm:units`  
- `kfm:site`  
- `kfm:method`  
- `datetime` ranges  

This accelerates UI search and STAC API filtering.

---

# 🕸 6. DCAT 3.0 Mappings (Hydrology Domain)

| STAC Field | DCAT Equivalent |
|------------|-----------------|
| `id` | `dct:identifier` |
| `description` | `dct:description` |
| `providers` | `dcat:contactPoint` |
| `assets[].href` | `dcat:downloadURL` |
| `extent.spatial` | `dct:spatial` |
| `extent.temporal` | `dct:temporal` |
| `keywords` | `dcat:keyword` |
| `license` | `dct:license` |

---

# 🧬 7. PROV-O Lineage Mapping

Every hydrology STAC Item creates:

### Entities
- `prov:Entity` → the dataset  
- `prov:Activity` → ETL process that generated it  
- `prov:Agent` → USGS, USACE, KWO, KDHE, etc.

### Required relationships
- `prov:wasGeneratedBy`  
- `prov:wasAttributedTo`  
- `prov:used` (raw sources)  

---

# 🛰 8. Graph Ontology (CIDOC-CRM + GeoSPARQL + OWL-Time)

Every STAC Item maps to:

### CRM Entities
- `E73 InformationObject` — dataset  
- `E53 Place` — spatial grounding  
- `E7 Activity` — events (e.g., WID 2025)  
- `E3 ConditionState` — hydrologic condition summaries  
- `ObservationSeries` — for time-series  

### GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin`  
- `geo:asWKT`

### OWL-Time
- `time:hasTime`  
- `time:hasBeginning`  
- `time:hasEnd`

---

# 🔬 9. STAC → ETL → Graph Pipeline

```
Raw Dataset
    ↓ (extract)
Schema normalization
    ↓ (transform)
Asset production (CSVW, COG, GeoJSON)
    ↓ (annotate-stac)
STAC Items created
    ↓ (validate)
STAC → Graph ingestion
```

All steps recorded in:
`mcp/experiments/hydrology/stac_creation_<id>.md`

---

# 🧪 10. Hydrology STAC Item Classes

### 10.1 Hydrology Core
- inflows  
- outflows  
- stage  
- storage  
- hydrographs  
- climate drivers  

### 10.2 Bathymetry
- DEM rasters  
- DoD (difference-of-DEM)  
- reservoir polygon updates  

### 10.3 Sedimentation
- sediment cores  
- volume timeseries  
- delta position datasets  

### 10.4 Water Quality
- turbidity  
- DO  
- nutrients  
- conductivity  

### 10.5 WID 2025
- turbidity sensors  
- density-current ADCP  
- nutrient samples  
- jet operations metadata  

### 10.6 Downstream Effects
- tailwater DO  
- tailwater turbidity  
- plume propagation polygons  

### 10.7 Ecology
- fish surveys  
- mussel polygons  
- macroinvertebrate data  

---

# 🎯 11. Focus Mode v3 Integration

Focus Mode uses STAC metadata to:

- Load hydrology time-series  
- Render bathymetry maps  
- Highlight WID turbidity pulses  
- Summarize sedimentation  
- Visualize downstream responses  
- Link datasets → Story Nodes → timelines  

---

# 📖 12. Story Node Integration

Hydrology datasets provide foundational assets for:

- **"A Reservoir Filling From the Bottom Up"**  
- **"Downstream of the Dam"**  
- **"The 2025 WID Demonstration"**  
- **"Kansas Climate Cycles"**  
- **"Sediment on the Move"**  

Each Story Node references this hydrology domain via `relation.rel = "uses-dataset"`.

---

# 🚀 13. Expansion Roadmap

Future hydrology STAC needs:

- 3D hydrodynamic model outputs (NetCDF/GRIB)  
- Real-time MQTT sensor streaming  
- Climate vulnerability rasters (2030–2100)  
- Flood inundation polygons  
- Sentinel-2 turbidity rasters  
- Lidar-derived water-surface models  
- Cross-reservoir transport datasets  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of hydrology STAC domain index (super-edition).

---

[⬅️ Back to Data Home](../../README.md) • [🏠 KFM v11 Master Guide](../../../docs/reference/kfm_v11_master_documentation.md)

