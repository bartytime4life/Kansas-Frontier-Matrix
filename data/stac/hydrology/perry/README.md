---
title: "🌊 Kansas Frontier Matrix — Perry Lake Hydrology STAC Collection (v11 Super-Edition)"
path: "data/stac/hydrology/perry/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Reservoir Systems Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-perry-index-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Collection Index"
intent: "stac-hydrology-perry-index"
semantic_document_id: "kfm-stac-hydrology-perry-index"
doc_uuid: "urn:kfm:stac:hydrology:perry:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌊 **Perry Lake Hydrology — STAC Collection (v11 Super-Edition)**  
`data/stac/hydrology/perry/README.md`

**Purpose:**  
Provide the **complete STAC metadata specification** for **Perry Lake** hydrology, sedimentation,  
bathymetry, water-quality, ecology, downstream impacts, flood behavior, and hydroclimate datasets  
as integrated into the **Kansas Frontier Matrix (KFM) v11**.  
Defines Item-level metadata, asset schemas, ETL → STAC → Graph workflows, ontology mappings,  
and Focus Mode/Story Node integration.

</div>

---

# 📘 0. Reservoir Overview

**Perry Lake**, completed in **1970**, is a major federal reservoir in the Delaware River basin and part of the  
core Kansas reservoir chain:

```
Milford → Tuttle Creek → Perry → Clinton → Kansas River → Missouri River
```

Perry Lake plays central roles in:

- Flood moderation for Topeka & Lawrence  
- Multi-reservoir hydrologic operations  
- Sediment trapping and water-quality modulation  
- Downstream ecological corridors  
- Drought resiliency & augmentation  
- Regional recreation and aquatic biodiversity  

This STAC Collection catalogs *all spatiotemporal datasets for Perry Lake*.

---

# 🗂️ 1. Directory Layout

```text
data/
└── stac/
    └── hydrology/
        └── perry/
            ├── collection.json
            └── items/
                ├── bathymetry-1970.json
                ├── bathymetry-1990.json
                ├── bathymetry-2012.json
                ├── bathymetry-2024.json
                ├── dod-1970-1990.json
                ├── dod-1990-2012.json
                ├── dod-2012-2024.json
                ├── hydrology-inflows.json
                ├── hydrology-outflows.json
                ├── wq-turbidity.json
                ├── wq-do.json
                ├── wq-nutrients.json
                ├── sediment-cores.json
                ├── sediment-volumes.json
                ├── delta-migration.json
                ├── downstream-do.json
                ├── downstream-turbidity.json
                ├── ecology-fish.json
                ├── ecology-mussels.json
                ├── macroinv-surveys.json
                ├── riparian-zones.json
                ├── hydroclimate.json
                └── flood-history.json
```

This is identical in structure to Milford, Tuttle Creek, Clinton, and Kansas River STAC domains  
for maximum cross-reservoir consistency.

---

# 🌍 2. Spatial + Temporal Extents

### Spatial Bounding Box (approximate Perry Lake polygon)
```
[-95.51, 39.16, -95.27, 39.32]
```

### Temporal Coverage
```
1970-01-01T00:00:00Z → present
```

---

# 🌊 3. Perry Lake Dataset Themes

## ✔ 3.1 Bathymetry (DEM & DoD)
- 1970 post-closure baseline  
- 1990 mid-life survey  
- 2012 USACE multibeam  
- 2024 updated DEM  
- DoD rasters: deposition & erosion mapping  

Bathymetry supports:
- Sedimentation history  
- Delta & forebay evolution  
- Reservoir capacity assessments  
- Hydraulic modeling  

---

## ✔ 3.2 Hydrology (USGS + USACE)
- Inflows from **Delaware River**, tributaries, watershed channels  
- Outflows to the Kansas River  
- Stage–storage relationships  
- Gate operations & release hydrographs  

---

## ✔ 3.3 Water Quality (KDHE, USACE)
- Turbidity  
- DO profiles  
- Nutrients (TN/TP/NO₃/NH₄)  
- Conductivity/pH  
- Seasonal stratification  

---

## ✔ 3.4 Sediment
- Sediment cores  
- Stratigraphic profiles  
- Sediment volume curves  
- Delta advancement over time  

---

## ✔ 3.5 Downstream Effects
- Tailwater DO & turbidity  
- Sediment pulses to the Kansas River  
- Nutrient transport mapping  

---

## ✔ 3.6 Ecology
- Fish assemblage surveys  
- Mussel bed polygons  
- Macroinvertebrate indices  
- Riparian vegetation mapping  
- Habitat quality zones (riffle/pool/backwater)  

---

## ✔ 3.7 Flood & Hydroclimate
- Flood hydrographs (e.g., 1993, 2019)  
- Inundation rasters  
- PRISM & Mesonet precipitation  
- SPI/PDSI drought cycles  

---

# 📐 4. Required STAC Metadata (Hydrology v11 Profile)

Every Perry Lake STAC Item must include both **STAC 1.0.0** core fields and the complete  
**KFM Hydrology Extensions**.

### Core STAC fields
```
stac_version
type = "Feature"
id
collection = "perry-lake-hydrology"
geometry
bbox
properties.datetime
assets
```

### Hydrology `kfm:*` Fields (Mandatory)
| Field | Purpose |
|-------|----------|
| `kfm:parameter` | bathymetry, inflow, turbidity, DO, sediment, etc. |
| `kfm:units` | SI or domain units |
| `kfm:provider` | USACE, USGS, KDHE, KDWPT, etc. |
| `kfm:method` | multibeam, gauge, lab, drone, etc. |
| `kfm:site` | station ID, transect ID, polygon ID |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | QA tier |
| `kfm:hydro_region` | `Perry_Reservoir`, `Perry_Tailwater`, etc. |
| `kfm:project` | e.g., Sedimentation-History, Hydrology-Core |

### Recommended
- `kfm:dominant_species` (ecology)  
- `kfm:habitat_type`  
- `kfm:processing_history`  
- `kfm:crs`, `kfm:vertical_datum`

---

# 🧭 5. Asset Schema Rules (COG • CSVW • GeoJSON • NetCDF • MP4)

### ✔ Raster (COG)
Used for:
- Bathymetry  
- DoD  
- Inundation rasters  

Requirements:
- `image/tiff; application=geotiff; profile=cloud-optimized`  
- `roles = ["data"]`  
- Must include `proj:*` fields & checksums  

---

### ✔ GeoJSON
Used for:
- Delta outlines  
- Habitat polygons  
- Ecological survey sites  
- Channel migration zones  

---

### ✔ CSV / CSVW
Used for:
- Inflow/outflow hydrographs  
- Time-series WQ  
- Sediment lab results  
- Biological survey data  

Columns must include:
`timestamp, parameter, value, units, site_id, qc_flag, provenance_id`

---

### ✔ NetCDF
Used for:
- Climate grids  
- Hydrodynamic model outputs  

---

### ✔ MP4
Used for:
- Drone shoreline surveys  
- Submerged habitat monitoring  

---

# 🧪 6. Example Perry Lake STAC Items

## 6.1 Bathymetry DEM — 2024

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "perry-bathymetry-2024",
  "collection": "perry-lake-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-95.51, 39.16, -95.27, 39.32],
  "properties": {
    "datetime": "2024-08-01T00:00:00Z",
    "kfm:parameter": "bathymetry",
    "kfm:units": "meters",
    "kfm:provider": "USACE Kansas City District",
    "kfm:method": "multibeam",
    "kfm:lineage": "etl/perry_bathy2024_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Perry_Reservoir",
    "kfm:project": "Sedimentation-History"
  },
  "assets": {
    "dem": {
      "href": "https://example.org/perry/bathy_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

## 6.2 Inflow Time-Series — Delaware River

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "perry-inflow-delaware-2020-2025",
  "collection": "perry-lake-hydrology",
  "geometry": { "type": "Point", "coordinates": [-95.43, 39.24] },
  "bbox": [-95.44, 39.23, -95.42, 39.25],
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:parameter": "inflow",
    "kfm:units": "cfs",
    "kfm:provider": "USGS NWIS",
    "kfm:method": "stream_gauge",
    "kfm:lineage": "etl/perry_inflow2025_v2",
    "kfm:quality": "A",
    "kfm:hydro_region": "Perry_Reservoir",
    "kfm:project": "Hydrology-Core"
  },
  "assets": {
    "timeseries": {
      "href": "https://example.org/perry/inflows_2020_2025.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

## 6.3 Mussel Survey — Tailwater

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "perry-mussels-tailwater-2024",
  "collection": "perry-lake-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-95.30, 39.18, -95.29, 39.19],
  "properties": {
    "datetime": "2024-07-10T00:00:00Z",
    "kfm:parameter": "mussels",
    "kfm:units": "individuals_per_m2",
    "kfm:provider": "KDWPT",
    "kfm:method": "quadrat",
    "kfm:lineage": "etl/ecology_perry2024_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Perry_Tailwater",
    "kfm:project": "Ecology-Monitoring"
  },
  "assets": {
    "geojson": {
      "href": "https://example.org/perry/mussels_2024.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

---

# 🧠 7. Ontology Mapping (CIDOC-CRM + GeoSPARQL + OWL-Time)

## CIDOC-CRM  
- `E73 InformationObject` — STAC Item  
- `E53 Place` — reservoir polygon, tailwater, survey site  
- `E7 Activity` — survey, bathy scan, flood event  
- `E3 ConditionState` — sedimentation state, ecological condition  
- `E39 Actor` — USACE, USGS, KDHE, KDWPT, KWO  

## GeoSPARQL  
- `geo:hasGeometry`  
- `geo:sfWithin`  
- `geo:asWKT`  

## OWL-Time  
- `time:hasTime`  
- `time:hasBeginning`  
- `time:hasEnd`  

---

# 🔬 8. DCAT 3.0 & PROV-O Crosswalk

## DCAT
| STAC | DCAT |
|------|------|
| id | dct:identifier |
| assets.href | dcat:downloadURL |
| description | dct:description |
| bbox | dct:spatial |
| properties.datetime | dct:temporal |

## PROV-O
Each item is:

- `prov:Entity`  
- Generated via `prov:Activity` (ETL or field survey)  
- Attributed to `prov:Agent` (provider)  

Links include:
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasDerivedFrom`

---

# 🛰 9. ETL → STAC → Graph Workflow

```
Raw Data Acquisition
    ↓ extract
QA & Unit Harmonization
    ↓ transform
Generate Assets (COG, CSVW, GeoJSON)
    ↓ annotate
Create STAC Items
    ↓ stac-validate
Graph ingestion (Neo4j: CIDOC + GeoSPARQL + OWL-Time)
    ↓
Focus Mode v3 + Story Node v3 updates
```

ETL processes must be recorded in:

```
mcp/experiments/hydrology/perry/
```

---

# 🎯 10. Focus Mode v3 Integration

Focus Mode automatically loads:

- Bathymetry (1970→2024)  
- Sedimentation/DoD  
- Inflow/outflow hydrographs  
- WQ (TSS, DO, nutrients)  
- Downstream DO/turbidity  
- Ecological conditions  

Filter rules:

- `place = Perry_Reservoir`  
- `hydro_region = Perry_*`  
- `parameter IN (bathymetry, inflow, turbidity, DO, sediment, ecology)`  

---

# 📖 11. Story Node v3 Integration

Perry Lake supports Story Nodes such as:

- **“Perry Lake: A Middle-Chain Reservoir”**  
- **“Flood Control Across the Reservoir Cascade”**  
- **“Sediment Pathways: Delaware River → Perry → Kansas River”**  
- **“Ecology of the Delaware–Kansas River Corridor”**

Story Nodes reference items via:

```json
{
  "rel": "uses-dataset",
  "target": "perry-bathymetry-2024"
}
```

---

# 🚀 12. Expansion Roadmap

Future Perry STAC Items:

- UAV-derived bathymetry 2026+  
- Annual fish & macroinvertebrate monitoring Items  
- 3D hydrodynamic model outputs (HEC-RAS/Delft3D)  
- Sediment fingerprinting & source-apportionment datasets  
- Climate-influenced hydrology projections (CMIP6)  
- Habitat quality rasters  

All must comply with the **Hydrology STAC Profile v11**.

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Perry Lake Hydrology STAC Collection (Super-Edition).

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [📂 Data Home](../../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

