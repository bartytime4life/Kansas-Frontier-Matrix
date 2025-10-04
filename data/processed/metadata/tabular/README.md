<div align="center">

# 📊 Kansas Frontier Matrix — Tabular Metadata  
`data/processed/metadata/tabular/`

**Mission:** Curate, document, and standardize all **processed tabular and statistical datasets**  
for Kansas Frontier Matrix — enabling reproducible analysis of population, economics, climate statistics,  
and other structured data that inform the state’s historical and environmental trends.

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

This directory contains metadata for all **tabular datasets** processed within Kansas Frontier Matrix (KFM).  
These include statistical, census, and numeric records describing Kansas’s **population, economy, climate, agriculture, and land use** over time.

Each dataset has:
- STAC 1.0-compliant metadata (`.json`)
- Open data license and provenance trail
- Validation against a shared schema (`data/processed/metadata/schema/tabular.schema.json`)
- Reproducible ETL lineage documented in `src/pipelines/tabular/`

These tables serve as structured inputs for cross-domain analysis and AI reasoning in the Frontier Matrix knowledge graph.

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/tabular/
├── README.md
├── census_population_1860_2020.json
├── agricultural_production_1870_2020.json
├── economic_indicators_1900_2025.json
└── thumbnails/
    ├── census_population_1860_2020.png
    ├── agricultural_production_1870_2020.png
    └── economic_indicators_1900_2025.png
````

> **Note:**
> Each `.json` file represents a STAC Item for a tabular dataset in `data/processed/tabular/`.
> The `/thumbnails/` folder holds lightweight previews (charts or plots) of the associated tables.

---

## 📋 Tabular Datasets (Processed Assets)

| Dataset                                 | Source                                      | Format        | Temporal Coverage | Output                                                             |
| :-------------------------------------- | :------------------------------------------ | :------------ | :---------------- | :----------------------------------------------------------------- |
| **Census Population (1860–2020)**       | US Census Bureau / Kansas State Data Center | CSV → Parquet | 1860–2020         | `data/processed/tabular/census_population_1860_2020.parquet`       |
| **Agricultural Production (1870–2020)** | USDA NASS / Kansas Ag. Statistics           | CSV → Parquet | 1870–2020         | `data/processed/tabular/agricultural_production_1870_2020.parquet` |
| **Economic Indicators (1900–2025)**     | BEA / BLS / Kansas Dept. of Revenue         | CSV → Parquet | 1900–2025         | `data/processed/tabular/economic_indicators_1900_2025.parquet`     |

All files are standardized to open formats (**CSV**, **Parquet**)
and indexed under `data/stac/tabular/` for discoverability.

---

## 💾 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "census_population_1860_2020",
  "properties": {
    "title": "Kansas Population Census Data (1860–2020)",
    "datetime": "2020-01-01T00:00:00Z",
    "description": "Historical population counts by Kansas county from 1860 to 2020.",
    "themes": ["tabular", "demographics", "population"],
    "license": "Public Domain (US Census Bureau)",
    "providers": [
      {"name": "US Census Bureau", "roles": ["producer"]},
      {"name": "Kansas Frontier Matrix", "roles": ["processor"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../tabular/census_population_1860_2020.parquet",
      "type": "application/x-parquet",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "thumbnails/census_population_1860_2020.png"
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

---

## 🧩 Schema & Semantic Alignment

| Entity             | Ontology Mapping                          | Example                             |
| :----------------- | :---------------------------------------- | :---------------------------------- |
| Census Table       | `E31_Document` + `E73_Information_Object` | “Population by County, 1860–2020”   |
| Economic Indicator | `E16_Measurement` + `E55_Type`            | “Per Capita Income”                 |
| Agricultural Yield | `E16_Measurement` + `E53_Place`           | “Wheat Production, Sedgwick County” |
| Temporal Span      | OWL-Time interval                         | “1900–2025”                         |

Semantic mapping supports integration with the KFM knowledge graph
for timeline visualization and cross-domain analytics.

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make tabular` → runs `src/pipelines/tabular/tabular_pipeline.py`

**Dependencies:**
`pandas`, `pyarrow`, `fastparquet`, `geopandas`, `requests`, `matplotlib`

**Steps:**

1. Download CSV data from public sources (USDA, Census, BLS, etc.)
2. Clean and normalize columns (units, categories, NA handling)
3. Convert to Parquet for efficient storage
4. Generate preview thumbnails (plots)
5. Create STAC metadata JSONs
6. Compute `.sha256` checksums for provenance
7. Validate schema and STAC structure in CI

Logs and validation artifacts are stored in `data/processed/checksums/tabular/`.

---

## 🧮 Provenance & Validation

* **Checksums:** `.sha256` sidecars for every file
* **Licensing:** Public domain or CC-BY for derived datasets
* **Validation:** JSON Schema + STAC compliance (automated via CI/CD)
* **Cross-links:** Source descriptors in `data/sources/tabular/*.json`

---

## 🔗 Integration Points

| Component                         | Role                                              |
| :-------------------------------- | :------------------------------------------------ |
| `data/stac/tabular/`              | STAC Items and Collections for tabular datasets   |
| `web/config/layers.json`          | Enables data-driven charts and analytics overlays |
| `src/graph/tabular_nodes.py`      | Knowledge graph ingestion of structured tables    |
| `docs/architecture.md`            | ETL and data design reference                     |
| `data/processed/metadata/schema/` | Shared validation schemas                         |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                |
| :---------------------- | :-------------------------------------------- |
| **Documentation-first** | README + STAC metadata per dataset            |
| **Reproducibility**     | Deterministic Makefile + Python ETL pipelines |
| **Open Standards**      | CSV, Parquet, JSON Schema, STAC               |
| **Provenance**          | Source URLs + checksums for each dataset      |
| **Auditability**        | CI validation + reproducible rebuild logs     |

---

## 📅 Version History

| Version | Date       | Summary                                                                       |
| :------ | :--------- | :---------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial tabular metadata release — Census, Agriculture, and Economic datasets |

---

## 📎 References

* [US Census Bureau Data Portal](https://data.census.gov/)
* [USDA National Agricultural Statistics Service](https://www.nass.usda.gov/)
* [Bureau of Economic Analysis (BEA)](https://www.bea.gov/)
* [Bureau of Labor Statistics (BLS)](https://www.bls.gov/)
* [Master Coder Protocol Docs](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Quantifying History: Turning Numbers Into Narrative.”*
📍 [`data/processed/metadata/tabular/`](.) · Integrated within the **STAC Data Catalog Layer**

</div>
