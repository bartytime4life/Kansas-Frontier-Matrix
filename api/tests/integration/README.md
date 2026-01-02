# 🧪 API Integration Tests

![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![pytest](https://img.shields.io/badge/tests-pytest-blue?logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/runtime-Docker-2496ED?logo=docker&logoColor=white)
![Contract-first](https://img.shields.io/badge/philosophy-contract--first-black)

> [!TIP]
> **Quick run (most common):**
> ```bash
> pytest -m integration --integration api/tests/integration
> ```

---

## 🎯 Purpose

These tests verify the **API “boundary behavior” end-to-end** — i.e., the API routes + business logic + persistence layer (and any local dependencies) work together as a coherent system.

In KFM terms, these integration tests are part of the **API stage quality gates**: they help ensure the API stays contract-respecting, governed (redaction/classification), and stable for the UI and any external consumers. ✅

---

## ✅ What belongs in `api/tests/integration/`

Integration tests should answer questions like:

- 🌐 **Do endpoints respond correctly?** (status codes, payload shapes, error handling)
- 🧩 **Do dependencies compose correctly?** (DB + repositories + services + adapters)
- 🔐 **Are auth/roles enforced?** (unauthorized vs forbidden vs allowed)
- 🧼 **Are redaction & classification rules applied?** (no “leaks” of sensitive fields)
- 📜 **Does the API contract remain consistent?** (OpenAPI output still matches expectations)

> [!NOTE]
> We intentionally keep **unit tests** (pure logic) and **frontend E2E tests** (browser flows) out of this folder.

---

## 🗂️ Expected Layout

```text
📁 api/
  📁 tests/
    📁 integration/
      📄 README.md              👈 you are here
      📄 conftest.py            # integration-only fixtures (db, client, auth)
      📄 test_health.py
      📄 test_auth_flows.py
      📄 test_field_timeseries.py
      📄 test_simulation_run.py
```

### Naming conventions ✅
- Files: `test_*.py`
- Tests: `test_*`
- Prefer **Arrange → Act → Assert** blocks in each test for readability.

---

## 🧰 Prerequisites

- 🐍 Python environment for the API service
- 🧪 `pytest` (and any plugins used by the repo)
- 🐳 Docker / Docker Compose (recommended for DB + graph + queues)

> [!TIP]
> If your repo provides a root `.env.example`, copy it first:
> ```bash
> cp .env.example .env
> ```

---

## 🚀 Running the Integration Tests

### Option A — “Local stack” (recommended) 🐳
Use Docker Compose to boot the dependencies (DB/graph/cache/etc.), then run tests locally.

```bash
# from repo root
docker compose up -d --build

# run only API integration tests
pytest -m integration --integration api/tests/integration
```

**Why this mode?**  
It most closely matches real service behavior (connections, migrations, real drivers).

---

### Option B — “In-process TestClient” (FastAPI-style) ⚡
If the integration suite is designed to run in-process (no HTTP sockets), tests may use `fastapi.testclient.TestClient` and dependency overrides.

Minimal pattern:

```python
# example only — adapt imports to your app layout
import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.integration

from api.main import app  # or: from src.server.main import app

@pytest.fixture()
def client():
    return TestClient(app)

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
```

> [!IMPORTANT]
> Even in-process, **still treat it like integration**: real DB connections, real adapters, minimal mocking.

---

## 🏷️ Markers, Skips, and “Only run when asked”

Integration tests are intentionally slower. The recommended pattern is:

- Mark integration tests with `pytest.mark.integration`
- Skip them by default unless explicitly enabled

### Mark a whole module ✅
```python
import pytest
pytestmark = pytest.mark.integration
```

### Gate execution behind a CLI flag (recommended) 🔒
If your project doesn’t already include this, add it to a shared `conftest.py` (repo-wide) or the API test conftest:

```python
# conftest.py (example)
import pytest

def pytest_addoption(parser):
    parser.addoption("--integration", action="store_true", help="run integration tests")

def pytest_runtest_setup(item):
    if "integration" in item.keywords and not item.config.getvalue("integration"):
        pytest.skip("need --integration option to run")
```

Then run:

```bash
pytest -m integration --integration api/tests/integration
```

---

## 🧬 Test Data Rules (Keep it Clean ✅)

### ✅ DO
- Use **synthetic** fixtures (fake users, fake field IDs, fake timeseries)
- Use transactional patterns (rollback after each test) where possible
- Seed only the **minimum** required data per test (fast + readable)

### ❌ DO NOT
- Include real secrets / tokens / API keys
- Commit real PII or sensitive coordinates
- Depend on external third-party APIs (unless recorded/stubbed)

> [!WARNING]
> Security and governance scans may flag secrets or sensitive content. Treat test data as production-adjacent.

---

## 🧭 What to Test (Recommended Coverage Map)

| Area | Examples | Why it matters |
|---|---|---|
| ✅ Health & readiness | `/health`, `/ready`, DB connectivity | smoke signal for CI + deploys |
| 🔐 AuthZ/AuthN | login, token validation, role gates | prevents data leakage |
| 🧾 Contract behavior | response shape, required fields, OpenAPI consistency | contract-first discipline |
| 🗄️ Persistence | CRUD, migrations applied, query correctness | real reliability |
| 🧼 Governance | redaction, classification propagation | “no output less restricted than inputs” |
| 🧵 Background work (if applicable) | enqueue job, poll status | validates async flows |

---

## 🧯 Debugging & Troubleshooting

### Run a single file
```bash
pytest -m integration --integration api/tests/integration/test_field_timeseries.py -vv
```

### Run a single test
```bash
pytest -m integration --integration api/tests/integration/test_field_timeseries.py::test_timeseries_happy_path -vv
```

### Keep logs noisy (helpful in CI)
```bash
pytest -m integration --integration -vv -s --log-cli-level=INFO api/tests/integration
```

### If Docker services are weird 🐳
```bash
docker compose ps
docker compose logs -f
```

---

## 🧱 When Adding a New Integration Test

Use this mini-checklist ✅:

- [ ] Test is marked `integration`
- [ ] Uses **synthetic** data only
- [ ] Cleans up after itself (transaction rollback / fixture teardown)
- [ ] Asserts both **status codes** and **response shape**
- [ ] Includes at least one “negative” case (401/403/404/422)
- [ ] Does **not** depend on the test order
- [ ] If you changed an endpoint contract: update contract artifacts/tests too 📜

---

## 🔗 Reference Docs (Repo)

- 📘 Master Guide / Pipeline invariants: `../../../docs/MASTER_GUIDE_v13.md`
- 🧭 Architecture blueprints: `../../../docs/architecture/`
- 📜 API contract extension template: `../../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- ⚖ Governance & review gates: `../../../docs/governance/`
- 🧾 Standards & writing protocol: `../../../docs/standards/`

> [!NOTE]
> If your API service lives outside the monorepo layout, keep these links updated to match this service’s structure.
