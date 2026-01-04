# 🔐 Auth Response Fixtures (Test “Golden Files”)

![scope](https://img.shields.io/badge/scope-auth-blue)
![type](https://img.shields.io/badge/type-test_fixture-orange)
![format](https://img.shields.io/badge/format-json-success)
![contract](https://img.shields.io/badge/contract-first-informational)
![security](https://img.shields.io/badge/security-no_secrets-critical)

> [!NOTE]
> This folder contains **canonical response fixtures** used by the auth test suite.  
> Think of these files as **“golden” expected outputs** for contract-style tests: *given input X, the API should respond with Y* ✅

---

## 📌 Purpose

We keep response fixtures here to make auth tests:

- **Deterministic** 🧊 (stable outputs → stable tests → stable CI)
- **Readable** 👀 (diffs show exactly what changed)
- **Contract-focused** 📜 (fixtures reflect the API contract for each scenario)
- **Safe to commit** 🔒 (no secrets, no real user data)

---

## 🗂️ What belongs in this folder

✅ **Allowed**
- `*.json` response bodies (preferred)
- Optional `*.headers.json` / `*.meta.json` if tests validate headers or response metadata
- Small supporting `*.md` notes when a fixture needs context (rare)

🚫 **Not allowed**
- Real tokens, API keys, session cookies, or credentials
- Real personal data (names, emails, phone numbers, addresses)
- Volatile values (timestamps, random UUIDs) **unless normalized** (see below)

> [!IMPORTANT]
> Treat every fixture as if it will be scanned by CI for **secrets + PII**. If it can leak, it doesn’t belong here.

---

## 🧭 Directory layout

We prefer grouping fixtures by **endpoint / flow** (easy to scan) 🧠

```text
📁 api/
  📁 src/
    📁 auth/
      📁 tests/
        📁 fixtures/
          📁 responses/
            📄 README.md   👈 you are here
            📁 login/
              📄 success.json
              📄 invalid-credentials.json
              📄 locked-out.json
            📁 refresh/
              📄 success.json
              📄 expired-refresh-token.json
            📁 logout/
              📄 success.json
```

If the folder is currently flat, keep it flat until it becomes painful—then refactor to subfolders once there’s enough volume.

---

## 🏷️ Naming conventions

Keep names **boringly consistent** (future-you will thank you) 🙏

### ✅ Recommended pattern

- **Folder:** `<endpoint-or-flow>/`
- **File:** `<scenario>.json`

Examples:
- `login/success.json`
- `login/invalid-credentials.json`
- `refresh/expired-refresh-token.json`
- `logout/success.json`

### 🔍 Scenario naming tips

- Use **lowercase + dashes** (`kebab-case`)
- Prefer **what happened**, not implementation details:
  - ✅ `mfa-required.json`
  - 🚫 `error-412.json` *(unless the status code is the key behavior)*

---

## 🧼 Determinism rules (aka “don’t snapshot chaos”)

Auth responses often contain values that *should not* be stored as-is.

### Replace volatile fields with stable placeholders

Common volatile fields:
- `access_token`, `refresh_token`, `id_token`
- `expires_in`, `expiresAt`, `issued_at`
- `sessionId`, `nonce`, `state`
- random UUIDs, request IDs, correlation IDs

✅ Use placeholders like:
- `"<<ACCESS_TOKEN>>"`
- `"<<REFRESH_TOKEN>>"`
- `"<<REQUEST_ID>>"`
- `"<<USER_ID>>"`

Example:
```json
{
  "access_token": "<<ACCESS_TOKEN>>",
  "refresh_token": "<<REFRESH_TOKEN>>",
  "expires_in": 3600
}
```

> [!TIP]
> If the test only needs to verify **presence/shape**, prefer matcher-based assertions in tests (e.g., “is a string”) rather than hard-coding the full value.

---

## 🔒 Redaction & safety checklist

Before committing any fixture, ensure:

- [ ] No secrets (JWTs, API keys, passwords, client secrets, cookies)
- [ ] No real emails (use `user@example.test`)
- [ ] No real names / phone numbers / addresses
- [ ] No real IPs (use test ranges like `203.0.113.0/24`)
- [ ] No internal hostnames or private URLs (sanitize if needed)
- [ ] Any IDs are stable placeholders (not real production identifiers)

> [!WARNING]
> **Never** commit a real JWT “just for testing.”  
> Even expired tokens teach attackers about structure, claims, issuers, and internal conventions.

---

## 🧪 How tests should use these fixtures

The intent is typically one of these patterns:

1) **Exact match** (strict contract)
- `expect(res.body).toEqual(expectedFixture)`

2) **Partial match** (contract core + flexible extras)
- `expect(res.body).toMatchObject(expectedFixture)`

3) **Schema-style assertions** (when values are volatile)
- Assert types + required keys, then compare a normalized response

### Example helper (Node/TS-style)

```ts
import fs from "node:fs";
import path from "node:path";

export function loadResponseFixture<T = unknown>(relativePath: string): T {
  const abs = path.resolve(__dirname, "../fixtures/responses", relativePath);
  return JSON.parse(fs.readFileSync(abs, "utf8")) as T;
}
```

Usage:
```ts
const expected = loadResponseFixture("login/success.json");

expect(res.status).toBe(200);
expect(res.body).toEqual(expected);
```

> [!NOTE]
> If your suite already has a fixture loader, **use the existing helper** rather than rolling a new one.

---

## ➕ Adding a new response fixture

1. **Capture** the response (local/dev environment only)
2. **Strip** anything not needed for the test (keep fixtures minimal)
3. **Normalize** volatile fields (tokens, timestamps, random IDs)
4. **Format** the JSON (pretty print, consistent ordering if possible)
5. **Reference** it from the test (don’t inline big blobs)
6. **Run** the test suite locally
7. **Sanity check**: read the fixture like an attacker would 😅

### Formatting options

- Prettier (recommended if already in the repo toolchain):
  ```bash
  npx prettier --write "api/src/auth/tests/fixtures/responses/**/*.json"
  ```

- `jq` (handy for canonical formatting):
  ```bash
  jq -S . raw.json > formatted.json
  ```

---

## 🧯 Troubleshooting

**“Fixture mismatch” but response looks the same**
- JSON key ordering can fool the eye in diffs.
- Make sure files are consistently formatted.

**“Fixture keeps changing every run”**
- You’re snapshotting volatile data (token, timestamps, request IDs).
- Normalize in the API test (or in a small `normalizeAuthResponse()` helper).

**“CI failed due to secret/PII scan”**
- Assume it’s correct until proven otherwise.
- Remove the sensitive value, replace with a placeholder, and re-run.

---

## ✅ Definition of Done for a fixture

A fixture is “done” when:

- [ ] It encodes a clear auth scenario (success or specific failure)
- [ ] It is deterministic (no volatile values)
- [ ] It contains no secrets / no PII
- [ ] It is formatted consistently
- [ ] At least one test uses it meaningfully (no orphan fixtures)

---

<details>
<summary><strong>💡 Why not auto-record fixtures from live auth?</strong></summary>

Recording live auth responses tends to capture secrets, volatile tokens, and environment-specific values.  
Golden fixtures should represent the **contract**, not the runtime noise.

</details>

