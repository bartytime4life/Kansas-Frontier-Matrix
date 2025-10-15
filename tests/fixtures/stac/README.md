<div align="center">

# 🗂️ Kansas Frontier Matrix — **STAC Fixtures**  
`tests/fixtures/stac/`

**STAC Collections · Items · JSON Schema Compliance**

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../../.github/workflows/tests.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • STAC Fixtures (tests/fixtures/stac/)"
version: "v1.0.0"
last_updated: "2025-10-14"
owners: ["@kfm-data", "@kfm-validation"]
tags: ["stac","fixtures","json","schema","metadata","mcp"]
license: "MIT"
semantic_alignment:
  - STAC 1.0.0
  - JSON Schema Draft-07
  - MCP-DL v6.2 Provenance + Validation Standards
---
````

---

## 🧭 Overview

The `tests/fixtures/stac/` directory contains **minimal and deterministic STAC Items and Collections** used to validate
metadata compliance within the Kansas Frontier Matrix (KFM) data pipeline.

These files serve as **canonical references** for schema validation, ingestion tests, and CI integrity checks.
They represent the **simplest valid STAC examples** that still pass **STAC 1.0.0** validation and KFM’s custom schema extensions.

> **Purpose:** Guarantee schema compliance and reproducibility across all STAC-based workflows — from data ingestion to frontend visualization.

---

## 🧱 Directory Structure

```text
tests/fixtures/stac/
├── stac_item_min.json           # Minimal valid STAC Item (Feature)
├── stac_collection_min.json     # Minimal valid STAC Collection
├── stac_item_ai_example.json    # Example with AI metadata extension
├── stac_item_provenance.json    # Example with provenance properties
└── README.md                    # This documentation file
```

---

## 🧩 Fixture Descriptions

| File                        | Type            | Description                                                | Schema                      | Usage                          |
| :-------------------------- | :-------------- | :--------------------------------------------------------- | :-------------------------- | :----------------------------- |
| `stac_item_min.json`        | STAC Item       | Minimal valid Item (single raster asset)                   | STAC 1.0.0                  | Unit & schema tests            |
| `stac_collection_min.json`  | STAC Collection | Minimal Collection definition with spatial/temporal extent | STAC 1.0.0                  | Integration + validation       |
| `stac_item_ai_example.json` | STAC Item       | Demonstrates AI metadata extension                         | STAC 1.0 + KFM-AI Extension | AI provenance and NLP tests    |
| `stac_item_provenance.json` | STAC Item       | Includes `prov:wasDerivedFrom` and lineage fields          | STAC 1.0 + PROV-O alignment | Provenance tracking validation |

---

## 🧠 Example — `stac_item_min.json`

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "usgs_topo_larned_1894",
  "properties": {
    "datetime": "1894-01-01T00:00:00Z",
    "proj:epsg": 4326
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-99.4, 38.1],
      [-99.0, 38.1],
      [-99.0, 38.4],
      [-99.4, 38.4],
      [-99.4, 38.1]
    ]]
  },
  "bbox": [-99.4, 38.1, -99.0, 38.4],
  "links": [],
  "assets": {
    "cog": {
      "href": "data/cogs/usgs_topo_larned_1894.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

> A fully schema-valid STAC Item used in multiple tests for STAC compliance, schema evolution, and JSON structure checks.

---

## 🧩 Example — `stac_collection_min.json`

```json
{
  "stac_version": "1.0.0",
  "id": "historic_topo_maps",
  "type": "Collection",
  "description": "A sample collection of historic Kansas topographic maps.",
  "license": "Public Domain",
  "extent": {
    "spatial": { "bbox": [[-102.05, 36.99, -94.6, 40.0]] },
    "temporal": { "interval": [["1890-01-01T00:00:00Z", "1905-12-31T23:59:59Z"]] }
  },
  "links": [],
  "summaries": { "proj:epsg": [4326] }
}
```

> Provides minimal coverage of required fields, ensuring compliance with the STAC Collection schema.

---

## 🧪 Testing Integration

These STAC fixtures are consumed by:

* `tools/validate_stac.py` — schema and STAC validation tests
* `tools/build_config.py` — web UI sync tests (layers + STAC assets)
* `tests/tools/test_validate_stac.py` — integration test coverage
* CI workflows — validation logs included in test artifacts

**Example validation snippet:**

```python
from pystac import Item
from pathlib import Path

def test_stac_item_valid(fixtures_dir):
    item_path = Path(fixtures_dir) / "stac/stac_item_min.json"
    item = Item.from_file(item_path)
    item.validate()  # raises no exceptions if valid
```

---

## 🧩 Provenance & Metadata Example (`stac_item_provenance.json`)

```json
{
  "type": "Feature",
  "id": "treaty_boundaries_overlay",
  "properties": {
    "datetime": "1850-01-01T00:00:00Z",
    "prov:wasDerivedFrom": ["data/raw/treaty_maps_original.tif"],
    "kfm:processedBy": "convert_gis.py",
    "kfm:checksum:sha256": "e4b9f1..."
  },
  "assets": {
    "overlay": {
      "href": "data/processed/maps/treaty_overlay.svg",
      "type": "image/svg+xml",
      "roles": ["visual"]
    }
  },
  "bbox": [-100.0, 37.0, -95.0, 40.0]
}
```

> Demonstrates provenance alignment between STAC and PROV-O ontologies (key MCP compliance element).

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                       |
| :--------------- | :------------------------------------------------ |
| **Inputs**       | Synthetic STAC JSONs, minimal schema examples     |
| **Outputs**      | Schema-validated, CI-tested STAC fixtures         |
| **Dependencies** | PySTAC, JSONSchema, pytest                        |
| **Integrity**    | SHA256 checksums stored per fixture               |
| **Traceability** | Metadata links each file to STAC schema commit ID |

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                          |
| :------------------ | :------------------------------------------------------ |
| Documentation-first | Each fixture documented with schema alignment           |
| Reproducibility     | Deterministic JSON + validated structure                |
| Provenance          | Lineage fields (`prov:wasDerivedFrom`) and checksums    |
| Open Standards      | STAC 1.0.0, JSON Schema Draft-07                        |
| Accessibility       | UTF-8 encoded, minimal, human-readable JSON             |
| Auditability        | CI validation reports published with schema version tag |

---

<div align="center">

🗂️ **Every STAC fixture is a contract.**
These minimal examples guarantee Kansas Frontier Matrix stays aligned with global metadata standards.

</div>
```

