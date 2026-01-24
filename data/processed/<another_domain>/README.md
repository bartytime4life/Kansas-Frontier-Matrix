# 📦 Processed Data — `<another_domain>` (KFM)

![Lifecycle](https://img.shields.io/badge/lifecycle-processed-blue)
![Evidence Stack](https://img.shields.io/badge/evidence-STAC%20%7C%20DCAT%20%7C%20PROV-success)
![Governance](https://img.shields.io/badge/policy-fail--closed-critical)
![Reproducible](https://img.shields.io/badge/pipelines-deterministic%20%26%20reproducible-informational)
![Ready for UI](https://img.shields.io/badge/serving-API%20%2B%20UI%20%2B%20Focus%20Mode-brightgreen)

> [!IMPORTANT]
> **Nothing in `data/processed/` is “hand-edited”.** Every byte in this folder must be **reproducible** from `data/raw/…` inputs + pipeline code/config, and must be **discoverable + auditable** via the KFM evidence stack.

---

## 🎯 Purpose

This directory stores **final, publishable artifacts** for the **`<another_domain>`** domain:
- ✅ cleaned / normalized / validated outputs  
- ✅ ready to be served by **API**, visualized in **UI**, and cited by **Focus Mode**  
- ✅ referenced by **STAC/DCAT** catalogs and **PROV** lineage  
- ✅ safe to distribute (respecting **FAIR + CARE**, sensitivity labels, and policy gates)

> Replace `<another_domain>` with your domain slug (recommended: `kebab-case`).

---

## ✅ What belongs here

**Put these here:**
- 🧱 **Authoritative processed datasets** (the ones we’re willing to stand behind)
- 🗺️ **UI-ready geospatial artifacts**  
  - vectors (e.g., GeoParquet, GeoJSON for small sets)  
  - rasters (e.g., COGs)  
  - tiles / caches (e.g., PMTiles or precomputed tiles)  
- 📌 **Sidecar integrity + audit files** next to the artifacts (checksums, run manifests)
- 🧾 **Stable, versioned releases** (date- or semver-based)

---

## 🚫 What does *not* belong here

**Never put these here:**
- 🧪 experimental outputs (keep in `data/work/…` until promoted)
- 🧱 raw downloads “as-received” (those live in `data/raw/…`)
- ✍️ manual “fix-ups” (fix the pipeline/config instead)
- 🧨 orphan files not referenced by catalogs/provenance
- 🔑 secrets / tokens / credentials (policy should block these anyway)

---

## 🔗 The KFM Evidence Stack Contract (non‑negotiable)

For **every dataset version** promoted into `data/processed/<another_domain>/…`, you must ensure the **catalog triplet** exists and stays consistent:

1) 🗺️ **STAC** (spatiotemporal + asset metadata)  
2) 🧾 **DCAT** (publication, license, distribution, governance fields)  
3) 🧬 **PROV** (lineage: inputs → activity/run → outputs)

**Optional but strongly recommended sidecars (per version):**
- 🔐 `checksums.sha256` (or multihash file)
- 🧾 `run_manifest.json` (run_id, tool versions, inputs/outputs summary)
- 📚 `data_dictionary.md` (field meaning, units, caveats)
- 🧪 `validation_report.json` (schema/geometry/range checks)

> [!TIP]
> If a dataset can’t be traced, it can’t be trusted. If it can’t be trusted, it can’t be served.

---

## 🗂️ Recommended Folder Structure

> This is the **recommended** structure inside `data/processed/<another_domain>/`.  
> Keep it boring and consistent. Future you will thank you. ✅

```text
📁 data/processed/<another_domain>/
├─ 📄 README.md                       # 👈 you are here
├─ 📁 _schemas/                       # shared schema contracts (optional)
│  └─ 📄 <dataset_id>.schema.json
├─ 📁 _docs/                          # domain-specific notes (optional)
│  └─ 📄 glossary.md
├─ 📁 <dataset_id>/                   # one folder per canonical dataset
│  ├─ 📁 v<version>/                  # one folder per release
│  │  ├─ 🧱 <dataset_id>__v<version>.geoparquet
│  │  ├─ 🗺️ <dataset_id>__v<version>.pmtiles
│  │  ├─ 🛰️ <dataset_id>__v<version>.cog.tif
│  │  ├─ 🔐 checksums.sha256
│  │  ├─ 🧾 run_manifest.json
│  │  ├─ ✅ validation_report.json
│  │  └─ 📚 data_dictionary.md
│  └─ 📄 LATEST                        # (optional) pointer file or note
└─ 📁 _inventory/
   └─ 📄 inventory.csv                 # (optional) domain inventory export
```

---

## 🆔 Dataset IDs, Versions, and Naming

### Canonical dataset ID (`dataset_id`)
Use a **stable canonical ID** everywhere (catalogs + provenance + filenames).

**Suggested pattern (adapt to your repo conventions):**
- `kfm.ks.<another_domain>.<dataset_slug>`

Examples:
- `kfm.ks.hydrology.usgs_nwis_gauges`
- `kfm.ks.agriculture.usda_cropland_data_layer`

### Versioning
Pick one version strategy and stick to it per dataset:
- 📅 date-based: `v2026-01-24`
- 🧪 semver: `v1.3.0`
- 🧊 content-hash builds (advanced): keep a human-friendly tag + recorded digest

### Filename convention
Use **dataset_id + version** in filenames to keep artifacts self-describing:
- `<dataset_id>__v<version>.<ext>`

---

## 🔁 Promotion Workflow: Detect → Validate → Promote (GitOps)

```mermaid
flowchart LR
  A[📥 data/raw/<another_domain>/<dataset_id>/] --> B[🧪 Ingestion Gate<br/>checksum + sanity]
  B --> C[🧰 data/work/<another_domain>/<dataset_id>/]
  C --> D[⚙️ Deterministic ETL Pipeline<br/>(config-driven)]
  D --> E[📦 data/processed/<another_domain>/<dataset_id>/vX/]
  E --> F[🗺️ STAC + 🧾 DCAT + 🧬 PROV updates]
  F --> G[🔗 Graph import / index refresh]
  G --> H[🌍 API + UI + 🤖 Focus Mode consume]
```

### Automation (optional but encouraged) 🤖🤝⚙️
- 🕵️ **Watcher** detects upstream changes (new source version, new feed, etc.)
- 🧠 **Planner** generates a deterministic plan (what to ingest + which pipeline/config)
- 🧰 **Executor** runs the pipeline + opens a PR (never auto-merges)

---

## ✅ Validation & Policy Gates (Fail Closed)

Before anything in this folder is considered **live**, the following must pass:

- 🧱 **Schema validation** (fields, types, required columns)
- 🗺️ **Spatial validation** (CRS expectations, geometry validity, extents)
- 🧾 **License presence** (no unknown license)
- 🏷️ **Sensitivity / classification correctness**  
  - classification must propagate correctly through transforms
- 🧬 **Provenance completeness** (inputs + processing steps declared)
- 🔍 **Catalog completeness** (STAC/DCAT/PROV are present + consistent)

> [!NOTE]
> Policy gates should block merges when rules fail. Don’t “fix it later” — later becomes never.

---

## 🔐 Sensitivity, CARE, and Privacy (Don’t Ship Harm)

If your domain touches **sensitive locations, vulnerable communities, PII, or culturally sensitive info**:

- 🏷️ label the dataset correctly (classification + care/ethics signals)
- 🧊 prefer **aggregation/generalization** over raw precision in public outputs
- 🌫️ apply **blurring / zoom-based generalization** where appropriate (UI-safe artifacts)
- 🧪 consider privacy-preserving techniques for releases (e.g., record-level privacy / noise for aggregates)

> [!IMPORTANT]
> If the dataset requires community/tribal approval or special handling, do **not** promote without the required review & governance record.

---

## 🚀 Publishing & Distribution Options

### Option A — Repo/Object Storage (standard)
- Store large artifacts in `data/processed/…` or in object storage (S3/CDN).
- Ensure **every file is referenced** in metadata (no hidden/orphan blobs).
- Keep **checksums** next to the artifact and/or in catalogs.

### Option B — OCI Artifact Distribution (advanced) 📦🔏
Package datasets like “data containers”:
- push artifacts (PMTiles / GeoParquet / COG) with **ORAS**
- sign with **Cosign**
- attach **PROV** + run manifest + SBOM/SLSA attestations as referrers

<details>
<summary>🧠 Why OCI distribution is useful</summary>

- 🔁 makes rollback easy (tags + digests)
- 🧾 encourages immutable, content-addressed releases
- 🔏 improves supply-chain security (signatures + attestations)
- 🌍 enables federation (other regions can mirror/pull artifacts)

</details>

---

## 🧪 Simulations & Models (Special Case)

Simulation/model outputs should follow a **sandbox → promotion** pattern:

- 🧰 first run in `data/work/sims/…` (or domain workbench)
- ✅ promote only after review + evidence stack artifacts are generated
- 🚫 never point production UI/graph to `data/work/…` outputs directly

---

## 🧭 UI + API Consumption Notes (what to optimize for)

KFM’s consumers generally expect:
- 🗺️ tile-friendly formats (fast pan/zoom)
- ⏳ time-awareness (timeline slider / temporal filtering)
- 🧾 “Layer Info” provenance (source, license, processing summary)
- 🤖 Focus Mode citations: answers must point to datasets/assets that back claims

If you’re unsure, prioritize:
- **GeoParquet** for analytics + joins
- **PMTiles** (or vector tiles) for interactive maps
- **COGs** for rasters + fast tiling

---

## 🧑‍💻 Add a New Dataset (Checklist)

> Print this checklist into your soul 😄✅

### 1) Define the dataset
- [ ] Choose `dataset_id` (stable canonical ID)
- [ ] Choose versioning scheme
- [ ] Decide output formats (vector/raster/tiles)

### 2) Ingest raw evidence
- [ ] Add raw files to `data/raw/…` (as-received)
- [ ] Generate `checksums.sha256`
- [ ] Record source + license + access constraints

### 3) Run deterministic pipeline
- [ ] Pipeline config committed
- [ ] Run produces artifacts into `data/processed/<another_domain>/<dataset_id>/v<version>/…`
- [ ] Generate `run_manifest.json` + `validation_report.json`

### 4) Generate evidence stack artifacts
- [ ] STAC item/collection updated/created
- [ ] DCAT dataset/distributions updated/created
- [ ] PROV lineage generated/updated

### 5) Governance & safety
- [ ] classification propagated correctly (no “accidental public”)
- [ ] sensitive attributes handled (generalize/blur/aggregate if needed)

### 6) Open PR + pass CI gates
- [ ] PR contains processed artifacts + catalogs + provenance
- [ ] CI passes (policy + validation)
- [ ] Human review completed

---

## 📋 Domain Inventory (Template)

> Keep this table updated (or auto-generate it from catalogs).

| Dataset ID | Title | Version | Formats | Temporal | License | Classification | Notes |
|---|---|---:|---|---|---|---|---|
| `kfm.ks.<another_domain>.example` | Example dataset | `v1.0.0` | GeoParquet, PMTiles | 1850–2025 | CC-BY-4.0 | public | demo row |

---

## 🆘 Troubleshooting (Common “Why did CI fail?”)

- ❌ **Missing license** → add SPDX-like license value in DCAT and/or contract metadata  
- ❌ **STAC/DCAT/PROV mismatch** → dataset_id/version must line up across all three  
- ❌ **Checksum mismatch** → regenerate checksums after pipeline writes outputs  
- ❌ **Classification violation** → outputs cannot be less restrictive than any input  
- ❌ **Orphan artifacts** → every file must be referenced by metadata/catalogs  

---

## 📚 Related Docs (in-repo pointers)

- 🧭 `docs/architecture/…` — system blueprint & evidence stack rules  
- 📥 `docs/guides/pipelines/…` — ingestion & pipeline conventions  
- 🔐 `api/scripts/policy/README.md` — policy pack / governance checks  
- 🗂️ `data/catalog/…` — published STAC/DCAT  
- 🧬 `data/provenance/…` — PROV records

---

## 🧾 Changelog (optional)

- **YYYY-MM-DD** — created `<another_domain>` processed domain README ✅

