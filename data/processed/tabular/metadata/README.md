<div align="center">

# 📊 Kansas Frontier Matrix — Tabular Metadata  
`data/processed/tabular/metadata/`

**Mission:** Curate, document, and standardize all **processed tabular datasets**  
within the Kansas Frontier Matrix (KFM) — including historical census, agricultural, and economic data —  
to ensure open, reproducible, and interoperable structured data for long-term analysis.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **metadata JSON files** describing the structure, provenance, and  
standards compliance for all tabular datasets under `data/processed/tabular/`.  

These datasets represent **quantitative and statistical data** across Kansas —  
covering demography, agriculture, economics, and land use — and are essential for  
cross-domain analysis within the Kansas Frontier Matrix.

Each metadata file includes:
- STAC 1.0-compliant JSON metadata  
- Provenance and licensing information  
- Associated `.sha256` integrity checksum  
- Schema validation (`data/processed/metadata/schema/tabular.schema.json`)  
- References to thumbnails and visualization previews  

---

## 🗂️ Directory Layout

```bash
data/processed/tabular/metadata/
├── README.md
├── census_population_1860_2020.json
├── agricultural_production_1870_2020.json
├── economic_indicators_1900_2025.json
└── thumbnails/
    ├── census_population_1860_2020.png
    ├── agricultural_production_1870_2020.png
    └── economic_indicators_1900_2025.png
````

> **Note:** Each `.json` file conforms to the STAC specification and references its
> processed dataset in `data/processed/tabular/` as well as its checksum in
> `data/processed/checksums/tabular/`.

---

## 📈 Tabular Datasets (Processed Assets)

| Dataset                                 | Source                                      | Format  | Temporal Coverage | Output                                                             |
| :-------------------------------------- | :------------------------------------------ | :------ | :---------------- | :----------------------------------------------------------------- |
| **Census Population (1860–2020)**       | US Census Bureau / Kansas State Data Center | Parquet | 1860–2020         | `data/processed/tabular/census_population_1860_2020.parquet`       |
| **Agricultural Production (1870–2020)** | USDA NASS / KS Ag. Statistics               | Parquet | 1870–2020         | `data/processed/tabular/agricultural_production_1870_2020.parquet` |
| **Economic Indicators (1900–2025)**     | BEA / BLS / Kansas Dept. of Revenue         | Parquet | 1900–2025         | `data/processed/tabular/economic_indicators_1900_2025.parquet`     |

All datasets are structured and validated for integration into KFM’s graph and analytical systems.
They adhere to open formats (`CSV`, `Parquet`) and are linked to STAC records under `data/stac/tabular/`.

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
    "description": "Population totals by Kansas county from 1860 through 2020.",
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

## 🧩 Semantic & Ontological Alignment

| Entity              | Ontology Mapping                          | Example                        |
| :------------------ | :---------------------------------------- | :----------------------------- |
| Population Table    | `E31_Document` + `E73_Information_Object` | County-level census dataset    |
| Economic Indicator  | `E16_Measurement` + `E55_Type`            | Per-capita income over time    |
| Agricultural Output | `E16_Measurement` + `E53_Place`           | Wheat yield in Sedgwick County |
| Time Period         | OWL-Time interval                         | 1860–2020                      |

This alignment ensures that tabular data is interoperable within the KFM knowledge graph
and can connect with spatial and narrative layers through ontology mappings.

---

## ⚙️ ETL & Processing Workflow

**Pipeline Command:**

```bash
make tabular
```

**Python Script:**

```bash
python src/pipelines/tabular/tabular_pipeline.py
```

**Steps:**

1. Fetch and normalize tabular datasets (CSV or API).
2. Clean and harmonize column names and units.
3. Convert to Parquet for efficient querying and storage.
4. Compute `.sha256` checksums for reproducibility.
5. Generate STAC metadata and preview thumbnails.
6. Validate structure via JSON Schema + CI STAC tests.

---

## 🧮 Provenance & Validation

* **Checksums:** Located in `data/processed/checksums/tabular/`
* **Licensing:** Public domain or CC-BY (depending on source)
* **Validation:** STAC + JSON Schema validation via GitHub CI workflows
* **Cross-links:** Sources documented in `data/sources/tabular/*.json`

---

## 🔗 Integration Points

| Component                           | Role                                                    |
| :---------------------------------- | :------------------------------------------------------ |
| `data/stac/tabular/`                | STAC items and collections for tabular datasets         |
| `web/config/layers.json`            | Web interface integration for charts and data summaries |
| `src/graph/tabular_nodes.py`        | Knowledge graph ingestion and entity linking            |
| `data/processed/checksums/tabular/` | Checksum verification for reproducibility               |
| `docs/architecture.md`              | Data architecture overview for tabular integration      |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                    |
| :---------------------- | :------------------------------------------------ |
| **Documentation-first** | README + STAC metadata per dataset                |
| **Reproducibility**     | Deterministic ETL with tracked checksum outputs   |
| **Open Standards**      | CSV, Parquet, STAC, JSON Schema                   |
| **Provenance**          | Clear source-to-product lineage                   |
| **Auditability**        | CI workflows validate schema, STAC, and checksums |

---

## 📅 Version History

| Version | Date       | Summary                                                                                |
| :------ | :--------- | :------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial tabular metadata release — includes census, agriculture, and economic datasets |

---

<div align="center">

**Kansas Frontier Matrix** — *“Quantifying History: Turning Data Into Discovery.”*
📍 [`data/processed/tabular/metadata/`](.) · Integrated with the **Tabular STAC Collection**

</div>
