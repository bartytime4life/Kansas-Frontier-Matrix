# 🧪 Contract Test Fixtures (API)

![Contract Tests](https://img.shields.io/badge/tests-contract-blue)
![Fixtures](https://img.shields.io/badge/fixtures-golden%20cases-informational)
![Policy](https://img.shields.io/badge/policy-contract--first%20%26%20governed-brightgreen)

These fixtures are the **canonical (“golden”) request/response examples** used by contract tests to verify that the API still honors its published **contracts** (OpenAPI / GraphQL) for **known inputs and expected outputs**.

> ✅ If a contract test fails because a fixture no longer matches the API, treat it as a **contract regression** (or an intentional contract change that must be versioned + documented).

---

## 🎯 Why this folder exists

Contract tests are part of KFM’s non-negotiable boundary checks: **data → catalogs → graph → API → UI → narrative**. The API layer is a governed boundary (enforcing schema consistency, redaction, and classification).  
Fixtures make those expectations **testable and repeatable**.

---

## ✅ What belongs here

Typical fixture contents include:

- 📥 **Request bodies / query params** (e.g., JSON payloads, query strings, path params)
- 📤 **Expected response bodies** (success and error cases)
- 🧾 **Expected headers** (when relevant to the contract)
- 🧪 **Edge cases** that verify:
  - schema correctness ✅
  - backwards compatibility ✅
  - redaction & classification behavior ✅
  - deterministic outputs ✅

---

## 🚫 What must NOT go here (hard rules)

- 🔑 **Secrets** (API keys, tokens, passwords, service creds)
- 🧍 **PII / personal data** (names, emails, phone numbers, addresses, etc.)
- 🧭 **Sensitive locations** or restricted coordinates that should not be public
- 📦 Large blobs / real datasets (fixtures should stay small + minimal)
- 🧨 “Live” snapshots that change every run (timestamps, random IDs, unstable ordering)

> 🧯 This repo is expected to be scanned for secrets/PII/sensitive content. Keep fixtures **clean**.

---

## 📦 Suggested fixture layout (recommended)

Your test harness may already enforce a structure — **follow what exists first**.  
If you’re adding a new area, this layout is recommended for clarity and stability:

```text
api/tests/contract/fixtures/
├── 📄 README.md
├── 📁 v1/
│   ├── 📁 <operationId-or-route-slug>/
│   │   ├── 📄 meta.yml
│   │   ├── 📄 request.json
│   │   ├── 📄 response.200.json
│   │   ├── 📄 response.400.json
│   │   └── 📄 headers.json
│   └── 📁 <another-operation>/
│       └── ...
└── 📁 _shared/
    ├── 📄 ids.json
    └── 📄 common-errors.json
```

### 🧷 Route slug convention

If you don’t have an `operationId`, use a deterministic slug:

- `GET__stac__collections`
- `POST__graph__query`
- `GET__story_nodes__by_id`

(Use `__` to separate segments; avoid `/` in folder names.)

---

## 🏷️ Fixture naming conventions

Keep filenames boring and predictable:

- `request.json`
- `response.<status>.json` → `response.200.json`, `response.404.json`
- `headers.json` (optional; only if contract tests assert headers)
- `meta.yml` (strongly recommended)

### ✅ JSON formatting rules

- 2-space indentation
- final newline
- stable key ordering **if your formatter supports it**
- arrays should be **stable and consistently ordered** (don’t rely on DB insertion order)

---

## 🧾 `meta.yml` (recommended)

A small metadata file makes fixtures maintainable and auditable.

**Example:**

```yaml
# api/tests/contract/fixtures/v1/GET__stac__collections/meta.yml
contract_ref:
  # Prefer pointing to the actual spec file + operationId where possible
  openapi_path: ../../../../src/server/contracts/openapi.yml
  operation_id: stacListCollections

case:
  name: happy_path
  description: Minimal STAC Collections list with 2 collections.

http:
  method: GET
  path: /v1/stac/collections
  expected_status: 200

governance:
  classification: public
  contains_sensitive_locations: false
  redaction_expected: none

notes:
  - "Fixture uses synthetic IDs only."
  - "Do not include any real person names."
```

> If your repo’s API contracts live somewhere else (e.g., `api/contracts/…`), update `openapi_path` accordingly.

---

## 🧱 Determinism rules (fixtures must be replayable)

To keep contract tests stable (and to align with the broader deterministic pipeline principle), fixtures must avoid unstable data.

### ✅ Do
- Use **fixed IDs** (UUIDs that never change)
- Use **fixed timestamps** (or omit timestamps entirely in fixtures)
- Use **small datasets** that still represent realistic shapes
- Keep ordering stable (especially for arrays)
- Prefer “schema minimal + representative” payloads

### ❌ Don’t
- Assert on request IDs, trace IDs, nonces, build timestamps, random salts
- Include data that is “current” (e.g., `now()`, “latest”, “today”)
- Depend on external services (fixtures should run offline / mocked)

---

## 🔐 Governance & sovereignty expectations

Fixtures are test artifacts, but they’re still part of the repo and must respect governance rules:

- 🧭 **Redaction and classification** behavior is enforced at the API boundary  
- 🧬 **Classification must not be downgraded** through processing or testing artifacts  
- 🪶 If a scenario involves restricted/sensitive concepts, fixtures should use:
  - generalized coordinates (e.g., centroid of a large region),
  - synthetic locations,
  - or a “redacted” example response shape.

> If you need to test redaction behavior, prefer fixtures that validate **the redacted output** (not the sensitive raw values).

---

## 🔄 Updating fixtures (workflow)

When you change anything API-facing, assume fixtures may need updates.

1. 🧩 **Update the contract first** (OpenAPI / GraphQL)  
2. 🧠 Decide if the change is **breaking**  
   - Breaking changes require a **version bump** (e.g., `/v2/...`) or explicit negotiation strategy  
3. 🧪 Update / add fixtures to reflect the new contract behavior  
4. ✅ Run contract tests and ensure they pass locally and in CI  
5. 📝 If behavior changed intentionally, document it (see API contract extension template)

Helpful references (repo paths):
- `../../../../docs/MASTER_GUIDE_v13.md`
- `../../../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- `../../../../docs/governance/ROOT_GOVERNANCE.md`
- `../../../../docs/governance/SOVEREIGNTY.md`

---

## 🧰 Quick checklist before you open a PR

- [ ] Fixture is minimal but representative
- [ ] No secrets / tokens / credentials
- [ ] No PII
- [ ] No sensitive coordinates (unless *redacted output* is what’s being tested)
- [ ] Response matches the contract schema (and required fields are present)
- [ ] Ordering is stable (arrays and object keys where relevant)
- [ ] If it’s a breaking change: a version bump strategy exists (v2 path, etc.)

---

## 🧩 Troubleshooting

<details>
  <summary><strong>Contract tests fail because of timestamps / IDs</strong></summary>

- Remove volatile fields from fixtures, or
- Normalize them in the test harness (e.g., ignore `requestId`, `traceId`, `generatedAt`) **only if those fields are explicitly non-contractual**.
</details>

<details>
  <summary><strong>Fixture response is “too big”</strong></summary>

Reduce to the smallest payload that still:
- satisfies required fields,
- includes one realistic example,
- and covers the contract shape you’re protecting.
</details>

<details>
  <summary><strong>You need a fixture for a “restricted” scenario</strong></summary>

Prefer fixtures that prove:
- the API returns **redacted/generalized** data, or
- the API returns a **permission error** with a stable error shape.

Do **not** commit restricted raw data into the repo.
</details>