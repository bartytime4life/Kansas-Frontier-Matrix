# 🧯 Errors Utilities (`api/src/utils/errors`)

![layer](https://img.shields.io/badge/layer-api%20utils-blue)
![contract](https://img.shields.io/badge/contract--first-required-purple)
![status](https://img.shields.io/badge/status-stable%20wire%20format-brightgreen)

> **Goal:** one predictable way to **create**, **normalize**, **log**, and **serialize** errors at the API boundary—without leaking internals and without breaking client contracts.  
> KFM treats **contracts** as first-class, versioned artifacts and expects deterministic, governed behavior at boundaries.

---

## 🔎 What belongs in this folder?

This folder is the “error toolkit” used by the API layer to:

- 🧱 define **typed/structured errors** (e.g., `NotFound`, `Validation`, `Unauthorized`, `Conflict`, `Upstream`, `Internal`)
- 🧭 map internal errors → **HTTP status + stable error code**
- 🧼 normalize unknown throwables (strings, `Error`, library exceptions) into a safe, consistent shape
- 🧾 serialize a **standard error envelope** for clients (wire format)
- 🧯 enforce **redaction** rules (no stack traces / internal details in production responses)

Because KFM is **contract-first** and expects governed interfaces, the wire-format error envelope + codes should be treated as part of the public API contract.

---

## 🧠 Design principles (KFM-aligned)

### 1) Contract-first + versioned
A “contract artifact” is a machine-validated schema/spec and must be versioned and honored by implementations—error payloads fall under this principle when exposed to clients.

### 2) Backward compatible by default
APIs are expected to remain backward compatible unless a version bump occurs; contract changes should be tested.

### 3) Deterministic behavior at the boundary
The boundary should behave in an idempotent, predictable way (same class of error → same HTTP + code + envelope).

### 4) Safety & redaction
Avoid leaking sensitive/internal information in responses; keep full details in logs/telemetry, not in client payloads.

---

## 🏗️ Where this fits in the architecture

KFM documentation describes a layered structure and a shared `utilities` area for reusable helpers; error utilities are a classic fit there, used by routes/controllers and adapters to keep behavior consistent.:contentReference[oaicite:8]{index=8}

**Layering reminder:** keep imports directional (outer layers depend inward), and avoid leaking HTTP concerns into domain logic.:contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}

---

## 🧾 Standard error envelope (wire format)

Treat this shape as the stable, client-facing contract.

```json
{
  "error": {
    "code": "KFM_NOT_FOUND",
    "message": "Story node not found.",
    "status": 404,
    "details": {
      "resource": "StoryNode",
      "id": "abc123"
    },
    "requestId": "req_01H..."
  }
}
```

### Field rules
- `error.code` ✅ stable, machine-parseable (client logic can branch on this)
- `error.message` ✅ human-readable **and safe** (no SQL, no stack traces, no secrets)
- `error.status` ✅ HTTP status used in the response
- `error.details` ⚠️ optional, **must be safe to expose** (validation errors, missing fields, etc.)
- `error.requestId` ✅ correlation ID to connect client errors to server logs (recommended)

> If you add/remove/rename fields in this envelope, treat it as a contract change and update the relevant contract artifacts + tests.

---

## 🧭 Error taxonomy (recommended)

A practical taxonomy that keeps client behavior predictable:

| Category | Typical HTTP | Example code | Notes |
|---|---:|---|---|
| Validation / Parameters | 400 | `KFM_VALIDATION_ERROR` | client can fix request |
| Authentication | 401 | `KFM_UNAUTHORIZED` | missing/invalid auth |
| Authorization | 403 | `KFM_FORBIDDEN` | authenticated but not allowed |
| Not found | 404 | `KFM_NOT_FOUND` | safe to reveal resource type (usually) |
| Conflict | 409 | `KFM_CONFLICT` | concurrency/uniqueness |
| Rate limit | 429 | `KFM_RATE_LIMITED` | include `retryAfter` in details if safe |
| Upstream dependency | 502/503/504 | `KFM_UPSTREAM_ERROR` | do **not** leak vendor internals |
| Internal / Unknown | 500 | `KFM_INTERNAL_ERROR` | default for unhandled errors |

---

## 🔁 Error normalization flow (boundary pattern)

```mermaid
flowchart LR
  A[throw / reject anywhere] --> B[normalizeError(err)]
  B --> C[map to code + HTTP status]
  B --> D[log full error + context]
  C --> E[toErrorResponse()]
  E --> F[send standard error envelope]
```

**Why normalize?** In JS/TS, “errors” can be strings, library objects, or standard `Error` instances. Normalization makes outputs deterministic and contract-safe.

---

## 🛠️ Usage patterns (Express-style middleware)

If this API is using Express (or an Express-compatible stack), the canonical pattern is:

### 1) In routes/controllers: `next(err)` on failure
Node/Express error flow: if you pass an argument to `next()`, Express treats it as an error and routes it to error-handling middleware.:contentReference[oaicite:13]{index=13}

```ts
router.get("/story-nodes/:id", async (req, res, next) => {
  try {
    const node = await storyNodeService.getById(req.params.id);

    if (!node) {
      // Prefer throwing/returning a typed error rather than ad-hoc responses
      throw new NotFoundError("StoryNode", { id: req.params.id });
    }

    res.json({ data: node });
  } catch (err) {
    next(err); // ✅ routes into error middleware
  }
});
```

### 2) Register error middleware LAST
Express error-handling middleware is defined with **four parameters** `(err, req, res, next)` and should be registered at the end of the middleware chain.:contentReference[oaicite:14]{index=14}

```ts
app.use(errorHandler); // ✅ last
```

---

## 🧯 Logging & redaction rules

The Node.js reference notes that common error objects include a `message`, a `status`, and a `stack` trace (often used for debugging).:contentReference[oaicite:15]{index=15}

**Policy (recommended):**
- ✅ Log the original error + stack server-side (and include `requestId`, route, user/tenant context as allowed)
- ✅ Return the standardized envelope with safe `message` + stable `code`
- ❌ Do not send `stack` traces or raw `cause` objects to clients in production
- ⚠️ Only include `details` when it is clearly safe and useful (validation messages, missing parameters, etc.)

KFM governance emphasizes respecting redaction rules at API boundaries and avoiding data leakage.

---

## 🧩 Result-style errors (optional pattern)

Some clean-architecture implementations model failures as **explicit response objects** (e.g., `ResponseFailure`) that carry a `type` + `message` and can map cleanly to status codes—this can be useful for domain/use-case layers to avoid coupling to HTTP exceptions.:contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}

If you use this pattern:
- Domain/use-cases return a failure object (no HTTP knowledge)
- API adapter maps failure type → `error.code` + HTTP status + envelope

---

## 🧪 Testing expectations

KFM guidance calls out that APIs should have contracts (e.g., OpenAPI schemas) and that changes should be tested, including contract tests where appropriate.

Additionally, the project’s “Master Coder Protocol” emphasizes automated testing and CI as part of maintaining correctness and repeatability.:contentReference[oaicite:20]{index=20}

**Minimum tests to add when touching this folder:**
- ✅ unit tests for `normalizeError()` (unknowns become `KFM_INTERNAL_ERROR`)
- ✅ unit tests for status/code mapping
- ✅ serialization tests (no sensitive fields)
- ✅ contract tests (error envelope matches the API contract)

---

## ➕ Adding a new error (checklist)

1. 🆕 Add a new **stable code** (do not reuse old codes)
2. 🧭 Map code → HTTP status (and keep mapping deterministic)
3. 🧾 Document:
   - when it is thrown
   - what `details` may include (and what must never be included)
4. 🧪 Add/adjust tests (unit + contract)
5. 📜 If it changes a public surface, update the relevant contract artifacts/templates (see templates referenced in the master guide).

---

## ✅ Definition of Done (for changes in this folder)

KFM’s documentation workflow highlights a “Definition of Done” including “front-matter complete,” “all claims link to sources,” and validation steps—apply the same rigor to error-contract changes.

- [ ] Error envelope still matches contract (no breaking field changes)
- [ ] New/changed codes are documented and tested
- [ ] No sensitive info can leak via `message` or `details`
- [ ] Middleware is registered last (Express-style)
- [ ] Unit tests updated/added
- [ ] Contract tests updated/added (if applicable)
- [ ] Docs updated (and checklist completed)

> Markdown guidance also recommends using clear templates + checklists for transparency and reviewability.:contentReference[oaicite:23]{index=23}

---

## 📌 Optional metadata (if this README is ingested by docs tooling)

<details>
<summary>🗂️ YAML front-matter snippet (example)</summary>

```yaml
---
title: "Errors Utilities"
path: "api/src/utils/errors/README.md"
version: "v0.1.0"
last_updated: "2026-01-04"
status: "active"
doc_kind: "Reference"
---
```

YAML front-matter examples like this are commonly used in KFM-style governed documentation to keep metadata consistent.:contentReference[oaicite:24]{index=24}

</details>

---

## 📚 References (project files used)

- **KFM Master Markdown Guide (v13)** — contract-first, deterministic pipeline, templates, and definition-of-done guidance.
- **KFM Technical Documentation** — layered structure + utilities folder expectations and import direction guidance.:contentReference[oaicite:29]{index=29}
- **Node.js Notes for Professionals** — Express error middleware semantics and signature details.:contentReference[oaicite:30]{index=30}:contentReference[oaicite:31]{index=31}
- **Scientific Method / Master Coder Protocol** — automated testing + CI emphasis.:contentReference[oaicite:32]{index=32}
- **Clean Architectures in Python** — example of modeling failures as explicit response objects and mapping failure types to HTTP status codes.:contentReference[oaicite:33]{index=33}:contentReference[oaicite:34]{index=34}

