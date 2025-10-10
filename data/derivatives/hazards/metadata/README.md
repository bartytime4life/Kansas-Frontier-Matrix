<div align="center">

# ⚡ Kansas Frontier Matrix — Hazard Derivative Metadata  
`data/derivatives/hazards/metadata/`

**Purpose:** Store structured, machine-readable metadata for all processed **hazard derivative artifacts**  
(tornado tracks, drought rasters, flood composites, storm summaries), linking them to checksums, STAC entries, and source provenance.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **metadata JSON files** describing all derived hazard datasets generated under  
`data/derivatives/hazards/`. Each `.json` metadata file captures the dataset’s **source lineage, variables, temporal and spatial coverage, CRS**, and **relationships** to STAC and checksum manifests.

These files serve as documentation and validation bridges between:
- ETL-derived hazard artifacts (e.g., GeoJSON tracks or COG rasters)  
- Integrity manifests (`/checksums`)  
- STAC catalog entries (`data/stac/`)  
- Knowledge graph ingestion (Neo4j relationships such as `HAS_DERIVATIVE`, `HAS_SOURCE`, `HAS_CHECKSUM`)  

They ensure that all hazard data products meet the **Master Coder Protocol (MCP)** standards for reproducibility and provenance.

---

## 🧭 Metadata Generation Flow

```mermaid
flowchart TD
  A["Sources\nNOAA SPC · FEMA · USGS · NCEI Storm Data"] --> B["ETL\nExtract · Transform · Derive"]
  B --> C["Hazard Derivatives\nCOG · GeoJSON · Parquet · CSV"]
  C --> D["Metadata JSONs\nvariables · CRS · temporal range · provenance"]
  D --> E["Checksums\nSHA-256 validation"]
  D --> F["STAC Items\nassets + metadata linkage"]
  F --> G["Knowledge Graph\nentity creation + relations"]
  G --> H["API & Web UI\nhazard map · timeline metadata"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

metadata/
├── tornado_tracks_1950_2024.json
├── flood_zones_1990_2025.json
├── drought_index_annual_ks.json
├── severe_storm_reports_1955_2024.json
└── README.md

Each .json file corresponds directly to a processed hazard dataset and adheres to the KFM JSON metadata schema aligned with STAC and DCAT standards.

⸻

🧾 Metadata Schema (JSON Example)

{
  "id": "tornado_tracks_1950_2024",
  "title": "Tornado Tracks Across Kansas (1950–2024, NOAA SPC)",
  "description": "Line vector dataset of all recorded tornado tracks in Kansas from 1950–2024, derived from NOAA SPC historical records.",
  "type": "vector",
  "format": "GeoJSON",
  "file": "../tornado_tracks_1950_2024.geojson",
  "checksum": "../checksums/tornado_tracks_1950_2024.geojson.sha256",
  "source": "../../../sources/noaa_spc_tornadoes.json",
  "stac_item": "../../../stac/items/tornado_tracks_1950_2024.json",
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "temporal": {
    "start": "1950-01-01",
    "end": "2024-12-31"
  },
  "variables": [
    {
      "name": "tornado_path",
      "units": "miles",
      "description": "Geospatial track path and EF rating attributes for tornadoes."
    }
  ],
  "license": "CC-BY-4.0",
  "created": "2025-10-10",
  "mcp_stage": "derivatives"
}

💡 Tip: Align paths and IDs with corresponding STAC and checksum files.
Each metadata JSON must reference its dataset’s provenance (source), checksum, and STAC item.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
🧭 Source Metadata	data/sources/	Defines raw hazard source datasets (NOAA, FEMA, USGS).
⚙️ Derivative Metadata	data/derivatives/hazards/metadata/	Describes ETL-processed hazard products.
🧾 Checksums	data/derivatives/hazards/checksums/	Ensures binary file integrity.
🗺️ STAC Catalog	data/stac/	Registers assets with time and space metadata.
🧠 Knowledge Graph	(Neo4j)	Links hazard events and layers as graph entities.


⸻

🧠 Usage in the Pipeline
	•	ETL Step: Scripts generate or update metadata automatically post-processing.
	•	Validation: STAC and JSON Schema validators confirm completeness and field consistency.
	•	CI/CD: The stac-validate.yml GitHub Action ensures every hazard dataset has matching metadata and checksum.
	•	Graph Integration: Neo4j loader scripts parse fields (e.g., temporal.start, variables.name) to populate entity nodes.

⸻

🧱 Metadata Best Practices

Category	Guideline
✅ Completeness	Every hazard derivative must include a metadata JSON file.
🔗 Linkage	Reference associated checksum, STAC item, and source manifest.
🕓 Timestamps	Include created and last_updated (ISO 8601).
🧮 Variables	Explicitly define attributes with names and units (e.g., EF scale, flood depth).
🧾 Licensing	Record dataset-specific license (default: CC-BY-4.0).
🧪 Validation	Run make validate or rely on CI for schema checks.


⸻

🔒 Reproducibility & MCP Alignment

Hazard metadata files implement the Master Coder Protocol requirements by providing:
	•	Explicit provenance (source, checksum, stac_item)
	•	Machine-readable semantics using STAC/DCAT standards
	•	Temporal and spatial consistency across derivative layers

They allow hazard data (tornadoes, floods, droughts) to be independently verified, reused, and versioned within the KFM architecture.

⸻

🧱 Related Documentation
	•	data/derivatives/hazards/checksums/README.md — checksum workflow
	•	data/stac/README.md — STAC item structure and validation
	•	docs/architecture.md — ETL and provenance system overview
	•	data/sources/README.md — hazard source manifest standards

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of hazard derivative metadata schema and examples.