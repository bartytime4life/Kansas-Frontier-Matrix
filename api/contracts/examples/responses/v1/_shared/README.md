# 📦 KFM API · Shared Response Examples (v1) — `_shared/` 🔗

![contract-first](https://img.shields.io/badge/contract--first-yes-1f6feb)
![evidence-first](https://img.shields.io/badge/evidence--first-yes-1f6feb)
![provenance](https://img.shields.io/badge/STAC%20%7C%20DCAT%20%7C%20PROV-required-1f6feb)
![governance](https://img.shields.io/badge/FAIR%20%2B%20CARE-governance-1f6feb)

> **This folder** contains **reusable response shapes & example fragments** used across KFM’s **v1** API contracts: envelopes, errors, pagination, provenance, governance, and telemetry.  
> Goal: every endpoint response is **trustable**, **traceable**, and **policy-aware** — without each endpoint reinventing JSON structures.

---

## 🗂️ Where you are

```text
api/
└─ 📜 contracts/
   └─ 🧪 examples/
      └─ 📤 responses/
         └─ 🧬 v1/
            └─ ♻️ _shared/
               ├─ 📄 README.md                 # 👈 you are here 📌 Shared response example conventions + how tests consume them
               ├─ 📦🧾 envelope.*.json          # (recommended) Standard response envelopes (data/meta/links/request_id)
               ├─ 🚨🧾 error.*.json             # (recommended) Error examples (ProblemDetails, validation errors, policy denials)
               ├─ 📑🧾 pagination.*.json        # (recommended) Pagination examples (cursor/limit/next/prev shapes)
               └─ 🧬🧾 provenance.*.json        # (recommended) Provenance examples (STAC/DCAT/PROV refs + evidence manifest refs)
```

---

## 🧭 Contents

- [Why `_shared` exists](#why-_shared-exists)
- [KFM response envelope](#kfm-response-envelope)
- [Shared building blocks](#shared-building-blocks)
  - [`meta`](#meta)
  - [`errors`](#errors)
  - [`links`](#links)
  - [`provenance`](#provenance)
  - [`governance`](#governance)
  - [`telemetry`](#telemetry)
- [Copy/paste examples](#copypaste-examples)
- [Conventions & compatibility](#conventions--compatibility)
- [Adding or changing shared examples](#adding-or-changing-shared-examples)
- [Design references](#design-references)

---

## Why `_shared` exists

KFM’s architecture emphasizes:

- 🧱 **Contract-first**: schemas + examples should validate in CI (policy gates, schema checks, quality checks).
- 🔎 **Evidence-first**: UI/AI must show “what this is based on” (citations, manifests, provenance graph links).
- 🔗 **Provenance-first publishing**: “published” data should have provenance artifacts (STAC/DCAT/PROV).
- 🛡️ **Governance-first**: classification/sovereignty/redactions propagate; outputs can’t be “less restricted” than inputs.
- 🧭 **One API boundary**: UI goes through the API boundary so policy/redaction can happen consistently.

This folder keeps shared response patterns **consistent** across:
- REST JSON endpoints ✅
- “JSON descriptors” for binary endpoints (tiles/downloads) ✅
- GraphQL resolvers (conceptual mapping) ✅

---

## KFM response envelope

### ✅ Canonical shape

Most **JSON** responses should follow this shape:

```json
{
  "meta": { },
  "data": { },
  "errors": [ ],
  "warnings": [ ],
  "links": { },
  "provenance": { },
  "governance": { },
  "telemetry": { }
}
```

### 🧩 Type (reference)

```ts
export type KfmResponse<T> = {
  meta: KfmMeta;
  data?: T;
  errors?: KfmError[];
  warnings?: KfmWarning[];
  links?: KfmLinks;
  provenance?: KfmProvenance;
  governance?: KfmGovernance;
  telemetry?: KfmTelemetry;
};
```

### 🧠 Envelope rules

- **`meta` MUST exist** (even on errors) so clients can correlate `request_id` with logs/telemetry.
- **`data` MUST be omitted on error** (or present as `null` only when explicitly documented).
- **`errors[]` MUST be present on errors** and SHOULD be absent (or empty) on success.
- **`provenance` SHOULD exist when returning derived/curated/AI content** (anything needing traceability).
- **`governance` SHOULD exist when redaction, sensitivity, sovereignty, or licensing matters** (which is… often).
- **Binary endpoints** (MVT tiles, file downloads) MAY return raw bytes; see [Conventions & compatibility](#conventions--compatibility).

---

## Shared building blocks

### `meta`

| Field | Type | Req | Notes |
|---|---|---:|---|
| `api_version` | string | ✅ | `"v1"` |
| `request_id` | string | ✅ | Trace/correlation id (UUID/ULID). Also echo in headers if desired. |
| `generated_at` | string (RFC3339) | ✅ | UTC timestamp |
| `service` | object | ⬆️ | `{ name, version, instance?, region? }` |
| `duration_ms` | number | ⬆️ | Server-side compute time |
| `page` | object | ➕ | For list endpoints (cursor pagination recommended) |
| `deprecation` | object | ➕ | Optional sunset warnings for clients |

> Tip 💡: Treat `meta` as the “control plane” for clients.

---

### `errors`

| Field | Type | Req | Notes |
|---|---|---:|---|
| `code` | string | ✅ | Stable machine code (`KFM_*`) |
| `message` | string | ✅ | Human-friendly |
| `details` | object | ➕ | Field errors, expected constraints, etc. |
| `retryable` | boolean | ➕ | Client backoff behavior |
| `docs` | string | ➕ | Link to docs route or error catalog id |

**Error code conventions**
- Prefix with `KFM_`
- Include broad domain: `KFM_AUTH_*`, `KFM_VALIDATION_*`, `KFM_POLICY_*`, `KFM_NOT_FOUND_*`, `KFM_RATE_LIMIT_*`

---

### `links`

A lightweight way to keep clients moving without memorizing routes.

| Field | Type | Notes |
|---|---|---|
| `self` | string | This resource |
| `next` / `prev` | string | Pagination |
| `related[]` | array | Related resources |
| `docs` | string | Endpoint documentation |

---

### `provenance`

KFM treats provenance as a **first-class contract concept**.

| Field | Type | Notes |
|---|---|---|
| `citations[]` | array | Canonical citations list (datasets, documents, stations, etc.) |
| `prov_bundle` | object | Link + digest to PROV/JSON-LD bundle |
| `artifacts[]` | array | Manifests, catalogs, exports, run outputs |
| `generated_by` | object | Agent/system that produced this response (when relevant) |

#### Suggested `citations[]` item shape

```json
{
  "id": "cite_01",
  "label": "USGS NWIS — Kansas River gauge (Topeka)",
  "kind": "dataset|document|station|model_output",
  "href": "/v1/catalog/dcat/kfm.dcat.usgs.nwis.realtime.json",
  "retrieved_at": "2026-01-24T18:00:00Z",
  "license": "Public Domain",
  "hash": { "sha256": "..." }
}
```

> ✅ If **AI text** references facts, it should reference `citation_ids` that point back to this list.

---

### `governance`

Governance communicates “what you can do with this” and “what was done to this.”

| Field | Type | Notes |
|---|---|---|
| `sensitivity` | object | `{ classification, handling, reasons? }` |
| `license` | object | `{ spdx?, name?, href?, attribution? }` |
| `policy_gates[]` | array | Which checks ran and their outcome |
| `redactions[]` | array | What was removed/generalized and why |
| `privacy` | object | Query-auditing / inference controls when applicable |
| `ai` | object | `generated`, `model?`, `review_status?` |

**Redaction shape (recommended)**

```json
{
  "path": "/data/features/0/geometry",
  "technique": "omit|generalize|fuzz|aggregate",
  "reason": "sensitive_location",
  "policy_id": "policy.sensitivity.protect_precise_locations"
}
```

> 🛡️ Privacy note: KFM should treat *outputs* as potentially sensitive too (inference attacks). Consider query auditing and inference controls for certain endpoints.

---

### `telemetry`

Keep telemetry **useful but safe** (no secrets, no PII). Useful for debugging + monitoring.

| Field | Type | Notes |
|---|---|---|
| `cache` | object | `{ hit, layer?, ttl_ms? }` |
| `db` | object | `{ postgis_ms?, neo4j_ms?, search_ms? }` |
| `ai` | object | `{ tokens_in?, tokens_out?, latency_ms? }` |
| `policy` | object | `{ evaluated_ms?, ruleset_version? }` |

---

## Copy/paste examples

> All examples use **snake_case** for REST JSON. (GraphQL will typically use **camelCase**.)

<details>
<summary><strong>✅ Minimal success envelope</strong></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "request_id": "req_01HVJ4QZ1Y9V9K7R8P4FZ4G2XW",
    "generated_at": "2026-01-24T18:04:12Z",
    "service": { "name": "kfm-api", "version": "1.0.0" }
  },
  "data": {
    "type": "health",
    "status": "ok"
  }
}
```
</details>

<details>
<summary><strong>✅ Success with provenance + governance</strong></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "request_id": "req_01HVJ4R3P6QW8Y2B1D8GZP1H6A",
    "generated_at": "2026-01-24T18:05:02Z",
    "service": { "name": "kfm-api", "version": "1.0.0", "region": "us-central1" },
    "duration_ms": 18
  },
  "data": {
    "type": "stations_snapshot",
    "format": "geojson",
    "feature_collection": {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "id": "kfm.station.usgs.06889635",
          "geometry": { "type": "Point", "coordinates": [ -95.676, 39.047 ] },
          "properties": {
            "station_id": "06889635",
            "value": 12.3,
            "unit": "ft",
            "timestamp": "2026-01-24T18:00:00Z"
          }
        }
      ]
    }
  },
  "provenance": {
    "citations": [
      {
        "id": "cite_01",
        "label": "USGS NWIS — Real-time Water Data",
        "kind": "dataset",
        "href": "/v1/catalog/dcat/kfm.dcat.usgs.nwis.realtime.json",
        "retrieved_at": "2026-01-24T18:00:00Z",
        "license": "Public Domain"
      }
    ],
    "prov_bundle": {
      "id": "kfm.prov.req_01HVJ4R3P6QW8Y2B1D8GZP1H6A",
      "href": "/v1/catalog/prov/kfm.prov.req_01HVJ4R3P6QW8Y2B1D8GZP1H6A.jsonld",
      "sha256": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "media_type": "application/ld+json"
    }
  },
  "governance": {
    "sensitivity": { "classification": "public", "handling": "open" },
    "policy_gates": [
      { "id": "policy.provenance_required", "status": "pass", "version": "2026.01" },
      { "id": "policy.license_required", "status": "pass", "version": "2026.01" }
    ],
    "redactions": []
  },
  "telemetry": {
    "cache": { "hit": true, "layer": "stations_snapshot" },
    "db": { "postgis_ms": 9 }
  }
}
```
</details>

<details>
<summary><strong>📄 Cursor pagination (recommended)</strong></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "request_id": "req_01HVJ4S0MZ2P3H8J8A0VQ4W8Z9",
    "generated_at": "2026-01-24T18:06:40Z",
    "page": {
      "mode": "cursor",
      "limit": 50,
      "cursor": "cur_01HVJ4RZ...",
      "next_cursor": "cur_01HVJ4S1..."
    }
  },
  "data": {
    "type": "search_results",
    "items": [
      { "id": "kfm.doc.news.1934-04-14.garden_city", "title": "Dust Storm Hits Western Kansas" }
    ]
  },
  "links": {
    "self": "/v1/search?q=dust%20storm&limit=50&cursor=cur_01HVJ4RZ...",
    "next": "/v1/search?q=dust%20storm&limit=50&cursor=cur_01HVJ4S1..."
  }
}
```
</details>

<details>
<summary><strong>❌ Validation error</strong></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "request_id": "req_01HVJ4T0C9X7F4R2H8ZQ0N2M1B",
    "generated_at": "2026-01-24T18:07:21Z"
  },
  "errors": [
    {
      "code": "KFM_VALIDATION_QUERY_PARAM",
      "message": "Invalid query parameter: limit",
      "details": { "field": "limit", "expected": "integer (1..1000)", "received": -5 },
      "retryable": false,
      "docs": "/docs/api/errors#KFM_VALIDATION_QUERY_PARAM"
    }
  ]
}
```
</details>

<details>
<summary><strong>🛡️ Forbidden / sensitive output (redaction-aware)</strong></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "request_id": "req_01HVJ4V2Z5R6Y8K2C0M3N9Q1T7",
    "generated_at": "2026-01-24T18:08:10Z"
  },
  "errors": [
    {
      "code": "KFM_POLICY_FORBIDDEN_SENSITIVE_LOCATION",
      "message": "Requested resource contains restricted location details.",
      "retryable": false
    }
  ],
  "governance": {
    "sensitivity": {
      "classification": "restricted",
      "handling": "role_required",
      "reasons": [ "cultural_sensitivity", "sovereignty_constraints" ]
    },
    "policy_gates": [
      { "id": "policy.no_output_less_restricted_than_inputs", "status": "fail", "version": "2026.01" }
    ],
    "redactions": [
      {
        "path": "/data/geometry",
        "technique": "omit",
        "reason": "restricted_location",
        "policy_id": "policy.sensitivity.protect_precise_locations"
      }
    ]
  }
}
```
</details>

<details>
<summary><strong>🤖 AI answer (with citation_ids + PROV logging)</strong></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "request_id": "req_01HVJ4W5H2E9T9J0A1B2C3D4E5",
    "generated_at": "2026-01-24T18:09:44Z",
    "duration_ms": 312
  },
  "data": {
    "type": "ai_answer",
    "answer_markdown": "As of **2026-01-24 18:00 UTC**, the Kansas River gauge at Topeka reads **12.3 ft**.[^cite_01]",
    "citation_ids": [ "cite_01" ],
    "ai": {
      "generated": true,
      "model": "kfm-focus-v1",
      "review_status": "unreviewed"
    }
  },
  "provenance": {
    "citations": [
      {
        "id": "cite_01",
        "label": "USGS NWIS — Kansas River at Topeka (station 06889635)",
        "kind": "station",
        "href": "/v1/stations/kfm.station.usgs.06889635",
        "retrieved_at": "2026-01-24T18:00:00Z",
        "license": "Public Domain"
      }
    ],
    "prov_bundle": {
      "id": "kfm.prov.focus.req_01HVJ4W5H2E9T9J0A1B2C3D4E5",
      "href": "/v1/catalog/prov/kfm.prov.focus.req_01HVJ4W5H2E9T9J0A1B2C3D4E5.jsonld",
      "sha256": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
      "media_type": "application/ld+json"
    }
  },
  "governance": {
    "policy_gates": [
      { "id": "policy.ai_output_requires_citation", "status": "pass", "version": "2026.01" }
    ],
    "ai": { "generated": true }
  },
  "telemetry": {
    "ai": { "latency_ms": 280, "tokens_in": 512, "tokens_out": 96 }
  }
}
```

> Footnotes in `answer_markdown` are allowed (GitHub-style). The canonical data lives in `provenance.citations[]`.

</details>

<details>
<summary><strong>⚡ Pulse Thread (short-form narrative update)</strong></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "request_id": "req_01HVJ4X9G0D2F3H4J5K6L7M8N9",
    "generated_at": "2026-01-24T18:11:05Z"
  },
  "data": {
    "type": "pulse_thread",
    "id": "kfm.pulse.1934-04.dust_storms.west_ks",
    "title": "1934 Dust Storm Reports in Western Kansas",
    "summary": "Multiple local reports describe intense dust storms affecting visibility and travel during April 1934.",
    "time_range": [ "1934-04-01", "1934-04-30" ],
    "location": { "type": "Point", "coordinates": [ -101.0, 38.5 ] },
    "tags": [ "dust_bowl", "weather", "transport" ],
    "citation_ids": [ "cite_02", "cite_03" ]
  },
  "provenance": {
    "citations": [
      {
        "id": "cite_02",
        "label": "Local newspaper archive clipping (April 1934)",
        "kind": "document",
        "href": "/v1/docs/kfm.doc.news.1934-04-14.garden_city"
      },
      {
        "id": "cite_03",
        "label": "Regional weather dataset / index reference",
        "kind": "dataset",
        "href": "/v1/catalog/dcat/kfm.dcat.noaa.historical_weather_index.json"
      }
    ]
  }
}
```
</details>

---

## Conventions & compatibility

### 🧾 JSON conventions

- **REST JSON**: `snake_case` keys.
- **GraphQL**: `camelCase` per GraphQL conventions.
- Timestamps: **RFC3339 / ISO8601**, **UTC** whenever possible (`...Z`).

### 🌎 GeoJSON conventions

- Coordinates use **WGS84** and **[longitude, latitude]** ordering.
- Prefer `FeatureCollection` for map-ready responses.

### 🧱 Binary endpoints (tiles, downloads)

Some endpoints may return:
- 🧩 `application/x-protobuf` (vector tiles)
- 📦 large files (exports, rasters, archives)

For those endpoints:
- Return raw bytes **OR**
- Provide a JSON **descriptor** endpoint that returns:
  - signed URL / href
  - digests
  - license + governance
  - provenance artifacts

### 🛡️ Governance & privacy

- If data is sensitive, **either omit, generalize, or refuse** — but always **explain via `governance`**.
- Consider **query auditing / inference control** patterns for endpoints that could be combined to infer restricted attributes.

---

## Adding or changing shared examples

### ✅ Definition of Done checklist

- [ ] Example validates against the corresponding schema (JSON Schema / OpenAPI example validators).
- [ ] Includes `meta.request_id` and `meta.api_version`.
- [ ] Uses stable IDs and realistic fields (no placeholders like `"foo"` unless truly generic).
- [ ] If AI text is present, includes `citation_ids` and provenance entries.
- [ ] If redaction/sensitivity is involved, includes `governance.sensitivity` + `redactions[]`.
- [ ] Pagination examples include `meta.page` + `links.next`.
- [ ] CI policy gates won’t fail (license required, provenance required, etc.).

### 🧪 Suggested filenames (if/when added)

```text
_shared/
  envelope.success.min.json
  envelope.success.full.json
  envelope.error.validation.json
  envelope.error.forbidden.sensitive.json
  pagination.cursor.json
  provenance.bundle.json
  governance.redaction.json
  ai.answer.json
  pulse_thread.item.json
```

---

## Design references

These shared response patterns align with the broader KFM docs & proposals, especially around:
- REST + GraphQL boundaries
- provenance enforcement (STAC/DCAT/PROV)
- governance policy gates (OPA/Conftest)
- evidence-first UI + AI outputs (citations, manifests)
- redaction & sensitivity propagation
- reproducibility + artifact integrity

📚 Key project docs referenced while shaping these examples:

- **KFM Data Intake – Technical & Design Guide**
- **KFM Comprehensive Technical Documentation**
- **KFM Architecture, Features, and Design**
- **KFM AI System Overview**
- **KFM UI System Overview**
- **Innovative Concepts to Evolve KFM**
- **Latest Ideas & Future Proposals**
- **Additional Project Ideas**
- **Open-Source Geospatial Historical Mapping Hub Design**
- **Design Audit – Gaps and Enhancement Opportunities**
- **KFM Python Geospatial Analysis Cookbook**
- **Data Management / Programming / Mapping resource portfolios**
- **Data Mining Concepts & Applications (privacy & inference control concepts)**

---

🧭 _If you’re editing endpoint-specific examples_: keep endpoint details in the endpoint folder, and only promote a shape to `_shared/` when it’s truly reusable.
