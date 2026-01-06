# 🧰 Kansas Frontier Matrix (KFM) — API Scripts (`api/scripts`)

[![Scripts](https://img.shields.io/badge/KFM-scripts-1f6feb)](#-kansas-frontier-matrix-kfm--api-scripts-apiscripts)
[![Language](https://img.shields.io/badge/bash-%E2%9C%85-4EAA25?logo=gnubash&logoColor=white)](#-script-standards)
[![Language](https://img.shields.io/badge/python-%E2%9C%85-3776AB?logo=python&logoColor=white)](#-script-standards)
[![Ops](https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white)](#-local-dev--ops-shortcuts)
[![Safety](https://img.shields.io/badge/safety-deny--by--default-critical)](#-safety--governance-guardrails)

> 🧭 **Purpose:** This folder contains **operational & developer scripts** that support the KFM API stack — bootstrapping local dev, running maintenance tasks, importing governed datasets, generating catalogs/lineage artifacts, and performing repeatable admin operations.  
> 🧱 **Non-goal:** runtime business logic. Keep domain/use-case logic in `api/src/` (services/use-cases), not here.

---

## 📌 Quick links

- [🧠 What belongs in `api/scripts`](#-what-belongs-in-apiscripts)
- [🧱 Directory layout](#-directory-layout-recommended)
- [🚦 Safety & governance guardrails](#-safety--governance-guardrails)
- [🚀 Local dev & ops shortcuts](#-local-dev--ops-shortcuts)
- [🛰️ Data & catalog workflows](#️-data--catalog-workflows-stacdcatprov)
- [🗄️ Database & graph tasks](#️-database--graph-tasks)
- [🧪 QA / CI helpers](#-qa--ci-helpers)
- [🧩 Script standards](#-script-standards)
- [➕ Adding a new script](#-adding-a-new-script-template)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 Project reference library](#-project-reference-library)

---

## 🧠 What belongs in `api/scripts`

This folder is for **repeatable automation** that is *close to the API stack*, for example:

- 🏗️ **Environment bootstrap:** create venvs, install deps, validate toolchain
- 🐳 **Ops glue:** bring up/down local dependencies (Postgres/Neo4j/Redis), run health checks
- 🗄️ **DB/Graph admin:** migrations, seed data, role setup, integrity checks
- 🛰️ **Catalog production:** build/validate STAC/DCAT/PROV artifacts and sync references into the graph
- 🧪 **CI-friendly tasks:** contract checks, smoke tests, schema validation gates
- 📦 **Build tooling:** generate OpenAPI clients, bundle schemas, produce SBOMs (optional)

> [!IMPORTANT]
> If the script contains **domain rules**, a **simulation algorithm**, or **redaction/classification logic** — that belongs in `api/src/services/` (and should be importable/testable).  
> Scripts should orchestrate; core code should **live in the app**.

---

## 🧱 Directory layout (recommended)

> 🧩 If your repo differs, keep the same *intent*: scripts grouped by purpose, with shared helpers and clearly documented side-effects.

```text
📁 api/
└── 📁 scripts/
    ├── 📄 README.md                      # 📘 you are here
    ├── 📁 _lib/                          # 🧰 shared helpers (small + boring)
    │   ├── 📄 common.sh                  # strict-mode helpers, log formatting
    │   ├── 📄 env.sh                     # env loading, validation
    │   └── 📄 python.py                  # python helpers (paths, subprocess)
    ├── 📁 dev/                           # 🧑‍💻 local development convenience
    │   ├── 📄 up.sh                      # docker compose up
    │   ├── 📄 down.sh                    # docker compose down
    │   ├── 📄 reset.sh                   # ⚠️ destructive: reset local state
    │   └── 📄 smoke.sh                   # quick sanity checks
    ├── 📁 db/                            # 🗄️ Postgres tasks (migrate/seed/backup)
    │   ├── 📄 migrate.py
    │   ├── 📄 seed.py
    │   ├── 📄 backup.sh
    │   └── 📄 restore.sh
    ├── 📁 graph/                         # 🧠 Neo4j / graph sync tasks
    │   ├── 📄 sync_catalog.py
    │   └── 📄 validate_refs.py
    ├── 📁 catalogs/                      # 🛰️ STAC/DCAT/PROV generation + validation
    │   ├── 📄 build_stac.py
    │   ├── 📄 build_dcat.py
    │   ├── 📄 build_prov.py
    │   └── 📄 validate_catalogs.py
    ├── 📁 contracts/                     # 📜 OpenAPI/Schema gates + client generation
    │   ├── 📄 lint_openapi.py
    │   ├── 📄 validate_jsonschema.py
    │   └── 📄 generate_client.sh
    └── 📁 ci/                            # 🧪 CI entrypoints (keep them stable)
        ├── 📄 check.sh
        └── 📄 test_contracts.sh
```

---

## 🚦 Safety & governance guardrails

KFM scripts often have **privileged access** (DB/graph/secrets). Treat them like production code.

> [!CAUTION]
> **Default posture: “deny-by-default”**  
> Scripts must not accidentally export sensitive data, modify production state, or weaken governance controls.

### ✅ Required safety behaviors

- 🔐 **No secrets in repo:** never print tokens/keys; never commit `.env`; never echo credentials
- 🧷 **Classification propagation:** outputs must be at least as restrictive as inputs (no “privacy downgrade”)
- 🧼 **Redaction is not optional:** if a script produces artifacts consumed by the API/UI, apply the same redaction rules as the API boundary
- 🧯 **Destructive operations are explicit:**
  - require `--confirm` or `KFM_CONFIRM=1`
  - support `--dry-run` where possible
  - log “what will change” before making changes
- 🧾 **Provenance-first:** any generated dataset views should be able to point back to evidence (STAC/DCAT/PROV IDs/links)
- 🧪 **Validation gates:** schema checks and invariants should fail fast with non-zero exit codes

> [!IMPORTANT]
> If you discover a security issue in scripts, **do not** open a public GitHub Issue/PR comment.  
> Follow the repo’s security policy in `SECURITY.md` (or `docs/security/` if present). 🛡️

---

## 🚀 Local dev & ops shortcuts

### 1) Prereqs ✅
- 🐍 Python (recommended: project’s supported version)
- 🐳 Docker + Docker Compose
- 🧰 Basic CLI tooling: `bash`, `curl`, `jq` (recommended)

### 2) Environment variables (typical)

> Keep a **safe sample** at `api/.env.example` and load real values locally via `api/.env` (gitignored).

```bash
# App
KFM_ENV=dev
KFM_LOG_LEVEL=INFO

# Data stores
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
<summary><strong>💡 Recommended “make” wrappers</strong></summary>

If you use a repo-level `Makefile`, keep script invocation consistent:

```makefile
api-up:
\tcd api && ./scripts/dev/up.sh

api-smoke:
\tcd api && ./scripts/dev/smoke.sh
```

</details>

---

## 🛰️ Data & catalog workflows (STAC/DCAT/PROV)

KFM’s pipeline expects a canonical flow (data → catalogs → graph → API). Scripts are allowed to automate **catalog generation** and **graph sync**, but should not bypass governance.

### Common tasks

- 🗂️ Build STAC Items/Collections (assets, geometry, timestamps, checksum hints)
- 🧾 Build DCAT dataset views (discovery-oriented metadata)
- 🧬 Build PROV lineage bundles (process + inputs + outputs)
- ✅ Validate catalogs (schema + project invariants)
- 🧠 Sync **references** into the graph (graph points back to catalogs; doesn’t replace them)

Example flow (illustrative):

```bash
# 1) Build catalogs
python ./scripts/catalogs/build_stac.py   --in ./data/raw --out ./data/catalogs/stac
python ./scripts/catalogs/build_dcat.py   --stac ./data/catalogs/stac --out ./data/catalogs/dcat
python ./scripts/catalogs/build_prov.py   --runs ./data/runs --out ./data/catalogs/prov

# 2) Validate
python ./scripts/catalogs/validate_catalogs.py --root ./data/catalogs

# 3) Sync references to graph
python ./scripts/graph/sync_catalog.py --stac ./data/catalogs/stac --dcat ./data/catalogs/dcat --prov ./data/catalogs/prov
```

> [!TIP]
> Prefer **immutable outputs** for catalogs (content-addressed paths or checksums) so lineage and reproducibility stay strong 🧬.

---

## 🗄️ Database & graph tasks

### Postgres (migrations, seed, backup)

Recommended script behaviors:
- Migrations are **ordered** and **tracked**
- Seeding uses **non-production** fixtures only
- Backups are **encrypted** (if stored) and never include secrets in logs

Examples:

```bash
# migrate up
python ./scripts/db/migrate.py up

# seed dev data
python ./scripts/db/seed.py --fixture dev_minimal

# backup local db
./scripts/db/backup.sh --out ./backups/kfm-local.sql.gz
```

### Neo4j / graph sync

Graph scripts should:
- treat the graph as a **reference index** (not the source of truth)
- never store sensitive raw payloads if catalogs already hold them
- preserve **stable IDs** (STAC/DCAT/PROV identifiers) to support traceability

Example:

```bash
python ./scripts/graph/validate_refs.py --fail-on-orphans
```

---

## 🧪 QA / CI helpers

Use scripts here to keep CI stable and readable:

- 📜 OpenAPI linting + contract checks
- ✅ JSON Schema validation (requests/responses/envelopes)
- 🔍 “Invariant checks” (pipeline ordering, classification propagation)
- 🧨 Security-focused tests (redaction regression, authz guardrails)

Example:

```bash
./scripts/ci/check.sh
./scripts/ci/test_contracts.sh
```

> [!NOTE]
> CI scripts should be **deterministic**, **fast**, and **non-interactive**. Avoid prompts; use flags/env vars instead.

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
- `--help` support (or clear usage on bad args)
- consistent logging (timestamp + level)
- non-zero exit codes on failure
- no silent destructive actions

### Python scripts ✅
Prefer importable modules (so logic is testable):

- scripts call into `api/src/...` (services/use-cases) rather than re-implementing logic
- parse args with `argparse` (or Typer, if used in-repo)
- validate env vars up-front and fail fast

### Naming conventions 🏷️
- `verb_noun` or `verb-noun` (pick one and stick to it)
  - `build_stac.py`, `sync_catalog.py`, `backup.sh`, `restore.sh`
- group by intent (`db/`, `graph/`, `catalogs/`, `contracts/`, `dev/`, `ci/`)

### Required documentation 📘
Every script must include:
- short description
- inputs/outputs
- side-effects
- required env vars
- examples

---

## ➕ Adding a new script (template)

Copy/paste this header pattern into new scripts:

```text
📌 Script: <name>
🎯 Goal: <what it does>
📥 Inputs: <files/urls/db tables>
📤 Outputs: <files/db changes>
⚠️ Side effects: <writes/deletes/network calls>
🔐 Required env: <KFM_* vars>
✅ Safety: <dry-run/confirm/idempotent?>
🧪 Tests: <where/how verified>
```

> [!TIP]
> If a script is “important enough to be scary”, it’s important enough to have:
> - `--dry-run`
> - `--confirm`
> - a unit-testable core function in `api/src/`

---

## 🧯 Troubleshooting

### Common issues

- 🐳 **Docker not running**
  - Confirm: `docker ps`
  - Restart Docker Desktop / daemon
- 🗄️ **Postgres connection failures**
  - Check `KFM_POSTGRES_URL`
  - Confirm port mappings in compose
- 🧠 **Neo4j auth errors**
  - Verify `KFM_NEO4J_USER/PASSWORD`
  - Confirm `bolt://` URI and container health
- 🧪 **Schema validation fails**
  - Rebuild catalogs
  - Confirm schema versions match the API contracts
- 🧷 **Classification/redaction mismatch**
  - Treat as a governance bug; fix before shipping artifacts to the UI/API

---

## 📚 Project reference library

These scripts and conventions are shaped by the project’s broader engineering + geospatial foundations:

<details>
<summary><strong>🏗️ Architecture & engineering</strong></summary>

- Kansas Frontier Matrix (KFM) – Master Technical Specification  
- Clean Architectures in Python  
- Implementing Programming Languages (Compilers/Interpreters)  
- Command Line Kung Fu (Bash scripting & shell ops)  
- Introduction to Docker  

</details>

<details>
<summary><strong>🗄️ Data systems</strong></summary>

- PostgreSQL Notes for Professionals  
- MySQL Notes for Professionals  

</details>

<details>
<summary><strong>🌎 GIS / remote sensing / catalogs</strong></summary>

- Geographic Information System Basics  
- Python Geospatial Analysis Cookbook  
- Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals & Applications)  
- Google Earth Engine Applications  

</details>

<details>
<summary><strong>🌐 Web / visualization (context for outputs)</strong></summary>

- Google Maps JavaScript API Cookbook  
- WebGL Programming Guide  
- Responsive Web Design with HTML5 and CSS3  

</details>

---

<!--
Maintainers’ TODOs ✅ (keep or remove):
- Add an api/.env.example (safe defaults, no secrets).
- Add a scripts/_lib/env.sh with env validation + redaction/classification guards.
- Decide whether scripts are invoked directly or via Makefile targets.
- Add CI workflows that call scripts/ci/* as stable entrypoints.
-->