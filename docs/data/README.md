# 🧰 Data Documentation Hub (`docs/data/`)

![KFM](https://img.shields.io/badge/KFM-living%20atlas-blue)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-brightgreen)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-orange)
![Pipeline](https://img.shields.io/badge/pipeline-no%20skips-red)

Welcome to the **data documentation home** for **Kansas Frontier Matrix (KFM)** — where each data domain has a runbook, each dataset has traceable metadata, and every derived artifact has provenance. KFM is explicitly designed so **evidence flows through catalogs and contracts before it reaches the graph, API, UI, or narrative layer.** [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> ✅ **This folder (`docs/data/`) is documentation** (runbooks, sources, ETL notes, governance notes).  
> 📦 **Actual datasets live in `data/`** (raw/work/processed + catalogs/provenance). [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔗 Quick Links (high-signal)

- 📘 **Master Guide v13 (canonical)** → `../MASTER_GUIDE_v13.md` [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- 🧾 **Metadata profiles**
  - STAC → `../standards/KFM_STAC_PROFILE.md` [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
  - DCAT → `../standards/KFM_DCAT_PROFILE.md` [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
  - PROV → `../standards/KFM_PROV_PROFILE.md` [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- ⚖️ **Governance**
  - Root governance → `../governance/ROOT_GOVERNANCE.md` [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
  - Ethics → `../governance/ETHICS.md` [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
  - Sovereignty → `../governance/SOVEREIGNTY.md` [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- 🧩 Templates
  - Universal doc → `../templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗺️ Canonical Pipeline (non‑negotiable)

KFM’s **canonical pipeline ordering** is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → Map UI → Story Nodes → Focus Mode** [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Any proposal or implementation that “shortcuts” this ordering is considered flawed unless explicitly justified and governed. [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

```mermaid
flowchart LR
  A[📥 ETL / Normalization] --> B[🧾 STAC/DCAT/PROV Catalogs]
  B --> C[🕸️ Neo4j Graph<br/>(references catalogs)]
  C --> D[🧩 API Layer<br/>(contracts + redaction)]
  D --> E[🗺️ Map UI]
  E --> F[📝 Story Nodes]
  F --> G[🎯 Focus Mode]
```

(High-level flow matches KFM’s “boundary artifact” approach: each stage consumes the previous stage’s outputs to preserve traceability.) [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📦 Data vs Docs: What lives where?

### ✅ The *data* lifecycle (required staging)

All data must move through these staged directories:

- `data/raw/<domain>/` → raw source snapshots (**read-only**)
- `data/work/<domain>/` → intermediate/transient processing outputs
- `data/processed/<domain>/` → final, standardized outputs ready for serving/publishing [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Raw data is treated as **write-once, read-only “evidence”** and should not be modified by pipelines. [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ✅ The “boundary artifacts” (required to be considered *published*)

At publication time, every dataset generates catalog/provenance records:

- **STAC**  
  - `data/stac/collections/` (collection-level)  
  - `data/stac/items/` (item-level) [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **DCAT**  
  - `data/catalog/dcat/` (dataset discovery JSON-LD catalog entries) [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **PROV**  
  - `data/prov/` (lineage bundle: inputs, activities, agents) [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> 🧠 **Legacy note (v12→v13 migrations):** older docs may refer to `data/catalog/` and `data/provenance/`. v13 standardizes the canonical homes to `data/stac/`, `data/catalog/dcat/`, and `data/prov/`. [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧩 Domain Modules in `docs/data/`

Each domain should have a concise README under `docs/data/<domain>/` describing:

- source(s) & licensing
- ETL steps & pipeline entry points
- quality checks & caveats
- governance, FAIR/CARE, sovereignty considerations
- mapping to STAC/DCAT/PROV “boundary artifacts” (optional `mappings/`) [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🌱 Existing / Example modules

- 🏛️ `historical/land-treaties/README.md` [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- 🌫️ `air-quality/README.md` [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- 🌾 `soils/sda/README.md` [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> 🔁 If you add a new domain module, it should be linkable from the Master Guide for visibility and stewardship clarity. [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

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
- [ ] Raw source snapshot is stored under `data/raw/<domain>/` and treated as **read-only evidence** [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Pipeline processes raw → processed via deterministic steps (no interactive/manual prompts) [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] **No ad-hoc edits**: processed outputs are never manually “tweaked”; fix pipeline or raw input and re-run [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 📦 Output
- [ ] Final outputs stored under `data/processed/<domain>/...` in appropriate formats (e.g., GeoJSON/Parquet/GeoTIFF as needed) [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🧾 Metadata (required)
- [ ] STAC collection + item(s) exist (canonical `data/stac/...`) [oai_citation:29‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] DCAT dataset entry exists (`data/catalog/dcat/`) and includes title, description, license, keywords, distribution links [oai_citation:30‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] PROV bundle exists (`data/prov/`) and links raw → work → processed outputs [oai_citation:31‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

PROV should be rich enough to answer “how was this produced?”, including:
- **Entities** (inputs/outputs, checksums/refs)  
- **Activities** (pipeline run info, timestamps)  
- **Agents** (human/software) [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 📚 Docs
- [ ] Domain README updated (`docs/data/<domain>/README.md`) with ETL notes, sources, governance considerations [oai_citation:33‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] If AI/analysis produced the dataset, it is treated as a first-class **evidence artifact**: stored in processed, cataloged in STAC/DCAT, traced in PROV [oai_citation:34‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧪 CI / Review expectations
- [ ] PR includes processed file **and** corresponding metadata/provenance records (CI validates presence/consistency) [oai_citation:35‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] PR includes explicit license info; missing license should fail closed [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🌐 STAC/DCAT/PROV “Alignment Rules” (required)

KFM requires every dataset (including evidence artifacts) to have:

- STAC collection/item(s)
- DCAT dataset entry
- PROV activity bundle [oai_citation:37‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

And KFM expects cross-layer linkage:

- STAC → points to data asset (processed file or stable API endpoint)
- DCAT → links to STAC and/or distributions
- PROV → links raw inputs → intermediates → processed outputs, and identifies the pipeline run/config (e.g., commit hash) [oai_citation:38‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Also:
- Graph stores **references to catalogs**, not bulky payloads (graph models relationships; catalogs store metadata + links). [oai_citation:39‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ⚖️ Governance & Safety (FAIR + CARE)

KFM is designed to “fail closed” when governance requirements aren’t met (e.g., missing license, broken checks). [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

FAIR and CARE are built into the architecture via:
- required metadata (findable/interoperable)
- open formats + version control (accessible/reusable)
- access control + sovereignty-aware handling for sensitive data (CARE) [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> 📌 For domain-specific governance rules (classification, redaction constraints, community ownership), see:  
> `../governance/ROOT_GOVERNANCE.md`, `../governance/ETHICS.md`, `../governance/SOVEREIGNTY.md` [oai_citation:42‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗂️ Handy “Where do I put this?” map

From the v13 repository map (expected structure): [oai_citation:43‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

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

v13 introduced canonical subsystem homes and filled missing expected top-level dirs like `data/catalog/dcat/` and `data/prov/` (superseding v12 guidance). [oai_citation:44‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:45‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📚 Sources used to author this README

- Master Guide v13 excerpts (pipeline order, data lifecycle, domain docs expectations, and repo map). [oai_citation:46‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:47‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:48‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- KFM technical blueprint excerpts (raw/processed rules, no ad-hoc edits, provenance expectations, CI requirements, FAIR/CARE fail-closed principles). [oai_citation:49‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:50‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:51‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:52‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)