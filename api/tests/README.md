# 🧪 API Test Suite (`api/tests/`)

![pytest](https://img.shields.io/badge/pytest-ready-blue) ![fastapi](https://img.shields.io/badge/FastAPI-tested-009688) ![governance](https://img.shields.io/badge/fail--closed-governance-critical-red)

Welcome to the **KFM API test suite** ✅  
This folder is the home for **unit**, **integration**, and **contract-style** tests that keep the FastAPI backend reliable, reproducible, and safe-by-default.

---

## 🎯 What these tests protect

### ✅ Reliability & regressions
- Endpoints keep returning the expected **status codes** and **response shapes**
- Service-layer logic stays correct as models evolve
- Query filters/pagination don’t silently break

### 🔐 Governance & “fail-closed” behavior
- If a policy/validation check fails, the API must **block** the action (not “best effort”)
- Sensitive/special cases must return the **expected error** (403/422/400/etc.)
- Changes that would weaken guardrails should be caught early

### 🧾 Provenance-first mindset
- Prefer deterministic tests and fixture-driven expectations
- Keep test data small, explicit, and easy to audit

---

## ⚡ Quickstart

> Most common workflow: run tests **inside the API container**.

### 🐳 Docker Compose (recommended)
From the repo root:

```bash
# if the stack isn't already running
docker-compose up -d

# run all backend tests
docker-compose exec api pytest
```

### 🧰 Helpful pytest commands
```bash
# run a single test file
docker-compose exec api pytest api/tests/test_health.py

# run tests matching a substring
docker-compose exec api pytest -k "datasets"

# show prints/logs (useful when debugging)
docker-compose exec api pytest -s

# fail fast on first error
docker-compose exec api pytest -x
```

> If your tests require databases (PostGIS/Neo4j), make sure the compose stack is up.

---

## 🗂️ Recommended directory layout

> Your repo may vary — this is a **suggested** structure that scales well.

```text
api/tests/
├── README.md                # 👈 you are here
├── conftest.py              # 🧩 shared pytest fixtures
├── unit/                    # ✅ fast, pure-python tests
│   ├── test_services_*.py
│   └── test_models_*.py
├── integration/             # 🔌 API + DB/Adapters (TestClient + test DB)
│   ├── test_routes_*.py
│   └── test_authz_*.py
├── contract/                # 📜 schema & contract checks (OpenAPI/GraphQL)
│   ├── test_openapi_*.py
│   └── test_graphql_*.py
└── fixtures/                # 🧪 small JSON/GeoJSON/CSV fixtures
    ├── datasets/
    ├── stories/
    └── graph/
```

---

## 🧩 Fixtures & test data rules

### ✅ DO
- Keep fixtures **minimal** (small JSON/GeoJSON snippets)
- Use factories/helpers to build valid Pydantic models quickly
- Prefer **explicit** test setup over “magic” data generation
- Use temp dirs (`tmp_path`) for any filesystem writes

### ❌ DON’T
- Don’t commit large datasets here (tests should stay fast ⚡)
- Don’t include secrets, tokens, or any real sensitive data
- Don’t mutate “raw” pipeline inputs (treat them as read-only evidence)

---

## 🧪 Writing tests (practical patterns)

### 1) Unit tests (fast, isolated)
Use these for:
- service-layer logic
- parsing/validation helpers
- domain rules
- small transformers that don’t require a DB

✅ Preferred traits:
- no network
- no DB (or mocked repository interfaces)
- deterministic

---

### 2) Integration tests (end-to-end-ish)
Use these for:
- router behavior (inputs/outputs)
- dependency injection wiring
- authorization + governance checks
- DB adapters (PostGIS/Neo4j) using test fixtures

Typical approach:
- Load fixtures (or seed a test DB)
- Call endpoints through **FastAPI TestClient**
- Assert on the JSON + status code

---

### 3) Contract tests (schemas must stay honest)
Use these for:
- OpenAPI schema invariants
- GraphQL schema invariants (if enabled)
- “Known input → known output contract” checks for critical endpoints

---

## 🧭 Manual API exploration (great for debugging)
Even with tests, it’s helpful to quickly poke the API:

- Swagger UI: `http://localhost:8000/docs` 🧭  
- GraphQL (if enabled): `http://localhost:8000/graphql` 🧬

---

## 🧱 CI expectations (what will block your PR)

Most repos run these checks automatically in CI:

- ✅ **Backend tests** (`pytest`)
- 🧹 Lint/format checks (e.g., `black --check`, `flake8`, etc.)
- 📜 API contract tests (OpenAPI/GraphQL expectations)
- 🔍 Policy & governance scans (secret/PII/sensitive checks)
- 🧾 Documentation/link/schema validation (where configured)

**Rule of thumb:**  
If you change behavior, **add or update tests** in the same PR. ✅

---

## 🧯 Troubleshooting

### Ports / container readiness
If DB containers are still starting, tests may fail with connection errors.  
Try re-running after the stack is fully healthy:

```bash
docker-compose ps
docker-compose logs -f api
```

### “It works in Swagger but fails in tests”
- Make sure your test fixtures match the seeded data (or the mocked adapters)
- Confirm the route prefix/version (`/api/v1/...`) used by the app

---

## ✅ Test-writing checklist (copy/paste)

- [ ] I wrote/updated a unit test for the service logic (when applicable)
- [ ] I wrote/updated an integration test for the endpoint behavior (when applicable)
- [ ] I asserted **status code + response shape**
- [ ] I added at least one **negative** test (bad input / forbidden action)
- [ ] Tests run locally via `docker-compose exec api pytest`
- [ ] No secrets / sensitive data added anywhere 🛑

---

### 🧠 Tip
If you’re unsure where a behavior belongs:
- **Unit test** the “rule”
- **Integration test** the “wiring” (router + DI + adapter calls)
- **Contract test** the “promise” (schema + stable responses)