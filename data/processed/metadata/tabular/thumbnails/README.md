<div align="center">

# 🖼️ Kansas Frontier Matrix — Tabular Thumbnails  
`data/processed/metadata/tabular/thumbnails/`

**Mission:** Store and describe **thumbnail preview images** generated from tabular datasets —  
providing visual summaries of Kansas Frontier Matrix’s census, agriculture, and economic time-series data.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **static PNG preview charts** for tabular datasets documented in  
`data/processed/metadata/tabular/`.  

Each image serves as a **visual summary of trends and values** — for use in:
- The **web UI analytics dashboard** (map + timeline overlays)
- **STAC catalog thumbnails** in metadata JSON
- **Documentation previews** and research summaries  

Thumbnails are automatically generated during the ETL process (`make tabular`)  
and are safe to delete and regenerate at any time.

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/tabular/thumbnails/
├── README.md
├── census_population_1860_2020.png
├── agricultural_production_1870_2020.png
└── economic_indicators_1900_2025.png
````

> **Note:** Each `.png` corresponds to a dataset in
> `data/processed/metadata/tabular/` and is referenced in its STAC metadata JSON
> under the `"thumbnail"` asset field.

---

## 📊 Thumbnail Index

| Dataset                                 | Thumbnail File                          | Source Dataset                                                     | Description                                                       |
| :-------------------------------------- | :-------------------------------------- | :----------------------------------------------------------------- | :---------------------------------------------------------------- |
| **Census Population (1860–2020)**       | `census_population_1860_2020.png`       | `data/processed/tabular/census_population_1860_2020.parquet`       | Line chart showing Kansas population growth from 1860 to 2020     |
| **Agricultural Production (1870–2020)** | `agricultural_production_1870_2020.png` | `data/processed/tabular/agricultural_production_1870_2020.parquet` | Multi-line chart showing key crop yields and acreage through time |
| **Economic Indicators (1900–2025)**     | `economic_indicators_1900_2025.png`     | `data/processed/tabular/economic_indicators_1900_2025.parquet`     | Plot summarizing GDP, employment, and per-capita income trends    |

---

## 🧰 Generation Workflow

Thumbnails are automatically created as part of the tabular ETL pipeline:

1. Run `make tabular` or execute
   `src/pipelines/tabular/tabular_pipeline.py`
2. Each dataset is loaded using `pandas` or `pyarrow`
3. Visualization is created using `matplotlib` or `seaborn`
4. Charts are exported as PNG files (`1024×768` default resolution)
5. Thumbnails are saved here and linked to STAC metadata as:

```json
"thumbnail": { "href": "thumbnails/economic_indicators_1900_2025.png" }
```

These images provide fast-loading visual references in the Frontier Matrix web interface and GitHub viewer.

---

## 🧮 Specifications & Provenance

| Property            | Specification                                              |
| :------------------ | :--------------------------------------------------------- |
| **Format**          | PNG (`≤1024×768`, ≤500 KB per image)                       |
| **Color Palette**   | Frontier Matrix palette (teal–gold–gray)                   |
| **Source Data**     | Derived from tabular Parquet datasets                      |
| **Attribution**     | Data: US Census, USDA, BEA, BLS — Visuals: Frontier Matrix |
| **Storage**         | Tracked in Git for documentation; regenerated in ETL       |
| **Reproducibility** | Thumbnails are deterministic given identical inputs        |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                |
| :---------------------- | :-------------------------------------------- |
| **Documentation-first** | Each thumbnail linked from its STAC metadata  |
| **Reproducibility**     | Automatically generated in ETL pipeline       |
| **Open Standards**      | PNG previews; STAC-compliant asset references |
| **Provenance**          | Source datasets defined in metadata JSON      |
| **Auditability**        | Regenerated on every build; validated in CI   |

---

## 📅 Version History

| Version | Date       | Summary                                                                  |
| :------ | :--------- | :----------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of tabular thumbnails (population, agriculture, economy) |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing the Data Behind the Frontier.”*
📍 [`data/processed/metadata/tabular/thumbnails/`](.) · Linked to the **Tabular STAC Collection**

</div>
