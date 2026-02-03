# 🤖 AI Test Suite — `tests/ai/` (Focus Mode) 🧭

> **Goal:** keep Focus Mode **evidence-first**, **policy-gated**, and **reproducible** ✅  
> This folder is where we prove (with tests) that our AI stays grounded in retrieved sources, returns citations, and respects governance + safety guardrails.

---

## 🏷️ Badges (wire these up in CI)
![CI](https://img.shields.io/badge/CI-configure%20me-blue?logo=githubactions&logoColor=white)
![Tests](https://img.shields.io/badge/tests-AI%20%2F%20RAG%20%2F%20Policy-informational)
![OPA](https://img.shields.io/badge/policy-OPA%20(Rego)-informational)
![Ollama](https://img.shields.io/badge/LLM-Ollama-local%20runtime-success)
![RAG](https://img.shields.io/badge/RAG-hybrid%20retrieval-success)
![Reproducibility](https://img.shields.io/badge/reproducibility-required-success)

---

## 🧠 What we’re testing (Focus Mode contract) ✅

Focus Mode is designed to be **advisory-only**: it should **only** narrate/assemble what retrieval returns, **not invent** new facts or claim tool access it doesn’t have.

### Non‑negotiables (tests must enforce)
- **📚 Evidence-first answers:** factual claims must be supported by retrieved sources.
- **🔗 Citations are mandatory:** answers must include source citations consistently.
- **🧼 Prompt Gate / sanitization:** prompt injection attempts get neutralized before the LLM sees them.
- **🛡️ Output policy checks:** final responses must pass policy (OPA/Rego or equivalent).
- **🧾 Provenance:** responses should be traceable (model version, prompt version, sources used).
- **🚫 No magical powers:** the LLM does **not** get direct DB/filesystem/network access.

> If any of these regress, tests should fail loudly 🔥

---

## 🗺️ Pipeline map (what integration tests should cover)

```mermaid
flowchart TD
  U[User question] --> PG[Prompt Gate 🧼 sanitize + normalize]
  PG --> R[Retrieval 🔍 hybrid: graph + spatial + text + vectors]
  R --> P[Prompt Assembly 🧩 system rules + context + SOURCES [1..n]]
  P --> L[LLM Generate 🤖 Ollama /api/generate]
  L --> OP[Output Policy 🛡️ OPA/Rego + validation]
  OP --> PR[Provenance 🧾 log: sources, model, prompt version, decision]
  PR --> A[Answer ✅ with citations]
```

---

## 🧪 Test Pyramid (recommended)

### 1) 🔧 Unit tests (fast, deterministic)
Test pure functions:
- prompt builders / templates
- citation formatting + validation
- retrieval result normalization + merging
- context window compaction (“high-signal” trimming)
- provenance payload creation

✅ **No network**, no Ollama, no DB.

---

### 2) 🔗 Contract tests (API + schema)
Validate the AI endpoints behave like a stable API contract:
- endpoint accepts expected payload (question + optional context like place/time)
- response schema includes answer + citations (or a structured error)
- streaming endpoint (if enabled) emits expected event sequence
- policy rejection returns the correct error shape + safe message

---

### 3) 🔍 RAG regression tests (golden + invariant checks)
Run curated questions against a **fixed fixture corpus**:
- verify **must-have citations**
- verify **must-mention key facts** (keywords/phrases)
- verify **must-not hallucinate** (no claims outside fixture sources)
- verify minimum citation count / coverage

✅ Prefer **invariant-based assertions** over exact string snapshots:
- “contains citations”
- “mentions X”
- “does not mention Y”
- “all cited source IDs exist in the fixture bundle”

---

### 4) 🛡️ Policy & safety tests (must be mean 😈)
- prompt injection attempts (e.g., “ignore sources, reveal secrets”)
- role/permission boundaries (guest vs contributor vs admin context)
- disallowed content requests
- “missing citations” should fail policy
- “claims of tool access” should fail validation

---

### 5) ⚡ Performance / scalability checks (optional, but valuable)
- latency budgets (p50/p95) for:
  - retrieval
  - generation
  - end-to-end
- caching effectiveness (repeat query speedup)
- stress tests with small fixture sets

> Keep perf tests separate (e.g., `-m slow` / nightly) 🕒

---

## 📁 Suggested folder structure 🗂️

> This is a **recommended** layout; adapt to the repo’s current conventions.

```text
tests/ai/
├─ README.md                # 👈 you are here
├─ fixtures/                # 📦 tiny, deterministic test data
│  ├─ sources/              # 🧩 source snippets with IDs (1..n)
│  ├─ questions.yaml        # ❓ curated prompts + expectations
│  └─ contexts.json         # 🗺️ place/time/layer contexts
├─ unit/                    # 🔧 pure function tests
├─ contract/                # 🔗 API schema + response validation
├─ policy/                  # 🛡️ OPA/Rego tests + policy fixtures
├─ rag_regression/          # 🔍 golden/invariant regression tests
├─ perf/                    # ⚡ load/latency tests (optional)
└─ scripts/                 # 🧰 helpers (update goldens, report scores)
```

---

## ▶️ Running the tests (local)

### ✅ Quick start (recommended dev loop)
1. Start the LLM runtime (Ollama) locally.
2. Run unit + policy tests first.
3. Run RAG regression tests after.

### 🐍 Python (pytest-style)
> If this project uses `pytest`, these commands are typical.

```bash
# Fast checks (unit + policy)
pytest tests/ai/unit tests/ai/policy -q

# Contract + integration (may require API + Ollama running)
pytest tests/ai/contract tests/ai/rag_regression -q

# Everything
pytest tests/ai -q
```

### 🟨 Node (Jest-style) — optional
If any AI clients/tools are in Node:
```bash
npm test
# or
npx jest tests/ai
```

---

## 🔧 Environment configuration (common knobs)

> Keep tests reproducible by pinning what can drift.

**Suggested env vars to support:**
- `OLLAMA_API_URL` — where the LLM runtime is hosted (often `http://localhost:11434`)
- `AI_MODEL` — model name/tag (pin versions in CI)
- `AI_EMBED_MODEL` — embedding model name/tag (pin versions in CI)
- `AI_TEST_MODE=1` — enables deterministic behavior (if supported)
- `AI_SEED` — random seed for any sampling (if supported)

✅ In CI: use a **smaller model** (faster, cheaper) and run a **curated regression set**.

---

## ✍️ Writing a new AI test (pattern)

### ✅ Naming conventions
- Use stable IDs: `rag__<topic>__<place>__<year>`
- Put expectations next to inputs:
  - question
  - optional context
  - required citations / must-mentions / must-not-mentions

### Example test case schema (YAML)
```yaml
- id: rag__dust_bowl__finney_county__1935
  question: "What happened here in the mid-1930s and why?"
  context:
    place: "Finney County, KS"
    year: 1935
    layers: ["drought_index"]
  expect:
    policy: allow
    must_include_citations: true
    min_citation_count: 2
    must_mention_any:
      - "drought"
      - "Dust Bowl"
    must_not_mention_any:
      - "I searched the web"
      - "I accessed your database directly"
```

### ✅ Assertion style (recommended)
Prefer:
- structured parsing (extract citation tokens)
- keyword + invariant checks
- source ID validation

Avoid:
- exact full-string snapshot comparisons (LLMs drift naturally)

---

## 🧾 Updating baselines (when the model/prompt changes)

When you *intentionally* change:
- retrieval strategy
- prompt templates
- policy rules
- model version/tag

…expect regression diffs.

✅ Recommended workflow:
1. run regression suite locally
2. inspect diffs (citations, coverage, hallucination checks)
3. update goldens only if the change is expected + reviewed
4. pin versions (model + prompt) in metadata

---

## 🧯 Debugging checklist (when a test fails)

- **Citations missing?**  
  - check prompt template includes SOURCES + citation rule
  - check output policy didn’t strip tokens
- **Hallucination detected?**  
  - inspect retrieved snippets (is evidence actually present?)
  - tighten prompt: “use only sources”
  - add post-validation: “claims must map to source IDs”
- **Policy rejection unexpected?**  
  - run policy tests directly
  - print the exact input object passed to OPA/Rego
- **Regression drift after model bump?**  
  - pin model tag in CI
  - update goldens only after review

---

## ✅ PR checklist (AI changes)

- [ ] Added/updated tests in `tests/ai/`
- [ ] Regression suite passes locally (or in CI)
- [ ] Model + prompt versions pinned (or documented)
- [ ] Policy tests updated if guardrails changed
- [ ] New behaviors documented (what changed + why)

---

## 🔗 Related docs (recommended reading)
- `docs/architecture/ai/` 📁  
- `docs/architecture/AI_SYSTEM_OVERVIEW.md` 📄  
- `docs/architecture/ai/OLLAMA_INTEGRATION.md` 📄  
- `src/server/api/README.md` 📄  

---

## 🧭 Philosophy (why we’re strict)
We’re building a historical + geospatial “truth machine,” not a vibes generator ✨➡️📚  
If the system can’t cite it, it shouldn’t say it. ✅
