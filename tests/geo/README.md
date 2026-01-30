# 🌎 Geo Test Suite (`tests/geo/`)

![tests](https://img.shields.io/badge/tests-geo%20suite-brightgreen)
![pytest](https://img.shields.io/badge/runner-pytest-blue)
![spatial](https://img.shields.io/badge/focus-CRS%20%7C%20topology%20%7C%20PostGIS-orange)

> 🧭 **Intent:** Keep Kansas Frontier Matrix geospatial pipelines *correct, consistent, and explainable* — from CRS transforms to topology rules to metadata/provenance.

---

## 📌 What lives here

This folder is dedicated to **geospatial correctness tests** that protect:

- 🗺️ **CRS & projection invariants** (EPSG rules, axis order, bounding sanity)
- 🧩 **Geometry validity + topology rules** (no self-intersections, no overlaps where forbidden)
- 🧪 **Spatial predicate correctness** (contains/within/intersects/distance semantics)
- 🛰️ **Raster sanity checks** (CRS, nodata, alignment, resolution assumptions)
- 🧾 **Metadata + provenance lints** (STAC-ish catalog completeness and consistency)

---

## 🚀 Quickstart

### Run all geo tests (local)
```bash
pytest -q tests/geo
```

### Run a focused subset
```bash
pytest -q tests/geo -k crs
pytest -q tests/geo -k topology
pytest -q tests/geo -k postgis
```

### Run inside containers (if your stack uses Compose)
```bash
docker compose exec api pytest -q tests/geo
```

> ✅ Tip: Keep `tests/geo` fast. Put heavy workloads behind explicit markers like `@pytest.mark.slow`.

---

## 🧱 Test layout

Suggested structure (adapt to the repo as it evolves):

```text
tests/geo/
├─ README.md                 👈 you are here
├─ conftest.py               🧰 geo fixtures (CRS helpers, sample AOIs)
├─ unit/                     🧪 pure Python tests (no DB)
│  ├─ test_crs_rules.py
│  ├─ test_geojson_bounds.py
│  ├─ test_topology_rules.py
│  └─ test_raster_sanity.py
├─ integration/              🔌 needs services (PostGIS, tile server, etc.)
│  ├─ test_postgis_predicates.py
│  ├─ test_ingest_pipeline_spatial.py
│  └─ test_catalog_metadata_geo.py
├─ fixtures/                 📦 tiny inputs (GeoJSON / GeoTIFF / WKT)
│  ├─ ks_aoi.geojson
│  ├─ counties_min.geojson
│  └─ dem_tiny.tif
└─ golden/                   🏆 expected outputs (stable, reviewed)
   ├─ catalog_item_expected.json
   └─ provenance_expected.json
```

---

## ✅ Geo invariants we enforce

### 1) 🧭 CRS & projection rules

**Core idea:** spatial data must declare (or reliably imply) its CRS, and tests should catch “looks right but is wrong.”

Checklist:
- ✅ Default lon/lat datasets behave like **WGS84 / EPSG:4326**
- ✅ Lon/lat coordinates remain within valid world bounds
- ✅ Reprojection steps are explicit and repeatable (no silent CRS guessing)
- ✅ If using web-map tiles, data aligns with **EPSG:3857** expectations
- ✅ If using local/state projections (SPCS / Kansas-specific), distance/area calculations must be performed in an appropriate projected CRS

Recommended assertions:
- `feature_collection_has_crs_or_assumed_default()`
- `all_lonlat_within_bounds()`
- `reproject_roundtrip_is_stable()` (within tolerance)
- `axis_order_is_correct()` (especially when swapping between libraries)

---

### 2) 🧩 Geometry validity & topology

**Core idea:** invalid geometry poisons everything downstream (joins, overlays, stats, rendering).

We typically enforce:
- ✅ geometries are valid (or a consistent “make valid” strategy is applied)
- ✅ polygons don’t self-intersect
- ✅ polygon overlap rules (dataset-dependent):
  - administrative boundaries: overlaps usually **not allowed**
  - time-sliced layers: overlaps might be allowed **within a time window**, but must be explicit
- ✅ networks (roads/rails/rivers): node/edge connectivity assumptions remain true after transforms

Suggested test names:
- `test_geom_is_valid()`
- `test_no_polygon_overlaps()` (or `test_overlaps_only_when_allowed()`)
- `test_network_snapping_tolerance()`

---

### 3) 📐 Spatial predicates behave as expected

When the system relies on spatial predicates (Python or PostGIS), we lock in semantics:

Common expectations:
- `within(A, B)` implies `intersects(A, B)`
- `distance(A, B) == 0` for overlapping/intersecting geometries (depending on geometry types)
- `dwithin(A, B, r)` matches the chosen distance units + CRS

Suggested tests:
- `test_within_intersects_consistency()`
- `test_dwithin_matches_expected_units()`
- `test_intersects_is_symmetric()`

---

### 4) 🛰️ Raster sanity checks

For small, test-friendly rasters:
- ✅ CRS is present and matches expectations
- ✅ transform + resolution are stable
- ✅ nodata is defined (or an explicit default is used)
- ✅ (optional) alignment checks when clipping/masking (pixel edges vs. vector boundaries)

Suggested tests:
- `test_raster_has_crs_and_transform()`
- `test_raster_clip_is_deterministic()`

---

### 5) 🧾 Metadata & provenance lints

Geospatial outputs are only useful if we can **find, interpret, and trust** them later.

We lint for:
- ✅ catalog entry exists for each processed dataset
- ✅ metadata includes spatial/temporal extent
- ✅ projection/CRS is captured
- ✅ provenance log exists and references inputs + transforms
- ✅ license/source attribution isn’t missing for new data

Suggested tests:
- `test_catalog_item_exists_for_processed_dataset()`
- `test_catalog_extent_matches_data_bounds()`
- `test_provenance_references_inputs_and_steps()`

---

## 🧪 Writing a new geo test

### 🧰 Choose the right level

| Level | Folder | Fast? | Needs DB? | Use when… |
|---|---|---:|---:|---|
| Unit | `unit/` | ✅ | ❌ | CRS rules, geometry validity, file parsing |
| Integration | `integration/` | ⚠️ | ✅/❌ | PostGIS predicates, ingest pipelines, catalog/provenance |
| Slow / E2E | `integration/` + marker | ❌ | ✅ | tile rendering, big joins, performance guardrails |

### 🧷 Keep fixtures tiny

Rules of thumb:
- Prefer 5–200 features (not 50k)
- Prefer rasters under ~1–5 MB
- Use “Kansas AOI” cutouts for anything spatially heavy
- Golden outputs must be stable and reviewed in PR

---

## 🧠 Debug toolbox

Helpful one-liners:

```bash
# show full assertion diffs
pytest -q tests/geo -vv

# stop on first failure
pytest -q tests/geo -x

# run only marked tests
pytest -q tests/geo -m postgis
pytest -q tests/geo -m slow
```

Common failure causes:
- CRS mismatch between fixtures and code defaults
- silent reprojection (or missing reprojection)
- floating precision + topology edge cases
- using geographic CRS for distance/area math

---

## 🔒 CI expectations

- ✅ Geo tests should be deterministic
- ✅ Failures should be explainable (clear assertion messages)
- ✅ Missing metadata/provenance should fail fast
- ✅ If a PR adds/changes spatial outputs, it should also update relevant golden files

---

## 📚 Project reading list (handy references)

- 🧱 *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint*
- 🗺️ *Making Maps: A Visual Guide to Map Design for GIS*
- 🧭 *Map Reading & Land Navigation*
- 🧩 *Archaeological 3D GIS* (topology + spatial relationships)
- 🛰️ *Cloud-Based Remote Sensing with Google Earth Engine* (raster workflows + scale pitfalls)
- 🧰 *Python Geospatial Analysis Cookbook* (EPSG + PostGIS examples)

---

