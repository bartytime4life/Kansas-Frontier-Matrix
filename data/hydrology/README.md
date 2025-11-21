---
title: "💧 Kansas Frontier Matrix — Hydrology Data Domain Index (v11 Super-Edition)"
path: "data/hydrology/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-hydrology-index-v1.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Dataset Index"
intent: "hydrology-dataset-domain-index"
semantic_document_id: "kfm-data-hydrology-domain-index"
doc_uuid: "urn:kfm:data:hydrology:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public /Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology Data Domain Index (Super-Edition)**  
`data/hydrology/README.md`

**Purpose:**  
Serve as the authoritative **v11 hydrology domain index**, defining the dataset architecture,  
FAIR+CARE metadata, STAC integration, ETL lineage, schema rules, graph-ontology mapping,  
and Focus Mode v3 linkages for **all hydrology data** across KFM.

</div>

---

# 📘 0. Overview

The **Hydrology Domain** within the Kansas Frontier Matrix includes all datasets related to:

- Streamflow, inflows, outflows  
- Reservoir storage & operations  
- Water quality (turbidity, TSS, DO, nutrients)  
- Sediment transport  
- Hydrodynamics & bathymetry  
- Climate & hydroclimate drivers  
- Dredging & sediment export (WID 2025)  
- Downstream biological and geomorphic responses  

This README defines how hydrology datasets are structured, stored, validated, cataloged,  
and connected to the knowledge graph and Story Nodes.

---

# 🗂 1. Directory Layout (Authoritative)

```text
data/
└── hydrology/
    ├── raw/
    │   ├── inflows/
    │   ├── outflows/
    │   ├── bathymetry/
    │   ├── sediment-cores/
    │   ├── water-quality/
    │   ├── wid-2025/
    │   ├── climate/
    │   └── downstream/
    ├── processed/
    │   ├── hydrology-timeseries/
    │   ├── turbidity-do/
    │   ├── bathymetry/
    │   ├── sediment-volumes/
    │   ├── ecological-surveys/
    │   ├── wid/
    │   └── hydroclimate/
    └── stac/
        ├── hydrology/
        ├── bathymetry/
        ├── sediment/
        ├── wid-2025/
        ├── downstream/
        └── ecology/
```

**raw/** = immutable inputs  
**processed/** = harmonized, schema-validated outputs  
**stac/** = STAC-compliant catalog + items  

---

# 💧 2. Hydrology Dataset Classes (Full Taxonomy)

## **2.1 Core Hydrology (USGS / USACE / Mesonet / NOAA)**
- Streamflows (cfs)  
- Reservoir elevations (ft)  
- Gate releases (cfs)  
- Storage curves  
- Temperature, precipitation, soil moisture  
- Climate normals, anomalies  

## **2.2 Water Quality**
- Turbidity (NTU)  
- TSS (mg/L)  
- DO (mg/L)  
- Nutrients (TP, TN, NH₄, NO₃)  
- Conductivity, pH, chlorophyll  

## **2.3 Sediment & Bathymetry**
- Multibeam DEMs  
- DoD (Difference of DEM) rasters  
- Sediment core stratigraphy  
- Grain-size spectra (LISST)  
- Watershed sediment yield datasets  

## **2.4 WID (Water Injection Dredging)**
- Turbidity sensors (1–5 min)  
- DO sensors (min-level)  
- ADCP plume transects  
- Jet operations logs  
- Density-current modeling data  

## **2.5 Ecology & Downstream Effects**
- Mussel beds  
- Fish assemblage  
- Macroinvertebrate  
- Vegetation  
- Habitat polygons  

## **2.6 Climate & Hydroclimate**
- PRISM  
- NOAA NCEI  
- Mesonet  
- CMIP6 downscaled futures  

---

# 🧪 3. Dataset Schema Rules (CSV, GeoJSON, COG, NetCDF)

## **3.1 CSVW (Time Series)**
Required fields:
| column | description |
|--------|-------------|
| timestamp | ISO 8601 datetime |
| value | numeric value |
| units | SI / hydrology standard |
| parameter | e.g., flow, turbidity, DO |
| site_id | canonical KFM site ID |
| provenance | ETL / dataset lineage |

---

## **3.2 GeoJSON (Vector Data)**
Required:
- FeatureCollection  
- CRS: WGS84  
- geometry: Point / Line / Polygon  
- properties: license, provider, parameter, timestamp  

---

## **3.3 Cloud-Optimized GeoTIFF (COG)**
Used for:
- Bathymetry  
- DoD rasters  
- Sediment extent  

Requirements:
- Internal tiling  
- Overviews  
- EPSG:4326 or reservoir CRS  
- Includes metadata tags:  
  - `kfm:dataset_type`  
  - `kfm:lineage`  
  - `kfm:processing`  

---

## **3.4 NetCDF (Climate & Hydraulics)**
Requirements:
- CF-conformant  
- Dimensions: time, lat, lon  
- Variables: precipitation, temperature, hydraulic variables  
- Full metadata including provenance  

---

# 🛠 4. ETL Pipeline Architecture (Hydrology Domain)

### **Extraction**
- USGS NWIS APIs  
- KDHE WQ archives  
- USACE choke-point data  
- Mesonet API  
- NOAA climate APIs  
- Local CSV, PDF, DOC parsing  

### **Transformation**
- Harmonization to CSVW / GeoJSON / NetCDF  
- QA/QC flagging  
- Spatial reprojection  
- Time-series interpolation/resampling  
- Unit normalization  
- Data validation against schemas  

### **Loading**
- Processed datasets written into data/hydrology/processed/  
- STAC Items generated and placed into data/hydrology/stac/**  
- Graph ingestion (Neo4j) using ETL lineage  

---

# 🛰 5. STAC Collections (Hydrology Domain)

```text
data/hydrology/stac/
├── hydrology/
│   ├── collection.json
│   └── items/
├── bathymetry/
├── wid-2025/
├── sediment/
├── ecology/
└── downstream/
```

Each **collection.json** includes:
- id, title, description  
- spatial + temporal extents  
- license  
- providers  
- DCAT & STAC compatibility  
- PROV-O lineage  
- Keywords (sediment, hydrology, climate, ecology, etc.)

---

# 🛰️ 6. STAC Item Template (Hydrology)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "usgs-big-blue-inflow-2020-2025",
  "collection": "tuttle-creek-hydrology",
  "geometry": { "type": "Point", "coordinates": [-96.6005, 39.2758] },
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:parameter": "inflow",
    "kfm:units": "cfs",
    "providers": [
      { "name": "USGS NWIS", "roles": ["producer"] },
      { "name": "Kansas Water Office", "roles": ["processor"] }
    ]
  },
  "assets": {
    "timeseries": {
      "href": "https://example.org/data/inflow_2020_2025.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

# 🕸 7. Knowledge Graph Ontology (CIDOC-CRM + GeoSPARQL + OWL-Time)

### **Entities**
- `E53 Place:Big_Blue_River`  
- `E53 Place:Tuttle_Creek_Reservoir`  
- `E5 Event:WID_2025`  
- `E73 InformationObject:HydrologyDataset`  
- `ObservationSeries:Hydro_Data_<Parameter>`  
- `E3 ConditionState:Hydro_Condition_<Year>`

### **Relations**
- `geo:hasGeometry` → Place geometry  
- `time:hasTime` → dataset date/time  
- `prov:wasGeneratedBy` → ETL pipeline  
- `P70_documents` → source provenance  
- `P7_took_place_at` → spatial grounding  

---

# 🧬 8. FAIR+CARE Metadata Requirements

### Every dataset MUST include:
- License  
- Spatial footprint  
- Temporal coverage  
- Provenance (PROV-O)  
- Processing lineage  
- Creator/Provider roles  
- Calibration metadata  
- QA/QC flags  
- DCAT 3.0 dataset fields  
- Ethical checks (CARE)  

---

# 🎯 9. Focus Mode v3 Integration

Focus Mode links datasets to:

- Places (reservoir, dam, channels)  
- Events (WID 2025, floods, droughts)  
- Observations (timeseries)  
- Bathymetry and sediment layers  
- Climate/hydroclimate drivers  

Focus Mode surfaces:
- Plots  
- Maps  
- STAC assets  
- Narrative summaries  
- Dataset provenance  

---

# 📖 10. Story Node Integration

Story Nodes using hydrology datasets:

- **“A Reservoir Filling From the Bottom Up”**  
  - bathymetry, sediment cores, inflows  

- **“Downstream of the Dam”**  
  - turbidity, DO, fish & mussel surveys  

- **“The 2025 WID Demonstration”**  
  - turbidity sensors, ADCP, nutrient datasets  

Story Nodes reference dataset IDs using  
`relations[].rel = "uses-dataset"`.

---

# 🚀 11. Expansion Roadmap

Future dataset additions:

- 2D/3D hydrodynamic models  
- Climate-sediment interaction models  
- Reservoir bathymetry + sediment lidar (future USACE)  
- Watershed erosion source fingerprinting  
- Multisensor turbidity fusion (Sentinel-2 + USGS)  
- Real-time streaming sensors (MQTT → STAC)  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial super-edition creation of hydrology domain dataset index.

---

[🏠 Back to KFM v11 Master Guide](../../docs/reference/kfm_v11_master_documentation.md) • [📂 Data Home](../README.md)

