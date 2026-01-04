---
title: "Validation Utilities ✅"
path: "api/src/utils/validation"
status: "active"
owner: "API Team"
last_updated: "2026-01-04"
tags:
  - api
  - validation
  - contract-first
  - error-handling
---

# ✅ Validation Utilities (`api/src/utils/validation`)

> **Runtime guards at the API boundary** — validate untrusted inputs early, normalize errors consistently, and keep endpoints aligned with the repo’s contract-first philosophy. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 📘 Overview

### 🎯 Purpose

This folder exists to provide a **single, reusable validation layer** for the API surface area:

- ✅ **Contract-first enforcement**: schemas + API contracts are first-class artifacts; changes trigger strict versioning/compatibility expectations. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}
- ✅ **Governed API boundary**: all access flows through the API layer to enforce schema consistency, access control, redaction, and classification rules. :contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}
- ✅ **Clean architecture boundary hygiene**: translate “messy” framework inputs (HTTP) into clean, typed values for use cases (“talk inwards with simple data”). :contentReference[oaicite:6]{index=6}

### ✅ In scope

- 🧾 Request validation (body, query, params, headers)
- 🧼 Coercion/normalization (strings → numbers/dates/booleans) where safe
- 🧯 Standardized validation errors (shape + mapping to HTTP)
- 🧩 Shared reusable validators (pagination, IDs, date ranges, bbox, etc.)
- 🧪 Helpers that make **API contract tests** easy to write and maintain :contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

### 🚫 Out of scope

- ❌ Business rules (belongs in services/use-cases)
- ❌ DB lookups / repository access
- ❌ Authorization decisions (but validation may check *presence/shape* of auth claims)
- ❌ “Fixing” sensitive data classification (validation must **respect propagation**, not override it) :contentReference[oaicite:9]{index=9}

---

## 🗂️ Directory Layout (recommended)

> If the folder currently differs, treat this as the **target** structure. 🧭

```text
📦 api/
 └─ 📦 src/
    └─ 🧰 utils/
       └─ ✅ validation/
          ├─ 📄 README.md            👈 you are here
          ├─ 🧩 index.ts             (public exports)
          ├─ 🧪 validate.ts          (core validation wrapper)
          ├─ 🧯 errors.ts            (error types + normalizers)
          ├─ 🧾 schemas/             (request/response schemas)
          │   ├─ 🧾 pagination.ts
          │   ├─ 🧾 ids.ts
          │   └─ 🧾 geo.ts
          └─ 🧷 types.ts             (shared types for validators)
```

---

## 🧠 Core Principles (KFM-aligned)

### 1) 🧾 Contract-first, always

A **contract artifact** is a machine-validated schema/spec that defines an interface (JSON Schema, OpenAPI spec, GraphQL SDL, etc.). It must be versioned and honored by implementations. :contentReference[oaicite:10]{index=10}

**Implication for validation**:
- Your runtime validators are the **enforcement mechanism** for those contracts.
- Any change to request/response shape must be reflected in:
  - 📜 OpenAPI / GraphQL schema
  - ✅ runtime validator schema(s)
  - 🧪 contract tests (to lock expected behavior) :contentReference[oaicite:11]{index=11}:contentReference[oaicite:12]{index=12}

### 2) 🧱 Backwards-compat is the default

APIs should remain backwards-compatible unless a **version bump** is declared; breaking the OpenAPI contract means incrementing the version. :contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}

**Implication for validation**:
- Prefer additive changes (optional fields, new enum values with defaults)
- Reject breaking constraints unless versioned (e.g., `v2/` route)

### 3) 🧼 Validate at the boundary, keep the core clean

KFM’s architecture emphasizes inner layers being unaware of outer implementations, using simple data inward and interfaces outward. :contentReference[oaicite:15]{index=15}

**Implication for validation**:
- Validation happens in route handlers/middleware/resolvers.
- Use cases should receive **already-validated** inputs.

### 4) 🔒 Governance is not optional

Sensitive/redacted/classified data must be protected end-to-end, including at the API layer. :contentReference[oaicite:16]{index=16}:contentReference[oaicite:17]{index=17}

**Implication for validation**:
- Validate that “public endpoints” cannot accept parameters that would expose restricted data.
- Enforce constraints like max precision, bounded geo windows, paging caps, etc.

---

## 🔌 Integration Patterns

### 🧩 Pattern A — Middleware/handler-level validation (REST)

✅ Validate *before* controller logic:

```ts
// pseudo-code (adapt to Express/Fastify/Nest/etc.)
import { validateBody, validateQuery, validateParams } from "@/utils/validation";

router.get(
  "/layers/:layerId",
  validateParams(Schemas.layerIdParams),
  validateQuery(Schemas.layerQuery),
  async (req, res) => {
    // req.params / req.query are now trusted & typed
    const result = await useCases.getLayer.execute({
      layerId: req.params.layerId,
      date: req.query.date,
    });

    return res.status(200).json(result);
  }
);
```

### 🧠 Pattern B — “Request Object” boundary (Clean Architecture flavor)

When you want a clear seam, create a request DTO that is built only from validated inputs:

```ts
// pseudo-code
const request = BuildGetLayerRequest({
  params: req.params,
  query: req.query,
});

if (!request.ok) return res.status(400).json(request.error);

return useCase.execute(request.value);
```

This pattern pairs nicely with standardized failure objects (next section). :contentReference[oaicite:18]{index=18}

---

## 🧯 Error Model (standardized)

### ✅ Goals

- consistent across endpoints
- easy to test in contract tests
- safe (no leaking stack traces or internals by default)

### 🧩 Recommended shape

```json
{
  "error": {
    "type": "ParametersError",
    "message": "layerId: Is mandatory\nbbox: invalid format",
    "details": [
      { "path": "layerId", "message": "Is mandatory" },
      { "path": "bbox", "message": "invalid format" }
    ]
  }
}
```

### 🏷️ Error types (suggested)

Borrowing the clean “typed failure” approach:

- `ParametersError` → 400
- `ResourceError` → 404
- `SystemError` → 500 :contentReference[oaicite:19]{index=19}:contentReference[oaicite:20]{index=20}

The key point is **consistent** `type` + `message` formatting and a clean `details[]` structure. :contentReference[oaicite:21]{index=21}

---

## 🧰 What to Put in This Folder (concrete checklist)

### ✅ Validators to centralize

- 🔢 Pagination:
  - `limit` max cap (prevent abuse)
  - `offset`/`cursor` mutual exclusivity
- 🆔 IDs:
  - UUID/slug validation
  - allowlist patterns
- 🗓️ Dates & time ranges:
  - ISO parsing
  - `start <= end`
- 🗺️ Geo inputs (if applicable):
  - bbox validation
  - GeoJSON shape validation
  - max area / max point count constraints
- 🧪 “Contract alignment helpers”:
  - build test payloads
  - snapshot-friendly error formatting (stable ordering)

### 🚫 Validators that don’t belong here

- checking user permissions (“can user see this layer?”)
- cross-entity existence checks (“does this layerId exist?”) → repository/service responsibility

---

## 🧪 Validation & CI Expectations

KFM’s CI gates include contract tests and schema linting for API interfaces; changes that break expected behavior are blocked. :contentReference[oaicite:22]{index=22}

Your validation utilities should make it easy to satisfy these gates:

- ✅ deterministic error messages (stable ordering of `details`)
- ✅ predictable HTTP statuses
- ✅ shared schemas so behavior doesn’t drift across endpoints

Also note: CI runs security/governance scans and checks for sensitive data leaks; validation utilities can help enforce safe bounds. :contentReference[oaicite:23]{index=23}:contentReference[oaicite:24]{index=24}

---

## 🧭 Adding / Updating Validation (repeatable steps)

> “Validation steps are listed and repeatable” is part of the project’s definition of done. :contentReference[oaicite:25]{index=25}

### ✅ Step-by-step

1) 🧾 **Update the contract**
   - OpenAPI / GraphQL schema is the source of truth.
   - If breaking, version it. :contentReference[oaicite:26]{index=26}

2) 🧩 **Add or update runtime schema**
   - place in `schemas/`
   - keep naming aligned with endpoint path and method

3) 🔌 **Wire validation at the boundary**
   - middleware / handler / resolver entry point

4) 🧪 **Update/add contract tests**
   - cover happy path + validation failure shapes
   - CI enforces these tests. :contentReference[oaicite:27]{index=27}

5) 🔒 **Check governance implications**
   - ensure no input allows bypassing redaction/classification constraints
   - remember: no output can be less restricted than its inputs. :contentReference[oaicite:28]{index=28}:contentReference[oaicite:29]{index=29}

6) 📝 **Document the change**
   - for endpoint changes, use the API contract extension template. :contentReference[oaicite:30]{index=30}

---

## 🔗 Related Docs (repo paths)

- 📄 `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` — required pattern for adding/changing endpoints. :contentReference[oaicite:31]{index=31}
- 📘 KFM Master Guide v13 (draft) — contract-first + CI gates (v13.0.0-draft dated 2025-12-28). :contentReference[oaicite:32]{index=32}
- ⚖️ Governance & sovereignty docs (see `docs/governance/`) for sensitive data rules. :contentReference[oaicite:33]{index=33}

---

## 🧾 Source Notes (why this README is structured this way)

This README is aligned to:

- **Contract-first** definition and contract artifacts as first-class, versioned interfaces. :contentReference[oaicite:34]{index=34}:contentReference[oaicite:35]{index=35}
- **API subsystem contract** expectations (OpenAPI/GraphQL + contract tests + compatibility). :contentReference[oaicite:36]{index=36}:contentReference[oaicite:37]{index=37}
- **Clean architecture boundary rules** (“simple data inward, interfaces outward”). :contentReference[oaicite:38]{index=38}
- **Typed failure objects** pattern for consistent error shaping. :contentReference[oaicite:39]{index=39}

