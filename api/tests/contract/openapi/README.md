# 🧪 OpenAPI Contract Tests (API)

![Contract Tests](https://img.shields.io/badge/tests-contract%20(OpenAPI)-blue)
![Contract-First](https://img.shields.io/badge/approach-contract--first-brightgreen)
![Backwards Compatible](https://img.shields.io/badge/API-backwards--compatible-important)
![KFM](https://img.shields.io/badge/project-KFM-lightgrey)

> [!IMPORTANT]
> In KFM, the **OpenAPI spec is a contract artifact** 📜  
> Treat it as a **first-class, versioned interface**. If you break it, you **must** bump versions and provide a migration path.

---

## 🎯 Why this folder exists

This directory contains **contract tests** that verify the running API stays aligned with the **OpenAPI contract**:

- ✅ The contract is valid (well-formed OpenAPI)
- ✅ The implementation matches the contract (status codes, schemas, response shapes)
- ✅ The API stays **backwards-compatible** unless a version bump is explicitly declared
- ✅ Any contract change is validated against **known inputs/outputs** (golden examples) to prevent silent drift

Contract tests are not “unit tests.” They sit closer to **integration testing**, but with a strict focus on **interface correctness** and **compatibility**.

---

## 🧭 Quick links

- 📌 **Master governance + contract conventions:** `docs/MASTER_GUIDE_v13.md`
- 🧩 **API contract change template:** `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

---

## 🗂️ What lives here

Suggested/typical layout (your repo may vary slightly):

```text
📦 api/
└─ 🧪 tests/
   └─ 🤝 contract/
      └─ 📜 openapi/
         ├─ ✅ README.md
         ├─ 🧾 cases/                  # "Known inputs/outputs" (golden requests + expected responses)
         ├─ 🧰 helpers/                # Shared HTTP / auth / assertion helpers
         ├─ ⚙️  config.*               # Base URL, contract path, auth strategy, timeouts
         └─ 🧪 test_openapi_*.py        # Contract test modules (or equivalent)
```

> [!TIP]
> If you don’t see `cases/` yet, add it. Contract changes should be pinned to at least one **golden** request/response so we detect regressions early.

---

## 📜 Where the OpenAPI contract comes from

Depending on how your service is wired, the contract may be:

- **Committed contract file** (preferred “contract-first”):
  - `src/server/contracts/openapi.yaml` (v13 canonical pattern), **or**
  - `api/contracts/openapi.yaml` / `api/openapi.yaml` (service-local pattern)
- **Runtime contract** exposed by the server (common with FastAPI):
  - served as JSON (often at a predictable endpoint like `/openapi.json`)

> [!NOTE]
> Even if the runtime spec is generated, we still treat the *contract* as a governed interface: **version it, test it, and keep it stable**.

---

## ✅ Prerequisites

Before running these tests, you typically need:

- 🟢 A running API instance (local dev server, docker-compose, or CI service container)
- 🔐 Any auth credentials required to hit protected endpoints
- 🧪 A test runner environment (commonly Python-based for KFM backend services)

---

## 🚀 Running locally

### 1) Start the API

Run the API using your normal dev workflow (examples only):

- `docker compose up api`
- or run the Python service directly (FastAPI/Flask, depending on implementation)

Make sure you know the **base URL** (example: `http://localhost:8000`).

---

### 2) Configure the test target

These tests should be runnable against **any environment** by setting configuration values.

Common environment variables (adjust names to match the repo’s conventions):

```bash
export KFM_API_BASE_URL="http://localhost:8000"
export KFM_OPENAPI_CONTRACT_PATH="src/server/contracts/openapi.yaml"   # or api/contracts/openapi.yaml
export KFM_API_AUTH_TOKEN="..."                                        # if required
```

> [!TIP]
> If you’re unsure where the contract file lives, search for `contracts/openapi` or `openapi.yaml` in the repo.

---

### 3) Run the OpenAPI contract tests

Example `pytest` invocations (adjust to your runner):

```bash
# Run only this folder
pytest api/tests/contract/openapi -q

# If the repo uses pytest markers (recommended):
pytest -m contract -q
```

---

## 🧪 What these tests should cover

### ✅ 1) Contract validity
We validate that the OpenAPI document is:

- parseable (YAML/JSON)
- structurally valid for the OpenAPI version
- internally consistent (refs resolve, schemas are coherent)

### ✅ 2) Implementation conformance
We validate the live API conforms to the contract, including:

- paths + HTTP methods exist as declared
- status codes match documented responses
- content-types match (`application/json`, etc.)
- response bodies validate against schemas
- required fields exist and types match
- error payloads are consistent and documented

### ✅ 3) Backwards compatibility
We treat backwards compatibility as a **default requirement**.

- Adding optional fields ✅
- Adding new endpoints ✅
- Making a previously optional field required ❌ (breaking)
- Removing/renaming fields or endpoints ❌ (breaking)

### ✅ 4) Known inputs/outputs (“golden cases”)
For every meaningful contract change, add/update at least one golden case:

- request (method, URL, headers, body)
- expected status code
- expected response schema + key fields (and optionally full-body snapshots)

This protects against:
- accidental schema drift
- behavior changes that still “look valid” structurally but break client assumptions

---

## ✍️ Making contract changes safely

When you add/change endpoints:

1. 🧩 Draft the change using the template:
   - `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
2. 📜 Update the OpenAPI contract (and version it correctly)
3. 🧾 Add/update golden cases in `cases/`
4. 🧪 Run:
   - unit tests
   - integration tests
   - **OpenAPI contract tests (this suite)**
5. 🧭 If breaking:
   - bump the API version
   - document migration steps for clients
   - consider supporting old + new versions in parallel if required

> [!IMPORTANT]
> “It works on my machine” is not a contract.  
> The contract is the OpenAPI spec + the tests that enforce it.

---

## 💥 What counts as a breaking change?

<details>
<summary><strong>Click to expand</strong> ⚠️</summary>

Breaking changes typically include:

- ❌ Removing an endpoint
- ❌ Renaming a path or changing an HTTP method
- ❌ Changing a response status code for an existing success path
- ❌ Removing a response field that clients may use
- ❌ Changing a field type (e.g., `string` → `number`)
- ❌ Changing semantics without versioning (same schema, different meaning)
- ❌ Tightening validation (making an optional field required, stricter enums) without a version bump
- ❌ Changing auth rules (public → auth required) without versioning/migration plan

</details>

---

## 🧯 Troubleshooting

### “Schema drift” failures (contract ≠ runtime)
- Ensure the API instance you’re testing is running the same commit / image you expect.
- If the runtime OpenAPI is generated, confirm it’s generated from the same source-of-truth assumptions as the committed contract.

### 401/403 failures
- Set the required token(s) / headers.
- If the environment uses a different auth provider, ensure the tests support that via configuration.

### Flaky tests
- Prefer deterministic golden cases over random data.
- If endpoints rely on time or async jobs, add stable polling rules and timeouts.

---

## ✅ CI expectations

These tests should run in CI on every PR that touches:

- API routes/handlers
- schemas/models
- the OpenAPI contract file(s)
- auth / middleware that changes request/response behavior

Contract tests are allowed to be strict. They exist to protect **clients**, **integrations**, and **downstream systems** from unannounced breaking changes.

---

## 🤝 Contributing checklist

- [ ] Contract updated (OpenAPI)
- [ ] Golden case added/updated
- [ ] Backwards compatibility considered (or version bumped)
- [ ] Contract suite passes locally + in CI
- [ ] Any client-facing change is documented

---