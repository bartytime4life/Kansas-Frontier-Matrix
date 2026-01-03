# 🧾 Shared Request Headers (Contract Fixtures)

![Contract-first](https://img.shields.io/badge/contract--first-required-2ea44f)
![CI Gate](https://img.shields.io/badge/CI-gated-blue)
![No Secrets](https://img.shields.io/badge/security-no%20secrets%20in%20fixtures-red)
![Fixtures](https://img.shields.io/badge/fixtures-_shared%2Fheaders-8a2be2)

> According to a document from **2025-12-28** (KFM Master Guide v13 draft), **API contract tests are a required CI gate** and automated **secret/sensitive scans** are enforced. This folder exists so headers used across contract tests stay **consistent**, **deterministic**, and **safe**. 🧪🔒

📍 **Location:** `api/tests/contract/fixtures/_shared/headers/`

---

## 🎯 What this folder is

This directory contains **reusable header sets** (“header fixtures”) for API **contract tests**.

**Why we centralize them:**
- ✅ Keep contract tests consistent across endpoints
- ✅ Avoid copy/paste drift across suites
- ✅ Make it obvious what headers are “baseline” vs “scenario-specific”
- ✅ Reduce security risk (no tokens floating around in random test files) 🔐

---

## ✅ What belongs here (and what doesn’t)

### ✅ Put these here
- **Baseline HTTP headers** used for most requests (e.g., `Accept`, `Content-Type`)
- **Non-secret auth placeholders** (e.g., `Authorization: Bearer <TEST_TOKEN>`)
- **Deterministic tracing/correlation headers** (stable IDs used in assertions)
- **Contract-defined custom headers** that are used across multiple tests  
  (example: classification/redaction context headers *only if they exist in the API contract*)

### 🚫 Do **not** put these here
- ❌ Real API keys / passwords / tokens (even “dev” ones)
- ❌ User PII or “looks-like-real” sensitive data
- ❌ Per-test dynamic values (generate them in the test harness and merge at runtime)
- ❌ Ad-hoc headers not defined in the API contract (update the contract first)

---

## 🧱 Naming & organization conventions

Keep filenames boring and searchable:

- Prefer **kebab-case** or **snake_case** (match the existing convention in this repo)
- Encode intent in the name:
  - `base.*` → baseline headers for most requests
  - `auth-*.*` → auth-related variants (still **placeholders**, not secrets)
  - `version-*.*` → API version negotiation headers (if the API supports it)
  - `classification-*.*` → classification/redaction context (only if contract-defined)

📌 **Rule of thumb:** if two different suites would use the same header set, it belongs here.

---

## 📦 Fixture format

> Follow the format already used in this folder. If you’re adding the first header fixture set, choose one of these patterns:

### Option A: JSON object (recommended)
**Pros:** easy merging, language-agnostic, simple diff.

```json
{
  "Accept": "application/json",
  "Content-Type": "application/json",
  "User-Agent": "kfm-contract-tests/1.0",
  "X-Request-Id": "00000000-0000-0000-0000-000000000000"
}
```

### Option B: “.headers” plain text
**Pros:** very readable; mirrors raw HTTP.

```text
Accept: application/json
Content-Type: application/json
User-Agent: kfm-contract-tests/1.0
X-Request-Id: 00000000-0000-0000-0000-000000000000
```

---

## 🧠 Golden rules for header fixtures

### 1) Determinism wins 🧊
If a header value is referenced in assertions (or impacts caching / versioning), keep it stable.

- ✅ Good: `X-Request-Id: 00000000-0000-0000-0000-000000000000`
- ✅ Good: `X-Test-Run: contract-fixtures`
- ⚠️ Avoid: random UUIDs *inside the fixture file*

If you need uniqueness, generate it **in the test harness** and merge it in.

---

### 2) No secrets — ever 🔐
Header fixtures must be safe to commit. Use placeholders like:
- `<TOKEN>`
- `${ENV_VAR_NAME}`
- `__REPLACE_ME__`

If a real secret is required for contract execution:
- inject it at runtime (CI env vars / secret manager)
- substitute it in the test harness
- never store it in this folder

---

### 3) Only contract-defined custom headers 🧩
If you want to introduce a new header:
1. Add it to the **API contract** (OpenAPI / GraphQL, etc.)
2. Update contract tests
3. Then add a fixture here (if shared/reused)

---

## 🧪 Example usage patterns

> Keep request assembly predictable: **base → scenario → per-test overrides**

### Pseudocode (language-agnostic)
```text
headers = merge(
  load("base.json"),
  load("auth-bearer.json"),
  { "X-Request-Id": generatedOrTestSpecificValue }
)
```

### Minimal precedence rule
- Later merges override earlier ones
- Per-test overrides win over shared fixtures

---

## 🧷 Suggested “baseline” header set contents

Use these as a checklist when creating `base.*`:

- `Accept`: usually `application/json`
- `Content-Type`: set when sending a body
- `User-Agent`: stable identifier for contract test traffic
- `X-Request-Id` (or equivalent): stable correlation/tracing header (if supported)

> If the KFM API contract defines **versioning** or **classification/redaction context** headers, create dedicated shared fixtures for them rather than sprinkling them across tests.

---

## 🛠️ Adding a new header fixture (checklist)

- [ ] The header(s) are defined in the API contract (or the contract was updated first)
- [ ] Values are deterministic or intentionally overridden in tests
- [ ] No secrets / tokens / PII included (placeholders only)
- [ ] The fixture is reused by ≥2 tests/suites (otherwise keep it local)
- [ ] Contract tests pass locally + in CI

---

## 🧯 Troubleshooting

### “Works locally, fails in CI”
- Check if CI replaces placeholders (token injection) but local does not (or vice versa)
- Ensure `Authorization` (if needed) is coming from runtime env and not hardcoded

### “Endpoint rejects my request”
- Confirm you’re setting `Accept` / `Content-Type` properly
- Confirm you’re not missing contract-required headers (versioning, correlation IDs, etc.)

### “Why did this PR get blocked?”
- Common causes:
  - a header change broke an existing contract test expectation
  - a fixture accidentally included a secret-like value and triggered scanning
  - a new header was used without updating the contract spec

---

## 🔗 Related (paths)

- `api/tests/contract/` (contract test suites)
- `api/tests/contract/fixtures/_shared/` (shared fixtures root)
- `docs/MASTER_GUIDE_v13.md` (contract-first + CI gates)
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (how to add/change API endpoints)

---

## 🧾 Quick reminder

If you’re unsure whether a header should be shared:
- **Shared** = helps multiple tests + safe + stable ✅  
- **Local** = one-off scenario, highly dynamic, or experimental 🧪

