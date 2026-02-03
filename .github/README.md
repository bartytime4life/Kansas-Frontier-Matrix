<div align="center">

# 🌾 Kansas Frontier Matrix (KFM)
### 🗺️ Evidence-first “Living Atlas” of Kansas  
**Raw evidence ➜ governed datasets ➜ interactive maps/timelines ➜ citation-backed answers**

<!-- Badges (keep lightweight + stable) -->
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Governance](https://img.shields.io/badge/governance-fail--closed-critical)
![Provenance](https://img.shields.io/badge/evidence-STAC%20%2B%20DCAT%20%2B%20PROV-blue)
![Stack](https://img.shields.io/badge/stack-FastAPI%20%7C%20React%20%7C%20PostGIS%20%7C%20Neo4j%20%7C%20OPA%20%7C%20Ollama-informational)

</div>

---

## 🧭 Start Here

**KFM turns Kansas history + environment + infrastructure data into a governed, explorable knowledge system**—with the *“map behind the map”* always traceable.

### 🔗 Quick Navigation
- ✨ [What KFM is](#-what-kfm-is)
- 🧱 [Non‑negotiables](#-non-negotiables)
- 🏗️ [Architecture](#️-architecture-at-a-glance)
- 📦 [Repo layout](#-repo-layout)
- 🚀 [Quickstart](#-quickstart)
- 🧪 [Quality + governance gates](#-quality--governance-gates)
- 🤝 [Contributing](#-contributing)
- 🧠 [Focus Mode AI](#-focus-mode-ai)
- 📚 [Project library](#-project-library)

---

## ✨ What KFM is

KFM is a **pipeline → catalog → graph/DB → API → UI → narrative → AI** platform that transforms raw sources into **trustworthy, explorable** knowledge.

### ✅ What you get
- 🗺️ **2D/3D mapping** (web map + globe) with time-based exploration  
- 🕰️ **Timelines + Story Nodes** (narrative that moves the map)  
- 🧾 **Evidence-first outputs** (every layer/claim ties back to sources)  
- 🧠 **Focus Mode AI** (retrieval + citations + audit trail)

### 🚫 What KFM is not
- ❌ Not a “black-box” data portal  
- ❌ Not an ungoverned chatbot  
- ❌ Not a system where UI touches databases directly

> **Boundary rule:** the UI does **not** query PostGIS/Neo4j directly—**all access is mediated by the API** so governance can be enforced end-to-end.

---

## 🧱 Non-negotiables

These invariants are the “do not regress” rules that drive CI/CD, code review, and data governance:

1. **Truth Path is mandatory**  
   `Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI`  
2. **Provenance-first**  
   Nothing goes downstream without **STAC + DCAT + PROV** metadata.
3. **Fail-closed by default** 🔒  
   If a check is missing/uncertain, **block** until corrected.
4. **Classification propagation**  
   Outputs cannot be *less restricted* than inputs.
5. **Deterministic pipelines**  
   Idempotent, config-driven, logged, re-runnable.

> 🧠 Guiding ethos: **FAIR + CARE by design** (findable/reusable + respectful governance).

---

## 🏗️ Architecture at a glance

### 🧩 “Truth Path” flow
```mermaid
flowchart LR
  A[📥 Raw Sources\n(data/raw)] --> B[🏭 ETL Pipelines\n(pipelines/)]
  B --> C[🧼 Processed Outputs\n(data/processed)]
  C --> D[🏷️ Catalog Metadata\n(data/catalog: STAC/DCAT)]
  D --> E[🧾 Provenance Logs\n(data/provenance: PROV)]
  E --> F[🗃️ Runtime Stores\nPostGIS • Neo4j • Search • Object Storage]
  F --> G[🌐 Governed API\n(FastAPI/GraphQL + OPA gates)]
  G --> H[🗺️ Web UI\n(React + MapLibre/Cesium)]
  G --> I[🤖 Focus Mode AI\n(retrieval + citations)]
```

### 🧠 Clean layering (implementation tip)
- 🧱 **Domain logic stays pure**
- 🔌 Infra adapters (DBs/APIs) are swappable
- 🌐 The API is the enforcement layer (policies + contracts)

---

## 📦 Repo layout

Top-level (monorepo) structure — keep the iconography consistent 🧰:

```text
📦 Kansas-Frontier-Matrix/
├─ 🧠 api/                 # FastAPI backend (services, policy gates, adapters)
├─ 🖥️  web/                # React + TypeScript UI (MapLibre/Cesium + timelines)
├─ 🏭 pipelines/            # ETL + ingest + transforms (idempotent + logged)
├─ 🗃️  data/
│  ├─ 📥 raw/               # immutable source snapshots
│  ├─ 🧼 processed/         # cleaned, standardized, publishable outputs
│  ├─ 🏷️ catalog/           # STAC + DCAT metadata
│  └─ 🧾 provenance/        # W3C PROV lineage documents + run manifests
├─ 📚 docs/                 # architecture, standards, runbooks, Story Nodes
├─ 🧪 tests/                # contract + pipeline + governance tests
├─ 🧰 tools/                # validators, linters, helpers
└─ 🧩 .github/              # CI/CD, templates, governance workflows
```

---

## 🚀 Quickstart

### ✅ Recommended: Docker Compose
```bash
# from repo root
docker compose up --build
```

### 🔌 Typical local endpoints (adjust to your compose)
- 🖥️ Web UI: `http://localhost:3000`
- 🌐 API: `http://localhost:8000`
- 📜 OpenAPI docs: `http://localhost:8000/docs`
- 🧠 Neo4j browser: `http://localhost:7474`

> 🧯 If ports conflict, update mappings in `docker-compose.yml` and restart.

---

## 🧪 Quality + governance gates

KFM treats CI as **governance infrastructure**, not “just tests”.

### ✅ Examples of fail-closed checks
- 🏷️ **License + source manifest required** at ingestion
- 🧾 **STAC/DCAT/PROV required** to publish catalog artifacts
- 🔐 **OPA policy gates** for sensitive data + redaction rules
- 🤖 **AI output gate**: citations required, disallowed content blocked
- 🧬 **Provenance ledger**: append-only audit trail for pipeline runs + AI answers

> If a gate fails, the correct next step is **fix the metadata/policy**, not “work around it”.

---

## 🤝 Contributing

KFM contributions are intentionally:
- **Contracted** (schemas + templates first)
- **Evidence-first** (data + provenance before interpretation)

### 1) Add a dataset (Raw ➜ Work ➜ Processed ➜ Catalog ➜ Graph/DB)
**Required PR artifacts:**
- ✅ `data/processed/<domain>/...`
- ✅ `data/catalog/...` (STAC + DCAT)
- ✅ `data/provenance/...` (PROV lineage + manifests)
- ✅ `docs/data/<domain>/README.md` (sources, caveats, ETL steps)

**Anti-patterns to avoid:**
- ❌ “Inject directly into UI”
- ❌ “Skip catalogs/provenance”
- ❌ “Put interpretation before evidence”

### 2) Add a Story Node (narrative as governed data) 🧠
Story Nodes are Markdown documents that:
- 📌 include **provenance for every factual claim**
- 🧷 reference graph entities via stable identifiers
- 🧪 clearly separate **fact vs interpretation**

> Story Nodes should be *machine-ingestible* and *human-readable*.

### 3) Add an API capability 🌐
- Define contract first (OpenAPI/GraphQL)
- Add tests (contract + access policy expectations)
- Update docs + examples

### 4) Add a UI feature 🗺️
- UI features must **link back to provenance**
- Map layers must show **source + lineage** in legends/popovers
- Respect CARE constraints (avoid exposing sensitive coordinates)

---

## 🧠 Focus Mode AI

Focus Mode is **advisory-only** and **explainable by design**:

### ✅ What it should do
- Retrieve governed evidence (cataloged sources)
- Produce an answer with **clickable citations**
- Offer an “audit panel” (retrieved snippets + provenance metadata)
- Log model version + sources + policy decisions (append-only)

### 🚫 What it must not do
- Invent sources
- Bypass policy gates
- Access raw DBs/files directly (AI stays sandboxed behind the app)

> Default deployment favors **local models (Ollama)** to keep AI **auditable, reproducible, and controllable**.

---

## 🗺️ Design + cartography principles

KFM maps are not decoration—they’re **interfaces for evidence**.

Core UI/UX goals:
- 🧭 Clear hierarchy (what matters first, what’s supporting context)
- 🧩 Progressive disclosure (detail on demand)
- 🧾 Provenance always accessible (“map behind the map”)
- 🕰️ Temporal clarity (timelines that explain change, not just animate it)
- ♿ Accessibility (contrast, keyboard paths, readable typography)

---

## 📚 Project library

A curated “build shelf” for KFM work (engineering + GIS + design):

### 🧱 Architecture / governance / pipelines
- 📘 *KFM Comprehensive System Documentation*  
- 📘 *KFM Comprehensive Technical Blueprint*  
- 📗 *Unified Technical Blueprint & Supporting Ideas*  
- 📙 DevOps / CI / security references (Docker, pipelines, validation)

### 🗺️ GIS / cartography / spatial thinking
- 🗺️ *Making Maps* (visual map design)
- 🧭 *Mapping Urban Spaces*
- 🧱 *GIS Mapping + Topology*
- 🏺 *Archaeological 3D GIS* (3D reasoning patterns)

### 🧪 Analysis / modeling toolkits
- 🧮 R + graphical data analysis
- 🐍 Python + scientific tools (NumPy/SciPy/PyTorch)
- 📐 MATLAB engineering concepts

### 🖥️ Web + UI engineering
- 🌐 HTML/CSS foundations
- ⚛️ Node.js + front-end fundamentals

> 🧠 Tip: When you add a new subsystem, add at least one “library pointer” here so newcomers can onboard faster.

---

## 🧾 License & attribution

- Respect upstream dataset licenses and community governance constraints.
- If you publish derived layers, ensure **provenance is complete** and **classification rules propagate**.
- Prefer open formats (GeoJSON/GeoPackage/Parquet for vectors; COG/tiles for rasters).

---

## 🌾 Community

KFM is built for:
- 🎓 educators + researchers
- 🏛️ policy and planning
- 🧑‍🤝‍🧑 community storytellers
- 🧑‍💻 contributors who care about reproducibility

If you want to help, remember the prime directive:

> **Evidence first. Governance always. No bypasses.**
