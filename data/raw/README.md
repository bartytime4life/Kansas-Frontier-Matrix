# 🧱 `data/raw/` — Immutable Raw Data (Source Snapshots)

![stage](https://img.shields.io/badge/data-stage_raw-blue)
![policy](https://img.shields.io/badge/policy-write_once%20%7C%20read_only-orange)
![provenance](https://img.shields.io/badge/provenance-required-brightgreen)
![governance](https://img.shields.io/badge/governance-FAIR%2BCARE-purple)

> **Raw = evidence.** This folder holds *exact source snapshots* (downloads, scans, scrapes) and is treated as **write-once / read-only**.  
> Pipelines may **read** from here, but must **never modify** anything here. [^kfm-raw]

---

## 🎯 Purpose

`data/raw/` is the **staging area for input data as obtained from original sources**, preserved without modification to keep an auditable “chain of custody” from evidence → outputs. [^kfm-raw]

This enables:
- 🧾 **Reproducibility**: re-run ETL years later against the same artifacts. [^kfm-raw]
- 🧬 **Traceability**: provenance can reference *exact* inputs (including checksums / source pointers). [^prov-inputs]
- 🧠 **Governed knowledge**: no dataset “enters” KFM without licensing + metadata gates. [^kfm-doc-gate] [^kfm-fail-closed]

---

## ✅ What goes in `data/raw/`

Examples (non-exhaustive):
- 📦 **Zips / archives** exactly as downloaded (optionally *plus* extracted contents in the same folder)
- 🗺️ **Shapefiles** (and sidecar files) / GeoPackages as delivered
- 🧾 **CSVs** / JSON exports / scraped dumps (unchanged)
- 🖼️ **Scanned maps** (`.tif`, `.jpg`, `.pdf`) as scanned
- 🛰️ **Raster sources** (if small enough for Git) or **pointers** to object storage/DVC (if large) [^kfm-large] [^dvc]

---

## 🚫 What does **NOT** go in `data/raw/`

- ❌ Anything *cleaned*, normalized, reprojected, clipped, deduped, etc. → put that in `data/processed/`
- ❌ Pipeline intermediates / scratch outputs → use `data/work/` or an equivalent temp workspace [^mg-domain]
- ❌ “Quick fixes” to outputs → fix **pipeline code** (or replace raw snapshot properly) and re-run [^kfm-no-edits]

---

## 🗂️ Recommended structure

KFM allows organizing by **source** or **topic/domain** (choose one and be consistent within a domain). [^kfm-raw]

### Option A — group by *source/provider* ✅
```text
data/raw/
  usgs_water/
    <dataset>/
      snapshot_YYYY-MM-DD/
        ...
  noaa_climate/
    <dataset>/
      snapshot_YYYY-MM-DD/
        ...
```

### Option B — group by *topic/domain* ✅
```text
data/raw/
  historical_maps/
    1930_county_map/
      1930_county_map.pdf
      source.yaml
      checksums.sha256
  census/
    1900/
      census_1900.csv
      source.yaml
      checksums.sha256
```

### 🧭 Domain expansion rule (when adding a new domain)
- Put raw sources under `data/raw/<new-domain>/`
- Use `data/work/<new-domain>/` for intermediate processing
- Output final curated artifacts to `data/processed/<new-domain>/`
- Document ETL + sources in a domain runbook under `docs/data/<new-domain>/` [^mg-domain]

---

## 🧾 Required “sidecar” files (per dataset folder)

Raw files should be accompanied by **minimal machine + human readable context**, so downstream PROV/STAC/DCAT can be generated accurately and reviewed quickly. [^maps-metadata] [^mg-stac]

### 1) `source.yaml` (minimum metadata)

Create **one `source.yaml` per dataset folder** (or per snapshot if the dataset updates over time):

```yaml
dataset_id: historical_maps__1930_county_map
title: "Kansas County Map (1930) — Scanned PDF"
description: >
  Briefly describe what this raw artifact is, what it covers, and why it matters.

source:
  provider: "Kansas Historical Society"
  homepage: null
  url: "https://example.org/source-page"   # where it came from
  retrieved_at: "2026-01-30"
  retrieved_by: "YOUR_NAME_OR_HANDLE"
  method: "download|scan|scrape|api_export"
  license: "UNKNOWN|Public Domain|CC-BY-4.0|..."  # do not leave ambiguous
  citation: "Provider (Year). Title. URL. Accessed YYYY-MM-DD."

coverage:
  spatial:
    region: "Kansas"
    bbox_wgs84: null
  temporal:
    start: "1930-01-01"
    end: "1930-12-31"

data_characteristics:
  format: "pdf"
  notes: "Any quirks, missing pages, encoding issues, etc."

governance:
  sensitivity: "public|internal|restricted"
  pii: false
  restrictions: null
```

**Why this matters:** dependable geographic data expects metadata such as identification, spatial reference, distribution/use policy, citation, temporal info, and contact details. [^maps-metadata]

### 2) `checksums.sha256` (immutability proof)

```bash
# from inside the dataset folder
sha256sum * > checksums.sha256
```

Example file:
```text
9d5c... 1930_county_map.pdf
```

> These checksums are especially helpful because provenance logs commonly reference raw inputs by filename **plus** checksum and/or source URL pointers. [^prov-inputs]

---

## 🧩 Adding new raw data (PR checklist)

- [ ] Create a domain folder under `data/raw/<domain>/...` (or extend an existing one) [^kfm-raw]
- [ ] Add raw files **exactly as obtained** (no “helpful” conversions) [^kfm-raw]
- [ ] Add `source.yaml` with **license + citation + retrieval date** [^maps-metadata]
- [ ] Add `checksums.sha256`
- [ ] If the raw artifact is large, follow the **Large Files Policy** (below) [^kfm-large] [^dvc]
- [ ] Add/adjust pipeline(s) to produce outputs in `data/processed/` (no manual edits) [^kfm-no-edits]
- [ ] Ensure downstream metadata + provenance are created/updated (`data/catalog/`, `data/provenance/`) — CI expects it [^kfm-doc-gate] [^mg-stac]

---

## 🧯 Fixing issues found in raw data

Raw is treated as “sacrosanct evidence.” If an error is found:
- Prefer **adding a corrected snapshot** (new `snapshot_YYYY-MM-DD/`) and recording what changed in `source.yaml`
- Or replace the artifact in Git with clear history (and/or keep the old copy elsewhere + reference it), but avoid “silent edits” [^kfm-raw]

---

## 📦 Large Files Policy (Git-friendly, still auditable)

KFM recognizes that **very large data** can be challenging in Git and may require:
- storing **references + hashes** in the repo,
- slicing into smaller diffable chunks,
- or using object storage (e.g., S3) while keeping the repo as the **catalog of record**. [^kfm-large]

For large rasters / 3D / point clouds, the project design also supports **DVC** to track big artifacts without bloating Git. [^dvc]

**Rule of thumb**
- ✅ Small/medium artifacts: commit directly into `data/raw/`
- ✅ Large artifacts: commit a **pointer + checksum** (and keep the remote location stable and governed)

---

## 🔁 Where `data/raw/` sits in the canonical pipeline

```mermaid
flowchart LR
  raw["🧱 data/raw/ (evidence)"] --> etl["⚙️ pipelines/ (deterministic ETL)"]
  etl --> processed["📦 data/processed/ (curated outputs)"]
  processed --> catalogs["🧾 data/catalog/ (STAC/DCAT)"]
  processed --> prov["🧾 data/provenance/ (PROV lineage)"]
  catalogs --> graph["🕸️ graph/runtime stores"]
  prov --> graph
  graph --> api["🔌 API layer"]
  api --> ui["🗺️ UI"]
  ui --> stories["📚 Story Nodes"]
```

The ordering is **non-negotiable**: ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes. [^mg-order]

---

## ⚖️ Licensing, copyright, and “don’t break the build”

### License is mandatory ✅
If data is added without a license, KFM is designed to **fail closed** (CI blocks the merge). [^kfm-fail-closed]

### Maps and scanned works require extra care 🗺️
Maps/charts are covered by copyright in their *representation*, and it’s best to assume works are copyrighted until verified otherwise. [^maps-copyright]

---

## 🧭 Related docs & standards (project files)

- 📘 KFM Comprehensive Technical Blueprint  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- 🧾 Master Guide v13 (STAC/DCAT/PROV + invariants)  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- 🗺️ Metadata & copyright notes (GIS map design guide)  [oai_citation:2‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)  
- 🧩 Large data versioning option (DVC design note)  [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  

---

## 📌 Footnotes / Sources

[^kfm-raw]: `data/raw/` is defined as immutable source snapshots (write-once/read-only) and can be grouped by source/topic; raw is preserved as evidence and is not edited by pipelines.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^kfm-no-edits]: KFM rule: processed data must not be manually edited; fix pipeline or raw inputs and re-run to maintain reproducibility.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^kfm-doc-gate]: Pipelines must update catalog + provenance artifacts; contributions missing these are expected to be rejected by CI (“no data enters KFM without documentation”).  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^kfm-fail-closed]: “Fail closed” governance: if checks fail (e.g., missing license), CI blocks the action/merge.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^kfm-large]: Large data in Git is challenging; KFM may store references/hashes for huge data (e.g., rasters), slice into diffable chunks, or use external storage while keeping the repo as the record.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^prov-inputs]: Provenance logs record raw input entities with references such as filename plus checksum and/or pointer to source URL.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

[^mg-stac]: KFM requires STAC/DCAT/PROV alignment for each dataset/evidence artifact; CI validates conformance to defined profiles.  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

[^mg-order]: Pipeline ordering is stated as absolute/inviolable in the Master Guide invariants.  [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

[^mg-domain]: Domain expansion pattern: use `data/raw/<new-domain>/`, `data/work/<new-domain>/`, output to `data/processed/<new-domain>/`, and maintain a domain README/runbook in `docs/data/<new-domain>/`.  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

[^maps-metadata]: GIS guidance highlights the need for detailed metadata (identification, quality, spatial reference, distribution/use policy, citation, temporal info, contact) and emphasizes standards/interoperability.  [oai_citation:13‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

[^maps-copyright]: GIS guidance notes maps/charts are covered under copyright for their representation and recommends assuming works are copyrighted until confirmed otherwise.  [oai_citation:14‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

[^dvc]: Design note proposes DVC for large data artifacts to avoid bloating Git while still tracking data versions alongside code.  [oai_citation:15‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)