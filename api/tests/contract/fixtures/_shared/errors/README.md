# 🧩 Shared Error Fixtures for API Contract Tests

![Contract-first](https://img.shields.io/badge/contract--first-%E2%9C%85-blue)
![Contract Tests](https://img.shields.io/badge/tests-contract-orange)
![Fixtures](https://img.shields.io/badge/fixtures-_shared%2Ferrors-purple)
![Safety](https://img.shields.io/badge/no%20PII%20%7C%20no%20secrets-%F0%9F%94%92-success)

This folder contains **reusable error-response fixtures** shared across the **API contract test suite**.  
The goal is to keep error outputs **consistent, deterministic, and safe** across endpoints.

> [!IMPORTANT]
> **If the API error contract changes**, you must update:
> 1) the contract (OpenAPI/GraphQL/JSON Schema), and  
> 2) the relevant contract tests + fixtures  
> in the **same change-set** to prevent drift.

---

## 📍 Where you are

```text
📁 api/
└── 📁 tests/
    └── 📁 contract/
        └── 📁 fixtures/
            └── 📁 _shared/
                └── 📁 errors/
                    ├── 📄 README.md   👈 you are here
                    ├── 📄 <shared error fixtures live here>
                    └── 📄 ...
```

---

## 🎯 Why shared error fixtures exist

Shared error fixtures help us:

- ✅ **Avoid duplication** (same 401/403/404/429/500 shapes used everywhere)
- 🧠 Keep error handling **predictable** for clients (UI, SDKs, integrators)
- 🧪 Make contract tests **stable** and easier to maintain
- 🔒 Ensure fixtures remain **sanitized** (no secrets, no PII, no internal stack traces)

---

## 📦 What belongs here vs. what doesn’t

### ✅ Put these here
- “Standard”/cross-cutting errors used by many endpoints:
  - authentication/authorization (`401`, `403`)
  - not found (`404`)
  - validation (`400`, `422`)
  - rate limit (`429`)
  - server failures (`500`, `503`)
- Canonical examples of **shared error envelope** shapes.

### 🚫 Do NOT put these here
- Endpoint-specific, one-off errors that only apply to a single route  
  → keep those in the endpoint’s own fixture folder.
- Any fixture containing:
  - real user identifiers, names, emails, phone numbers, coordinates that should be private
  - API keys, tokens, passwords
  - internal stack traces or framework exception dumps

> [!TIP]
> If you’re unsure whether an error is “shared”, ask:  
> **Would multiple endpoints reuse this exact error shape and semantics?**  
> If yes → `_shared/errors/`. If no → keep it endpoint-scoped.

---

## 🧱 Error response shape

> [!NOTE]
> The **source of truth** for the exact error payload shape is the **API contract** (OpenAPI/GraphQL + schemas).  
> This README shows a **pattern**, not a guarantee of the real schema.

### Suggested baseline fields (typical pattern)
Keep shared error fixtures aligned with whatever the contract defines, but commonly you’ll see:

- `status` (HTTP status code or equivalent)
- `code` (stable, machine-friendly error code)
- `message` (human-readable summary)
- `errorId` / `requestId` / `correlationId` (safe identifier for support + logging)
- `details` (optional structured details for validation errors)

### Example payload (illustrative)
```json
{
  "error": {
    "status": 422,
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "errorId": "err_0000000000000000",
    "details": [
      {
        "path": "query.limit",
        "issue": "must be <= 100"
      }
    ]
  }
}
```

✅ **Good fixture traits**
- Deterministic values (stable IDs, fixed timestamps if present)
- Safe text (no internal stack trace, no leaking system internals)
- Matches the contract schema (field names, required/optional, types)

---

## 🏷️ Naming convention

Use filenames that are:
- predictable
- sortable
- stable over time

**Recommended pattern:**
```text
<httpStatus>__<slug>.json
```

**Examples:**
- `401__unauthorized.json`
- `403__forbidden.json`
- `404__not_found.json`
- `422__validation_error.json`
- `429__rate_limited.json`
- `500__internal_error.json`

> [!IMPORTANT]
> Do **not** rename fixtures casually.  
> Treat them like “public test contracts” consumed by the test suite.

---

## 🧪 Using shared error fixtures in tests

How they’re used depends on the contract testing harness, but the intent is:

- Endpoint tests reference shared fixtures for common error cases
- Tests assert:
  - status code
  - headers (if part of contract)
  - response body shape (schema match or exact match, depending on test strategy)

### Pseudo-example
```ts
// Example only — adapt to your test harness
const unauthorized = loadFixture("_shared/errors/401__unauthorized.json");

expect(response.status).toBe(401);
expect(response.body).toMatchObject(unauthorized);
```

---

## 🛠️ Adding or updating an error fixture

### Step-by-step ✅
1. **Confirm contract**: identify the canonical error schema in:
   - API contract definitions (OpenAPI/GraphQL), and/or
   - JSON Schemas used by the API boundary
2. Add/adjust the fixture JSON **to match the contract**
3. Keep values **deterministic** (avoid `Date.now()`, random UUIDs, etc.)
4. Ensure the fixture is **sanitized**
5. Update any tests that reference the fixture

### Checklist (copy/paste) ✅
- [ ] Matches the contract schema (types + required fields)
- [ ] No secrets (keys/tokens/passwords)
- [ ] No PII / sensitive coordinates
- [ ] No internal stack traces / framework exception dumps
- [ ] Deterministic values (stable IDs, fixed timestamps if present)
- [ ] Referenced by tests (or documented if intentionally unused)

---

## 🧯 Troubleshooting

### “Contract test failed: error response mismatch”
Common causes:
- Contract changed but fixture did not (or vice versa)
- Endpoint returned a different error envelope than the shared standard
- A “dynamic field” (timestamp, random ID) wasn’t stabilized or ignored by assertions

Suggested approach:
1. Check the **API contract** first (schema + examples)
2. Compare actual response vs. fixture
3. Decide:
   - Should the endpoint conform to the shared error envelope? ✅ (preferred)
   - Or is it endpoint-specific and should move out of `_shared`?

---

## 🔗 Related docs & paths (repo-root)

- 📘 Master guide (contract-first / CI expectations): `/docs/MASTER_GUIDE_v13.md`
- 🧾 API contract work template: `/docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- 🧱 Schemas: `/schemas/`
- 🌐 API boundary (service + contract definitions): `/src/server/`

---

