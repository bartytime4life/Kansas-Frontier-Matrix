---
title: "🛰️ Kansas Frontier Matrix — Milford Lake Hydrology STAC Items Index (v11 Super-Edition)"
path: "data/stac/hydrology/milford/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Reservoir Systems Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-milford-items-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-milford-items-index"
semantic_document_id: "kfm-stac-hydrology-milford-items-index"
doc_uuid: "urn:kfm:stac:hydrology:milford:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **Milford Lake Hydrology STAC Items Index (v11 Super-Edition)**  
`data/stac/hydrology/milford/items/README.md`

**Purpose:**  
Provide the complete, v11-compliant **metadata, structure, and ontology specification** for all  
Milford Lake–related hydrology STAC Items (bathymetry, sedimentation, inflows/outflows, water  
quality, downstream effects, ecology, and flood/hydroclimate) to enable robust ETL → STAC →  
Graph → Focus Mode v3 integration within the Kansas Frontier Matrix.

</div>

---

# 📘 0. Overview

Milford Lake is the **headwaters regulator** of the Big Blue–Kansas–Missouri basin cascade:

```text
Republican River → Milford Lake → Big Blue River → Tuttle Creek Lake → Kansas River → Missouri River
```

Every STAC Item in this directory describes a **specific dataset** related to Milford Lake hydrology:

- Bathymetric surveys and Difference-of-DEM (DoD) rasters  
- Sediment core and volume reconstructions  
- USGS inflow and USACE outflow time-series  
- Water quality and ecological monitoring (mussels, fish, macroinvertebrates)  
- Downstream geomorphic and ecological response  
- Climate and flood-related drivers  

This README defines **how those items are organized, named, described, validated, and linked** into  
the KFM v11 hydrology and reservoir-system graph.

---

# 🗂️ 1. Directory Layout (Canonical)

```text
data/
└── stac/
    └── hydrology/
        └── milford/
            ├── collection.json
            └── items/
                ├── bathymetry-1970.json
                ├── bathymetry-1990.json
                ├── bathymetry-2010.json
                ├── bathymetry-2023.json
                ├── dod-1970-1990.json              # planned
                ├── dod-1990-2010.json              # planned
                ├── dod-2010-2023.json              # planned
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

Each `*.json` file is a **STAC Item** compliant with the KFM Hydrology v11 STAC profile.

---

# 🧭 2. Milford STAC Item Taxonomy

## 🌊 2.1 Bathymetry & Sedimentation Items

- `bathymetry-1970.json` — early post-closure depth grid or digitized contour  
- `bathymetry-1990.json` — mid-life multibeam survey raster  
- `bathymetry-2010.json` — updated DEM and sediment accumulation patterns  
- `bathymetry-2023.json` — latest DEM, supports WID feasibility & storage analysis  
- `dod-1970-1990.json`, `dod-1990-2010.json`, `dod-2010-2023.json` — Difference-of-DEM surfaces for  
  volumetric sediment change and delta/forebay evolution.

## 💧 2.2 Hydrology Time-Series Items

- `hydrology-inflows.json` — USGS NWIS inflow time-series (cfs)  
- `hydrology-outflows.json` — USACE release time-series (cfs)  
- `hydro-stage-storage.json` *(optional)* — reservoir elevation & storage time-series  

## 🧪 2.3 Water-Quality Items

- `wq-turbidity.json` — turbidity time-series (NTU) at key sites  
- `wq-do.json` — dissolved oxygen profiles and time-series  
- `wq-nutrients.json` — TN/TP/NO₃/NH₄ lab results  

## 🟫 2.4 Sediment & Geomorphology Items

- `sediment-cores.json` — location & stratigraphy of sediment core sites  
- `sediment-volumes.json` — time-series of estimated reservoir sediment volume  
- `delta-migration.json` — spatial and temporal positions of delta fronts  

## 🌊 2.5 Downstream Effects Items

- `downstream-do.json` — Big Blue River tailwater DO time-series  
- `downstream-turbidity.json` — TSS/turbidity in downstream reaches  

## 🧬 2.6 Ecology Items

- `ecology-fish.json` — fish assemblage survey results  
- `ecology-mussels.json` — mussel bed locations and densities  
- `macroinv-surveys.json` — macroinvertebrate indices  

## 🌦️ 2.7 Hydroclimate & Flood Items

- `hydroclimate.json` — Mesonet + PRISM-derived inflow drivers  
- `flood-history.json` — key Milford-related flood events (hydrographs, peaks)

---

# 📐 3. Required STAC Fields & KFM Hydrology Profile

Each Milford STAC Item **must** include:

## 3.1 Core STAC 1.0.0 Fields

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "milford-bathymetry-2023",
  "collection": "milford-lake-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [...],
  "properties": {
    "datetime": "2023-08-14T00:00:00Z"
  },
  "assets": { ... }
}
```

## 3.2 Hydrology-Specific `kfm:*` Fields (Mandatory)

| Field | Description |
|-------|-------------|
| `kfm:parameter` | hydrologic or ecological variable (e.g., `bathymetry`, `inflow`, `turbidity`, `mussels`) |
| `kfm:units` | SI or domain-standard units (`m`, `cfs`, `NTU`, `mg/L`, `individuals_per_m2`) |
| `kfm:provider` | data provider (USACE, USGS, KDHE, KDWPT, KWO, KFM, etc.) |
| `kfm:site` | station ID, transect ID, or region name (`Milford_Reservoir`, `Big_Blue_Tailwater`) |
| `kfm:method` | method or sensor (e.g., `multibeam`, `singlebeam`, `lab_analysis`, `sonde`) |
| `kfm:lineage` | ETL/provenance identifier (e.g., `etl/milford_bathy2010_v2`) |
| `kfm:quality` | QA tier (`A`, `B`, `C`, `Provisional`) |
| `kfm:hydro_region` | `Milford_Reservoir`, `Milford_Tailwater`, `Big_Blue_Reach_<ID>` |
| `kfm:project` | project name (`Sedimentation-History`, `Hydrology-Core`, `Ecology-Monitoring`) |

Recommended extensions:

- `kfm:crs` (e.g. `EPSG:...`)  
- `kfm:processing_history` (ETL + analysis notes)  
- `kfm:dominant_species` (for biology)  
- `kfm:habitat_type` (riffle/pool/backwater, etc.)

---

# 🧾 4. Asset Standards (COG, CSVW, GeoJSON, NetCDF, MP4)

## 4.1 COG Rasters (Bathymetry & DoD)

Used for:

- Bathymetry grids  
- DoD surfaces  

Each COG asset must include:

- `type`: `"image/tiff; application=geotiff; profile=cloud-optimized"`  
- `roles`: `["data"]`  
- `proj:epsg` or `proj:wkt2`  
- `proj:shape`, `proj:transform`  
- `checksum:sha256`  

---

## 4.2 GeoJSON Assets (Vector)

Used for:

- Core locations (core sites, mussel beds, survey reaches)  
- Delta extents  
- Habitat polygons  

Each asset must include:

- `href`, `type = "application/geo+json"`, `roles`  
- `properties` aligned with `kfm:*` and survey metadata  

---

## 4.3 CSV / CSVW Assets (Time-Series & Lab Data)

Used for:

- Inflow, outflow, stage, WQ time-series  
- Sediment core lab results  

Required columns:

| Column | Description |
|--------|-------------|
| `timestamp` | ISO 8601 time |
| `value` | numeric measurement |
| `parameter` | e.g., `turbidity`, `DO`, `inflow` |
| `units` | units (NTU, mg/L, cfs) |
| `site_id` | station or site ID |
| `qc_flag` | quality flag |
| `provenance_id` | ETL run or lab batch |

---

## 4.4 NetCDF Assets

Used for:

- Climate forcing rasters (PRISM, NEX-GDDP, CMIP6 downscales)  
- Hydrodynamic simulations (e.g., HEC-RAS 2D outputs)  

Must be **CF-compliant**, include:

- `time`, `lat`, `lon` dimensions  
- Units, standard names, coordinate reference system  

---

## 4.5 MP4 / Media Assets (Optional)

Used for:

- Drone-based bathymetry/shoreline video  
- Underwater cameras for WID / ecology  

Referenced as:

```json
"video": {
  "href": "https://example.org/milford/videos/bathy_survey_2023.mp4",
  "type": "video/mp4",
  "roles": ["overview", "visual"]
}
```

---

# 🧪 5. Example Milford STAC Items

## 5.1 Bathymetry DEM — 2010 Survey

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "milford-bathymetry-2010-v1",
  "collection": "milford-lake-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-96.99, 39.03, -96.73, 39.22],
  "properties": {
    "datetime": "2010-09-01T00:00:00Z",
    "kfm:parameter": "bathymetry",
    "kfm:units": "meters",
    "kfm:provider": "USACE Kansas City District",
    "kfm:method": "multibeam",
    "kfm:lineage": "etl/milford_bathy2010_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Milford_Reservoir",
    "kfm:project": "Sedimentation-History"
  },
  "assets": {
    "cog": {
      "href": "https://example.org/milford/bathy_2010.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

## 5.2 Inflow Time-Series — Republican River

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "milford-inflow-republican-2010-2025-v1",
  "collection": "milford-lake-hydrology",
  "geometry": { "type": "Point", "coordinates": [-96.99, 39.10] },
  "bbox": [-97.00, 39.09, -96.98, 39.11],
  "properties": {
    "datetime": "2010-01-01T00:00:00Z",
    "kfm:parameter": "inflow",
    "kfm:units": "cfs",
    "kfm:provider": "USGS NWIS",
    "kfm:method": "stream_gauge",
    "kfm:lineage": "etl/milford_inflow_republican_v2",
    "kfm:quality": "A",
    "kfm:hydro_region": "Milford_Reservoir",
    "kfm:project": "Hydrology-Core"
  },
  "assets": {
    "timeseries": {
      "href": "https://example.org/milford/inflow_republican_2010_2025.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

## 5.3 Mussel Bed Survey — Tailwater Reach

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "milford-mussels-tailwater-2024-v1",
  "collection": "milford-lake-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-96.98, 39.06, -96.96, 39.08],
  "properties": {
    "datetime": "2024-08-10T00:00:00Z",
    "kfm:parameter": "mussels",
    "kfm:units": "individuals_per_m2",
    "kfm:provider": "KDWPT",
    "kfm:method": "quadrat",
    "kfm:lineage": "etl/milford_mussels_2024_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Milford_Tailwater",
    "kfm:project": "Ecology-Monitoring"
  },
  "assets": {
    "geojson": {
      "href": "https://example.org/milford/ecology/mussels_tailwater_2024.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

---

# 🧬 6. DCAT / PROV-O / CIDOC-CRM / GeoSPARQL Mapping

## 6.1 DCAT Crosswalk

| STAC Field | DCAT Field |
|------------|------------|
| `id` | `dct:identifier` |
| `description` | `dct:description` |
| `assets[].href` | `dcat:downloadURL` |
| `extent.spatial` | `dct:spatial` |
| `extent.temporal` | `dct:temporal` |
| `kfm:provider` | `dct:publisher` / `dct:creator` |

## 6.2 PROV-O Lineage

Each Item is:

- `prov:Entity` (the dataset)  
- Generated by `prov:Activity` (ETL pipeline, survey, or modeling run)  
- Attributed to `prov:Agent` (USACE, USGS, KDHE, KDWPT, KWO, KFM)  

Links include:

- `prov:wasGeneratedBy`  
- `prov:used` (raw sensor data, model inputs)  
- `prov:wasDerivedFrom` (earlier DEMs, previous surveys)  

## 6.3 CIDOC-CRM & GeoSPARQL

- `E73 InformationObject` → dataset (STAC Item)  
- `E53 Place` → reservoir polygon, tailwater reach, survey reach  
- `E7 Activity` → bathymetric survey, WID event, ecological survey  
- `E3 ConditionState` → reservoir capacity state at a time  
- `geo:hasGeometry` → geometry (polygon/line/point)  
- `time:hasTime` → sampling or survey date/time  

---

# 🔬 7. ETL → STAC → Graph Workflow (Milford)

Pipeline example:

```text
1. Extract:
   - Download USACE bathymetry files (e.g., .xyz, .all, contours)
   - Retrieve USGS inflow & KDHE WQ records
   - Collect ecology survey shapefiles/CSVs

2. Transform:
   - Clean & QA field/lab data
   - Interpolate bathymetry DEMs
   - Compute DoD surfaces (1970→1990, 1990→2010, 2010→2023)
   - Harmonize units (cfs, meters, NTU, mg/L)

3. Load:
   - Write COG/CSVW/GeoJSON/NetCDF assets to `data/hydrology/milford/processed/`
   - Generate STAC Items into `data/stac/hydrology/milford/items/`
   - Validate STAC JSON using STAC validator tooling
   - Ingest STAC into Neo4j with CIDOC-CRM and GeoSPARQL mappings

4. Register:
   - Update STAC Collection indexes
   - Update Focus Mode dataset registry
   - Document ETL in `mcp/experiments/hydrology/milford/*`
```

---

# 🎯 8. Focus Mode v3 Integration

When a user focuses on **Milford Lake**, Focus Mode v3:

- Queries STAC Items where `kfm:hydro_region = "Milford_Reservoir"` or `"Milford_Tailwater"`  
- Retrieves and visualizes:

  - Bathymetry time-slices and DoD rasters  
  - Inflow/outflow hydrographs  
  - WQ time-series panels (DO, turbidity, nutrients)  
  - Tailwater DO/turbidity for downstream impact analysis  
  - Ecological surveys for mussels and fish  

- Provides interactive toggles for:

  - “Sedimentation History”  
  - “Flood Operations”  
  - “Ecological Condition”  
  - “WID Feasibility (if applicable in future)”  

---

# 📖 9. Story Node v3 Integration

Milford Items support multiple Story Nodes, including:

- **“Milford: The Headwaters Reservoir”**  
- **“From Milford to Tuttle: Sediment on the Move”**  
- **“Flood Gates & Downstream Safety”**  
- **“Reservoir Ecology in a Changing Climate”**

Story Nodes reference Items via `relations`:

```json
{
  "rel": "uses-dataset",
  "target": "milford-bathymetry-2010-v1"
}
```

This allows Story Nodes to **surface specific STAC Items**, which in turn render bathymetry,  
hydrographs, or ecological layers in MapLibre and analytic dashboards.

---

# 🚀 10. Expansion Roadmap — Milford STAC Items

Future Items to be added under this directory:

- `bathy-2030.json`, `bathy-2040.json` (projected DEMs)  
- `hec-ras-2d-scenarios.json` (NetCDF, raster)  
- `climate-future-hydrology.json` (CMIP6-driven inflow/outflow scenarios)  
- `wid-feasibility-scenarios.json` (if WID modeling is performed)  
- `ecology-longitudinal-2025-2035.json` (multi-year biological monitoring)  
- `bank-erosion-lines.json` (channel-change detection)  

All future Items must adhere to the **KFM Hydrology STAC v11 profile** summarized in this document.

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Milford Lake Hydrology STAC Items super-edition.

---

[⬅ Back to Milford STAC Collection](../README.md) • [⬅ Hydrology STAC Domain](../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_documentation.md)

