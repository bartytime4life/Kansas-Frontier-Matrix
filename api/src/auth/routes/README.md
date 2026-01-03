# 🔐 Auth Routes (`api/src/auth/routes/`)

![Auth](https://img.shields.io/badge/Auth-JWT%20%2B%20Refresh%20Tokens-blue)
![Security](https://img.shields.io/badge/Security-bcrypt%20%7C%20Argon2-success)
![Access](https://img.shields.io/badge/Access-RBAC%20%2B%20ACL-orange)
![Ops](https://img.shields.io/badge/Ops-Operational%20Access%20Levels-purple)
![Audit](https://img.shields.io/badge/Audit-Logging-informational)

> 🧭 This folder defines **HTTP routes** for authentication + authorization in the KFM API.
> Keep routes **thin**, push logic into **controllers/services**, and enforce security **consistently**.

---

## 📌 What belongs in this folder?

✅ **Do** (Route Layer Responsibilities)
- Define route paths + HTTP methods (REST-ish)
- Apply **validation** (body/query/params)
- Attach **auth middleware** (JWT verification) and **role/ACL guards**
- Apply **rate limiting / lockout hooks** where relevant (e.g., login)
- Call controllers/services and return **sanitized** responses
- Emit **audit events** for security-sensitive actions

🚫 **Don’t**
- Implement business logic here (keep it in `services/` / `use-cases/`)
- Query the DB directly from routes
- Leak security details in error messages (user existence, token reasons, etc.)

---

## 🧱 Clean Architecture wiring (the “thin routes” rule)

A typical request flow (framework-agnostic, same idea for Express/Fastify/etc.):

```text
🌐 HTTP Request
  → 🧭 Route (this folder)
    → ✅ Validate
    → 🛡️ Auth Guard (JWT)
    → 🎚️ Role/ACL Guard
    → 🎯 Controller
      → 🧠 Service / Use-Case
        → 🗄️ Repository / DB Adapter
  ← 📦 HTTP Response
```

> 🧩 The route layer may import controllers/services/models, but the inner layers **must not** import routes.

---

## 🔑 Token model (KFM standard)

### ✅ Access Token (JWT)
- Sent on each request:
  - `Authorization: Bearer <accessToken>`
- Short-lived (example target: ~1 hour)

### ♻️ Refresh Token
- Long-lived, stored **securely**
- **Only** sent to the refresh endpoint
- Used to mint a new access token without forcing re-login

> ⚠️ **Never** send refresh tokens to non-refresh endpoints. Keep them scoped.

---

## 🧾 Route inventory (expected endpoints)

> These are the “canonical” auth capabilities for KFM. Your concrete paths may vary — keep the **semantics** consistent.

| Area | Method | Route (example) | Auth? | Purpose |
|------|--------|------------------|-------|---------|
| Login | `POST` | `/auth/login` | ❌ | Verify credentials, return access token (+ refresh token mechanism) |
| Refresh | `POST` | `/auth/refresh` | ❌* | Exchange refresh token for new access token |
| Logout | `POST` | `/auth/logout` | ✅ | Invalidate refresh token / end session |
| Current user | `GET` | `/auth/me` | ✅ | Return current user profile + roles/claims |
| Register (optional) | `POST` | `/auth/register` | ❌ | Create account (if not using external IdP) |
| Forgot password | `POST` | `/auth/password/forgot` | ❌ | Start reset flow, email one-time token |
| Reset password | `POST` | `/auth/password/reset` | ❌ | Complete reset using one-time token |
| MFA challenge (optional) | `POST` | `/auth/mfa/challenge` | ❌/✅ | Issue OTP/email challenge (admin/high-sensitivity accounts) |
| MFA verify (optional) | `POST` | `/auth/mfa/verify` | ❌/✅ | Verify OTP/email code and finalize auth |

\* Refresh typically does **not** require an access token; it relies on the refresh token itself.

---

## 🛡️ Security baseline (non-negotiables)

### 🔒 Password handling
- Passwords are **hashed** (bcrypt or Argon2)
- Enforce complexity rules
- Password reset uses **email confirmation + one-time token**

### 🚦 Abuse resistance
- Rate-limit login attempts
- Temporarily lock account or IP after repeated failures
- Alert admins on suspicious activity (where applicable)

### 🧑‍⚖️ Authorization
- Enforce RBAC + ACL checks:
  - Example roles: **Admin**, **Researcher**, **Farmer/User**
- Protect “sensitive” operations with **Operational Access Levels** (admin-only, internal staff roles, etc.)
- Return correct status codes:
  - `401 Unauthorized` → missing/invalid token
  - `403 Forbidden` → valid token, insufficient privileges

### 🧾 Audit logging
Log all security-sensitive actions:
- login/logout
- password reset initiation/completion
- role/permission changes
- data modifications (POST/PUT/PATCH/DELETE)

### 🔐 Transport & storage security
- Use HTTPS/TLS for all network communication
- Encrypt data at rest (including backups)

---

## 🧰 Conventions used by routes here

### ✅ Validation
- Prefer schema-based validation (e.g., Zod/Joi/Yup) over ad-hoc checks
- Reject invalid requests with `400` / `422` and a consistent error shape

### ✅ Error shape (recommended)
```json
{
  "ok": false,
  "error": {
    "code": "AUTH_INVALID_CREDENTIALS",
    "message": "Invalid credentials"
  }
}
```

### ✅ Response shape (recommended)
```json
{
  "ok": true,
  "data": {
    "accessToken": "<jwt>",
    "expiresIn": 3600,
    "user": {
      "id": "user_123",
      "roles": ["researcher"]
    }
  }
}
```

> 🧼 Never return password hashes, reset tokens, or internal permission graphs in responses.

---

## 📂 Expected folder layout

> Your exact filenames may differ, but keep responsibilities split.

```text
📦 api/
└─ 📂 src/
   └─ 📂 auth/
      ├─ 📂 routes/        👈 you are here
      │  ├─ 📄 README.md
      │  ├─ 📄 index.ts            # exports router(s)
      │  ├─ 📄 login.routes.ts     # /auth/login
      │  ├─ 📄 refresh.routes.ts   # /auth/refresh
      │  ├─ 📄 password.routes.ts  # forgot/reset flows
      │  └─ 📄 mfa.routes.ts       # optional MFA
      ├─ 📂 controllers/    # HTTP → use-case mapping
      ├─ 📂 services/       # business logic / use-cases
      ├─ 📂 middleware/     # auth guards, rate limiters
      └─ 📂 models/         # user / claims / token DTOs
```

---

## ➕ Adding a new auth-protected endpoint

1. **Define** the route + method (keep naming consistent)
2. Add **schema validation**
3. Apply `requireAuth` (JWT verify)
4. Apply `requireRole` / `requireACL` / `requireAccessLevel`
5. Call the controller/service
6. Add **audit logging** if the action is sensitive
7. Write tests:
   - success case
   - missing token → `401`
   - wrong role → `403`
   - invalid payload → `400/422`
   - abuse scenario if relevant (rate limit / lockout)

---

## 🧪 Testing checklist

✅ Unit tests
- Validators accept/reject correct payloads
- Guards enforce 401/403 properly
- Controller integration with service (mock service)

✅ Integration tests
- Login flow returns tokens and correct expiry
- Refresh token rotates / renews access token as expected
- Password reset issues one-time token and allows reset
- MFA flow (if enabled) requires second factor for admin accounts

---

## 🧯 Common gotchas

- **Refresh token leakage**: never log it; never send it to non-refresh endpoints
- **User enumeration**: password reset endpoints should respond safely (avoid “email not found”)
- **Incorrect 401 vs 403**: keep semantics strict
- **Role drift**: always read roles/claims from token + server-side source of truth (when needed)
- **Over-trusting JWT**: validate signature, expiry, and audience/issuer if used

---

## 🔗 Related areas
- `api/src/auth/middleware/` → auth guards & rate limiting
- `api/src/auth/services/` → credential verification, token minting/rotation, MFA logic
- `api/src/auth/models/` → user claims / DTOs
- `api/src/*/routes/` → follow the same “thin route” conventions

---

> ✅ Goal: predictable, secure auth endpoints that stay maintainable as KFM grows. 🚀

