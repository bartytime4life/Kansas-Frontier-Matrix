<!--
📍 Path: api/src/auth/tests/fixtures/README.md
-->

# Auth Test Fixtures 🔐🧪

![scope](https://img.shields.io/badge/scope-auth-blue)
![tests](https://img.shields.io/badge/tests-fixtures-brightgreen)
![data](https://img.shields.io/badge/fixtures-deterministic-informational)
![security](https://img.shields.io/badge/security-no%20real%20secrets-critical)

This folder contains **reusable, deterministic test fixtures** for the `auth` module (users, tokens, keys, request/response bodies, and any mock identity-provider payloads). The goal is to keep tests:

- ✅ **Readable** (tests focus on behavior, not setup noise)
- ✅ **Stable** (no time-based flakiness, no random IDs unless seeded)
- ✅ **Safe** (no production secrets, no real PII)
- ✅ **Portable** (CI + local runs behave the same)

---

## What counts as a “fixture”? 🧩

Fixtures here are **test data artifacts** such as:

- **Static files**: JSON/YAML/Pem/JWK samples, golden responses, seed payloads.
- **Exportable objects**: reusable objects/constants used by tests.
- **Signing materials for tests only**: non-sensitive keys used to mint JWTs during tests.

> If a “fixture” needs logic (e.g., generating a JWT), prefer putting that logic in test helpers (e.g., `tests/utils/`) and keep this folder focused on **data**.

---

## Folder layout 📁

> Adjust this tree to match what’s actually in the folder—this is the **intended** structure.


```text
📁 api/src/auth/tests/fixtures/                       # 🧫 fixture root (data-only)
├─ 📝 README.md                                       # 👈 you are here
├─ 👥 users/                                          # 👤 test users & role scenarios
│  ├─ 👑 user_admin.json                               # admin principal (highest privilege)
│  ├─ 🧑‍🔬 user_researcher.json                         # researcher principal (scoped access)
│  └─ 👁️ user_viewer.json                              # read-only principal (least privilege)
├─ 🎟️ tokens/                                         # jwt/refresh token samples (valid/expired/tampered)
│  ├─ ✅ jwt_valid.txt                                 # signature/claims pass
│  ├─ ⛔ jwt_expired.txt                               # exp in the past (time-bound tests)
│  └─ 🔁 refresh_token_valid.txt                       # refresh token happy-path
├─ 🔐 keys/                                           # TEST-ONLY signing keys (NEVER production)
│  ├─ 🧿 jwk_private.json                              # private JWK (commit-safe test key)
│  ├─ 🪪 jwk_public.json                               # public JWK
│  └─ 🗝️ jwks.json                                     # JWKS bundle (kid rotation tests)
├─ 📦 requests/                                       # request bodies for auth endpoints
│  ├─ ✅ login_ok.json                                 # valid credentials payload
│  ├─ ❌ login_bad_password.json                       # wrong password payload
│  └─ ✅ refresh_ok.json                               # valid refresh flow payload
└─ 🧾 responses/                                      # golden/expected response payloads
   ├─ 🎉 login_ok.json                                 # expected success envelope
   ├─ 🔄 refresh_ok.json                               # expected refresh envelope
   └─ 🛑 error_unauthorized.json                        # expected 401 error envelope
```

---

## Fixture catalog 🗂️

| Category | What it supports | Examples |
|---|---|---|
| 👤 Users | role/permission tests, account states | `admin`, `researcher`, `viewer`, `disabled`, `locked` |
| 🎟️ Tokens | JWT validation/refresh flows | valid, expired, wrong signature, wrong `aud`, missing `sub` |
| 🔑 Keys | JWT signing / JWKS lookup tests | RSA/EC keys in JWK/JWKS format |
| 📦 Requests | endpoint contract tests | login payloads, refresh payloads, logout payloads |
| 🧾 Responses | snapshot/golden assertions | success responses, error envelopes |

---

## Usage examples 🧪

### Example A — import a JSON fixture (Node/TS style)

```ts
import adminUser from "./fixtures/users/user_admin.json";
import loginOk from "./fixtures/requests/login_ok.json";

// Example pseudo-usage
test("login succeeds for admin", async () => {
  const res = await login(loginOk);
  expect(res.user.id).toBe(adminUser.id);
});
```

### Example B — load a fixture file (Python/pytest style)

```py
import json
from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"

def load_json(relpath: str):
    return json.loads((FIXTURES / relpath).read_text())

def test_login_ok(client):
    payload = load_json("requests/login_ok.json")
    res = client.post("/auth/login", json=payload)
    assert res.status_code == 200
```

### Example C — stable token tests (time-safe) ⏱️

When testing JWT expiry logic, avoid relying on the real clock:

- Use a **fixed “now”** in tests (fake timers / time-freeze utilities).
- Prefer JWT fixtures with a far-future `exp` for “valid” tests.
- Prefer explicit, intentionally expired `exp` for “expired” tests.

---

## Conventions ✅

### 1) Deterministic IDs & timestamps
Use fixed values so snapshots and assertions don’t drift.

- IDs: `user_admin_0001`, `sess_0001`, `token_0001` (or UUIDs that never change)
- Timestamps: fixed ISO strings like `2025-01-01T00:00:00Z` (or epoch seconds)

### 2) Minimal payloads
Fixtures should contain **only fields needed** for the test(s).  
If you need a “full schema” payload, keep it in a dedicated file like `*_full.json`.

### 3) Name fixtures by behavior
Prefer naming by intent (what scenario it tests) instead of by endpoint.

- ✅ `jwt_expired.txt`
- ✅ `login_bad_password.json`
- ❌ `fixture1.json`

### 4) Never store real secrets 🛡️
- Test keys must be **non-production** and safe to commit.
- Never paste real JWTs from real environments.
- Emails/domains should be `.test` (e.g., `admin@example.test`).

---

## Adding a new fixture ✍️

Checklist:

- [ ] File name clearly states the scenario (`*_ok`, `*_invalid`, `*_expired`, etc.)
- [ ] Contains **no real secrets** / PII
- [ ] Values are deterministic (no random UUIDs unless seeded)
- [ ] If the fixture is shared across multiple tests, add a short note in the test(s) describing why
- [ ] If updating an existing fixture, update the corresponding golden response fixtures too

---

## Common gotchas 🧯

### “This JWT suddenly started failing”
Likely causes:
- Token `exp` reached (use far-future `exp` for “valid” fixtures)
- Clock drift in CI (freeze time where needed)
- Mismatched `kid` / JWKS lookup

### “Snapshot changed but logic didn’t”
- A fixture got updated (IDs/timestamps changed)
- Tests depend on fields that shouldn’t be asserted (assert only what matters)

---

## Related docs 🔗

- `../../README.md` (auth module overview, if present)
- `../../../../..` (repo root docs, if present)

> If you add a new auth flow (e.g., SSO/OIDC), please add a corresponding `providers/` or `oidc/` fixture set here to keep endpoint tests clean.

