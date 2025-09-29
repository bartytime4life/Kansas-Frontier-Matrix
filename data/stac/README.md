<div align="center">

# 🗂️ Kansas-Frontier-Matrix — **STAC Catalog** (`data/stac/`)

**Purpose:** a strict, machine-readable **SpatioTemporal Asset Catalog (STAC 1.0.0)** that is the **single source of truth** for:  
**what** datasets exist, **where** they live, **when/where** they apply, and **how** they were produced.

</div>

---

## Why STAC here?

- **Discoverability** — one entry point (`catalog.json`) for humans & machines.  
- **Interoperability** — STAC Items/Collections follow a public spec (1.0.0).  
- **Reproducibility** — provenance, versions, checksums, links to processing logs.  
- **Separation of concerns** — raw/processed artifacts live in `data/**`; **only metadata** lives here.  

---

## Catalog Layout

```text
data/stac/
├── catalog.json                 # Root STAC catalog (entry point)
├── collections/                 # Logical groupings
│   ├── dem.json                 # Digital Elevation Models
│   ├── topo.json                # Historic topographic maps
│   ├── overlays.json            # Color-reliefs, hillshades, styled rasters
│   └── vectors.json             # Treaties, trails, towns, rail, etc.
└── items/                       # Individual datasets (STAC Items)
    ├── dem/ks_1m_dem_2018.json
    ├── topo/usgs_larned_1894.json
    ├── overlays/ks_hillshade_2018.json
    └── vectors/ks_treaties.json

Rule of thumb
	•	Collections group related things with common semantics/time ranges.
	•	Items describe a single logical dataset (COG, GeoJSON, PMTiles, KMZ…) with concrete assets.

⸻

STAC Specification
	•	Core: STAC 1.0.0
	•	Extensions used (as needed):
	•	proj — CRS & grid metadata
	•	raster — per-band nodata, sampling, data type
	•	eo — band info (when relevant)
	•	version — semantic versioning & deprecation flags
	•	checksum — data integrity
	•	processing — pipeline info (optional but recommended)
	•	scientific — citations/DOIs (optional but recommended)

⸻

Conventions

IDs & Names
	•	Lowercase, underscores: ks_1m_dem_2018, usgs_larned_1894, ks_treaties.
	•	Stable over time; use the version extension to track updates.

Datetime
	•	Single date (e.g., publication or acquisition): properties.datetime.
	•	Intervals: properties.start_datetime and properties.end_datetime (omit datetime).

Assets & Media types
	•	COG raster: image/tiff; application=geotiff; profile=cloud-optimized
	•	GeoJSON: application/geo+json
	•	PMTiles: application/vnd.mapbox-vector-tile with "roles":["tiles"]
	•	KML/KMZ: application/vnd.google-earth.kmz
	•	Thumbnail/PNG: image/png with "roles":["thumbnail"]

Paths (relative to STAC item)
	•	Raster COGs → ../../../../data/cogs/...
	•	Vectors → ../../../../data/processed/...
	•	KML/KMZ → ../../../../data/kml/...

Provenance & Providers

Always include:
	•	license
	•	providers (name, roles: producer, processor, host, URLs)
	•	created / updated (ISO 8601)
	•	checksum:sha256 on each asset (match .sha256 sidecars)
	•	A links entry back to ../../provenance/registry.json#<id> when possible.

⸻

How to Add a Dataset (authoritative checklist)
	1.	Prepare the artifact
	•	Raster → COG

rio cogeo create input.tif data/cogs/my_layer.tif --web-optimized


	•	Vector → GeoJSON in WGS84

ogr2ogr -f GeoJSON -t_srs EPSG:4326 data/processed/my_layer.json input.shp


	•	(Optional) tiles → PMTiles/MBTiles (if needed for web perf).

	2.	Compute checksum

sha256sum data/cogs/my_layer.tif > data/cogs/my_layer.tif.sha256


	3.	Create the STAC Item
	•	Copy a template (see Templates below).
	•	Update: id, bbox, geometry, datetime or start_datetime+end_datetime, assets.href, checksum:sha256, links.
	4.	Link into a Collection
	•	Add the Item’s link to the correct collections/*.json or ensure the Collection’s links contain the Item path (root catalog must also include the Collection).
	5.	Validate

make stac
make stac-validate
pre-commit run --all-files



⸻

Quality Gates (what CI enforces)
	•	Schema validity: all *.json under data/stac/ pass STAC 1.0.0 validation.
	•	Checksums present: every asset has checksum:sha256 matching the sidecar hash.
	•	COG correctness: COGs open and contain overviews/tiling; nodata declared (via raster ext) when applicable.
	•	CRS recorded: proj:epsg or proj:wkt2 in Items with rasters. All vectors are EPSG:4326.
	•	Time semantics: use datetime OR start/end_datetime (not both).
	•	Links walk: root → collections → items round-trip without dead refs.

⸻

Templates (copy-paste and edit)

1) DEM (COG) — items/dem/ks_1m_dem_2018.json

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018",
  "collection": "dem",
  "properties": {
    "datetime": "2018-12-31T00:00:00Z",
    "license": "Public Domain",
    "created": "2025-01-01T00:00:00Z",
    "updated": "2025-01-01T00:00:00Z"
  },
  "bbox": [-102.051, 36.993, -94.588, 40.003],
  "geometry": { "type": "Polygon", "coordinates": [[
    [-102.051,36.993],[-94.588,36.993],[-94.588,40.003],[-102.051,40.003],[-102.051,36.993]
  ]]},
  "assets": {
    "data": {
      "href": "../../../../data/cogs/ks_1m_dem_2018.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "proj:epsg": 4326,
      "checksum:sha256": "<sha256sum>"
    },
    "thumbnail": {
      "href": "../../../../data/cogs/thumbs/ks_1m_dem_2018.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/dem.json", "type": "application/json" },
    { "rel": "via", "href": "../../provenance/registry.json#ks_1m_dem_2018", "type": "application/json" }
  ],
  "proj:epsg": 4326,
  "raster:bands": [
    { "sampling": "point", "data_type": "float32", "nodata": -9999.0 }
  ]
}

2) Historic Topo (COG, single year) — items/topo/usgs_larned_1894.json

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "usgs_larned_1894",
  "collection": "topo",
  "properties": {
    "datetime": "1894-01-01T00:00:00Z",
    "license": "Public Domain",
    "created": "2025-01-01T00:00:00Z"
  },
  "bbox": [-99.40, 38.0, -98.80, 38.50],
  "geometry": { "type": "Polygon", "coordinates": [[
    [-99.40,38.0],[-98.80,38.0],[-98.80,38.50],[-99.40,38.50],[-99.40,38.0]
  ]]},
  "assets": {
    "image": {
      "href": "../../../../data/cogs/topo/usgs_larned_1894.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["visual"],
      "checksum:sha256": "<sha256sum>"
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/topo.json", "type": "application/json" },
    { "rel": "derived_from", "href": "../../provenance/registry.json#usgs_larned_1894", "type": "application/json" }
  ],
  "proj:epsg": 4326
}

3) Vectors (GeoJSON, time interval) — items/vectors/ks_treaties.json

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_treaties",
  "collection": "vectors",
  "properties": {
    "start_datetime": "1854-01-01T00:00:00Z",
    "end_datetime":   "1890-12-31T23:59:59Z",
    "license": "CC-BY-4.0",
    "created": "2025-01-01T00:00:00Z"
  },
  "bbox": [-102.051, 36.993, -94.588, 40.003],
  "geometry": { "type": "Polygon", "coordinates": [[
    [-102.051,36.993],[-94.588,36.993],[-94.588,40.003],[-102.051,40.003],[-102.051,36.993]
  ]]},
  "assets": {
    "data": {
      "href": "../../../../data/processed/vectors/ks_treaties.geojson",
      "title": "Kansas Treaties (GeoJSON)",
      "type": "application/geo+json",
      "roles": ["data"],
      "checksum:sha256": "<sha256sum>"
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/vectors.json", "type": "application/json" },
    { "rel": "via", "href": "../../provenance/registry.json#ks_treaties", "type": "application/json" }
  ]
}


⸻

Collections (policy & example fields)

Each Collection should include:
	•	id, title, description
	•	keywords (e.g., ["kansas", "dem", "lidar", "terrain"])
	•	extent.spatial (bbox) and extent.temporal (intervals)
	•	license, providers
	•	summaries (for common fields across items: proj:epsg, raster:bands.data_type, etc.)
	•	links to contained items (or rely on crawler discovery)

Keep domains intuitive: dem, topo, overlays, vectors. Add sub-collections if a domain becomes crowded.

⸻

Versioning & Deprecation
	•	Use the version extension for semantic versioning: version, version:predecessor, version:successor, version:deprecated.
	•	When replacing an Item (e.g., reprocessed DEM):
	1.	Publish a new Item with a higher version.
	2.	Add links with rel="successor" / rel="predecessor".
	3.	Optionally mark the old Item with "version:deprecated": true and explain in description.

⸻

Integration Points (beyond STAC)
	•	Provenance registry → data/provenance/registry.json holds lineage: raw → processed → STAC. Link with rel:"via" or rel:"derived_from".
	•	Web viewer → layer manifests in web/data/*.json should reference STAC ids or hrefs.
	•	Knowledge graph → ETL writes nodes/edges and stores back-refs; add a links entry with rel:"related" to the graph API/entity when available.
	•	Experiments (MCP) → cite STAC IDs in docs/experiments/**/experiment.md for reproducibility.

⸻

CI & Local Validation

Local

make stac              # generate/refresh any derived JSON if scripted
make stac-validate     # schema & extension checks
pre-commit run --all-files

CI
	•	.github/workflows/stac-validate.yml runs STAC validation + checksums.
	•	Pre-commit enforces the same checks before merge.

⸻

Common Pitfalls (and fixes)
	•	❌ Both datetime and start/end_datetime present → Pick one (STAC requirement).
	•	❌ Missing checksum:sha256 on an asset → generate a sidecar + copy value into the Item.
	•	❌ Wrong CRS for vectors → convert to EPSG:4326 before publishing.
	•	❌ No overviews/tiling on COG → use rio cogeo create --web-optimized.
	•	❌ Bounding box not matching geometry → recompute hull/extent and keep them consistent.

⸻

Authoring Flow (visual)

flowchart TD
  A[Artifact ready<br/>(COG/GeoJSON/PMTiles)] --> B[Compute checksum]
  B --> C[Draft STAC Item<br/>(copy template)]
  C --> D[Link to Collection<br/>& Root catalog]
  D --> E[Local validate<br/>make stac-validate]
  E --> F[Commit & PR<br/>(pre-commit OK?)]
  F --> G[CI validates & publishes]


⸻

Media-type crib sheet

Type	Media type	Roles
COG	image/tiff; application=geotiff; profile=cloud-optimized	data, visual
GeoJSON	application/geo+json	data
PMTiles	application/vnd.mapbox-vector-tile (or vendor/pmtiles)	tiles
KMZ	application/vnd.google-earth.kmz	data, visual
Thumbnail	image/png	thumbnail


⸻

TL;DR
	•	Catalog in data/stac/ is authoritative metadata — not data files.
	•	Every asset has a checksum, CRS, time info, and pointed provenance link.
	•	Collections are clean, Items are specific, CI keeps us honest.
	•	If in doubt: copy a template, fill the blanks, validate, then PR.

