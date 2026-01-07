# 🧪 KFM API Test Suite — `api/tests/`

<p align="left">
  <img alt="Tests" src="https://img.shields.io/badge/tests-automated-blue" />
  <img alt="Style" src="https://img.shields.io/badge/style-clean%20architecture-3c4" />
  <img alt="API" src="https://img.shields.io/badge/API-REST%20%2B%20GeoJSON-7aa" />
  <img alt="Governance" src="https://img.shields.io/badge/governance-auth%20%7C%20redaction%20%7C%20classification-critical" />
  <img alt="Contracts" src="https://img.shields.io/badge/contracts-OpenAPI%20%2B%20JSON%20Schema-85EA2D?logo=openapiinitiative&logoColor=white" />
  <img alt="Determinism" src="https://img.shields.io/badge/determinism-seeded%20%7C%20no%20network-111827" />
</p>

Welcome to the **API boundary test suite** for the Kansas Frontier Matrix (KFM) backend.  
This folder verifies the **web/API boundary**: routing, request/response validation, auth, serialization, catalog/provenance linking, and orchestration behavior.

> [!IMPORTANT]
> 🛑 **KFM invariant:** **ETL → STAC/DCAT/PROV Catalogs → Graph → API → UI → Story Nodes → Focus Mode**  
> Tests should fail if the API attempts to serve **uncataloged** or **policy-ambiguous** data.

---

## 🔗 Quick links

- [🎯 What lives here](#-what-lives-here)
- [🧭 Test philosophy](#-test-philosophy-kfm-friendly)
- [⚡ Quickstart](#-quickstart)
- [🗂️ Suggested folder layout](#️-suggested-folder-layout)
- [🧱 Test types](#-test-types-we-expect-in-kfm)
- [🧪 Writing a new API test](#-writing-a-new-api-test)
- [🧰 Fixtures & test data rules](#-fixtures--test-data-rules)
- [🔐 Auth testing tips](#-auth-testing-tips)
- [🧯 Common pitfalls](#-common-pitfalls)
- [✅ Definition of Done](#-definition-of-done-dod-for-api-work)
- [📚 Handy pytest patterns](#-handy-pytest-patterns)
- [📦 CI hardening](#-ci-hardening-recommended)
- [📚 Project reference library → testing rules](#-project-reference-library--testing-rules-uses-all-project-files)

---

## 🎯 What lives here?

This directory focuses on **API-facing behavior**:

- ✅ Request parsing + validation (query params, request bodies, headers)
- ✅ Authentication & authorization behavior (401/403, roles/scopes, token expiry)
- ✅ Response shapes (JSON / GeoJSON / CSV / tiles) and status codes
- ✅ Error semantics (400 vs 404 vs 422 vs 500) + safe messages
- ✅ “Thin controller” rule: API layer calls **use-cases/services** and formats output
- ✅ Governance outputs: **classification propagation**, **redaction warnings**, **evidence pointers** (STAC/DCAT/PROV)
- ✅ Orchestration: job creation is fast; job progress/result endpoints are consistent

> 💡 The API should stay **thin**: validate inputs, delegate to application logic, format outputs, attach governance metadata.

---

## 🧭 Test Philosophy (KFM-friendly)

### 🧼 Clean Architecture first
- Core logic should be testable without FastAPI (unit tests live elsewhere).
- API tests verify the boundary glue and policy gates, not the domain math.

### 🧊 Deterministic & reproducible
- 🚫 No live calls to Earth Engine, NOAA, or any external service in standard CI.
- Use fakes/stubs/recorded responses for external dependencies.
- Seed randomness for ML/simulation endpoints (and assert the seed is recorded in artifacts).

### 🧯 Safe by default
- Never point tests at production infrastructure.
- Integration tests use disposable containers, ephemeral schemas, or temporary DBs.
- Any test that *could* mutate data must run against a test-only environment.

### 🧾 Evidence over vibes
If an endpoint returns something that implies a claim (trend, anomaly, “model says…”), tests should verify:
- ✅ the response includes provenance pointers (STAC/DCAT/PROV)
- ✅ uncertainty/assumptions are represented (where applicable)
- ✅ classification is explicit and correct

---

## ⚡ Quickstart

From repo root:

```bash
python -m pytest api/tests -q
```

Run a single test file:

```bash
python -m pytest api/tests/routes/test_fields_timeseries.py -q
```

Run tests matching a keyword:

```bash
python -m pytest api/tests -k timeseries -q
```

Stop on first failure + show locals:

```bash
python -m pytest api/tests -x --showlocals
```

> [!TIP]
> If the repo has a `Makefile`, strongly consider adding:
> - `make test`
> - `make test-api`
> - `make test-contract`
> - `make test-integration`

---

## 🗂️ Suggested folder layout

> If your suite grows, use a structure like this 👇 (clean, predictable, CI-friendly)

```text
📦 api/
└── 🧪 tests/
    ├── 📄 README.md
    ├── 🧰 conftest.py                  # shared fixtures (client, tokens, db, stubs)
    ├── 🧩 unit/                        # pure unit tests for API helpers (no DB)
    │   ├── test_validation.py
    │   ├── test_serialization.py
    │   └── test_error_mapping.py
    ├── 🌐 routes/                      # endpoint tests (FastAPI routes)
    │   ├── test_health.py
    │   ├── test_auth_me.py
    │   ├── test_fields_timeseries.py
    │   ├── test_catalog_stac.py
    │   ├── test_evidence_bundle.py
    │   ├── test_simulation_run.py
    │   └── test_data_upload.py
    ├── 🔐 auth/                        # authn/authz tests
    │   ├── test_jwt.py
    │   ├── test_rbac.py
    │   └── test_classification_gates.py
    ├── 🧬 governance/                  # redaction + classification propagation tests
    │   ├── test_redaction_fields.py
    │   ├── test_no_privacy_downgrade.py
    │   └── test_provenance_required.py
    ├── 🔌 integration/                 # real DB/adapters + API boundary
    │   ├── test_postgis_queries.py
    │   ├── test_graph_refs.py
    │   └── test_task_queue.py
    ├── 🤝 contract/                    # OpenAPI/schema expectations
    │   ├── test_openapi_contract.py
    │   ├── test_jsonschema_examples.py
    │   └── test_breaking_change_guard.py
    ├── 🧵 jobs/                        # async job orchestration behavior
    │   ├── test_job_lifecycle.py
    │   └── test_job_authz.py
    ├── 📡 realtime/                    # WS/SSE (if enabled)
    │   ├── test_ws_handshake.py
    │   └── test_sse_job_progress.py
    └── 🧪 fixtures/                    # small synthetic inputs (JSON/GeoJSON/CSV)
        ├── 📁 geo/
        │   ├── ks_bbox.json
        │   └── geometry_county.geojson
        ├── 📁 api/
        │   ├── field_minimal.json
        │   └── timeseries_ndvi.json
        ├── 📁 catalogs/
        │   ├── stac_collection_min.json
        │   ├── stac_item_min.json
        │   ├── dcat_dataset_min.json
        │   └── prov_run_min.json
        └── 📁 evidence/
            └── evidence_bundle_min.json
```

---

## 🧱 Test Types we expect in KFM

### 🧩 Unit tests (fast)
**Goal:** test small pieces of API logic (pure functions / helpers)

Examples:
- query param parsing
- response serialization (entity → JSON)
- validation rules for enums/ranges
- error mapping (domain error → HTTP error)

✅ Should run in < 1s locally.

---

### 🔌 Integration tests (real DB / real adapters)
**Goal:** verify behavior across layers when a real dependency matters:
- Postgres/PostGIS queries
- repository adapters
- migrations + schema expectations
- graph reference sync behavior (STAC IDs ↔ graph nodes)
- file/object storage stubs (local temp dirs)

**Recommended approach**
- run via `docker compose` with disposable DB containers
- isolate using unique schemas per test run, or recreate DB per run
- keep data tiny but realistic (a few features, not millions)

---

### 🤝 Contract tests (API shape guarantees)
**Goal:** keep the API predictable for UI + external integrators.

Examples:
- OpenAPI file is valid and includes expected endpoints
- response schema for `timeseries` is stable
- error responses always include agreed keys (`error.code`, `message`, `request_id`)
- examples validate against JSON Schema (if enforced)

> [!TIP]
> Contract tests are the “alarm system” for breaking changes.

---

### 🛰️ Geospatial / Remote Sensing endpoint tests
KFM is geo-heavy, so we treat these as first-class:

- GeoJSON validity (geometry type present, coordinates parse)
- correct content-type headers (`application/geo+json`)
- bbox sanity (west < east, south < north)
- CRS expectations (documented + consistent)
- tile endpoints return expected binary content + caching headers (if used)
- *no silent projection mixing* (if an endpoint uses 3857 tiles, tests must assert it)

---

### 🧵 Long-running jobs (simulations, ML, heavy processing)
For “start job” endpoints:
- ✅ returns `job_id`
- ✅ returns quickly (usually `202 Accepted`)
- ✅ status polling endpoint transitions correctly (queued → running → succeeded/failed)
- ✅ unauthorized users cannot query others’ jobs
- ✅ job result references are **catalog-backed** (or explicitly “not published yet”)

---

### 📡 Real-time updates (WebSockets/SSE)
If enabled:
- handshake tests
- subscription authorization tests
- basic message schema tests
- backpressure safety (no unbounded message spam)

---

## 🧪 Writing a new API test

### ✅ Minimum checklist per new endpoint
For each new route, include:

- ✅ happy path (200/201/202)
- ✅ invalid input (400/422)
- ✅ not found (404) where applicable
- ✅ unauthorized (401)
- ✅ forbidden (403) for role-gated endpoints
- ✅ serialization shape checks (keys + types that matter)
- ✅ governance checks (classification label present; redaction warnings if expected)
- ✅ provenance/evidence pointers when response implies a claim

### 🧠 Keep tests readable
Prefer **Arrange → Act → Assert**, short fixtures, and explicit intent.

```python
# Arrange
# Act
# Assert
```

---

## 🧰 Fixtures & Test Data Rules

### 📦 Fixtures
- Put shared fixtures in `conftest.py`
- Prefer small explicit fixtures over massive “kitchen sink” payloads
- Name fixtures by domain intent (e.g., `viewer_token`, `admin_token`, `ks_county_geojson`)

### 🧬 Synthetic test data
- Don’t copy production datasets into tests
- Use *small*, *representative* samples
- Store reusable payloads under `fixtures/` as JSON/GeoJSON/CSV

### 🧊 “No network” rule (recommended)
- CI blocks outbound network by default
- Tests that require recorded responses use local fixtures or VCR-style recorded payloads

---

## 🔐 Auth testing tips

If using JWT-like tokens:
- include fixtures for:
  - valid viewer token
  - expired token
  - admin token
  - token missing roles/scopes
  - token with wrong issuer/audience

Also verify:
- ownership rules (resource belongs to user/org)
- classification gates (restricted dataset requires appropriate scope)
- redaction is applied consistently regardless of client

---

## 🧯 Common pitfalls

- 🕒 **Timezones & date parsing** — always use ISO-8601, include timezone when needed
- 🎲 **Randomness** — seed non-deterministic code paths and assert seed captured
- 🗃️ **DB state leakage** — cleanup via transactions or recreate DB/schema per run
- 🌍 **External API calls** — block network or stub everything
- 🧠 **“Success but wrong classification”** — treat as a test failure; governance is part of correctness
- 🧾 **Uncited claims** — if output implies a conclusion, ensure provenance pointers are present

---

## ✅ Definition of Done (DoD) for API work

A change is “done” when:

- [ ] tests added/updated for new or changed behavior
- [ ] tests pass locally (`pytest api/tests`)
- [ ] CI is green (no merges on red)
- [ ] contract/shape remains stable (or versioned intentionally)
- [ ] any new fixtures are minimal + documented
- [ ] governance is tested: classification + redaction + provenance pointers (when required)

---

## 📚 Handy pytest patterns

- Filter by keyword: `-k timeseries`
- Re-run last failures: `--lf`
- Show slow tests: `--durations=20`
- Markers (recommended):
  - `@pytest.mark.unit`
  - `@pytest.mark.integration`
  - `@pytest.mark.contract`
  - `@pytest.mark.security`
  - `@pytest.mark.slow`

---

## 📦 CI hardening (recommended)

These improvements align with KFM’s “governed boundary” posture:

- 🧱 `docker-compose.test.yml` for integration tests (clean, disposable stack)
- 📈 Coverage reporting (`pytest --cov ...`) with sensible thresholds
- 🚫 Block outbound network in CI (enforce determinism)
- 🧾 Contract diff checks: fail on breaking changes unless versioned
- 🧷 Governance regression suite:
  - redaction cannot regress
  - classification cannot downgrade
  - provenance pointers required for claim-like outputs
- 🧨 Fuzz-lite tests for GeoJSON parsing and upload endpoints (bounded size)

---

## 📚 Project reference library → testing rules (uses all project files)

> Requirement: this section maps **every project file** to a concrete `api/tests` expectation, guardrail, or test type.

<details>
<summary><strong>🧠 Expand: Influence map (all project files)</strong></summary>

| Project file | Testing impact (what it changes in `api/tests/`) |
|---|---|
| `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx` | Adds boundary invariants as tests (catalog gate, evidence bundles, Story/Focus flows), plus system flow assertions (publish requires STAC/DCAT/PROV) |
| `Latest Ideas.docx` | Drives policy-as-code tests (classification propagation, redaction regression), and CI “fail fast” checks for governance drift |
| `Data Spaces.pdf` | Enforces pointer-over-payload expectations: tests assert the API returns stable IDs/links rather than dumping giant blobs |
| `Introduction to Digital Humanism.pdf` | Adds tests ensuring AI-assisted outputs are labeled and user-facing claims are auditable (provenance pointers present) |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | Encourages explicit job state transitions & feedback-loop checks (job lifecycle tests, cancellation semantics, bounded retries) |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | Drives audit-ready AI tests: model/version/config captured; “explainability hooks” exist via evidence bundles |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | Adds remote sensing endpoint tests: time-series shapes, compositing parameters recorded, export jobs are async and catalog-backed |
| `python-geospatial-analysis-cookbook.pdf` | CRS and geometry validity tests: SRID assumptions, bbox sanity, PostGIS operation correctness |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | Adds tests for legend/ramp endpoints or metadata: avoid misleading defaults; ensure attribution/provenance is included when serving cartographic assets |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | Adds offline/low-bandwidth considerations: caching headers on tiles, payload size bounds, and sensitivity labeling for location-centric outputs |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | Integration tests for indexing/pagination correctness, query bounds, and migration expectations |
| `Scalable Data Management for Future Hardware.pdf` | Performance-guard tests: prevent unbounded responses; enforce limits and server-side pagination on list endpoints |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | Adds concurrency tests: job queue behavior, backpressure, and safe “no blocking in request thread” expectations |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | Security regression tests: auth bypass attempts, request size limits, SSRF protections, and safe error handling (no stack traces) |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | Hardening tests: fuzz-lite parsing inputs, malicious payload handling, and validation failures that don’t leak internals |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | Tests for image/quicklook endpoints: correct content-type, size limits, and consistent caching behavior |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | Tests for 3D asset endpoints (if any): coordinate metadata present, safe serving headers, graceful failure shapes |
| `Spectral Geometry of Graphs.pdf` | Graph endpoints tests: bounded subgraph queries, stable IDs, and explainable/consistent metrics (no “mystery graph math”) |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | Simulation tests: reproducibility (seed captured), V&V artifact presence, explicit assumptions metadata, and job lifecycle correctness |
| `Generalized Topology Optimization for Structural Design.pdf` | Optimization job tests: objective/constraints metadata recorded, deterministic configs, artifact pointers not blobs |
| `Understanding Statistics & Experimental Design.pdf` | Analytics endpoint tests require assumptions/uncertainty fields; avoid “overclaiming” outputs without context |
| `graphical-data-analysis-with-r.pdf` | Tests for EDA artifacts: distributions/outlier summaries returned deterministically and labeled properly |
| `regression-analysis-with-python.pdf` | Regression endpoints must include diagnostics fields or evidence pointers (residual checks, fit metrics) |
| `Regression analysis using Python - slides-linear-regression.pdf` | Normalizes regression response shape tests (coef tables, metrics), ensuring UI compatibility |
| `think-bayes-bayesian-statistics-in-python.pdf` | Bayesian endpoint tests: prior disclosed, posterior summaries include credible intervals, outputs are reproducible |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | ML job tests: training is async, artifacts are cataloged, and model-card-like metadata exists |
| `A programming Books.pdf` | Contributor shelf: encourages language-agnostic test hygiene and repeatable tooling patterns |
| `B-C programming Books.pdf` | Contributor shelf |
| `D-E programming Books.pdf` | Contributor shelf |
| `F-H programming Books.pdf` | Contributor shelf |
| `I-L programming Books.pdf` | Contributor shelf |
| `M-N programming Books.pdf` | Contributor shelf |
| `O-R programming Books.pdf` | Contributor shelf |
| `S-T programming Books.pdf` | Contributor shelf |
| `U-X programming Books.pdf` | Contributor shelf |
| `responsive-web-design-with-html5-and-css3.pdf` | Tests that drive UI safety: stable response shapes, caching headers, and payload-size discipline (since UI performance depends on it) |

</details>

---

🧭 **KFM test suite motto:** if it’s not **governed**, **reproducible**, and **defensible**, it’s not done.