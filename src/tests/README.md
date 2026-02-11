# 🧪 KFM Test Suite (src/tests)

> **Scope:** This directory contains automated tests for the KFM code that lives under `src/`.
>
> In the v13 repo layout, tests are typically organized in a top-level `tests/` directory. If your repository
> uses both `tests/` (root) **and** `src/tests/`, treat `src/tests/` as **module-scoped** tests and keep the
> canonical, cross-cutting suites in `tests/`. (If your repo only has `src/tests/`, this directory is the
> canonical home by default.)

---

## ✅ What these tests protect

KFM is a governed, provenance-first system. Tests are part of the **trust membrane**:

- They enforce clean architecture boundaries (domain ↔ services ↔ adapters ↔ infrastructure).
- They ensure no client/UI path bypasses the governed API boundary.
- They keep contracts stable (schemas, API specs, GraphQL schema, dataset metadata profiles).

---

## 🧭 Test categories

| Category | What it covers | What it must *not* do | Typical tooling |
|---|---|---|---|
| **Unit** | Pure functions, domain entities, validators, small service logic | Network, DB, filesystem (unless explicitly a file-unit test) | `pytest`, `unittest`, `vitest/jest` |
| **Use-case / service** | Workflows + business rules (orchestrations) using **fake/in-memory repos** | Real PostGIS/Neo4j/search | `pytest` + fakes/mocks |
| **Integration** | Repository adapters, migrations, API routes, persistence round-trips | Depend on production secrets; run against shared/stale DBs | `pytest` + Docker Compose |
| **Contract** | OpenAPI / GraphQL schema snapshots, JSON Schema validation, “breaking change” checks | “Silent” contract drift | schema diff tools, `openapi-spec-validator`, `graphql` schema export |
| **E2E (optional)** | UI flows (map layers, story nodes, Focus Mode UX surfaces) | Flaky “sleep-based” tests; reliance on non-deterministic data | Playwright/Cypress |

> [!NOTE]
> If you add a new test type (e.g., load/perf, security fuzzing), add a section here and wire it into CI.

---

## 🗂️ Recommended directory layout

Adjust to match the repo’s actual tech stack.

```text
src/tests/
  README.md
  unit/
    domain/
    services/
    utils/
  integration/
    api/
    repositories/
    db/
  contract/
    openapi/
    graphql/
    schemas/
  fixtures/
    data/
    geojson/
    stac/
    dcat/
    prov/
  helpers/
    factories/
    fakes/
    assertions/
```

### Naming conventions

- **Python:** `test_*.py` (or `*_test.py`)
- **TypeScript/JS:** `*.test.ts(x)` / `*.spec.ts(x)`
- **Golden files:** keep them in `fixtures/` and document update procedures.

---

## ▶️ Running tests locally

### Python (FastAPI backend)

> If your backend is Python/FastAPI, it likely uses `pytest`.

```bash
# from repo root
python -m venv .venv
source .venv/bin/activate

# install deps (choose the repo’s actual dependency method)
pip install -r requirements.txt
pip install -r requirements-dev.txt

pytest -q
```

Common variations:
- `pytest -q src/tests/unit`
- `pytest -q -k "test_name_substring"`
- `pytest -q --maxfail=1`

### Frontend (React / web)

If the repo includes a `web/` or `frontend/` package, run its tests from that package directory:

```bash
npm install
npm test
```

### Integration tests (Docker-backed)

Integration tests should run against **fresh** local services (Postgres/PostGIS, Neo4j, search index) started via Docker Compose.

```bash
docker compose up -d
pytest -q src/tests/integration
docker compose down -v
```

> [!WARNING]
> Don’t point tests at shared, long-lived databases. Prefer disposable containers and deterministic fixtures.

---

## 🔒 Governance & sensitive data rules (FAIR+CARE)

KFM may contain sensitive or culturally restricted information. Tests must **not** leak it.

- ✅ Prefer **synthetic** or **heavily redacted** fixtures.
- ✅ If you must use a real excerpt, store only what’s necessary and document provenance.
- ✅ Add tests that confirm redaction/generalization behavior when data is classified as sensitive.

---

## 🧪 Clean architecture testing rules

### Domain layer
- Tests should import only domain code and standard libs.
- No DB adapters, no API frameworks.

### Service/use-case layer
- Use in-memory repositories or mocks.
- Assert business rules, not storage details.

### Integration layer
- Verify adapters correctly translate domain objects ↔ storage representations.
- Verify repository interfaces (ports) are honored.

### Infrastructure layer
- Keep heavy tests here (DB, graph, search).
- Make failures actionable: clear logs, minimal moving parts.

---

## 📦 Contract testing guidance

Contract tests prevent silent drift across the pipeline and UI.

Recommended contract checks:
- **OpenAPI**: validate spec, and diff spec output in CI.
- **GraphQL**: export schema and diff in CI.
- **Schemas**: validate STAC/DCAT/PROV JSON against project profiles.

> [!TIP]
> Store exported schemas/specs as CI artifacts so reviewers can inspect changes.

---

## ✅ Definition of Done for test changes

- [ ] New behavior has a **unit** or **service** test.
- [ ] Any new adapter/repository behavior has an **integration** test.
- [ ] Any API or schema change has a **contract** test (or an explicit waiver with rationale).
- [ ] Fixtures are minimal, synthetic/redacted, and documented.
- [ ] Tests are deterministic (no sleeps, no reliance on clock/timezones unless explicitly testing time).
- [ ] CI passes locally (`pytest` / `npm test` / etc.).

---

## 🛠️ Troubleshooting

<details>
<summary><strong>Docker services won’t start / ports in use</strong></summary>

- Check for local services already bound to `5432` (Postgres) or `7474/7687` (Neo4j).
- Stop the conflicting service, or change the port mapping in `docker-compose.yml`.
- If containers are unhealthy, view logs:
  - `docker compose logs -f`
</details>

<details>
<summary><strong>Tests are flaky in CI</strong></summary>

- Remove time-based sleeps; wait on readiness probes / health checks.
- Ensure tests don’t share state across runs.
- Prefer `docker compose down -v` for integration suites to clear volumes.
</details>

---

## 🗺️ Test flow at a glance

```mermaid
flowchart TD
  A[Unit: domain + small logic] --> B[Service/use-case tests]
  B --> C[Integration: adapters + API routes]
  C --> D[Contract: OpenAPI/GraphQL/schemas]
  D --> E[E2E: UI flows (optional)]
```