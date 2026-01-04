# 🔐 Register — Request Fixtures 📦🧪

![Fixtures](https://img.shields.io/badge/fixtures-request_payloads-blue)
![Module](https://img.shields.io/badge/module-auth-purple)
![Purpose](https://img.shields.io/badge/purpose-contract_tests%20%2B%20validation-success)

These files are **canonical request payloads** for the **Auth → Register** flow, used by automated tests to verify:
- ✅ **happy-path** registration
- ❌ **validation failures** (missing/invalid fields)
- 🧯 **security edges** (unexpected fields, attempted role escalation, etc.)
- 🔁 **determinism** (stable, repeatable inputs)

> 🧭 Guiding idea: a fixture is a **contract example** — small, readable, deterministic, and aligned with the API’s schema.

---

## 📍 Location

```text
api/src/auth/tests/fixtures/requests/register/
```

---

## 🗂️ What lives here

```text
register/
├── 📄 README.md                # You are here
├── 📄 ok.json                  # (recommended) baseline valid request
├── 📄 missing_email.json       # (recommended) validation: required field
├── 📄 invalid_email.json       # (recommended) validation: format
├── 📄 missing_password.json    # (recommended) validation: required field
├── 📄 weak_password.json       # (recommended) validation: strength/policy
├── 📄 duplicate_email.json     # (recommended) conflict / idempotency behavior
└── 📄 extra_fields.json        # (recommended) unknown fields / hardening
```

> ⚠️ Your repo may have different filenames already — that’s fine.  
> Keep the **intent** consistent and keep this README’s “Fixture Index” updated.

---

## ✅ Fixture conventions (non-negotiable)

### 1) Contract-aligned ✅
Fixtures must match the **current API contract** (schema / DTO / OpenAPI / GraphQL input).  
If the contract changes, update:
- the fixture(s)
- the related test(s)
- (if applicable) any contract snapshot / schema validation expectations

### 2) Deterministic 🔁
Fixtures should be stable over time:
- ❌ no random emails generated inside JSON
- ❌ no timestamps (unless explicitly required by the contract)
- ✅ if uniqueness is needed (e.g., email), prefer **test setup** to isolate DB state, or generate uniqueness **in test code** (not inside fixture)

### 3) No real-world PII or secrets 🛡️
Fixtures are scanned and reviewed like production code:
- ✅ Use safe domains like `example.com`  
- ✅ Use obvious test-only values like `TestOnly!ChangeMe123`
- ❌ Never paste real emails, tokens, API keys, or personal data

### 4) Keep payloads minimal ✂️
A fixture should contain only what it needs to prove the behavior:
- ✅ minimum required fields for `ok.json`
- ✅ one targeted failure mode per error fixture

---

## 📚 Fixture Index (keep this current)

| Fixture file | Goal 🎯 | Notes 📝 |
|---|---|---|
| `ok.json` | ✅ Valid registration | Minimal required fields only |
| `missing_email.json` | ❌ Required-field validation | Expect 4xx |
| `invalid_email.json` | ❌ Format validation | Expect 4xx |
| `missing_password.json` | ❌ Required-field validation | Expect 4xx |
| `weak_password.json` | ❌ Password policy | Expect 4xx |
| `duplicate_email.json` | 🔁 Duplicate identity behavior | Often 409 or 4xx; depends on contract |
| `extra_fields.json` | 🧯 Hardening / unknown fields | Ensure unknown fields are rejected or ignored per contract |

---

## 🧩 Suggested payload shape (illustrative)

Because **the contract is the source of truth**, these examples are *schematic*.
Adjust field names to match the real request schema.

<details>
  <summary><strong>✅ ok.json</strong> (example)</summary>

```json
{
  "email": "test.user+register_ok@example.com",
  "password": "TestOnly!ChangeMe123",
  "displayName": "Test User"
}
```
</details>

<details>
  <summary><strong>❌ invalid_email.json</strong> (example)</summary>

```json
{
  "email": "not-an-email",
  "password": "TestOnly!ChangeMe123",
  "displayName": "Test User"
}
```
</details>

<details>
  <summary><strong>🧯 extra_fields.json</strong> (example)</summary>

```json
{
  "email": "test.user+register_extra_fields@example.com",
  "password": "TestOnly!ChangeMe123",
  "displayName": "Test User",
  "role": "admin",
  "isAdmin": true
}
```

> ✅ Registration should not allow client-controlled privilege escalation.
</details>

---

## 🧪 Using these fixtures in tests

Keep tests readable by loading fixtures and focusing assertions on the behavior.

<details>
  <summary><strong>Example</strong> (pseudo-code)</summary>

```ts
// Arrange
const payload = loadJsonFixture('requests/register/ok.json');

// Act
const res = await http.post(REGISTER_ENDPOINT, payload);

// Assert
expect(res.status).toBe(201); // or 200 per contract
expect(res.body).not.toHaveProperty('password'); // never echo secrets
```
</details>

### 🧠 Tip: centralize a fixture loader
If multiple tests load JSON fixtures, use a single helper to:
- resolve paths safely
- enforce UTF-8
- optionally validate fixtures against a schema in test time

---

## ➕ Adding a new fixture (checklist)

- [ ] Name the file by **intent** (e.g., `missing_<field>.json`, `invalid_<field>.json`, `policy_<rule>.json`)
- [ ] Keep it **minimal** (one behavior per fixture)
- [ ] Ensure it includes **no PII / secrets**
- [ ] Add it to the **Fixture Index** table above
- [ ] Add/adjust test coverage to use it
- [ ] Confirm CI passes ✅ (lint + tests + scans)

---

## 🔎 Troubleshooting (common gotchas)

- **“duplicate email” fails unpredictably**  
  → your tests may be sharing DB state. Prefer DB reset between tests, or generate uniqueness in test code.

- **fixture drift after contract changes**  
  → treat fixtures like a contract artifact: update fixture + tests in the same PR.

- **unexpected 500 instead of 4xx**  
  → likely missing request validation / schema guards; add validation and update tests.

---

## 🔗 See also

- 📁 `api/src/auth/tests/fixtures/requests/` — other auth request fixtures (login, refresh, etc.)
- 📁 `api/src/auth/tests/fixtures/responses/` — response fixtures (if present)
- 📄 API contract / schema definitions (wherever the auth contracts live in this repo)

