---
title: "🌫️ KFM — /air/now FastAPI Endpoint (OpenAQ v3 · CAMS NRT · Redis cache · PROV headers)"
path: "src/api/air/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Reliability Eng."
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "API Module"
intent: "serve-near-real-time-air-quality"
semantic_document_id: "kfm-api-air-now-v11.2.6"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:api:air:now:readme:v11.2.6"
event_source_id: "ledger:src/api/air/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/air-quality-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/air-quality-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"

header_profile: "standard"
footer_profile: "standard"
---

# 🌫️ `/air/now` — Near-Real-Time Air Quality API

## 📘 Overview

The `/air/now` module implements a **FastAPI** endpoint that serves **near-real-time air-quality readings** for a given latitude/longitude (and optional radius) by blending:

- **OpenAQ v3** ground monitors (observed data), and  
- **CAMS NRT** model fields (gridded forecasts / analyses).

Results are:

- Cached in **Redis** for approximately 10 minutes, and  
- Returned with **provenance headers** so dashboards, APIs, and Story Nodes can trace readings back to source telemetry, cache state, and KFM PROV bundles.

This module is part of the KFM air-quality pipeline:

> OpenAQ v3 / CAMS NRT → ETL & normalization → STAC/DCAT/PROV → Neo4j → `/air/now` API → dashboards / Story Nodes / Focus Mode

and is governed by the **Air Quality Sources & API Governance** standard in `docs/data/air-quality/README.md` (not shown here).

---

## 🗂️ Directory Layout

The `/air/now` API module lives under `src/api/air/` and interacts with ETL, graph, and telemetry components:

~~~text
📁 src/
  📁 api/
    📄 README.md                 # (planned) API root index
    📁 air/
      📄 README.md               # This file – /air/now API module spec
      📄 router.py               # FastAPI router and /air/now endpoint implementation
      📄 models.py               # Pydantic models for requests/responses
      📄 dependencies.py         # Dependency wiring (Redis, OpenAQ client, CAMS client)
      📄 cache.py                # Redis cache helpers and key/TTL logic
      📄 provenance.py           # PROV header and lineage bundle helpers
      📄 telemetry.py            # Metrics + traces for air-quality API
📁 data/
  📁 air-quality/
    📁 stac/                     # STAC catalogs for air-quality datasets
    📁 dcat-prov/                # DCAT + PROV bundles for air-quality sources
📁 schemas/
  📁 telemetry/
    📄 air-quality-v11.json      # Telemetry schema referenced by telemetry_ref
📁 releases/
  📁 v11.2.6/
    📄 air-quality-telemetry.json # Aggregated telemetry bundle for air APIs
~~~

Any new files under `src/api/air/` MUST be documented here and in the air-quality governance docs as appropriate.

---

## 🧱 Architecture

### 1. Endpoint Definition

- **Method**: `GET /air/now`  
- **Purpose**: Return blended near-real-time air-quality metrics for a given coordinate (and optional radius), with clear provenance and cache metadata.

#### Query Parameters

- `lat` (float, required)  
- `lon` (float, required)  
- `radius_km` (float, default: `25.0`)  
  - Search window for OpenAQ ground stations.  
- `pollutants` (comma-separated list, default: `pm25,pm10,o3,no2,so2,co`)  
- `units` (enum, default: `ugm3`)  
  - Allowed: `ugm3`, `aqi_us`.  
- `blend` (enum, default: `smart`)  
  - Allowed:
    - `smart` — combine ground + model data (see blending rules below).  
    - `ground_only` — use OpenAQ only (if available).  
    - `model_only` — use CAMS NRT only.

#### Response Headers

- `X-KFM-PROV-HASH`  
  - SHA256 over the normalized PROV/lineage bundle for this response.
- `X-KFM-SOURCE-LIST`  
  - Comma-separated list of upstream sources used (e.g., `openaq,cams-nrt`).
- `X-KFM-CACHE`  
  - `HIT` or `MISS` (or `STALE` if staleness window is explicitly supported).
- `X-KFM-TTL-SEC`  
  - Remaining TTL in seconds as observed at response time.

### 2. Internal Flow

High-level internal steps:

1. Validate and normalize query (lat/lon, radius, pollutants, units, blend).  
2. Generate a cache key (e.g., hashed tuple of normalized query parameters).  
3. Look up Redis cache:
   - If **HIT** and not stale, return cached payload with `X-KFM-CACHE: HIT`.  
4. If cache MISS:
   - Query **OpenAQ v3** for ground stations within `radius_km`.  
   - Query **CAMS NRT** for the relevant grid cell(s).  
   - Apply blending strategy (see below).  
   - Build response object and PROV lineage bundle.  
   - Store serialized response in Redis with TTL (~600 seconds).  
5. Emit telemetry and traces (latency, errors, cache hit rates, upstream timings).  
6. Return JSON response + headers.

### 3. Blending Strategy (Smart Mode)

When `blend=smart`:

- Prefer **ground measurements** when:
  - At least one station is available and recent (e.g., ≤ 60–90 min old).  
- Use **CAMS NRT model** to:
  - Fill in spatial gaps (no stations in radius).  
  - Smooth anomalies or short outages using weighted averages.  
- Example weight scheme:
  - Ground weight decays with station distance and age.  
  - Model weight increases when ground coverage is sparse or stale.

Actual blending parameters (distance thresholds, staleness windows, weights) MUST be:

- Config-driven (`configs/air/air-now-blend.yaml` or equivalent).  
- Documented in air-quality governance docs and/or this README if changed.

---

## 📦 Data & Metadata

### 1. Response Schema (Conceptual)

The Pydantic model returned by `/air/now` SHOULD follow this structure:

~~~json
{
  "coord": { "lat": 39.05, "lon": -95.67 },
  "timestamp": "2025-12-11T04:20:00Z",
  "pollutants": {
    "pm25": { "value": 8.2, "units": "µg/m³", "source": "blend" },
    "o3":   { "value": 41.0, "units": "µg/m³", "source": "blend" }
  },
  "blend_meta": {
    "strategy": "smart",
    "ground_points": 3,
    "model_cell": "0.1deg",
    "weights": { "ground": 0.7, "model": 0.3 }
  },
  "provenance_ref": "urn:kfm:prov:air:now:39.05:-95.67:2025-12-11T04:20:00Z"
}
~~~

Key fields:

- `coord` — the coordinate actually used for blending (may be snapped or validated).  
- `timestamp` — ISO-8601 UTC timestamp for the reading (blend time).  
- `pollutants` — dictionary keyed by pollutant ID:
  - Each object MUST have:
    - `value` (numeric),
    - `units` (string, consistent with `units` parameter),
    - `source` (`ground`, `model`, or `blend`).  
- `blend_meta` — optional diagnostic information about the blending process.  
- `provenance_ref` — URN or URL referencing the PROV bundle describing upstream data and processing steps.

### 2. Units and Conversions

- Default unit: `ugm3` (micrograms per cubic meter).
- Optional: `aqi_us` for US-style AQI.
- Conversion logic MUST be:
  - Config-driven (lookup tables, breakpoints).
  - Documented in a shared air-quality unit conversion spec (e.g., `docs/data/air-quality/units.md`).

---

## 🌐 STAC, DCAT & PROV Alignment

Even though `/air/now` is a live API endpoint, its outputs are tied to STAC/DCAT/PROV as follows:

- **STAC / DCAT**  
  - Underlying datasets (OpenAQ station time series, CAMS NRT gridded products) are cataloged via STAC/DCAT in `data/air-quality/`.  
  - `/air/now` responses reference these datasets through `provenance_ref` and internal identifiers in the PROV bundle.

- **PROV-O**  
  - Each response can be associated with a PROV `Activity` representing the `/air/now` inference for a particular coord/time.  
  - Upstream `Entity` records include:
    - OpenAQ station readings used for the blend.  
    - CAMS NRT grid values.  
    - Configuration versions and blending parameters.  
  - `Agent`s include:
    - The KFM air-quality service.  
    - Any human or automated processes responsible for the configuration.

- **Headers**  
  - `X-KFM-PROV-HASH` allows downstream systems to verify that the returned payload corresponds to a particular normalized PROV bundle (hash-based integrity check).  

---

## ⚖ FAIR+CARE & Governance

Air-quality data and derived products are part of KFM’s environmental monitoring responsibilities and must:

- Be **transparent**:
  - Expose source types (`ground`, `model`, `blend`).
  - Provide clear units and timestamps.
- Be **responsibly interpreted**:
  - `/air/now` is not a medical device; health advice belongs in separate, curated Story Nodes or external public health guidance.
- Respect **FAIR+CARE**:
  - FAIR: Reusable metadata and clear provenance, enabling reproducible analyses.  
  - CARE: Ensure that narratives and dashboards built on `/air/now` do not misrepresent exposure or risk for vulnerable communities and do not undermine environmental justice considerations.

Any Story Nodes or Focus Mode narratives that rely on `/air/now` must clearly state:

- That CAMS is a model product (not a direct measurement).  
- That OpenAQ is a federation of monitoring networks with heterogeneous coverage and quality.  

---

## 🧪 Validation & CI/CD

Changes to the `/air/now` module MUST:

- Pass `markdown-lint` and front-matter schema validation for this README.  
- Pass air-quality test suites under `src/api/air/tests/` (e.g., unit tests for:
  - parameter validation,
  - blending logic,
  - cache behavior,
  - error handling).
- Emit telemetry conforming to `air-quality-v11.json`:
  - Latency, error rates, cache hit/miss ratio.
  - Upstream availability (OpenAQ / CAMS) and fallback behavior.

Recommended CI checks:

- Contract tests for response schema (`models.py` vs. example JSON).  
- Integration tests with mock OpenAQ/CAMS and Redis backends.  
- Rate-limiting and failure-mode tests to ensure graceful degradation.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                  |
|----------:|-----------:|----------------------------------------------------------|
| v11.2.6   | 2025-12-11 | Initial API module README for `/air/now` (NRT blend API) |

---

<div align="center">

🌫️ **KFM — /air/now FastAPI Endpoint**  
Near-Real-Time Air Quality · OpenAQ v3 · CAMS NRT · Redis · PROV Headers  

[📘 Docs Root](../../../docs/README.md) · [🧭 API Index](../README.md) · [🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>