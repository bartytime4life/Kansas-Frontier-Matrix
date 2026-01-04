<!--
📍 Path: api/src/auth/tests/fixtures/users/README.md
-->

# 🧪 Auth Test User Fixtures

![scope](https://img.shields.io/badge/scope-tests-blue)
![module](https://img.shields.io/badge/module-auth-purple)
![fixtures](https://img.shields.io/badge/fixtures-users-orange)
![data](https://img.shields.io/badge/data-fake%20only-success)

> [!IMPORTANT]
> These are **test-only** users meant for **repeatable auth/authorization tests** ✅  
> Use **fake identities** (`.test` emails), **deterministic IDs**, and **hashed passwords**. Never add real PII or production secrets.

---

## 🗂️ You are here

```text
📁 api/
 └─ 📁 src/
    └─ 📁 auth/
       └─ 📁 tests/
          └─ 📁 fixtures/
             └─ 📁 users/   👈
                ├─ 📄 README.md
                └─ 📄 (fixture files live next to this README)
```

---

## 🎯 What this folder is for

This folder exists to provide a **single source of truth** for users referenced across auth tests, including:

- ✅ Login success/failure cases  
- ✅ Role-based access control (RBAC) checks (admin/researcher/user/etc.)  
- ✅ Account state edge cases (locked/disabled/unverified)  
- ✅ Security flows (MFA-required accounts, rate-limit/lockout scenarios)  
- ✅ Token claims validation (roles, subject/user id, expiry)

The goal is **confidence without fragility**: tests should be readable, stable, and easy to extend.

---

## 🧠 Golden rules (please follow)

### ✅ Do
- Use **stable IDs** (UUIDs) so tests can reference users reliably.
- Use **fake emails** like `name@kfm.test` or `name@example.test`.
- Store **password hashes**, not plaintext passwords.
- Keep fixtures **minimal**: only fields needed by tests.
- Keep fixtures **deterministic**: avoid randomness unless seeded.
- Prefer generating **JWTs during tests** (less brittle than static tokens).

### ❌ Don’t
- Don’t commit real emails, real names, phone numbers, or anything resembling production dumps.
- Don’t embed production secrets (JWT signing keys, real refresh tokens, etc.).
- Don’t “share” one fixture user across unrelated tests if it makes test intent unclear.

---

## 👤 Fixture catalog

> [!NOTE]
> This table is a **recommended baseline**. If your fixture set differs, update the table so it matches reality.

| Key 🔑 | Typical Roles 🎭 | Status 🧯 | Used to test 🧪 |
|---|---|---|---|
| `admin` | `["admin"]` | active | Admin-only endpoints, user management |
| `researcher` | `["researcher"]` | active | Elevated read access without admin powers |
| `farmer` / `user` | `["user"]` or `["farmer"]` | active | Standard permissions, ownership rules |
| `locked_user` | `["user"]` | locked | Lockout handling, brute-force mitigation |
| `disabled_user` | `["user"]` | disabled | Access denied even with correct password |
| `unverified_user` | `["user"]` | pending | Email verification gating |
| `mfa_admin` | `["admin"]` | active + MFA | MFA challenge flow / step-up auth |
| `service_account` | `["service"]` | active | Service-to-service auth / internal calls |

---

## 🧾 Recommended user fixture shape

> [!TIP]
> Keep the “fixture contract” close to your domain model, but don’t be afraid to add test-only fields (like `fixtureKey`) if it improves clarity.

```json
{
  "id": "0d3b2fb3-2b2d-4c2f-8c7c-2c9a9f3a9a01",
  "email": "admin@kfm.test",
  "displayName": "Admin (Fixture)",
  "passwordHash": "$2b$10$REDACTED_HASH",
  "roles": ["admin"],
  "status": "active",
  "mfa": {
    "enabled": false
  },
  "createdAt": "2026-01-01T00:00:00.000Z",
  "updatedAt": "2026-01-01T00:00:00.000Z"
}
```

### 🔐 About passwords in fixtures
- Store **only**: `passwordHash`
- Keep any “known plaintext password” in **test helpers** (or in this README examples), not in fixture JSON/TS.

Example doc-only passwords (choose one project-wide and keep it consistent):
- `TestPassword!123`
- `KFM_Test_1234!`

---

## 🪪 JWT expectations (auth tests)

Most auth tests will follow this pattern:

1) seed user fixtures into a test database  
2) `POST /auth/login` with `{ email, password }`  
3) receive `{ accessToken, refreshToken? }`  
4) call protected endpoints with `Authorization: Bearer <accessToken>`

Typical claim expectations:
- `sub` (subject) or equivalent → user id
- `roles` (or permissions claim) → fixture roles
- `exp` / expiry → should be valid for test duration

> [!WARNING]
> Avoid storing long-lived static JWT strings in fixtures unless your tests freeze time. Tokens expire and will create noisy failures.

---

## 🧪 How tests should use these fixtures

Below is **intentionally generic** (works conceptually for Jest/Vitest/Mocha + Supertest or similar).

```ts
// pseudo-example (adjust import paths + helpers to match the repo)
import { users } from "./index";           // exports fixture objects
import { seedUsers, resetDb } from "../../helpers/db";
import { loginAs } from "../../helpers/auth";
import request from "supertest";

beforeEach(async () => {
  await resetDb();
  await seedUsers(Object.values(users));
});

test("admin can access admin route", async () => {
  const token = await loginAs(users.admin); // uses admin.email + known password
  const res = await request(app)
    .get("/api/admin/stats")
    .set("Authorization", `Bearer ${token}`);

  expect(res.status).toBe(200);
});

test("regular user cannot access admin route", async () => {
  const token = await loginAs(users.user);
  const res = await request(app)
    .get("/api/admin/stats")
    .set("Authorization", `Bearer ${token}`);

  expect(res.status).toBe(403);
});
```

---

## ➕ Adding a new fixture user

### 1) Pick a clear fixture key 🏷️
Good:
- `analyst_readonly`
- `user_with_expired_password`
- `mfa_admin`

Avoid:
- `user2`
- `temp`
- `bob`

### 2) Choose deterministic identifiers 🧷
- Use a UUID and **never change it** once referenced in tests.
- Prefer `.test` emails.

### 3) Generate a password hash 🔒

Pick whatever the auth module uses (commonly **bcrypt** or **Argon2**). Example snippets:

<details>
<summary><strong>🧰 Bcrypt (Node) example</strong></summary>

```bash
node -e "const bcrypt=require('bcryptjs'); console.log(bcrypt.hashSync('TestPassword!123', 10));"
```
</details>

<details>
<summary><strong>🧰 Argon2 (Node) example</strong></summary>

```bash
node -e "const argon2=require('argon2'); argon2.hash('TestPassword!123').then(console.log)"
```
</details>

> [!NOTE]
> Keep the hash cost reasonable for tests. If hashing is too slow, tests will feel “sticky”.

### 4) Add the user to the fixture export 🧩
- If you maintain an `index.ts`, add the new user there.
- Keep exports grouped (base users vs edge-case users).

### 5) Add a test that uses it ✅
If it’s worth a fixture, it’s worth at least one test.

---

## 🧼 Test hygiene & cleanup

> [!TIP]
> Always reset state between tests. Auth tests are easy to accidentally couple through shared DB state (e.g., failed login counters, lockout flags, refresh token tables).

Recommended approaches:
- Transaction per test (rollback after)
- Truncate tables between tests
- Recreate schema in a disposable DB container

---

## 🛡️ Security + privacy guardrails

- 🚫 No real user data, ever  
- 🧪 Use test domains (`.test`)  
- 🔑 Keep secrets out of fixtures (JWT keys, API keys, real refresh tokens)  
- 🧾 Prefer generating tokens during tests so expiry/claims remain consistent  
- 🧯 Include edge-case users intentionally (locked/MFA/disabled) to harden auth flows

---

## 🧭 Troubleshooting

**“Login works locally but fails in CI”**
- Check that fixture password hashing cost/settings match CI environment.
- Ensure the test database is fully reset between tests (lockout counters can persist).

**“JWT expired”**
- Don’t store static JWTs.
- Generate tokens during tests or freeze time.

**“Role checks are flaky”**
- Ensure your fixtures’ `roles` (and claim mapping) are consistent.
- Keep role naming stable (e.g., `admin` vs `ADMIN`).

---

## ✅ When to edit this README

Update this file when you:
- add/remove a fixture user
- change the user schema used in tests
- introduce new auth states (MFA, lockout policy, refresh token changes)
- change how tokens are minted/validated in tests

📌 Keeping this README accurate makes auth tests *much* easier to maintain. ✨

