---
title: "Data Domain — <domain>"
path: "docs/data/<domain>/README.md"
version: "v0.1.0"
last_updated: "2026-01-26"
status: "active" # draft | active | deprecated
doc_kind: "Domain Runbook"
license: "CC-BY-4.0"
fair_category: "FAIR+CARE"
care_label: "TBD"          # Public | Restricted | Tribal Sensitive | etc.
sensitivity: "public"      # public | restricted
classification: "open"     # open | internal | confidential
owner: "@<github-handle-or-team>"
---

# 🗂️ Data Domain — `<domain>` 🧭

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Domain](https://img.shields.io/badge/domain-%3Cdomain%3E-blue)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-purple)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE-teal)
![Provenance](https://img.shields.io/badge/provenance-evidence--first-orange)

> **What this is:** the **runbook + index** for everything KFM considers “published” in the **`<domain>`** data module: sources, ETL, outputs, catalogs, QA, and how this domain shows up in UI + Focus Mode 🤖.

---

## 🔗 Quick links

- 🧾 **Add a dataset:** see **[Adding / Updating a Dataset](#-adding--updating-a-dataset)**
- ✅ **Publish gate (Definition of Done):** see **[Definition of Done](#-definition-of-done)**
- 🧠 **Focus Mode coverage:** see **[Focus Mode Coverage](#-focus-mode-coverage)**
- 🗺️ **Story Nodes usage:** see **[UI + Story Node Integration](#️-ui--story-node-integration)**

---

## 📚 Table of contents

- [🧭 Overview](#-overview)
- [🧱 Scope](#-scope)
- [🧺 Domain inventory](#-domain-inventory)
- [🔁 Data lifecycle](#-data-lifecycle)
- [🧾 Metadata + provenance contract](#-metadata--provenance-contract)
- [🛠️ Pipelines](#️-pipelines)
- [✅ QA + validation](#-qa--validation)
- [🔐 Governance + sensitivity](#-governance--sensitivity)
- [🌐 API surfaces](#-api-surfaces)
- [🖥️ UI + Story Node integration](#️-ui--story-node-integration)
- [🤖 Focus Mode coverage](#-focus-mode-coverage)
- [🤝 Contributing](#-contributing)
- [✅ Definition of Done](#-definition-of-done)
- [📎 Appendix: Templates](#-appendix-templates)
- [📚 Project reference library](#-project-reference-library)

---

## 🧭 Overview

**Domain goal:** describe *what* `<domain>` is, *why* it exists in KFM, and *which data products* are considered authoritative here.

**Replace `<domain>` with something stable + folder-safe**, e.g.:
- `land_treaties`
- `air_quality`
- `hydrology`
- `railroads`
- `archaeology_sites`

> 💡 Tip: Keep the domain name a **noun** (or noun phrase) and use `snake_case`.

---

## 🧱 Scope

| In scope ✅ | Out of scope 🚫 |
|---|---|
| Source inventories + acquisition notes | Platform-wide architecture (belongs in global docs) |
| ETL/normalization steps and run commands | Secrets, tokens, private keys |
| Output datasets + schemas + data dictionary | Raw data storage policies outside KFM conventions |
| Catalog artifacts (STAC/DCAT/PROV) | One-off “mystery” files with no provenance |
| QA checks + validation results | Non-domain utilities (shared tooling goes elsewhere) |
| Story Nodes + examples that depend on this domain | Cross-domain narrative decisions (use Story governance docs) |

---

## 🧺 Domain inventory

### 🗺️ Data products (authoritative outputs)

> Fill this table in as you publish datasets. Keep it small and scannable ✨

| product_id | type | canonical_output | temporal? | steward | sensitivity |
|---|---:|---|---:|---|---|
| `kfm.<domain>.<dataset>` | vector/raster/tabular/text | `data/processed/<domain>/<dataset>/...` | ✅/❌ | @name | public/restricted |
| `kfm.<domain>.<dataset2>` |  |  |  |  |  |

### 📖 Story Nodes that use this domain

- `stories/<domain>/<story_slug>.md` + `stories/<domain>/<story_slug>.json`
- Add new entries as they ship.

### 🧪 Notebooks / analyses (optional)

- `notebooks/<domain>/...` (if you maintain notebooks)
- Link anything meant to be reused (tutorials, reproducible analyses)

---

## 🔁 Data lifecycle

KFM treats data as a **staged pipeline** (raw → work → processed), and only considers something “published” once **catalog boundary artifacts** exist (STAC/DCAT/PROV).

### 📦 Required staging areas (filesystem convention)

```text
data/
  raw/<domain>/         # immutable intake (exactly what you received)
  work/<domain>/        # intermediate products (re-runnable, disposable)
  processed/<domain>/   # final, versioned, publishable outputs ✅
```

### 🧷 Catalog boundary artifacts (publication gate)

```text
data/
  stac/
    collections/        # collection metadata
    items/              # item-level metadata
  catalog/
    dcat/               # dataset-level discovery entries (JSON-LD)
  prov/                 # lineage bundles (inputs, steps, agents)
```

### 🧬 Evidence artifacts (AI / analysis outputs)

Any **analysis output** or **AI-generated dataset** that will be used downstream (UI, graph, reporting, Focus Mode) must be treated like a *first-class dataset*:
- stored in `data/processed/...`
- gets full STAC/DCAT/PROV
- documented here (sources + method + QA)

---

## 🧾 Metadata + provenance contract

### 🎯 The “metadata triplet” (required)

Every published dataset in this domain must produce:

1. **STAC** (collection + items) → geospatial discovery + bounding boxes + assets  
2. **DCAT** (JSON-LD) → dataset-level catalog + licensing + distributions  
3. **PROV** (JSON) → lineage: inputs → activities → outputs (and who/what ran it)

> ✅ Rule: **If it can’t be cited, it can’t be used.** (This is what powers evidence-first UI + Focus Mode.)

### 🧷 Domain-specific schemas

Store domain schema definitions here:

```text
docs/data/<domain>/
  schemas/
    <dataset>.schema.json
    <dataset>.fields.md
```

Minimum: define
- required fields
- geometry type (if geospatial)
- time fields (if temporal)
- primary keys / identifiers
- controlled vocabularies (if any)

### 🧠 Ontology mapping (graph alignment)

If this domain maps into the knowledge graph, document:
- node labels + edge types
- entity resolution rules (IDs, aliases)
- provenance links (graph nodes must reference catalog IDs)

```text
docs/data/<domain>/
  ontology/
    mapping.md
    entities.md
    relationships.md
```

---

## 🛠️ Pipelines

### 🧰 Where pipeline code should live

Pick one pattern and stick to it:

- `pipelines/<domain>/...` *(recommended if repo is code-heavy)*
- or `docs/data/<domain>/pipelines/` *(if your pipelines are mostly documented runbooks)*

### ♻️ Pipeline rules (non-negotiable)

- **Deterministic outputs** (seed randomness where applicable)
- **Immutable raw** inputs
- **Version outputs** (and never silently overwrite “published” artifacts)
- **Produce the metadata triplet** every publish run
- **Log + checksum** key artifacts

### 🐳 Local dev expectation

If the project uses containerized services, keep commands simple and repeatable:

```bash
# Example (adjust to your repo tooling)
make etl DOMAIN=<domain>
make publish DOMAIN=<domain>
make validate DOMAIN=<domain>
```

> 🧩 If you need PostGIS / Neo4j / search locally, prefer Docker Compose / containers instead of “install it on your laptop” instructions.

---

## ✅ QA + validation

### ✅ Minimum QA checklist (per dataset)

- Schema validation passes ✅
- Geometry validity checks pass (if geospatial) ✅
- Time fields validate (if temporal) ✅
- Counts / distributions sanity-checked ✅
- Duplicate IDs resolved ✅
- Spot-check sample records against raw evidence ✅
- Licensing and sensitivity labels confirmed ✅

### 🧪 Regression tests (pipeline-level)

When possible:
- unit tests for transformations
- integration tests for end-to-end ETL
- CI runs on PRs

---

## 🔐 Governance + sensitivity

### 🧭 FAIR + CARE (required posture)

Each dataset/doc declares:
- **license**
- **sensitivity**
- **classification**
- **care_label** (if applicable)

> ⚠️ If a dataset includes culturally sensitive or restricted info, document the **redaction/aggregation strategy** (and who approved it).

### 🧱 Policy enforcement

Document here any domain rules that must be enforced at query-time:
- attribute redaction
- coordinate fuzzing / generalization
- access rules / role gates
- “no-export” constraints for certain subsets

---

## 🌐 API surfaces

Document how users/devs should access this domain.

### 🧾 REST endpoints (examples)

```http
GET /api/layers/<layer_id>?bbox=<...>&time=<...>
GET /api/datasets/<dataset_id>
GET /api/tiles/<layer_id>/{z}/{x}/{y}.pbf?time=<...>
GET /api/search?q=<term>&domain=<domain>
```

### 🧬 GraphQL (examples)

```graphql
query DomainEntities($q: String!) {
  searchEntities(query: $q, domain: "<domain>") {
    id
    label
    type
    provenance { stac dcat prov }
  }
}
```

### 🤖 Focus Mode endpoint (evidence-first)

```http
POST /focus-mode/query
{
  "question": "What changed in <domain> between 1880 and 1900?",
  "domain": "<domain>",
  "constraints": { "time_range": ["1880-01-01", "1900-12-31"] }
}
```

---

## 🖥️ UI + Story Node integration

### 🗺️ Layer behavior

Document:
- layer IDs exposed in UI
- category grouping (Historical / Environmental / Social / etc.)
- time filtering behavior (if the layer is time-aware)

### 📖 Story Nodes (Markdown + JSON)

Story Nodes should reference **domain datasets** via IDs and cite sources in narrative text.

```text
stories/<domain>/
  <story_slug>.md     # narrative
  <story_slug>.json   # map/timeline script
```

> ✨ Keep the narrative readable for non-technical contributors; keep the JSON script predictable for the UI.

---

## 🤖 Focus Mode coverage

### 🎯 Questions this domain must answer well

Add 5–15 canonical questions that define “good coverage” for `<domain>`:

1. “What are the key datasets in `<domain>` and what do they represent?”
2. “What changed in `<domain>` over time in region X?”
3. “What is the provenance of dataset Y?”
4. “Which Story Nodes reference dataset Y?”
5. “What are known limitations / gaps in this domain?”

### 🧾 Citation expectations

For every question above, Focus Mode should be able to return:
- a direct answer **and**
- citations to dataset artifacts / catalog entries / story sources

---

## 🤝 Contributing

### 🧑‍💻 Workflow

1. Create a branch: `domain/<domain>/<short-change>`
2. Add/modify:
   - sources manifests
   - pipeline code/runbooks
   - processed outputs metadata (STAC/DCAT/PROV)
   - docs + examples
3. Open a PR:
   - include QA evidence
   - link to issues if applicable
4. Review focuses on:
   - provenance completeness
   - schema correctness
   - governance labels
   - reproducibility

---

## ✅ Definition of Done

### ✅ Dataset publish DoD

- [ ] Raw intake stored under `data/raw/<domain>/...` (immutable)
- [ ] ETL is deterministic and repeatable (documented run command)
- [ ] Output stored under `data/processed/<domain>/...`
- [ ] STAC collection + items generated
- [ ] DCAT dataset entry generated (JSON-LD)
- [ ] PROV lineage bundle generated
- [ ] QA checklist completed + results recorded
- [ ] License + sensitivity + CARE labels declared
- [ ] UI layer IDs documented (if applicable)
- [ ] Focus Mode questions updated (if this changes expected answers)

### ✅ Doc DoD (this README)

- [ ] Scope table filled
- [ ] Domain inventory table has authoritative outputs
- [ ] Pipeline section contains runnable commands
- [ ] Governance section states any special rules
- [ ] Examples / queries included
- [ ] Links are valid and up-to-date

---

## 📎 Appendix: Templates

<details>
  <summary>📄 Source manifest template (copy/paste)</summary>

```yaml
# docs/data/<domain>/sources/<source_id>.yml
source_id: "<source_id>"
title: "<human title>"
owner: "<org/person>"
retrieved_at: "YYYY-MM-DD"
license: "<license>"
original_format: "<pdf/csv/shp/api/etc>"
access:
  method: "<url/api/physical>"
  url: "<link or internal path>"
integrity:
  sha256: "<hash if file-based>"
coverage:
  spatial: "<bbox or region>"
  temporal: "<range or n/a>"
notes: |
  - What is this source?
  - Any known issues?
```

</details>

<details>
  <summary>🧾 Dataset doc template</summary>

```markdown
# Dataset — <dataset_id>

## Summary
## Source(s)
## Schema
## Processing steps (ETL)
## QA results
## Provenance links
- STAC:
- DCAT:
- PROV:
## Known limitations
## Consumers (UI / API / Stories / Focus Mode)
```

</details>

---

## 📚 Project reference library

Use these as source-of-truth while filling this domain README (and link them in PRs when relevant) 📌

### 🧩 KFM core (architecture + platform)
- *Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf*
- *Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf*
- *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf*
- *Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf*

### 🤖 AI + infrastructure
- *Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf*
- *KFM AI Infrastructure – Ollama Integration Overview.pdf*

### 🧠 Documentation + protocols
- *Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx*
- *Scientific Method _ Research _ Master Coder Protocol Documentation.pdf*
- *MARKDOWN_GUIDE_v13.md.gdoc*

### 🗺️ Reference compendiums (portfolios)
- *AI Concepts & more.pdf*
- *Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf*
- *Various programming langurages & resources 1.pdf*
- *Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf*
- *Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf*
- *Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf*

---

⬆️ **Back to top:** [Table of contents](#-table-of-contents)