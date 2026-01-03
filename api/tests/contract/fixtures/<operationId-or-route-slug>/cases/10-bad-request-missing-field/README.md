---
title: "Contract Fixture — Case 10: 400 Bad Request (Missing Required Field)"
path: "api/tests/contract/fixtures/<operationId-or-route-slug>/cases/10-bad-request-missing-field/README.md"
version: "v0.1.0"
last_updated: "2026-01-03"
status: "active"
doc_kind: "TestFixture"
markdown_protocol_version: "1.0"

fixture:
  kind: "api-contract"
  case_id: "10"
  case_slug: "bad-request-missing-field"
  expected_http_status: 400

operation:
  id_or_slug: "<operationId-or-route-slug>"
  method: "<HTTP_METHOD>"
  route: "<ROUTE_PATH>"

owner: "API Team"
tags:
  - contract-first
  - api
  - contract-tests
  - validation
  - negative-test
  - 400
---

🧪 **Contract Fixture** · 🚫 **Negative Test** · 🧾 **Schema-Backed** · 🛡️ **No PII** · 🔁 **Deterministic**

# 🧪 Case 10: 400 Bad Request — Missing Required Field

This case locks in **input validation behavior** for the operation **`<operationId-or-route-slug>`**: when a request is missing a **required** field (as defined by the API contract), the API must return a **`400 Bad Request`** with the **standard error shape** for this endpoint.

> [!TIP]
> Keep this case **single-fault**: remove **exactly one** required field and keep everything else valid. That prevents flaky tests caused by error-ordering differences.

---

## 📘 Overview

### Purpose 🎯
Ensure the API responds predictably (and contract-compliantly) when a client omits a required input field—preventing silent failures and protecting downstream pipeline integrity.

### Scope ✅ / ❌

| In Scope ✅ | Out of Scope ❌ |
|---|---|
| Missing a required field in request body/params | Authentication/authorization failures (401/403) |
| HTTP status is **400** | Rate limiting (429) |
| Error payload matches the endpoint’s **400 error schema** | Business-rule validation (domain-level rejects) |
| Deterministic, reviewable fixture data | Performance testing |

### Audience 👥
- **Primary:** API developers maintaining `<operationId-or-route-slug>`
- **Secondary:** Contract-test maintainers, reviewers, governance/QA

### Definitions 📚
- **operationId / route slug:** The parent fixture folder identifier for a single endpoint contract.
- **Required field:** A field marked required by the API contract (e.g., OpenAPI `required`, request model requirement, etc.).
- **Contract test:** An automated test that verifies inputs/outputs against the published API contract.

### Key Artifacts 🧩
| Artifact | Where | Notes |
|---|---|---|
| API contract (OpenAPI/GraphQL) | `<path-to-api-contract>` | Source of truth for required fields + error schema |
| This fixture case | `cases/10-bad-request-missing-field/` | Locks in expected 400 behavior |
| Expected error schema | `components.schemas.<ErrorSchema>` (or equivalent) | Must be consistent across endpoints |

---

## 🗂️ Directory Layout

### Placement in repo 🧭
This file is located at:

📁 `api/`  
└── 📁 `tests/`  
&nbsp;&nbsp;&nbsp;&nbsp;└── 📁 `contract/`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 📁 `fixtures/`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 📁 `<operationId-or-route-slug>/`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 📁 `cases/`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 📁 `10-bad-request-missing-field/`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 📄 `README.md` ✅

### Case folder contents 📦
Case folders typically include a **request variant** (with the missing field) and an **expected response** (400 + error payload). Filenames may vary by runner—follow whatever files already exist alongside this README.

> [!NOTE]
> Avoid creating Markdown links to sibling fixture files unless you’re sure they exist—some CI pipelines validate internal links.

---

## 🧾 Scenario

### Preconditions ✅
- Any required auth headers / tokens for this endpoint are present (so we **don’t** accidentally trigger 401/403).
- All non-target fields are valid and within allowed ranges.
- Only **one** required field is omitted.

### Mutation 🔧
Remove exactly one required field:

- Missing field name: **`<REQUIRED_FIELD_NAME>`**
- Field location: **`<body | query | path | headers>`**
- Field meaning: **`<short description>`**

> [!IMPORTANT]
> “Missing” means the key/parameter is **absent**, not `null` (unless the contract explicitly treats `null` as missing).

### Expected Behavior ✅
- **HTTP Status:** `400 Bad Request`
- **Content-Type:** `application/json` (or the contract-defined type)
- **Body:** matches the operation’s **400 error response schema**
- Error identifies the missing field in a **machine-parseable** way (path/loc), and ideally also provides a **human-readable** message.

<details>
  <summary>📎 Illustrative (non-normative) error payload example</summary>

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Missing required field: <REQUIRED_FIELD_NAME>",
    "details": [
      {
        "path": "<body.<REQUIRED_FIELD_NAME>>",
        "reason": "FIELD_REQUIRED"
      }
    ]
  }
}
```

</details>

---

## 🧠 Authoring Notes

### How to pick the missing field 🧩
1. Find a field that is **required** by the contract for this operation.
2. Prefer a field that produces a **single clear error** (e.g., a top-level property).
3. Avoid fields whose absence causes cascading errors (e.g., removing a parent object might produce many missing-child errors).

### Determinism rules 🔁
To keep contract tests stable:
- Remove **only one** required field
- Keep enum/string formats correct for all other fields
- Keep IDs/UUIDs deterministic or clearly fake (`"00000000-0000-0000-0000-000000000000"`)
- Avoid timestamps like “now” unless the contract explicitly expects them

### Common pitfalls 🧯
- You get **422** instead of **400**: the framework may be returning its default validation status. This case is here to ensure KFM’s contract stays consistent (400 for missing required input).
- You get **401/403**: missing/invalid auth is masking the validation behavior—fix auth first.
- Error array ordering differs: reduce to a **single missing field** to avoid multi-error ordering issues.

---

## 🧪 Validation & CI/CD Expectations

> [!NOTE]
> KFM’s CI gates commonly include: contract tests (endpoint must respond as expected), Markdown/front-matter validation (docs must follow protocol), and security/governance scans (no secrets/PII/sensitive locations). Keep fixture data clean and synthetic.

### Fixture data hygiene 🧼
- ✅ Synthetic values only (no real user data)
- ✅ No API keys/tokens/passwords in fixtures
- ✅ No precise sensitive coordinates unless explicitly allowed and properly handled

---

## ✅ Definition of Done

- [ ] `<REQUIRED_FIELD_NAME>` is required by the contract for `<operationId-or-route-slug>`
- [ ] Request fixture omits **only** that field
- [ ] Response fixture asserts **HTTP 400**
- [ ] Response body matches the contract-defined 400 error schema
- [ ] Error output clearly identifies the missing field (path/loc)
- [ ] No secrets, no PII, no sensitive locations in fixture values
- [ ] Contract test suite passes locally and in CI ✅

---

## 🔎 References

- `docs/MASTER_GUIDE_v13.md` (contract-first + CI gates)
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (how endpoint contracts are added/changed)
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` (Markdown protocol + required sections)

