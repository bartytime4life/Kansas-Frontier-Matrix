# 🧪 API Test Suite (`api/tests`)

![Tests](https://img.shields.io/badge/tests-automated-blue)
![Style](https://img.shields.io/badge/style-clean%20architecture-3c4)
![API](https://img.shields.io/badge/API-REST%20%2B%20GeoJSON-7aa)

Welcome to the **API boundary test suite** for the Kansas Frontier Matrix (KFM) backend.  
This folder is for testing the **web/API layer**: routing, request/response validation, auth, serialization, and orchestration behavior.

---

## 🎯 What lives here?

This directory focuses on **API-facing behavior**:

- ✅ Request parsing + validation (query params, request bodies, headers)
- ✅ Authentication & authorization behavior (401/403, role checks, token expiry)
- ✅ Response shapes (JSON / GeoJSON / CSV / tiles) and status codes
- ✅ Error semantics (400 vs 404 vs 422 vs 500) + safe messages
- ✅ “Thin controller” rules: API layer calls **use-cases/services** and formats output

> 💡 The API should stay **thin**: it validates inputs, delegates to application logic, and formats outputs.

---

## 🧭 Test Philosophy (KFM-friendly)

### 🧼 Clean Architecture first
- **Core logic should be testable without the framework.**
- API tests are **not** where business rules live — they verify the boundary glue.

### 🧊 Deterministic & reproducible
- No live calls to remote sensing services / Earth Engine / external APIs.
- Prefer fakes/stubs/recorded responses for external dependencies.
- Seed randomness when ML/simulation endpoints are involved.

### 🧯 Safe by default
- Never point tests at production infrastructure.
- Integration tests must use **test databases** and disposable containers.

---

## ⚡ Quickstart

From repo root:

```bash
python -m pytest api/tests -q
```

Run a single test file:

```bash
python -m pytest api/tests/test_timeseries.py -q
```

Run tests matching a keyword:

```bash
python -m pytest api/tests -k timeseries -q
```

Stop on first failure + show locals:

```bash
python -m pytest api/tests -x --showlocals
```

> 🧩 If your repo provides a `Makefile`, it’s recommended to add:
> - `make test`
> - `make test-api`
> - `make test-integration`

---

## 🗂️ Suggested folder layout

> If your test suite grows, use a structure like this 👇

```text
📦 api/
└── 🧪 tests/
    ├── 📄 README.md
    ├── 🧰 conftest.py              # shared fixtures (client, tokens, db, etc.)
    ├── 🧩 unit/                    # pure unit tests for API helpers (no DB)
    │   ├── test_validation.py
    │   └── test_serialization.py
    ├── 🌐 routes/                  # endpoint tests (FastAPI/Flask routes)
    │   ├── test_health.py
    │   ├── test_fields_timeseries.py
    │   ├── test_simulation_run.py
    │   └── test_data_upload.py
    ├── 🔐 auth/                    # authn/authz tests
    │   ├── test_jwt.py
    │   └── test_rbac.py
    ├── 🔌 integration/             # DB + repository + API boundary
    │   ├── test_postgis_queries.py
    │   └── test_task_queue.py
    ├── 🤝 contract/                # OpenAPI/schema expectations
    │   └── test_openapi_contract.py
    └── 🧪 fixtures/                # small, synthetic JSON/GeoJSON/CSV inputs
        ├── field_minimal.json
        ├── timeseries_ndvi.json
        └── geometry_county.geojson
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
- repository adapters (SQLAlchemy/raw SQL)
- migrations + schema expectations
- file/object storage stubs (local temp dirs)

**Recommended approach:**
- run via `docker compose` using a disposable test database container
- isolate using unique schemas or re-create DB per run

---

### 🤝 Contract tests (API shape guarantees)
**Goal:** keep the API predictable for front-end and external integrators.

Examples:
- OpenAPI is generated and includes expected endpoints
- response schema for `timeseries` is stable
- error responses always include `error_code` + `message` (if that’s the project rule)

---

### 🛰️ Geospatial / Remote Sensing endpoint tests
KFM is geospatial-heavy, so we treat these as first-class:

- GeoJSON validity (geometry type present, coordinates parse)
- correct content-type headers
- bbox sanity checks (west < east, south < north)
- coordinate reference expectations (documented + consistent)
- tile endpoints return expected binary content + caching headers (if used)

---

### 🧵 Long-running jobs (simulations, ML, heavy processing)
For “start job” endpoints:
- ✅ returns a `job_id`
- ✅ returns quickly (typically `202 Accepted` or similar)
- ✅ status polling endpoint transitions correctly
- ✅ unauthorized users cannot query others’ jobs

---

### 📡 Real-time updates (WebSockets/SSE)
If enabled:
- handshake tests
- subscription authorization tests
- basic message schema tests

---

## 🧪 Writing a new API test

### ✅ Minimum checklist per new endpoint
For each new route, include:

- ✅ **happy path** (200/201/202)
- ✅ **invalid input** (400/422)
- ✅ **not found** (404) when applicable
- ✅ **unauthorized** (401)
- ✅ **forbidden** (403) for role-gated endpoints
- ✅ **serialization** shape check (keys + types that matter)

### 🧠 Keep tests readable
Prefer **Arrange → Act → Assert** and short fixtures.

```python
# Arrange
# Act
# Assert
```

---

## 🧰 Fixtures & Test Data Rules

### 📦 Fixtures
- Put shared fixtures in `conftest.py`
- Prefer small, explicit fixtures over massive “kitchen sink” objects
- Keep fixture names domain-specific (e.g., `field_id`, `ndvi_timeseries`)

### 🧬 Synthetic test data
- Don’t copy production datasets into tests
- Use *small*, *representative* samples
- Store reusable payloads under `fixtures/` as JSON/GeoJSON/CSV

---

## 🔐 Auth testing tips

If using JWT-like tokens:
- include fixtures for:
  - valid user token
  - expired token
  - admin token
  - token with missing role claims

Also verify:
- endpoints enforce ownership rules (e.g., field belongs to user/org)

---

## 🧯 Common pitfalls

- 🕒 **Timezones & date parsing** (always specify ISO-8601 in tests)
- 🎲 **Randomness** (seed any non-deterministic code paths)
- 🗃️ **DB state leakage** (ensure cleanup / transactions / recreate DB)
- 🌍 **External API calls** (block network in CI unless explicitly allowed)

---

## ✅ Definition of Done (DoD) for API work

A change is “done” when:

- [ ] tests added/updated for new or changed behavior
- [ ] tests pass locally (`pytest api/tests`)
- [ ] CI is green (no merges on red)
- [ ] contract/shape remains stable (or is versioned intentionally)
- [ ] any new fixtures are minimal + documented

---

## 🧾 KFM-flavored endpoint examples to cover

These are typical patterns we want strong coverage for:

- `GET /api/field/{field_id}/timeseries?var=ndvi`
- `POST /api/simulation/run`
- `POST /api/data/upload` (admin / privileged)
- any GeoJSON or tile-serving endpoints (if present)

---

## 📚 Handy pytest patterns

- Filter by keyword: `-k timeseries`
- Re-run last failures: `--lf`
- Show slow tests: `--durations=20`
- Add markers for test classes (recommended):
  - `@pytest.mark.unit`
  - `@pytest.mark.integration`
  - `@pytest.mark.contract`
  - `@pytest.mark.slow`

---

## 🔄 Next improvements (nice-to-have)

- 🧱 Add `docker-compose.test.yml` for integration tests
- 📈 Add coverage reporting in CI (`pytest --cov ...`)
- 🚫 Block outbound network in CI to enforce deterministic tests
- 🧾 Add OpenAPI contract test that fails on accidental breaking changes