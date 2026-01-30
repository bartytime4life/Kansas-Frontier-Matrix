# 🧪 Unit Tests — `tests/unit/`

![Unit Tests](https://img.shields.io/badge/tests-unit-blue)
![Fast Feedback](https://img.shields.io/badge/goal-fast%20feedback-brightgreen)
![Deterministic](https://img.shields.io/badge/rule-deterministic-important)

> 🎯 **Purpose:** Unit tests provide **fast, deterministic** verification of **pure logic** across KFM subsystems (ETL/pipelines, graph logic, API/service logic, and shared utilities) — without requiring live databases, networks, or full-stack orchestration.

---

## 🧭 What belongs here (Unit vs. Integration)

### ✅ Put these in `tests/unit/`
- Pure functions / small classes (no I/O)
- Data normalization / parsing / validation logic (CSV/JSON transforms, geometry utils, etc.)
- Schema & contract validation helpers (JSON Schema utilities, contract shims, mappers)
- Policy *helpers* (pure functions that interpret/transform policy inputs/outputs)
- “Business logic” services when dependencies are **mocked** (no DB, no HTTP)

### 🚫 Don’t put these in `tests/unit/`
- Database reads/writes (Postgres/PostGIS, Neo4j) ✅→ move to `tests/integration/`
- API endpoint round-trips (FastAPI/HTTP client calls) ✅→ `tests/integration/`
- Anything requiring Docker Compose to be “up” ✅→ `tests/integration/` or `tests/e2e/`
- Large/real datasets, or anything sensitive/restricted ✅→ use **small synthetic fixtures**

---

## 🧱 KFM testing principles (non-negotiable vibes)

- 🧾 **Contract-first:** tests should pin expected contracts/outputs so refactors don’t silently break downstream stages.
- 🧬 **Provenance-first:** if a function produces an “artifact,” unit tests should verify the **required metadata hooks** (IDs, lineage pointers, etc.) are present (even if fully validated later).
- 🧊 **Deterministic:** no flaky tests. Avoid time dependence; seed randomness; isolate environment state.
- 🧪 **Small + fast:** aim for milliseconds per test. Prefer many small tests over one mega-test.
- 🔒 **Safety & governance aware:** don’t embed secrets; don’t commit real restricted data; avoid leaking sensitive locations/details in fixtures.

---

## 🗂️ Recommended layout inside `tests/unit/`

> This repo is organized as a monorepo; unit tests should mirror the subsystem structure.

```text
tests/
└── unit/
    ├── README.md                 👈 you are here
    ├── python/                   🐍 pytest-style unit tests (pipelines/graph/server)
    │   ├── test_*.py
    │   └── conftest.py           (optional shared fixtures)
    ├── web/                      🌐 (optional) unit tests for UI utilities (Vitest/Jest)
    │   └── *.test.ts(x)
    ├── fixtures/                 🧩 tiny synthetic “golden” inputs/outputs
    │   ├── json/
    │   ├── geojson/
    │   └── csv/
    └── helpers/                  🧰 shared test helpers (builders, factories, fakes)
```

> 💡 If your backend code currently lives in `api/` (older layout) vs `src/server/` (v13+), keep tests aligned with the **actual** code location — but keep them in **one** canonical unit test home: `tests/unit/`.

---

## ▶️ Running unit tests (local)

### 🐍 Python unit tests (recommended for pipelines/graph/server logic)

<details>
<summary><strong>Option A — Run via Docker Compose (most consistent)</strong> 🐳</summary>

```bash
# from repo root
docker-compose exec api pytest -q tests/unit/python
```

✅ Best when dependencies (GDAL, DB clients, geo libs) are container-managed.

</details>

<details>
<summary><strong>Option B — Run in local virtualenv</strong> 🧪</summary>

```bash
# from repo root
python -m pytest -q tests/unit/python
```

✅ Best for quick iteration if your venv matches container deps.

</details>

---

### 🌐 Web unit tests (optional; UI utilities/components)

```bash
cd web
npm test
```

> If your frontend uses a different script (e.g., `npm run test` / `vitest`), prefer the repo’s canonical `package.json` commands.

---

## ✍️ Writing unit tests (conventions)

### 🧷 Naming
- **Python (pytest):** `test_<topic>.py`, functions `test_<behavior>_<scenario>()`
- **TS/JS:** `<thing>.test.ts(x)` or `<thing>.spec.ts(x)` (match the frontend standard)

### 🧠 Test structure
- Prefer **Arrange → Act → Assert** (AAA)
- One behavior per test
- Keep assertions specific (avoid “assert something truthy”)

### 🎭 Mocking rules
- Mock external boundaries:
  - DB clients, filesystem, HTTP, environment variables
- Keep mocks local to the test unless a fixture is clearly reusable
- Avoid mocking the function under test (mock its dependencies instead)

---

## 🧩 Fixtures (tiny + synthetic)

### ✅ Good fixtures
- Small, representative inputs (1–20 rows, 1–5 features)
- “Golden” outputs that are stable and easy to diff
- Fake IDs/coordinates when geography is needed

### 🚫 Bad fixtures
- Real datasets (too big, likely governed, hard to review)
- Anything that could be sensitive (e.g., precise archeological locations)
- Anything that changes frequently (live API responses)

---

## ✅ Definition of Done (DoD) for unit-testable changes

When you add/modify logic that can be unit-tested:

- [ ] Unit tests added/updated in `tests/unit/`
- [ ] Tests are deterministic (no flake)
- [ ] Tests run locally (Python and/or Web, as applicable)
- [ ] No secrets / sensitive data / large fixtures committed
- [ ] CI should stay green ✅

---

## 🧰 Minimal templates

<details>
<summary><strong>🐍 Pytest template</strong></summary>

```python
def test_behavior__scenario__expected_result():
    # Arrange
    input_value = "TODO"
    # Act
    result = some_function(input_value)
    # Assert
    assert result == "EXPECTED"
```

</details>

<details>
<summary><strong>🌐 TS/JS test template</strong></summary>

```ts
import { describe, it, expect } from "vitest"; // or jest

describe("someUtility", () => {
  it("does X when Y", () => {
    // Arrange
    const input = "TODO";
    // Act
    const result = someUtility(input);
    // Assert
    expect(result).toBe("EXPECTED");
  });
});
```

</details>

---

## 🔗 Related docs (recommended reading) 📚

- 📘 `docs/MASTER_GUIDE_v13.md` (repo structure + invariants)
- 🧱 `docs/architecture/` (contracts, boundaries, long-term vision)
- ⚖️ `docs/governance/` (ethics, sovereignty, review gates)
- 🤝 `CONTRIBUTING.md` (how to contribute + review expectations)

---

## 🆘 Troubleshooting (quick hits)

- 🐳 Compose tests fail because services aren’t up?  
  → Unit tests **should not require** live services. Mock those boundaries or move the test to `tests/integration/`.

- 🧊 Flaky tests?  
  → Remove time dependency, seed randomness, avoid ordering assumptions, avoid shared global state.

- 🧱 Contract mismatch after refactor?  
  → Update tests **only if** the contract change is intentional and documented (prefer contract-first updates).

---

