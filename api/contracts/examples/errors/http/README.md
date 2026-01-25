# 🧯 HTTP Error Examples (REST) — KFM API Contracts

![Contracts](https://img.shields.io/badge/contracts-api-blue)
![Errors](https://img.shields.io/badge/errors-http-red)
![Format](https://img.shields.io/badge/format-problem%2Bjson-informational)
![Governance](https://img.shields.io/badge/FAIR%2BCARE-enforced-success)
![Policy](https://img.shields.io/badge/OPA%2FConftest-policy--gates-purple)

> 🎯 **Purpose:** This folder contains **canonical HTTP error payload examples** for KFM’s **FastAPI REST API** (and any HTTP endpoints served alongside it).  
> These examples are contract fixtures for:
> - ✅ UI (React/TypeScript) error UX consistency (map, timeline, story nodes, Focus Mode)
> - ✅ API client/SDK integration (typed errors)
> - ✅ Policy & provenance gates (“fail closed”)
> - ✅ PostGIS/Neo4j upstream failures (governed + observable)

---

## 🔗 Quick nav

- ⬆️ Up one level: [`../`](../)
- ⬆️ Errors root: [`../README.md`](../README.md) _(if present)_
- ⬆️ Examples root: [`../../README.md`](../../README.md) _(if present)_

---

## 🗂️ Folder layout

```text
api/contracts/examples/errors/http/
├── README.md                         👈 (you are here)
├── 400.invalid_query.json            🧾 Bad request (params)
├── 401.missing_token.json            🔐 Auth missing/invalid
├── 403.policy_denied.json            🛑 Governance / OPA deny
├── 404.not_found.json                🕳️ Missing resource (non-enumerating)
├── 409.conflict.idempotency.json     ♻️ Idempotency / version conflict
├── 412.precondition_failed.etag.json 🧷 ETag / optimistic concurrency
├── 413.payload_too_large.json        📦 Upload/ingest limit
├── 415.unsupported_media_type.json   🧪 Wrong Content-Type
├── 422.validation_error.json         🧩 Schema/validator errors (Pydantic-ish)
├── 422.ai_insufficient_evidence.json 🧠 Focus Mode refusal (citations required)
├── 429.rate_limited.json             🧯 Throttling / abuse protection
├── 502.upstream_bad_gateway.json     🧱 PostGIS/Neo4j proxy failure
├── 503.service_unavailable.json      🛠️ Maintenance / offline pack build
└── 504.gateway_timeout.json          ⏳ Slow upstream / query timeout
```

> 🧠 **Naming convention (recommended):**  
> `STATUS.short_slug[.subreason].json`  
> Keep slugs stable because the UI and tests will reference them.

---

## 🧾 Contract: KFM Problem Details (HTTP)

KFM is **contract-first** (every dataset + API surface area is schema-driven) and **provenance-first** (nothing enters or leaves without traceability).  
So **all non-2xx HTTP responses** should follow a single, predictable envelope based on **Problem Details for HTTP APIs** (RFC 9457 / RFC 7807-style). 🧷

### ✅ Canonical envelope (JSON)

```json
{
  "type": "urn:kfm:problem:validation",
  "title": "Validation error",
  "status": 422,
  "detail": "One or more fields failed validation.",
  "instance": "/api/datasets/kfm.ks.example.0001",

  "code": "KFM.API.VALIDATION_ERROR",

  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H4D",
  "trace": {
    "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
    "span_id": "00f067aa0ba902b7"
  },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": false,

  "errors": [
    {
      "loc": ["query", "bbox"],
      "msg": "bbox must have 4 numbers: minLon,minLat,maxLon,maxLat",
      "type": "value_error.bbox",
      "input": "foo"
    }
  ],

  "policy": {
    "decision": "allow",
    "gate": "api.request",
    "rule_id": null
  },

  "provenance": {
    "stac_item_id": null,
    "dcat_dataset_id": "kfm.ks.example.0001",
    "prov_activity_id": null,
    "run_manifest": null
  },

  "links": {
    "docs": "urn:kfm:docs:errors#KFM.API.VALIDATION_ERROR",
    "support": "urn:kfm:support"
  }
}
```

### 🧩 Field rules (what clients can count on)

| Field | Required | Meaning | Notes |
|---|---:|---|---|
| `type` | ✅ | Stable problem identifier | Prefer `urn:kfm:problem:*` or a stable URL |
| `title` | ✅ | Short human summary | Keep generic (safe for UI toast titles) |
| `status` | ✅ | HTTP status integer | Must match the actual HTTP status |
| `detail` | ✅ | Human-readable explanation | Must be non-sensitive + user-safe |
| `instance` | ✅ | The request path or instance identifier | Avoid leaking restricted resource existence |
| `code` | ✅ | Stable machine error code | Used for UI routing + analytics |
| `request_id` | ✅ | Correlation id | Also return as `X-KFM-Request-Id` header |
| `trace` | ⚠️ | OpenTelemetry-ish trace identifiers | Optional but strongly recommended |
| `timestamp` | ✅ | RFC 3339 timestamp | UTC (`Z`) preferred |
| `retryable` | ✅ | Whether a retry might succeed | For UI/SDK auto-retry |
| `errors[]` | ⚠️ | Field-level errors | Required for validation failures |
| `policy` | ⚠️ | Policy-gate outcome (OPA/Conftest style) | Include **only** safe denial details |
| `provenance` | ⚠️ | Provenance pointers (STAC/DCAT/PROV + run manifest) | Include when safe + relevant |
| `links` | ⚠️ | Docs/support pointers | Use `urn:*` if no public URL yet |

> 🔒 **Redaction rule:**  
> Never include stack traces, raw SQL, internal hostnames, secrets, or sensitive dataset metadata in `detail`, `errors`, `policy`, or `provenance`.  
> KFM governance is “**fail closed**” — errors must be safe-by-default.

---

## 🧬 Error code taxonomy (KFM-style)

Use stable, namespaced codes so the UI and external integrations can behave deterministically:

```text
KFM.API.*        → request/validation/contract failures
KFM.AUTH.*       → authentication/session/token
KFM.POLICY.*     → authorization, FAIR+CARE constraints, governance gates
KFM.CATALOG.*    → DCAT/STAC dataset & asset lookup
KFM.GRAPH.*      → Neo4j graph traversal/limits/depth
KFM.GEO.*        → tiles, bbox, CRS, geometry/topology issues
KFM.PIPELINE.*   → ingest/job execution, run-manifest, provenance checks
KFM.AI.*         → Focus Mode, citations, prompt security, drift flags
KFM.ARTIFACT.*   → OCI/ORAS/Cosign supply chain verification
KFM.RATE_LIMIT.* → throttling & abuse protection
KFM.UPSTREAM.*   → PostGIS/Neo4j/filesystem/service dependencies
KFM.SYSTEM.*     → maintenance, kill-switch, degraded mode
```

---

## 📦 Standard error headers

Return these headers consistently (where applicable):

- `Content-Type: application/problem+json`
- `X-KFM-Request-Id: <request_id>`
- `WWW-Authenticate: Bearer ...` _(401 only)_
- `Retry-After: <seconds | http-date>` _(429/503 recommended)_
- `ETag: "<etag>"` _(responses that support optimistic concurrency)_

> 🧭 Why headers matter: the UI is decoupled via REST/GraphQL and must be able to show **friendly**, **actionable** messages while still letting support trace a request end-to-end.

---

## 🗺️ Status code matrix (what to use when)

| HTTP | Example file | When to use | UI hint |
|---:|---|---|---|
| 400 | `400.invalid_query.json` | Malformed params (bbox, date range, paging) | “Fix query” + highlight param |
| 401 | `401.missing_token.json` | Missing/expired token | Show sign-in |
| 403 | `403.policy_denied.json` | Policy gate denies access | Lock icon + “Request access” |
| 404 | `404.not_found.json` | Resource missing **or** non-enumerating access | “Not found” + check filters |
| 409 | `409.conflict.idempotency.json` | Idempotency/version conflict | Suggest refresh + retry |
| 412 | `412.precondition_failed.etag.json` | ETag mismatch | “Your view is stale” |
| 413 | `413.payload_too_large.json` | Upload/ingest too big | Suggest chunking |
| 415 | `415.unsupported_media_type.json` | Wrong `Content-Type` | Show supported types |
| 422 | `422.validation_error.json` | Schema/validator fails | Show field errors |
| 422 | `422.ai_insufficient_evidence.json` | Focus Mode cannot cite sources → refusal | Ask user to add context/sources |
| 429 | `429.rate_limited.json` | Rate limit exceeded | Show countdown / backoff |
| 502 | `502.upstream_bad_gateway.json` | Upstream proxy error | Show degraded badge |
| 503 | `503.service_unavailable.json` | Maintenance / offline pack generation | Retry after |
| 504 | `504.gateway_timeout.json` | Query timeout | Suggest smaller query |

---

## 🧪 Examples (copy/paste fixtures)

> Tip: These payloads are intentionally **deterministic** (stable keys, predictable IDs) so contract tests can snapshot them. ♻️

<details>
<summary><strong>400 — Invalid query (bbox too large / malformed)</strong> 🗺️</summary>

```http
HTTP/1.1 400 Bad Request
Content-Type: application/problem+json
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H4D
```

```json
{
  "type": "urn:kfm:problem:invalid-query",
  "title": "Invalid query",
  "status": 400,
  "detail": "The query parameters are invalid.",
  "instance": "/api/tiles/vector?bbox=foo&z=9",
  "code": "KFM.API.INVALID_QUERY",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H4D",
  "trace": { "trace_id": "11111111111111111111111111111111", "span_id": "2222222222222222" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": false,
  "errors": [
    { "loc": ["query", "bbox"], "msg": "bbox must be 4 numbers", "type": "value_error", "input": "foo" }
  ],
  "policy": { "decision": "allow", "gate": "api.request", "rule_id": null },
  "provenance": { "stac_item_id": null, "dcat_dataset_id": null, "prov_activity_id": null, "run_manifest": null },
  "links": { "docs": "urn:kfm:docs:errors#KFM.API.INVALID_QUERY", "support": "urn:kfm:support" }
}
```
</details>

---

<details>
<summary><strong>401 — Missing/invalid token</strong> 🔐</summary>

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/problem+json
WWW-Authenticate: Bearer realm="kfm", error="invalid_token"
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H4E
```

```json
{
  "type": "urn:kfm:problem:unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "detail": "Authentication is required to access this resource.",
  "instance": "/api/datasets/kfm.ks.restricted.0001",
  "code": "KFM.AUTH.UNAUTHORIZED",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H4E",
  "trace": { "trace_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "span_id": "bbbbbbbbbbbbbbbb" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": true,
  "errors": [],
  "policy": { "decision": "deny", "gate": "authn", "rule_id": "KFM-AUTH-001" },
  "provenance": { "stac_item_id": null, "dcat_dataset_id": null, "prov_activity_id": null, "run_manifest": null },
  "links": { "docs": "urn:kfm:docs:errors#KFM.AUTH.UNAUTHORIZED", "support": "urn:kfm:support" }
}
```
</details>

---

<details>
<summary><strong>403 — Policy denied (OPA / FAIR+CARE gate)</strong> ⚖️🛑</summary>

> 🔒 **Non-enumeration guidance:**  
> For some resources, use **404** instead of **403** to avoid revealing existence.  
> Use **403** when existence is already obvious to the user (e.g., they created it, or it’s publicly indexed but access is restricted).

```http
HTTP/1.1 403 Forbidden
Content-Type: application/problem+json
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H4F
```

```json
{
  "type": "urn:kfm:problem:policy-denied",
  "title": "Policy denied",
  "status": 403,
  "detail": "Access to this resource is restricted by governance policy.",
  "instance": "/api/datasets/kfm.ks.indigenous_sensitive.0007",
  "code": "KFM.POLICY.DENIED",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H4F",
  "trace": { "trace_id": "cccccccccccccccccccccccccccccccc", "span_id": "dddddddddddddddd" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": false,
  "errors": [],
  "policy": {
    "decision": "deny",
    "gate": "authz.dataset.read",
    "rule_id": "KFM-CARE-ACCESS-007",
    "reason": "requires_review_and_role"
  },
  "provenance": {
    "stac_item_id": null,
    "dcat_dataset_id": "kfm.ks.indigenous_sensitive.0007",
    "prov_activity_id": null,
    "run_manifest": null
  },
  "links": { "docs": "urn:kfm:docs:errors#KFM.POLICY.DENIED", "support": "urn:kfm:support" }
}
```
</details>

---

<details>
<summary><strong>404 — Not found (safe by default)</strong> 🕳️</summary>

```http
HTTP/1.1 404 Not Found
Content-Type: application/problem+json
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H50
```

```json
{
  "type": "urn:kfm:problem:not-found",
  "title": "Not found",
  "status": 404,
  "detail": "The requested resource was not found.",
  "instance": "/api/datasets/kfm.ks.does_not_exist.9999",
  "code": "KFM.API.NOT_FOUND",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H50",
  "trace": { "trace_id": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "span_id": "ffffffffffffffff" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": false,
  "errors": [],
  "policy": { "decision": "allow", "gate": "api.request", "rule_id": null },
  "provenance": { "stac_item_id": null, "dcat_dataset_id": null, "prov_activity_id": null, "run_manifest": null },
  "links": { "docs": "urn:kfm:docs:errors#KFM.API.NOT_FOUND", "support": "urn:kfm:support" }
}
```
</details>

---

<details>
<summary><strong>409 — Conflict (idempotency / duplicate run manifest)</strong> ♻️</summary>

> ♻️ KFM pipelines and agents are designed to be **idempotent**.  
> When the same operation (same canonicalized run manifest digest) is submitted twice, return a conflict.

```http
HTTP/1.1 409 Conflict
Content-Type: application/problem+json
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H51
```

```json
{
  "type": "urn:kfm:problem:conflict",
  "title": "Conflict",
  "status": 409,
  "detail": "An identical operation has already been accepted or completed.",
  "instance": "/api/ingest/runPipeline",
  "code": "KFM.PIPELINE.IDEMPOTENCY_CONFLICT",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H51",
  "trace": { "trace_id": "12121212121212121212121212121212", "span_id": "3434343434343434" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": false,
  "errors": [],
  "policy": { "decision": "allow", "gate": "pipeline.submit", "rule_id": null },
  "provenance": {
    "stac_item_id": null,
    "dcat_dataset_id": "kfm.ks.example.0001",
    "prov_activity_id": "urn:kfm:prov:activity:ingest:01J2W9M7K3",
    "run_manifest": {
      "run_id": "run_01J2W9M7K3",
      "canonical_digest_sha256": "b3b4f7b9f65d5cf5f7d4c0b3f4a2c6d5b1d7a0f9c3e2a1b0d9c8e7f6a5b4c3d2"
    }
  },
  "links": { "docs": "urn:kfm:docs:errors#KFM.PIPELINE.IDEMPOTENCY_CONFLICT", "support": "urn:kfm:support" }
}
```
</details>

---

<details>
<summary><strong>412 — Precondition failed (ETag mismatch)</strong> 🧷</summary>

```http
HTTP/1.1 412 Precondition Failed
Content-Type: application/problem+json
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H52
```

```json
{
  "type": "urn:kfm:problem:precondition-failed",
  "title": "Precondition failed",
  "status": 412,
  "detail": "Your update was based on a stale version. Refresh and retry.",
  "instance": "/api/story_nodes/story_1930s_drought",
  "code": "KFM.API.ETAG_MISMATCH",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H52",
  "trace": { "trace_id": "abababababababababababababababab", "span_id": "cdcdcdcdcdcdcdcd" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": true,
  "errors": [],
  "policy": { "decision": "allow", "gate": "story.update", "rule_id": null },
  "provenance": { "stac_item_id": null, "dcat_dataset_id": null, "prov_activity_id": null, "run_manifest": null },
  "links": { "docs": "urn:kfm:docs:errors#KFM.API.ETAG_MISMATCH", "support": "urn:kfm:support" }
}
```
</details>

---

<details>
<summary><strong>422 — Validation error (schema / contract-first)</strong> 🧩</summary>

```http
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/problem+json
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H53
```

```json
{
  "type": "urn:kfm:problem:validation",
  "title": "Validation error",
  "status": 422,
  "detail": "One or more fields failed validation.",
  "instance": "/api/graph/query",
  "code": "KFM.API.VALIDATION_ERROR",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H53",
  "trace": { "trace_id": "99999999999999999999999999999999", "span_id": "8888888888888888" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": false,
  "errors": [
    { "loc": ["body", "depth"], "msg": "depth must be <= 6", "type": "value_error.max_depth", "input": 99 }
  ],
  "policy": { "decision": "allow", "gate": "graph.query", "rule_id": "KFM-GRAPH-DEPTH-001" },
  "provenance": { "stac_item_id": null, "dcat_dataset_id": null, "prov_activity_id": null, "run_manifest": null },
  "links": { "docs": "urn:kfm:docs:errors#KFM.API.VALIDATION_ERROR", "support": "urn:kfm:support" }
}
```
</details>

---

<details>
<summary><strong>422 — Focus Mode refusal (insufficient evidence / missing citations)</strong> 🧠⛓️</summary>

> ⛓️ KFM AI outputs **must include citations**. If the system cannot ground an answer in available data, it **refuses** instead of fabricating.

```http
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/problem+json
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H54
```

```json
{
  "type": "urn:kfm:problem:ai-insufficient-evidence",
  "title": "Insufficient evidence",
  "status": 422,
  "detail": "The assistant cannot answer this request with citations from KFM sources. Add sources, narrow scope, or change timeframe.",
  "instance": "/api/focus_mode/ask",
  "code": "KFM.AI.INSUFFICIENT_EVIDENCE",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H54",
  "trace": { "trace_id": "77777777777777777777777777777777", "span_id": "6666666666666666" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": true,
  "errors": [],
  "policy": {
    "decision": "deny",
    "gate": "ai.focus_mode.citations_required",
    "rule_id": "KFM-AI-CITE-001",
    "reason": "no_citable_sources_found"
  },
  "provenance": { "stac_item_id": null, "dcat_dataset_id": null, "prov_activity_id": null, "run_manifest": null },
  "links": { "docs": "urn:kfm:docs:errors#KFM.AI.INSUFFICIENT_EVIDENCE", "support": "urn:kfm:support" }
}
```
</details>

---

<details>
<summary><strong>429 — Rate limited</strong> 🧯</summary>

```http
HTTP/1.1 429 Too Many Requests
Content-Type: application/problem+json
Retry-After: 30
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H55
```

```json
{
  "type": "urn:kfm:problem:rate-limited",
  "title": "Rate limited",
  "status": 429,
  "detail": "Too many requests. Please retry after the specified delay.",
  "instance": "/api/search?q=drought",
  "code": "KFM.RATE_LIMIT.EXCEEDED",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H55",
  "trace": { "trace_id": "55555555555555555555555555555555", "span_id": "4444444444444444" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": true,
  "errors": [],
  "policy": { "decision": "allow", "gate": "api.request", "rule_id": "KFM-RATE-001" },
  "provenance": { "stac_item_id": null, "dcat_dataset_id": null, "prov_activity_id": null, "run_manifest": null },
  "links": { "docs": "urn:kfm:docs:errors#KFM.RATE_LIMIT.EXCEEDED", "support": "urn:kfm:support" }
}
```
</details>

---

<details>
<summary><strong>503 — Service unavailable (maintenance / offline pack build / kill-switch)</strong> 🛠️📱</summary>

> 📱 The UI supports mobile/offline packs and can surface “degraded mode” messaging.  
> Use 503 when the service is intentionally unavailable or temporarily degraded.

```http
HTTP/1.1 503 Service Unavailable
Content-Type: application/problem+json
Retry-After: 120
X-KFM-Request-Id: req_01J2W9M7K3K0MZ9Q0C3A9E9H56
```

```json
{
  "type": "urn:kfm:problem:service-unavailable",
  "title": "Service unavailable",
  "status": 503,
  "detail": "The service is temporarily unavailable. Please retry later.",
  "instance": "/api/offline/packs/kansas-1930s",
  "code": "KFM.SYSTEM.UNAVAILABLE",
  "request_id": "req_01J2W9M7K3K0MZ9Q0C3A9E9H56",
  "trace": { "trace_id": "33333333333333333333333333333333", "span_id": "2222222222222222" },
  "timestamp": "2026-01-24T19:12:45Z",
  "retryable": true,
  "errors": [],
  "policy": { "decision": "allow", "gate": "system.status", "rule_id": null },
  "provenance": { "stac_item_id": null, "dcat_dataset_id": null, "prov_activity_id": null, "run_manifest": null },
  "links": { "docs": "urn:kfm:docs:errors#KFM.SYSTEM.UNAVAILABLE", "support": "urn:kfm:support" }
}
```
</details>

---

## 🧭 UI/Client behavior guidelines (React/TypeScript + MapLibre/Cesium)

Because the UI is decoupled from the backend via REST/GraphQL and prioritizes transparency:

- 🗺️ **Map tiles / layers:**  
  - `KFM.GEO.*` → show “Layer unavailable” but keep map responsive  
  - Prefer retry with backoff on `retryable=true`

- 🧠 **Focus Mode:**  
  - `KFM.AI.INSUFFICIENT_EVIDENCE` → show a refusal card + suggestions (“zoom in”, “pick a timeframe”, “add sources”)  
  - Never “fake” an answer client-side

- ⚖️ **Governance/CARE restrictions:**  
  - `KFM.POLICY.DENIED` → lock UI + “Request access” pathway  
  - Avoid leaking restricted dataset existence (use 404 patterns where required)

- 📱 **Offline packs:**  
  - `KFM.SYSTEM.UNAVAILABLE` or `KFM.OFFLINE.*` → show offline/degraded banner  
  - Offer cached content if available

---

## 🛠️ Backend implementation notes (FastAPI-friendly)

> 🧱 Architecture reminder: KFM domain logic is kept separate from infrastructure; HTTP mapping belongs in the API adapter layer.

### ✅ Recommended approach

- A middleware assigns `request_id` + `trace` on every request
- Exception handlers convert:
  - validation errors → 422 with `errors[]`
  - policy denials (OPA runtime) → 403/404 with safe detail
  - upstream failures (PostGIS/Neo4j) → 502/504/503
- Always respond with `application/problem+json` for non-2xx

### 🧾 TypeScript type (client-safe)

```ts
export type KfmProblemDetails = {
  type: string;
  title: string;
  status: number;
  detail: string;
  instance: string;

  code: string;

  request_id: string;
  trace?: { trace_id?: string; span_id?: string };
  timestamp: string;
  retryable: boolean;

  errors?: Array<{
    loc: Array<string | number>;
    msg: string;
    type: string;
    input?: unknown;
  }>;

  policy?: {
    decision: "allow" | "deny";
    gate?: string;
    rule_id?: string | null;
    reason?: string;
  };

  provenance?: {
    stac_item_id?: string | null;
    dcat_dataset_id?: string | null;
    prov_activity_id?: string | null;
    run_manifest?: unknown | null;
  };

  links?: {
    docs?: string;
    support?: string;
  };
};
```

---

## 🧠 GraphQL note (FYI)

GraphQL typically returns `200 OK` with an `errors[]` array.  
KFM should still reuse the **same** `code`, `request_id`, `policy`, and `provenance` fields under `errors[].extensions` for parity. 🧩

---

## 🧾 Adding a new example (checklist)

1. 🏷️ Pick correct HTTP status + stable `KFM.*` code  
2. 🧼 Ensure `detail` is safe (no secrets, no sensitive dataset metadata)  
3. 🔗 Include `request_id` + `timestamp`  
4. ⚖️ Add `policy` and/or `provenance` if relevant **and safe**  
5. ♻️ Keep IDs deterministic for snapshot tests  
6. ✅ Validate against the HTTP error schema (when present in `api/contracts/schemas/...`)

---

## 📚 Design inputs (why this looks like this)

This contract style intentionally supports KFM’s broader system goals:

- 🧱 **API architecture:** stateless FastAPI + OpenAPI + GraphQL access patterns  
- 🧭 **UI needs:** 2D/3D maps, timeline, story nodes, Focus Mode, mobile/offline, AR  
- ⚖️ **Governance:** FAIR+CARE, policy gates (OPA/Conftest), fail-closed checks  
- ⛓️ **Provenance:** STAC/DCAT/PROV pointers + run-manifest/idempotency concepts  
- 🛡️ **Supply chain:** artifact signing/verification concepts (Cosign/OCI/ORAS)  
- 🧠 **AI:** citations-required, prompt security layers, drift monitoring, auditability  
- 🗺️ **Geospatial:** CRS/bbox/topology patterns and web-API pitfalls  
- 📈 **Analytics:** modeling/simulation pipeline failure modes  
- 🧾 **Docs style:** KFM markdown conventions (templates, checklists, clarity)

---

## ✅ Definition of Done (DoD)

- [ ] Every example returns `application/problem+json`
- [ ] Every example includes `code`, `request_id`, `timestamp`, `retryable`
- [ ] `policy` / `provenance` only contain **safe** fields (no leaks)
- [ ] 4xx vs 5xx semantics are correct
- [ ] UI can map the `code` to a deterministic experience
- [ ] Examples are deterministic (snapshot-safe)
- [ ] Added/updated examples are referenced in this README’s folder tree

---
