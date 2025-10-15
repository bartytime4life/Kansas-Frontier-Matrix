<div align="center">

# 🌐 Kansas Frontier Matrix — **Source Manifest Fixtures**  
`tests/fixtures/sources/`

**Data Source Manifests · Download Metadata · Fetch Tests**

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../../.github/workflows/tests.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Source Manifest Fixtures (tests/fixtures/sources/)"
version: "v1.0.0"
last_updated: "2025-10-14"
owners: ["@kfm-data", "@kfm-ingestion"]
tags: ["sources","manifests","fetch","fixtures","data","mcp"]
license: "MIT"
semantic_alignment:
  - FAIR Data Principles (Reproducible Source Metadata)
  - MCP-DL v6.2 Provenance Documentation
  - STAC-Compatible Data Ingestion
---
````

---

## 🧭 Overview

The `tests/fixtures/sources/` directory contains **mock source manifests** used to test
KFM’s **data ingestion** and **fetch utilities** — particularly the `tools/fetch_data.py`
and `validate_stac.py` scripts.

Each manifest represents a **single data source** (e.g., USGS map, NOAA dataset) and provides
a compact, deterministic example of KFM’s **data/sources/*.json** structure.

> **Purpose:** Validate that manifest parsing, HTTP fetching, and provenance logging work identically across environments — without contacting real external APIs.

---

## 🧱 Directory Structure

```text
tests/fixtures/sources/
├── usgs_topo_sample.json      # Example USGS topographic dataset
├── noaa_climate_sample.json   # Example NOAA climate data manifest
├── treaty_boundaries_sample.json # Example vector data source manifest
└── README.md                  # This documentation file
```

---

## 🧩 Manifest Schema (Simplified)

Every manifest fixture mirrors the `data/sources/schema/source.schema.json` specification.

| Field         | Type   | Description                 | Example                                                 |
| :------------ | :----- | :-------------------------- | :------------------------------------------------------ |
| `id`          | string | Unique dataset identifier   | `"usgs_topo_larned_1894"`                               |
| `title`       | string | Descriptive name            | `"USGS Topographic Map (Larned, 1894)"`                 |
| `description` | string | Summary of dataset content  | `"Historic topographic map scanned and georeferenced."` |
| `license`     | string | License or usage rights     | `"Public Domain"`                                       |
| `source`      | object | Links to primary data files | `{"url": "https://example.org/data.tif"}`               |
| `format`      | string | File format type            | `"GeoTIFF"`                                             |
| `category`    | string | Thematic classification     | `"Topography"`                                          |
| `contact`     | string | Data provider or curator    | `"U.S. Geological Survey"`                              |
| `created`     | string | ISO 8601 creation date      | `"1894-01-01T00:00:00Z"`                                |

---

## 🧠 Example Fixture — `usgs_topo_sample.json`

```json
{
  "id": "usgs_topo_larned_1894",
  "title": "USGS Topographic Map (Larned, 1894)",
  "description": "Historic topographic survey of Larned, Kansas digitized from the USGS archive.",
  "license": "Public Domain",
  "format": "GeoTIFF",
  "category": "Topography",
  "contact": "U.S. Geological Survey",
  "source": {
    "url": "https://example.org/data/usgs_topo_larned_1894.tif",
    "checksum": "sha256:e4b9f1...",
    "size": 51200
  },
  "created": "1894-01-01T00:00:00Z"
}
```

> Used in tests to mock a valid data source download without hitting external endpoints.

---

## 🧩 Example Fixture — `noaa_climate_sample.json`

```json
{
  "id": "noaa_kansas_precip_1936",
  "title": "NOAA Kansas Precipitation Data (1936)",
  "description": "Daily precipitation values collected during the Dust Bowl period.",
  "license": "Public Domain",
  "format": "CSV",
  "category": "Climate",
  "contact": "National Oceanic and Atmospheric Administration",
  "source": {
    "url": "https://example.org/data/noaa_kansas_precip_1936.csv",
    "checksum": "sha256:11af2e...",
    "size": 2048
  },
  "created": "1936-01-01T00:00:00Z"
}
```

> Ensures the `fetch_data.py` utility correctly handles tabular file downloads and checksum validation.

---

## 🧪 Usage in Tests

These fixtures support integration and unit tests for data ingestion:

### ✅ Example — Python (Pytest)

```python
from tools.fetch_data import fetch_manifest
import json

def test_manifest_parsing(fixtures_dir):
    manifest = json.loads((fixtures_dir / "sources/usgs_topo_sample.json").read_text())
    assert manifest["id"].startswith("usgs_topo")
    assert manifest["license"] == "Public Domain"
```

### ✅ Example — CLI Test

```bash
pytest tools/tests/test_fetch_data.py::test_fetch_manifest
```

### ✅ Example — Schema Validation

```python
from jsonschema import validate
from tools.utils.schemas import SOURCE_SCHEMA

def test_source_manifest_valid(fixtures_dir):
    manifest = json.loads((fixtures_dir / "sources/noaa_climate_sample.json").read_text())
    validate(instance=manifest, schema=SOURCE_SCHEMA)
```

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                                        |
| :--------------- | :----------------------------------------------------------------- |
| **Inputs**       | Synthetic JSON manifests (mocked source data definitions)          |
| **Outputs**      | Validated source manifests for ingestion tests                     |
| **Dependencies** | pytest, jsonschema, requests-mock                                  |
| **Integrity**    | SHA256 checksums embedded in `source.url` objects                  |
| **Traceability** | All manifests linked to real dataset archetypes in `data/sources/` |

---

## ♿ Accessibility & Compliance

* UTF-8 encoded JSON
* Uses human-readable field names and descriptions
* Metadata compatible with **STAC Extensions** (`data`, `provenance`, `license`)
* Accessible documentation and schema descriptions under `data/sources/schema/`

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                        |
| :------------------ | :---------------------------------------------------- |
| Documentation-first | Every manifest includes structured metadata           |
| Provenance          | SHA256 and dataset lineage embedded in source entries |
| Reproducibility     | Deterministic fixtures ensure stable testing          |
| Open Standards      | JSON + STAC-compatible schema                         |
| Accessibility       | Human-readable, schema-validated, UTF-8 compliant     |
| Auditability        | CI logs validate all manifests during tests.yml run   |

---

<div align="center">

🌐 **Source fixtures prove the pipeline works before the data flows.**
*They are the fingerprints of reproducible ingestion.*

</div>
```

