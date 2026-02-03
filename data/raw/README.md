# 📦 `data/raw/` — Immutable Source Data (Read‑Only) 🧊

![Data Stage](https://img.shields.io/badge/data_stage-raw-informational)
![Truth Path](https://img.shields.io/badge/policy-truth_path-critical)
![Provenance](https://img.shields.io/badge/provenance-required-success)
![No Edits](https://img.shields.io/badge/rule-never_edit_in_place-red)

> 🧭 **“The map behind the map” starts here.**  
> `data/raw/` holds **unaltered source snapshots** that feed KFM pipelines. Treat it like a museum archive: label it, checksum it, don’t “fix” it.

---

## 🎯 Purpose

This folder is the **landing zone for original inputs** (downloads, exports, scans, vendor drops, agency releases) **before** they are cleaned, standardized, or transformed.

**Raw ➜ Processed ➜ Catalog/Provenance ➜ Databases ➜ API ➜ UI/AI**  
Nothing skips the line. ✅

---

## 🧱 Golden Rules (Non‑Negotiable)

1. **🚫 Never edit raw files in place**
   - If something is “wrong,” that’s part of the historical record.
   - Fixes happen in `pipelines/` and land in `data/processed/`.

2. **🧾 Every dataset gets “source context”**
   - Record where it came from, when it was fetched, license, and what’s inside.

3. **🧼 No derived outputs in `raw/`**
   - No cleaned CSVs, reprojected GeoJSON, clipped rasters, simplified shapes, etc.

4. **🧩 Preserve original packaging**
   - Keep vendor/agency folder structure when possible.
   - Prefer storing the original `.zip` plus (optional) extracted contents *only if required*.

5. **🔐 No secrets or sensitive personal data**
   - Never store API keys, tokens, passwords, or private datasets here.

---

## 🗂 Recommended Folder Structure

You can organize by **domain** then **dataset** (preferred), or by dataset only—pick one approach and be consistent.

```text
data/raw/
  README.md  ✅ (this file)
  <domain>/                        # e.g., hydrology/, historical/, remote_sensing/
    <dataset_id>/                  # stable slug (snake_case)
      source.yaml                  # required 🧾
      checksums.sha256             # strongly recommended 🔒
      snapshots/                   # optional but great for immutability 🧊
        2026-02-03/                # ISO date of acquisition
          original.zip
          extracted/               # only if needed by pipeline
            ...
```

### ✅ Dataset IDs (`<dataset_id>`)
Use **lowercase `snake_case`** and keep it stable over time:
- `census_1900_county`
- `usgs_nwis_daily_discharge`
- `kdot_roads_centerlines`
- `landsat_scenes_kansas`

---

## 🏷️ Naming Conventions

- **Dates:** ISO format `YYYY-MM-DD` (sortable!)
- **Versioned snapshots:** `snapshots/YYYY-MM-DD/`
- **Avoid spaces:** use `_` not spaces
- **Keep originals recognizable:** don’t rename beyond necessity

Examples:
- `2026-02-03__kdot_roads.zip`
- `2025-11-01__nwis_daily.csv`

---

## 🧾 Required Sidecar Metadata: `source.yaml`

Each dataset folder must include a `source.yaml` describing provenance and constraints.

<details>
<summary><strong>📄 Minimal <code>source.yaml</code> template (copy/paste)</strong></summary>

```yaml
id: "<dataset_id>"
title: ""
description: ""

origin:
  publisher: ""
  source_urls:
    - ""
  retrieved_at: "YYYY-MM-DD"
  retrieved_by: ""
  license: ""             # SPDX if possible (e.g., CC-BY-4.0), otherwise plain text
  citation: ""            # preferred formal citation if provided

scope:
  geography: "Kansas"
  spatial_extent:
    bbox_wgs84: [minLon, minLat, maxLon, maxLat]   # optional but helpful
  temporal_extent:
    start: "YYYY-MM-DD"     # optional
    end: "YYYY-MM-DD"       # optional

files:
  packaging: "zip|folder|single_file|api_export"
  contents:
    - path: "snapshots/YYYY-MM-DD/original.zip"
      description: ""
      sha256: ""            # optional here if using checksums.sha256

notes:
  known_issues: []
  pii: "none|possible|present"
  restrictions: ""
```
</details>

---

## 🔒 Checksums: `checksums.sha256` (Strongly Recommended)

Why: helps detect accidental edits, corrupted transfers, and supports deterministic re-runs.

Example file:
```text
<sha256>  snapshots/2026-02-03/original.zip
<sha256>  snapshots/2026-02-03/extracted/roads.shp
```

---

## 🧰 Large Files (COGs, LiDAR, Big Rasters) 🐘

Raw artifacts can be huge. Recommended options:
- **DVC** (preferred for big data artifacts)
- **Git LFS** (acceptable when appropriate)
- **External object storage pointers** (S3/Azure/GCS), tracked with metadata

Rule of thumb:
- If it makes Git painful, don’t force it into Git. Track it cleanly.

---

## ⚙️ How Pipelines Should Use `data/raw/`

Pipelines should:
- ✅ **Read from** `data/raw/<domain>/<dataset_id>/...`
- 🚫 **Never modify** anything in `data/raw/`
- ✅ Write outputs to:
  - `data/processed/` (cleaned/standardized outputs)
  - `data/catalog/` (STAC/DCAT metadata)
  - `data/provenance/` (W3C PROV lineage logs)

> If you can’t regenerate processed outputs from raw + pipeline code, it’s not reproducible. 🧪

---

## 🔁 Updating or Re‑Fetching Data (Don’t Overwrite!)

If a source updates:
- Add a **new snapshot**: `snapshots/YYYY-MM-DD/`
- Update `source.yaml` if scope or license changed
- Run the pipeline to create updated processed outputs + provenance

✅ This keeps an audit trail and supports time-based comparisons.

---

## ✅ Intake Checklist (Before a PR)

- [ ] Created `data/raw/<domain>/<dataset_id>/`
- [ ] Added `source.yaml` with **URL + retrieval date + license**
- [ ] Stored raw artifact(s) in `snapshots/YYYY-MM-DD/`
- [ ] Added `checksums.sha256` (or equivalent)
- [ ] Confirmed no derived/cleaned outputs are placed in `raw/`
- [ ] Confirmed no secrets / sensitive personal data present
- [ ] Ran pipeline and produced:
  - [ ] `data/processed/...`
  - [ ] `data/catalog/...`
  - [ ] `data/provenance/...`

---

## 🆘 Common Gotchas

- **“I reprojected the shapefile to EPSG:4326 and replaced it.”**  
  ❌ Don’t. Put the reprojected result in `data/processed/`.

- **“The agency ZIP has nested folders and weird names.”**  
  ✅ Keep it. Normalize in the pipeline.

- **“This dataset contains addresses / individuals.”**  
  🚫 Stop. Move to restricted storage and document the handling plan.

---

## 🔗 Related (Repo‑Local)

- `pipelines/` — ETL scripts and notebooks
- `data/processed/` — cleaned outputs
- `data/catalog/` — STAC/DCAT metadata
- `data/provenance/` — lineage logs (W3C PROV)
- `docs/standards/` — project governance + profiles (STAC/DCAT/PROV)

---

**✨ Reminder:** Raw is sacred. Processing is where the magic happens. 🧙‍♂️