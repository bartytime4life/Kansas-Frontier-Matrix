# 🧪 API Contract Test Helpers

![scope](https://img.shields.io/badge/scope-contract%20tests-3b82f6)
![boundary](https://img.shields.io/badge/boundary-API%20contracts-8b5cf6)
![ci](https://img.shields.io/badge/CI-gated-ef4444)

Shared helper utilities for **API contract tests** (REST/OpenAPI + GraphQL), focused on keeping the **API boundary stable, testable, and governance-safe**.

> 📌 These helpers exist so contract tests stay **short**, **readable**, and **consistent** across endpoints.

---

## 🔎 Table of contents
- [What “contract tests” mean here](#-what-contract-tests-mean-here)
- [What belongs in helpers](#-what-belongs-in-helpers)
- [Suggested folder layout](#-suggested-folder-layout)
- [Common helper patterns](#-common-helper-patterns)
- [When you change the API](#-when-you-change-the-api)
- [Governance & redaction expectations](#-governance--redaction-expectations)
- [Troubleshooting](#-troubleshooting)

---

## 📜 What “contract tests” mean here

Contract tests verify the **published API contract** stays true in practice:

- ✅ Endpoints respond as expected for **known inputs**
- ✅ Responses conform to the **declared schema** (OpenAPI / GraphQL)
- ✅ Changes are either **backwards-compatible** or explicitly **versioned**

In KFM’s contract-first philosophy, the contract (spec/schema) is a **first-class artifact** and **drives development**, not the other way around. That’s why contract tests are treated as a **merge gate** in CI. 🧱🔒

---

## 🧩 What belongs in helpers

This folder should contain **reusable building blocks**, not test cases.

✅ Good fits:
- API client builders (base URL, auth headers, retry policy for flaky local startup)
- Contract loaders (OpenAPI YAML/JSON loader, GraphQL SDL loader)
- Response/schema assertion helpers (e.g., “response matches spec”, “no unknown fields”)
- Fixture tooling (known inputs, deterministic seed data, snapshot normalization)
- Time/randomness controls (freeze time, deterministic IDs)
- Governance assertions (redaction guarantees, classification guardrails)

🚫 Not a fit:
- Full endpoint test suites (put those in `api/tests/contract/`)
- Large fixture blobs with real data (especially anything sensitive)
- Business-logic validation (belongs in unit/integration tests)

---

## 📁 Suggested folder layout

> Your repo may vary — this is the **recommended mental model** for keeping helpers discoverable.

```text
api/
└── tests/
    └── contract/
        ├── helpers/
        │   ├── README.md                👈 you are here
        │   ├── client.*                 # test client / request wrapper
        │   ├── contracts.*              # spec/schema loading + caching
        │   ├── assertions.*             # schema + invariants assertions
        │   ├── fixtures.*               # known inputs / seed helpers
        │   ├── normalization.*          # stable snapshots (sort keys, redact volatile fields)
        │   └── auth.*                   # tokens/roles helpers (NO real secrets)
        └── test_*.*
```

---

## 🧰 Common helper patterns

### 1) ✅ Create a “single way” to call the API
All contract tests should call the API **the same way**.

**Goals**
- consistent base URL resolution (local, CI, docker)
- consistent headers (Accept / Content-Type)
- consistent auth simulation (roles, scopes)
- consistent logging on failure (print request + response)

<details>
<summary>Example shape (pseudo-code)</summary>

```python
client = make_api_client(base_url=TEST_API_BASE_URL, role="public")

resp = client.get("/v1/catalog/stac/items?limit=1")

assert_ok(resp)
assert_conforms_to_openapi(resp, operation_id="listStacItems")
```
</details>

---

### 2) 📦 Load contracts once, validate everywhere
Contract tests should treat schemas as **the source of truth**.

Typical responsibilities:
- load OpenAPI spec from the canonical location
- optionally lint/validate the spec itself
- cache parsed schemas for test speed

---

### 3) 🧾 Normalize before snapshotting
If you snapshot responses, normalize:
- sort object keys / lists when order is not meaningful
- strip volatile fields (timestamps, random IDs, request IDs)
- keep stable formatting for diffs

> 🧠 Rule of thumb: contract tests should fail only on **meaningful contract drift**.

---

### 4) 🧊 Determinism helpers
Contract tests should be deterministic and replayable:
- freeze time
- stable random seeds
- stable fixture IDs

---

## 🔁 When you change the API

Contract tests are a CI gate, so **every API change must be accompanied by contract alignment**:

### ✅ Safe changes (usually)
- add **optional** response fields
- add new endpoints without touching old ones
- broaden enums only if schema allows

### ⚠️ Breaking changes (must be versioned)
- removing fields
- changing field meaning/type
- changing default behavior in ways clients rely on

**If it’s breaking:** introduce a **new versioned endpoint** (e.g., `/v2/...`) and keep the old one until a deprecation plan exists.

### Contract-first workflow (recommended)
1. 📐 Update the contract (OpenAPI/GraphQL) first
2. 🧪 Update/add contract tests to reflect the new expected behavior
3. 🛠️ Implement server changes to satisfy the contract
4. ✅ Ensure CI passes (spec lint + contract tests)

> Helpful reference: the repo contains an API contract extension template under `docs/templates/` (use it when adding/changing endpoints).

---

## 🔒 Governance & redaction expectations

Because the API boundary is where “what can be shown” is enforced, contract tests should also include **safety invariants**, for example:

- 🔐 Sensitive fields are not present for public roles
- 🧭 Sensitive locations are generalized/omitted when required
- 🧾 Classification is not silently downgraded across transformations
- 🧪 Fixtures are sanitized and never include secrets/PII

**Practical guidance**
- Prefer synthetic fixtures over real extracts
- If you must include representative data, ensure it’s **explicitly approved and scrubbed**
- Never embed tokens/keys; use `.env.example`-style placeholders or CI secrets (but contract tests should not depend on real secrets)

---

## 🛠️ Troubleshooting

### “Spec mismatch” failures
- Confirm the test is validating against the correct spec version
- Check whether the endpoint change is breaking (needs version bump)
- Validate the schema itself (lint step) before debugging code

### “Flaky” contract tests
- Ensure no external network calls
- Ensure fixture DB/data is stable and seeded deterministically
- Normalize volatile response fields before comparisons

### “Local passes, CI fails”
- CI may run with mocked data or a minimal fixture environment — avoid relying on developer-only datasets
- Ensure your helpers use environment-driven base URLs and do not hardcode localhost ports

---

## 🤝 Contributing rules for this folder

- Keep helpers **small** and **composable**
- Prefer pure functions (easy to reuse + test)
- Put complex behavior behind a single exported helper (don’t repeat in tests)
- Add a short docstring/comment for any helper that enforces a “KFM invariant”

---

### 🔗 Related docs (repo root paths)
- `/docs/MASTER_GUIDE_v13.md`
- `/docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- `/src/server/contracts/` (canonical home for API contracts in v13)