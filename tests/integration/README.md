# 🧪 Integration Tests (KFM)

[![tests](https://img.shields.io/badge/tests-integration-blue)](#-integration-tests-kfm)
[![runner](https://img.shields.io/badge/runner-Docker%20Compose-2496ED?logo=docker&logoColor=white)](#-quickstart)
[![framework](https://img.shields.io/badge/api-FastAPI-009688?logo=fastapi&logoColor=white)](#-api-integration)
[![db](https://img.shields.io/badge/db-PostGIS-336791?logo=postgresql&logoColor=white)](#-service-stack)
[![kg](https://img.shields.io/badge/kg-Neo4j-008CC1?logo=neo4j&logoColor=white)](#-service-stack)
[![policy](https://img.shields.io/badge/policy-OPA-7C3AED?logo=openpolicyagent&logoColor=white)](#-policy--governance-tests)
[![py](https://img.shields.io/badge/python-pytest-0A9EDC?logo=python&logoColor=white)](#-running-the-suite)

> [!IMPORTANT]
> Integration tests verify the full **“truth path”** (a.k.a. canonical pipeline):  
> `Raw ➜ Processed ➜ Catalog/Provenance ➜ Databases/KG ➜ API ➜ UI/AI`  
> If it can’t be **provenanced/cited**, it can’t be considered “done.” ✅

---

## 🧭 What lives in `tests/integration/`?

Integration tests cover **cross-boundary behavior** (real services talking to each other):

- ✅ API ↔ PostGIS (spatial queries, migrations, indexes, geometry formats)
- ✅ API ↔ Neo4j (graph relationships, entity lookups, link integrity)
- ✅ Pipelines ↔ Catalog/Provenance (STAC/DCAT + PROV outputs exist & validate)
- ✅ Policy enforcement (OPA gates: ingestion ✅ / serving ✅ / AI ✅)
- ✅ Focus Mode AI: answers include **citations** + pass policy checks
- ✅ Optional UI “smoke”: API contracts match what the map/timeline UI expects

**Not** the place for:
- Unit tests (pure functions + mocks)
- Load/performance tests (`tests/performance/`, `bench/`)
- Full browser E2E (prefer `tests/e2e/`)

---

## 📁 Suggested layout

```text
tests/
  integration/
    README.md
    docker/
      docker-compose.itest.yml        # test overrides/additional services
    fixtures/
      data/
        raw/
        processed/
        catalog/
        provenance/
      sql/
      cypher/
      prompts/
    api/
      test_datasets.py
      test_features.py
      test_search.py
    pipelines/
      test_ingest_smoke.py
      test_catalog_validation.py
      test_prov_lineage.py
    policies/
      test_opa_serving.py
      test_opa_ingestion.py
      test_opa_ai.py
    focus_mode/
      test_ai_citations_required.py
      test_ai_policy_blocks_sensitive.py
    helpers/
      clients.py
      wait_for.py
      assertions.py
```

> [!TIP]
> Keep fixtures **tiny + deterministic**.  
> If a test needs a state-wide dataset to pass, it’s probably a **benchmark**, not an integration test.

---

## 🧰 Service stack

Most integration tests assume you can run a realistic stack with **Docker Compose**, typically including:

- 🌐 **API** (FastAPI)
- 🐘 **PostgreSQL + PostGIS**
- 🕸️ **Neo4j**
- 🔎 *(Optional)* Search index (Elasticsearch/OpenSearch/vector store)
- 🪣 *(Optional)* Object storage (S3/MinIO) for COGs/tiles/large artifacts
- 🧑‍⚖️ **OPA** (Open Policy Agent) policy gatekeeper
- 🤖 *(Optional)* Ollama (local LLM runtime) for Focus Mode regression tests
- 🗺️ *(Optional)* Web UI (React/MapLibre/Cesium) for smoke checks

### Ports you’ll commonly see 👇
- `8000` API
- `5432` PostGIS
- `7474/7687` Neo4j
- `8181` OPA *(varies)*
- `3000` Web UI *(varies)*

> [!NOTE]
> Port collisions are common (especially `5432`, `7474`, `8000`, `3000`).  
> If you already run services locally, remap host ports in Compose.

---

## 🚀 Quickstart

### 1) Bring up the test stack

From repo root:

```bash
# Option A (recommended): base compose + integration overrides
docker compose -f docker-compose.yml -f tests/integration/docker/docker-compose.itest.yml up -d --build

# Option B: integration stack only (if self-contained)
docker compose -f tests/integration/docker/docker-compose.itest.yml up -d --build
```

### 2) Configure environment (common vars)

Most stacks use a `.env` derived from `.env.example` at repo root. Common variables:

- `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`
- `NEO4J_AUTH`
- `OPA_URL` (or similar)
- `S3_ENDPOINT`, `S3_BUCKET` *(if using MinIO/S3)*

> [!IMPORTANT]
> Integration tests should run against **ephemeral** services (Compose / CI services).  
> Never point tests at production resources.

### 3) Seed minimal test data (if required)

```bash
# Example: run a tiny seed/pipeline inside the API container
docker compose exec api python pipelines/seed_minimal.py
```

### 4) Run the suite

```bash
# Python-based integration tests
pytest -q -m integration

# Or repo wrapper (if provided)
make test-integration
```

---

## 🧪 Running the suite

### Test “lanes” 🛣️

| Lane | Goal | When to run | Typical runtime |
|---|---|---:|---:|
| `smoke` | Stack health + 1 request per critical path | every PR | minutes |
| `integration` | Full cross-service coverage | main / targeted PRs | 5–20 min |
| `policy` | OPA allow/deny checks at boundaries | PRs touching policies | minutes |
| `migration` | DB schema/migrations/seed | PRs touching DB | minutes |
| `ai` | Focus Mode regressions (citations + policy) | nightly / gated | varies |

### Common commands

```bash
# Run only smoke tests
pytest -q -m smoke

# Run API integration tests
pytest -q -m "integration and api"

# Run policy gate tests
pytest -q -m policy

# Run AI tests (requires Ollama service or a deterministic AI mock)
pytest -q -m ai
```

> [!TIP]
> Prefer **markers** over directory-only filtering so you can keep tests organized by capability *and* by execution lane.

---

## 🔌 API integration

Focus areas:
- **Dataset browsing** endpoints return metadata + asset links (STAC/DCAT).
- **Search** endpoints filter by bbox/time range and return stable schemas.
- **Feature/entity** endpoints return consistent IDs and geometry formats.
- **Gatekeeping**: UI should only access data through the API (no bypass paths).

### Contract expectations ✅
Any API response representing a dataset should include (or link to):
- `id`
- `license` / `accessLevel` *(or equivalent)*
- provenance pointer/reference
- links to assets / tiles / documents

> [!TIP]
> Validate response schemas in tests (Pydantic models or JSONSchema) to prevent silent breaking changes.

---

## 🏭 Pipelines + Catalog + Provenance tests

These tests validate the canonical pipeline:

1. Drop a tiny raw input into `data/raw/` (or test fixtures)
2. Run a pipeline step
3. Assert outputs exist in:
   - `data/processed/`
   - `data/catalog/` (STAC/DCAT)
   - `data/provenance/` (PROV logs)
4. Load into PostGIS/Neo4j (if applicable)
5. Confirm API now serves it with correct metadata + lineage

### Suggested checks ✅
- STAC items are valid JSON and required fields exist
- DCAT metadata includes license + source attribution
- PROV records reference inputs + processing steps
- Pipeline is **idempotent** (running twice doesn’t double-insert)

---

## 🧑‍⚖️ Policy & governance tests (OPA)

Policy tests verify that rules are enforced at boundaries:

- Serving layer denies restricted datasets to unauthorized roles
- AI layer refuses/redacts restricted/sensitive content
- Ingestion blocks datasets lacking required license metadata

### Patterns to test
- ✅ Allowed: public dataset is listed and queryable
- ❌ Blocked: restricted dataset does not appear in listings
- ❌ Blocked: direct asset access is gated/denied (or requires auth)
- ✅ Auditable: denials produce structured logs (if implemented)

> [!IMPORTANT]
> Policies are code. Treat them like code: versioned, reviewed, and tested.

---

## 🤖 Focus Mode AI regression tests

Goal: prevent “AI drift” from silently breaking trust guarantees.

What we test:
- Answers include **at least one citation** for factual claims
- “How do you know?” style queries return explainable sources
- Policy engine blocks disallowed outputs (sensitive sites, PII, restricted datasets)
- Optional: tool-usage traces recorded to provenance logs

### Two modes
1. **Fast mode (CI-friendly)**  
   - Use a small local model or deterministic mock
2. **Full mode (nightly)**  
   - Run Ollama + target model
   - Execute curated prompt set (“golden prompts”)

> [!TIP]
> Store *expectations*, not full answers.  
> Prefer checking: citations present ✅, key entities present ✅, disallowed content absent ✅.

---

## 🧼 Reset & cleanup

```bash
# Stop stack
docker compose -f docker-compose.yml -f tests/integration/docker/docker-compose.itest.yml down

# Nuke volumes (⚠️ wipes DB and local test data)
docker compose -f docker-compose.yml -f tests/integration/docker/docker-compose.itest.yml down -v
```

---

## 🧯 Troubleshooting

### Common issues
- **DB not ready**: add `depends_on` + healthchecks, or retry test setup
- **Port conflicts**: remap host ports in compose (5432/7474/8000/3000)
- **Volume permissions**: ensure container user can write to mounted `data/`
- **Stale containers**: rebuild after dependency changes (`--build`)

### Debug helpers
```bash
# Follow logs
docker compose logs -f api
docker compose logs -f db
docker compose logs -f neo4j
docker compose logs -f opa

# Exec into a container
docker compose exec api bash
docker compose exec db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"
```

---

## 🤝 Writing a new integration test

1. Pick the **boundary** you’re testing (API↔DB, pipeline↔catalog, policy gate, AI)
2. Add/reuse a **tiny fixture**
3. Assert on:
   - correctness
   - metadata/provenance completeness
   - policy compliance (allow/deny)
4. Ensure the test is:
   - deterministic
   - isolated (no hidden dependency on other tests)
   - CI-friendly

### Naming convention
- `test_<capability>__<expectation>.py`  
  Example: `test_datasets__requires_license.py`

---

## 🧬 CI notes

Recommended CI strategy:
- PRs: run `smoke` + any impacted lanes (api/policies/pipelines)
- Main: run full `integration`
- Nightly: run `ai` full mode

Example workflow idea (pseudo):

```yaml
# .github/workflows/integration-tests.yml
# (illustrative — adapt to your repo)
jobs:
  integration:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: docker compose -f docker-compose.yml -f tests/integration/docker/docker-compose.itest.yml up -d --build
      - run: pytest -q -m integration
      - if: always()
        run: docker compose -f docker-compose.yml -f tests/integration/docker/docker-compose.itest.yml down -v
```

---

## 📚 Related docs in this repo

- `docs/architecture/` (system overview + truth path)
- `pipelines/` (ETL conventions + validation rules)
- `policies/` or `opa/` (policy bundles + Rego)
- `src/server/api/` (API contract + endpoints)