# `data/` — Sources, Artifacts, Catalogs (Kansas-Frontier-Matrix)

Mission: keep **inputs reproducible**, **artifacts derivable**, and **catalogs discoverable**.

- **Sources** (small, human-edited): `data/sources/*.json`
- **Processed artifacts** (derived, often LFS): `data/processed/**`
- **STAC** (items/collections): `data/stac/**`
- **Working scratch** (ignored): `data/{work,tmp,cache,_cache,tiles}/**`

> Every derivation writes a `_meta.json` manifest capturing command, timestamps, inputs, versions, and checksums.

---

## Directory layout

```

data/
├── sources/                 # Hand-curated descriptors & small lookup tables
│   ├── schema.source.json   # JSON Schema for source files (see below)
│   ├── ks\_hydrography.json
│   ├── ks\_roads\_1930s.json
│   └── ks\_landcover\_1936.json
│
├── processed/               # Derived vectors/rasters (LFS), plus lightweight metadata
│   ├── vectors/
│   │   ├── hydrography\_1936.geojson
│   │   └── roads\_1930s.geojson
│   ├── dem/
│   │   └── ks\_1m\_dem.tif
│   └── \_meta.json           # Index manifest for this subtree (optional)
│
├── stac/                    # Space-time catalogs for discovery
│   ├── collections/
│   │   └── ks\_hydrography.json
│   └── items/
│       ├── hydrography\_1936.json
│       └── roads\_1930s.json
│
├── work/                    # Ephemera (ignored)
├── tmp/                     # Ephemera (ignored)
├── cache/                   # Ephemera (ignored)
└── tiles/                   # Ephemera (ignored)

````

**Git policy**
- `.gitignore` keeps `processed/**` out by default but **allows**: `_meta.json`, `*.meta.json`, `*.sha256`, and small JSON/CSV docs to be versioned.
- `.gitattributes` routes heavy binaries (COGs, MBTiles/PMTiles, GPKG, shapefile parts, LAS/LAZ, archives, etc.) to **Git LFS**; text descriptors remain normal Git.

---

## Workflow (Make targets)

1. Edit/add a source descriptor in `data/sources/*.json`.
2. `make fetch` → pull/download stream; stage raw inputs (usually under `data/raw/**` or direct to `processed/**` if streaming).
3. `make cogs` → convert rasters to COGs in `processed/**`.
4. `make terrain` → derive hillshade/slope/aspect from DEMs.
5. `make vectors` → normalize/clip/clean vector layers.
6. `make stac` → (re)build collections/items under `data/stac/**`.
7. `make kml` / `make site` → Google Earth KML/KMZ & web overlays.

Each step should emit or update a `*_meta.json` and `*.sha256` alongside outputs.

---

## Naming conventions

- **Vectors**: `data/processed/vectors/<layer>_<period>.geojson`  
  Examples: `hydrography_1936.geojson`, `roads_1930s.geojson`
- **Rasters**: `data/processed/dem/ks_1m_dem.tif`, `data/processed/hillshade/ks_hillshade_2018_2020.tif`
- **STAC items**: `data/stac/items/<layer>_<period>.json`
- **STAC collections**: `data/stac/collections/<theme>.json`
- **Periods**: prefer one of `{YYYY, YYYY-YYYY, 1930s, late-19c}` (lowercase, hyphenated).

---

## Source descriptor schema (excerpt)

Keep sources small and explicit. Fields below are recommended and enforced by `sources/schema.source.json`.

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
    "urls": {
      "type": "array",
      "items": { "type": "string", "format": "uri" }
    },
    "license": {
      "type": "object",
      "required": ["name"],
      "properties": { "name": { "type": "string" }, "url": { "type": "string", "format": "uri" } }
    },
    "provenance": {
      "type": "object",
      "properties": {
        "attribution": { "type": "string" },
        "publisher": { "type": "string" },
        "doi": { "type": "string" }
      }
    },
    "retrieved": { "type": "string", "format": "date-time" },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "notes": { "type": "string" }
  },
  "additionalProperties": true
}
````

**Tip:** if a source spans multiple download parts, use one descriptor with multiple `urls[]`; the fetch step will fan-out and merge.

---

## `_meta.json` & checksums

Each output directory should maintain lightweight, diffable records:

* `*_meta.json` (per artifact) — command line, tool versions, env, inputs (`sha256`, sizes), time, CRS, bbox, feature/row counts.
* `*.sha256` (per binary) — one-line checksum for integrity and CI verification.
* Optional subtree index: `processed/_meta.json` listing contained artifacts and their summaries.

Example per-artifact meta:

```json
{
  "artifact": "data/processed/vectors/hydrography_1936.geojson",
  "generated_by": "scripts/build_vectors.py --layer hydrography --period 1936",
  "timestamp": "2025-09-21T18:12:03Z",
  "inputs": [
    {"path": "data/sources/ks_hydrography.json", "sha256": "…"}
  ],
  "software": {"gdal": "3.9.0", "proj": "9.4.0"},
  "spatial": {"crs": "EPSG:4326", "bbox": [-102.1, 36.99, -94.6, 40.0]},
  "stats": {"features": 18432},
  "sha256": "…"
}
```

---

## STAC guidance

* **Collections** group related items (e.g., `ks_hydrography`), include `extent` (spatial & temporal), `license`, and `keywords`.
* **Items** represent concrete artifacts (e.g., `hydrography_1936`) with:

  * `geometry` & `bbox`
  * `properties.datetime` or `start_datetime`/`end_datetime`
  * `assets`: at minimum a `data` asset pointing to the file (COG/GeoJSON/GPKG)
  * `proj:*` & `gsd` if raster; vector counts in `kfm:feature_count`
  * `kfm:confidence` propagated from source (0–1)

> Use `make stac` to validate & (re)generate; CI runs `stac-validate` in `.github/workflows/stac-validate.yml`.

---

## LFS & storage rules

* Heavy/opaque binaries are forced to **Git LFS** by `.gitattributes` (COGs, MBTiles/PMTiles, GPKG, FlatGeobuf, shapefile parts, LAS/LAZ, Parquet, archives, big images, PDFs).
* Text descriptors (JSON/YAML/CSV/GeoJSON/TopoJSON/KML, `*.aux.xml`, `*.vrt`, `*.md`) remain **regular Git** for clean diffs.
* If you need tiny demo artifacts under `processed/**`, add an explicit negate rule in `.gitattributes` (e.g., `!data/processed/samples/**`).

---

## QA & self-checks

* **Schema validate**: `make validate-sources` → validate `data/sources/*.json` against `schema.source.json`.
* **Geometry sanity**: `make validate-vectors` → CRS, self-intersections, empties, bbox within Kansas.
* **COG audit**: `make validate-cogs` → COG layout, tiling, overviews, compression.
* **Hashes**: `make checksums` → (re)write `*.sha256`; CI verifies unchanged artifacts.
* **STAC**: `make stac && make validate-stac`.

---

## Gotchas

* Shapefile families (`.shp/.shx/.dbf/...`) are brittle; prefer **GPKG** or **FlatGeobuf** for interchange and **COG** for rasters.
* Avoid ad-hoc sidecars (`.prj` mismatches): normalize to **EPSG:4326** unless a strong reason exists; record CRS in meta.
* If an artifact is **regenerated**, update `_meta.json` and `*.sha256` in the same commit for traceability.

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

*This README reflects the repo’s guardrails: `.gitignore` keeps transient/processed noise out; `.gitattributes` ensures large binaries go to LFS while keeping human-readable metadata diffable.*

```
```
