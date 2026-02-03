# 📦 `data/external/` — External Data Staging (Bring-Your-Own-Data)

![Data Layer](https://img.shields.io/badge/Data-Layer%3A%20External-6f42c1?style=for-the-badge)
![Policy](https://img.shields.io/badge/Policy-Provenance--First-success?style=for-the-badge)
![Repo Hygiene](https://img.shields.io/badge/Repo-Hygiene-important?style=for-the-badge)

> 🧭 **Purpose:** `data/external/` is a **local staging area** for datasets that **cannot** (or **should not**) live in Git — e.g., too large, license-restricted, or access-controlled.  
> ✅ KFM still requires the **same documentation discipline**: metadata + provenance + reproducible fetch instructions.

---

## 🧠 How this fits the KFM data flow

KFM follows a strict, traceable sequence:

➡️ **Raw → Processed → Catalog/Provenance → Database → API → UI**

`data/external/` exists *alongside* that sequence as a **storage pressure valve**:
- It holds **inputs** and **intermediate artifacts** that are sourced externally.
- The **source of truth** remains:
  - `data/raw/` for “commit-worthy” raw evidence
  - `data/processed/` for curated outputs
  - `data/catalog/` + `data/provenance/` for traceability and auditability

---

## ✅ What belongs here (and what does NOT)

### ✅ Good candidates for `data/external/`
- 🛰️ **Huge rasters / imagery** (e.g., multi-GB GeoTIFF collections)
- 🔐 **License-restricted datasets** (requires separate download agreement)
- 🏛️ **Archive scans** (TIFF/PDF bundles too large for repo)
- 🌐 **API exports** or **bulk pulls** that are reproducible but not commit-friendly
- 🧪 **Working caches** used during pipeline runs (downloaded once; re-used locally)

### ❌ Do **NOT** put these here
- 🔑 **Secrets / API keys / credentials** (use env vars + secret managers)
- 🧬 **Processed outputs meant to ship** (those go in `data/processed/`)
- 🧾 **Anything that should be reviewable in PR diff** (commit it properly)
- 🧍 **Sensitive/PII** unless the project explicitly supports private deployments + governance

---

## 🧷 Golden Rules (Non-Negotiables)

1) 🧊 **Treat external data as immutable**  
   Never “edit in place.” If something’s wrong, re-download or re-export.

2) 🧾 **Everything must be reproducible**  
   If someone can’t recreate your external files from:
   - a manifest + checksums + script + documented source  
   …then it doesn’t belong in the system.

3) 🧭 **No data enters KFM undocumented**  
   Even if the bytes aren’t committed, the dataset must have:
   - **Metadata** (catalog record)
   - **Provenance** (lineage: inputs → script → outputs)

4) ⚖️ **Respect licensing & access restrictions**  
   If the license forbids redistribution, only commit manifests/metadata and keep bytes external.

---

## 📁 Recommended folder layout

> This layout is designed to keep things organized **by dataset ID** and make fetches repeatable.

```text
data/
  external/
    README.md
    manifests/                 # ✅ committed: fetch recipes + checksums
      <dataset_id>.yml
    cache/                     # ❌ not committed: temporary downloads, partials
    sources/                   # ❌ not committed: downloaded data organized by provider/topic
      <provider_or_topic>/
        <dataset_id>/
          (files...)
```

---

## 🧾 External dataset manifest (required)

Create a manifest per dataset at:

✅ `data/external/manifests/<dataset_id>.yml`

### Suggested schema
```yaml
id: ks_usgs_water_daily_v1
title: "USGS Water Daily Export (Kansas)"
provider: "USGS"
source:
  type: "http"
  url: "https://example.gov/dataset/export.zip"
license: "public-domain-or-url"
retrieval:
  method: "pipelines/usgs_water/fetch.py"
  notes: "Requires bbox + date range params"
integrity:
  sha256: "<sha256-of-archive-or-primary-file>"
  bytes: 123456789
storage:
  location: "data/external/sources/usgs/ks_usgs_water_daily_v1/"
  git_tracked: false
kfm:
  raw_equivalent: "data/raw/usgs_water/"     # if a smaller canonical subset is committed
  processed_outputs:
    - "data/processed/hydrology/usgs_water_daily.parquet"
  catalog_record: "data/catalog/ks_usgs_water_daily_v1.stac.json"
  provenance_record: "data/provenance/ks_usgs_water_daily_v1.prov.json"
```

> 🧷 **Tip:** Store checksums for the **primary artifact** (zip/tar/geotiff) and optionally per-file for multi-asset bundles.

---

## 🛠️ Workflow: Adding a new external dataset

### 1) Decide: `raw/` vs `external/`
Use this quick test:

- ✅ Put it in `data/raw/` when:
  - It’s small enough to version
  - License allows redistribution
  - It’s stable “evidence” you want forever

- ✅ Put it in `data/external/` when:
  - It’s too large for repo norms
  - License prohibits redistribution
  - It requires authentication / gated access
  - It’s generated via a reproducible export pipeline

### 2) Add a fetch script (or reuse an existing one)
- Put the fetch logic under `pipelines/<source>/` (preferred).
- The script should:
  - download/export
  - write into `data/external/sources/...`
  - compute SHA256
  - update or validate the manifest

### 3) Add catalog + provenance records
Even if bytes are external, KFM expects:
- 🧾 `data/catalog/` record (STAC/DCAT-style)
- 🧬 `data/provenance/` record (lineage: source → fetch → transform → outputs)

### 4) Produce *processed* outputs into `data/processed/`
Pipelines should generate curated outputs that:
- are standardized
- are usable by database loaders / API endpoints
- have stable identifiers

---

## 🧼 Git hygiene (recommended)

✅ Only commit:
- `README.md`
- `manifests/**`

❌ Do not commit:
- `sources/**`
- `cache/**`

Suggested `.gitignore` (add in `data/external/.gitignore`):
```gitignore
# Ignore everything by default
*

# Keep docs + manifests
!README.md
!manifests/
!manifests/**
!.gitignore
```

---

## 🧯 Troubleshooting

### “My pipeline works locally but fails in CI”
✅ Expected if your pipeline depends on `data/external/`.  
CI environments often **do not** have access to gated data.

Fix patterns:
- Provide a **tiny committed fixture** under `data/raw/fixtures/…`
- Add a **mock mode** for CI
- Separate “fetch” from “transform” so transform can run on fixtures

### “My external dataset changed upstream”
If upstream is not stable:
- Pin to a versioned release if possible
- Capture **retrieval date**, **URL**, and **hash**
- Consider storing a **snapshot** in an approved external bucket (S3/Drive/etc.)
  - Commit only the pointer + checksum + governance notes

---

## 🔗 Related folders

- 📁 `data/raw/` — canonical raw evidence (when commit-friendly)
- 📁 `data/processed/` — curated datasets used by the platform
- 📁 `data/catalog/` — dataset metadata (STAC/DCAT)
- 📁 `data/provenance/` — lineage logs (W3C PROV / custom)

---

## 🧭 One-line definition

> `data/external/` is **where big or restricted inputs live**, while **documentation, metadata, and provenance still live in Git** ✨