# 🔐 Password Request Fixtures

![Scope](https://img.shields.io/badge/scope-auth%2Fpassword-2ea44f)
![Type](https://img.shields.io/badge/type-test%20fixtures-informational)
![Format](https://img.shields.io/badge/format-json%20request%20bodies-blue)

> **Folder:** `api/src/auth/tests/fixtures/requests/password/`  
> **Goal:** Keep **canonical, reusable request payloads** for password-related auth tests (happy paths + edge cases) 🧪

---

## 🧭 Navigation

- [📦 What belongs here?](#-what-belongs-here)
- [🧩 Supported flows](#-supported-flows)
- [📁 Naming & layout conventions](#-naming--layout-conventions)
- [🧪 Using fixtures in tests](#-using-fixtures-in-tests)
- [🔒 Security & realism notes](#-security--realism-notes)
- [➕ Adding / updating fixtures](#-adding--updating-fixtures)
- [🧹 Common pitfalls](#-common-pitfalls)

---

## 📦 What belongs here?

This directory contains **request-body fixtures** (usually JSON) for password workflows, such as:

- **Forgot password** (request a reset email / reset token) ✉️
- **Reset password** (submit token + new password) 🔁
- **Change password** (authenticated user changes password) 🔄

✅ Keep this folder strictly about **request payloads**.  
➡️ If you store response fixtures, put them in a sibling folder like `fixtures/responses/...` (or the project’s chosen structure).

---

## 🧩 Supported flows

> The exact endpoint paths and field names depend on the API contract in this repo.  
> The examples below use common conventions so the intent is obvious.

### 1) Forgot password ✉️

**Intent:** user submits email → backend sends reset token/link out-of-band.

Typical request fields:

- `email`

Example fixture:

```json
{
  "email": "user@example.com"
}
```

Suggested cases to cover:

- ✅ valid email
- ❌ malformed email
- ❌ unknown email (if API intentionally returns 200 to avoid user enumeration, document that in the test)

---

### 2) Reset password 🔁

**Intent:** user submits reset token + new password.

Typical request fields:

- `token` (one-time reset token)
- `new_password`
- `confirm_password` (or `confirm_new_password`)

Example fixture (with placeholder token):

```json
{
  "token": "{{reset_token}}",
  "new_password": "CorrectHorseBatteryStaple!1",
  "confirm_password": "CorrectHorseBatteryStaple!1"
}
```

Suggested cases to cover:

- ✅ valid token + strong password
- ❌ invalid token format
- ❌ expired token (if distinguishable)
- ❌ reused token (one-time token replay)
- ❌ weak password
- ❌ password mismatch

---

### 3) Change password 🔄

**Intent:** authenticated user changes password (usually requires `Authorization: Bearer <token>` header set in the test).

Typical request fields:

- `current_password`
- `new_password`
- `confirm_password`

Example fixture:

```json
{
  "current_password": "OldPassword!1",
  "new_password": "NewPassword!2",
  "confirm_password": "NewPassword!2"
}
```

Suggested cases to cover:

- ✅ correct current password + strong new password
- ❌ wrong current password
- ❌ new password too weak
- ❌ new password equals old password (if policy disallows)
- ❌ password mismatch

---

## 📁 Naming & layout conventions

### ✅ Recommended naming

Use **one of these** styles (pick one and stay consistent):

**Option A: flat filenames (simple, grep-friendly)**  
`<flow>.<case>.json`

Examples:
- `forgot.valid.json`
- `forgot.invalid_email.json`
- `reset.valid.json`
- `reset.invalid_token.json`
- `change.valid.json`
- `change.wrong_current_password.json`

**Option B: subfolders per flow (scales better as cases grow)**  
`<flow>/<case>.json`

Examples:
- `forgot/valid.json`
- `reset/invalid_token.json`
- `change/wrong_current_password.json`

### 🗂️ Example folder tree

```text
📁 api/
  📁 src/
    📁 auth/
      📁 tests/
        📁 fixtures/
          📁 requests/
            📁 password/
              📄 README.md
              📄 forgot.valid.json
              📄 forgot.invalid_email.json
              📄 reset.valid.json
              📄 reset.invalid_token.json
              📄 change.valid.json
              📄 change.wrong_current_password.json
```

### 🧷 Placeholders (tokens, IDs, etc.)

When a value must be generated at runtime (e.g., reset token), store a clear placeholder and replace it in the test:

- `{{reset_token}}`
- `{{access_token}}`
- `{{user_id}}`

✅ The fixture remains stable.  
✅ The test controls the runtime value.

---

## 🧪 Using fixtures in tests

### Example (Node / TS)

```ts
import fs from "node:fs";
import path from "node:path";

function loadFixture(name: string) {
  const p = path.join(__dirname, "../fixtures/requests/password", name);
  return JSON.parse(fs.readFileSync(p, "utf8"));
}

// Example: reset password happy path
const body = loadFixture("reset.valid.json");
body.token = resetTokenFromFactoryOrEmail;
```

### Example (Python)

```py
import json
from pathlib import Path

def load_fixture(name: str) -> dict:
    p = Path(__file__).parent / "fixtures" / "requests" / "password" / name
    return json.loads(p.read_text(encoding="utf-8"))

body = load_fixture("reset.valid.json")
body["token"] = reset_token
```

---

## 🔒 Security & realism notes

- Fixtures represent **what the client sends** → they contain **plain-text passwords** by design.  
  Hashing happens server-side. ✅
- Do **not** commit real secrets/tokens. Use placeholders + runtime injection. 🧯
- If the API uses JWT access tokens + refresh tokens:
  - request-body fixtures live here ✅
  - **headers** (e.g., `Authorization`) should be set in the test harness 🔧

---

## ➕ Adding / updating fixtures

When you add a new password-related endpoint or validation rule:

- [ ] Add at least **1 happy path** fixture ✅  
- [ ] Add at least **2 negative cases** (validation + authz/authn) ❌  
- [ ] Use stable placeholder tokens (don’t hardcode real tokens) 🧩  
- [ ] Update tests that import fixtures 🧪  
- [ ] Update this README if you introduce new flows or naming rules 📝

---

## 🧹 Common pitfalls

- **Mixing headers + body** in the same fixture (keep this folder body-only).  
- **Burying meaning** in filenames like `case1.json` (prefer explicit cases).  
- **Brittle fixtures** that include runtime-only values (timestamps, expiring tokens).  
- **Silent drift** between API contract and fixtures (update fixtures whenever request DTO changes).

---

⬆️ _Back to top_  

