# 🧰 Data Documentation Hub (`docs/data/`)

![KFM](https://img.shields.io/badge/KFM-living%20atlas-blue)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-brightgreen)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-orange)
![Pipeline](https://img.shields.io/badge/pipeline-no%20skips-red)

Welcome to the **data documentation home** for **Kansas Frontier Matrix (KFM)** — where each data domain has a runbook, each dataset has traceable metadata, and every derived artifact has provenance. KFM is explicitly designed so **evidence flows through catalogs and contracts before it reaches the graph, API, UI, or narrative layer.**:contentReference[oaicite:0]{index=0}

> ✅ **This folder (`docs/data/`) is documentation** (runbooks, sources, ETL notes, governance notes).  
> 📦 **Actual datasets live in `data/`** (raw/work/processed + catalogs/provenance).:contentReference[oaicite:1]{index=1}

---

## 🔗 Quick Links (high-signal)

- 📘 **Master Guide v13 (canonical)** → `../MASTER_GUIDE_v13.md`:contentReference[oaicite:2]{index=2}
- 🧾 **Metadata profiles**
  - STAC → `../standards/KFM_STAC_PROFILE.md`:contentReference[oaicite:3]{index=3}
  - DCAT → `../standards/KFM_DCAT_PROFILE.md`:contentReference[oaicite:4]{index=4}
  - PROV → `../standards/KFM_PROV_PROFILE.md`:contentReference[oaicite:5]{index=5}
- ⚖️ **Governance**
  - Root governance → `../governance/ROOT_GOVERNANCE.md`:contentReference[oaicite:6]{index=6}
  - Ethics → `../governance/ETHICS.md`:contentReference[oaicite:7]{index=7}
  - Sovereignty → `../governance/SOVEREIGNTY.md`:contentReference[oaicite:8]{index=8}
- 🧩 Templates
  - Universal doc → `../templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`:contentReference[oaicite:9]{index=9}

---

## 🗺️ Canonical Pipeline (non‑negotiable)

KFM’s **canonical pipeline ordering** is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → Map UI → Story Nodes → Focus Mode**:contentReference[oaicite:10]{index=10}

Any proposal or implementation that “shortcuts” this ordering is considered flawed unless explicitly justified and governed.:contentReference[oaicite:11]{index=11}

```mermaid
flowchart LR
  A[📥 ETL / Normalization] --> B[🧾 STAC/DCAT/PROV Catalogs]
  B --> C[🕸️ Neo4j Graph<br/>(references catalogs)]
  C --> D[🧩 API Layer<br/>(contracts + redaction)]
  D --> E[🗺️ Map UI]
  E --> F[📝 Story Nodes]
  F --> G[🎯 Focus Mode]
```

(High-level flow matches KFM’s “boundary artifact” approach: each stage consumes the previous stage’s outputs to preserve traceability.):contentReference[oaicite:12]{index=12}

---

## 📦 Data vs Docs: What lives where?

### ✅ The *data* lifecycle (required staging)

All data must move through these staged directories:

- `data/raw/<domain>/` → raw source snapshots (**read-only**)
- `data/work/<domain>/` → intermediate/transient processing outputs
- `data/processed/<domain>/` → final, standardized outputs ready for serving/publishing:contentReference[oaicite:13]{index=13}

Raw data is treated as **write-once, read-only “evidence”** and should not be modified by pipelines.:contentReference[oaicite:14]{index=14}

### ✅ The “boundary artifacts” (required to be considered *published*)

At publication time, every dataset generates catalog/provenance records:

- **STAC**  
  - `data/stac/collections/` (collection-level)  
  - `data/stac/items/` (item-level):contentReference[oaicite:15]{index=15}
- **DCAT**  
  - `data/catalog/dcat/` (dataset discovery JSON-LD catalog entries):contentReference[oaicite:16]{index=16}
- **PROV**  
  - `data/prov/` (lineage bundle: inputs, activities, agents):contentReference[oaicite:17]{index=17}

> 🧠 **Legacy note (v12→v13 migrations):** older docs may refer to `data/catalog/` and `data/provenance/`. v13 standardizes the canonical homes to `data/stac/`, `data/catalog/dcat/`, and `data/prov/`.:contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}

---

## 🧩 Domain Modules in `docs/data/`

Each domain should have a concise README under `docs/data/<domain>/` describing:

- source(s) & licensing
- ETL steps & pipeline entry points
- quality checks & caveats
- governance, FAIR/CARE, sovereignty considerations
- mapping to STAC/DCAT/PROV “boundary artifacts” (optional `mappings/`):contentReference[oaicite:20]{index=20}

### 🌱 Existing / Example modules

- 🏛️ `historical/land-treaties/README.md`:contentReference[oaicite:21]{index=21}
- 🌫️ `air-quality/README.md`:contentReference[oaicite:22]{index=22}
- 🌾 `soils/sda/README.md`:contentReference[oaicite:23]{index=23}

> 🔁 If you add a new domain module, it should be linkable from the Master Guide for visibility and stewardship clarity.:contentReference[oaicite:24]{index=24}

---

## 🧱 Recommended doc structure for a Domain README

Use this as a consistent “runbook skeleton” for `docs/data/<domain>/README.md`:

1. **Scope & datasets** (what’s in/out)
2. **Sources** (URLs, citations, download notes)
3. **License & usage constraints** (including redistribution)
4. **Governance & sovereignty** (classification, redaction, sensitivity, CARE notes)
5. **ETL / pipeline runbook**
   - input(s): `data/raw/<domain>/...`
   - process: scripts/notebooks + configs
   - outputs: `data/processed/<domain>/...`
6. **Metadata & lineage**
   - STAC collection/items links
   - DCAT entry links
   - PROV bundle links
7. **QA / validation checks**
8. **Known limitations & uncertainty**

---

## ✅ Dataset Publication Checklist (Definition of Done)

Use this checklist before opening a PR for a new dataset or update:

### 📥 Ingest
- [ ] Raw source snapshot is stored under `data/raw/<domain>/` and treated as **read-only evidence**:contentReference[oaicite:25]{index=25}
- [ ] Pipeline processes raw → processed via deterministic steps (no interactive/manual prompts):contentReference[oaicite:26]{index=26}
- [ ] **No ad-hoc edits**: processed outputs are never manually “tweaked”; fix pipeline or raw input and re-run:contentReference[oaicite:27]{index=27}

### 📦 Output
- [ ] Final outputs stored under `data/processed/<domain>/...` in appropriate formats (e.g., GeoJSON/Parquet/GeoTIFF as needed):contentReference[oaicite:28]{index=28}

### 🧾 Metadata (required)
- [ ] STAC collection + item(s) exist (canonical `data/stac/...`):contentReference[oaicite:29]{index=29}
- [ ] DCAT dataset entry exists (`data/catalog/dcat/`) and includes title, description, license, keywords, distribution links:contentReference[oaicite:30]{index=30}
- [ ] PROV bundle exists (`data/prov/`) and links raw → work → processed outputs:contentReference[oaicite:31]{index=31}

PROV should be rich enough to answer “how was this produced?”, including:
- **Entities** (inputs/outputs, checksums/refs)  
- **Activities** (pipeline run info, timestamps)  
- **Agents** (human/software):contentReference[oaicite:32]{index=32}

### 📚 Docs
- [ ] Domain README updated (`docs/data/<domain>/README.md`) with ETL notes, sources, governance considerations:contentReference[oaicite:33]{index=33}
- [ ] If AI/analysis produced the dataset, it is treated as a first-class **evidence artifact**: stored in processed, cataloged in STAC/DCAT, traced in PROV:contentReference[oaicite:34]{index=34}

### 🧪 CI / Review expectations
- [ ] PR includes processed file **and** corresponding metadata/provenance records (CI validates presence/consistency):contentReference[oaicite:35]{index=35}
- [ ] PR includes explicit license info; missing license should fail closed:contentReference[oaicite:36]{index=36}

---

## 🌐 STAC/DCAT/PROV “Alignment Rules” (required)

KFM requires every dataset (including evidence artifacts) to have:

- STAC collection/item(s)
- DCAT dataset entry
- PROV activity bundle:contentReference[oaicite:37]{index=37}

And KFM expects cross-layer linkage:

- STAC → points to data asset (processed file or stable API endpoint)
- DCAT → links to STAC and/or distributions
- PROV → links raw inputs → intermediates → processed outputs, and identifies the pipeline run/config (e.g., commit hash):contentReference[oaicite:38]{index=38}

Also:
- Graph stores **references to catalogs**, not bulky payloads (graph models relationships; catalogs store metadata + links).:contentReference[oaicite:39]{index=39}

---

## ⚖️ Governance & Safety (FAIR + CARE)

KFM is designed to “fail closed” when governance requirements aren’t met (e.g., missing license, broken checks).:contentReference[oaicite:40]{index=40}

FAIR and CARE are built into the architecture via:
- required metadata (findable/interoperable)
- open formats + version control (accessible/reusable)
- access control + sovereignty-aware handling for sensitive data (CARE):contentReference[oaicite:41]{index=41}

> 📌 For domain-specific governance rules (classification, redaction constraints, community ownership), see:  
> `../governance/ROOT_GOVERNANCE.md`, `../governance/ETHICS.md`, `../governance/SOVEREIGNTY.md`:contentReference[oaicite:42]{index=42}

---

## 🗂️ Handy “Where do I put this?” map

From the v13 repository map (expected structure):​:contentReference[oaicite:43]{index=43}

- 📁 `data/` → raw/work/processed + catalog outputs (STAC/DCAT/PROV)
- 📁 `docs/` → canonical governed docs (guides, designs, domain notes)
- 📁 `docs/data/` → **domain runbooks (this folder)**
- 📁 `schemas/` → JSON Schemas for STAC/DCAT/PROV/storynodes/etc.
- 📁 `src/pipelines/` → ETL jobs
- 📁 `src/graph/` → graph build
- 📁 `src/server/` → API boundary
- 📁 `web/` → UI

---

## 🕰️ Versioning note (v13 migration)

v13 introduced canonical subsystem homes and filled missing expected top-level dirs like `data/catalog/dcat/` and `data/prov/` (superseding v12 guidance).:contentReference[oaicite:44]{index=44}:contentReference[oaicite:45]{index=45}

---

## 📚 Sources used to author this README

- Master Guide v13 excerpts (pipeline order, data lifecycle, domain docs expectations, and repo map).:contentReference[oaicite:46]{index=46}:contentReference[oaicite:47]{index=47}:contentReference[oaicite:48]{index=48}
- KFM technical blueprint excerpts (raw/processed rules, no ad-hoc edits, provenance expectations, CI requirements, FAIR/CARE fail-closed principles).:contentReference[oaicite:49]{index=49}:contentReference[oaicite:50]{index=50}:contentReference[oaicite:51]{index=51}:contentReference[oaicite:52]{index=52}
