---
title: "🌊 Kansas Frontier Matrix — Tuttle Creek Hydrology Analysis Index"
path: "docs/analyses/hydrology/tuttle-creek/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/docs-analyses-hydrology-tuttle-creek-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Analysis"
intent: "hydrology-tuttle-creek-index"
semantic_document_id: "kfm-analyses-hydrology-tuttle-creek-index"
doc_uuid: "urn:kfm:docs:analyses:hydrology:tuttle-creek:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌊 **Kansas Frontier Matrix — Tuttle Creek Hydrology Analysis Index**  
`docs/analyses/hydrology/tuttle-creek/README.md`

**Purpose:**  
Serve as the v11-compliant index for all Tuttle Creek hydrology, sedimentation, hazard, and  
water-quality analyses within the Kansas Frontier Matrix. Provides navigational structure, STAC/graph  
integration context, and links to all Tuttle-Creek-related subdocuments.

</div>

---

# 📘 Overview

Tuttle Creek Lake is one of Kansas’s most important multipurpose reservoirs, with a hydrologic record  
shaped by sedimentation, flood-control operations, WID (Water Injection Dredging) experimentation,  
watershed behavior, and downstream ecological interactions.  

This index consolidates all Tuttle Creek–specific hydrology analyses, monitoring designs, datasets, STAC  
collections, and Story Nodes that interact with the reservoir and its operations.

---

# 🗂 Directory Layout

```text
docs/
└── analyses/
    └── hydrology/
        ├── README.md
        └── tuttle-creek/
            ├── README.md                     # this file
            ├── water-injection-dredging-2025.md
            ├── monitoring-design-2025.md     # future WQ/QA-QC spec
            ├── sedimentation-history.md      # future long-term trends
            ├── downstream-effects.md         # future geomorphology/biology
            └── datasets/
                └── README.md                 # dataset-level index
```

---

# 🧭 Hydrology Focus Areas

These are the primary hydrologic dimensions tracked for the Tuttle Creek system:

## 💧 1. Reservoir Water Balance
- Inflows (Big Blue & Little Blue Rivers)  
- Storage, pool elevation, releases  
- Evaporation & watershed climatic drivers  
- Integration with historical USGS NWIS streamflow

## 🏞️ 2. Sedimentation & Capacity Loss
- Long-term sediment accumulation (1962–present)  
- Storage loss curves & projections  
- Spatial sediment distribution (delta, forebay, channel)  
- Watershed erosion contributors  

## 🌪️ 3. Flood Operations & Hydrologic Hazards
- Historical flood hydrographs  
- USACE flood-control manuals & regulation schedules  
- Connections to Kansas River peak flows  
- Downstream risk propagation

## 🧪 4. Water Quality & Ecological Conditions
- Turbidity / TSS / nutrients  
- DO sag during high-turbidity events  
- Mussel, fish, and riparian responses  
- Seasonal thermal stratification impacts

## 🚧 5. Water Injection Dredging (WID) Program
- 2025 Phase 1 demonstration experiment  
- Monitoring design, sensor networks, turbidity thresholds  
- Sediment density-current behavior  
- Comparative analysis: WID vs. traditional dredging  

---

# 🛰️ STAC & Data Integration

Tuttle Creek hydrology analyses are supported by a dedicated STAC collection:

```text
data/stac/hydrology/tuttle-creek/
├── collection.json
└── items/
    ├── inflow-timeseries.json
    ├── turbidity-wid-2025.json
    ├── sediment-core-locations.json
    └── wq-dam-tailwater-2025.json
```

Each STAC Item includes:

- **Spatial footprint** (reservoir, dam, or monitoring station)  
- **Temporal range**  
- **Parameter type:** inflow, turbidity, DO, suspended sediment, etc.  
- **Provenance:** agency source, dataset lineage, ETL step  
- **Licensing & attribution**

---

# 🕸 Graph Integration (CIDOC-CRM + GeoSPARQL + OWL-Time)

Tuttle Creek entities in the knowledge graph include:

- `Place:Tuttle_Creek_Reservoir`  
- `Place:Tuttle_Creek_Dam`  
- `Event:WID_Phase1_2025`  
- `Event:Historic_Flood_<Year>`  
- `ObservationSeries:Turbidity_Tailwater`  
- `Actor:USACE_Kansas_City_District`  
- `Actor:Kansas_Water_Office`  

All entities use:

- **GeoSPARQL geometry** for spatial features  
- **OWL-Time** for temporal anchors  
- **PROV-O** for dataset lineage  
- **DCAT** for dataset cataloging

---

# 📄 Available Subdocuments

### 📘 Tuttle Creek Water Injection Dredging (WID) — 2025 Technical Summary  
`water-injection-dredging-2025.md`  
Comprehensive description of the 2025 WID demonstration, monitoring, sediment behavior, risks, and  
STAC/graph connections.

### 📘 Monitoring Design — Water Quality & Ecological 2025  
`monitoring-design-2025.md` *(future)*  
Detailed QA/QC framework for turbidity, DO, nutrients, biological surveys, and downstream analysis.

### 📘 Sedimentation History & Capacity Trends  
`sedimentation-history.md` *(future)*  
Long-term storage loss reconstruction + projections through 2100.

### 📘 Downstream Effects & Geomorphic Response  
`downstream-effects.md` *(future)*  
Channel morphology & ecological response modeling under different hydrologic/depositional conditions.

### 📘 Dataset Index  
`datasets/README.md` *(future)*  
Pointer to STAC Items + processed hydrology assets.

---

# 📖 Story Node / Focus Mode Integration

Tuttle Creek has multiple candidate Story Nodes:

- **“A Reservoir Filling from the Bottom Up”** — sedimentation narrative  
- **“The 2025 Water Injection Experiment”** — engineering & hazards  
- **“Downstream from the Dam”** — ecological storyline  
- **“Floodwaters and the Big Blue”** — hydrologic hazard storyline  

Each Story Node links:

- Places → Reservoir / dam / river  
- Events → WID / floods / sedimentation transitions  
- Documents → USACE, KWO, academic, press  
- Observations → time-series from STAC

All Story Nodes should be encoded using `story-node.schema.json` with:

- Geometry (Point/Polygon)  
- Temporal extent  
- Provenance links  
- Alternate narratives for different audiences  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Tuttle Creek hydrology index under KFM-MDP v11.

---

[⬅️ Back to Hydrology Index](../README.md) • [🏠 Back to KFM v11 Master Guide](../../../reference/kfm_v11_master_documentation.md) • [📂 Data & Sources Index](../../../data/README.md)

