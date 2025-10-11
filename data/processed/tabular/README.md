<div align="center">

# 🧾 Kansas Frontier Matrix — Processed Tabular Data  
`data/processed/tabular/`

**Mission:** Store and document all **cleaned, structured, and analysis-ready tabular datasets** —  
statistical summaries, time series, and cross-domain tables derived from Kansas historical, climatic,  
and ecological data sources.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [System Flow (Mermaid)](#system-flow-mermaid)
- [Directory Layout](#directory-layout)
- [Core Tabular Datasets](#core-tabular-datasets)
- [Schema Standards](#schema-standards)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [AI & Semantic Integration](#ai--semantic-integration)
- [Contributing New Tabular Data](#contributing-new-tabular-data)
- [References](#references)
- [Version History](#version-history)

---

## 📊 Overview

This subdirectory holds **processed tabular datasets** that have been cleaned,  
validated, and normalized for analytical integration within the **Kansas Frontier Matrix (KFM)**.  

Includes:
- **Climate time series**
- **Demographic and population tables**
- **Ecological and land use metrics**
- **Cross-domain relational datasets**

All files are **ready for ingestion** into analytics engines, dashboards, or the KFM knowledge graph.

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Raw CSVs / XLSX\n(data/raw/tabular)"] --> B["Cleaning & Transformation\n(Pandas · NumPy · CSVKit)"]
  B --> C["Processed Tables\n(data/processed/tabular/*.csv)"]
  C --> D["Metadata & Checksums\n(metadata/*.json · checksums/*.sha256)"]
  D --> E["STAC Items\n(data/stac/tabular/*.json)"]
  E --> F["Knowledge Graph Ingestion\n(src/graph/tabular_nodes.py)"]
  %% END OF MERMAID
````

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── tabular/
        ├── county_population_1850_2020.csv
        ├── precipitation_trends_1895_2024.csv
        ├── tornado_counts_1950_2024.csv
        ├── landuse_by_county_1992_2021.csv
        ├── drought_summary_1895_2024.csv
        ├── metadata/
        │   ├── county_population_1850_2020.json
        │   ├── tornado_counts_1950_2024.json
        │   └── landuse_by_county_1992_2021.json
        ├── checksums/
        │   ├── county_population_1850_2020.csv.sha256
        │   ├── precipitation_trends_1895_2024.csv.sha256
        │   └── tornado_counts_1950_2024.csv.sha256
        └── README.md
```

---

## 🧩 Core Tabular Datasets

| Dataset                              | File                                 | Description                              | Source     | Units  | Format |
| :----------------------------------- | :----------------------------------- | :--------------------------------------- | :--------- | :----- | :----- |
| **County Population (1850–2020)**    | `county_population_1850_2020.csv`    | Decennial population by county           | US Census  | people | CSV    |
| **Precipitation Trends (1895–2024)** | `precipitation_trends_1895_2024.csv` | Annual precipitation anomalies           | NOAA NCEI  | mm     | CSV    |
| **Tornado Counts (1950–2024)**       | `tornado_counts_1950_2024.csv`       | Tornado events aggregated by county-year | NOAA SPC   | count  | CSV    |
| **Landcover by County (1992–2021)**  | `landuse_by_county_1992_2021.csv`    | Percent cover by NLCD class              | USGS NLCD  | %      | CSV    |
| **Drought Summary (1895–2024)**      | `drought_summary_1895_2024.csv`      | Annual SPI / drought index               | NOAA + CPC | index  | CSV    |

---

## 🧮 Schema Standards

All tabular datasets conform to **MCP schema consistency rules** and column naming standards.

| Field          | Example               | Description                          |
| :------------- | :-------------------- | :----------------------------------- |
| `county_name`  | "Douglas County"      | County standardized to 2020 boundary |
| `fips_code`    | 20045                 | County FIPS identifier               |
| `year`         | 1993                  | Observation or record year           |
| `value`        | 874.5                 | Measurement value                    |
| `source`       | "NOAA NCEI"           | Origin dataset or authority          |
| `unit`         | "mm", "°C", "%"       | Measurement units                    |
| `derived_from` | `data/raw/precip.csv` | Provenance pointer                   |

Schemas follow **JSON Table Schema (CSVW)** + **STAC property extensions for tabular data**.
Validation occurs automatically during CI via `make validate-tabular`.

---

## 🌐 STAC Metadata

Every dataset includes a **STAC-compliant item** documenting schema, provenance, and lineage.

Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "tornado_counts_1950_2024",
  "properties": {
    "title": "Tornado Counts by County (1950–2024) – Kansas",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Cleaned tornado event counts aggregated by county and year, derived from NOAA SPC records.",
    "processing:software": "Python + Pandas",
    "mcp_provenance": "sha256:cbf98b…",
    "license": "CC-BY 4.0",
    "derived_from": ["data/raw/noaa_tornado_events.csv"]
  },
  "assets": {
    "data": {
      "href": "./tornado_counts_1950_2024.csv",
      "type": "text/csv"
    }
  }
}
```

---

## ⚙️ Processing Workflow

Data cleaning and harmonization are handled by `tools/tabular/` scripts
and the main project `Makefile`.
All scripts are executed in Dockerized environments with **Python 3.11 + Pandas + GDAL**.

Example pipeline:

```bash
# Clean population data
python tools/tabular/clean_population.py \
  --input data/raw/census_population.csv \
  --output data/processed/tabular/county_population_1850_2020.csv

# Join precipitation data with county boundaries
python tools/tabular/join_precip_counties.py \
  --input data/raw/precip_1895_2024.csv \
  --geo data/sources/ks_counties.geojson \
  --output data/processed/tabular/precipitation_trends_1895_2024.csv

# Aggregate tornado events
python tools/tabular/aggregate_tornado_counts.py \
  --input data/raw/tornado_events.csv \
  --output data/processed/tabular/tornado_counts_1950_2024.csv
```

---

## 🔁 Reproducibility & Validation

| Validation Type       | Method                | Purpose                              |
| :-------------------- | :-------------------- | :----------------------------------- |
| **Checksums**         | `.sha256` per dataset | Ensures binary integrity             |
| **Schema Validation** | JSON Table Schema     | Verifies structure & field types     |
| **STAC Validation**   | STAC 1.0 + MCP schema | Ensures compliance & linkage         |
| **CI Automation**     | GitHub Actions        | Validates metadata & checksums       |
| **Containerization**  | Docker environment    | Guarantees reproducibility           |
| **Cross-Validation**  | Archive comparison    | Confirms historical data consistency |

**Makefile Targets**

* `make tabular` → run ETL
* `make validate-tabular` → run schema + STAC validation

---

## 🤖 AI & Semantic Integration

KFM’s AI pipelines automatically process tabular datasets to:

* Extract named entities and semantic relationships.
* Map numeric series into the **Knowledge Graph** (e.g., population → region → time).
* Compute **confidence scores** and detect outliers in trends.
* Tag datasets with semantic metadata (domain = climate, demography, etc.).

All enrichments are stored in:
`data/processed/tabular/ai_metadata/`
and versioned for full auditability.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                        |
| :---------------------- | :---------------------------------------------------- |
| **Documentation-first** | README + STAC metadata per dataset                    |
| **Reproducibility**     | Containerized ETL + schema validation                 |
| **Open Standards**      | CSVW, JSON Table Schema, STAC 1.0                     |
| **Provenance**          | Embedded hashes, lineage, and derived-from references |
| **Auditability**        | CI/CD validation logs & reproducibility manifests     |

---

## 🧾 Version History

| Version   | Date       | Summary                                                                                          |
| :-------- | :--------- | :----------------------------------------------------------------------------------------------- |
| **2.0.0** | 2025-10-11 | Added front-matter metadata, Mermaid workflow, AI semantic integration, and MCP compliance table |
| 1.1.0     | 2025-08-20 | Schema updates and additional STAC metadata validation                                           |
| 1.0.0     | 2025-07-02 | Initial release: processed CSV datasets + checksums + STAC metadata                              |

---

## 📖 References

* **US Census Bureau:** [https://www.census.gov/data.html](https://www.census.gov/data.html)
* **NOAA NCEI:** [https://www.ncei.noaa.gov/](https://www.ncei.noaa.gov/)
* **USGS NLCD:** [https://www.mrlc.gov/data](https://www.mrlc.gov/data)
* **FEMA Open Data Portal:** [https://www.fema.gov/openfema-data-page](https://www.fema.gov/openfema-data-page)
* **CSVW / JSON Table Schema:** [https://www.w3.org/TR/tabular-data-primer/](https://www.w3.org/TR/tabular-data-primer/)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“Behind every map lies a table —
each row a fragment of Kansas history,
structured for discovery.”*

</div>
```
