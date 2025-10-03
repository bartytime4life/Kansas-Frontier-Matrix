<div align="center">


🧭 Kansas Frontier Matrix — Data & Catalog Architecture

Time · Terrain · History · Knowledge Graphs

</div>



⸻

Overview

This document defines the mission-grade data architecture for the Kansas-Frontier-Matrix (KFM). It explains how sources are described, fetched, transformed into open formats, cataloged with STAC, and wired into CI for provenance, integrity, and reproducibility. The design follows the project’s documentation-first / MCP principles and the end-to-end stack shown in the Architecture docs.  ￼  ￼

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

⸻

Directory Structure

In KFM, all datasets and metadata live under data/, split by lifecycle stage.  ￼

data/
├─ sources/     # JSON manifests (external pointers + metadata)
├─ raw/         # fetched originals (DVC/LFS pointers)
├─ processed/   # COGs, GeoJSON, CSV/Parquet — analysis-ready
└─ stac/        # STAC catalog (collections/items/assets)

data/sources/ {#datasources}

What it is: a lightweight catalog of manifests (JSON) that declare what a dataset is, where it comes from (URLs/APIs), license, spatial/temporal extent, and expected outputs. Pipelines read these to fetch/convert data without committing bulky binaries.  ￼

Why: keeps the repo lean and reproducible; every dataset starts with documented provenance.

⸻

data/raw/ {#dataraw}

What it is: a workspace for downloaded originals (archives, shapefiles, GeoTIFFs). We track pointers via DVC/Git LFS; not the bytes. Integrity sidecars (.sha256) accompany files.  ￼

Why: avoid repo bloat while retaining versioned, re-fetchable inputs.

⸻

data/processed/ {#dataprocessed}

What it is: analysis- and web-ready outputs in open formats:
	•	rasters → COG GeoTIFF (with internal overviews)
	•	vectors → GeoJSON/TopoJSON
	•	tables → CSV/Parquet

Consistent CRS (EPSG:4326) unless noted.  ￼

Why: interoperable, streamable layers for MapLibre, notebooks, and exports.  ￼

⸻

data/stac/ {#datastac}

What it is: a STAC catalog (collections/items) indexing every processed asset with time, space, hrefs, media types, and provenance. Drives discoverability and UI layer config.  ￼  ￼

⸻

Data Processing Pipeline

The ETL pipeline converts sources/ manifests into processed layers and STAC entries; it is Makefile-orchestrated with Python scripts.  ￼

flowchart TD
  A["Manifest JSON<br/>(data/sources/*.json)"] -->|make fetch| B["Raw Files<br/>(data/raw/)"]
  B -->|make cogs / make vectors| C["Processed Outputs<br/>(data/processed/)"]
  C -->|make stac| D["STAC Catalog<br/>(data/stac/)"]
  B --> E["SHA-256 Sidecars"]
  C --> E

<!-- END OF MERMAID -->


	•	Fetch — declarative downloads (HTTP/ArcGIS REST/API) with checksum verification.  ￼
	•	Transform — reprojection to WGS84, COG creation (rio-cogeo), GeoJSON conversion (ogr2ogr), attribute cleaning.
	•	Catalog — STAC item/collection generation + schema validation in CI.  ￼

⸻

Spatial Catalog (STAC)

KFM uses STAC 1.x to index all geospatial assets:
	•	Collections group related items (e.g., “Historic Topographic Maps”).
	•	Items include id, bbox/geometry, properties.datetime/interval, assets (e.g., COG or GeoJSON with accurate MIME types), and derived-from/source links for traceability.  ￼  ￼

Benefits: machine-readable discovery, consistent temporal/CRS metadata, smooth handoff to the web UI (layers config) and Earth/KML exports.  ￼

⸻

Provenance & Reproducibility

KFM bakes MCP rigor into data ops:
	•	Checksums — .sha256 sidecars for raw & processed artifacts detect drift and enable cacheable builds.  ￼
	•	Versioning — DVC/LFS pointers for large files; manifests are Git-tracked; all steps scripted.
	•	CI/Quality — GitHub Actions run STAC & JSON Schema validation, unit tests, CodeQL, and Trivy scans on every PR.
	•	Docs-first — SOPs, architecture, and experiment logs live in docs/ and are kept current (MCP).

⸻

Open Formats & Interoperability
	•	COG GeoTIFF / GeoJSON / CSV/Parquet are the canonical outputs for web + analysis.  ￼
	•	STAC powers indexing; metadata can be exposed as DCAT/JSON-LD where needed.  ￼
	•	Temporal semantics align with OWL-Time, and cultural-heritage entities (events/people/places) map into a CIDOC-CRM-aligned knowledge graph (beyond this doc’s scope, see Architecture + KG docs).  ￼

⸻

Tooling & Automation
	•	Makefile targets: fetch, cogs, vectors, stac, checksums, site.  ￼
	•	Python ETL: ingest/*, pipelines/* with modular converters and validators.
	•	GDAL/rio-cogeo for reprojection/COG; ogr2ogr for vector conversion; PySTAC for catalog build.

⸻

Contributing New Data

Goal: add a dataset once, with complete provenance, and have it appear in the timeline/map automatically.

	1.	Author a source manifest in data/sources/ (id, title, endpoint.urls or service, bbox/crs, temporal coverage, license). Keep CRS/time accurate for the timeline.
	2.	Run ETL — make fetch → make cogs/make vectors → make stac. Confirm outputs land in data/processed/ and a new STAC item appears.  ￼
	3.	Verify integrity — commit .sha256 sidecars and manifest; let CI validate STAC/schema.  ￼
	4.	(If UI-facing) — ensure the collection or item is discoverable by the web config build (layers are generated from STAC).  ￼

Tips
	•	Prefer GeoTIFF → COG and Shapefile → GeoJSON conversions; set output EPSG:4326 unless a different CRS is essential.
	•	Capture a precise time (single date or interval) for map/timeline filtering.  ￼
	•	Cite the original license/source in the manifest and check redistribution terms.

⸻

Appendix — Example minimal source descriptor

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

Processed COG will be referenced by a STAC Item with assets.cog.href pointing to the path above; UI layers are resolved from STAC.  ￼  ￼

⸻

References
Architecture & ETL/CI:  ￼ · Data layout & STAC:  ￼ · UI wiring:  · Source integration (GIS):  · Project docs/MCP:
