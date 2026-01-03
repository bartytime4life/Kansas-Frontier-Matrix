# 🔐 Auth Test Suite — `api/src/auth/tests`

![Auth](https://img.shields.io/badge/security-authentication%20%26%20authorization-2f2f2f)
![Tests](https://img.shields.io/badge/tests-unit%20%7C%20integration%20%7C%20security%20regression-2f2f2f)
![Determinism](https://img.shields.io/badge/testing-deterministic%20%26%20repeatable-2f2f2f)
![CI](https://img.shields.io/badge/CI-required%20gates-2f2f2f)

> [!IMPORTANT]
> Auth is a **trust boundary**. These tests exist to prevent regressions that can leak data, escalate privileges, or silently weaken security. ✅

---

## 🎯 What this folder covers

This directory contains automated tests for the API’s authentication + authorization layer, including:

- ✅ **Login** (credential verification, token issuance)
- ✅ **JWT access tokens** (claims, expiration, signature handling)
- ✅ **Refresh tokens** (rotation / refresh flow behavior)
- ✅ **Role-based access control** (ACL / roles → permissions mapping)
- ✅ **Password security** (hash + verify, reset flow, complexity rules)
- ✅ **Brute-force protections** (rate limiting / lockout logic)
- ✅ **(Optional) MFA** flows for privileged users
- ✅ **Audit logging** for security-sensitive actions (login/logout/permission changes)

> [!NOTE]
> KFM security expectations include JWT-based sessions, refresh tokens, hashed passwords (bcrypt/Argon2), lockout protections, optional MFA, and audit logging. This test suite is structured to verify those expectations continuously in CI. 🧭

---

## 🧱 Test philosophy (quick rules)

- 🧪 **Prefer unit tests** for pure logic (token creation, claim validation, role checks).
- 🌐 **Use integration tests** to validate HTTP/API behavior end-to-end (status codes, headers, cookies, JSON shape).
- 🧯 **Security regressions get permanent tests**: once a bug is found, it becomes a test that can never be removed without a replacement.
- 🔁 **Deterministic by default**: no real network calls, no real email delivery, no reliance on wall-clock time.

---

## 📁 Suggested folder layout

> If your repo already has a structure, keep it — but try to match this naming style for consistency.

```text
📦 api/
└─ 📂 src/
   └─ 📂 auth/
      └─ 📂 tests/
         ├─ 📄 README.md ✅ (you are here)
         ├─ 📂 unit/ 🧩
         │  ├─ token.service.spec.ts
         │  ├─ password.service.spec.ts
         │  ├─ roles.spec.ts
         │  └─ lockout.spec.ts
         ├─ 📂 integration/ 🌐
         │  ├─ login.spec.ts
         │  ├─ refresh.spec.ts
         │  ├─ logout.spec.ts
         │  ├─ reset-password.spec.ts
         │  └─ rbac.spec.ts
         ├─ 📂 fixtures/ 🧰
         │  ├─ users.ts
         │  └─ tokens.ts
         └─ 📂 helpers/ 🛠️
            ├─ makeApp.ts
            ├─ authHeader.ts
            ├─ freezeTime.ts
            └─ testDb.ts
```

---

## ▶️ Running the tests

### Option A — Node/TypeScript (common for `api/src/...`)

```bash
# from api/ (or repo root, depending on your setup)
npm test

# run only auth tests (Jest-style path filter)
npm test -- src/auth/tests

# watch mode (if available)
npm test -- --watch src/auth/tests
```

### Option B — Python (if this service is Python-based)

```bash
pytest -q api/src/auth/tests
pytest -q api/src/auth/tests -k "login or token or rbac"
```

> [!TIP]
> If you’re unsure which runner is configured, check the API service root for `package.json` scripts or a `pyproject.toml/requirements.txt` test section.

---

## 🔧 Test environment & config

Auth tests typically need **safe, test-only** configuration values:

- `JWT_SECRET` / signing key (test-only)
- `ACCESS_TOKEN_TTL_SECONDS` (or equivalent)
- `REFRESH_TOKEN_SECRET` (test-only)
- `REFRESH_TOKEN_TTL_SECONDS` (or equivalent)
- `PASSWORD_HASH_ALGO` (bcrypt/argon2) *(or derived from implementation)*
- `AUTH_LOCKOUT_THRESHOLD`, `AUTH_LOCKOUT_WINDOW`, etc.
- `AUDIT_LOG_SINK=memory` *(recommended for tests)*

### ✅ Recommended: `.env.test` (never commit real secrets)

```bash
# Example ONLY — keep test secrets non-production
JWT_SECRET="test-only-secret"
REFRESH_TOKEN_SECRET="test-only-refresh-secret"
ACCESS_TOKEN_TTL_SECONDS="3600"
REFRESH_TOKEN_TTL_SECONDS="1209600"
AUDIT_LOG_SINK="memory"
```

> [!WARNING]
> Never reuse production secrets in tests. Never print tokens or passwords to CI logs.

---

## 🧰 Fixtures & helpers (how we keep tests clean)

Use fixtures/factories so tests read like stories:

- `createUser({ role: 'admin' })`
- `loginAs('researcher')`
- `makeAuthHeader(accessToken)`
- `freezeTime('2026-01-03T00:00:00Z')`
- `expectAuditLog({ action: 'login', userId })`

### Time control is non-negotiable ⏱️
Anything involving expiration (JWT TTL, lockout windows, reset tokens) must use a **mocked clock**.

---

## ✅ Coverage checklist (auth + security)

Use this as the “definition of done” before merging auth changes.

| Area | What must be true | Unit | Integration |
|------|--------------------|:---:|:----------:|
| 🔑 Login | Valid credentials → access token issued | ✅ | ✅ |
| 🔑 Login | Invalid credentials → no token; correct error response | ✅ | ✅ |
| 🪪 JWT Claims | Token contains required claims (user id, roles, etc.) | ✅ | ⬜ |
| 🪪 JWT Expiry | Expired access token is rejected | ✅ | ✅ |
| 🔁 Refresh | Refresh returns new access token; old access token still expires normally | ✅ | ✅ |
| 🔁 Refresh | Refresh token reuse/rotation rules enforced *(if implemented)* | ✅ | ✅ |
| 🧑‍⚖️ RBAC | Role → permission mapping is correct (ACL) | ✅ | ✅ |
| 🚫 Privilege Escalation | User cannot access admin endpoints | ✅ | ✅ |
| 🔐 Password Hashing | Hash + verify works; never stores plaintext | ✅ | ⬜ |
| ✉️ Password Reset | Reset flow uses one-time token (email stubbed) | ✅ | ✅ |
| 🧱 Lockout / Throttle | Repeated failures trigger lockout/throttle | ✅ | ✅ |
| 🔒 MFA (optional) | MFA required for privileged users if enabled | ✅ | ✅ |
| 🧾 Audit Logging | Login/logout/permission changes produce audit log events | ✅ | ✅ |

> [!NOTE]
> If your implementation does not include a row yet (e.g., MFA), keep the tests skipped/placeholder and label it clearly so we don’t forget it later. 🧷

---

## 🧪 Writing a new auth test (golden path)

1. 🧭 **Pick the right level**
   - Pure function / service logic → `unit/`
   - HTTP boundary / middleware behavior → `integration/`

2. 🧩 **Use fixtures**
   - Don’t hand-roll users/tokens in every test.

3. 🧯 **Assert on security outcomes**
   - Status codes, headers, cookie flags, token contents (claims), permission checks.
   - Ensure failures do not leak sensitive details.

4. 🧾 **Add an audit expectation** (if the action is security-sensitive)

5. 🧹 **Keep it deterministic**
   - Freeze time, stub randomness, stub external IO.

---

## 🛡️ Security regression patterns we always test

### 1) “Missing auth header” should fail closed
- No token → **401** (or your standard)
- No user context should be constructed

### 2) “Valid token, wrong role” should be denied
- Token valid but insufficient privileges → **403**

### 3) “Token tampering” must be rejected
- Modified signature / payload → **401**
- No partial acceptance

### 4) “Refresh token theft” should be limited (if supported)
- Rotation / reuse detection should revoke or deny as designed

---

## 🧯 Troubleshooting (fast fixes)

<details>
<summary><strong>❌ Tests failing only in CI</strong></summary>

- Check for hidden dependencies on local `.env`
- Ensure DB/services are started in CI (or mocked)
- Ensure tests don’t rely on timezone/local time
</details>

<details>
<summary><strong>❌ Flaky expiry tests</strong></summary>

- Freeze time
- Avoid `setTimeout` sleeps — advance the mocked clock instead
</details>

<details>
<summary><strong>❌ Random failures around rate limiting / lockout</strong></summary>

- Reset in-memory counters between tests
- Use isolated test users / isolated IP identifiers
</details>

---

## 🤝 Contribution notes

- Keep PRs small and reviewable 🧩
- Any auth behavior change should come with:
  - ✅ tests
  - ✅ updated API contract docs (if endpoint changes)
  - ✅ clear migration notes if the change affects clients

> [!TIP]
> If you’re adding a new endpoint or changing auth responses, treat the API contract as “first-class” and ensure tests lock the behavior down.

---

## 📚 Related docs (in-repo)

- `../../../../docs/MASTER_GUIDE_v13.md` — repo structure & validation culture 📘  
- `../../../../SECURITY.md` — security policy & disclosure 🔒  
- `../../../../CONTRIBUTING.md` — PR + CI expectations 🧑‍💻

---
_✨ Goal: tests that make auth boring — because boring auth is secure auth._

