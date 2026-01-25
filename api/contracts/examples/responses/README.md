# 📦 API Contract Response Examples (Fixtures)  
![contract-first](https://img.shields.io/badge/contract--first-✅-2ea44f) ![provenance-first](https://img.shields.io/badge/provenance--first-🔎-0ea5e9) ![open-standards](https://img.shields.io/badge/open%20standards-STAC%20%7C%20DCAT%20%7C%20PROV%20%7C%20GeoJSON-f59e0b) ![tests](https://img.shields.io/badge/CI-contract%20tests-8b5cf6)

> **This folder is the canonical home for response “golden files.”**  
> They power contract tests, docs screenshots, UI mocks, and cross-hub federation compatibility. 🌾🗺️

---

## 🎯 What lives here?

This directory contains **example API response payloads** that are treated as **first-class contract artifacts**:

- ✅ **Contract tests (CI):** verify endpoint responses match the OpenAPI/GraphQL contracts
- 📚 **Documentation:** examples shown in docs without hitting a live server
- 🧪 **Fixture-driven development:** stable mocks for UI + SDKs
- 🧭 **Governance & auditability:** examples demonstrate provenance, licensing, and redaction patterns

> **Rule of thumb:** if an endpoint exists, it should have at least one **200** and one **error** example here. 🧷

---

## 🗂️ Recommended layout

Keep examples grouped by **API version** and then by **domain** (datasets, stac, stories, graph, tiles, focus, etc.):

```text
api/
└─ 📜 contracts/
   └─ 🧪 examples/
      └─ 📤 responses/
         ├─ 📄 README.md                 # 👈 you are here 📌 How response examples are organized + validation rules/tests
         ├─ 🧬 v1/                        # Versioned response examples (match API contract version)
         │  ├─ ❤️ health/                 # Health/readiness response examples (ok/degraded/down)
         │  ├─ 🗂️ datasets/               # Dataset responses (cards, detail, distributions, provenance refs)
         │  ├─ 🛰️ stac/                   # STAC API responses (collections/items/search)
         │  ├─ 🗺️ geojson/                # GeoJSON responses (Feature/FeatureCollection examples)
         │  ├─ 🧱 tiles/                  # Tile responses (HTTP header examples + caching semantics)
         │  ├─ 🕸️ graph/                  # Graph responses (place context, lineage, query shapes)
         │  ├─ 📚 stories/                # Story/Story Node responses (content + step bundles + evidence refs)
         │  └─ 🔎 focus/                  # Focus Mode responses (answers with citations/redactions/uncertainty)
         └─ ♻️ _shared/                   # Shared examples reused across versions/endpoints
            ├─ 🚨 problem+json/           # Standard Problem Details error examples (validation/policy/upstream/etc.)
            ├─ 📑 pagination/             # Pagination examples (cursor/offset/since + Link headers/body links)
            └─ 🧬 provenance/             # Provenance examples (STAC/DCAT/PROV refs + evidence manifest refs)
```

### ✅ Why this structure?
- Makes contract tests trivial to discover (`responses/v1/...`)
- Keeps shared patterns reusable (`_shared/`)
- Keeps federation-ready compatibility by versioning at the top level (`v1/`, `v2/`, …)

---

## 🏷️ File naming convention

Use a **predictable, greppable** naming scheme:

```
{method}__{path_slug}__{status}__{variant}.{ext}
```

### ✅ Examples
- `get__v1.health__200__ok.json`
- `get__v1.datasets.list__200__paginated.json`
- `get__v1.datasets.{dataset_id}__404__not_found.problem+json`
- `get__v1.tiles.{dataset_id}.tilejson__200__default.json`
- `post__v1.focus.answer__200__with_citations.json`

### 📌 Path slug rules
- replace `/` with `.`
- keep path params as `{param}`
- prefer **consistent naming** (align with OpenAPI `operationId` if available)

---

## 🧾 Extensions & content types

| Extension | Typical `Content-Type` | Use for |
|---|---|---|
| `.json` | `application/json` | default API responses |
| `.geojson` | `application/geo+json` | vector features (GeoJSON) |
| `.problem+json` | `application/problem+json` | standardized errors |
| `.jsonl` / `.ndjson` | `application/x-ndjson` | streaming / evented output |
| `.stac-item.json` / `.stac-collection.json` *(optional)* | `application/json` | STAC-specific examples (clarity) |

> ⚠️ Keep examples **small** and **deterministic**. If you need “big payload” realism, include a **minimal** and a **representative** variant instead of committing huge blobs.

---

## 🧠 KFM response principles (non-negotiables)

### 1) 🧱 Contract-first
Examples must validate against the **current contract** (OpenAPI + JSON Schemas, GraphQL schema).

### 2) 🔁 Deterministic & replayable
Examples should not depend on “now”, random IDs, or unstable ordering.

**Use fixed placeholders**:
- timestamps like `2026-01-01T00:00:00Z`
- IDs like `00000000-0000-0000-0000-000000000000`
- stable ordering for arrays where meaningful (features, items, links)

### 3) 🔎 Provenance-first
If a response is derived (filtered, aggregated, simplified, redacted, etc.), include **explicit provenance**:
- what sources were used
- what transformation happened
- what policies were applied (if relevant)

### 4) 🧭 Evidence-first focus
Any “narrative” or “AI” response must include citations (or explicitly say none are available).

---

## 🧱 Reusable response building blocks

### 🧩 KFM “foreign members” (namespaced keys)

For standards like GeoJSON and STAC, we avoid breaking compatibility by storing KFM additions under **namespaced fields** such as:

- `"kfm:meta"`  
- `"kfm:provenance"`  
- `"kfm:citations"`  
- `"kfm:redactions"`

This keeps clients happy while preserving auditability.

---

## 🚨 Error responses (`application/problem+json`)

All error examples should follow RFC 7807 style plus KFM additions.

✅ Minimal template:

```json
{
  "type": "https://kfm.example/errors/invalid-parameter",
  "title": "Invalid parameter",
  "status": 400,
  "detail": "Query parameter 'bbox' must be four numbers [minLon,minLat,maxLon,maxLat].",
  "instance": "/v1/datasets?bbox=bad",
  "kfm:request_id": "req_0000000000000000",
  "kfm:trace_id": "trace_0000000000000000"
}
```

**Recommended add-ons (when applicable):**
- `kfm:violations`: validation errors by field
- `kfm:docs`: link or doc key
- `kfm:retry_after_seconds`: for rate limits / backpressure

---

## 🗺️ GeoJSON example template (`.geojson`)

<details>
<summary><strong>📍 Example: FeatureCollection with provenance</strong></summary>

```json
{
  "type": "FeatureCollection",
  "bbox": [-102.051, 36.993, -94.589, 40.003],
  "features": [
    {
      "type": "Feature",
      "id": "feat_0000000000000001",
      "geometry": {
        "type": "Point",
        "coordinates": [-96.576, 39.184]
      },
      "properties": {
        "name": "Example Place",
        "kind": "place",
        "time_range": {
          "start": "1854-01-01",
          "end": "1865-12-31"
        }
      }
    }
  ],
  "kfm:meta": {
    "api_version": "v1",
    "dataset_id": "kfm.ks.example.1854_1865.v1",
    "generated_at": "2026-01-01T00:00:00Z",
    "request_id": "req_0000000000000000"
  },
  "kfm:provenance": {
    "profiles": ["KFM_PROV_PROFILE@v1"],
    "was_generated_by": "etl_run_2026-01-01T00:00:00Z",
    "used": [
      {
        "type": "stac-item",
        "id": "stac_item_0000000000000001",
        "rel": "source"
      }
    ]
  }
}
```
</details>

---

## 🛰️ STAC example template (`.json`)

<details>
<summary><strong>🗃️ Example: STAC Item (COG asset + provenance link)</strong></summary>

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-asset-0001",
  "collection": "kfm.ks.remote_sensing.ndvi",
  "bbox": [-102.051, 36.993, -94.589, 40.003],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-102.051, 36.993],
        [-94.589, 36.993],
        [-94.589, 40.003],
        [-102.051, 40.003],
        [-102.051, 36.993]
      ]
    ]
  },
  "properties": {
    "datetime": "2021-07-01T00:00:00Z",
    "license": "CC-BY-4.0"
  },
  "assets": {
    "data": {
      "href": "https://kfm.example/assets/ndvi_2021_07_01.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  },
  "links": [
    { "rel": "self", "href": "https://kfm.example/stac/items/kfm-asset-0001" },
    { "rel": "collection", "href": "https://kfm.example/stac/collections/kfm.ks.remote_sensing.ndvi" },
    { "rel": "root", "href": "https://kfm.example/stac" },
    {
      "rel": "derived_from",
      "href": "https://kfm.example/prov/etl_run_2026-01-01T00:00:00Z.jsonld",
      "type": "application/ld+json"
    }
  ],
  "kfm:meta": {
    "hub_id": "kfm.ks",
    "api_version": "v1"
  }
}
```
</details>

---

## 🧠 Focus Mode example template (citations required)

<details>
<summary><strong>🧠 Example: Focus answer with citations</strong></summary>

```json
{
  "type": "kfm.focus.answer",
  "question": "What significant events are linked to this area?",
  "answer_markdown": "Here is a sourced summary based on KFM records...\n\n- Point 1\n- Point 2",
  "citations": [
    {
      "id": "stac_item_0000000000000001",
      "kind": "stac-item",
      "title": "Example STAC Item",
      "license": "CC-BY-4.0",
      "href": "https://kfm.example/stac/items/kfm-asset-0001"
    },
    {
      "id": "doc_0000000000000002",
      "kind": "document",
      "title": "Example Source Document",
      "href": "https://kfm.example/docs/doc_0000000000000002"
    }
  ],
  "kfm:provenance": {
    "policy": {
      "evidence_required": true,
      "no_unsourced_claims": true
    },
    "generated_at": "2026-01-01T00:00:00Z",
    "request_id": "req_0000000000000000"
  }
}
```
</details>

---

## 🕸️ GraphQL response example template

GraphQL responses may contain both `data` and `errors`. Keep error examples realistic and stable.

<details>
<summary><strong>🕸️ Example: GraphQL partial success</strong></summary>

```json
{
  "data": {
    "place": {
      "id": "place_0001",
      "name": "Example Place",
      "events": null
    }
  },
  "errors": [
    {
      "message": "Access denied to field 'events' for current role.",
      "path": ["place", "events"],
      "extensions": {
        "code": "FORBIDDEN",
        "kfm:request_id": "req_0000000000000000",
        "kfm:trace_id": "trace_0000000000000000"
      }
    }
  ]
}
```
</details>

---

## ⏳ Async job response template (background tasks)

Some operations queue work (ETL, heavy analysis, tiling). Use **202 Accepted** patterns in examples.

```json
{
  "type": "kfm.job.accepted",
  "job_id": "job_0000000000000001",
  "status": "queued",
  "status_url": "/v1/jobs/job_0000000000000001",
  "submitted_at": "2026-01-01T00:00:00Z",
  "kfm:request_id": "req_0000000000000000"
}
```

---

## 🧪 Adding or updating an example (workflow)

### ✅ Step-by-step
1. **Pick the endpoint & status** (e.g., `GET /v1/datasets/{dataset_id}` → `200`)
2. Create the example file using naming convention  
3. Ensure it matches:
   - OpenAPI response schema (or GraphQL type)
   - Any JSON Schema profiles (STAC/DCAT/PROV, Story Node, etc.)
4. Add/refresh error cases for that endpoint if needed (400/404/422/etc.)
5. Run formatting & validation locally (and ensure CI passes)

### 🧷 Definition of done checklist
- [ ] Schema-valid ✅
- [ ] No secrets / PII / sensitive coordinates 🔐
- [ ] Licensing/attribution present where relevant 🧾
- [ ] Deterministic values used (stable timestamps/IDs) 🔁
- [ ] Provenance included for derived outputs 🔎
- [ ] “Focus/AI” responses include citations (or explicitly empty) 🧠

---

## 🚫 Anti-patterns (please don’t)

- ❌ embedding real API keys, tokens, or credentials
- ❌ leaking precise sensitive locations (use redaction patterns)
- ❌ returning raw stack traces to clients (use `problem+json` + trace ID)
- ❌ “mystery data” without provenance or license fields
- ❌ unstable ordering or “now” timestamps in golden files

---

## 🔗 Related docs (repo-level)

If present in this repo, these are the canonical companions to this folder:

- `docs/MASTER_GUIDE_v13.md` 📘
- `docs/standards/KFM_STAC_PROFILE.md` 🛰️
- `docs/standards/KFM_DCAT_PROFILE.md` 🗃️
- `docs/standards/KFM_PROV_PROFILE.md` 🧬
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` 🧩
- `docs/templates/TEMPLATE__STORY_NODE_V3.md` 🎬

---

## 🌱 Tip for federation readiness

If/when multiple “Frontier Matrix” hubs exist (KS/NE/OK/etc.), examples should demonstrate:
- a clear `api_version`
- a `hub_id` / origin marker (e.g., `kfm.ks`)
- standards-first payloads (STAC/DCAT/PROV/GeoJSON)
- deterministic identifiers that do **not** require string-parsing for semantics

This is how we keep schemas portable across regions while staying audit-friendly. 🤝
