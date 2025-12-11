---
title: "💧 Kansas Frontier Matrix — Hydrology Data Domain Index (v11 Super-Edition)"
path: "data/hydrology/README.md"
version: "v11.2.2"
last_updated: "2025-12-10"
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

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/focus-telemetry.json"
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

Anchored in the KFM core pipeline: **Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode**.

</div>

---

## 📘 Overview

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
and connected to the knowledge graph, Story Nodes, and Focus Mode v3, **within the KFM pipeline**:

- Deterministic hydrology ETL jobs under `src/pipelines/hydrology/**`  
- STAC/DCAT/PROV catalogs under `data/hydrology/stac/**` and `data/sources/**`  
- Neo4j hydrology subgraph ingest (`:HydroSite`, `:HydroTimeSeries`, `:HydroRaster`, `:HydroEvent`)  
- API surfaces (hydrology-aligned endpoints in `src/api/**`)  
- React/MapLibre/Cesium layers and Focus Mode v3 Story Nodes for hydrology events and trends  

All changes to this domain index **must** remain compatible with that end-to-end chain.

---

## 🗂️ Directory Layout

Authoritative layout · Emoji Style A · Hydrology domain only.

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

Each subdirectory must have:

- A **source manifest** under `data/sources/**` (FAIR+CARE, license, provenance)  
- A **STAC Collection / Item** under `data/hydrology/stac/**`  
- A **Neo4j ingestion config** under `src/graph/hydrology/**` (or shared graph configs)  

---

## 💧 Hydrology Dataset Classes (Domain Taxonomy)

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

## 🧪 Dataset Schema Rules (CSV, GeoJSON, COG, NetCDF)

Hydrology datasets **must** conform to KFM contracts and schemas. CSV/GeoJSON/COG/NetCDF schemas are validated via:

- Data contracts under `schemas/contracts/hydrology/**`  
- CI checks under `.github/workflows/data-hydrology-validate.yml`  

### 4.1 CSVW (Time Series)

**Required columns:**

| column       | description                          |
|--------------|--------------------------------------|
| `timestamp`  | ISO 8601 datetime                    |
| `value`      | Numeric value                        |
| `units`      | SI / hydrologic standard (e.g., cfs) |
| `parameter`  | e.g., `flow`, `turbidity`, `DO`      |
| `site_id`    | Canonical KFM hydrology site ID      |
| `provenance` | ETL / dataset lineage identifier     |

Additional **recommended** columns:

- `qflag` (QA/QC flags, BDL, sensor error codes)  
- `method` (e.g., `USGS-provisional`, `model-output`, `lab-analysis`)  
- `sample_depth_m` (for vertical profiles)  

CSV schemas must pass validation against the hydrology data contract derived from `data_contract_ref`.

---

### 4.2 GeoJSON (Vector Data)

**Requirements:**

- `type: "FeatureCollection"`  
- CRS: WGS84 (EPSG:4326)  
- `geometry`: `Point`, `LineString`, or `Polygon`  

`properties` MUST include:

- `license`  
- `provider`  
- `parameter` (e.g., `DO`, `turbidity`)  
- `timestamp` or `valid_time`  
- `kfm:dataset_id`  

Recommended hydrology-specific properties:

- `hydro:reach_id`, `hydro:segment_id`  
- `hydro:transect_id` (for ADCP / WID traverses)  
- `care:sovereignty` flags where Indigenous or sensitive sites are present  

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

COGs are listed as STAC raster assets, and linked to:

- Graph nodes `:HydroRaster`  
- Story Nodes that visualize change through time (e.g., bathymetric differencing)  

---

### 4.4 NetCDF (Climate & Hydraulics)

**Requirements:**

- CF-conformant NetCDF  
- Dimensions: `time`, `lat`, `lon` (and optionally `depth`, `layer`)  
- Variables: precipitation, temperature, hydraulic variables, etc.  

Full metadata:

- `source`  
- `history` (processing chain)  
- `institution`  
- `references`  

Hydrology-oriented metadata:

- `kfm:scenario` (e.g., `historical`, `ssp245`, `ssp585`)  
- `kfm:run_id` for ensemble members  
- `prov:wasGeneratedBy` references for model workflows  

---

## 🛠 ETL Pipeline Architecture (Hydrology Domain)

Hydrology ETL pipelines live under `src/pipelines/hydrology/**` and are **config-driven, deterministic, and reproducible**.

### 5.1 Extraction

From:

- **USGS NWIS** APIs  
- **KDHE** water-quality archives  
- **USACE** choke-point/reservoir data  
- **Kansas Mesonet** API  
- **NOAA** climate services  
- Local CSV, PDF, DOC, and other formats  

Extraction rules:

- Credentialed sources must use secrets compliant with `docs/security/SECRETS-POLICY.md`.  
- Each extract job writes raw files into `data/hydrology/raw/**` plus a `*_source.json` manifest under `data/sources/**`.  

### 5.2 Transformation

- Harmonization to CSVW / GeoJSON / NetCDF as appropriate  
- QA/QC flagging (e.g., `qflag` columns, BDL handling)  
- Spatial reprojection to KFM-standard CRS  
- Time-series interpolation/resampling (documented)  
- Unit normalization (e.g., mg/L, cfs, °C)  
- Validation against hydrology schemas & data contracts  

Transformation logs:

- PROV Activities under `mcp/experiments/hydrology/**`  
- Deterministic seeds recorded where randomness exists (e.g., Monte Carlo or bootstrapping)  

### 5.3 Loading

- Processed datasets → `data/hydrology/processed/**`  
- STAC Items → `data/hydrology/stac/**`  

Graph ingestion (Neo4j):

- Nodes:
  - `:Place` (rivers, reservoirs, gages)  
  - `:HydroSite`, `:HydroTimeSeries`, `:HydroRaster`, `:HydroEvent`  
  - `:Dataset` and `:Document` entities for catalogs  

- Edges:
  - `prov:wasGeneratedBy` → ETL pipeline / model step  
  - `prov:wasDerivedFrom` → raw input entities  
  - `geo:hasGeometry` → spatial representation  
  - `time:hasTime` → temporal extent  

APIs expose hydrology content via contracts in `src/api/**`, and front-end layers in `src/web/**` consume those APIs for MapLibre/Cesium visualizations.

---

## 🛰️ STAC Collections (Hydrology Domain · Emoji Style A)

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
- Spatial & temporal `extent`  
- `license`, `providers`  
- DCAT 3.0 alignment & PROV-O lineage summary  

All hydrology collections must:

- Declare `stac_extensions` relevant to time-series and rasters.  
- Include `kfm:*` properties for graph-ontology mapping (e.g., `kfm:parameter`, `kfm:units`, `kfm:place_ids`).  

---

## 🛰️ STAC Item Template (Hydrology)

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

Hydrology STAC items should also include:

- `prov:wasGeneratedBy` referencing an ETL activity id  
- `kfm:graph_node_ids` to link into Neo4j  
- Optional quicklook assets for Focus Mode charts (e.g., PNG of hydrograph)  

---

## 🕸 Knowledge Graph Ontology (CIDOC-CRM + GeoSPARQL + OWL-Time)

### 8.1 Entities

Core hydrology-related entities:

- `E53 Place:Big_Blue_River`  
- `E53 Place:Tuttle_Creek_Reservoir`  
- `E5 Event:WID_2025`  
- `E73 InformationObject:HydrologyDataset`  
- Observation series nodes (`ObservationSeries:Hydro_Data_<Parameter>`)  
- `E3 ConditionState:Hydro_Condition_<Year>`  

Hydrology-specific candidates (draft KFM-OP extensions):

- `:HydroSite` (gages, sampling points, transects)  
- `:HydroTimeSeries` (parameterized observation series)  
- `:HydroRaster` (bathymetry, DoD, plume models)  
- `:HydroEvent` (floods, droughts, dredging operations)  

### 8.2 Relations

- `geo:hasGeometry` → spatial representation  
- `time:hasTime` → temporal extent  
- `prov:wasGeneratedBy` → ETL pipeline / model step  
- `prov:wasDerivedFrom` → upstream datasets  
- `P70_documents` → link to source documentation  
- `P7_took_place_at` → event-location link  

Hydrology graph ingestion must be:

- **Schema-aligned** with KFM-OP v11.0  
- **Traceable** back to STAC/DCAT/PROV entities  
- **Queryable** by place, parameter, and time for Focus Mode and Story Nodes  

---

## 🧬 FAIR+CARE Metadata Requirements

Hydrology datasets must include:

- License  
- Spatial footprint  
- Temporal coverage  
- Provenance & lineage  
- Creator & provider roles  
- QA/QC flags  
- DCAT 3.0 fields  
- CARE/sovereignty metadata where relevant  

CARE/sovereignty notes:

- Sensitive ecological or cultural sites may be generalized or redacted.  
- Indigenous rights metadata is recorded at **dataset-level and site-level** where appropriate.  
- Any automated discovery or surfacing of sensitive hydrology sites in Focus Mode must respect `sovereignty_policy`.  

---

## 🎯 Focus Mode v3 Integration

Focus Mode v3:

- Uses hydrology datasets + graph context.  
- Generates narrative explanations for hydrologic events/trends (e.g., floods, WID operations, droughts).  
- Links directly to STAC items and underlying files.  
- Always shows provenance chips and CARE labels.  

Focus Mode hydrology panels typically include:

- **Map view** (river/reservoir context).  
- **Time-series plots** (flows, turbidity, DO, etc.).  
- **Narrative text** grounded in data and graph relations.  
- **Links** to raw and processed hydrology assets for expert review.  

AI summaries must be **fully grounded** in hydrology data and graph facts. Speculation must be explicitly labeled as such.

---

## 📖 Story Node Integration

Story Nodes using hydrology:

- Represent events (floods, droughts, WID operations, reservoir management changes).  
- Reference hydrology datasets by ID and graph node.  
- Provide time + place + narrative + supporting plots.  

Examples:

- “A Reservoir Filling From the Bottom Up”  
- “Downstream of the Dam”  
- “The 2025 WID Demonstration”  

Each hydrology Story Node should:

- Cite relevant STAC items (`kfm:stac_item_ids`).  
- Link to `:HydroEvent`, `:Place`, and `:HydroTimeSeries` nodes.  
- Provide quick, accessible explanations of uncertainty and limitations.

---

## 🚀 Expansion Roadmap

Planned hydrology domain features:

- 2D/3D hydrodynamic model integration (CFD outputs as STAC assets & Neo4j entities).  
- Climate-sediment-coupled overlays (CMIP6 + sediment yield models).  
- Bathymetric change visualization timelines (multi-epoch DoD sequences).  
- Streaming sensor ingestion & STAC streaming collections for near-real-time Focus Mode views.  

All new features must:

- Register new collections/items under `data/hydrology/stac/**`.  
- Extend graph schema via KFM-OP review.  
- Add or update CI workflows and telemetry to cover hydrology impacts.

---

## 🕰️ Version History

| Version | Date       | Notes                                                                                     |
|--------:|-----------:|-------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Applied emoji styling to STAC collections; updated metadata; enforced KFM-MDP v11.2.2.   |
| v11.0.0 | 2025-11-21 | Initial “Super-Edition” hydrology domain index & taxonomy.                                |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[⬅️ Back](../README.md) · [🗃️ Archive & Provenance](../archive/README.md) · [🛡️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
