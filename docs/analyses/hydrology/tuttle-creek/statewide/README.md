---
title: "🌎 Kansas Frontier Matrix — Statewide Hydrology Context for Tuttle Creek"
path: "docs/analyses/hydrology/tuttle-creek/statewide/README.md"
version: "v11.1.0"
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
doc_uuid: "urn:kfm:docs:analyses:hydrology:tuttle-creek:statewide:index:v11.1.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌎 **Statewide Hydrology Context for Tuttle Creek Reservoir**  
`docs/analyses/hydrology/tuttle-creek/statewide/README.md`

**Purpose:**  
Provide an expanded, reorganized, and technically enriched overview of Kansas-wide hydrology,  
sedimentation, climate, and multi-reservoir interactions shaping the dynamics at **Tuttle Creek Lake**.  
This file serves as the statewide parent index for all hydrologic analyses connected to the  
Tuttle Creek watershed in KFM v11.

</div>

---

# 🌎 Kansas Hydrology at a Glance (Executive Summary)

Kansas hydrology is governed by **continental gradients**, **reservoir regulation**, **climate variability**,  
and **watershed land use**. These statewide drivers converge at **Tuttle Creek**, influencing:

- Inflows & storage  
- Sediment loading  
- Flood risk  
- Water quality  
- Ecological connectivity  
- WID (Water Injection Dredging) performance  

This expanded document provides statewide-scale analysis that informs Tuttle Creek–specific  
modules throughout the hydrology folder.

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
                ├── README.md                   # this file
                └── sedimentation-overview.md   # statewide sedimentation analysis
```

---

# 🌧️ 1. Kansas Hydroclimate Overview

Kansas spans multiple climatic regimes, with strong **east–west gradients**:

### 🌡️ Climate & Hydrologic Drivers
- Western Kansas: **semi-arid**, low runoff  
- Central Kansas: mixed agricultural runoff, sand-bed rivers  
- Eastern Kansas: humid continental, highest precipitation and discharge  

### 🌪️ Key Extreme Event Patterns
- Frequent multi-day convective rainfall  
- Snowmelt-driven spring flows in northern basins (NE/IA)  
- Recurring drought–flood cycles  
- Strong ENSO teleconnections  
- Intensifying rainfall under climate change  

These patterns set boundary conditions for sedimentation, WID operations, and flood-control behavior at  
Tuttle Creek.

---

# 🏞️ 2. Statewide Watersheds & Geomorphic Provinces

Kansas contains several hydrologic provinces:

### 🗺️ 2.1 Big Blue River Basin (Primary Source for Tuttle Creek)
- Upland loess soils → highly erodible  
- Strong spring pulses  
- Agricultural stormflow  
- High sediment yield relative to basin size  

### 🗺️ 2.2 Kansas River Basin
- Receives Tuttle Creek outflows  
- Controls hydrologic risk for Topeka, Lawrence, and Kansas City  
- Major tributaries: Republican, Smoky Hill, Saline, Solomon  

### 🗺️ 2.3 Supporting Basins
- Missouri River (ultimate sink)  
- Lower Republican (inter-reservoir dynamics)  
- Sand-bed rivers (Arkansas, Ninnescah, Cimarron)  

---

# 🌊 3. Multi-Reservoir Operational Chain Dynamics

Tuttle Creek is embedded in the **Milford → Tuttle → Perry → Clinton → Kaw** system:

| Reservoir | Function | Influence on Tuttle Creek |
|---------:|----------|---------------------------|
| **Milford** | Upstream regulation | Controls Tuttle inflows & sediment |
| **Tuttle Creek** | Flood control, sediment risk | Core of this analysis |
| **Perry** | Downstream buffer | Receives altered water-quality signals |
| **Clinton** | Regional modulator | Alters Kaw River baseflows |
| **Kaw River** | Primary floodpath | Downstream hazard propagation |

Key dynamics:

- Upstream drawdowns amplify WID density-current transport.  
- Tuttle’s releases alter Kansas River sediment-starvation patterns.  
- Reservoir chain dynamics shape downstream Story Nodes.  

---

# 🧪 4. Statewide Sediment Budget (Macro Drivers)

Sedimentation at Tuttle Creek is a **statewide phenomenon**, not an isolated reservoir problem.

### 🧱 4.1 Erosion Sources
- Loess uplands (SE Nebraska → NE Kansas)  
- Agricultural storm runoff  
- Channel-bank sloughing  
- Flood-enhanced sediment mobilization  

### 🩻 4.2 Transport Pathways
```text
Upland erosion → Tributaries → Big Blue River → Tuttle Creek delta → Forebay → Dam outlet
```

### 🧮 4.3 Reservoir Sediment Sinks
- Tuttle Creek (~46% capacity loss)  
- Perry (~30–40%)  
- Milford (~20–25%)  
- Clinton (~15–20%)  

Reference: See `sedimentation-overview.md` for full statewide analysis.

---

# 💧 5. Statewide Water-Quality Regime

Important indicators shaping WID and sedimentation analyses:

- **Turbidity** (consistent east–west gradient)  
- **Nutrient loads** (ag ricultural watersheds → Big Blue → Tuttle Creek)  
- **Temperature stratification** (affects density-current pathways)  
- **Dissolved oxygen sag events** (critical for downstream WID monitoring)  

Statewide monitoring networks (KDHE, USGS NWIS) feed directly into KFM’s hydrology datasets.

---

# 🛰️ 6. Remote Sensing & Statewide Monitoring Assets

### 📡 Satellite & Aerial Data
- Landsat (sediment plume dynamics, land cover)  
- Sentinel-2 (turbidity proxies)  
- NAIP (high-res aerial basemaps)  

### 🛰️ Ground-Based Networks
- USGS stream gauges  
- KDHE long-term monitoring stations  
- Reservoir bathymetry surveys  
- Kansas Mesonet (climate forcing inputs)

All of these produce STAC-ready assets in KFM’s statewide collection.

---

# 🌪️ 7. Flood & Drought Regimes

Flood-control behavior at Tuttle drives statewide risk.

### 🚨 Major historical events
- 1903, 1951, 1993, 2019  
- Ice-jam risks (Kansas/Republican confluence)  
- Kansas River floodplain vulnerability  

### 🔥 Drought impacts
- Ogallala declines influence tributary flows  
- 2011–2013 drought reshaped flood-control rule curves  

These events have their own Story Nodes intersecting Tuttle Creek.

---

# 🐟 8. Statewide Ecological Corridors

### 🧬 Critical habitats
- Mussel corridors (Big Blue → Kansas → Missouri)  
- Prairie river fish assemblages  
- Riparian vegetation mosaics  
- Wetland complexes: Cheyenne Bottoms, Quivira  

### 🌱 Why this matters for Tuttle Creek
- Downstream ecology drives WID monitoring thresholds  
- Habitat continuity → species response to sediment pulses  
- Reservoir operations influence ecological drought severity  

---

# 🛰️ 9. STAC Integration (Statewide Layers)

Recommended statewide hydrology STAC Items:

```text
data/stac/hydrology/statewide/
├── climate-gradient.json
├── kansas-river-system.json
├── statewide-sediment-budget.json
├── flood-hydrographs.json
└── ecological-corridors.json
```

Each Item includes:

- Spatial footprint (statewide or HUC region)  
- Temporal precision (annual, daily, event-based)  
- License & provenance  
- Sensor lineage & data-quality notes  

---

# 🕸️ 10. Graph Model (State → Basin → Reservoir → Event)

Hierarchy:

- `Place:Kansas`  
- `Place:Hydrologic_Province_<Region>`  
- `Place:Big_Blue_River_Basin`  
- `Place:Tuttle_Creek_Reservoir`  
- `Event:Flood_<Year>`  
- `E3 ConditionState:Sediment_Load_<Year>`  
- `ObservationSeries:HydroClimate`  

Relationships allow:

- Focus Mode → navigate from statewide → Tuttle Creek → WID event  
- Story Nodes → link local narratives to statewide drivers  
- Data fusion between basins and reservoirs  

---

# 📖 11. Story Node Integration

Statewide narratives foundational to Tuttle Creek:

- **“Kansas Climate Cycles”** — ENSO, drought–flood sequences  
- **“Sediment on the Move”** — watershed erosion → reservoir impacts  
- **“Chain of Reservoirs”** — multi-reservoir system shaping Kansas River  
- **“The Great Floods”** — multi-reservoir mitigation across decades  

Each statewide Story Node should frame how local events at Tuttle Creek fit into broader hydrology.

---

# 🧭 12. Recommended Next Datasets & Analyses

### Phase II expansion suggestions:
- Kansas River 2D hydrodynamic models  
- Snowmelt-driven forecast layers (Big Blue headwaters)  
- USACE bathymetry → long-term delta growth curves  
- Multi-sensor turbidity fusion (Sentinel-2 + USGS + KDHE)  
- WID scenario modeling under climate futures  

---

# 🕰 Version History

- **v11.1.0 (2025-11-21):** Major content expansion, reorganization, and section restructuring.  
- **v11.0.0 (2025-11-21):** Initial creation of statewide hydrology context for Tuttle Creek.

---

[⬅️ Back to Tuttle Creek Index](../README.md) • [🏠 KFM v11 Master Guide](../../../../reference/kfm_v11_master_documentation.md) • [📂 Data Index](../../../../data/README.md)
