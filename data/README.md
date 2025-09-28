# `data/` — Sources, Artifacts, Catalogs (Kansas-Frontier-Matrix)

Mission: keep **inputs reproducible**, **artifacts derivable**, and **catalogs discoverable**.

- **Sources** (small, human-edited): `data/sources/*.json`
- **Processed artifacts** (derived, often LFS): `data/processed/**`
- **COGs / canonical outputs**: `data/cogs/**`
- **Derivatives** (analysis-ready blends): `data/derivatives/**`
- **STAC** (items/collections): `data/stac/**`
- **Working scratch / ephemeral** (ignored): `data/{work,tmp,cache,_cache,tiles,staging,joins,ocr}/**`

> Every derivation writes a `_meta.json` manifest capturing command, timestamps, inputs, versions, and checksums.

---

## Directory layout

```

data/
├── sources/                 # Hand-curated descriptors & small lookup tables
│   ├── schema.source.json   # JSON Schema for source files
│   ├── ks_hydrography.json
│   ├── ks_roads_1930s.json
│   └── ks_landcover_1936.json
│
├── processed/               # Derived vectors/rasters (LFS), plus lightweight metadata
│   ├── vectors/
│   │   ├── hydrography_1936.geojson
│   │   └── roads_1930s.geojson
│   ├── dem/
│   │   └── ks_1m_dem.tif
│   └── _meta.json           # Index manifest (optional)
│
├── cogs/                    # Canonical rasters (COGs)
│   └── hillshade_2020.tif
│
├── derivatives/             # Higher-order blends (slope/aspect, TRI, overlays)
│   └── terrain/…
│
├── stac/                    # Space-time catalogs for discovery
│   ├── collections/
│   │   └── ks_hydrography.json
│   └── items/
│       ├── hydrography_1936.json
│       └── roads_1930s.json
│
├── work/    # Ephemera (ignored)
├── tmp/     # Ephemera (ignored)
├── cache/   # Ephemera (ignored)
└── tiles/   # Ephemera (ignored)

````

---

## Git & LFS policy

- `.gitignore`:
  - Keeps `processed/**`, `cogs/**`, `derivatives/**`, `work/**`, `tmp/**` out by default.
  - **Allows**: `_meta.json`, `*.stac.json`, `*.sha256`, curated CSV/TSV/GeoJSON, and README docs.
- `.gitattributes`:
  - Routes heavy binaries (COGs, MBTiles/PMTiles, GPKG, FlatGeobuf, shapefile families, LAS/LAZ, archives, PDFs) to **Git LFS**.
  - Leaves text descriptors (JSON/YAML/CSV/GeoJSON/TopoJSON/KML, metadata sidecars) in regular Git for clean diffs.

---

## Workflow (Make targets)

1. **Define source**: edit/add `data/sources/*.json`.
2. **Fetch**: `make fetch` → pull/download stream; stage raw inputs.
3. **COGs**: `make cogs` → convert rasters to Cloud-Optimized GeoTIFFs.
4. **Terrain**: `make terrain` → derive hillshade/slope/aspect from DEMs.
5. **Vectors**: `make vectors` → normalize/clip/clean vector layers.
6. **Derivatives**: `make derivatives` → compute TRI/TPI/roughness, shaded relief blends, etc.
7. **STAC**: `make stac` → (re)build collections/items under `data/stac/**`.
8. **Export**: `make kml` / `make site` → Google Earth KML/KMZ & web overlays.

Each step should emit or update a `*_meta.json` and `*.sha256` alongside outputs.

---

## Naming conventions

- **Vectors**: `data/processed/vectors/<layer>_<period>.geojson`  
  Example: `hydrography_1936.geojson`
- **Rasters**: `data/processed/dem/ks_1m_dem.tif`  
  Example: `hillshade_2018_2020.tif`
- **STAC items**: `data/stac/items/<layer>_<period>.json`
- **STAC collections**: `data/stac/collections/<theme>.json`
- **Periods**: one of `{YYYY, YYYY-YYYY, 1930s, late-19c}` (lowercase, hyphenated).

---

## Source descriptor schema (excerpt)

Curated sources must validate against `schema.source.json`.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Source Descriptor",
  "type": "object",
  "required": ["id", "title", "type", "license", "provenance", "retrieved"],
  "properties": {
    "id": { "type": "string", "pattern": "^[a-z0-9_\\-]+$" },
    "title": { "type": "string" },
    "type": { "enum": ["vector", "raster", "collection", "service"] },
    "period": { "type": "string" },
    "bbox": { "type": "array", "minItems": 4, "maxItems": 4, "items": { "type": "number" } },
    "crs": { "type": "string", "default": "EPSG:4326" },
    "urls": { "type": "array", "items": { "type": "string", "format": "uri" } },
    "license": {
      "type": "object",
      "required": ["name"],
      "properties": { "name": { "type": "string" }, "url": { "type": "string", "format": "uri" } }
    },
    "provenance": { "type": "object" },
    "retrieved": { "type": "string", "format": "date-time" },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 }
  }
}
````

If a source spans multiple parts, list them in `urls[]`; `make fetch` will fan-out and merge.

---

## Metadata & checksums

Each output directory maintains lightweight records:

* `*_meta.json` — provenance (command, inputs, versions, CRS, bbox, stats).
* `*.sha256` — per-binary checksum.
* `_meta.json` — optional subtree index.

---

## STAC guidance

* **Collections**: thematic groups (`ks_hydrography`, `ks_roads`).
* **Items**: concrete artifacts (e.g. `hydrography_1936`).

  * Must have geometry, bbox, datetime/temporal extent.
  * Assets: at minimum `data` pointing to COG/GeoJSON.
  * Add `proj:*`, `gsd` for rasters; `kfm:feature_count` for vectors.
  * Carry forward `kfm:confidence` from source descriptors.

Run `make stac && make validate-stac` — CI enforces validation.

---

## QA & validation

* `make validate-sources` — JSON Schema check on `sources/**`.
* `make validate-vectors` — CRS, self-intersections, bbox sanity.
* `make validate-cogs` — COG tiling, overviews, compression.
* `make checksums` — refresh `*.sha256`.
* CI also runs **stac-validate** and checksum verification.

---

## Gotchas

* Shapefiles are brittle → prefer **GeoPackage** / **FlatGeobuf** for vectors.
* Normalize CRS → **EPSG:4326** unless strong reason otherwise.
* If regenerating, update `_meta.json` and `.sha256` in same commit.
* Ephemeral scratch belongs only in `work/` or `tmp/` — never commit.

---

## Quickstart

```bash
# 1) Add a source
$ $EDITOR data/sources/ks_hydrography.json

# 2) Pull & build
$ make fetch vectors stac

# 3) Validate & record
$ make validate-sources validate-vectors checksums

# 4) Browse
$ open data/processed/vectors/hydrography_1936.geojson
$ open data/stac/items/hydrography_1936.json
```

---

✦ **Summary:** `data/` is organized for **NASA-grade reproducibility**:

* descriptors in `sources/` →
* reproducible outputs in `processed/`, `cogs/`, `derivatives/` →
* discoverable metadata in `stac/` →
* all guarded by `.gitignore`, `.gitattributes`, and CI validation.

```
