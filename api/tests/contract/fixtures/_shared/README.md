# 🧩 Shared Contract Test Fixtures (`_shared/`)

![Contract Tests](https://img.shields.io/badge/tests-contract-blue)
![Fixtures](https://img.shields.io/badge/fixtures-shared-informational)
![Deterministic](https://img.shields.io/badge/goal-deterministic%20runs-success)

> [!NOTE]
> This folder is for **cross-endpoint, reusable fixture building blocks** used by the contract test suite.  
> If a fixture is **only** relevant to one endpoint or one scenario, it should live beside that endpoint’s fixtures (not here).

---

## 🎯 What this folder is for

Contract tests are “**do-not-break**” checks that assert our API behavior stays consistent for **known inputs/outputs**.  
The `_shared/` folder exists to keep those tests **DRY**, **stable**, and **easy to update** without copy/paste drift.

Use `_shared/` for things like:

- ✅ Common IDs (stable UUIDs), timestamps, paging defaults
- ✅ Reusable request fragments (filters, geo params, headers)
- ✅ Reusable response fragments (standard error payloads, pagination envelope)
- ✅ Shared “golden” primitives (minimal objects used across many endpoints)

Avoid putting these here:

- ❌ Endpoint-specific payloads (put them in the endpoint’s fixture folder)
- ❌ Large datasets (fixtures should be small + fast)
- ❌ Anything sensitive (PII, secrets, real protected coordinates)

---

## 🧱 How shared fixtures typically get used

> [!TIP]
> Think “**Lego bricks**”: `_shared/` holds the bricks; each endpoint fixture assembles the final structure.

Common patterns:
- **Build inputs**: assemble request payloads from shared fragments
- **Assert outputs**: compare API responses to a “golden” JSON file (with normalization for dynamic fields)
- **Schema-first**: fixtures should reflect the current contract (OpenAPI/GraphQL) and backwards-compat expectations

<details>
  <summary><strong>Example: Load a shared JSON fixture (Python-ish pseudo)</strong></summary>

```py
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SHARED = HERE / "_shared"

def load_shared(name: str) -> dict:
    return json.loads((SHARED / name).read_text(encoding="utf-8"))

BASE_HEADERS = load_shared("headers.json")
ERROR_401 = load_shared("errors/401.json")
```
</details>

<details>
  <summary><strong>Example: Compose a request using shared fragments</strong></summary>

```py
req = {
  **load_shared("defaults/paging.json"),
  "filters": {
    **load_shared("filters/common.json"),
    "var": "ndvi"
  }
}
```
</details>

---

## 📁 Suggested layout (guideline, not a law)

If you’re adding new shared fixtures, prefer grouping by purpose:

```text
📁 api/tests/contract/fixtures/
└─ 📁 _shared/
   ├─ 📝 README.md              👈 you are here
   ├─ 📁 defaults/              (paging, common query params)
   ├─ 📁 headers/               (content-type, accept, test-only headers)
   ├─ 📁 ids/                   (stable UUIDs / test identifiers)
   ├─ 📁 time/                  (fixed timestamps / date ranges)
   ├─ 📁 geo/                   (safe demo geometries / bboxes)
   ├─ 📁 errors/                (standard error responses)
   └─ 📁 envelopes/             (pagination/list response shells)
```

> [!IMPORTANT]
> **Stability beats cleverness.** Favor explicit JSON files over magic generation unless generation is deterministic and well-documented.

---

## 🧼 Fixture rules (please don’t skip)

### 1) 🧊 Deterministic by default
Contract tests must be repeatable. Fixtures should not change based on:
- current time
- random UUIDs
- environment-specific paths
- nondeterministic ordering (e.g., dict key order, unsorted lists)

**If** the API naturally returns dynamic fields (e.g., `request_id`, `generated_at`), tests should:
- normalize/ignore those fields, or
- assert them using patterns (e.g., “is a UUID”), not exact equality

---

### 2) 🔐 Safe & non-sensitive
Fixtures are treated like production-adjacent artifacts.

- Use **synthetic** names/emails/tokens
- Use **fake** API keys (or omit entirely)
- Use **non-sensitive** coordinates and coarse geometries  
- Never include anything that could trigger governance or privacy concerns

> [!CAUTION]
> If you wouldn’t paste the data into a public issue, it does not belong in fixtures.

---

### 3) 🧩 Small & composable
Shared fixtures should be:
- minimal
- reusable
- easy to read in diffs

Prefer:
- `filters/common.json` over `massive_everything_payload.json`
- “one concept per file” over mega-blobs

---

## 🔄 Updating fixtures safely

When you change anything in `_shared/`, assume it may affect **many** contract tests.

Recommended workflow:

1. 🔍 Identify which tests import the shared fixture
2. 🧪 Run the contract test suite locally (or via the project test runner)
3. 🧾 If golden outputs change, update them deliberately (don’t “accept all” blindly)
4. 🧠 Ask: is this change **backwards-compatible**?
   - If yes → update fixtures/tests accordingly
   - If no → consider introducing a versioned variant of the fixture and keeping the old behavior intact

---

## 🏷️ Naming conventions

A few conventions that keep the repo tidy:

- Use `snake_case.json` (or `snake_case.yaml`) ✅
- Prefer semantic names over “test1/test2” ✅  
  - `paging_default.json` ✅  
  - `bbox_kansas_demo.json` ✅  
  - `error_403_forbidden.json` ✅
- If you need variants, suffix them:
  - `filters_basic.json`
  - `filters_basic__missing_var.json`

> [!TIP]
> If you can’t name it clearly, it might not be a shared fixture yet.

---

## 🧯 Troubleshooting

**“Everything failed after I changed one shared file.”**  
Yep — shared fixtures are high blast-radius. Restore backwards compatibility or introduce a new versioned fixture.

**“The response doesn’t match because of ordering.”**  
Normalize sorting in the test harness (preferred) or store fixtures in a deterministic sorted order.

**“CI fails on sensitive data/secret scanning.”**  
Remove the value immediately and replace it with synthetic data. Assume fixtures are scanned like production.

---

## 👥 Ownership & expectations

- Treat `_shared/` as **core infrastructure** for contract tests.
- Changes should be intentional, reviewed, and aligned with the API contract.
- When in doubt, add a new fixture rather than mutating an existing one that’s widely reused.

---

✅ If you’re reading this because a contract test failed: start by checking whether a shared fixture changed, and whether the API contract (OpenAPI/GraphQL) still matches the intended behavior.

