---
title: "🚧 Kansas Frontier Matrix — WID (Water Injection Dredging) STAC Items Index (v11 Super-Edition)"
path: "data/stac/hydrology/wid/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Engineering Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/data-stac-hydro-wid-items-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-wid-items-index"
semantic_document_id: "kfm-stac-hydrology-wid-items-index"
doc_uuid: "urn:kfm:stac:hydrology:wid:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🚧 **Water Injection Dredging — STAC Items Index (v11 Super-Edition)**  
`data/stac/hydrology/wid/items/README.md`

**Purpose:**  
Serve as the complete domain-level index, metadata specification, ontology mapping, QA/QC  
framework, sensor schema standard, ETL lineage reference, and integration guide for  
**all Water Injection Dredging (WID) STAC Items** in the Kansas Frontier Matrix.

</div>

---

# 📘 0. Overview

This directory contains **all WID-specific STAC Items**, including:

- Turbidity & DO high-frequency sensors  
- ADCP density-current transects  
- WID plume geometry  
- Nutrient & chemistry samples  
- Barge operations logs  
- WID event summaries  
- Downstream DO/turbidity responses  
- Pre/post-WID comparative layers  
- Hydrodynamic model derivatives (future)  

These Items act as the atomic, machine-readable source for:

```
STAC → Neo4j Knowledge Graph → Focus Mode v3 → Story Node v3
```

---

# 🗂️ 1. Directory Layout (Authoritative)

```text
data/
└── stac/
    └── hydrology/
        └── wid/
            ├── collection.json
            └── items/
                ├── wid-2025-turbidity-b1.json
                ├── wid-2025-turbidity-b2.json
                ├── wid-2025-turbidity-b3.json
                ├── wid-2025-do-b1.json
                ├── wid-2025-do-b2.json
                ├── wid-2025-density-current.json
                ├── wid-2025-adcp-transect-01.json
                ├── wid-2025-adcp-transect-02.json
                ├── wid-2025-plume-geometry.json
                ├── wid-2025-nutrient-samples.json
                ├── wid-2025-operations-log.json
                ├── wid-2025-downstream-do.json
                ├── wid-2025-downstream-turbidity.json
                └── wid-2025-summary.json
```

---

# 🚧 2. WID STAC Item Categories

## ✔ 2.1 Turbidity Time-Series Items
- High-frequency (1–5 minute) NTU data  
- At stations B1, B2, B3  
- Used to detect plume passage & DO sag correlation  

## ✔ 2.2 DO Time-Series Items
- Dissolved oxygen  
- Minutes-level resolution  
- Tailwater oxygen sag monitoring  

## ✔ 2.3 ADCP Transects (Velocity Profiles)
- Horizontal density-current characterization  
- Plume height, velocity, shear  

## ✔ 2.4 Plume Geometry Items
- 2D polygons  
- Time-specific or composite  
- Generated via ADCP + turbidity sensors  

## ✔ 2.5 Nutrient Data Items
- TN, TP, NO₃, NH₄  
- Metals screening  
- Pre/post-WID nutrient delta  

## ✔ 2.6 Barge Operational Logs
- Jet pressure  
- Jet flow (L/s)  
- Nozzle depth  
- GPS track log  
- Operation start/stop windows  

## ✔ 2.7 Downstream Impact Items
- Downstream DO  
- Downstream turbidity  
- Downstream sediment response  

## ✔ 2.8 WID Experiment Summary Items
- Event metadata  
- Operational timeline  
- Sensor network summary  

---

# 📐 3. Required STAC Metadata (WID v11 Profile)

## ✔ Core STAC 1.0.0 fields
```
stac_version
type
id
collection
geometry
bbox
properties.datetime
assets
```

## ✔ Required WID `kfm:*` Fields

| Field | Description |
|------|-------------|
| `kfm:parameter` | turbidity, DO, adcp_velocity, plume_extent, nutrient, ops_log |
| `kfm:units` | NTU, mg/L, m/s, L/s, psi |
| `kfm:provider` | USACE, KWO, KFM |
| `kfm:method` | sonde, ADCP, lab, pressure-sensor |
| `kfm:site` | B1/B2/B3, transect ID, ops session ID |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | A/B/C/provisional |
| `kfm:hydro_region` | Tuttle_Creek, Tailwater, Downstream_Reaches |
| `kfm:project` | WID-2025 |
| `kfm:wid_phase` | Phase-1, Phase-2 |
| `kfm:ops_window` | operational window ID |

### Recommended fields:
- `kfm:crs`  
- `kfm:processing_history`  
- `kfm:barge_track_id`  
- `kfm:plume_confidence`  

---

# 🧪 4. Asset Types & Schemas

## ✔ Turbidity / DO → CSVW  
Columns:  
`timestamp, value, units, station, qc_flag, provenance_id`

## ✔ ADCP → CSV or NetCDF  
- velocity magnitude  
- velocity direction  
- transect geometry  

## ✔ Plume Geometry → GeoJSON  
Polygon representing plume footprint.

## ✔ Nutrients → CSV  
Lab sample data with site, depth, concentration.

## ✔ Operations Logs → CSV or JSON  
Operational metadata for the WID barge.

## ✔ COG Rasters (future)  
Hydrodynamic or plume propagation rasters.

## ✔ MP4 Videos (optional)  
Drone or underwater camera footage.

---

# 🧭 5. Example STAC Items

## 5.1 Turbidity — Station B1

```json
{
  "stac_version":"1.0.0",
  "type":"Feature",
  "id":"wid-2025-turbidity-b1",
  "collection":"wid-hydrology",
  "geometry":{"type":"Point","coordinates":[-96.6005,39.2758]},
  "bbox":[-96.601,39.275,-96.600,39.276],
  "properties":{
    "datetime":"2025-09-17T00:00:00Z",
    "kfm:parameter":"turbidity",
    "kfm:units":"NTU",
    "kfm:provider":"USACE",
    "kfm:method":"sonde",
    "kfm:site":"B1",
    "kfm:lineage":"etl/wid_turbidity_v3",
    "kfm:quality":"A",
    "kfm:hydro_region":"Tuttle_Creek_Reservoir",
    "kfm:project":"WID-2025",
    "kfm:wid_phase":"Phase-1"
  },
  "assets":{
    "csv":{
      "href":"https://example.org/wid2025/turbidity/B1.csv",
      "type":"text/csv",
      "roles":["data"]
    }
  }
}
```

---

## 5.2 ADCP — Primary Transect

```json
{
  "stac_version":"1.0.0",
  "type":"Feature",
  "id":"wid-2025-adcp-transect-01",
  "collection":"wid-hydrology",
  "geometry":{"type":"LineString","coordinates":[... ]},
  "bbox":[...],
  "properties":{
    "datetime":"2025-09-22T17:00:00Z",
    "kfm:parameter":"adcp_velocity",
    "kfm:units":"m/s",
    "kfm:provider":"USACE",
    "kfm:method":"adcp",
    "kfm:site":"transect-01",
    "kfm:lineage":"etl/wid_adcp_v1",
    "kfm:quality":"A",
    "kfm:hydro_region":"Tuttle_Creek_Reservoir",
    "kfm:project":"WID-2025",
    "kfm:wid_phase":"Phase-1"
  },
  "assets":{
    "csv":{
      "href":"https://example.org/wid2025/adcp/transect01.csv",
      "type":"text/csv",
      "roles":["data"]
    }
  }
}
```

---

## 5.3 Plume Geometry

```json
{
  "stac_version":"1.0.0",
  "type":"Feature",
  "id":"wid-2025-plume-extent",
  "collection":"wid-hydrology",
  "geometry":{"type":"Polygon","coordinates":[ ... ]},
  "bbox":[ ... ],
  "properties":{
    "datetime":"2025-09-22T18:00:00Z",
    "kfm:parameter":"plume_extent",
    "kfm:units":"none",
    "kfm:provider":"KFM-Analysis",
    "kfm:method":"sensor+adcp+interpolation",
    "kfm:lineage":"etl/wid_plume_v1",
    "kfm:quality":"A",
    "kfm:hydro_region":"Tuttle_Creek_Reservoir",
    "kfm:project":"WID-2025",
    "kfm:wid_phase":"Phase-1"
  },
  "assets":{
    "geojson":{
      "href":"https://example.org/wid2025/plume_extent.geojson",
      "type":"application/geo+json",
      "roles":["data"]
    }
  }
}
```

---

# 🧠 6. Ontology Mapping (CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O)

## CIDOC-CRM Entities  
- `E7 Activity` → WID event  
- `E73 InformationObject` → WID datasets  
- `E53 Place` → plume region, station, transect  
- `E3 ConditionState` → turbidity/DO states  
- `E39 Actor` → USACE personnel, monitoring teams  

## PROV-O  
- `prov:wasGeneratedBy` → ETL  
- `prov:used` → raw sensors/logs  
- `prov:wasAttributedTo` → USACE / KWO  

## GeoSPARQL  
- `geo:hasGeometry`  
- `geo:sfWithin`  

## OWL-Time  
- `time:Instant` for sensors  
- `time:Interval` for WID operational windows  

---

# 🛰 7. ETL → STAC → Graph Workflow

```
Raw WID data
    ↓ extract
QA/QC + timestamp harmonization
    ↓ transform
Generate assets (CSV, GeoJSON, NetCDF, COG)
    ↓ annotate-stac
Create STAC Items
    ↓ stac-validate
Ingest into Neo4j (CIDOC + GeoSPARQL)
    ↓
Activate in Focus Mode v3 + Story Nodes
```

ETL logs must be stored under:

```
mcp/experiments/hydrology/wid/
```

---

# 🎯 8. Focus Mode v3 Integration

- Displays turbidity & DO time-series  
- Highlights ADCP transects  
- Renders plume polygons  
- Shows operational timeline  
- Links WID data to downstream sediment/DO behavior  
- Integrates into reservoir hydrodynamic narrative flows  

---

# 📖 9. Story Node Integration

WID data fuels nodes like:

- **“The 2025 Density Current Experiment”**  
- **“Plume in Motion”**  
- **“A Reservoir Reacts to Innovation”**  
- **“Downstream of the WID Test”**  

Story Nodes reference Items using:

```json
{
  "rel": "uses-dataset",
  "target": "wid-2025-adcp-transect-01"
}
```

---

# 🚀 10. Expansion Roadmap

Future WID Items may include:

- 2026+ WID experiments  
- Hydrodynamic model NetCDF  
- Real-time plume prediction models  
- Enhanced nutrient‐sediment coupling datasets  
- Multi-sensor fusion turbidity grids  
- Drone-based plume mapping MP4/COG  
- 3D plume reconstructions  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial WID STAC Items Super-Edition created.

---

[⬅ Back to WID STAC Collection](../README.md) • [⬅ Hydrology STAC Domain](../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

