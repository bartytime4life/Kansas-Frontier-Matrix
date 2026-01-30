# 🧪 `data/work/` — Working Space (WIP ➜ Canonical)  

![Status](https://img.shields.io/badge/status-WIP%20friendly-blue)
![Data](https://img.shields.io/badge/data-deterministic%20pipelines-5865F2)
![Provenance](https://img.shields.io/badge/provenance-required-brightgreen)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%2B%20PROV-orange)

> [!IMPORTANT]
> **`data/work/` is a scratch + staging area** for datasets, experiments, and intermediate artifacts that are **not yet ready** to become canonical KFM inputs/outputs.  
> Canonical data still flows **Raw → Processed → Catalog/Prov → Database → API → UI**. [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 Why this folder exists

KFM is designed so **raw inputs remain immutable evidence** and **processed outputs remain ready-to-serve, versioned deliverables**—with metadata + provenance as hard requirements. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

`data/work/` exists to keep in-progress work *useful* without polluting canonical folders:

- 🧩 **Staging** for downloads, decompressions, and exploratory slices before committing anything into `data/raw/`.
- 🧪 **Experimentation** (QA checks, small prototypes, trial transformations) before “locking” an approach into a pipeline.
- 🧾 **Repro notes & run logs** that help others repeat your process (and help *future-you*).
- 🧹 **Clean separation**: “Work-in-progress” stays here until it earns promotion into the canonical pipeline.

---

## ✅ What belongs here vs. what doesn’t

### ✅ Good fits for `data/work/`
- 📦 Unzipped source bundles you’re still inspecting (e.g., “what’s in this ZIP?”)
- 🧪 Notebook outputs / quick plots / QA summaries
- 🧱 Intermediate conversion products (e.g., reprojected shapefiles, clipped rasters) **not final**
- 🧰 One-off scripts used during research (before being formalized into `pipelines/`)
- 🧾 Draft metadata + provenance files while iterating

### 🚫 Not allowed / strongly discouraged
- 🔐 Secrets / tokens / private keys (never store these anywhere in-repo)
- 🧨 Anything you can’t legally redistribute
- 🧱 “Final” data that the API/UI should rely on  
  → that belongs in `data/processed/` **only after** it’s standardized and documented. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- ✍️ Manual-only workflows that cannot be rerun  
  → official pipelines must be **deterministic, reproducible, and non-interactive**. [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🗂️ Recommended structure

You can organize however you like, but this pattern keeps things predictable:

```text
data/
└── work/ 🧪
    ├── incoming/ 📥            # temp downloads / raw bundles before promotion into data/raw/
    ├── scratch/ 🧻             # throwaway transforms, quick checks, spikes
    ├── notebooks/ 📓           # exploratory notebooks (ensure they can be rerun!)
    ├── runs/ 🧾                # dated run logs + reproducibility details
    ├── qa/ ✅                   # validation reports, schema checks, spot-check notes
    ├── exports/ 📤             # shareable snapshots (small) used in PR discussion
    └── _templates/ 🧰          # starter templates for work items (README, metadata drafts)
```

> [!TIP]
> If something in `data/work/` becomes important for others to reproduce, promote it into:
> - `pipelines/` (the *how*)  
> - `data/raw/` (the *evidence*)  
> - `data/processed/` (the *deliverable*)  
> - `data/catalog/` + `data/provenance/` (the *why + lineage*) [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧬 “Promotion” path: from WIP to Canonical

When your work is ready to become part of KFM, the promotion steps should follow the project’s canonical order. [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 1) 📥 Stage evidence into `data/raw/` (immutable)
Raw data should be a **write-once snapshot**, treated as evidence and never modified by pipelines. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 2) 🧪 Convert/clean via a deterministic pipeline
Pipelines should:
- produce identical results given identical inputs/config
- avoid interactive prompts/manual steps
- control randomness (fixed seeds) [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3) 📦 Write deliverables into `data/processed/`
Processed outputs are the **ready-to-use** forms (GeoJSON/Parquet/GeoTIFF/etc.) served by the system. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 4) 🧾 Add metadata + provenance (hard requirement)
For every dataset, create/update:
- **Catalog metadata** (e.g., STAC Item/Collection, DCAT record)  
- **Provenance record** (e.g., W3C PROV or project provenance log) describing inputs, script version, run date, and outputs [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> [!WARNING]
> KFM treats metadata/provenance as non-optional: *no data enters without documentation.* [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 5) 🔁 PR + CI validation
When you open a PR, CI may verify processed outputs have corresponding catalog/provenance and basic validations pass. [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧾 Minimum “work item” template (copy/paste)

Create a subfolder per effort:

```text
data/work/
└── <topic-or-dataset-slug>/ 🧪
    ├── README.md
    ├── sources.md
    ├── notes.md
    ├── runbook.md
    ├── inputs/             # local copies BEFORE promotion to data/raw/
    ├── intermediates/      # temporary transforms (not canonical)
    └── outputs/            # preview outputs for review (small!)
```

### `README.md` (inside your work item) should include:
- 🎯 **Goal** (what you’re trying to add/learn)
- 🔗 **Sources & licensing notes**
- 🧰 **Tools used** (versions, environment notes)
- 🔁 **Exact repro steps**
- ✅ **QA checklist + results**
- 📌 **Promotion decision**: what will move to `data/raw/`, `data/processed/`, and what will be discarded

> [!NOTE]
> Treat this like an “experiment capsule”: document versions and what changed.  
> A changelog + snapshots/checkpoints are recommended for traceability. [oai_citation:16‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🏷️ Naming + organization conventions

### ✅ Folder naming
Use `kebab-case` or `snake_case` consistently:
- `census-1900-import/`
- `usgs-waterways-v1/`
- `landsat-drought-spike/`

### 🗓️ Run folders
Use ISO dates so sorting is automatic:

```text
data/work/runs/
└── 2026-01-30__census-1900__trial-02/
```

### 🧾 Logs
If you’re producing logs, include:
- input file list (with checksums if possible)
- script name + commit hash (if available)
- runtime parameters
- output file list and summary stats

This aligns with the provenance expectation that runs record *what produced what, when, and from which sources.* [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧷 Metadata discipline (even in WIP)

Even before promotion, start capturing metadata early. Strong metadata improves interoperability and reduces “mystery datasets.” [oai_citation:18‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

A good working metadata stub includes:
- 📛 identification (what is it)
- ✅ quality (known issues, accuracy, validation)
- 🧭 spatial reference (CRS/projection)
- 🧱 schema (entities/attributes)
- 📦 distribution + license
- 🕒 temporal coverage (collected/updated)
- 📣 citation guidance + contacts [oai_citation:19‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

> [!TIP]
> KFM’s architecture leans heavily on **centralized metadata** as a way to connect and govern datasets at scale (a “data hub” concept). [oai_citation:20‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

---

## 🧹 Cleanup rules

- 🗑️ Assume `data/work/` is disposable unless explicitly promoted.
- 🧯 Keep large blobs out of Git history whenever possible (prefer references + reproducible download scripts).
- 🧽 Delete stale WIP folders that aren’t being actively worked—especially if they duplicate what’s already in `data/raw/`.

---

## 📚 References used for this folder’s conventions

- Kansas Frontier Matrix — pipeline order, raw/processed roles, and metadata/provenance requirements. [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Map data best practices — why metadata matters and what it should contain. [oai_citation:24‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)
- Research traceability — changelogs, snapshots/checkpoints, and reproducible experiment capsules. [oai_citation:25‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Data Spaces — metadata-as-the-hub pattern for integrating many distributed data assets. [oai_citation:26‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)