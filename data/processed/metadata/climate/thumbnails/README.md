<div align="center">

# 🖼️ Kansas Frontier Matrix — Climate Thumbnails  
`data/processed/metadata/climate/thumbnails/`

**Mission:** Store and describe **preview thumbnails** for processed climate datasets  
to support quick visualization in the Kansas Frontier Matrix web app and documentation.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **thumbnail preview images** for the processed climate datasets  
documented in `data/processed/metadata/climate/`.  

Thumbnails are lightweight **static PNGs** automatically generated during the ETL process  
(`make climate`) to provide visual summaries of datasets for the KFM web interface,  
the documentation site, and the STAC catalog.

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/climate/thumbnails/
├── README.md
├── daymet_1980_2024.png
├── noaa_normals_1991_2020.png
└── drought_monitor_2000_2025.png
````

> **Note:** Filenames correspond directly to dataset IDs from
> `data/processed/metadata/climate/`.
> Each thumbnail is referenced by a `"thumbnail"` asset in the associated STAC metadata JSON.

---

## 🧰 Thumbnail Specifications

| Dataset                              | Thumbnail File                  | Source Layer                                            | Description                                               |
| :----------------------------------- | :------------------------------ | :------------------------------------------------------ | :-------------------------------------------------------- |
| **Daymet (1980–2024)**               | `daymet_1980_2024.png`          | `data/processed/climate/daymet_1980_2024.tif`           | Map preview of gridded temperature and precipitation data |
| **NOAA Climate Normals (1991–2020)** | `noaa_normals_1991_2020.png`    | `data/processed/climate/noaa_normals_1991_2020.geojson` | Station point visualization of 30-year averages           |
| **U.S. Drought Monitor (2000–2025)** | `drought_monitor_2000_2025.png` | `data/processed/climate/drought_monitor_2000_2025.tif`  | Composite image showing drought severity classes          |

---

## 🧩 Generation Workflow

Thumbnails are generated automatically by the ETL pipeline:

1. Run `make climate` or execute
   `src/pipelines/climate/climate_pipeline.py`
2. Each raster or GeoJSON dataset is opened with `rasterio` or `geopandas`
3. A PNG preview is rendered using `matplotlib` or `Pillow`
4. Images are saved here (`data/processed/metadata/climate/thumbnails/`)
5. References are embedded into each dataset’s STAC metadata:

```json
"thumbnail": { "href": "thumbnails/daymet_1980_2024.png" }
```

This ensures visual previews appear in both the web map and static documentation.

---

## 🧮 Provenance & Standards

* **Format:** PNG (`1024×1024` max, ≤500 KB per image)
* **Color scheme:** consistent with KFM theme (warm–cool blue/orange ramp)
* **Attribution:** Derived from public-domain datasets (NASA, NOAA, USDA)
* **Regeneration:** Safe to delete; recreated on each pipeline run
* **Storage:** Tracked via `.gitignore` exception (only small static previews committed)

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                |
| :---------------------- | :-------------------------------------------- |
| **Documentation-first** | Every thumbnail linked from STAC metadata     |
| **Reproducibility**     | Generated deterministically by ETL pipeline   |
| **Open Standards**      | PNG format, referenced via STAC assets        |
| **Provenance**          | Source dataset noted in metadata              |
| **Auditability**        | Regenerated automatically and validated in CI |

---

## 📅 Version History

| Version | Date       | Summary                                                                       |
| :------ | :--------- | :---------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of climate thumbnails (Daymet, NOAA Normals, Drought Monitor) |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing Climate Through Time and Data.”*
📍 [`data/processed/metadata/climate/thumbnails/`](.) · Linked to the **STAC Climate Collection**

</div>

