<div align="center">

# 🌦️ Kansas Frontier Matrix — Normalized Climate Data  
`data/work/staging/tabular/normalized/climate/`

**“Tracing Kansas climate across time and terrain.”**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This subdirectory stores **normalized climate and weather observation tables** produced during the ETL pipeline.  
These datasets unify multiple climate sources into standardized columns, datatypes, and spatial-temporal identifiers  
for seamless integration with geospatial layers and historical event records.

Examples of included datasets:

- **NOAA NCEI GHCN-Daily** – Daily station observations (temperature, precipitation, snowfall, etc.).  
- **NASA Daymet v4** – Gridded daily weather parameters (temperature, radiation, vapor pressure, etc.).  
- **NOAA Climate Normals (1991–2020)** – 30-year baseline summaries for context and anomaly detection.  
- **Drought and precipitation indices** (SPI, PDSI) from the Kansas Mesonet and National Climate Data Center.  

---

## 🧩 Workflow Context

```mermaid
flowchart LR
  A["data/raw/climate/*.csv\n(GHCN, Daymet, Normals)"] --> B["Normalization\nscripts/normalize_climate.py"]
  B --> C["data/work/staging/tabular/normalized/climate/\nstandardized CSVs (aligned schema)"]
  C --> D["data/work/staging/tabular/validation/\nQA Reports + Checksums"]
  D --> E["data/processed/climate/\nready for STAC + Visualization"]
%% END OF MERMAID
````

**Automation:**
Normalization runs via `make tabular-normalize` or `make climate-normalize`, which calls
`scripts/normalize_climate.py` to standardize headers, encode datatypes, convert timestamps,
and append provenance metadata.

---

## 🗂️ Directory Layout

```bash
data/work/staging/tabular/normalized/climate/
├── README.md                     # This documentation
├── noaa_ghcn_daily.csv           # Station-based daily weather records
├── daymet_daily_summary.csv      # Gridded weather summaries (1 km)
├── climate_normals_1991_2020.csv # NOAA 30-year baselines
├── drought_indices.csv           # SPI / PDSI indices
├── metadata/                     # JSON metadata for each dataset
└── tmp/                          # Temporary or batch-run files (ignored in Git)
```

---

## ⚙️ Usage

```bash
# Normalize all climate datasets
make climate-normalize

# Normalize a specific dataset manually
python scripts/normalize_climate.py \
  --input ../../../raw/climate/noaa_ghcn_daily.csv \
  --schema ../../../validation/schemas/climate.schema.json \
  --output ./noaa_ghcn_daily.csv

# Summarize normalization results
python scripts/describe_csv.py --input ./daymet_daily_summary.csv
```

Outputs include:

* `*_normalized.csv` — cleaned, type-consistent tables
* `*.meta.json` — dataset metadata and schema
* log entries appended to `../validation/summary.log`

---

## 🧾 Standards & Schema Alignment

| Standard        | Function                                                  |
| --------------- | --------------------------------------------------------- |
| **CSVW**        | Defines columns, datatypes, and measurement units         |
| **JSON-Schema** | Validates normalized tables in next stage                 |
| **STAC**        | Adds discoverability and temporal metadata                |
| **OWL-Time**    | Encodes precise or interval-based timestamps              |
| **CIDOC CRM**   | Links climate phenomena to historical events and entities |

Each normalized file includes the following core columns:

| Column             | Description                            |
| ------------------ | -------------------------------------- |
| `station_id`       | Unique climate station or grid cell ID |
| `date`             | ISO-8601 date (UTC)                    |
| `tmin_c`, `tmax_c` | Min/Max temperature (°C)               |
| `precip_mm`        | Precipitation (mm/day)                 |
| `snow_mm`          | Snowfall (mm/day)                      |
| `source`           | Data origin (e.g., NOAA, NASA)         |
| `etl_commit`       | Git commit hash of ETL process         |
| `ingested_at`      | Timestamp of normalization             |

---

## 🔍 Provenance & Integrity

Every file carries associated artifacts:

| Artifact      | Purpose                                               |
| ------------- | ----------------------------------------------------- |
| `*.meta.json` | Dataset-level metadata (schema, source, coverage)     |
| `*.sha256`    | Checksum manifest for integrity                       |
| `summary.log` | Normalization summary with record counts & timestamps |

Example provenance snippet:

```json
{
  "dataset": "noaa_ghcn_daily",
  "normalized_at": "2025-10-09T00:00:00Z",
  "records": 23542,
  "etl_commit": "{{ GIT_COMMIT }}",
  "sha256": "9bfcae...e89a",
  "status": "normalized"
}
```

---

## 🧠 Related Documentation

* [Normalized Tabular Overview](../README.md)
* [Validation Workspace](../../validation/README.md)
* [Architecture Overview](../../../../../../docs/architecture.md)
* [Data Sources: Climate & Hazards](../../../../../sources/README.md)
* [STAC Catalog](../../../../../stac/catalog.json)

---

## 🪪 License

All normalized climate datasets are released under **CC-BY-4.0** unless otherwise stated.
When reusing, please credit **Kansas Frontier Matrix (KFM)** and relevant data providers (NOAA, NASA, etc.).
