---
title: "🚧 Kansas Frontier Matrix — Water Injection Dredging (WID) STAC Collection (v11 Super-Edition)"
path: "data/stac/hydrology/wid/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual • Hydrology & Engineering Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-wid-index-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Collection Index"
intent: "stac-hydrology-wid-index"
semantic_document_id: "kfm-stac-hydrology-wid-index"
doc_uuid: "urn:kfm:stac:hydrology:wid:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public-Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🚧 **Water Injection Dredging (WID) — Hydrology STAC Collection (v11 Super-Edition)**  
`data/stac/hydrology/wid/README.md`

**Purpose:**  
Provide the **complete metadata, ontology, and dataset architecture** for the Water Injection  
Dredging (WID) domain in the Kansas Frontier Matrix, including bathymetry context,  
density-current sediment transport, turbidity/DO high-frequency sensors, plume geometry, ADCP  
transects, nutrient sampling, barge operations logs, and downstream ecological response.

</div>

---

# 📘 0. Overview

The **WID STAC Collection** encodes all datasets associated with **Water Injection Dredging**  
experiments and modeling within Kansas reservoirs (starting with **Tuttle Creek WID 2025**).

This includes:

- WID barge operations  
- Jet pressure/flow logs  
- Density-current formation and transport  
- Turbidity time-series (1-sec → 5-min)  
- Dissolved oxygen (DO) monitoring  
- ADCP plume velocity transects  
- Plume geometry polygons (2D)  
- Vertical turbidity profiles  
- Nutrient + chemical samples  
- Upstream/downstream monitoring (TSS, clarity, DO)  
- Environmental compliance thresholds  
- Bathymetry tie-in to WID flowpaths  
- Hydrodynamic model outputs (future)  
- Pre- and post-WID comparisons  

This domain acts as the **experimental hydrodynamics branch** of the KFM hydrology system.

---

# 🗂 1. Directory Layout (Canonical)

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

# 🧭 2. WID Dataset Themes

## ✔ 2.1 WID Barge Operations  
- Jet pressure  
- Flow rates  
- Injection depth  
- Barge GPS path  
- Operational “windows” (start/stop)

## ✔ 2.2 Turbidity Sensors  
- B1/B2/B3 stations  
- 1–5 minute intervals  
- NTU + QA/QC  
- Vertical profiles

## ✔ 2.3 DO Sensors  
- High-frequency DO sag monitoring  
- Hypolimnetic signal interpretation  
- Tailwater and downstream DO chains

## ✔ 2.4 ADCP Density-Current Transects  
- Velocity magnitude/direction  
- Shear + turbulence indicators  
- Transect geometry (line)  

## ✔ 2.5 Plume Geometry  
- 2D plume polygons  
- Maximum extent  
- Time-varying plume outlines (future)

## ✔ 2.6 Nutrient + Chem Sampling  
- TN/TP  
- Metals (screening)  
- Sediment-bound nutrient shifts  
- Lab metadata

## ✔ 2.7 Downstream Effects  
- DO  
- Turbidity  
- TSS  
- Fish/mussel response signals (linked via ecology STAC)

---

# 📐 3. Required STAC Metadata (WID v11 Profile)

## Core STAC Fields
```
stac_version = "1.0.0"
type = "Feature"
id
collection = "wid-hydrology"
geometry
bbox
properties.datetime
assets
```

## Required WID `kfm:*` Metadata

| Field | Meaning |
|-------|---------|
| `kfm:parameter` | turbidity, DO, adcp_velocity, plume_extent, jet_flow |
| `kfm:units` | NTU, mg/L, m/s, none, L/s, psi |
| `kfm:provider` | USACE, KWO, KFM sensors |
| `kfm:method` | sonde, ADCP, lab, pressure transducers |
| `kfm:site` | B1/B2/B3, transect ID, barge log ID |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | A/B/C/Provisional |
| `kfm:hydro_region` | Tuttle_Creek_Reservoir, Tailwater, etc. |
| `kfm:project` | WID-2025 |
| `kfm:wid_phase` | Phase-1, Phase-2 |
| `kfm:wid_operation_id` | Operation session code |

## Recommended
- `kfm:crs`  
- `kfm:processing_history`  
- `kfm:barge_track_id`  

---

# 🗃 4. Asset Types

## ✔ Turbidity / DO Sensors → **CSVW**
Columns:
`timestamp, value, units, station, qc_flag, provenance_id`

## ✔ ADCP Data → **CSV or NetCDF**  
- Transects  
- Velocity grids  

## ✔ Plume Geometry → **GeoJSON**  
- Polygons or multi-polygons  

## ✔ Operations Log → **CSV / JSON**  
- Jet pressure/flow  
- Movement & timestamps  

## ✔ Raster Products → **COG (future)**  
- Hydrodynamic model fields  
- Density-current staging  

## ✔ Media → **MP4 (optional)**  
- Barge deck cams  
- Drone plume captures  

---

# 🧪 5. Example STAC Items

## 5.1 Turbidity Sensor B1

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "wid-2025-turbidity-b1",
  "collection": "wid-hydrology",
  "geometry": { "type": "Point", "coordinates": [-96.6005, 39.2758] },
  "bbox": [-96.601, 39.275, -96.600, 39.276],
  "properties": {
    "datetime": "2025-09-17T00:00:00Z",
    "kfm:parameter": "turbidity",
    "kfm:units": "NTU",
    "kfm:provider": "USACE",
    "kfm:method": "sonde",
    "kfm:site": "B1",
    "kfm:lineage": "etl/wid2025_turbidity_v3",
    "kfm:quality": "A",
    "kfm:hydro_region": "Tuttle_Creek_Reservoir",
    "kfm:project": "WID-2025",
    "kfm:wid_phase": "Phase-1"
  },
  "assets": {
    "csv": {
      "href": "https://example.org/wid2025/turbidity/B1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

## 5.2 ADCP Density-Current Transect

```json
{
  "stac_version":"1.0.0",
  "type":"Feature",
  "id":"wid-2025-adcp-transect-01",
  "collection":"wid-hydrology",
  "geometry":{ "type":"LineString", "coordinates":[ ... ] },
  "bbox":[ ... ],
  "properties":{
    "datetime":"2025-09-22T17:00:00Z",
    "kfm:parameter":"adcp_velocity",
    "kfm:units":"m/s",
    "kfm:provider":"USACE",
    "kfm:method":"adcp",
    "kfm:site":"transect-01",
    "kfm:lineage":"etl/wid_adcp2025_v1",
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

## 5.3 Plume Geometry Polygon

```json
{
  "stac_version":"1.0.0",
  "type":"Feature",
  "id":"wid-2025-plume-geometry",
  "collection":"wid-hydrology",
  "geometry":{ "type":"Polygon", "coordinates":[ ... ] },
  "bbox":[ ... ],
  "properties":{
    "datetime":"2025-09-22T18:00:00Z",
    "kfm:parameter":"plume_extent",
    "kfm:units":"none",
    "kfm:provider":"KFM-Analysis",
    "kfm:method":"sonde+adcp+interpolation",
    "kfm:lineage":"etl/wid-plume-extent_v1",
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

# 🧠 6. Ontology Mapping (CIDOC-CRM + GeoSPARQL + OWL-Time + PROV-O)

## CIDOC-CRM
- `E7 Activity` → WID dredging operation  
- `E73 InformationObject` → turbidity/DO datasets, ADCP files  
- `E53 Place` → plume geometry, B1/B2/B3 sites  
- `E3 ConditionState` → reservoir turbidity/DO state  
- `E39 Actor` → USACE, KWO, KFM  

## GeoSPARQL  
- `geo:hasGeometry`  
- `geo:sfWithin` (reservoir, plume region)  
- `geo:asWKT`

## OWL-Time  
- `time:Instant` for sensor data  
- `time:Interval` for WID operational window  

## PROV-O  
- `prov:wasGeneratedBy` → ETL pipeline  
- `prov:used` → raw sensors / logs  
- `prov:wasAttributedTo` → agency/lab  

---

# 🔬 7. ETL → STAC → Graph Pipeline

```
Raw WID Inputs (sensors, ADCP, logs, lab samples)
       ↓ extract
Harmonize units + timestamps + stations
       ↓ transform
Generate assets (CSV, GeoJSON, COG, NetCDF)
       ↓ annotate-stac
Create STAC Items (*.json)
       ↓ stac-validate
Ingest into Neo4j (CIDOC + GeoSPARQL + OWL-Time)
       ↓
Expose to Focus Mode v3 + Story Node v3
```

ETL lineage must be stored in:

```
mcp/experiments/hydrology/wid/
```

---

# 🎯 8. Focus Mode v3 Integration

When focusing on **WID 2025**:

- Loads turbidity & DO chains (B1/B2/B3)  
- Shows ADCP plume slices  
- Renders plume polygons over bathymetry  
- Loads operations log (timeline)  
- Highlights downstream response  
- Pulls connected sedimentation & bathymetry Items  

Focus Mode filter logic:

```
kfm:project = "WID-2025"
place ∈ [Tuttle_Creek_Reservoir, Tailwater]
parameter ∈ [turbidity, DO, adcp_velocity, plume_extent, wid_ops]
```

---

# 📖 9. Story Node v3 Integration

WID datasets support nodes like:

- **“The 2025 Density-Current Experiment”**  
- **“A Reservoir Reacts to Innovation”**  
- **“Plume in Motion: The Deepwater Path”**  
- **“Downstream of the WID Experiment”**  

Nodes embed Items via:

```json
{
  "rel": "uses-dataset",
  "target": "wid-2025-turbidity-b1"
}
```

---

# 🚀 10. Expansion Roadmap

Future WID STAC Items:

- 2026+ WID experiments (if repeated)  
- Hydrodynamic model outputs (2D/3D NetCDF)  
- Quasi-real-time plume prediction model datasets  
- Multi-sensor fusion turbidity fields  
- ADCP → ML velocity interpolations  
- WID environmental compliance datasets  
- UAV bathymetry and plume imagery  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial WID STAC Collection Super-Edition created.

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [📂 Data Home](../../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

