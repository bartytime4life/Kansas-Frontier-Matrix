<!-- According to a document from 2026-02-03 -->

<div align="center">

# 🧪 API Tests (KFM) — `api/tests/`

**Evidence-first. Policy-gated. Reproducible.**  
🧷 *“No Source, No Answer”* is a **feature**, not a suggestion.

<br/>

![Python](https://img.shields.io/badge/Python-3.x-blue)
![pytest](https://img.shields.io/badge/pytest-test%20runner-brightgreen)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20server-teal)
![Docker](https://img.shields.io/badge/Docker-Compose-informational)
![PostGIS](https://img.shields.io/badge/PostGIS-spatial%20db-blueviolet)
![Neo4j](https://img.shields.io/badge/Neo4j-knowledge%20graph-important)
![OpenAPI](https://img.shields.io/badge/OpenAPI-contracts-orange)
![GraphQL](https://img.shields.io/badge/GraphQL-optional-ff69b4)
![OPA](https://img.shields.io/badge/OPA-Policy%20as%20Code-purple)
![Conftest](https://img.shields.io/badge/Conftest-OPA%20CLI-6f42c1)
![Ollama](https://img.shields.io/badge/Ollama-local%20LLM-black)

</div>

---

## 🧭 Why this test suite exists

KFM is **not** “just a CRUD API.” It’s a **governed geospatial knowledge platform** with:

- 🗺️ Spatial + temporal datasets (PostGIS)  
- 🧠 Knowledge graph relationships (Neo4j)  
- 🔎 Search + retrieval for evidence-backed answers  
- 🤖 Focus Mode (RAG) that must produce **cited** outputs  
- 🛡️ Runtime + CI policy gates (OPA/Rego + Conftest)  
- 🧾 Provenance / audit hooks (log what sources + policies produced what output)

This folder is where we encode those guarantees into executable proof.

> [!IMPORTANT]
> If the API returns a “nice answer” but it’s **uncited**, **policy-bypassing**, or **un-auditable**… that’s a **bug**.

---

## 🗺️ Table of contents

- [📦 What lives here](#-what-lives-here)
- [🏛️ Architectural contracts we enforce](#️-architectural-contracts-we-enforce)
- [⚡ Quickstart](#-quickstart)
- [🧪 How to run tests](#-how-to-run-tests)
- [🧷 pytest markers](#-pytest-markers)
- [🗂️ Suggested folder layout](#️-suggested-folder-layout)
- [🤖 Focus Mode test playbook](#-focus-mode-test-playbook)
- [🛡️ Policy, security, and governance tests](#️-policy-security-and-governance-tests)
- [📜 Contract tests](#-contract-tests)
- [🧰 Troubleshooting](#-troubleshooting)
- [✅ Contribution checklist](#-contribution-checklist)
- [🔗 Useful cross-links](#-useful-cross-links)

---

## 📦 What lives here?

This directory contains the **backend API test suite** for KFM:

- 🌐 REST endpoints (OpenAPI / Swagger)
- 🧬 GraphQL endpoint (if enabled)
- 🤖 Focus Mode AI endpoint (RAG + citations + policy checks)
- 🛡️ Security & governance behaviors (AuthN/AuthZ + RBAC + sensitivity rules)
- 🔌 Integration with core services (PostGIS, Neo4j, search, vector store, object storage, etc.)
- 🧾 Provenance / audit hooks (answers and data releases must be traceable)

---

## 🏛️ Architectural contracts we enforce

KFM’s “trust story” is built on a few non-negotiable contracts. Tests exist to prevent drift.

### 1) ✅ The Truth Path must be respected
**Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI**

No “back doors,” no direct DB calls from UI, no unpublished data leaking via internal endpoints.

### 2) ✅ Fail closed by default
If metadata is missing, policy is uncertain, or evidence is insufficient → the system must **block**.

### 3) ✅ Focus Mode is advisory-only + explainable
The model is treated like an **untrusted narrator**:
- It can generate text
- It must cite
- It cannot bypass governance
- Its output must be policy-checked and auditable

---

## ⚡ Quickstart

> [!TIP]
> Keep the Compose stack running while you develop so integration tests can hit real services.

### 1) Bring up the dev stack 🐳
```bash
docker compose up -d
# legacy:
docker-compose up -d
```

### 2) Sanity-check the API is reachable 🔎
```bash
# Swagger UI (typical default)
open http://localhost:8000/docs

# Optional: readiness endpoint (if implemented)
curl -sS http://localhost:8000/readyz || true
```

### 3) Run the backend tests ✅
```bash
# common service name:
docker compose exec api pytest

# some stacks name the service api-server:
docker compose exec api-server pytest
```

### 4) Run policy checks (Conftest) 🛡️
```bash
# run all policies (repo-wide)
conftest test .

# or target the policy directory
conftest test policy/
```

---

## 🧪 How to run tests

### Run fast-by-default_patch-first 🧩
```bash
pytest -m "not integration and not slow"
```

### Run a single suite 📌
```bash
pytest api/tests/unit
pytest api/tests/contract
pytest api/tests/integration
pytest api/tests/ai
pytest api/tests/security
```

### Run with higher signal logs 🧯
```bash
pytest -q --disable-warnings -rA
```

### Parallelize locally (optional) ⚡
```bash
pytest -n auto
```

---

## 🧷 pytest markers

Markers keep CI fast and local runs intentional:

- `unit` — pure logic, no IO  
- `contract` — schema & endpoint shape  
- `integration` — requires Docker services running  
- `ai` — Focus Mode (mocked by default)  
- `security` — authn/authz + negative access tests  
- `policy` — policy pack behavior (OPA/Rego)  
- `slow` — big queries / heavy seeds / expensive paths  
- `external` — hits a remote API (off by default)

Example:
```bash
pytest -m unit
pytest -m "contract and not slow"
pytest -m "integration and not slow"
pytest -m "ai and not slow"
pytest -m "security or policy"
```

> [!NOTE]
> Add marker definitions to `pytest.ini` (or `pyproject.toml`) so unknown-markers don’t silently rot.

---

## 🗂️ Suggested folder layout

> Your exact structure may vary — but keep *intent* obvious.

```text
api/tests/
  README.md                👈 you are here 📍
  conftest.py              🧩 shared pytest fixtures
  unit/                    🧪 fast tests (no network / no DB)
  contract/                📜 OpenAPI + schema + response-shape tests
  integration/             🧱 requires Docker services (PostGIS/Neo4j/etc.)
  ai/                      🤖 Focus Mode + citation + policy gating tests
  security/                🛡️ authn/authz + negative access tests
  policy/                  🧷 targeted Rego/OPA behavior tests (if needed)
  performance/             ⏱️ smoke tests + regression guardrails (optional)
  fixtures/                🧰 tiny deterministic datasets & payloads
  golden/                  🏆 “golden” expected outputs (optional; keep small)
```

---

## 🧩 Fixtures & patterns

### ✅ FastAPI test client
Prefer in-process clients (`TestClient` / `httpx`) for unit/contract tests:
- Avoid “real network” for unit tests  
- Use dependency overrides:
  - DB session / repository layer
  - policy engine client
  - model client (Ollama/OpenAI/etc.)
  - clock/time provider (for reproducible timestamps)

### 🧪 Deterministic test data
- Keep fixtures tiny and readable (`api/tests/fixtures/`)
- Prefer explicit IDs (example style: `ks_hydrology_1880`)
- Use migrations/seeding **only** in integration tests
- Treat fixture files like public API: stable, small, and versioned

### 🧾 Audit/provenance assertions
Where applicable, validate:
- an audit event was emitted
- the event includes source IDs, policy decision outcome, and request metadata
- the logging path is append-only (implementation-dependent)

---

## 🤖 Focus Mode test playbook

Focus Mode is a trust-critical surface. A “correct but uncited” answer is a failing behavior.

### 🔎 Minimum trust guarantees to test

#### ✅ Citations required
- Answer contains bracket citations: `[1]`, `[2]`, …
- Citations map to actual source metadata in the response payload (if your API returns it)

#### ✅ Prompt injection is neutralized
- Injection attempts do not alter system policy or reveal restricted data
- Prompt Gate behavior is observable (sanitize/strip/escape)

#### ✅ Policy enforces the output contract (OPA/Rego)
- **Missing citations ⇒ denied**
- **Disallowed content ⇒ denied**
- **Role violation ⇒ denied**
- Safe, non-leaky error messaging when denied

#### ✅ Provenance is recorded
- Question, selected sources, model ID/prompt version, and policy decision are logged

---

### 🧪 “No Source, No Answer” regression suite (required)

Keep a dedicated suite that protects the core UX + trust mechanic:

- 🚫 missing citations ⇒ denied  
- 🚫 hallucinated citation IDs ⇒ rejected (if you validate citation IDs)  
- 🧾 citation mapping returns metadata (title/license/source id/etc.)  
- 🔁 citation order deterministic when inputs deterministic (avoid flaky tests)

> [!WARNING]
> These tests prevent the worst regression class: “it still answers… but without sources.”

---

### 🧠 Mocked vs real LLM runs

**Default**: run Focus Mode tests with a mocked model client that returns deterministic outputs.

**Optional**: allow real-model runs behind a flag/marker (developer machine or specialized CI job).

Suggested pattern:
- `pytest -m ai` runs mocked model tests  
- `pytest -m ai --run-real-ollama` runs end-to-end (if Ollama service is available)

Example behaviors to assert with a real model:
- citation formatting survives generation
- policy check still denies unsafe outputs
- response latency doesn’t exceed a basic smoke threshold (non-flaky)

> [!TIP]
> If you ever run AI regression tests in CI, prefer a smaller model + CPU mode to keep it stable.

---

## 🛡️ Policy, security, and governance tests

KFM governance is **runtime-enforced** and **CI-enforced**.

### 🧷 Policy checks (OPA/Rego + Conftest)
Validate that:
- policy bundles load successfully
- key rules deny on missing metadata (license, sensitivity labels, provenance pointers)
- policy decisions produce expected HTTP codes (`401/403`) and safe error messages
- policy changes don’t silently weaken gates (tests should fail loudly)

### 🔐 RBAC & sensitivity
Test matrix should cover:
- Public viewer vs contributor vs maintainer vs admin roles (whatever your system defines)
- restricted dataset access blocked by default
- sensitive fields masked/redacted where policy demands it
- GraphQL introspection/admin fields locked down (if applicable)

---

## 📜 Contract tests

Contract tests prevent “works on my machine” API drift.

### Health & readiness 🩺
If implemented, assert:
- `GET /healthz` returns a stable shape
- `GET /readyz` indicates dependency readiness
- `GET /version` includes semantic version/build metadata

### OpenAPI shape 🔧
- `GET /openapi.json` returns valid JSON
- OpenAPI includes core endpoints (datasets, catalog/search, AI if enabled)
- response schemas match what UI expects (especially citations payload)

### Data catalog & datasets 🗃️
Contract + integration tests for:
- metadata includes `license`, `title`, `description` at minimum
- catalog search supports filters (keyword, bbox, time range) where implemented
- dataset data endpoint supports format selection (e.g., GeoJSON) + bbox filtering where implemented

### GraphQL (if enabled) 🧬
- `/graphql` is reachable
- baseline introspection works (or is intentionally restricted)
- core query paths are stable and versioned

---

## 🧰 Troubleshooting

### 🐳 Compose flakiness / startup timing
- Re-run Compose if a dependency wasn’t ready:
  ```bash
  docker compose up -d
  ```
- Check service logs:
  ```bash
  docker compose logs api
  docker compose logs db
  docker compose logs neo4j
  ```

### 🔌 Port conflicts
Common defaults:
- PostGIS: `5432`
- Neo4j: `7474`
- API: `8000`
- Web: `3000`
- Ollama: `11434`

If something is already using a port, stop local services or remap ports in `docker-compose.yml`.

### 🧱 Permissions on mounted volumes
If containers can’t write to mounted paths:
- ensure `data/` (or the configured mount) is writable
- verify UID/GID mapping if on Linux
- on macOS/Windows, double-check Docker file sharing settings

### 🌱 Missing sample data
If the API expects seeded data for integration tests:
- run whatever “seed/init” script your repo provides (if present)
- or run a pipeline import inside the API container

Example pattern (only if your repo provides these scripts):
```bash
docker compose exec api python scripts/init_sample_data.py
# or
docker compose exec api python pipelines/import_some_dataset.py
```

---

## ✅ Contribution checklist

Before opening a PR:

- [ ] New endpoint? Add **contract + behavior** tests  
- [ ] Bug fix? Add a **regression test** (prove it never comes back)  
- [ ] Touch Focus Mode? Add **citation + policy gating** coverage  
- [ ] Touch metadata/pipelines? Ensure **policy checks** still pass  
- [ ] CI green locally: `pytest` + policy checks  
- [ ] Tests explain the **trust guarantee** they protect

---

## 🔗 Useful cross-links

From this directory (`api/tests/`), these are usually relevant:

- `../../src/server/api/README.md` — API surface area & examples  
- `../../docs/architecture/ai/OLLAMA_INTEGRATION.md` — Focus Mode / RAG pipeline behavior  
- `../../docs/architecture/AI_SYSTEM_OVERVIEW.md` — AI system architecture & guardrails  
- `../../docs/architecture/system_overview.md` — system layering & “truth path”  
- `../../policy/` — OPA/Rego policies (governance gates)  
- `../../pipelines/README.md` — ingestion/build steps that affect integration tests  

---

## 🧠 Guiding principle

> If a test can’t explain **what trust guarantee it protects**, it probably belongs in `unit/`… or doesn’t belong at all. 😉