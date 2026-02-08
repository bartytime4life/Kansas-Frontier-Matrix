# 📦 `data/raw/` — Immutable Source Data (Read‑Only) 🧊

![Data Stage](https://img.shields.io/badge/data_stage-raw-informational)
![Truth Path](https://img.shields.io/badge/policy-truth_path-critical)
![Provenance](https://img.shields.io/badge/provenance-required-success)
![No Edits](https://img.shields.io/badge/rule-never_edit_in_place-red)

> 🧭 **“The map behind the map” starts here.**  
> `data/raw/` holds **unaltered source snapshots** that feed KFM pipelines. Treat it like a museum archive: label it, checksum it, don’t “fix” it.

---

## 🎯 Overview

### Purpose
This folder is the **landing zone for original inputs** (downloads, exports, scans, vendor drops, agency releases) **before** they are cleaned, standardized, or transformed.

### Canonical Ordering (Non‑Negotiable)
KFM’s pipeline is strict. **Nothing skips the line.**  

**Raw → Work → Processed → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**

> If an output cannot be regenerated from raw + pipeline code + config (with lineage), it is not reproducible.

---

## ✅ What Belongs in `data/raw/`

- Original vendor/agency archives (`.zip`, `.7z`, `.tar.gz`)
- Original file exports (`.csv`, `.xlsx`, `.gpkg`, `.shp`, `.tif`, `.pdf`, etc.)
- Original scans (TIFF/JPEG/PDF)
- Original API exports as delivered (no normalization)
- Sidecar provenance notes (**see `source.yaml`**) and integrity files (**see `checksums.sha256`**)

### ❌ What Must *Never* Be in `data/raw/`
- Cleaned/normalized CSVs
- Reprojected / clipped / dissolved / simplified geodata
- Derived tiles / COG conversions / geometry fixes
- Model outputs, OCR outputs, AI-derived layers (those are **evidence artifacts → `data/processed/`**)
- Secrets: tokens, keys, passwords, `.env`, private credentials
- Unreviewed sensitive personal data (PII) or restricted community data (see governance section below)

---

## 🧱 Golden Rules (Non‑Negotiable)

1. **🚫 Never edit raw files in place**
   - If something is “wrong,” that’s part of the historical record.
   - Fixes happen in `src/pipelines/` and land in `data/processed/`.

2. **📌 Raw is an audit trail**
   - Raw must remain stable so provenance can point back to exact artifacts.

3. **🧼 No derived outputs in `raw/`**
   - Derived artifacts belong in `data/work/` (intermediate) or `data/processed/` (canonical outputs).

4. **🧳 Preserve original packaging**
   - Prefer storing the original archive as‑is.
   - Only extract if the pipeline requires it (and keep the original archive too).

5. **🔐 Security + sovereignty first**
   - Do not place secrets here.
   - Do not place restricted/sensitive datasets here unless they are explicitly approved and handled per governance (often: store in restricted storage and commit only metadata/pointers).

---

## 🗂 Directory Layout

### Primary (Stage‑First) Layout (this folder)
```text
data/raw/
  README.md
  <domain>/                          # e.g., hydrology/, historical/, remote_sensing/
    <dataset_id>/                    # stable slug (snake_case)
      source.yaml                    # intake metadata + provenance starter
      checksums.sha256               # integrity manifest (recommended)
      snapshots/                     # immutability snapshots (recommended)
        2026-02-03/                  # ISO acquisition date
          original.zip               # original packaging
          extracted/                 # only if required by pipeline
            ...
```

### Equivalent (Domain‑First) Layout (if your repo uses it)
Some v13 layouts group by domain under `data/<domain>/raw|work|processed`.  
If you use that structure, **apply the same rules** and keep `source.yaml` + checksums adjacent to the raw artifacts.

```text
data/
  <domain>/
    raw/
      <dataset_id>/
        ...
```

---

## 🏷 Dataset IDs (`<dataset_id>`)
Use **lowercase `snake_case`** and keep it stable over time:
- `census_1900_county`
- `usgs_nwis_daily_discharge`
- `kdot_roads_centerlines`
- `landsat_scenes_kansas`

Recommendation: Align `<dataset_id>` with the identifiers used in:
- STAC Collection IDs (for cataloging)
- DCAT dataset identifiers (for discovery)
- PROV entity identifiers (for lineage)

---

## 🏷 Naming Conventions

- **Dates:** ISO `YYYY-MM-DD` (sortable)
- **Snapshots:** `snapshots/YYYY-MM-DD/`
- **Avoid spaces:** use `_`
- **Keep originals recognizable:** do not rename beyond necessity

Examples:
- `2026-02-03__kdot_roads.zip`
- `2025-11-01__nwis_daily.csv`

---

## 🧾 Required Intake Sidecar: `source.yaml`

KFM requires metadata + license + sensitivity context **before outputs can be treated as published**.  
We capture that as early as possible in `data/raw/.../source.yaml` so pipelines can generate the required catalog/provenance artifacts later.

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
  license: ""              # SPDX if possible (e.g., CC-BY-4.0), else plain text
  citation: ""             # formal citation if provided
  upstream_version: ""     # optional: agency version tag / release id

governance:
  # IMPORTANT: classification must never be downgraded downstream without review.
  sensitivity: "public|internal|restricted"
  classification: "open|restricted|confidential"
  care_label: "Public|Restricted|Tribal Sensitive"
  restrictions: ""         # free text summary (e.g., "no redistribution", "IRB required")
  pii: "none|possible|present"

  # Optional: use when sovereignty/ownership controls apply
  owner_group: ""          # e.g., tribal nation / steward group
  access_level: "public|restricted"
  consent_basis: ""        # optional: "community consent", "public domain", etc.
  takedown_contact: ""     # optional: who to contact for corrections/takedown

scope:
  geography: "Kansas"
  spatial_extent:
    bbox_wgs84: [minLon, minLat, maxLon, maxLat]   # optional
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
  processing_hints: []      # optional: any upstream quirks for ETL maintainers
```
</details>

---

## 🔒 Checksums: `checksums.sha256` (Strongly Recommended)

Integrity manifests help detect accidental edits/corruption and support deterministic re-runs.

Example:
```text
<sha256>  snapshots/2026-02-03/original.zip
<sha256>  snapshots/2026-02-03/extracted/roads.shp
```

---

## ⚖ Governance, Sovereignty, and Sensitive Data Handling

KFM’s governance requires:
- **no data leakage**
- **no silent downgrades of sensitivity/classification**
- **review gates for restricted or sovereignty-sensitive datasets**

Practical rules for `data/raw/`:
- If a dataset is **restricted/confidential**, prefer **restricted storage** (object store / private repo) and commit:
  - `source.yaml`
  - checksums (if appropriate)
  - a pointer/reference file describing where the raw artifact is stored and how access is governed
- If you find **PII present** and it’s not explicitly authorized/approved:
  - stop intake,
  - move the artifact to restricted handling,
  - document the decision and next steps in the domain runbook (`docs/data/<domain>/...`)

---

## 🧰 Large Artifacts (COGs, LiDAR, Big Rasters) 🐘

If it makes Git painful, don’t force it:
- Use **DVC** or **Git LFS** for big binaries when appropriate
- Or store in **object storage** (S3/MinIO/etc.) and reference from catalogs
- Keep `source.yaml` and checksums so the lineage stays intact

---

## ⚙️ How Pipelines Should Use Raw Data

Pipelines must:
- ✅ **Read from** `data/raw/<domain>/<dataset_id>/...`
- 🚫 **Never modify** anything in `data/raw/`
- ✅ Write intermediate work to: `data/work/<domain>/...`
- ✅ Write canonical outputs to: `data/processed/<domain>/...`

Then (before anything is “published” / consumed by graph, API, UI, or Story Nodes), produce the required boundary artifacts:
- ✅ STAC: `data/stac/collections/` and `data/stac/items/`
- ✅ DCAT: `data/catalog/dcat/`
- ✅ PROV: `data/prov/`

> Evidence artifacts (OCR corpora, model outputs, AI-derived layers) follow the exact same rule: **processed + cataloged + prov’d**, never placed into raw.

---

## 🔁 Updating or Re‑Fetching Data (Never Overwrite)

If an upstream source updates:
- Add a **new snapshot**: `snapshots/YYYY-MM-DD/`
- Update `source.yaml` if license/scope/classification changed
- Re-run pipelines to create updated processed outputs + catalogs + lineage

This preserves the audit trail and supports time-based comparisons.

---

## ✅ Intake Checklist (Before a PR)

- [ ] Created `data/raw/<domain>/<dataset_id>/`
- [ ] Added `source.yaml` with **URL + retrieval date + license + classification**
- [ ] Stored raw artifact(s) under `snapshots/YYYY-MM-DD/`
- [ ] Added `checksums.sha256` (or equivalent)
- [ ] Confirmed **no derived outputs** were placed in `data/raw/`
- [ ] Confirmed **no secrets** are present
- [ ] Confirmed PII/sensitive handling is correct for governance level
- [ ] Ran pipeline and produced:
  - [ ] `data/work/...` (if applicable)
  - [ ] `data/processed/...`
  - [ ] `data/stac/...`
  - [ ] `data/catalog/dcat/...`
  - [ ] `data/prov/...`

---

## 🆘 Common Gotchas

- **“I reprojected the shapefile to EPSG:4326 and replaced it.”**  
  ❌ Don’t. Put the reprojected result in `data/processed/`.

- **“The agency ZIP has nested folders and weird names.”**  
  ✅ Keep it. Normalize in the pipeline.

- **“I ran OCR / an ML model and put outputs next to the raw scans.”**  
  ❌ Don’t. That’s an evidence artifact → `data/processed/` + STAC/DCAT/PROV.

- **“This dataset contains addresses / individuals.”**  
  🚫 Stop. Move to restricted handling and document the plan.

---

## 🔗 Related (Repo‑Local)

- `src/pipelines/` — ETL code (domain pipelines)
- `data/work/` — intermediate outputs (ephemeral / reproducible)
- `data/processed/` — canonical cleaned outputs
- `data/stac/` — STAC collections/items (catalog interface)
- `data/catalog/dcat/` — DCAT dataset entries (discovery interface)
- `data/prov/` — W3C PROV lineage bundles (lineage interface)
- `docs/data/<domain>/` — domain runbooks + intake notes
- `docs/standards/` — KFM profiles (STAC/DCAT/PROV) + governance protocols

---

**✨ Reminder:** Raw is sacred. Processing is where the magic happens. 🧙‍♂️
