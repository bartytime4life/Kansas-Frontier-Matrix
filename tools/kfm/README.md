# 🧰 KFM Toolbelt (`tools/kfm/`)

<p align="center">
  <img alt="KFM Toolbelt" src="https://img.shields.io/badge/KFM-tools%2Fkfm-2b6cb0?style=for-the-badge" />
  <img alt="Provenance First" src="https://img.shields.io/badge/Provenance-first-16a34a?style=for-the-badge" />
  <img alt="Fail Closed" src="https://img.shields.io/badge/Governance-fail%20closed-f97316?style=for-the-badge" />
  <img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%20%2B%20CARE-by%20design-a855f7?style=for-the-badge" />
</p>

> **“The map behind the map.”** Every layer, dataset, story, and even AI-generated output is expected to be traceable back to original sources.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🎯 What belongs in `tools/kfm/`

`tools/kfm/` is the **developer + ops toolbelt** for the Kansas Frontier Matrix (KFM): scripts and CLIs that keep the system **reproducible**, **auditable**, and **policy-compliant** across the full stack.

KFM is designed as a **pipeline → catalog → database → API → UI** system that transforms raw files into trustworthy, explorable knowledge.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ✅ Typical responsibilities

- 🏗️ **Orchestrate pipelines** (run ETL plugins/modules in the right order)
- 🧾 **Generate + validate metadata** (STAC/DCAT + required dataset descriptors)
- 🧬 **Generate + validate provenance** (W3C PROV logs + lineage checks)
- 🧪 **Run quality gates** (schema checks, geometry checks, license checks → “fail closed”)
- 🧰 **Dev helpers** (docker-compose wrappers, smoke tests, log tailing)
- 🗃️ **Ops helpers** (reindex search/graph, seed initial data, export snapshots)

---

## 🧠 Mental model: the canonical data path

KFM treats this order as **non-negotiable**:

**Raw → Processed → Catalog/Prov → Database → API → UI**  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### Why this matters
- “Shortcuts” (injecting data directly into UI/DB or skipping provenance/metadata) are considered **flawed** unless proven otherwise.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- Governance is designed to **fail closed**: if policy/metadata/license checks fail, the action is blocked (e.g., CI rejects merges).  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧩 Where `tools/kfm` sits in the monorepo

```text
📦 Kansas-Frontier-Matrix/
├── api/                     # FastAPI backend
├── web/                     # React + TypeScript frontend
├── pipelines/               # ETL pipelines + simulations
├── data/
│   ├── raw/                 # Immutable source snapshots
│   ├── processed/           # Cleaned/standardized outputs
│   ├── catalog/             # STAC / DCAT metadata
│   └── provenance/          # W3C PROV lineage logs
├── policy/                  # Governance policies (e.g., OPA/Rego)
└── tools/
    └── kfm/                 # 👈 this directory
        └── README.md
```  
 [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🚀 Quickstart: “How do I poke the system?”

> This project expects you to work through the API layer (and its governance), not around it.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 1) Start the dev stack (Docker Compose)
```bash
docker-compose up
```

**Common pitfalls** (ports, resources, volumes):
- Port conflicts (e.g., `5432`, `7474`, `8000/3000`)
- Docker memory limits during large dataset loads
- Volume permissions / mounts not applying as expected  
 [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 2) Explore the API (Swagger)
With the environment up, open:
- `http://localhost:8000/docs` (Swagger UI)  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3) Use “CLI-ish” commands via containers
The blueprint suggests the repository may provide CLI utilities like `manage.py`, or scripts under `api/scripts/`. Typical patterns look like:

```bash
docker-compose exec api python manage.py [command]
```

Or drop into the container and run ad-hoc code:

```bash
docker-compose exec api bash
python -c "print('hello from api container')"
```

 [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🛠️ Tooling interface (recommended target)

To keep the developer experience consistent, aim for a single entrypoint:

- `kfm` (or `./kfm`) with subcommands

### Suggested command map 🧭
> These are *recommended conventions* for what should live here, aligned with the blueprint’s operational guidance.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

```text
kfm dev up|down|logs|shell
kfm api open-docs
kfm pipeline run <plugin> [--since DATE] [--dry-run]
kfm data validate <path-or-dataset-id>
kfm catalog build <dataset-id>
kfm prov init <dataset-id>
kfm db load <dataset-id>
kfm search reindex
kfm export snapshot [--out DIR]
```

### Command behavior principles ✅
- ♻️ **Idempotent**: safe to run twice (no double-loading unless intended)
- 🧾 **Auditable**: produce structured logs + provenance artifacts
- 🧪 **Fail closed**: validation errors stop execution (no partial “success”)
- 🧷 **Deterministic**: same inputs → same outputs (or explicitly versioned outputs)

---

## 🧬 Dataset contribution workflow (the “happy path”)

### 0) Before you begin
KFM is intentionally strict:
- Nothing enters without provenance + metadata
- CI is expected to reject undocumented / unlicensed additions  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 1) Add raw source snapshot
- Place unmodified source data in `data/raw/...` (treat as immutable)  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 2) Run or implement the pipeline step
- Pipelines should produce:
  - `data/processed/...` outputs  
  - `data/catalog/...` metadata (STAC/DCAT)  
  - `data/provenance/...` lineage (W3C PROV)  
 [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3) Validate outputs
Your toolbelt should validate (at minimum):
- ✅ GeoJSON/JSON validity (and basic geometry sanity)
- ✅ Metadata exists + is complete (STAC/DCAT)
- ✅ Provenance exists + links inputs → scripts → outputs (PROV)
- ✅ License/rights metadata present (fail if missing)  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 4) Commit & PR
- CI checks should enforce catalog/provenance presence and consistency  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🤖 Tooling + AI “Focus Mode” (why this folder matters)

KFM’s AI assistant is **not** meant to be an ungoverned chatbot. It is constrained by policy and designed to return answers with citations and traceability.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

The blueprint describes an approach where the AI can call safe tools (search/query) and “show its work,” with traces recorded as part of provenance logs.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Implication for `tools/kfm/`:**
- Tools here should be safe to call from agent workflows (bounded, logged, permission-aware).

---

## 🧯 Troubleshooting checklist

- 🔌 **Port conflicts**: change compose port mappings or stop local services (Postgres on `5432`, etc.)  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- 🐳 **Resource limits**: increase Docker memory if containers are killed/slow  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- 📁 **Volume permissions**: ensure mounted directories are writable from containers  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- 🔁 **Rebuild when deps change**:
  ```bash
  docker-compose up --build
  # or
  docker-compose build
  ```
   [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🔗 Helpful links (inside this repo)

- `../../docs/` → architecture & narrative docs  
- `../../pipelines/` → ingestion + transformation modules  
- `../../data/catalog/` → STAC/DCAT metadata  
- `../../data/provenance/` → W3C PROV lineage logs  
- `../../policy/` → governance rules (“fail closed”)  

(These paths align to the blueprint’s repository structure discussion.)  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📚 Background reading (project library)

> These PDFs are part of the project’s reference stack and inform design choices in mapping, ethics, time-oriented visualization, and scalable systems.

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint**  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- **Introduction to Digital Humanism**  [oai_citation:26‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)  
- **Visualization of Time-Oriented Data**  [oai_citation:27‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)  
- **Scalable Data Management for Future Hardware**  [oai_citation:28‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)  

---

## 🗺️ Roadmap for `tools/kfm/`

- [ ] Bootstrap `kfm` CLI scaffold (Typer/Click/etc.)
- [ ] `kfm data validate` (schema + license + geometry)
- [ ] `kfm catalog build` (STAC/DCAT templates + generation)
- [ ] `kfm prov init` (W3C PROV templates + run stamping)
- [ ] `kfm pipeline run` (plugin discovery + orchestrated runs)
- [ ] `kfm db load` (safe loaders; no direct UI → DB)
- [ ] `kfm search reindex` (graph/search refresh hooks)
- [ ] Agent-safe wrappers for Focus Mode tool calls (bounded + logged)

---

## 🤝 Contributing guidelines for tool scripts

- ✅ Keep tooling **thin**: orchestrate + validate; don’t embed business logic that belongs in `pipelines/` or `api/`.
- ✅ Prefer **explicit inputs/outputs**: file paths, dataset ids, and version stamps.
- ✅ Always produce **machine-readable logs** (JSON lines recommended).
- ✅ If it’s not reproducible, it doesn’t ship. 🔒

---