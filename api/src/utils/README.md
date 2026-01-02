# 🧰 `api/src/utils` — API Utilities

![Scope](https://img.shields.io/badge/scope-api%2Fsrc%2Futils-0b7285)
![Style](https://img.shields.io/badge/style-small%20%26%20focused-495057)
![Architecture](https://img.shields.io/badge/architecture-clean%20%2B%20contract--first-364fc7)
![Tests](https://img.shields.io/badge/tests-required-212529)

> [!TIP]
> Utilities should be **boring, predictable, and reusable**. If a file starts feeling like a “misc dumping ground”, split it. 🪓

---

## 🎯 What this folder is

`api/src/utils/` is the **shared toolbox** for cross-cutting, low-level helpers used by the API codebase—things like:

- 🧩 **Config / env parsing**
- 🕒 **Date/time parsing + formatting**
- 🧾 **Error helpers (normalize, wrap, rethrow safely)**
- 🧭 **Logging helpers (structured fields, request correlation)**
- ✅ **Validation glue (runtime validation around contract shapes)**
- 🧼 **Sanitization/redaction helpers**
- ⏳ **Async helpers (retry/timeout/backoff)**

**Goal:** Keep API routes/services consistent and lightweight by centralizing common primitives here—**without** mixing in business logic.

---

## 🧱 Architectural guardrails

> [!IMPORTANT]
> Treat `utils/` as a **low-level layer**. It can be imported “up” by API modules, but it **must not reach upward** into routes/controllers or domain/business rules.

### ✅ Rules of thumb

- ✅ **Single Responsibility:** one module = one job
- ✅ **Prefer pure functions:** same input → same output (easy to test, easy to reason about)
- ✅ **No hidden I/O:** if a util touches network/filesystem/env, make that explicit in naming + docs
- ✅ **No circular dependencies:** if you feel a cycle coming, extract a tiny interface or move the code
- ✅ **One canonical home:** don’t duplicate helpers in multiple folders—utilities live here (or in the repo’s chosen canonical location)

### 🚫 Anti-patterns

- ❌ Business logic (e.g., “how to rank parcels”)
- ❌ DB queries / repositories
- ❌ Route handlers / middleware stacks
- ❌ “God utils” (`utils.ts` with 50 unrelated exports)
- ❌ Copy-pasted helpers in features (“just this once”) 🙃

---

## 🗂️ Suggested layout

This is a **recommended** structure to keep growth controlled (adjust to what the repo actually uses):

```text
📦 api/
└── 🧩 src/
    └── 🧰 utils/
        ├── 📘 README.md                 👈 you are here
        ├── 🧭 index.ts                  (optional barrel export)
        ├── ⚙️ config/                   (env + config parsing)
        ├── 🧯 errors/                   (AppError, error mapping)
        ├── 🪵 logging/                  (logger helpers, request context)
        ├── ✅ validation/               (schema validators + guards)
        ├── ⏱️ time/                     (date parsing, durations)
        ├── 🛡️ security/                 (redaction, safe output helpers)
        └── 🔁 async/                    (retry, timeout, concurrency)
```

> [!NOTE]
> Prefer **small subfolders** by concern over a flat folder of random helpers.

---

## 🧾 Exports & import conventions

### Prefer stable imports 📦

- If you have an `index.ts` barrel:
  - ✅ `import { parseIsoDate } from "@/utils"` *(example)*
- If you don’t:
  - ✅ `import { parseIsoDate } from "@/utils/time/parseIsoDate"`

### Naming conventions 🏷️

- **Files:** `camelCase.ts` or `kebab-case.ts` (pick one and stay consistent)
- **Functions:** `camelCase`
- **Types/classes:** `PascalCase`
- **Booleans:** `isX / hasX / canX`
- **Guards/assertions:** `assertX / requireX`

---

## ✅ How to add a new utility

Use this checklist so utils stay clean:

- [ ] Does it have **one clear purpose**?
- [ ] Is it **pure by default** (or clearly named if it performs I/O)?
- [ ] Does it avoid importing from higher layers (routes/controllers)?
- [ ] Does it have **unit tests** (especially for parsing, validation, edge cases)?
- [ ] Does it have **typed input/output** (if using TS)?
- [ ] Did you document it (JSDoc + brief mention in this README if it’s widely used)?

---

## 🧪 Testing expectations

Utilities are ideal candidates for fast unit tests:

- ✅ parsers: invalid inputs, boundary cases, weird whitespace
- ✅ validators: expected failures (don’t only test happy paths)
- ✅ error helpers: ensure “unknown errors” become consistent app errors
- ✅ logging helpers: make sure sensitive fields are redacted

> [!TIP]
> If a util is hard to test, it’s often a sign it’s doing too much (split it).

---

## 🔐 Config & secrets (don’t leak 🙅)

- Never log secrets (API keys, tokens, raw auth headers).
- Prefer **validated env/config access**:
  - fail fast on missing vars
  - provide defaults only when safe
  - keep `.env.example` up to date (if present)

---

## 📜 Contract-first mindset (why utils matter)

This repo’s docs emphasize that **API contracts are first-class artifacts** and should be versioned/tested as contracts change. Utilities should support that reality:

- request parsing helpers that don’t “invent” fields
- runtime validators aligned with contract shapes
- consistent error envelopes (so clients can depend on them)
- helpers that make contract tests simpler, not harder

---

## 🧭 Quick “Should this be a util?” decision tree

<details>
  <summary><strong>🧠 Click to expand</strong></summary>

- **Is it used in 2+ places?**
  - If no → keep it local for now.
  - If yes → continue.
- **Is it domain/business logic?**
  - If yes → belongs in domain/services, not utils.
  - If no → continue.
- **Is it framework-specific (Express/Fastify/Nest middleware)?**
  - If yes → keep it in the framework layer, not utils.
  - If no → continue.
- **Is it a small, stable helper with a clear boundary?**
  - If yes → ✅ `utils/`
  - If no → refactor first, then decide.

</details>

---

## 🔗 Related docs (repo-level)

- 📘 Master guide / architecture: `../../../docs/MASTER_GUIDE_v13.md` (or repo equivalent)
- 🧾 API contract changes: `../../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- 🧭 Repo structure standards: `../../../docs/standards/` *(if present)*

---

