---
title: "KFM API Contracts — Analysis Request Examples"
description: "Copy/paste request fixtures for analysis endpoints (REST + GraphQL) with provenance-first, contract-first patterns."
path: "api/contracts/examples/requests/analysis/README.md"
version: "0.1.0"
status: "draft"
last_updated: "2026-01-24"
tags: ["kfm", "api", "contracts", "examples", "requests", "analysis"]
---

# 🔬 Analysis Request Examples (KFM API Contracts)

![Contract-First](https://img.shields.io/badge/Contract--First-222?style=flat)
![Provenance-First](https://img.shields.io/badge/Provenance--First-222?style=flat)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![OpenAPI](https://img.shields.io/badge/OpenAPI-6BA539?logo=openapiinitiative&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?logo=graphql&logoColor=white)
![PostGIS](https://img.shields.io/badge/PostGIS-4169E1?logo=postgresql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-008CC1?logo=neo4j&logoColor=white)
![STAC](https://img.shields.io/badge/STAC-0B3D91?style=flat)
![DCAT](https://img.shields.io/badge/DCAT-0B3D91?style=flat)
![PROV-O](https://img.shields.io/badge/PROV--O-0B3D91?style=flat)
![OPA](https://img.shields.io/badge/OPA%20%2F%20Conftest-7A3E9D?style=flat)

> [!NOTE]
> This folder is for **request examples** (fixtures) used by 📘 docs, ✅ API contract tests, 🧪 integration tests, and 🧰 client SDK examples.
>
> The goal is simple: **every analysis request is reproducible, auditable, and schema-valid**—no “mystery inputs,” no “mystery layers.” 🧾🗺️

---

## 📌 What lives here

This directory contains **copy/pasteable requests** for analysis-type operations, such as:

- 📈 time series + indicators (e.g., NDVI per county)
- 🧮 aggregations + histograms (e.g., landcover classes in a bbox)
- 🧭 spatial ops (buffer, intersect, area summaries, joins)
- 🧵 async “analysis jobs” (long-running workflows)
- 🤖 Focus Mode / AI-assisted analysis requests (with evidence constraints)
- 🧪 deterministic simulation / “what-if” runs (seeded + auditable)

---

## 🧱 Design constraints (non‑negotiables)

> [!IMPORTANT]
> These examples assume KFM’s platform principles: **contract-first** + **evidence/provenance-first** + **policy gates**.

### ✅ 1) Contract-first payloads
Every request example in this directory should:
- validate cleanly against the endpoint’s JSON Schema / Pydantic model
- be stable and deterministic when possible (especially simulations)
- carry explicit versioning where relevant (`schema_version`, `api_version`, etc.)

### ✅ 2) Provenance-first analysis
Analysis requests must contain enough information to:
- reproduce the run later (inputs, filters, parameters, seed, versions)
- generate a PROV record (who/what/when/how)
- link outputs back to cataloged datasets and distributions

### ✅ 3) Evidence triplet mindset (publishable outputs)
When an analysis produces something publishable (layer, story, model output), it should be promotable into:
- **STAC** (assets/observations)
- **DCAT** (dataset metadata + distributions)
- **PROV** (lineage of how it was produced)

### ✅ 4) Policy-aware by default
Requests should include policy signals that make enforcement straightforward:
- classification (public / restricted / sensitive)
- privacy constraints for aggregated queries (minimum counts, etc.)
- access intent (UI display vs research export vs public embed)

---

## 🗂️ Directory map (suggested)

```text
api/contracts/examples/requests/analysis/
├── ✅📄 README.md                                  # 👈 you are here 📌 How analysis request examples are named, validated, and used in tests
├── 📥🔎 analysis__ndvi_timeseries__county.get.http  # Example GET request (raw HTTP): NDVI timeseries by county (params/headers)
├── 📤📈 analysis__ndvi_timeseries__county.post.json # Example POST body: NDVI timeseries query (time range + county selector)
├── 📤📊 analysis__aggregate__landcover_histogram.post.json
│   # Example POST body: landcover histogram aggregation (bins/categories + region/time filters)
├── 📤🗺️ analysis__spatial__buffer_intersect_area.post.json
│   # Example POST body: spatial op (buffer geometry → intersect → area totals; includes units + CRS assumptions)
├── 📥🧱 analysis__tiles__landcover_mvt.get.http     # Example GET request (raw HTTP): landcover MVT tiles (z/x/y + style hints)
├── 📤🧪 analysis__simrun__drought_2040.post.json    # Example POST body: simulation run request (scenario params + seeds + outputs)
├── 📤🔎📚 analysis__focus__ask_with_context.post.json # Example POST body: Focus ask routed via analysis surface (context + citations)
├── 📤🧵 analysis__pulse__thread_create.post.json    # Example POST body: create a pulse thread (summary + evidence refs)
└── 📤📡 analysis__realtime__water_level.post.json   # Example POST body: realtime query (station id + window + freshness constraints)
```

> [!TIP]
> File names aren’t links (on purpose). CI typically validates *links*, so keep fixtures discoverable by naming, not brittle internal references. 🧩

---

## 🧭 Request flow (mental model)

```mermaid
flowchart LR
  ui[🧑‍💻 UI / Client] --> api[⚙️ API Gateway (FastAPI)]
  api --> v[✅ Schema + Policy Validation]
  v -->|sync| pg[(🗺️ PostGIS)]
  v -->|graph| neo[(🕸️ Neo4j)]
  v -->|async| job[🧵 Job Runner / Pipeline]
  job --> cat[📚 STAC + DCAT + PROV]
  job --> art[📦 Artifacts (tiles, parquet, geotiff)]
  cat --> api
  art --> api
  api --> ui
```

---

## 🧩 Shared conventions

### Headers (recommended)
Use these headers consistently in request examples:

- `Content-Type: application/json`
- `X-Request-Id: <uuid-or-ulid>`
- `Idempotency-Key: <stable-key>` (especially for POST)
- `Authorization: Bearer <token>` (omit in public examples as needed)
- `X-KFM-Client: web|cli|agent`
- `X-KFM-Trace: <trace-id>` (optional; great for debugging)

### Identifiers
Prefer **stable IDs** over raw URLs:
- `dataset_id`: `kfm.ks.<domain>.<name>.<version>`
- `place_id`: `kfm.place.<...>`
- `story_id`: `kfm.story.<...>`
- `concept_ids`: `kfm.concept.<...>`

### Spatial + temporal shapes
- Geometry: **GeoJSON**
- Bounding box: `[minLon, minLat, maxLon, maxLat]` (WGS84 unless specified)
- Time: ISO 8601 timestamps; use inclusive `start` + exclusive `end` unless your schema states otherwise.

---

## 🧱 Recommended “analysis request envelope” (copy/paste)

> [!NOTE]
> Not every endpoint needs every field, but examples should **prefer the same top-level shape** so clients can reuse code.

```json
{
  "request_id": "req_01J4X3Z8K4W9J2A5VQ2Y7D6B3N",
  "idempotency_key": "analysis:ndvi_timeseries:county=Douglas:start=2010-01-01:end=2020-12-31",
  "actor": {
    "type": "user",
    "id": "user:anonymous",
    "roles": ["viewer"]
  },
  "context": {
    "ui": {
      "viewport": { "bbox": [-96.0, 38.2, -94.4, 39.4], "zoom": 7 },
      "active_layers": ["kfm.ks.landcover.2020"],
      "selected": { "kind": "place", "id": "kfm.place.ks.douglas.county" }
    },
    "time": { "start": "2010-01-01", "end": "2020-12-31", "step": "month" }
  },
  "inputs": {
    "datasets": ["kfm.ks.remote_sensing.landsat.ndvi.v1"],
    "filters": { "county": "Douglas" },
    "parameters": { "cloud_mask": true, "engine": "local" }
  },
  "output": {
    "mode": "inline",
    "formats": ["json"],
    "include_debug": false
  },
  "provenance": {
    "capture": true,
    "include_parameters": true,
    "link_mode": "ref"
  },
  "policy": {
    "classification": "public",
    "privacy": { "min_count": 10, "noise": "none" }
  }
}
```

---

## 🧪 Request examples

### 1) 📈 NDVI time series (quick analysis)

<details>
<summary><strong>GET example (query params)</strong> 🧾</summary>

```http
GET /api/analysis/ndvi?county=Douglas&start=2010-01-01&end=2020-12-31&step=month HTTP/1.1
X-Request-Id: req_01J4X3Z8K4W9J2A5VQ2Y7D6B3N
X-KFM-Client: web
```

✅ Use this style for “fast” analyses that can run synchronously.

</details>

<details>
<summary><strong>POST example (job-friendly body)</strong> 🧵</summary>

```http
POST /api/analysis/ndvi HTTP/1.1
Content-Type: application/json
Idempotency-Key: analysis:ndvi_timeseries:Douglas:2010-01-01:2020-12-31
X-Request-Id: req_01J4X40T8Y7JK2N6S8S7K9FQ1A
X-KFM-Client: web

{
  "context": {
    "time": { "start": "2010-01-01", "end": "2020-12-31", "step": "month" }
  },
  "inputs": {
    "datasets": ["kfm.ks.remote_sensing.landsat.ndvi.v1"],
    "filters": { "place_id": "kfm.place.ks.douglas.county" },
    "parameters": {
      "cloud_mask": true,
      "engine": "gee",
      "bands": ["NIR", "RED"]
    }
  },
  "output": {
    "mode": "inline",
    "formats": ["json", "csv"]
  },
  "provenance": { "capture": true, "link_mode": "ref" },
  "policy": { "classification": "public" }
}
```

🧠 Notes:
- `engine: "gee"` is useful when remote sensing computation is delegated to a managed compute backend.
- Use POST when you might later evolve to an async job without breaking clients.

</details>

---

### 2) 🧮 Landcover histogram (bbox + time)

<details>
<summary><strong>POST /api/analysis/aggregate</strong> 📊</summary>

```json
{
  "request_id": "req_01J4X4C4T4Z0R5H5ZJY0V0ZQ3R",
  "idempotency_key": "analysis:landcover_histogram:bbox=-97.2,38.6,-96.4,39.1:year=2020",
  "inputs": {
    "datasets": ["kfm.ks.landcover.2020"],
    "filters": {
      "bbox": [-97.2, 38.6, -96.4, 39.1],
      "time": { "start": "2020-01-01", "end": "2021-01-01" }
    },
    "parameters": {
      "group_by": "class_id",
      "stat": "count"
    }
  },
  "output": {
    "mode": "inline",
    "formats": ["json"],
    "include_geometry": false
  },
  "provenance": { "capture": true },
  "policy": {
    "classification": "public",
    "privacy": { "min_count": 20, "noise": "none" }
  }
}
```

✅ Perfect for:
- legends that need counts
- dashboards
- “summary” panels in the UI

</details>

---

### 3) 🧭 Buffer + intersect + area summary

<details>
<summary><strong>POST /api/analysis/spatial</strong> 🗺️</summary>

```json
{
  "request_id": "req_01J4X4JX0NR3R7Z8A7R5Y3T2D0",
  "inputs": {
    "datasets": ["kfm.ks.hydrology.rivers.v1", "kfm.ks.boundaries.counties.v1"],
    "filters": {
      "place_id": "kfm.place.ks.douglas.county"
    },
    "parameters": {
      "operation": "buffer_intersect_area",
      "buffer_meters": 500,
      "target_dataset_id": "kfm.ks.hydrology.rivers.v1",
      "within_dataset_id": "kfm.ks.boundaries.counties.v1",
      "units": "sq_km"
    }
  },
  "output": {
    "mode": "inline",
    "formats": ["json"],
    "include_debug": true
  },
  "provenance": { "capture": true, "include_parameters": true },
  "policy": { "classification": "public" }
}
```

🔎 Great for:
- “impact zones” around features
- quick spatial joins without shipping huge GeoJSON blobs to the client

</details>

---

### 4) 🧱 Vector tile request (analysis layer output)

<details>
<summary><strong>GET /tiles/&lt;layer&gt;/{z}/{x}/{y}.pbf</strong> 🧊</summary>

```http
GET /tiles/landcover/7/30/50.pbf HTTP/1.1
X-Request-Id: req_01J4X4P3AJ0SR1B9Z9D1Q6E1M2
X-KFM-Client: web
```

🧠 Notes:
- Keep tiles “dumb” and fast: styling belongs client-side.
- Aggregation endpoints complement tiles: tiles show *where*, aggregates show *how much*.

</details>

---

### 5) 🧪 Deterministic simulation run (“what-if”)

<details>
<summary><strong>POST /api/sim/run</strong> 🎛️</summary>

```json
{
  "request_id": "req_01J4X4WQZ2M0Y7GQ5E3W2Q2G2W",
  "idempotency_key": "simrun:drought_2040:seed=1337:Douglas",
  "inputs": {
    "scenario": {
      "name": "drought_2040",
      "time": { "start": "2030-01-01", "end": "2041-01-01" },
      "place_id": "kfm.place.ks.douglas.county",
      "assumptions": [
        "simulation_is_evidence_not_truth",
        "report_uncertainty"
      ]
    },
    "datasets": [
      "kfm.ks.climate.historical.v1",
      "kfm.ks.landcover.2020"
    ],
    "parameters": {
      "model": "ModelX",
      "ensemble": ["optimistic", "pessimistic"],
      "seed": 1337,
      "virtual_clock": true
    }
  },
  "output": {
    "mode": "artifact",
    "formats": ["geotiff", "stac", "prov"],
    "publish": {
      "draft_pr": true,
      "promotion_bundle": true
    }
  },
  "provenance": {
    "capture": true,
    "include_parameters": true,
    "link_mode": "embed"
  },
  "policy": {
    "classification": "restricted",
    "review_required": true
  }
}
```

✅ Why it looks “heavy”:
- deterministic runs need explicit `seed` + environment constraints
- promoting results should produce a “bundle” (STAC/DCAT/PROV + artifacts) for review

</details>

---

### 6) 🤖 Focus Mode “ask” (analysis with evidence constraints)

<details>
<summary><strong>POST /api/focus</strong> 🧠🧾</summary>

```json
{
  "request_id": "req_01J4X52T4Y7JH2ZV8J1J7B0D9P",
  "question": "How has drought impacted Kansas agriculture in the last decade?",
  "context": {
    "ui": {
      "viewport": { "bbox": [-102.0, 36.9, -94.6, 40.0], "zoom": 6 },
      "active_layers": [
        "kfm.ks.climate.drought_index.v2",
        "kfm.ks.agriculture.crop_yields.v1"
      ]
    },
    "time": { "start": "2015-01-01", "end": "2025-01-01" },
    "focus_concepts": ["kfm.concept.drought", "kfm.concept.agriculture"]
  },
  "constraints": {
    "require_citations": true,
    "refuse_if_insufficient_evidence": true,
    "show_reasoning_audit": true
  },
  "output": {
    "mode": "inline",
    "formats": ["markdown", "json"]
  },
  "provenance": { "capture": true },
  "policy": { "classification": "public" }
}
```

✅ Recommended defaults:
- force citations and refusal when evidence is insufficient
- include UI context (viewport, layers, time) to keep answers grounded

</details>

---

### 7) 🧾 Story / narrative evidence bundle (internal authoring)

<details>
<summary><strong>POST /api/story/submit (evidence-manifest aware)</strong> 📚</summary>

```json
{
  "request_id": "req_01J4X5A7WZ2E3J4M5N6P7Q8R9S",
  "story": {
    "title": "Drought & Agriculture: 2015–2025",
    "summary": "A guided narrative that links drought indices to agricultural outcomes.",
    "steps": [
      { "camera": { "bbox": [-100.0, 37.5, -96.0, 39.5], "zoom": 7 }, "text": "Drought conditions intensify in central Kansas..." }
    ],
    "citations_block": [
      "kfm.ks.climate.drought_index.v2",
      "kfm.ks.agriculture.crop_yields.v1"
    ],
    "evidence_manifest_ref": "evidence/EM-0001.yaml"
  },
  "provenance": { "capture": true, "link_mode": "embed" },
  "policy": { "classification": "public" }
}
```

🧠 Notes:
- Humans can author stories; agents can assist, but evidence is always explicit.
- The evidence manifest can record checksums, query params, and exact sources.

</details>

---

### 8) 📍 Pulse thread creation (geo-tagged, evidence-backed)

<details>
<summary><strong>POST /api/pulse_threads</strong> 🌋</summary>

```json
{
  "request_id": "req_01J4X5H8Q2N0A9T0F0Z3Y8Z7K1",
  "pulse": {
    "title": "Reservoir levels dropping faster than seasonal norm",
    "kind": "anomaly",
    "location": { "type": "Point", "coordinates": [-95.68, 39.05] },
    "time": { "observed_at": "2026-01-24T03:15:00Z" },
    "linked_entities": [
      { "type": "dataset", "id": "kfm.ks.hydrology.reservoir_levels.v1" },
      { "type": "concept", "id": "kfm.concept.drought" }
    ],
    "evidence_manifest_ref": "evidence/EM-0042.yaml"
  },
  "provenance": { "capture": true },
  "policy": { "classification": "public" }
}
```

✅ Useful for:
- automated “watchers” that detect anomalies (GTFS-RT, sensors, alerts)
- human analysts who want to capture a geo-tagged insight with traceability

</details>

---

### 9) ⏱ Real-time station query (latest observation)

<details>
<summary><strong>POST /api/transport/buses or /api/hydrology/stations/latest</strong> 🚰</summary>

```json
{
  "request_id": "req_01J4X5NQH0B2Z9Q3Y2B7R1D8F4",
  "inputs": {
    "station_id": "kfm.station.usgs.nwis.topeka.ks_river",
    "as_of": "now"
  },
  "output": { "mode": "inline", "formats": ["geojson", "json"] },
  "provenance": { "capture": true },
  "policy": {
    "classification": "public",
    "respect_sensitive_station_flags": true
  }
}
```

🧠 Notes:
- “as_of: now” should still be logged in provenance so answers can cite a specific reading timestamp.

</details>

---

## ✅ Validation & CI expectations (why examples matter)

These request fixtures are not “just documentation”:
- they are **contract test vectors**
- they enforce that request/response schemas stay stable
- they reduce regressions when endpoints evolve

> [!TIP]
> If you add a new analysis endpoint, add at least:
> 1) a **minimal valid request**
> 2) a **maximal request** (all optional fields)
> 3) at least one **policy edge case** (classification / privacy / sensitive geometry)

---

## 🧰 How to add a new request example

1. 🧾 Name it predictably:  
   `analysis__<capability>__<scope>.<method>.<json|http>`
2. ✅ Ensure the payload is schema-valid (no “extra” fields).
3. 🧬 Include provenance intent (`provenance.capture: true`) unless the endpoint explicitly forbids it.
4. 🧷 Use stable IDs (dataset/place/concept), not raw URLs.
5. 🛡️ Include `policy.classification` and any privacy constraints required for aggregates.
6. 🧪 Make sure CI contract tests can run it deterministically (idempotency key, seed, etc.).

---

## 📚 Related docs (human-readable)

These request patterns are aligned with KFM’s broader docs on:
- API design (FastAPI + OpenAPI + GraphQL)
- evidence-first catalogs (STAC/DCAT/PROV)
- PostGIS tile + aggregation patterns
- Focus Mode AI (citations, context awareness, refusal on missing evidence)
- deterministic simulation tooling (kfm-sim-run)
- policy-as-code enforcement (OPA + Conftest)
- UI principles (“the map behind the map”)

> [!NOTE]
> Keep this README practical. The deep philosophy lives in the architecture + governance docs. This folder is about **requests you can run today** ✅

---
