<!-- According to a document from 2026-02-03 -->

# 🧪 API Tests (KFM) — `api/tests/`

![Python](https://img.shields.io/badge/Python-3.x-blue)
![pytest](https://img.shields.io/badge/pytest-test%20runner-brightgreen)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20server-teal)
![Docker](https://img.shields.io/badge/Docker-Compose-informational)
![OPA](https://img.shields.io/badge/OPA-Policy%20as%20Code-purple)

> ✅ **Testing mantra:** **Evidence-first. Policy-gated. Reproducible.**  
> 🧷 **No Source, No Answer** is a *feature*, not a suggestion.

---

## 📚 What lives here?

This folder contains the **backend API test suite** for the Kansas Frontier Matrix (KFM) server:
- REST endpoints (OpenAPI / Swagger)
- GraphQL endpoint (if enabled)
- “Focus Mode” AI endpoint (RAG pipeline + citations + policy checks)
- Security & governance behaviors (RBAC / policy enforcement)
- Integration behavior with core services (PostGIS, Neo4j, search, vector store, etc.)

---

## ⚡ Quickstart

### 1) Bring up the dev stack 🐳
```bash
docker-compose up -d
# or
docker compose up -d
```

### 2) Run the backend tests ✅
```bash
docker-compose exec api pytest
# (some stacks name the service api-server)
docker-compose exec api-server pytest
```

### 3) Run policy checks (if you have Conftest) 🛡️
```bash
conftest test .
# or target the repo policy directory, e.g.
conftest test policy/
```

> 💡 Keep the compose stack running during development so integration tests can hit real services.

---

## 🧭 Test philosophy (KFM-specific)

KFM isn’t a “basic CRUD API.” The backend includes an **AI-assisted RAG pipeline** and **policy enforcement** at runtime. That means our tests must validate not only correctness, but also **trust guarantees**:

### 🔎 Core guarantees we test
- **Citations exist** and match the required bracket format: `[1]`, `[2]`, …  
- **Prompt injection is neutralized** (Prompt Gate behavior)
- **Policy checks run** (OPA / Rego) and can deny unsafe or un-cited output
- **Role-based access control** works for sensitive datasets
- **Contracts don’t drift** (OpenAPI + response schemas)
- **Provenance/audit hooks** are triggered where expected

---

## 🗂️ Recommended folder layout

> Your exact structure may vary — but please keep *intent* clear.

```text
api/tests/
  README.md                👈 you are here
  conftest.py              🧩 shared pytest fixtures
  unit/                    🧪 fast tests (no network / no DB)
  contract/                📜 OpenAPI + schema + response-shape tests
  integration/             🧱 requires Docker services (PostGIS/Neo4j/etc.)
  ai/                      🤖 Focus Mode + citation + policy gating tests
  security/                🛡️ authn/authz + negative access tests
  fixtures/                🧰 small deterministic datasets & payloads
```

---

## 🧷 pytest markers (recommended)

Use markers so CI can run fast-by-default:

- `unit` — pure logic, no IO  
- `contract` — schema & endpoint shape  
- `integration` — needs Docker services running  
- `ai` — Focus Mode (may mock LLM by default)  
- `slow` — big queries / heavier seeds

Example:
```bash
pytest -m unit
pytest -m "not integration"
pytest -m "integration and not slow"
pytest -m "ai and not slow"
```

---

## 🧩 Fixtures & patterns

### ✅ FastAPI client
Provide a `client` fixture that builds the app in **test mode** and uses `TestClient` / `httpx`:
- Avoid “real network” in unit tests.
- Prefer dependency overrides (DB session, policy engine, model client).

### 🧪 Deterministic data
- Keep fixtures tiny and readable (`api/tests/fixtures/`).
- Prefer explicit IDs in tests (`ks_hydrology_1880` style IDs are great).
- Use seeds/migrations only in integration tests.

### 🤖 LLM handling in tests
Most tests should NOT require a real model:
- Mock the Ollama/OpenAI client (return predictable text + citations)
- Assert the pipeline **rejects** un-cited answers
- Add *optional* “real model” tests behind a marker/flag

Example (pattern):
- default: `pytest -m ai` runs mocked model tests
- optional: `pytest -m ai --run-real-ollama` runs end-to-end (developer machine only)

---

## ✅ High-value test targets

### 🩺 Health & readiness
Test that “platform sanity” endpoints behave correctly:
- `GET /healthz`
- `GET /readyz`
- `GET /version` (or equivalent)

### 📜 OpenAPI contract tests
- `GET /openapi.json` returns valid JSON
- The OpenAPI schema includes core endpoints (datasets, search, AI if enabled)

### 🗃️ Data catalog & datasets
Contract + integration tests for:
- dataset metadata has license/title/description
- search supports filters (keyword, bbox, time range)
- dataset data endpoint supports format + bbox filtering

### 🧠 Focus Mode (AI) — trust tests
Minimum required behaviors:
- `POST /focus-mode/query` returns an answer containing citations like `[1]`
- Prompt injection attempts are removed/neutralized (Prompt Gate)
- Policy denies:
  - answers without citations
  - disallowed content
  - role violations for sensitive sources

### 🛡️ Security
- unauthorized users cannot access restricted datasets
- policy enforcement produces correct HTTP codes (`401/403`) and safe messages

---

## 🧪 “No Source, No Answer” regression tests

Because citations are a core UX + trust mechanic, keep a dedicated regression suite that tests:
- **missing citations ⇒ denied** (policy gate)
- **hallucinated citations ⇒ rejected** (if your implementation validates citation IDs)
- citation mapping attaches metadata (if the API/UI expects footnote links)

> 🧯 These tests prevent “it still answers, but without sources” regressions.

---

## 🧰 Troubleshooting (common dev issues)

### 🐳 Docker/Compose flakiness
- If a service isn’t ready, try re-running `docker-compose up` (or wait for healthchecks).
- Check logs:
  ```bash
  docker-compose logs api
  docker-compose logs db
  docker-compose logs neo4j
  ```

### 🔌 Port conflicts
- If `5432`, `7474`, `8000`, or `3000` are in use, stop local services or change compose ports.

### 🧱 Permissions on mounted volumes
- If the API can’t write to `data/` or a mounted path, ensure the directory is writable by the container user.

---

## ✅ Contribution checklist

Before you open a PR:

- [ ] New endpoint? **Add contract + behavior tests**
- [ ] Bug fix? **Add a regression test**
- [ ] Touch AI pipeline? **Add citation + policy gating coverage**
- [ ] Touch metadata/pipelines? **Run Conftest policy checks**
- [ ] CI green locally: `pytest` + policy checks

---

## 🔗 Useful cross-links

From the repo root, these docs usually matter for test authors:

- `src/server/api/README.md` — API surface area & examples  
- `docs/architecture/ai/OLLAMA_INTEGRATION.md` — Focus Mode / RAG pipeline behavior  
- `policy/` — OPA/Rego policies (governance gates)  
- `pipelines/README.md` — data build steps that may affect integration tests

---

## 🧠 Guiding principle

> If a test can’t explain **what trust guarantee it protects**, it probably belongs in `unit/` or doesn’t belong at all. 😉