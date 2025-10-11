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

Datasets span **demography, agriculture, economics, and land use** and are essential for cross-domain analysis within KFM.

Each metadata file includes:
- **STAC 1.0**-compliant JSON metadata  
- **CSVW/JSON Table Schema** reference for columns & types  
- **Provenance & licensing** information  
- Associated **`.sha256`** integrity checksum  
- Links to **thumbnails** and visualization previews  

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Processed Tables\n(data/processed/tabular/*.csv|*.parquet)"] --> B["Metadata Authoring\n(this folder: *.json)"]
  B --> C["Schema & CSVW\n(tabular.schema.json · field dict)"]
  B --> D["Thumbnails\n(thumbnails/*.png)"]
  B --> E["CI Validation\n(CSVW/JSON Schema · STAC 1.0)"]
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
├── tabular.schema.json                # CSVW/JSON Table Schema (shared)
└── thumbnails/
    ├── census_population_1860_2020.png
    ├── agricultural_production_1870_2020.png
    └── economic_indicators_1900_2025.png
```

> **Note:** Each `.json` conforms to **STAC 1.0**, references its processed dataset in
> `../` (`data/processed/tabular/`), and its checksum in the sibling folder `../checksums/`.

---

## 📈 Tabular Datasets (Processed Assets)

| Dataset                                 | Source                                      | Format  | Temporal Coverage | Output                                                             |
| :-------------------------------------- | :------------------------------------------ | :------ | :---------------- | :----------------------------------------------------------------- |
| **Census Population (1860–2020)**       | US Census Bureau / Kansas State Data Center | Parquet | 1860–2020         | `data/processed/tabular/census_population_1860_2020.parquet`       |
| **Agricultural Production (1870–2020)** | USDA NASS / KS Ag. Statistics               | Parquet | 1870–2020         | `data/processed/tabular/agricultural_production_1870_2020.parquet` |
| **Economic Indicators (1900–2025)**     | BEA / BLS / KS Dept. of Revenue             | Parquet | 1900–2025         | `data/processed/tabular/economic_indicators_1900_2025.parquet`     |

All datasets are validated for KFM’s **knowledge graph** and analytics pipelines, use open formats (**CSV**, **Parquet**), and are cataloged under `data/stac/tabular/`.

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

## 🧮 CSVW / JSON Table Schema (field pattern)

> Use `tabular.schema.json` to define column names, types, units, constraints, and value semantics.

**Minimal example snippet:**

```json
{
  "@context": "http://www.w3.org/ns/csvw",
  "tables": [{
    "url": "../tabular/census_population_1860_2020.parquet",
    "tableSchema": {
      "columns": [
        {"name": "fips_code", "datatype": "string", "required": true},
        {"name": "county_name", "datatype": "string"},
        {"name": "year", "datatype": {"base": "gYear"}, "required": true},
        {"name": "population", "datatype": "integer", "required": true},
        {"name": "source", "datatype": "string"},
        {"name": "license", "datatype": "string"}
      ],
      "primaryKey": ["fips_code", "year"]
    }
  }]
}
```

---

## 📓 Data Dictionary (per-dataset template)

| Column        | Type    | Unit   | Description                               | Allowed / Notes           |
| :------------ | :------ | :----- | :---------------------------------------- | :------------------------ |
| `fips_code`   | string  | —      | County FIPS (5-digit, left-padded if CSV) | `^\d{5}$`                 |
| `county_name` | string  | —      | County name (2020 boundaries)             | Title case                |
| `year`        | gYear   | —      | Observation year                          | 1860–2025                 |
| `population`  | integer | people | Population total                          | `>=0`                     |
| `source`      | string  | —      | Originating dataset                       | e.g., “US Census”         |
| `license`     | string  | —      | Data license                              | CC-BY-4.0 / Public Domain |

> Place dataset-specific dictionaries beside each STAC item (e.g., `census_population_1860_2020.dict.md`).

---

## ✅ QA / CI Checklist (copy into PRs)

* [ ] STAC item validates (CI badge green)
* [ ] CSVW schema validates types & constraints
* [ ] `.sha256` present in `../checksums/` and passes `sha256sum -c`
* [ ] Thumbnail present & path correct in `assets.thumbnail`
* [ ] `derived_from` / provenance fields populated
* [ ] Data dictionary updated & consistent with CSVW schema

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
6. Validate via **CSVW/JSON Schema** + **STAC 1.0** in CI.

---

## 🧮 Provenance & Validation

* **Checksums:** `data/processed/tabular/checksums/`
* **Licensing:** Public domain or **CC-BY** (source-dependent)
* **Validation:** STAC + CSVW/JSON Schema in CI
* **Source Manifests:** `data/sources/tabular/*.json`

---

## 🔗 Integration Points

| Component                           | Role                                       |
| :---------------------------------- | :----------------------------------------- |
| `data/stac/tabular/`                | STAC Items & Collections                   |
| `web/config/layers.json`            | UI integration for charts & summaries      |
| `src/graph/tabular_nodes.py`        | Knowledge Graph ingestion + entity linking |
| `data/processed/tabular/checksums/` | Reproducibility & integrity                |
| `docs/architecture.md`              | End-to-end data architecture               |

---

## 🤖 AI & Metadata Notes

* **Entity extraction & linking** to places, periods, topics (demography, agriculture, economics).
* **Quality signals** (outlier detection) with `confidence` scores (0–1).
* **Non-destructive**: AI inferences stored in `data/processed/tabular/ai_metadata/`.

---

## 🧠 MCP Compliance Summary

| Principle           | Implementation                                         |
| :------------------ | :----------------------------------------------------- |
| Documentation-first | README + per-dataset STAC item + data dictionary       |
| Reproducibility     | Containerized ETL, checksums, deterministic transforms |
| Open Standards      | CSV/Parquet, **STAC 1.0**, **CSVW/JSON Table Schema**  |
| Provenance          | Source → process → product with cryptographic hashes   |
| Auditability        | CI validation logs + schema/STAC gates                 |

---

## 🧾 Version History

|  Version  | Date       | Summary                                                                                                |
| :-------: | :--------- | :----------------------------------------------------------------------------------------------------- |
| **1.2.0** | 2025-10-11 | Added CSVW schema file, data-dictionary pattern, QA checklist; refined Mermaid; tightened STAC fields. |
| **1.1.0** | 2025-10-11 | Badge paths fixed; Mermaid flow; stronger STAC example; MCP table                                      |
|   1.0.0   | 2025-10-04 | Initial tabular metadata release (census, agriculture, economic datasets + thumbnails)                 |

---

<div align="center">

**Kansas Frontier Matrix** — *“Quantifying History: Turning Data Into Discovery.”*
📍 [`data/processed/tabular/metadata/`](.)

</div>
```
