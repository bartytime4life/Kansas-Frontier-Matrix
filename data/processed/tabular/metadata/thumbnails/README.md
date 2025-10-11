<div align="center">

# 🖼️ Kansas Frontier Matrix — Tabular Thumbnails  
`data/processed/tabular/metadata/thumbnails/`

**Mission:** Store and describe **thumbnail preview images** generated from processed tabular datasets —  
including census, agricultural, and economic time-series data — for use in Frontier Matrix visual dashboards,  
the STAC catalog, and documentation pages.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains **PNG thumbnail images** automatically generated from  
KFM’s processed tabular datasets under `data/processed/tabular/`.  

Each image serves as a **visual summary** (line, bar, or area charts) representing data trends.  
They are used for:
- 📊 **Analytics dashboards** in the MapLibre/React interface  
- 📦 **STAC catalog thumbnails** for dataset previews  
- 📖 **Documentation visuals** for reports and notebooks  

> 🧩 Thumbnails are regenerated automatically during the ETL process (`make tabular`)  
and may be safely deleted or rebuilt at any time.

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Processed Tabular Datasets\n(data/processed/tabular/*.parquet|*.csv)"] --> B["Thumbnail Generator\n(Python · Matplotlib · Seaborn · Plotly)"]
  B --> C["Thumbnails (.png)\n(data/processed/tabular/metadata/thumbnails)"]
  C --> D["STAC Metadata Linkage\n(data/processed/tabular/metadata/*.json)"]
  D --> E["STAC Catalog + Web Dashboards\n(data/stac/tabular · web/config/layers.json)"]
  %% END OF MERMAID
````

---

## 🗂️ Directory Layout

```bash
data/processed/tabular/metadata/thumbnails/
├── README.md
├── census_population_1860_2020.png
├── agricultural_production_1870_2020.png
└── economic_indicators_1900_2025.png
```

> **Note:**
> Each `.png` corresponds to a metadata JSON record in
> `data/processed/tabular/metadata/` and is referenced in the `"thumbnail"` asset field of its STAC Item.

---

## 📊 Thumbnail Index

| Dataset                                 | Thumbnail File                          | Source Data                                                        | Description                                                           |
| :-------------------------------------- | :-------------------------------------- | :----------------------------------------------------------------- | :-------------------------------------------------------------------- |
| **Census Population (1860–2020)**       | `census_population_1860_2020.png`       | `data/processed/tabular/census_population_1860_2020.parquet`       | Line chart visualizing Kansas population growth over time.            |
| **Agricultural Production (1870–2020)** | `agricultural_production_1870_2020.png` | `data/processed/tabular/agricultural_production_1870_2020.parquet` | Multi-series plot showing crop yield trends and land-use transitions. |
| **Economic Indicators (1900–2025)**     | `economic_indicators_1900_2025.png`     | `data/processed/tabular/economic_indicators_1900_2025.parquet`     | Area chart depicting GDP, employment, and income changes.             |

---

## ⚙️ Thumbnail Generation Workflow

Thumbnails are created automatically via the **tabular ETL pipeline**.

**Makefile target**

```bash
make tabular-thumbnails
```

**Python command**

```bash
python src/pipelines/tabular/tabular_pipeline.py --generate-thumbnails
```

**Steps**

1. Load processed datasets (`.csv` or `.parquet`).
2. Render visual summaries using `matplotlib`, `seaborn`, or `plotly`.
3. Apply the **Frontier Matrix theme** (teal–gold–gray).
4. Export as `.png` ≤ 1024×768 px.
5. Save in this folder & update `"thumbnail"` assets in STAC metadata.

> ♻️ All thumbnails regenerate automatically whenever tabular data is rebuilt.

---

## 🧮 Specifications & Provenance

| Property         | Specification                                              |
| :--------------- | :--------------------------------------------------------- |
| **Format**       | PNG                                                        |
| **Resolution**   | ≤ 1024×768 px                                              |
| **Color Scheme** | Frontier Matrix (teal–gold–gray)                           |
| **Generated By** | `matplotlib`, `seaborn`, `plotly`                          |
| **Attribution**  | Data: US Census, USDA, BEA, BLS · Visuals: Frontier Matrix |
| **Regeneration** | Safe to delete — auto-generated by ETL                     |

---

## 🔗 Integration with Metadata & STAC

| Linked Component                            | Role / Purpose                                             |
| :------------------------------------------ | :--------------------------------------------------------- |
| `data/processed/tabular/metadata/*.json`    | STAC Items reference each thumbnail                        |
| `src/pipelines/tabular/tabular_pipeline.py` | Generates and attaches thumbnails during ETL               |
| `data/stac/tabular/`                        | Includes `"thumbnail"` assets for catalog previews         |
| `web/config/layers.json`                    | Displays thumbnails in analytic dashboards and UI previews |

---

## 🤖 AI & Visualization Integration

* **Auto-tagging:** Machine vision identifies chart type (line, bar, area) and embeds metadata tags.
* **Thematic labeling:** AI appends inferred domain tags (e.g., “demographics,” “agriculture”).
* **Confidence tracking:** Every AI label includes a `confidence` score (0–1).
* **Graph linkage:** AI annotations feed into `src/graph/tabular_nodes.py` for cross-domain connections.

> 🔬 All AI augmentations are stored separately in `data/processed/tabular/ai_metadata/`
> and can be reverted or revalidated manually.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                  |
| :---------------------- | :-------------------------------------------------------------- |
| **Documentation-first** | Every tabular dataset includes README, STAC JSON, and thumbnail |
| **Reproducibility**     | Deterministic generation via Dockerized ETL                     |
| **Open Standards**      | PNG previews referenced in STAC 1.0 metadata                    |
| **Provenance**          | Derived from validated tabular sources                          |
| **Auditability**        | Regeneration verified in CI pipelines                           |

---

## 🧾 Version History

| Version   | Date       | Summary                                                                                          |
| :-------- | :--------- | :----------------------------------------------------------------------------------------------- |
| **1.1.0** | 2025-10-11 | Added front-matter metadata, Mermaid workflow, AI auto-tagging integration, and full MCP summary |
| 1.0.0     | 2025-10-04 | Initial release — includes census, agriculture, and economic chart thumbnails                    |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing the Numbers Behind the Narrative.”*
📍 [`data/processed/tabular/metadata/thumbnails/`](.) · Linked to the **Tabular STAC Collection**

</div>
```
