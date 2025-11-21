---
title: "🟫 Kansas Frontier Matrix — Statewide Sedimentation Dynamics & Tuttle Creek Context"
path: "docs/analyses/hydrology/tuttle-creek/statewide/sedimentation-overview.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/docs-analyses-hydrology-tc-statewide-sedimentation-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Analysis"
intent: "hydrology-tuttle-creek-statewide-sedimentation-overview"
semantic_document_id: "kfm-analyses-hydrology-tuttle-creek-statewide-sedimentation"
doc_uuid: "urn:kfm:docs:analyses:hydrology:tuttle-creek:statewide:sedimentation-overview:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🟫 **Statewide Sedimentation Dynamics — Tuttle Creek Reservoir Context**  
`docs/analyses/hydrology/tuttle-creek/statewide/sedimentation-overview.md`

**Purpose:**  
Provide a Kansas-wide sedimentation overview, highlighting watershed-scale erosion, reservoir  
sediment budgets, geomorphic processes, and how these factors converge at **Tuttle Creek Lake**,  
one of the highest sediment-loading sites in the state. Designed for KFM v11 integration  
(STAC → Graph → Focus Mode → Story Nodes).

</div>

---

# 📘 Overview

Sedimentation is one of the defining long-term hydrologic hazards in Kansas.  
Across the state’s reservoir network, sediment accumulation reduces storage capacity, affects  
aquatic habitats, and drives costly maintenance interventions. **Tuttle Creek Lake**, with **~438 million  
cubic yards** of accumulated sediment since 1962, is among the most extreme examples.  

This statewide overview contextualizes the reservoir within Kansas’s broader sediment regime.

---

# 🗺️ 1. Statewide Sediment Sources & Transport Pathways

Kansas sediment delivery is shaped by:

## 🌾 1.1 Land Use & Erosivity Patterns
- Dominance of agricultural land cover (row crops, tilled fields).  
- Higher erosivity in **loess-derived uplands** (NE Kansas, SE Nebraska).  
- Storm-driven erosion pulses during convective rainfall events.  
- Reduced prairie/grassland buffering accelerates overland sediment export.

## 🏞️ 1.2 Geologic Controls
- **Loess hills** → Easily mobilized silt/sand fraction.  
- **Alluvial valleys** → Sediment storage + remobilization cycles.  
- **Sand-bed rivers** (Republican, Kansas, Arkansas) → high mobility.

## 🌪️ 1.3 Hydrologic Drivers
- Extreme precipitation events (50–200-year storms).  
- Snowmelt contributions in the Big Blue/Little Blue headwaters.  
- Multi-year drought–flood sequences altering channel shape and transport.

---

# 📉 2. Reservoir Sedimentation Across Kansas

Kansas’s federal reservoirs exhibit a wide range of storage loss:

| Reservoir | Decade of Closure | Est. Sediment Accumulation | Storage Loss |
|---------:|-------------------|----------------------------|--------------|
| Tuttle Creek | 1962 | ~438M cy | ~46% |
| Milford | 1967 | Moderate | ~20–25% |
| Perry | 1970 | High in delta | ~30–40% |
| Clinton | 1977 | Low–moderate | ~15–20% |

## 🧭 2.1 Regional Patterns
- **Northeast Kansas**: highest erosion and reservoir sedimentation.  
- **Central Kansas**: mixed sediment loads; sand-bed channels.  
- **Western Kansas**: lower sediment due to semi-aridity but vulnerable to dust-era erosion.

## 🏗️ 2.2 Statewide Sediment Budget (Conceptual)
```text
Watershed Erosion
    ↓
Channel Transport
    ↓
Tributary Confluences
    ↓
Reservoir Delta Formation
    ↓
Forebay Aggradation
    ↓
Long-term Capacity Loss
```

---

# 🌊 3. Why Tuttle Creek Receives So Much Sediment

Tuttle Creek is uniquely exposed:

## 🗺️ 3.1 Large Watershed (Big Blue Basin)
- Drains significant portions of **Nebraska** and **Kansas**.  
- High loess content → fine sediment transport.  
- Long flowpaths → more opportunities for entrainment.

## 🧱 3.2 Reservoir Geometry
- Deep, narrow channel upstream → efficient density-current delivery.  
- Large forebay → accumulation zone with reduced velocities.

## 🚜 3.3 Land Use Upstream
- Row-crop intensity in NE Kansas & SE Nebraska.  
- Variable BMP adoption.  
- High sediment yields tied to spring storms.

## 🌊 3.4 Hydrologic Extremes
- 1993, 2019, and other major floods delivered outsized sediment pulses.  
- Seasonal snowmelt events transport sediment from headwaters to the lake.

---

# 🧪 4. Sedimentation Processes at Tuttle Creek

## 🏞️ 4.1 Delta Formation
- Sediment deltas grow from the Big Blue River inflow zone.  
- Shifting delta lobes impact recreation and channel depth.

## 🌫️ 4.2 Density Currents
- Fine sediment is transported as near-bed plumes.  
- These currents move down-reservoir even during low inflow conditions.

## 🧱 4.3 Forebay Aggradation
- Persistent infilling near the dam narrows channels and affects WID operations.

## 📉 4.4 Storage Loss Trajectory
- Without intervention, models predict **~75%** multipurpose pool filling by **2074**.

---

# 🦫 5. Ecological & Geomorphic Consequences

## 🐟 5.1 Habitat Alteration
- Loss of deep-water habitat.  
- Increased turbidity affects visual feeders.  
- Delta vegetation changes riparian structure.

## ⚖️ 5.2 Downstream Geomorphology
- Sediment-starved water downstream of reservoirs → channel incision.  
- During WID, sediment release may partially offset long-term sediment deficits.

## 🧬 5.3 Water-Quality Interactions
- Nutrient binding to sediments can amplify eutrophication.  
- Metals/legacy contaminants can mobilize.

---

# 🛰️ 6. STAC Integration (Statewide Sediment Layers)

Dataset suggestions:

```text
data/stac/hydrology/statewide-sedimentation/
├── reservoir-storage-loss.json
├── sediment-yield-county.json
├── watershed-erosion-index.json
├── tuttle-creek-delta-extent.json
└── statewide-sediment-timeseries.json
```

Each Item should include:

- Spatial polygon (HUC or reservoir extent)  
- Temporal coverage (annual/decadal)  
- Data lineage (USACE, KWO, USGS, NASA)  
- License (public domain)

---

# 🕸️ 7. Graph Model Integration

CIDOC-CRM → Neo4j mappings:

- `Place:Tuttle_Creek_Reservoir`  
- `Place:Big_Blue_River_Basin`  
- `Place:Kansas_River_Basin`  
- `E7 Activity:Sediment_Transport_<Year>`  
- `E7 Activity:Flood_Event_<Year>`  
- `E3 ConditionState:Tuttle_Creek_Capacity_<Year>`  
- `E73 InformationObject:Sediment_Survey`  
- `ObservationSeries:Sediment_Inputs`  

Key relationships:

- `P7_took_place_at` → Sediment events  
- `P70_documents` → Sediment surveys  
- `geo:hasGeometry` → Basin/reservoir polygons  
- `time:hasTime` → Annual cycles  
- `prov:wasGeneratedBy` → ETL pipelines

---

# 📖 8. Story Node Narrative (Mini)

> **“Sediment on the Move”**  
>  
> From the loess hills of Nebraska to the prairie rivers of Kansas, sediment is always in motion.  
> Every spring storm or snowmelt pulse gathers silt, clay, and sand and sends them downstream.  
> For Tuttle Creek, these pulses have added up for more than sixty years. The delta has marched  
> forward, the forebay has risen, and the reservoir’s capacity has nearly halved.  
>  
> Statewide patterns frame this story: land use, flood cycles, and watershed erosion all converge  
> here. Understanding Kansas sedimentation means understanding why Tuttle Creek fills faster  
> than nearly any other reservoir in the region.

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of statewide sedimentation overview for Tuttle Creek.

---

[⬅️ Back to Statewide Hydrology](README.md) • [🏠 KFM v11 Master Guide](../../../../../reference/kfm_v11_master_documentation.md) • [📂 Data Index](../../../../../data/README.md)

