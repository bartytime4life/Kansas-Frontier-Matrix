# 🧪 `api/tests` — API Test Suite

![pytest](https://img.shields.io/badge/tests-pytest-blue)
![FastAPI](https://img.shields.io/badge/api-FastAPI-009688)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-black)
![Style](https://img.shields.io/badge/style-black%2Fflake8-friendly)

> [!NOTE]
> This folder is the home for the backend test suite: **unit tests for service/use-case logic** and **integration tests for API endpoints**.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🎯 What lives here?

KFM’s backend typically includes an `api/tests/` directory with:
- ✅ **Unit tests** for service functions (fast, isolated)
- ✅ **Integration tests** for API endpoints (FastAPI test client + fixtures) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Why this matters: the API is the **central control plane** (routing, dependency injection, governance checks), so tests protect both correctness and policy enforcement.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ⚡ Quick start

### Option A — Run tests in Docker Compose ✅ (recommended)

KFM’s workflow expects a live Compose dev stack so you can run tests from a second terminal.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

```bash
# from repo root
docker-compose up -d
docker-compose exec api pytest
```

`pytest` is the standard backend test runner, and CI also runs it on PRs.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> [!TIP]
> If your project uses Docker v2 syntax, replace `docker-compose` with `docker compose`.

### Option B — Run tests locally (no Docker)

If you’re running the API natively (venv/uv/pip), install the backend + dev deps, then:

```bash
# from repo root or ./api depending on how dependencies are wired
pytest
```

---

## 🧱 Suggested test layout

> [!IMPORTANT]
> Keep tests aligned to the architecture: **domain/service tests should not require DB/network**, while endpoint tests can validate full request/response behavior.

<details>
<summary><strong>📁 Example folder tree (recommended)</strong></summary>

```text
📁 api/
  📁 tests/
    📄 README.md
    📄 conftest.py
    📁 unit/
      📄 test_services_*.py
      📄 test_domain_*.py
    📁 integration/
      📄 test_routes_*.py
      📄 test_graphql_*.py
    📁 contract/
      📄 test_openapi_*.py
    📁 fixtures/
      📄 *.json
      📄 *.geojson
```
</details>

---

## 🧠 Test philosophy (matches KFM’s architecture)

### ✅ Unit tests = *Service/use-case correctness*
KFM’s clean architecture separates core logic from adapters so you can test service logic in isolation using mock data.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Unit tests should:**
- Avoid DB / HTTP / filesystem unless explicitly testing adapters
- Exercise domain + service rules (pure Python/Pydantic)
- Be fast enough to run constantly during development

### 🔌 Integration tests = *Endpoint behavior + governance*
Integration tests commonly:
- Build/seed **fixtures** (small, deterministic)
- Call endpoints using **FastAPI’s test client**
- Assert status codes + response bodies + errors + auth/policy gates [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ✍️ Writing new tests

### 1) Adding a **service/use-case** test (unit)

**Where:** `api/tests/unit/`

**Pattern:**
- Arrange: build domain objects + inputs
- Act: call service function
- Assert: validate returned domain model / computation / decision rules

```python
def test_example_service_rule():
    # Arrange
    # domain_obj = ...
    # Act
    # result = some_service(domain_obj)
    # Assert
    # assert result == expected
    pass
```

### 2) Adding a **route/endpoint** test (integration)

**Where:** `api/tests/integration/`

**Pattern:**
- Use fixtures to build data (or point to a test DB)
- Use FastAPI test client to call the route
- Assert response + headers + any governance/policy behavior [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

```python
def test_example_endpoint(client):
    resp = client.get("/datasets")  # example endpoint (if present)
    assert resp.status_code in (200, 404)
```

> [!TIP]
> Prefer asserting **behavior** (status, schema, meaning) over brittle exact payloads unless the payload is stable and intentional.

---

## 🧩 Fixtures & determinism

KFM emphasizes **deterministic, reproducible** pipelines; tests should follow the same rule: no hidden randomness, no “works on my machine” data.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Rules of thumb:**
- ✅ Keep fixtures tiny and explicit
- ✅ Use stable seeds if randomness is unavoidable
- ✅ Avoid external network calls (mock adapters instead)
- ✅ Never depend on large `data/raw/` artifacts in unit tests

---

## 🤖 CI expectations (don’t fight the pipeline)

On PRs, CI typically runs:
- ✅ backend tests via `pytest`
- ✅ linters/formatters
- ✅ policy checks (Conftest/Rego) [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Local policy checks can be simulated with:

```bash
conftest test .
```

…and CI will tell you which policy rule failed (e.g., missing dataset metadata).  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🛠️ Useful pytest commands

<details>
<summary><strong>⚙️ Common invocations</strong></summary>

```bash
# run everything
pytest

# quiet output
pytest -q

# only matching tests
pytest -k "datasets and not slow"

# stop on first failure
pytest -x

# show stdout/stderr
pytest -s
```
</details>

---

## 🧯 Troubleshooting

### API can’t connect to DB / services
- Check logs: `docker-compose logs api`
- Compose sometimes needs a restart if dependencies weren’t ready.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### Port conflicts
If something is already using Postgres/Neo4j/API ports, either stop it or adjust mappings.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### Dependency changes not picked up
If you changed requirements, rebuild:

```bash
docker-compose up --build -d
# or
docker-compose build
```

 [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📚 References (project grounding)

- Kansas Frontier Matrix (KFM) — Comprehensive Technical Blueprint (architecture, CI, tests)  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---