# 🧩 KFM API v1 — Problem Details Examples (`application/problem+json`)

![status](https://img.shields.io/badge/status-draft-orange)
![contract](https://img.shields.io/badge/contracts-v1-blue)
![content-type](https://img.shields.io/badge/Content--Type-application%2Fproblem%2Bjson-4c1)
![style](https://img.shields.io/badge/style-contract--first%20%2B%20provenance--first-7b2cbf)

> [!IMPORTANT]
> KFM is **contract-first + provenance-first** (“no mystery layers”), and the UI is **decoupled** from the back-end via **REST + GraphQL**.  
> That combo makes *consistent, safe, machine-readable error payloads* non-negotiable. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🎯 What this folder is

This directory holds **canonical examples** of KFM API v1 error responses formatted as **Problem Details** JSON:

- ✅ predictable fields for clients (web UI, mobile, offline/AR clients)
- ✅ human-friendly `title/detail` + machine-friendly `type/code/errors[]`
- ✅ safe-by-default (no secrets, no sensitive location leaks, no stack traces)
- ✅ governance-aware (policy denials, provenance gates, query auditing)

KFM’s API layer is designed as the governed “middle layer” (**the UI must not bypass it**) and is expected to enforce validation + governance before anything becomes visible in UI/graph/story/AI flows. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

---

## 📦 Directory layout (recommended)

```text
api/contracts/examples/responses/v1/problem+json/
├─ README.md                               👈 you are here
├─ 400.validation-failed.json              ✅ invalid request (schema/params)
├─ 401.authentication-required.json        🔐 missing/invalid auth
├─ 403.policy-denied.json                  🛡️ governance/policy denial
├─ 404.not-found.json                      🕵️ missing resource
├─ 409.conflict.json                       🔁 version/idempotency conflict
├─ 422.provenance-required.json            🧾 evidence-triplet missing/incomplete
├─ 429.rate-limited.json                   🧯 throttle/rate limit
├─ 503.upstream-unavailable.json           🧱 dependency outage (graph/db/tiles)
└─ 500.internal-error.json                 💥 unexpected server error
```

> [!NOTE]
> You can keep examples as standalone JSON files (for OpenAPI examples + SDK tests), *and/or* embed them in this README for quick scanning.

---

## 🧠 Why Problem Details in KFM?

### 1) The API is the contract boundary
- KFM’s backend is described as a **stateless FastAPI service**, with **OpenAPI/Swagger** docs for REST and a **GraphQL schema** for semantic queries. :contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}
- The **web UI** is explicitly **decoupled** and communicates via **REST/GraphQL** endpoints. :contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}

### 2) Provenance is a gate, not a garnish 🧾
KFM requires an “**evidence triplet**” (**STAC + DCAT + PROV**) before data is “officially part of the platform” (“evidence-first publishing”). :contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}

### 3) Governance is policy-as-code (fail closed) 🛡️
KFM’s governance model uses **OPA/Rego + Conftest** “policy gates” in CI, and explicitly promotes a **fail-closed** posture. :contentReference[oaicite:10]{index=10}:contentReference[oaicite:11]{index=11}

### 4) Multiple clients (web, mobile, offline packs, AR) need one error language 📱🗺️
KFM’s roadmap and UI concept include mobile/offline packs and AR clients that reuse the same APIs. Consistent error contracts matter even more when you have “new front-end clients drawing from the same well-governed source.” :contentReference[oaicite:12]{index=12}:contentReference[oaicite:13]{index=13}

---

## 🧱 Contract: base Problem Details shape

KFM uses the common Problem Details members:

| Field | Type | Meaning |
|---|---:|---|
| `type` | string (URI) | Stable identifier for the problem class (e.g., `…/provenance-required`) |
| `title` | string | Human-readable short title |
| `status` | integer | HTTP status code |
| `detail` | string | Human-readable explanation (safe + non-sensitive) |
| `instance` | string (URI-ref) | Identifies this *specific occurrence* (often request path + request id) |

> [!TIP]
> `type` is what client code switches on. `title/detail` are what humans see.

---

## 🧬 KFM extensions (recommended)

Problem Details allows extra fields. KFM namespaces extensions under a single object to avoid collisions:

### ✅ `kfm` object (top-level extension)

| Field | Type | Example | Notes |
|---|---:|---|---|
| `kfm.code` | string | `KFM-PROV-001` | Stable internal code (maps to policy + validation catalogs) |
| `kfm.request_id` | string | `01HX…` / UUID | Correlation id (also in headers) |
| `kfm.trace_id` | string | W3C traceparent / UUID | Distributed tracing |
| `kfm.timestamp` | string (RFC3339) | `2026-01-24T18:03:45Z` | When the error was produced |
| `kfm.service` | string | `kfm-api` | Service emitting the error |
| `kfm.component` | string | `datasets` / `graph` / `tiles` | Owning domain |
| `kfm.errors[]` | array | see below | Field-level validation problems |
| `kfm.policy` | object | see below | Present for governance denials / redactions |
| `kfm.provenance` | object | see below | Present for provenance gates |
| `kfm.retry` | object | see below | Present for 429/503 retryable scenarios |
| `kfm.remediation` | object | see below | Optional “what to do next” (safe + non-sensitive) |

### 🔎 `kfm.errors[]` item shape (validation granularity)

| Field | Type | Example |
|---|---:|---|
| `code` | string | `KFM-API-VAL-003` |
| `message` | string | `"bbox must contain 4 numbers"` |
| `path` | string | `"query.bbox"` / `"body.dataset.license"` |
| `expected` | string | `"xmin,ymin,xmax,ymax"` |
| `received` | string | `"1,2,3"` |
| `hint` | string | `"See docs for bbox format"` |

---

## 🛡️ Safety + privacy rules (KFM-aligned)

> [!WARNING]
> **Never** include secrets, stack traces, SQL, internal hostnames, or sensitive coordinates in `detail` or `kfm.*`.

KFM’s design explicitly anticipates:
- **classification-aware filtering** (e.g., API may omit sensitive stations unless authorized) :contentReference[oaicite:14]{index=14}
- **geo-obfuscation / generalized coordinates** for sensitive records (differential access) :contentReference[oaicite:15]{index=15}
- **query auditing / inference control** where dangerous queries can be denied to prevent disclosure :contentReference[oaicite:16]{index=16}

So:
- for policy denials, prefer **403** with a safe explanation (“Denied by policy”) + structured reasons (non-sensitive).
- if a request might leak via inference, return **403** type `…/inference-risk` (optional) and log the specifics server-side.

---

## 🗺️ Status → problem type mapping (v1)

| HTTP | `type` slug | Example filename | Typical cause |
|---:|---|---|---|
| 400 | `invalid-request` | `400.validation-failed.json` | Malformed input, invalid params, schema mismatch |
| 401 | `authentication-required` | `401.authentication-required.json` | Missing/invalid token |
| 403 | `policy-denied` | `403.policy-denied.json` | Governance rule denial, sovereignty/CARE restrictions |
| 404 | `not-found` | `404.not-found.json` | Dataset/node not present |
| 409 | `conflict` | `409.conflict.json` | Version conflict / idempotency collision |
| 422 | `provenance-required` | `422.provenance-required.json` | Evidence triplet missing/incomplete |
| 429 | `rate-limited` | `429.rate-limited.json` | Throttle |
| 503 | `upstream-unavailable` | `503.upstream-unavailable.json` | PostGIS/Neo4j/tiles down |
| 500 | `internal-error` | `500.internal-error.json` | Unhandled server error |

---

## 🧪 Examples (inline)

> [!NOTE]
> These payloads are **illustrative**. Replace IDs/timestamps in real responses.

<details>
<summary><strong>400 — Validation Failed ✅</strong></summary>

```http
HTTP/1.1 400 Bad Request
Content-Type: application/problem+json
X-Request-Id: 01J0KFM9E7Y7J2Q9C9T2X9A3QH
```

```json
{
  "type": "https://kfm.dev/problems/invalid-request",
  "title": "Invalid request",
  "status": 400,
  "detail": "One or more request parameters failed validation.",
  "instance": "/api/v1/tiles?bbox=1,2,3",
  "kfm": {
    "code": "KFM-API-VAL-001",
    "request_id": "01J0KFM9E7Y7J2Q9C9T2X9A3QH",
    "trace_id": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
    "timestamp": "2026-01-24T18:03:45Z",
    "service": "kfm-api",
    "component": "tiles",
    "errors": [
      {
        "code": "KFM-API-VAL-003",
        "message": "bbox must contain 4 comma-separated numbers",
        "path": "query.bbox",
        "expected": "xmin,ymin,xmax,ymax",
        "received": "1,2,3",
        "hint": "Provide 4 values: xmin,ymin,xmax,ymax"
      }
    ]
  }
}
```
</details>

<details>
<summary><strong>401 — Authentication Required 🔐</strong></summary>

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/problem+json
WWW-Authenticate: Bearer realm="kfm", error="invalid_token"
X-Request-Id: 01J0KFMAB2R3Y3Y6R1B0Q0Q5W2
```

```json
{
  "type": "https://kfm.dev/problems/authentication-required",
  "title": "Authentication required",
  "status": 401,
  "detail": "A valid access token is required for this endpoint.",
  "instance": "/api/v1/datasets/kfm.ks.private.sites",
  "kfm": {
    "code": "KFM-AUTH-401",
    "request_id": "01J0KFMAB2R3Y3Y6R1B0Q0Q5W2",
    "timestamp": "2026-01-24T18:05:12Z",
    "service": "kfm-api",
    "component": "datasets",
    "auth": {
      "scheme": "Bearer",
      "required_scopes": ["datasets:read"]
    }
  }
}
```
</details>

<details>
<summary><strong>403 — Policy Denied 🛡️</strong></summary>

KFM governance includes **differential access** patterns (classification-aware filtering, CARE/sensitivity rules, and “fail closed” gates). :contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}

```http
HTTP/1.1 403 Forbidden
Content-Type: application/problem+json
X-Request-Id: 01J0KFMBBEJ9Y2JZQ0R5QJ6H0Z
```

```json
{
  "type": "https://kfm.dev/problems/policy-denied",
  "title": "Forbidden",
  "status": 403,
  "detail": "Access to the requested resource is denied by governance policy.",
  "instance": "/api/v1/datasets/kfm.ks.sacred_sites.full",
  "kfm": {
    "code": "KFM-POLICY-403",
    "request_id": "01J0KFMBBEJ9Y2JZQ0R5QJ6H0Z",
    "timestamp": "2026-01-24T18:06:01Z",
    "service": "kfm-api",
    "component": "datasets",
    "policy": {
      "pack": "kfm-policy-pack",
      "decision": "deny",
      "reasons": [
        "classification=culturally_sensitive",
        "role=public not permitted"
      ],
      "care_labels": ["culturally_sensitive"],
      "redaction_hint": "Request an approved generalized dataset instead (if available)."
    }
  }
}
```
</details>

<details>
<summary><strong>422 — Provenance Required 🧾</strong></summary>

KFM expects the **STAC + DCAT + PROV** “evidence triplet” before graph/UI use (“evidence-first publishing”). :contentReference[oaicite:19]{index=19}:contentReference[oaicite:20]{index=20}

```http
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/problem+json
X-Request-Id: 01J0KFMC7P0T7QFJ5GQJ5PZ6K9
```

```json
{
  "type": "https://kfm.dev/problems/provenance-required",
  "title": "Provenance required",
  "status": 422,
  "detail": "This operation requires STAC, DCAT, and PROV metadata for auditability and traceability.",
  "instance": "/api/v1/ingest/runPipeline",
  "kfm": {
    "code": "KFM-PROV-001",
    "request_id": "01J0KFMC7P0T7QFJ5GQJ5PZ6K9",
    "timestamp": "2026-01-24T18:08:44Z",
    "service": "kfm-api",
    "component": "ingest",
    "provenance": {
      "required_artifacts": ["stac", "dcat", "prov"],
      "missing": ["prov"],
      "catalog_paths_hint": [
        "data/stac/<id>.json",
        "data/catalogs/<id>.json",
        "data/prov/<run_id>.jsonld"
      ]
    },
    "errors": [
      {
        "code": "KFM-PROV-001",
        "message": "Processed data changed without matching PROV update.",
        "path": "body.provenance",
        "hint": "Attach or generate a PROV record describing inputs, transforms, and outputs."
      }
    ]
  }
}
```

> [!TIP]
> The CI/policy toolchain is designed to fail builds on provenance/policy violations (fail closed). :contentReference[oaicite:21]{index=21}

</details>

<details>
<summary><strong>409 — Conflict (Idempotency / Version) 🔁</strong></summary>

KFM’s audit/run manifests can be **canonicalized + hashed** (RFC 8785) and used as **idempotency keys**. :contentReference[oaicite:22]{index=22}

```http
HTTP/1.1 409 Conflict
Content-Type: application/problem+json
X-Request-Id: 01J0KFMDQ8D2JRB2V3X6Y7P2S1
```

```json
{
  "type": "https://kfm.dev/problems/conflict",
  "title": "Conflict",
  "status": 409,
  "detail": "An identical ingest operation was already recorded; use the existing run_id or change inputs.",
  "instance": "/api/v1/ingest/runPipeline",
  "kfm": {
    "code": "KFM-INGEST-409",
    "request_id": "01J0KFMDQ8D2JRB2V3X6Y7P2S1",
    "timestamp": "2026-01-24T18:09:22Z",
    "service": "kfm-api",
    "component": "ingest",
    "manifest": {
      "idempotency_key": "sha256:7b0a2d4e…",
      "canonical_digest": "sha256:7b0a2d4e…",
      "existing_run_id": "run_01J0KFM2KZ8J8H0Z5G8JY0D9D4"
    },
    "remediation": {
      "next_steps": [
        "Fetch status via GET /api/v1/pipelines/status?run_id=run_…",
        "If you intended a new run, modify inputs/config so the manifest digest changes."
      ]
    }
  }
}
```
</details>

<details>
<summary><strong>429 — Rate Limited 🧯</strong></summary>

KFM’s API design includes throttling/rate limiting expectations. :contentReference[oaicite:23]{index=23}

```http
HTTP/1.1 429 Too Many Requests
Content-Type: application/problem+json
Retry-After: 30
X-Request-Id: 01J0KFMES0N1A7V9E6J0W0Y3R7
```

```json
{
  "type": "https://kfm.dev/problems/rate-limited",
  "title": "Too many requests",
  "status": 429,
  "detail": "Request rate exceeded; retry after the suggested delay.",
  "instance": "/api/v1/search?q=dust%20bowl",
  "kfm": {
    "code": "KFM-API-RATE-429",
    "request_id": "01J0KFMES0N1A7V9E6J0W0Y3R7",
    "timestamp": "2026-01-24T18:10:55Z",
    "service": "kfm-api",
    "component": "search",
    "retry": {
      "retry_after_seconds": 30,
      "retryable": true
    }
  }
}
```
</details>

<details>
<summary><strong>503 — Upstream Unavailable 🧱</strong></summary>

```http
HTTP/1.1 503 Service Unavailable
Content-Type: application/problem+json
Retry-After: 10
X-Request-Id: 01J0KFMFZ1Q1X5R1F7S2E9Z8G0
```

```json
{
  "type": "https://kfm.dev/problems/upstream-unavailable",
  "title": "Service unavailable",
  "status": 503,
  "detail": "A required dependency is unavailable. Please retry.",
  "instance": "/api/v1/graph/query",
  "kfm": {
    "code": "KFM-UPSTREAM-503",
    "request_id": "01J0KFMFZ1Q1X5R1F7S2E9Z8G0",
    "timestamp": "2026-01-24T18:12:03Z",
    "service": "kfm-api",
    "component": "graph",
    "upstream": [
      { "name": "neo4j", "status": "unhealthy" }
    ],
    "retry": {
      "retry_after_seconds": 10,
      "retryable": true
    }
  }
}
```
</details>

---

## 🧬 GraphQL interoperability (optional pattern)

KFM supports GraphQL for graph traversals. When a GraphQL call fails, keep GraphQL-compliant errors **and** include a Problem Details payload in `extensions.problem` so clients can reuse the same parsing. :contentReference[oaicite:24]{index=24}:contentReference[oaicite:25]{index=25}

```json
{
  "errors": [
    {
      "message": "Forbidden",
      "extensions": {
        "problem": {
          "type": "https://kfm.dev/problems/policy-denied",
          "title": "Forbidden",
          "status": 403,
          "detail": "Access denied by governance policy.",
          "instance": "/graphql",
          "kfm": {
            "code": "KFM-POLICY-403",
            "request_id": "01J0KFMBBEJ9Y2JZQ0R5QJ6H0Z"
          }
        }
      }
    }
  ],
  "data": null
}
```

---

## 🧪 Contract-testing expectations

These examples are intended to support:
- OpenAPI examples (FastAPI auto-docs) and SDK test fixtures :contentReference[oaicite:26]{index=26}
- Governance testing: OPA/Rego + Conftest fail-closed policy gates (no “merge” if policies violated) :contentReference[oaicite:27]{index=27}:contentReference[oaicite:28]{index=28}
- Deterministic auditability: canonicalized JSON digests for manifests/idempotency keys :contentReference[oaicite:29]{index=29}

---

## 🔗 KFM docs & design inputs (internal)

> These are the project documents that informed this contract folder.

- :contentReference[oaicite:30]{index=30} **Comprehensive Technical Documentation** (API, contract-first/provenance-first, OpenAPI/GraphQL)
- :contentReference[oaicite:31]{index=31} **Data Intake Guide** (evidence triplet, API as governed gateway, fail-closed posture)
- :contentReference[oaicite:32]{index=32} **Comprehensive UI System Overview** (REST/GraphQL decoupling, provenance surfaced in UI)
- :contentReference[oaicite:33]{index=33} **Additional Project Ideas** (policy gates, manifests, canonical hashing, supply chain)
- :contentReference[oaicite:34]{index=34} **Innovative Concepts** (CARE/sovereignty, sensitivity-aware handling, differential access)
- :contentReference[oaicite:35]{index=35} **Data Mining Concepts & Applications** (query auditing / inference control patterns)

### 📚 Reference portfolios (bundled as PDF portfolios)
These live in the repo as “portfolio” PDFs (collections of embedded documents), and are used as broader implementation references:
- `AI Concepts & more.pdf`
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`
- `Various programming langurages & resources 1.pdf`
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`

---

## ✅ Checklist for adding a new example

- [ ] Use `Content-Type: application/problem+json`
- [ ] Include `type/title/status/detail/instance`
- [ ] Include `kfm.request_id` + `kfm.code`
- [ ] Keep `detail` **safe** (no secrets, no sensitive coords, no internal stack traces)
- [ ] If denial is policy-based, include `kfm.policy` (non-sensitive reasons)
- [ ] If denial is provenance-based, include `kfm.provenance.missing[]`
- [ ] Keep examples stable/deterministic (good for contract tests) 🔒

