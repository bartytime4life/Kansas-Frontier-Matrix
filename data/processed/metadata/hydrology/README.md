<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Metadata  
`data/processed/metadata/hydrology/`

**Mission:** Curate, document, and standardize all **processed hydrology datasets**  
powering Kansas Frontier Matrix’s time-aware analysis of rivers, watersheds, floods, and aquifers.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains metadata for all **hydrology-related processed datasets**  
within the **Kansas Frontier Matrix (KFM)** project.  

These datasets describe Kansas’s surface and groundwater systems —  
rivers, watersheds, aquifers, flood zones, and historic events — standardized for  
reproducibility, STAC interoperability, and MCP documentation compliance.

Each dataset includes:
- STAC-compliant metadata (`.json`)
- Provenance records (`.sha256` checksums, source URLs, licenses)
- Validated schema definitions
- Processing lineage documented in `src/pipelines/hydrology/`

---

## 🗂️ Directory Layout

```bash
data/
└── processed/
    ├── hydrology/                     # Processed hydrology layers (GeoJSON, CSV, COG)
    │   ├── nhd_flowlines_ks.geojson
    │   ├── watersheds_huc12_ks.geojson
    │   ├── fema_nfhl_ks.geojson
    │   ├── groundwater_levels_ks.geojson
    │   ├── flood_events_ks.geojson
    │   └── checksums/                 # SHA-256 sidecars for data integrity
    │
    ├── metadata/
    │   ├── hydrology/                 # ← This directory (metadata + STAC)
    │   │   ├── README.md
    │   │   ├── ks_watersheds_huc12_2019.json
    │   │   ├── ks_fema_nfhl_2024.json
    │   │   └── ks_groundwater_levels_2025.json
    │   └── schema/                    # JSON Schemas for validation
    │       ├── hydrology.schema.json
    │       └── examples/
    │           └── hydrology_example.json
    │
    └── stac/
        └── hydrology/                 # STAC Items & Collections
            ├── ks_hydrology_collection.json
            ├── ks_watersheds_huc12_2019.json
            └── ks_flood_events_2025.json
````

> **Note:** Each hydrology dataset is represented by a STAC Item under
> `data/stac/hydrology/` and validated automatically in CI workflows.

---

## 🗺️ Hydrology Layers (Processed Assets)

| Layer                                | Source             | Format        | Spatial Unit | Temporal Coverage | Output                                                   |
| :----------------------------------- | :----------------- | :------------ | :----------- | :---------------- | :------------------------------------------------------- |
| **Rivers & Streams (NHD Flowlines)** | USGS NHD / KS DASC | GeoJSON       | Statewide    | 2020              | `data/processed/hydrology/nhd_flowlines_ks.geojson`      |
| **Watersheds (HUC-12)**              | USGS WBD / EPA     | GeoJSON       | Sub-basins   | 2019              | `data/processed/hydrology/watersheds_huc12_ks.geojson`   |
| **Flood Hazard Zones (NFHL)**        | FEMA NFHL          | GeoJSON       | County       | 2024              | `data/processed/hydrology/fema_nfhl_ks.geojson`          |
| **Groundwater Levels (NWIS)**        | USGS NWIS API      | CSV → GeoJSON | Wells        | 1950-2025         | `data/processed/hydrology/groundwater_levels_ks.geojson` |
| **Major Flood Events**               | NOAA / USGS        | CSV + GeoJSON | Event Points | 1900-2025         | `data/processed/hydrology/flood_events_ks.geojson`       |

All files are in **EPSG:4326 (WGS84)** and discoverable via the project’s STAC catalog.

---

## 💾 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_watersheds_huc12_2019",
  "properties": {
    "title": "Kansas Watershed Boundaries (HUC-12, 2019)",
    "datetime": "2019-06-01T00:00:00Z",
    "description": "Hydrologic units delineating Kansas sub-basins (USGS WBD).",
    "proj:epsg": 4326,
    "themes": ["hydrology", "watersheds"],
    "license": "Public Domain (USGS/EPA)",
    "providers": [
      {"name": "USGS", "roles": ["producer"]},
      {"name": "EPA WBD", "roles": ["licensor"]},
      {"name": "Kansas DASC", "roles": ["processor"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../hydrology/watersheds_huc12_ks.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity                  | Ontology Mapping                      | Example                 |
| :---------------------- | :------------------------------------ | :---------------------- |
| River Segment           | `E26_Physical_Feature` + `E53_Place`  | Arkansas River reach    |
| Watershed               | `E27_Site` + `E53_Place`              | Smoky Hill Basin        |
| Flood Event             | `E5_Event` + `P7_took_place_at`       | 1951 Kansas River Flood |
| Observation (flow/well) | `E16_Measurement` + OWL-Time interval | NWIS groundwater record |

Semantic mappings ensure hydrology layers integrate seamlessly
with the Neo4j knowledge graph for timeline and spatial queries.

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make hydrology` → executes `src/pipelines/hydrology/hydrology_pipeline.py`

**Dependencies:**
`geopandas`, `rasterio`, `rio-cogeo`, `requests`, `usgs`, `pandas`, `pyproj`

**Steps:**

1. Fetch data via APIs (USGS, EPA, NOAA, FEMA)
2. Harmonize projections → EPSG:4326
3. Simplify geometries for web rendering
4. Merge regional datasets → statewide composite layers
5. Derive basin centroids or flow grids
6. Export GeoJSON and generate STAC items
7. Compute `.sha256` checksums for integrity

Logs, timestamps, and hashes are maintained under
`data/processed/checksums/hydrology/`.

---

## 🧮 Provenance & Validation

* **Checksums:** SHA-256 validation for every artifact
* **Licensing:** Public Domain (USGS/EPA/FEMA); derived layers → CC-BY 4.0
* **Validation:** JSON Schema + STAC validation in CI
* **Cross-referenced:** Source metadata at `data/sources/hydrology/`

---

## 🔗 Integration Points

| Component                      | Role                                   |
| :----------------------------- | :------------------------------------- |
| `data/stac/hydrology/`         | STAC Items & Collections for discovery |
| `web/config/layers.json`       | Frontend MapLibre configuration        |
| `src/graph/hydrology_nodes.py` | Knowledge graph ingestion logic        |
| `docs/architecture.md`         | Architecture reference for ETL         |
| `data/processed/hazards/`      | Linked drought/flood hazard overlays   |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                         |
| :---------------------- | :----------------------------------------------------- |
| **Documentation-first** | All hydrology layers documented via README + STAC      |
| **Reproducibility**     | Makefile + Python pipelines with deterministic outputs |
| **Open Formats**        | GeoJSON, CSV, COG                                      |
| **Provenance**          | URLs, timestamps, checksums                            |
| **Auditability**        | Continuous STAC + checksum validation                  |

---

## 📅 Version History

| Version | Date       | Summary                                                                               |
| :------ | :--------- | :------------------------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial hydrology metadata release — rivers, watersheds, floodplains, and groundwater |

---

## 📎 References

* [USGS National Hydrography Dataset (NHD)](https://www.usgs.gov/national-hydrography)
* [EPA Watershed Boundary Dataset (WBD)](https://www.epa.gov/waterdata/watershed-boundary-dataset)
* [FEMA National Flood Hazard Layer (NFHL)](https://msc.fema.gov/portal/home)
* [USGS NWIS Water Data](https://waterdata.usgs.gov/nwis)
* [NOAA Storm Events Archive](https://www.ncei.noaa.gov/stormevents/)
* [Master Coder Protocol Templates](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Tracing the Flow of Time and Water Across the Plains.”*
📍 [`data/processed/metadata/hydrology/`](.) · Part of the **STAC Data Catalog Layer**

</div>
