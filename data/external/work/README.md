<div align="center">

# 📁 `data/external/work/`  
**External “workbench” for evaluating + transforming outside data _before_ it enters the canonical KFM pipeline** 🧪🧰

![Stage](https://img.shields.io/badge/Data%20Stage-external%2Fwork-blue)
![Pipeline](https://img.shields.io/badge/Pipeline-provenance--first-brightgreen)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-purple)
![Scope](https://img.shields.io/badge/Scope-non--authoritative-lightgrey)

</div>

> ⚠️ **Non-authoritative workspace:** Nothing inside `data/external/work/` is considered “published,” “trusted,” or safe to power the graph/API/UI/stories. KFM’s ordering rules require ETL → catalogs (STAC/DCAT/PROV) → graph → API → UI → Story Nodes → Focus Mode, and that order is **non-negotiable**.:contentReference[oaicite:0]{index=0}

---

<details>
<summary>🧭 Table of Contents</summary>

- [✨ What this folder is for](#-what-this-folder-is-for)
- [🚦 How this differs from `data/work/`](#-how-this-differs-from-datawork)
- [🗂️ Recommended layout](#️-recommended-layout)
- [🧰 Work package checklist](#-work-package-checklist)
- [🧾 Required metadata](#-required-metadata)
- [🔐 Governance, licensing, and safety](#-governance-licensing-and-safety)
- [⏱️ Time semantics](#️-time-semantics)
- [🧹 Cleanup + promotion rules](#-cleanup--promotion-rules)
- [📎 Templates](#-templates)
- [🔗 Related docs](#-related-docs)

</details>

---

## ✨ What this folder is for

KFM is designed as a **pipeline–catalog–database–API–UI** system where every dataset/story/answer is traceable back to original sources (“the map behind the map”).:contentReference[oaicite:1]{index=1}  
This directory exists to support the messy reality that **external inputs arrive messy**.

Use `data/external/work/` for:
- 🧲 **Pulling/receiving external datasets** (downloads, scans, exports, dumps) *while you evaluate them*
- 🧪 **Prototyping transformations** (format conversion, georeferencing experiments, schema mapping drafts)
- 🧾 **Capturing provenance + license notes early**, before anything becomes “real” in the pipeline
- 📦 **Holding intermediate artifacts** that are *not yet deterministic, validated, or governance-approved*

KFM expects a clear lifecycle where data moves **raw → work → processed**, and only becomes “published” once it generates the required boundary artifacts (STAC/DCAT/PROV).:contentReference[oaicite:2]{index=2}

---

## 🚦 How this differs from `data/work/`

KFM’s canonical staging is:

- `data/raw/<domain>/` → immutable ingested sources  
- `data/work/<domain>/` → deterministic ETL intermediates  
- `data/processed/<domain>/` → authoritative outputs  
…and then catalogs/provenance are produced as required artifacts (STAC/DCAT/PROV).:contentReference[oaicite:3]{index=3}

So what’s `data/external/work/`?

✅ **Pre-ingestion sandbox**  
- You’re still deciding: *Do we keep this? Is the license OK? Is it sensitive? Is it even relevant?*  
- Transformations can be exploratory.

🚫 **Not allowed**  
- No direct consumption by graph/API/UI. The UI must not bypass governed layers, and published artifacts must be provenance-registered before any downstream use.:contentReference[oaicite:4]{index=4}

---

## 🗂️ Recommended layout

> Keep it boring and consistent. “One dataset = one folder.” 📁

```text
📁 data/
└─ 📁 external/
   └─ 📁 work/                                              🧪 external staging area (ephemeral; safe to prune)
      └─ 📁 <source_slug>__<dataset_slug>__v<ver>__YYYY-MM-DD/  🧷 one ingestion run (source + dataset + version + date)
         ├─ 📁 00_original/                                  🧾 immutable: as-received originals (never edit)
         ├─ 📁 01_extract/                                   📦 extracted contents (unzip/untar/unpack outputs)
         ├─ 📁 02_scratch/                                   🧪 experiments + dead-ends (safe to delete)
         ├─ 📁 03_normalize_draft/                            🧼 early normalization outputs (not yet canonical)
         ├─ 📁 90_notes/                                      📝 human notes, decisions, screenshots, links
         ├─ 📄 MANIFEST.yaml                                  ✅ required: run metadata (source, inputs, tools, outputs)
         ├─ 📄 LICENSE_NOTES.md                               🧾 license interpretation + citations/links (human-readable)
         ├─ 📄 CHECKSUMS.sha256                               ✅ required: integrity list (originals + key artifacts)
         └─ 📄 INGEST_PLAN.md                                 ✅ required: promotion plan (raw → work → processed + STAC/DCAT/PROV)
```

---

## 🧰 Work package checklist

### ✅ Minimum “ready for review” (inside external/work)

- [ ] **Originals preserved** in `00_original/` (no edits)
- [ ] **Manifest exists** (`MANIFEST.yaml`) with source links, retrieval date, license notes, and sensitivity classification
- [ ] **Checksums computed** for originals (`CHECKSUMS.sha256`)
- [ ] **Basic data quality scan done** (missing fields, obvious geometry issues, encoding problems)  
  > Expect data quality work to dominate effort—time-oriented datasets are especially error-prone, and it’s common that “dirty data” issues only appear once you start visualizing/inspecting it.:contentReference[oaicite:5]{index=5}

### 🟩 “Promotable” into the canonical pipeline

- [ ] License confirmed / usage terms compatible (or clearly restricted)
- [ ] Sensitivity classification finalized + propagation plan documented (no output less restricted than inputs):contentReference[oaicite:6]{index=6}
- [ ] Deterministic ETL steps identified (config-driven + idempotent):contentReference[oaicite:7]{index=7}
- [ ] Clear mapping to `data/raw/<domain>/…` and planned outputs to `data/processed/<domain>/…`:contentReference[oaicite:8]{index=8}
- [ ] Plan to generate **STAC/DCAT/PROV** artifacts before graph/UI use:contentReference[oaicite:9]{index=9}

---

## 🧾 Required metadata

KFM’s governance expects new external sources to be reviewed for **license, provenance quality, and standards alignment**.:contentReference[oaicite:10]{index=10}  
So every dataset folder here must include a minimal “paper trail” even if the data is ultimately rejected.

### 📌 Minimum fields (put these in `MANIFEST.yaml`)

| Field | Why it matters |
|---|---|
| `source.name` + `source.url` | Traceability + attribution |
| `retrieval.date` + `retrieval.by` | Provenance (who/when acquired) |
| `license.declared` + `license.link` | Legal/ethical constraints |
| `sensitivity.classification` | Governance + propagation rules |
| `geo.crs` / `time.internal` / `time.external` | Correct mapping + analysis semantics |
| `intended_domain` | Where it belongs in `data/raw/<domain>/…` |
| `notes.risks` | Anything that triggers governance review |

---

## 🔐 Governance, licensing, and safety

### 🧷 Governance triggers you should assume apply here
These changes often require manual review beyond automated checks:
- 🧾 **New external data sources** (license + provenance quality review):contentReference[oaicite:11]{index=11}
- 🪶 **Sensitive cultural/location layers** (e.g., archaeological sites, tribal lands) requiring permission and often obfuscation:contentReference[oaicite:12]{index=12}
- 🔁 **Classification changes** (anything becoming “less restricted”):contentReference[oaicite:13]{index=13}

### 🔒 Hard rules (don’t accidentally create a governance incident)
- **No secrets** (API keys, tokens) stored alongside data.
- **No PII/sensitive coordinates** unless explicitly permitted, classified, and handled with redaction plans (and expect scans to flag issues).:contentReference[oaicite:14]{index=14}
- **No output can be less restricted than its inputs** (classification must propagate).:contentReference[oaicite:15]{index=15}

---

## ⏱️ Time semantics

Many KFM datasets are time-oriented. Track time correctly by distinguishing:
- **Internal time** = when the information is valid (the time dimension inside the dataset)
- **External time** = when the dataset/version was created/updated (how it evolves over time):contentReference[oaicite:16]{index=16}

✅ In `MANIFEST.yaml`, capture both:
- `time.internal`: e.g., observation dates, event year ranges  
- `time.external`: retrieval date, last-updated date, pipeline run date

---

## 🧹 Cleanup + promotion rules

### 🗑️ Cleanup policy (recommended)
- `02_scratch/` is intentionally disposable.
- If a dataset is **rejected**, keep only:
  - `MANIFEST.yaml`
  - `LICENSE_NOTES.md`
  - a tiny excerpt or checksum list proving what was evaluated (no restricted content)

### 🚀 Promotion policy (when you “accept” the dataset)
1. Move immutable sources into `data/raw/<domain>/<dataset>/` (or reference via LFS/checksum fetch, if huge):contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}
2. Convert exploratory transforms into a deterministic pipeline that writes intermediates to `data/work/<domain>/…` and finals to `data/processed/<domain>/…`:contentReference[oaicite:19]{index=19}
3. Generate required boundary artifacts:
   - `data/stac/collections/` + `data/stac/items/`  
   - `data/catalog/dcat/`  
   - `data/prov/`:contentReference[oaicite:20]{index=20}
4. Only then: load into graph / expose through API / reference in Story Nodes.

> 🧠 Reminder: the repo is treated like a “versioned data lake” where changes are traceable through Git history.:contentReference[oaicite:21]{index=21}  
> For large binaries, use Git LFS or checksums + fetch scripts so identity stays tracked without bloating the repo.:contentReference[oaicite:22]{index=22}

---

## 📎 Templates

### 🧾 `MANIFEST.yaml` (starter)

```yaml
dataset:
  id: "<source_slug>__<dataset_slug>__v1__YYYY-MM-DD"
  title: "Human-readable title"
  intended_domain: "<domain>"   # maps to data/raw/<domain>/...
  description: >
    What is this dataset and why is it being evaluated?

source:
  name: "Provider / Archive / Agency"
  url: "https://example.org/dataset"
  citation: "How the provider requests citation (if known)"
  contact: "optional"

retrieval:
  date: "YYYY-MM-DD"
  by: "<name_or_handle>"
  method: "download | scan | api | email | physical_media"
  notes: "any access constraints (login, FOIA, etc.)"

license:
  declared: "unknown | public-domain | CC-BY-4.0 | custom | restricted"
  link: "https://example.org/license"
  notes: >
    What we believe the license allows/forbids (and what still needs verification).

sensitivity:
  classification: "public | internal | restricted"
  sovereignty_flags:
    - "CARE"
    - "sensitive-locations"
  redaction_needed: false
  redaction_notes: ""

geo:
  crs: "unknown | EPSG:4326 | EPSG:####"
  bbox: "optional"
  geometry_type: "raster | vector | tabular | text | mixed"

time:
  internal:
    start: "YYYY-MM-DD | YYYY | null"
    end: "YYYY-MM-DD | YYYY | null"
  external:
    retrieved: "YYYY-MM-DD"
    last_updated_upstream: "YYYY-MM-DD | null"

integrity:
  checksums_file: "CHECKSUMS.sha256"
  originals_path: "00_original/"

work_status:
  stage: "triage | profiling | normalization-draft | ready-for-governance | promote-to-raw | rejected"
  risks:
    - "missing license clarity"
    - "possible sensitive site coordinates"
  next_actions:
    - "run geometry validity checks"
    - "confirm license"
```

### 🧭 `INGEST_PLAN.md` (starter)

```markdown
# Ingest Plan — <dataset id>

## Target home
- data/raw/<domain>/<dataset>/
- data/work/<domain>/<dataset>/
- data/processed/<domain>/<dataset>/

## Deterministic pipeline outline
1) Extract/standardize inputs  
2) Normalize schema + attributes  
3) Reproject/align (if needed)  
4) Validate outputs  
5) Generate STAC/DCAT/PROV

## Governance notes
- License summary:
- Sensitivity classification:
- Redaction/generalization plan:
```

---

## 🔗 Related docs

- 📘 `docs/MASTER_GUIDE_v13.md` (canonical pipeline + invariants):contentReference[oaicite:23]{index=23}
- 🧾 STAC/DCAT/PROV alignment + expectations:contentReference[oaicite:24]{index=24}
- 🧭 KFM system overview + monorepo philosophy:contentReference[oaicite:25]{index=25}

---

<div align="center">

✅ If it’s not **cataloged + provenance-linked**, it’s not “real” in KFM yet.  
🧱 `external/work` is where we earn that trust.

</div>

