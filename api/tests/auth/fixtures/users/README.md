# 👤 Auth Test User Fixtures (`api/tests/auth/fixtures/users`)

![scope](https://img.shields.io/badge/scope-tests-blue) ![area](https://img.shields.io/badge/area-auth-purple) ![data](https://img.shields.io/badge/type-fixtures-brightgreen)

This folder contains **deterministic user fixtures** used by the API auth test suite (login, RBAC, JWT claims, lockouts, MFA edge-cases, etc.). The goal is to make tests **repeatable**, **readable**, and **secure-by-default**.

> KFM’s security model is role-based (e.g., *farmer*, *researcher*, *admin*) and uses JWT for session management, with hashed passwords and optional MFA for sensitive accounts. :contentReference[oaicite:0]{index=0}

---

## 📦 What lives here

Typical contents you’ll find (or should add) in this directory:

```text
📂 api/tests/auth/fixtures/users/
├─ 📄 README.md                # you are here ✅
├─ 👤 admin.json               # admin account fixture
├─ 👤 researcher.json          # researcher account fixture
├─ 👤 farmer.json              # standard end-user fixture
├─ 👤 locked.json              # fixture representing locked/blocked login state
├─ 👤 mfa_admin.json           # admin w/ MFA enabled (if we test MFA)
└─ 📄 index.(ts|js|py)         # optional: exports/helpers to load fixtures
```

> If your repo currently uses a different naming scheme (e.g., `admin.user.json`, `user_admin.json`, `seed_users.ts`), keep it consistent—this README documents the **intent** and **contract**.

---

## 🎯 Fixture philosophy (why this exists)

- **Single source of truth** for auth-relevant user data.
- **Stable identifiers** so assertions don’t rely on DB auto-increments.
- **Readable scenarios**: fixtures should communicate *why* they exist.
- **Isolation-friendly**: fixtures should be easy to seed and tear down between tests (clean state).  
  Clean-architecture testing patterns strongly benefit from reusable fixtures and clear scoping/cleanup. :contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 🧭 Roles & authorization model (expected)

KFM’s documented authorization model is role/privilege based:

- **Admin**: manage users/settings; access everything
- **Researcher**: broad read access; limited admin actions
- **Farmer/User**: scoped access to their own data/resources

The backend should validate authorization per request against role/permission mappings. :contentReference[oaicite:3]{index=3}

**Fixtures in this folder should map cleanly to those roles** so tests can verify:
- role-gated endpoints
- forbidden vs unauthorized behavior
- JWT claims include expected roles

---

## 🧩 Fixture “contract” (recommended schema)

> Keep the fixture fields minimal but sufficient to test real auth flows.

### ✅ Required fields (recommended)
- `id` (string; UUID preferred)
- `email` (string; must be unique across fixtures)
- `roles` (string[]; e.g., `["admin"]`)
- `status` (string; e.g., `active | disabled | locked`)
- `password` **or** `passwordHash` (see below)

### 🔐 Password representation (choose one approach)
**Option A — Store `password` in fixture (preferred for readability)**  
Tests (or seed helpers) hash it using bcrypt/Argon2 at insert time. KFM expects strong password hashing (bcrypt/Argon2). :contentReference[oaicite:4]{index=4}

**Option B — Store `passwordHash` in fixture**  
Use if your seed pipeline doesn’t hash or you need deterministic hashes across languages.

### 🪪 JWT claim mapping (what tests usually assert)
KFM describes returning a signed JWT containing **user ID and roles**. :contentReference[oaicite:5]{index=5}

So tests often validate:
- `sub` or equivalent claim contains `id`
- `roles`/`scope` claim matches fixture roles
- expiration handling (token TTL)

---

## 🧪 Example fixtures

### 👑 `admin.json`
```json
{
  "id": "11111111-1111-1111-1111-111111111111",
  "email": "admin.fixture@kfm.local",
  "roles": ["admin"],
  "status": "active",
  "password": "AdminPass!234",
  "mfaEnabled": true
}
```

### 🧑‍🔬 `researcher.json`
```json
{
  "id": "22222222-2222-2222-2222-222222222222",
  "email": "researcher.fixture@kfm.local",
  "roles": ["researcher"],
  "status": "active",
  "password": "ResearchPass!234",
  "mfaEnabled": false
}
```

### 🌾 `farmer.json`
```json
{
  "id": "33333333-3333-3333-3333-333333333333",
  "email": "farmer.fixture@kfm.local",
  "roles": ["farmer"],
  "status": "active",
  "password": "FarmerPass!234"
}
```

### 🔒 `locked.json` (for brute-force / lockout tests)
```json
{
  "id": "44444444-4444-4444-4444-444444444444",
  "email": "locked.fixture@kfm.local",
  "roles": ["farmer"],
  "status": "locked",
  "password": "DoesNotMatter!234",
  "failedLoginCount": 10,
  "lockUntil": "2099-01-01T00:00:00.000Z"
}
```

> Lockout behavior is part of KFM’s security posture (“after several failed attempts, an account or IP is temporarily locked”). :contentReference[oaicite:6]{index=6}

---

## 🛠️ How fixtures are typically used

### Pattern 1 — Seed DB before tests
1. Start test DB (or transaction)
2. Insert users from fixtures
3. Run tests
4. Cleanup users / rollback transaction

This “seed → test → teardown” style aligns with fixture hygiene and clean test structure. :contentReference[oaicite:7]{index=7}

### Pattern 2 — Stub auth provider / user repo (unit tests)
- Load fixture user object
- Mock repository method: `getUserByEmail(email) -> fixtureUser`
- Assert use-case behavior (no DB required)

---

## 🧰 Suggested helper API (if you add `index.ts/js/py`)

### TypeScript / JavaScript (example)
```ts
import admin from "./admin.json";
import farmer from "./farmer.json";

export const userFixtures = { admin, farmer };
```

### Python (example)
```py
import json
from pathlib import Path

ROOT = Path(__file__).parent

def load_user(name: str) -> dict:
    return json.loads((ROOT / f"{name}.json").read_text(encoding="utf-8"))
```

---

## ➕ Adding a new user fixture

1. **Pick a scenario** (what test needs it?)
   - example: `disabled`, `pending_email_verification`, `mfa_required`, `no_roles`
2. **Create a file** named after the scenario
   - `disabled.json`, `mfa_admin.json`, etc.
3. **Use stable IDs**
   - UUIDs only; never depend on DB auto-increment.
4. **Use safe local emails**
   - `*.fixture@kfm.local` (avoid real domains)
5. **Keep it minimal**
   - Add only fields that tests assert on.

---

## 🧯 Security & hygiene rules (non-negotiable)

- ✅ **Never** put real credentials, API keys, or production-like secrets in fixtures.
- ✅ Fixture passwords are **test-only** and must not match any real password.
- ✅ Don’t encode JWT signing secrets here—keep those in test config/env.
- ✅ If MFA is tested, use a deterministic test method (stubbed OTP, fixed seed, etc.).
- ✅ Keep fixtures aligned with documented auth architecture (JWT + roles + hashed passwords). :contentReference[oaicite:8]{index=8}

---

## 🧷 Troubleshooting

- **Login tests fail after adding a fixture**
  - Confirm `email` uniqueness and that seeding hashes `password` (if you use plaintext).
- **RBAC tests failing**
  - Confirm endpoint permission logic expects `roles` claim shape that matches what token builder emits.
- **Flaky tests**
  - Ensure DB cleanup happens per test (or use transaction rollback). :contentReference[oaicite:9]{index=9}

---

## 📚 References (project grounding)

- KFM security/auth model: JWT sessions, roles, password hashing, lockouts, MFA. :contentReference[oaicite:10]{index=10}
- Clean-architecture fixture hygiene: reusable fixtures, controlled setup/teardown patterns. :contentReference[oaicite:11]{index=11}:contentReference[oaicite:12]{index=12}

