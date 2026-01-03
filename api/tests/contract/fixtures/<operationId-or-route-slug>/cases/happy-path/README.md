# ✅ Contract Fixture — Happy Path

![contract-first](https://img.shields.io/badge/contract--first-enforced-blue)
![fixture](https://img.shields.io/badge/fixture-happy--path-brightgreen)
![openapi](https://img.shields.io/badge/OpenAPI-contract-orange)
![ci](https://img.shields.io/badge/CI-blocks--on--contract--break-red)

> According to a document from **2025-12-28**, KFM treats schemas/API specs as first-class contract artifacts, and CI runs API contract tests to prevent accidental breaking changes. [^kfm-master] [^kfm-contract-first] [^kfm-ci-contract]

---

## 🎯 Purpose

This folder is the canonical **happy-path** contract fixture for **`<operationId-or-route-slug>`**.

It represents the most common successful request shape (✅ 2xx) **and** the expected observable response contract:

- ✅ Request method + path + params + headers + body (as applicable)
- ✅ Expected HTTP status + response headers + response body
- ✅ Expected redaction/classification behavior at the API boundary (no “UI bypass”)

KFM’s pipeline explicitly places the **API layer (contracts + redaction)** between the graph and the UI. [^kfm-pipeline]

---

## 🧭 Endpoint mapping (fill this in)

| Item | Value |
|---|---|
| operationId | `<operationId>` |
| Route slug (folder name) | `<operationId-or-route-slug>` |
| Method | `<GET|POST|PUT|PATCH|DELETE>` |
| Path | `</v1/...>` |
| Expected status | `<200|201|204>` |
| Auth context | `<public|authenticated|service>` |
| Fixture dataset dependency | `<name/slug of seeded dataset (if any)>` |
| One-line intent | `<what this call does>` |

---

## 📁 Expected layout

```text
api/tests/contract/fixtures/
├─ 🧰  (root) Contract-test fixtures registry (all operations live under here)
└─ 🧩  <operationId-or-route-slug>/            Operation-specific fixture bundle (one endpoint/operation)
   └─ 🧪  cases/                               Scenario library for this operation (happy-path, errors, etc.)
      └─ ✅  happy-path/                       Success case (2xx) — the “golden” contract behavior
         ├─ 📘  README.md                      👈 you are here (rules + intent + how this case is validated)
         ├─ 📤  request.json                   ✅ required (normalized request: method/path/params/headers/body)
         ├─ 📥  response.json                  ✅ required (expected status/headers/body; public contract output)
         └─ 🧷  matchers.json                  ➕ optional (ignore/regex matchers for volatile fields like ids/timestamps)
```

---

## 📄 Fixture files

### `request.json` (required)

A complete request description **without environment-specific values**:

```json
{
  "method": "GET",
  "path": "/v1/replace/me",
  "headers": {
    "accept": "application/json"
  },
  "query": {
    "limit": 10
  },
  "pathParams": {
    "id": "example-id"
  },
  "body": null
}
```

**Rules ✅**
- Keep it **minimal but real**: required params + 1–2 meaningful optional params.
- No hostnames, no local ports, no env-specific toggles.
- Never commit real tokens/keys; use placeholders like:
  - `"Authorization": "Bearer <TEST_TOKEN>"`
  - `"x-api-key": "<TEST_KEY>"`  
  CI scans for secrets and sensitive content. [^kfm-security]

---

### `response.json` (required)

The expected *observable contract output* (what a client depends on):

```json
{
  "status": 200,
  "headers": {
    "content-type": "application/json"
  },
  "body": {
    "example": "replace me"
  }
}
```

**Rules ✅**
- Prefer deterministic outputs (see “Determinism checklist”).
- If the endpoint returns catalog/graph references, use stable IDs from the fixture dataset.

---

### `matchers.json` (optional)

Use matchers only when the API must return non-deterministic values (timestamps, request IDs, etc.).

```json
{
  "ignoreJsonPaths": [
    "$.body.requestId",
    "$.body.generatedAt"
  ],
  "regex": {
    "$.body.id": "^[a-f0-9-]{36}$"
  }
}
```

> If you’re ignoring many fields, it may mean the endpoint is leaking unstable internals into its public contract.

---

## ✅ What “happy-path” means here

This case should model:

- **Valid input** (passes validation + schema)
- **Expected authorization** for the intended audience (public/auth/service)
- **Successful response** (2xx)
- **Correct contract shape** (matches the OpenAPI/GraphQL schema)
- **Correct governance behavior** (redaction/classification enforced; no bypass)

KFM’s invariant is that the **UI must never query Neo4j directly**; access flows through the governed API boundary to enforce controls and consistency. [^kfm-api-boundary]

---

## 🎛️ Determinism checklist

Contract tests are only useful if they’re repeatable. KFM emphasizes deterministic behavior. [^kfm-determinism]

- [ ] No `now()` timestamps in the expected response (or matcher them)
- [ ] Stable IDs (seeded fixtures / deterministic UUIDs / fixed known IDs)
- [ ] Stable ordering (explicit sort order; never depend on DB default)
- [ ] Stable pagination defaults (explicit `limit`, `offset`/`cursor`)
- [ ] Stable float formatting (rounding policy; avoid raw float comparisons when not required)

---

## 🧯 Safety & governance rules (non-negotiable)

These fixtures are subject to CI gates, including security/governance scans:

- 🔒 **No secrets** (API keys, tokens, passwords). [^kfm-security]
- 🧑‍⚕️ **No PII / sensitive content** unless explicitly approved and properly handled. [^kfm-security]
- 🗺️ **No sensitive locations** unless generalized/withheld per sovereignty rules. [^kfm-security]
- 🏷️ **No classification downgrades** (outputs can’t be “less restricted” than inputs). [^kfm-classification]

If you need a sensitive example, create a **separate** case folder (not `happy-path/`) that asserts the correct **redaction** behavior instead.

---

## 🔁 When to update this fixture

Update this folder when:

- The OpenAPI/GraphQL contract changes (new fields, renamed fields, new defaults)
- The endpoint behavior changes (even if schema didn’t)
- Redaction/classification behavior at the API boundary changes

Breaking changes must be handled via **API versioning** (e.g., `/v1/...` → `/v2/...`), because the **OpenAPI definition is the contract** and breaking it requires incrementing the version. [^kfm-versioning]

---

## 🧩 Related workflow

- Use the API contract extension template when adding/changing endpoints (governed API change process). [^kfm-api-template]
- Keep fixtures aligned with CI contract testing; CI blocks merges when unexpected contract changes occur. [^kfm-ci-contract]

---

## 📚 Sources

[^kfm-master]: Master Guide v13 version history shows **v13.0.0-draft** dated **2025-12-28**.:contentReference[oaicite:0]{index=0}

[^kfm-contract-first]: Contract-first principle: schemas and API contracts are first-class artifacts, and changes trigger strict versioning/compatibility checks.:contentReference[oaicite:1]{index=1}

[^kfm-pipeline]: KFM pipeline diagram places **API Layer (contracts + redaction)** between graph and UI.:contentReference[oaicite:2]{index=2}

[^kfm-ci-contract]: CI runs API contract tests; OpenAPI/GraphQL schemas are linted; changes must be backwards-compatible or tests updated, otherwise CI blocks merge.:contentReference[oaicite:3]{index=3}

[^kfm-security]: CI includes security/governance scans for secrets, PII, sensitive locations, and classification consistency.:contentReference[oaicite:4]{index=4}

[^kfm-api-boundary]: API boundary rule: UI must not query Neo4j directly; all access goes through the governed API layer to enforce controls/redaction/schema consistency.:contentReference[oaicite:5]{index=5}

[^kfm-determinism]: Deterministic pipeline principle: stable outputs for given inputs (reproducibility).:contentReference[oaicite:6]{index=6}

[^kfm-classification]: Sovereignty/classification propagation: outputs cannot be less restricted than inputs (no downgrades).:contentReference[oaicite:7]{index=7}

[^kfm-versioning]: API versioning rule: breaking changes require a new versioned endpoint; OpenAPI definition is the contract and breaking it means incrementing the version.:contentReference[oaicite:8]{index=8}

[^kfm-api-template]: API contract extension template path for adding/changing endpoints is documented under `docs/templates/`.:contentReference[oaicite:9]{index=9}

