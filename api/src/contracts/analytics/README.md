# 📊 Analytics Contracts (`api/src/contracts/analytics`)

![contracts](https://img.shields.io/badge/contracts-API-blue)
![openapi](https://img.shields.io/badge/OpenAPI-ready-2ea44f)
![graphql](https://img.shields.io/badge/GraphQL-compatible-purple)
![provenance](https://img.shields.io/badge/provenance-first-ff7a18)
![policy](https://img.shields.io/badge/policy-fail--closed-critical)
![fair+care](https://img.shields.io/badge/FAIR%20%2B%20CARE-aligned-0aa)

> **What this folder is:** versioned, reusable **request/response contracts** for _analytics_ in Kansas Frontier Matrix (KFM): geospatial stats, time-series, graph analytics, narrative pattern outputs (e.g., Pulse Threads), and AI/ops telemetry.

---

## 🧭 Quick metadata

| Field | Value |
|---|---|
| Purpose | Shared analytics schemas (REST + GraphQL) |
| Primary consumers | API layer, UI dashboards, Focus Mode, watchers/jobs |
| Key constraints | **Evidence-first**, **policy-first**, reproducible, cache-friendly |
| Data backends (typical) | PostGIS 🗺️, Neo4j 🕸️, object storage 📦, vector/text index 🔎 |
| Style | Contract-first + strongly typed + “no mystery numbers” |

---

## 🗂️ Suggested folder map (keep contracts boring ✅)

> Use this as a north-star layout; align names to the actual codebase conventions.

```text
api/src/contracts/
  analytics/
    README.md                 👈 you are here
    base.py                   🧱 shared primitives (TimeRange, SpatialFilter, Envelope)
    metrics.py                📐 MetricSpec, DimensionSpec, Units, Uncertainty
    queries.py                🔎 AnalyticsQuery (and specialized queries)
    responses.py              📦 AnalyticsResponse + result unions
    provenance.py             🧾 ProvenanceRef, EvidenceManifestRef
    policy.py                 🛡️ PolicyDecision, Redaction, Sensitivity
    telemetry.py              📈 TelemetrySummary, FocusTelemetry, SLOs
    jobs.py                   🧵 AsyncJobRef, JobStatus, Progress
    narrative.py              📝 PulseThreadResult, NarrativeSignals
    graph.py                  🕸️ GraphAnalyticsResult, HealthChecks
```

---

## ✨ Core design goals

### 1) Evidence-first outputs 🧾
Analytics responses must be **auditable**: every number, chart, or “insight” should be traceable back to:
- dataset IDs (DCAT/STAC),
- transformation activity IDs (PROV),
- query parameters,
- tool versions and runtime details (where applicable).

### 2) Policy-first, fail-closed 🚦
If the system cannot satisfy:
- licensing requirements,
- sensitivity rules (CARE / TK labels / restricted sites),
- minimum aggregation thresholds (privacy / inference-control),
then it should **deny or coarsen** results rather than “best guess”.

### 3) Contract-first interoperability 🔌
Contracts here should:
- generate clean JSON Schema / OpenAPI,
- map cleanly to GraphQL types,
- be easy to bind into TypeScript types for the UI.

### 4) Reproducibility & cacheability ♻️
Requests should support stable hashing / idempotency keys so repeated computations can be cached, audited, and replayed.

---

## 🧱 Canonical envelope (recommended)

All analytics endpoints should return a predictable envelope:

```json
{
  "meta": {
    "request_id": "req_01H...",
    "run_id": "run_2026-01-23T12:34:56Z_...",
    "issued_at": "2026-01-23T12:34:57Z",
    "cache": { "hit": true, "key": "sha256:..." }
  },
  "policy": {
    "decision": "allow",
    "classification": "public",
    "redactions": [],
    "notes": []
  },
  "provenance": {
    "inputs": [
      {
        "dataset_id": "urn:kfm:dcat:dataset:ks:usgs_stream_gauges:v1",
        "stac_item_ids": ["ks-usgs-06713500-2026-01-23"],
        "prov_activity_ids": ["urn:kfm:prov:activity:ingest:..."],
        "license": "CC-BY-4.0",
        "checksums": [{ "alg": "sha256", "value": "..." }]
      }
    ],
    "query": {
      "canonical_request_digest": "sha256:...",
      "engine": "postgis",
      "sql_template_id": "histogram_v2"
    }
  },
  "telemetry": {
    "duration_ms": 183,
    "db_time_ms": 91,
    "rows_scanned": 124901,
    "bytes_scanned": 20394812
  },
  "data": {
    "kind": "timeseries",
    "result": { }
  },
  "errors": []
}
```

**Why this matters:** UI components (dashboards, map overlays, Focus Mode, audit panels) can trust that every analytics response includes **policy + provenance + telemetry**, even when the `data.kind` differs.

---

## 🧩 Shared primitives

### ⏱️ `TimeRange`
**Required** for time-series and strongly recommended for any analytics query.

Suggested fields:
- `start` (ISO-8601)
- `end` (ISO-8601)
- `timezone` (IANA string; optional)
- `inclusive` (boolean; optional)

### 🗺️ `SpatialFilter`
Support at least:
- `bbox` (WGS84)
- `geojson` geometry (Polygon/MultiPolygon)
- `place_id` (ontology-backed: e.g., FIPS county code)
- `tile` (z/x/y for tile-derived summaries)

### 🧪 `Uncertainty`
Because KFM uses both classical and Bayesian approaches, keep uncertainty **first-class** when available:
- `kind`: `ci95 | credible_interval | stddev | quantiles | none`
- `lower`, `upper`, `q05`, `q95` etc
- `method`: e.g., `bootstrap`, `bayesian`, `stl`, `robust_z`

### 📏 `Unit`
Analytics is only as useful as its units:
- `unit`: UCUM-ish string if possible (`"1"` for unitless, `"mm"`, `"m3/s"`, etc.)
- `display`: human readable (`"m³/s"`)

---

## 🔎 Main request: `AnalyticsQuery`

A “one request fits most dashboards” query. The contract should stay expressive but safe.

### Suggested shape
```json
{
  "dataset": { "dataset_id": "urn:kfm:dcat:dataset:...", "version": "v1" },
  "time": { "start": "2021-01-01", "end": "2021-12-31" },
  "space": { "place_id": "KS-County-FIPS:155" },
  "filters": [
    { "field": "sensor_type", "op": "eq", "value": "stream_gauge" }
  ],
  "metrics": [
    { "name": "flow_p10", "field": "flow_cfs", "agg": "percentile", "params": { "p": 10 }, "unit": "ft3/s" },
    { "name": "flow_mean", "field": "flow_cfs", "agg": "mean", "unit": "ft3/s" }
  ],
  "group_by": [
    { "dimension": "time", "granularity": "P1D" }
  ],
  "output": {
    "format": "timeseries",
    "include_empty_bins": true
  },
  "policy_hints": {
    "min_group_size": 20,
    "allow_coarsening": true
  },
  "explain": {
    "include_query_plan": false,
    "include_geo_xai": false
  },
  "idempotency_key": "sha256:optional-if-client-supplies"
}
```

### 🔧 Operators (`FilterPredicate`)
Keep predicates constrained for safety:
- ops: `eq | neq | lt | lte | gt | gte | in | not_in | between | like`
- value types: string/number/boolean/date
- forbid arbitrary “raw SQL” in contracts

---

## 📦 Results: `AnalyticsResult` union

Use a **discriminated union** via `kind`:

### ✅ `scalar`
```json
{
  "kind": "scalar",
  "result": {
    "name": "ndvi_mean",
    "value": 0.63,
    "unit": "1",
    "uncertainty": { "kind": "ci95", "lower": 0.59, "upper": 0.67, "method": "bootstrap" }
  }
}
```

### 📈 `timeseries`
```json
{
  "kind": "timeseries",
  "result": {
    "series": [
      {
        "name": "ndvi_mean",
        "unit": "1",
        "points": [
          { "t": "2021-01-01", "v": 0.58 },
          { "t": "2021-01-02", "v": 0.59 }
        ]
      }
    ],
    "granularity": "P1D"
  }
}
```

### 🧮 `table`
```json
{
  "kind": "table",
  "result": {
    "columns": [
      { "name": "county_fips", "type": "string" },
      { "name": "ndvi_mean", "type": "number", "unit": "1" }
    ],
    "rows": [
      ["KS-County-FIPS:155", 0.63],
      ["KS-County-FIPS:173", 0.61]
    ]
  }
}
```

### 🗺️ `geojson` (stats attached to features)
```json
{
  "kind": "geojson",
  "result": {
    "feature_collection": {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "properties": { "county_fips": "155", "ndvi_mean": 0.63 },
          "geometry": { "type": "Polygon", "coordinates": [] }
        }
      ]
    }
  }
}
```

### 🧊 `tile_summary` (fast map overlays)
When the UI needs **quick choropleths / heatmaps**, use tile summaries.

```json
{
  "kind": "tile_summary",
  "result": {
    "z": 8,
    "x": 54,
    "y": 98,
    "layer": "streamflow",
    "stats": {
      "count": 1023,
      "min": 1.2,
      "max": 93.4,
      "histogram": { "bins": [0, 10, 20], "counts": [512, 311, 200] }
    }
  }
}
```

### 📦 `artifact_ref` (large outputs)
For large products (GeoParquet, PMTiles, COGs, reports), return an artifact reference:

```json
{
  "kind": "artifact_ref",
  "result": {
    "artifact_id": "urn:kfm:artifact:run:...:ndvi_timeseries_v1",
    "media_type": "application/x-parquet",
    "href": "s3://kfm-artifacts/run_.../ndvi.parquet",
    "checksums": [{ "alg": "sha256", "value": "..." }]
  }
}
```

---

## 🧾 Provenance blocks (required)

### `ProvenanceRef` essentials
At minimum, provenance should carry:
- `dataset_id` (DCAT)
- `stac_item_id` / `stac_collection_id` (STAC)
- `prov_activity_id` (PROV)
- `license` (SPDX string when possible)
- `checksums` (for reproducibility)

### `EvidenceManifestRef` (narratives + advanced analytics)
When analytics produces a story-like or “insight” output, it should include an **evidence manifest reference** so users can drill into exact sources.

---

## 🛡️ Policy blocks (required)

Analytics contracts should support:
- `classification`: `public | internal | restricted | tribal_sensitive | ...`
- `decision`: `allow | deny | allow_with_redaction | allow_with_coarsening`
- `redactions`: list of applied transformations (e.g., coordinate fuzzing, aggregation)
- `reason_codes`: stable machine-readable codes for UI + audits

### Example redaction
```json
{
  "type": "geo_fuzz",
  "detail": "Coordinates rounded to 2 decimals (~1km).",
  "fields": ["geometry"]
}
```

---

## 📈 Telemetry blocks (strongly recommended)

Telemetry supports:
- performance (SLOs),
- operational health checks,
- Focus Telemetry (AI mode latency/usage),
- reproducibility context.

Suggested fields:
- `duration_ms`, `db_time_ms`, `cpu_ms`
- `rows_scanned`, `bytes_scanned`
- `cache_hit`, `cache_key`
- `engine`: `postgis | neo4j | hybrid | external`
- optional: `energy_estimate_j`, `co2e_estimate_g` (if tracked)

---

## 🧵 Async analytics (jobs)

Some analytics should run as background jobs (heavy graph algorithms, big joins, simulations).

### `AsyncJobRef`
```json
{
  "job_id": "job_01H...",
  "status": "queued",
  "submitted_at": "2026-01-23T12:34:00Z",
  "poll_after_ms": 1500
}
```

---

## 🕸️ Graph analytics contracts

### Common graph outputs
- centrality (PageRank-like)
- community detection clusters
- shortest paths / subgraph extraction
- graph “health checks” (schema drift, missing provenance links, orphan nodes)

### Minimal `GraphAnalyticsQuery`
```json
{
  "root": { "node_id": "urn:kfm:place:KS-County-FIPS:155", "kind": "place" },
  "depth": 3,
  "algorithms": [
    { "name": "pagerank", "params": { "damping": 0.85 } },
    { "name": "community", "params": { "method": "louvain" } }
  ],
  "filters": [{ "rel_type": "RELATED_TO", "direction": "both" }],
  "output": { "include_subgraph": false }
}
```

---

## 📝 Narrative analytics outputs (Pulse Threads & signals)

Some analytics results are “insight-shaped” and should be modeled explicitly.

### `PulseThreadResult` (shape)
A Pulse Thread is a short narrative update tied to a geo context, backed by evidence.

```json
{
  "kind": "pulse_thread",
  "result": {
    "pulse_id": "urn:kfm:pulse:2026-01-23:drought:ks:watersheds",
    "title": "Emerging low-flow anomaly cluster",
    "summary": "Several stream gauges show 7-day flows in the lowest decile of historical range.",
    "geo": { "place_ids": ["urn:kfm:watershed:HUC8:..."] },
    "signals": [
      { "name": "flow_percentile", "value": 0.08, "unit": "1", "threshold": 0.10 }
    ],
    "evidence_manifest": {
      "manifest_id": "urn:kfm:evidence:manifest:...",
      "prov_activity_id": "urn:kfm:prov:activity:analysis:..."
    }
  }
}
```

---

## 🧠 GeoXAI & explainability (optional but future-proof)

Analytics contracts should allow returning model explanations without leaking sensitive internals:
- feature contributions (SHAP-like)
- counterfactuals (bounded + policy-approved)
- explanation artifacts (charts, reports) via `artifact_ref`

Suggested pattern:
```json
{
  "explainability": {
    "kind": "feature_contrib",
    "top_features": [
      { "feature": "precip_30d", "contribution": 0.42 },
      { "feature": "temp_mean", "contribution": -0.11 }
    ],
    "method": "shap_approx",
    "notes": ["Aggregated to county level."]
  }
}
```

---

## 🧪 Example: NDVI time-series query (UI ↔ API contract)

### Request
```json
{
  "dataset": { "dataset_id": "urn:kfm:dcat:dataset:ks:ndvi:v1" },
  "time": { "start": "2021-01-01", "end": "2021-12-31" },
  "space": { "place_id": "KS-County-FIPS:155" },
  "metrics": [{ "name": "ndvi_mean", "field": "ndvi", "agg": "mean", "unit": "1" }],
  "group_by": [{ "dimension": "time", "granularity": "P1W" }],
  "output": { "format": "timeseries" }
}
```

### Response (trimmed)
```json
{
  "meta": { "request_id": "req_...", "run_id": "run_..." },
  "policy": { "decision": "allow", "classification": "public", "redactions": [] },
  "provenance": { "inputs": [{ "dataset_id": "urn:kfm:dcat:dataset:ks:ndvi:v1", "license": "CC-BY-4.0" }] },
  "telemetry": { "duration_ms": 212, "cache": { "hit": false } },
  "data": {
    "kind": "timeseries",
    "result": {
      "series": [{ "name": "ndvi_mean", "unit": "1", "points": [{ "t": "2021-01-03", "v": 0.61 }] }],
      "granularity": "P1W"
    }
  },
  "errors": []
}
```

---

## 🧷 Versioning rules

### SemVer-ish (recommended)
- **MAJOR**: breaking schema changes (rename fields, change meaning)
- **MINOR**: backward-compatible additions (new optional fields)
- **PATCH**: docs, stricter validation that doesn’t break valid requests

### Compatibility promise
- Never remove a response field without:
  - a deprecation window,
  - a clear migration path,
  - and a contract version bump.

---

## ✅ Adding a new analytics contract (checklist)

1. **Start with a real UI/user need** (dashboard card, map overlay, Focus Mode view).
2. Model it as:
   - request → response envelope → result union → provenance/policy/telemetry.
3. Add:
   - JSON examples (request + response),
   - schema tests (“golden schema”),
   - policy considerations (what could be sensitive?).
4. Ensure:
   - no free-form SQL,
   - no ambiguous units,
   - provenance always included.

---

## 🧯 Error contract (recommended)

Errors should be structured, stable, and UI-friendly.

```json
{
  "code": "POLICY_DENIED",
  "message": "Query denied by policy.",
  "details": {
    "reason_codes": ["SENSITIVE_GEO", "INSUFFICIENT_AGGREGATION"],
    "can_retry": false
  }
}
```

---

## 🔥 Definition of Done (DoD) for this folder

- [ ] Every contract has **examples** (JSON).
- [ ] Response envelope includes **policy + provenance + telemetry**.
- [ ] All fields have **clear units** and **documented meaning**.
- [ ] Contracts are **language-agnostic** (JSON Schema clean).
- [ ] Changes are **versioned** and backwards-compatible where possible.
- [ ] Sensitive outputs have **explicit policy behavior** (deny/coarsen/redact).
- [ ] No “mystery numbers” — every result has traceability hooks 🧾

---

## 📚 Design sources (project docs that informed these contracts)

> This is a curated list of the internal docs that shaped the constraints above (evidence-first, policy gates, geospatial + graph analytics, telemetry, UI needs, and future expansions like Pulse Threads / GeoXAI).

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation
- Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖
- Kansas Frontier Matrix – Comprehensive UI System Overview
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)
- Additional Project Ideas (Pulse Threads, Conceptual Attention Nodes, narrative signals)
- Maps / WebGL / virtual worlds / geospatial resources portfolio
- AI concepts resources portfolio
- Data management + Bayesian/statistical methods portfolio
- Programming languages & resources portfolio

