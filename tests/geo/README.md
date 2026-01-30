# 🌍 Geo Test Suite (`tests/geo`)

![pytest](https://img.shields.io/badge/tests-pytest-2b6cb0)
![geo](https://img.shields.io/badge/domain-geo%2Fgis-22863a)
![postgis](https://img.shields.io/badge/db-PostGIS-1f6feb)
![crs](https://img.shields.io/badge/CRS-EPSG%3A4326%20%E2%86%94%20projected-f59e0b)

> 🧭 **Purpose:** keep KFM’s geospatial output *correct, reproducible, and provenance-safe* — from raw ingest ➜ processing ➜ database ➜ API payloads ➜ UI-ready GeoJSON/tiles.

---

## 🧭 Quick Nav

- [🚀 Running the tests](#-running-the-tests)
- [🗂️ Folder layout](#️-folder-layout)
- [✅ What we test](#-what-we-test)
- [🏷️ Markers](#️-markers)
- [🧩 Fixtures & test data](#-fixtures--test-data)
- [📐 CRS & projection guardrails](#-crs--projection-guardrails)
- [🧱 Geometry invariants](#-geometry-invariants)
- [🛰️ Raster & remote-sensing checks](#️-raster--remote-sensing-checks)
- [🗄️ PostGIS integration checks](#️-postgis-integration-checks)
- [🧾 Provenance & metadata checks](#-provenance--metadata-checks)
- [➕ Adding a new geo test](#-adding-a-new-geo-test)
- [🧰 Troubleshooting](#-troubleshooting)
- [📚 Reference shelf](#-reference-shelf)

---

## 🚀 Running the tests

### 🐳 Docker (recommended)

```bash
# from repo root
docker-compose exec api pytest -q tests/geo
```

Common patterns:

```bash
# only fast/unit-ish checks
docker-compose exec api pytest -q tests/geo -m "not integration and not slow"

# just PostGIS integration
docker-compose exec api pytest -q tests/geo -m postgis

# run a single file
docker-compose exec api pytest -q tests/geo/test_crs_transform.py
```

### 🧪 Local (if you have native deps)

```bash
pytest -q tests/geo
```

> ⚠️ Local runs may require native libs (GDAL/PROJ/GEOS) and a reachable PostGIS if you run integration tests.

### 🛡️ Policy tests (repo-wide)

If your change touches **data**, **metadata**, or **provenance** rules, run the local policy gate:

```bash
conftest test .
```

---

## 🗂️ Folder layout

> This is the *intended* structure. If the repo differs, update this README to match reality ✅

```text
tests/geo/
├── 🧪 unit/                # pure-python geometry/CRS/time tests (fast)
├── 🔌 integration/         # hits services (PostGIS, tile server, pipeline outputs)
├── 🧰 fixtures/            # small, committed test datasets (GeoJSON, CSV, small rasters)
├── 🧾 schemas/             # JSONSchema / checks for GeoJSON + metadata (optional)
├── 📸 snapshots/           # golden outputs (GeoJSON/JSON) for regression tests
├── 🧠 helpers/             # shared helpers (tolerances, validators, builders)
├── 🧷 conftest.py           # pytest fixtures + shared config
└── 📘 README.md            # you are here 🙂
```

---

## ✅ What we test

### ✅ In scope

- 🧭 **CRS transforms** (e.g., EPSG:4326 ↔ projected CRS), axis order, round-trips
- 🧱 **Geometry validity** (self-intersections, empties, rings, multiparts)
- 🧲 **Spatial predicates** (within/contains/intersects) + edge cases (touching boundaries)
- 📦 **GeoJSON outputs** (valid JSON, correct coordinate order, stable properties)
- 🗄️ **PostGIS spatial SQL** (SRID correctness, `ST_Transform`, export to GeoJSON, spatial indexes)
- 🛰️ **Raster checks** (pixel scale, projection consistency, nodata handling) *if raster is part of the pipeline*
- ⏳ **Spatiotemporal sanity** (time ranges, granularity, “interval vs instant” semantics) where geo features include time

### 🚫 Out of scope (usually)

- 🧑‍🎨 Cartographic styling correctness (that belongs in UI/design review unless you snapshot-render maps)
- 🧪 E2E UI map interaction (prefer `tests/ui` / Playwright / Cypress if present)
- 🌐 Third-party service uptime (mock unless we explicitly do smoke tests)

---

## 🏷️ Markers

Use markers to keep CI fast and deterministic:

| Marker | Meaning | Typical deps |
|---|---|---|
| `geo` | “this is a geo test” umbrella marker | none |
| `crs` | CRS/projection behavior | pyproj/PROJ |
| `geometry` | Shapely/GEOS vector operations | shapely/GEOS |
| `postgis` | Requires PostGIS + seeded data | PostgreSQL/PostGIS |
| `raster` | Raster validation | GDAL/rasterio |
| `slow` | Expensive tests (big fixtures, many geometries) | varies |
| `integration` | Hits real services/containers | docker stack |

Example:

```python
import pytest

pytestmark = [pytest.mark.geo, pytest.mark.crs]
```

---

## 🧩 Fixtures & test data

### 🎒 Rules for fixtures

- 📦 Keep fixtures **small** and **committed** (tiny GeoJSON, minimal rasters)
- 🧭 Prefer **EPSG:4326** for interchange fixtures unless the test is explicitly projection-focused
- 🧱 Include **nasty geometries**:
  - self-intersecting polygon
  - hole touching shell
  - multipolygon with tiny slivers
  - “touching-but-not-overlapping” boundaries
- 🧾 Every fixture should be **explained**:
  - add a short `README.md` inside `fixtures/` *or*
  - comment in the test explaining what the fixture is proving

### 📦 Suggested fixture set (starter kit)

- `fixtures/kansas_bbox.geojson` (simple polygon / bbox baseline)
- `fixtures/sample_points_lonlat.geojson` (known lon/lat points)
- `fixtures/invalid_self_intersection.geojson` (expected invalid)
- `fixtures/timed_features.geojson` (features with `start`, `end`, or `year`)

---

## 📐 CRS & projection guardrails

### 🧭 Coordinate order (critical)

- In **EPSG:4326**, coordinates are **(lon, lat)** for GeoJSON.
- When using `pyproj`, explicitly force axis order:

```python
from pyproj import CRS, Transformer

src = CRS.from_epsg(4326)
dst = CRS.from_epsg(3857)
tf = Transformer.from_crs(src, dst, always_xy=True)  # ✅ always_xy avoids axis surprises

x, y = tf.transform(-95.689, 39.055)  # lon, lat (example point)
```

### 🎯 Tolerances (floating point reality)

Geospatial math is float-heavy. Prefer tolerant comparisons:

- Degrees: `1e-8` (roughly sub-millimeter at equator, but varies)
- Meters: `1e-3` to `1e-2` depending on pipeline precision
- Raster pixels: allow ±1 pixel where resampling occurs

> ✅ Tip: define tolerances once in `helpers/tolerance.py` and import everywhere.

---

## 🧱 Geometry invariants

These are the “must never break” rules we like to enforce:

- ✅ no empty geometries in published outputs
- ✅ polygons have closed rings
- ✅ no invalid geometries unless explicitly marked as “expected invalid”
- ✅ consistent SRIDs through the pipeline
- ✅ stable feature IDs (or stable hashing strategy)
- ✅ bounding boxes behave (minx ≤ maxx, miny ≤ maxy)
- ✅ `within/contains` semantics are correct for boundary-touching cases

Example invariant test idea:

```python
def test_output_geojson_is_valid(feature_collection):
    assert feature_collection["type"] == "FeatureCollection"
    assert all(f["type"] == "Feature" for f in feature_collection["features"])
    assert all("geometry" in f for f in feature_collection["features"])
```

---

## 🛰️ Raster & remote-sensing checks

If KFM produces/consumes rasters (COGs, hillshades, NDVI, DEMs), raster tests should verify:

- 🧭 projection is what we claim (CRS metadata present)
- 📏 pixel scale/resolution is stable (or within expected bounds)
- 🧩 nodata is preserved
- 🔁 reprojection/resampling choices are consistent
- 🧮 band math outputs are within expected numeric ranges

> 🎛️ If the pipeline uses multiple CRSs, raster tests should assert **explicit** transforms, not “whatever GDAL defaults to”.

---

## 🗄️ PostGIS integration checks

When PostGIS is involved, integration tests should cover:

- 🧭 SRIDs are set and correct (`ST_SRID(geom)`)
- 🔁 transforms are explicit (`ST_Transform`)
- 🧱 spatial predicates match expected truth tables
- 🧾 GeoJSON exports are correct (`ST_AsGeoJSON`)
- ⚡ indexes exist for hot paths (`GIST` on geometry columns)

Example “export contract” query (illustrative):

```sql
SELECT
  id,
  ST_AsGeoJSON(ST_Transform(geom, 4326))::json AS geometry
FROM features
WHERE ST_Within(geom, ST_Transform(ST_GeomFromText('POLYGON(...)', 4326), ST_SRID(geom)))
LIMIT 10;
```

---

## 🧾 Provenance & metadata checks

KFM’s geo stack is **provenance-first** 🧬 — tests should enforce “no mystery layers”:

✅ Examples of checks that belong here:

- `data/processed/*` assets have:
  - 📇 an entry in `data/catalog/…`
  - 🧾 a provenance record in `data/provenance/…`
- GeoJSON in `data/processed/` is valid JSON and has expected schema/property keys
- Published layers include:
  - source citation / attribution
  - license terms
  - CRS information (or explicit statement that output is EPSG:4326)

> 🧠 Rule of thumb: if a layer can show up in the UI, it must be explainable end-to-end.

---

## ➕ Adding a new geo test

1. 🧭 Decide the category:
   - **unit** if it’s pure geometry/CRS logic  
   - **integration** if it needs PostGIS, pipeline outputs, or container services
2. 🧩 Add or reuse a fixture:
   - keep it tiny
   - document why it exists
3. 🧪 Write the test:
   - use markers (`@pytest.mark.geo`, `@pytest.mark.crs`, etc.)
   - use shared tolerances
4. 📸 If regression-prone, add a snapshot:
   - store in `snapshots/`
   - keep stable ordering of features/properties
5. 🛡️ If it touches data policy, run:
   - `conftest test .`

---

## 🧰 Troubleshooting

<details>
<summary>🧭 “My CRS transform is flipped (lat/lon swapped)”</summary>

- Ensure `always_xy=True` in `pyproj.Transformer`
- Ensure GeoJSON uses `(lon, lat)` order
- Confirm tests aren’t mixing EPSG axis-order conventions with GeoJSON conventions

</details>

<details>
<summary>🧱 “Geometry validity differs on CI vs local”</summary>

- Shapely/GEOS versions can change robustness
- Normalize geometries if needed (e.g., snap to grid, buffer(0) cautiously)
- Prefer tolerance + invariant checks over exact coordinate equality

</details>

<details>
<summary>🗄️ “PostGIS tests failing: connection / SRID / permission”</summary>

- Confirm docker stack is up and PostGIS is ready
- Confirm the test DB is seeded/migrated
- Print SRIDs in failing assertions (`ST_SRID`) to detect silent mismatches

</details>

---

## 📚 Reference shelf

These project docs/books strongly influence how geo tests are written 🧠📖:

| 📄 Doc | Why it matters for `tests/geo` |
|---|---|
| **Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint** | provenance-first architecture, pipeline order, CI expectations |
| **Making Maps: A Visual Guide to Map Design for GIS** | metadata expectations, projection basics, map/scale discipline |
| **Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals & Applications)** | raster projection/pixel-scale reasoning for remote-sensing pipelines |
| **Python Geospatial Analysis Cookbook** | practical CRS transforms, GeoJSON generation, PostGIS patterns |
| **Visualization of Time-Oriented Data** | spatiotemporal semantics (instants vs intervals), data quality pitfalls |
| **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design** | stack assumptions (GDAL/Rasterio/GeoPandas/PyProj) + pipeline mindset |

---

🧭 **Mantra:** *No broken geometries, no silent CRS drift, no orphaned layers.* ✅