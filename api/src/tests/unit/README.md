# 🧪 API Unit Tests ( `api/src/tests/unit` )

![tests](https://img.shields.io/badge/tests-unit-2ea44f)
![scope](https://img.shields.io/badge/scope-api-blue)
![goal](https://img.shields.io/badge/goal-fast%20%26%20deterministic-important)
![style](https://img.shields.io/badge/style-clean--architecture-6f42c1)

> ✅ **Mission:** Keep KFM’s backend logic trustworthy by running **fast, deterministic, isolated** unit tests that catch regressions before they reach integration/production.

---

## 📌 What belongs in **unit** tests?

Unit tests validate **small, pure(ish) units of behavior** (functions/classes/use-cases) in isolation — no real network, no real DB, no real filesystem.

### ✅ Good candidates (examples)
- 🔁 **Pure data transforms** (e.g., converting raw sensor data → standardized units)
- 🧠 **Use-cases / service methods** (business logic)
- 🧩 **Domain model behavior** (dataclasses / entity invariants)
- 🧰 **Utils** (date parsing, config parsing, geometry helpers)
- 🧪 **Validation & mapping logic** (DTO ↔ domain ↔ persistence)

### 🚫 Not unit tests (put elsewhere)
- 🌐 Hitting HTTP endpoints (that’s integration)
- 🗄️ Real Postgres/MySQL queries (integration)
- ☁️ External APIs (integration / contract tests)
- 🧭 End-to-end flows (e2e)

---

## 🗂️ Folder map (suggested)

```text
📁 api/
└── 📁 src/
    ├── 📁 (app code...)
    └── 📁 tests/
        ├── 📁 unit/
        │   ├── 📄 README.md          👈 you are here
        │   ├── 📁 domain/            # entities + value objects
        │   ├── 📁 services/          # use-cases / business logic
        │   ├── 📁 utils/             # pure helpers + transforms
        │   └── 📁 adapters/          # interface-level logic (mocked deps)
        └── 📁 integration/           # API endpoints + DB + external systems
```

> 💡 **Rule of thumb:**  
> If the test needs Docker, a database, a server, credentials, or the internet… it’s **not** a unit test.

---

## 🏃 Running the unit tests locally

> Pick the command that matches the backend implementation in this repo (Python vs Node).  
> If you’re unsure, check the `api/` root for `pyproject.toml/requirements*.txt` (Python) or `package.json` (Node).

### 🐍 Python (pytest)
```bash
cd api

# run unit tests
python -m pytest -q src/tests/unit

# run a single file
python -m pytest -q src/tests/unit/path/to/test_something.py

# run tests matching a keyword
python -m pytest -q src/tests/unit -k "sensor" -vv
```

### 🟦 Node / TypeScript (Jest/Vitest/Mocha)
```bash
cd api

# run unit tests (project-defined runner)
npm test -- src/tests/unit

# common alternatives (only if your repo uses them)
npx vitest run src/tests/unit
npx jest src/tests/unit
```

---

## 🧠 Unit test principles we enforce

### ⚡ Fast
Tests should run constantly (locally + CI) without becoming a “tax.”  
If the suite starts dragging, split out slow checks into integration/e2e.

### 🔁 Idempotent
Tests should not depend on run order and should not leave the world “dirty” afterward.

### 🧊 Isolated & deterministic
No reliance on:
- current time
- environment-specific paths
- external services
- shared global state
- random values without seeding

> ✅ **If it flakes, it fails** (even if it “usually passes”).

---

## 🧩 Clean Architecture alignment (why unit tests matter)

KFM’s architecture is layered: inner logic should be testable without outer infrastructure.

- **Talk inwards with simple structures** (domain-friendly objects)
- **Talk outwards through interfaces** (repositories/clients injected into use-cases)

That makes unit tests easy:
- Replace DB repositories with **in-memory fakes**
- Replace HTTP clients with **stubs**
- Replace time/random with **controlled providers**

---

## 🎭 Mocking policy (practical + strict)

### ✅ Prefer fakes/stubs over heavy mocks
- **Fake**: simple in-memory implementation (best for repositories)
- **Stub**: returns predefined values
- **Mock**: asserts calls/arguments (use sparingly)

### 🪝 Mocks are “hooks”
Mocks can become tightly coupled to implementation details.  
If you find yourself building lots of mocks, consider refactoring so dependencies are injected and testable via interfaces.

---

## 🧪 Naming & structure conventions

### ✅ File naming
Use the framework’s discovery rules:

- **Python:** `test_*.py`
- **TS/JS:** `*.spec.ts` / `*.test.ts`

### ✅ Test naming
Prefer intent-focused names:
- `test_<behavior>__<expected_outcome>`
- `given_<state>__when_<action>__then_<result>`

### ✅ Pattern
Use **Arrange → Act → Assert** (AAA):
- Arrange inputs & fakes
- Act once
- Assert outcomes (and only what matters)

---

## 🧰 Fixtures & test data

### 🎯 Keep fixtures tiny
- Minimal objects, minimal data
- Prefer factory helpers (`make_*`) for readability
- Keep test geometry/time-series/sensor datasets **small** and **purpose-built**

### 🧼 Cleanup always
If you create temp files/dirs, ensure teardown happens every run.

---

## 🧩 Templates (copy/paste)

<details>
<summary><strong>🐍 Python unit test template (pytest)</strong></summary>

```python
# src/tests/unit/services/test_unit_conversion.py

def test_convert_raw_sensor_units__converts_to_standard_units():
    # Arrange
    raw = {"temperature_f": 77.0}

    # Act
    result = convert_raw_sensor_units(raw)

    # Assert
    assert result["temperature_c"] == 25.0
```
</details>

<details>
<summary><strong>🟦 TypeScript unit test template (Jest/Vitest-style)</strong></summary>

```ts
// src/tests/unit/services/unitConversion.spec.ts

import { convertRawSensorUnits } from "../../../services/unitConversion";

test("convertRawSensorUnits converts to standard units", () => {
  // Arrange
  const raw = { temperature_f: 77.0 };

  // Act
  const result = convertRawSensorUnits(raw);

  // Assert
  expect(result.temperature_c).toBe(25.0);
});
```
</details>

---

## 🧭 What goes where (quick table)

| Concern | Test Type ✅ | Where 📁 |
|---|---:|---|
| pure function / transform | Unit | `src/tests/unit/` |
| use-case logic with fake repo | Unit | `src/tests/unit/` |
| repository hitting DB | Integration | `src/tests/integration/` |
| API endpoint behavior | Integration | `src/tests/integration/` |
| frontend components | UI unit | `web/...` (frontend test dirs) |
| login + map layer + report flow | E2E | Cypress/Selenium dirs |

---

## ✅ PR checklist (unit tests)

- [ ] New behavior has a unit test (or explicitly justified why not)
- [ ] Tests are **fast** (<1s per file is a good smell-check)
- [ ] No real DB/network/filesystem dependencies
- [ ] No reliance on “current time” without control
- [ ] Tests are deterministic (seeded randomness if used)
- [ ] CI should pass without secret credentials

---

## 🆘 Troubleshooting

### “Works on my machine” failures
- You’re probably relying on:
  - timezone / locale
  - an env var not present in CI
  - filesystem paths
  - test order

✅ Fix by injecting dependencies and using fixtures/fakes.

### Flaky tests
- Remove real sleeps and timing-based asserts
- Control time (freeze/mock)
- Seed randomness

---

## 🔗 Related docs (repo)
- 📚 System + engineering practices live in the project’s master docs (architecture, workflows, CI expectations)
- 🧱 Clean architecture boundaries should guide what’s unit-testable vs integration-testable

---

### 🧠 Final reminder
Unit tests are the **inner shield**: they make refactors safe and keep core logic stable as data sources, APIs, and UI layers evolve. 🛡️

