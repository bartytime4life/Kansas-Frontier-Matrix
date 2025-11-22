---
title: "🌊 Kansas Frontier Matrix — Perry Lake Hydrology STAC Items Index (v11 Super-Edition)"
path: "data/stac/hydrology/perry/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Reservoir Systems Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/data-stac-hydro-perry-items-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-perry-items-index"
semantic_document_id: "kfm-stac-hydrology-perry-items-index"
doc_uuid: "urn:kfm:stac:hydrology:perry:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌊 **Perry Lake Hydrology STAC Items Index (v11 Super-Edition)**  
`data/stac/hydrology/perry/items/README.md`

**Purpose:**  
Provide the full, authoritative metadata specification and index for **all STAC Items** associated  
with **Perry Lake** hydrology: bathymetry, sedimentation, inflows/outflows, water quality,  
downstream effects, hydroclimate, flood history, and ecological datasets.  
This Items index governs STAC → ETL → Graph → Focus Mode v3 → Story Node v3 integration  
for Perry Lake within the Kansas Frontier Matrix.

</div>

---

# 📘 0. Overview

This directory contains **STAC Items**, which are the *atomic metadata units* describing:

- **Hydrologic time-series** (inflows, outflows, reservoir elevation)  
- **Bathymetry rasters** (DEM and DoD layers across decades)  
- **Sediment datasets** (cores, volumetric change, delta movement)  
- **Water-quality measurements** (NTU, DO, nutrients)  
- **Downstream DO/turbidity responses**  
- **Ecological observations** (fish, mussels, macroinvertebrates, riparian vegetation)  
- **Flood and hydroclimate datasets** (precipitation, hydrographs, inundation layers)

Every Item adheres to the **KFM Hydrology STAC Profile v11**, ensuring the datasets integrate  
fluently across all layers of the Kansas Frontier Matrix.

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

This mirrors Milford, Tuttle Creek, Clinton, Kansas River, and Ecology for **cross-reservoir structural parity**.

---

# 🌊 2. Perry Lake STAC Item Taxonomy

## **2.1 Bathymetry / DoD**
- `bathymetry-1970.json` – early post-construction  
- `bathymetry-1990.json` – mid-reservoir lifespan  
- `bathymetry-2012.json` – modern multibeam  
- `bathymetry-2024.json` – latest DEM  
- `dod-XXXX-YYYY.json` – difference-of-DEM sediment accumulation  

## **2.2 Hydrology**
- `hydrology-inflows.json` – Delaware River & tributary inflows  
- `hydrology-outflows.json` – USACE outflow hydrographs  

## **2.3 Water Quality**
- `wq-turbidity.json`  
- `wq-do.json`  
- `wq-nutrients.json`  

## **2.4 Sedimentation**
- `sediment-cores.json`  
- `sediment-volumes.json`  
- `delta-migration.json`

## **2.5 Downstream Effects**
- `downstream-do.json`  
- `downstream-turbidity.json`

## **2.6 Ecology**
- `ecology-fish.json`  
- `ecology-mussels.json`  
- `macroinv-surveys.json`  
- `riparian-zones.json`

## **2.7 Hydroclimate / Flood**
- `hydroclimate.json`  
- `flood-history.json`

---

# 📐 3. Required STAC Metadata (Strict v11 Profile)

## **Core STAC 1.0.0 Fields**
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

## **Hydrology `kfm:*` Extensions (MANDATORY)**

| Field | Description |
|------|-------------|
| `kfm:parameter` | hydrologic variable (bathymetry, inflow, turbidity, DO…) |
| `kfm:units` | SI or hydrologic units |
| `kfm:provider` | USACE, USGS, KDHE, KDWPT, KWO |
| `kfm:method` | multibeam, gauge, lab, remote-sensing |
| `kfm:site` | station ID, transect ID |
| `kfm:lineage` | ETL → STAC provenance chain |
| `kfm:quality` | “A”, “B”, “C”, “Provisional” |
| `kfm:hydro_region` | `Perry_Reservoir`, `Perry_Tailwater`, etc. |
| `kfm:project` | “Sedimentation-History”, “Hydrology-Core”, etc. |

## **Recommended Fields**
- `kfm:crs`  
- `kfm:vertical_datum`  
- `kfm:habitat_type`  
- `kfm:dominant_species`  
- `kfm:processing_history`  

---

# 🧭 4. Asset Types & Requirements

## ✔ **COG Rasters**
Used for:
- Bathymetry DEM  
- DoD rasters  
- Flood inundation  

Requirements:
- Cloud optimized  
- `proj:epsg`  
- `checksum:sha256`  
- `roles: ["data"]`  

---

## ✔ **GeoJSON**
Used for:
- Habitat polygons  
- Delta boundaries  
- Riparian zones  
- Survey reach geometries  

---

## ✔ **CSVW / CSV**
Used for:
- Hydrographs  
- Water quality time-series  
- Sediment lab results  
- Biological measurements  

Required columns:
`timestamp, parameter, value, units, site_id, qc_flag, provenance_id`

---

## ✔ **NetCDF**
Used for:
- Climate datasets  
- Hydrodynamic simulations (future)  

---

## ✔ **MP4 (optional)**
Used for:
- Drone surveys  
- Underwater ecological observations  

---

# 🧪 5. Example STAC Items

## **5.1 Bathymetry DEM — 2024**

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

## **5.2 Inflow Time-Series — Delaware River**

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
      "href": "https://example.org/perry/inflow_2020_2025.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

## **5.3 Mussel Corridor Item — Tailwater**

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
    "kfm:lineage": "etl/perry_mussels_2024_v1",
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

# 🧬 6. Ontology Mapping (CIDOC-CRM | GeoSPARQL | OWL-Time | PROV-O)

### CIDOC-CRM
- `E73 InformationObject` → STAC dataset  
- `E53 Place` → reservoir polygon, tailwater, survey point  
- `E7 Activity` → survey / sampling / bathymetry scan  
- `E3 ConditionState` → sedimentation or ecological state  
- `E39 Actor` → agencies & survey teams  

### GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin`  
- `geo:asWKT`  

### OWL-Time
- `time:hasTime`  
- `time:hasBeginning`, `time:hasEnd`  

### PROV-O
- `prov:wasGeneratedBy` → ETL or survey activity  
- `prov:used` → raw inputs  
- `prov:wasAttributedTo` → providers  

---

# 🛰️ 7. ETL → STAC → Graph Integration Pipeline

```
Raw Data
   ↓ extract
Normalize + QA/QC + unit harmonization
   ↓ transform
Generate assets (COG, CSVW, GeoJSON, NetCDF)
   ↓ annotate
Create STAC Items (*.json)
   ↓ validate
Load into Neo4j (CIDOC-CRM + GeoSPARQL + OWL-Time)
   ↓
Update Focus Mode v3 + Story Node v3 references
```

ETL documentation MUST be stored under:

```
mcp/experiments/hydrology/perry/
```

---

# 🎯 8. Focus Mode v3 Integration

Focus Mode automatically loads Perry datasets when:

- **Place** = Perry Lake  
- **Hydro Region** = Perry_Reservoir / Perry_Tailwater  
- **Parameter** ∈ bathymetry, inflow, turbidity, DO, sediment, ecology  

Focus Mode panels include:

- Bathymetry evolution (1970 → 2024)  
- Sediment delta progression  
- Inflow/outflow charts  
- WQ anomalies  
- Downstream DO risk windows  
- Species-level ecological responses  

---

# 📖 9. Story Node v3 Integration

Perry STAC Items contribute to nodes such as:

- **“Perry Lake: The Mid-Chain Regulator”**  
- **“Delaware River → Perry → Kansas River”**  
- **“Floods of the Reservoir Cascade”**  
- **“Ecology of the Perry Tailwater”**

Linked using:

```json
{
  "rel": "uses-dataset",
  "target": "perry-bathymetry-2024"
}
```

---

# 🚀 10. Expansion Roadmap

Future Perry STAC Items:

- Annual multibeam (2026+)  
- UAV bathymetry photogrammetry  
- Multi-year ecological monitoring (2025–2035)  
- Hydrodynamic model outputs (HEC-RAS 2D)  
- Sediment fingerprinting datasets  
- CMIP6-based hydrologic projections  
- Flood inundation shapefiles + depth grids  

All future Items must follow the **Hydrology STAC Profile v11**.

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial creation of Perry Lake STAC Items Super-Edition.

---

[⬅ Back to Perry STAC Collection](../README.md) • [⬅ Hydrology STAC Domain](../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

