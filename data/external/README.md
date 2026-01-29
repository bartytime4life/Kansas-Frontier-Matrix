# 🌍 External Data (Third‑Party Sources)

![Provenance](https://img.shields.io/badge/provenance-first-brightgreen)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-governed-blue)
![STAC](https://img.shields.io/badge/STAC-catalog-orange)
![DCAT](https://img.shields.io/badge/DCAT-discovery-purple)
![PROV](https://img.shields.io/badge/W3C%20PROV-lineage-informational)

This folder is the **“intake dock”** for datasets that originate **outside** the project (archives, agencies, open-data portals, vendors, research groups, etc.) and are brought into KFM as **evidence-backed** inputs.

> ✅ Goal: make it impossible for “mystery data” to slip into the platform.  
> Everything added here must be **traceable**, **license-aware**, and **pipeline-ready**.

---

## 🧭 Contents

- [🧩 What belongs here](#-what-belongs-here)
- [🚫 What must NOT be here](#-what-must-not-be-here)
- [🗂️ Directory layout](#️-directory-layout)
- [🔁 Canonical flow](#-canonical-flow)
- [➕ Add a new external dataset](#-add-a-new-external-dataset)
- [🧾 Required “boundary artifacts”](#-required-boundary-artifacts)
- [🔐 Licensing, sensitivity, and governance](#-licensing-sensitivity-and-governance)
- [✅ Quality checks](#-quality-checks)
- [🧰 Templates](#-templates)
- [🔎 Tips for big / remote datasets](#-tips-for-big--remote-datasets)

---

## 🧩 What belongs here

Typical examples:

- 🗺️ **Historical maps** (scans, GeoTIFFs, PDFs) + any georeferencing control files
- 🧾 **Archival indexes** (CSV/JSON metadata pulled from institutions)
- 🛰️ **Remote sensing derivatives** (small subsets / derived rasters, not entire global catalogs)
- 🧭 **Reference layers** (boundaries, hydrography, transportation, place names)
- 🧪 **Evidence artifacts** generated from external sources (OCR outputs, extracted tables), *as long as provenance is captured*

---

## 🚫 What must NOT be here

- 🔑 **Secrets** (API keys, tokens, passwords)
- 🧍 **PII / sensitive personal data** unless explicitly governed and approved
- 🧨 “Random” files with unknown origin (if you can’t cite it, it doesn’t ship)
- 🧱 Direct DB dumps meant to bypass the pipeline (no “shortcut imports”)

---

## 🗂️ Directory layout

This domain is expected to follow the standard “stage” structure (raw → work → processed).  
If your repo uses a different layout elsewhere, keep the **spirit** identical: isolate external sources, keep raw read-only, and emit governed outputs.

```text
📁 data/
└─📁 external/
  ├─📄 README.md                         👈 you are here
  ├─📁 raw/                              🧾 immutable snapshots (read-only)
  │  └─📁 <dataset_slug>/
  │     ├─📄 SOURCE.yaml                 (where it came from + license + retrieval date)
  │     ├─📄 CHECKSUMS.sha256            (hashes for integrity)
  │     └─📦 <original_download>.*       (zip/csv/tif/pdf/etc)
  ├─📁 work/                             🧪 intermediates (throwaway / reproducible)
  │  └─📁 <dataset_slug>/
  ├─📁 processed/                        ✅ curated outputs (served downstream)
  │  └─📁 <dataset_slug>/
  │     ├─🗺️ <layer>.geojson|parquet|tif
  │     └─📄 README.md                   (dataset-specific notes + known issues)
  └─📁 mappings/                         🧭 optional helper docs for metadata linkage
     └─📁 <dataset_slug>/
        ├─📄 stac.plan.md
        ├─📄 dcat.plan.md
        └─📄 prov.plan.md
```

---

## 🔁 Canonical flow

**No skipping steps.** External data must move through the same governed sequence as everything else:

```text
RAW → WORK → PROCESSED → (STAC/DCAT/PROV) → DATABASE → API → UI
```

> If a feature proposal “injects” data directly into the UI, DB, or graph *without* catalogs/provenance, it’s not considered a valid approach in this project.

---

## ➕ Add a new external dataset

### 1) Create a dataset slug 🏷️
Use a stable, readable ID:

- ✅ `usgs_wbd_huc8_ks_2024`
- ✅ `kshs_railroads_index_1890s`
- ❌ `newdata-final-v2-FORREAL`

### 2) Drop the immutable raw snapshot 🧾
Put original inputs into:

- `data/external/raw/<dataset_slug>/`

Rules:
- Raw is **write-once** (treat as evidence).
- Prefer storing the *original container* (zip/tar) + a `CHECKSUMS.sha256`.

### 3) Document origin + license 📜
Add `SOURCE.yaml` (template below).  
If the license is unclear, **stop** and route to governance review.

### 4) Build a deterministic pipeline 🧰
Pipelines must:
- read from `data/external/raw/<dataset_slug>/`
- write intermediates to `data/external/work/<dataset_slug>/`
- write final outputs to `data/external/processed/<dataset_slug>/`
- run end-to-end without prompts (no “click to continue”)

> 📌 Put pipeline code where the repo standard expects it (commonly `src/pipelines/…` or `pipelines/…`). The key is *repeatability*.

### 5) Emit the required metadata artifacts 🧾
Every dataset must have:
- STAC Collection + Item(s)
- DCAT Dataset entry
- PROV activity bundle

These usually live in canonical catalog locations like:
- `data/stac/…`
- `data/catalog/dcat/…`
- `data/prov/…` (or `data/provenance/…` depending on repo layout)

### 6) Validate + open PR ✅
Before a PR is considered “ready”:
- metadata schema validation must pass
- secret scanning must be clean
- any sensitivity/classification constraints must be satisfied

---

## 🧾 Required boundary artifacts

These are the “interfaces” from external data into the rest of the system:

### 🗺️ STAC
- Points to the processed asset files (or stable object storage)
- Captures spatial/temporal footprint where applicable
- Includes source + license references

### 🧾 DCAT
- Makes the dataset discoverable in the project’s catalog
- Includes title/description/keywords/license/distributions

### 🧬 PROV
- Captures lineage end-to-end: **raw inputs → work intermediates → processed outputs**
- Records **who/what** ran the pipeline and **when**
- Prefer recording pipeline commit hash / run id for auditability

---

## 🔐 Licensing, sensitivity, and governance

External data is not “free by default.” Treat license and sensitivity as **first-class fields**.

### License rules 📜
- Include the license identifier (or full text if needed).
- Record any constraints: attribution, non-commercial, share-alike, embargo, etc.
- If “Terms of Use” are webpage-only, capture the URL + retrieval date in `SOURCE.yaml`.

### Sensitivity rules 🧭
- If the dataset includes sensitive locations or culturally sensitive content:
  - do not publish precise coordinates publicly
  - document any redaction/generalization performed
  - ensure the API/UI layers enforce access controls (never rely on “the UI hides it”)

### Governance triggers ⚖️
Expect manual review when:
- adding a **new external provider/source**
- introducing **restricted / sensitive** layers
- changing dataset classification or access scope

---

## ✅ Quality checks

Recommended minimum checks (prefer automated):

- ✅ record counts / null-rate summaries
- ✅ geometry validity (for vector)
- ✅ CRS normalization (document CRS transforms)
- ✅ plausible range checks (years, coordinates, units)
- ✅ duplicate detection (hash-based)

> Tip: store a tiny QA report (Markdown or JSON) in `processed/<dataset_slug>/README.md` so reviewers can verify quickly.

---

## 🧰 Templates

### `SOURCE.yaml` (required)

```yaml
dataset_id: "<dataset_slug>"
title: "<human readable title>"
provider: "<organization / archive / portal>"
source_url: "<canonical landing page or download endpoint>"
retrieved_at: "YYYY-MM-DD"
license:
  name: "<e.g., Public Domain | CC-BY-4.0 | custom>"
  url: "<license/terms page>"
attribution:
  required: true
  text: "<preferred attribution statement>"
sensitivity:
  classification: "public | restricted | confidential"
  notes: "<why / what to watch for>"
contents:
  - path: "raw/<file_or_bundle_name>"
    description: "<what it is>"
    sha256: "<fill from CHECKSUMS.sha256>"
processing:
  expected_outputs:
    - "processed/<dataset_slug>/<output_file>"
  pipeline_ref: "<path/to/pipeline or module name>"
```

### `CHECKSUMS.sha256` (recommended)

```text
<sha256_hash>  <filename>
<sha256_hash>  <filename>
```

### Dataset README (recommended)

Create: `data/external/processed/<dataset_slug>/README.md`

Include:
- source summary + license
- processing summary
- known limitations / uncertainty
- links to STAC/DCAT/PROV artifact IDs

---

## 🔎 Tips for big / remote datasets

When the upstream dataset is huge (e.g., national rasters, satellite archives):

- ✅ Prefer **derived products** (clipped to Kansas AOI, summarized, or tiled)
- ✅ Store a **manifest + checksums** rather than committing multi‑GB blobs
- ✅ Ensure STAC assets point to **stable storage** (release bundle, object store, or controlled mirror)
- ✅ Keep raw “evidence” verifiable: capture retrieval date + exact query parameters + hashes

---

### ✅ PR checklist (copy/paste)

- [ ] Raw files added under `data/external/raw/<dataset_slug>/` (or manifest if too large)
- [ ] `SOURCE.yaml` present + license documented
- [ ] Checksums recorded (`CHECKSUMS.sha256`)
- [ ] Pipeline added/updated and is deterministic
- [ ] Outputs written to `data/external/processed/<dataset_slug>/`
- [ ] STAC Collection + Item(s) created/updated
- [ ] DCAT Dataset entry created/updated
- [ ] PROV bundle created/updated (raw→work→processed chain)
- [ ] Any sensitivity/redaction documented (if applicable)

---

