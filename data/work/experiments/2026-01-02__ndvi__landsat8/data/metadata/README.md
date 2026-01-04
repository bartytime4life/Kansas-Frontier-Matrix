---
title: "Experiment Metadata — NDVI (Landsat 8) — 2026-01-02"
path: "data/work/experiments/2026-01-02__ndvi__landsat8/data/metadata/README.md"
version: "v0.1.0"
status: "draft"
last_updated: "2026-01-03"
doc_kind: "ExperimentMetadata"
project: "Kansas Frontier Matrix"
experiment_id: "2026-01-02__ndvi__landsat8"
tags:
  - ndvi
  - landsat8
  - remote-sensing
  - raster
  - vegetation-index
license: "TBD"
sensitivity: "public"
care_label: "Public"
markdown_protocol_version: "v13"
commit_sha: "TBD" # fill with git commit that generated these artifacts
doc_uuid: "urn:kfm:experiment:ndvi:landsat8:2026-01-02:metadata-readme:v0.1.0"
---

![Status](https://img.shields.io/badge/status-draft-yellow)
![Experiment](https://img.shields.io/badge/experiment-NDVI%20%E2%80%94%20Landsat%208-blue)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT%20%2B%20PROV-6f42c1)
![Reproducibility](https://img.shields.io/badge/pipeline-deterministic%20%26%20logged-brightgreen)

# 🧾 Metadata README — NDVI (Landsat 8) Experiment

This folder contains **run-level metadata** and **draft catalog/provenance artifacts** for the experiment:

📅 `2026-01-02__ndvi__landsat8`

> [!IMPORTANT]
> KFM treats all derived geospatial outputs as **first-class datasets**: they must be reproducible, fully logged, and ready to publish through **STAC/DCAT/PROV** before they are exposed downstream (graph → API → UI → story).:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🎯 Purpose

✅ This README defines:

- what “metadata” means for this experiment (what files belong here)
- what minimum fields we must record for **reproducibility** (deterministic pipeline + lineage):contentReference[oaicite:2]{index=2}
- how NDVI is computed from Landsat 8 (formula + band mapping):contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}
- how to “promote” this experiment from *work* → *published catalogs* (STAC/DCAT/PROV):contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}

---

## 🗂️ Where this folder sits

Expected experiment layout (📌 adjust if your local run differs):

```text
📁 data/work/experiments/2026-01-02__ndvi__landsat8/
└── 📁 data/
    ├── 📁 metadata/         # ✅ you are here
    ├── 📁 raw/              # raw downloads / source snapshots (never overwrite)
    ├── 📁 work/             # intermediate artifacts (tiles, masks, temp rasters)
    └── 📁 processed/        # candidate final outputs (still “pre-publish”)
```

This mirrors the KFM domain pattern: raw → work → processed, with catalogs published to canonical locations (STAC/DCAT/PROV).:contentReference[oaicite:7]{index=7}

---

## 📦 What belongs in `data/metadata/`

> [!NOTE]
> During experimentation, it’s OK to keep *draft* metadata here.  
> When results are accepted, copy/move the finalized records into the canonical repo catalogs:
> `data/stac/`, `data/catalog/dcat/`, `data/prov/`.:contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}

### ✅ Recommended files (create if missing)

| File | Kind | Why it exists |
|---|---|---|
| `run.yaml` | run log | who/when/where/how this run executed (command, commit, env) |
| `inputs.yaml` | inputs registry | upstream dataset IDs, filters (dates, AOI), cloud mask rules |
| `params.yaml` | parameter snapshot | NDVI method settings (band mapping, nodata, scaling, masks) |
| `outputs.yaml` | outputs registry | list of produced assets + checksums + stats |
| `qa_report.md` | QA narrative | quick sanity checks + anomalies found |
| `checksums.sha256` | integrity | reproducible verification for all exported files |
| `stac_item.json` / `stac_collection.json` | STAC (draft) | spatial/temporal discovery metadata:contentReference[oaicite:10]{index=10} |
| `dcat_dataset.jsonld` | DCAT (draft) | catalog discovery & distribution links:contentReference[oaicite:11]{index=11} |
| `prov.jsonld` | PROV (draft) | lineage (inputs → steps → outputs):contentReference[oaicite:12]{index=12} |

---

## 🧪 NDVI specification (this experiment)

### Formula ✅

NDVI is computed as:

\[
NDVI = \frac{NIR - Red}{NIR + Red}
\]

It is designed to range from **−1 to 1**; typical healthy vegetation tends to be high (often ~0.8–0.9) while water is near −1.:contentReference[oaicite:13]{index=13}

### Landsat 8 band mapping ✅

When NDVI is computed from **Landsat 8 OLI surface reflectance**, use:

- **NIR** = **band 5** (Landsat 8)
- **Red** = **band 4** (Landsat 8)

This mapping is explicitly used in Landsat NDVI workflows and is documented alongside the NDVI equation.:contentReference[oaicite:14]{index=14}

> [!TIP]
> If you ever mix sensors (e.g., Landsat 5/7 + Landsat 8), document *per-sensor band mapping* (because NIR/Red band numbers differ).:contentReference[oaicite:15]{index=15}

---

## ☁️ Cloud / shadow / snow masking (QA_PIXEL)

If you are using Landsat Level-2 products with `QA_PIXEL`, these bit meanings are commonly used for masking:

- Bit 0: Fill  
- Bit 1: Dilated Cloud  
- Bit 2: Cirrus (high confidence) (L8)  
- Bit 3: Cloud  
- Bit 4: Cloud Shadow  
- Bit 5: Snow  
- Bit 6: Clear  
- Bit 7: Water:contentReference[oaicite:16]{index=16}

Record in `params.yaml`:

- which bits you used
- whether you masked **water** or retained it
- whether you **require Clear=1** (recommended default)

---

## 🚫 Division-by-zero + NoData conventions

NDVI can produce invalid values where `(NIR + Red) == 0`. A robust pattern is:

- mask pixels where denominator is zero
- compute NDVI
- write a consistent **NoData** value for masked pixels:contentReference[oaicite:17]{index=17}

> [!RECOMMENDED]
> Choose a NoData value that cannot be confused with real NDVI (e.g., `-99`) and record it in `params.yaml` and output raster metadata.:contentReference[oaicite:18]{index=18}

---

## 🧬 Provenance + lineage (KFM rules)

KFM expects **deterministic, idempotent, config-driven, fully logged** transformations so the same inputs + params produce the same outputs.:contentReference[oaicite:19]{index=19}

### Minimum lineage fields to capture (put in `run.yaml` + `prov.jsonld`)

- `run_id` (unique; timestamp + short hash)
- `operator` (person or service)
- `created_at` (ISO)
- `pipeline_name` and `pipeline_version`
- `git_commit_sha`
- `environment` (python/node versions, container image, etc.)
- `inputs[]` (dataset IDs, scene IDs, filters)
- `activities[]` (masking, NDVI calc, reprojection, export)
- `outputs[]` (assets + checksums + stats)

This matches the “boundary artifacts” pattern: STAC/DCAT/PROV are required for publish readiness.:contentReference[oaicite:20]{index=20}:contentReference[oaicite:21]{index=21}

### Canonical pipeline ordering (don’t skip steps 🚦)

KFM’s ordering is non-negotiable:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes**:contentReference[oaicite:22]{index=22}

---

## 🧪 Metadata schema (starter templates)

### `run.yaml` (example)

```yaml
run_id: "2026-01-02T231500Z__ndvi__landsat8__<short-hash>"
experiment_id: "2026-01-02__ndvi__landsat8"
operator: "TBD"
created_at: "2026-01-02T23:15:00Z"

code:
  repo: "Kansas-Matrix-System"
  commit_sha: "TBD"
  pipeline: "TBD"
  command: "TBD"
  notes: "TBD"

environment:
  container_image: "TBD"
  python: "TBD"
  gee: "TBD" # if applicable

inputs:
  - source_name: "Landsat 8 SR"
    collection_id: "TBD"   # e.g., GEE collection ID or local archive reference
    date_range: ["TBD", "TBD"]
    aoi: "TBD (Kansas default?)"
    scene_ids: []          # list explicitly if possible

outputs:
  - asset: "../processed/ndvi.tif"
    sha256: "TBD"
    nodata: -99
    dtype: "float32"
    stats:
      min: "TBD"
      max: "TBD"
      mean: "TBD"
      pct_nodata: "TBD"

qa:
  cloud_mask_method: "QA_PIXEL clear bit"
  notes: "TBD"
```

### `params.yaml` (NDVI + masking)

```yaml
ndvi:
  formula: "(NIR - RED) / (NIR + RED)"
  landsat8:
    nir_band: 5
    red_band: 4

masking:
  qa_pixel_bits:
    clear: 6
    cloud: 3
    cloud_shadow: 4
    snow: 5
    water: 7
  require_clear: true
  drop_water: false

nodata:
  value: -99
  rule: "set where (nir + red) == 0"
```

Band mapping + NDVI equation are grounded in Landsat NDVI documentation and NDVI arithmetic definition.:contentReference[oaicite:23]{index=23}:contentReference[oaicite:24]{index=24}

---

## ✅ QA checklist (fast, repeatable)

> [!NOTE]
> KFM pipelines are expected to include data-quality checks and stop/flag issues if results look off.:contentReference[oaicite:25]{index=25}

Record outcomes in `qa_report.md`:

- [ ] NDVI min/max within plausible bounds (expect ~[-1, 1], ignoring NoData):contentReference[oaicite:26]{index=26}
- [ ] Percent NoData (clouds + masked + denom=0) reported
- [ ] Percent “clear pixels” reported (if QA_PIXEL masking used):contentReference[oaicite:27]{index=27}
- [ ] Quick histogram / summary stats recorded
- [ ] Visual spot-check tile(s) in known vegetation + known water areas
- [ ] Re-run produces identical checksums (deterministic output expectation):contentReference[oaicite:28]{index=28}

---

## 🛡️ Governance / sensitivity / CARE

Even when the source is public remote sensing, KFM expects explicit governance tags in front-matter (e.g., `care_label`, `sensitivity`, `classification`).:contentReference[oaicite:29]{index=29}

- **sensitivity:** `public` (default)  
- **care_label:** `Public` (update if special handling required)

> [!CAUTION]
> If you ever derive layers that could expose sensitive locations or restricted sites, update `care_label` + `sensitivity`, and ensure downstream access is governed (API enforcement).:contentReference[oaicite:30]{index=30}:contentReference[oaicite:31]{index=31}

---

## 🧱 CI / validation expectations (why this README is strict)

KFM CI expectations include:

- YAML front-matter validation
- link/reference validation
- JSON schema validation for STAC/DCAT/PROV
- security/governance scans for sensitive content:contentReference[oaicite:32]{index=32}

This is why we keep metadata explicit, structured, and repeatable.

---

## ✅ Definition of Done (for `data/metadata/`)

- [ ] Front-matter complete + valid (path/version/status/etc.):contentReference[oaicite:33]{index=33}
- [ ] All claims link to datasets / schemas / sources (where applicable):contentReference[oaicite:34]{index=34}
- [ ] Validation steps listed and repeatable (QA checklist filled):contentReference[oaicite:35]{index=35}
- [ ] Governance + FAIR/CARE explicitly stated:contentReference[oaicite:36]{index=36}
- [ ] Draft STAC/DCAT/PROV present (or tracked as TODO):contentReference[oaicite:37]{index=37}
- [ ] `checksums.sha256` created for all exported assets

---

## 📚 References (project files)

These are the *project sources* this README is aligned to:

- MARKDOWN_GUIDE_v13 (contract-first, deterministic pipeline, STAC/DCAT/PROV expectations) :contentReference[oaicite:38]{index=38}  
- KFM Comprehensive Technical Documentation (pipeline + quality checks + lineage concepts) :contentReference[oaicite:39]{index=39}  
- Cloud-Based Remote Sensing with Google Earth Engine (NDVI equation, QA_PIXEL masking patterns) :contentReference[oaicite:40]{index=40}  
- Google Earth Engine Applications (Landsat NDVI band mapping; SR + QA usage in workflows) :contentReference[oaicite:41]{index=41}  
- Geoprocessing with Python (robust NDVI compute + denom=0 handling + NoData pattern) :contentReference[oaicite:42]{index=42}  
- Scientific Method / Research / Master Coder Protocol (experiment protocol + logging discipline) :contentReference[oaicite:43]{index=43}  
- Comprehensive Markdown Guide (front-matter governance tags like `care_label`) :contentReference[oaicite:44]{index=44}  

