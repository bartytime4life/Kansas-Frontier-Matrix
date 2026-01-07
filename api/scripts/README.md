# 🧰 Kansas Frontier Matrix (KFM) — API Scripts (`api/scripts/`)

<p align="left">
  <a href="#-kansas-frontier-matrix-kfm--api-scripts-apiscripts"><img alt="KFM Scripts" src="https://img.shields.io/badge/KFM-scripts-1f6feb" /></a>
  <a href="#-script-standards"><img alt="Bash" src="https://img.shields.io/badge/bash-%E2%9C%85-4EAA25?logo=gnubash&logoColor=white" /></a>
  <a href="#-script-standards"><img alt="Python" src="https://img.shields.io/badge/python-%E2%9C%85-3776AB?logo=python&logoColor=white" /></a>
  <a href="#-local-dev--ops-shortcuts"><img alt="Docker Compose" src="https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white" /></a>
  <a href="#-safety--governance-guardrails"><img alt="Safety" src="https://img.shields.io/badge/safety-deny--by--default-critical" /></a>
  <a href="#-data--catalog-workflows-stacdcatprov"><img alt="Catalogs" src="https://img.shields.io/badge/catalog-STAC%20%7C%20DCAT%20%7C%20PROV-845ef7" /></a>
  <a href="#-qa--ci-helpers"><img alt="CI" src="https://img.shields.io/badge/ci-contracts%20%7C%20schemas%20%7C%20policy-111827" /></a>
</p>

> 🧭 **Purpose:** This folder contains **operational & developer scripts** that support the KFM API stack — bootstrapping local dev, running maintenance tasks, importing governed datasets, generating catalogs/lineage artifacts, and performing repeatable admin operations.  
> 🧱 **Non-goal:** runtime business logic. Keep domain/use-case logic in `api/src/` (services/use-cases), not here.

> [!IMPORTANT]
> 🛑 **API boundary rule:** scripts may touch internal stores, but **clients must not**.  
> Scripts exist to help the API boundary stay clean, governed, and reproducible — not to create “backdoors.”

> [!IMPORTANT]
> ⛓️ **Pipeline order is absolute:** **ETL → STAC/DCAT/PROV Catalogs → Graph → API → UI → Story Nodes → Focus Mode**  
> Scripts are allowed to automate this flow, but must never bypass governance.

---

## 📌 Quick links

- [🧾 Doc metadata](#-doc-metadata)
- [🧠 What belongs in `api/scripts`](#-what-belongs-in-apiscripts)
- [🧱 Directory layout](#-directory-layout-recommended)
- [📦 Script contract (CLI + outputs)](#-script-contract-cli--outputs)
- [🚦 Safety & governance guardrails](#-safety--governance-guardrails)
- [🚀 Local dev & ops shortcuts](#-local-dev--ops-shortcuts)
- [🛰️ Data & catalog workflows](#️-data--catalog-workflows-stacdcatprov)
- [🗄️ Database & graph tasks](#️-database--graph-tasks)
- [🧪 QA / CI helpers](#-qa--ci-helpers)
- [🧩 Script standards](#-script-standards)
- [➕ Adding a new script](#-adding-a-new-script-template)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 Project reference library → script rules](#-project-reference-library--script-rules-uses-all-project-files)

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `api/scripts/README.md` |
| Status | Active ✅ |
| Last updated | **2026-01-07** |
| Applies to | dev/ops tooling, catalog builders, graph sync, contract QA, admin scripts |
| Safety stance | **deny-by-default** + explicit confirms for destructive actions |

---

## 🧠 What belongs in `api/scripts/`

This folder is for **repeatable automation** that is *close to the API stack*, for example:

- 🏗️ **Environment bootstrap:** create venvs, install deps, validate toolchain
- 🐳 **Ops glue:** bring up/down dependencies (Postgres/Neo4j/Redis), run health checks
- 🗄️ **DB/Graph admin:** migrations, seed data, role setup, integrity checks
- 🛰️ **Catalog production:** build/validate STAC/DCAT/PROV artifacts and sync references into the graph
- 🧪 **CI-friendly tasks:** contract checks, smoke tests, schema validation gates
- 📦 **Build tooling:** generate OpenAPI clients, bundle schemas, produce SBOMs (optional)
- 🧾 **Artifact hygiene:** generate checksums, quicklooks, run manifests, provenance bundles

> [!IMPORTANT]
> If the script contains **domain rules**, a **simulation algorithm**, or **redaction/classification logic** — that belongs in `api/src/` (services/use-cases) and should be importable + testable.  
> Scripts should orchestrate; core code should live in the app.

---

## 🧱 Directory layout (recommended)

> 🧩 If your repo differs, keep the same *intent*: scripts grouped by purpose, with shared helpers and clearly documented side-effects.

```text
📁 api/
└── 🧰 scripts/
    ├── 📄 README.md                      # 📘 you are here
    ├── 🧰 _lib/                          # 🧰 shared helpers (small + boring)
    │   ├── 📄 common.sh                  # strict-mode helpers, logging, traps
    │   ├── 📄 env.sh                     # env loading + validation
    │   ├── 📄 safety.sh                  # confirm/dry-run guards, prod-block rules
    │   └── 📄 run_manifest.py            # run metadata capture (git/env/inputs/outputs)
    ├── 🧑‍💻 dev/                          # local development convenience
    │   ├── 📄 up.sh                      # docker compose up
    │   ├── 📄 down.sh                    # docker compose down
    │   ├── 📄 reset.sh                   # ⚠️ destructive: reset local state
    │   └── 📄 smoke.sh                   # quick sanity checks
    ├── 🗄️ db/                            # Postgres tasks (migrate/seed/backup)
    │   ├── 📄 migrate.py
    │   ├── 📄 seed.py
    │   ├── 📄 backup.sh
    │   └── 📄 restore.sh
    ├── 🕸️ graph/                         # Neo4j / graph sync tasks
    │   ├── 📄 sync_catalog.py            # catalogs → graph references
    │   └── 📄 validate_refs.py           # orphan checks, ID consistency
    ├── 🛰️ catalogs/                      # STAC/DCAT/PROV build + validation
    │   ├── 📄 build_stac.py
    │   ├── 📄 build_dcat.py
    │   ├── 📄 build_prov.py
    │   └── 📄 validate_catalogs.py
    ├── 📡 rs/                            # remote sensing helpers (GEE orchestration, quicklooks)
    │   ├── 📄 gee_export.py
    │   └── 📄 build_quicklooks.py
    ├── 🧪 analysis/                       # analysis runners (regression/bayes/diagnostics) via api/src
    │   ├── 📄 run_regression.py
    │   └── 📄 run_bayes.py
    ├── 🧮 simulation/                     # simulation runners + V&V checks via api/src
    │   ├── 📄 run_simulation.py
    │   └── 📄 vv_check.py
    ├── 📜 contracts/                     # OpenAPI/Schema gates + client generation
    │   ├── 📄 lint_openapi.py
    │   ├── 📄 validate_jsonschema.py
    │   └── 📄 generate_client.sh
    ├── 🧪 ci/                            # CI entrypoints (stable + non-interactive)
    │   ├── 📄 check.sh
    │   └── 📄 test_contracts.sh
    └── 🛡️ security/                      # “trust but verify” helpers
        ├── 📄 secret_scan.sh
        ├── 📄 dependency_audit.sh
        └── 📄 policy_check.sh
```

> [!NOTE]
> The recommended `rs/`, `analysis/`, `simulation/`, and `security/` folders are optional — but they align with KFM’s “catalog + evidence + reproducibility” posture and keep scripts discoverable.

---

## 📦 Script contract (CLI + outputs)

KFM scripts are most useful when they behave consistently. Aim for a shared “script contract.”

### ✅ Standard CLI flags (recommended)
| Flag | Meaning | Why it matters |
|---|---|---|
| `--help` | usage + examples | discoverability |
| `--env dev|staging|prod` | target environment | prevents accidents |
| `--dry-run` | print plan, change nothing | safety + review |
| `--confirm` | allow destructive actions | “no foot-guns” |
| `--out <dir>` | write artifacts here | repeatability |
| `--json` | machine-readable logs | CI + pipelines |
| `--since <date>` | incremental runs | scalability |
| `--limit <n>` | bound work | abuse resistance |

> [!TIP]
> For Bash scripts: support `KFM_CONFIRM=1` and `KFM_DRY_RUN=1` as environment equivalents.

### 📤 Standard outputs (recommended)
Scripts that generate or mutate artifacts should output:

- ✅ **Run manifest**: `run.manifest.json`
- ✅ **Artifact list**: `artifacts.json` (or JSON Lines)
- ✅ **Checksums**: `sha256sums.txt`
- ✅ **Catalog pointers** (when applicable): STAC/DCAT/PROV IDs

Suggested `run.manifest.json` shape:
```json
{
  "run_id": "kfm.run.catalog.build.2026-01-07T12:34:56Z",
  "started_at": "2026-01-07T12:34:56Z",
  "git": { "commit": "abc123", "dirty": false },
  "environment": { "env": "dev", "python": "3.11.7", "platform": "linux" },
  "inputs": [
    { "type": "dataset", "id": "kfm.ks.boundaries.counties.v1", "classification": "public" }
  ],
  "outputs": [
    { "type": "stac_collection", "id": "kfm.stac.collection.ks.boundaries", "path": "..." }
  ],
  "warnings": [],
  "errors": []
}
```

> [!IMPORTANT]
> Treat run manifests as governance artifacts: they should never leak secrets, but they **should** capture enough to reproduce.

---

## 🚦 Safety & governance guardrails

KFM scripts often have privileged access (DB/graph/object store). Treat them like production code.

> [!CAUTION]
> **Default posture: “deny-by-default.”**  
> Scripts must not accidentally export sensitive data, modify production state, or weaken governance controls.

### ✅ Required safety behaviors

- 🔐 **No secrets in repo:** never print tokens/keys; never commit `.env`; never echo credentials
- 🧷 **Classification propagation:** outputs ≥ strictest input classification (no privacy downgrade)
- 🧼 **Redaction consistency:** if a script produces UI/API-consumed outputs, it must use the same redaction policy as the API boundary
- 🧯 **Destructive operations are explicit:**
  - require `--confirm` (or `KFM_CONFIRM=1`)
  - support `--dry-run` where possible
  - print a “plan” before executing changes
- 🧾 **Provenance-first:** generated views and artifacts must link back to evidence (STAC/DCAT/PROV IDs/links)
- 🧪 **Validation gates:** schema checks and invariants fail fast with non-zero exit codes
- 🧵 **Bounded work:** limit query scope; avoid full-table scans by default; enforce timeouts

### 🧨 Prod-block rule (recommended)
Scripts that can mutate or delete must refuse production unless explicitly overridden:

- block if `KFM_ENV=prod` and **no** `--i-know-what-im-doing` style flag
- block if target DB hostname matches protected list
- require a second confirmation prompt *only when interactive* (never in CI)

> [!IMPORTANT]
> If you discover a security issue in scripts, **do not** open a public GitHub Issue/PR comment.  
> Follow `SECURITY.md` (or `docs/security/` if present). 🛡️

---

## 🚀 Local dev & ops shortcuts

### 1) Prereqs ✅
- 🐍 Python (project-supported version)
- 🐳 Docker + Docker Compose
- 🧰 CLI tooling: `bash`, `curl`, `jq` (recommended)

### 2) Environment variables (typical)

Keep a safe sample at `api/.env.example` and load real values locally via `api/.env` (gitignored).

```bash
# App
KFM_ENV=dev
KFM_LOG_LEVEL=INFO

# Stores
KFM_POSTGRES_URL=postgresql://user:pass@localhost:5432/kfm
KFM_NEO4J_URI=bolt://localhost:7687
KFM_NEO4J_USER=neo4j
KFM_NEO4J_PASSWORD=please-change-me

# Governance
KFM_REDACTION_MODE=strict
KFM_DEFAULT_CLASSIFICATION=public
```

### 3) Bring up dependencies (example)
```bash
cd api
./scripts/dev/up.sh
```

### 4) Smoke test (example)
```bash
./scripts/dev/smoke.sh
```

<details>
<summary><strong>💡 Optional: Makefile wrappers</strong></summary>

```makefile
api-up:
\tcd api && ./scripts/dev/up.sh

api-smoke:
\tcd api && ./scripts/dev/smoke.sh
```

</details>

---

## 🛰️ Data & catalog workflows (STAC/DCAT/PROV)

KFM’s publishing posture is: **data outputs become real only when cataloged**.

Scripts may:
- build STAC Items/Collections (assets, geometry, timestamps, checksums)
- build DCAT dataset/distribution views (discovery metadata)
- build PROV lineage bundles (inputs → activities → outputs)
- validate catalogs (schema + KFM invariants)
- sync *references* into the graph (graph points to catalogs; it does not replace them)

### 🧭 Canonical flow
```mermaid
flowchart LR
  R["📦 Raw/Processed Outputs"] --> S["🏷️ STAC/DCAT/PROV Build"]
  S --> V["✅ Validate (schema + invariants)"]
  V --> G["🕸️ Graph Sync (references only)"]
  G --> A["🚪 API Serves Catalog-backed Views"]
```

### Example run (illustrative)
```bash
# 1) Build catalogs
python ./scripts/catalogs/build_stac.py   --in ./data/processed --out ./data/catalogs/stac
python ./scripts/catalogs/build_dcat.py   --stac ./data/catalogs/stac --out ./data/catalogs/dcat
python ./scripts/catalogs/build_prov.py   --runs ./data/runs --out ./data/catalogs/prov

# 2) Validate
python ./scripts/catalogs/validate_catalogs.py --root ./data/catalogs

# 3) Sync references to graph
python ./scripts/graph/sync_catalog.py --stac ./data/catalogs/stac --dcat ./data/catalogs/dcat --prov ./data/catalogs/prov
```

> [!TIP]
> Prefer immutable/cataloged outputs (content-addressable paths or checksums) so provenance and reproducibility stay strong 🧬.

---

## 🗄️ Database & graph tasks

### 🗄️ Postgres tasks (migrations, seed, backup)
Recommended behaviors:
- migrations are ordered and tracked
- seeding uses non-production fixtures only
- backups are encrypted (if stored) and never leak secrets in logs

Examples:
```bash
python ./scripts/db/migrate.py up
python ./scripts/db/seed.py --fixture dev_minimal
./scripts/db/backup.sh --out ./backups/kfm-local.sql.gz
```

### 🕸️ Graph tasks (Neo4j sync & validation)
Graph scripts should:
- treat the graph as a **reference index**
- avoid storing sensitive raw payloads if catalogs already hold them
- preserve **stable IDs** (STAC/DCAT/PROV identifiers) for traceability

Examples:
```bash
python ./scripts/graph/validate_refs.py --fail-on-orphans
python ./scripts/graph/sync_catalog.py --env dev --stac ./data/catalogs/stac
```

---

## 🧪 QA / CI helpers

Use scripts here to keep CI stable and readable:

- 📜 OpenAPI linting + contract checks
- ✅ JSON Schema validation (requests/responses/envelopes)
- 🧷 “Invariant checks” (pipeline ordering, classification propagation)
- 🧨 Security checks (redaction regression, authz guardrails)
- 🧪 Catalog QA runs (a dedicated `catalog_qa` runner is recommended)

Example:
```bash
./scripts/ci/check.sh
./scripts/ci/test_contracts.sh
```

> [!NOTE]
> CI scripts must be deterministic, fast, and non-interactive. Avoid prompts; use flags/env vars.

---

## 🧩 Script standards

### Bash scripts ✅
Use strict mode + safe defaults:
```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
```

Minimum expectations:
- usage on bad args + `--help`
- consistent logging (timestamp + level)
- non-zero exit codes on failure
- no silent destructive actions

### Python scripts ✅
Prefer importable modules (so logic is testable):
- scripts call into `api/src/...` (services/use-cases) instead of re-implementing logic
- parse args with `argparse` (or Typer if adopted)
- validate env vars up-front and fail fast
- write artifacts (manifests, checksums, catalogs) deterministically

### Naming conventions 🏷️
Pick one and stick to it:
- `verb_noun` (recommended): `build_stac.py`, `sync_catalog.py`
- group by intent: `db/`, `graph/`, `catalogs/`, `contracts/`, `dev/`, `ci/`, `security/`

### Required documentation 📘
Every script must include:
- short description
- inputs/outputs
- side-effects
- required env vars
- examples

---

## ➕ Adding a new script (template)

Copy/paste this header into new scripts:

```text
📌 Script: <name>
🎯 Goal: <what it does>
📥 Inputs: <files/urls/db tables>
📤 Outputs: <files/db changes>
⚠️ Side effects: <writes/deletes/network calls>
🔐 Required env: <KFM_* vars>
✅ Safety: <dry-run/confirm/idempotent?>
🧪 Tests: <where/how verified>
🧾 Provenance: <STAC/DCAT/PROV links or IDs, if applicable>
🏷️ Classification: <how computed/propagated>
```

> [!TIP]
> If a script is “important enough to be scary,” it’s important enough to have:
> - `--dry-run`
> - `--confirm`
> - a unit-testable core function in `api/src/`

---

## 🧯 Troubleshooting

### Common issues

- 🐳 **Docker not running**
  - check: `docker ps`
  - restart Docker daemon/desktop
- 🗄️ **Postgres connection failures**
  - verify `KFM_POSTGRES_URL`
  - confirm port mappings in compose
- 🕸️ **Neo4j auth errors**
  - verify `KFM_NEO4J_USER/PASSWORD`
  - confirm `bolt://` URI and container health
- 🧪 **Schema/catalog validation fails**
  - rebuild catalogs
  - confirm schema versions match API contracts
- 🧷 **Classification/redaction mismatch**
  - treat as a governance bug; fix before publishing artifacts

---

## 📚 Project reference library → script rules (uses all project files)

> Requirement: this section maps **every project file** to a concrete `api/scripts` convention, guardrail, or workflow expectation.

<details>
<summary><strong>🧠 Expand: Influence map (all project files)</strong></summary>

| Project file | Script impact (what it changes here) |
|---|---|
| `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx` | Establishes “automation + CLI tooling” posture (Makefile-like rebuilds), catalog-first pipeline order, and governed operations discipline |
| `Latest Ideas.docx` | Adds “catalog QA” mindset, policy-as-code checks (OPA/Conftest concepts), and supply-chain hygiene (SLSA/SBOM/Cosign direction) for script-driven pipelines |
| `Data Spaces.pdf` | Reinforces pointer-over-payload patterns: scripts should generate catalogs and references, not copy huge datasets into repo paths |
| `Introduction to Digital Humanism.pdf` | Human-centered governance: scripts must preserve agency, avoid privacy downgrade, and keep auditability first-class |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | Systems thinking: explicit state transitions, closure/feedback loops, and “safe bounded automation” patterns |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | Forces audit-ready AI/ML outputs: scripts must record model/version/config and produce provenance pointers |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | Shapes remote sensing scripts (GEE exports, time-series derivatives, catalog emission, and reproducible parameters) |
| `python-geospatial-analysis-cookbook.pdf` | CRS sanity rules in scripts: transforms at boundaries, explicit SRIDs, geometry validation and simplification done intentionally |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | Scripts that generate legends/quicklooks/tiles must avoid misleading cartography and keep symbology decisions documented |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | Supports offline and constrained-device workflows: scripts for tile bundles/quicklooks should optimize for bandwidth and context |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | DB scripts: safe migrations, backup/restore discipline, indexing awareness, and bounded maintenance tasks |
| `Scalable Data Management for Future Hardware.pdf` | Encourages incremental builds, streaming I/O, bounded memory use, and “don’t accidentally do O(N) over huge datasets” defaults |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | Concurrency discipline: idempotent job runners, bounded worker fanout, backpressure, and safe retries |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | Security posture: scripts must be hardened (least privilege, segmentation assumptions, safe network operations) |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | Defensive coding: hostile input handling, safe parsing, and “assume fuzzing” for file/geo parsers and ingestion |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | Quicklook/thumbnail scripts: choose formats intentionally and optimize outputs for UI performance without losing meaning |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | 3D asset pipeline scripts: coordinate sanity, safe loader posture, and “3D is optional; degrade gracefully” support tooling |
| `Spectral Geometry of Graphs.pdf` | Graph-related scripts: bounded analytics, explainable metrics, and careful handling of graph operations |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | Simulation scripts: reproducibility, run manifests, V&V checks, scenario metadata, sensitivity hooks |
| `Generalized Topology Optimization for Structural Design.pdf` | Optimization workflows: scripts should capture objective/constraints metadata and treat results as governed artifacts |
| `Understanding Statistics & Experimental Design.pdf` | Analysis scripts must avoid misleading inference: require assumptions, document experimental context, and output uncertainty |
| `graphical-data-analysis-with-r.pdf` | EDA scripts: produce diagnostics plots/tables, highlight outliers, and keep exploration artifacts deterministic |
| `regression-analysis-with-python.pdf` | Regression scripts: include residual checks, diagnostics, and explicit model assumptions in artifacts |
| `Regression analysis using Python - slides-linear-regression.pdf` | Standardizes regression run outputs for UI consumption: coefficients + fit metrics + diagnostics references |
| `think-bayes-bayesian-statistics-in-python.pdf` | Bayesian scripts: priors disclosed, posterior summaries with credible intervals, and provenance recorded |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | ML scripts: artifact/version driven, training separated from API runtime, model-card-friendly outputs |
| `A programming Books.pdf` | Contributor shelf: script style is language-agnostic; supports future adapters and tooling |
| `B-C programming Books.pdf` | Contributor shelf |
| `D-E programming Books.pdf` | Contributor shelf |
| `F-H programming Books.pdf` | Contributor shelf |
| `I-L programming Books.pdf` | Contributor shelf |
| `M-N programming Books.pdf` | Contributor shelf |
| `O-R programming Books.pdf` | Contributor shelf |
| `S-T programming Books.pdf` | Contributor shelf |
| `U-X programming Books.pdf` | Contributor shelf |
| `responsive-web-design-with-html5-and-css3.pdf` | Scripts generating UI assets (quicklooks/legends) must respect performance budgets and responsive delivery considerations |

</details>

---

<!--
Maintainers’ TODOs ✅ (keep or remove):
- Add `api/.env.example` (safe defaults, no secrets).
- Add `scripts/_lib/safety.sh` with prod-block + confirm/dry-run utilities.
- Add `scripts/_lib/run_manifest.py` and require it for any artifact-producing script.
- Decide invocation style: direct scripts vs Makefile targets (either is fine; just standardize).
- Add CI workflows that call scripts/ci/* as stable entrypoints.
-->