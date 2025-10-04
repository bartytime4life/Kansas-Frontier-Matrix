<div align="center">

# 🧾 Kansas-Frontier-Matrix — Processed Tabular Data (`data/processed/tabular/`)

**Mission:** Contain all **cleaned, structured, and analysis-ready tabular datasets** —  
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
- [Directory Layout](#directory-layout)
- [Core Tabular Datasets](#core-tabular-datasets)
- [Schema Standards](#schema-standards)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Tabular Data](#contributing-new-tabular-data)
- [References](#references)

---

## 📊 Overview

This subdirectory holds **processed tabular datasets** that have been cleaned,  
validated, and formatted for integration with Kansas-Frontier-Matrix’s analytical layers.  

These include **climate time series**, **demographic tables**, **ecological metrics**,  
and **cross-domain data joins** linking geography, history, and environmental data.  

All datasets here have:
- standardized column names and units,  
- explicit metadata (schema + provenance),  
- and format compatibility with CSV, JSON, and Parquet for downstream use.  

These files serve as **structured analytical bridges** between raw data and the knowledge graph.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── tabular/
        ├── county_population_1850_2020.csv       # Historical population by county
        ├── precipitation_trends_1895_2024.csv    # Annual precipitation trend data
        ├── tornado_counts_1950_2024.csv          # Tornado event counts by county/year
        ├── landuse_by_county_1992_2021.csv       # Landcover class percentages
        ├── drought_summary_1895_2024.csv         # Drought SPI summary by year
        ├── metadata/
        │   ├── county_population_1850_2020.json
        │   ├── tornado_counts_1950_2024.json
        │   └── landuse_by_county_1992_2021.json
        ├── checksums/
        │   ├── county_population_1850_2020.csv.sha256
        │   ├── precipitation_trends_1895_2024.csv.sha256
        │   └── tornado_counts_1950_2024.csv.sha256
        └── README.md
````

---

## 🧩 Core Tabular Datasets

| Dataset                              | File                                 | Description                                  | Source     | Units  | Format |
| ------------------------------------ | ------------------------------------ | -------------------------------------------- | ---------- | ------ | ------ |
| **County Population (1850–2020)**    | `county_population_1850_2020.csv`    | Decennial population by county               | US Census  | people | CSV    |
| **Precipitation Trends (1895–2024)** | `precipitation_trends_1895_2024.csv` | Annual precipitation anomaly per county      | NOAA NCEI  | mm     | CSV    |
| **Tornado Counts (1950–2024)**       | `tornado_counts_1950_2024.csv`       | Tornado events aggregated by county and year | NOAA SPC   | count  | CSV    |
| **Landcover by County (1992–2021)**  | `landuse_by_county_1992_2021.csv`    | Percent cover by NLCD class                  | USGS NLCD  | %      | CSV    |
| **Drought Summary (1895–2024)**      | `drought_summary_1895_2024.csv`      | Annual SPI and drought occurrence index      | NOAA + CPC | index  | CSV    |

---

## 🧮 Schema Standards

All tabular datasets follow **MCP schema consistency rules** and column naming conventions:

| Field Type     | Example               | Description                                  |
| -------------- | --------------------- | -------------------------------------------- |
| `county_name`  | "Douglas County"      | County name standardized to 2020 boundaries  |
| `fips_code`    | 20045                 | County FIPS identifier                       |
| `year`         | 1993                  | Observation or record year                   |
| `value`        | 874.5                 | Measurement value (unit defined in metadata) |
| `source`       | "NOAA NCEI"           | Originating dataset                          |
| `unit`         | "mm", "°C", "%"       | Measurement units                            |
| `derived_from` | `data/raw/precip.csv` | Provenance pointer                           |

Metadata JSON files define these fields in alignment with the **JSON Table Schema (CSVW)**
and STAC property extensions for tabular data.

---

## 🌐 STAC Metadata

Each CSV dataset has an accompanying **STAC metadata file** describing
source lineage, schema, and data type (tabular asset).

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

All processing and cleaning are performed via `tools/tabular/` scripts and the project `Makefile`.
Typical tools include **Pandas**, **NumPy**, and **CSVKit**, executed in a Dockerized Python environment.

Example pipeline:

```bash
# 1. Clean raw population table
python tools/tabular/clean_population.py --input data/raw/census_population.csv \
  --output data/processed/tabular/county_population_1850_2020.csv

# 2. Join NOAA precipitation time series with county boundaries
python tools/tabular/join_precip_counties.py --input data/raw/precip_1895_2024.csv \
  --geo data/sources/ks_counties.geojson \
  --output data/processed/tabular/precipitation_trends_1895_2024.csv

# 3. Aggregate tornado events by county-year
python tools/tabular/aggregate_tornado_counts.py --input data/raw/tornado_events.csv \
  --output data/processed/tabular/tornado_counts_1950_2024.csv
```

---

## 🔁 Reproducibility & Validation

* **Checksums:** Each CSV includes a `.sha256` integrity hash.
* **Schema Validation:** CI validates all CSVs using JSON Table Schema definitions.
* **STAC Validation:** Each metadata file tested for STAC 1.0 compliance.
* **Makefile Targets:**

  * `make tabular` → runs tabular ETL pipeline
  * `make validate-tabular` → checks schema and STAC metadata
* **Containerization:** Executed in Docker (Python + Pandas + GDAL).
* **Cross-Validation:** Datasets checked against historical archives and official statistics for accuracy.

---

## 🧠 Contributing New Tabular Data

1. Add the processed CSV/Parquet file here.
2. Include:

   * `.sha256` checksum under `checksums/`
   * STAC metadata JSON under `metadata/`
   * Schema definition or reference (if new structure).
3. Run validation:

   ```bash
   make validate-tabular
   ```
4. Document the source, schema, and transformation steps in a short `DERIVATION.md`.
5. Submit a PR with data source citations, schema updates, and licensing info.

---

## 📖 References

* **US Census Bureau Data:** [https://www.census.gov/data.html](https://www.census.gov/data.html)
* **NOAA National Centers for Environmental Information (NCEI):** [https://www.ncei.noaa.gov/](https://www.ncei.noaa.gov/)
* **USGS National Land Cover Database (NLCD):** [https://www.mrlc.gov/data](https://www.mrlc.gov/data)
* **FEMA Open Data Portal:** [https://www.fema.gov/openfema-data-page](https://www.fema.gov/openfema-data-page)
* **CSVW JSON Table Schema:** [https://www.w3.org/TR/tabular-data-primer/](https://www.w3.org/TR/tabular-data-primer/)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“Behind every map lies a table — each row a fragment of Kansas history, structured for discovery.”*

</div>
```

