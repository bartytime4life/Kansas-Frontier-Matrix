# 🚦 GraphQL Error Contract & Examples (KFM)

![Contract](https://img.shields.io/badge/contract-GraphQL%20Errors-blue)
![Scope](https://img.shields.io/badge/scope-%2Fgraphql%20API-0aa)
![Governance](https://img.shields.io/badge/governance-evidence--first%20%2B%20OPA-purple)
![Stability](https://img.shields.io/badge/stability-draft-yellow)

Canonical **GraphQL error payloads** for Kansas Frontier Matrix (KFM) — designed for **contract-first APIs**, **evidence-first governance**, and **safe-by-default** error handling.

---

## 📌 What lives here

This folder is the **single source of truth** for how GraphQL errors should look and how clients should interpret them.

✅ Use these examples for:
- SDK/client handling (web, mobile, scripts)
- Snapshot tests / contract tests
- API gateway / observability mapping
- Documentation and onboarding

---

## 🗂️ Expected layout

```text
📁 api/
  📁 contracts/
    📁 examples/
      📁 errors/
        📁 graphql/
          ✅ README.md
          📄 KFM-AUTH-001_unauthenticated.json
          📄 KFM-POLICY-101_opa_deny_provenance_required.json
          📄 KFM-QUERY-251_query_too_deep.json
          📄 KFM-VALID-201_invalid_bbox.json
          📄 KFM-GEO-401_invalid_geometry.json
          📄 KFM-SENS-401_sensitive_field_requires_clearance.json
          📄 KFM-PRIV-501_privacy_query_denied.json
          📄 KFM-RATE-601_rate_limited.json
          📄 KFM-UP-701_upstream_timeout.json
          📄 KFM-INT-901_internal_error.json
```

> [!NOTE]
> The JSON files listed above are the **recommended** canonical examples. If they don’t exist yet, create them incrementally as you wire up resolvers and tests.

---

## 🎯 Design goals (KFM-specific)

KFM is not a “generic API” — it’s a governed, provenance-forward system. Error payloads must support:

- **Stable machine codes** (contract-first)
- **Safe user messaging** (no leaks, no stack traces)
- **Governance context** (OPA policy denials, data classification, FAIR+CARE constraints)
- **Provenance context** (missing evidence triplet, unpublishable artifacts)
- **Partial data behaviors** (GraphQL `data` + `errors` is normal)
- **Observability** (requestId/traceId for audits + support)

---

## 🧱 Baseline GraphQL error envelope

GraphQL responses can include both `data` and `errors`. Clients MUST handle:
- `errors` with `data: null`
- `errors` with **partial** `data`

Minimal shape (GraphQL standard):

```json
{
  "data": null,
  "errors": [
    {
      "message": "Human readable message",
      "locations": [{ "line": 1, "column": 1 }],
      "path": ["fieldName", 0, "subField"],
      "extensions": {}
    }
  ]
}
```

---

## 🧩 KFM `extensions` contract

### ✅ Required `extensions` fields

| Field | Type | Why it exists |
|------|------|----------------|
| `code` | `string` | Stable, contract-tested machine code (e.g., `KFM-POLICY-101`) |
| `kind` | `string` | Short semantic label (e.g., `OPA_DENY`, `UNAUTHENTICATED`) |
| `category` | `string` | Routing bucket (AUTH, POLICY, VALIDATION, QUERY, GEO, PRIVACY, RATE, UPSTREAM, INTERNAL) |
| `httpStatus` | `number` | Semantic status mapping (GraphQL may still respond 200) |
| `requestId` | `string` | Support + user-reported correlation |
| `traceId` | `string` | Distributed tracing (APM) |
| `timestamp` | `string` | ISO-8601 UTC |
| `retryable` | `boolean` | Client backoff logic |

### 🧠 Optional (but strongly recommended) fields

| Field | Type | When present |
|------|------|--------------|
| `userAction` | `object` | Safe hint for end-users |
| `details` | `object` | Structured debug for clients (never secrets) |
| `policy` | `object` | OPA/policy gate denials |
| `provenance` | `object` | Missing evidence / blocked publish |
| `sensitivity` | `object` | Masking / clearance / CARE labeling |
| `privacy` | `object` | Query auditing / inference control / DP budget |
| `limits` | `object` | Rate limit / query complexity hints |

> [!IMPORTANT]
> `extensions.details` must be **safe-to-return**. Never include raw SQL, stack traces, tokens, filesystem paths, or internal hostnames.

---

## 🧾 Error code system

### 🔢 Naming rules

Use **stable numeric codes**:
- Format: `KFM-<DOMAIN>-<NNN>`
- Example: `KFM-POLICY-101`

`kind` is the human-friendly semantic label that can evolve without breaking compatibility.

### 🧭 Domains & suggested ranges

| Domain | Range | Examples |
|--------|-------|----------|
| `AUTH` | 001–099 | unauthenticated, forbidden |
| `POLICY` | 100–199 | OPA deny, provenance required |
| `VALID` | 200–249 | invalid args, invalid enum |
| `QUERY` | 250–299 | too deep, too complex |
| `EVID` | 300–349 | evidence manifest missing |
| `GEO` | 400–449 | invalid geometry, unsupported CRS |
| `SENS` | 450–499 | clearance required, masked field |
| `PRIV` | 500–599 | query auditing deny, DP budget exceeded |
| `RATE` | 600–649 | rate limit |
| `UP` | 700–799 | upstream timeout/unavailable |
| `INT` | 900–999 | internal error |

---

## 🧪 Canonical examples

> [!TIP]
> In examples below, operations/fields are illustrative. Keep the **error contract** stable even if schema names change.

---

### 1) 🔐 `KFM-AUTH-001` — Unauthenticated

**Request**
```graphql
query Me {
  me { id displayName }
}
```

**Response**
```json
{
  "data": { "me": null },
  "errors": [
    {
      "message": "Authentication required.",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["me"],
      "extensions": {
        "code": "KFM-AUTH-001",
        "kind": "UNAUTHENTICATED",
        "category": "AUTH",
        "httpStatus": 401,
        "requestId": "req_01HQZ9M1XQK2S9J7J4P2",
        "traceId": "trace_01HQZ9M1XQK2S9J7J4P2",
        "timestamp": "2026-01-24T18:33:12.511Z",
        "retryable": false,
        "userAction": { "summary": "Sign in, then retry." }
      }
    }
  ]
}
```

---

### 2) 🧾 `KFM-POLICY-101` — OPA deny: provenance required

**Request**
```graphql
query Dataset {
  dataset(id: "kfm.ks.landcover.2020") {
    id
    title
    stac { id }
    dcat { license }
    prov { id }
  }
}
```

**Response**
```json
{
  "data": { "dataset": null },
  "errors": [
    {
      "message": "Access blocked by governance policy.",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["dataset"],
      "extensions": {
        "code": "KFM-POLICY-101",
        "kind": "OPA_DENY_PROVENANCE_REQUIRED",
        "category": "POLICY",
        "httpStatus": 403,
        "requestId": "req_01HQZ9N8Q8WZC0QH9V5A",
        "traceId": "trace_01HQZ9N8Q8WZC0QH9V5A",
        "timestamp": "2026-01-24T18:34:55.102Z",
        "retryable": false,
        "policy": {
          "decision": "deny",
          "ruleId": "kfm.provenance.required",
          "reason": "Dataset is not publishable until the evidence triplet is complete."
        },
        "provenance": {
          "datasetId": "kfm.ks.landcover.2020",
          "required": ["STAC", "DCAT", "PROV"],
          "missing": ["PROV"],
          "blockedUntil": "Catalog entries exist and are linked into the graph."
        },
        "userAction": {
          "summary": "Complete provenance (PROV) for this dataset, then retry.",
          "nextSteps": [
            "Add/verify DCAT + STAC entries",
            "Generate PROV for the pipeline run",
            "Re-run catalog QA and graph ingest"
          ]
        }
      }
    }
  ]
}
```

---

### 3) 🧠 `KFM-QUERY-251` — Query too deep / too expensive

**Request**
```graphql
query DeepTraversal {
  person(name: "John Brown") {
    name
    events {
      title
      locations {
        name
        datasets {
          id
          relations {
            derivedFrom {
              id
              relations {
                derivedFrom { id }
              }
            }
          }
        }
      }
    }
  }
}
```

**Response**
```json
{
  "data": { "person": null },
  "errors": [
    {
      "message": "Query exceeds allowed complexity.",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["person"],
      "extensions": {
        "code": "KFM-QUERY-251",
        "kind": "QUERY_TOO_DEEP",
        "category": "QUERY",
        "httpStatus": 400,
        "requestId": "req_01HQZ9P1XG5QF3ZV2F9Y",
        "traceId": "trace_01HQZ9P1XG5QF3ZV2F9Y",
        "timestamp": "2026-01-24T18:36:10.004Z",
        "retryable": true,
        "details": {
          "query": {
            "maxDepth": 8,
            "actualDepth": 14,
            "hint": "Use pagination + narrower selection sets; avoid deep derivedFrom chains."
          }
        }
      }
    }
  ]
}
```

---

### 4) ✅ `KFM-VALID-201` — Invalid bounding box input

**Request**
```graphql
query FeaturesInBBox {
  features(layerId: "rivers", bbox: { xmin: -97.0, ymin: -200.0, xmax: -94.0, ymax: 39.5 }) {
    id
  }
}
```

**Response**
```json
{
  "data": { "features": null },
  "errors": [
    {
      "message": "Invalid request parameters.",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["features"],
      "extensions": {
        "code": "KFM-VALID-201",
        "kind": "INPUT_VALIDATION_FAILED",
        "category": "VALIDATION",
        "httpStatus": 422,
        "requestId": "req_01HQZ9Q7X9EJ3YH7R8R2",
        "traceId": "trace_01HQZ9Q7X9EJ3YH7R8R2",
        "timestamp": "2026-01-24T18:37:21.901Z",
        "retryable": false,
        "details": {
          "validation": [
            { "field": "bbox.ymin", "error": "must be between -90 and 90", "value": -200.0 }
          ]
        }
      }
    }
  ]
}
```

---

### 5) 🗺️ `KFM-GEO-401` — Invalid geometry

**Request**
```graphql
mutation UpsertFeature {
  upsertFeature(
    layerId: "sites",
    feature: {
      id: "site_123",
      geometry: { type: "Polygon", coordinates: [[[0,0],[1,1],[1,0],[0,1],[0,0]]] }
    }
  ) {
    id
  }
}
```

**Response**
```json
{
  "data": { "upsertFeature": null },
  "errors": [
    {
      "message": "Geometry is invalid.",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["upsertFeature"],
      "extensions": {
        "code": "KFM-GEO-401",
        "kind": "INVALID_GEOMETRY",
        "category": "GEO",
        "httpStatus": 422,
        "requestId": "req_01HQZ9RZQY4E1ZQ0A2W1",
        "traceId": "trace_01HQZ9RZQY4E1ZQ0A2W1",
        "timestamp": "2026-01-24T18:38:44.012Z",
        "retryable": false,
        "details": {
          "geometry": {
            "expected": "Valid GeoJSON geometry (right-hand rule, non-self-intersecting polygons)",
            "reason": "Self-intersection detected",
            "hint": "Run a geometry validation/repair step before submitting."
          }
        }
      }
    }
  ]
}
```

---

### 6) 🧷 `KFM-SENS-451` — Sensitive field requires clearance (partial data)

**Request**
```graphql
query Site {
  site(id: "arch.site.007") {
    id
    name
    approxLocation { lat lon }
    exactLocation { lat lon }
  }
}
```

**Response**
```json
{
  "data": {
    "site": {
      "id": "arch.site.007",
      "name": "Restricted Archaeological Site",
      "approxLocation": { "lat": 38.50, "lon": -96.50 },
      "exactLocation": null
    }
  },
  "errors": [
    {
      "message": "Field requires elevated clearance.",
      "locations": [{ "line": 6, "column": 5 }],
      "path": ["site", "exactLocation"],
      "extensions": {
        "code": "KFM-SENS-451",
        "kind": "CLEARANCE_REQUIRED",
        "category": "SENSITIVITY",
        "httpStatus": 403,
        "requestId": "req_01HQZ9T4KQ1QH7K9M3D0",
        "traceId": "trace_01HQZ9T4KQ1QH7K9M3D0",
        "timestamp": "2026-01-24T18:40:05.450Z",
        "retryable": false,
        "sensitivity": {
          "classification": "restricted",
          "maskingApplied": "approx_location_only",
          "policy": "No output may be less restricted than its inputs."
        },
        "userAction": {
          "summary": "Request access or use the approximated location.",
          "nextSteps": ["Contact a maintainer for clearance", "Use aggregated/approx fields in public contexts"]
        }
      }
    }
  ]
}
```

---

### 7) 🕵️ `KFM-PRIV-501` — Privacy query denied (inference control / query auditing)

**Request**
```graphql
query PotentiallyDisclosiveQuery {
  sensitiveStats(regionId: "small_region_1", groupBy: "household") {
    key
    value
  }
}
```

**Response**
```json
{
  "data": { "sensitiveStats": null },
  "errors": [
    {
      "message": "Query denied to protect privacy.",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["sensitiveStats"],
      "extensions": {
        "code": "KFM-PRIV-501",
        "kind": "QUERY_AUDITING_DENY",
        "category": "PRIVACY",
        "httpStatus": 403,
        "requestId": "req_01HQZ9V0E8C7H6M2R9Q3",
        "traceId": "trace_01HQZ9V0E8C7H6M2R9Q3",
        "timestamp": "2026-01-24T18:41:19.993Z",
        "retryable": false,
        "privacy": {
          "mechanism": "query_auditing",
          "reason": "Result could enable disclosure of confidential data via inference.",
          "recommendedMitigation": "Use larger aggregation regions and minimum group thresholds."
        },
        "userAction": {
          "summary": "Broaden your query scope or request an approved, privacy-preserving aggregate."
        }
      }
    }
  ]
}
```

---

### 8) ⏳ `KFM-RATE-601` — Rate limited

**Request**
```graphql
query Search {
  search(text: "drought") { id title }
}
```

**Response**
```json
{
  "data": { "search": null },
  "errors": [
    {
      "message": "Rate limit exceeded.",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["search"],
      "extensions": {
        "code": "KFM-RATE-601",
        "kind": "RATE_LIMITED",
        "category": "RATE",
        "httpStatus": 429,
        "requestId": "req_01HQZ9W9V3G2T1J8J2K5",
        "traceId": "trace_01HQZ9W9V3G2T1J8J2K5",
        "timestamp": "2026-01-24T18:42:30.111Z",
        "retryable": true,
        "limits": {
          "limit": 60,
          "windowSeconds": 60,
          "retryAfterSeconds": 10,
          "resetAt": "2026-01-24T18:42:40.000Z"
        }
      }
    }
  ]
}
```

---

### 9) 🔌 `KFM-UP-701` — Upstream timeout (retryable)

**Request**
```graphql
query TilePreview {
  tilePreview(layerId: "landcover", z: 8, x: 62, y: 98) { url }
}
```

**Response**
```json
{
  "data": { "tilePreview": null },
  "errors": [
    {
      "message": "Temporary upstream failure.",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["tilePreview"],
      "extensions": {
        "code": "KFM-UP-701",
        "kind": "UPSTREAM_TIMEOUT",
        "category": "UPSTREAM",
        "httpStatus": 504,
        "requestId": "req_01HQZ9XQG8Q0A9D7F6P1",
        "traceId": "trace_01HQZ9XQG8Q0A9D7F6P1",
        "timestamp": "2026-01-24T18:43:12.876Z",
        "retryable": true,
        "details": {
          "upstream": {
            "service": "tile-cache",
            "timeoutMs": 2000
          }
        },
        "userAction": { "summary": "Retry shortly. If persistent, report requestId to support." }
      }
    }
  ]
}
```

---

### 10) 💥 `KFM-INT-901` — Internal error (sanitized)

**Response**
```json
{
  "data": null,
  "errors": [
    {
      "message": "Unexpected error.",
      "extensions": {
        "code": "KFM-INT-901",
        "kind": "INTERNAL_ERROR",
        "category": "INTERNAL",
        "httpStatus": 500,
        "requestId": "req_01HQZA01Q9R0J3M4K8W2",
        "traceId": "trace_01HQZA01Q9R0J3M4K8W2",
        "timestamp": "2026-01-24T18:44:09.210Z",
        "retryable": true
      }
    }
  ]
}
```

> [!CAUTION]
> Never expose stack traces or internal exception messages in production GraphQL responses.

---

## 🧭 Client handling guidelines

✅ Clients should:
- Treat `extensions.code` as the **primary** decision point
- Support **partial data** (`data` present + `errors` present)
- Log or surface `requestId` to make support/audit workflows sane
- Retry only when `retryable: true` and/or category is RATE/UPSTREAM
- Avoid “string matching” against `message`

Suggested client strategy:

```text
if error.extensions.code startsWith("KFM-AUTH-") → prompt login
if error.extensions.code startsWith("KFM-POLICY-") → show governance message + next steps
if error.extensions.code startsWith("KFM-VALID-") → highlight fields
if error.extensions.retryable → exponential backoff + jitter
always log requestId + traceId
```

---

## 🧰 Server implementation notes (resolver-side)

**Contract requirements**
- Always attach the required `extensions` fields
- Use consistent `category` strings
- Populate `policy` / `provenance` / `privacy` context when relevant
- Prefer **one error per denied field** for partial responses (GraphQL-native behavior)

**Pseudocode adapter**

```python
def to_graphql_error(err, request_id, trace_id):
    return GraphQLError(
        message=err.safe_message,
        extensions={
            "code": err.code,
            "kind": err.kind,
            "category": err.category,
            "httpStatus": err.http_status,
            "requestId": request_id,
            "traceId": trace_id,
            "timestamp": now_iso_utc(),
            "retryable": err.retryable,
            "details": err.safe_details(),
            "policy": err.safe_policy_context(),
            "provenance": err.safe_provenance_context(),
            "privacy": err.safe_privacy_context(),
            "sensitivity": err.safe_sensitivity_context(),
        },
    )
```

---

## ✅ Adding a new error (checklist)

- [ ] Assign a new `KFM-<DOMAIN>-NNN` code
- [ ] Add it to the taxonomy section above
- [ ] Add a JSON example file in this folder
- [ ] Add/extend resolver mapping (exception → error)
- [ ] Add a contract test snapshot using the JSON example
- [ ] Verify message + details are safe (no secrets, no stack traces)
- [ ] Confirm client behavior (retry? userAction?)

---

## 🧬 Versioning rules

- Additive-only changes are allowed without breaking clients (e.g., new optional fields)
- Changing meaning/structure of required fields requires a **major contract bump**
- Codes must be stable forever once published (deprecate, don’t reuse)

> [!NOTE]
> If you need a contract version field, add `extensions.contractVersion` as an optional string and keep it additive.

---
