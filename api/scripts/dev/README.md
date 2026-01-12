# 🛠️ `api/scripts/dev` — Dev Scripts for the API (Local-Only)

![Scope](https://img.shields.io/badge/scope-dev%20only-orange)
![Python](https://img.shields.io/badge/python-%E2%89%A53.11-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white)
![PostGIS](https://img.shields.io/badge/PostGIS-PostgreSQL-336791?logo=postgresql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-graph-018BFF?logo=neo4j&logoColor=white)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1)

> ⚠️ **Danger (by design):** These scripts may drop/rebuild local databases, wipe dev volumes, and regenerate derived artifacts.  
> **Never** point them at production credentials, production buckets, or shared environments.

---

## 🎯 What this folder is for

This directory contains **developer-only “thin wrapper” scripts** that make it painless to:

- 🚀 Stand up / tear down the **local KFM stack** (DBs + services)
- 🧱 Initialize schemas, extensions (e.g., PostGIS), and run migrations
- 🌱 Seed **small, deterministic** demo datasets for UI + API smoke tests
- 🛰️ Run a local ingest loop that turns “raw” → “processed” → “catalogs”
- 🧾 Generate + validate **STAC / DCAT / PROV** artifacts
- 🕸️ Export / import graph fixtures (CSV/Cypher) and rebuild Neo4j
- 🔎 Run “doctor” checks and smoke tests (ports, credentials, healthchecks)

The **philosophy** is “**contract-first + provenance-first**”: dev scripts should be repeatable, transparent, and always leave behind enough artifacts to explain *what happened* and *why*.

---

## 🧭 Quick Links (Project Canon)

> These are the “source-of-truth” docs for how the system is meant to work end-to-end.

- 📘 `docs/MASTER_GUIDE_v13.md`
- 🧱 `docs/KFM_REDESIGN_BLUEPRINT_v13.md`
- 🧠 `docs/KFM_VISION_FULL_ARCHITECTURE_v13.md`
- 🗂️ `docs/KFM_REPO_STRUCTURE_STANDARD_v13.md`
- ✍️ `docs/KFM_MARKDOWN_WORK_PROTOCOL_v13.md`
- 🏛️ `docs/ROOT_GOVERNANCE_v13.md`
- ✅ `docs/REVIEW_GATES_v13.md`

---

## ✅ Golden Rules (Non‑Negotiables)

### 1) Dev scripts must be **safe by default**
- Default env file should be `.env.dev` or `dev.env` (never `.env.prod`)
- Require explicit flags for destructive operations (`--yes`, `--i-understand`, etc.)

### 2) Dev scripts must be **idempotent**
Running a script twice should either:
- do nothing the second time, or
- converge to the same output without creating duplicates

### 3) Dev scripts must be **deterministic**
- Stable seeds (where randomness exists)
- Stable file naming (hash / timestamp + run-id)
- Stable outputs for the same inputs (or clearly recorded reasons why not)

### 4) Dev scripts must be **provenance-first**
Every meaningful run should write:
- a config snapshot (inputs, versions, flags)
- a run manifest (what was produced)
- links to generated STAC/DCAT/PROV artifacts

### 5) Dev scripts are **wrappers**, not business logic
Business logic lives in canonical modules (typically under `src/` and `tools/`).
Dev scripts should call into those modules rather than copy/paste pipeline code.

---

## 🧰 Expected Local Stack

Most dev workflows assume a local stack that looks like:

- 🐘 **PostgreSQL + PostGIS** (canonical spatial store / SQL)
- 🕸️ **Neo4j** (property graph for relationship + inference navigation)
- 🗃️ **Object storage** (local filesystem or S3-compatible like MinIO) for rasters/tiles/exports
- 🧪 Optional “helpers” (depending on your branch): Redis, search, metrics

> If your branch uses a different set of services, document it in the **Script Catalog** below.

---

## 🚀 Quickstart (Happy Path)

### 0) Always run from repo root 📍
This avoids “it worked on my machine” path issues.

```bash
cd "$(git rev-parse --show-toplevel)"
```

### 1) Create a dev env file
```bash
cp .env.example .env.dev
```

Recommended env vars (names may differ by implementation; align with your API config):

```dotenv
# --- Core environment ---
KFM_ENV=dev
LOG_LEVEL=info

# --- PostGIS / Postgres ---
DATABASE_URL=postgresql+psycopg://kfm:kfm@localhost:5432/kfm

# --- Neo4j ---
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=please-change-me

# --- Storage (optional) ---
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
S3_BUCKET=kfm-dev
```

### 2) Start infra (Docker Compose)
```bash
docker compose up -d
docker compose ps
```

### 3) Bootstrap dev (schema + seed + minimal catalogs)
```bash
bash api/scripts/dev/bootstrap.sh --env-file .env.dev
```

### 4) Run the API (example)
> The exact command depends on your API entrypoint. Keep this section updated as the API evolves.

```bash
# Example (FastAPI)
uvicorn src.server.main:app --reload --port 8000
```

### 5) Smoke test
```bash
bash api/scripts/dev/smoke_test.sh --base-url http://localhost:8000
```

---

## 🗂️ Script Catalog (Spec + Living Inventory)

> ✅ If a script exists, keep the row accurate.  
> 🧩 If a script doesn’t exist yet, treat the row as the **backlog/spec** for what we want.

| Script | Purpose | Safe? | Typical Outputs |
|---|---|---:|---|
| `doctor.(sh|py)` | Checks dev prerequisites (Docker, ports, env vars, DB connectivity) | ✅ | Console report, optional JSON report |
| `up.(sh)` | Starts dev services (compose) | ✅ | Running containers |
| `down.(sh)` | Stops dev services (compose) | ✅ | Stopped containers |
| `reset.(sh)` | **Destructive**: drops volumes, clears derived data | ❌ | Clean slate |
| `bootstrap.(sh|py)` | One-shot local bootstrap: migrations + seed + sample catalogs | ⚠️ | DB schema, seed rows, `data/*` artifacts |
| `migrate.(sh|py)` | Runs migrations (forward only) | ✅ | DB migrated |
| `seed_minimal.(py)` | Inserts minimal reference data (roles, sample layers, etc.) | ✅ | DB seeded |
| `ingest_sample.(py)` | Runs ingest on a known tiny dataset bundle | ✅ | `data/.../processed`, catalogs |
| `build_stac.(py)` | Builds STAC Collections/Items for processed artifacts | ✅ | `data/stac/**` |
| `build_dcat.(py)` | Builds DCAT exports for discoverability | ✅ | `data/catalog/dcat/**` |
| `build_prov.(py)` | Builds PROV bundles per run/dataset | ✅ | `data/prov/**` |
| `validate_catalogs.(py)` | Validates STAC/DCAT/PROV against `schemas/` + profiles | ✅ | Validation report |
| `export_graph.(py)` | Exports graph fixtures (CSV/Cypher) | ✅ | `data/graph/csv/**`, `data/graph/cypher/**` |
| `import_graph.(py)` | Imports graph fixtures into Neo4j + applies constraints | ⚠️ | Neo4j populated |
| `smoke_test.(sh|py)` | Hits key API endpoints; confirms contracts/health | ✅ | Report + exit code |

---

## 🧾 Outputs & Where They Go (Project Standard)

The repo’s canonical layout assumes artifacts land in predictable places:

- 📦 `data/<domain>/raw/` — **source snapshots** (rarely committed; license-aware)
- 🧼 `data/<domain>/processed/` — normalized outputs ready for cataloging
- 🛰️ `data/stac/collections/` + `data/stac/items/` — STAC artifacts
- 🗃️ `data/catalog/dcat/` — DCAT exports
- 🧬 `data/prov/` — provenance bundles (PROV)
- 🕸️ `data/graph/csv/` + `data/graph/cypher/` — graph interchange formats
- 🧪 `data/work/` — scratch space (**never commit**)
- 📊 `mcp/runs/` — run logs + experiment artifacts (recommended for modeling runs)

> ✅ Rule of thumb: if a dev script produces something that would help another developer reproduce your results, it belongs in **a stable artifact folder** (not in your OS temp dir).

---

## 🔁 CI Alignment: “Detect → Validate → Promote”

Dev scripts should mirror the system’s governance pipeline:

1) **Detect**: identify new/changed data, code, or configs  
2) **Validate**: schema checks, metadata checks, provenance checks, contract tests  
3) **Promote**: move artifacts into canonical locations, update manifests/indexes

If a dev workflow *can’t* be expressed in those three stages, it’s a sign we should refactor it.

---

## 🧪 Dev Scripts as Scientific Instruments (Reproducibility Checklist)

When scripts influence **analysis / modeling / inference**, treat them like lab instruments:

- 🧷 Pin versions (Python deps, GDAL, database versions)
- 🧾 Log configs + seeds
- 📦 Store intermediate artifacts (not just final results)
- 🔍 Make validation executable (not “manual QA”)

This keeps “research workflows” and “software workflows” aligned, and prevents silent drift.

---

## 🧩 Adding a New Dev Script (Template Rules)

### Naming
- Bash: `kebab-case.sh` (e.g., `reset-local-stack.sh`)
- Python: `snake_case.py` (e.g., `validate_catalogs.py`)

### Required CLI flags
Every script should support:
- `--help`
- `--env-file PATH` (defaults to `.env.dev` if present)
- `--dry-run` where possible
- `--json` output option for CI-style parsing (optional but recommended)

### Logging
- Human-readable logs to stdout
- Optional `--out DIR` to write a run folder (`mcp/runs/<timestamp>_<run_id>/...`)

### Provenance hooks
- If a script creates/changes data artifacts, it should call the provenance builder (`build_prov`) or write a minimal run manifest:
  - inputs (paths/URLs/hashes)
  - outputs (paths/hashes)
  - environment (versions)
  - timestamp + run-id

---

## 🆘 Troubleshooting

### “Ports already in use”
```bash
docker compose ps
lsof -i :5432
lsof -i :7687
```

### “PostGIS extension missing”
If your migrations rely on extensions, ensure they’re created during bootstrap (or as a migration).

### “Neo4j import is slow / fails”
- Ensure constraints are applied *before* bulk import (where applicable)
- Prefer CSV bulk load patterns for large graphs; use Cypher for small dev graphs

### “Catalog validators fail”
- Confirm you’re validating against the correct profiles in `schemas/`
- Diff the failing JSON against the last known-good artifact in `data/stac/` / `data/catalog/`

---

## 📁 Suggested Folder Shape (Inside `api/scripts/dev`)

> This is the recommended structure as the dev toolkit grows.

```text
📂 api/scripts/dev/
├─ 📄 README.md
├─ 🩺🐚 doctor.sh
├─ 🧱⬆️🐚 up.sh
├─ 🧱⬇️🐚 down.sh
├─ 🧨♻️🐚 reset.sh
├─ 🚀🧱🐚 bootstrap.sh
├─ 🧬⬆️🐚 migrate.sh
├─ 🌱🐍 seed_minimal.py
├─ 📥🧪🐍 ingest_sample.py
├─ ✅🧾🐍 validate_catalogs.py
├─ 📤🕸️🐍 export_graph.py
├─ 📥🕸️🐍 import_graph.py
└─ 🧪✅🐚 smoke_test.sh
```

---

## 📚 Project Reference Shelf (Optional, but helpful)

<details>
<summary><b>Click to expand the project’s working library 📖</b></summary>

### 🧭 Core KFM Design & Planning
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx`
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`

### 🗺️ GIS / Cartography / Mapping
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

### 🧾 Data Standards / Data Platforms
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 📊 Stats / Modeling / Experiments
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `graphical-data-analysis-with-r.pdf`

### 🧠 AI / Society / Governance
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### 🕸️ Graphs / Optimization
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

### 🌐 Web / UI / Visualization
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`

### 🧵 Systems / Concurrency
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`

### 🔐 Security (Reference-Only)
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 🧰 Programming Compendiums (Multi-Book PDFs)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

</details>

---

## ✅ “Before you push” checklist

- [ ] Dev scripts changed? Update the **Script Catalog** table above  
- [ ] Validators pass (schemas, STAC/DCAT/PROV)  
- [ ] No sensitive values committed (`.env*`, tokens, real credentials)  
- [ ] No dev artifacts accidentally committed (`data/work/`, temp dumps)  
- [ ] Run `doctor` + `smoke_test` locally  
- [ ] If artifacts changed: new provenance bundle generated (`data/prov/`)

---

> 🧠 Reminder: if you’re unsure whether a script belongs here, ask:
> “Is this a **repeatable dev workflow** that should be easy for the next contributor to run?”
> If yes — it belongs in `api/scripts/dev`.

