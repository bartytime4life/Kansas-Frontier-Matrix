# 🧪 API Unit Tests (KFM)  

![unit-tests](https://img.shields.io/badge/tests-unit%20tests-blue)
![runner](https://img.shields.io/badge/runner-pytest-brightgreen)
![goal](https://img.shields.io/badge/goal-fast%20%26%20deterministic-ff69b4)

Welcome to the **unit-test** suite for the API layer. These tests exist to keep the API **trustable**, **refactor-friendly**, and **safe-to-change** without regressions. ✅

> [!TIP]
> If a test needs a real DB / network / external service, it probably belongs in **integration** tests, not here.

---

## 📌 What goes in `tests/unit`?

✅ **Good fits (unit scope)**  
- Pure functions (parsers, validators, formatters, helpers)  
- Domain/service logic (business rules) with **mocked** adapters  
- API route handlers **only when** dependencies are overridden/mocked  
- Auth/role checks when the auth dependency is **stubbed**  
- Error handling, edge cases, and redaction rules (as pure logic)

🚫 **Not a good fit (move to integration/e2e)**  
- Real database queries (Postgres/Neo4j/etc.)  
- Real calls to external APIs (GEE, remote sensing feeds, third-party services)  
- File-system heavy workflows (ETL runs, large dataset IO)  
- Full “system behavior” across multiple services

---

## 🚀 Running unit tests locally

> [!NOTE]
> Commands below assume **pytest**. If your environment uses `poetry`, `pipenv`, or `uv`, prefix accordingly (e.g., `poetry run pytest ...`).

### ✅ Run all unit tests
```bash
pytest api/tests/unit
```

### ⚡ Fast/quiet mode
```bash
pytest api/tests/unit -q
```

### 🎯 Run a single file
```bash
pytest api/tests/unit/test_example.py -vv
```

### 🔎 Run by keyword
```bash
pytest api/tests/unit -k "auth or redaction"
```

### 🧱 Stop on first failure
```bash
pytest api/tests/unit -x
```

### 🧾 Collect tests without running (sanity check)
```bash
pytest api/tests/unit --collect-only
```

> [!TIP]
> When debugging a tricky failure, `-vv` + `-s` (prints) is your friend:
> ```bash
> pytest api/tests/unit -vv -s
> ```

---

## 📁 Suggested layout & naming

Keep tests easy to discover and map to the code they protect.

```text
📦 api/
└── 🧪 tests/
    ├── 🧩 unit/
    │   ├── 📄 README.md  👈 you are here
    │   ├── 📁 routes/            # thin route tests (deps overridden)
    │   ├── 📁 services/          # domain/service layer tests
    │   ├── 📁 utils/             # helpers, parsing, validation
    │   ├── 📁 security/          # authZ/authN logic, redaction rules
    │   └── 📄 test_<thing>.py    # pytest discovery friendly
    └── 🔗 integration/           # real DB / containers / real HTTP (not unit)
```

### 🧷 Naming rules
- Test files: `test_<feature>.py`
- Test functions: `test_<behavior>_<expected_result>()`
- Prefer descriptive names over short ones (future-you will thank you 😄)

---

## 🧰 Test conventions (the “KFM way”)

### 1) Keep tests **deterministic**
- Avoid real time (`datetime.now()`), randomness, or ordering assumptions
- If needed, inject time/random providers or freeze them in tests

### 2) Arrange → Act → Assert (AAA)
A clean structure makes failures obvious:
```python
def test_something_happens_when_condition_is_met():
    # Arrange
    input_data = ...
    service = ...

    # Act
    result = service.do_the_thing(input_data)

    # Assert
    assert result == ...
```

### 3) Mock at the **boundary**
Mock external systems *where they enter your code* (DB client, HTTP client, queue publisher), not deep inside your domain rules.

✅ Good: mock `GeoRepository.get_timeseries()`  
🚫 Not great: mock `internal_helper_that_you_own()` (usually means the test is too coupled)

---

## 🧪 FastAPI-style testing (dependency overrides)

If the API uses dependency injection (common in FastAPI), route tests can stay “unit-level” by overriding dependencies with fakes.

<details>
<summary><strong>Example: route test with mocked dependency (click to expand) 🧩</strong></summary>

```python
from fastapi.testclient import TestClient

# from api.main import app
# from api.dependencies import get_current_user, get_repo

def test_endpoint_returns_403_for_missing_role(test_app, fake_user_no_access):
    # Arrange
    app = test_app
    client = TestClient(app)

    # Act
    res = client.get("/api/field/10/timeseries?var=ndvi")

    # Assert
    assert res.status_code == 403
```

</details>

> [!TIP]
> Keep route tests **thin**. Most coverage should come from testing the **service/use-case layer** directly.

---

## 🔒 Security & governance checks (unit-testable pieces)

Even without running the full system, unit tests should protect:
- **AuthN** behavior (401 when unauthenticated)  
- **AuthZ** behavior (403 when authenticated but unauthorized)  
- **Redaction/classification** logic (sensitive fields removed or generalized)  
- “No secrets in code” patterns (tests should *never* require real tokens)

> [!IMPORTANT]
> Unit tests must not rely on developer machine secrets (API keys, private datasets, etc.).  
> If you need configuration, use **test defaults**, **fakes**, or **fixtures**.

---

## 📜 Contract-first alignment (don’t drift)

KFM treats API contracts (OpenAPI/JSON Schemas/etc.) as **first-class artifacts**.  
When you:
- add an endpoint ✅  
- change request/response shapes ✅  
- modify validation rules ✅  

…you should update:
- unit tests here (**behavior**) 🧪  
- contract tests elsewhere (**schema compliance**) 📄  

> [!NOTE]
> Contract tests are usually enforced in CI and should block merges if the API behavior no longer matches the contract.

---

## 🧯 Troubleshooting

### “Tests fail only on CI”
- Check for reliance on filesystem paths, OS-specific behavior, or ordering
- Ensure no implicit dependency on local `.env` values

### “ImportError / module not found”
- Confirm you’re running from the correct working directory  
- Use `python -m pytest ...` if imports behave differently in your setup

### “Flaky tests”
- Remove real time, randomness, and shared mutable state  
- Avoid reusing global singletons between tests unless properly reset

---

## ✅ PR checklist (unit-test edition)

- [ ] New/changed logic has **unit tests** (happy + sad paths)  
- [ ] Tests are deterministic (no real time/network)  
- [ ] External boundaries are mocked/stubbed  
- [ ] Security behavior is covered (401/403/redaction where relevant) 🔐  
- [ ] Naming is clear and consistent (`test_*.py`, `test_*`)  
- [ ] Tests run fast locally (`pytest api/tests/unit`) ⚡

---

## 🔗 Handy links (repo)

- 📘 Master Guide: `../../../docs/MASTER_GUIDE_v13.md`
- 🧾 API Contract template: `../../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- 🧩 API boundary (canonical in v13): `../../../src/server/`
