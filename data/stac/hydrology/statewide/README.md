---
title: "🌎 Kansas Frontier Matrix — Statewide Hydrology STAC Collection (v11 Super-Edition)"
path: "data/stac/hydrology/statewide/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Hydroclimate Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-statewide-index-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Collection Index"
intent: "stac-hydrology-statewide-index"
semantic_document_id: "kfm-stac-hydrology-statewide-index"
doc_uuid: "urn:kfm:stac:hydrology:statewide:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌎 **Statewide Hydrology STAC Collection — Kansas Frontier Matrix (v11 Super-Edition)**  
`data/stac/hydrology/statewide/README.md`

**Purpose:**  
Provide the **comprehensive metadata specification** for *all statewide hydrology datasets*, including  
precipitation, temperature, runoff, drought indices, hydroclimate drivers, statewide river flows,  
groundwater interactions, soil moisture, extreme events, and multi-basin composite datasets.  
This collection unifies spatial + temporal hydrology across Kansas into the KFM v11 STAC framework.

</div>

---

# 📘 0. Overview

The **Statewide Hydrology STAC Collection** contains datasets representing:

- Kansas precipitation & temperature fields  
- Statewide runoff indices & basin water balance  
- Drought metrics (SPI, SPEI, PDSI)  
- Snowpack-driven upstream runoff (NE/CO/SD influences)  
- Statewide streamflow composites  
- Soil moisture networks  
- Hydroclimate anomalies (ENSO, AO, PDO)  
- Statewide extreme events (1951, 1993, 2019, etc.)  
- Flood-depth rasters & classified inundation maps  
- Future climate-driven hydrologic projections  
- Cross-reservoir hydrologic system datasets  

These datasets provide the **global hydrologic context** for all reservoir-specific collections (Milford →  
Tuttle Creek → Perry → Clinton) and riverine corridors (Kansas River, Big Blue, Smoky Hill).

---

# 🗂 1. Directory Layout (Canonical)

```text
data/
└── stac/
    └── hydrology/
        └── statewide/
            ├── collection.json
            └── items/
                ├── statewide-hydroclimate.json
                ├── statewide-runoff.json
                ├── statewide-drought.json
                ├── statewide-precipitation.json
                ├── statewide-temperature.json
                ├── statewide-streamflow-composite.json
                ├── statewide-extreme-events.json
                ├── statewide-flood-inundation.json
                ├── statewide-hydro-anomalies.json
                ├── statewide-soil-moisture.json
                ├── climate-futures-2030-2100.json
                └── multi-basin-hydrology.json
```

This structure mirrors all other STAC super-edition domains in KFM.

---

# 🌧️ 2. Dataset Themes (Statewide Hydrology)

## ✔ 2.1 Hydroclimate  
- Mesonet precipitation  
- NOAA NCEI temperature & precipitation normals  
- PRISM interpolated fields  
- Gridded runoff & evapotranspiration  

## ✔ 2.2 Surface Hydrology  
- USGS statewide streamflow composites  
- Baseflow separation products  
- Flash-drought signals  
- Inter-reservoir flow datasets  

## ✔ 2.3 Drought & Moisture  
- SPEI & SPI indices  
- PDSI drought classes  
- Soil moisture networks (in-situ + satellites)  

## ✔ 2.4 Flood & Extreme Events  
- Flood depth rasters  
- Inundation extents  
- Statewide hydrographs during major events (1951, 1993, 2019)  

## ✔ 2.5 Climate Futures  
- Downscaled CMIP6 hydrology fields  
- Scenario-based hydrologic anomalies (2030–2100)  

## ✔ 2.6 Statewide-Integrated Hydrology  
- Multi-basin water balance  
- Kansas River basin → Missouri River connections  
- Aggregate reservoir-system hydrology  

---

# 📐 3. Required STAC Metadata (Hydrology v11 Profile)

### Core 1.0.0 fields:

```
stac_version
type = "Feature"
id
collection = "statewide-hydrology"
geometry
bbox
properties.datetime
assets
```

### Hydrology-specific `kfm:*` fields (required)

| Field | Description |
|------|-------------|
| `kfm:parameter` | hydroclimate variable (precip, temp, runoff, drought…) |
| `kfm:units` | in, mm, C°, index units, m³/s |
| `kfm:provider` | NOAA, USGS, Mesonet, KWO, PRISM, KFM |
| `kfm:method` | interpolation, gauge, satellite, model |
| `kfm:site` | site/group identifier (if applicable) |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | QA tier |
| `kfm:hydro_region` | `Kansas_Statewide`, `Plains_Region`, etc. |
| `kfm:project` | project anchor (Hydrology-Core, Climate-Futures) |

### Recommended fields
- `kfm:climate_scenario`  
- `kfm:ensemble_member`  
- `kfm:grid_resolution`  
- `kfm:vertical_datum`  

---

# 📁 4. Asset Types & Schema Rules

## ✔ COG (Raster)
For:
- Precipitation rasters  
- Temperature rasters  
- Runoff / soil moisture grids  
- Flood inundation maps  

Must include:
- `proj:*`, overviews, internal tiling  
- `checksum:sha256`  

---

## ✔ GeoJSON
For:
- Watershed polygons  
- Statewide hydrologic zones  
- Inundation polygons  
- Event-based outlines  

---

## ✔ CSVW / CSV
For:
- Composite hydrographs  
- Drought time-series  
- Climate driver indices  
- Station-based measurements  

Required columns:  
`timestamp, parameter, value, units, site_id, qc_flag, provenance_id`

---

## ✔ NetCDF
For:
- Climate futures  
- Hydrology projections  
- Soil moisture models  
- Hydroclimate anomaly grids  

CF-compliant, with proper metadata.

---

## ✔ MP4 (optional)
For:
- Aerial/ground hydrology survey documentation  
- Flood event footage  

---

# 🧪 5. Example STAC Items

## 5.1 Statewide Hydroclimate Grid

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "statewide-hydroclimate-2000-2025",
  "collection": "statewide-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-102.05, 36.99, -94.59, 40.01],
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:parameter": "hydroclimate",
    "kfm:units": "various",
    "kfm:provider": "PRISM, Mesonet, NOAA",
    "kfm:method": "interpolation+gauges",
    "kfm:lineage": "etl/statewide_hydroclimate_v5",
    "kfm:quality": "A",
    "kfm:hydro_region": "Kansas_Statewide",
    "kfm:project": "Hydrology-Core"
  },
  "assets": {
    "netcdf": {
      "href": "https://example.org/hydroclimate_2000_2025.nc",
      "type": "application/netcdf",
      "roles": ["data"]
    }
  }
}
```

---

## 5.2 Drought Time-Series (SPI)

```json
{
  "id": "statewide-drought-spi-1980-2025",
  "type": "Feature",
  "stac_version": "1.0.0",
  "collection": "statewide-hydrology",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:parameter": "drought_spi",
    "kfm:units": "index",
    "kfm:provider": "NOAA",
    "kfm:method": "statistical_index",
    "kfm:lineage": "etl/statewide_spi_v3",
    "kfm:quality": "A",
    "kfm:hydro_region": "Kansas_Statewide",
    "kfm:project": "Hydrology-Core"
  },
  "assets": {
    "csv": {
      "href": "https://example.org/drought/spi_1980_2025.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

# 🧭 6. Ontology + Metadata Mapping

## CIDOC-CRM  
- `E73 InformationObject` → STAC Item  
- `E53 Place` → statewide extent or watershed polygon  
- `E7 Activity` → climate or hydrology event  
- `E3 ConditionState` → drought/flood/hydroclimate state  

## GeoSPARQL  
- `geo:hasGeometry`  
- `geo:sfWithin`  

## OWL-Time  
- Supports multi-decadal temporal coverage  

## PROV-O  
- Lineage fields: `prov:wasGeneratedBy`, `prov:used`, `prov:wasDerivedFrom`  

## DCAT 3.0  
- Dataset/Distribution mapping applied to all Items  

---

# 🔬 7. ETL → STAC → Graph Workflow

```
Raw statewide hydrology inputs
      ↓ extract
Normalize + QA/QC + grid alignment
      ↓ transform
Create assets (NetCDF, COG, CSVW, GeoJSON)
      ↓ stac-annotate
Generate STAC Items (*.json)
      ↓ stac-validate
Load into Neo4j (CIDOC-CRM + GeoSPARQL)
      ↓
Focus Mode v3 registration & Story Node integration
```

ETL logs stored in:

```
mcp/experiments/hydrology/statewide/
```

---

# 🎯 8. Focus Mode v3 Integration

Statewide Items drive:

- Climate anomalies panel  
- Statewide precipitation animations  
- Drought timelines  
- Statewide flood risk maps  
- Hydroclimate → reservoir behavior correlation analytics  

Focus Mode automatically filters Items by:

- `kfm:hydro_region = Kansas_Statewide`  
- Time range  
- Parameter type  

---

# 📖 9. Story Node Integration

Statewide datasets support narrative blocks:

- **“Kansas Climate Cycles (ENSO, AO, PDO)”**  
- **“The Great Droughts and Floods of Kansas”**  
- **“Hydroclimate & Reservoir Cascades”**  
- **“Extreme Events in Kansas History”**

Linked through:

```json
{
  "rel": "uses-dataset",
  "target": "statewide-drought-spi-1980-2025"
}
```

---

# 🚀 10. Expansion Roadmap

- CMIP7-based hydrology projections  
- Statewide 2D flood models (HEC-RAS)  
- ML-generated hydroclimate anomaly forecasts  
- Extreme precipitation stochastic ensembles  
- Multi-reservoir connected hydrology simulations  
- LoRa/MQTT-based statewide hydrology streaming sensors  
- Surface–groundwater exchange modeling  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial statewide hydrology STAC Collection (super-edition).

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [📂 Data Home](../../../README.md) • [🏠 KFM v11 Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

