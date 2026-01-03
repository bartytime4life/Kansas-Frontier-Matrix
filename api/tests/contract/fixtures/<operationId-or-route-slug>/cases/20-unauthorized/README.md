---
title: "Case 20 — Unauthorized (401)"
path: "api/tests/contract/fixtures/<operationId-or-route-slug>/cases/20-unauthorized/README.md"
version: "v1.0.0"
last_updated: "2026-01-03"
status: "active"
doc_kind: "Contract Test Fixture"
case:
  id: 20
  slug: "20-unauthorized"
  expected_http_status: 401
  category: "auth"
---

# 🔒 Case 20 — Unauthorized (401)

![Contract Fixture](https://img.shields.io/badge/contract-fixture-blue)
![HTTP 401](https://img.shields.io/badge/HTTP-401%20Unauthorized-critical)
![Auth](https://img.shields.io/badge/auth-bearer%20JWT-informational)

> ✅ **Intent:** Prove this endpoint **rejects requests without a valid auth token** and returns a stable, non-leaky **401 Unauthorized** response.

---

## 📘 Overview

### 🎯 Purpose
This fixture case verifies that **authentication is enforced** for `<operationId-or-route-slug>` by asserting:

- Requests **missing** a bearer token → **401 Unauthorized**
- Requests with a **malformed / invalid / expired** token → **401 Unauthorized**

It also helps keep the **401 vs 403 boundary** crisp:
- **401** = you are not authenticated (no/invalid token)
- **403** = you are authenticated (valid token) but **not allowed** (permission/ownership/role)

### 🧭 Scope

| ✅ In Scope | ❌ Out of Scope |
|---|---|
| Missing `Authorization` header | Permission/ownership failures (belongs in `30-forbidden`) |
| Invalid token format / scheme | Business validation (belongs in `4x/5x` cases) |
| Expired token behavior | Rate limiting / throttling behavior |
| Stable error shape (contract) | Full auth provider / login flow |

### 👥 Audience
- 🧪 Contract-test authors maintaining fixtures
- 🔧 API implementers validating middleware/auth guards
- 🛡️ Reviewers checking security regressions

### 📚 Definitions
- **JWT**: A signed token containing identity + claims (roles/expiry).
- **Bearer token**: The token format carried in `Authorization: Bearer <token>`.
- **Unauthorized (401)**: Authentication failed or is missing.
- **Forbidden (403)**: Authenticated but not permitted.

---

## 🗂️ Directory Layout

Expected location:

```text
📁 api/
├─ 📁 tests/
│  └─ 📁 contract/
│     └─ 📁 fixtures/
│        └─ 📁 <operationId-or-route-slug>/
│           └─ 📁 cases/
│              └─ 📁 20-unauthorized/
│                 ├─ 📄 README.md      👈 you are here
│                 ├─ 📄 request.*      📨 fixture request (NO auth header)
│                 ├─ 📄 expected.*     🔒 expected response (401)
│                 └─ 📄 meta.*         🧩 optional (notes/overrides/matchers)
```

> 🧩 **Note:** File names vary by runner (`.json`, `.yml`, etc.). Keep the intent the same: **request without valid auth** + **expected 401**.

---

## 🧩 Scenario Matrix

| Scenario | What we send | Expected |
|---|---|---|
| 🚫 No auth header | No `Authorization` header at all | **401** |
| 🧨 Wrong scheme | `Authorization: Basic ...` | **401** |
| 🧻 Empty bearer | `Authorization: Bearer` | **401** |
| 🧟 Expired token | `Authorization: Bearer <expired>` | **401** |
| 🧩 Invalid token | `Authorization: Bearer invalid-token` | **401** |

✅ Pick **one** canonical scenario for this case folder (usually **no header**) to keep fixtures deterministic, and only add more variants if the contract runner supports scenario parameterization cleanly.

---

## 📨 Request Contract

### ✅ Required shape
Use the **same method/path/query/body** as the “happy path” case for this operation, except:

- **MUST NOT include** `Authorization`
- **MUST NOT include** cookies/session headers that implicitly authenticate
- **MUST NOT include** real tokens (even expired ones)

### Example (raw HTTP)
```http
<METHOD> <PATH> HTTP/1.1
Host: <host>
Accept: application/json
Content-Type: application/json

{ "…": "…" }
```

### Example (curl)
```bash
curl -i \
  -X <METHOD> "<BASE_URL><PATH>" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  --data '<BODY_JSON>'
```

> 🧪 Tip: If this endpoint is `GET` with no body, omit `--data` and keep the request minimal.

---

## ✅ Expected Response Contract

### 🔢 Status
- **401 Unauthorized**

### 🧾 Headers (typical)
Depending on implementation, you may see:
- `Content-Type: application/json`
- `WWW-Authenticate: Bearer …` *(optional but common)*

Don’t over-specify volatile headers (dates, request IDs) unless your runner supports matchers.

### 🧱 Body (must be safe & stable)
Your error payload must:
- Not leak protected resource details
- Not include secrets/tokens
- Be consistent enough to be a contract (stable keys + stable meaning)

**Recommended minimal JSON pattern (example):**
```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

<details>
  <summary>🧠 If your API uses an RFC7807-style "problem details" shape</summary>

```json
{
  "type": "about:blank",
  "title": "Unauthorized",
  "status": 401,
  "detail": "Missing or invalid bearer token."
}
```
</details>

---

## 🛡️ Security & Hygiene Notes

- 🔥 **Never commit real credentials**: no API keys, passwords, tokens, or “real looking” JWT strings in fixtures.
- 🧼 Prefer placeholders: `<TOKEN>`, `<EXPIRED_TOKEN>`, `invalid-token`.
- 🧯 Keep the unauthorized response generic: avoid confirming whether a resource exists.

---

## 🧪 Validation Notes

- These fixtures exist to keep **API behavior stable** across refactors.
- Contract tests should fail loudly if:
  - A formerly protected endpoint becomes accessible without auth
  - A response changes shape unexpectedly
  - A 401/403 boundary gets blurred

---

## ✅ Definition of Done

- [ ] Request fixture omits `Authorization` completely (or uses the canonical invalid scenario)
- [ ] Response fixture asserts **401** (not 403, not 200)
- [ ] Error payload is stable + non-leaky
- [ ] No secrets / tokens / credentials appear anywhere in this case folder
- [ ] Contract suite passes locally + in CI for this operation

---

