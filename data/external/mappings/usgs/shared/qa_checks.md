<!-- According to a document from 2026-01-29: consolidated QA policy derived from KFM + GIS reference PDFs shipped with this repo. -->

# 🧪🗺️ USGS Shared QA Checks

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-0B7285?logo=github)
![USGS](https://img.shields.io/badge/source-USGS-1C7ED6)
![QA](https://img.shields.io/badge/quality-gates%20%26%20checks-2F9E44)
![Scope](https://img.shields.io/badge/scope-shared%20policy-orange)

📍 **Path:** `data/external/mappings/usgs/shared/qa_checks.md`  
🎯 **Applies to:** everything under `data/external/mappings/usgs/**`  
🧷 **Goal:** consistent, reproducible, provable ingest quality (vector + raster) with minimal surprises.

> [!IMPORTANT]
> This is the **shared** policy. If a dataset needs extra checks, add a `qa_checks.md` inside that dataset folder **and link back here**.

---

## 🧭 Table of contents

- [🧠 What this covers](#-what-this-covers)
- [🧱 Non-negotiable principles](#-non-negotiable-principles)
- [📁 Recommended folder layout](#-recommended-folder-layout)
- [🚦 Severity levels](#-severity-levels)
- [🧪 QA gates checklist](#-qa-gates-checklist)
  - [Gate 0: Source, license, and intent](#gate-0-source-license-and-intent)
  - [Gate 1: Packaging and integrity](#gate-1-packaging-and-integrity)
  - [Gate 2: CRS, datum, and units](#gate-2-crs-datum-and-units)
  - [Gate 3: Spatial sanity](#gate-3-spatial-sanity)
  - [Gate 4: Vector geometry and topology](#gate-4-vector-geometry-and-topology)
  - [Gate 5: Raster georeferencing and pixel rules](#gate-5-raster-georeferencing-and-pixel-rules)
  - [Gate 6: Attributes and semantics](#gate-6-attributes-and-semantics)
  - [Gate 7: Time and versioning](#gate-7-time-and-versioning)
  - [Gate 8: Regression and change detection](#gate-8-regression-and-change-detection)
  - [Gate 9: Publish readiness](#gate-9-publish-readiness)
- [🔧 Suggested automation commands](#-suggested-automation-commands)
- [📝 QA report template](#-qa-report-template)
- [🆘 Troubleshooting quick hits](#-troubleshooting-quick-hits)
- [📚 Project reference docs](#-project-reference-docs)

---

## 🧠 What this covers

This checklist is optimized for **USGS mapping deliverables** such as:

- 🗺️ **Historical topo maps** (GeoTIFF/GeoPDF scans, stitched mosaics, georeferenced rasters)
- 🏔️ **Elevation products** (DEMs / DSMs / DTMs)
- 🌊 **Hydrography / boundaries / transportation** (vector layers)
- 🧯 Anything else we park inside `data/external/mappings/usgs/`

It’s designed for two workflows:

1. **Automated QA** (CI/CD gate + scripts)
2. **Human QA** (review checklist + signoff + documented exceptions)

---

## 🧱 Non-negotiable principles

✅ These are the “rules of the road” for USGS data entering KFM:

- **Reproducible ingest** 🔁  
  If we can’t reproduce it, we can’t trust it.
- **Raw stays raw** 🧊  
  Never “fix” raw files in place. Put fixes into `processed/` outputs.
- **Provenance-first** 🧾  
  Every dataset must have traceable “where did it come from?” + “what did we do to it?”.
- **Fail closed** ⛔  
  If something fundamental is missing (CRS, license, checksums, etc.), ingestion stops.
- **Prefer canonical spatial conventions** 🧭  
  Keep a stable canonical CRS for the system (commonly WGS84/EPSG:4326), while preserving original CRS alongside it.

> [!TIP]
> Treat QA like a “seatbelt”: slightly annoying until the day it saves you.

---

## 📁 Recommended folder layout

Use this layout as the default “shape” for a USGS dataset:

```text
📁 data/
  └── 📁 external/
      └── 📁 mappings/
          └── 📁 usgs/
              ├── 📁 shared/
              │   └── 📄 qa_checks.md          👈 this file
              └── 📁 <dataset_slug>/
                  ├── 📄 README.md              (what it is + how to reproduce)
                  ├── 📁 raw/                   (immutable source drop)
                  ├── 📁 processed/             (standardized outputs)
                  ├── 📁 metadata/              (FGDC/ISO/STAC/DCAT + local notes)
                  ├── 📁 provenance/            (run logs, PROV, command history)
                  ├── 📁 qa/
                  │   ├── 📄 qa_report.md       (latest)
                  │   └── 📄 qa_report.json     (latest, machine-readable)
                  └── 📁 scripts/               (pipeline + QA helpers)
```

---

## 🚦 Severity levels

Use these severities consistently across QA reports:

| Severity | Label | Meaning | Typical action |
|---:|---|---|---|
| P0 | ⛔ Blocker | Data cannot be trusted or used safely | **Reject / stop** |
| P1 | ⚠️ Major | Usable *only* with documented caveat | Fix soon + note exception |
| P2 | 🟡 Minor | Cosmetic / convenience / performance | Fix when convenient |
| P3 | 💡 Nice | Enhancements | Optional |

---

## 🧪 QA gates checklist

### Gate 0: Source, license, and intent

- [ ] ✅ **Source identification**
  - [ ] USGS source name (program/product line)
  - [ ] Stable identifier(s): download ID, product code, DOI, or catalog ID
  - [ ] Retrieval date + method (manual download, API, scripted pull)
- [ ] ✅ **License / terms**
  - [ ] License text or policy copied into `metadata/` or referenced clearly in `README.md`
  - [ ] Attribution/citation string recorded (even if “public domain”)
- [ ] ✅ **Use intent**
  - [ ] What is KFM using this for? (basemap, analysis layer, story overlay, validation, etc.)

> [!NOTE]
> If you can’t answer “where did this come from?” in 10 seconds, it’s not ready.

---

### Gate 1: Packaging and integrity

- [ ] 📦 **File integrity**
  - [ ] `checksums.sha256` (or equivalent) created for all delivered files
  - [ ] Archive expands cleanly (if ZIP/TAR) and filenames are stable
- [ ] 🧼 **No mystery edits**
  - [ ] Raw files are unchanged from the original source package
  - [ ] Any modification occurs only in `processed/`
- [ ] 🧾 **Basic inventory**
  - [ ] An inventory list exists (`qa_report.json` or `README.md`) with:
    - file path
    - file type
    - size
    - checksum
    - intended role (raw/processed/metadata)

---

### Gate 2: CRS, datum, and units

This gate exists because **CRS ambiguity is the #1 silent killer** in GIS.

- [ ] 🧭 **CRS is explicitly defined**
  - [ ] Vector: CRS present in the container (GeoPackage/GeoJSON), or `.prj` exists for Shapefile
  - [ ] Raster: CRS present in file metadata (GeoTIFF tags / GDAL reports it)
- [ ] 🧱 **Horizontal datum is known**
  - [ ] If dataset is legacy/topo/historic: confirm datum note (NAD27 vs NAD83 vs WGS84, etc.)
- [ ] 🏔️ **Vertical datum is known** (if elevation)
  - [ ] Vertical units declared (meters/feet)
  - [ ] Vertical datum identified (if provided)
- [ ] 📐 **Units match operations**
  - [ ] Any analysis expecting **meters** is not fed **degrees** (critical for rasterization, buffering, distance, area)

> [!WARNING]
> Datum mismatches can cause map shifts that “look like bad science” but are actually just bad metadata.

---

### Gate 3: Spatial sanity

- [ ] 🧭 **Extent sanity**
  - [ ] Bounding box is plausible (not global unless expected)
  - [ ] Coordinates are not swapped (lon/lat vs lat/lon)
- [ ] 🧩 **AOI expectation**
  - [ ] Data overlaps the intended area (Kansas / target region) OR the reason it doesn’t is documented
- [ ] 🧪 **Spot-check overlay**
  - [ ] Quick visual overlay in a GIS viewer against a known basemap (even a 30-second check)
  - [ ] If historical map scan: confirm visible control points roughly align (roads/river junctions/town centers)

---

### Gate 4: Vector geometry and topology

- [ ] 🧷 **Geometry validity**
  - [ ] No invalid polygons (self-intersections, rings not closed, etc.)
  - [ ] No empty geometries unless documented
- [ ] 🧠 **Topology rules**
  - [ ] Polygons that should not overlap **do not overlap**
  - [ ] Adjacent polygons meet cleanly (no gaps/slivers) when required
  - [ ] Networks (roads/rivers) have expected connectivity (no obvious breaks)
- [ ] 🧯 **Duplicate control**
  - [ ] Duplicate features are removed or explained (same geometry + same ID)

> [!TIP]
> If the dataset will ever be routed over (roads/trails), do topology checks **now**, not after the first bug report.

---

### Gate 5: Raster georeferencing and pixel rules

- [ ] 🗺️ **Georeferencing exists**
  - [ ] Raster has a non-empty CRS + affine transform
  - [ ] Pixel size is reasonable for the product
- [ ] 🧊 **NoData is defined**
  - [ ] NoData value present and matches reality (not wiping real data)
- [ ] 🧰 **Bands and interpretation**
  - [ ] Band count matches expectation (RGB vs grayscale vs multi-band)
  - [ ] Data type makes sense (uint8 vs float32, etc.)
- [ ] 🚀 **Cloud-ready optimization** (if used for web tiles)
  - [ ] COG (Cloud-Optimized GeoTIFF) or internal overviews exist (or a plan to generate them)

---

### Gate 6: Attributes and semantics

- [ ] 🧾 **Schema sanity**
  - [ ] Field names consistent and documented
  - [ ] Primary identifiers exist (or are created deterministically)
- [ ] 📏 **Units**
  - [ ] Attribute units are explicit (feet vs meters, cfs vs cms, etc.)
- [ ] 🧪 **Value validation**
  - [ ] Categorical domains are valid (no unexpected categories)
  - [ ] Numeric ranges are plausible (no impossible elevations, negative areas, etc.)
- [ ] 🔗 **Join integrity**
  - [ ] Join keys exist if the dataset is intended to link to others

---

### Gate 7: Time and versioning

- [ ] 🕰️ **Temporal metadata**
  - [ ] Dataset has a clear “as-of” date / publication date / revision date
  - [ ] If historical topo map: capture key map dates (survey/compilation/revision/publication) when available
- [ ] 🧾 **Version pinning**
  - [ ] The exact USGS version/edition is recorded (not “latest”)
- [ ] 🔁 **Update plan**
  - [ ] If this dataset will be refreshed: define refresh cadence and how diffs will be detected

---

### Gate 8: Regression and change detection

When replacing/refreshing datasets, always compare:

- [ ] 📊 **Counts**
  - [ ] Feature count delta is expected (or explained)
- [ ] 🗺️ **Extent**
  - [ ] Extent and coverage changes are expected (or explained)
- [ ] 🧪 **Basic stats**
  - [ ] Raster histogram summary or min/max sanity (if elevation imagery)
  - [ ] Attribute distributions didn’t “teleport” unexpectedly
- [ ] 🧾 **Breaking changes**
  - [ ] Schema changes are documented and downstream impacts noted

---

### Gate 9: Publish readiness

- [ ] 🗂️ **Catalog**
  - [ ] Dataset has a catalog record (STAC/DCAT/your chosen schema) with:
    - title, description, extent, time
    - CRS
    - license
    - links to artifacts
- [ ] 🧾 **Provenance**
  - [ ] A provenance record exists capturing:
    - inputs
    - transforms
    - tools + versions
    - parameters
- [ ] 🔥 **Smoke test**
  - [ ] Can we load it into the DB/services (if applicable)?
  - [ ] Does a minimal map render without shifting/exploding?

---

## 🔧 Suggested automation commands

<details>
<summary><strong>📌 File hashing</strong></summary>

```bash
# from the dataset root
find raw processed -type f -maxdepth 3 -print0 | xargs -0 sha256sum > qa/checksums.sha256
```
</details>

<details>
<summary><strong>🧭 CRS + extent (vector)</strong></summary>

```bash
# Shapefile
ogrinfo -al -so raw/my_layer.shp

# GeoPackage
ogrinfo -al -so raw/my_layer.gpkg
```
</details>

<details>
<summary><strong>🗺️ CRS + transform (raster)</strong></summary>

```bash
gdalinfo raw/my_raster.tif
gdalinfo -json raw/my_raster.tif > qa/gdalinfo.my_raster.json
```
</details>

<details>
<summary><strong>🧪 Geometry validity (Python sketch)</strong></summary>

```python
import geopandas as gpd

gdf = gpd.read_file("processed/my_layer.gpkg")
bad = (~gdf.is_valid)
print("invalid geometries:", bad.sum())

# optional: try repair (always write to processed/, never raw/)
# gdf["geometry"] = gdf.buffer(0)
```
</details>

<details>
<summary><strong>🚀 Raster overviews / COG hint</strong></summary>

```bash
# Build internal overviews (example)
gdaladdo -r average processed/my_raster.tif 2 4 8 16
```
</details>

---

## 📝 QA report template

Drop one of these in `qa/` as `qa_report.md` and/or `qa_report.json`.

<details>
<summary><strong>📄 Markdown report skeleton</strong></summary>

```markdown
# QA Report — <dataset_slug>

- Date: YYYY-MM-DD
- Reviewer: <name/handle>
- Source: <USGS product + identifier>
- Ingest method: <script/command/path>

## Summary
- P0 blockers: 0
- P1 majors: 0
- Notes: <brief>

## Gate Results
- Gate 0: PASS/FAIL
- Gate 1: PASS/FAIL
- Gate 2: PASS/FAIL
- Gate 3: PASS/FAIL
- Gate 4: PASS/FAIL
- Gate 5: PASS/FAIL
- Gate 6: PASS/FAIL
- Gate 7: PASS/FAIL
- Gate 8: PASS/FAIL
- Gate 9: PASS/FAIL

## Exceptions
- <exception id>: <reason + mitigation + owner + target date>

## Attachments
- checksums.sha256
- gdalinfo/ogrinfo dumps
- screenshots (optional)
```
</details>

<details>
<summary><strong>🤖 JSON report skeleton</strong></summary>

```json
{
  "dataset": {
    "slug": "<dataset_slug>",
    "source": "<usgs_product_identifier>",
    "retrieved_at": "YYYY-MM-DD",
    "license": "<text-or-id>"
  },
  "results": [
    { "gate": 0, "status": "pass" },
    { "gate": 1, "status": "pass" },
    { "gate": 2, "status": "pass" }
  ],
  "issues": [
    {
      "severity": "P1",
      "check_id": "CRS.DATUM.MISMATCH",
      "message": "Horizontal datum differs from expected; reprojected to canonical CRS; original preserved.",
      "mitigation": "Documented in metadata + provenance",
      "owner": "<handle>"
    }
  ]
}
```
</details>

---

## 🆘 Troubleshooting quick hits

### 🧭 “It’s shifted on the map”
- Likely CRS/datum mismatch, or axis order swap.
- Confirm: CRS is defined, datum is correct, and coordinates are in expected unit space.

### 📏 “Buffer distances look wrong”
- You probably buffered in degrees (EPSG:4326) instead of meters.
- Reproject to a meter-based CRS (UTM/local equal-area) before distance/area ops.

### 🧊 “Raster looks fine but won’t line up”
- Check for missing/incorrect geotransform, wrong EPSG, or a raster that’s visually aligned but not georeferenced properly.

### 🧷 “Vector is valid but routing fails”
- Topology issue: intersections not noded, overshoots/undershoots, duplicated segments, bridges/tunnels treated as intersections.

---

## 📚 Project reference docs

These repo-shipped PDFs heavily informed this policy:

- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Map Reading & Land Navigation.pdf`
- `Visualization of Time-Oriented Data.pdf`
- `Introduction to Digital Humanism.pdf`
- `Archaeological 3D GIS.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf`

