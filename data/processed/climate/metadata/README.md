<div align="center">

# 🌦️ Kansas Frontier Matrix — Processed Climate Metadata  
`data/processed/climate/metadata/`

**Mission:** Maintain authoritative **metadata records** for all processed climate datasets — documenting  
provenance, spatial/temporal coverage, and processing lineage — to ensure every dataset in Kansas Frontier Matrix  
is **auditable, interoperable, and reproducible** in accordance with MCP and STAC standards.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Metadata Schema](#metadata-schema)
- [STAC Integration](#stac-integration)
- [Validation & Provenance](#validation--provenance)
- [Adding or Updating Metadata](#adding-or-updating-metadata)
- [Version History](#version-history)
- [References](#references)

---

## 🧠 Overview

This folder stores **JSON metadata records** describing each processed climate dataset in  
`data/processed/climate/`. Every file documents the dataset’s **lineage**, **source inputs**,  
**processing tools**, and **checksum provenance**, establishing a transparent, machine-readable record  
of the entire ETL workflow.

These metadata files serve as the canonical registry for the **Climate Collection** within KFM,  
automatically synchronized to the STAC catalog and linked to checksums and source datasets via MCP provenance.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── climate/
        └── metadata/
            ├── temp_mean_annual_1895_2024.json
            ├── precip_total_annual_1895_2024.json
            ├── drought_spi12_1895_2024.json
            ├── climate_normals_1991_2020.json
            ├── template.json
            └── README.md

Each file represents one dataset in data/processed/climate/, describing its provenance,
lineage, and processing configuration. template.json provides a scaffold for new metadata.

⸻

🧩 Metadata Schema

Each metadata file conforms to the MCP–STAC hybrid schema, blending reproducibility metadata (MCP)
with spatial/temporal discoverability (STAC).

Example JSON

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "precip_total_annual_1895_2024",
  "properties": {
    "title": "Total Annual Precipitation (1895–2024) – Kansas",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Gridded total annual precipitation for Kansas aggregated from NOAA and PRISM datasets.",
    "processing:software": "Python + xarray + rasterio + GDAL 3.8.0",
    "mcp_provenance": "sha256:4bd72e4e...",
    "license": "CC-BY 4.0",
    "derived_from": [
      "data/raw/noaa_precip_1895_2024.csv",
      "data/raw/prism_precip_monthly.nc"
    ],
    "temporal_extent": { "start": "1895-01-01", "end": "2024-12-31" },
    "spatial_extent": [-102.05, 36.99, -94.59, 40.01],
    "keywords": ["precipitation", "climate", "Kansas", "PRISM", "NOAA"]
  },
  "assets": {
    "data": {
      "href": "../precip_total_annual_1895_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}

Required Fields

Field	Description	Example
id	Unique dataset identifier	"temp_mean_annual_1895_2024"
title	Descriptive dataset title	"Mean Annual Temperature (1895–2024) – Kansas"
description	Dataset summary	"Derived from NOAA NCEI and PRISM data"
datetime	Reference or processing date	"2024-01-01T00:00:00Z"
derived_from	Source datasets	["data/raw/prism_temp_monthly.nc"]
processing:software	Tools used in generation	"Python + xarray + rasterio"
mcp_provenance	Checksum reference	"sha256:de23a9..."
license	Dataset license	"CC-BY 4.0"
spatial_extent	Bounding box [W, S, E, N]	[-102.05, 36.99, -94.59, 40.01]
temporal_extent	Coverage range	{"start": "1895-01-01", "end": "2024-12-31"}


⸻

🌐 STAC Integration

Each metadata record is mirrored as a STAC Item under data/stac/items/climate_*.
This allows:
	•	Spatial and temporal filtering of datasets
	•	Keyword-based discovery ("precipitation", "drought", etc.)
	•	Automated ingestion into visualization and API layers
	•	Direct provenance linking to raw and derivative datasets

🧩 The STAC index rebuilds automatically via GitHub Actions upon metadata additions.

⸻

🔍 Validation & Provenance

Validation ensures metadata adheres to MCP and STAC schema standards.
	1.	Schema Validation: JSON checked for required structure and types.
	2.	Checksum Match: mcp_provenance hash validated against .sha256 files.
	3.	Temporal Extent Check: Confirms metadata coverage aligns with dataset content.
	4.	License Verification: Ensures license inheritance from source datasets.

Run validations locally:

make validate-climate

A validation_report.json is generated with summary results.

⸻

🧠 Adding or Updating Metadata
	1.	Copy template.json and rename to the dataset ID.
	2.	Fill all required fields (see schema).
	3.	Include dataset checksum (mcp_provenance).
	4.	Validate with:

make validate-climate


	5.	Commit both metadata and data updates, then open a Pull Request.
CI/CD automatically enforces STAC and MCP compliance.

When reprocessing data: update both the .sha256 and the metadata mcp_provenance and datetime.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Enhanced schema documentation and CI validation integration.
1.0.0	2025-10-04	Initial processed climate metadata documentation and files.


⸻

📖 References
	•	STAC Specification 1.0: https://stacspec.org
	•	NOAA NCEI: https://www.ncei.noaa.gov/
	•	PRISM Climate Group: https://prism.oregonstate.edu/
	•	NASA Daymet: https://daac.ornl.gov/DAYMET/
	•	xarray: https://docs.xarray.dev/
	•	JSON Schema: https://json-schema.org
	•	MCP Standards: ../../../../docs/standards/

⸻


<div align="center">


“Every temperature, every raindrop — these metadata records preserve the provenance of Kansas’s climate story.”
📍 data/processed/climate/metadata/

</div>
```