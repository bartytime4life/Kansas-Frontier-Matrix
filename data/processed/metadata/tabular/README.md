<div align="center">

# 📊 Kansas Frontier Matrix — Tabular Metadata  
`data/processed/metadata/tabular/`

**Mission:** Curate, document, and standardize all **processed tabular and statistical datasets**  
for Kansas Frontier Matrix — enabling reproducible analysis of population, economics, climate statistics,  
and other structured data that inform the state’s historical and environmental trends.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains metadata for all **tabular datasets** processed within Kansas Frontier Matrix (KFM).  
These include statistical, census, and numeric records describing Kansas’s **population, economy, climate, agriculture, and land use** over time.

Each dataset provides:
- **STAC 1.0** item (`.json`)
- Open data license & provenance trail
- Validation against a shared schema (`data/processed/metadata/schema/tabular.schema.json`)
- Reproducible ETL lineage documented in `src/pipelines/tabular/`

These tables serve as structured inputs for cross-domain analysis and AI reasoning in the KFM knowledge graph.

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Raw Tables / APIs\n(Census · USDA · BEA · BLS)"] --> B["ETL Normalize\n(Pandas · PyArrow · CSVKit)"]
  B --> C["Processed Tables\n(data/processed/tabular/*.csv|*.parquet)"]
  C --> D["Metadata Authoring\n(data/processed/metadata/tabular/*.json)"]
  D --> E["Validation\n(CSVW/JSON Schema · STAC 1.0 · CI)"]
  E --> F["Catalog & Graph\n(data/stac/tabular · src/graph/tabular_nodes.py)"]
  %% END OF MERMAID
````

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
```

> **Note:** Each `.json` is a STAC Item for a tabular dataset in `data/processed/tabular/`.
> Thumbnails provide lightweight previews (charts/plots) for the catalog & UI.

---

## 📋 Tabular Datasets (Processed Assets)

| Dataset                                 | Source                                  | Format        | Temporal Coverage | Output                                                             |
| :-------------------------------------- | :-------------------------------------- | :------------ | :---------------- | :----------------------------------------------------------------- |
| **Census Population (1860–2020)**       | US Census Bureau / KS State Data Center | CSV → Parquet | 1860–2020         | `data/processed/tabular/census_population_1860_2020.parquet`       |
| **Agricultural Production (1870–2020)** | USDA NASS / Kansas Ag. Statistics       | CSV → Parquet | 1870–2020         | `data/processed/tabular/agricultural_production_1870_2020.parquet` |
| **Economic Indicators (1900–2025)**     | BEA / BLS / Kansas Dept. of Revenue     | CSV → Parquet | 1900–2025         | `data/processed/tabular/economic_indicators_1900_2025.parquet`     |

All files use open formats (**CSV**, **Parquet**) and are discoverable under `data/stac/tabular/`.

---

## 💾 Example STAC Item (enhanced)

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
    "description": "Historical population counts by Kansas county from 1860 to 2020.",
    "datetime": "2020-01-01T00:00:00Z",
    "themes": ["tabular","demographics","population"],
    "processing:software": "Python 3.11; Pandas 2.x; PyArrow",
    "kfm:mcp_provenance": "sha256:<PUT_FILE_HASH_HERE>",
    "license": "Public Domain (US Census Bureau)",
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
      "href": "../tabular/checksums/census_population_1860_2020.parquet.sha256",
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

## 🧩 Schema & Semantic Alignment

| Entity             | Ontology Mapping                                | Example                             |
| :----------------- | :---------------------------------------------- | :---------------------------------- |
| Census Table       | CIDOC `E31_Document` + `E73_Information_Object` | “Population by County, 1860–2020”   |
| Economic Indicator | CIDOC `E16_Measurement` + `E55_Type`            | “Per-Capita Income”                 |
| Agricultural Yield | CIDOC `E16_Measurement` + `E53_Place`           | “Wheat Production, Sedgwick County” |
| Temporal Span      | **OWL-Time** interval                           | “1900–2025”                         |

Schemas follow **CSVW/JSON Table Schema**; semantic fields enable graph & timeline integration.

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

1. Download CSV/API sources (Census, USDA, BEA, BLS).
2. Clean & normalize (units, categories, NA handling).
3. Convert to **Parquet** for efficient storage/query.
4. Generate preview thumbnails (plots).
5. Create **STAC items** + compute **`.sha256`** checksums.
6. Validate **CSVW/JSON Schema** + **STAC 1.0** in CI.

---

## 🧮 Provenance & Validation

* **Checksums:** `data/processed/tabular/checksums/`
* **Licensing:** Public domain or **CC-BY** (source-dependent)
* **Validation:** CSVW/JSON Schema + STAC 1.0 via GitHub Actions
* **Source Manifests:** `data/sources/tabular/*.json`

---

## 🔗 Integration Points

| Component                         | Role                                                    |
| :-------------------------------- | :------------------------------------------------------ |
| `data/stac/tabular/`              | STAC Items & Collections for tabular datasets           |
| `web/config/layers.json`          | UI integration for charts & analytics                   |
| `src/graph/tabular_nodes.py`      | Knowledge graph ingestion & entity linking              |
| `data/processed/metadata/schema/` | Shared validation schemas (incl. `tabular.schema.json`) |

---

## ✅ QA Checklist (copy into PRs)

* [ ] STAC item validates (CI green)
* [ ] `kfm:mcp_provenance` hash equals file checksum in `../tabular/checksums/`
* [ ] CSVW schema present & fields match (types, units, primary keys)
* [ ] Thumbnail present and referenced in `assets.thumbnail`
* [ ] Links (`self`, `collection`, `parent`) resolve; paths are relative
* [ ] Licensing and providers populated & accurate

---

## 🧠 MCP Compliance Summary

| Principle           | Implementation                                             |
| :------------------ | :--------------------------------------------------------- |
| Documentation-first | README + per-dataset STAC item + CSVW schema               |
| Reproducibility     | Containerized ETL; deterministic transforms; checksums     |
| Open Standards      | **CSV/Parquet**, **CSVW/JSON Schema**, **STAC 1.0**        |
| Provenance          | Source URLs, providers, licenses, and cryptographic hashes |
| Auditability        | CI validation logs; schema/STAC gates across environments  |

---

## 📅 Version History

|  Version  | Date       | Summary                                                                                                           |
| :-------: | :--------- | :---------------------------------------------------------------------------------------------------------------- |
| **1.1.0** | 2025-10-11 | Fixed badge paths; added Mermaid flow; enhanced STAC item (collection/geometry/checksum/CSVW/links); QA checklist |
|   1.0.0   | 2025-10-04 | Initial tabular metadata release — Census, Agriculture, and Economic datasets                                     |

---

## 📎 References

* **US Census Bureau:** [https://data.census.gov/](https://data.census.gov/)
* **USDA NASS:** [https://www.nass.usda.gov/](https://www.nass.usda.gov/)
* **BEA:** [https://www.bea.gov/](https://www.bea.gov/) · **BLS:** [https://www.bls.gov/](https://www.bls.gov/)
* **MCP Standards:** `docs/standards/` · **Schemas:** `data/processed/metadata/schema/`

---

<div align="center">

**Kansas Frontier Matrix** — *“Quantifying History: Turning Numbers Into Narrative.”*
📍 [`data/processed/metadata/tabular/`](.)

</div>
```
