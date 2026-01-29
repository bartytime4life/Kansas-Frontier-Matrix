# 🌾 `<dataset_id>` — Source NOTES (Agriculture Mapping)

![status](https://img.shields.io/badge/status-draft-yellow)
![domain](https://img.shields.io/badge/domain-agriculture-2ea44f)
![stage](https://img.shields.io/badge/stage-external__source-blue)
![contracts](https://img.shields.io/badge/contracts-STAC%20%7C%20DCAT%20%7C%20PROV-purple)

> **Folder:** `data/external/mappings/agriculture/sources/<dataset_id>/`  
> **Goal:** Capture **what this dataset is**, **where it came from**, **how we ingest it**, and **how it becomes map-ready**—with provenance-first discipline ✅

---

## 📌 At-a-glance

| Field | Value |
|---|---|
| **Dataset ID** | `<dataset_id>` |
| **Dataset Name** | `<human_readable_name>` |
| **Provider / Owner** | `<org_or_agency>` |
| **Data Type** | `<vector | raster | tabular | mixed>` |
| **Primary Use in KFM** | `<basemap overlay | classification | boundary layer | analytics | labeling | tiles>` |
| **Spatial Coverage** | `<Kansas | CONUS | county list | bbox>` |
| **Temporal Coverage** | `<YYYY–YYYY | snapshot date>` |
| **Update Frequency** | `<annual | monthly | ad-hoc | static>` |
| **Upstream Version** | `<vX.Y | collection name | publication date>` |
| **License** | `<public domain | CC-BY | custom>` |
| **Internal Classification** | `<Public | Internal | Confidential | Restricted>` |
| **Last Sync** | `<YYYY-MM-DD>` |
| **Maintainer** | `<name/handle>` |

---

## 🧭 Why this dataset exists in Agriculture Mapping

**This dataset supports**:
- 🌱 Agricultural context layers (cropland/landcover/fields)
- 🧑‍🌾 Production + practice proxies (irrigation/tillage/cover crop signals)
- 🧱 Soils & capability overlays (soil classes, productivity indices)
- 🌦️ Environmental drivers (rainfall, drought indices, NDVI/phenology)

> If this dataset will be used to support claims in narratives or analytics, it must be **traceable, licensed, and reproducible**.

---

## 🗂️ Folder layout

```text
📁 data/external/mappings/agriculture/sources/<dataset_id>/
├─ 📄 NOTES.md                👈 you are here
├─ 📄 source.url              🔗 upstream URL(s) / API endpoints
├─ 📄 LICENSE.txt             ⚖️ upstream license text (or link)
├─ 📄 manifest.json           🧾 file list + sizes + checksums + dates
├─ 📁 raw/                    🧊 untouched downloads (read-only snapshots)
├─ 📁 staging/                🧰 extracted/unzipped/temporary working files
└─ 📁 logs/                   🧪 download + validation logs (optional)
```

✅ **Rule of thumb:** keep **huge binaries** here (or in object storage referenced by checksum), but commit:
- `NOTES.md`, `source.url`, `LICENSE.txt` (or link), `manifest.json`
- small representative samples only if allowed by license

---

## ⚡ Quick start (what to run)

> Replace placeholders with the actual pipeline names used in your repo.

1) **Download / refresh source**
```bash
python pipelines/mappings/agriculture/<dataset_id>/download.py
```

2) **Validate + freeze raw snapshot**
```bash
python pipelines/mappings/agriculture/<dataset_id>/validate_raw.py
```

3) **Process to canonical map-ready outputs**
```bash
python pipelines/mappings/agriculture/<dataset_id>/etl.py
```

4) **Publish contracts + lineage (non-negotiable)**
```bash
python pipelines/mappings/agriculture/<dataset_id>/publish_catalogs.py
```

---

## 🔗 Upstream source(s)

### Primary upstream link(s)
- **Landing page:** `<URL>`
- **Direct download / API:** `<URL>`
- **Docs / schema:** `<URL>`
- **Known mirrors:** `<URL>`

### `source.url` format suggestion
```text
# One URL per line
<URL>
<URL>
```

---

## ⚖️ License, attribution, and constraints

### License summary
- **License type:** `<…>`
- **Attribution required?** `<yes/no>`
- **Derivative works allowed?** `<yes/no>`
- **Redistribution allowed?** `<yes/no>`
- **Commercial use allowed?** `<yes/no>`
- **Special restrictions:** `<none | list>`

### Attribution snippet (copy/paste)
> `<Provider>` (<year>): `<Dataset Name>`. Retrieved `<YYYY-MM-DD>`. License: `<license>`.

> ⚠️ If the upstream provides a citation format, paste it verbatim here.

---

## 🧾 Metadata expectations (minimum bar)

To keep this dataset interoperable and future-proof, capture the essentials:

- **Identification** (what it is)
- **Quality** (known error/accuracy)
- **Spatial reference** (CRS/projection)
- **Entity/attribute dictionary** (fields/bands)
- **Distribution** (who provides it, how obtained)
- **Temporal info** (when collected/updated)
- **Contact** (who to ask)

✅ Use this NOTES.md for human-readable context and generate **machine-readable metadata** in your catalog layer (DCAT/STAC), plus lineage (PROV).

---

## 🧠 Data contracts + pipeline order (KFM discipline)

This dataset must follow the canonical order:

**Raw → Processed → Catalog/PROV → Database → API → UI**

**No shortcuts.** If a layer appears in the UI, it must have:
- catalog metadata (STAC/DCAT)
- provenance (PROV)
- reproducible ETL

---

## 📥 Acquisition details

### Download method
- [ ] Manual download
- [ ] Scripted HTTP download
- [ ] API client
- [ ] ArcGIS REST
- [ ] Google Earth Engine export
- [ ] Other: `<…>`

### Raw snapshot rules ✅
- **Do not modify raw files**
- Store raw data as dated snapshots if the upstream updates:
  - `raw/2026-01-29/<files...>`
- Record **checksums** in `manifest.json`

### `manifest.json` suggested shape
```json
{
  "dataset_id": "<dataset_id>",
  "retrieved_at": "<YYYY-MM-DD>",
  "upstream_version": "<string>",
  "files": [
    {
      "path": "raw/<date>/file.ext",
      "bytes": 0,
      "sha256": "<hex>",
      "source_url": "<URL>"
    }
  ]
}
```

---

## 🧼 Processing & standardization (what “done” means)

### Canonical outputs (choose what applies)
- **Vector:** `GeoPackage` / `GeoJSON` / `GeoParquet` + optional **vector tiles** (PMTiles)
- **Raster:** **COG GeoTIFF** (+ overviews) + optional **raster tiles**
- **Tabular:** `Parquet` + data dictionary + join keys

### CRS / projection rules
- **Keep original CRS recorded**
- **Pick a canonical analytic CRS** (commonly `EPSG:4326` or a Kansas-appropriate projection)
- **For rasterization & distance-based ops:** use a **projected CRS in meters** (avoid doing meter math in `EPSG:4326`)

> 🧩 Tip: if you rasterize vectors or compute pixel sizes, your input should be in a Cartesian/projection-in-meters CRS.

### Normalization checklist
- [ ] Clip to Kansas AOI (if applicable)
- [ ] Fix invalid geometries (vector)
- [ ] Remove slivers / dissolve where appropriate
- [ ] Normalize column names to `snake_case`
- [ ] Standardize units (document conversions)
- [ ] Ensure time fields parse consistently (`YYYY-MM-DD`)
- [ ] Add stable IDs (join keys)
- [ ] Build “legend” mapping for coded attributes

---

## 🧪 QA / QC

### Always run
- [ ] File integrity (size + checksum matches manifest)
- [ ] CRS detected and recorded
- [ ] Bounds sanity check (Kansas overlaps expected)
- [ ] Nulls / NaNs assessed + documented
- [ ] Duplicates checked (features or records)
- [ ] Geometry validity (vector)
- [ ] NoData + data type sanity (raster)

### If classification / landcover product
- [ ] Accuracy assessment plan documented (sample design)
- [ ] Confusion matrix or published accuracy referenced
- [ ] Known error modes listed (e.g., crop confusion, phenology overlaps)

---

## 🧩 Schema / data dictionary

### Core fields / bands
| Field/Band | Type | Units | Meaning | Notes |
|---|---:|---:|---|---|
| `<field>` | `<type>` | `<units>` | `<meaning>` | `<notes>` |

### Code lists (if applicable)
| Code | Label | Notes |
|---:|---|---|
| `<n>` | `<label>` | `<notes>` |

---

## 🗺️ Map rendering defaults (optional but helpful)

> Store “style defaults” here so map layers look consistent.

- **Default visibility:** `<on/off>`
- **Opacity:** `<0–1>`
- **Color ramp / palette:** `<…>`
- **Classification:** `<quantile | equal interval | categorical>`
- **Legend title:** `<…>`
- **Hover fields:** `<field1, field2>`

---

## 🔌 Integration targets in KFM

### Output destinations (fill in actual paths used in your repo)
- **Processed data:** `data/processed/mappings/agriculture/<dataset_id>/…`
- **Catalog (DCAT):** `data/catalog/dcat/<dataset_id>.json` (or `data/catalog/dcat/datasets/...`)
- **Catalog (STAC):** `data/stac/collections/<dataset_id>.json` + `data/stac/items/...`
- **Provenance (PROV):** `data/prov/<dataset_id>/<run_id>.json` *(or `data/provenance/...`)*

### Database / API
- **PostGIS table(s):** `<schema.table>`
- **Vector tileset id:** `<tileset_id>`
- **API route(s):** `/api/layers/<dataset_id>` (example)

---

## 🧾 Provenance log (human-readable)

> In addition to PROV JSON, keep a simple log here for quick audits.

| Date | Action | Who/What | Input snapshot | Output artifact(s) | Notes |
|---|---|---|---|---|---|
| `<YYYY-MM-DD>` | `<download>` | `<script/person>` | `raw/<date>/...` | `—` | `<…>` |
| `<YYYY-MM-DD>` | `<etl>` | `<pipeline>` | `raw/<date>/...` | `data/processed/...` | `<…>` |

---

## 🐞 Known issues / caveats

- ⚠️ `<issue_1>`
- ⚠️ `<issue_2>`
- ✅ Workarounds: `<…>`

---

## 🧊 Changelog

- **`<YYYY-MM-DD>`** — `<what changed>` (upstream version: `<…>`)
- **`<YYYY-MM-DD>`** — `<what changed>`

---

## ✅ “Ready for map” gate (definition of done)

- [ ] License confirmed + attribution written
- [ ] Raw snapshot frozen + checksummed
- [ ] Processed outputs generated deterministically
- [ ] STAC/DCAT metadata published
- [ ] PROV lineage published
- [ ] QA checks passed + documented
- [ ] Layer renders correctly in map UI (style defaults recorded)

---

## 📚 References (project-internal)

- Kansas Frontier Matrix (KFM) Technical Blueprint (provenance-first pipeline + monorepo philosophy)
- KFM v13 Markdown/Repo Guide (directory + contract conventions)
- Earth Engine Remote Sensing guide (agriculture + time-series + classification workflows)
- Map design + metadata guidance (copyright, metadata essentials)

