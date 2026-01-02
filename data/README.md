# 🗃️ `data/` — Kansas Frontier Matrix Data Lake + Catalog

![Geo](https://img.shields.io/badge/geo-vector%20%2B%20raster-informational)
![Lifecycle](https://img.shields.io/badge/lifecycle-raw%20%E2%86%92%20work%20%E2%86%92%20processed-blue)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-success)
![Serving](https://img.shields.io/badge/serving-API%20%2B%20Map%20UI-ff69b4)

This folder is the **single source of truth for KFM datasets** (raw → intermediate → published), plus the **metadata artifacts** that make KFM traceable, auditable, and discoverable (STAC/DCAT/PROV).

> ✅ **Design intent:** KFM treats data pipelines as staged ETL with clear phases (ingest → transform → load → publish/serve). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧭 Quick links

- 📘 Project overview: `../README.md`
- 🌐 Web app docs: `../web/README.md`
- 🧩 Standards & diagrams: see **KFM metadata alignment** (STAC/DCAT/PROV) in the project guide. [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧱 Data lifecycle (required)

KFM uses **explicit staging** so it’s obvious what’s raw, what’s intermediate, and what’s ready for users:

- **`data/raw/<domain>/`** → raw ingested sources  
- **`data/work/<domain>/`** → intermediate transforms (scratch + QA checkpoints)  
- **`data/processed/<domain>/`** → final, reusable outputs (what the API/UI should rely on)

This staging layout is a **required convention** in KFM. [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Why this matters 🧠
- **Reproducibility:** raw stays raw (re-run transforms anytime). [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- **Auditability:** every published dataset has provenance + catalog entries (below). [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Performance:** processed outputs can be indexed/served quickly (tiles, vector simplifications, DB indexes). [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🗂️ Directory layout

```text
data/
  README.md

  raw/                         # ✅ raw source drops (minimal changes)
    <domain>/
      ...

  work/                        # 🧪 intermediate outputs, checkpoints, scratch
    <domain>/
      ...

  processed/                   # ⭐ “published” outputs used by API/UI
    <domain>/
      ...

  stac/                        # 🛰️ STAC records (geo assets)
    collections/
    items/

  catalog/                     # 📚 discovery catalogs
    dcat/                      # DCAT JSON-LD entries

  prov/                        # 🧾 provenance bundles (lineage)
    ...

  exports/                     # 📦 human-friendly exports (optional)
  tmp/                         # 🧯 safe-to-delete scratch (local only)
```

### 🛰️ Catalog boundary artifacts (required)
Before data is considered “published,” it must generate:
- **STAC** records → `data/stac/collections/` and `data/stac/items/`  
- **DCAT** dataset entry → `data/catalog/dcat/`  
- **PROV** lineage bundle → `data/prov/`  

These “boundary artifacts” are required and form the interface to downstream stages (graph/API/UI). [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔁 How data moves through KFM (ETL + serving)

KFM pipelines are conceptualized as:

1. **Ingestion (Extract)**  
2. **Processing (Transform)**  
3. **Storage (Load)**  
4. **Publication / Serving** (APIs + visualizations)

This is the standard KFM pipeline model. [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

### Common ingestion modes
- **Scheduled batch ingest** (e.g., daily satellite updates, weekly reports) using cron/Airflow-style scheduling. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- **Streaming ingest** (e.g., sensors) via MQTT/HTTP → queue/raw store. [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- **Manual uploads** (admin/domain expert supplied CSVs, surveys). [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

> 🔐 **Rule:** Store raw inputs first with minimal transformation so re-processing is always possible. [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🗺️ Data types we support (and preferred formats)

KFM is inherently **spatiotemporal**, so we plan for both **vector** and **raster** workflows:
- In GIS terms, most data is either **raster** (pixel grids) or **vector** (points/lines/polygons). [oai_citation:12‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk)

### ✅ Vector (points / lines / polygons)
Preferred:
- **GeoPackage** (`.gpkg`) for durable local exchange
- **GeoJSON** (`.geojson`) for web-friendly interchange (keep it simplified!)
- **Parquet + GeoParquet** when appropriate (analytics-first)

### ✅ Raster (imagery / grids)
Preferred:
- **GeoTIFF** (`.tif`), ideally as **COG** (Cloud-Optimized GeoTIFF) for fast map serving

> Example: KFM workflows explicitly mention ingesting GeoTIFF and tagging by date/region before further processing. [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

### ✅ Tabular / timeseries
Preferred:
- **Parquet** (`.parquet`) for analytics + ML feature stores
- **CSV** (`.csv`) for “hand-off” datasets (but treat as less strict)

---

## 🧾 STAC / DCAT / PROV alignment (non-negotiable)

Every new dataset or evidence artifact **must** have:
- **STAC Collection + Items** (for geospatial assets)  
- **DCAT dataset entry** (for discovery)  
- **PROV activity bundle** (how it was produced)

This policy is required in KFM. [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Cross-linking expectations 🔗
- **STAC Items** point to the actual assets (files or endpoints) in `data/processed/**` (or equivalent stable storage). [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **DCAT** entries include distribution links to STAC or direct resources. [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **PROV** captures raw → intermediate → processed lineage, including run IDs/commit hashes where possible. [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Evidence artifacts (ML/simulation outputs) are first-class datasets

KFM treats **analysis outputs** (simulations, OCR corpora, AI-predicted layers, etc.) as datasets that must:
- be stored in `data/processed/...`
- be cataloged in **STAC/DCAT**
- be traced in **PROV**
- be exposed only through governed APIs (not hardcoded in UI)

This is an explicit KFM rule. [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🏷️ Naming conventions

Be boring. Be searchable. Be stable.

### File naming pattern (recommended)
```text
<source>__<dataset>__<domain>__<region>__<YYYY-MM-DD>__v<major>.<ext>
```

Examples:
```text
usgs__landsat_ndvi__agriculture__kansas__2025-03-01__v1.tif
noaa__precip_daily__climate__kansas__2025-03-01__v1.parquet
kfm__ndvi_weekly_county__agriculture__kansas__2025-W09__v2.parquet
```

> KFM explicitly calls out date+region tagging for ingested imagery naming to keep a coherent data lake. [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧰 Database + warehouse guidance (PostGIS + file storage)

KFM uses “best of both worlds”:
- SQL databases (relational + constraints + spatial indexing)
- Object/file storage for large binaries + historical archives [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

### PostGIS organization tip 🧩
It’s common to store spatial tables in a **non-default schema** (not `public`) to keep the DB organized and backups cleaner. [oai_citation:21‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### Materialized views ⚡
For UI-heavy aggregates, use materialized views like “avg NDVI per county per week,” refreshed on schedule. [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## ✅ Data quality, validation, and checks

Pipelines should include validations after load, e.g.:
- “all expected stations present”
- “no wildly out-of-range values”
- schema checks and constraints

KFM explicitly calls out post-load validation and alerting to prevent bad data from propagating. [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

Minimum recommended checks:
- 🧾 schema validation (columns, types, ranges)
- 🗺️ geometry validity (self-intersections, null geometries)
- 🌍 CRS normalization (document + enforce)
- 🧊 raster nodata & band metadata sanity
- 🧮 reproducibility (hashes/checksums on outputs)

---

## ➕ Adding a new dataset (contributor checklist)

### 1) Pick a domain folder 🗂️
- `data/raw/<new-domain>/`
- `data/work/<new-domain>/`
- `data/processed/<new-domain>/` [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 2) Ingest raw data 📥
- Save originals with minimal modification (don’t “fix” raw).
- Record where it came from and licensing.

### 3) Transform in `work/` 🧪
- Normalize CRS/units
- Clean + join + derive metrics (e.g., NDVI computation is a common example in KFM pipelines). [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

### 4) Publish to `processed/` ⭐
- Outputs must be stable and reusable
- Prefer performant formats (COG, Parquet)

### 5) Generate required metadata artifacts 🧾
- STAC → `data/stac/...`
- DCAT → `data/catalog/dcat/...`
- PROV → `data/prov/...` [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 6) Add a domain runbook 📓
Maintain a concise README under:
- `docs/data/<new-domain>/README.md` (ETL procedures, sources, gotchas) [oai_citation:27‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔐 Security & privacy notes

- **Do not commit secrets** (API keys, database URLs, tokens).
- Treat any user-submitted data and sensor identifiers as potentially sensitive.
- For governed access, KFM uses tiered networking (public web layer, private DB/processing) and controlled API boundaries. [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧹 Git strategy for data (recommended defaults)

- Commit **metadata, schemas, small samples**, and **catalog artifacts**
- Keep **large raw binaries** out of Git; store via object storage, DVC, or external dataset registry

Suggested `.gitignore` patterns (adapt to your workflows):
```gitignore
# big data
data/raw/**
data/work/**
data/tmp/**
# allow metadata + catalogs
!data/**/README.md
!data/stac/**
!data/catalog/**
!data/prov/**
```

---

## 📚 Project references (in-repo library)

Core project docs & standards:
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- KFM Markdown & metadata standards (STAC/DCAT/PROV)  [oai_citation:32‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:33‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Geospatial + remote sensing references:
- GIS basics  [oai_citation:34‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)
- Geoprocessing with Python (GDAL/OGR patterns)  [oai_citation:35‡geoprocessing-with-python.pdf](file-service://file-NkXrdB4FwTruwhQ9Ggn53T)
- Python Geospatial Analysis Cookbook  [oai_citation:36‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)  [oai_citation:37‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- Cloud-Based Remote Sensing with Google Earth Engine  [oai_citation:38‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk)
- Google Earth Engine Applications  [oai_citation:39‡Google Earth Engine Applications.pdf](file-service://file-SmoZrQ3nZSAdHHNqcVzYCq)
- Making Maps (map design guidance)  [oai_citation:40‡Spectral Geometry of Graphs.pdf](file-service://file-DWxRbQDZGktGtiWtzAQxs8)

Engineering + infrastructure references:
- Clean Architectures in Python  [oai_citation:41‡clean-architectures-in-python.pdf](file-service://file-6YHot4AqfpdbcrdfiYfpHM)
- Node.js Notes for Professionals  [oai_citation:42‡Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf](file-service://file-9qS1yEFvCBXbDdtTfpt3Ye)  [oai_citation:43‡Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf](file-service://file-9qS1yEFvCBXbDdtTfpt3Ye)
- PostgreSQL Notes for Professionals  [oai_citation:44‡PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf](file-service://file-742sw3gADJniEdmC19JeAC)
- MySQL Notes for Professionals  [oai_citation:45‡MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf](file-service://file-GQ5jWwmLZCFb6enxwykaRh)  [oai_citation:46‡MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf](file-service://file-GQ5jWwmLZCFb6enxwykaRh)
- Introduction to Docker  [oai_citation:47‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)

Data science + methods references:
- Applied Data Science with Python & Jupyter  [oai_citation:48‡applied-data-science-with-python-and-jupyter.pdf](file-service://file-2PdBHtR24Wq7MYWfG8agQo)
- Scalable Data Management for Future Hardware  [oai_citation:49‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)
- Scientific Method / Research protocol guide  [oai_citation:50‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Digital Humanism (ethics + governance context)  [oai_citation:51‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)
- Principles of Biological Autonomy (systems thinking)  [oai_citation:52‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf)

UI + visualization references:
- Responsive Web Design (HTML5/CSS3)  [oai_citation:53‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- WebGL Programming Guide  [oai_citation:54‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  [oai_citation:55‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)
- MATLAB Programming for Engineers  [oai_citation:56‡MATLAB Programming for Engineers Stephen J. Chapman.pdf](file-service://file-GVz6J2tWsQSJL4sFY1Niqe)
- Implementing Programming Languages  [oai_citation:57‡implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf](file-service://file-JaNsY7yoyJTAzMJSwt9LDA)

---

## ✅ TL;DR checklist (pin this)

- [ ] Raw data → `data/raw/<domain>/`
- [ ] Intermediate work → `data/work/<domain>/`
- [ ] Publish outputs → `data/processed/<domain>/`
- [ ] Produce metadata → STAC + DCAT + PROV [oai_citation:58‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Validate quality (ranges, geometry, CRS) [oai_citation:59‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- [ ] Keep big files out of Git (use remote storage)