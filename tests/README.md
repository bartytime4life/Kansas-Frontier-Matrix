# 🧪 Tests — Kansas Frontier Matrix (KFM) / Kansas‑Matrix‑System

![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2ea44f?logo=githubactions&logoColor=white)
![Coverage](https://img.shields.io/badge/Coverage-target%20%F0%9F%9A%80-informational)
![Python](https://img.shields.io/badge/Python-pytest-blue?logo=python&logoColor=white)
![Node](https://img.shields.io/badge/Node.js-test%20runner-brightgreen?logo=node.js&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ed?logo=docker&logoColor=white)

> KFM is a “trust-first” geospatial + simulation + AI system. This folder is where we prove (continuously) that our code, data pipelines, and UI behaviors are **correct**, **reproducible**, and **honest about uncertainty**.  
> (KFM’s stack spans React + responsive UI, geospatial pipelines, APIs, and CI gates.) [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧭 What this README is

This file is the **tests playbook**:
- ✅ how to run tests locally (fast + full)
- ✅ where tests live (by layer & domain)
- ✅ what to test (and what *not* to test)
- ✅ CI gates & “Definition of Done”
- ✅ domain-specific validation (GIS, remote sensing, ML, simulation, visualization)

---

## 🚀 Quickstart

### 1) Fast checks (pre‑commit vibes)
```bash
# Python
pytest -q

# Node/Web (if applicable)
npm test
```

### 2) Full suite (recommended on feature branches)
```bash
# If we use Make targets (recommended for repeatability)
make test

# Or run suites explicitly (examples)
pytest -m "not slow"
pytest -m "integration"
npm run test:e2e
```

### 3) Integration tests with containers (preferred)
If your tests require a DB / services, use Docker Compose so everyone runs the same stack:
```bash
docker compose up -d --build
pytest -m integration
docker compose down -v
```

> Why Docker-first? It makes CI ≈ local and reduces “works on my machine” drift. KFM’s DevOps approach explicitly centers containerized components and Compose/Kubernetes‑style orchestration. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧱 Test pyramid (how we keep velocity + confidence)

**Rule of thumb:** most tests should be cheap, deterministic, and close to the code.  
Then we add fewer (but high-value) integration + end-to-end flows.

```
          🔺 E2E (few)        → critical user journeys, UI + API + DB
        🔺🔺 Integration (some) → services together (DB, API, pipelines)
      🔺🔺🔺 Unit (many)        → pure logic, models, transforms, validators
```

KFM explicitly calls out:
- unit tests for pure functions
- integration tests for API endpoints with a test DB
- component tests (Jest + React Testing Library)
- end-to-end tests (Cypress/Selenium) for key flows [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🗂️ Suggested folder layout

Adapt as needed to match the repo, but keep intent obvious:

```
📦 repo-root/
├─ 📂 🧪 tests/
│  ├─ 📄 README.md                      # this playbook
│  ├─ 📂 🧷 fixtures/                   # tiny, deterministic test data
│  │  ├─ 📂 🗺️ geo/                     # small vector/raster samples (safe + tiny)
│  │  ├─ 📂 🧬 ml/                      # toy datasets / model artifacts (non-sensitive)
│  │  ├─ 📂 🧾 schemas/                 # JSON/YAML schemas used in tests
│  │  └─ 📄 📘 FIXTURES.md              # fixture rules + provenance notes
│  ├─ 📂 🐍 python/
│  │  ├─ 📂 🧩 unit/                    # pure functions, domain rules
│  │  ├─ 📂 🔌 integration/             # DB/API/service interactions
│  │  ├─ 📂 ✅ validation/              # “scientific correctness” checks
│  │  ├─ 📂 ⏱️ performance/             # benchmarks (nightly / non-gating)
│  │  ├─ 📂 🧷 helpers/                 # shared utilities
│  │  ├─ 📄 🧱 conftest.py              # shared fixtures
│  │  ├─ 📄 🧾 pytest.ini               # markers, defaults (optional)
│  │  └─ 📄 📘 PYTHON_TESTS.md          # python suite conventions
│  ├─ 📂 🌐 web/
│  │  ├─ 📂 🧩 unit/                    # JS/TS unit tests
│  │  ├─ 📂 🧱 component/               # React component tests
│  │  ├─ 📂 🧭 e2e/                     # Cypress/Playwright/Selenium
│  │  ├─ 📂 🖼️ visual/                  # screenshot / render snapshots
│  │  ├─ 📂 🧷 helpers/                 # test helpers, mocks
│  │  └─ 📄 📘 WEB_TESTS.md             # web suite conventions
│  ├─ 📂 🗄️ db/
│  │  ├─ 📂 🧬 migrations/              # migration assertions
│  │  ├─ 📂 🔌 integration/             # DB-level integration tests
│  │  ├─ 📂 🧪 seed/                    # minimal seed data for tests
│  │  └─ 📄 📘 DB_TESTS.md              # DB test guidance
│  ├─ 📂 🧾 contracts/
│  │  ├─ 📂 📜 api/                     # OpenAPI/GraphQL contract fixtures
│  │  ├─ 📂 🗺️ stac/                    # STAC Item/Collection contract fixtures
│  │  ├─ 📂 🧾 dcat/                    # DCAT dataset contract fixtures
│  │  ├─ 📂 🧬 prov/                    # PROV lineage contract fixtures
│  │  └─ 📄 📘 CONTRACT_TESTS.md        # contract testing rules
│  ├─ 📂 🧰 tools/
│  │  ├─ 📄 🔧 run_unit.sh              # optional helper
│  │  ├─ 📄 🔧 run_integration.sh       # optional helper
│  │  ├─ 📄 🔧 run_e2e.sh               # optional helper
│  │  └─ 📄 📘 TOOLS.md                 # helper scripts doc
│  └─ 📄 📘 TEST_POLICY.md              # definition of done + CI gates
└─ 📂 🧰 scripts/                       # optional: CI glue, seeders, utilities
   ├─ 📄 🧪 test_env_up.sh
   ├─ 📄 🧪 test_env_down.sh
   └─ 📄 📘 SCRIPTS.md```
---

## ✅ CI gates (non‑negotiable)

**Policy:** the pipeline must be green before merge. CI should run on every PR/push and execute tests + static checks. [oai_citation:4‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

Typical PR gates:
1) 🧹 format + lint (Python + JS/TS)
2) 🧪 unit tests
3) 🔌 integration tests (with ephemeral DB/services)
4) 🌐 build web bundle (catch compile issues)
5) 🧾 contract/schema validation (OpenAPI, STAC/DCAT/PROV if used)
6) 📈 coverage thresholds (target, not a religion)

> KFM documentation describes CI that runs tests + linting/type checks and blocks merges on failures. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧠 Writing great tests (the KFM way)

### ✅ Test public behavior, not private plumbing
Don’t lock tests to implementation details unless it’s truly business-critical. Prefer testing public entry points; private helpers are validated indirectly. This reduces refactor friction. [oai_citation:6‡clean-architectures-in-python.pdf](file-service://file-6YHot4AqfpdbcrdfiYfpHM)

### 🔁 Determinism is a feature
For research/AI/simulation code: set seeds, pin dependencies, and eliminate hidden state. Deterministic outputs allow re-running results exactly. [oai_citation:7‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

**Checklist:**
- [ ] seeds set (Python, NumPy, ML frameworks)
- [ ] stable sorting (don’t rely on hash order)
- [ ] time mocked/frozen where needed
- [ ] no network calls in unit tests (record/replay if unavoidable)
- [ ] fixtures are tiny & versioned

### 🧩 Prefer contracts at boundaries
- API boundary: OpenAPI schema tests + golden requests
- data boundary: schema + constraints + “expected distribution” smoke checks (especially for pipelines)

The project’s QA guidance explicitly calls out:
- unit/integration/e2e tests
- pipeline integrity checks
- scientific “known result / analytical solution” comparisons [oai_citation:8‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🐍 Python test guidance

### Unit tests
Best for:
- coordinate transforms
- unit conversions
- parser/validator logic
- pure math transforms
- domain rules

### Integration tests
Best for:
- PostGIS / DB interactions
- API endpoints
- “glue code” that hits filesystem, cloud, queues, etc.

### Scientific / simulation validation
Treat simulation/analysis code like scientific instruments:
- **verification**: does the implementation match the intended math?
- **validation**: does it match reality (within uncertainty)?
- **regression baselines**: freeze known-good outputs to detect drift

---

## 🌐 Web / Frontend test guidance

KFM’s frontend is a browser-based React app that must be responsive across devices and modern browsers. [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

### Component tests (fast)
- render correctness given props/state
- event dispatch correctness
- accessibility checks (labels, keyboard nav)

### E2E tests (few but powerful)
Focus on “money paths”:
- login
- load a layer
- timeline navigation
- select a field → chart/metadata shows correctly
- export/report

### Visual regression (maps + 3D)
When rendering matters, use snapshot-based checks:
- map symbology doesn’t silently change
- overlays remain legible at common zoom levels
- dark/light modes don’t break contrast

---

## 🗺️ Geospatial tests (GIS correctness)

Geospatial pipelines are fragile in predictable ways; test these explicitly:
- **CRS sanity:** EPSG correctness, meters vs degrees issues  
- **topology:** valid geometries, no self-intersections if required
- **overlay correctness:** clip/intersect/union behaviors
- **raster alignment:** resolution, nodata handling, resampling method
- **format IO:** GeoJSON/GeoPackage/COG round-trips

The geospatial cookbook and geoprocessing resources in this repo cover common patterns (DB + geometry + GeoJSON) and are a good reference for realistic test fixtures and “known output” comparisons. [oai_citation:10‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) [oai_citation:11‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

## 🛰️ Remote sensing tests (Earth Engine & imagery)

Remote sensing pipelines fail quietly unless you test the assumptions:
- band availability & naming
- scale / resolution
- cloud masking logic (QA bits)
- temporal compositing rules
- normalization & index calculations (e.g., NDVI)
- export formats & metadata consistency

Add “truthiness checks”:
- output image has expected range
- masked pixels count within expected band
- time series has monotonic timestamps

---

## 📊 ML / stats tests (don’t fool yourself)

Data science code needs tests beyond “it runs”:
- Train/val/test split is correct and leak-free
- Metrics are stable (within tolerance)
- Baseline model comparison exists
- Confidence intervals / uncertainty reporting is present when relevant
- Guard against “multiple comparisons” / p-hacking patterns

KFM explicitly emphasizes evidence-driven evaluation and communicating uncertainty (not false precision). [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧩 Graphs, agents, optimization, and “hard math” modules

If the code includes:
- graph algorithms (spectral methods, routing)
- autonomous agents / planners
- optimization loops (topology/structure/constraints)

Add tests that check:
- invariants (symmetry, conservation, monotonicity)
- convergence behavior (within iteration limits)
- gradient checks (finite difference sanity)
- known benchmark problems (tiny, deterministic)

---

## 🗄️ Database tests (PostgreSQL / MySQL)

Principles:
- isolate with ephemeral DBs (containers)
- run migrations in CI
- use transactions for isolation
- seed minimal fixtures, not production dumps

**Recommended:**
- migration tests: upgrade/downgrade + schema assertions
- query tests: correctness + indexes used (where critical)
- contract tests: API responses match schema

---

## 🐳 Docker + Compose: the integration test backbone

KFM DevOps guidance calls out Dockerfiles for components and Compose for multi-container setups. [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

**Pattern:**
- Compose defines `db`, `api`, maybe `worker`
- tests bring stack up, run, and tear down
- CI runs the same Compose profile

---

## 🧾 PR checklist (copy/paste)

- [ ] Unit tests added/updated
- [ ] Integration tests added (if behavior crosses boundaries)
- [ ] Seeds fixed / deterministic output confirmed (if ML/sim) [oai_citation:14‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Any new data schema validated (and documented)
- [ ] UI changes include component tests + (if visual) snapshot updates
- [ ] CI is green (required) [oai_citation:15‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🧯 Troubleshooting

**Tests fail only in CI?**
- compare dependency lockfiles
- ensure Docker-based services run identical versions locally
- check for reliance on local paths, locale, timezone, GPU availability

**Flaky tests?**
- eliminate timing sleeps; wait on conditions
- stabilize randomness (seed)
- isolate external services (record/replay or mock)

---

## 📚 Project library map (used to shape this test strategy)

<details>
<summary>📦 Click to expand the full “project files” list (with how each informs testing)</summary>

### 🧱 Architecture, devops, and engineering discipline
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf  [oai_citation:17‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- clean-architectures-in-python.pdf  [oai_citation:18‡clean-architectures-in-python.pdf](file-service://file-6YHot4AqfpdbcrdfiYfpHM)
- Introduction-to-Docker.pdf (Compose-driven integration & CI parity)
- Command Line Kung Fu_ Bash Scripting Tricks… (CLI workflows for test automation)
- implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf (parser/AST “golden file” testing patterns)
- MARKDOWN_GUIDE_v13.md.gdoc  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) (validation + CI/CD gates & doc governance)

### 📊 Statistics, scientific rigor, and reproducibility
- Scientific Method _ Research _ Master Coder Protocol Documentation.pdf  [oai_citation:20‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf (V&V + uncertainty thinking)
- Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf (avoid statistical traps)
- Understanding Statistics & Experimental Design.pdf (randomization/power/validity)
- Bayesian computational methods.pdf (posterior predictive checks & uncertainty)
- regression-analysis-with-python.pdf (diagnostics & evaluation)
- graphical-data-analysis-with-r.pdf  [oai_citation:21‡graphical-data-analysis-with-r.pdf](file-service://file-K7oxq5mFmdE9HrPPev6c7L) (visual diagnostics mindset)
- applied-data-science-with-python-and-jupyter.pdf (reproducible notebooks → testable pipelines)

### 🧠 ML / AI / agents
- deep-learning-in-python-prerequisites.pdf (train/val/test splits & generalization)
- Artificial-neural-networks-an-introduction.pdf (overtraining/generalization guardrails)
- Data Mining Concepts & applictions.pdf (evaluation metrics, validation discipline)
- Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf (CV/bootstrap grounding)
- AI Foundations of Computational Agents 3rd Ed.pdf (agent evaluation & safety checks)

### 🗺️ Geospatial, GIS, cartography, mapping
- Geographic Information System Basics - geographic-information-system-basics.pdf (CRS/projection correctness)
- geoprocessing-with-python.pdf (vector/raster processing patterns)
- python-geospatial-analysis-cookbook.pdf (topology/overlays/routing fixtures)
- making-maps-a-visual-guide-to-map-design-for-gis.pdf (visual correctness & map design checks)
- Google Maps API Succinctly - google_maps_api_succinctly.pdf (map UI behaviors & API assumptions)
- google-maps-javascript-api-cookbook.pdf (Map API patterns)
- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf  [oai_citation:22‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7quELMw4FrspPczB9Y3BTp) (rendering + shader pipeline considerations)
- responsive-web-design-with-html5-and-css3.pdf (breakpoints/responsive test strategy)

### 🛰️ Remote sensing (GEE)
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf (cloud masks, band logic)
- Google Earth Engine Applications.pdf (workflows & edge cases)

### 🗄️ Data systems & performance
- PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf (DB behaviors, backups, transactions)
- MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf (DB ops/testing hygiene)
- Scalable Data Management for Future Hardware.pdf  [oai_citation:23‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE) (performance/throughput thinking → benchmarks)

### 🧮 Optimization, graphs, graphics, and tooling
- Spectral Geometry of Graphs.pdf (spectral invariants & graph algorithm tests)
- Generalized Topology Optimization for Structural Design.pdf (optimization convergence/gradient tests)
- Computer Graphics using JAVA 2D & 3D.pdf (render pipeline mindset)
- Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf (server/runtime test practices)
- MATLAB Programming for Engineers Stephen J. Chapman.pdf (MATLAB scripts/functions test approach)

### ⚖️ Human-centered / ethics / autonomy
- Introduction to Digital Humanism.pdf (human-centered QA + safety expectations)
- Principles of Biological Autonomy - book_9780262381833.pdf (systems thinking for autonomous behaviors)

</details>

---

## 🧷 Links
- 🔙 Return to repo root README: `../README.md` (if present)
- 🧑‍💻 Contribution guidelines: `../CONTRIBUTING.md` (recommended)
- 🧾 Test policy docs (suggested): `../docs/testing/TEST_POLICY.md`

---

### ✨ Small “next improvements” (optional but recommended)
- Add `make test`, `make test-unit`, `make test-integration`, `make test-e2e` targets
- Add CI artifacts: coverage report + E2E screenshots on failure
- Add metadata validation for outputs (STAC/DCAT/PROV if used)
- Add nightly performance benchmarks (separate from PR gating)