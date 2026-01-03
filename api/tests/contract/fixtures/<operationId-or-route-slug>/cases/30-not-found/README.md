![Contract Tests](https://img.shields.io/badge/contract-tests-fixture-blue) ![Case](https://img.shields.io/badge/case-30--not--found-orange) ![HTTP](https://img.shields.io/badge/HTTP-404_Not_Found-red)

# 🚫 Case 30 — Not Found (404)

> **Fixture scope:** `api/tests/contract/fixtures/<operationId-or-route-slug>/cases/30-not-found/`  
> ✅ Use this case to prove the endpoint returns a **standards-compliant 404** when the target resource cannot be found.

---

## 🧾 Summary

| Field | Value |
|---|---|
| Case ID | `30-not-found` |
| Category | Negative / error path |
| Expected status | `404 Not Found` |
| Why it exists | Protects the API contract (CI-gated) ✅ |
| Typical trigger | “valid request, missing resource” (unknown ID / slug) |

---

## 🎯 What this case is testing

This case should validate that the API:

- returns **HTTP `404`** (not `200`, not `500`)  
- returns a response that matches the **OpenAPI/GraphQL contract** for the 404 branch (schema + media type)  
- returns a **safe** error payload (no stack traces, no secrets, no internal implementation details) 🔒  
- is **deterministic** in the parts that matter for contracts (status + schema + stable fields) 🧊

> [!TIP]
> Think of `30-not-found` as: *“the request was valid, authorization is fine, but the thing you asked for doesn’t exist.”*

---

## 📦 Fixture anatomy

> The exact file names depend on the fixture runner, but the intent is the same:
> one **request definition**, one **expected response definition**, plus optional setup/notes.

```text
📦 api/
└── 🧪 tests/
    └── 🧾 contract/
        └── 🧷 fixtures/
            └── 🧭 <operationId-or-route-slug>/
                └── 🧰 cases/
                    └── 🚫 30-not-found/
                        ├── 📝 README.md              # 👈 you are here (case docs + intent)
                        ├── 📩 request.*              # request fixture (method/path/headers/body)
                        ├── 📤 response.*             # expected fixture (404 status/headers/body)
                        └── 🧪 state.*                # (optional) seed/setup ensuring “resource absent”
```

---

## 🧪 Scenario definition

### ✅ Preconditions

- The request is **syntactically valid** (all required params exist, types are correct).
- The caller is **allowed to access** the endpoint (so we don’t accidentally test auth as the reason).
- The requested resource identifier is **guaranteed absent** from the seeded fixture dataset.

### 🧷 Pick an “absent” identifier

Use an ID that passes validation but does not exist:

- **UUID routes:** `00000000-0000-0000-0000-000000000000`
- **Numeric IDs:** `999999999` (or another non-seeded sentinel)
- **Slug IDs:** `__does-not-exist__`
- **Composite keys:** keep format valid, but choose non-seeded values

> [!IMPORTANT]
> If the identifier is *invalid* (wrong type/format), that’s a **400** case, not a **404** case.

---

## 📩 Request expectations

Your `request.*` file should:
- include all **required headers** (e.g., `Accept`, auth headers if required by the operation)
- include all **required params** (path/query)
- use a **valid-but-absent** identifier as described above

Example (pseudo, adapt to your endpoint):

```http
GET /<route>/<valid-but-absent-id>
Accept: application/json
Authorization: Bearer <valid-test-token>
```

---

## 📤 Response expectations (what `response.*` must assert)

At minimum:

- **Status:** `404`
- **Headers:** whatever the contract requires (often `Content-Type`)
- **Body:** must validate against the **404 response schema** for this operation

Example body shape (pseudo only — follow the contract’s actual error schema):

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Resource not found",
    "details": {
      "resource": "<type>",
      "id": "<valid-but-absent-id>"
    }
  }
}
```

> [!NOTE]
> If your API uses RFC7807 style “Problem Details”, prefer `application/problem+json` and the contract’s `ProblemDetails` schema.

---

## ✅ Assertions checklist

Use this to confirm the fixture is “contract-grade”:

- [ ] Status code is exactly **404**
- [ ] `Content-Type` matches the contract (and body matches that media type)
- [ ] Response body validates against the **404 schema** in the API contract
- [ ] No secrets / stack traces / internal file paths leak 🔒
- [ ] Deterministic fields are stable (status + schema + stable error code/message)
- [ ] Any dynamic fields (like `requestId`, `traceId`, timestamps) are either:
  - [ ] explicitly allowed to vary by the contract runner, **or**
  - [ ] asserted with pattern/“present” rules instead of exact matches

---

## 🧠 Common gotchas

- **List endpoints** typically return `200` + `[]` when “no results” — don’t force 404 unless the contract says so.
- If you see `500`, the handler is probably throwing instead of mapping the missing resource to a typed not-found error.
- If you see `403/401`, your fixture request is testing auth (or missing/invalid credentials).

---

## 🛡️ Fixture hygiene rules

- ✅ Use synthetic IDs and synthetic content  
- ❌ Never paste real API keys, tokens, secrets, or user data into fixtures  
- ✅ Keep the fixture small and readable (contract tests should be fast)

---

## 🏁 Why this file matters

Contract fixtures are **living truth**: when the contract changes, the fixtures and tests must change with it — and CI should catch any drift.

> [!TIP]
> If you add a new not-found behavior, prefer **adding a new case** (e.g., `31-not-found-alt`) over mutating this one unless it is truly the same semantics.

