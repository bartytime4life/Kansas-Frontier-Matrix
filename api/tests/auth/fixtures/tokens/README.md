# 🔐 Token Fixtures for Auth Tests

> 📍 **Folder:** `api/tests/auth/fixtures/tokens/`  
> 🧪 **Purpose:** Stable, repeatable token inputs for the auth test suite (happy paths + denial paths)

KFM uses **token-based authentication (JWT)**: clients send `Authorization: Bearer <token>`, the backend validates **signature + expiry**, and authorization is enforced via **roles/levels claims** (including “operational access levels” for sensitive actions).[^kfm-auth]  
This folder exists to make those behaviors **easy to test** without relying on live login flows or external identity providers.

---

## 🧭 Why fixtures (instead of logging in for every test)?

- ⚡ **Fast tests** encourage frequent execution and make failures easier to pinpoint.[^tdd-fast]
- 🔁 **Deterministic inputs** prevent flaky failures (especially around time-based claims like `exp`).[^deterministic]
- 🤝 **CI-friendly**: CI runs the test suite on PRs; fixtures keep auth tests self-contained.[^kfm-ci][^ci-testing]

---

## ✅ What belongs here

- **Test-only JWT strings** (access tokens, refresh tokens, “bad” tokens)
- Small metadata files (optional), e.g. a manifest documenting claims/purpose
- Documentation (this README)

### 🚫 What must NOT belong here
- ❌ Production secrets / keys
- ❌ Real user tokens from production/staging
- ❌ Anything that could grant real access outside a test environment

---

## 📦 Suggested fixture set

> If the repo already has established names, keep those.  
> If you’re adding new fixtures, use a naming pattern like the table below to stay predictable.

| Fixture file (example) | Kind | Used for | Expectations |
|---|---|---|---|
| `access.user.jwt` | Access | Standard “authenticated user” requests | Should pass auth + include baseline role |
| `access.researcher.jwt` | Access | Researcher-only endpoints | Should include `roles: ["researcher"]` |
| `access.admin.jwt` | Access | Admin-only endpoints | Should include admin role/level claims |
| `access.service.jwt` | Access | Internal service-to-service calls | Should model “service token” behavior[^kfm-auth] |
| `refresh.user.jwt` | Refresh | Token refresh endpoint tests | Long-lived; only accepted by refresh endpoint[^kfm-refresh] |
| `expired.access.jwt` | Negative | Expired token rejection | `exp` intentionally in the past |
| `invalid.signature.jwt` | Negative | Signature verification failure | Token is tampered or signed with wrong key |
| `wrong.aud.jwt` | Negative | Audience/issuer validation | Wrong `aud` and/or `iss` |
| `missing.roles.jwt` | Negative | Authorization failure | No roles/levels claim present |

---

## 🧾 Token “claims contract” (what tests should assume)

JWT payloads should remain **small and intentional**. KFM authorization is role-driven and may also use operational access levels in claims.[^kfm-auth]

A **typical test access token payload** might look like:

```json
{
  "iss": "kfm-test",
  "aud": "kfm-api",
  "sub": "user:00000000-0000-0000-0000-000000000000",
  "roles": ["user"],
  "oal": ["read:field", "run:analysis"],
  "iat": 1700000000,
  "exp": 4102444800,
  "jti": "test-access-user-01"
}
```

### ⏱️ Time-based guidance (avoid flaky tests)
- Valid “happy path” tokens should use a **far-future `exp`**, *or* tests should freeze/mock time.
- Expired-token tests should use **intentionally expired `exp`** values.
- Keep `iat/exp` **stable** so test results are reproducible.[^deterministic]

---

## 🧪 How to use these tokens in tests

### Option A: Read raw JWT strings from files
Most fixtures should be **exactly one JWT string** (no JSON wrapper), ideally **no trailing newline**.

#### Node-style example (Jest/Vitest + fetch/supertest)
```ts
import fs from "node:fs";
import path from "node:path";

const token = fs.readFileSync(
  path.join(__dirname, "fixtures/tokens/access.user.jwt"),
  "utf8"
).trim();

await request(app)
  .get("/api/protected")
  .set("Authorization", `Bearer ${token}`)
  .expect(200);
```

#### Python-style example (pytest + client)
```py
from pathlib import Path

token = Path("api/tests/auth/fixtures/tokens/access.user.jwt").read_text().strip()
headers = {"Authorization": f"Bearer {token}"}

resp = client.get("/api/protected", headers=headers)
assert resp.status_code == 200
```

> 🧠 Reminder: the backend verifies **signature + expiry** on each request.[^kfm-auth]

---

## 🔁 Refresh token fixtures

KFM’s session management can use **short-lived access tokens** (e.g., ~1 hour) paired with a **refresh token mechanism** to extend sessions without forcing login again.[^kfm-refresh]  
For tests, this usually means:

- `refresh.user.jwt` is accepted by the refresh endpoint only
- The refresh endpoint returns a new access token (often with a fresh `exp`)
- Refresh tokens are treated as more sensitive and should be tightly scoped

---

## 🛠️ Updating / regenerating fixtures

Regenerate tokens when any of these change:
- Claim schema (roles/levels, subject format, issuer/audience)
- Signing algorithm / key material (even for tests)
- Auth middleware validation rules

### Recommended workflow
1. **Update the token payload template** (claims + timestamps)
2. **Re-sign** using **test-only** key material
3. Replace the affected `.jwt` fixture files
4. Run the auth test suite + CI checks

> 🧩 If you use pytest, keep shared fixtures (like token loaders) in `conftest.py` for global availability.[^pytest-fixtures]

---

## 🧯 Troubleshooting checklist

- **401 Unauthorized (unexpected):**
  - Token expired? (`exp`)
  - Wrong signing key/algorithm?
  - Wrong `iss`/`aud` enforcement?
- **403 Forbidden (unexpected):**
  - Roles/levels claim missing or mismatched
  - Endpoint requires admin-only operational access levels[^kfm-auth]
- **Tests suddenly failing “today”:**
  - A “valid” fixture token used a near-term `exp` (fix by far-future `exp` or mocked time)[^deterministic]

---

## 📚 Project references

- KFM technical blueprint (auth model, JWT, roles/levels): :contentReference[oaicite:0]{index=0}  
- Testing/fixtures patterns (pytest `conftest.py`, fixture ergonomics): :contentReference[oaicite:1]{index=1}  
- Reproducible testing + CI practices: :contentReference[oaicite:2]{index=2}  

---

## 🧷 Footnotes

[^kfm-auth]: KFM uses JWT-based auth; clients send `Authorization: Bearer <token>`, backend validates signature/expiry, and authorization checks role/level claims (including operational access levels and service-token cases).:contentReference[oaicite:3]{index=3}
[^kfm-refresh]: KFM describes access-token expiry and a refresh-token mechanism for keeping sessions alive without re-login (refresh tokens are long-lived and used for the refresh endpoint).:contentReference[oaicite:4]{index=4}
[^kfm-ci]: KFM describes CI running the test suite and checks on PRs/changes, keeping merges gated on green status. :contentReference[oaicite:5]{index=5}
[^tdd-fast]: Tests should be fast so developers run them frequently; otherwise they become less useful as guidance. :contentReference[oaicite:6]{index=6}
[^pytest-fixtures]: Pytest fixtures are commonly centralized in `conftest.py` to make them globally available and reduce “magic” surprises. :contentReference[oaicite:7]{index=7}
[^ci-testing]: Automated testing and CI are key quality practices (unit/integration/E2E + pipelines running on pushes/PRs). :contentReference[oaicite:8]{index=8}
[^deterministic]: Deterministic outputs are recommended for reproducibility (e.g., stable inputs/seeds/time assumptions). :contentReference[oaicite:9]{index=9}

