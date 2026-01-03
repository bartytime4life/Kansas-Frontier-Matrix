# 🚫 Not Found (404) — Contract Fixture

<kbd>case:not-found</kbd> <kbd>http:404</kbd> <kbd>tests:contract</kbd> <kbd>boundary:api</kbd> <kbd>contract-first</kbd>

> [!IMPORTANT]
> This folder defines the **canonical** “resource does not exist” behavior for **this operation** (`<operationId-or-route-slug>`).  
> Keep it **deterministic**, **backwards-compatible**, and **safe** (no data leaks).

---

## 🎯 Purpose

This “not-found” case exists to lock down the API’s **stable** behavior when a client requests a *valid* identifier that does **not** exist.

Why this matters:

- ✅ Clients can reliably handle missing resources
- ✅ Contract tests catch breaking changes early (status codes + error shape drift)
- ✅ Error responses stay **consistent** across refactors and backend swaps

---

## ✅ What counts as “Not Found”

Use this case when:

- The request is **schema-valid** (headers/params/body parse correctly)
- The resource identifier is **well-formed**
- The resource **does not exist** (or is intentionally treated as non-existent per contract)

Typical examples:

- `GET /…/{id}` with a missing `{id}`
- `PATCH|PUT /…/{id}` with a missing `{id}`
- `DELETE /…/{id}` with a missing `{id}`
- Nested: `GET /parents/{parentId}/children/{childId}` where any required ID is missing

---

## 🚫 What this case is NOT

Don’t use this folder for:

- ❌ validation / schema errors → usually `400 Bad Request`
- ❌ authn/authz errors → usually `401/403`  
  - unless your contract explicitly returns `404` to prevent “existence leaks” (document that in `notes.md`)
- ❌ conflict/concurrency issues → `409`
- ❌ intentional retirement → `410 Gone`

---

## 🗂️ Folder anatomy

📁 `api/tests/contract/fixtures/<operationId-or-route-slug>/cases/not-found/`

```text
📁 api/
 └── 📁 tests/
     └── 📁 contract/
         └── 📁 fixtures/
             └── 📁 <operationId-or-route-slug>/
                 └── 📁 cases/
                     └── 📁 not-found/
                         ├── 📄 README.md           👈 you are here
                         ├── 📄 request.(json|yml)  ✅ required by runner
                         ├── 📄 response.(json|yml) ✅ required by runner
                         └── 📄 notes.md            📝 optional (human context)
```

> [!TIP]
> **Do not invent new filenames** here. Mirror the conventions used by sibling cases under the same operation folder so the contract runner can discover and execute the case.

---

## 🧪 How to author a solid Not Found fixture

### 1) Pick a deterministic “missing” identifier 🧷

Choose a value that is **guaranteed not to exist** in the seeded/fixture dataset used by contract tests.

| ID style | Recommended “missing” value | Why it works |
|---|---|---|
| UUID | `00000000-0000-0000-0000-000000000000` | obvious + deterministic |
| Integer | `999999999` | unlikely to collide with seeds |
| Slug | `__missing__` / `does-not-exist` | readable + deterministic |
| Composite | `parentId=__missing__`, `childId=__missing__` | points to the failing key |

> [!WARNING]
> Avoid random UUIDs unless the runner supports placeholders/matchers. Random inputs make failures harder to reproduce and debug.

### 2) Make the request “valid but missing” ✅

- ✅ all required headers present
- ✅ all required params present and parseable
- ✅ request body (if any) is valid
- ❌ don’t violate schema on purpose (that belongs in a `bad-request/` case)

### 3) Keep the response stable + minimal 🔒

At minimum, assert:

- ✅ HTTP status: `404`
- ✅ `Content-Type`: whatever the API contract specifies (usually JSON)
- ✅ error **shape** matches the API contract
- ✅ no sensitive/internal leakage (stack traces, SQL details, filesystem paths, secrets, PII)

---

## 📦 Example fixtures

> [!NOTE]
> These examples are intentionally generic. Adjust the **shape** to match this repo’s contract runner conventions and the API’s published error schema.

<details>
<summary><strong>Example request.json</strong> 📄</summary>

```json
{
  "name": "not-found",
  "description": "Requested resource does not exist",
  "request": {
    "method": "GET",
    "path": "/v1/<resource>/{id}",
    "pathParams": {
      "id": "00000000-0000-0000-0000-000000000000"
    },
    "headers": {
      "Accept": "application/json"
    }
  }
}
```
</details>

<details>
<summary><strong>Example response.json</strong> 📄</summary>

```json
{
  "status": 404,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "error": {
      "code": "NOT_FOUND",
      "message": "Resource not found"
    }
  }
}
```
</details>

### Volatile fields (trace IDs, timestamps) ⏱️

If your API includes a `requestId` / `traceId` and it changes every request:

- ✅ exclude it from strict equality assertions, **or**
- ✅ use the runner’s matcher/placeholder feature (if available)

---

## 🧷 Common pitfalls

- **404 vs 400**: if `{id}` fails validation/parsing, it’s not “not found”
- **404 vs 403**: if you intentionally return `404` for unauthorized to prevent existence leaks, document it in `notes.md`
- **Body drift**: renaming fields (e.g., `error.code` → `code`) breaks clients; prefer additive changes

---

## ✅ Definition of Done

- [ ] The “missing” identifier cannot exist in any seeded/fixture dataset
- [ ] The request is schema-valid (no intentional validation errors)
- [ ] The response is `404` and matches the API’s error schema
- [ ] No volatile fields are hard-asserted unless matchers are used
- [ ] Contract suite passes locally and in CI 🎉

---

## 🔗 Related (for API changes)

If this not-found behavior changes, it’s likely an **API contract change**.  
Use the repo’s API contract change process/template (if applicable) and update fixtures alongside the spec.

- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

