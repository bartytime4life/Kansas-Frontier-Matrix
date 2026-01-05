---
title: "Auth Test Fixtures — Serialized Tokens (Decoded)"
path: "api/src/auth/tests/fixtures/tokens/serialized/decoded/README.md"
version: "v0.1.0"
last_updated: "2026-01-05"
status: "active"
doc_kind: "Test Fixture README"
license: "TBD"
markdown_protocol_version: "1.0"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "TBD"
doc_uuid: "urn:kfm:doc:api:auth:tests:fixtures:tokens:serialized-decoded:v0.1.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# 🔐 Token Fixtures — Serialized → Decoded (Auth Tests)

![status](https://img.shields.io/badge/status-active-brightgreen)
![area](https://img.shields.io/badge/area-auth%20tests-blue)
![fixture](https://img.shields.io/badge/fixture-decoded%20JWT%20JSON-orange)

This folder contains **decoded “golden” fixtures** that correspond to **serialized token strings** used in authentication/authorization tests.

> ⚠️ **Safety rule:** These fixtures must be **synthetic test tokens** only — no real user data, no real secrets, no production tokens.

---

## 📘 Overview

### Purpose 🎯
- Provide a **stable, reviewable** source of truth for what a “decoded token” looks like in tests.
- Enable **deterministic auth tests** by comparing decoder output against known-good decoded JSON.

### Scope ✅ / ❌

| In Scope ✅ | Out of Scope ❌ |
|---|---|
| Decoded token fixtures used by unit/integration tests | Production secrets/keys |
| Token claim shapes (expected payload structure) | Real user identities / PII |
| Role/permission edge-cases (admin/user/etc.) | Full auth implementation docs |

### Audience 👥
- Backend developers working on `api/src/auth/*`
- Test authors adding or updating auth/ACL coverage
- Reviewers validating auth claim/role changes

### Definitions 🧾
- **Serialized token**: the compact string (e.g., a JWT) sent in headers (`Authorization: Bearer <token>`).
- **Decoded token**: the JSON object produced by our decode helper (claims/payload, and optionally header fields).
- **Fixture**: committed test data used to make tests deterministic and repeatable.

### Key Artifacts 🧩

| Artifact | Location | What it’s for |
|---|---|---|
| This README | `api/src/auth/tests/fixtures/tokens/serialized/decoded/README.md` | Conventions + guardrails |
| Decoded fixtures | `api/src/auth/tests/fixtures/tokens/serialized/decoded/*` | Expected decoded outputs (JSON) |
| Serialized fixtures | `api/src/auth/tests/fixtures/tokens/serialized/*` | Token strings that decode to the above |

### Definition of Done ✅
- [ ] New fixture has a **clear scenario name** (what is it testing?)
- [ ] Decoded JSON contains **no PII** (no real emails, names, addresses, phone numbers)
- [ ] Time-based claims (`iat/exp/nbf`) are **deterministic** (see below)
- [ ] Fixture is linked 1:1 with a matching serialized token fixture
- [ ] Tests pass locally and in CI

---

## 🗂️ Directory Layout

### You are here 📍
```
📁 api/
  └─ 📁 src/
     └─ 📁 auth/
        └─ 📁 tests/
           └─ 📁 fixtures/
              └─ 📁 tokens/
                 └─ 📁 serialized/
                    └─ 📁 decoded/   👈 (this folder)
                       ├─ 📄 README.md
                       └─ 📄 *.json (decoded fixtures)
```

### Naming convention 🏷️
Use **scenario-first** naming so failures are obvious in test output.

Recommended patterns:
- `<token_kind>.<scenario>.<actor>.json`
  - `access.valid.admin.json`
  - `access.expired.user.json`
  - `refresh.valid.user.json`
  - `access.invalid_signature.user.json`

If your repo already has a naming scheme, **match it**—consistency beats “perfect.”

---

## 🧬 Fixture Content Contract

### What goes in a decoded fixture?
A decoded fixture MUST mirror **exactly** what our code under test returns.

Common approaches:
1) **Payload-only** decoded output (most common)
2) `{ header, payload }`
3) `{ header, payload, signature }` (rare in app-level tests)

If tests only assert claims, prefer **payload-only** fixtures for readability.

### Typical claim fields (example) 🧾
Below is an *illustrative* payload fixture shape (your real fixture should match your decoder output contract):

```json
{
  "iss": "kfm-api",
  "aud": "kfm-client",
  "sub": "user_test_0001",
  "jti": "jti_test_0001",
  "iat": 1700000000,
  "nbf": 1700000000,
  "exp": 1700003600,
  "roles": ["user"],
  "access_level": "standard",
  "org_id": "org_test_0001",
  "scopes": ["read:public", "read:owned"]
}
```

### Determinism rules 🧊
Time-related fields are a common source of flaky tests.

**Pick one strategy** and stick to it:
- ✅ **Fixed epoch seconds** in fixtures + tests that compare exact values  
- ✅ **Freeze time** in tests (fake timers / clock injection) + fixtures written relative to that frozen “now”
- ❌ “Real current time” during fixture generation (will drift and break snapshots)

---

## 🧪 How Tests Use These Fixtures

### Golden decode test (example) 🧷
Typical pattern:
1) Load serialized token string fixture  
2) Decode token using auth utilities  
3) Compare result to decoded JSON fixture in this folder  

```ts
import fs from "node:fs";
import path from "node:path";

// import { decodeToken } from "@/auth/tokens"; // example only

const FIXTURE_DIR = __dirname;

function readText(p: string) {
  return fs.readFileSync(p, "utf8").trim();
}

function readJson(p: string) {
  return JSON.parse(fs.readFileSync(p, "utf8"));
}

test("decodes access.valid.admin correctly", () => {
  const token = readText(path.join(FIXTURE_DIR, "..", "access.valid.admin.jwt")); // example path
  const expected = readJson(path.join(FIXTURE_DIR, "access.valid.admin.json"));

  const decoded = decodeToken(token); // must match your project API
  expect(decoded).toEqual(expected);
});
```

> 🧠 Tip: If your decoder returns additional fields (like `header`), store them in the fixture and assert them too—especially if `kid/alg` matters.

---

## ➕ Adding or Updating Fixtures

### When to add a new decoded fixture ✅
Add fixtures when:
- Introducing a **new claim** (e.g., `tenant_id`, `capabilities`, `scopes`)
- Changing **role/permission semantics**
- Adding auth edge-cases (expired, not-yet-valid, wrong audience, etc.)
- Fixing a bug in token parsing/validation behavior

### Minimal process (safe + repeatable) 🔁
1. Decide the scenario and **name it clearly**
2. Create/update the **serialized token fixture** (string) using only test secrets/keys
3. Decode it using the **same decode path** used in production code
4. Save the decoder output as JSON in this folder
5. Run the test suite and confirm stability

---

## 🛡️ Security & Governance Notes

### Hard rules 🚫
- Do **not** store real credentials, API keys, or production tokens in fixtures.
- Do **not** include PII in claims (emails, real names, phone numbers, addresses).
- Use obviously synthetic identifiers:
  - `user_test_####`
  - `org_test_####`
  - `tenant_test_####`

### Secret-scanner friendliness 🧯
Serialized tokens can *look* like secrets. If secret scanning is strict in this repo:
- Prefer generating serialized tokens at test runtime from decoded JSON + a known test key
- Or clearly isolate fixture patterns and document allow-list strategy (project-specific)

---

## 🧩 Troubleshooting

### “Fixture changed” / snapshot diffs everywhere
- Check `iat/exp/nbf` drift (time determinism rules above)
- Confirm token generation isn’t using system clock
- Ensure decode helper version didn’t change output shape (e.g., adds `header`)

### “Invalid token” failures after claim changes
- Ensure the auth middleware expects the new claim schema
- Update both **serialized** and **decoded** fixtures together
- Confirm roles/scopes in fixtures align with endpoint permission checks

---

## 🔚 References
- Project security/auth design notes (JWT sessions, access/refresh token behavior, role-based authorization)
- KFM Markdown Protocol / universal template conventions (front-matter + required sections)

---
💡 Maintainers: Keep this README small-but-strict. Fixtures are only valuable if they stay deterministic, reviewable, and safe.
