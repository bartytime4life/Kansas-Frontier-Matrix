<a id="top"></a>

# 🧰🧩 `setup-kfm` — Standard CI Bootstrap for Kansas Frontier Matrix (Python + Node + GIS)

[![Composite Action](https://img.shields.io/badge/action-composite-informational)](#-what-this-action-does)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Node](https://img.shields.io/badge/node-18%2B-brightgreen)
![GIS](https://img.shields.io/badge/GIS-GDAL%20%7C%20PROJ%20%7C%20GEOS-orange)
![Caches](https://img.shields.io/badge/caching-pip%20%7C%20npm-success)
![Least Privilege](https://img.shields.io/badge/security-least--privilege-black)
![Boring CI](https://img.shields.io/badge/CI-boring%20by%20design-success)

> `setup-kfm` is a **repo-local composite action** that standardizes the **build environment** across KFM workflows.  
> It keeps CI/CD **predictable** and **repeatable** while KFM stays ambitious:  
> 🧭 **ETL → Metadata (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**
>
> ✅ Use it anywhere you would otherwise copy/paste: `setup-python`, `setup-node`, caches, and optional GIS tooling.

---

## 🧾 Action metadata

| Field | Value |
|---|---|
| 🧩 Action name | `kfm/setup-kfm` |
| 🧱 Type | Composite Action |
| 📁 Folder | `📁 .github/actions/setup-kfm/` |
| 📄 Action file | `📄 .github/actions/setup-kfm/action.yml` *(expected)* |
| 📄 Docs | `📄 .github/actions/setup-kfm/README.md` |
| ✅ Status | Active (spec + operating guide) |
| 🗓️ Last updated | **2026-01-10** |
| 🎯 Goal | One consistent “bootstrap” for Python/Node/GIS across workflows |
| 🔐 Default stance | Least privilege • safe on fork PRs (no secrets needed) |

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
| 🐳 Standard image build | 📄 [`../docker-build/README.md`](../docker-build/README.md) |

---

<details>
<summary><strong>📌 Table of contents</strong></summary>

- [🎯 What this action does](#-what-this-action-does)
- [🧠 Why KFM needs a dedicated setup action](#-why-kfm-needs-a-dedicated-setup-action)
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

### ✅ Baseline features (expected)
- 🐍 Set up **Python** (version configurable)
- 🟩 Set up **Node** (version configurable)
- ♻️ Enable **dependency caching**
  - `pip` cache (and optionally venv caching patterns)
  - `npm` cache for the `web/` workspace
- 🧭 Export consistent environment flags for CI stability
  - `PIP_DISABLE_PIP_VERSION_CHECK=1`, `PYTHONUNBUFFERED=1`, etc.
- 🧰 Optional **GIS native deps** on Linux runners:
  - GDAL / PROJ / GEOS (enables raster/vector tooling + Python wheels when builds occur)
- 🗄️ Optional **db tools** for integration lanes:
  - `postgresql-client` (psql) to sanity-check service containers

> [!IMPORTANT]
> This action should **not** do domain logic (ETL, validation, publishing).  
> It only prepares the environment so domain actions/tools run the same everywhere.

---

## 🧠 Why KFM needs a dedicated setup action

KFM touches multiple stacks at once:

- 🗺️ Geospatial processing often needs system libs (GDAL/PROJ/GEOS)
- 🛰️ Remote sensing and raster workflows lean on native dependencies and predictable environments
- 🌐 Web map UIs require Node tooling and build determinism
- 🧪 Modeling/analytics runs benefit from stable Python + pinned toolchains
- 🔐 CI/CD needs least privilege + predictable caching (avoid flaky installs)

A composite setup action prevents:
- YAML drift between workflows
- “works on my runner” failures
- inconsistent caching strategies
- ad-hoc dependency installation patterns

---

## 🧱 What it installs and configures

### 🐍 Python
- Uses `actions/setup-python` with pinned versions (workflow controls version)
- Enables pip caching for speed and repeatability
- Sets “CI-safe” env defaults (no interactive prompts, stable encoding)

### 🟩 Node
- Uses `actions/setup-node` with pinned versions
- Supports `web/` workspace caching (`package-lock.json`-based)

### 🗺️ GIS dependencies (optional)
For Ubuntu runners, optionally installs common system deps:

- `gdal-bin`, `libgdal-dev`
- `proj-bin`, `libproj-dev`
- `libgeos-dev`
- optional: `jq`, `yq`, `zip`, `unzip`

> These are **optional** because many repos can rely on wheels; but KFM frequently crosses into “native land,” and this makes CI less brittle.

### 🗄️ DB client tools (optional)
Installs `postgresql-client` so integration lanes can:
- check DB readiness (`psql`, `pg_isready`)
- run minimal “smoke queries” against PostGIS service containers

---

## ⚙️ Inputs

> GitHub Actions inputs are strings. Use `"true"` / `"false"` for booleans.

| Input | Required | Default | Description |
|---|---:|---|---|
| `python_version` | ❌ | `3.12` | Python version to install (supports 3.10+) |
| `node_version` | ❌ | `20` | Node version to install (supports 18+) |
| `enable_pip_cache` | ❌ | `"true"` | Enable pip cache |
| `enable_npm_cache` | ❌ | `"true"` | Enable npm cache |
| `npm_cache_dependency_path` | ❌ | `web/package-lock.json` | Lockfile path for npm caching |
| `web_workdir` | ❌ | `web` | Where frontend lives (for convenience) |
| `install_gis_deps` | ❌ | `"false"` | Install GDAL/PROJ/GEOS system deps (Linux only) |
| `install_db_tools` | ❌ | `"false"` | Install psql client tools (Linux only) |
| `extra_apt_packages` | ❌ | *(empty)* | Space-separated extra apt packages |
| `pip_upgrade` | ❌ | `"true"` | Run `python -m pip install -U pip` |
| `print_versions` | ❌ | `"true"` | Print tool versions (safe) |

> [!TIP]
> Keep defaults conservative; enable heavy system installs only in workflows that actually need them.

---

## 📤 Outputs

| Output | Meaning |
|---|---|
| `python` | Resolved Python version string |
| `node` | Resolved Node version string |
| `gdal` | GDAL version if installed (else empty) |
| `proj` | PROJ version if installed (else empty) |
| `geos` | GEOS version if installed (else empty) |

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
```

### 2) 🌐 Web UI job (frontend lane)

```yaml
steps:
  - uses: actions/checkout@v4

  - name: 🧰 Setup KFM (Web)
    uses: ./.github/actions/setup-kfm
    with:
      python_version: "3.12"   # optional; keep if tooling uses python scripts
      node_version: "20"
      enable_pip_cache: "false"
      enable_npm_cache: "true"
      npm_cache_dependency_path: "web/package-lock.json"
```

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
```

### 4) 🧬 Integration lane (PostGIS service containers)

```yaml
steps:
  - uses: actions/checkout@v4

  - name: 🧰 Setup KFM (db tools)
    uses: ./.github/actions/setup-kfm
    with:
      python_version: "3.12"
      install_db_tools: "true"
```

> [!NOTE]
> Even with `install_db_tools=true`, prefer **service containers** for real PostGIS/Neo4j integration.  
> This action is about consistent client tooling + predictable environments.

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
- errors compiling `rasterio`, `fiona`, `shapely`, etc.

Fixes:
- run setup-kfm with `install_gis_deps: "true"`
- ensure Ubuntu runner is used (`ubuntu-latest`)
- prefer wheels when possible (pin deps to versions with wheels)

---

### “npm cache didn’t hit”
Common causes:
- lockfile path mismatch
- using pnpm/yarn but caching npm

Fixes:
- set `enable_npm_cache: "true"`
- ensure `npm_cache_dependency_path` matches your lockfile
- if you use pnpm, consider extending the action (or create `setup-kfm-pnpm`)

---

### “GDAL version is different between runs”
Runner images evolve over time.

Fixes:
- pin GIS deps via a container image (promotion lanes)
- prefer deterministic release lanes via `docker-build` with pinned base images
- treat system deps as part of your “toolchain provenance” (record versions in build-info / PROV)

---

### “Action works locally but fails in CI”
Check:
- runner OS (Linux required for apt installs)
- permissions (should be `contents: read`)
- whether a workflow uses a different working directory than expected

---

## 🔐 Security & determinism notes

### ✅ Least privilege by default
Most jobs should run with:

```yaml
permissions:
  contents: read
```

This action should not need secrets and should be safe on fork PRs.

### ✅ Deterministic outputs
- Prefer pinned versions for Python/Node
- Avoid time-based “latest” behaviors
- Print versions for auditing (safe, non-secret)

### ✅ Network hygiene
- Keep downloads limited and pinned
- Avoid `curl | bash` patterns in CI (or checksum-verify if unavoidable)
- Prefer toolchain containers for promotion lanes (digest-pinned)

---

## 📚 Reference library (project files)

KFM’s “bootstrap philosophy” is shaped by the project’s broader constraints:
- reproducibility + validation discipline (modeling & simulation)
- geospatial correctness (CRS/PROJ/GDAL realities)
- scaling and robustness (deterministic lanes)
- governance and security posture (least privilege, supply-chain awareness)

<details>
<summary><strong>📚 Reading pack that influences this action</strong></summary>

### 🧭 Canonical KFM direction
- 📄 `docs/specs/Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`
- 📄 `docs/specs/MARKDOWN_GUIDE_v13.md(.gdoc)`
- 📄 `docs/specs/Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`
- 📄 `docs/specs/Latest Ideas.pdf`

### 🗺️ GIS + tooling constraints
- 📄 `docs/library/python-geospatial-analysis-cookbook.pdf`
- 📄 `docs/library/PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- 📄 `docs/library/making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- 📄 `docs/library/compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 🛰️ Remote sensing and large-scale workflows
- 📄 `docs/library/Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

### 🧪 Modeling and reproducibility discipline
- 📄 `docs/library/Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- 📄 `docs/library/Understanding Statistics & Experimental Design.pdf`
- 📄 `docs/library/think-bayes-bayesian-statistics-in-python.pdf`

### ❤️ Governance + security mindset
- 📄 `SECURITY.md`
- 📄 `docs/library/Data Spaces.pdf`
- 📄 `docs/library/Introduction to Digital Humanism.pdf`

</details>

---

<p align="right"><a href="#top">⬆️ Back to top</a></p>

