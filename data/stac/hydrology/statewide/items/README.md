---
title: "🌎 Kansas Frontier Matrix — Statewide Hydrology STAC Items Index (v11 Super-Edition)"
path: "data/stac/hydrology/statewide/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Hydroclimate Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/data-stac-hydro-statewide-items-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-statewide-items-index"
semantic_document_id: "kfm-stac-hydrology-statewide-items"
doc_uuid: "urn:kfm:stac:hydrology:statewide:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌎 **Statewide Hydrology — STAC Items Index (v11 Super-Edition)**  
`data/stac/hydrology/statewide/items/README.md`

**Purpose:**  
Provide the **complete Items-level governance** for all statewide hydrology STAC Items used by  
the Kansas Frontier Matrix (KFM). This includes climate, precipitation, temperature, drought,  
runoff, soil moisture, flood extents, hydroclimate anomalies, statewide streamflow composites,  
and CMIP6/CMIP7 hydrologic futures.  
Defines metadata, asset schemas, ontology mapping, ETL lineage, and Focus Mode v3 linkage.

</div>

---

# 📘 0. Overview

This directory contains **all STAC Items** representing statewide hydrologic datasets across Kansas.  
These Items describe:

- Gridded hydroclimate measurements  
- Statewide precipitation and temperature rasters  
- Soil moisture and drought records  
- Streamflow compositing datasets  
- Flood inundation rasters and polygons  
- Hydroclimate anomaly indicators  
- Climate futures (2030–2100)  
- Cross-basin hydrologic composites  
- Multi-decadal water-balance datasets  

Each Item here acts as a **machine-readable metadata node** bridging space, time, hydrologic  
parameters, hydroclimate drivers, and model outputs. These Items are used across:

```
STAC → Neo4j Graph (CIDOC + GeoSPARQL + OWL-Time)
     → KFM API (GraphQL/REST)
     → Timeline Engine
     → MapLibre/DeckGL Visualization
     → Focus Mode v3
     → Story Node v3
```

---

# 🗂️ 1. Directory Structure

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

Every file inside `items/` is a **STAC Item** with strict hydrology-statewide metadata.

---

# 🌍 2. Statewide STAC Item Taxonomy

## ✔ 2.1 Hydroclimate Grids  
- PRISM / Mesonet precipitation  
- NOAA/NCEI temperature rasters  
- Evapotranspiration & water-balance grids  

## ✔ 2.2 Runoff & Streamflow  
- Statewide runoff indices  
- Multi-basin streamflow composites  
- Snowmelt-driven inflow aggregates  

## ✔ 2.3 Drought  
- SPI, SPEI indices  
- PDSI classifications  
- Soil moisture anomaly time-series  

## ✔ 2.4 Extreme Events  
- Multi-year statewide hydrographs during major floods  
- Flood inundation rasters  
- Event polygons (1993, 2019, 1951)  

## ✔ 2.5 Climate Futures (2030–2100)  
- Downscaled CMIP6 hydrologic projections  
- Ensemble futures (SSP1–2.6, SSP2–4.5, SSP5–8.5)  
- Precip/Temp/Runoff future anomaly rasters  

## ✔ 2.6 Hydroclimate Anomalies  
- ENSO, AO, PDO teleconnection indices  
- Hydrologic regime classifications  

## ✔ 2.7 Soil Moisture  
- In-situ Mesonet observations  
- GRACE satellite water storage anomalies  
- SMAP soil moisture grids  

---

# 📐 3. Required Metadata Structure (Statewide Hydrology Profile)

## ✔ Core STAC 1.0.0
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

## ✔ Hydrology `kfm:*` Extensions (MANDATORY)

| Field | Meaning |
|------|---------|
| `kfm:parameter` | e.g., precip, temp, drought_spi, runoff, anomaly |
| `kfm:units` | mm, in, C°, index units, m³/s equivalents |
| `kfm:provider` | NOAA, USGS, Mesonet, PRISM, KWO |
| `kfm:method` | gauge, interpolation, satellite, model |
| `kfm:site` | region/station/grid code |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | A/B/C/provisional |
| `kfm:hydro_region` | `Kansas_Statewide` |
| `kfm:project` | Hydrology-Core, Climate-Futures |

### Recommended  
- `kfm:ensemble_member`  
- `kfm:scenario` (SSP1, SSP2, SSP5…)  
- `kfm:grid_resolution` (e.g., 4km PRISM, 1/8° NLDAS)  
- `kfm:temporal_resolution`  

---

# 🗃️ 4. Asset Schema Requirements

## ✔ COG Rasters  
Used for:
- precipitation grids  
- temperature grids  
- runoff rasters  
- flood inundation maps  
- climate future rasters  

Required:
- `proj:*` fields  
- internal tiling + overviews  
- checksum hashes  

---

## ✔ GeoJSON  
Used for:
- statewide zones  
- flood polygons  
- watershed masks  
- event outlines  

---

## ✔ CSVW / CSV  
Used for:
- drought time-series  
- statewide composite hydrographs  
- anomaly indices  
- station climatology  

Minimum columns:  
`timestamp, parameter, value, units, site_id, qc_flag, provenance_id`

---

## ✔ NetCDF  
Used for:
- climate futures  
- large gridded datasets  
- hydrology simulations  

CF-compliant with dimensions: `time`, `lat`, `lon`.

---

## ✔ MP4  
Optional video assets for statewide flood documentation.

---

# 🧪 5. Example STAC Items

## 5.1 Statewide Precipitation Raster (PRISM)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "statewide-precipitation-2024",
  "collection": "statewide-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-102.05, 36.99, -94.59, 40.01],
  "properties": {
    "datetime": "2024-12-31T00:00:00Z",
    "kfm:parameter": "precipitation",
    "kfm:units": "mm",
    "kfm:provider": "PRISM",
    "kfm:method": "interpolation",
    "kfm:lineage": "etl/prism_precip2024_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Kansas_Statewide",
    "kfm:project": "Hydrology-Core"
  },
  "assets": {
    "cog": {
      "href": "https://example.org/statewide/precip_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

---

## 5.2 Drought Index (SPI)

```json
{
  "stac_version":"1.0.0",
  "type":"Feature",
  "id":"statewide-drought-spi-1980-2025",
  "collection":"statewide-hydrology",
  "properties":{
    "datetime":"2025-01-01T00:00:00Z",
    "kfm:parameter":"drought_spi",
    "kfm:units":"index",
    "kfm:provider":"NOAA",
    "kfm:method":"index_calculation",
    "kfm:lineage":"etl/statewide_spi_v4",
    "kfm:quality":"A",
    "kfm:hydro_region":"Kansas_Statewide",
    "kfm:project":"Hydrology-Core"
  },
  "geometry":null,
  "bbox":null,
  "assets":{
    "csv":{
      "href":"https://example.org/drought/spi_1980_2025.csv",
      "type":"text/csv",
      "roles":["data"]
    }
  }
}
```

---

# 🧠 6. Ontology Mapping (CIDOC-CRM • GeoSPARQL • OWL-Time • PROV-O • DCAT 3.0)

## CIDOC-CRM
- `E73 InformationObject` → dataset  
- `E53 Place` → statewide polygon or null  
- `E7 Activity` → drought/flood/hydroclimate events  
- `E3 ConditionState` → statewide hydrologic state  

## GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin` (when using watershed polygons)

## OWL-Time
Supports:
- multi-decadal intervals  
- temporal reasoning across climate cycles  

## PROV-O
- ETL lineage via:  
  - `prov:wasGeneratedBy`  
  - `prov:used`  
  - `prov:wasAttributedTo`  
  - `prov:wasDerivedFrom`  

## DCAT 3.0
All Items map cleanly to DCAT Dataset/Distribution objects.

---

# 🔬 7. ETL → STAC → Graph Workflow

```
Raw Inputs (NOAA, Mesonet, PRISM, USGS, CMIP)
      ↓ extract
QA/QC + harmonization
      ↓ transform
Asset creation (COG, NetCDF, CSVW, GeoJSON)
      ↓ annotate
STAC Item generation
      ↓ stac-validate
Graph ingestion (CIDOC + GeoSPARQL)
      ↓
Focus Mode v3 + Story Node v3 registration
```

All ETL lineage is stored under:

```
mcp/experiments/hydrology/statewide/
```

---

# 🎯 8. Focus Mode v3 Integration

Statewide Items power:

- Climate maps & anomaly panels  
- Statewide precipitation/temperature animations  
- Drought visualizations  
- Flood-depth rasters  
- Climate change scenarios  
- Hydrology-climate connections for Story Nodes  

---

# 📖 9. Story Node Integration

Story Nodes using statewide Items:

- **“Kansas Climate Cycles (ENSO → Flood → Drought)”**  
- **“Hydroclimate of the Great Plains”**  
- **“The Great Floods of Kansas”**  
- **“Future Hydrology Under Climate Change”**

Example linkage:

```json
{
  "rel": "uses-dataset",
  "target": "statewide-hydroclimate-2000-2025"
}
```

---

# 🚀 10. Expansion Roadmap

Future statewide hydrology Items:

- CMIP7 hydroclimate projections  
- Statewide 2D flood models  
- Snowpack-to-Kansas hydrology connectivity  
- Climate anomaly ensemble datasets  
- Machine-learning hydrology forecasts  
- Soil moisture–runoff coupling datasets  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial statewide hydrology STAC Items Super-Edition.

---

[⬅ Back to Statewide Hydrology Collection](../README.md) • [⬅ Hydrology STAC Domain](../../README.md) • [🏠 KFM v11 Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

