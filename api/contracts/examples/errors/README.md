---
title: "KFM API Error Contract Examples"
path: "api/contracts/examples/errors/README.md"
contract: "kfm.problem.v1"
status: "draft"
last_updated: "2026-01-24"
---

<!-- 📌 File: api/contracts/examples/errors/README.md -->

# 🔥 KFM API Error Contract Examples (REST + GraphQL)

![contract](https://img.shields.io/badge/contract-kfm.problem.v1-2563eb)
![format](https://img.shields.io/badge/format-RFC7807--ish-16a34a)
![governance](https://img.shields.io/badge/governance-OPA%2FConftest-7c3aed)
![ux](https://img.shields.io/badge/UX-plain_language%2Baccessible-f97316)

Canonical, copy/paste-able **error response examples** for the Kansas Frontier Matrix (KFM) API:
- 🌐 **FastAPI REST** (OpenAPI/Swagger)
- 🧬 **GraphQL** (knowledge graph traversal)
- 🤖 **AI / Focus Mode** (evidence-first + governance-gated)

These examples are used for:
- ✅ **contract tests** (don’t break clients)
- 🧩 **UI rendering** (consistent messages + accessibility)
- 📘 **docs & onboarding** (contributors see “what good looks like”)

> [!IMPORTANT]
> **Errors are part of the public contract.** Treat changes as semver-impacting: clients + UI depend on this shape.

---

## 🧭 Table of Contents
- [📦 What’s in this folder](#-whats-in-this-folder)
- [🧠 Contract principles](#-contract-principles)
- [🧯 The error envelope](#-the-error-envelope)
- [🧩 Policy & provenance extensions](#-policy--provenance-extensions)
- [🧪 HTTP examples](#-http-examples)
- [🧬 GraphQL examples](#-graphql-examples)
- [🖥️ UI rendering rules](#️-ui-rendering-rules)
- [🔐 Security & privacy rules](#-security--privacy-rules)
- [🧰 Adding a new error example](#-adding-a-new-error-example)
- [✅ Definition of Done](#-definition-of-done)

---

## 📦 What’s in this folder

Recommended layout (you can adjust filenames, but keep them predictable and grep-friendly):

```text
api/contracts/examples/errors/
├─ README.md
├─ http/
│  ├─ 400.validation.invalid_bbox.problem+json
│  ├─ 401.auth.missing_token.problem+json
│  ├─ 403.policy.denied_classification.problem+json
│  ├─ 404.data.not_found.problem+json
│  ├─ 409.data.etag_conflict.problem+json
│  ├─ 422.validation.body_schema.problem+json
│  ├─ 429.rate_limited.problem+json
│  ├─ 503.upstream.postgis_unavailable.problem+json
│  ├─ 503.upstream.neo4j_unavailable.problem+json
│  ├─ 422.ai.evidence_required.problem+json
│  └─ 409.artifact.signature_invalid.problem+json
└─ graphql/
   ├─ depth_limit.json
   ├─ policy_denied.json
   └─ evidence_required.json
```

> [!TIP]
> Put REST errors under `http/` using `application/problem+json` examples, and GraphQL under `graphql/` using the standard `{"data":..., "errors":[...]}` shape.

---

## 🧠 Contract principles

KFM’s error contract is shaped by a few non-negotiables:

- 🧾 **Provenance-first**: errors should help you trace what happened (request IDs, links to metadata/provenance when relevant).
- 🛡️ **Governance-first**: when something is denied, the response must be *machine-readable* (policy rule IDs, decision context) without leaking sensitive data.
- 🧑‍🏫 **UX-first**: payloads must be safe to show in the UI with plain language and accessible affordances (a human should understand the fix).
- 🧱 **API boundary**: the UI talks to KFM through APIs (REST/GraphQL); clients should never have to infer internal DB details from errors.

---

## 🧯 The error envelope

KFM uses an **RFC7807-style “Problem Details”** envelope with a few KFM extensions.

### ✅ Response headers (REST)
- `Content-Type: application/problem+json`
- `X-Request-Id: <request_id>` *(recommended)*
- `Cache-Control: no-store` *(recommended for errors involving auth/policy)*

### 📐 Required fields

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `type` | string (URI/URN) | ✅ | Stable problem identifier (use `urn:kfm:problem:<CODE>`). |
| `title` | string | ✅ | Short, human-friendly summary. |
| `status` | number | ✅ | HTTP status code. |
| `code` | string | ✅ | Stable KFM error code (clients branch on this). |
| `detail` | string | ⛔️ | Safe, plain-language description (no secrets). |
| `instance` | string | ⛔️ | Request path or instance pointer (e.g. `/api/search`). |
| `timestamp` | string (ISO-8601) | ✅ | UTC timestamp. |
| `request_id` | string | ✅ | Correlates logs + governance ledger. |
| `trace_id` | string | ⛔️ | For distributed tracing (optional but recommended). |
| `service` | string | ✅ | Origin service (e.g. `api`, `graph`, `ai`). |
| `retryable` | boolean | ⛔️ | Client hint: should the UI show a “Retry” CTA? |

### 🧱 Optional standard extensions

| Field | Type | When to use |
|---|---|---|
| `errors[]` | array | Validation issues (field-level, bbox, geometry, schema, etc.) |
| `policy` | object | Policy-denied / governance enforcement |
| `prov` | object | Provenance pointers (PROV/DCAT/STAC links) |
| `links[]` | array | “docs”, “support”, “dcat”, “stac”, “prov”, “run”, “artifact” |

---

## 🧩 Policy & provenance extensions

### `policy` object (OPA / governance)

Use this when access is denied, content is blocked, or outputs fail a governance check.

**Shape (example):**
```json
{
  "engine": "OPA",
  "pack": "policy-pack-v13",
  "decision": "deny",
  "decision_id": "opa_decision_01HTR8...",
  "rule_ids": ["KFM-CAT-001", "KFM-PROV-001"],
  "reasons": [
    { "rule_id": "KFM-CAT-001", "message": "Dataset classification is restricted." },
    { "rule_id": "KFM-PROV-001", "message": "Processed data changed without matching PROV update." }
  ]
}
```

### `prov` object (traceability)

Use this when the error relates to **data lineage**, **ingest**, **pipelines**, **AI outputs**, or **artifact verification**.

**Shape (example):**
```json
{
  "activity_id": "prov:activity:ingest_2026_01_24_001",
  "entity_id": "prov:entity:kfm.dataset.ks.landcover.v3",
  "links": [
    { "rel": "dcat", "href": "/data/catalog/dcat/kfm.dataset.ks.landcover.v3.jsonld" },
    { "rel": "stac", "href": "/data/catalog/stac/kfm.dataset.ks.landcover.v3/collection.json" },
    { "rel": "prov", "href": "/data/prov/kfm.dataset.ks.landcover.v3.prov.json" }
  ]
}
```

---

## 🧪 HTTP examples

> [!NOTE]
> These are **examples**. Use your real endpoint paths, dataset IDs, and rule IDs when you generate actual fixtures.

### 400 — Invalid bbox (geospatial parameter validation)

<details>
<summary><strong>📄 http/400.validation.invalid_bbox.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.VALIDATION.INVALID_BBOX",
  "title": "Invalid request parameter",
  "status": 400,
  "code": "KFM.VALIDATION.INVALID_BBOX",
  "detail": "bbox must be 4 numbers in WGS84 order [minLon, minLat, maxLon, maxLat].",
  "instance": "/api/search",
  "timestamp": "2026-01-24T19:21:05Z",
  "request_id": "req_01HTR8C3K0ZQ2P7M3W4Y0QX9Q1",
  "trace_id": "trace_8f3a2c1d9b1c4a4a",
  "service": "api",
  "retryable": false,
  "errors": [
    { "path": "bbox[2]", "rule": "range", "message": "must be <= 180", "value": 220 },
    { "path": "bbox[3]", "rule": "range", "message": "must be <= 90", "value": 120 }
  ],
  "links": [
    { "rel": "docs", "href": "/docs/api#search" }
  ]
}
```
</details>

---

### 401 — Missing token (authentication)

<details>
<summary><strong>📄 http/401.auth.missing_token.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.AUTH.UNAUTHENTICATED",
  "title": "Authentication required",
  "status": 401,
  "code": "KFM.AUTH.UNAUTHENTICATED",
  "detail": "This endpoint requires a valid access token.",
  "instance": "/api/ingest",
  "timestamp": "2026-01-24T19:23:01Z",
  "request_id": "req_01HTR8D0JXH9Y8G7W2D1Q4B2K0",
  "trace_id": "trace_2bd4c613a6b047de",
  "service": "api",
  "retryable": false,
  "links": [
    { "rel": "docs", "href": "/docs/auth" }
  ]
}
```
</details>

---

### 403 — Policy denied (classification / CARE / FAIR governance)

<details>
<summary><strong>📄 http/403.policy.denied_classification.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.GOV.POLICY_DENIED",
  "title": "Access denied by policy",
  "status": 403,
  "code": "KFM.GOV.POLICY_DENIED",
  "detail": "You do not have permission to access this resource.",
  "instance": "/api/datasets/kfm.dataset.ks.sensitive_sites.v1",
  "timestamp": "2026-01-24T19:25:44Z",
  "request_id": "req_01HTR8F0Y9K5Y3D8C2C2H1M9Q7",
  "trace_id": "trace_8bbcf8f2ab8d4c1e",
  "service": "api",
  "retryable": false,
  "policy": {
    "engine": "OPA",
    "pack": "policy-pack-v13",
    "decision": "deny",
    "decision_id": "opa_decision_01HTR8F0Y9K5Y3D8C2C2H1M9Q7",
    "rule_ids": ["KFM-CAT-001"],
    "reasons": [
      { "rule_id": "KFM-CAT-001", "message": "Dataset classification is restricted." }
    ]
  },
  "links": [
    { "rel": "docs", "href": "/docs/governance/classification" }
  ]
}
```
</details>

---

### 404 — Dataset not found

<details>
<summary><strong>📄 http/404.data.not_found.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.DATA.NOT_FOUND",
  "title": "Resource not found",
  "status": 404,
  "code": "KFM.DATA.NOT_FOUND",
  "detail": "No dataset exists with the provided identifier.",
  "instance": "/api/datasets/kfm.dataset.ks.nope.v1",
  "timestamp": "2026-01-24T19:28:10Z",
  "request_id": "req_01HTR8GJ3T0Z6JY9Q1N8R2K7P3",
  "trace_id": "trace_0a2c8e8d4e2d4fd1",
  "service": "api",
  "retryable": false
}
```
</details>

---

### 409 — ETag conflict (optimistic concurrency)

<details>
<summary><strong>📄 http/409.data.etag_conflict.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.DATA.CONFLICT",
  "title": "Update conflict",
  "status": 409,
  "code": "KFM.DATA.ETAG_MISMATCH",
  "detail": "The resource changed since you last fetched it. Re-fetch and retry with the latest ETag.",
  "instance": "/api/story_nodes/prairie_fire_story",
  "timestamp": "2026-01-24T19:31:02Z",
  "request_id": "req_01HTR8J4FQ9R3M0Q8J3B7Y1X2Z",
  "trace_id": "trace_4c10f5e9a7d9494b",
  "service": "api",
  "retryable": true,
  "links": [
    { "rel": "docs", "href": "/docs/api#story-nodes" }
  ]
}
```
</details>

---

### 422 — Body schema validation (Pydantic / JSON schema)

<details>
<summary><strong>📄 http/422.validation.body_schema.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.VALIDATION.BODY_SCHEMA",
  "title": "Request body validation failed",
  "status": 422,
  "code": "KFM.VALIDATION.BODY_SCHEMA",
  "detail": "One or more fields are invalid.",
  "instance": "/api/ingest",
  "timestamp": "2026-01-24T19:33:19Z",
  "request_id": "req_01HTR8KQH1Z6P7X0V0G3Q0P4Y1",
  "trace_id": "trace_93f7b4b8b1b64a63",
  "service": "api",
  "retryable": false,
  "errors": [
    { "path": "dataset_id", "rule": "required", "message": "field is required" },
    { "path": "source_url", "rule": "format", "message": "must be a valid URL", "value": "not-a-url" }
  ],
  "links": [
    { "rel": "docs", "href": "/docs/api#ingest" }
  ]
}
```
</details>

---

### 429 — Rate limited (throttling)

<details>
<summary><strong>📄 http/429.rate_limited.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.RATE_LIMITED",
  "title": "Too many requests",
  "status": 429,
  "code": "KFM.RATE_LIMITED",
  "detail": "Please slow down and retry after the specified interval.",
  "instance": "/api/search",
  "timestamp": "2026-01-24T19:35:02Z",
  "request_id": "req_01HTR8M2C8D2M7F6X1G0A3V9N8",
  "trace_id": "trace_0f7c8de2f1b34c95",
  "service": "api",
  "retryable": true,
  "links": [
    { "rel": "docs", "href": "/docs/api#rate-limits" }
  ]
}
```
</details>

---

### 503 — Upstream unavailable (PostGIS)

<details>
<summary><strong>📄 http/503.upstream.postgis_unavailable.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.UPSTREAM.UNAVAILABLE",
  "title": "Upstream service unavailable",
  "status": 503,
  "code": "KFM.UPSTREAM.POSTGIS_UNAVAILABLE",
  "detail": "A required geospatial service is temporarily unavailable. Please retry.",
  "instance": "/api/search",
  "timestamp": "2026-01-24T19:36:41Z",
  "request_id": "req_01HTR8N4H2T0B6K9Z7A1V0X2C1",
  "trace_id": "trace_48a3f1f5d0b84414",
  "service": "api",
  "retryable": true,
  "links": [
    { "rel": "status", "href": "/status" }
  ]
}
```
</details>

---

### 503 — Upstream unavailable (Neo4j)

<details>
<summary><strong>📄 http/503.upstream.neo4j_unavailable.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.UPSTREAM.UNAVAILABLE",
  "title": "Upstream service unavailable",
  "status": 503,
  "code": "KFM.UPSTREAM.NEO4J_UNAVAILABLE",
  "detail": "A required knowledge-graph service is temporarily unavailable. Please retry.",
  "instance": "/graphql",
  "timestamp": "2026-01-24T19:37:22Z",
  "request_id": "req_01HTR8NQJ7S9T2H7M1P0K4X8R2",
  "trace_id": "trace_89b00b6b9b5b4c48",
  "service": "graph",
  "retryable": true,
  "links": [
    { "rel": "status", "href": "/status" }
  ]
}
```
</details>

---

### 422 — AI evidence required (Focus Mode hard gate)

Use when an AI endpoint cannot provide an evidence-backed response and policy requires refusal.

<details>
<summary><strong>📄 http/422.ai.evidence_required.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.AI.EVIDENCE_REQUIRED",
  "title": "Insufficient evidence to answer",
  "status": 422,
  "code": "KFM.AI.EVIDENCE_REQUIRED",
  "detail": "No supporting sources were found in the KFM catalogs for this request. Provide more context or narrow the query.",
  "instance": "/api/focus",
  "timestamp": "2026-01-24T19:40:11Z",
  "request_id": "req_01HTR8Q3E1M2Z9C3G5J6D7P8V1",
  "trace_id": "trace_5b9f1a4f2a6e4b12",
  "service": "ai",
  "retryable": false,
  "policy": {
    "engine": "OPA",
    "pack": "policy-pack-v13",
    "decision": "deny",
    "decision_id": "opa_decision_01HTR8Q3E1M2Z9C3G5J6D7P8V1",
    "rule_ids": ["KFM-AI-001"],
    "reasons": [
      { "rule_id": "KFM-AI-001", "message": "AI output must be evidence-backed with citations." }
    ]
  },
  "links": [
    { "rel": "docs", "href": "/docs/focus-mode#evidence" }
  ]
}
```
</details>

---

### 409 — Artifact signature invalid (OCI/ORAS + Cosign)

Use when a content-addressed artifact fails verification (digest mismatch, missing signature, invalid signature).

<details>
<summary><strong>📄 http/409.artifact.signature_invalid.problem+json</strong></summary>

```json
{
  "type": "urn:kfm:problem:KFM.ARTIFACT.SIGNATURE_INVALID",
  "title": "Artifact verification failed",
  "status": 409,
  "code": "KFM.ARTIFACT.SIGNATURE_INVALID",
  "detail": "The requested artifact could not be verified. The system will not serve untrusted or tampered content.",
  "instance": "/api/artifacts/oci/kfm.dataset.ks.air_quality.nowcast@sha256:deadbeef...",
  "timestamp": "2026-01-24T19:42:58Z",
  "request_id": "req_01HTR8RZC9X1V4M7D2N5Q8P3K6",
  "trace_id": "trace_2a4d1bcf4e7e4b78",
  "service": "api",
  "retryable": false,
  "prov": {
    "activity_id": "prov:activity:artifact_verify_2026_01_24_004",
    "entity_id": "prov:entity:oci:kfm.dataset.ks.air_quality.nowcast@sha256:deadbeef",
    "links": [
      { "rel": "artifact", "href": "/data/artifacts/kfm.dataset.ks.air_quality.nowcast" },
      { "rel": "prov", "href": "/data/prov/artifacts/kfm.dataset.ks.air_quality.nowcast.prov.json" }
    ]
  },
  "links": [
    { "rel": "docs", "href": "/docs/artifacts#verification" }
  ]
}
```
</details>

---

## 🧬 GraphQL examples

GraphQL responses follow the standard shape:

- `data` MAY be `null` if the operation fails
- `errors[]` contains error objects
- We standardize `errors[].extensions.code` to match the REST `code`

### Depth limit / expensive query blocked

<details>
<summary><strong>📄 graphql/depth_limit.json</strong></summary>

```json
{
  "data": null,
  "errors": [
    {
      "message": "Query is too complex.",
      "extensions": {
        "code": "KFM.GRAPHQL.DEPTH_LIMIT",
        "status": 400,
        "request_id": "req_01HTR8T5D1A4N7V9B3C5M1Q6Z8",
        "retryable": false,
        "limits": {
          "max_depth": 10,
          "observed_depth": 17
        }
      }
    }
  ]
}
```
</details>

### Policy denied (GraphQL)

<details>
<summary><strong>📄 graphql/policy_denied.json</strong></summary>

```json
{
  "data": null,
  "errors": [
    {
      "message": "Access denied by policy.",
      "extensions": {
        "code": "KFM.GOV.POLICY_DENIED",
        "status": 403,
        "request_id": "req_01HTR8V2F0P7K6C2Y9D8A1R4W3",
        "retryable": false,
        "policy": {
          "engine": "OPA",
          "pack": "policy-pack-v13",
          "decision": "deny",
          "decision_id": "opa_decision_01HTR8V2F0P7K6C2Y9D8A1R4W3",
          "rule_ids": ["KFM-CAT-001"],
          "reasons": [
            { "rule_id": "KFM-CAT-001", "message": "Dataset classification is restricted." }
          ]
        }
      }
    }
  ]
}
```
</details>

---

## 🖥️ UI rendering rules

KFM’s UI emphasizes **clarity, accessibility, and provenance**. Error payloads should support these patterns:

### 🎯 Where errors show up
- **Inline** (preferred): validation errors (400/422) → highlight the field + show `errors[]` messages
- **Toast / banner**: transient issues (429, retryable 503) → show “Retry” button if `retryable=true`
- **Blocking modal**: auth/policy gating (401/403) → offer sign-in or “Request Access” flow
- **Context panel**: provenance/policy issues → show `policy.reasons[]` and link to `prov.links[]` if present

### 🧠 Message tone
- ✅ “What happened” in `title`
- ✅ “How to fix” in `detail`
- ❌ Avoid internal stack traces, SQL/Cypher fragments, or secret values

> [!TIP]
> If the UI can’t safely show a technical detail to the public, it doesn’t belong in `detail`. Put it in **server logs**, correlated by `request_id`.

---

## 🔐 Security & privacy rules

**MUST NOT** include:
- tokens / secrets
- raw query text containing sensitive values
- internal hostnames, service topology, stack traces (unless explicitly gated to internal users)

**SHOULD** include:
- stable `code` for client branching
- `request_id` (always)
- policy rule IDs (when denied)
- links to docs or provenance where helpful

**Policy-denied behavior (important):**
- Prefer “not authorized” over confirming existence of restricted resources
- For sensitive geo data, return generalized errors (and keep details behind policy)

---

## 🧰 Adding a new error example

### 1) Pick a stable code 🏷️
Convention:
- `KFM.<DOMAIN>.<NAME>`
- Examples:
  - `KFM.VALIDATION.INVALID_BBOX`
  - `KFM.AUTH.UNAUTHENTICATED`
  - `KFM.GOV.POLICY_DENIED`
  - `KFM.UPSTREAM.POSTGIS_UNAVAILABLE`
  - `KFM.AI.EVIDENCE_REQUIRED`

### 2) Add a fixture file 📄
- REST → `http/<status>.<domain>.<name>.problem+json`
- GraphQL → `graphql/<name>.json`

### 3) Keep the shape consistent 🧱
- `type`, `title`, `status`, `code`, `timestamp`, `request_id`, `service` should exist in every REST example
- Use `errors[]`, `policy`, `prov`, `links[]` only when relevant

### 4) Wire into tests ✅
- Contract tests should validate:
  - required fields exist
  - `code` is stable + documented
  - no banned fields leak (tokens, stack traces, internal hosts)

---

## ✅ Definition of Done

- [ ] Example uses the **kfm.problem.v1** envelope (REST) or standard GraphQL `errors[]`
- [ ] `code` is stable, descriptive, and matches naming conventions
- [ ] No secrets / no internal stack traces
- [ ] `request_id` included
- [ ] Policy denials include `policy.rule_ids[]` + safe `policy.reasons[]`
- [ ] Provenance-related failures include `prov.links[]` when applicable
- [ ] UI can render the message in **plain language** (accessible and non-jargony)
- [ ] Contract tests updated (or test plan documented)

---
