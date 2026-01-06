# 🧪 Tests — Kansas Frontier Matrix (KFM) / Kansas‑Matrix‑System

![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2ea44f?logo=githubactions&logoColor=white)
![Coverage](https://img.shields.io/badge/Coverage-target%20%F0%9F%9A%80-informational)
![Python](https://img.shields.io/badge/Python-pytest-blue?logo=python&logoColor=white)
![Node](https://img.shields.io/badge/Node.js-test%20runner-brightgreen?logo=node.js&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ed?logo=docker&logoColor=white)
![Reproducible](https://img.shields.io/badge/Reproducible-%E2%9C%85-success)

> KFM is a **trust-first** geospatial + simulation + AI system. This folder is where we prove (continuously) that our code, data pipelines, and UI behaviors are **correct**, **reproducible**, and **honest about uncertainty**.  
> (KFM’s stack spans React + responsive UI, geospatial pipelines, APIs, and CI gates.)  
> [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧭 What this README is

This file is the **tests playbook**:
- ✅ how to run tests locally (fast + full)
- ✅ where tests live (by layer & domain)
- ✅ what to test (and what *not* to test)
- ✅ CI gates & “Definition of Done”
- ✅ domain-specific validation (GIS, remote sensing, ML, simulation, visualization)

---

## 🗺️ Quick navigation

- 📁 **Folder layout:** see [Suggested folder layout](#%EF%B8%8F-suggested-folder-layout)
- 🚀 **Run tests now:** see [Quickstart](#-quickstart)
- ✅ **Merge gates:** see [CI gates](#-ci-gates-non-negotiable)
- 🧪 **Scientific validity:** see [Scientific / simulation validation](#-scientific--simulation-validation)
- 🗺️ **GIS correctness:** see [Geospatial tests](#%EF%B8%8F-geospatial-tests-gis-correctness)
- 🛰️ **Remote sensing:** see [Remote sensing tests](#%EF%B8%8F-remote-sensing-tests-earth-engine--imagery)
- 🌐 **Frontend:** see [Web / frontend test guidance](#-web--frontend-test-guidance)
- 📚 **Reference library:** see [Project library map](#-project-library-map-used-to-shape-this-test-strategy)

---

## 🚀 Quickstart

### 0) Preconditions (one-time)
- 🐍 Python env ready (`python -m venv .venv` / conda / uv / etc.)
- 🌐 Node env ready (`npm ci` / `pnpm i` / `yarn`)
- 🐳 Docker installed (for integration parity) :contentReference[oaicite:0]{index=0}
- 🧩 Prefer `docker compose` (Compose is integrated into the Docker CLI) :contentReference[oaicite:1]{index=1}

> [!TIP]
> If your feature touches DB/API/pipelines: **run the Docker-backed integration tests** at least once before opening a PR.

### 1) Fast checks (pre‑commit vibes ⚡)
```bash
# Python
pytest -q

# Node/Web (if applicable)
npm test
```

### 2) Full suite (recommended on feature branches ✅)
```bash
# If we use Make targets (recommended for repeatability)
make test

# Or run suites explicitly (examples)
pytest -m "not slow"
pytest -m "integration"
npm run test:e2e
```

### 3) Integration tests with containers (preferred 🐳)
If your tests require a DB / services, use Docker Compose so everyone runs the same stack:

```bash
docker compose up -d --build
pytest -m integration
docker compose down -v
```

> Why Docker-first? It reduces “works on my machine” drift and makes CI ≈ local. Compose is specifically designed to define and run **multi-container** stacks in a single YAML and start them with one command. :contentReference[oaicite:2]{index=2}

---

## 🧱 Test pyramid (how we keep velocity + confidence)

**Rule of thumb:** most tests should be cheap, deterministic, and close to the code.  
Then we add fewer (but high-value) integration + end-to-end flows.

```
          🔺 E2E (few)         → critical user journeys, UI + API + DB
        🔺🔺 Integration (some) → services together (DB, API, pipelines)
      🔺🔺🔺 Unit (many)         → pure logic, models, transforms, validators
```

KFM explicitly calls out:
- unit tests for pure functions
- integration tests for API endpoints with a test DB
- component tests (Jest + React Testing Library)
- end-to-end tests (Cypress/Selenium) for key flows  
[oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧷 Core test principles (KFM style)

### ✅ Test public behavior, not private plumbing
Don’t lock tests to implementation details unless it’s truly business-critical. Prefer testing public entry points; private helpers are validated indirectly. This reduces refactor friction. :contentReference[oaicite:3]{index=3}

### 🔁 Determinism is a feature
For research/AI/simulation code: set seeds, pin dependencies, and eliminate hidden state. Deterministic outputs allow re-running results exactly.  
[oai_citation:7‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

**Determinism checklist:**
- [ ] seeds set (Python, NumPy, ML frameworks)
- [ ] stable sorting (don’t rely on hash order)
- [ ] time mocked/frozen where needed
- [ ] no network calls in unit tests (record/replay if unavoidable)
- [ ] fixtures are tiny & versioned
- [ ] floating point comparisons use tolerances (not `==`)

### 🧾 “Trust-first” means we test uncertainty too
If outputs are probabilistic / noisy / estimated:
- assert **ranges**, **invariants**, **calibration**, or **distributional sanity**
- log uncertainty artifacts (CI attachments: plots, traces, summaries)
- store baseline comparisons with tolerances + rationale

The NASA-grade modeling approach treats verification/validation/uncertainty as first-class engineering work. :contentReference[oaicite:4]{index=4}

---

## 🗂️ Suggested folder layout

Adapt as needed to match the repo, but keep intent obvious:

```text
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
│  │  ├─ 📂 🧭 e2e/                     # Playwright/Cypress/Selenium
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
   └─ 📄 📘 SCRIPTS.md
```

---

## ✅ CI gates (non‑negotiable)

**Policy:** the pipeline must be green before merge. CI should run on every PR/push and execute tests + static checks.  
[oai_citation:4‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

Typical PR gates:
1) 🧹 format + lint (Python + JS/TS)
2) 🧪 unit tests
3) 🔌 integration tests (with ephemeral DB/services)
4) 🌐 build web bundle (catch compile issues)
5) 🧾 contract/schema validation (OpenAPI, STAC/DCAT/PROV if used)
6) 📈 coverage thresholds (target, not a religion)

> KFM documentation describes CI that runs tests + linting/type checks and blocks merges on failures.  
> [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

### 🧨 What should *not* gate PRs (usually)
Keep PR CI fast. Push expensive checks to nightly/scheduled pipelines:
- ⏱️ performance benchmarks (trend monitoring)
- 🧠 long ML training runs (use tiny toy models on PRs)
- 🗺️ large geospatial/raster workloads (use fixtures & sampling)

> [!NOTE]
> Compose is built for consistency across environments (“define once, run anywhere”). CI parity is the reason we prefer it for integration tests. :contentReference[oaicite:5]{index=5}

---

## 🧪 Test categories & markers (suggested)

If using `pytest`, standardize markers so devs can run focused slices:

```ini
# tests/python/pytest.ini (example)
[pytest]
markers =
  unit: fast pure logic
  integration: hits db/services/filesystem
  e2e: end-to-end journeys (rare for python)
  slow: long-running tests (non-gating)
  validation: scientific/V&V tests (tolerance-based)
  perf: benchmarks (nightly)
```

---

## 🐍 Python test guidance

### 🧩 Unit tests
Best for:
- coordinate transforms
- unit conversions
- parser/validator logic
- pure math transforms
- domain rules

✅ Tips:
- prefer `numpy.testing.assert_allclose` / `pytest.approx` for floats
- encode invariants (monotonicity, conservation) instead of brittle constants
- include at least one “sad path” (invalid input) per public function

### 🔌 Integration tests
Best for:
- PostGIS / DB interactions
- API endpoints
- “glue code” that hits filesystem, cloud, queues, etc.

✅ Tips:
- use Compose to create repeatable dependencies
- isolate state via transactions or per-test schemas
- avoid reaching the public internet; record/replay if unavoidable

---

## 🧠 Scientific / simulation validation

Treat simulation/analysis code like **scientific instruments**:
- **verification**: does the implementation match the intended math?
- **validation**: does it match reality (within uncertainty)?
- **regression baselines**: freeze known-good outputs to detect drift

A “NASA-grade” posture emphasizes rigor + documentation + governance so results remain reproducible and explainable years later. :contentReference[oaicite:6]{index=6}

### ✅ Recommended validation patterns
- **Analytical solution comparisons** (tiny cases with known answers)
- **Convergence tests** (refine timestep / resolution → error shrinks)
- **Invariant checks** (energy/mass conservation, monotonicity, symmetry)
- **Tolerance-based golden files** (store arrays/rasters with metadata + tolerances)
- **Uncertainty reporting** (intervals, credible bands, posterior predictive checks)

> [!TIP]
> If results are stochastic, test *properties* (ranges, quantiles, calibration) rather than single-point outputs.

---

## 🌐 Web / frontend test guidance

KFM’s frontend is a browser-based React app that must be responsive across devices and modern browsers.  
[oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L) :contentReference[oaicite:7]{index=7}

### 🧱 Component tests (fast)
- render correctness given props/state
- event dispatch correctness
- accessibility checks (labels, keyboard nav)

### 🧭 E2E tests (few but powerful)
Focus on “money paths”:
- login
- load a layer
- timeline navigation
- select a field → chart/metadata shows correctly
- export/report

### 🖼️ Visual regression (maps + 3D)
When rendering matters, use snapshot-based checks:
- map symbology doesn’t silently change
- overlays remain legible at common zoom levels
- dark/light modes don’t break contrast
- WebGL render regressions tracked with screenshot diffs (tolerance-based) :contentReference[oaicite:8]{index=8}

---

## 🗺️ Geospatial tests (GIS correctness)

Geospatial pipelines are fragile in predictable ways; test these explicitly:
- **CRS sanity:** EPSG correctness, meters vs degrees issues  
- **topology:** valid geometries, no self-intersections if required
- **overlay correctness:** clip/intersect/union behaviors
- **raster alignment:** resolution, nodata handling, resampling method
- **format IO:** GeoJSON/GeoPackage/COG round-trips

The geospatial cookbook is a strong reference for realistic fixtures, overlays/topology patterns, and known-output comparisons. :contentReference[oaicite:9]{index=9}

> [!NOTE]
> For GIS tests, always document the CRS and units in the test name or fixture metadata (it prevents “silent degrees vs meters” disasters).

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
- masked pixels count within expected bounds
- time series has monotonic timestamps

---

## 📊 ML / stats tests (don’t fool yourself)

Data science code needs tests beyond “it runs”:
- Train/val/test split is correct and leak-free
- Metrics are stable (within tolerance)
- Baseline model comparison exists
- Confidence intervals / uncertainty reporting is present when relevant
- Guard against “multiple comparisons” / p-hacking patterns :contentReference[oaicite:10]{index=10}

KFM explicitly emphasizes evidence-driven evaluation and communicating uncertainty (not false precision).  
[oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

> [!TIP]
> When in doubt: add a simple baseline + sanity-check plots (and attach them as CI artifacts in failure cases). :contentReference[oaicite:11]{index=11}

---

## 🧩 Graphs, agents, optimization, and “hard math” modules

If the code includes:
- graph algorithms (spectral methods, routing) :contentReference[oaicite:12]{index=12}
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

Refs: PostgreSQL/MySQL operator notes are handy for edge-case behaviors and testing hygiene. :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14}

---

## 🐳 Docker + Compose: the integration test backbone

KFM DevOps guidance calls out Dockerfiles for components and Compose for multi-container setups.  
[oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

**Pattern:**
- Compose defines `db`, `api`, maybe `worker`
- tests bring stack up, run, and tear down
- CI runs the same Compose profile

**Compose tips that help tests stay reliable:**
- add `healthcheck:` so tests can wait for readiness :contentReference[oaicite:15]{index=15}
- keep stacks minimal for PR gates (only required services)
- use dedicated volumes for DB data and wipe with `down -v` between runs

---

## 🧾 PR checklist (copy/paste ✅)

- [ ] Unit tests added/updated
- [ ] Integration tests added (if behavior crosses boundaries)
- [ ] Seeds fixed / deterministic output confirmed (if ML/sim)  
  [oai_citation:14‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Any new data schema validated (and documented)
- [ ] UI changes include component tests + (if visual) snapshot updates
- [ ] CI is green (required)  
  [oai_citation:15‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🧯 Troubleshooting

### ❌ Tests fail only in CI?
- compare dependency lockfiles
- ensure Docker-based services run identical versions locally
- check for reliance on local paths, locale, timezone, GPU availability

### 🎲 Flaky tests?
- eliminate timing sleeps; wait on conditions
- stabilize randomness (seed)
- isolate external services (record/replay or mock)

### 🐳 Docker stack won’t start?
- check logs: `docker compose logs -f`
- rebuild: `docker compose up -d --build`
- validate config: `docker compose config` :contentReference[oaicite:16]{index=16}

---

## 📚 Project library map (used to shape this test strategy)

<details>
<summary>📦 Click to expand the full “project files” list (with how each informs testing)</summary>

### 🧱 Architecture, devops, and engineering discipline
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  
  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf  
  [oai_citation:17‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- clean-architectures-in-python.pdf (architecture → test boundaries) :contentReference[oaicite:17]{index=17}
- Introduction-to-Docker.pdf (Compose-driven integration & CI parity) :contentReference[oaicite:18]{index=18}
- Command Line Kung Fu_ Bash Scripting Tricks… (CLI workflows for test automation)
- implementing-programming-languages… (parser/AST “golden file” testing patterns) :contentReference[oaicite:19]{index=19}
- Unified Knowledge Base_ Future-Proof Tech Documentation.docx (interdisciplinary QA mindset) :contentReference[oaicite:20]{index=20}

### 📊 Statistics, scientific rigor, and reproducibility
- Scientific Method _ Research _ Master Coder Protocol Documentation.pdf  
  [oai_citation:20‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf (V&V + uncertainty) :contentReference[oaicite:21]{index=21}
- Statistics Done Wrong (avoid statistical traps) :contentReference[oaicite:22]{index=22}
- Bayesian computational methods (posterior predictive checks & uncertainty mindset) :contentReference[oaicite:23]{index=23}
- Applied Data Science with Python and Jupyter (reproducible notebooks → testable pipelines) :contentReference[oaicite:24]{index=24}

### 🧠 ML / AI / agents
- AI Foundations of Computational Agents 3rd Ed.pdf (agent evaluation & safety checks)

### 🗺️ Geospatial, GIS, cartography, mapping
- python-geospatial-analysis-cookbook.pdf (topology/overlays/routing fixtures) :contentReference[oaicite:25]{index=25}
- responsive-web-design-with-html5-and-css3.pdf (breakpoints/responsive test strategy) :contentReference[oaicite:26]{index=26}
- webgl-programming-guide… (rendering + shader pipeline considerations) :contentReference[oaicite:27]{index=27}

### 🗄️ Data systems & performance
- PostgreSQL Notes for Professionals (DB behaviors, transactions) :contentReference[oaicite:28]{index=28}
- MySQL Notes for Professionals (DB ops/testing hygiene) :contentReference[oaicite:29]{index=29}
- Scalable Data Management for Future Hardware (performance thinking → benchmarks) :contentReference[oaicite:30]{index=30}

### ⚖️ Human-centered / ethics / autonomy
- Introduction to Digital Humanism (human-centered QA + safety expectations) :contentReference[oaicite:31]{index=31}
- Principles of Biological Autonomy (systems thinking for autonomous behaviors) :contentReference[oaicite:32]{index=32}
</details>

---

## 🧷 Links
- 🔙 Return to repo root README: `../README.md` (if present)
- 🧑‍💻 Contribution guidelines: `../CONTRIBUTING.md` (recommended)
- 🧾 Test policy docs (suggested): `../docs/testing/TEST_POLICY.md`

---

## ✨ Small “next improvements” (optional but recommended)
- Add `make test`, `make test-unit`, `make test-integration`, `make test-e2e` targets
- Add CI artifacts: coverage report + E2E screenshots on failure
- Add metadata validation for outputs (STAC/DCAT/PROV if used)
- Add nightly performance benchmarks (separate from PR gating)
