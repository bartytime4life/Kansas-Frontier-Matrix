# 🧪 Unit Tests — `tests/unit/`

![Scope](https://img.shields.io/badge/scope-unit%20tests-blue?style=for-the-badge)
![Runner](https://img.shields.io/badge/runner-pytest%20%2F%20jest-purple?style=for-the-badge)
![Philosophy](https://img.shields.io/badge/philosophy-fail%20closed%20%26%20evidence--first-orange?style=for-the-badge)

Welcome to the **fastest** test layer in the Kansas Frontier Matrix / Kansas-Matrix-System. ✅  
This folder is for **pure, deterministic, low-latency tests** that validate *core logic* without depending on live infrastructure.

> [!IMPORTANT]
> **Unit tests protect our non-negotiables**:
> - 🧱 **Fail-closed governance** (missing metadata / policy violations must block by default)
> - 🔎 **Evidence-first answers** (citations are required, not optional)
> - 🛡️ **Policy enforcement stays wired-in** (security & content rules can’t be “accidentally” bypassed)

---

## 📌 Quick links
- [🚀 Quickstart](#-quickstart)
- [✅ What belongs in unit tests](#-what-belongs-in-unit-tests)
- [🚫 What does NOT belong here](#-what-does-not-belong-here)
- [📂 Suggested layout](#-suggested-layout)
- [🧠 KFM-specific invariants we unit test](#-kfm-specific-invariants-we-unit-test)
- [🧰 Patterns & helpers](#-patterns--helpers)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ PR checklist](#-pr-checklist)

---

## 🚀 Quickstart

### 🐍 Backend (Python / API)
Run unit tests (preferred):
```bash
# from repo root (recommended if running services via docker-compose)
docker-compose exec api pytest tests/unit -q
```

If you run Python tests locally (outside Docker), use your normal workflow (e.g., `pytest tests/unit`).

### 🌐 Frontend (React / Web)
If the web app has unit tests enabled:
```bash
npm test
```

### 🧷 Policy gates (OPA “conftest”, NOT pytest’s `conftest.py`)
To replicate policy validation locally:
```bash
conftest test .
```

> [!TIP]
> The word “conftest” is overloaded:
> - ✅ `conftest` (CLI) = **OPA/rego policy testing**  
> - ✅ `conftest.py` (file) = **pytest fixtures**  
> They are unrelated. Don’t confuse them. 🙂

---

## ✅ What belongs in unit tests

Unit tests should hit **logic** (not infrastructure). Great targets:

- 🧩 **Pure functions** (transformations, parsers, formatters)
- 🧾 **Metadata validation** (required fields present, schema-ish checks)
- 🔐 **Policy decision wiring** (inputs → allow/deny/sanitize decisions)
- ⛓️ **Provenance builders** (PROV objects / ledger entry construction)
- 🧠 **Focus Mode pipeline logic** *(mock dependencies)*:
  - prompt building
  - citation marker formatting
  - post-processing & guardrails
  - “refuse/sanitize” behavior on restricted content
- 🧰 **Utilities** (time normalization, ID formatting, slugging, etc.)

---

## 🚫 What does NOT belong here

Keep unit tests **small + local**. These belong elsewhere (integration/e2e):

- 🗄️ Real database calls (PostGIS / Neo4j / any live DB)
- 🌍 Network calls (HTTP to external services)
- 🧠 Real LLM inference (Ollama/OpenAI) **in unit tests**
- 🐳 Docker orchestration checks
- 🧱 Full-stack flows (UI ↔ API ↔ DB)

> [!NOTE]
> If a test requires spinning up containers or depends on “it works on my machine” state, it’s not a unit test.

---

## 📂 Suggested layout

Use whatever structure matches the repo, but aim for **discoverable + stable** organization:

```text
📦 tests/
 └── 🧪 unit/
     ├── 🐍 api/              # request parsing, response shaping, helpers
     ├── 🧠 ai/               # Focus Mode pipeline logic (mock retrieval + LLM)
     ├── 🛡️ policy/           # policy adapters + rego-related unit checks (no network)
     ├── ⛓️ provenance/        # PROV builders, audit/ledger record constructors
     ├── 🧰 utils/            # shared pure helpers
     ├── 🧷 fixtures/         # tiny JSON/text fixtures used across tests
     └── 📄 README.md         # (you are here)
```

> [!TIP]
> Prefer **many small test files** over one “mega test file”.  
> Example: `test_prompt_builder.py`, `test_citation_formatter.py`, `test_rbac_decision.py`

---

## 🧠 KFM-specific invariants we unit test

### 1) 🧱 “Fail closed” behavior
If anything is missing or invalid, the safest default is **deny/block**.

✅ Unit tests should assert:
- missing license → rejected (or marked non-publishable)
- missing sensitivity label → rejected (or forced to safest classification)
- missing provenance pointer/record → rejected (or flagged)

### 2) 🔎 Evidence-first: citations are mandatory
For Focus Mode / AI responses:
- citations must exist
- citation markers must map to sources
- “no evidence” must produce a refusal or safe fallback

✅ Unit tests should assert:
- answer without citations → fails validation / triggers refusal
- citations are stable and correctly formatted (e.g., numeric markers)
- post-processing never drops citations accidentally

### 3) 🛡️ Policy is always enforced
We do not allow “direct DB bypass” behaviors and we don’t ship code that forgets to call policy checks.

✅ Unit tests should assert:
- policy check is invoked for protected operations
- policy denial returns a denial/sanitized result consistently
- restricted outputs are masked/sanitized when required

### 4) ⛓️ Audit + provenance record construction is correct
Even if a deeper storage layer is integration-tested, unit tests should validate:
- required fields exist (timestamps, actor, activity, inputs, outputs)
- stable identifiers/hashes are produced as expected
- serialization is deterministic (ordering, schema shape)

---

## 🧰 Patterns & helpers

### ✅ Arrange–Act–Assert (AAA)
Keep each test focused and readable:

```python
def test_citation_formatter_includes_markers():
    # Arrange
    sources = [{"id": "doc_1"}, {"id": "dataset_9"}]

    # Act
    answer = format_answer_with_citations("Hello", sources)

    # Assert
    assert "[1]" in answer and "[2]" in answer
```

### 🧪 Use fakes at the boundaries
Prefer these layers (from simplest → heaviest):
- ✅ Fake object
- ✅ Stubbed interface
- ✅ Monkeypatch/mock
- ❌ Real dependency

Examples of what to fake:
- LLM client
- retrieval/search client
- policy client
- clock/time provider

### ⏱️ Time & randomness must be deterministic
- freeze time (or inject a clock)
- set random seeds (or inject RNG)

> [!TIP]
> If a test sometimes fails “only on CI”, it’s usually:
> - time
> - randomness
> - hidden network/FS dependency
> - implicit ordering

---

## 🧯 Troubleshooting

### “My unit tests are slow…”
- Check for accidental network calls
- Check for real DB initialization
- Remove sleeps/timeouts and inject clocks instead

### “CI failed on a governance/policy rule”
- Run policy checks locally:
```bash
conftest test .
```
- Fix the file the rule complains about (often metadata fields / provenance presence).

### “I’m not sure where my test belongs”
Rule of thumb:
- **Unit** = no infrastructure
- **Integration** = multiple components talking together
- **E2E** = user-level flow

---

## ✅ PR checklist

Before you open a PR:

- [ ] 🧪 You added/updated unit tests for new logic
- [ ] ⚡ Tests are deterministic (no time/random/network surprises)
- [ ] 🧱 Fail-closed paths are explicitly tested
- [ ] 🔎 Citation enforcement is covered for Focus Mode logic (when applicable)
- [ ] 🛡️ Policy checks are not bypassed (deny/sanitize behavior tested)
- [ ] 🧹 Linters pass locally (where configured)

---

### 🎯 North Star
**Fast unit tests** = confident refactors + safer governance + fewer regressions. ✅  
If it can break production behavior in a subtle way, it deserves a unit test.