# 🔄 Refresh Response Fixtures (Auth)

`🧪 tests` `🔐 auth` `♻️ refresh` `📦 fixtures` `✅ contract-first`

> [!NOTE]
> This folder stores **golden** (known-good) response bodies for the **token refresh** flow.
> The goal is predictable tests, clean diffs, and zero accidental secret/PII leaks.

---

## 📌 Overview

The **refresh** endpoint exists to keep sessions alive by exchanging a **refresh token** for a new **access token** (typically a JWT).  
These fixtures act as the “expected” JSON responses for endpoint/contract tests.

**Why fixtures instead of hardcoding in tests?**
- ✅ Makes behavior changes obvious in PR diffs
- ✅ Encourages contract-first thinking (fixtures mirror the API contract)
- ✅ Keeps tests deterministic & repeatable
- ✅ Centralizes security hygiene (placeholders only)

---

## 🗂️ Directory Layout

```text
api/src/auth/tests/fixtures/responses/refresh/
├── 📄 README.md
├── 📄 <status>.<scenario>.json
└── 📄 ...
```

> [!TIP]
> Keep file names “greppable”: **status + scenario** is usually enough to understand intent without opening the file.

---

## 🧾 Recommended Naming Convention

Use:

`<status>.<scenario>.json`

Examples:
- `200.ok.json`
- `401.invalid-refresh-token.json`
- `401.expired-refresh-token.json`
- `403.refresh-token-revoked.json`
- `429.too-many-requests.json`

---

## 📦 What Goes In a Refresh Fixture?

The **API contract** is the source of truth for the exact schema.  
That said, most refresh responses fall into two buckets:

### ✅ Success (2xx)

Usually includes:
- `accessToken` (new access token)
- `refreshToken` (optional rotation)
- token metadata like `tokenType`, `expiresIn`, etc.

Example (illustrative only — align to the real contract):

```json
{
  "accessToken": "<ACCESS_TOKEN_PLACEHOLDER>",
  "refreshToken": "<REFRESH_TOKEN_PLACEHOLDER>",
  "tokenType": "Bearer",
  "expiresIn": 3600
}
```

### ❌ Failure (4xx/5xx)

Usually includes:
- a stable machine-readable `error` / `code`
- a human-readable `message`
- optional `details` for debugging

Example (illustrative only — align to the real contract):

```json
{
  "error": "invalid_refresh_token",
  "message": "Refresh token is invalid, expired, or revoked."
}
```

---

## 🧪 Using Fixtures in Tests

### TypeScript (Jest/Vitest) — strict equality (stable responses)

```ts
import expected from "./200.ok.json";

it("returns refreshed tokens", async () => {
  const res = await request(app)
    .post("/auth/refresh")
    .send({ refreshToken: "<REFRESH_TOKEN_PLACEHOLDER>" });

  expect(res.status).toBe(200);
  expect(res.body).toEqual(expected);
});
```

### TypeScript (Jest/Vitest) — partial matching (dynamic fields)

If the endpoint returns values that legitimately vary (timestamps, rotated tokens, UUIDs), prefer partial assertions:

```ts
import expected from "./200.ok.json";

expect(res.status).toBe(200);
expect(res.body).toMatchObject({
  ...expected,
  accessToken: expect.any(String),
  refreshToken: expect.any(String),
});
```

> [!TIP]
> If you’re `expect.any(...)`-ing half the payload, consider validating **shape** via schema/contract tests and only asserting the critical fields.

---

## 🔒 Security & Repo Hygiene

> [!WARNING]
> **Never** commit real secrets (tokens, keys, cookies) or real user data (PII) into fixtures.

Hard rules ✅
- [ ] Tokens must be **placeholders**, not real JWTs / opaque refresh tokens
- [ ] No emails, phone numbers, names, or production identifiers
- [ ] Keep responses deterministic (stable ordering, stable values where possible)
- [ ] Avoid embedding timestamps unless your tests freeze time

---

## ♻️ Updating / Adding Fixtures

1. Update the **API contract** (if the response schema/meaning changes).
2. Update the endpoint implementation.
3. Add/update fixture JSON files in this folder.
4. Update tests to reference the fixture(s).
5. Run local checks (unit + integration + contract).

### Definition of Done ✅
- [ ] Contract tests pass
- [ ] Auth refresh tests pass
- [ ] Lint + type checks pass
- [ ] No secret/PII scanners are triggered
- [ ] Fixture diffs clearly explain the behavior change

---

## 🧭 Nearby Fixture Folders (Context)

```text
api/src/auth/tests/fixtures/responses/
├── 📁 login/
├── 📁 logout/
├── 📁 refresh/   👈 you are here
└── 📁 me/
```

