Got it — here’s a GitHub-safe, aligned, and consistently titled rewrite you can drop into data/architecture.md. I removed fragile Unicode dividers, standardized headings, fixed center alignment, and made the Mermaid block GitHub-parser-friendly (quoted labels + closing comment).

<div align="center">

# 🗃️ Kansas Frontier Matrix — Data & Catalog Architecture  
`data/architecture.md`

[![Build & Deploy](../.github/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](../.github/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](../.github/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](../.github/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-commit](../.github/workflows/pre-commit.yml/badge.svg)](../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![License: Code](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../LICENSE)

</div>

---

## Overview

This document defines the **data architecture** for KFM, following **MCP** (documentation-first + reproducibility). It explains how data is **organized**, **processed** (ETL), **cataloged** (STAC), and **verified** (provenance + CI).

---

## Table of Contents

- [Repository Layout](#repository-layout)
- [End-to-End Flow](#end-to-end-flow)
- [Source Descriptors (`data/sources/`)](#source-descriptors-datasources)
- [Processed Outputs (`data/processed/`)](#processed-outputs-dataprocessed)
- [STAC Catalog (`data/stac/`)](#stac-catalog-datastac)
- [Provenance & Integrity](#provenance--integrity)
- [Open Standards & Semantics](#open-standards--semantics)
- [Pipelines & Make Targets](#pipelines--make-targets)
- [CI/CD & Validation](#cicd--validation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)

---

## Repository Layout

data/
├─ sources/     # JSON descriptors (external pointers + metadata)
├─ raw/         # fetched originals (DVC/LFS; not stored in Git history)
├─ processed/   # normalized outputs (COG, GeoJSON, CSV/Parquet)
└─ stac/        # STAC Collections/Items indexing processed assets

- **`sources/`**: minimal JSON manifests (id, title, license, bbox/time, endpoints).  
- **`raw/`**: originals fetched via `make fetch` (tracked with **DVC** or **Git LFS**), plus `*.sha256`.  
- **`processed/`**: analysis/web-ready outputs (COG rasters, GeoJSON vectors, CSV/Parquet tables).  
- **`stac/`**: authoritative catalog (Items/Collections + assets + provenance links).

---

## End-to-End Flow

```mermaid
flowchart TD
  A["Sources\n\"scans, rasters, vectors, docs\""] --> B["ETL Pipeline\n\"Makefile, Python, checksums\""]
  B --> C["Processed Layers\n\"COGs, GeoJSON, tables\""]
  B --> I["AI/ML Enrichment\n\"NER, geocoding, linking\""]
  C --> D["STAC Catalog\n\"collections, items, assets\""]
  D --> E["Web Config Build\n\"app.config.json, layers.json\""]
  D --> H["Knowledge Graph\n\"Neo4j, CIDOC CRM, OWL-Time\""]
  I --> H
  H --> J["API Layer\n\"FastAPI, GraphQL\""]
  D --> J
  J --> F["Frontend (React + MapLibre)\n\"map, timeline, search\""]
<!-- END OF MERMAID -->


⸻

Source Descriptors (data/sources/)

Each dataset begins as a descriptor: a compact JSON contract the pipeline reads to fetch, normalize, and catalog data.

Typical fields
	•	id, title, description, license, providers
	•	spatial (bbox, crs), temporal (start, end or datetime)
	•	endpoint (type: http/api/arcgis; urls list)
	•	optional outputs (suggested target paths under data/processed/)

Example

{
  "id": "usda_soil_1967",
  "title": "Soil Survey Map (1967)",
  "type": "raster",
  "license": "Public Domain",
  "spatial": { "bbox": [-101.5, 39.0, -100.8, 39.5], "crs": "EPSG:4326" },
  "temporal": { "start": "1967-01-01", "end": "1967-12-31" },
  "endpoint": { "type": "http", "urls": ["https://example.org/soils/kansas_1967_map.tif"] },
  "outputs": { "cog": "data/processed/overlays/usda_soil_1967.tif" }
}

Guideline: Prefer canonical inputs (GeoTIFF/MrSID for rasters; Shapefile/FGDB/GeoJSON for vectors). Everything is normalized to COG/GeoJSON.

⸻

Processed Outputs (data/processed/)
	•	Rasters → COG (Cloud-Optimized GeoTIFF)
	•	Tiled, overviewed, HTTP-range friendly; default EPSG:4326 unless otherwise justified.
	•	Vectors → GeoJSON (Vector tiles optional for scale)
	•	WGS84 coordinates; split by county/year when heavy.
	•	Tables → CSV/Parquet
	•	Small factual tables may live directly in Git; larger via LFS/DVC.

⸻

STAC Catalog (data/stac/)

Items describe individual assets; Collections group related items.

Minimal Item (COG asset):

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
  },
  "links": [
    { "rel": "derived_from", "href": "../../data/sources/usgs_topo_larned_1894.json" }
  ]
}

STAC is the single source of truth for discovery, powering UI configs and API queries.

⸻

Provenance & Integrity
	•	Checksums: *.sha256 sidecars for fetched and key processed files (make checksums).
	•	DVC/LFS: large binaries tracked out-of-Git with immutable content hashes.
	•	Determinism: ETL steps are repeatable; schemas validated in CI.
	•	Uncertainty: include confidence fields where applicable; surface in UI symbology.

⸻

Open Standards & Semantics
	•	Formats: COG, GeoJSON, CSV/Parquet; vector tiles/PMTiles for scale.
	•	Catalogs: STAC 1.0; optional DCAT/JSON-LD export.
	•	Ontology: CIDOC-CRM for heritage entities; OWL-Time for intervals; PeriodO for named eras.

⸻

Pipelines & Make Targets

# Fetch all sources
fetch:
	python tools/fetch_data.py

# Process: rasters->COG, vectors->GeoJSON, tables->CSV/Parquet
cogs vectors tables:
	python tools/process.py --stage $@

# Generate & validate STAC
stac:
	python tools/generate_stac.py
	python tools/validate_stac.py

# Verify integrity
checksums:
	python tools/checksums.py --verify


⸻

CI/CD & Validation
	•	GitHub Actions: pre-commit, unit tests, STAC validation, JSON Schema checks, CodeQL, Trivy.
	•	Fail-fast on metadata drift (missing fields, invalid bbox, wrong media types).

⸻

Examples

Vector source (multi-year)

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
  "outputs": { "geojson": "data/processed/transport/railroads_1900s.geojson" }
}

STAC roles (raster)

"assets": {
  "cog":   { "href": "...", "type": "image/tiff; application=geotiff; profile=cloud-optimized", "roles": ["data"] },
  "thumb": { "href": ".../thumb.jpg", "type": "image/jpeg", "roles": ["thumbnail"] }
}


⸻

Troubleshooting
	•	STAC won’t validate → run make stac then the validator; check datetime, bbox, media type.
	•	COG slow → ensure internal overviews (e.g., rio cogeo create --overview-level=5) and HTTP range.
	•	Vectors too heavy → split by county/year or produce vector tiles/PMTiles.
	•	CRS mismatch → standardize to EPSG:4326; record original CRS in spatial.

⸻

Roadmap
	•	DCAT/JSON-LD exports from STAC
	•	PMTiles for statewide vector/raster layers
	•	Confidence-aware styling in the UI
	•	Deeper CIDOC-CRM profiles for treaties, deeds, oral histories

⸻

Rebuild everything:
make fetch cogs vectors tables stac checksums

If you want, I can also push a variant that replaces the centered HTML wrapper with a plain H1 (some orgs prefer zero HTML in markdown).