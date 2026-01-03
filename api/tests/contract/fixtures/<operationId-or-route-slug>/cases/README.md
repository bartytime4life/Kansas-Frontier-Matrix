# 🧪📦 Contract Fixture Cases

![contract-first](https://img.shields.io/badge/contract--first-required-2ea44f)
![api-contract-tests](https://img.shields.io/badge/tests-contract%20fixtures-blue)
![deterministic](https://img.shields.io/badge/deterministic-fixtures-important-6f42c1)

This folder contains **golden contract-test cases** for a single API operation (the parent directory: `api/tests/contract/fixtures/<operationId-or-route-slug>/`).

Contract cases are the **“known inputs → expected outputs”** snapshots that CI uses to ensure an endpoint remains stable (or is explicitly versioned when it changes). ✅

---

## 🧭 What belongs here (and what does not)

✅ **Belongs here**
- Stable request/response expectations: status codes, error shapes, headers, JSON structure.
- Small, deterministic payloads.
- “Golden” cases we want to preserve across refactors.

🚫 **Does NOT belong here**
- Performance tests, load tests, soak tests.
- Huge fixtures or raw datasets.
- Secrets, real tokens, private keys, or sensitive/PII data.

> 🔒 Keep fixtures **sanitized** and **shareable**. If a case needs “realistic” data, prefer **synthetic** or **redacted** examples.

---

## 🗂️ Directory layout

Inside `cases/`, each **case is a folder** with a required `case.json`.

```text
📁 api/
  📁 tests/
    📁 contract/
      📁 fixtures/
        📁 <operationId-or-route-slug>/
          📁 cases/
            📄 README.md   ← (this file)
            📁 00-smoke-ok/
              📄 case.json
            📁 10-bad-request-missing-field/
              📄 case.json
            📁 20-unauthorized/
              📄 case.json
            📁 30-not-found/
              📄 case.json
```

### 🏷️ Case folder naming
Use **kebab-case** plus a numeric prefix so ordering is deterministic:

- `00-smoke-ok`
- `10-bad-request-missing-field`
- `20-unauthorized`
- `30-not-found`

---

## 🧩 `case.json` format

Each `case.json` is intended to be **portable**, **minimal**, and **explicit**.

### Required keys
- `id` (string) — unique within this operation
- `title` (string) — short human label
- `request` (object) — what to send
- `expect` (object) — what must come back

### Recommended keys
- `description` (string)
- `tags` (array of strings)
- `notes` (string) — e.g., why this case exists / what regression it prevents
- `assert` (object) — “ignore paths” + matchers for dynamic fields

---

## ✅ Example `case.json`

```json
{
  "id": "smoke-ok",
  "title": "Smoke test: returns 200 for a valid request",
  "description": "Minimal happy-path contract. Keep this stable unless the endpoint is versioned.",
  "tags": ["happy-path", "smoke"],

  "request": {
    "method": "GET",
    "path": "/v1/example/resource",
    "headers": {
      "accept": "application/json"
    },
    "query": {
      "limit": 1
    }
  },

  "expect": {
    "status": 200,
    "headers": {
      "content-type": "application/json"
    },
    "body": {
      "ok": true
    }
  }
}
```

---

## 🧷 Handling “dynamic” response fields (timestamps, IDs, etc.)

Contract tests should be **deterministic**. If the real API includes dynamic fields, you have three options:

1. **Prefer making the API deterministic in test mode**
   - e.g., freeze time, seeded IDs, fixed ordering.

2. **Add an `assert` section** (if/when the runner supports it)
   - `ignorePaths`: ignore volatile fields
   - `matchers`: validate type/shape instead of exact value

Example pattern:

```json
{
  "assert": {
    "ignorePaths": [
      "$.meta.requestId",
      "$.meta.generatedAt"
    ],
    "matchers": {
      "$.data.items[*].id": "uuid",
      "$.meta.generatedAt": "iso8601"
    }
  }
}
```

> 🧠 Rule of thumb: **don’t snapshot random noise**. Snapshot *meaningful* contract guarantees.

---

## 🧰 Adding a new case (checklist)

- [ ] Pick or confirm the parent folder name: `fixtures/<operationId-or-route-slug>/`
- [ ] Add a new folder under `cases/` using numeric prefix + slug (`NN-my-case/`)
- [ ] Create `case.json`
- [ ] Keep the body small + deterministic
- [ ] Avoid secrets / PII / sensitive coordinates
- [ ] If this change alters a public contract, make sure the **API contract** (OpenAPI/GraphQL) is updated too
- [ ] If it’s a breaking change, **version the endpoint** (don’t silently break old clients)

---

## 🧭 How these cases are used in CI

Contract cases are executed by the contract-test runner to verify:

- the endpoint responds correctly for known inputs ✅
- the contract doesn’t drift unintentionally ✅
- changes are either backwards compatible **or** explicitly versioned ✅

If a case fails unexpectedly, treat it like a **breaking-change alarm**:
- either you introduced a bug/regression, **or**
- you changed the contract and must update both the spec + cases (and possibly version the endpoint).

---

## 🔗 Related KFM docs (source-of-truth paths)

- `docs/MASTER_GUIDE_v13.md` 📘 (contract-first + CI expectations)
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` 🧾 (how to propose/record API contract changes)

> Tip: when changing endpoints, update the contract docs **and** the fixture cases together so reviews are straightforward.

