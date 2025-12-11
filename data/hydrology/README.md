---
title: "💧 Kansas Frontier Matrix — Hydrology Data Domain Index (v11 Super-Edition)"
path: "data/hydrology/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Hydrology & Hazards Council"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-data-hydrology-domain-index"
doc_uuid: "urn:kfm:data:hydrology:index:v11.0.0"
event_source_id: "ledger:data/hydrology/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-hydrology-index-v1.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active · Enforced"
doc_kind: "Dataset Index"
intent: "hydrology-dataset-domain-index"
role: "archive-registry"
category: "Data · Hydrology · Domain Index"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity_level: "Mixed"
public_exposure_risk: "Dataset-level"
indigenous_rights_flag: "Dataset-level"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Varies by dataset"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next hydrology-domain update"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology Data Domain Index (Super-Edition)**  
`data/hydrology/README.md`

**Purpose**  
Serve as the authoritative **v11 hydrology domain index**, defining dataset architecture,  
FAIR+CARE metadata, STAC integration, ETL lineage, schema rules, graph-ontology mapping,  
and Focus Mode v3 linkages for **all hydrology data** in KFM.

</div>

---

## 📘 1. Overview

The **Hydrology Domain** within KFM includes all datasets related to:

- Streamflow (inflows, outflows, baseflows)  
- Reservoir storage & operations  
- Water quality (turbidity, TSS, DO, nutrients)  
- Sediment transport & deposition  
- Hydrodynamics & bathymetry  
- Climate & hydroclimate drivers  
- Dredging & sediment export (e.g., WID 2025)  
- Downstream ecological and geomorphic responses  

This README defines how hydrology datasets are structured, stored, validated, cataloged,  
and connected to the knowledge graph, Story Nodes, and Focus Mode v3, following the  
KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

---

## 🗂 2. Directory Layout (Authoritative · Emoji Style A)

~~~text
data/hydrology/
├── 📄 README.md
│
├── 📂 raw/
│   ├── 💧 inflows/
│   ├── 💧 outflows/
│   ├── 🗺️ bathymetry/
│   ├── 🧪 sediment-cores/
│   ├── 🧪 water-quality/
│   ├── 🚜 wid-2025/
│   ├── 🌦️ climate/
│   └── 🌊 downstream/
│
├── 📂 processed/
│   ├── 📈 hydrology-timeseries/
│   ├── 🧪 turbidity-do/
│   ├── 🗺️ bathymetry/
│   ├── 📦 sediment-volumes/
│   ├── 🪶 ecological-surveys/
│   ├── 🚜 wid/
│   └── 🌦️ hydroclimate/
│
└── 📂 stac/
    ├── 💧 hydrology/
    ├── 🗺️ bathymetry/
    ├── 🧱 sediment/
    ├── 🚜 wid-2025/
    ├── 🌊 downstream/
    └── 🌿 ecology/
~~~

- **raw/** → immutable inputs from agencies & sensors  
- **processed/** → harmonized, contract-validated outputs  
- **stac/** → STAC collections/items & DCAT-aligned metadata  

---

## 💧 3. Hydrology Dataset Classes (Domain Taxonomy)

### 3.1 Core Hydrology (USGS / USACE / Mesonet / NOAA)

- Streamflows (cfs)  
- Reservoir elevations (ft)  
- Gate releases (cfs)  
- Storage curves / state-space representations  
- Temperature, precipitation, soil moisture  
- Climate normals, anomalies, indices  

### 3.2 Water Quality

- Turbidity (NTU)  
- TSS (mg/L)  
- DO (mg/L)  
- Nutrients (TP, TN, NH₄, NO₃)  
- Conductivity, pH, chlorophyll  

### 3.3 Sediment & Bathymetry

- Multibeam bathymetric DEMs  
- DoD (Difference of DEM) rasters  
- Sediment core stratigraphy records  
- Grain-size spectra (e.g., LISST)  
- Watershed sediment yield data  

### 3.4 WID (Water Injection Dredging)

- Turbidity sensors (1–5 minute resolution)  
- DO sensors (minute-level)  
- ADCP plume transects  
- Jet operations logs  
- Density-current modeling outputs  

### 3.5 Ecology & Downstream Effects

- Mussel beds & locations  
- Fish assemblage surveys  
- Macroinvertebrate indices  
- Vegetation & riparian habitat polygons  

### 3.6 Climate & Hydroclimate

- PRISM precipitation/temperature  
- NOAA NCEI station time series  
- Mesonet station data (multiple depths)  
- CMIP6 downscaled future scenarios  

---

## 🧪 4. Dataset Schema Rules (CSV, GeoJSON, COG, NetCDF)

### 4.1 CSVW (Time Series)

**Required columns:**

| column       | description                           |
|--------------|---------------------------------------|
| `timestamp`  | ISO 8601 datetime                     |
| `value`      | Numeric value                         |
| `units`      | SI / hydrologic standard (e.g., cfs)  |
| `parameter`  | e.g., `flow`, `turbidity`, `DO`       |
| `site_id`    | Canonical KFM hydrology site ID       |
| `provenance` | ETL / dataset lineage identifier      |

CSV schemas must pass validation against the hydrology data contract derived from `data_contract_ref`.

---

### 4.2 GeoJSON (Vector Data)

**Requirements:**

- `type: "FeatureCollection"`  
- CRS: WGS84 (EPSG:4326)  
- `geometry`: `Point`, `LineString`, or `Polygon`  
- `properties` MUST include:
  - `license`  
  - `provider`  
  - `parameter` (e.g., `DO`, `turbidity`)  
  - `timestamp` or `valid_time`  
  - `kfm:dataset_id`  

---

### 4.3 Cloud-Optimized GeoTIFF (COG)

Used for:

- Bathymetry rasters  
- DoD rasters  
- Sediment extent / plume models  

**Requirements:**

- Internal tiling & overviews  
- EPSG:4326 or reservoir-specific CRS with metadata  
- Must include tags:
  - `kfm:dataset_type`  
  - `kfm:lineage`  
  - `kfm:processing_step`  

---

### 4.4 NetCDF (Climate & Hydraulics)

**Requirements:**

- CF-conformant NetCDF  
- Dimensions: `time`, `lat`, `lon` (and optionally `depth`, `layer`)  
- Variables: precipitation, temperature, hydraulic variables, etc.  
- Full metadata:
  - `source`  
  - `history` (processing chain)  
  - `institution`  
  - `references`  

---

## 🛠 5. ETL Pipeline Architecture (Hydrology Domain)

### 5.1 Extraction

From:

- **USGS NWIS** APIs  
- **KDHE** water-quality archives  
- **USACE** choke-point/reservoir data  
- **Kansas Mesonet** API  
- **NOAA** climate services  
- Local CSV, PDF, DOC, and other formats  

### 5.2 Transformation

- Harmonization to CSVW / GeoJSON / NetCDF as appropriate  
- QA/QC flagging (e.g., `qflag` columns, BDL handling)  
- Spatial reprojection to KFM-standard CRS  
- Time-series interpolation/resampling (documented)  
- Unit normalization (e.g., mg/L, cfs, °C)  
- Validation against hydrology schemas & data contracts  

### 5.3 Loading

- Processed datasets → `data/hydrology/processed/**`  
- STAC Items → `data/hydrology/stac/**`  
- Graph ingestion (Neo4j):

  - Nodes: Places, Events, Datasets, Observations  
  - Edges: `prov:wasGeneratedBy`, `geo:hasGeometry`, `time:hasTime`  

APIs expose hydrated domain views from Neo4j to the frontend; hydrology datasets **must not** be read directly from filesystem by UI components except in governed migration or debugging utilities.

---

## 🛰 6. STAC Collections (Hydrology Domain · Emoji Style A)

~~~text
data/hydrology/stac/
├── 💧 hydrology/
│   ├── 📁 collection.json
│   └── 📂 items/
│        ├── 💧 inflows/
│        ├── 💧 outflows/
│        ├── 📈 timeseries/
│        └── 🧪 water-quality/
│
├── 🗺️ bathymetry/
│   ├── 📁 collection.json
│   └── 📂 items/
│        ├── 🗺️ multibeam/
│        ├── 🗺️ dod/
│        └── 🧪 sediment-cores/
│
├── 🧱 sediment/
│   ├── 📁 collection.json
│   └── 📂 items/
│        ├── 🧱 volumes/
│        ├── 🧱 grain-size/
│        └── 🧱 cores/
│
├── 🚜 wid-2025/
│   ├── 📁 collection.json
│   └── 📂 items/
│        ├── 🚜 adcp/
│        ├── 🚜 sensors/
│        └── 🚜 operations/
│
├── 🌊 downstream/
│   ├── 📁 collection.json
│   └── 📂 items/
│        ├── 🌊 turbidity/
│        ├── 🌊 do/
│        └── 🌿 ecology/
│
└── 🌿 ecology/
    ├── 📁 collection.json
    └── 📂 items/
         ├── 🌿 fish/
         ├── 🌿 mussels/
         └── 🌿 macroinvertebrates/
~~~

Each `collection.json` includes:

- `id`, `title`, `description`  
- spatial & temporal `extent`  
- `license`, `providers`  
- DCAT 3.0 alignment & PROV-O lineage summary  

---

## 🛰️ 7. STAC Item Template (Hydrology)

~~~json
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
~~~

---

## 🕸 8. Knowledge Graph Ontology (CIDOC-CRM + GeoSPARQL + OWL-Time)

### 8.1 Entities

- `E53 Place:Big_Blue_River`  
- `E53 Place:Tuttle_Creek_Reservoir`  
- `E5 Event:WID_2025`  
- `E73 InformationObject:HydrologyDataset`  
- Observation series nodes (`ObservationSeries:Hydro_Data_<Parameter>`)  
- `E3 ConditionState:Hydro_Condition_<Year>`  

### 8.2 Relations

- `geo:hasGeometry` → spatial representation  
- `time:hasTime` → temporal extent  
- `prov:wasGeneratedBy` → ETL pipeline / model step  
- `P70_documents` → link to source documentation  
- `P7_took_place_at` → event-location link  

All hydrology entities and relations must pass the KFM graph schema validation for Neo4j ingestion before deployment.

---

## 🧬 9. FAIR+CARE Metadata Requirements

Hydrology datasets must include:

- License  
- Spatial footprint  
- Temporal coverage  
- Provenance & lineage  
- Creator & provider roles  
- QA/QC flags  
- DCAT 3.0 fields  
- CARE/sovereignty metadata where relevant  

Sensitive or culturally restricted locations may be generalized or redacted in public exports, in line with `sovereignty_policy`.

---

## 🎯 10. Focus Mode v3 Integration

Focus Mode v3:

- Uses hydrology datasets + graph context  
- Gives narrative explanations for hydrologic events/trends  
- Links to STAC and underlying files via the API (never direct disk paths)  
- Always shows provenance chips and CARE labels  

AI summaries must be **fully grounded** in data, with explicit links back to:

- STAC Items  
- Graph entities (Events, Places, Datasets, Observations)  
- Source documents and ETL runs  

---

## 📖 11. Story Node Integration

Story Nodes using hydrology:

- Represent events (floods, droughts, WID operations)  
- Reference hydrology datasets by ID  
- Provide time + place + narrative + supporting plots  

Examples (to be instantiated as Story Node configs under `docs/reports/visualization/focus_mode/story_nodes/`):

- “A Reservoir Filling From the Bottom Up”  
- “Downstream of the Dam”  
- “The 2025 WID Demonstration”  

Each Story Node must specify:

- Spatial extent (GeoJSON / graph Place IDs)  
- Temporal extent (OWL-Time interval)  
- Linked datasets (STAC + graph IDs)  
- Narrative text + figure specifications  

---

## 🚀 12. Expansion Roadmap

Planned hydrology domain features (v11+):

- 2D/3D hydrodynamic model integration (NetCDF + COG tiles)  
- Climate-sediment-coupled overlays for extreme events  
- Bathymetric change visualization timelines in MapLibre/Cesium  
- Streaming sensor ingestion & STAC streaming collections  
- Dedicated hydrology API surface and schema docs under `docs/architecture/api/hydrology-api.md`  

All new features MUST:

- Extend this index and associated STAC collections  
- Register PROV entities/activities for every new ETL or model run  
- Pass CI checks for STAC, DCAT, PROV, and graph schemas  

---

## 🕰 13. Version History

| Version | Date       | Notes                                                                                                  |
|--------:|-----------:|--------------------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | Realigned to **KFM-MDP v11.2.6**, updated release refs, tilde code fences, and clarified pipeline links. |
| v11.2.2 | 2025-11-27 | Applied emoji styling to STAC collections; updated metadata; enforced KFM-MDP v11.2.2.                |
| v11.0.0 | 2025-11-21 | Initial “Super-Edition” hydrology domain index & taxonomy.                                             |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[⬅️ Back](../README.md) · [🗃️ Archive & Provenance](../archive/README.md) · [🛡️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
