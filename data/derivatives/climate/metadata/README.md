<div align="center">

# 🧮 Kansas Frontier Matrix — Climate Derivative Metadata  
`data/derivatives/climate/metadata/`

**Purpose:** Store structured metadata describing each processed **climate derivative artifact**  
(COG, GeoJSON, Parquet, CSV), linking them to their provenance, checksum, and STAC representation.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-brightgreen)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **machine-readable metadata JSON files** for all climate derivative outputs generated under  
`data/derivatives/climate/`. Each metadata file defines a dataset’s **origin, variables, temporal range, CRS, and relationships** to its checksum and STAC item.  

Metadata here serves as a bridge between the raw derivative files, their checksum manifests (`/checksums`),  
and the **STAC catalog** (`data/stac/`). It ensures the **traceability, reproducibility, and semantic integrity**  
of all derived climate products within the Kansas Frontier Matrix (KFM) pipeline.  

---

## 🧭 Metadata generation flow

```mermaid
flowchart TD
  A["Sources\nNOAA · Daymet · Normals"] --> B["ETL\nNormalize · Derive"]
  B --> C["Climate Derivatives\nCOG · GeoJSON · Parquet · CSV"]
  C --> D["Metadata JSONs\nvariables · CRS · temporal range · provenance"]
  D --> E["Checksums\n*.sha256 (validation)"]
  D --> F["STAC Items\nassets + metadata"]
  F --> G["Knowledge Graph\nnodes + relations"]
  G --> H["API + Web UI\ntimeline · search · layer metadata"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂 Directory layout

data/derivatives/climate/
├── metadata/
│   ├── daymet_1980_2024_tmin_ks.json
│   ├── daymet_1980_2024_prcp_ks.json
│   ├── normals_1991_2020_prcp.json
│   ├── drought_index_annual_ks.json
│   └── README.md
├── checksums/
└── *.tif · *.geojson · *.parquet · *.csv

Each .json metadata file corresponds directly to a processed artifact,
providing structured details aligned with STAC and DCAT schemas.

⸻

🧾 Metadata schema (JSON structure)

Each metadata file follows this standardized schema:

{
  "id": "daymet_1980_2024_tmin_ks",
  "title": "Daily Minimum Temperature (Daymet, 1980–2024, Kansas)",
  "description": "Derived daily minimum temperature (tmin) dataset aggregated for Kansas from NASA Daymet v4.",
  "type": "raster",
  "format": "COG",
  "file": "../daymet_1980_2024_tmin_ks_cog.tif",
  "checksum": "../checksums/daymet_1980_2024_tmin_ks_cog.tif.sha256",
  "source": "../../../sources/daymet.json",
  "stac_item": "../../../stac/items/daymet_1980_2024_tmin_ks.json",
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "temporal": {
    "start": "1980-01-01",
    "end": "2024-12-31"
  },
  "variables": [
    {
      "name": "tmin",
      "units": "°C",
      "description": "Daily minimum temperature"
    }
  ],
  "license": "CC-BY-4.0",
  "created": "2025-10-10",
  "mcp_stage": "derivatives"
}

🔍 Tip: Include human-readable descriptions and ensure field alignment with
data/sources/<source>.json and data/stac/items/<id>.json for STAC validation consistency.

⸻

🧩 Relationship to other metadata layers

Layer	Path	Purpose
Source Metadata	data/sources/	Defines raw dataset provenance (e.g., Daymet, NOAA).
Derivative Metadata	data/derivatives/climate/metadata/	Documents ETL-transformed products.
Checksums	data/derivatives/climate/checksums/	Ensures file integrity.
STAC Catalog	data/stac/	Registers assets with temporal & spatial metadata.
Knowledge Graph	(Neo4j)	Stores semantic links (HAS_DERIVATIVE, HAS_PROVENANCE).


⸻

🧠 Usage in pipeline
	•	ETL stage: Python ETL scripts create or update these .json metadata files automatically.
	•	Validation: STAC and JSON Schema validators confirm field presence, type, and alignment.
	•	CI/CD: The stac-validate.yml GitHub Action cross-checks that each derivative file has a metadata JSON entry and a matching checksum.
	•	Graph Load: During Neo4j ingestion, metadata properties are parsed to enrich graph nodes (e.g., temporal.start, variables.name).

⸻

🧱 Metadata best practices

Category	Guideline
✅ Completeness	Every climate derivative must have a metadata JSON file.
🔗 Linkage	Always reference its checksum, STAC item, and source manifest.
🕓 Timestamps	Include created and last_updated in ISO 8601 format.
🧮 Variables	Explicitly list all measured/derived variables with units.
🧾 Licensing	Record dataset-specific license terms (default: CC-BY-4.0).
🧪 Validation	Run make validate or CI to enforce schema conformity.


⸻

🔒 Reproducibility & MCP alignment

These metadata files fulfill MCP’s documentation-first requirement by encoding data provenance and semantics
in open formats (JSON, STAC, DCAT).
They make every derived dataset self-describing, verifiable, and linkable to its lineage,
as emphasized in KFM’s File and Data Architecture and Monorepo Design docs.

⸻

🧱 Related docs
	•	data/derivatives/climate/checksums/README.md — hash integrity workflow
	•	docs/architecture.md — ETL & data provenance chain
	•	data/stac/README.md — STAC catalog design
	•	data/sources/README.md — source manifest conventions

⸻

🗓 Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of climate derivative metadata schema & examples.