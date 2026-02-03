<!-- According to a document from February 3, 2026. -->

# 🧪 `my-tool` — Tests

[![Tests](https://img.shields.io/badge/tests-local%20%2B%20CI-blue)](../../)
[![Style](https://img.shields.io/badge/style-lint%20%2B%20format-informational)](../../)
[![Policy](https://img.shields.io/badge/policy-conftest%20%2B%20OPA-purple)](../../)

Welcome to the test suite for **`tools/my-tool`** ✅  
This folder exists to keep `my-tool` **correct**, **reproducible**, and aligned with the broader KFM mindset: *repeatable pipelines, provenance-first outputs, and policy-aware guardrails*.

---

## 🧭 Table of Contents

- [🎯 What these tests cover](#-what-these-tests-cover)
- [⚡ Quick start](#-quick-start)
- [🧰 Choose your runner](#-choose-your-runner)
  - [🐍 Python (pytest)](#-python-pytest)
  - [🟦 Node (Jest/Vitest)](#-node-jestvitest)
- [🧱 Test layout](#-test-layout)
- [🏷️ Test markers & naming](#️-test-markers--naming)
- [🧪 Writing good tests](#-writing-good-tests)
- [🧯 Troubleshooting](#-troubleshooting)

---

## 🎯 What these tests cover

At minimum, tests in this folder should validate:

- **Determinism** 🔁: same inputs → same outputs (especially for transforms & exports)
- **Schema safety** 🧩: outputs conform to expected structure (JSON/CSV/GeoJSON/etc.)
- **Edge cases** 🧨: empty input, missing fields, weird encodings, large files
- **Provenance hooks** 🧾: if `my-tool` writes metadata/prov, it should be present + well-formed
- **Policy alignment** 🛡️: when applicable, artifacts should pass repo policy checks (Conftest/OPA)

---

## ⚡ Quick start

From the repo root:

```bash
# 1) Go to the tool
cd tools/my-tool

# 2) Run the test command that matches the tool stack (see below)
# Python:
pytest -q

# Node:
npm test
```

> 💡 Tip: If your CI runs in containers, run tests *inside the same container* to match CI behavior.

---

## 🧰 Choose your runner

Not sure which runner applies? Use this quick sniff test:

- If you see `pyproject.toml`, `requirements*.txt`, or `setup.cfg` → **Python**
- If you see `package.json` → **Node**
- If you see both → this tool may be hybrid; run both test suites

---

## 🐍 Python (pytest)

### ✅ Install (local venv)

```bash
cd tools/my-tool
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# Install dev deps (pick what exists in this tool)
pip install -r requirements-dev.txt
# or:
pip install -e ".[dev]"
```

### ▶️ Run tests

```bash
# all tests
pytest

# quieter output
pytest -q

# run a single file
pytest tests/test_smoke.py

# run by keyword
pytest -k "geocode" -vv

# stop early
pytest --maxfail=1
```

### 🧪 Coverage (optional)

```bash
pytest --cov=my_tool --cov-report=term-missing
```

> 🧠 Keep unit tests fast: mock network calls, patch time, and prefer fixtures over live dependencies.

---

## 🟦 Node (Jest/Vitest)

### ✅ Install

```bash
cd tools/my-tool
npm ci
# or: npm install
```

### ▶️ Run tests

```bash
# run once
npm test

# watch mode (if configured)
npm run test:watch
```

### 📈 Coverage (optional)

```bash
npm run test:coverage
```

> 🧩 If you test UI-ish logic, keep it headless by default (CI-friendly). Use browser/acceptance tests only where they add real value.

---

## 🧱 Test layout

Recommended structure (adapt as needed):

```text
📁 tools/
  📁 my-tool/
    📁 tests/
      📁 unit/           ✅ pure functions, no IO
      📁 integration/    🔌 filesystem, DB, services, docker, etc.
      📁 fixtures/       🧰 sample inputs + golden outputs
      📁 snapshots/      📸 snapshot outputs (only when stable + justified)
      📄 conftest.py     (pytest) shared fixtures + helpers
      📄 README.md       (this file)
```

---

## 🏷️ Test markers & naming

### Python (pytest) suggestions

- `unit`: no IO, no network, no DB
- `integration`: requires filesystem/containers/services
- `slow`: anything that takes “noticeably long”

Example:

```python
import pytest

@pytest.mark.integration
def test_import_pipeline_writes_expected_outputs(tmp_path):
    ...
```

Run only unit tests:

```bash
pytest -m "not integration"
```

### Node suggestions

Prefer consistent naming:

- `*.test.ts` / `*.test.js`
- `__tests__/` for colocated tests if that’s your style

---

## 🧪 Writing good tests

### ✅ Golden rule: test behavior, not implementation

- Assert outputs, side-effects, and contracts (schemas)
- Avoid locking tests to internal function call order unless necessary

### 🔒 Keep tests hermetic

- No network by default 🚫🌐
- Use fixtures for inputs and deterministic seed(s) for randomness 🎲
- If time matters, freeze/patch time ⏱️

### 🧾 Provenance-friendly fixtures

If the tool emits catalog/prov metadata:

- include a **minimal fixture** that exercises metadata generation
- assert required keys exist (e.g., `source`, `license`, `generated_at`, `inputs`, `hashes`, etc.)
- ensure output includes a stable identifier strategy (hashing, canonicalization)

---

## 🧯 Troubleshooting

### 🐳 “Works locally, fails in CI”

- Run tests the same way CI does (often inside Docker)
- Ensure environment variables used in CI are set locally (`.env.test`, etc.)
- If ports or services conflict, stop local processes or change mappings

### 🧩 Import/module resolution issues

- Python: confirm editable install (`pip install -e .`) or proper `PYTHONPATH`
- Node: confirm `type: module` vs CJS expectations, and TS config alignment

### 🧪 Flaky tests

- Eliminate shared global state
- Avoid relying on filesystem ordering
- Don’t use real timeouts unless required; prefer deterministic mocks

---

## ✅ Definition of Done (DoD)

Before merging changes to `my-tool`:

- [ ] unit tests pass locally
- [ ] integration tests pass (when run in CI-equivalent environment)
- [ ] outputs are deterministic (or explicitly documented where not possible)
- [ ] policy checks (if applicable) pass for produced artifacts
- [ ] new functionality includes tests (no “it’s small” exceptions 🙃)

---
