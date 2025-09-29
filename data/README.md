<div align="center">

# 📂 Kansas-Frontier-Matrix — `data/`

**Mission:** keep **inputs reproducible**, **artifacts derivable**, and **catalogs discoverable**.  
This directory implements the project’s **MCP-style data lifecycle** end-to-end.

[![Build & Deploy](../.github/badges/site.svg)](../actions/workflows/site.yml)
[![STAC Validate](../.github/badges/stac.svg)](../actions/workflows/stac-badges.yml)
[![Pre-commit](../.github/badges/precommit.svg)](../.pre-commit-config.yaml)

</div>

---

## Contents

- [Philosophy](#philosophy)
- [Directory Layout](#directory-layout)
- [Git & LFS Policy](#git--lfs-policy)
- [Lifecycle & Make Targets](#lifecycle--make-targets)
- [Naming Conventions](#naming-conventions)
- [Source Descriptor Schema](#source-descriptor-schema)
- [Provenance & Checksums](#provenance--checksums)
- [STAC Guidance](#stac-guidance)
- [QA & Validation](#qa--validation)
- [Quickstart](#quickstart)
- [Gotchas](#gotchas)

---

## Philosophy

- **Raw is immutable.** We never hand-edit downloads; we annotate with tiny sidecars.  
- **Processing is reproducible.** Any artifact is re-creatable from scripts + configs.  
- **Catalogs are first-class.** Everything lands in **STAC 1.0.0** for discovery + time.

---

## Directory Layout

data/
├─ raw/                     # Immutable source payloads (GeoTIFF, ZIP, CSV, GPKG, PDF…)
│  ├─ /…
│  └─ _src.json       # Minimal provenance sidecar for the adjacent payload
│
├─ sources/                 # Human-curated descriptors & lookups (small, texty)
│  ├─ schema.source.json    # JSON Schema for validation
│  ├─ ks_hydrography.json
│  └─ ks_landcover_1936.json
│
├─ work/                    # Scratch, staging, temporary intermediates (non-committed)
├─ tmp/                     # Ephemeral (ignored), wiped by CI
│
├─ processed/               # Analysis-ready outputs (vectors/rasters/joins)
│  ├─ vectors/
│  │  ├─ hydrography_1936.geojson
│  │  └─ roads_1930s.geojson
│  ├─ dem/
│  │  └─ ks_1m_dem_2018.tif
│  └─ _meta.json            # Optional index of subtree provenance
│
├─ cogs/                    # Canonical Cloud-Optimized GeoTIFFs (mission-final rasters)
│  └─ hillshade_2020.tif
│
├─ derivatives/             # Higher-order blends/analytics (TRI, TPI, roughness, shaded relief)
│  └─ terrain/tri_2020.tif
│
├─ stac/                    # Space-time discovery catalog (collections + items)
│  ├─ collections/
│  │  └─ ks_hydrography.json
│  └─ items/
│     ├─ vectors/hydrography_1936.json
│     └─ vectors/roads_1930s.json
│
└─ tiles/                   # Ephemeral z/x/y PNGs or PMTiles for local preview (ignored)

> **Rule:** Every derivation should emit a `*_meta.json` capturing command, inputs, timestamps, versions, and checksums.

---

## Git & LFS Policy

**`.gitignore`**
- Keep `processed/**`, `cogs/**`, `derivatives/**`, `work/**`, `tmp/**`, and `tiles/**` out **by default**.
- Allow only: `*_meta.json`, `.sha256`, curated CSV/TSV/GeoJSON, and small README docs.

**`.gitattributes`**
- Route heavy binaries to **Git LFS**:
  - `*.tif *.tiff *.mbtiles *.pmtiles *.gpkg *.fgb *.shp *.dbf *.prj *.shx *.zip *.7z *.laz *.las *.pdf`
- Keep diff-friendly text in normal Git:
  - `*.json *.geojson *.topojson *.yaml *.yml *.csv *.tsv *.kml *.kmz (kmz via LFS if large)`

---

## Lifecycle & Make Targets

```mermaid
flowchart TD
  S[Define Source\n(data/sources/*.json)] --> F[Fetch\nmake fetch]
  F --> P1[Process Vectors\nmake vectors]
  F --> P2[Process Rasters\nmake cogs]
  P2 --> T[Terrain Derivatives\nmake terrain]
  P1 --> D[Derivatives\nmake derivatives]
  P2 --> D
  D --> C[STAC Build\nmake stac]
  C --> V[Validate\nmake validate-*]
  C --> X[Exports\nmake kml / make site]

Canonical targets
	1.	Define → data/sources/*.json
	2.	Fetch → make fetch
	3.	Vectors → make vectors (reproject to EPSG:4326, normalize fields)
	4.	Rasters → make cogs (COG-ify) · make terrain (hillshade, slope, aspect)
	5.	Derive → make derivatives (TRI/TPI/roughness, blends)
	6.	STAC → make stac (collections/items under data/stac/**)
	7.	Validate → make validate-* (schema, CRS, COG, STAC, checksums)
	8.	Export → make kml / make site (KMZ/KML + web viewer overlays)

All steps should refresh *_meta.json and *.sha256.

⸻

Naming Conventions
	•	Vectors → data/processed/vectors/<layer>_<period>.geojson
	•	e.g., hydrography_1936.geojson
	•	Rasters → data/processed/dem/<id>.tif
	•	e.g., ks_1m_dem_2018.tif
	•	COGs → data/cogs/<id>.tif
	•	STAC Items → data/stac/items/<collection>/<id>.json
	•	Periods → {YYYY | YYYY-YYYY | 1930s | late-19c} (lowercase, hyphenated)

⸻

Source Descriptor Schema

All curated sources must validate against sources/schema.source.json.

{
  "required": ["id", "title", "type", "license", "provenance", "retrieved"],
  "properties": {
    "id":        { "type": "string", "pattern": "^[a-z0-9_\\-]+$" },
    "title":     { "type": "string" },
    "type":      { "enum": ["vector", "raster", "collection", "service", "document"] },
    "period":    { "type": "string" },
    "bbox":      { "type": "array", "minItems": 4, "maxItems": 4 },
    "urls":      { "type": "array", "items": { "type": "string", "format": "uri" } },
    "license":   { "type": "object" },
    "provenance":{ "type": "object" },
    "retrieved": { "type": "string", "format": "date-time" },
    "confidence":{ "type": "number", "minimum": 0, "maximum": 1 }
  },
  "additionalProperties": true
}

Example (excerpt)

{
  "id": "ks_hydrography_1936",
  "title": "Kansas Hydrography (ca. 1936)",
  "type": "vector",
  "period": "1930s",
  "bbox": [-102.051, 36.993, -94.588, 40.003],
  "urls": ["https://.../download.zip"],
  "license": { "name": "Public Domain" },
  "provenance": { "agency": "NHD/USGS", "notes": "Digitized from 1930s sheets" },
  "retrieved": "2025-09-26T00:00:00Z",
  "confidence": 0.82
}


⸻

Provenance & Checksums

Each output directory should contain:
	•	*_meta.json → command, inputs, CRS, bbox, stats, versions (GDAL, PROJ), wall-time
	•	*.sha256 → one line per binary (COGs, PMTiles, GPKG, ZIP, PDFs…)
	•	_meta.json → optional subtree index

*_meta.json (minimal example)

{
  "command": "make terrain HILLSHADE=1 SOURCE=data/processed/dem/ks_1m_dem_2018.tif",
  "started": "2025-09-26T12:00:00Z",
  "finished": "2025-09-26T12:05:09Z",
  "inputs": [
    "data/processed/dem/ks_1m_dem_2018.tif",
    "scripts/terrain.py"
  ],
  "outputs": [
    "data/cogs/hillshade_2020.tif"
  ],
  "software": { "gdal": "3.9.0", "proj": "9.4.0", "python": "3.12" },
  "crs": "EPSG:4326",
  "bbox": [-102.051, 36.993, -94.588, 40.003],
  "stats": { "pixels": 123456789, "nodata": -9999 },
  "checksums": {
    "data/cogs/hillshade_2020.tif": "sha256:abc123..."
  }
}


⸻

STAC Guidance
	•	Collections → thematic groupings (dem, terrain, vectors, overlays)
	•	Items → concrete datasets (e.g., hydrography_1936)

Each STAC Item must include:
	•	geometry, bbox, and properties.datetime or properties.start_datetime / end_datetime
	•	At least one asset (COG or GeoJSON), with:
	•	roles: e.g., ["data"], optional ["visual"] for hillshade/tiles/KMZ
	•	checksum:sha256, type (MIME), title, href
	•	license
	•	Links to:
	•	self, parent (collection), root (catalog)
	•	Optional provenance registry: data/provenance/registry.json

Build + validate:

make stac
make stac-validate

The top-level catalog is referenced from the root README and by the web viewer.

⸻

QA & Validation
	•	make validate-sources → JSON Schema for sources/**
	•	make validate-vectors → CRS, topology, bbox sanity
	•	make validate-cogs → COG tiling, overviews, compression
	•	make stac-validate → STAC 1.0.0 compliance
	•	make checksums → refresh SHA-256 sidecars

CI runs STAC + checksum verification on PRs.

⸻

Quickstart

# 1) Add a source descriptor
$ $EDITOR data/sources/ks_hydrography.json

# 2) Fetch + process
$ make fetch vectors stac

# 3) Validate + record
$ make validate-sources validate-vectors checksums

# 4) Inspect outputs
$ open data/processed/vectors/hydrography_1936.geojson
$ open data/stac/items/vectors/hydrography_1936.json


⸻

Gotchas
	•	Shapefiles are brittle → prefer GeoPackage or FlatGeobuf.
	•	Normalize to EPSG:4326 (unless there’s a strong, documented reason).
	•	When regenerating, commit _meta.json + .sha256 together.
	•	Scratch stays in work/ or tmp/ — never commit ephemeral intermediates.

⸻

TL;DR
	•	Curated descriptors in sources/
	•	Immutable payloads in raw/
	•	Reproducible outputs in processed/, cogs/, derivatives/
	•	Discoverable metadata in stac/
	•	Guarded by .gitignore, .gitattributes, pre-commit, and CI.
	•	Every step emits provenance + checksums for auditability.

---
