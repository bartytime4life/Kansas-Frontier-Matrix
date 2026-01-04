# 🔐 Token Request Fixtures (Auth Tests)

![tests](https://img.shields.io/badge/tests-fixtures-6f42c1)
![area](https://img.shields.io/badge/area-auth%2Ftokens-0b7285)
![format](https://img.shields.io/badge/format-JSON-1f6feb)
![policy](https://img.shields.io/badge/policy-no%20secrets%20%F0%9F%9B%A1%EF%B8%8F-red)

> 🧪 This folder contains **request fixtures** used by auth/token tests — focused on **JWT token issuance + refresh flows**.

---

## 📌 Why this folder exists

KFM uses **token-based authentication** (JWT) with **short-lived access tokens** and a **refresh-token mechanism** to keep sessions alive without re-login. These fixtures exist so tests can:

- ✅ Stay **contract-first** (requests match the token endpoint contract)
- 🔁 Reuse **known-good** and **known-bad** request payloads across test suites
- 🧾 Keep tests **deterministic** and reviewable (“evidence-first” mindset)
- 🛡️ Pass **CI security scans** (no real tokens / passwords committed)

---

## 🗂️ Location & expected structure

```text
📁 api/
  📁 src/
    📁 auth/
      📁 tests/
        📁 fixtures/
          📁 requests/
            📁 tokens/
              🧪 password.valid.json
              🧪 password.invalid_password.json
              🧪 refresh.valid.json
              🧪 refresh.expired.json
              🧪 refresh.missing_token.json
              📄 README.md   👈 you are here
```

> ℹ️ File names above are examples — keep the **same naming pattern** your repo already uses.

---

## 🧱 Fixture format

These fixtures are intended to represent **token endpoint requests** (e.g., “issue token” and “refresh token”).  
Depending on the test harness, fixtures are typically one of these formats:

### ✅ Preferred: “request descriptor” JSON (body + optional headers)

Use this if your tests want to load *everything* from one fixture file.

```json
{
  "headers": {
    "content-type": "application/json"
  },
  "body": {
    "grant_type": "password",
    "username": "test.user@kfm.local",
    "password": "P@ssw0rd_Test_Only"
  }
}
```

### 🟦 Alternate: “body-only” JSON

Use this if your tests set headers/route separately.

```json
{
  "grant_type": "refresh_token",
  "refresh_token": "<<REFRESH_TOKEN>>"
}
```

> ✅ **Rule:** Pick one format per folder and stick with it (don’t mix styles unless the loader supports it).

---

## 🧬 Token request fields (common patterns)

Even if implementation details vary (OAuth2 password grant vs custom endpoint), token requests usually fall into these shapes:

### 1) Password / login flow

- `grant_type`: `"password"` *(optional in custom endpoints)*
- `username` or `email`
- `password`
- optional: `mfa_code` *(only for accounts requiring MFA)*

### 2) Refresh flow

- `grant_type`: `"refresh_token"` *(or custom refresh endpoint)*
- `refresh_token`

> 🔑 **Bearer tokens** are generally sent in the `Authorization: Bearer <token>` header for downstream API calls — **not** usually required when *requesting* tokens (unless your implementation mandates it).

---

## 🧪 Included scenarios (recommended minimum set)

Keep a simple matrix so coverage stays obvious:

| Flow | Scenario | Expected outcome |
|------|----------|------------------|
| password | valid credentials | ✅ 200 (tokens issued) |
| password | invalid password | ❌ 401 |
| password | missing fields | ❌ 400 / 422 |
| password | locked account / rate limited | ❌ 423 / 429 |
| refresh | valid refresh token | ✅ 200 (new access token) |
| refresh | expired refresh token | ❌ 401 |
| refresh | malformed refresh token | ❌ 400 / 422 |
| refresh | missing refresh token | ❌ 400 / 422 |

> 🧭 Use the exact status codes your API contract defines — the table above is a **starting point**.

---

## 🧩 Placeholder tokens (SAFE by design)

**Never commit real access tokens, refresh tokens, or production-like JWTs.**  
Instead, use explicit placeholders that your tests replace at runtime:

| Placeholder | Meaning | How to satisfy in tests |
|------------|---------|--------------------------|
| `<<ACCESS_TOKEN>>` | A valid access JWT | Generate/sign with test secret |
| `<<REFRESH_TOKEN>>` | A valid refresh token | Generate/store via setup step |
| `<<EXPIRED_REFRESH_TOKEN>>` | Expired refresh token | Generate with past `exp` |
| `<<MALFORMED_TOKEN>>` | Not a token | Hardcode `"not-a-token"` |

> 🛡️ CI includes **secret scanning** — “JWT-looking” strings can get flagged. Keep placeholders obvious and non-production-like.

---

## 🧪 How to use these fixtures in tests

<details>
<summary><strong>Node / TS example (Jest + supertest-style)</strong> 🟩</summary>

```ts
import fs from "node:fs";
import path from "node:path";

// Adjust this path to match your test file location
const fixturePath = path.join(
  __dirname,
  "..",
  "fixtures",
  "requests",
  "tokens",
  "password.valid.json"
);

const fixture = JSON.parse(fs.readFileSync(fixturePath, "utf8"));

// If using request-descriptor format:
const body = fixture.body ?? fixture;
const headers = fixture.headers ?? {};

await request(app)
  .post("/auth/tokens")
  .set(headers)
  .send(body)
  .expect(200);
```
</details>

<details>
<summary><strong>Python example (pytest client)</strong> 🐍</summary>

```py
import json
from pathlib import Path

fixture_path = Path(__file__).parent / "fixtures" / "requests" / "tokens" / "refresh.valid.json"
fixture = json.loads(fixture_path.read_text())

body = fixture.get("body", fixture)
headers = fixture.get("headers", {})

resp = client.post("/auth/tokens/refresh", json=body, headers=headers)
assert resp.status_code == 200
```
</details>

---

## 🔁 Determinism rules (make tests stable)

Tokens are *time-sensitive* by nature. To prevent flaky tests:

- ⏱️ **Freeze or stub time** when generating JWTs (`iat`, `exp`)
- 🔐 Use a **test-only signing secret** (never production keys)
- 🧪 Prefer generating valid/expired tokens **in code**, not stored in JSON fixtures
- 🧼 Keep test setup/teardown clean so token state doesn’t leak between tests

---

## 🛡️ Security & governance checklist (non-negotiable)

Before committing a new fixture:

- [ ] 🚫 No real secrets (tokens, API keys, passwords)
- [ ] 🧍 No PII (real emails, names, phone numbers, addresses)
- [ ] 🧾 Matches API contract for the endpoint (schema + required fields)
- [ ] ✅ JSON is valid (no trailing commas / comments)
- [ ] 🧪 Added/updated a test that uses the new fixture
- [ ] 📚 Updated the scenario table above if coverage changed

> 🧱 KFM CI gates typically include **API contract tests** and **security scans** — treat fixtures as part of the contract surface.

---

## ➕ Adding a new fixture (quick steps)

1. 🧪 Copy the closest existing fixture file.
2. ✍️ Change only what’s required for the scenario (minimal diff).
3. 🛡️ Replace any sensitive-looking value with a placeholder (see table above).
4. ✅ Add/extend the test case using the fixture.
5. 🧾 If this represents a new contract case, update the contract docs/spec too.

---

## 🧯 Troubleshooting

**Secret scanner flagged my fixture**  
- Replace JWT-shaped strings (`xxx.yyy.zzz`) with placeholders like `<<ACCESS_TOKEN>>`.

**My refresh-token test flakes**  
- Your refresh token may be time-bound or stored server-side. Generate it in setup and inject it into the request.

**The fixture doesn’t match the endpoint anymore**  
- Update the fixture *and* the contract tests together. Contract-first means fixtures evolve with the API contract.

---

## 📎 Related docs (repo references)

- `docs/MASTER_GUIDE_v13.md` (contract-first, determinism, governance)
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (how to change endpoints safely)
- `docs/governance/ROOT_GOVERNANCE.md` (security + review gates)

> 🧭 If you don’t see these files yet, check the project’s master markdown guide for the expected doc map.

