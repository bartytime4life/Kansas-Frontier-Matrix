# 🗺️ Historical Mapping Source Notes — <SOURCE_NAME>

![type](https://img.shields.io/badge/type-notes.md-6e40c9)
![domain](https://img.shields.io/badge/domain-historical-2ea44f)
![layer](https://img.shields.io/badge/layer-external%2Fmappings-0ea5e9)
![status](https://img.shields.io/badge/status-draft-yellow)

> **TL;DR**: This file defines **what the source is**, **how we ingest/normalize it**, and **how we publish it into KFM** (STAC/DCAT/PROV + DB + API/UI).  
> <!-- Evidence: KFM uses an ingestion pipeline + shared spatial reference + STAC-like catalog + COG/GeoJSON outputs:contentReference[oaicite:0]{index=0}; Pipeline order is “inviolable”:contentReference[oaicite:1]{index=1} -->

---

## 🧾 Source Identity

| Field | Value |
|---|---|
| **source_slug** | `<source_slug>` (kebab-case) |
| **source_name** | `<SOURCE_NAME>` |
| **publisher / custodian** | `<ORG / AGENCY / ARCHIVE>` |
| **source_type** | `raster` / `vector` / `tiles` / `mixed` |
| **primary region** | `<Kansas / County / Multi-state / etc>` |
| **temporal coverage** | `<YYYY–YYYY>` (or `<circa YYYY>`) |
| **spatial coverage** | `<bbox / statewide / county list>` |
| **native CRS / datum** | `<EPSG:#### or “unknown / varies”>` |
| **license / rights** | `<Public domain / CC / custom / TBD>` |
| **access method** | `<bulk download / API / scrape / manual>` |
| **last verified** | `2026-01-29` |

> ✅ **Slug guidance**: keep `source_slug` stable, kebab-case, and consistent with other KFM slugs (e.g., `land-treaties`).  
> <!-- Evidence: slugged dataset path example `historical/land-treaties`:contentReference[oaicite:2]{index=2} -->

---

## 🎯 Intended Use in KFM

- What research questions does this source unlock?  
  - `<e.g., change detection, settlement evolution, hydrology changes, land ownership boundaries, etc.>`
- What KFM UI affordances should this support?  
  - `<time slider/timeline, layer toggle, click-through to metadata, etc.>`  
  <!-- Evidence: KFM UI uses time slider and layered exploration; catalog includes bbox/time range/source info:contentReference[oaicite:3]{index=3} -->

---

## 🧬 KFM Integration Contract

### ✅ Canonical pipeline order
**Raw → Processed → Catalog/Prov → Database → API → UI** (treat as inviolable).  
<!-- Evidence: blueprint explicitly states this order is inviolable:contentReference[oaicite:4]{index=4} -->

### 🗂️ Expected directory layout pointers
Even though this file lives under `data/external/mappings/...`, the *data artifacts* should still align to the canonical `data/<domain>/...` layout (raw/work/processed/mappings/etc.).  
<!-- Evidence: master guide’s domain layout includes `raw/`, `work/`, `processed/`, and `mappings/` under each domain such as `historical/`:contentReference[oaicite:5]{index=5} -->

```text
📁 data/
  📁 external/
    📁 mappings/
      📁 historical/
        📁 <source_slug>/
          📝 notes.md   👈 (this file)

📁 data/
  📁 historical/
    📁 raw/
      📁 <source_slug>/
    📁 work/
      📁 <source_slug>/
    📁 processed/
      📁 <source_slug>/
    📁 mappings/
      📁 <source_slug>/   (optional: machine mappings, schemas, crosswalks)
```

---

## 🧱 Data Shape, Formats, and Normalization Targets

### 🎛️ Supported outputs (preferred)
- **Raster** → Cloud Optimized GeoTIFF (**COG**)  
- **Vector** → **GeoJSON** (or shapefile when needed for legacy)  
- **Interactive** → **map tiles** and/or **KML/KMZ** when useful for Earth/web overlays  
<!-- Evidence: KFM design explicitly calls for COGs for rasters, GeoJSON/shapefiles for vectors, and tiles or KML/KMZ for interactive use:contentReference[oaicite:6]{index=6} -->

### 🧭 CRS / datum / projection considerations
- Record **native CRS + datum** *as observed*; do not guess.  
- If multiple inputs vary, normalize to `<TARGET_EPSG>` and document the conversion.  
- Expect conversions: datasets based on different datums/ellipsoids may not align without transformation.  
<!-- Evidence: datasets based on different ellipsoids/datums “will not work together” and conversion is expected; WGS84 and NAD83 context:contentReference[oaicite:7]{index=7} -->

> 📌 Practical reminder: at large scales, projection distortion is often less visible, but it can bite when combining layers with different projections.  
> <!-- Evidence: distortion discussion and layer-combination issue:contentReference[oaicite:8]{index=8} -->

### 🗺️ (Optional) Scale & “map-type” notes
- If source is cartographic (paper maps/scans), capture:
  - nominal **map scale** (e.g., `1:24,000`, `1:100,000`)  
  - edition year / publish year vs survey year  
- Some military map guidance ties common scale ranges to common projections (document what’s relevant for your source).  
<!-- Evidence: map-reading reference notes about transverse Mercator and Lambert conformal conic by scale bands:contentReference[oaicite:9]{index=9} -->

---

## 🧾 Metadata Requirements

### 🧷 Minimum metadata to capture (KFM-friendly)
KFM expects a catalog-like record per dataset/layer (and sometimes per item), including:
- original URL / archive reference
- coordinate system
- resolution / scale
- temporal coverage
- processing summary (what we did + how)  
<!-- Evidence: STAC-like catalog enumerates original URL/reference, CRS, resolution, temporal coverage, and processing notes:contentReference[oaicite:10]{index=10} -->

### 🗂️ STAC / DCAT / PROV “publish gates”
Every processed artifact should ship with:
- **STAC** (collection + items where appropriate)
- **DCAT** dataset entry (for discovery / governance)
- **PROV** lineage (what produced what, when, with what config)  
<!-- Evidence: master guide requires artifacts to be cataloged (STAC/DCAT) and traced (PROV) as part of the evidence artifact pattern:contentReference[oaicite:11]{index=11} -->

#### Suggested STAC properties (starter)
```yaml
# stac.item.properties (starter — customize!)
kfm:source_slug: "<source_slug>"
kfm:domain: "historical"
kfm:layer_type: "raster|vector|tiles"
kfm:scale: "<1:24000|unknown>"
kfm:year_start: <YYYY>
kfm:year_end: <YYYY>
kfm:georeferencing:
  method: "<manual_gcp|auto|native_geotiff>"
  control_points: <int_or_null>
  rmse_meters: <float_or_null>
proj:epsg: <EPSG_int_or_null>
```

---

## ⚙️ Ingestion & Processing Plan

### 🧰 Scripts / pipeline hooks
- Pipeline scripts should remain **small & focused**, invoked via CLI/Makefile, and cover steps like:
  - download/fetch
  - georeference (if needed)
  - convert TIFF → COG
  - build overlays / KMZ packaging  
<!-- Evidence: design doc describes small focused scripts like `georef_map.py` and `pack_kmz.py` invoked via Makefile/CLI as core pipeline steps:contentReference[oaicite:12]{index=12} -->

### 🧊 Raster normalization recipe (COG)
<details>
<summary>🧊 Example: GeoTIFF → COG (GDAL)</summary>

```bash
# 1) Validate / inspect
gdalinfo input.tif

# 2) Convert to COG (example settings — tune for your source)
gdal_translate input.tif output_cog.tif \
  -of COG \
  -co COMPRESS=DEFLATE \
  -co LEVEL=9 \
  -co OVERVIEWS=IGNORE_EXISTING

# 3) Build overviews if needed (depends on workflow and COG driver behavior)
gdaladdo -r average output_cog.tif 2 4 8 16 32
```
</details>

### 🧷 Vector normalization recipe
<details>
<summary>🧷 Example: Shapefile → GeoJSON (OGR)</summary>

```bash
ogr2ogr -f GeoJSON output.geojson input.shp \
  -t_srs EPSG:<TARGET_EPSG>
```
</details>

---

## ✅ QA / Validation Checklist

- [ ] **Integrity**: hashes recorded for raw inputs (sha256)  
- [ ] **CRS sanity**: CRS/datum known (or explicitly unknown) + transformations documented  
- [ ] **Georeferencing**: visually spot-check overlays against a modern basemap  
- [ ] **COG validity**: `gdalinfo` confirms COG structure + overviews exist  
- [ ] **Temporal tags**: year/range encoded in metadata + consistent naming  
- [ ] **Catalog**: STAC/DCAT generated and passes schema validation  
- [ ] **PROV**: lineage links raw → processed → published artifacts  
- [ ] **UI smoke test**: layer loads and can be toggled (and time-filtered if applicable)  
<!-- Evidence: KFM emphasizes traceability/metadata in ingestion and STAC-like indexing by bbox/time range/source info:contentReference[oaicite:13]{index=13} -->

---

## ⚖️ License / Rights Notes

> ⚠️ **Don’t assume “it’s old” means “it’s free.”**  
> Maps (as representations) are commonly protected by copyright; the *facts/data* may not be, but photographic reproduction of a copyrighted map is not the same as extracting facts. Treat rights as **TBD until verified**.  
> <!-- Evidence: map representations are covered under U.S. copyright; data/facts are not, and photographic reproduction is restricted; “best to assume works are copyrighted until you learn otherwise.”:contentReference[oaicite:14]{index=14} -->

**Fill this in:**
- Rights statement: `<…>`  
- Allowed uses: `<…>`  
- Attribution requirement: `<…>`  
- Redistribution allowed?: `<yes/no/tbd>`  

---

## 🧪 Example (Filled) — USGS Historical Topographic Maps

> Use this as a reference fill-out. Copy the structure, not necessarily the values.

<details>
<summary>📌 Example: <code>source_slug = usgs-historical-topo-maps</code></summary>

### Source Identity (example)
| Field | Value |
|---|---|
| source_slug | `usgs-historical-topo-maps` |
| source_name | `USGS Historical Topographic Map Collection` |
| source_type | `raster` (georeferenced scanned topo maps) |
| temporal coverage | `1880s–2000s` |
| key value | baseline per era + multi-edition change detection |
| org strategy | organize layers by date + scale; tag each map’s year/range in STAC-like metadata |

<!-- Evidence: USGS historical topo maps from 1880s–2000s as baseline; georeferenced overlay; organize by date/scale; STAC-like metadata tags year/range:contentReference[oaicite:15]{index=15} -->

### KFM mapping highlights (example)
- Output: **COGs** + (optional) tiles/KMZ for interactive viewing  
- Catalog: STAC-like JSON with bbox + time range + source info  
<!-- Evidence: KFM calls for COGs/GeoJSON + STAC-like indexing and interactive tile/KML/KMZ support:contentReference[oaicite:16]{index=16} -->

</details>

---

## 📚 References inside the repo (project files)

- KFM architecture & data layer design (STAC-like catalog, COG/GeoJSON/KMZ targets)  
  <!-- Evidence: architecture + ingestion + outputs + UI time slider:contentReference[oaicite:17]{index=17} -->
- KFM canonical pipeline ordering (raw → … → UI)  
  <!-- Evidence: “inviolable” pipeline order:contentReference[oaicite:18]{index=18} -->
- Master Guide v13: artifact pattern + STAC/DCAT/PROV requirements + domain layout  
  <!-- Evidence: evidence artifact + STAC/DCAT/PROV:contentReference[oaicite:19]{index=19}; domain folder layout includes mappings:contentReference[oaicite:20]{index=20} -->
- Cartography/metadata/datum notes to avoid projection surprises  
  <!-- Evidence: metadata categories & standards focus:contentReference[oaicite:21]{index=21}; datum/ellipsoid compatibility + conversions:contentReference[oaicite:22]{index=22}; projection-by-scale note:contentReference[oaicite:23]{index=23} -->

---

## ✅ Definition of Done

- [ ] Filled all `<PLACEHOLDERS>` in this file  
- [ ] Raw artifacts stored + hashed  
- [ ] Processed artifacts created (COG/GeoJSON/tiles as applicable)  
- [ ] STAC/DCAT/PROV generated and validated  
- [ ] Source is queryable via DB/API and viewable in UI (at least a smoke test)


