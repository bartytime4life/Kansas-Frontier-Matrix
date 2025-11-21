---
title: "🛰️ Kansas Frontier Matrix — Clinton Lake Hydrology STAC Items Index (v11 Super-Edition)"
path: "data/stac/hydrology/clinton/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/data-stac-hydro-clinton-items-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-clinton-items-index"
semantic_document_id: "kfm-stac-hydrology-clinton-items-index"
doc_uuid: "urn:kfm:stac:hydrology:clinton:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **Clinton Lake Hydrology STAC Items Index (v11 Super-Edition)**  
`data/stac/hydrology/clinton/items/README.md`

**Purpose:**  
Provide the full metadata specification and authoritative domain index for all **Clinton Lake  
Hydrology STAC Items**, including bathymetry, hydrology, sediment, WQ, downstream impacts,  
ecological layers, and derived data products. Defines Item-level metadata, asset profiles,  
ETL lineage, ontology mappings, DCAT/PROV-O relationships, and integration with  
Focus Mode v3 and Story Node v3.

</div>

---

# 📘 0. Overview

This folder contains the **STAC Items** for all Clinton Lake hydrologic datasets.  
Each Item describes **one dataset**, including:

- Geometry  
- Temporal coverage  
- Dependency on sensors, surveys, or models  
- Assets (COG, GeoJSON, CSVW, NetCDF, MP4)  
- Hydrologic semantic metadata  
- Full provenance lineage  
- Cross-domain references (sediment, ecology, climate)

These Items feed the entire KFM v11 stack:

```
STAC → Neo4j Graph → API → Timeline → MapLibre → Focus Mode v3 → Story Nodes
```

---

# 🗂️ 1. Directory Layout (Authoritative)

```text
data/
└── stac/
    └── hydrology/
        └── clinton/
            ├── collection.json
            └── items/
                ├── bathymetry-1994.json
                ├── bathymetry-2010.json
                ├── bathymetry-2022.json
                ├── dod-1994-2010.json                   # future
                ├── dod-2010-2022.json                   # future
                ├── hydrology-inflows.json
                ├── hydrology-outflows.json
                ├── wq-turbidity.json
                ├── wq-do.json
                ├── sediment-cores.json
                ├── sediment-volumes.json
                ├── downstream-do.json
                ├── downstream-turbidity.json
                ├── ecology-fish.json
                └── ecology-mussels.json
```

All Items follow the **KFM-Hydro-Bathy/WQ/Sediment/WID v11 STAC Profile**.

---

# 🛰️ 2. Clinton Lake STAC Item Taxonomy

## ✔ 2.1 Bathymetry Items (COG)
- `bathymetry-1994.json`  
- `bathymetry-2010.json`  
- `bathymetry-2022.json`  
- `dod-1994-2010.json` *(planned)*  
- `dod-2010-2022.json` *(planned)*  

Bathymetry underpins:
- Sedimentation history  
- Forebay evolution  
- Delta trajectory  
- Flood-control behavior  

---

## ✔ 2.2 Hydrology Time-Series Items (CSVW)
- inflows (USGS NWIS)  
- outflows (USACE)  
- reservoir elevation  
- temperature  
- discharge dynamics  

---

## ✔ 2.3 Water Quality (WQ) Items
- Turbidity (NTU)  
- Dissolved Oxygen  
- Nutrients (future)  

---

## ✔ 2.4 Sedimentation Items
- Sediment core surveys  
- Sediment volume time-series  

---

## ✔ 2.5 Downstream Effects Items
- Tailwater DO  
- Downstream turbidity  
- Velocity profiles (future ADCP outputs)  

---

## ✔ 2.6 Ecological Items
- Fish assemblage datasets  
- Mussel habitat polygons  
- Macroinvertebrate inventories *(future)*  

---

# 📐 3. Required STAC Metadata Fields

Every Item MUST include:

## 3.1 Core STAC Fields
```
stac_version: "1.0.0"
type: "Feature"
id: <unique>
collection: "clinton-lake-hydrology"
geometry: <GeoJSON>
bbox: <array>
properties.datetime: <ISO timestamp>
assets: <object>
```

## 3.2 Required Hydrology + KFM v11 Fields (`kfm:*`)

| Field | Description |
|------|-------------|
| `kfm:parameter` | bathymetry, inflow, DO, turbidity, etc. |
| `kfm:units` | SI or hydrology units |
| `kfm:provider` | USACE, USGS, KDHE, KWO |
| `kfm:site` | gauge/WQ station/survey code |
| `kfm:method` | multibeam, buoy sensor, lab sample, etc. |
| `kfm:lineage` | ETL → STAC provenance chain |
| `kfm:quality` | A/B/C QA category |
| `kfm:hydro_region` | `Clinton_Reservoir` |
| `kfm:project` | e.g., `Sedimentation-History` |

---

# 🧭 4. Asset Standards (Bathymetry, Hydrology, WQ, Ecology)

## ✔ 4.1 Raster Assets (COG)
Used for:
- Bathymetry  
- DoD rasters  
- Sediment surfaces  

Required metadata:
- `proj:epsg`  
- `proj:shape`  
- `proj:transform`  
- `checksum:sha256`  
- `roles = ["data"]`  

## ✔ 4.2 Vector Assets (GeoJSON)
Used for:
- Habitat maps  
- Delta extents  
- Survey transects  
- ADCP lines *(future)*  

## ✔ 4.3 CSVW (Timeseries)
Columns:
- `timestamp`  
- `value`  
- `units`  
- `parameter`  
- `site_id`  
- `qc_flag`  

## ✔ 4.4 NetCDF (Optional)
Used for:
- Climate drivers  
- Hydrodynamic model outputs  

## ✔ 4.5 MP4 (Optional)
Used for:
- Drone or ADCP plume visualizations  

---

# 🧬 5. Example STAC Item (Hydrology)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "clinton-inflow-2024",
  "collection": "clinton-lake-hydrology",
  "geometry": { "type": "Point", "coordinates": [-95.39, 38.92] },
  "bbox": [-95.40, 38.91, -95.38, 38.93],
  "properties": {
    "datetime": "2024-01-01T00:00:00Z",
    "kfm:parameter": "inflow",
    "kfm:units": "cfs",
    "kfm:method": "USGS stream gauge",
    "kfm:provider": "USGS NWIS",
    "kfm:lineage": "etl/usgs_ingest_v4",
    "kfm:quality": "A",
    "kfm:hydro_region": "Clinton_Reservoir"
  },
  "assets": {
    "series": {
      "href": "https://example.org/data/clinton/inflow_2024.csv",
      "type": "text/csv",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

# 📚 6. Bathymetry Item Example (COG)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "clinton-bathymetry-2022",
  "collection": "clinton-lake-hydrology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-95.47, 38.86, -95.27, 38.99],
  "properties": {
    "datetime": "2022-07-15T00:00:00Z",
    "kfm:parameter": "bathymetry",
    "kfm:units": "meters",
    "kfm:method": "multibeam",
    "kfm:provider": "USACE Kansas City District",
    "kfm:lineage": "etl/clinton-bathy-2022-v2",
    "kfm:quality": "A",
    "kfm:crs": "NAVD88",
    "kfm:hydro_region": "Clinton_Reservoir"
  },
  "assets": {
    "cog": {
      "href": "https://example.org/data/clinton/bathymetry_2022.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "checksum:sha256": "..."
    }
  }
}
```

---

# 🧩 7. PROV-O Lineage Mapping (Per Item)

Each STAC Item maps to:

### Entities
- `prov:Entity` = dataset / asset  

### Activities
- `prov:Activity` = ETL process  

### Agents
- `prov:Agent` = USACE, USGS, KDHE, KWO, KFM  

### Required relationships
- `prov:wasGeneratedBy`  
- `prov:wasAttributedTo`  
- `prov:used`  

---

# 🧠 8. CIDOC-CRM + GeoSPARQL + OWL-Time Mapping

### CIDOC Entities
- `E73 InformationObject` — dataset metadata  
- `E53 Place` — spatial footprint of Clinton Lake  
- `E7 Activity` — hydrologic or survey activities  
- `ObservationSeries` — time-series  

### CRM Properties
- `P7_took_place_at`  
- `P70_documents`  
- `P1_is_identified_by`  

### GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin`  
- `geo:asWKT`  

### OWL-Time
- `time:hasTime`  
- `time:hasBeginning`  
- `time:hasEnd`  

---

# 🛰 9. ETL → STAC → Graph Ingestion Workflow

```
Raw Data  
    ↓ extract  
Normalization → QA → Unit harmonization  
    ↓ transform  
COG/CSV/GeoJSON/NetCDF creation  
    ↓ asset-create  
STAC Item JSON creation  
    ↓ validate  
Graph ingestion  
    ↓  
Focus Mode v3 binding
```

Every transformation must be documented in  
`mcp/experiments/hydrology/clinton/*`.

---

# 🎯 10. Focus Mode v3 Integration

Focus Mode uses Clinton STAC Items to populate:

- Hydrology charts  
- Bathymetry overlays  
- Sedimentation timelines  
- Downstream DO/turbidity panels  
- Ecological status snapshots  
- Story Node context windows  

Selecting **“Clinton Lake”** automatically activates data filters:

- Items with `kfm:hydro_region = "Clinton_Reservoir"`  
- All bathymetry Items  
- Hydrology & WQ Items  
- Downstream Items  

---

# 📖 11. Story Node Integration

Story Nodes referencing Clinton Lake datasets include:

- **“Clinton Lake Through Time”**  
- **“Sediment Trends in the 2010–2022 Period”**  
- **“Downstream of Clinton Lake”**  

Linked via:

```json
{
  "rel": "uses-dataset",
  "target": "clinton-bathymetry-2010"
}
```

---

# 🚀 12. Expansion Roadmap

Planned STAC Items:

- UAV bathymetry photogrammetry (2026+)  
- 3D point-cloud STAC Items (`.las/.laz`)  
- HEC-RAS 2D hydrodynamic model output Items  
- Multi-reservoir comparative DoD datasets  
- Annual sediment core datasets  
- Glider-based WQ cross-sections  

---

# 🕰 13. Version History

- **v11.0.0 (2025-11-21):** Initial super-edition STAC Items index for Clinton Lake.

---

[⬅ Back to Clinton Lake STAC Collection](../README.md) • [⬅ Hydrology STAC Domain](../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

