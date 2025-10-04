<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Metadata  
`data/processed/metadata/hydrology/`

**Mission:** Curate, document, and standardize all **processed hydrology datasets**  
powering Kansas Frontier Matrix’s temporal exploration of rivers, watersheds, aquifers,  
and flood records.

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

This directory contains metadata and provenance documentation for all **hydrology-related processed datasets**  
within the Kansas Frontier Matrix (KFM). These datasets underpin the system’s interactive **map + timeline**,  
linking Kansas’s rivers, watersheds, floods, and groundwater observations through time.

Each layer here is:
- Stored in **open formats** (`GeoJSON`, `COG`, `CSV`)  
- Indexed in the project’s **STAC catalog** (`data/stac/hydrology/`)  
- Processed via reproducible **Makefile + Python pipelines**  
- Tracked with **SHA-256 checksums** for provenance  

---

## 🗂️ Directory Layout

```

data/
└── processed/
├── hydrology/                     # Processed hydrology data (GeoJSON, CSV, COG)
│   ├── nhd_flowlines_ks.geojson
│   ├── watersheds_huc12_ks.geojson
│   ├── fema_nfhl_ks.geojson
│   ├── groundwater_levels_ks.geojson
│   ├── flood_events_ks.geojson
│   └── checksums/                 # SHA-256 hash sidecars for integrity
│
├── metadata/
│   ├── hydrology/                 # ← This directory (metadata, STAC, schema docs)
│   │   ├── README.md
│   │   ├── ks_watersheds_huc12_2019.json
│   │   ├── ks_fema_nfhl_2024.json
│   │   └── ks_groundwater_levels_2025.json
│   └── schema/                    # Shared JSON Schemas
│       ├── hydrology.schema.json
│       └── examples/
│           └── hydrology_example.json
│
└── stac/
└── hydrology/                 # STAC Items / Collections
├── ks_hydrology_collection.json
├── ks_watersheds_huc12_2019.json
└── ks_flood_events_2025.json

````

> **Note:** Every hydrology layer has an associated STAC Item and checksum;  
> this ensures full traceability and CI-validated reproducibility.

---

## 🗺️ Hydrology Layers (Processed Assets)

| Layer | Source | Format | Spatial Unit | Temporal Coverage | Output |
|-------|---------|---------|---------------|------------------|---------|
| **Rivers & Streams (NHD Flowlines)** | USGS NHD / KS DASC | GeoJSON | Statewide | 2020 | `data/processed/hydrology/nhd_flowlines_ks.geojson` |
| **Watersheds (HUC-12)** | USGS WBD / EPA | GeoJSON | Sub-basins | 2019 | `data/processed/hydrology/watersheds_huc12_ks.geojson` |
| **Flood Hazard Zones (NFHL)** | FEMA NFHL | GeoJSON | County | 2024 | `data/processed/hydrology/fema_nfhl_ks.geojson` |
| **Groundwater Levels (NWIS)** | USGS NWIS API | CSV → GeoJSON | Wells | 1950–2025 | `data/processed/hydrology/groundwater_levels_ks.geojson` |
| **Major Flood Events** | NOAA / USGS | CSV + GeoJSON | Event Points | 1900–2025 | `data/processed/hydrology/flood_events_ks.geojson` |

All layers use **EPSG 4326 (WGS84)** and are indexed under `data/stac/hydrology/`.

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
````

---

## 🧩 Semantic & Ontological Alignment

| Entity                  | Ontology Mapping                      | Example                 |
| :---------------------- | :------------------------------------ | :---------------------- |
| River segment           | `E26_Physical_Feature` + `E53_Place`  | Arkansas River reach    |
| Watershed               | `E27_Site` + `E53_Place`              | Smoky Hill Basin        |
| Flood Event             | `E5_Event` + `P7_took_place_at`       | 1951 Kansas River Flood |
| Observation (flow/well) | `E16_Measurement` + OWL-Time interval | NWIS groundwater record |

Semantic grounding allows graph-level queries such as
*“show hydrologic events overlapping the 1930s Dust Bowl era.”*

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make hydrology` → runs `src/pipelines/hydrology/hydrology_pipeline.py`

**Dependencies:**
`geopandas`, `rasterio`, `rio-cogeo`, `requests`, `usgs`, `pandas`, `pyproj`

**Steps:**

1. Fetch data (USGS, EPA, NOAA, FEMA)
2. Reproject geometries → EPSG 4326
3. Simplify shapes for web use
4. Merge multi-county shapefiles → statewide layers
5. Derive flow grids / centroids
6. Export GeoJSON + generate STAC
7. Compute `.sha256` hash for provenance

Logs + hashes are stored in `data/processed/checksums/hydrology/`.

---

## 🧮 Provenance & Validation

* **Checksums:** SHA-256 sidecars for all outputs
* **Licensing:** USGS/EPA/FEMA → Public Domain; derived layers → CC-BY 4.0
* **Validation:** JSON Schema + STAC validator in CI/CD
* **Cross-links:** `data/sources/hydrology/*.json` maintains source records

---

## 🔗 Integration Points

| Component                      | Role                                   |
| ------------------------------ | -------------------------------------- |
| `data/stac/hydrology/`         | STAC Items & Collections for discovery |
| `web/config/layers.json`       | Frontend MapLibre layer configuration  |
| `src/graph/hydrology_nodes.py` | Graph import and relationships         |
| `docs/architecture.md`         | Pipeline and system design reference   |
| `data/processed/hazards/`      | Linked flood/drought hazard layers     |

---

## 🧠 MCP Compliance Summary

| Principle               | Implementation                                   |
| ----------------------- | ------------------------------------------------ |
| **Documentation-first** | README + STAC per layer                          |
| **Reproducibility**     | Make + Python pipelines logged deterministically |
| **Open Formats**        | GeoJSON, CSV, COG only                           |
| **Provenance**          | URLs + checksums tracked                         |
| **Auditability**        | CI validation via STAC and hash tests            |

---

## 📅 Version History

| Version | Date       | Summary                                                                           |
| :------ | :--------- | :-------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial hydrology metadata release — rivers, watersheds, floodplains, groundwater |

---

## 📎 References

* [USGS National Hydrography Dataset (NHD)](https://www.usgs.gov/national-hydrography)
* [EPA Watershed Boundary Dataset (WBD)](https://www.epa.gov/waterdata/watershed-boundary-dataset)
* [FEMA National Flood Hazard Layer (NFHL)](https://msc.fema.gov/portal/home)
* [USGS NWIS Water Data](https://waterdata.usgs.gov/nwis)
* [NOAA Storm Events Archive](https://www.ncei.noaa.gov/stormevents/)
* [Master Coder Protocol Docs](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Tracing the Flow of Time and Water Across the Plains.”*
📍 [`data/processed/metadata/hydrology/`](.) · 🔗 Integrated with the STAC Data Catalog Layer

</div>
