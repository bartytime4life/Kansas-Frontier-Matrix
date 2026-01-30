# 🧪 Unit Tests (KFM) ✅

![scope](https://img.shields.io/badge/scope-unit_tests-blue)
![speed](https://img.shields.io/badge/goal-fast_%26_deterministic-brightgreen)
![governance](https://img.shields.io/badge/governance-fail--closed-important)
![stack](https://img.shields.io/badge/stack-Python_%7C_TypeScript_%7C_Rego-informational)

> **Purpose:** fast, deterministic tests for the **Kansas Frontier Matrix (KFM)** monorepo — focused on correctness, contracts, and governance invariants.  
> **Non-goal:** validating real DBs/services (that’s for integration/e2e).  

---

## 🎯 What counts as a “unit test” here?

A test is **unit** if it is:

- ⚡ **Fast** (ideally milliseconds; the whole suite should feel “cheap”)
- 🧼 **Hermetic** (no network, no real Neo4j/PostGIS, no external API calls)
- 🎲 **Deterministic** (same inputs → same outputs, no clock randomness without freezing)
- 🧩 **Scoped** (tests a single function/module boundary, or a tight “contract”)

> [!IMPORTANT]
> KFM is **fail-closed** by design: if a policy/check is missing or uncertain, the system blocks merges/answers rather than guessing.  
> Unit tests should reinforce this posture (missing license/metadata/policy input should **fail**, not “warn and continue”).

---

## 🗺️ KFM invariants that unit tests should protect

These are the “do not regress” rules that unit tests should keep sharp:

- 🧱 **Pipeline order is sacred:** Raw → Processed → Catalog/PROV → Database → API → UI  
- 🧾 **Provenance-first:** derived artifacts must be traceable; metadata isn’t optional  
- 🔁 **Deterministic ETL:** idempotent runs; stable outputs; predictable logs/lineage  
- 🛡️ **UI never talks directly to DBs:** governance enforcement happens via the API boundary  
- 🔐 **Classification propagation:** outputs must not be less restricted than inputs  

---

## 🗂️ Folder layout (recommended)

This folder is organized by *subsystem* so it maps cleanly to the monorepo:

```text
tests/
└── unit/
    ├── api/          🐍 Backend unit tests (FastAPI domain/services)
    ├── pipelines/    🐍 ETL + transforms (pure functions, schemas, IO adapters mocked)
    ├── web/          🌐 Frontend unit tests (React/TS components + utilities)
    ├── policy/       🛡️ Governance unit tests (OPA/Rego via Conftest, if used)
    ├── fixtures/     🧰 Shared fixtures + tiny sample inputs (golden files allowed)
    └── README.md     📌 You are here
```

> [!TIP]
> Keep **fixtures small** and **representative**. If a dataset is needed, create a minimal “toy” version rather than copying large `data/processed` artifacts.

---

## ▶️ Running unit tests

### 🐍 Python (API + pipelines)

From repo root:

```bash
python -m pytest -q tests/unit
```

Useful options:

```bash
# show slowest tests (helps keep unit tests fast)
python -m pytest tests/unit --durations=10

# run a single file
python -m pytest tests/unit/api/test_something.py -q

# run tests matching a substring
python -m pytest tests/unit -k "provenance" -q
```

### 🌐 Web (React + TypeScript)

From repo root, run the test script configured in `web/`:

```bash
cd web
npm test
```

If your project uses a different package manager:

```bash
cd web
pnpm test   # or: yarn test
```

> [!NOTE]
> Unit tests should not require Docker. If a test needs services, it belongs in `tests/integration/` or `tests/e2e/`.

### 🛡️ Policy checks (OPA/Rego via Conftest) — if enabled

If KFM policy tests are implemented with Conftest:

```bash
conftest test tests/unit/policy -p policy
```

Typical unit-level policy assertions include:
- ❌ block merges when license metadata is missing
- ❌ block missing STAC/DCAT/PROV for new processed data
- ✅ allow only sanctioned file locations / naming conventions
- ✅ deny restricted dataset access for unauthorized roles

---

## ✍️ Writing tests (style guide)

### ✅ Prefer “AAA”
**Arrange → Act → Assert**, with minimal setup.

### ✅ Keep IO at the boundary
- Test pure transforms as pure functions.
- Wrap file/DB/network behavior behind adapters and **mock** them in unit tests.

### ✅ Make failure messages helpful
- Assert with intent and clarity.
- If you add a policy check, include “what to do next” in the failure output.

### ✅ Freeze time & randomness
If the logic depends on time/UUID/randomness:
- inject a clock/seed
- or use a freeze/mocking tool appropriate for the language

---

## 🧰 Fixtures & golden files

### 🧪 Fixtures
- Put shared fixtures in `tests/unit/fixtures/`
- Prefer JSON/GeoJSON/CSV “toy” fixtures over big binary blobs
- Name fixtures by **what they represent**, not their origin (`parcel_minimal.geojson` > `ksdata2.geojson`)

### 🧊 Golden files (snapshot testing)
Allowed for:
- schema outputs
- normalized transforms
- provenance rendering
- policy decision payloads

Rules:
- Keep snapshots **reviewable** (small, stable, pretty-printed)
- If a snapshot changes, the PR must explain **why**

---

## 🚫 Anti-patterns (please don’t)

- 🌍 Hitting live services (Neo4j/PostGIS/External APIs)
- 🧨 Requiring secrets to run unit tests
- 🐌 “Unit tests” that take seconds each
- 🧩 Testing multiple layers at once (pipeline + API + UI) in one test file
- 🧹 Mutating real repo data directories (write to temp dirs instead)

---

## 🧩 Tiny templates

### 🐍 Python (pytest)

```python
def test_normalizes_titlecase():
    # Arrange
    raw = "  dUsT bOwL  "

    # Act
    out = normalize_title(raw)

    # Assert
    assert out == "Dust Bowl"
```

### 🌐 TypeScript

```ts
import { normalizeTitle } from "../src/normalizeTitle";

test("normalizes titlecase", () => {
  expect(normalizeTitle("  dUsT bOwL  ")).toBe("Dust Bowl");
});
```

### 🛡️ Policy (conceptual)

```rego
# tests/unit/policy/deny_missing_license_test.rego
# Assert: datasets without license metadata are denied (fail-closed)
```

---

## 🔗 Related docs (quick jumps)

- 🏛️ Architecture: `../../docs/architecture/`
- 📐 Standards (STAC/DCAT/PROV, schemas): `../../docs/standards/`
- 🧭 Governance policy: `../../policy/`
- 🧰 Tooling scripts: `../../tools/`

---

## ✅ PR checklist for unit tests

- [ ] Tests are deterministic (no flakiness)
- [ ] No network / no real DB calls
- [ ] New logic has coverage at the right layer
- [ ] Failure messages are actionable
- [ ] Any governance-related change includes policy/unit coverage
- [ ] Runtime remains “fast by default” ⚡

---