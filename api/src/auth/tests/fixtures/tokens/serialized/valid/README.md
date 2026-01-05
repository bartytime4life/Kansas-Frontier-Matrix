---
title: "Auth Test Fixtures — ✅ Valid Serialized Tokens"
path: "api/src/auth/tests/fixtures/tokens/serialized/valid/README.md"
version: "v1.0.0"
last_updated: "2026-01-05"
status: "active"
doc_kind: "Test Fixture README"
license: "CC-BY-4.0"

# Profile / protocol versions (project-governed)
markdown_protocol_version: "1.0"
pipeline_contract_version: "n/a"

# Governance & CARE/FAIR metadata
governance_ref: "TBD"
ethics_ref: "TBD"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

# Provenance (fill during merge/release automation if available)
doc_uuid: "urn:kfm:doc:api:auth:tests:fixtures:tokens:serialized:valid:readme:v1.0.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# ✅ Valid Serialized Token Fixtures 🔐🧪

![Scope](https://img.shields.io/badge/scope-tests-blue)
![Domain](https://img.shields.io/badge/domain-auth-purple)
![Artifact](https://img.shields.io/badge/artifact-serialized%20tokens-green)
![Format](https://img.shields.io/badge/format-JWT%20%28string%29-orange)

> [!NOTE]
> This folder contains **pre-serialized, known-good token strings** used by auth tests.  
> These are “golden” fixtures: **treat them as immutable** unless you’re intentionally updating the golden output.

---

## 📌 Table of contents

- [📘 Overview](#-overview)
- [🗂️ Directory layout](#️-directory-layout)
- [✅ What “valid” means](#-what-valid-means)
- [🧪 How tests should use these fixtures](#-how-tests-should-use-these-fixtures)
- [🧩 Adding a new valid token fixture](#-adding-a-new-valid-token-fixture)
- [🔐 Security & governance notes](#-security--governance-notes)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Definition of Done](#-definition-of-done)

---

## 📘 Overview

### Purpose 🎯
Provide **stable, deterministic token strings** for tests that need to verify:
- serialization/encoding output (“golden” strings)
- decoding/verification behavior on known inputs
- role/claim combinations without re-signing tokens during every test run

### Scope 📦
| In Scope ✅ | Out of Scope 🚫 |
|---|---|
| Access tokens that should pass verification in the test runtime | Real production tokens, secrets, API keys |
| “Golden” serialized strings (exact bytes matter) | Dynamic token generation helpers (those belong in test utilities) |
| Role/claim variants required by unit/contract tests | Expired / malformed tokens (those belong in `invalid/` fixtures) |

### Audience 👥
- **Primary:** API/auth developers writing unit + contract tests
- **Secondary:** CI maintainers (secret scanning & test determinism)

### Definitions 📚
- **Token (serialized):** A single string representation of an auth token (commonly a JWT in `header.payload.signature` form).
- **Valid fixture:** A token that should pass the verifier **with the test configuration** (issuer/audience/secret/public-key, clock rules, etc.).
- **Golden fixture:** A token string whose **exact value** is asserted in tests (string equality), not merely “decodes correctly”.

### Key artifacts 🧾
This directory is expected to contain one or more token files (format may vary by project conventions). Common patterns:

- `*.jwt` / `*.token` / `*.txt` files holding **exactly one token string** (newline allowed at EOF)
- Optional sidecar metadata (`*.json`) if your tests need a human-readable summary

> [!TIP]
> If you’re adding a new token, follow the **existing naming style** in this folder.  
> If no clear convention exists yet, a good default is:
> `"<token_type>__<role>__<scenario>__v<major>.jwt"`  
> Example: `access__admin__baseline__v1.jwt`

---

## 🗂️ Directory layout

```text
📦 api/
└─ 🧩 src/
   └─ 🔐 auth/
      └─ 🧪 tests/
         └─ 🧷 fixtures/
            └─ 🪙 tokens/
               └─ 🧊 serialized/
                  ├─ ✅ valid/
                  │  ├─ README.md  👈 you are here
                  │  ├─ <token files live here…>
                  │  └─ ...
                  └─ ❌ invalid/
                     └─ <expired / malformed / wrong-signature tokens…>
```

---

## ✅ What “valid” means

A token fixture in this folder should meet **all** of the following (as applicable to your verifier):

1. **Signature verification passes**  
   - Signed with the **test-only signing key** (never a prod key)
2. **Not expired under test clock rules**  
   - Either `exp` is far enough in the future *or* tests use a frozen clock aligned to the token’s timestamps
3. **Claims satisfy your verifier**
   - issuer/audience (if enforced)
   - required fields present (e.g., subject/user id, roles/permissions)
4. **String formatting is clean**
   - no leading/trailing whitespace beyond the one optional trailing newline at EOF

> [!IMPORTANT]
> “Valid” here means **valid for tests**.  
> These tokens must be **non-sensitive** and must **not** work against any production environment.

---

## 🧪 How tests should use these fixtures

### ✅ Recommended usage pattern
Use these fixtures when the test needs:
- a fixed token string (golden output tests)
- a known token that exercises specific parsing/verification branches

Prefer dynamic token builders when the test only needs:
- “a token with claims X/Y/Z” (and string equality is NOT asserted)

### Example (Node/TypeScript-style) 🟦
```ts
import fs from "node:fs";
import path from "node:path";

const tokenPath = path.join(
  __dirname,
  "fixtures",
  "tokens",
  "serialized",
  "valid",
  "access__admin__baseline__v1.jwt"
);

const token = fs.readFileSync(tokenPath, "utf8").trim();

// Example: attach to Authorization header
const headers = { Authorization: `Bearer ${token}` };

// ...use headers with your request helper / test client
```

### Fixture file rules 🧼
- **One token per file**
- Keep the token on **one line**
- End-of-file newline is OK (recommended), but tests should `trim()` when reading
- Don’t wrap the token in quotes unless your existing fixture format requires it

---

## 🧩 Adding a new valid token fixture

> [!NOTE]
> Adding fixtures increases repo surface area and can trigger secret scanners.  
> Only add a new token if it provides **unique** coverage.

### 1) Choose the reason ✅
Examples of valid reasons:
- you need a **golden serialized token** string (exact match)
- you need a token with a very specific claim set that’s expensive to build in every test
- cross-language compatibility test needs a stable specimen

### 2) Generate using the test signing configuration 🔧
- Use the same **test secret / test keypair** configured for the auth verifier in tests
- Ensure issuer/audience rules match the test verifier config (if enforced)
- Ensure the token is not bound to real user data (no PII)

### 3) Make it future-proof 🕒
To avoid flaky tests:
- Prefer an `exp` far in the future **OR** freeze the clock in tests
- Keep `iat/nbf` consistent with your test clock assumptions

### 4) Save to this folder 💾
- Filename should clearly reflect:
  - token type (`access` / `refresh` / `service` / etc.)
  - role (`admin` / `researcher` / `user` / etc.)
  - scenario (`baseline` / `missing-scope` / `elevated-role` / etc.)
  - version (`v1`, `v2`, …) if you expect evolution

### 5) Add/update documentation 📝
- If you add a new file, consider adding a short note under **Key artifacts** describing:
  - what it represents
  - which tests rely on it (by filename, not by fragile line numbers)

---

## 🔐 Security & governance notes

### 🚫 Never commit real secrets
Even test tokens can look like secrets. Treat this folder as **high scrutiny**.

- ✅ OK: tokens signed with a **test-only** key/secret that is **not reused anywhere**
- 🚫 Not OK: tokens signed with production keys, tokens copied from real environments, tokens containing real user identifiers

### 🧠 Keep tokens non-identifying
- Use synthetic subjects (e.g., `user_test_admin_001`)
- Avoid emails, phone numbers, addresses, or any real-world identifiers

### 🧯 Secret scanner tripwires
If CI flags a token:
- confirm it’s truly test-only and non-sensitive
- consider storing tokens in a representation your scanner allowlists (project-specific)
- if a scanner must be configured, do it transparently and narrowly (directory-based allowlist), not broadly

---

## 🧯 Troubleshooting

### “token expired” 🕒
- Token’s `exp` is too close to “now”
- Fix by:
  - regenerating with a far-future `exp`, or
  - freezing the test clock to a known instant

### “invalid signature” ✍️
- Token was signed with the wrong key/secret
- Fix by regenerating using the test verifier’s signing config

### “invalid issuer/audience” 🧾
- The verifier enforces `iss` / `aud` and fixture doesn’t match
- Fix by aligning claims to test config (or updating test config if intended)

### “works locally but fails in CI” 🤖
- CI clock, env vars, or verifier config differ
- Ensure fixtures don’t depend on local env-only values

---

## ✅ Definition of Done

**Before merging changes to this folder:**
- [ ] Front-matter complete and valid (no removed fields; use `TBD`/`n/a` where needed)
- [ ] This README contains **Overview** and **Directory Layout** sections
- [ ] Added tokens are test-only, non-sensitive, and non-identifying
- [ ] Tests referencing new fixtures pass locally and in CI
- [ ] No secret scanner violations (or an approved, narrow allowlist is in place)
- [ ] Filenames are descriptive and follow existing conventions
