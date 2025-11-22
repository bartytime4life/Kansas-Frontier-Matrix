---
title: "🛰️ Kansas Frontier Matrix — Hydrology STAC Items Domain Index (v11 Super-Edition)"
path: "data/stac/hydrology/items/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-stac-hydrology-items-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active • Enforced"
doc_kind: "STAC Items Index"
intent: "stac-hydrology-items-domain-index"
semantic_document_id: "kfm-stac-hydrology-items-domain-index"
doc_uuid: "urn:kfm:stac:hydrology:items:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **Hydrology STAC Items — Domain-Wide Index (v11 Super-Edition)**  
`data/stac/hydrology/items/README.md`

**Purpose:**  
Serve as the **global STAC Items index** for the *entire hydrology domain* of the Kansas Frontier Matrix.  
This includes Items for **all reservoirs (Tuttle Creek, Milford, Perry, Clinton), rivers (Kansas, Blue, Smoky Hill), hydroclimate, flood operations, sedimentation, WID datasets, bathymetry, downstream impacts, and ecological datasets linked to hydrology**.  
Defines naming, metadata, assets, ontology mappings, ETL lineage, focus-mode integration, and dataset governance for all Items under `data/stac/hydrology/**/items/`.

</div>

---

# 📘 0. Overview

This directory acts as the **central reference hub** for all hydrology STAC Items across Kansas.  
Each Item describes:  

- **What** dataset it is (parameter, method, provider)  
- **Where** it belongs (reservoir, river reach, basin, statewide)  
- **When** the data applies (instant/interval)  
- **How** the data was produced (provenance, method, QA/QC)  
- **Which** assets are included (COG, GeoJSON, CSVW, NetCDF, MP4)  
- **Who** produced it (provider, ETL pipeline, sensor network)  
- **Why** the dataset matters (hydrologic/geomorphic/biological significance)

This index ensures **cross-collection consistency** and **domain-wide harmonization** for all hydrology STAC Items.

---

# 🗂️ 1. Domain-Wide Directory Layout

```text
data/
└── stac/
    └── hydrology/
        ├── README.md                 # domain-level STAC collection index
        ├── items/                    # THIS DIRECTORY (domain-wide Items hub)
        │   ├── statewide-hydroclimate.json
        │   ├── statewide-runoff-index.json
        │   ├── kansas-river-flood-1993.json
        │   ├── reservoirs-system-storage.json
        │   ├── sediment-budget-statewide.json
        │   ├── hydro-observation-network.json
        │   └── flood-inundation-curves.json
        ├── tuttle-creek/
        │   └── items/                # reservoir-level Items
        ├── milford/
        │   └── items/
        ├── perry/
        │   └── items/
        ├── clinton/
        │   └── items/
        ├── ecology/
        │   └── items/
        ├── bathymetry/
        │   └── items/
        └── sediment/
            └── items/
```

This README indexes items in **this domain-wide folder**, while reservoir-specific READMEs index their own items.

---

# 🛰️ 2. Domain-Wide Item Classes

These Items typically describe:

## ✔ Statewide Hydrology
- Hydroclimate drivers (precipitation, temperature)  
- Runoff indices  
- Drought severity (SPI, PDSI)  
- Large-scale flow anomalies  

## ✔ Flood Events
- Kansas River flood Items (1951, 1993, 2019)  
- Hydrographs + inundation curves  
- Floodplain extent layers  

## ✔ Multi-Reservoir System Items
- Storage-vs-elevation rasters  
- Systemwide sediment budgets  
- Multi-reservoir operational summaries  

## ✔ Statewide Sediment Items
- Sediment yield grids  
- Loess erosion indices  
- Soil loss estimates  
- Transport pathway composites  

## ✔ Hydrologic Observation Networks
- USGS gauges (statewide metadata)  
- Mesonet climate stations  
- Cross-basin hydrology observation domains  

---

# 📐 3. Required STAC Metadata Fields

Every Item MUST satisfy:

### Core STAC 1.0.0:

```
stac_version
type = "Feature"
id
collection
geometry
bbox
properties.datetime
assets
```

### Hydrology Domain `kfm:*` fields:

| Field | Description |
|--------|-------------|
| `kfm:parameter` | hydrologic variable |
| `kfm:units` | units |
| `kfm:method` | sensor/survey/algorithm |
| `kfm:provider` | data owner/host |
| `kfm:site` | location ID |
| `kfm:lineage` | ETL provenance chain |
| `kfm:quality` | QA/QC tier |
| `kfm:hydro_region` | Kansas, Big Blue, Kansas River, statewide, etc. |
| `kfm:project` | project anchor (Sedimentation, FloodHistory, WID, etc.) |

---

# 🌍 4. Asset Standards (Domain-Wide)

## ✔ Allowed asset types
- **COG (GeoTIFF)** → rasters (bathymetry, sedimentation, hydrodynamics, flood extents)  
- **GeoJSON** → vector layers (habitat, survey sites, inundation polygons)  
- **CSVW/CSV** → time-series hydrology datasets  
- **NetCDF** → climate/hydrodynamic models  
- **MP4** → visualization assets  

## ✔ Required asset fields
- `href`  
- `type`  
- `roles`  
- recommended: `checksum:sha256`, `title`, `description`

---

# 🧬 5. Example STAC Items (Domain Level)

### 5.1 Statewide Hydroclimate

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "statewide-hydroclimate-2000-2025",
  "collection": "hydrology-domain",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-102.05, 36.99, -94.59, 40.01],
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:parameter": "hydroclimate",
    "kfm:units": "various",
    "kfm:provider": "NOAA, Mesonet",
    "kfm:method": "climate-interpolation",
    "kfm:lineage": "etl/statewide_hydroclimate_v3",
    "kfm:quality": "A",
    "kfm:hydro_region": "Kansas",
    "kfm:project": "Hydrology-Core"
  },
  "assets": {
    "netcdf": {
      "href": "https://example.org/statewide/hydroclimate_2000_2025.nc",
      "type": "application/netcdf",
      "roles": ["data"]
    }
  }
}
```

---

### 5.2 Kansas River Flood Event (1993)

```json
{
  "id": "kansas-river-flood-1993",
  "type": "Feature",
  "stac_version": "1.0.0",
  "collection": "hydrology-domain",
  "geometry": { "type": "LineString", "coordinates": [...] },
  "properties": {
    "datetime": "1993-07-15T00:00:00Z",
    "kfm:parameter": "flood_hydrograph",
    "kfm:units": "cfs",
    "kfm:provider": "USGS NWIS",
    "kfm:method": "gauge_timeseries",
    "kfm:lineage": "etl/kansas-flood-1993-v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Kansas_River",
    "kfm:project": "FloodHistory"
  },
  "assets": {
    "hydrograph": {
      "href": "https://example.org/kansasriver/1993/hydrograph.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

# 🕸️ 6. DCAT, PROV-O, CIDOC-CRM, GeoSPARQL Crosswalk

## ✔ DCAT
- `id` → `dct:identifier`  
- `assets[].href` → `dcat:downloadURL`  
- `extent.spatial` → `dct:spatial`  

## ✔ PROV-O
- `prov:Entity` → STAC Item  
- `prov:Activity` → ETL pipeline  
- `prov:Agent` → provider agency  

## ✔ CIDOC-CRM
- `E73 InformationObject` → dataset  
- `E53 Place` → geometry entity  
- `E7 Activity` → hydrologic event or survey  
- `E3 ConditionState` → hydrologic state of system  

## ✔ GeoSPARQL
- `geo:hasGeometry`  
- `geo:sfWithin`  

---

# 🎯 7. Focus Mode v3 Integration

Domain-wide Items support:

- Multi-reservoir comparisons  
- Statewide drought/flood overlays  
- Hydrology corridor narratives  
- Reservoir-system analytics  
- Sediment transport comparison  

Focus Mode queries Items by:

- Place  
- Time  
- Parameter  
- Ecology group  
- Event (e.g., flood, WID, drought)

---

# 📖 8. Story Node v3 Integration

Hydrology STAC Items feed Story Nodes such as:

- **“The Great Kansas Floods”**  
- **“Sediment on the Move”**  
- **“Reservoir Systems: Milford → Tuttle → Perry → Clinton”**  
- **“Hydroclimate Cycles of the Great Plains”**

Nodes embed dataset references through:

```json
{
  "rel": "uses-dataset",
  "target": "kansas-river-flood-1993"
}
```

---

# 🚀 9. Expansion Roadmap

Upcoming Items (2025–2028):

- Climate projection rasters (CMIP6 downscaled)  
- Multi-reservoir hydrodynamic models (NetCDF/COG hybrid)  
- High-frequency sensor streams (MQTT → STAC)  
- Statewide inundation polygons  
- Cross-basin sediment delivery grids  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial super-edition creation of domain-wide hydrology STAC Items index.

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [📂 Data Home](../../README.md) • [🏠 KFM Master Guide](../../../../docs/reference/kfm_v11_master_documentation.md)
