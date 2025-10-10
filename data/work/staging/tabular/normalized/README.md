<div align="center">

# 🧮 Kansas Frontier Matrix — Normalized Tabular Data  
`data/work/staging/tabular/normalized/`

**“From messy CSVs to meaningful structure.”**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 Purpose

The `normalized/` layer holds **clean, standardized CSVs or Parquet files** derived from the `data/raw/` sources.  
These files are formatted for interoperability, validation, and ingestion into higher layers like:

- the **Knowledge Graph (Neo4j)** for entity linking and CIDOC CRM mapping  
- **GIS/STAC** layers for geospatial-temporal indexing  
- **Visualization tools** (timeline, map, AI summaries)

Each dataset here is *normalized but not yet fully validated*; the next step occurs in  
[`../validation/`](../validation/) where JSON-Schema checks and checksum verification are run.

---

## 🧩 Workflow Context

```mermaid
flowchart LR
  A["data/raw/\nraw CSVs & XLS"] --> B["Normalize\nscripts/normalize_tabular.py"]
  B --> C["data/work/staging/tabular/normalized/\nclean CSVs (standard schema)"]
  C --> D["data/work/staging/tabular/validation/\nJSON-Schema QA"]
  D --> E["data/processed/\nfinal CSVs + STAC Items"]
%% END OF MERMAID
````

**Automation:**
Normalization runs automatically as part of `make tabular-normalize`, which applies consistent
column naming, encoding (`UTF-8`), and field type casting across all tabular datasets.

---

## 📁 Directory Layout

```bash
data/work/staging/tabular/normalized/
├── README.md                  # This file
├── climate/                   # e.g., NOAA, Daymet station datasets
├── hydrology/                 # USGS/NWIS discharge or groundwater tables
├── treaties/                  # Parsed treaty and land-cession tables
├── demographics/              # Census or population records
└── tmp/                       # Working files (excluded from Git)
```

---

## ⚙️ Usage

```bash
# Normalize all raw tabular datasets
make tabular-normalize

# Normalize a specific dataset
python scripts/normalize_tabular.py --input ../../raw/usgs_hydro.csv --schema schemas/usgs_hydro.schema.json --output ./hydrology/

# Generate schema summary and stats
python scripts/describe_csv.py --input ./climate/daymet_ks.csv
```

Normalization steps include:

* Standardize **headers** (snake_case, ASCII)
* Enforce **ISO-8601 dates** and numeric types
* Append provenance columns (`source`, `etl_commit`, `ingested_at`)
* Detect and log anomalies to `../validation/reports/`

---

## 🧾 Standards & Schema

| Standard        | Purpose                                              |
| --------------- | ---------------------------------------------------- |
| **CSVW**        | Defines columns, datatypes, units                    |
| **JSON-Schema** | Structural validation & auto-QA in next stage        |
| **DCAT**        | Dataset metadata and lineage                         |
| **CIDOC CRM**   | Semantic model for entities (events, people, places) |
| **OWL-Time**    | Temporal modeling of dates and intervals             |

Each normalized file is accompanied by a `.meta.json` file describing schema, source, and time coverage.
Schema definitions are stored in `../validation/schemas/`.

---

## 🔍 Provenance & Integrity

| Artifact      | Description                  | Integrity Check       |
| ------------- | ---------------------------- | --------------------- |
| `*.csv`       | Normalized tabular output    | SHA-256 checksums     |
| `*.meta.json` | Schema & provenance metadata | JSON-Schema           |
| `summary.log` | ETL normalization summary    | Git-tracked timestamp |

Each normalization run appends an entry to `summary.log` with commit hash and record counts.
Example entry:

```json
{
  "dataset": "noaa_stations_ks",
  "normalized_at": "2025-10-09T00:00:00Z",
  "records": 18453,
  "etl_commit": "{{ GIT_COMMIT }}",
  "sha256": "e4f98d...b20",
  "status": "normalized"
}
```

---

## 🧠 Related Documentation

* [Validation Workspace](../validation/README.md)
* [ETL Pipeline SOP](../../../../../docs/sop.md)
* [Architecture Overview](../../../../../docs/architecture.md)
* [STAC Catalog](../../../../stac/catalog.json)

---

## 🪪 License

All normalized datasets and derived works are distributed under **CC-BY-4.0** unless otherwise noted.
Users must credit *Kansas Frontier Matrix* when redistributing normalized data products.
