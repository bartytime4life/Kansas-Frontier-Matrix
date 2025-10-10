<div align="center">

# 🧮 Kansas Frontier Matrix — Climate Derivative Metadata  
`data/derivatives/climate/metadata/`

**Purpose:** Store structured metadata describing each processed **climate derivative artifact**  
(COG · GeoJSON · Parquet · CSV) and link them to their **provenance, checksum, and STAC representations**.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `metadata/` directory contains **machine-readable JSON metadata files** describing each processed climate derivative product generated under `data/derivatives/climate/`.  

Each file documents:
- dataset **origin and lineage**
- **variables**, units, and time range  
- **coordinate system and spatial bounds**
- links to its **checksum** and **STAC item**

These metadata files act as the connective tissue between:
- the raw climate derivative files  
- their integrity manifests (`/checksums`)  
- and the **STAC catalog** (`data/stac/`)  

They ensure **traceability, reproducibility, and semantic interoperability** across the Kansas Frontier Matrix (KFM) ecosystem.

---

## 🧭 Metadata Generation Flow

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

🗂️ Directory Layout

metadata/
├── daymet_1980_2024_tmin_ks.json
├── daymet_1980_2024_prcp_ks.json
├── normals_1991_2020_prcp.json
├── drought_index_annual_ks.json
└── README.md

Each .json file corresponds directly to a derivative dataset and follows the KFM STAC/DCAT-aligned schema.

⸻

🧾 JSON Metadata Schema

Below is the canonical metadata schema structure:

{
  "id": "daymet_1980_2024_tmin_ks",
  "title": "Daily Minimum Temperature (Daymet, 1980–2024, Kansas)",
  "description": "Derived daily minimum temperature dataset aggregated for Kansas from NASA Daymet v4.",
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

💡 Tip: Ensure file, checksum, and stac_item paths are relative and that metadata values align with
data/sources/<source>.json and data/stac/items/<id>.json for validation consistency.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
🧭 Source Metadata	data/sources/	Defines raw dataset provenance (Daymet, NOAA, etc.)
🧮 Derivative Metadata	data/derivatives/climate/metadata/	Documents ETL-processed products
🧾 Checksums	data/derivatives/climate/checksums/	Ensures file integrity
🗺️ STAC Catalog	data/stac/	Registers assets with spatial + temporal metadata
🧠 Knowledge Graph	(Neo4j)	Stores semantic links (HAS_DERIVATIVE, HAS_PROVENANCE)


⸻

🧠 Usage in the Pipeline
	•	ETL Stage: Python ETL scripts auto-generate or update metadata after processing.
	•	Validation: JSON Schema and STAC validators ensure structural compliance.
	•	CI/CD: The stac-validate.yml workflow checks that every derivative file has matching metadata and checksum.
	•	Graph Load: Neo4j ingestion parses these JSON files, linking metadata fields (e.g., temporal.start, variables.name) to entity nodes.

⸻

🧱 Metadata Best Practices

Category	Guideline
✅ Completeness	Every derivative must have an accompanying metadata JSON file.
🔗 Linkage	Always reference its checksum, STAC item, and source manifest.
🕓 Timestamps	Include created and last_updated (ISO 8601).
🧮 Variables	List all measured or derived variables with units.
🧾 Licensing	Record dataset-specific license terms (default: CC-BY-4.0).
🧪 Validation	Run make validate or rely on CI to enforce schema conformance.


⸻

🔒 Reproducibility & MCP Alignment

These metadata files embody Master Coder Protocol principles:
	•	Documented provenance and semantic traceability.
	•	Open, machine-readable formats (JSON/STAC/DCAT).
	•	Clear lineage from raw → processed → graph → UI.

They make every dataset self-describing, verifiable, and interoperable within KFM’s architecture.

⸻

🧱 Related Documentation
	•	data/derivatives/climate/checksums/README.md — hash integrity workflow
	•	docs/architecture.md — ETL & provenance design
	•	data/stac/README.md — STAC catalog schema
	•	data/sources/README.md — raw dataset manifests

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of climate derivative metadata schema and examples
