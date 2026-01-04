# 🔐 JWT Claim Fixtures (Auth Tests)

![scope:tests](https://img.shields.io/badge/scope-tests-blue) ![module:auth](https://img.shields.io/badge/module-auth-purple) ![artifact:fixtures](https://img.shields.io/badge/artifact-fixtures-orange) ![security:no-secrets](https://img.shields.io/badge/security-no%20secrets-brightgreen)

> 🧪 **Deterministic JWT claim payloads** used by authentication + authorization tests.  
> 📍 Location: `api/src/auth/tests/fixtures/tokens/claims/`

---

## 📚 Contents

- [🎯 What lives here](#-what-lives-here)
- [🗂️ Folder layout](#️-folder-layout)
- [🧾 Claim contract (shape)](#-claim-contract-shape)
- [🧠 How fixtures become tokens](#-how-fixtures-become-tokens)
- [✅ Naming conventions](#-naming-conventions)
- [🧪 Using a claim fixture in tests](#-using-a-claim-fixture-in-tests)
- [🔒 Security & hygiene rules](#-security--hygiene-rules)
- [➕ Adding a new fixture](#-adding-a-new-fixture)
- [🧯 Troubleshooting](#-troubleshooting)

---

## 🎯 What lives here

This folder contains **JWT “claims” / payload fixtures** (the JSON object that becomes the token payload).

KFM uses **token-based authentication** (JWT-style): clients send tokens via `Authorization: Bearer <token>`, the backend validates **signature + expiry**, then enforces **authorization** using the token’s **roles** and **operational access levels** (for sensitive actions). ✅

These fixtures exist so tests can cover:

- ✅ **Happy paths** (valid roles/levels)
- 🚫 **Negative paths** (missing/invalid claims, expired tokens, wrong audience/issuer, etc.)
- 🧪 **Permission boundaries** (admin-only endpoints, restricted resources, etc.)

> 🧾 **Contract-first reminder:** Claim shapes behave like a “boundary contract” between client ↔ auth middleware ↔ endpoints.  
> If you change the claim schema, treat it like an API contract change (update types/schema + tests together).

---

## 🗂️ Folder layout

> This is the **recommended** structure. Your repo may flatten this into a single folder (that’s fine—just keep names consistent).

```text
📦 api/src/auth/tests/fixtures/tokens/
└─ 🧾 claims/
   ├─ ✅ valid/                  # Good claim payloads (role/level scenarios)
   │  ├─ user.access.json
   │  ├─ researcher.access.json
   │  ├─ admin.access.json
   │  └─ service.access.json
   ├─ 🚫 invalid/                # Bad claim payloads (negative testing)
   │  ├─ expired.access.json
   │  ├─ missing-roles.access.json
   │  ├─ wrong-aud.access.json
   │  └─ malformed.json
   └─ 📄 README.md               # ← you are here
```

---

## 🧾 Claim contract (shape)

A JWT payload is **just JSON**, but the auth layer expects certain fields to exist and to be well-typed.

Use this table as a **practical contract** when adding fixtures. If the project has a canonical `JwtClaims` type / schema, **it wins**—keep fixtures aligned with it.

| Claim | Type | Example | Why it matters |
|------|------|---------|----------------|
| `sub` | `string` | `"0b3b2c9a-..."` | Subject ID (user/service identifier) |
| `iss` | `string` | `"kfm-api"` | Issuer check (prevents tokens from other issuers) |
| `aud` | `string \| string[]` | `"kfm-ui"` | Audience check (token intended for this API/client) |
| `iat` | `number` | `1700000000` | Issued-at (useful for debugging + some validation flows) |
| `exp` | `number` | `1700003600` | Expiry (auth middleware must reject expired tokens) |
| `jti` | `string` | `"f02c..."` | Token ID (revocation / tracking / replay prevention patterns) |
| `typ` | `string` | `"access"` / `"refresh"` / `"service"` | Token “kind” (access vs refresh vs internal service) |
| `roles` | `string[]` | `["user"]` / `["admin"]` | Coarse authorization (role checks in middleware/decorators) |
| `levels` | `string[] \| number` | `["adminOnly"]` or `3` | Operational access levels for sensitive actions |
| `scope` *(optional)* | `string[]` / `string` | `["fields:read"]` | Fine-grained permissions (if used) |
| `orgId` *(optional)* | `string` | `"org_kansas_001"` | Multi-tenant authorization boundaries (if used) |

> 💡 **Fixture tip:** If tests are getting flaky due to time, prefer generating `iat/exp` at runtime in a signing helper (and only hardcode time for fixtures specifically testing expiry).

---

## 🧠 How fixtures become tokens

```mermaid
flowchart LR
  A[🧾 claims/*.json<br/>payload fixtures] --> B[🧰 signTestToken()<br/>adds iat/exp if needed<br/>signs with test key]
  B --> C[📨 HTTP Request<br/>Authorization: Bearer &lt;token&gt;]
  C --> D[🛡️ auth middleware<br/>verify signature + exp<br/>read roles/levels]
  D --> E[🧭 route / controller<br/>permission checks]
  E --> F[✅ test assertions]
```

---

## ✅ Naming conventions

Pick **one** convention and stick to it.

### Option A: Subfolders (recommended)

- `valid/<persona>.<tokenType>.json`
- `invalid/<reason>.<tokenType>.json`

Examples:
- `valid/admin.access.json`
- `valid/user.access.json`
- `invalid/expired.access.json`
- `invalid/missing-roles.access.json`

### Option B: Flat files (works fine)

- `valid__admin__access.json`
- `invalid__expired__access.json`

> 🧭 Rule of thumb: Names should answer **“who?”** and **“what kind of token?”** and (for negatives) **“what failure?”**.

---

## 🧪 Using a claim fixture in tests

Most tests follow the same pattern:

1. Load a **claims fixture** (JSON payload)
2. Use a **test signer helper** to create a JWT (never commit real secrets)
3. Attach token to request as `Authorization: Bearer <token>`
4. Assert on status + response + permission behavior

<details>
<summary>🟦 Example (TypeScript/Jest-style pseudocode)</summary>

```ts
import adminAccessClaims from "./claims/valid/admin.access.json";
import { signTestToken } from "../helpers/signTestToken";

it("allows admin-only endpoint for admin token", async () => {
  const token = signTestToken(adminAccessClaims);

  await request(app)
    .post("/api/admin/reload-base-data")
    .set("Authorization", `Bearer ${token}`)
    .expect(200);
});
```

</details>

<details>
<summary>🐍 Example (Python/pytest-style pseudocode)</summary>

```py
from tests.fixtures.tokens.helpers import sign_test_token
from tests.fixtures.tokens.claims.valid import admin_access_claims

def test_admin_endpoint_allows_admin(client):
    token = sign_test_token(admin_access_claims)
    res = client.post(
        "/api/admin/reload-base-data",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert res.status_code == 200
```

</details>

---

## 🔒 Security & hygiene rules

> 🚨 This folder is inside `tests/`, but it still lives in the repo — treat it as public by default.

- ✅ **Use fake IDs only** (UUIDs are fine; no real usernames/emails)
- ✅ **No private keys, API keys, or real signed JWTs** committed here
- ✅ Keep fixtures **minimal**: include only what the test needs
- ✅ Prefer **deterministic** fixtures (avoid “works only today” timestamps)
- ✅ Don’t encode sensitive geo/person info into claims (even in tests)
- ✅ If a fixture represents elevated access: ensure there’s a paired test proving **non-admin** tokens are rejected (`403`)

---

## ➕ Adding a new fixture

When you add a new claim payload, follow this checklist:

- [ ] Identify the scenario (role/level/scope/resource boundary)
- [ ] Copy the closest existing fixture and edit *only what matters*
- [ ] Use synthetic identifiers (UUIDs, `org_demo_*`, etc.)
- [ ] If time-sensitive: decide whether to **inject `iat/exp`** in signer helper or hardcode for a specific negative test
- [ ] Add/extend at least **one** test that proves the behavior you want
- [ ] Run the auth test suite locally (or via CI)
- [ ] Double-check the fixture won’t trip secret/PII scanners ✅

---

## 🧯 Troubleshooting

**Seeing `401 Unauthorized` unexpectedly?**
- Verify `exp` isn’t in the past
- Verify `iss` / `aud` match what the middleware expects
- Ensure your signer helper uses the same algorithm/keypair as the test middleware

**Seeing `403 Forbidden` unexpectedly?**
- Check `roles` / `levels` in the fixture
- Confirm the endpoint decorator/middleware uses the same claim names (e.g., `roles` vs `role`)

**Tests are flaky around time?**
- Avoid hardcoding `iat/exp` for “valid” fixtures
- Generate them at signing time; hardcode only for “expired token” tests

---

🧩 _If you’re unsure what to put in a new claims fixture, start from the endpoint’s auth guard: which claim keys does it read, and what values does it expect?_ ✅

