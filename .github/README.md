<div align="center">

# 🧭 Kansas Frontier Matrix (KFM)

**Open-source geospatial + historical mapping hub for Kansas — from raw sources ➜ governed datasets ➜ interactive 2D/3D maps ➜ evidence-backed answers.**[^kfm_system]

<p>
  <a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix"><img alt="Repo" src="https://img.shields.io/badge/GitHub-Kansas--Frontier--Matrix-181717?style=for-the-badge&logo=github"></a>
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
  <img alt="Stars" src="https://img.shields.io/github/stars/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
  <img alt="Issues" src="https://img.shields.io/github/issues/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix?style=for-the-badge">
</p>

**Quick links:**  
[🚀 Quickstart](#-quickstart) · [🍳 Usage recipes](#-usage-recipes) · [🏗️ Architecture](#️-architecture-at-a-glance) · [📦 Repo layout](#-repo-layout) · [🧩 the-github-folder](#-the-github-folder-what-should-live-in-github) · [🤖 Focus Mode AI](#-focus-mode-ai-local-first-but-governed) · [🤝 Contributing](#-contributing) · [📚 Project library](#-project-library) · [🧾 Sources](#-sources-footnotes)

</div>

> [!NOTE]
> This file lives in `.github/README.md` so it shows up when browsing the `.github/` folder.  
> If you also maintain a root README, keep it shorter and link here for the GitHub ops details. 🧩

---

## 🔎 What is KFM?

KFM is a **pipeline → catalog → database → API → UI** system that transforms raw historical + geospatial sources into **traceable** layers, stories, and answers.[^kfm_system]  
The UI doesn’t query databases directly; everything is mediated via the backend so governance rules are enforceable end-to-end.[^kfm_system]

> [!IMPORTANT]
> KFM is designed to **fail closed**: if policy/permission is uncertain, access is denied by default.[^fail_closed]

---

## 🗺️ Features

### ✅ What you can do (today + near-term)

- **Ingest & normalize** raw sources (rasters, vectors, tables) into cleaned “processed” artifacts.[^kfm_pipeline_order]
- **Publish a catalog** using standards-friendly outputs (**STAC / DCAT / PROV**) so people can trust what they’re seeing.[^stac_dcat_prov]
- **Explore Kansas in 2D & 3D** with modern web mapping (MapLibre) + optional 3D globe/terrain (Cesium).[^tech_stack]
- **Use “story nodes”**: narrative Markdown + a choreography script that drives map state (camera, layers, timeline).[^story_nodes]
- **Ask questions** in *Focus Mode* and get responses constrained by governance (even with a local model).[^focus_mode]
- **Export & interop** (COGs, GeoJSON, Shapefiles, tiles, KML/KMZ) for sharing and downstream analysis.[^exports_formats]

### 🧬 Project principles

- **Metadata is not optional.** Every dataset/evidence artifact must ship with **STAC + DCAT + PROV** records; CI validates conformance.[^stac_dcat_prov]
- **Cartography is communication.** Map outputs should clearly communicate scale, projection/CRS, and sources/credits.[^map_design]
- **Provenance over vibes.** Nothing enters KFM without provenance logs + descriptive metadata; AI answers and narratives attach citations.[^provenance_first]

---

## 🚀 Quickstart

### ✅ Recommended: Docker Compose

```bash
# from the repo root
docker compose up --build
# (older Docker setups: docker-compose up --build)
```

Default local endpoints:

- 🖥️ **Web UI**: `http://localhost:3000`
- 🧠 **API**: `http://localhost:8000`
- 📘 **Swagger / OpenAPI docs**: `http://localhost:8000/docs`
- 🕸️ **Neo4j Browser**: `http://localhost:7474`

If ports conflict, change mappings in `docker-compose.yml` and restart.[^docker_quickstart]

---

### 🧰 Local dev (manual) — for contributors

> [!TIP]
> These commands are “typical FastAPI/React” defaults; adapt to your repo’s actual `requirements` / package manager.

<details>
<summary><b>Backend (FastAPI)</b></summary>

KFM’s backend pattern emphasizes: **routers** validate inputs, call **service** logic, and enforce governance checks in a consistent place.[^tech_stack]

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r api/requirements.txt

uvicorn api.main:app --reload --port 8000
```

</details>

<details>
<summary><b>Frontend (React + MapLibre + optional Cesium)</b></summary>

```bash
cd web
npm install
npm run dev
```

MapLibre is used for 2D interactive maps, with Cesium as an optional 3D view.[^tech_stack]

</details>

<details>
<summary><b>Datastores (PostGIS + Neo4j)</b></summary>

- PostGIS stores spatial primitives + queryable layers (boundaries, overlays).
- Neo4j stores relationships (events ↔ people ↔ places) for “relatedness” and story graph traversal.[^tech_stack]

</details>

---

## 🍳 Usage recipes

### 1) Explore the API surface

- Open `http://localhost:8000/docs` (Swagger UI) to try endpoints and inspect request/response models.[^docker_quickstart]

### 2) Add a new dataset the “KFM way” (Raw ➜ Processed ➜ Catalog/PROV)

KFM’s canonical order is:

**Raw → Processed → Catalog/PROV → Database → API → UI**.[^kfm_pipeline_order]

A “complete” dataset contribution includes:

- ✅ **Processed output(s)** saved under `data/processed/**` (or the canonical equivalent).[^kfm_pipeline_order]
- ✅ **STAC** Collection + Item(s)
- ✅ **DCAT** dataset entry
- ✅ **PROV** activity bundle that links raw inputs → intermediate work → processed outputs (including who/what/when/how).[^stac_dcat_prov]

> [!CAUTION]
> Any feature proposal that shortcuts the pipeline (for example, “inject data directly into the UI”) is considered flawed unless rigorously justified.[^kfm_pipeline_order]

### 3) Run Focus Mode AI with a local model (Ollama)

<details>
<summary><b>Install + run Ollama (example)</b></summary>

```bash
# Linux install (per project guide)
curl -fsSL https://ollama.com/install.sh | sh

# pull + run a model
ollama pull llama3.2
ollama run llama3.2

# server mode (optional)
ollama serve
```

</details>

Focus Mode’s governance layer still applies when running local inference: responses are expected to be sourced, policy-checked, and logged.[^focus_mode][^ollama_install]

### 4) Build a “story node” (narrative + choreography)

A Story Node is typically:

- a **Markdown narrative** (with citations), plus  
- a **JSON “choreography” script** describing map state changes (center, zoom, layers, time filters, etc.).[^story_nodes]

KFM treats story contributions as reviewable, first-class artifacts; stories should be vetted for accuracy, citations, and sensitivity concerns.[^story_nodes]

---

## 🏗️ Architecture at a glance

### Data + map lifecycle (mental model)

```mermaid
flowchart LR
  A[📥 Raw evidence\n(data/raw)] --> B[🧼 Pipelines\n(pipelines/*)]
  B --> C[📦 Processed artifacts\n(data/processed)]
  C --> D[🗂️ Metadata & catalogs\nSTAC / DCAT\n(data/stac, data/catalog)]
  C --> E[🧾 Provenance logs\nPROV\n(data/prov)]
  D --> F[(🗄️ Datastores\nPostGIS / Neo4j)]
  F --> G[🔌 API\nFastAPI]
  G --> H[🗺️ UI\nReact + MapLibre\n(+ Cesium optional)]
  G --> I[🤖 Focus Mode\n(governed AI)]
  H --> J[📖 Story Nodes\n(docs/stories/*)]
```

The “pipeline → catalog → database → API → UI” model is explicit, and provenance-first is treated as a core invariant.[^kfm_system][^provenance_first]

---

## 📦 Repo layout

KFM uses a monorepo approach where **code + data** live together so that dataset changes can be reviewed and versioned like code.[^repo_versioning]

### Recommended layout (canonical targets)

```text
📦 Kansas-Frontier-Matrix/
├─ 🧩 .github/                 # Templates, workflows, automation (this folder) 🛠️
├─ 🧠 src/
│  ├─ server/                  # Backend API (FastAPI)  ← legacy: api/[^repo_layout]
│  └─ web/                     # Frontend UI (React)   ← legacy: web/[^repo_layout]
├─ 🧰 pipelines/                # ETL + validation + exporters
├─ 🗃️ data/
│  ├─ 📥 raw/                  # Immutable inputs (as obtained)
│  ├─ 🧪 work/                 # Scratch/intermediate artifacts
│  ├─ 🧼 processed/             # Cleaned/normalized outputs (serveable)
│  ├─ 🗂️ stac/
│  │  ├─ collections/          # STAC Collections
│  │  └─ items/                # STAC Items
│  ├─ 🧾 catalog/
│  │  └─ dcat/                 # DCAT dataset records
│  └─ 🧾 prov/                 # PROV lineage bundles
├─ 📚 docs/                    # Architecture, governance, stories, guides
├─ 🛡️ policy/                  # Governance rules (e.g., OPA/Rego policies)
├─ ⚙️ ops/                      # Deployment/ops scripts (optional)
└─ 📌 CITATION.cff             # How to cite the repo/version (recommended)[^repo_versioning]
```

> [!NOTE]
> You may still see legacy folder names (`api/`, `web/`) while converging toward `src/server/` + `src/web/`.[^repo_layout]

---

## 🧩 The `.github/` folder: what should live in `.github/`?

GitHub treats `.github/` as a special “repo hygiene + automation” directory. In KFM’s blueprint, `.github/` is explicitly part of the repo structure used for CI/CD workflows and community health files.[^github_dir]

### ✅ Baseline (what you already have)

From your current `.github/` structure (per screenshot), these are solid foundations:

- `ISSUE_TEMPLATE/` (issue templates)
- `actions/` (custom actions)
- `workflows/` (CI/CD workflows)
- `CODEOWNERS`
- `PULL_REQUEST_TEMPLATE.md`
- `README.md` (this file)
- `SECURITY.md`
- `dependabot.yml`
- `release-drafter.yml`

### ⭐ Recommended `.github/` tree (KFM-friendly)

```text
.github/
├─ 📌 README.md                        # What this folder does + how to use it
├─ 👥 CODEOWNERS                       # Required reviewers for sensitive areas
├─ 🔐 SECURITY.md                      # Security policy + reporting
├─ 🔁 dependabot.yml                   # Dependency update automation
├─ 🧾 release-drafter.yml              # Release notes automation
├─ 💬 PULL_REQUEST_TEMPLATE.md         # PR checklist + required artifacts
│
├─ 🧰 actions/                         # Reusable composite actions
│  ├─ setup-python/                    # e.g., cache deps, install, lint
│  ├─ validate-metadata/               # STAC/DCAT/PROV schema checks
│  └─ ...                              # keep small + reusable
│
├─ 🧵 workflows/                       # CI/CD (the “fail-closed” gate) 🛡️
│  ├─ ci.yml                           # tests/lint for api + web
│  ├─ data-contract.yml                # validate STAC/DCAT/PROV + provenance
│  ├─ docs.yml                         # markdown lint, link check, spell (optional)
│  ├─ security.yml                     # CodeQL / dependency scanning (optional)
│  ├─ docker.yml                       # build images, smoke tests (optional)
│  └─ release.yml                      # tag/release automation (optional)
│
└─ 🧷 ISSUE_TEMPLATE/
   ├─ bug_report.yml                   # bugs
   ├─ feature_request.yml              # features
   ├─ dataset_request.yml              # data additions (raw ➜ processed ➜ metadata)
   ├─ story_node.yml                   # narrative/story contributions
   ├─ governance_question.yml          # policy + sensitivity questions
   └─ config.yml                       # template chooser config
```

### 🧠 Why KFM cares so much about `.github/workflows`

KFM’s governance model is designed to **block non-compliant merges** (ex: missing license/metadata) — this is how “fail closed” becomes real in day-to-day collaboration.[^fail_closed]

Docs and dataset contributions benefit from “Definition of Done” gates and CI checks that keep templates + requirements consistent across the repo.[^doc_dod]

---

## 🧭 Cartography, coordinates, and “don’t lie with maps”

### Minimum map essentials (UI + exports)

When presenting a map (especially in stories), include:

- Title / explanatory text  
- Legend  
- Scale (scale bar)  
- Direction indicator (north arrow / compass rose)  
- Projection / coordinate system (CRS)  
- Sources & credits (data attribution + cartographic authorship)[^map_design]

### Metadata standards & interoperability

Dependable GIS datasets carry explicit metadata (identification, quality, spatial reference, distribution/use policy, temporal info, and citation guidance). Standards improve interoperability, and copyright typically protects the *representation* of facts—not the underlying data/facts.[^metadata]

### Grid reading conventions (field + GIS sanity)

When reading grid coordinates (e.g., MGRS/UTM grids): **read to the RIGHT (easting) and then UP (northing)**.[^grid_reading]

> [!CAUTION]
> Many spatial operations (distance/area) require projected coordinates in meters; working in lat/long degrees can break assumptions.[^projection_meters]

---

## 🧊 3D / 4D GIS and time

KFM’s design supports time-aware and 3D-aware narratives. A multi-temporal approach is central when monitoring/representing change across time, and multi-resolution perspectives matter as data fidelity varies across sources.[^arch3d_time][^arch3d_resolution]

---

## 📊 Analytics and QA

Exploratory analysis relies heavily on graphics to discover structure, pattern, and relationships in data.[^r_eda]

---

## 🤖 Focus Mode AI: local-first, but governed

Focus Mode is designed as a governed workflow: it is expected to provide **citations**, apply a **policy engine**, and use only approved tools/paths for retrieving information.[^focus_mode]

---

## 🧼 Data quality, validation, and “messy data reality”

Incorrect/inconsistent data can distort analysis—cleaning and preparation are first-class work in KFM pipelines and review culture.[^data_quality]

---

## 🤝 Contributing

### How to contribute effectively

- **Document-first:** treat metadata + provenance as part of the deliverable, not a “nice-to-have.”[^stac_dcat_prov]
- **Reproducible methods:** treat pipelines like experiments (inputs, method, outputs, traceability).[^master_coder]
- **Keep docs synced:** update docs/templates in the same PR when behavior or requirements change.[^doc_dod]

### PR checklist (suggested)

- [ ] Data placed under `data/raw/<domain>/...` with source notes (license + provenance)
- [ ] Pipeline produces `data/processed/...` outputs[^kfm_pipeline_order]
- [ ] STAC/DCAT/PROV artifacts generated and linked[^stac_dcat_prov]
- [ ] Story/map content includes citations + credits + CRS[^map_design]
- [ ] Tests / validations updated (or added) where applicable

### Sensitive / culturally restricted data 🪶

If a dataset/story involves sensitive locations or culturally restricted knowledge, consider redaction/aggregation and label sensitivity explicitly; KFM’s governance approach includes CARE-oriented handling.[^kfm_system][^doc_dod]

---

## 📚 Project library

These files actively inform KFM’s architecture, implementation patterns, and writing standards:

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint** (architecture + governance + pipelines + UI + AI)[^kfm_system]
- **MARKDOWN_GUIDE_v13** (canonical data/metadata layout + STAC/DCAT/PROV alignment policy)[^stac_dcat_prov][^repo_layout]
- **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design** (exports, tiles, KML/KMZ, time-aware UI)[^exports_formats]
- **Comprehensive Guide to Ollama** (local LLM workflow + install/run/serve commands)[^ollama_install]
- **Making Maps: A Visual Guide to Map Design for GIS** (cartographic essentials, metadata/copyright)[^map_design][^metadata]
- **Map Reading & Land Navigation** (grid reading conventions)[^grid_reading]
- **Archaeological 3D GIS** (multi-temporal + multi-resolution thinking in 3D/4D GIS)[^arch3d_time][^arch3d_resolution]
- **Graphical Data Analysis with R** (EDA mindset)[^r_eda]

> [!TIP]
> Put these under something like `docs/library/` in-repo so dataset cards can link to exact “house style” references. 📚✨

---

## 📜 Notice & licensing

- Respect source licensing and attribution.
- The *data/facts* can be reusable even when a *map’s representation* is copyrighted—document both carefully.[^metadata]
- See `LICENSE` for code licensing (and dataset cards for data licensing).

---

## 🧾 Sources (footnotes)

[^kfm_system]: KFM is defined as a provenance-first geospatial knowledge platform and explicitly described as a “pipeline–catalog–database–API–UI system,” with governance mediation between UI and databases (and FAIR/CARE emphasis). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^kfm_pipeline_order]: KFM’s pipeline order is treated as canonical (“Raw → Processed → Catalog/Prov → Database → API → UI”), and shortcuts are considered flawed unless justified. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^fail_closed]: “Fail closed” governance: policy/check failures block actions (including CI failures preventing merges for missing license/metadata). [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^provenance_first]: “Provenance First” is stated as an invariant: every dataset must have provenance + descriptive metadata; AI answers and stories attach citations (no black-box outputs). [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^stac_dcat_prov]: STAC/DCAT/PROV alignment policy: every dataset/evidence artifact must include STAC Collection/Items, a DCAT entry, and a PROV bundle; CI validates against profiles and expects cross-linking across layers. [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^repo_versioning]: KFM treats the Git repo as a source of truth for code + data; commit history versions processed/catalog/provenance, and `CITATION.cff` supports citing a specific repo version/snapshot. [oai_citation:5‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)
[^repo_layout]: Canonical layout targets include `data/catalog/dcat/`, `data/prov/`, and consolidating legacy `api/` + `web/` into `src/server/` + `src/web/` for long-term structure consistency. [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^tech_stack]: KFM stack references include FastAPI + GraphQL, PostGIS, Neo4j, MapLibre (2D), Cesium (3D), and governance via a policy engine (OPA/Rego). [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^docker_quickstart]: Docker Compose setup and default dev endpoints/ports (UI `:3000`, API `:8000` with `/docs`, Neo4j Browser `:7474`), plus port conflict guidance. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:9‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)
[^story_nodes]: Story Nodes are described as Markdown narratives paired with JSON choreography driving map state; story contributions should be reviewed for accuracy, citations, and sensitive content handling. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^focus_mode]: Focus Mode AI is designed to be policy-governed, to cite sources, and to use approved tools (with a policy engine gate). [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
[^ollama_install]: Ollama guide includes Linux install via `curl ... install.sh | sh`, plus `ollama serve` guidance. [oai_citation:13‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)
[^exports_formats]: KFM hub design calls for rasters saved as COGs, vectors as GeoJSON/Shapefiles, and generating tiles or KML/KMZ for interactive use (including Google Earth integration). [oai_citation:14‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) [oai_citation:15‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)
[^map_design]: Map design guidance includes showing direction (compass rose), scale (scale bar), supplying projection/coordinate system, and citing sources/credits (e.g., date and author). [oai_citation:16‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)
[^metadata]: GIS metadata categories (identification, quality, spatial reference, distribution/use policy, citation guidance, temporal info), FGDC mention, interoperability definition, and copyright note that protection applies to representation—not underlying facts/data. [oai_citation:17‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)
[^grid_reading]: Grid reading convention: “read to the RIGHT and then UP” (easting then northing). [oai_citation:18‡Map Reading & Land Navigation.pdf](sediment://file_00000000b14c7230b1b262ddd9df4e5d)
[^projection_meters]: Spatial operations require correct CRS/units; a projected CRS in meters is often needed, while geographic CRS uses degrees (and degrees-based calculations can be invalid). [oai_citation:19‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) [oai_citation:20‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
[^arch3d_time]: Archaeological 3D GIS highlights “multitemporal approach” for monitoring/capturing changes over time in archaeological contexts (4D). [oai_citation:21‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](sediment://file_00000000ebac71f7ba1281d629a3ff9b)
[^arch3d_resolution]: Archaeological 3D GIS emphasizes multi-resolution perspectives and data fusion as source fidelity changes across space/time and technologies. [oai_citation:22‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
[^r_eda]: EDA framing: exploratory analysis “employs largely graphical methods … to discover the structure, pattern, relationship, and anomalies in the data.” [oai_citation:23‡graphical-data-analysis-with-r.pdf](sediment://file_00000000f0f471f7aa621700c1f24d08)
[^data_quality]: Data quality issues (incorrect/inconsistent data) can distort analysis and outcomes; quality must be managed explicitly. [oai_citation:24‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
[^master_coder]: Reproducibility mindset: treat workflows like experiments, control sources of variation, and keep results traceable/reproducible across runs and environments. [oai_citation:25‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
[^doc_dod]: Documentation governance: Definition of Done checklists, consistent templates, and CI/automation for Markdown quality and links are encouraged for repo health and contributor alignment. [oai_citation:26‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
[^github_dir]: The blueprint’s repository structure includes `.github/` for CI/CD workflows and other repo-level community/automation files. [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)