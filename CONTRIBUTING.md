# 🤝 Contributing to Kansas Frontier Matrix (KFM)

![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue.svg)
![Docs](https://img.shields.io/badge/docs-Markdown%20first-informational.svg)

**Last updated:** 2026-01-02

> [!NOTE]
> KFM is a multidisciplinary, GIS + data + modeling + human-centered initiative. We care about **reproducibility, clarity, and real-world usability**—not just “it runs on my machine.” 🌾🗺️🧠

---

## 🧭 Table of Contents

- [👋 Ways to contribute](#-ways-to-contribute)
- [🗺️ “KFM-first” principles](#️-kfm-first-principles)
- [🚀 Quick start setup](#-quick-start-setup)
- [🧪 Quality gates](#-quality-gates)
- [🧱 Architecture rules](#-architecture-rules)
- [🌍 Geospatial & remote sensing rules](#-geospatial--remote-sensing-rules)
- [🧠 Data science, ML, and statistics rules](#-data-science-ml-and-statistics-rules)
- [🧬 Modeling & simulation rules](#-modeling--simulation-rules)
- [🎨 Frontend & visualization rules](#-frontend--visualization-rules)
- [🗄️ Database & data management rules](#️-database--data-management-rules)
- [🔐 Security & privacy](#-security--privacy)
- [🧾 Git workflow + PR standards](#-git-workflow--pr-standards)
- [📝 Documentation standards](#-documentation-standards)
- [🏷️ Issue labels & triage](#️-issue-labels--triage)
- [📚 Project reference shelf](#-project-reference-shelf)

---

## 👋 Ways to contribute

You can contribute in **any** of these lanes:

- 🐛 **Bug fixes** (logic, data quality, UI issues, performance regressions)
- ✨ **Features** (new analysis modules, new map layers, new workflows)
- 🗺️ **GIS layers & ETL** (ingestion, transforms, QA, metadata)
- 🤖 **ML/AI** (model training, evaluation, inference integration, monitoring)
- 🧪 **Experiments** (validation studies, benchmarks, simulation experiments)
- 🎨 **Frontend** (React components, responsive layouts, WebGL overlays)
- 🔧 **Infra/DevOps** (Docker, orchestration, CI improvements, observability)
- 📚 **Documentation** (READMEs, tutorials, diagrams, “why” explanations)

> [!TIP]
> If you’re new: start with a small docs fix or a “good first issue” and learn the system boundaries as you go. ✅

---

## 🗺️ “KFM-first” principles

These are the project-wide expectations (applies to code, docs, and data):

- **Human-centered decision support** 🧑‍🌾  
  We build tools that *augment* human judgment. Make uncertainty visible; don’t overclaim.
- **Architecture > cleverness** 🧱  
  Keep core logic independent from frameworks/vendors. Prefer simple, testable modules.
- **Reproducibility is a feature** 🔁  
  Seeds, configs, dependencies, and data provenance must be documented.
- **Geospatial correctness matters** 🌍  
  CRS, units, and temporal alignment must be explicit.
- **Security & privacy by default** 🔐  
  Never commit secrets; avoid shipping PII; follow responsible disclosure.

---

## 🚀 Quick start setup

> [!NOTE]
> KFM supports a **Docker-first** workflow and a **local-first** workflow. Pick what fits your role.

### 🐳 Option A — Docker-first (recommended)

1. Install Docker / Docker Desktop  
2. Create your local env file:
   - Copy `.env.example` → `.env`
3. Bring the stack up (if compose files exist in this repo):
   ```bash
   docker compose up --build
   ```
4. Run tests/linters inside the container (or via `make`, `task`, or npm scripts if provided).

**Docker contribution expectations**
- Prefer multi-stage builds where possible.
- Don’t bake secrets into images; use env vars and secret mechanisms.
- Add healthchecks for long-running services if supported.

### 🧪 Option B — Local-first (Python + Node)

#### 1) System prerequisites (common)
- Git
- Python (3.x)
- Node.js (LTS)
- Docker (optional but helpful)
- Postgres + PostGIS (if running DB locally)
- GIS tooling (often needed): GDAL / PROJ (or run via Docker)

#### 2) Python environment
```bash
python -m venv .venv
# activate:
#   macOS/Linux: source .venv/bin/activate
#   Windows:     .venv\Scripts\activate
python -m pip install --upgrade pip
```

Install dependencies **based on what the repo uses**:
```bash
# If pyproject.toml exists (preferred)
python -m pip install -e ".[dev]"

# OR if requirements files exist
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

#### 3) Node environment (if frontend exists)
```bash
npm ci
# or: npm install
```

#### 4) Environment variables
- Copy `.env.example` → `.env`
- Never commit `.env` 🚫

---

## 🧪 Quality gates

Before opening a PR, you should be able to say “✅ green” on these:

### ✅ Pre-commit (recommended)
If the repo includes `.pre-commit-config.yaml`:
```bash
python -m pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### 🧼 Formatting & linting
Typical commands (use what the repo defines):
```bash
# Python
python -m black .
python -m ruff check .   # if ruff is used
python -m pylint your_package  # if used
python -m mypy .         # if types are used

# JS/TS
npm run lint
npm run format
```

### 🧪 Tests
```bash
# Python
pytest

# JS/TS
npm test
```

> [!IMPORTANT]
> If you change behavior, add/adjust tests. If you change outputs, update docs/screenshots/examples accordingly.

---

## 🧱 Architecture rules

KFM follows a layered / clean-architecture approach:

- 🧠 **Domain (Entities)**: pure models + domain rules  
- 🧩 **Use cases (Application services)**: workflows + orchestration of domain logic  
- 🔌 **Interfaces (Ports)**: abstract contracts (repositories, gateways, presenters)  
- 🧰 **Infrastructure (Adapters)**: DB, web frameworks, external APIs, queues, file systems

**Golden rules**
- ✅ Inner layers must not import outer layers.
- ✅ Business logic must not depend on frameworks.
- ✅ External services are called through interfaces (ports).
- ✅ Keep use cases small and single-responsibility.

**When adding a new feature**
- Start with a use case and domain data.
- Define interfaces for anything “outside” (DB, remote sensing API, filesystem).
- Implement adapters in infrastructure.
- Add tests at the use case level (mock interfaces).

> [!TIP]
> If your change requires touching domain + infrastructure in the same file, you’re probably crossing boundaries—split it. 🪓

---

## 🌍 Geospatial & remote sensing rules

This is a GIS-first system. Treat spatial correctness like you’d treat financial correctness. 💸➡️🗺️

### ✅ CRS & units
- Always declare **CRS** for geometries and rasters.
- Avoid “mystery coordinates.” Store SRID / EPSG with data.
- Make **units explicit** (meters vs feet, mm vs inches, etc.).

### ✅ Temporal alignment
- Document timestamps & timezones.
- Align remote sensing snapshots with ground truth windows (don’t “mix dates” silently).

### ✅ Data provenance
Every GIS layer should have:
- source (where it came from)
- acquisition date/time
- processing steps (what you did to it)
- version or hash if possible
- licensing/usage constraints (if applicable)

### ✅ Remote sensing + Earth Engine
- Avoid hardcoding API keys.
- Keep Earth Engine scripts reproducible:
  - pin datasets/collections (by ID)
  - document region of interest + scale
  - include export parameters
- Prefer pipelines that allow re-processing from raw inputs.

> [!NOTE]
> If you add a new layer that influences decisions, include uncertainty notes and validation strategy.

---

## 🧠 Data science, ML, and statistics rules

KFM cares about **truthful uncertainty** and **avoiding statistical self-deception**.

### ✅ Reproducible experiments
- Fix random seeds where relevant.
- Record dataset versions / queries / filters.
- Provide a minimal “rerun” path:
  - config file
  - command(s)
  - expected outputs

### ✅ Avoid common pitfalls
- No leakage (train/test contamination).
- No “metric shopping” without disclosure.
- Report uncertainty (CIs, error bars, posterior intervals, calibration).
- If using p-values: don’t treat “p<0.05” as magic.

### ✅ Evaluation
Include:
- baseline comparison
- failure cases
- calibration / reliability (when applicable)
- spatial & temporal generalization checks (not just random split)

### ✅ Notebooks (if used)
- Keep notebooks narrative + reproducible.
- Clear outputs before committing (unless the output is the point).
- Promote stable work into scripts/modules for production use.

---

## 🧬 Modeling & simulation rules

Simulation contributions must be credible and reviewable:

- ✅ **Verification**: did we implement the equations/logic correctly?
- ✅ **Validation**: does the model match reality (within uncertainty)?
- ✅ **Sensitivity analysis**: which parameters matter most?
- ✅ **Unit consistency**: enforce and test units early
- ✅ **Document assumptions**: what you *assumed* is often more important than what you computed

> [!IMPORTANT]
> If a simulation is used for advisory outputs, it must surface uncertainty and assumptions in UI/docs.

---

## 🎨 Frontend & visualization rules

### ✅ Responsive-first
- UI must work on desktop and mobile.
- Use sensible breakpoints, accessible controls, readable text.

### ✅ Accessibility
- Provide alt text for important images.
- Maintain heading order.
- Avoid “color-only meaning” in maps/charts.

### ✅ Mapping & 3D
- Make layers discoverable (legend, toggles, metadata).
- Don’t block interaction with heavy rendering; use progressive loading.
- If using WebGL overlays: test performance on modest hardware.

---

## 🗄️ Database & data management rules

### ✅ Schema & migrations
- Prefer migrations over “manual DB changes.”
- Consider indexing for spatial queries (PostGIS GiST, etc.).
- If you add a column: document it + add tests.

### ✅ Query hygiene
- Avoid `SELECT *` in production paths.
- Use parameterized queries to avoid injection.
- Validate and sanitize user inputs (especially geometry uploads).

### ✅ Large data
- Don’t commit large binaries or raw imagery to git.
- Use designated storage (object store, data lake, artifacts) and track metadata in-repo.

---

## 🔐 Security & privacy

Please read: `.github/SECURITY.md` (responsible disclosure) 🔒

**Hard rules**
- 🚫 Never commit secrets (API keys, tokens, private certs)
- 🚫 Don’t upload real PII into example datasets
- ✅ Use `.env` locally; keep `.env.example` safe and documented
- ✅ If you find a vulnerability, follow the security policy instead of opening a public issue

**Privacy rules**
- Treat location traces, sensor data, and user data as potentially sensitive.
- If a dataset could identify individuals/farms/entities, anonymize/aggregate and document the approach.

---

## 🧾 Git workflow + PR standards

### 🌿 Branch naming
Use descriptive branches:
- `feature/<short-name>`
- `fix/<short-name>`
- `docs/<short-name>`
- `chore/<short-name>`

Example:
- `feature/crop-rotation-analysis`
- `fix/map-layer-caching`

### ✅ Commit messages
Prefer clear, scoped commits (Conventional Commits encouraged):
- `feat: add soil moisture interpolation`
- `fix: correct CRS handling in NDVI export`
- `docs: clarify docker compose setup`
- `test: add regression tests for ETL pipeline`

### 🔁 PR checklist (Definition of Done)
Before you open a PR:

- [ ] The change is linked to an issue (or explains why none exists)
- [ ] Tests added/updated
- [ ] Lint/format passes
- [ ] Docs updated (if behavior changed)
- [ ] No secrets committed
- [ ] Data provenance included (if new data/layer)
- [ ] Architecture boundaries respected

### 🧑‍⚖️ Review expectations
- Small PRs merge faster 🏎️
- If your change is big, split into:
  1) refactor/scaffolding  
  2) behavior change  
  3) UI/UX polish  
- Respect CODEOWNERS reviews (see `.github/CODEOWNERS`)

---

## 📝 Documentation standards

Docs are part of the product. ✅

**Write docs like you write code**
- Clear headings
- Short paragraphs
- Examples that actually run
- Minimal duplication (link instead)
- Keep docs in Markdown (GitHub-friendly)

**Good doc PRs include**
- before/after screenshots (UI)
- examples and sample data (where safe)
- Mermaid diagrams (when helpful)

> [!TIP]
> If you fix a bug, update the docs in the same PR whenever feasible. 📚

---

## 🏷️ Issue labels & triage

Recommended labels (use what the repo already has):
- `bug` 🐛
- `enhancement` ✨
- `docs` 📚
- `good first issue` 🌱
- `help wanted` 🙋
- `security` 🔐
- `data` 🗂️
- `gis` 🗺️
- `ml` 🤖
- `simulation` 🧬

When filing issues, include:
- expected behavior vs actual behavior
- steps to reproduce
- logs / screenshots
- environment (OS, python/node versions, docker version)

---

## 📚 Project reference shelf

These contribution guidelines were shaped by the project’s internal reference library. 📖✨

<details>
<summary><strong>📦 Core KFM master doc (read this daily)</strong></summary>

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

</details>

<details>
<summary><strong>🧱 Architecture & engineering</strong></summary>

- Clean Architectures in Python  [oai_citation:1‡clean-architectures-in-python.pdf](file-service://file-6YHot4AqfpdbcrdfiYfpHM)  
- Scalable Data Management for Future Hardware  [oai_citation:2‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
- Implementing Programming Languages (Compilers & Interpreters)  [oai_citation:3‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
- Node.js Notes for Professionals  [oai_citation:4‡Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf](file-service://file-9qS1yEFvCBXbDdtTfpt3Ye)  
- PostgreSQL Notes for Professionals  [oai_citation:5‡PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf](file-service://file-742sw3gADJniEdmC19JeAC)  
- MySQL Notes for Professionals  [oai_citation:6‡MATLAB Programming for Engineers Stephen J. Chapman.pdf](file-service://file-GVz6J2tWsQSJL4sFY1Niqe)  
- Introduction to Docker  [oai_citation:7‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)  

</details>

<details>
<summary><strong>🌍 GIS, mapping, remote sensing</strong></summary>

- Geoprocessing with Python  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  
- Making Maps: A Visual Guide to Map Design for GIS  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  
- Geographic Information System Basics  [oai_citation:10‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)  
- Python Geospatial Analysis Cookbook  [oai_citation:11‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)  
- Google Maps JavaScript API Cookbook  [oai_citation:12‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)  
- Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals & Applications)  [oai_citation:13‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk)  
- Google Earth Engine Applications  [oai_citation:14‡Google Earth Engine Applications.pdf](file-service://file-SmoZrQ3nZSAdHHNqcVzYCq)  
- WebGL Programming Guide (Interactive 3D Graphics)  [oai_citation:15‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  

</details>

<details>
<summary><strong>🧠 ML, statistics, data science</strong></summary>

- AI Foundations of Computational Agents (3rd Ed.)  [oai_citation:16‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
- Deep Learning in Python — Prerequisites  [oai_citation:17‡deep-learning-in-python-prerequisites.pdf](file-service://file-9pQhD3FNUGoYzmKrdm26cg)  
- Artificial Neural Networks: An Introduction  [oai_citation:18‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)  
- Data Mining Concepts & Applications  [oai_citation:19‡graphical-data-analysis-with-r.pdf](file-service://file-K7oxq5mFmdE9HrPPev6c7L)  
- Regression Analysis with Python  [oai_citation:20‡Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf](file-service://file-THLZMx2BnXCR4bvvPJsMQm)  
- Data Science & Machine Learning (Mathematical & Statistical Methods)  [oai_citation:21‡Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf](file-service://file-MRNb2uGPEwpkSDsxF983PC)  
- Statistics Done Wrong  [oai_citation:22‡Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf](file-service://file-THLZMx2BnXCR4bvvPJsMQm)  
- Understanding Statistics & Experimental Design  [oai_citation:23‡Understanding Statistics & Experimental Design.pdf](file-service://file-SdX6LMgi1uDRk5kd4H4Bg3)  
- Bayesian Computational Methods  [oai_citation:24‡Bayesian computational methods.pdf](file-service://file-6NmuxfJsrfDTxQmEi8A7jo)  
- Graphical Data Analysis with R  [oai_citation:25‡graphical-data-analysis-with-r.pdf](file-service://file-K7oxq5mFmdE9HrPPev6c7L)  
- Applied Data Science with Python and Jupyter  [oai_citation:26‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  

</details>

<details>
<summary><strong>🧬 Simulation, visualization, and ethics</strong></summary>

- Scientific Modeling and Simulation (NASA-grade guide)  [oai_citation:27‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)  
- Computer Graphics using JAVA 2D & 3D  [oai_citation:28‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
- Generalized Topology Optimization for Structural Design  [oai_citation:29‡geoprocessing-with-python.pdf](file-service://file-NkXrdB4FwTruwhQ9Ggn53T)  
- Spectral Geometry of Graphs  [oai_citation:30‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)  
- Introduction to Digital Humanism  [oai_citation:31‡Data Mining Concepts & applictions.pdf](file-service://file-CCSRY2RwLx1w6m1RMReuBG)  
- Principles of Biological Autonomy  [oai_citation:32‡Artificial-neural-networks-an-introduction.pdf](file-service://file-DhnuQ12UtyRb9q5u5CptWo)  
- MATLAB Programming for Engineers  [oai_citation:33‡PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf](file-service://file-742sw3gADJniEdmC19JeAC)  

</details>

> [!NOTE]
> Some legacy/reference PDFs may be partially unparseable depending on how they were generated; if a reference can’t be searched, it can still be useful as background reading.

---

✅ Thanks for helping build KFM—every doc fix, test, and careful boundary line makes the system more trustworthy. 🌾🧭