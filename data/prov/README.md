# 🔗 `data/prov/` — Provenance & Lineage (Evidence-First) ⛓️🧭

![Provenance First](https://img.shields.io/badge/provenance-first-1f6feb?style=flat-square)
![W3C PROV](https://img.shields.io/badge/W3C-PROV--O-0b7285?style=flat-square)
![STAC + DCAT](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT-6f42c1?style=flat-square)
![Append-Only](https://img.shields.io/badge/logs-append--only-orange?style=flat-square)

KFM is **evidence-first**: every dataset, map layer, and AI output must be traceable back to its sources — the **“map behind the map”** 🗺️✨  
This folder stores **W3C PROV-style lineage bundles** (and related run manifests) that explain **how** something was produced, **from what**, **by whom/what**, **when**, and **with which configuration**.

---

## 🧭 Quick Navigation

- [Why this exists](#-why-this-exists)
- [What belongs in `data/prov/`](#-what-belongs-in-dataprov)
- [Recommended layout](#-recommended-layout)
- [Naming conventions](#-naming-conventions)
- [PROV concepts used (KFM minimum)](#-prov-concepts-used-kfm-minimum)
- [Cross-links to STAC & DCAT](#-cross-links-to-stac--dcat)
- [How to add a provenance record](#-how-to-add-a-provenance-record)
- [AI Answer Provenance](#-ai-answer-provenance)
- [Governance & security notes](#-governance--security-notes)
- [Anti-patterns](#-anti-patterns)

---

## 🎯 Why this exists

Provenance is how we enforce these invariants ✅:

- **Nothing is publishable without provenance** (missing lineage = 🚫 not shippable).
- Data flows through a canonical “truth path”:
  - **Raw ➜ Work ➜ Processed ➜ Catalog ➜ Datastores ➜ API ➜ UI/AI**
- **AI is “No Source, No Answer”**: outputs must be backed by citations and logged for audit.

If you can’t answer **“Where did this come from?”** using this folder, then the artifact isn’t ready.

---

## 📦 What belongs in `data/prov/`

This directory holds provenance artifacts for:

### 1) 📚 Published datasets (primary)
A **PROV bundle per dataset version/run**, capturing:
- input source entities (raw files / source URLs)
- processing activities (ETL steps, scripts, containers)
- agents (software + human operators where applicable)
- output entities (final processed files / database loads)
- hashes/checksums and immutable identifiers
- links to catalog entries (STAC/DCAT)

### 2) 🏗️ Pipeline runs (manifests)
Append-only run manifests that capture operational details:
- run ID, timestamps, environment
- config files used
- input/output checksums
- pipeline version / git commit

### 3) 🤖 AI provenance (auditable answers)
For each answer (or batch), record:
- question + scope (bbox/time/entities)
- retrieved sources (doc IDs, dataset IDs, graph node IDs)
- model name/version + runtime config
- policy decision result (allowed/blocked)
- output checksum / immutable ID

---

## 🗂️ Recommended layout

> Keep it **boringly consistent**. Predictability is a feature. 😄

```text
data/
└── prov/
    ├── README.md
    ├── 📁 datasets/                  # dataset-level provenance bundles
    │   └── <domain>/
    │       └── <dataset_id>/
    │           ├── <dataset_id>__<run_id>.prov.jsonld
    │           ├── <dataset_id>__<run_id>.manifest.json
    │           └── checksums__<run_id>.json
    ├── 📁 ai/                        # AI answer provenance + audit
    │   └── <yyyy-mm>/
    │       ├── answer__<answer_id>.prov.jsonld
    │       └── session__<session_id>.json
    ├── 📁 templates/                 # starter templates for new bundles
    │   ├── TEMPLATE__DATASET_PROV.jsonld
    │   └── TEMPLATE__AI_ANSWER_PROV.jsonld
    └── 📁 index/                     # optional indices for quick lookup
        ├── datasets.index.json
        └── ai.index.json
```

> ⚠️ Note: older docs may refer to `data/provenance/`. In v13-style structure, **canonical path is `data/prov/`**. If you keep a legacy path, prefer a **symlink** or a **mirror index** to avoid confusion.

---

## 🏷️ Naming conventions

### Run ID
Use a stable run identifier:
- `YYYYMMDDThhmmssZ__<pipeline>__<shortsha>`
- Example: `20260131T034455Z__import_hydro__a1b2c3d`

### Dataset PROV bundle filename
- `<dataset_id>__<run_id>.prov.jsonld`

### Manifest filename
- `<dataset_id>__<run_id>.manifest.json`

### Checksums filename
- `checksums__<run_id>.json` (or inline in the manifest)

---

## 🧠 PROV concepts used (KFM minimum)

We follow **W3C PROV** ideas with a KFM-minimal vocabulary:

- **Entity**: a thing (file, table, API resource, STAC Item, DCAT Dataset, model output)
- **Activity**: a process (ETL step, normalization, join, raster reprojection, model run)
- **Agent**: who/what acted (pipeline container, script version, operator, CI runner)

### Minimum required fields (dataset bundles)
- Entities:
  - inputs (raw + intermediate)
  - outputs (processed + published)
- Activities:
  - each major step (or one “bundle activity” if needed)
- Agents:
  - software agent (name, version, image tag, commit)
  - optional human agent (role, identifier)
- Integrity:
  - `sha256` for key entities
- Linkage:
  - STAC Item/Collection IDs and DCAT Dataset ID (or paths)
- Governance:
  - license + sensitivity/classification tags

---

## 🔄 Cross-links to STAC & DCAT

In KFM, provenance is a **boundary artifact** with metadata alignment:

- **STAC** describes the *geospatial assets* (items/collections).
- **DCAT** describes the *catalog discovery view* (title/license/keywords/distributions).
- **PROV** describes the *how it was produced* chain (inputs → steps → outputs).

**Expectation:** a published dataset has all 3:
- `data/stac/...` ✅
- `data/catalog/dcat/...` ✅
- `data/prov/...` ✅

---

## 🛠️ How to add a provenance record

### ✅ Checklist (Definition of Done)
When publishing a dataset version:

1. **Create a `run_id`**
2. **Record inputs**
   - source URL (or origin system)
   - local raw path
   - checksum (sha256)
   - license + attribution
3. **Record processing**
   - pipeline name + entrypoint
   - container image tag (if any)
   - git commit SHA / version
   - parameters + config paths
4. **Record outputs**
   - processed file path(s) + checksum(s)
   - optional DB load target (table/view ID)
5. **Link catalogs**
   - STAC collection/item IDs
   - DCAT dataset ID
6. **Write bundle**
   - to: `data/prov/datasets/<domain>/<dataset_id>/<dataset_id>__<run_id>.prov.jsonld`
7. **Write manifest**
   - same folder: `<dataset_id>__<run_id>.manifest.json`
8. **Never mutate old records**
   - provenance is **append-only**: new run = new files ✅

---

## 🧾 Example (minimal) dataset PROV bundle (JSON-LD)

> This is intentionally compact — expand as needed, but don’t omit the minimums.

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "kfm": "https://kansasfrontiermatrix.org/ns#"
  },
  "@id": "kfm:prov/datasets/ks_hydrology_1880/20260131T034455Z__import_hydro__a1b2c3d",
  "@type": "prov:Bundle",

  "prov:wasAssociatedWith": [
    {
      "@id": "kfm:agent/software/import_hydro",
      "@type": "prov:SoftwareAgent",
      "kfm:gitCommit": "a1b2c3d",
      "kfm:containerImage": "ghcr.io/kfm/pipelines/import_hydro:2026.01.31"
    }
  ],

  "prov:activity": [
    {
      "@id": "kfm:activity/import_hydro__20260131T034455Z",
      "@type": "prov:Activity",
      "prov:startedAtTime": "2026-01-31T03:44:55Z",
      "prov:endedAtTime": "2026-01-31T03:49:12Z",
      "kfm:paramsRef": "data/work/hydrology/import_hydro/config.yaml"
    }
  ],

  "prov:entity": [
    {
      "@id": "kfm:entity/raw/usgs_source_csv",
      "@type": "prov:Entity",
      "kfm:path": "data/raw/hydrology/usgs_hydro_1880.csv",
      "kfm:sha256": "<sha256-here>",
      "kfm:license": "public-domain-or-source-license",
      "kfm:sourceUrl": "<source-url-here>"
    },
    {
      "@id": "kfm:entity/processed/ks_hydrology_1880",
      "@type": "prov:Entity",
      "kfm:path": "data/processed/hydrology/ks_hydrology_1880.parquet",
      "kfm:sha256": "<sha256-here>",
      "kfm:stacItemId": "stac:item:ks_hydrology_1880__20260131",
      "kfm:dcatDatasetId": "dcat:dataset:ks_hydrology_1880"
    }
  ],

  "prov:used": [
    {
      "prov:activity": { "@id": "kfm:activity/import_hydro__20260131T034455Z" },
      "prov:entity": { "@id": "kfm:entity/raw/usgs_source_csv" }
    }
  ],

  "prov:wasGeneratedBy": [
    {
      "prov:entity": { "@id": "kfm:entity/processed/ks_hydrology_1880" },
      "prov:activity": { "@id": "kfm:activity/import_hydro__20260131T034455Z" }
    }
  ]
}
```

---

## 🤖 AI answer provenance

AI output is treated as a first-class “evidence artifact”:
- it should be **citable**
- it should be **auditable**
- it should be **replayable** (same inputs + same model config = explainable differences)

### What we log (minimum)
- `question`
- `retrieved_sources[]` (doc IDs, dataset IDs, graph node IDs)
- `model` (name/tag), `runtime` (context window, temperature, etc.)
- `policy_gate` outcome (allowed/blocked + reason)
- `answer_hash` (sha256), `created_at`

> If an answer later becomes disputed, provenance lets us retrieve the exact context + model version used.

---

## 🔐 Governance & security notes

- **Fail-closed**: missing provenance/metadata blocks publication.
- **Append-only**: treat provenance logs like an immutable ledger.
- **Sensitivity-aware**: provenance may reference restricted inputs; do not leak restricted values into public metadata.
- **Signing (optional but recommended)**: future-friendly path is signing manifests and/or hashing indexes.

---

## 🚫 Anti-patterns

Avoid these (they break trust fast):

- ❌ “We processed it somehow” (no activity details)
- ❌ missing checksums (can’t verify integrity)
- ❌ no source URL / attribution (license risk)
- ❌ editing old PROV files (breaks audit trail)
- ❌ publishing a dataset with STAC/DCAT but no PROV (incomplete boundary artifacts)

---

## ✅ Bottom line

If it’s visible in the UI or referenced by the AI, it must be explainable here — **prov or it didn’t happen** 😄⛓️