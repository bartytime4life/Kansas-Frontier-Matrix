<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Metadata  
`data/processed/metadata/hydrology/`

**Mission:** Curate, document, and standardize all **processed hydrological data layers**  
powering Kansas Frontier Matrix’s time-aware exploration of rivers, watersheds, aquifers, and flood events.

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

This directory documents **metadata and provenance** for all hydrology datasets processed within  
the **Kansas Frontier Matrix (KFM)**. These data describe rivers, basins, aquifers, floods, and related  
water systems across Kansas — standardized for reproducibility, open-science integration, and temporal mapping.

Each dataset includes:
- STAC 1.0 metadata (`.json`)  
- Provenance information (source, license, collection date)  
- SHA-256 checksum linkage (`data/processed/checksums/hydrology/`)  
- Validation schema references (`data/processed/metadata/schema/`)  
- Reproducibility notes under the **Master Coder Protocol (MCP)**  

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/hydrology/
├── README.md
├── nhd_flowlines_ks_2020.json
├── watersheds_huc12_2019.json
├── fema_nfhl_2024.json
├── groundwater_levels_2025.json
└── thumbnails/
    ├── nhd_flowlines_ks_2020.png
    ├── watersheds_huc12_2019.png
    ├── fema_nfhl_2024.png
    └── groundwater_levels_2025.png
````

> **Note:**
> Each `.json` file follows the STAC specification, referencing the corresponding dataset under
> `data/processed/hydrology/` and its checksum entry under `data/processed/checksums/hydrology/`.

---

## 🌊 Hydrology Layers (Processed Assets)

| Dataset                              | Source             | Format  | Spatial Coverage | Temporal Range | Output                                                   |
| :----------------------------------- | :----------------- | :------ | :--------------- | :------------- | :------------------------------------------------------- |
| **Rivers & Streams (NHD Flowlines)** | USGS NHD / KS DASC | GeoJSON | Statewide        | 2020           | `data/processed/hydrology/nhd_flowlines_ks.geojson`      |
| **Watersheds (HUC-12)**              | USGS WBD / EPA     | GeoJSON | Sub-basins       | 2019           | `data/processed/hydrology/watersheds_huc12_ks.geojson`   |
| **Flood Hazard Zones (NFHL)**        | FEMA NFHL          | GeoJSON | County           | 2024           | `data/processed/hydrology/fema_nfhl_ks.geojson`          |
| **Groundwater Levels (NWIS)**        | USGS NWIS          | GeoJSON | Point (wells)    | 1950–2025      | `data/processed/hydrology/groundwater_levels_ks.geojson` |

All datasets are projected to **EPSG:4326 (WGS84)** and indexed in the project’s
STAC catalog (`data/stac/hydrology/`).

---

## 💾 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "watersheds_huc12_2019",
  "properties": {
    "title": "Kansas Hydrologic Unit Boundaries (HUC-12, 2019)",
    "datetime": "2019-06-01T00:00:00Z",
    "description": "Sub-basin hydrologic unit boundaries for Kansas (HUC-12, EPA WBD).",
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
    },
    "thumbnail": {
      "href": "thumbnails/watersheds_huc12_2019.png"
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity                  | Ontology Mapping                      | Example                          |
| :---------------------- | :------------------------------------ | :------------------------------- |
| River or Stream         | `E26_Physical_Feature` + `E53_Place`  | Kansas River reach               |
| Watershed               | `E27_Site` + `E53_Place`              | Smoky Hill Basin                 |
| Flood Event             | `E5_Event` + `P7_took_place_at`       | 1951 Kansas River Flood          |
| Groundwater Observation | `E16_Measurement` + OWL-Time interval | 2005–2025 well monitoring record |

Semantic alignment supports integration with CIDOC CRM and OWL-Time ontologies
for spatiotemporal reasoning in the KFM knowledge graph.

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make hydrology` → executes `src/pipelines/hydrology/hydrology_pipeline.py`

**Dependencies:**
`geopandas`, `rasterio`, `rio-cogeo`, `pandas`, `usgs`, `requests`, `pyproj`

**Steps:**

1. Download raw hydrology data from official APIs and archives.
2. Reproject to EPSG:4326 (WGS84) for cross-domain consistency.
3. Simplify geometries for efficient web rendering.
4. Generate GeoJSON and COG outputs.
5. Create thumbnails and STAC metadata entries.
6. Generate `.sha256` checksums for integrity tracking.
7. Validate metadata using JSON Schema and STAC CI checks.

---

## 🧮 Provenance & Validation

* **Checksums:** SHA-256 validation in `data/processed/checksums/hydrology/`
* **Licensing:** Public domain or CC-BY for derived layers
* **Validation:** JSON Schema + STAC 1.0.0 validation in CI/CD
* **Cross-links:** `data/sources/hydrology/*.json` documents source URLs and formats

---

## 🔗 Integration Points

| Component                             | Role                                             |
| :------------------------------------ | :----------------------------------------------- |
| `data/stac/hydrology/`                | STAC Items for discovery and catalog integration |
| `web/config/layers.json`              | Frontend map configuration for hydrology layers  |
| `src/graph/hydrology_nodes.py`        | Knowledge graph ingestion and relationship logic |
| `docs/architecture.md`                | Design documentation and data flow reference     |
| `data/processed/checksums/hydrology/` | Linked checksum files for integrity tracking     |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                         |
| :---------------------- | :----------------------------------------------------- |
| **Documentation-first** | README + STAC metadata per dataset                     |
| **Reproducibility**     | Deterministic pipelines with logged outputs            |
| **Open Standards**      | GeoJSON, COG, JSON Schema, STAC                        |
| **Provenance**          | Source URLs, processing logs, and checksums included   |
| **Auditability**        | CI-based metadata validation and checksum verification |

---

## 📅 Version History

| Version | Date       | Summary                                                                                            |
| :------ | :--------- | :------------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of hydrology metadata documentation (rivers, watersheds, floodplains, groundwater) |

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the Lifeblood of the Plains: Rivers, Floods, and Aquifers.”*
📍 [`data/processed/metadata/hydrology/`](.) · Integrated within the **Hydrology STAC Collection**

</div>
