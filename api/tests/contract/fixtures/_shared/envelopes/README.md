# 📨 Shared Envelope Fixtures (Contract Tests)

![Contract-first](https://img.shields.io/badge/contract--first-✔-blue)
![Contract tests](https://img.shields.io/badge/contract%20tests-fixtures-orange)
![Scope](https://img.shields.io/badge/scope-_shared%2Fenvelopes-lightgrey)

> **What this folder is:** Canonical, reusable **envelope** fixtures used by **API contract tests**.  
> **What this folder is not:** Endpoint/domain payload fixtures (those live next to the endpoint-specific tests/fixtures).

---

## 🧭 Quick navigation

- [📌 Purpose](#-purpose)
- [🗂️ Where this lives](#️-where-this-lives)
- [📦 What we mean by “envelope”](#-what-we-mean-by-envelope)
- [🧪 How contract tests should use these](#-how-contract-tests-should-use-these)
- [🧱 Conventions](#-conventions)
- [🔁 Versioning rules](#-versioning-rules)
- [✅ Add / update checklist](#-add--update-checklist)
- [🚫 Anti-patterns](#-anti-patterns)
- [🛠️ Troubleshooting](#️-troubleshooting)

---

## 📌 Purpose

This directory exists to keep **API boundaries consistent and testable** by sharing the *outer* response/message wrapper across contract tests.

In practical terms, contract tests often need to assert things like:

- The envelope shape is stable (same top-level keys, same error structure, same metadata strategy)
- Optional fields appear when expected (and stay absent when not)
- “Cross-cutting” metadata remains consistent across endpoints (e.g., request IDs, provenance blocks, pagination blocks)

Keeping these in `_shared/envelopes/` avoids:
- 🚫 copy/paste drift between endpoints
- 🚫 silent breaking changes caused by “just tweaking the wrapper”
- 🚫 testing each endpoint as if it invented its own transport format

---

## 🗂️ Where this lives

```text
📦 api/tests/contract/fixtures/
└── 📂 _shared/
    └── 📂 envelopes/
        ├── 📄 README.md      👈 you are here
        └── 📄 *.json         ✅ shared envelope fixtures (success/error/paging/etc.)
```

> 💡 If a fixture is *specific to one endpoint* (or one feature area), it should **not** go here — create/keep it under the endpoint’s fixture folder and only reuse the shared envelope(s).

---

## 📦 What we mean by “envelope”

An **envelope** is the transport wrapper around the “real” payload.

Typical envelopes include some combination of:

- ✅ success indicator / status
- 📦 `data` payload (the domain output)
- 🧾 metadata (paging, trace/provenance, timing, warnings)
- 🧨 structured errors (validation errors, auth errors, rule violations)

> 🔒 **Source of truth:** the *actual* envelope shape must match the API contracts (OpenAPI / GraphQL + any JSON Schemas).  
> This folder stores **examples** used for repeatable, automated verification — not an alternate spec.

---

## 🧪 How contract tests should use these

### Recommended usage pattern

1. **Pick a shared envelope** that matches the scenario
   - success / error / paginated / async-job / etc.
2. **Combine** it with endpoint-specific payload fixtures (if needed)
3. **Validate** the result against the contract (OpenAPI / GraphQL / JSON Schema)
4. **Assert invariants** that must never regress

### Example: compose envelope + payload (pseudo)

```js
// pseudo-code (framework-agnostic)
const envelope = loadJson('_shared/envelopes/success.json')
const payload  = loadJson('layers/get-layer.response.json')

const response = {
  ...envelope,
  data: payload
}

assertConformsToContract(response)
```

<details>
<summary>🧩 Example loaders (Node & Python)</summary>

```ts
// Node/TS example
import fs from "node:fs";
import path from "node:path";

export function loadJson(relPath: string) {
  const abs = path.join(process.cwd(), "api/tests/contract/fixtures", relPath);
  return JSON.parse(fs.readFileSync(abs, "utf8"));
}
```

```py
# Python example
import json
from pathlib import Path

def load_json(rel_path: str):
  base = Path.cwd() / "api" / "tests" / "contract" / "fixtures"
  return json.loads((base / rel_path).read_text(encoding="utf-8"))
```

</details>

---

## 🧱 Conventions

### 1) Fixture scope rules ✅

**Put it here** if:
- It represents a *generic* envelope used across many endpoints
- It encodes cross-cutting response/message structure

**Do NOT put it here** if:
- It contains domain-specific `data` (e.g., “soil profile payload”, “story node payload”)
- It includes endpoint-specific edge cases that don’t generalize

---

### 2) File naming 📛

Use names that communicate:

- **kind**: `success`, `error`, `paginated`, `accepted`, `stream`, etc.
- **variant**: `minimal`, `with_meta`, `with_provenance`, `validation`, `auth`, etc.
- **version** (when needed): `v1`, `v2`, etc. (folder or prefix)

Examples (choose one strategy and stick to it):

- `success.minimal.json`
- `success.with_meta.json`
- `error.validation.json`
- `v1/success.minimal.json`

> 🧠 Naming tip: if you can’t guess what it is from the filename, the next person can’t either.

---

### 3) Deterministic values 🎯

Contract fixtures should be **stable** and **diff-friendly**:

- Prefer fixed timestamps (e.g., `"2020-01-01T00:00:00Z"`) over “now”
- Prefer fixed IDs (e.g., `"req_00000001"`) over random UUIDs
- Avoid values that vary by machine/timezone/environment
- Keep fixtures small, but representative

---

### 4) Formatting & hygiene 🧹

- JSON should be pretty-printed (consistent indentation)
- Keep key ordering consistent (helps reviews, avoids noisy diffs)
- Newline at EOF (✅ yes, always)
- Never include secrets (tokens, API keys, private URLs)

---

## 🔁 Versioning rules

Envelopes are **contract artifacts** in practice, even when they’re “just fixtures”.

- ✅ Backwards-compatible additions are OK (new optional fields that contract allows)
- ⚠️ Removing or renaming envelope fields is a **breaking change**
- 🧱 If the contract requires a version bump, the fixture set must reflect that bump

> If you change an envelope fixture and multiple contract tests fail, that’s a feature — it’s showing you where the contract boundary changed.

---

## ✅ Add / update checklist

Before merging any envelope fixture change:

- [ ] The API contract (OpenAPI / GraphQL / schema) already matches the intended envelope shape
- [ ] The fixture is deterministic (no time/random/environment variance)
- [ ] The fixture is minimal but representative (includes required + important optional fields)
- [ ] Any breaking change is versioned (v1 vs v2, or clearly separated strategy)
- [ ] Contract tests are updated to use the right envelope variant
- [ ] You ran the contract suite locally and verified the diff is meaningful (not formatting noise)

---

## 🚫 Anti-patterns

- ❌ “Fixing” contract tests by loosening assertions instead of aligning fixtures + contracts
- ❌ Putting domain payload examples inside shared envelopes (causes coupling & confusion)
- ❌ Using placeholders that aren’t supported by the test harness (unless the harness explicitly templates fixtures)
- ❌ Adding fields that are not in the contract “because we return them anyway”
- ❌ Letting envelope drift between endpoints (the whole point is consistency)

---

## 🛠️ Troubleshooting

**Tests fail because envelope has extra fields**
- Ensure the contract actually allows them (additionalProperties vs strict schema)

**Tests fail because envelope is missing fields**
- Confirm whether the field is required by contract or only present in some variants (choose the right fixture)

**Flaky failures**
- Look for timestamps, random IDs, ordering differences, or environment-dependent values

---

## 📣 When in doubt…

Use the contract as the authority, and treat these fixtures as the *canonical examples* contract tests rely on. If you need a new envelope type, create it here once — and reuse it everywhere. 🧩✨

