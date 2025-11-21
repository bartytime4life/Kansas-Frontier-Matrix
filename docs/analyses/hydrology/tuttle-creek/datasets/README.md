---
title: "🗂️ Kansas Frontier Matrix — Tuttle Creek Hydrology Dataset Index (v11 Super-Edition)"
path: "docs/analyses/hydrology/tuttle-creek/datasets/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/docs-analyses-hydrology-tc-datasets-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Dataset Index"
intent: "hydrology-tuttle-creek-datasets"
semantic_document_id: "kfm-analyses-hydrology-tuttle-creek-datasets-index"
doc_uuid: "urn:kfm:docs:analyses:hydrology:tuttle-creek:datasets:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🗂️ **Tuttle Creek Hydrology Dataset Index — Comprehensive v11 Super-Edition**  
`docs/analyses/hydrology/tuttle-creek/datasets/README.md`

**Purpose:**  
Serve as the **canonical, authoritative dataset catalog** for all hydrologic, sediment, bathymetric,  
ecological, and WID-related datasets used in Tuttle Creek analyses. Provides STAC metadata, ETL  
guidance, ontology mapping, schema expectations, dataset QA/QC requirements, and Focus Mode  
integration for KFM v11.

</div>

---

# 📘 0. Executive Summary

This dataset index unifies all **Tuttle Creek hydrology datasets** across raw, processed, and STAC layers,  
forming the complete data backbone for:

- Sedimentation History (1962–2025)  
- Downstream Effects Analysis  
- Water Injection Dredging (WID) 2025  
- Monitoring & QA/QC networks  
- Flood operations  
- Ecological response assessments  
- Bathymetric reconstruction  
- Climate/hydroclimate patterns  
- Story Node v3 generation  
- Focus Mode v3 entity linking  

This document ensures **dataset consistency, discoverability, and traceability**, aligned with FAIR+CARE,  
STAC 1.x, DCAT 3.0, CIDOC-CRM, OWL-Time, GeoSPARQL, and MCP-DL v6.3.

---

# 🗂 1. Directory Layout — Complete Hierarchical Structure

```text
data/
└── hydrology/
    └── tuttle-creek/
        ├── raw/
        │   ├── bathymetry/
        │   ├── inflows/
        │   ├── outflows/
        │   ├── sediment-cores/
        │   ├── wid-2025/
        │   └── water-quality/
        ├── processed/
        │   ├── bathymetry/
        │   ├── hydrology-timeseries/
        │   ├── turbidity-do/
        │   ├── sediment-volumes/
        │   ├── ecological-surveys/
        │   └── wid/
        └── stac/
            ├── bathymetry/
            ├── hydrology/
            ├── wid-2025/
            ├── sediment/
            ├── ecology/
            └── downstream/
```

Each folder contains:

- **raw/** → Original datasets (immutable)  
- **processed/** → Cleaned, harmonized, schema-compliant datasets  
- **stac/** → STAC Items & Collection JSON  

---

# 🌊 2. Dataset Categories (Full Taxonomy)

### ✔ Hydrology (Core)
- USGS NWIS inflows  
- Dam releases  
- Gate operations  
- Stage hydrographs (AHPS)

### ✔ Sediment & Turbidity
- TSS  
- Turbidity  
- Particle-size spectra  
- Sediment core stratigraphy  
- Suspended sediment volumes  

### ✔ Bathymetry (1962–2025)
- Multibeam surveys  
- Single-beam historical transects  
- Digitized contour maps  
- Differencing-of-DEM (DoD) rasters  

### ✔ WID (2025 Demonstration)
- Turbidity time-series  
- Nutrients  
- DO  
- ADCP density-current transects  
- WID barge instrumentation logs  

### ✔ Ecology & Biology
- Mussel surveys  
- Fish community assessments  
- Macroinvertebrate surveys  
- Riparian vegetation surveys  

### ✔ Climate & Hydroclimate
- Mesonet  
- PRISM interpolations  
- NOAA climate normals  
- Event-based precipitation grids  

### ✔ Geomorphology
- Bank erosion pins  
- Substrate classifications  
- Channel cross-sections  
- Floodplain sediment traps  

---

# 🧪 3. Dataset Schemas (CSV, GeoJSON, COG, NetCDF)

## 📄 CSVW Tabular Schema

### Required columns for time-series datasets:
| Column | Description |
|--------|-------------|
| `timestamp` | ISO 8601 date-time |
| `value` | Observed variable value |
| `parameter` | e.g., turbidity, DO, flow |
| `units` | SI/hydrology units |
| `site_id` | KFM canonical site identifier |
| `provenance` | Source document or ETL ID |

---

## 🌍 GeoJSON Schema (Vector Data)
- `type`: FeatureCollection  
- `features[].geometry`: Point / LineString / Polygon  
- `features[].properties`:  
  - `parameter`  
  - `survey_date`  
  - `provider`  
  - `units`  
  - `license`  

---

## 🗺️ COG Raster Schema (Bathymetry / DEMs)
- Tiled internally  
- Overviews enabled  
- CRS: EPSG:4326 or USACE CRS per metadata  
- Tags:  
  - `kfm:dataset_type=dem`  
  - `kfm:processing`  
  - `kfm:lineage`  

---

## 📦 NetCDF Schema (Climate / Hydrology)
- Dimensions: time, lat, lon  
- Variables: precipitation, temperature, discharge  
- CF-compliant metadata  

---

# 🛰️ 4. STAC Integration (Full Specification)

## 📚 STAC Collection Layout
```text
data/stac/hydrology/tuttle-creek/
├── collection.json
└── items/
    ├── bathymetry-1962.json
    ├── bathymetry-1993.json
    ├── hydrology-inflows-usgs.json
    ├── wid-turbidity-b1.json
    ├── wid-density-current.json
    ├── sediment-core-locations.json
    ├── ecological-mussel-2025.json
    └── downstream-do.json
```

---

## 🛰️ STAC Template Example

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tuttle-creek-bathymetry-2019",
  "collection": "tuttle-creek-bathymetry",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [...],
  "properties": {
    "datetime": "2019-09-30T00:00:00Z",
    "kfm:parameter": "bathymetry",
    "kfm:units": "m",
    "kfm:project": "sedimentation-history",
    "providers": [
      { "name": "USACE Kansas City District", "roles": ["producer", "host"] }
    ]
  },
  "assets": {
    "cog": {
      "href": "https://example.org/data/tc/bathy_2019.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"]
    }
  }
}
```

---

# 🕸️ 5. Graph Model (CIDOC-CRM + GeoSPARQL + OWL-Time)

### Core Dataset Entities
- `E73 InformationObject:Bathymetry_2019`
- `E73 InformationObject:USGS_Inflow_Timeseries`
- `ObservationSeries:WID_Turbidity_B1`
- `E53 Place:Tuttle_Creek_Reservoir`
- `E53 Place:Big_Blue_River_Reaches`
- `E7 Activity:Sedimentation_Event_<Year>`

### Key Relationships
- `geo:hasGeometry` → reservoir / river polygons  
- `time:hasTime` → dataset temporal extent  
- `prov:wasGeneratedBy` → ETL pipeline  
- `P70_documents` → dataset provenance  
- `P7_took_place_at` → spatial entity  

---

# 🔬 6. ETL Pipelines (Extraction → Transform → Load)

### Extraction Sources
- USGS NWIS API  
- KDHE WQ archives  
- USACE bathymetry downloads  
- Mesonet API  
- NOAA NCEI climate datasets  

### Transform Steps
- Reprojection  
- Resampling  
- QA/QC flagging  
- Schema normalization (CSVW / GeoJSON / COG)  
- Adding STAC metadata  

### Load Targets
- STAC catalog  
- Neo4j knowledge graph  
- Processed datasets directory  

---

# 🧬 7. Focus Mode v3 Dataset Hooks

Each dataset supports:

- **Entity-level focus** (Place, Event, Dataset)  
- **Time-series visualizations** (charts, sensors, anomalies)  
- **Story Node enrichment**  
- **Cross-linking** to hydrology & sedimentation narratives  

Example:

- Focusing on `Place:Tuttle_Creek_Dam` loads:  
  - Tailwater DO + turbidity  
  - WID turbidity pulses  
  - Downstream geomorphology layers  

---

# 📖 8. Story Node Dataset Integration

Story Nodes referencing datasets:

- **“A Reservoir Filling From the Bottom Up”**  
  - bathymetry + sediment cores + inflow history  

- **“Downstream of the Dam”**  
  - DO + turbidity + biological surveys  

- **“The 2025 Water Injection Experiment”**  
  - WID turbidity + ADCP + nutrients + timelines  

Each Story Node references dataset IDs via:

- `relations[].rel = "uses-dataset"`  
- `relations[].target = "<dataset-id>"`

---

# 🛠️ 9. QA/QC Requirements (FAIR+CARE)

### Every dataset must include:
- License  
- Provenance chain  
- QA flags  
- Calibration references  
- Sensor metadata  
- Lineage (ETL steps)  
- Accessibility compliance  
- DCAT 3.0 fields  

---

# 📈 10. Dataset Expansion Roadmap

Recommended future additions:

- 2D/3D hydrodynamic models (HEC-RAS / Delft3D)  
- Watershed sediment source apportionment  
- Long-term reservoir stratigraphy  
- Climate-driven sediment yield projections  
- Mussel bed geospatial atlas  
- ADCP plume videos (stored as STAC assets)  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of full super-index dataset catalog.

---

[⬅️ Back to Tuttle Creek Index](../README.md) • [🏠 KFM v11 Master Guide](../../../../../reference/kfm_v11_master_documentation.md) • [📂 Data Index](../../../../../data/README.md)

