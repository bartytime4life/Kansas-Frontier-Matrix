<div align="center">


🧭 Kansas Frontier Matrix — Data & Catalog Architecture

Time · Terrain · History · Knowledge Graphs

</div>



⸻

📌 Overview

This document describes the data architecture of Kansas-Frontier-Matrix (KFM), following Master Coder Protocol (MCP) principles: documentation-first, provenance, and full reproducibility. It explains directory roles, the ETL pipeline, STAC cataloging, and integrity controls used to keep data interoperable and auditable.

⸻

📚 Table of Contents
	•	Directory Structure
	•	data/sources/ · data/raw/ · data/processed/ · data/stac/
	•	Data Processing Pipeline
	•	Spatial Catalog (STAC)
	•	Provenance & Reproducibility
	•	Open Formats & Interoperability
	•	Tooling & Automation
	•	Contributing New Data
	•	Appendix: Minimal Source Descriptor

⸻

Directory Structure

All datasets and metadata live under data/, organized by lifecycle stage.

data/
├─ sources/     # JSON manifests (external pointers + metadata)
├─ raw/         # fetched originals (tracked via DVC/LFS pointers)
├─ processed/   # analysis-/web-ready outputs (COGs, GeoJSON, CSV/Parquet)
└─ stac/        # STAC catalog (collections/items/assets)

data/sources/ {#datasources}

Manifest catalog declaring each dataset: id, title, source URLs/APIs, bbox, temporal coverage, license/credits, and expected outputs. Pipelines read these to fetch/convert data while keeping the repo lean.

data/raw/ {#dataraw}

Fetched originals (archives, shapefiles, GeoTIFFs, CSVs). Large binaries are not committed—use DVC/Git LFS pointers. Integrity sidecars (.sha256) accompany important files.

data/processed/ {#dataprocessed}

Analysis- and web-ready outputs in open formats:
	•	Rasters → Cloud-Optimized GeoTIFF (COG) with internal overviews
	•	Vectors → GeoJSON/TopoJSON
	•	Tables → CSV/Parquet
Default CRS EPSG:4326 unless noted.

data/stac/ {#datastac}

STAC catalog indexing every processed asset with accurate spatiotemporal metadata, MIME types, and provenance links. Drives discovery and UI layer configuration.

⸻

Data Processing Pipeline

Makefile-orchestrated ETL converts sources/ manifests to processed assets and STAC entries.

flowchart TD
  A["Manifest JSON<br/>(data/sources/*.json)"] -->|make fetch| B["Raw Files<br/>(data/raw/)"]
  B -->|make cogs / make vectors| C["Processed Outputs<br/>(data/processed/)"]
  C -->|make stac| D["STAC Catalog<br/>(data/stac/)"]
  B --> E["SHA-256 Sidecars"]
  C --> E

<!-- END OF MERMAID -->


Fetch → declarative downloads (HTTP/REST/API) with checksum verification
Transform → reprojection to WGS84, COG creation (rio-cogeo), vector conversion (ogr2ogr), attribute cleanup
Catalog → programmatic STAC item/collection generation + validation in CI

⸻

Spatial Catalog (STAC)
	•	Collections group related Items (e.g., “Historic Topographic Maps”).
	•	Items include id, bbox/geometry, properties.datetime/interval, and assets (COG/GeoJSON with proper media types), plus rel:derived_from or rel:source for provenance.
	•	Enables machine-readable discovery, temporal filtering, and smooth handoff to the web UI and external catalogs.

⸻

Provenance & Reproducibility
	•	Checksums — .sha256 sidecars detect drift and ensure byte-level fidelity.
	•	Versioned storage — DVC/LFS for large files; manifests & code in Git.
	•	Deterministic builds — scripted ETL (Make/Python) yields identical outputs from identical inputs.
	•	CI Guardrails — GitHub Actions run STAC & JSON Schema validation, unit tests, CodeQL, Trivy, SBOM export, and pre-commit checks.
	•	Docs-first MCP — every dataset/change includes documentation & metadata updates.

⸻

Open Formats & Interoperability
	•	COG GeoTIFF, GeoJSON/TopoJSON, CSV/Parquet as canonical outputs.
	•	STAC 1.x for indexing; optional DCAT/JSON-LD crosswalks.
	•	Temporal semantics align with OWL-Time; cultural-heritage entities map to CIDOC-CRM in the knowledge graph.

⸻

Tooling & Automation
	•	Makefile: fetch, cogs, vectors, stac, checksums, site.
	•	Python ETL: src/pipelines/**, modular converters & validators.
	•	GDAL/rasterio/rio-cogeo for rasters; OGR/Fiona/ogr2ogr for vectors; PySTAC for catalog build.
	•	Pre-commit formatting/linting; GitHub Actions for CI; DVC/LFS for data lineage.

⸻

Contributing New Data
	1.	Create a source manifest (data/sources/<id>.json): id, title, endpoint.urls, bbox, temporal, license.
	2.	Run ETL: make fetch → make cogs/make vectors → make stac.
	3.	Verify integrity: commit .sha256 sidecars; ensure STAC validates in CI.
	4.	Wire to UI (if applicable): ensure the collection/item is discoverable by the web config build (layers are generated from STAC).

Tips: Prefer GeoTIFF→COG and Shapefile→GeoJSON; default to EPSG:4326; capture precise datetimes/intervals for the timeline; cite original license/source.

⸻

Appendix — Minimal Source Descriptor

{
  "id": "usgs_topo_larned_1894",
  "title": "USGS Topographic Map — Larned (1894)",
  "type": "raster",
  "endpoint": { "type": "http", "urls": ["https://example.org/usgs/larned_1894.tif"] },
  "spatial": { "bbox": [-99.4, 38.1, -99.0, 38.4], "crs": "EPSG:4326" },
  "temporal": { "start": "1894-01-01", "end": "1894-12-31" },
  "license": "Public Domain",
  "outputs": { "cog": "data/processed/overlays/usgs_topo_larned_1894.tif" }
}

Processed COG is referenced by a STAC Item (assets.cog.href) and becomes discoverable to the web UI from the STAC catalog.
