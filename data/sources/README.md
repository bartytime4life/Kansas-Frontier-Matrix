<div align="center">

# 🧩 Kansas Frontier Matrix — Source Manifests  
`data/sources/`

**Mission:** Document and manage all **external data sources** used within the  
Kansas Frontier Matrix (KFM) — capturing origin, licensing, access methods,  
and provenance for every dataset integrated into the system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/sources/` directory contains **JSON manifest files** that define  
all raw and reference data sources used throughout the KFM pipelines.  

Each manifest provides:
- **Dataset identification** and versioning  
- **Source URLs** and access endpoints  
- **Licensing and usage terms**  
- **Data type, schema, and temporal coverage**  
- **Provenance details** linking raw inputs to processed outputs  

These manifests serve as the **authoritative source registry** for all external data dependencies,  
ensuring reproducibility and transparency across the project’s entire ETL ecosystem.

---

## 🗂️ Directory Layout

```bash
data/sources/
├── README.md
├── terrain/             # USGS 3DEP, Kansas DASC elevation data
│   ├── ks_lidar_2018_2020.json
│   └── usgs_3dep_dem.json
├── hydrology/           # NHD, WBD, and FEMA NFHL datasets
│   ├── usgs_nhd_flowlines.json
│   ├── epa_wbd_huc12.json
│   └── fema_nfhl.json
├── landcover/           # NLCD, USDA CDL, vegetation maps
│   ├── nlcd_1992_2021.json
│   └── usda_cdl_2020.json
├── climate/             # Daymet, NOAA, Drought Monitor
│   ├── nasa_daymet_1980_2024.json
│   ├── noaa_normals_1991_2020.json
│   └── usdm_drought_monitor.json
├── hazards/             # Tornado, wildfire, and flood data
│   ├── noaa_storm_events.json
│   ├── usgs_wildfire_perimeters.json
│   └── fema_flood_events.json
├── tabular/             # Census, USDA, BEA, BLS data
│   ├── us_census_population.json
│   ├── usda_agriculture_production.json
│   └── bea_economic_indicators.json
└── text/                # Historical documents, OCR sources, transcripts
    ├── loc_chronicling_america.json
    ├── kshs_oral_histories.json
    └── yale_avalon_treaties.json
````

> **Note:**
> Each manifest is a machine-readable `.json` file describing data origin,
> licensing, update cadence, and provenance for reproducibility.

---

## 🧩 Source Manifest Example

### Example: `usgs_3dep_dem.json`

```json
{
  "id": "usgs_3dep_dem",
  "title": "USGS 3D Elevation Program (3DEP) LiDAR DEM",
  "provider": "USGS",
  "description": "Nationwide LiDAR-derived DEMs providing 1-meter elevation data.",
  "endpoint": "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer",
  "access_method": "REST API",
  "license": "Public Domain (US Government)",
  "data_type": "raster",
  "format": "GeoTIFF",
  "spatial_coverage": "Kansas, USA",
  "temporal_coverage": "2018–2020",
  "update_frequency": "On Demand",
  "last_verified": "2025-10-04",
  "checksum": null,
  "linked_pipeline": "terrain_pipeline.py",
  "notes": "Used as source for `ks_1m_dem_2018_2020.tif`."
}
```

---

## ⚙️ Source Manifest Workflow

**Makefile target:**

```bash
make sources
```

**Manual validation:**

```bash
python src/utils/validate_sources.py data/sources/
```

**Workflow Steps:**

1. Define or update source manifests for new datasets.
2. Validate schema compliance (`source.schema.json`).
3. Fetch raw data via automated ETL pipelines.
4. Store metadata in `data/sources/` for future traceability.
5. Link processed outputs to their source manifests and STAC Items.

---

## 🧾 Manifest Schema

| Field               | Description                            | Example                                 |
| :------------------ | :------------------------------------- | :-------------------------------------- |
| `id`                | Unique identifier for the data source. | `usgs_3dep_dem`                         |
| `title`             | Human-readable name.                   | `USGS 3DEP DEM`                         |
| `provider`          | Organization providing the data.       | `USGS`                                  |
| `endpoint`          | URL or API endpoint.                   | `https://elevation.nationalmap.gov/...` |
| `license`           | Data usage license.                    | `Public Domain (US Govt)`               |
| `data_type`         | Type of dataset.                       | `raster`, `vector`, `tabular`, `text`   |
| `format`            | File format.                           | `GeoTIFF`, `CSV`, `JSONL`               |
| `spatial_coverage`  | Geographic extent.                     | `Kansas, USA`                           |
| `temporal_coverage` | Time range.                            | `2018–2020`                             |
| `update_frequency`  | Refresh interval.                      | `Annual`, `Monthly`, `On Demand`        |
| `linked_pipeline`   | Associated ETL script.                 | `terrain_pipeline.py`                   |
| `notes`             | Optional remarks or usage context.     | `Used for DEM generation.`              |

---

## 🧩 Integration with KFM Pipelines

| Linked Component                         | Function                                                |
| :--------------------------------------- | :------------------------------------------------------ |
| `src/pipelines/*`                        | Uses source manifests to fetch and register input data. |
| `data/processed/`                        | Outputs derived from these sources.                     |
| `data/checksums/`                        | Verifies raw and processed data integrity.              |
| `data/processed/metadata/`               | STAC metadata links back to source manifests.           |
| `.github/workflows/sources-validate.yml` | CI/CD workflow validating schema and availability.      |

---

## 🧹 Maintenance & Versioning

* **Add new sources:** Create a new JSON manifest following `source.schema.json`.
* **Update verification date:** Change `last_verified` after confirming source availability.
* **Deprecate sources:** Mark outdated sources with `"status": "deprecated"`.
* **Revalidate periodically:** Run `make sources-validate` to test URLs and schema.

**Cleanup command:**

```bash
make clean-sources
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                             |
| :---------------------- | :------------------------------------------------------------------------- |
| **Documentation-first** | Each dataset source is fully documented in a JSON manifest.                |
| **Reproducibility**     | Manifest-driven ETL ensures repeatable and deterministic data ingestion.   |
| **Open Standards**      | JSON + JSON Schema compliant; STAC-linked provenance.                      |
| **Provenance**          | Each manifest establishes the link between raw data and processed outputs. |
| **Auditability**        | Sources are versioned, validated, and CI-tested automatically.             |

---

## 📎 Related Directories

| Path                       | Description                                         |
| :------------------------- | :-------------------------------------------------- |
| `data/raw/`                | Immutable raw data downloaded from defined sources. |
| `data/processed/`          | Cleaned and validated outputs derived from sources. |
| `data/processed/metadata/` | STAC metadata for processed datasets.               |
| `data/checksums/`          | Validation hashes for source and processed data.    |
| `src/pipelines/`           | ETL scripts referenced by source manifests.         |

---

## 📅 Version History

| Version | Date       | Summary                                                      |
| :------ | :--------- | :----------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial creation of source manifest directory documentation. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Dataset Has a Story — and Every Story Starts with a Source.”*
📍 [`data/sources/`](.) · Repository of all raw data origins and provenance manifests powering KFM pipelines.

</div>
