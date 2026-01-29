# 🗺️ USGS Historical Topographic Maps (HTMC / US Topo) — `us_topo_historical`

![Dataset](https://img.shields.io/badge/dataset-us_topo_historical-0b7285)
![Source](https://img.shields.io/badge/source-USGS-1f2937)
![Type](https://img.shields.io/badge/type-raster%20maps%20%2F%20GeoTIFF%20%2F%20GeoPDF-334155)
![License](https://img.shields.io/badge/license-public%20domain%20%28mostly%29-166534)
![KFM Pipeline](https://img.shields.io/badge/KFM%20pipeline-raw%E2%86%92processed%E2%86%92catalog%2Fprov%E2%86%92db%E2%86%92api%E2%86%92ui-7c3aed)

📍 **Repo path:** `data/external/mappings/usgs/datasets/us_topo_historical/`

---

## 🎯 What this dataset is (and why we keep it)

This folder is the **external-source landing zone** for **USGS historical topographic map products** used as *time-aware basemaps* inside Kansas Frontier Matrix (KFM).

These high-resolution, georeferenced topo maps are the “baseline layer” for many eras — enabling:
- 🕰️ **Time-swipe / change detection** (towns, railroads, river courses, roads)
- 🧭 **Overlay workflows** (e.g., “1870s Kansas Territory” vs modern imagery)
- 🧱 **Map-derived digitization** (vector extraction in later pipelines)

> [!NOTE]
> **KFM rule:** datasets must flow through the pipeline in order (Raw → Processed → Catalog/Prov → DB → API → UI). This directory is intentionally **Raw/External-first** — processed derivatives live elsewhere. ✅

---

## 🔗 Official USGS entry points (bookmark these)

- 🗺️ **TopoView (browse + download)**: `https://ngmdb.usgs.gov/topoview/`
- 🧾 **Historical Topographic Maps (HTMC overview)**: `https://www.usgs.gov/programs/national-geospatial-program/historical-topographic-maps-preserving-past`
- 🌐 **The National Map Download Client** (bulk downloads): `https://apps.nationalmap.gov/downloader/`
- 🧰 **TNM Access API** (scriptable downloads): `https://apps.nationalmap.gov/tnmaccess/`
- 📦 **USGS Topo map licensing FAQ** (public domain rules + exceptions):  
  `https://www.usgs.gov/faqs/are-usgs-topographic-maps-copyrighted`

---

## 🧠 What “Historical” means here

This dataset is primarily built from:

- 🏛️ **HTMC** (Historical Topographic Map Collection): printed topo maps **1884–2006** (scanned + published digitally)
- 🧩 Optional continuity: **US Topo** (computer-generated topo maps **2009–present**) when you want modern topo in the same timeline

We treat both as a single “time stack” so the UI can offer a smooth topo timeline.

---

## 🗂️ Folder layout (recommended)

> [!TIP]
> Raw topo maps are big. Keep Git clean: **store raw binaries via DVC / LFS / object storage**, and keep *metadata + manifests* in Git.

```text
📁 us_topo_historical/
├─ 📄 README.md                      👈 you are here
├─ 📄 dataset.yaml                   🧾 dataset-level contract (recommended)
├─ 📄 sources.json                   🔗 authoritative source endpoints + notes
├─ 📁 raw/                           📦 downloaded source products (NOT in Git)
│  ├─ 📁 geopdf/
│  ├─ 📁 geotiff/
│  ├─ 📁 jpeg/
│  └─ 📁 kmz/
├─ 📁 inventory/                     🧮 HTMC/US Topo inventory CSV snapshots
├─ 📁 checksums/                     🔐 sha256 files (integrity + reproducibility)
└─ 📁 logs/                          🧰 fetch/process logs (timestamps matter)
```

---

## ⚙️ Acquisition options

### Option A — Manual (fastest for a few quads)
1. Open **TopoView**
2. Zoom to your AOI (Kansas + buffer, if desired)
3. Choose map scale and year/edition
4. Download preferred format:
   - ✅ **GeoTIFF** (best for GIS pipelines)
   - ✅ **GeoPDF** (best for human reading + carries attachments)
   - ✅ **KMZ** (easy for Google Earth)
   - ✅ **JPEG** (quick preview)

### Option B — Bulk (Download Client)
Use **The National Map Download Client** to filter by:
- State / bounding box
- Product type (Historical Topo / US Topo)
- Format

### Option C — Scripted (recommended for reproducibility)
Use **TNMAccess API** or TopoView’s **inventory CSV** to:
- generate a deterministic list of product IDs/URLs
- download with retries + checksums
- snapshot the inventory used for this run into `inventory/`

> [!IMPORTANT]
> Always capture:
> - the inventory snapshot used
> - the exact URLs/product IDs requested
> - download timestamps + checksums  
> This is *not bureaucracy* — it is the foundation of provenance.

---

## 🧱 Processing expectations (where this goes next)

This dataset is “raw external”. Downstream processing typically produces:

- 🟦 **COGs (Cloud Optimized GeoTIFF)** for fast range-requests + web streaming
- 🧩 **Web tiles** (e.g., PMTiles / MBTiles) for browser rendering
- 🌍 **KML/KMZ** derivatives for Google Earth (optional)
- 🧾 **STAC Items / Collections** to drive time sliders and discovery
- 🧬 **PROV** bundles logging every transformation

> [!NOTE]
> We aim to standardize rasters into predictable formats for KFM’s viewer and analysis layers.  
> Keep raw files immutable; derive everything else.

---

## 🧾 Metadata + provenance contract (KFM-required)

Every map sheet (or derived raster) should become a **time-aware asset** in the catalog.

### Required artifacts (minimum)
- 🧭 **STAC Collection + STAC Items** (spatiotemporal discoverability)
- 🗃️ **DCAT dataset entry** (global catalog visibility)
- 🧬 **PROV activity bundle** (how it was produced, by whom/what, when, with what inputs)

> [!WARNING]
> If you add map files but skip metadata/provenance, you’re creating a “data orphan.”  
> In KFM, orphans don’t ship.

### Suggested STAC Item fields (for each sheet)
- `id` (stable: USGS product ID preferred)
- `bbox` + `geometry`
- `datetime` or `start_datetime` / `end_datetime`  
  *(maps often represent an edition year; use best-known date range)*
- `properties`:
  - `title` (quad name + year)
  - `usgs:series` (`HTMC` / `US Topo`)
  - `usgs:scale`
  - `proj:epsg`
  - `gsd` (if known)
  - `created` (ingest time)
  - `license`
- `assets`:
  - `geotiff` / `geopdf` / `kmz`
  - `metadata_xml` (if bundled/provided)
  - `thumbnail` (optional but helpful)

### PROV “must include”
- original source URL(s) + product ID(s)
- retrieval timestamp
- checksums
- processing toolchain + versions
- parameters (crop/neatline, compression, reprojection decisions)
- responsible agent (human + pipeline)

---

## 🏷️ Naming conventions (predictable + grep-friendly)

### ✅ Raw downloads
Prefer something stable and globally unique:

```text
raw/<format>/USGS__<product_id>__<quad_slug>__<year>__<scale>.<ext>
```

Examples:
```text
raw/geotiff/USGS__12345678__lawrence-ks__1956__24000.tif
raw/geopdf/USGS__12345678__lawrence-ks__1956__24000.pdf
raw/kmz/USGS__12345678__lawrence-ks__1956__24000.kmz
```

### ✅ Checksums
```text
checksums/USGS__12345678__sha256.txt
```

### ✅ Inventory snapshots
```text
inventory/topoview_inventory__YYYY-MM-DD.csv
```

---

## ✅ Validation checklist (before moving to processed)

- [ ] File opens (GeoTIFF/GeoPDF/KMZ) ✅
- [ ] Georeferencing is present & sane (bounds match quad/AOI) 🧭
- [ ] SHA256 recorded for each raw artifact 🔐
- [ ] Inventory snapshot captured (if using scripted/bulk) 🧮
- [ ] STAC Item drafted (even if “raw-only” stage) 🧾
- [ ] PROV stub created (download activity at minimum) 🧬

---

## ⚖️ License & attribution (read this)

Most USGS-produced topographic maps are **public domain**.

However, **US Topo (2009–present)** has a few important exceptions (commercially licensed components in specific years/places). When those apply:
- retain the copyright notices
- preserve/ship the attached metadata and credit legend
- attribute properly in downstream products

✅ If in doubt, inspect:
- the map collar / credit legend
- the attached XML metadata (often bundled with GeoTIFF downloads or attached to GeoPDF)

---

## 🤝 Contributing a new quad / edition (PR checklist)

1. 📦 Add raw file(s) to the storage mechanism (DVC/LFS/remote)
2. 🔐 Add checksum file(s) under `checksums/`
3. 🧮 Add or update inventory snapshot under `inventory/`
4. 🧾 Add STAC Item stub (even if “raw-stage”)
5. 🧬 Add PROV record for download activity
6. ✅ Document anything weird (missing georef, wrong bounds, odd year labels)

---

## 🧩 Glossary (quick)
- 🟦 **COG**: Cloud Optimized GeoTIFF (web-friendly GeoTIFF with internal tiling + overviews)
- 🧾 **STAC**: SpatioTemporal Asset Catalog (standard for cataloging geospatial assets)
- 🗃️ **DCAT**: Data Catalog Vocabulary (dataset-level cataloging standard)
- 🧬 **PROV**: Provenance model (how data came to be)
- 🗺️ **HTMC**: Historical Topographic Map Collection (USGS scanned legacy maps)
- 🧭 **US Topo**: USGS topo series (2009–present)

---

## 📌 TODOs (expected next hardening)
- [ ] Add `dataset.yaml` contract and wire into validation CI ✅
- [ ] Add `sources.json` with TNMAccess endpoints + inventory URL(s)
- [ ] Add a `fetch_us_topo_historical` script target (Makefile/CLI)
- [ ] Add a `process_to_cog` pipeline step + reproducible configs
- [ ] Add STAC Collection skeleton for this dataset

