# 🧰 Kansas Frontier Matrix (KFM) — API Scripts (`api/scripts/`)

<p align="left">
  <a href="#kfm-api-scripts"><img alt="KFM Scripts" src="https://img.shields.io/badge/KFM-scripts-1f6feb" /></a>
  <a href="#script-standards"><img alt="Bash" src="https://img.shields.io/badge/bash-%E2%9C%85-4EAA25?logo=gnubash&logoColor=white" /></a>
  <a href="#script-standards"><img alt="Python" src="https://img.shields.io/badge/python-%E2%9C%85-3776AB?logo=python&logoColor=white" /></a>
  <a href="#local-dev--ops-shortcuts"><img alt="Docker Compose" src="https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white" /></a>
  <a href="#safety--governance-guardrails"><img alt="Safety" src="https://img.shields.io/badge/safety-deny--by--default-critical" /></a>
  <a href="#data--catalog-workflows-stacdcatprov"><img alt="Catalogs" src="https://img.shields.io/badge/catalog-STAC%20%7C%20DCAT%20%7C%20PROV-845ef7" /></a>
  <a href="#determinism--idempotency"><img alt="Repro" src="https://img.shields.io/badge/repro-deterministic%20%2B%20idempotent-0ea5e9" /></a>
  <a href="#qa--ci-helpers"><img alt="CI" src="https://img.shields.io/badge/ci-contracts%20%7C%20schemas%20%7C%20policy-111827" /></a>
</p>

<a id="kfm-api-scripts"></a>

> 🧭 **Purpose:** This folder contains **operational & developer scripts** that support the KFM API stack — bootstrapping local dev, running maintenance tasks, importing governed datasets, generating catalogs/lineage artifacts, emitting reproducibility evidence, and performing repeatable admin operations.  
> 🧱 **Non-goal:** runtime business logic. Keep domain/use-case logic in `api/src/` (services/use-cases), not here.

> [!IMPORTANT]
> 🛑 **API boundary rule:** scripts may touch internal stores, but **clients must not**.  
> Scripts exist to help the API boundary stay clean, governed, and reproducible — not to create “backdoors.”

> [!IMPORTANT]
> ⛓️ **Canonical pipeline order is absolute:** **Data → Catalogs → Graph → API → UI → Story Nodes → Focus Mode**  
> Scripts may automate this flow, but must never bypass governance or provenance.

> [!CAUTION]
> 🧨 **Evidence-first publishing:** “it doesn’t exist until it’s cataloged.”  
> Any data/analysis/simulation output meant for API/UI **must** land in STAC/DCAT/PROV (and carry license + classification) before it can be served.

---

## 📌 Quick links

- [🧾 Doc metadata](#doc-metadata)
- [🧭 Where scripts fit in the repo](#where-scripts-fit)
- [🧠 What belongs in `api/scripts`](#what-belongs-in-apiscripts)
- [🧱 Directory layout](#directory-layout-recommended)
- [📦 Script contract (CLI + outputs)](#script-contract-cli--outputs)
- [🧬 Determinism & idempotency](#determinism--idempotency)
- [🚦 Safety & governance guardrails](#safety--governance-guardrails)
- [🚀 Local dev & ops shortcuts](#local-dev--ops-shortcuts)
- [🛰️ Data & catalog workflows](#data--catalog-workflows-stacdcatprov)
- [🗄️ Database & graph tasks](#database--graph-tasks)
- [🧪 Analytics, simulation, and optimization runners](#analytics-simulation-and-optimization-runners)
- [🛡️ Security & supply-chain hygiene](#security--supply-chain-hygiene)
- [🧪 QA / CI helpers](#qa--ci-helpers)
- [🧩 Script standards](#script-standards)
- [➕ Adding a new script](#adding-a-new-script-template)
- [🧯 Troubleshooting](#troubleshooting)
- [📚 Project reference library → script rules](#project-reference-library--script-rules)

---

<a id="doc-metadata"></a>

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `api/scripts/README.md` |
| Status | Active ✅ |
| Last updated | **2026-01-09** |
| Applies to | dev/ops tooling, catalog builders, graph sync, contract QA, admin scripts |
| Safety stance | **deny-by-default** + explicit confirms for destructive actions |
| Cross-cutting invariants | contract-first 🧾 • evidence-first 🧬 • provenance-first 🧾 • deterministic runs 🎯 |
| Preferred artifacts | `run.manifest.json` + `sha256sums.txt` + catalog IDs (STAC/DCAT/PROV) |

---

<a id="where-scripts-fit"></a>

## 🧭 Where scripts fit in the repo

KFM separates **orchestration** from **implementation**. This README is for the orchestration layer.

| Path | What belongs there | What must *not* be there |
|---|---|---|
| `api/scripts/` 🧰 | repeatable ops/dev/admin runners (call into `api/src/`), catalog builders/validators, DB/graph sync, CI entrypoints | business rules, inference logic, “core algorithms” |
| `api/src/` 🧠 | services/use-cases, policy enforcement, redaction/classification logic, “the truth” | shell glue, environment hacks |
| `pipelines/` 📦 | reproducible ETL and domain pipelines (raw → work → processed) | ad-hoc local scripts |
| `tools/` 🧪 | validation utilities, catalog QA, one-off but reusable tooling | API runtime logic |
| `notebooks/` 📓 | exploratory work (EDA/prototyping) | production pipelines |
| `docs/` 📚 | governed docs (architecture, standards, Story Nodes, Focus Mode rules) | scripts-as-docs without code |

> [!TIP]
> **Rule of thumb:** scripts orchestrate and *call* stable code; stable code is importable, testable, and lives in `api/src/`.

---

<a id="what-belongs-in-apiscripts"></a>

## 🧠 What belongs in `api/scripts/`

This folder is for **repeatable automation** that’s *close to the API stack*, for example:

- 🏗️ **Environment bootstrap:** create venvs, install deps, validate toolchain
- 🐳 **Ops glue:** bring up/down dependencies (Postgres/Neo4j/Redis), run health checks
- 🗄️ **DB/Graph admin:** migrations, seed data, role setup, integrity checks
- 🛰️ **Catalog production:** build/validate STAC/DCAT/PROV artifacts and sync **references** into the graph
- 🧪 **CI-friendly tasks:** contract checks, smoke tests, schema validation gates, policy gates (fail-closed)
- 📦 **Build tooling:** generate OpenAPI clients, bundle schemas, produce SBOMs/attestations (optional but recommended)
- 🧾 **Artifact hygiene:** checksums, quicklooks, run manifests, provenance bundles

> [!IMPORTANT]
> If the script contains **domain rules**, a **simulation algorithm**, or **redaction/classification logic** — that belongs in `api/src/` (services/use-cases) and should be importable + testable.  
> Scripts should orchestrate; core code should live in the app.

---

<a id="directory-layout-recommended"></a>

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
    │   ├── 📄 io.py                      # atomic writes, checksums, temp dirs
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
    ├── 🕸️ graph/                         # Neo4j / graph sync tasks (references only)
    │   ├── 📄 sync_catalog.py            # catalogs → graph references
    │   ├── 📄 validate_refs.py           # orphan checks, ID consistency
    │   └── 📄 metrics.py                 # bounded graph metrics (optional)
    ├── 🛰️ catalogs/                      # STAC/DCAT/PROV build + validation
    │   ├── 📄 build_stac.py
    │   ├── 📄 build_dcat.py
    │   ├── 📄 build_prov.py
    │   └── 📄 validate_catalogs.py
    ├── 📡 rs/                            # remote sensing helpers (GEE orchestration, quicklooks)
    │   ├── 📄 gee_export.py
    │   ├── 📄 build_quicklooks.py
    │   └── 📄 validate_crs.py            # CRS + geometry sanity checks
    ├── 🧪 analysis/                       # analysis runners (regression/bayes/diagnostics) via api/src
    │   ├── 📄 run_regression.py
    │   ├── 📄 run_bayes.py
    │   └── 📄 diagnostics_report.py      # residuals, posterior checks, plots
    ├── 🧮 simulation/                     # simulation runners + V&V checks via api/src
    │   ├── 📄 run_simulation.py
    │   ├── 📄 vv_check.py                # verification & validation gates
    │   └── 📄 sensitivity.py             # optional scenario sweeps
    ├── 🧱 optimization/                   # optimization runners (topology, constraints) via api/src
    │   ├── 📄 run_optimization.py
    │   └── 📄 validate_constraints.py
    ├── 📜 contracts/                     # OpenAPI/Schema gates + client generation
    │   ├── 📄 lint_openapi.py
    │   ├── 📄 validate_jsonschema.py
    │   └── 📄 generate_client.sh
    ├── 🧪 ci/                            # CI entrypoints (stable + non-interactive)
    │   ├── 📄 check.sh
    │   ├── 📄 test_contracts.sh
    │   └── 📄 catalog_qa.sh              # wrapper around catalog QA tool (if elsewhere)
    ├── 🧾 policy/                        # policy-as-code gates (fail closed)
    │   ├── 📄 conftest.sh                # OPA/Conftest runner wrapper
    │   └── 📄 validate_policies.sh
    ├── 📈 telemetry/                     # operational telemetry emit/validate (optional)
    │   ├── 📄 emit_event.py              # emit JSON event envelopes
    │   └── 📄 validate_events.py         # schema validate telemetry JSONL
    └── 🛡️ security/                      # “trust but verify” helpers
        ├── 📄 secret_scan.sh
        ├── 📄 dependency_audit.sh
        ├── 📄 sbom_generate.sh           # optional
        └── 📄 policy_check.sh
```

> [!NOTE]
> The `rs/`, `analysis/`, `simulation/`, `optimization/`, `policy/`, and `telemetry/` folders are optional — but they align with KFM’s “catalog + evidence + reproducibility” posture and keep scripts discoverable.

---

<a id="script-contract-cli--outputs"></a>

## 📦 Script contract (CLI + outputs)

KFM scripts are most useful when they behave consistently. Aim for a shared “script contract.”

### ✅ Standard CLI flags (recommended)

| Flag | Meaning | Why it matters |
|---|---|---|
| `--help` | usage + examples | discoverability |
| `--env dev\|staging\|prod` | target environment | prevents accidents |
| `--dry-run` | print plan, change nothing | safety + review |
| `--confirm` | allow destructive actions | “no foot-guns” |
| `--out <dir>` | write artifacts here | repeatability |
| `--json` | machine-readable logs | CI + pipelines |
| `--since <date>` | incremental runs | scalability |
| `--limit <n>` | bound work | abuse resistance |
| `--timeout <sec>` | abort long operations | bounded automation |
| `--seed <string>` | deterministic seed / commit seed | reproducibility |
| `--idempotency-key <string>` | stable replay-safe run key | safe re-runs |

> [!TIP]
> For Bash scripts: support `KFM_CONFIRM=1` and `KFM_DRY_RUN=1` as environment equivalents.  
> For deterministic runs: support `KFM_COMMIT_SEED=...` and `KFM_IDEMPOTENCY_KEY=...`.

### 🧾 Standard “plan-first” behavior (recommended)

If a script can mutate state (DB/graph/object store), it should support:

- **Plan output** (what will change, why, and scope)
- **Validate** (schemas + invariants + policy)
- **Execute** (only after explicit confirm)

```mermaid
flowchart LR
  A["🧾 Plan"] --> B["✅ Validate"]
  B --> C{"Confirmed?"}
  C -->|No| D["🧯 Exit safe"]
  C -->|Yes| E["⚙️ Execute"]
  E --> F["📦 Emit artifacts + manifests"]
```

---

<a id="determinism--idempotency"></a>

## 🧬 Determinism & idempotency

KFM treats “rebuildability” as a **governance feature**, not a convenience.

### ✅ Minimum requirements

- 🎯 **Deterministic seed:** every artifact-producing script supports `--seed` (or derives from a `commit_seed`)
- 🔁 **Idempotency key:** every run has a stable `idempotency_key` and is safe to replay
- 🧾 **Manifested runs:** every run emits a `run.manifest.json` (and never leaks secrets)
- 🧪 **Repro checks:** CI can re-run scripts and compare output hashes for drift

### 🧷 Suggested idempotency key shape

Use a predictable key that changes when it should, and stays stable when it should:

```text
{component}.{subject}.{window}.{commit_seed}
```

Examples:
- `catalogs.build.ks_counties.2026q1.agents-wpe-arch-v11.2.6`
- `db.migrate.kfm_api_schema.v3.2026-01-09T00Z`

> [!IMPORTANT]
> **Idempotency is not optional** for scripts that run in CI/CD or automation. If re-running a job can change results, it must say so loudly and fail closed unless explicitly allowed.

---

### 📤 Standard outputs (recommended)

Scripts that generate or mutate artifacts should output:

- ✅ **Run manifest:** `run.manifest.json`
- ✅ **Plan (if mutating):** `plan.json`
- ✅ **Artifact list:** `artifacts.json` (or JSONL)
- ✅ **Checksums:** `sha256sums.txt`
- ✅ **Catalog pointers** (when applicable): STAC/DCAT/PROV IDs
- ✅ **Telemetry (optional):** `telemetry.jsonl` (validated against a schema)

Suggested `run.manifest.json` shape:

```json
{
  "run_id": "kfm.run.catalog.build.2026-01-09T12:34:56Z",
  "idempotency_key": "catalogs.build.ks_counties.2026q1.seed-abc",
  "started_at": "2026-01-09T12:34:56Z",
  "git": { "commit": "abc123", "dirty": false },
  "environment": { "env": "dev", "python": "3.11.7", "platform": "linux" },
  "inputs": [
    { "type": "dataset", "id": "kfm.ks.boundaries.counties.v1", "classification": "public", "license": "CC-BY-4.0" }
  ],
  "outputs": [
    { "type": "stac_collection", "id": "kfm.stac.collection.ks.boundaries", "path": "data/stac/collections/..." }
  ],
  "warnings": [],
  "errors": []
}
```

> [!IMPORTANT]
> Treat run manifests as governance artifacts: they should never leak secrets, but they **must** capture enough to reproduce.

---

<a id="safety--governance-guardrails"></a>

## 🚦 Safety & governance guardrails

KFM scripts often have privileged access (DB/graph/object store). Treat them like production code.

> [!CAUTION]
> **Default posture: “deny-by-default.”**  
> Scripts must not accidentally export sensitive data, modify production state, or weaken governance controls.

### ✅ Required safety behaviors

- 🔐 **No secrets in logs or artifacts**
  - never print tokens/keys
  - never commit `.env`
  - never echo credentials (even in `--debug`)
- 🧷 **Classification propagation**
  - outputs inherit the strictest input classification (no privacy downgrade)
  - include classification + license metadata in artifacts (especially catalogs)
- ⚖️ **License propagation**
  - do not strip licenses from derived outputs
  - if combining sources, document the controlling license and constraints
- 🧼 **Redaction consistency**
  - if a script produces UI/API-consumed outputs, it must use the same redaction policy as the API boundary (`api/src/`)
- 🧯 **Destructive operations are explicit**
  - require `--confirm` (or `KFM_CONFIRM=1`)
  - support `--dry-run` and print a plan before executing
- 🧾 **Provenance-first**
  - generated views and artifacts must link back to evidence (STAC/DCAT/PROV IDs/links)
- 🧪 **Validation gates**
  - schema checks + invariants fail fast with non-zero exit codes
- 🧵 **Bounded work**
  - limit query scope; avoid full-table scans by default; enforce timeouts; cap concurrency

### 🧨 Prod-block rule (recommended)

Scripts that can mutate or delete must refuse production unless explicitly overridden:

- block if `KFM_ENV=prod` and **no** `--i-know-what-im-doing` style flag
- block if target DB hostname matches a protected list
- require a second confirmation prompt *only when interactive* (never in CI)

### 🤖 Automation/agent safety (recommended)

If scripts are invoked by automation (e.g., Watcher/Planner/Executor systems):

- honor a **kill-switch** file (e.g., `ops/feature_flags/*.yml`)
- require **idempotency keys** + **deterministic seeds**
- prefer **PR-only promotion** (no direct merges/writes to protected branches)

> [!IMPORTANT]
> If you discover a security issue in scripts, **do not** open a public GitHub Issue/PR comment.  
> Follow `SECURITY.md` (or `docs/security/` if present). 🛡️

---

<a id="local-dev--ops-shortcuts"></a>

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

# Determinism
KFM_COMMIT_SEED=local-dev
KFM_IDEMPOTENCY_KEY=dev.smoke.local-dev

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

<a id="data--catalog-workflows-stacdcatprov"></a>

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
  S --> V["✅ Validate (schema + invariants + policy)"]
  V --> G["🕸️ Graph Sync (references only)"]
  G --> A["🚪 API Serves Catalog-backed Views"]
  A --> U["🗺️ UI / Story Nodes / Focus Mode"]
```

### 🗂️ Recommended staging (v13-style)

Keep data lifecycle explicit (this enables reproducibility + audit):

```text
📁 data/
  ├── raw/<domain>/            # source drops (immutable as possible)
  ├── work/<domain>/           # intermediate (rebuildable)
  ├── processed/<domain>/       # final outputs (what gets published)
  ├── stac/                     # STAC items + collections
  ├── catalog/dcat/             # DCAT dataset/distribution views
  ├── prov/                     # PROV lineage bundles
  └── runs/                     # run manifests, artifacts, logs (optional but recommended)
```

### Example run (illustrative)

```bash
# 1) Build catalogs
python ./scripts/catalogs/build_stac.py --in ./data/processed --out ./data/stac --seed "$KFM_COMMIT_SEED"
python ./scripts/catalogs/build_dcat.py --stac ./data/stac --out ./data/catalog/dcat --seed "$KFM_COMMIT_SEED"
python ./scripts/catalogs/build_prov.py --runs ./data/runs --out ./data/prov --seed "$KFM_COMMIT_SEED"

# 2) Validate (schema + invariants + policy)
python ./scripts/catalogs/validate_catalogs.py --root ./data

# 3) Sync references to graph (no payload copies)
python ./scripts/graph/sync_catalog.py --env dev --stac ./data/stac --dcat ./data/catalog/dcat --prov ./data/prov
```

> [!TIP]
> Prefer immutable/cataloged outputs (content-addressable paths or checksums) so provenance and reproducibility stay strong 🧬.

---

<a id="database--graph-tasks"></a>

## 🗄️ Database & graph tasks

### 🗄️ Postgres tasks (migrations, seed, backup)

Recommended behaviors:
- migrations are ordered and tracked
- seeding uses **non-production fixtures only**
- backups are encrypted (if stored) and never leak secrets in logs
- prefer parameterized SQL and least-privilege accounts (even for scripts)

Examples:
```bash
python ./scripts/db/migrate.py up --env dev --seed "$KFM_COMMIT_SEED"
python ./scripts/db/seed.py --fixture dev_minimal --env dev --seed "$KFM_COMMIT_SEED"
./scripts/db/backup.sh --out ./backups/kfm-local.sql.gz --env dev
```

### 🕸️ Graph tasks (Neo4j sync & validation)

Graph scripts should:
- treat the graph as a **reference index**
- avoid storing sensitive raw payloads if catalogs already hold them
- preserve **stable IDs** (STAC/DCAT/PROV identifiers) for traceability
- keep analytics bounded (avoid accidental `O(N)` over the whole graph)

Examples:
```bash
python ./scripts/graph/validate_refs.py --fail-on-orphans --env dev
python ./scripts/graph/sync_catalog.py --env dev --stac ./data/stac
```

> [!NOTE]
> If you add graph metrics (community detection, spectral-ish measures, centrality), output them as **evidence artifacts**: versioned + cataloged + traceable.

---

<a id="analytics-simulation-and-optimization-runners"></a>

## 🧪 Analytics, simulation, and optimization runners

These runners should feel like “science you can audit” ✅

### 📈 Regression & experimental design runners

When scripts run regression models or statistical experiments, they should output:

- coefficients + standard errors (or posteriors)
- model assumptions & checks (residuals, leverage/influence, collinearity notes)
- uncertainty (CIs or credible intervals)
- dataset/feature provenance links (STAC/DCAT/PROV)
- a short machine-readable `analysis.summary.json`

Example (illustrative):
```bash
python ./scripts/analysis/run_regression.py \
  --env dev \
  --dataset-id kfm.water.streamflow.v2 \
  --out data/processed/analysis/streamflow_regression_v1 \
  --seed "$KFM_COMMIT_SEED"
```

### 🎲 Bayesian runners

Bayesian scripts must **declare priors** and output:

- posterior summaries + credible intervals
- diagnostics (e.g., effective sample size, divergence counts where relevant)
- provenance (inputs + code version + sampler settings)

### 🧮 Simulation & V&V runners

Simulation scripts must be reproducible and V&V-aware:

- scenario ID + parameters
- numeric settings (tolerances, solver versions)
- V&V checks (sanity tests, invariants, regression tests)
- sensitivity hooks (optional but recommended)

Example:
```bash
python ./scripts/simulation/run_simulation.py --scenario kfm.scenario.flood.v1 --out data/processed/sim/flood_v1 --seed "$KFM_COMMIT_SEED"
python ./scripts/simulation/vv_check.py --in data/processed/sim/flood_v1 --fail-fast
```

### 🧱 Optimization runners (topology/constraints)

Optimization scripts should capture:

- objective function + constraints
- stopping conditions + solver settings
- initial conditions / seed
- artifact bundle (meshes, plots, results tables) with checksums

---

<a id="security--supply-chain-hygiene"></a>

## 🛡️ Security & supply-chain hygiene

Scripts are privileged. Secure them like prod services.

### ✅ Security basics

- least privilege credentials (dev/staging/prod separation)
- no plaintext secrets in logs, manifests, or artifacts
- safe parsing of untrusted files (geo + images + CSVs + JSON)
- fail closed (policy gates should block on errors)

### 🔎 Suggested helpers (optional but recommended)

- secret scanning (pre-commit + CI)
- dependency audits (pip/poetry/npm as applicable)
- SBOM generation (SPDX/CycloneDX)
- build attestations (SLSA, Sigstore-style signing)
- policy-as-code checks (OPA/Conftest) for:
  - classification propagation
  - license metadata presence
  - “no-prod-writes” rules
  - required artifacts (manifest + checksums)

> [!IMPORTANT]
> Do not include “how to exploit X” content in this repo. We harden defensively; we don’t publish offensive playbooks.

---

<a id="qa--ci-helpers"></a>

## 🧪 QA / CI helpers

Use scripts here to keep CI stable and readable:

- 📜 OpenAPI linting + contract checks
- ✅ JSON Schema validation (requests/responses/envelopes)
- 🧷 invariant checks (pipeline ordering, classification + license propagation)
- 🧨 security checks (redaction regression, authz guardrails)
- 🛰️ catalog QA runs (a dedicated catalog QA runner is recommended)

Example:
```bash
./scripts/ci/check.sh
./scripts/ci/test_contracts.sh
./scripts/ci/catalog_qa.sh
```

> [!NOTE]
> CI scripts must be deterministic, fast, and non-interactive. Avoid prompts; use flags/env vars.

---

<a id="script-standards"></a>

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
- always quote variables; use arrays for args

### Python scripts ✅

Prefer importable modules (so logic is testable):

- scripts call into `api/src/...` (services/use-cases) instead of re-implementing logic
- parse args with `argparse` (or Typer if adopted)
- validate env vars up-front and fail fast
- write artifacts deterministically
- bound concurrency (avoid “spawn 500 workers” defaults)
- stream large files (don’t load multi-GB into RAM)

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
- governance notes (classification/license/redaction)

---

<a id="adding-a-new-script-template"></a>

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
🧬 Determinism: <seed + idempotency key behavior>
🧾 Provenance: <STAC/DCAT/PROV links or IDs, if applicable>
🏷️ Classification: <how computed/propagated>
⚖️ License: <how computed/propagated>
🧪 Tests: <where/how verified>
```

> [!TIP]
> If a script is “important enough to be scary,” it’s important enough to have:
> - `--dry-run`
> - `--confirm`
> - a unit-testable core function in `api/src/`
> - a policy gate in CI

---

<a id="troubleshooting"></a>

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
  - confirm schema/profile versions match API contracts
- 🧷 **Classification/license mismatch**
  - treat as a governance bug; fix before publishing artifacts
- 🧬 **Non-deterministic outputs**
  - ensure `--seed` is wired and inputs are pinned
  - ensure the script doesn’t embed timestamps in output data (except manifests)

---

<a id="project-reference-library--script-rules"></a>

## 📚 Project reference library → script rules

> Requirement: this section maps **every project file** to a concrete `api/scripts` convention, guardrail, or workflow expectation.

<details>
<summary><strong>🧠 Expand: Influence map (all project files)</strong></summary>

| Project file | Script impact (what it changes here) |
|---|---|
| `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx` | 🧭 Canonical system posture: standards-first (STAC/DCAT/PROV), graph-as-reference, API boundary discipline, and “publish only via cataloged evidence.” |
| `Latest Ideas-1.docx` | 🤖 W·P·E agent safety blueprint: deterministic seeds, idempotency keys, kill-switch, PR-only promotion, SBOM/attestations, telemetry and reproducibility checks. |
| `MARKDOWN_GUIDE_v13.md.gdoc` | 🧾 Repo-level invariants: canonical pipeline ordering (Data → Catalogs → Graph → API → UI → Narrative), contract-first + evidence-first expectations. |
| `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx` | 📘 Doc rigor in scripts: consistent templates, metadata discipline, checklists, and clear side-effect documentation (Markdown as an auditable artifact). |
| `Data Spaces.pdf` | 🧩 Pointer-over-payload: scripts generate catalogs + references (don’t duplicate huge datasets), and enforce access-policy thinking at boundaries. |
| `Introduction to Digital Humanism.pdf` | 🧑‍🤝‍🧑 Human-centered governance: transparency, agency, audit trails, and avoiding privacy downgrade or “automation overreach.” |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | 🔁 Systems thinking: explicit state transitions, feedback loops (telemetry → validation → improvement), bounded automation. |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | ⚖️ Audit-ready ML: record model/version/config, ensure explainability boundaries, don’t over-claim outputs, keep provenance first-class. |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | 🧠 ML ops separation: training/finetuning in pipelines, not API runtime; emit model-card-friendly artifacts + provenance + evaluation summaries. |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | 🧮 Simulation governance: reproducibility, run manifests, scenario metadata, verification/validation hooks, sensitivity runs. |
| `Generalized Topology Optimization for Structural Design.pdf` | 🧱 Optimization artifacts: scripts must capture objectives/constraints/solver settings and treat results as governed evidence outputs. |
| `Understanding Statistics & Experimental Design.pdf` | 🧪 Experimental clarity: scripts must state assumptions, sampling design, uncertainty, and avoid misleading inference. |
| `regression-analysis-with-python.pdf` | 📈 Regression runner rules: residual diagnostics, assumption checks, coefficients/uncertainty outputs, and repeatable feature pipelines. |
| `Regression analysis using Python - slides-linear-regression.pdf` | 🧾 Standard output envelope: consistent metrics (R²/MAE/RMSE), coefficients table, diagnostics references for UI/CI consumption. |
| `think-bayes-bayesian-statistics-in-python.pdf` | 🎲 Bayesian runner rules: priors disclosed, posterior summaries with credible intervals, diagnostics and provenance recorded. |
| `graphical-data-analysis-with-r.pdf` | 🔎 EDA scripts: deterministic diagnostics plots/tables, outlier surfacing, “what changed” summaries suitable for PR review. |
| `Spectral Geometry of Graphs.pdf` | 🕸️ Graph analytics discipline: bounded, explainable metrics; avoid expensive global operations by default; treat metrics as evidence artifacts. |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | 🗄️ DB scripts: safe migrations, backup/restore discipline, indexing awareness, avoid dangerous defaults, bounded maintenance. |
| `Scalable Data Management for Future Hardware.pdf` | ⚡ Scalability: incremental builds, streaming I/O, bounded memory/concurrency, avoid accidental `O(N)` on massive datasets. |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | 🧵 Concurrency hygiene: idempotent job runners, bounded worker pools, backpressure, safe retries, predictable cancellation. |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | 🛰️ Remote sensing scripts: parameterized exports, reproducible AOI/time ranges, catalog emission, and traceable compute steps. |
| `python-geospatial-analysis-cookbook.pdf` | 🧭 Geo correctness: explicit CRS/SRID handling, geometry validation, careful transforms at boundaries, avoid silent reprojection bugs. |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | 🗺️ Cartographic honesty: quicklook/tile scripts must avoid misleading symbology, document styling decisions, include legend/scale where applicable. |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | 📱 Mobile constraints: quicklooks/tiles optimized for bandwidth; offline bundles; context-first design and performance budgets. |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | 🖼️ Image pipeline: choose formats intentionally (e.g., PNG for crisp linework, JPEG for photos), optimize size, avoid meaning-destroying compression. |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | 🧊 3D asset tooling: coordinate sanity, safe loaders, progressive enhancement, “3D optional” with graceful fallback artifacts. |
| `responsive-web-design-with-html5-and-css3.pdf` | 📐 UI asset generation: responsive budgets, small payloads, predictable filenames and caching; don’t break mobile rendering. |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | 🛡️ Defensive posture: least privilege, segmentation assumptions, safe network operations, harden scripts like production tools. |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | 🧷 Defensive coding mindset: treat file inputs as hostile, avoid unsafe parsing patterns, fuzz-awareness for ingestion scripts. |
| `A programming Books.pdf` | 📚 Contributor shelf: language-agnostic craft + future tooling adaptability (scripts remain small, readable, well-documented). |
| `B-C programming Books.pdf` | 🧪 DataOps for geospatial: schema + geometry validation in CI, repeatable pipeline checks, strong “data tests” culture. |
| `D-E programming Books.pdf` | 📚 Contributor shelf: algorithmic literacy informs performance + correctness expectations in scripts. |
| `F-H programming Books.pdf` | 📚 Contributor shelf |
| `I-L programming Books.pdf` | 📚 Contributor shelf (core language/runtime concepts that inform robust tooling) |
| `M-N programming Books.pdf` | 📚 Contributor shelf |
| `O-R programming Books.pdf` | 📚 Contributor shelf |
| `S-T programming Books.pdf` | 🛡️ Security awareness: never leak DB errors, avoid unsafe query construction, and treat admin tooling as attack surface. |
| `U-X programming Books.pdf` | 📚 Contributor shelf |

</details>

---

<!--
Maintainers’ TODOs ✅ (keep or remove):
- Add `api/.env.example` (safe defaults, no secrets).
- Add `scripts/_lib/safety.sh` with prod-block + confirm/dry-run utilities.
- Add `scripts/_lib/run_manifest.py` and require it for any artifact-producing script.
- Add `scripts/policy/` wrappers (OPA/Conftest) and wire into CI.
- Add `scripts/telemetry/` schema + validation for JSONL operational events (optional).
- Decide invocation style: direct scripts vs Makefile targets (either is fine; just standardize).
- Add CI workflows that call scripts/ci/* as stable entrypoints.
- Add a “repro check” job that rebuilds artifacts and compares hashes.
-->