# Kansas-Frontier-Matrix — `data/`

Mission: keep **inputs reproducible**, **artifacts derivable**, and **catalogs discoverable**.  
This is the backbone of the project’s **MCP-style data lifecycle**.

---

## Layers of the Data Tree

- **Raw payloads** (immutable, as-downloaded): `data/raw/**`  
- **Sources** (small, human-curated descriptors): `data/sources/*.json`  
- **Work** (scratch, intermediate staging): `data/work/**`  
- **Tmp** (ephemeral scratch, always ignored): `data/tmp/**`  
- **Processed artifacts** (analysis-ready vectors/rasters): `data/processed/**`  
- **COGs** (canonical rasters): `data/cogs/**`  
- **Derivatives** (higher-order blends/analytical outputs): `data/derivatives/**`  
- **STAC** (items + collections): `data/stac/**`  
- **Tiles** (ephemeral z/x/y or PMTiles for local preview): `data/tiles/**`

> ✦ Every derivation should emit a `*_meta.json` manifest capturing command, timestamps, inputs, versions, and checksums.

---

## Directory Layout

data/
├── raw/                     # Immutable source payloads (GeoTIFF, ZIP, PDF…)
│   └── *_src.json           # Compact provenance sidecars
│
├── sources/                 # Hand-curated descriptors & lookup tables
│   ├── schema.source.json   # JSON Schema for validation
│   ├── ks_hydrography.json
│   └── ks_landcover_1936.json
│
├── work/                    # Scratch, staging, intermediate artifacts
├── tmp/                     # Ephemeral (ignored), wiped by CI
│
├── processed/               # Derived vectors/rasters (analysis-ready)
│   ├── vectors/
│   │   ├── hydrography_1936.geojson
│   │   └── roads_1930s.geojson
│   ├── dem/
│   │   └── ks_1m_dem.tif
│   └── _meta.json           # Index manifest (optional)
│
├── cogs/                    # Canonical Cloud-Optimized GeoTIFFs
│   └── hillshade_2020.tif
│
├── derivatives/             # Higher-order blends, terrain metrics
│   └── terrain/tri_2020.tif
│
├── stac/                    # Space-time catalog for discovery
│   ├── collections/
│   │   └── ks_hydrography.json
│   └── items/
│       ├── hydrography_1936.json
│       └── roads_1930s.json
│
└── tiles/                   # Ephemeral web map tiles (ignored)

---

## Git & LFS Policy

- **`.gitignore`**  
  - Keeps `processed/**`, `cogs/**`, `derivatives/**`, `work/**`, `tmp/**`, and `tiles/**` out by default.  
  - Allows only: `_meta.json`, `.sha256`, curated CSV/TSV/GeoJSON, and README docs.

- **`.gitattributes`**  
  - Routes heavy binaries (COGs, MBTiles/PMTiles, GeoPackage, FlatGeobuf, shapefiles, LAS/LAZ, archives, PDFs) to **Git LFS**.  
  - Leaves text descriptors (JSON/YAML/CSV/GeoJSON/TopoJSON/KML) in normal Git for clean diffs.  

---

## Workflow (Make Targets)

1. **Define source** → add `data/sources/*.json`.  
2. **Fetch** → `make fetch` (downloads, caches raw payloads).  
3. **Process vectors** → `make vectors` (normalize, reproject to EPSG:4326, clean).  
4. **Process rasters** → `make cogs` (convert to COG), `make terrain` (hillshade, slope, aspect).  
5. **Derivatives** → `make derivatives` (TRI/TPI/roughness, shaded relief blends).  
6. **STAC** → `make stac` (re)build collections + items in `data/stac/**`.  
7. **Validate** → `make validate-*` (schema, CRS, checksums, STAC compliance).  
8. **Export** → `make kml` / `make site` → publish KML/KMZ and web viewer overlays.

Every step should update:
- `*_meta.json` (provenance log)  
- `*.sha256` (checksum)

---

## Naming Conventions

- **Vectors** → `data/processed/vectors/<layer>_<period>.geojson`  
  - Example: `hydrography_1936.geojson`  

- **Rasters** → `data/processed/dem/<id>.tif`  
  - Example: `ks_1m_dem_2018.tif`  

- **COGs** → `data/cogs/<id>.tif` (mission-final)  

- **STAC Items** → `data/stac/items/<collection>/<id>.json`  

- **Periods** → one of `{YYYY, YYYY-YYYY, 1930s, late-19c}` (lowercase, hyphenated).  

---

## Source Descriptor Schema (Excerpt)

All curated sources must validate against `schema.source.json`:

```json
{
  "required": ["id", "title", "type", "license", "provenance", "retrieved"],
  "properties": {
    "id": { "type": "string", "pattern": "^[a-z0-9_\\-]+$" },
    "title": { "type": "string" },
    "type": { "enum": ["vector", "raster", "collection", "service", "document"] },
    "period": { "type": "string" },
    "bbox": { "type": "array", "minItems": 4, "maxItems": 4 },
    "urls": { "type": "array", "items": { "type": "string", "format": "uri" } },
    "license": { "type": "object" },
    "provenance": { "type": "object" },
    "retrieved": { "type": "string", "format": "date-time" },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 }
  }
}


⸻

Metadata & Checksums

Each output directory should contain:
	•	*_meta.json → provenance (command, inputs, CRS, bbox, software versions, stats).
	•	*.sha256 → checksum for every binary.
	•	_meta.json → optional subtree index.

⸻

STAC Guidance
	•	Collections → thematic groups (dem, topo, overlays, vectors).
	•	Items → concrete datasets (e.g., hydrography_1936).

Each STAC Item must include:
	•	Geometry + bbox
	•	Datetime / temporal extent
	•	At least one data asset (COG or GeoJSON)
	•	Optional derived assets (hillshade, slope, tiles, KMZ) with "roles": ["visual"]
	•	checksum:sha256 and license
	•	Links to provenance registry (data/provenance/registry.json)

Run:

make stac && make stac-validate


⸻

QA & Validation
	•	make validate-sources → JSON Schema check on sources/**.
	•	make validate-vectors → CRS, topology, bbox sanity.
	•	make validate-cogs → COG compliance (tiling, overviews, compression).
	•	make checksums → refresh SHA-256s.
	•	CI also runs stac-validate and checksum verification on PRs.

⸻

Gotchas
	•	Shapefiles are brittle → prefer GeoPackage or FlatGeobuf.
	•	Normalize CRS to EPSG:4326 unless there is a strong reason otherwise.
	•	If regenerating, commit updates to _meta.json and .sha256 together.
	•	Ephemeral scratch belongs only in work/ or tmp/ — never commit them here.

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

✦ Summary
data/ is structured for NASA-grade reproducibility:
	•	Curated descriptors in sources/
	•	Immutable payloads in raw/
	•	Reproducible outputs in processed/, cogs/, derivatives/
	•	Discoverable metadata in stac/
	•	All governed by .gitignore, .gitattributes, and CI checks.
	•	Every step emits provenance and checksums for auditability.

---
