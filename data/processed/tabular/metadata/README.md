<div align="center">

# 📊 Kansas Frontier Matrix — Tabular Metadata  
`data/processed/tabular/metadata/`

**Mission:** Curate, document, and standardize all **processed tabular datasets**  
within the Kansas Frontier Matrix (KFM) — including historical census, agricultural, and economic data —  
to ensure open, reproducible, and interoperable structured data for long-term analysis.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **metadata JSON files** describing the structure, provenance, and  
standards compliance for all tabular datasets under `data/processed/tabular/`.  

These datasets represent **quantitative and statistical data** across Kansas — demography, agriculture, economics, and land use — and are essential for cross-domain analysis within KFM.

Each metadata file includes:
- **STAC 1.0**-compliant JSON metadata  
- **Provenance & licensing** information  
- Associated **`.sha256`** integrity checksum  
- **Schema validation** reference (`data/processed/metadata/schema/tabular.schema.json`)  
- Links to **thumbnails** and visualization previews  

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Processed Tables\n(data/processed/tabular/*.csv|*.parquet)"] --> B["Metadata Authoring\n(this folder: *.json)"]
  B --> C["Thumbnails\n(thumbnails/*.png)"]
  B --> D["Schema Validation\n(CSVW/JSON Schema · STAC 1.0)"]
  D --> E["CI Gate\n(GitHub Actions: stac-validate.yml)"]
  E --> F["Catalog & Graph\n(data/stac/tabular/* · src/graph/tabular_nodes.py)"]
  %% END OF MERMAID
````

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
```

> **Note:** Each `.json` conforms to **STAC 1.0** and references the processed dataset in
> `data/processed/tabular/` as well as its checksum in the sibling folder `../checksums/`.

---

## 📈 Tabular Datasets (Processed Assets)

| Dataset                                 | Source                                      | Format  | Temporal Coverage | Output                                                             |
| :-------------------------------------- | :------------------------------------------ | :------ | :---------------- | :----------------------------------------------------------------- |
| **Census Population (1860–2020)**       | US Census Bureau / Kansas State Data Center | Parquet | 1860–2020         | `data/processed/tabular/census_population_1860_2020.parquet`       |
| **Agricultural Production (1870–2020)** | USDA NASS / KS Ag. Statistics               | Parquet | 1870–2020         | `data/processed/tabular/agricultural_production_1870_2020.parquet` |
| **Economic Indicators (1900–2025)**     | BEA / BLS / KS Dept. of Revenue             | Parquet | 1900–2025         | `data/processed/tabular/economic_indicators_1900_2025.parquet`     |

All datasets are validated for integration into KFM’s **knowledge graph** and analytics pipelines,
use open formats (**CSV**, **Parquet**), and are cataloged under `data/stac/tabular/`.

---

## 💾 Example STAC Item (GitHub-safe minimal)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "census_population_1860_2020",
  "collection": "kfm_tabular",
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99], [-94.59, 36.99],
      [-94.59, 40.00], [-102.05, 40.00],
      [-102.05, 36.99]
    ]]
  },
  "properties": {
    "title": "Kansas Population Census Data (1860–2020)",
    "description": "Population totals by Kansas county from 1860 through 2020.",
    "datetime": "2020-01-01T00:00:00Z",
    "themes": ["tabular", "demographics", "population"],
    "processing:software": "Python 3.11; Pandas 2.x",
    "kfm:mcp_provenance": "sha256:<PUT_FILE_HASH_HERE>",
    "license": "CC-BY-4.0",
    "csvw:schema": "tabular.schema.json"
  },
  "assets": {
    "data": {
      "href": "../tabular/census_population_1860_2020.parquet",
      "type": "application/x-parquet",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "thumbnails/census_population_1860_2020.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    },
    "checksum:sha256": {
      "href": "../checksums/census_population_1860_2020.parquet.sha256",
      "type": "text/plain",
      "roles": ["metadata"]
    }
  },
  "links": [
    {"rel": "collection", "href": "../../../stac/collections/kfm_tabular.json", "type": "application/json"},
    {"rel": "self", "href": "census_population_1860_2020.json", "type": "application/json"},
    {"rel": "parent", "href": ".", "type": "text/html"}
  ]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity              | Ontology Mapping                                | Example                        |
| :------------------ | :---------------------------------------------- | :----------------------------- |
| Population Table    | CIDOC `E31_Document` + `E73_Information_Object` | County-level census dataset    |
| Economic Indicator  | CIDOC `E16_Measurement` + `E55_Type`            | Per-capita income over time    |
| Agricultural Output | CIDOC `E16_Measurement` + `E53_Place`           | Wheat yield in Sedgwick County |
| Time Period         | **OWL-Time** interval                           | 1860–2020                      |

These mappings make tabular data interoperable with KFM’s **spatial** and **narrative** layers.

---

## ⚙️ ETL & Processing Workflow

**Makefile**

```bash
make tabular
```

**Pipeline**

```bash
python src/pipelines/tabular/tabular_pipeline.py
```

**Steps**

1. Fetch & normalize tabular datasets (CSV/API).
2. Clean columns/units; enforce schema.
3. Convert to **Parquet** for efficient querying.
4. Compute **`.sha256`** checksums (stored in `../checksums/`).
5. Generate **STAC** items + thumbnails.
6. Validate structure via **CSVW/JSON Schema** + **STAC 1.0** in CI.

---

## 🧮 Provenance & Validation

* **Checksums:** `data/processed/tabular/checksums/` (sibling folder)
* **Licensing:** Public domain or **CC-BY** (source-dependent)
* **Validation:** STAC + JSON Schema validation in CI
* **Source Manifests:** `data/sources/tabular/*.json`

---

## 🔗 Integration Points

| Component                           | Role                                               |
| :---------------------------------- | :------------------------------------------------- |
| `data/stac/tabular/`                | STAC Items & Collections for tabular datasets      |
| `web/config/layers.json`            | UI integration for charts & summaries              |
| `src/graph/tabular_nodes.py`        | Knowledge Graph ingestion + entity linking         |
| `data/processed/tabular/checksums/` | Checksum verification for reproducibility          |
| `docs/architecture.md`              | Data architecture overview for tabular integration |

---

## 🤖 AI & Metadata Notes

* **Entity Extraction:** Auto-links datasets to places, periods, and topics (demography, economics, agriculture).
* **Quality Signals:** Outlier detection + consistency checks recorded with `confidence` scores (0–1).
* **Non-destructive:** AI inferences live under `data/processed/tabular/ai_metadata/` and are fully reversible.

---

## 🧠 MCP Compliance Summary

| Principle           | Implementation                                               |
| :------------------ | :----------------------------------------------------------- |
| Documentation-first | README + per-dataset STAC item                               |
| Reproducibility     | Containerized ETL, checksums, deterministic transforms       |
| Open Standards      | CSV/Parquet, STAC 1.0, CSVW/JSON Schema                      |
| Provenance          | Source → process → product lineage with cryptographic hashes |
| Auditability        | CI validation logs + schema/STAC gates                       |

---

## 🧾 Version History

|  Version  | Date       | Summary                                                                                      |
| :-------: | :--------- | :------------------------------------------------------------------------------------------- |
| **1.1.0** | 2025-10-11 | Upgraded README: corrected badge paths, added Mermaid flow, stronger STAC example, MCP table |
|   1.0.0   | 2025-10-04 | Initial tabular metadata release (census, agriculture, economic datasets + thumbnails)       |

---

<div align="center">

**Kansas Frontier Matrix** — *“Quantifying History: Turning Data Into Discovery.”*
📍 [`data/processed/tabular/metadata/`](.)

</div>
```
