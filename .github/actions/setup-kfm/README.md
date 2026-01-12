<a id="top"></a>

# 🧰🧩 `setup-kfm` — Standard CI Bootstrap for Kansas Frontier Matrix (Python + Node + GIS)
**Kansas Frontier Matrix (KFM)** • `.github/actions/setup-kfm/README.md`

[![Composite Action](https://img.shields.io/badge/action-composite-informational)](#-what-this-action-does)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Node](https://img.shields.io/badge/node-18%2B-brightgreen)
![GIS](https://img.shields.io/badge/GIS-GDAL%20%7C%20PROJ%20%7C%20GEOS-orange)
![Caches](https://img.shields.io/badge/caching-pip%20%7C%20npm-success)
![Least Privilege](https://img.shields.io/badge/security-least--privilege-black)
![Boring CI](https://img.shields.io/badge/CI-boring%20by%20design-success)

> `setup-kfm` is a **repo-local composite action** that standardizes the **runner environment** across KFM workflows: Python + Node + caching + (optional) GIS system libraries.
>
> KFM’s order is the constraint that makes the system governable:  
> 🧰 **ETL** → 🗂️ **Catalogs (STAC/DCAT/PROV)** → 🕸️ **Graph** → 🔌 **API** → 🌐 **UI** → 🎬 **Story Nodes** → 🧠 **Focus Mode**  
>
> ✅ Use this action anywhere you would otherwise copy/paste: `setup-python`, `setup-node`, caches, and “install GIS libs”.

---

## 🧾 Action metadata

| Field | Value |
|---|---|
| 🧩 Action name | `kfm/setup-kfm` |
| 🧱 Type | Composite Action |
| 📁 Folder | 📁 `.github/actions/setup-kfm/` |
| 📄 Action file | 📄 `.github/actions/setup-kfm/action.yml` *(implementation source of truth)* |
| 📄 Docs | 📄 `.github/actions/setup-kfm/README.md` |
| ✅ Status | Spec ✅ *(expected contract; keep aligned with `action.yml`)* |
| 🗓️ Last updated | **2026-01-12** |
| 🎯 Goal | One consistent bootstrap for Python/Node/GIS across CI lanes |
| 🧪 Typical lanes | PR CI • nightly validation • integration (PostGIS) |
| 🔐 Default stance | Least privilege • **no secrets required** • safe on fork PRs |
| 🐧 Runner assumptions | Best on `ubuntu-latest` (GIS/db installs are Linux-only) |

> [!NOTE]
> Composite actions exist to bundle repeatable steps into a single reusable unit and reduce workflow YAML drift.  
> That’s the point of `setup-kfm`: **make “boring setup” consistent across jobs.**

---

## ⚡ Quick links

| Need | Go |
|---|---|
| 🧩 Actions hub | 📄 [`../README.md`](../README.md) |
| 🧪 Workflows hub | 📄 [`../../workflows/README.md`](../../workflows/README.md) |
| 🤝 Collaboration rules | 📄 [`../../README.md`](../../README.md) |
| 🛡️ Security policy | 📄 [`../../../SECURITY.md`](../../../SECURITY.md) |
| ✅ Catalog quick gate | 📄 [`../catalog-qa/README.md`](../catalog-qa/README.md) |
| 🧾 Full metadata validation | 📄 [`../metadata-validate/README.md`](../metadata-validate/README.md) |
| 🧬 Provenance enforcement | 📄 [`../provenance-guard/README.md`](../provenance-guard/README.md) |
| 🧑‍⚖️ Policy-as-code gate | 📄 [`../policy-gate/README.md`](../policy-gate/README.md) |
| 🐳 Standard image build | 📄 [`../docker-build/README.md`](../docker-build/README.md) |

---

<details>
<summary><strong>📌 Table of contents</strong></summary>

- [🎯 What this action does](#-what-this-action-does)
- [🧠 Why KFM needs a dedicated setup action](#-why-kfm-needs-a-dedicated-setup-action)
- [🧭 Where this fits in the repo](#-where-this-fits-in-the-repo)
- [🧱 What it installs and configures](#-what-it-installs-and-configures)
- [⚙️ Inputs](#️-inputs)
- [📤 Outputs](#-outputs)
- [✅ Usage patterns](#-usage-patterns)
- [🧩 Target folder shape](#-target-folder-shape)
- [🧯 Troubleshooting](#-troubleshooting)
- [🔐 Security & determinism notes](#-security--determinism-notes)
- [📚 Reference library (project files)](#-reference-library-project-files)

</details>

---

## 🎯 What this action does

`setup-kfm` is meant to be the **first step** in most KFM CI jobs.

### ✅ Baseline features (expected contract)
- 🐍 Set up **Python** (version configurable)
- 🟩 Set up **Node** (version configurable) — important for the `web/` UI build lane
- ♻️ Enable **dependency caching**
  - pip cache for Python tooling / validators / ETL
  - npm cache for the frontend workspace
- 🧭 Export CI-stabilizing environment flags (non-secret; “boring defaults”)
- 🗺️ Optional **GIS native deps** on Linux runners:
  - GDAL / PROJ / GEOS (helps avoid brittle installs for geospatial Python libs and CLI tooling)
- 🗄️ Optional **db client tools** for integration lanes:
  - `postgresql-client` (`psql`, `pg_isready`) for smoke checks against PostGIS service containers

> [!IMPORTANT]
> This action should **not** do domain logic (ETL, validation, publishing).  
> It only prepares the environment so domain tools/actions run the same everywhere.

---

## 🧠 Why KFM needs a dedicated setup action

KFM is a multi-stack system:
- 🌐 **Frontend UI** is a web app (React) with mapping (MapLibre) and optional 3D (Cesium).
- 🧰 **ETL / tooling / validation** is Python-heavy and often geospatial.
- 🗄️ **Data services** commonly include PostgreSQL/PostGIS for spatial workloads.
- 🧪 CI is expected to be robust (tests, static analysis, and repeatable runs).

Without a shared bootstrap, workflows drift:
- different Python/Node versions
- mismatched caching and lockfiles
- ad-hoc GIS package installs that “work once”
- inconsistent environment flags (flake city)

`setup-kfm` exists to make the boring part **boring and consistent**.

---

## 🧭 Where this fits in the repo

KFM’s canonical “shape” puts different stacks in predictable places. This action supports those lanes:

```text
🏠 repo/
├─ 📁 src/
│  ├─ 📁 pipelines/        # 🧰 ETL + ingestion
│  ├─ 📁 server/           # 🔌 API boundary
│  └─ 📁 graph/            # 🕸️ graph ingest/build
├─ 📁 web/                 # 🌐 Frontend (React + MapLibre; optional Cesium)
├─ 📁 tools/
│  └─ 📁 validation/       # ✅ gates + QA tooling
└─ 📁 data/                # 🗂️ governed artifacts (catalogs, prov, processed outputs)
````

> [!TIP]
> If a workflow touches `web/`, you almost always want Node + npm cache.
> If it touches geospatial pipelines/validation, you often want GIS system deps on Linux.

---

## 🧱 What it installs and configures

### 🐍 Python

Expected behavior:

* uses `actions/setup-python` with a pinned `python_version`
* enables pip caching (when enabled)
* sets “CI-safe” defaults (e.g., non-interactive, predictable output)

**Recommended repo convention (not enforced):**

* prefer lockfiles/pins (`requirements*.txt`, `pyproject.toml` + lock) for determinism
* keep “dev tools” in a separate requirements file if needed (`requirements-dev.txt`)

### 🟩 Node

Expected behavior:

* uses `actions/setup-node` with a pinned `node_version`
* enables npm caching using `cache-dependency-path` (defaults to `web/package-lock.json`)

**Recommended repo convention:**

* commit your lockfile (`package-lock.json` / pnpm lockfile)
* keep frontend builds under `web/` (so caching stays scoped)

### 🗺️ GIS dependencies (optional; Linux only)

Geospatial stacks frequently rely on **GDAL + GEOS + PROJ**. When Python wheels aren’t enough (or you build from source), these system libraries matter.

When `install_gis_deps=true`, install common packages such as:

* `gdal-bin`, `libgdal-dev`
* `proj-bin`, `libproj-dev`
* `libgeos-dev`

Optional helpers (often useful in CI tooling):

* `jq`, `yq`, `zip`, `unzip`

> [!NOTE]
> Keep GIS installs opt-in. Many PR lanes don’t need them — but when they do, this prevents “native dependency roulette.”

### 🗄️ DB client tools (optional; Linux only)

When `install_db_tools=true`, install:

* `postgresql-client`

This enables:

* `pg_isready` health checks
* `psql` smoke queries against service containers (e.g., PostGIS)

---

## ⚙️ Inputs

> GitHub Actions inputs are strings. Use `"true"` / `"false"` for booleans.

| Input                       | Required | Default                 | Description                                          |
| --------------------------- | -------: | ----------------------- | ---------------------------------------------------- |
| `python_version`            |        ❌ | `3.12`                  | Python version to install (supports 3.10+)           |
| `node_version`              |        ❌ | `20`                    | Node version to install (supports 18+)               |
| `enable_pip_cache`          |        ❌ | `"true"`                | Enable pip caching                                   |
| `enable_npm_cache`          |        ❌ | `"true"`                | Enable npm caching                                   |
| `npm_cache_dependency_path` |        ❌ | `web/package-lock.json` | Lockfile path for npm caching                        |
| `web_workdir`               |        ❌ | `web`                   | Frontend directory (for convenience in commands)     |
| `install_gis_deps`          |        ❌ | `"false"`               | Install GDAL/PROJ/GEOS system deps (Linux only)      |
| `install_db_tools`          |        ❌ | `"false"`               | Install `postgresql-client` (Linux only)             |
| `extra_apt_packages`        |        ❌ | *(empty)*               | Space-separated additional apt packages (Linux only) |
| `pip_upgrade`               |        ❌ | `"true"`                | Run `python -m pip install -U pip`                   |
| `print_versions`            |        ❌ | `"true"`                | Print tool versions (safe + audit-friendly)          |

> [!TIP]
> Keep defaults conservative; enable heavy system installs only in workflows that actually need them.

---

## 📤 Outputs

| Output   | Meaning                                |
| -------- | -------------------------------------- |
| `python` | Resolved Python version string         |
| `node`   | Resolved Node version string           |
| `gdal`   | GDAL version if installed (else empty) |
| `proj`   | PROJ version if installed (else empty) |
| `geos`   | GEOS version if installed (else empty) |

> [!NOTE]
> Outputs are meant for logs, reports, and provenance/build-info tooling. Don’t use them as “secrets” (they are not).

---

## ✅ Usage patterns

### 1) 🧪 Python CI job (fast PR lane)

```yaml
steps:
  - uses: actions/checkout@v4

  - name: 🧰 Setup KFM (Python-only)
    uses: ./.github/actions/setup-kfm
    with:
      python_version: "3.12"
      enable_pip_cache: "true"
      enable_npm_cache: "false"
      install_gis_deps: "false"
      install_db_tools: "false"

  - name: Install deps
    run: |
      python -m pip install -U pip
      pip install -r requirements-dev.txt

  - name: Tests
    run: pytest -q
```

---

### 2) 🌐 Web UI job (frontend lane)

```yaml
steps:
  - uses: actions/checkout@v4

  - name: 🧰 Setup KFM (Web)
    uses: ./.github/actions/setup-kfm
    with:
      node_version: "20"
      enable_pip_cache: "false"
      enable_npm_cache: "true"
      npm_cache_dependency_path: "web/package-lock.json"

  - name: Install + build (web)
    working-directory: web
    run: |
      npm ci
      npm run build
```

---

### 3) 🗺️ GIS-heavy lane (raster/vector tooling)

```yaml
steps:
  - uses: actions/checkout@v4

  - name: 🧰 Setup KFM (GIS deps)
    uses: ./.github/actions/setup-kfm
    with:
      python_version: "3.12"
      install_gis_deps: "true"
      extra_apt_packages: "jq unzip"

  - name: Install deps
    run: |
      pip install -r requirements.txt

  - name: Run ETL / geo validation
    run: |
      python -m tools.validation.some_pipeline --help
```

---

### 4) 🧬 Integration lane (PostGIS service containers)

```yaml
steps:
  - uses: actions/checkout@v4

  - name: 🧰 Setup KFM (db tools)
    uses: ./.github/actions/setup-kfm
    with:
      python_version: "3.12"
      install_db_tools: "true"

  - name: Wait for Postgres
    run: |
      pg_isready -h localhost -p 5432

  - name: Smoke query
    env:
      PGPASSWORD: postgres
    run: |
      psql -h localhost -U postgres -d postgres -c "select version();"
```

---

### 5) 🧪 Matrix pattern (CI robustness)

If you want compatibility confidence (or you’re hardening promotion lanes), use a matrix:

```yaml
strategy:
  fail-fast: false
  matrix:
    python: ["3.10", "3.11", "3.12"]

steps:
  - uses: actions/checkout@v4

  - name: 🧰 Setup KFM
    uses: ./.github/actions/setup-kfm
    with:
      python_version: ${{ matrix.python }}
      enable_npm_cache: "false"
```

---

## 🧩 Target folder shape

```text
📁 .github/
└─ 🧩📁 actions/
   └─ 🧰📁 setup-kfm/
      ├─ 📄 action.yml
      └─ 📄 README.md   👈 you are here
```

---

## 🧯 Troubleshooting

### “pip install failed building wheels (GDAL/PROJ/GEOS)”

Symptoms:

* compile errors for `rasterio`, `fiona`, `shapely`, etc.

Fixes:

* run `setup-kfm` with `install_gis_deps: "true"`
* ensure Ubuntu runner is used (`ubuntu-latest`)
* prefer wheel-backed versions where possible (pin versions that ship wheels)

---

### “npm cache didn’t hit”

Common causes:

* lockfile path mismatch
* using pnpm/yarn but caching npm

Fixes:

* set `enable_npm_cache: "true"`
* ensure `npm_cache_dependency_path` matches your lockfile
* if you use pnpm, consider adding a sibling action (`setup-kfm-pnpm`) or extend this one

---

### “GDAL/PROJ versions drift over time”

Runner images evolve.

Fixes:

* pin GIS deps via a container image (promotion lanes)
* prefer deterministic release lanes via `docker-build` with digest-pinned base images
* record versions (print outputs; include them in build-info / PROV for traceability)

---

### “Action works locally but fails in CI”

Check:

* runner OS (apt installs are Linux-only)
* job permissions (`contents: read` is enough)
* working directories (`web/` vs repo root)
* lockfile presence (missing lockfiles make caching + installs less deterministic)

---

## 🔐 Security & determinism notes

### ✅ Least privilege by default

Most jobs should run with:

```yaml
permissions:
  contents: read
```

This action should not require secrets and should be safe on fork PRs.

### ✅ Determinism is the point

* pin Python/Node versions
* rely on lockfiles (pip pins / package-lock)
* keep caching consistent so CI behaves repeatably

### ✅ Network hygiene

* keep downloads minimal and pinned
* avoid `curl | bash` patterns in CI; checksum-verify if unavoidable
* for promotion lanes, prefer toolchain containers (digest-pinned) for maximum repeatability

---

## 📚 Reference library (project files)

This action is informed by KFM’s core system docs (pipeline order + repo layout), plus practical tooling constraints from geospatial and CI references.

<details>
<summary><strong>📚 Project files that influence setup-kfm</strong></summary>

### 🧭 Canonical KFM direction (order + layout + stack)

* 📄 `MARKDOWN_GUIDE_v13.md(.gdoc)` — pipeline order + directory layout (ETL → catalogs → graph → API → UI)
* 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx` — testing/CI posture + web mapping stack notes

### 🗺️ GIS + tooling constraints (why GDAL/GEOS/PROJ appear)

* 📄 `python-geospatial-analysis-cookbook.pdf` — practical geospatial stack dependencies (GDAL/GEOS/PROJ)
* 📄 `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` — Postgres tooling context (`psql`, integration habits)

### 🧪 CI patterns (why composite actions + caching exist)

* 📄 `B-C programming Books.pdf` — composite actions, caching, secrets handling, matrix patterns

### 🛰️ Remote sensing & scale (why repeatable toolchains matter)

* 📄 `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

</details>
