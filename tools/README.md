# 🧰 Tools

![Status](https://img.shields.io/badge/status-prototype-orange)
![Governance](https://img.shields.io/badge/governance-fail--closed-critical)
![Provenance](https://img.shields.io/badge/provenance-W3C%20PROV-blue)
![Stack](https://img.shields.io/badge/runtime-Docker%20Compose-2496ED)
![Geo](https://img.shields.io/badge/geo-PostGIS%20%7C%20Neo4j-informational)
![AI](https://img.shields.io/badge/AI-Ollama%20(local%20LLM)-6E40C9)

Developer utilities & operational scripts for the **Kansas Frontier Matrix (KFM)** monorepo—built to keep **code + data + docs** reproducible, traceable, and governance-compliant. KFM’s monorepo approach intentionally keeps everything versioned together so lineage is auditable from Git history and structured provenance logs.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 Table of Contents

- [Why this folder exists](#-why-this-folder-exists)
- [Run tools the “KFM way”](#-run-tools-the-kfm-way)
- [What belongs in `tools/`](#-what-belongs-in-tools)
- [Core rules (non-negotiables)](#-core-rules-non-negotiables)
- [Suggested folder layout](#-suggested-folder-layout)
- [Tool playbooks](#-tool-playbooks)
  - [🗺️ Data & GIS](#️-data--gis)
  - [🧾 Catalog & Metadata](#-catalog--metadata)
  - [🧬 Provenance](#-provenance)
  - [🧠 AI / Focus Mode](#-ai--focus-mode)
  - [🛠️ Dev / Ops](#️-dev--ops)
- [Adding a new tool](#-adding-a-new-tool)
- [Troubleshooting](#-troubleshooting)
- [📚 Sources used to ground this README](#-sources-used-to-ground-this-readme)

---

## 🧩 Why this folder exists

KFM is organized as a **single monorepo** (“backend, frontend, data, and documentation under one roof”) so artifacts evolve in lockstep and remain traceable.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
That’s powerful… but it also means we need **repeatable utilities** to keep the system consistent:

- 🔁 **Repeatable ingestion & transformations** supporting KFM’s **plugin-based ETL** model (ingest → transform → load).  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- 🧬 **Provenance-first workflows** so every dataset and important derived artifact has lineage.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- ✅ **Fail-closed governance** so missing metadata/license/provenance causes a *hard stop* (locally or in CI).  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🚀 Run tools the “KFM way”

### Preferred execution environment: Docker Compose ✅

KFM’s dev stack is designed around Docker Compose services (PostGIS, Neo4j, API, Web, etc.).  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
When you run scripts inside the API container, you inherit the same dependencies and mounted data volumes the system uses (including geospatial deps like GDAL).  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

```bash
# From repo root:
docker-compose up --build

# Run a one-off pipeline (example pattern):
docker-compose exec api python pipelines/my_pipeline.py
```
 [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### CLI-style tasks

The blueprint anticipates CLI utilities (e.g., a `manage.py`-style script or `api/scripts/` entrypoints) for tasks like creating users, seeding data, or reindexing.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

```bash
# Example pattern (if present in repo):
docker-compose exec api python manage.py reindex
docker-compose exec api python scripts/init_sample_data.py
```
 [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> 💡 **Rule of thumb:** if a tool needs PostGIS/Neo4j/GDAL/etc., run it via `docker-compose exec api …` so behavior matches production-like assumptions.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📦 What belongs in `tools/`

`tools/` is for **cross-cutting utilities** that don’t belong to:
- `api/` (runtime application code),
- `pipelines/` (dataset ETL plugins / ingestion jobs),
- `web/` (frontend),
- `docs/` (documentation source).

Think of `tools/` as the **workbench** 🔧:
- Validators
- Scaffolding generators
- Converters
- Auditors (metadata, license, provenance, schema)
- Index rebuilders (search/graph/embeddings)
- “Doctor” scripts (environment sanity checks)

---

## 🧱 Core rules (non-negotiables)

### 1) Provenance First 🧬
KFM’s invariant: **nothing enters the system without provenance** (and AI/story outputs must carry citations too).  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 2) Fail closed 🚫
If a dataset/output is missing required metadata, license, provenance, or schema integrity, the tool should **stop** and explain what to fix. This aligns with KFM’s “governance by default” / fail-closed posture.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3) Make provenance inspectable 🔍
KFM provenance logs are intended to answer: **“How was this data produced?”**—including entities (inputs/outputs), activities (pipeline run), and agents (person + software).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 4) Respect metadata + licensing 🧾
GIS work requires reliable metadata (ID, quality, spatial reference/projection, distribution, citation info, temporal info, etc.) and careful handling of copyright/licensing.  [oai_citation:14‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) [oai_citation:15‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

### 5) Align with the pipeline plugin model 🧩
KFM’s ETL is described as plugin-based, with a common interface (`ingest`, `transform`, `load`) and an orchestrator that discovers plugins based on config like `pipeline.yml`. Tools should *support* that model (scaffold, validate, lint), not bypass it.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🗂️ Suggested folder layout

> This is a recommended structure. Create folders as you implement tools.

```text
🧰 tools/
├─ 📘 README.md                # you are here
├─ 🐍 kfm/                     # (recommended) Python package for a unified CLI
│  ├─ __init__.py
│  ├─ __main__.py              # `python -m tools.kfm ...`
│  ├─ cli.py                   # Typer/Click entrypoint (recommended)
│  └─ commands/
│     ├─ data.py               # GIS/data helpers
│     ├─ catalog.py            # STAC/DCAT/metadata validators
│     ├─ prov.py               # provenance generators/linters
│     ├─ ai.py                 # focus-mode smoke tests / embedding jobs
│     └─ doctor.py             # environment checks
├─ 🧪 fixtures/                # sample inputs for tests (small + public)
└─ 🧾 templates/               # scaffold templates (pipeline/plugin/metadata)
```

---

## 🧠 Tool playbooks

### 🗺️ Data & GIS

**Typical jobs**
- Convert/reproject, simplify, validate geometry
- Validate outputs before they land in `data/processed/`

**Why this matters**
- CI is expected to validate basic GeoJSON sanity (valid JSON, coordinates make sense).  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Geometry validity checks (e.g., PostGIS `ST_IsValid`) are a standard quality gate.  [oai_citation:18‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

<details>
<summary><b>✅ Suggested commands (design targets)</b></summary>

```bash
# Validate geometry (design target)
python -m tools.kfm data validate-geoms --dsn "$POSTGIS_DSN"

# Reproject GeoJSON (design target)
python -m tools.kfm data reproject --in data/raw/x.geojson --out data/processed/x.geojson --to-epsg 4326
```

</details>

---

### 🧾 Catalog & Metadata

**Typical jobs**
- Ensure every processed dataset has:
  - catalog entry (`data/catalog/...`)
  - provenance entry (`data/provenance/...`)
  - license + citation + spatial reference info

**Why this matters**
CI is expected to check that `data/processed` outputs have corresponding entries in **`data/catalog`** and **`data/provenance`**.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

### 🧬 Provenance

**What “good provenance” looks like in KFM**
A provenance file should document:
- **Entities:** input raw files (with source pointers/checksums) + output file  
- **Activity:** the process (pipeline/script name), timestamp, parameters  
- **Agents:** the person + the software agent/version  
 [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> 🚩 If something doesn’t have provenance, it’s considered a red flag in KFM.  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

### 🧠 AI / Focus Mode

KFM’s Focus Mode is designed around a **local LLM** with **knowledge-grounded** responses, using approved tools/APIs and requiring citations for factual statements. It also records reasoning traces in PROV logs for auditability.  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Where tools help**
- Smoke tests for AI endpoints
- Local model setup checks (Ollama reachable)
- Rebuild semantic indexes / embeddings (if used)

**Ollama notes**
Ollama is described as an open-source platform for running models locally; it runs a local server (`ollama serve`) and exposes a REST API.  [oai_citation:23‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)  
It also exposes an OpenAI-compatible API, typically on `http://localhost:11434`.  [oai_citation:24‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)

<details>
<summary><b>🧪 Suggested “AI Doctor” checks (design targets)</b></summary>

```bash
# 1) Is Ollama up?
curl -s http://localhost:11434/api/tags | head

# 2) Can the API container reach Ollama?
docker-compose exec api python -c "import os,requests; print(requests.get(os.getenv('AI_BACKEND_URL','http://host.docker.internal:11434')+'/api/tags').status_code)"
```

</details>

---

### 🛠️ Dev / Ops

**Typical jobs**
- Environment checks
- DB connectivity tests
- Reindex tasks / migrations / seed sample data

**Testing**
CI is expected to run backend tests (e.g., `pytest`), and local dev should mirror that workflow.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ➕ Adding a new tool

### ✅ Checklist
- [ ] Name is clear and action-oriented (e.g., `validate_catalog`, `prov_lint`, `reproject_geojson`)
- [ ] Writes outputs only to intended locations (usually `data/processed`, `data/catalog`, `data/provenance`)
- [ ] Generates/updates provenance when producing derived artifacts (Entities/Activity/Agents)  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Fails closed on missing metadata/license/provenance/schema issues  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Includes a small test/fixture (public + tiny)
- [ ] Adds a short entry to this README under the relevant playbook

### 🧩 Prefer supporting pipelines, not bypassing them
If you’re doing ingestion work, consider whether it belongs as a **pipeline plugin** (ingest/transform/load), with tools acting as scaffolding/validation around it.  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🩺 Troubleshooting

<details>
<summary><b>🐳 Docker/Compose issues</b></summary>

- Port conflicts (5432/7474/8000/3000): adjust mappings or stop local services.  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Volume permissions: if the API can’t write to `data/`, fix host permissions or container user mapping.  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- DB readiness: if API starts before DB/graph are ready, check logs and restart stack.  [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

</details>

---

## 📚 Sources used to ground this README

- **KFM Monorepo philosophy & architecture**  [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **Fail-closed governance & invariants**  [oai_citation:33‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **Pipeline plugin model (ingest/transform/load + orchestrator discovery)**  [oai_citation:35‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **Provenance folder expectations (Entities/Activity/Agents)**  [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **CI checks for processed/catalog/provenance alignment**  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **Focus Mode AI governance, citations, and PROV audit traces**  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **Ollama local execution + server/API expectations**  [oai_citation:39‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi) [oai_citation:40‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)
- **Metadata + licensing essentials (GIS)**  [oai_citation:41‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) [oai_citation:42‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)
- **Example geometry validity checks (PostGIS)**  [oai_citation:43‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)