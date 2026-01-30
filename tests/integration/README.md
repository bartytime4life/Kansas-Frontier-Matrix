# 🧪🔗 Integration Tests (KFM)

![Tests](https://img.shields.io/badge/tests-integration-blue)
![Docker](https://img.shields.io/badge/docker-compose%20stack-required-informational)
![Policy](https://img.shields.io/badge/policy-Conftest%20%2B%20OPA-6e40c9)

Integration tests validate **Kansas Frontier Matrix (KFM)** as a *working system* — not just isolated functions.  
Think: **Pipelines → Databases → API → UI**, plus policy/metadata guardrails. ✅

---

## 🧭 What lives in `tests/integration/`

This folder is for tests that require **real services** (or realistic service doubles) and verify **cross-component contracts**, such as:

- 🗺️ PostGIS connectivity + geospatial queries behave as expected
- 🧠 Neo4j connectivity + graph queries return expected structures
- 🌐 API endpoints correctly round-trip to storage layers
- 📦 Pipeline outputs are usable by downstream layers (no “shortcutting”)
- 🛡️ Governance/policy checks catch invalid contributions early (CI parity)

> [!NOTE]
> If you can test it without PostGIS/Neo4j/containers, it probably belongs in `tests/unit/` instead.

---

## ⚡ Quick Start

### 1) Bring up the dev stack (Docker Compose)
From the repo root:

```bash
docker-compose up --build
```

> [!TIP]
> Prefer the newer syntax? This is equivalent on most machines:
> ```bash
> docker compose up --build
> ```

### 2) Run integration tests (recommended: inside the API container)

```bash
docker-compose exec api pytest -q tests/integration
```

Common variants:

```bash
# run only tests marked "integration" (if markers are used)
docker-compose exec api pytest -q -m integration

# run a single file
docker-compose exec api pytest -q tests/integration/test_api_smoke.py

# run a single test by keyword
docker-compose exec api pytest -q -k "neo4j" tests/integration
```

---

## 🧱 What these tests *should* verify

KFM has a strong “no-shortcuts” architecture rule: **data should flow through the canonical pipeline**.

✅ Good integration tests confirm:

- The system **boots** cleanly (containers, ports, readiness)
- The API is reachable (Swagger / docs page loads)
- API calls succeed **only when** the dependency layers are healthy
- Sample dataset ingestion produces:
  - processed artifacts
  - metadata/provenance where required
  - DB records retrievable via API queries
- Policy checks block non-compliant data/metadata contributions

❌ Avoid tests that:

- Write directly into UI state
- Bypass metadata/provenance creation “just to make the test pass”
- Depend on external network calls (unless explicitly marked + isolated)

---

## 🔌 Services & default ports (dev ergonomics)

You’ll commonly interact with these during integration testing:

- 🌐 **API** (Swagger docs): `http://localhost:8000/docs`
- 🧩 **GraphQL** (if enabled): `http://localhost:8000/graphql`
- 🗄️ **PostGIS**: `localhost:5432`
- 🧠 **Neo4j Browser UI**: `http://localhost:7474`  
  (Bolt is often `7687`)

> [!WARNING]
> Port conflicts are the #1 cause of “it works on my machine” test flakiness.  
> If you already have local Postgres on `5432`, stop it or remap ports in compose/.env.

---

## 🧫 Test data & seeding strategy

Integration tests must be **repeatable** and **small**:

- Use **tiny fixtures** (think “1–50 records”), not full datasets.
- Keep fixtures in version control when possible.
- Never commit sensitive / restricted data.

### Suggested fixture approach (recommended pattern)

1. ✅ Keep a minimal dataset in something like:
   - `data/raw/sample/…`
2. ✅ Run a pipeline that creates:
   - `data/processed/…`
   - catalog/prov artifacts (as required)
   - DB inserts (PostGIS / Neo4j)
3. ✅ Validate results through the API (preferred) or DB queries (acceptable)

### Seeding examples (check your repo for exact scripts)

```bash
# example: an init script (if present)
docker-compose exec api python scripts/init_sample_data.py

# example: a pipeline import (if present)
docker-compose exec api python pipelines/import_rainfall.py
```

> [!TIP]
> Keep the stack running in one terminal, and run pipelines/tests from another. It speeds up iteration.

---

## 🧰 Policy checks vs integration tests (don’t confuse “conftest”)

KFM may use **Open Policy Agent (OPA)** + **Conftest** in CI to enforce rules like:
- dataset license fields exist
- required provenance files exist
- restricted outputs aren’t exposed

Run local policy checks (if Conftest is installed):

```bash
conftest test .
```

Or target a specific path:

```bash
conftest test data/processed/mydata.csv
```

> [!IMPORTANT]
> This is *not* `pytest`’s `conftest.py`.  
> This is the **Conftest** CLI used for policy-as-code.

---

## 🧩 Writing new integration tests

### ✅ Golden rules
- 🧊 **Idempotent**: can run twice without manual cleanup
- ⏱️ **Fast-ish**: prefer < 60s per test file; use markers for slow tests
- 🎯 **Contract-focused**: validate boundaries, not implementation details
- 🧹 **Self-cleaning**: isolate data (schema/namespace/prefix), cleanup after

### Suggested structure (flexible)
```text
tests/
  integration/
    README.md
    api/
    db/
    pipelines/
    policy/
    fixtures/
```

### Minimal test template (pytest)
```python
def test_stack_is_healthy():
    # Example shape only — use the real endpoints your API exposes.
    # Prefer reading API base URL from env to keep local/CI consistent.
    assert True
```

> [!TIP]
> Prefer “API-first” assertions:
> - ✅ call the API and verify payload
> - ✅ only drop to DB-level checks when needed to verify invariants

---

## 🐛 Troubleshooting (common causes)

<details>
<summary><strong>API container can’t connect to DB</strong></summary>

- Check logs:
  ```bash
  docker-compose logs api
  ```
- Sometimes DB needs a moment; restart the stack:
  ```bash
  docker-compose down
  docker-compose up
  ```
- Ensure `depends_on` is correctly configured in compose (if you maintain it).

</details>

<details>
<summary><strong>Port conflicts (5432 / 7474 / 8000 / 3000)</strong></summary>

- Stop the conflicting local service, **or**
- Remap ports in `docker-compose.yml` / `.env`.

</details>

<details>
<summary><strong>Volume / permissions issues writing to <code>data/</code></strong></summary>

- Ensure the `data/` directory is writable by the container user.
- On Windows/macOS, path + mount quirks can cause “files don’t update”.

</details>

<details>
<summary><strong>Web UI doesn’t hot reload</strong></summary>

- Verify volume mounts include `web/src`.
- If dependencies changed:
  ```bash
  docker-compose up --build
  ```

</details>

---

## ✅ CI expectations (how to avoid red builds)

Before pushing / opening a PR, aim to pass locally:

- 🧪 Backend tests (pytest)
- 🎨 Linters/formatters (Python + JS)
- 🛡️ Policy checks (Conftest), if your change touches governed assets

> [!NOTE]
> CI commonly runs a combination of tests + lint + policy checks, and fails “closed” if requirements aren’t met.

---

## 📎 Related docs

- 📚 `docs/architecture/…` (system overview, service boundaries)
- 🧰 `CONTRIBUTING.md` (local dev + CI workflow expectations)
- 🧪 `tests/README.md` (overall testing strategy, if present)

---

## 🗺️ “Done right” checklist for new integration tests

- [ ] Uses the Compose stack (or an equivalent test harness)
- [ ] Seeds only minimal data needed
- [ ] Verifies behavior through stable contracts (API, schemas, policies)
- [ ] Leaves the environment clean for the next test
- [ ] Has a clear failure message (debuggable in CI logs)

✨ If you keep integration tests boring and deterministic, KFM stays powerful and trustworthy.

