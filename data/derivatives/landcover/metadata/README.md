<div align="center">

# 🌿 Kansas Frontier Matrix — Landcover Derivative Metadata  
`data/derivatives/landcover/metadata/`

**Purpose:** Define structured, machine-readable metadata for **landcover derivative datasets**  
(e.g., vegetation rasters, NLCD composites, cropland extent models, and historical land-use reconstructions)  
produced and versioned via the KFM ETL pipeline.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `metadata/` directory holds **JSON metadata files** documenting all processed landcover derivatives under  
`data/derivatives/landcover/`. Each metadata record provides:
- Source provenance and dataset lineage  
- Landcover variables and classification schema  
- Temporal coverage, spatial extent, and CRS  
- Checksum and STAC integration references  

These metadata files ensure that landcover datasets—such as historical vegetation maps, NLCD composites, and prairie extent rasters—are **self-describing**, **traceable**, and **interoperable** within KFM’s open, reproducible framework.

---

## 🧭 Metadata Generation Flow

```mermaid
flowchart TD
  A["Landcover Sources\nUSGS NLCD · KARS · USDA NRCS"] --> B["ETL\nExtract · Normalize · Derive"]
  B --> C["Landcover Derivatives\nCOG · GeoJSON · Parquet · CSV"]
  C --> D["Metadata JSONs\nvariables · CRS · temporal range · provenance"]
  D --> E["Checksums\nSHA-256 Validation"]
  D --> F["STAC Items\nLink assets + metadata"]
  F --> G["Knowledge Graph\nentity creation + relations"]
  G --> H["API & Web UI\nlandcover layers · vegetation analytics"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

metadata/
├── nlcd_1992_2021.json
├── vegetation_zones_1850_ks.json
├── landuse_1900_2000_composite.json
├── prairie_extent_2020.json
└── README.md

Each .json file corresponds directly to a processed derivative artifact and follows the KFM metadata schema aligned with STAC and DCAT conventions.

⸻

🧾 Metadata Schema (JSON Example)

{
  "id": "nlcd_1992_2021",
  "title": "National Land Cover Database (NLCD) Composite for Kansas (1992–2021)",
  "description": "Landcover composite derived from USGS NLCD rasters, harmonized to consistent categories and clipped to Kansas boundaries.",
  "type": "raster",
  "format": "COG",
  "file": "../nlcd_1992_2021_cog.tif",
  "checksum": "../checksums/nlcd_1992_2021_cog.tif.sha256",
  "source": "../../../sources/usgs_nlcd.json",
  "stac_item": "../../../stac/items/nlcd_1992_2021.json",
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "temporal": {
    "start": "1992-01-01",
    "end": "2021-12-31"
  },
  "variables": [
    {
      "name": "landcover_class",
      "units": "categorical",
      "description": "NLCD-derived landcover categories (e.g., water, forest, grassland, developed)."
    }
  ],
  "license": "CC-BY-4.0",
  "created": "2025-10-10",
  "mcp_stage": "derivatives"
}

💡 Tip: Align all file, checksum, and stac_item paths relative to the current directory.
Confirm each metadata JSON is referenced in its respective STAC item under data/stac/items/.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
🌿 Source Metadata	data/sources/	Defines provenance for landcover data (e.g., USGS NLCD, KARS vegetation surveys).
🧮 Derivative Metadata	data/derivatives/landcover/metadata/	Documents ETL-transformed landcover layers.
🧾 Checksums	data/derivatives/landcover/checksums/	Ensures artifact integrity.
🗺️ STAC Catalog	data/stac/	Registers assets with temporal and spatial metadata.
🧠 Knowledge Graph	(Neo4j)	Links landcover datasets to temporal trends and regions.


⸻

🧠 Usage in the Pipeline
	•	ETL: Python scripts automatically generate or update these .json files after processing.
	•	Validation: JSON Schema and STAC validators confirm schema compliance.
	•	CI/CD: The stac-validate.yml GitHub Action ensures all landcover derivatives have valid metadata and checksums.
	•	Graph Load: Metadata attributes (e.g., variables.name, temporal.start) feed into the Neo4j graph for spatiotemporal linkage.

⸻

🧱 Metadata Best Practices

Category	Guideline
✅ Completeness	Every derivative must include a metadata JSON file.
🔗 Linkage	Reference associated checksum, STAC item, and source manifest.
🕓 Timestamps	Use ISO 8601 for created and last_updated values.
🌾 Variables	Explicitly define landcover variables and categorical classes.
🧾 Licensing	Include license; default to CC-BY-4.0.
🧪 Validation	Run make validate or rely on CI checks.


⸻

🔒 Reproducibility & MCP Alignment

Landcover metadata files exemplify Master Coder Protocol standards by:
	•	Encoding open semantic metadata (STAC/DCAT/CIDOC CRM).
	•	Linking derivative assets to verifiable provenance and checksum references.
	•	Ensuring reproducibility through complete temporal, spatial, and variable documentation.

They make every KFM landcover dataset machine-actionable, traceable, and interoperable across GIS and AI pipelines.

⸻

🧱 Related Documentation
	•	data/derivatives/landcover/checksums/README.md — checksum workflow
	•	data/stac/README.md — STAC item structure and validation
	•	docs/architecture.md — ETL and provenance system design
	•	data/sources/README.md — landcover source manifest conventions

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of landcover derivative metadata schema and examples.