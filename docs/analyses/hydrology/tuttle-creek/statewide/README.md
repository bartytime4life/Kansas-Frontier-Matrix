---
title: "🌎 Kansas Frontier Matrix — Statewide Hydrology Context for Tuttle Creek"
path: "docs/analyses/hydrology/tuttle-creek/statewide/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/docs-analyses-hydrology-tc-statewide-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Analysis"
intent: "hydrology-tuttle-creek-statewide-context"
semantic_document_id: "kfm-analyses-hydrology-tuttle-creek-statewide-index"
doc_uuid: "urn:kfm:docs:analyses:hydrology:tuttle-creek:statewide:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌎 **Kansas Frontier Matrix — Statewide Hydrology Context for Tuttle Creek**  
`docs/analyses/hydrology/tuttle-creek/statewide/README.md`

**Purpose:**  
Provide statewide hydrologic, climatic, and watershed-scale context for interpreting Tuttle Creek  
Lake’s sedimentation, WID operations, flood behavior, and downstream ecological dynamics.  
Acts as a regional “parent index” connecting reservoir-scale analyses to Kansas-wide systems  
within KFM v11.

</div>

---

# 📘 Overview

Tuttle Creek Lake is embedded in a **much larger hydrologic system** spanning the **Big Blue River**,  
the **Kansas River**, the **Lower Missouri Basin**, and upstream **Nebraska/Iowa headwaters**.  

Understanding the reservoir’s sedimentation, water-quality behavior, and WID performance requires  
placing it within:

- Kansas-wide **hydroclimatic patterns**  
- Historical **flood and drought cycles**  
- **Statewide sediment budgets** and watershed erosion  
- **Groundwater–surface water interactions**  
- Inter-reservoir dynamics (Milford → Tuttle → Perry → Clinton → Kaw)  
- Downstream ecological corridors  

This document catalogs statewide hydrologic factors, datasets, STAC layers, and graph entities  
needed to contextualize all Tuttle Creek analyses.

---

# 🗂 Directory Layout

```text
docs/
└── analyses/
    └── hydrology/
        ├── README.md
        └── tuttle-creek/
            ├── README.md
            ├── water-injection-dredging-2025.md
            ├── monitoring-design-2025.md
            ├── sedimentation-history.md
            ├── downstream-effects.md
            └── statewide/
                └── README.md   # this file
```

---

# 🌧️ 1. Kansas Hydroclimate Overview

Kansas hydrology is governed by **continental climate gradients** and strong east–west contrasts:

- **Precipitation gradient:** ~18 inches/year (west) → ~40+ inches/year (east)  
- **Runoff increases eastward**; sediment yields generally increase from loess hills toward  
  agricultural basins  
- **Synoptic drivers:** ENSO, Arctic Oscillation, Rockies snowpack, Gulf moisture return  
- **Extreme events:**  
  - 1951 Great Flood  
  - 1986 Kansas River flooding  
  - 1993 Missouri Basin flood  
  - 2019 multi-reservoir overtopping near-misses  
  - 1930s Dust Bowl drought  
  - 1952–57 drought  
  - 2011–2013 Ogallala drought impacts  

These patterns form the backdrop for Tuttle Creek inflows, sediment delivery, and risks.

---

# 🏞️ 2. Statewide Watershed Structure

Kansas is partitioned into major HUC regions relevant to Tuttle Creek:

## 🗺️ 2.1 Big Blue River Basin (Primary Tuttle Creek watershed)
- Headwaters in Nebraska; loess-derived sediments  
- High sediment transport during snowmelt + convective storms  
- Major tributaries: Little Blue River, Black Vermillion River  
- Reservoir upstream: **Milford Lake**

## 🏞️ 2.2 Kansas River Basin
- Receives Tuttle Creek releases → influences Topeka & KCK flood stages  
- Key tributaries: Solomon, Saline, Republican, Smoky Hill

## 🌾 2.3 Agricultural hotspots
- No-till adoption varies by county  
- Row-crop intensification correlates with increased suspended sediment loads  
- Watershed BMPs influence long-term Tuttle Creek sedimentation

---

# 💧 3. Reservoir System Context (Milford → Tuttle → Perry → Clinton → Kaw)

Tuttle Creek is part of a **four-reservoir operational chain**:

| Reservoir | Purpose | Notes |
|---------:|---------|-------|
| **Milford Lake** | Upstream buffer | Influences Tuttle Creek inflows & sediment. |
| **Tuttle Creek** | Flood control, water supply, recreation | Significant sedimentation. |
| **Perry Lake** | Downstream buffer | Receives sediment-poor water from Tuttle Creek. |
| **Clinton Lake** | Regional modulator | Affects Kaw River dynamics. |

Implications:

- Upstream reservoir drawdowns impact WID density current behavior.  
- Tuttle Creek releases shape **Kansas River geomorphology**.  
- Reservoir-to-reservoir interactions are key Focus Mode pathways.

---

# 🧪 4. Statewide Sediment Budget

Kansas sediment dynamics reflect:

- **Loess-dominated uplands** → high erodibility  
- **Agricultural storm events** → rapid sediment pulses  
- **Channel incision / aggradation cycles**  
- **Reservoir trapping** as major sediment sinks  

Statewide sediment budget drivers:

- Land cover (cropland expansion, prairie loss)  
- Riparian buffer health  
- Upland erosion  
- Flood-driven sediment surges (e.g., 1993, 2019)

Tuttle Creek receives some of the **highest sediment loads in the state** due to watershed size  
and land use.

---

# 🌪️ 5. Flood Hazard Context

Flood impacts relevant to Tuttle Creek:

- **Kansas River floodplain** includes major population centers  
- Tuttle Creek’s flood-control function is critical for Topeka, Lawrence, KCK  
- During extreme events:

  - WID is suspended  
  - Gate operations shift to Stage-Based Regulation  
  - Downstream sediment and nutrient loads spike  

Flood datasets (to be included in STAC):

- USGS peak-flow series (NWIS)  
- NOAA Atlas 14 precipitation  
- FEMA flood insurance maps  
- NWS AHPS historical hydrographs  

---

# 🐟 6. Statewide Ecological Corridors

State-relevant ecological layers informing Tuttle Creek analyses:

- Mussel habitat corridors (Kansas River → Big Blue River)  
- Fish migration pathways (gar, catfish, sturgeon)  
- Wetland complexes (Cheyenne Bottoms, Quivira NWR)  
- Prairie–riparian transition zones  
- Downstream endangered species (e.g., pallid sturgeon)  

These help explain WID monitoring requirements and ecological constraints.

---

# 🛰 7. STAC Integration (Statewide Layers)

Recommended statewide hydrology layers:

```text
data/stac/hydrology/statewide/
├── kansas-river-inflows.json
├── statewide-flood-history.json
├── sediment-yield-by-county.json
├── hydroclimate-timeseries.json
└── reservoirs-system.json
```

All STAC Items must include:

- Spatial footprints (statewide or watershed polygons)  
- Temporal extents  
- Provenance & license  
- DCAT-compatible dataset descriptions  

---

# 🧠 8. Graph Model (State → Basin → Reservoir)

CIDOC-CRM + GeoSPARQL structure:

- `Place:Kansas`  
- `Place:Big_Blue_River_Basin`  
- `Place:Kansas_River_Basin`  
- `Place:Tuttle_Creek_Reservoir`  
- `Place:Milford_Reservoir`  
- `Place:Perry_Reservoir`  
- `ObservationSeries:StatewideHydroClimate`  
- `Event:Statewide_Flood_<Year>`  

Relationships enable Focus Mode to traverse:

- From statewide hydrology → basin → reservoir → event → dataset  
- Provide hierarchical roll-ups (state → watershed → reservoir)

---

# 📖 9. Story Node Integration

Statewide narratives relevant to Tuttle Creek:

- **“The Great Floods of Kansas”** — 1903, 1951, 1993  
- **“Sediment on the Move”** — agricultural erosion → reservoir impacts  
- **“Chain of Reservoirs”** — how Milford, Tuttle, Perry, Clinton interact  
- **“Kansas Climate Cycles”** — droughts, ENSO patterns, long-term shifts  

These statewide Story Nodes provide top-level context for reservoir-level Story Nodes such as  
**WID 2025**, **Sedimentation History**, and **Flood Operations**.

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of statewide hydrology context for Tuttle Creek.

---

[⬅️ Back to Tuttle Creek Index](../README.md) • [🏠 KFM v11 Master Guide](../../../../reference/kfm_v11_master_documentation.md) • [📂 Data Index](../../../../data/README.md)

