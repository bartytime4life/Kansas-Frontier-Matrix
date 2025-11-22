---
title: "🌊 Kansas Frontier Matrix — Kansas River Hydrology STAC Items Index (v11 Super-Edition)"
path: "data/stac/hydrology/kansas-river/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/data-stac-hydro-kansasriver-items-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Items Index"
intent: "stac-kansas-river-items-index"
semantic_document_id: "kfm-stac-hydrology-kansas-river-items"
doc_uuid: "urn:kfm:stac:hydrology:kansas-river:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌊 **Kansas River Hydrology STAC Items (v11 Super-Edition)**  
`data/stac/hydrology/kansas-river/items/README.md`

**Purpose:**  
Provide the authoritative domain-level index of **all Kansas River STAC Items** across hydrology,  
flood events, water quality, sediment transport, geomorphology, ecology, hydroclimate, and  
multi-reservoir influence. Defines Item-level metadata, asset requirements, ontology mappings,  
lineage, and KFM v11 integration across Focus Mode and Story Nodes.

</div>

---

# 📘 0. Overview

This directory contains **STAC Items** describing the Kansas River’s hydrologic, geomorphic,  
ecological, and flood-related datasets from 1800 → present.

These Items represent:

- Flood hydrographs (historic & modern)  
- Water quality time-series (DO, turbidity, nutrients)  
- Sediment transport & suspended sediment concentrations  
- Geomorphic transect data & channel change  
- Ecological corridors (mussels, fish, macroinvertebrates)  
- Riparian vegetation zones  
- Inundation rasters  
- Hydroclimate drivers  
- Multi-reservoir hydrologic influence  

Every Item follows the **KFM Hydrology STAC Profile v11** and integrates seamlessly into:

```
STAC → Neo4j Graph (CIDOC + GeoSPARQL + OWL-Time)
       → API (GraphQL/REST)
       → MapLibre (spatial renders)
       → Timeline (temporal alignment)
       → Focus Mode v3 (narratives + analytics)
       → Story Node v3 (historical/environmental storytelling)
```

---

# 🗂️ 1. Directory Structure

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
                ├── inundation-extents.json
                ├── hydrology-timeseries.json
                ├── wq-turbidity.json
                ├── wq-do.json
                ├── wq-nutrients.json
                ├── sediment-tss.json
                ├── sediment-transport.json
                ├── geomorphology-crosssections.json
                ├── ecological-corridors.json
                ├── macroinv-surveys.json
                ├── fish-assemblages.json
                ├── riparian-zones.json
                └── hydroclimate-drivers.json
```

---

# 🌍 2. Item Taxonomy (Kansas River Domain)

## ✔ 2.1 Flood Event Items  
- Flood 1903  
- Flood 1951  
- Flood 1993  
- Flood 2019  
- Event-based hydrographs (CSVW)  
- Inundation rasters (COG)  
- Floodplain polygons (GeoJSON)

## ✔ 2.2 Water Quality Items  
- Turbidity (NTU)  
- DO (mg/L)  
- Nutrients (TP, TN, NO₃, NH₄)  
- Temperature gradients  

## ✔ 2.3 Sediment Transport  
- TSS (mg/L)  
- Suspended sediment loads  
- Loess-derived inputs  
- Reservoir pulse influence (Tuttle → Perry → Clinton → Kaw)

## ✔ 2.4 Geomorphology  
- Cross-sections  
- Sand-bar migration  
- Bank erosion lines  
- Riffle/pool morphology

## ✔ 2.5 Ecology  
- Mussel corridors  
- Fish communities  
- Macroinvertebrates  
- Riparian habitat zones  

## ✔ 2.6 Hydroclimate  
- Mesonet precipitation  
- NOAA long-term climate normals  
- SPI/PDSI drought indices  

---

# 📐 3. Required Metadata Fields (STAC 1.0 + KFM Hydrology Profile)

### Core STAC fields
```
stac_version
type = “Feature”
id
collection
geometry
bbox
properties.datetime
assets
```

### Required KFM hydrology fields (`kfm:*`)
| Field | Description |
|--------|-------------|
| `kfm:parameter` | hydrologic/ecologic variable |
| `kfm:units` | units of measurement |
| `kfm:provider` | dataset origin |
| `kfm:site` | gauge / reach / transect / polygon ID |
| `kfm:method` | sampling or modeling method |
| `kfm:lineage` | ETL provenance |
| `kfm:quality` | QA tier (A/B/C) |
| `kfm:hydro_region` | Upper/Middle/Lower Kansas River |
| `kfm:project` | FloodHistory, SedimentRouting, EcologyCorridor |

---

# 🧭 4. Asset Types (Strict Domain Rules)

## ✔ COG Rasters
- Inundation maps  
- Hydrodynamic model outputs  
- Vegetation/suitability grids  

## ✔ GeoJSON
- Habitat polygons  
- Geomorphic transects  
- Ecological corridors  

## ✔ CSVW / CSV
- Hydrographs  
- WQ time-series  
- Sediment measurements  
- Biological surveys  

## ✔ NetCDF
- Climate drivers  
- Hydrodynamic simulations  

## ✔ MP4 (optional)
- Flood/drone corridor videos  
- ADCP velocity transects  

---

# 🧪 5. Example Items

## 5.1 Flood Hydrograph (1993)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "flood-1993-hydrograph",
  "collection": "kansas-river-hydrology",
  "geometry": { "type": "Point", "coordinates": [-95.67, 39.05] },
  "properties": {
    "datetime": "1993-07-15T00:00:00Z",
    "kfm:parameter": "flood_hydrograph",
    "kfm:units": "cfs",
    "kfm:provider": "USGS",
    "kfm:method": "gauge_timeseries",
    "kfm:lineage": "etl/kansas-flood-1993-v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Middle_Kansas_River",
    "kfm:project": "FloodHistory"
  },
  "assets": {
    "timeseries": {
      "href": "https://example.org/flood1993/hydrograph.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

## 5.2 Ecological Corridor Item

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kansas-river-ecology-corridor-2024",
  "collection": "kansas-river-hydrology",
  "geometry": { "type": "LineString", "coordinates": [...] },
  "properties": {
    "datetime": "2024-07-01T00:00:00Z",
    "kfm:parameter": "ecological_corridor",
    "kfm:units": "index",
    "kfm:provider": "KDWPT",
    "kfm:method": "habitat_synthesis",
    "kfm:lineage": "etl/ecology_corridor_2024",
    "kfm:quality": "A",
    "kfm:hydro_region": "Lower_Kansas_River",
    "kfm:project": "EcologyCorridor"
  },
  "assets": {
    "geojson": {
      "href": "https://example.org/kansasriver/corridors_2024.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

---

# 🧠 6. DCAT / PROV-O / CIDOC-CRM / GeoSPARQL Mapping

## DCAT 3.0
- `id` → `dct:identifier`
- `assets.href` → `dcat:downloadURL`
- `description` → `dct:description`

## PROV-O
- `prov:Entity` = dataset  
- `prov:Activity` = ETL run  
- `prov:Agent` = provider agency  

## CIDOC-CRM
- `E73 InformationObject` — dataset  
- `E7 Activity` — flood event, survey  
- `E53 Place` — river reach  
- `E3 ConditionState` — hydrologic/biologic state  

## GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin`  

---

# 🛰️ 7. ETL → STAC → Graph Workflows

```
Raw Data
  ↓ extract
Normalize + QA
  ↓ transform
Generate assets (CSVW, COG, GeoJSON)
  ↓ annotate-stac
Create STAC Item
  ↓ stac-validate
Load into Neo4j (CIDOC-CRM + GeoSPARQL)
  ↓
Expose via API + Focus Mode
```

All runs must be logged under:

```
mcp/experiments/hydrology/kansas-river/
```

---

# 🎯 8. Focus Mode v3 Integration

When a user focuses on:

### ✔ Kansas River  
Load all Items with:
- `kfm:hydro_region LIKE "Kansas%"`  

### ✔ A flood event  
Load flood hydrographs + inundation COGs + WQ/sediment data.

### ✔ Ecological topic  
Load corridors + fish + mussels + macroinvertebrates.

### ✔ Geomorphology  
Load cross-sections + sandbar migration.

---

# 📖 9. Story Node Integration

Story Nodes built on Kansas River Items:

- **“The Great Flood of 1951”**  
- **“The 1993 Midwest Flood”**  
- **“Sediment on the Move”**  
- **“Reservoir System & The Kaw”**  
- **“Ecological Corridors of the Kansas River”**

Example reference:

```json
{
  "rel": "uses-dataset",
  "target": "flood-1993-hydrograph"
}
```

---

# 🚀 10. Expansion Roadmap

Future Items:

- ADCP velocity transects (2026+)  
- Flood inundation ML rasters  
- Sediment connectivity models  
- Habitat suitability grids  
- Climate projection hydrology Items  
- UAV geomorphic monitoring  
- Multi-reservoir sediment budget Items  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Kansas River Hydrology STAC Items super-edition.

---

[⬅ Back to Kansas River STAC Collection](../README.md) • [⬅ Hydrology STAC Domain](../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

