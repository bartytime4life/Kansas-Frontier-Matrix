<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Derivative Metadata  
`data/derivatives/hydrology/metadata/`

**Purpose:** Define structured, machine-readable metadata for all **hydrological derivative artifacts**  
(e.g., streamflow rasters, watershed boundaries, aquifer grids, floodplains) generated via the KFM ETL pipeline.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory houses **metadata JSON files** describing hydrology-related derivative datasets created under  
`data/derivatives/hydrology/`. Each `.json` file documents a dataset’s **origin, hydrologic variable definitions, spatial and temporal extent, CRS**,  
and links to **checksum manifests**, **STAC items**, and **source datasets**.

These metadata files ensure that every hydrological product—such as river networks, floodplain rasters, or groundwater models—is:  
- Self-describing and semantically aligned with STAC/DCAT standards  
- Traceable to its data lineage through ETL provenance  
- Verifiable via checksum integration  

Together, they enable the Kansas Frontier Matrix to maintain a reproducible hydrological knowledge graph.

---

## 🧭 Metadata Generation Flow

```mermaid
flowchart TD
  A["Hydrology Sources\nUSGS · KDHE · NOAA · FEMA"] --> B["ETL\nExtract · Normalize · Derive"]
  B --> C["Hydrology Derivatives\nCOG · GeoJSON · Parquet · CSV"]
  C --> D["Metadata JSONs\nvariables · CRS · temporal range · provenance"]
  D --> E["Checksums\nSHA-256 Validation"]
  D --> F["STAC Items\nlink assets + metadata"]
  F --> G["Knowledge Graph\nentity creation + relations"]
  G --> H["API & Web UI\nriver basins · aquifers · floodplains"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

metadata/
├── streamflow_monthly_1990_2025.json
├── floodplain_extent_2020.json
├── aquifer_depth_ks.json
├── watershed_boundaries_huc8.json
└── README.md

Each .json metadata file maps directly to a processed hydrology derivative artifact and aligns with the KFM STAC/DCAT metadata schema.

⸻

🧾 Metadata Schema (JSON Example)

{
  "id": "streamflow_monthly_1990_2025",
  "title": "Monthly Streamflow Composite for Kansas (1990–2025, USGS NWIS)",
  "description": "Derived monthly mean streamflow (cfs) aggregated across Kansas HUC8 watersheds from USGS NWIS data.",
  "type": "raster",
  "format": "COG",
  "file": "../streamflow_monthly_1990_2025_cog.tif",
  "checksum": "../checksums/streamflow_monthly_1990_2025_cog.tif.sha256",
  "source": "../../../sources/usgs_nwis_streamflow.json",
  "stac_item": "../../../stac/items/streamflow_monthly_1990_2025.json",
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "temporal": {
    "start": "1990-01-01",
    "end": "2025-01-01"
  },
  "variables": [
    {
      "name": "streamflow",
      "units": "cubic feet per second (cfs)",
      "description": "Monthly mean discharge derived from USGS stream gauges."
    }
  ],
  "license": "CC-BY-4.0",
  "created": "2025-10-10",
  "mcp_stage": "derivatives"
}

💡 Tip: Always cross-reference paths with the associated data/sources/<source>.json and data/stac/items/<id>.json
to maintain STAC integrity and validation consistency.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
💧 Source Metadata	data/sources/	Defines raw hydrologic sources (USGS NWIS, FEMA NFHL, KDHE).
⚙️ Derivative Metadata	data/derivatives/hydrology/metadata/	Documents ETL-derived hydrology products.
🧾 Checksums	data/derivatives/hydrology/checksums/	Ensures artifact integrity.
🗺️ STAC Catalog	data/stac/	Registers spatial and temporal assets.
🧠 Knowledge Graph	(Neo4j)	Stores semantic relationships among hydrological entities.


⸻

🧠 Usage in Pipeline
	•	ETL Step: Python ETL modules auto-generate or update metadata after derivative creation.
	•	Validation: STAC and JSON Schema checks enforce structure, type, and linkage integrity.
	•	CI/CD: The stac-validate.yml action ensures all hydrology derivatives include valid metadata and checksums.
	•	Graph Load: Neo4j importer maps metadata fields (e.g., variables.name, temporal.start) to entity nodes for timeline visualization.

⸻

🧱 Metadata Best Practices

Category	Guideline
✅ Completeness	Every hydrology derivative requires a .json metadata file.
🔗 Linkage	Reference associated checksum, STAC item, and source manifest.
🕓 Timestamps	Use ISO 8601 for created and last_updated.
💧 Variables	Clearly define measured or modeled hydrologic attributes.
🧾 Licensing	Record license; defaults to CC-BY-4.0 unless restricted.
🧪 Validation	Run make validate or rely on CI workflow to verify schema compliance.


⸻

🔒 Reproducibility & MCP Alignment

Hydrology metadata files embody the Master Coder Protocol principles of documentation-first, reproducible science:
	•	Traceability: Metadata connects ETL products to raw sources and graph entities.
	•	Interoperability: JSON, STAC, and DCAT compliance for open data sharing.
	•	Accountability: SHA-256 checksums and provenance fields preserve data integrity.

⸻

🧱 Related Documentation
	•	data/derivatives/hydrology/checksums/README.md — checksum integrity workflow
	•	data/stac/README.md — STAC catalog schema and validation
	•	data/sources/README.md — hydrology source manifests
	•	docs/architecture.md — ETL architecture overview

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial hydrology metadata schema and examples.