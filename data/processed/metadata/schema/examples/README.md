<div align="center">

# 🧾 Kansas-Frontier-Matrix — Metadata Schema Examples (`data/processed/metadata/schema/examples/`)

**Mission:** Provide **practical JSON examples** demonstrating correct and incorrect implementations  
of metadata records validated against the **MCP + STAC hybrid schemas**.  
These examples act as **reference blueprints** for contributors creating new dataset metadata  
within the Kansas Frontier Matrix repository.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Purpose of Examples](#purpose-of-examples)
- [Valid Example Structure](#valid-example-structure)
- [Invalid Example Structure](#invalid-example-structure)
- [Usage in Validation](#usage-in-validation)
- [Best Practices](#best-practices)
- [References](#references)

---

## 🧠 Overview

This folder contains **reference JSON metadata examples** used to demonstrate  
how dataset metadata files should (and should not) conform to  
the **processed metadata schema** (`processed_item.schema.json`) and **STAC 1.0.0 standard**.

These examples serve both as:
- Learning tools for contributors building new metadata, and  
- Validation fixtures for automated schema testing in CI pipelines.

Each example clearly distinguishes between a **valid metadata file** (passes schema validation)  
and an **invalid example** (fails one or more validation checks), providing real-world context.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── metadata/
        └── schema/
            └── examples/
                ├── valid_metadata_example.json
                ├── invalid_metadata_example.json
                └── README.md
````

* `valid_metadata_example.json` — Demonstrates a complete, compliant metadata record.
* `invalid_metadata_example.json` — Illustrates typical errors or omissions that fail schema validation.

---

## 🎯 Purpose of Examples

* Serve as **templates** for creating metadata across project domains (terrain, climate, hazards, etc.).
* Provide **training data** for automated schema validation tools during CI testing.
* Help contributors quickly identify **missing fields**, **formatting mistakes**, and **schema violations**.
* Reinforce the MCP principle of **documentation-first reproducibility**.

---

## ✅ Valid Example Structure

### `valid_metadata_example.json`

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "terrain_slope_1m_ks",
  "properties": {
    "title": "Terrain Slope (1m) – Kansas LiDAR DEM",
    "datetime": "2020-01-01T00:00:00Z",
    "description": "Slope raster derived from 1m LiDAR DEM data using GDAL slope function.",
    "processing:software": "GDAL 3.8.0 + Python",
    "mcp_provenance": "sha256:a7c9e1...",
    "derived_from": ["data/raw/dem_1m_ks.tif"],
    "spatial_extent": [-102.05, 36.99, -94.59, 40.01],
    "temporal_extent": {"start": "2018-01-01", "end": "2020-12-31"},
    "license": "CC-BY 4.0",
    "keywords": ["DEM", "terrain", "slope", "Kansas"]
  },
  "assets": {
    "data": {
      "href": "../terrain_slope_1m_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

✅ **Passes validation because:**

* Includes all required MCP + STAC fields.
* `mcp_provenance` hash matches a corresponding `.sha256` file.
* `derived_from` correctly lists input dataset(s).
* Uses valid license and bounding box format.

---

## ❌ Invalid Example Structure

### `invalid_metadata_example.json`

```json
{
  "id": "terrain_slope_1m",
  "title": "Slope Map – Kansas",
  "description": "Missing required STAC fields and incorrect keys.",
  "processing-software": "GDAL",
  "license": "Proprietary",
  "spatial_extent": [102.05, 36.99, 94.59, 40.01]
}
```

❌ **Fails validation due to:**

* Missing `type` and `stac_version`.
* Invalid field name (`processing-software` instead of `processing:software`).
* Non-standard license (`"Proprietary"` violates open-data requirement).
* Incorrect bounding box order (W must precede E).
* No provenance or asset references.

---

## ⚙️ Usage in Validation

During CI/CD validation (`.github/workflows/stac-validate.yml`):

* `valid_metadata_example.json` must **pass all validation tests**.
* `invalid_metadata_example.json` must **fail intentionally** to confirm schema enforcement.

Developers can manually run schema validation with:

```bash
python tools/validate_json.py data/processed/metadata/schema/examples/valid_metadata_example.json
```

Results are logged in `validation_report.json` for automated reporting and QA review.

---

## 🧭 Best Practices

* Always validate new metadata against the latest schema before committing.
* Use the **valid example** as a template for creating new metadata files.
* Review the **invalid example** to avoid common formatting and naming mistakes.
* Maintain version control for schema and examples — changes to schema structure
  should always be paired with updated example files.
* Ensure licenses, bounding boxes, and derived source paths are accurate and traceable.

---

## 📖 References

* **STAC Specification 1.0.0:** [https://stacspec.org](https://stacspec.org)
* **JSON Schema (2020-12):** [https://json-schema.org](https://json-schema.org)
* **ISO 19115 Geospatial Metadata:** [https://www.iso.org/standard/53798.html](https://www.iso.org/standard/53798.html)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../../docs/standards/)
* **Kansas Frontier Matrix Metadata System:** [`data/processed/metadata/`](../../../../metadata/)

---

<div align="center">

*“Examples are the blueprint of reproducibility — every valid record echoes Kansas’s standard of scientific precision.”*

</div>
```

