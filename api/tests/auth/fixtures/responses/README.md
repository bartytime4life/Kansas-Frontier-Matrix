---
title: "Auth API Response Fixtures"
path: "api/tests/auth/fixtures/responses/README.md"
status: "active"
---

# 🔐 Auth API Response Fixtures

![fixtures](https://img.shields.io/badge/fixtures-responses-informational)
![scope](https://img.shields.io/badge/scope-auth-blueviolet)
![tests](https://img.shields.io/badge/tests-contract%20%2F%20integration-success)

This folder contains **golden response bodies** (a.k.a. *fixtures*) used by the Auth test suite to keep tests:

- ✅ deterministic (same input → same output)
- ✅ contract-aware (responses match the API contract)
- ✅ fast (no external dependencies just to validate shapes)
- ✅ reviewable (diffs show API changes clearly)

---

## 📦 What belongs here

**Only** response payloads (usually JSON) for Auth endpoints and edge cases.

Typical examples:
- ✅ login success response
- ✅ login error (invalid credentials)
- ✅ refresh success / refresh error
- ✅ token expired / invalid token
- ✅ forbidden (role/permission) responses
- ✅ validation error payloads (missing fields)
- ✅ rate-limit payloads (too many attempts)

> [!IMPORTANT]  
> **Never commit real secrets.** Any `access_token`, `refresh_token`, `session_id`, cookies, or PII must be replaced with stable placeholders (see **Redaction Rules**).

---

## 🗂️ Recommended layout

Keep fixtures grouped by endpoint (or feature) so they’re easy to discover and diff.

```text
📦 api/tests/auth/fixtures/responses/
├─ 📄 README.md
├─ 📁 login/
│  ├─ 🧾 200.success.json
│  ├─ 🧾 401.invalid_credentials.json
│  ├─ 🧾 422.validation_error.json
│  └─ 🧾 429.rate_limited.json
├─ 📁 refresh/
│  ├─ 🧾 200.success.json
│  ├─ 🧾 401.invalid_refresh_token.json
│  └─ 🧾 401.expired_refresh_token.json
├─ 📁 me/
│  ├─ 🧾 200.success.json
│  └─ 🧾 401.missing_or_invalid_access_token.json
└─ 📁 password-reset/
   ├─ 🧾 200.request_accepted.json
   ├─ 🧾 400.invalid_reset_token.json
   └─ 🧾 429.too_many_requests.json
```

> [!TIP]  
> If your auth endpoints are versioned (e.g., `/v1/auth/login`), you can add a version folder like `v1/login/…` to keep migrations clean.

---

## 🏷️ Naming conventions

A fixture filename should tell you **exactly** what it represents.

**Pattern:**
```text
<status>.<scenario>.json
```

Examples:
- `200.success.json`
- `401.invalid_credentials.json`
- `401.expired_token.json`
- `403.forbidden_role.json`
- `422.validation_error.json`

If you need more detail:
```text
<status>.<scenario>.<variant>.json
```
Example:
- `422.validation_error.missing_password.json`

---

## 🧼 Redaction rules (non‑negotiable)

Auth responses often contain sensitive values. Replace them with stable placeholders:

### ✅ Replace these always
- tokens: `access_token`, `refresh_token`, `id_token`
- identifiers: `session_id`, `device_id`, `jti`
- user fields: `email`, `phone`, `name` (unless you *explicitly* use test-only dummy values)
- timestamps that change every run: `iat`, `exp`, `created_at`, `last_login_at` (unless tests freeze time)

### ✅ Recommended placeholder vocabulary
Use consistent placeholder strings so diffs stay clean:
- `"<ACCESS_TOKEN>"`
- `"<REFRESH_TOKEN>"`
- `"<SESSION_ID>"`
- `"<USER_ID>"`
- `"<REQUEST_ID>"`
- `"<ISO_TIMESTAMP>"`

---

## 🧪 How tests should use these fixtures

### ✅ Rule of thumb
Fixtures should validate **shape + contract**, not brittle runtime details.

- Assert **HTTP status**
- Assert **content-type** (when applicable)
- Assert **response body** equals fixture (or equals fixture *after normalization*)

### 🧰 Suggested helper: `loadResponseFixture()`

If you don’t already have one, create a tiny loader helper (location varies by repo conventions):

```ts
// Example (TypeScript): api/tests/_utils/fixtures.ts
import fs from "node:fs";
import path from "node:path";

export function loadResponseFixture(relPath: string) {
  const fullPath = path.join(__dirname, "..", "auth", "fixtures", "responses", `${relPath}.json`);
  return JSON.parse(fs.readFileSync(fullPath, "utf8"));
}
```

Example test usage:
```ts
import { loadResponseFixture } from "../_utils/fixtures";

test("POST /auth/login → 401 invalid credentials", async () => {
  const expected = loadResponseFixture("login/401.invalid_credentials");

  const res = await client.post("/auth/login").send({
    email: "user@example.com",
    password: "wrong-password",
  });

  expect(res.status).toBe(401);
  expect(res.body).toEqual(expected);
});
```

> [!NOTE]  
> If your server includes dynamic fields (timestamps, request IDs), normalize them before comparing:
> - delete volatile keys
> - replace with placeholders
> - sort arrays when order is not guaranteed

---

## 🔁 Updating fixtures safely

Update fixtures **only** when one of these is true:

- ✅ the API contract changed intentionally (schema, field names, error structure)
- ✅ a bugfix changed the canonical output and the new output is correct
- ✅ an additional required field is introduced and versioning rules allow it

### Suggested workflow
1. Make the API change + update contract (OpenAPI / schema).
2. Run the auth tests to see failures.
3. Update **only the impacted** fixture(s).
4. Re-run tests and ensure diffs are minimal and reviewed.

---

## ✅ “Definition of Done” for a new fixture

- [ ] Fixture file is placed in the correct endpoint folder 📁  
- [ ] Filename includes status + scenario 🏷️  
- [ ] Contains **no secrets** (tokens, session IDs, real emails) 🧼  
- [ ] Uses stable placeholders for volatile fields ⏱️  
- [ ] Test asserts status + body against fixture 🧪  
- [ ] If contract changed, schema/OpenAPI updated too 📜  

---

## 🧯 Common pitfalls

- **❌ Accidentally committing real JWTs**  
  → Always replace token values with placeholders before commit.

- **❌ Freezing the entire response when only shape matters**  
  → Prefer normalizing volatile fields.

- **❌ Fixture drift** (fixtures no longer match contract)  
  → Treat fixtures as contract evidence and update them alongside contract changes.

---

## 🔎 Quick glossary

- **Fixture**: A stored, known-good sample response used for tests.
- **Golden file**: Same as fixture, with emphasis on “diff-driven” review.
- **Normalization**: Removing or stabilizing dynamic fields before comparison.

---

