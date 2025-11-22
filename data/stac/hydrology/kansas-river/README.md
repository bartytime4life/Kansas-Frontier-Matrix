---
title: "🌊 Kansas Frontier Matrix — Kansas River Hydrology STAC Collection (v11 Super-Edition)"
path: "data/stac/hydrology/kansas-river/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-kansasriver-index-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Collection Index"
intent: "stac-hydrology-kansas-river-index"
semantic_document_id: "kfm-stac-hydrology-kansas-river-index"
doc_uuid: "urn:kfm:stac:hydrology:kansas-river:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public • Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌊 **Kansas River Hydrology STAC Collection (v11 Super-Edition)**  
`data/stac/hydrology/kansas-river/README.md`

**Purpose:**  
Define the **complete STAC specification** for the Kansas River hydrology domain — including  
flood histories, water-quality trends, sediment transport, reservoir-system influence, geomorphic  
responses, ecological corridors, and climate-driven hydrologic behavior.  
This is the canonical metadata hub for all Kansas River datasets in KFM v11.

</div>

---

# 📘 0. Overview

The **Kansas River (“Kaw”)** is the *principal hydrologic artery* of northeast Kansas. It integrates the  
outflows of:

- **Milford Lake**  
- **Tuttle Creek Lake**  
- **Perry Lake**  
- **Clinton Lake**

and flows 170+ miles to Kansas City, where it joins the Missouri River.

The Kansas River hydrology STAC collection supports:

- Flood modeling (1903, 1951, 1993, 2019)  
- Sediment routing from upstream reservoirs  
- Water quality studies (TSS, turbidity, nutrients, DO)  
- Geomorphic assessment (incision, deposition, channel migration)  
- Ecological corridor mapping (mussels, fish, macroinvertebrates)  
- Climate-driven hydrologic variability  
- AI-narrative generation (Story Nodes, Focus Mode v3)  

---

# 🗂️ 1. Directory Layout

```text
data/
└── stac/
    └── hydrology/
        └── kansas-river/
            ├── collection.json
            └── items/
                ├── flood-1951-hydrograph.json
                ├── flood-1993-hydrograph.json
                ├── flood-2019-hydrograph.json
                ├── wq-turbidity.json
                ├── wq-do.json
                ├── sediment-tss.json
                ├── sediment-transport.json
                ├── geomorphology-crosssections.json
                ├── ecological-corridors.json
                ├── macroinv-surveys.json
                ├── fish-assemblages.json
                ├── riparian-zones.json
                ├── inundation-extents.json
                ├── hydroclimate-drivers.json
                └── statewide-integration.json
```

---

# 🌍 2. Spatial & Temporal Extent

### Spatial bbox (Kansas River corridor)
```
[-96.85, 38.70, -94.60, 39.25]
```

### Temporal range  
```
1800-01-01T00:00:00Z → present
```

---

# 🏞️ 3. Hydrologic Sub-Domains (Kansas River)

The Kansas River is divided into:

### ✔ Upper Kaw (Junction City → Topeka)
- Dominated by Milford + Tuttle discharge  
- High sediment variability  
- Strong flood-wave geometry  

### ✔ Middle Kaw (Topeka → Lawrence)
- Perry & Clinton influence  
- Turbidity + DO changes  
- Riffle/pool ecological zones  

### ✔ Lower Kaw (Lawrence → KCK)
- Urban corridor  
- Kansas City flood risk  
- Missouri River backwater influence  

Each reach has its own hydrology STAC Items.

---

# 🔍 4. Dataset Themes

## 4.1 Flood Events
- 1903  
- 1951  
- 1993  
- 2019  
- Simulated 500-yr flood grids  
- Inundation extents (GIS rasters)

## 4.2 Hydrology & Water Quality
- Streamflow  
- Stage  
- DO  
- Turbidity  
- Temperature  
- Nutrients  

## 4.3 Sediment Dynamics
- TSS  
- Suspended sediment transport  
- Reservoir-derived sediment pulses  
- Loess-derived watershed contributions  

## 4.4 Geomorphology
- Channel incision  
- Sand-bar migration  
- Riffle/pool geomorphology  
- Floodplain sedimentation  

## 4.5 Ecological Response
- Mussel corridors  
- Fish assemblages  
- Macroinvertebrates  
- Riparian communities  

## 4.6 Climate & Hydroclimate
- Mesonet hydroclimate signals  
- NOAA NCEI precipitation records  
- Drought indices (SPI/PDSI)  
- Temperature extremes  

---

# 📐 5. Required STAC Metadata (Kansas River v11 Profile)

### Core Meta
```
stac_version: "1.0.0"
type: "Feature"
id: <unique>
collection: "kansas-river-hydrology"
geometry: <GeoJSON>
bbox: <array>
properties.datetime: <ISO 8601>
assets: <object>
```

### Hydrology Required
| Field | Description |
|------|-------------|
| `kfm:parameter` | hydrologic variable |
| `kfm:units` | cfs, mg/L, NTU, °C, m/s, etc. |
| `kfm:method` | gauge, lab, satellite, ADCP, model |
| `kfm:provider` | USGS, KDHE, USACE, Mesonet |
| `kfm:site` | gauge ID, transect ID |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | QA tier |
| `kfm:hydro_region` | Upper/Middle/Lower Kansas River |
| `kfm:project` | FloodHistory, SedimentRouting, EcologyCorridor |

### Recommended
- `kfm:flood_stage_flag`  
- `kfm:sensitivity` (ecological)  
- `kfm:habitat_type`  
- `kfm:dominant_species`  

---

# 🧭 6. Asset Standards (COG, GeoJSON, CSVW, NetCDF, MP4)

## ✔ COG (Raster)
Used for:
- Inundation extents  
- DEMs  
- Hydrodynamic simulation outputs  

COG requirements:
- internal tiling  
- overviews  
- `proj:epsg` defined  
- `checksum:sha256`  

## ✔ GeoJSON (Vector)
Used for:
- Ecological corridors  
- Geomorphic transects  
- Fish/mussel habitats  

## ✔ CSV/CSVW (Tabular)
Used for:
- Hydrographs  
- Water-quality monitoring  
- Cross-sectional measurements  

## ✔ NetCDF
Used for:
- Hydroclimate grids  
- 2D hydrodynamic models  

## ✔ MP4 (Optional)
Used for:
- Drone surveys  
- ADCP plume videos  

---

# 🧪 7. Example STAC Items

## 7.1 Flood Hydrograph (1951)

```json
{
  "id": "kansas-river-flood-1951-hydrograph",
  "type": "Feature",
  "stac_version": "1.0.0",
  "collection": "kansas-river-hydrology",
  "geometry": { "type": "Point", "coordinates": [-95.67, 39.05] },
  "bbox": [-95.68, 39.04, -95.66, 39.06],
  "properties": {
    "datetime": "1951-07-13T00:00:00Z",
    "kfm:parameter": "flood_hydrograph",
    "kfm:units": "cfs",
    "kfm:provider": "USGS",
    "kfm:method": "stream_gauge",
    "kfm:lineage": "etl/kansasriver1951_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Middle_Kansas_River",
    "kfm:project": "FloodHistory"
  },
  "assets": {
    "timeseries": {
      "href": "https://example.org/kansas/1951/hydrograph.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

## 7.2 Ecological Corridor (Mussels)

```json
{
  "id": "kansas-river-mussels-corridor",
  "type": "Feature",
  "stac_version": "1.0.0",
  "collection": "kansas-river-hydrology",
  "geometry": { "type": "LineString", "coordinates": [...] },
  "properties": {
    "datetime": "2024-07-01T00:00:00Z",
    "kfm:parameter": "mussel_corridor",
    "kfm:units": "index",
    "kfm:provider": "KDWPT",
    "kfm:method": "survey_compilation",
    "kfm:lineage": "etl/kansasriver_mussels_2024",
    "kfm:quality": "A",
    "kfm:hydro_region": "Lower_Kansas_River",
    "kfm:project": "EcologyCorridor"
  },
  "assets": {
    "geojson": {
      "href": "https://example.org/kansas/ecology/mussels_corridor.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

---

# 🕸️ 8. Ontology Mapping (CIDOC-CRM, GeoSPARQL, OWL-Time)

## CIDOC-CRM
- `E53 Place` → Kansas River reaches  
- `E7 Activity` → hydrologic events (floods, surveys)  
- `E3 ConditionState` → ecological/hydrologic states  
- `E73 InformationObject` → STAC dataset  
- `E39 Actor` → USGS, KDHE, KDWPT, USACE  

## GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin`  
- `geo:asWKT`  

## OWL-Time
- `time:hasTime`  
- `time:hasBeginning`  
- `time:hasEnd`  

---

# 🔬 9. PROV-O Lineage

Each Item is:

- `prov:Entity` = dataset  
- Generated by `prov:Activity` = ETL pipeline  
- Attributed to `prov:Agent` = provider  
- Based on `prov:used` = raw source(s)  

Example lineage:

```
Raw USGS hydrograph → ETL normalization → CSVW → STAC Item → Graph
```

---

# 🚧 10. ETL → STAC → GRAPH Workflow

```
Raw Data
    ↓ extract
Normalize, harmonize, reproject
    ↓ transform
Generate assets (COG, CSVW, GeoJSON, MP4)
    ↓ annotate
Create STAC Item
    ↓ validate
Load into Neo4j graph
    ↓
Enable Focus Mode + Story Nodes
```

Document all runs under:  
`mcp/experiments/hydrology/kansas-river/*`

---

# 🎯 11. Focus Mode v3 Integration

Focus Mode uses Kansas River Items to show:

- Flood histories  
- Time-series of WQ/TSS/DO  
- Sediment transport  
- Ecological responses  
- Basin-wide hydrology  
- Reservoir-system interactions  
- Climate anomalies  
- Downstream propagation of flows/sediment  

Selecting **“Kansas River”** loads all Items where:

- `kfm:hydro_region LIKE "Kansas%"`  
- `parameter IN (flow, TSS, turbidity, DO, sediment_transport, hydroclimate)`  

---

# 📖 12. Story Node Integration

Kansas River Items drive Story Nodes such as:

- **“The Great Flood of 1951”**  
- **“The 1993 Midwest Flood”**  
- **“Sediment on the Move”**  
- **“Reservoirs and the Kaw: A Connected System”**  
- **“Ecological Corridors of the Kansas River”**

Each Node embeds dataset references:

```json
{
  "rel": "uses-dataset",
  "target": "kansas-river-flood-1993-hydrograph"
}
```

---

# 🚀 13. Expansion Roadmap

Upcoming Kansas River STAC Items:

- ADCP velocity transects (2026+)  
- Machine-learning flood depth rasters  
- CMIP6 hydrologic anomaly projections  
- Multi-reach sediment budget Items  
- 2D hydrodynamic simulation outputs  
- UAV-based geomorphic monitoring  
- Fish/mussel corridor updates  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial super-edition STAC collection index created.

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [📂 Data Home](../../README.md) • [🏠 KFM Master Guide](../../../../docs/reference/kfm_v11_master_documentation.md)

