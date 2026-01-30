# 🧪 Integration Tests (KFM)

![scope](https://img.shields.io/badge/scope-integration-blue)
![stack](https://img.shields.io/badge/stack-docker%20compose%20%2B%20pytest-0aa)
![mindset](https://img.shields.io/badge/mindset-provenance--first%20%26%20fail--closed-6a5acd)

Welcome to `tests/integration/` ✅  
These tests validate **KFM’s real service boundaries** (API ↔ databases ↔ pipelines ↔ policy gates) using a **containerized dev stack** — not mocks.

---

## 🧭 What counts as “integration” in KFM?

KFM is designed as a **pipeline → catalog/provenance → database → API → UI** system. Integration tests should **prove the seams hold**:

- ✅ API talks to **real** PostGIS + graph DB containers
- ✅ Data follows the canonical flow (no “UI talks to DB” shortcuts)
- ✅ Governance checks (policy-as-code) are enforced in the same repo reality as CI
- ✅ “Smoke paths” remain stable: `/docs`, GraphQL (if enabled), DB connectivity, seed data pipelines, etc.

> [!IMPORTANT]
> **Integration tests should only touch databases through the API layer** (by design).  
> If a test directly queries DB tables to “verify UI behavior,” you’re probably writing the wrong test.

---

## 📦 Recommended folder layout

```text
tests/
└── integration/
    ├── README.md                👈 you are here
    ├── conftest.py              🧰 pytest fixtures (base_url, clients, retries, cleanup)
    ├── test_health.py           ❤️ /health or minimal “API up” checks
    ├── test_datasets_api.py     🗂️ list/read datasets endpoints
    ├── test_graphql_smoke.py    🧬 optional GraphQL smoke tests
    ├── test_provenance.py       🧾 provenance artifacts exist for seeded data
    ├── test_policy_gates.py     🛡️ policy outcomes observable via API
    └── test_ai_focus_mode.py    🤖 optional (only if AI backend configured)
```

---

## ✅ Prerequisites

### Required
- 🐳 **Docker + Docker Compose** (Compose V2 recommended)
- 🐍 Python environment available **inside the API container** (tests generally run there)

### Optional (but recommended)
- 🛡️ **Conftest** for running policy gates locally (mirrors CI’s policy checks)
- 🤖 AI backend (e.g., Ollama or hosted provider) if you want to run AI integration tests

---

## 🚀 Quickstart: run integration tests locally

> [!TIP]
> Run integration tests from the **repo root** so Compose paths & env files resolve cleanly.

### 1) Start the dev stack

```bash
# Option A (classic)
docker-compose up -d

# Option B (Compose V2)
docker compose up -d
```

### 2) Run tests inside the API container

```bash
# Run all integration tests (recommended marker approach if configured)
docker-compose exec api pytest -m integration

# Or run just this folder
docker-compose exec api pytest tests/integration -q
```

### 3) Tear down when done

```bash
docker-compose down -v
```

---

## 🌱 Seeding sample data (so tests have something real to hit)

Many integration tests are more meaningful with a tiny “known-good” dataset seeded into:

- `data/raw/`
- `data/processed/`
- `data/catalog/`
- `data/provenance/`
- plus DB inserts done via pipelines

Suggested pattern:

```bash
# Example: run a one-off pipeline inside the API container
docker-compose exec api python pipelines/import_rainfall.py
```

> [!NOTE]
> If your repo doesn’t ship `import_rainfall.py`, keep the pattern and swap the script name for whatever sample pipeline exists.

---

## 🔎 Manual smoke checks (fast sanity before you debug tests)

These are “human integration tests” that quickly confirm your stack is wired correctly.

### ✅ API docs
- Open: `http://localhost:8000/docs`

### ✅ GraphQL (if enabled)
- Open: `http://localhost:8000/graphql`
- Example query:
```graphql
query {
  storyNodes {
    id
    title
    yearRange
  }
}
```

### ✅ Web UI (if running)
- Open: `http://localhost:3000`

### ✅ Databases (for debugging only)
- PostGIS: `localhost:5432`
- Graph DB UI (e.g., Neo4j): `http://localhost:7474`

> [!WARNING]
> Use DB UIs for debugging, not as your “test harness.”
> Integration truth should be asserted through the API responses and system outputs.

---

## 🧪 Test conventions (please follow)

### ✅ Naming & structure
- Files: `test_*.py`
- Tests: `test_<behavior>__<expected_outcome>()`
- Pattern: **Arrange → Act → Assert**
- Prefer **black-box** assertions:
  - “calling endpoint returns expected schema”
  - “seeded dataset appears in `/datasets`”
  - “policy prevents restricted access (403/deny response)”

### ✅ Keep tests stable
- Avoid time-based flake: add small retry helpers for service readiness
- Prefer idempotent setup:
  - write tests that can run twice without requiring manual cleanup
- Keep payload sizes tiny; integration tests should be fast enough for CI

---

## 🛡️ Policy checks (OPA/Rego) in the integration workflow

KFM uses “policy-as-code” to prevent non-compliant changes (e.g., missing license metadata, missing provenance artifacts, etc.).  
You should run these checks locally when your change touches:

- `data/processed/`
- `data/catalog/`
- `data/provenance/`
- policy files / AI prompt configs

### Run policy checks locally (if Conftest is installed)

```bash
conftest test .

# Targeted check example:
conftest test data/processed/mydata.csv
```

> [!TIP]
> If CI fails on a policy gate, treat it like a **test failure**: fix the inputs until the rule passes.

---

## 🧯 Troubleshooting

<details>
<summary><strong>⚠️ Port conflicts</strong> (Postgres 5432, Graph 7474, API 8000, Web 3000)</summary>

If you already run Postgres locally (or another service binds these ports), you may see failures.

**Fix options:**
- Stop the conflicting service
- Change host port mappings in `docker-compose.yml`
- Restart the stack after updating `.env` or compose config
</details>

<details>
<summary><strong>🐢 Containers start but API can’t reach DB</strong></summary>

Common causes:
- DB container not ready when API starts
- Missing `depends_on` or health checks
- First boot takes longer on low-resource machines

**Try:**
```bash
docker-compose logs api
docker-compose logs db
docker-compose up -d
```
</details>

<details>
<summary><strong>🗂️ Volume / permissions issues</strong> (especially macOS/Windows)</summary>

If the API writes into `data/` and you see permission errors:
- Ensure repo folders are writable by Docker
- Check volume mounts are correct
- Rebuild with `--build` if dependencies changed
</details>

---

## ➕ Adding a new integration test

1. Pick the seam you’re validating:
   - API ↔ PostGIS
   - API ↔ Graph DB
   - API ↔ pipeline outputs
   - API ↔ policy decision surface
2. Add/extend fixtures in `tests/integration/conftest.py`
3. Keep assertions **API-facing**
4. Ensure:
   - test passes on a clean `docker-compose up -d`
   - test does not depend on your local machine state

> [!TIP]
> If you need “known data,” prefer adding a tiny seed pipeline step (or a sample dataset) rather than hardcoding DB inserts in tests.

---

## 🎯 Definition of Done (DoD) for integration test PRs

- [ ] `docker-compose up -d` works on a fresh checkout
- [ ] Integration tests pass: `pytest tests/integration`
- [ ] Policy checks pass (when relevant): `conftest test .`
- [ ] No direct DB coupling for UI behavior
- [ ] Test failures are actionable (clear asserts + helpful messages)

---

### 🧾 Related docs (recommended)
- `docs/architecture/` 📐
- Root `README.md` 🗺️
- `policy/` 🛡️
- `pipelines/` 🔁