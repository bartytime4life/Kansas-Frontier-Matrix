<div align="center">


🗃️ Kansas Frontier Matrix — Data & Catalog Architecture

data/architecture.md

</div>


Mission: A documentation-first, reproducible data backbone that turns heterogeneous sources (scans, rasters, vectors, documents) into open, indexed, time-aware web layers and a semantic knowledge graph—backed by checksums, CI, and STAC metadata.  ￼

⸻

📚 Table of Contents
	•	Overview & Principles
	•	Repository Layout (Data)
	•	End-to-End Flow (Mermaid)
	•	Source Descriptors (data/sources/*.json)
	•	Processing Outputs (data/processed/)
	•	STAC Catalog (data/stac/)
	•	Provenance, Integrity & Uncertainty
	•	Open Standards & Semantics
	•	Pipelines & Make Targets
	•	CI/CD & Validation
	•	Examples (Descriptor, STAC Item)
	•	Troubleshooting & FAQ
	•	Roadmap & Extensibility

⸻

🧭 Overview & Principles

KFM’s data architecture couples deterministic ETL with cataloged, discoverable geospatial products and a graph-first integration layer. Core principles:
	•	MCP Documentation-First: every dataset and transform is explained, templated, and traceable.  ￼
	•	Open, Web-ready Formats: COG GeoTIFF for rasters; GeoJSON (or tiles) for vectors; time attributes everywhere.
	•	STAC 1.0 Cataloging: machine/human discoverability for all processed assets.
	•	Semantic Interop: entities and events map to CIDOC CRM and OWL-Time; periods can reference PeriodO.
	•	Integrity & Reproducibility: SHA-256 sidecars; schema validation; CI gates; containerized runs.

⸻

🗂 Repository Layout (Data)

data/
├─ sources/     # JSON descriptors (external pointers + metadata)
├─ raw/         # fetched originals (DVC/LFS pointers; not in Git history)
├─ processed/   # COGs, GeoJSON, tables ready for use
└─ stac/        # STAC Collections/Items (JSON) indexing processed assets

	•	data/sources/ → lightweight, versioned manifests for each dataset (id, title, license, bbox/time, endpoints). These power make fetch without bloating Git.
	•	data/raw/ → off-Git binaries (DVC/LFS pointers) + .sha256 sidecars for integrity.
	•	data/processed/ → normalized outputs (COG/GeoJSON/CSV/Parquet) for web & analysis.
	•	data/stac/ → the authoritative index of layers (assets + spatial/temporal metadata + links to provenance).

⸻

🔄 End-to-End Flow

flowchart TD
  A["Sources\nscans · rasters · vectors · documents"] --> B["ETL Pipeline\nMakefile · Python · checksums"]
  B --> C["Processed Layers\nCOGs · GeoJSON · tables"]
  B --> I["AI/ML Enrichment\nNER · geocoding · linking"]
  C --> D["STAC Catalog\ncollections · items · assets"]
  D --> E["Web Config Build\napp.config.json · layers.json"]
  D --> H["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
  I --> H
  H --> J["API Layer\nFastAPI · GraphQL"]
  D --> J
  J --> F["Frontend (React + MapLibreGL)\nmap · timeline · search"]

This is the canonical pipeline used across the repo for data creation, cataloging, and delivery.  ￼

⸻

🧾 Source Descriptors (data/sources/*.json)

A source descriptor is the contract between a dataset and the pipeline: it declares what to fetch, where it lives, when it applies, and how we’ll transform and license it.

Required fields (typical):
	•	id, title, description, license, providers
	•	spatial (bbox, CRS), temporal (start/end or instant)
	•	endpoint (http/ArcGIS REST/API list); assets or urls
	•	optional outputs (suggested target path(s) in data/processed/)

Example (historic soil map):

{
  "id": "usda_soil_1967",
  "title": "Soil Survey Map (1967)",
  "type": "raster",
  "license": "Public Domain",
  "spatial": { "bbox": [-101.5, 39.0, -100.8, 39.5], "crs": "EPSG:4326" },
  "temporal": { "start": "1967-01-01", "end": "1967-12-31" },
  "endpoint": {
    "type": "http",
    "urls": ["https://archive.example.org/soils/kansas_1967_map.tif"]
  },
  "outputs": {
    "cog": "data/processed/overlays/usda_soil_1967.tif"
  }
}

Tip: Prefer GeoTIFF/MrSID inputs for rasters and Shapefile/FGDB/GeoJSON for vectors; everything is normalized to COG/GeoJSON in processed/.

⸻

🏗 Processing Outputs (data/processed/)
	•	Rasters → COG (Cloud-Optimized GeoTIFF): tiled, overviewed, web-streamable; EPSG:4326 unless there’s a strong reason otherwise.
	•	Vectors → GeoJSON (or vector tiles for scale): projected to WGS84; per-county/per-year splits encouraged for heavy layers.
	•	Tables → CSV/Parquet: small factual tables stay in Git; large ones may use LFS/DVC.

⸻

🧭 STAC Catalog (data/stac/)

Every processed layer is minted as a STAC Item (grouped into Collections as needed). Items reference:
	•	geometry / bbox, datetime or start_datetime/end_datetime
	•	assets (e.g., cog, data, thumbnail) with media types
	•	links back to source descriptors or documents (provenance rels like derived_from)

Minimal STAC Item (COG asset):

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "usgs_topo_larned_1894",
  "properties": { "datetime": "1894-01-01T00:00:00Z" },
  "geometry": { "type": "Polygon", "coordinates": [[[...]]]},
  "bbox": [-99.4, 38.1, -99.0, 38.4],
  "assets": {
    "cog": {
      "href": "../../data/processed/overlays/usgs_topo_larned_1894.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "USGS Topographic Map (1894) — Larned"
    }
  }
}

The STAC is the single source of truth for the map/timeline catalog and powers layers.json and API discovery.  ￼

⸻

🧪 Provenance, Integrity & Uncertainty
	•	Checksums: Every fetched file gets a .sha256 sidecar; run make checksums to verify.  ￼
	•	Linkage: STAC links (e.g., derived_from) connect outputs back to data/sources/*.json.
	•	Uncertainty & Confidence: Where geocoding or OCR introduces ambiguity, record a confidence attribute (0–1) and visualize in UI (e.g., lighter symbology).

⸻

🔗 Open Standards & Semantics
	•	Formats: COG, GeoJSON, CSV/Parquet; tiles for scale.
	•	Catalogs: STAC for geospatial indexing; DCAT/JSON-LD exports optional.
	•	Ontology: CIDOC CRM for heritage entities; OWL-Time for intervals; PeriodO for named eras.

⸻

🛠 Pipelines & Make Targets

Common targets (non-exhaustive):

# Fetch raw data declared in data/sources/*.json
fetch:
	python tools/fetch_data.py

# Convert rasters to COG; vectors to GeoJSON; tables to CSV/Parquet
cogs vectors tables:
	python tools/process.py --stage $@

# Build/validate STAC
stac:
	python tools/generate_stac.py
	python tools/validate_stac.py

# Verify .sha256 integrity
checksums:
	python tools/checksums.py --verify

Pipelines are containerized and guarded by CI to ensure reproducible results and schema compliance.  ￼

⸻

✅ CI/CD & Validation
	•	GitHub Actions run on PRs: pre-commit, unit tests, STAC validation, JSON Schema checks, CodeQL, Trivy.  ￼
	•	Fail-fast on metadata drift: Any missing STAC fields or schema mismatches block merges.  ￼

⸻

📦 Examples

1) Vector source with multiple years (excerpt)

{
  "id": "ks_railroads_1900s",
  "title": "Kansas Railroads (1900s)",
  "type": "vector",
  "license": "CC-BY",
  "endpoint": {
    "type": "http",
    "urls": [
      "https://example.org/ks/railroads_1900.shp",
      "https://example.org/ks/railroads_1910.shp"
    ]
  },
  "spatial": {"bbox": [-102.1, 36.9, -94.6, 40.1], "crs": "EPSG:4326"},
  "temporal": {"start": "1900-01-01", "end": "1919-12-31"},
  "outputs": {
    "geojson": "data/processed/transport/railroads_1900s.geojson"
  }
}

2) STAC Asset roles for a raster

"assets": {
  "cog":   { "href": "...", "type": "image/tiff; application=geotiff; profile=cloud-optimized", "roles": ["data"]},
  "thumb": { "href": ".../thumb.jpg", "type": "image/jpeg", "roles": ["thumbnail"] }
}


⸻

🧰 Troubleshooting & FAQ
	•	STAC won’t validate → run make stac then tools/validate_stac.py for detailed errors; check bbox, datetime, media type.  ￼
	•	COG looks slow → ensure internal overviews (rio cogeo create --overview-level=5) and HTTP range requests are enabled.
	•	Vectors too heavy → split by county/year or convert to vector tiles; keep GeoJSON for small/medium layers.
	•	CRS mismatch → standardize to EPSG:4326 in pipeline; declare original CRS in source descriptor’s spatial.

⸻

🗺️ Roadmap & Extensibility
	•	DCAT feed export of the STAC for broader catalog interop.
	•	Vector tiling (PMTiles/MBTiles) for statewide, high-feature layers.
	•	Automated uncertainty viz (confidence-driven symbology) on the web map/timeline.
	•	Deeper semantics (CIDOC CRM profiles for treaties, deeds, and oral histories).

⸻

🔍 References (Project Docs)
	•	Architecture Overview (end-to-end stack, flow diagrams)  ￼
	•	File & Data Architecture (directory semantics, DVC/LFS, STAC)
	•	Web UI Architecture (MapLibre, Canvas timeline, layer config)
	•	GIS & Deeds Integration Guide (ArcGIS/Archive workflows, conversions)
	•	System Design (Knowledge Hub) (ETL+AI+Graph)
	•	MCP Foundations & Templates (experiments, SOPs, model cards)  ￼

⸻

Appendix A — At a Glance

Layer	Standard	What we store
Raster	COG GeoTIFF	Terrain, hillshade, scanned maps
Vector	GeoJSON / tiles	Boundaries, trails, railroads
Catalog	STAC 1.0	Items/Collections + assets
Semantics	CIDOC CRM, OWL-Time, PeriodO	People/Places/Events + intervals
Integrity	SHA-256 sidecars	All raw & key outputs
CI	Actions: STAC, Schema, CodeQL, Trivy	Validated on every PR

One command to rebuild: make fetch cogs vectors tables stac checksums
Sit back—your living, auditable atlas will be rebuilt end-to-end.  ￼

⸻
