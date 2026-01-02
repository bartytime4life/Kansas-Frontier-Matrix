# 🧪 API Route Tests (`api/tests/routes/`)

![Scope](https://img.shields.io/badge/scope-api%2Ftests%2Froutes-blue)
![Level](https://img.shields.io/badge/test%20level-route%20%2F%20contract-informational)
![Determinism](https://img.shields.io/badge/deterministic-required-red)
![Governance](https://img.shields.io/badge/governance-redaction%20%2B%20classification-orange)
![CI Gate](https://img.shields.io/badge/CI-gated-success)

> **TL;DR** ✅ These tests protect the **API boundary**: request/response behavior, auth, schema/contract, and governance (redaction + classification).  
> Keep them **fast, deterministic, and evidence-first**. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🧭 Quick Nav

- [🎯 Purpose](#-purpose)
- [🧱 What belongs here](#-what-belongs-here)
- [🏗️ Architecture context](#️-architecture-context)
- [📁 Suggested layout](#-suggested-layout)
- [🚀 Running route tests](#-running-route-tests)
- [✍️ Writing a new route test](#️-writing-a-new-route-test)
- [🧷 Contract-first expectations](#-contract-first-expectations)
- [🔒 Governance + safety expectations](#-governance--safety-expectations)
- [✅ Definition of done](#-definition-of-done)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 References](#-references)

---

## 🎯 Purpose

Route tests exist to ensure that **the API behaves as a stable, governed contract**:

- ✅ Correct **status codes** and **error shapes**
- ✅ Correct **request validation** (query/path/body)
- ✅ Correct **response schema** (shape, types, required fields)
- ✅ Correct **auth/permissions** behavior
- ✅ Correct **governance enforcement** (redaction, classification rules)

KFM’s documentation emphasizes a **contract-first** approach (contracts are first-class artifacts) and CI gates that include **API contract tests** and **governance scans**. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

---

## 🧱 What belongs here

<details>
<summary><strong>✅ Yes: route boundary behavior</strong> (click to expand)</summary>

- Status codes: 200/201/204, 400/401/403/404/409/422, 500 shape
- Headers: `Content-Type`, caching headers, pagination headers if used
- Auth flows: missing token, expired token, wrong role
- Validation: required params, enum constraints, bounds checks
- Serialization: date/time formatting, geometry encoding, numeric precision expectations
- Contract drift: “endpoint still returns what clients rely on”

</details>

<details>
<summary><strong>🚫 No: deep business logic</strong> (click to expand)</summary>

- Core algorithms and domain rules → **service tests** (unit)  
- Database query correctness → **repository / integration tests**
- Large end-to-end flows across subsystems → **e2e/system tests** (elsewhere)

</details>

> [!NOTE]
> Route tests should treat internals as a black box unless you’re explicitly verifying boundary-only behavior (e.g., correct dependency injection wiring).

---

## 🏗️ Architecture context

KFM follows **Clean Architecture / SOLID** with a layered structure (API routes/controllers → services/use cases → models → repositories), and dependency inversion is used to make testing easier (swap in dummy implementations). :contentReference[oaicite:4]{index=4}

That means route tests should usually:

- Exercise the **API entrypoint** (router/controller) through an HTTP test client
- Mock/stub **outgoing dependencies** (DB, graph, external services) where feasible
- Keep fixtures small and deterministic (avoid “real internet”, avoid flakiness)

---

## 📁 Suggested layout

Actual structure may vary, but this is the recommended mental model:

```text
📦 api/ 🏗️
 └─ 🧪 tests/ 🧫
    └─ 🛣️ routes/ 🧭🧾
       ├─ 📘✨ README.md                 👈 you are here
       ├─ 🧩🧷 conftest.py               (shared fixtures)  # if Python
       ├─ 🧰🔧 _helpers/                 (factories, builders, schema asserts)
       ├─ 🩺🧯 test_health.*             (smoke routes)
       ├─ 🔐🛡️ test_auth.*               (auth + permissions)
       ├─ 🛰️🗂️ stac/                     (catalog routes)
       ├─ 🕸️🔗 graph/                    (Neo4j/ontology-facing routes)
       ├─ 🗺️🧱 layers/                   (map layers / tiles / vectors)
       └─ 📖✨ story_nodes/              (narrative content delivery routes)
```

> [!TIP]
> Keep files grouped by **feature surface** (catalog/graph/layers/story) rather than by HTTP method.

---

## 🚀 Running route tests

KFM’s CI is expected to run tests and block merges on failures (tests + linting + type checks, etc.). :contentReference[oaicite:5]{index=5}

### 🐍 Python (pytest-style)

```bash
# From repo root
python -m pytest api/tests/routes -q
```

Run a single file:

```bash
python -m pytest -q api/tests/routes/test_<something>.py
```

Run a single test node:

```bash
python -m pytest -svv api/tests/routes/test_<something>.py::test_<case_name>
```

Pytest supports running a single test by node id like `file.py::test_name`. :contentReference[oaicite:6]{index=6}

### 🟩 Node (jest/supertest-style)

```bash
# From repo root (adjust script name to match package.json)
npm test -- api/tests/routes
```

> [!NOTE]
> If the route tests need DB/Neo4j containers, prefer starting them via a test-only compose profile so local runs match CI.

---

## ✍️ Writing a new route test

### 1) Name it like a contract 📜

Examples:

- `test_stac_collections_list__happy_path`
- `test_story_node_get__redacts_sensitive_fields`
- `test_graph_query__rejects_invalid_cypher`

### 2) Use AAA (Arrange → Act → Assert) 🧩

**Arrange**
- Build request inputs (path params, query, body)
- Prepare fixtures (seeded DB rows, graph fixtures, fake services)

**Act**
- Call the route via the test client

**Assert**
- `status_code`
- response shape (keys/types)
- governance guarantees (no sensitive fields leaked)
- errors: stable error schema

### 3) Prefer “boundary asserts” over “internal asserts” 🧠

Instead of asserting internal method calls, assert what clients care about:

- `status_code`
- `error.code`
- `error.message` (stable-ish)
- required fields present
- redaction honored

---

## 🧷 Contract-first expectations

KFM treats schemas/contracts as first-class and expects CI to run **API contract tests** and lint OpenAPI/GraphQL schemas for completeness. :contentReference[oaicite:7]{index=7}

**Rule of thumb:**
- If you change an endpoint behavior (inputs/outputs), you must update:
  - ✅ the contract (OpenAPI/GraphQL/JSON schema)
  - ✅ the route tests that lock the contract
  - ✅ any downstream fixtures that depend on it

If you’re adding/changing endpoints, use the governed template path referenced by the Master Guide:

- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` :contentReference[oaicite:8]{index=8}

> [!IMPORTANT]
> “Undocumented behavior” is treated as a bug. Route tests should fail if the implementation drifts away from the contract.

---

## 🔒 Governance + safety expectations

The KFM pipeline is governed end-to-end, and CI includes scans for secrets/PII and checks that sensitive locations/coordinates are not exposed incorrectly, and that classifications are not downgraded improperly. :contentReference[oaicite:9]{index=9}

### ✅ What governance tests should cover

- **Redaction**
  - Sensitive fields removed or generalized
  - Geometry precision reduced when required
  - PII absent when a user lacks permission

- **Classification enforcement**
  - Confidential → never becomes “public” by accident
  - Role-based responses differ correctly (public vs steward vs admin)

- **No “freeform evidence”**
  - If an endpoint serves a derived artifact, ensure it references governed artifacts (STAC/DCAT/PROV lineage), not ad-hoc blobs (aligns with evidence-first expectations). :contentReference[oaicite:10]{index=10}

> [!TIP]
> Add explicit “negative leak” assertions:
> - `assert "precise_location" not in response_json`
> - `assert response_json["classification"] != "public"` (when expected)
> - `assert response_json["geometry"]["coordinates"]` are generalized (when required)

---

## ✅ Definition of done

Before you open a PR, your route-test change should satisfy:

- [ ] **Deterministic**: no network calls, stable outputs for stable inputs :contentReference[oaicite:11]{index=11}
- [ ] **Contract-aligned**: tests match schema/contract (OpenAPI/GraphQL) :contentReference[oaicite:12]{index=12}
- [ ] **Governance-safe**: redaction + classification behavior tested :contentReference[oaicite:13]{index=13}
- [ ] **CI-friendly**: fast, minimal fixtures, no long sleeps
- [ ] **Readable**: clear Arrange/Act/Assert, descriptive test names

---

## 🧯 Troubleshooting

### “It passes locally but fails in CI” 🧊

Common causes:

- Hidden dependency on local env vars / secrets
- Non-deterministic timestamps / random seeds
- Dependency on a running local DB/graph that CI doesn’t have

KFM QA guidance expects automated tests and CI gating to keep the repo stable. :contentReference[oaicite:14]{index=14}

### “My test is flaky” 🎲

- Freeze time (or inject time providers)
- Seed randomness
- Replace external calls with mocks/fixtures

Deterministic outputs are a core reproducibility expectation. :contentReference[oaicite:15]{index=15}

---

## 📚 References

- 📘 KFM Technical Documentation (architecture, CI expectations) :contentReference[oaicite:16]{index=16}  
- 🧭 KFM Master Guide / Markdown Guide v13 (contract-first, CI gates, governance checks) :contentReference[oaicite:17]{index=17}  
- 🧪 Clean Architectures in Python (pytest usage patterns) :contentReference[oaicite:18]{index=18}  
- 🧠 Scientific Method / Master Coder Protocol (QA + determinism principles) :contentReference[oaicite:19]{index=19}
