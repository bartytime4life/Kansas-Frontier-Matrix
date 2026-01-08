<div align="center">

# 📡 KFM API Specification Hub

![Status](https://img.shields.io/badge/status-draft-orange)
![Contract First](https://img.shields.io/badge/contract--first-OpenAPI%20%2B%20GraphQL-blue)
![Geospatial](https://img.shields.io/badge/geospatial-STAC%20%7C%20DCAT%20%7C%20PROV-brightgreen)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE-6f42c1)

**The canonical home for Kansas Frontier Matrix (KFM) API contracts, conventions, examples, and governance gates.**

</div>

---

## 🎯 What this folder is

This directory defines the **public contract** between:

- 🧠 **Knowledge systems** (Neo4j graph + provenance)
- 🗂️ **Catalog systems** (STAC/DCAT/PROV)
- 🧪 **Analysis & simulation** services (Focus Mode + ABM jobs)
- 🗺️ **UI clients** (React + MapLibre time slider, panels, Story Nodes)
- 🤖 **Automation** (ingest triggers, validation hooks, release gating)

> [!IMPORTANT]
> **UI must use the API only** (no direct graph access). This is a governance + security + reproducibility requirement.

---

## 🧭 Quick navigation

- ✅ **Contract artifacts**: see **📦 Contract artifacts & folder layout**
- 🧱 **Rules & invariants**: see **🛡️ Non‑negotiables (governed)**
- 🧩 **Endpoint index**: see **🗺️ API surface map**
- 🧬 **Story Node versioning**: see **🧷 STAC Versioning + Story Nodes**
- 📏 **Schemas & examples**: see **🧪 Validation, schemas, and examples**

---

## 🧩 Architecture context (why the API looks like this)

KFM is a modular system that ingests heterogeneous historical + geospatial data, normalizes it into structured catalogs/databases, and serves it through an API to an interactive map/timeline UI. The AI reasoning layer cross-references spatial and textual repositories to generate explainable insights (Focus Mode), while maintaining provenance and governance controls. 🧭🗺️🧠

Key architectural implications for the API:

- **Catalog-first** publishing (STAC-like JSON + DCAT + PROV lineage)
- **Graph-backed** semantic navigation (Place ↔ Event ↔ Layer ↔ Document)
- **Deterministic** results and version pinning (reproducibility)
- **Governed** disclosure (FAIR+CARE + sensitive-location generalization)

---

## 📦 Contract artifacts & folder layout

> [!NOTE]
> These files may be created incrementally. The README is the index + ruleset; the *contracts* are the source of truth for implementation.

~~~text
📂 docs/specs/api/
├── 📄 README.md                    # You are here (rules, index, conventions)
├── 🧾 openapi.yaml                 # REST contract (canonical)
├── 🧬 graphql/
│   ├── 📜 schema.graphql           # GraphQL schema (canonical)
│   └── 🧩 operations/              # Saved queries (bounded, governed)
├── 🧪 examples/
│   ├── 📤 requests/                # Example request payloads
│   └── 📥 responses/               # Example responses (golden files)
├── 🧷 schemas/
│   ├── 🧱 api/                     # JSON Schemas for request/response objects
│   ├── 🛰️ stac/                    # STAC profiles + extensions (kfm-*)
│   └── 📡 telemetry/               # Telemetry event schemas (focus-telemetry.json)
└── 🧰 tests/
    ├── ✅ contract/                # Contract tests (REST + GraphQL)
    └── 🛡️ governance/              # Redaction + policy gate tests
~~~

---

## 🗺️ API surface map

KFM exposes **REST** and **GraphQL**:

- **REST (OpenAPI)**: stable resources, jobs, bulk retrieval, file-style assets
- **GraphQL**: graph-shaped queries for UI (Place/Event/Layer/Document traversals)

### ✅ Core REST domains

| Domain | Typical client | What it serves |
|---|---|---|
| 🗂️ Catalog | UI + pipelines | Datasets, STAC Collections/Items, search by bbox/time |
| 🕸️ Graph | UI | Governed entity navigation and relationship exploration |
| 🧠 Focus Mode | UI | Explainable narrative/insight packets with citations + provenance |
| 🧪 Simulation | UI + research | Async ABM jobs: submit → status → results |
| 🗺️ Tiles/Assets | UI | PMTiles/vector tiles/COGs/GeoParquet + metadata |
| 🧾 Provenance | auditors + UI | PROV bundles, run lineage, evidence links |
| 🔔 Automation | pipelines | Signed webhooks, idempotent ingest triggers |

---

## 🛡️ Non‑negotiables (governed)

These rules apply to **all** endpoints, REST or GraphQL:

1. 🧭 **No unbounded traversal**  
   - Enforce limits: `max_depth`, `max_nodes`, `max_time_range`, `max_bbox_area`, `max_items`.
2. 🔐 **No sensitive leakage**  
   - Apply redaction/generalization policy before results are returned.
3. 🧷 **No raw string-concatenated Cypher from clients**  
   - Prefer: saved queries, parameterized templates, allow-listed filters.
4. 🧾 **Deterministic ordering**  
   - Stable sorting required for pagination and reproducible outputs.
5. ⚖️ **Policy gates are first-class**  
   - Every response can explain *why* something was redacted/omitted (auditable).

> [!WARNING]
> If an API change impacts: **catalogs, ontology/graph labels, contracts, or Focus Mode behavior** → it requires a governance review gate (FAIR+CARE + security).

---

## 🧬 Versioning & compatibility

### API versioning

- **Base path**: `/api/v1` (recommended canonical)
- **SemVer** for contracts: `vMAJOR.MINOR.PATCH`
  - **MAJOR**: breaking change (rename/remove/meaning change)
  - **MINOR**: backward-compatible additive changes
  - **PATCH**: documentation/examples/tests only

### Deprecation rules

- Deprecations must include:
  - `Sunset` header date (when removed)
  - Replacement link in docs
  - Contract changelog entry

---

## 🔐 Authentication & authorization

> [!NOTE]
> The API is designed so that **public browsing** is possible for public assets, while **write/admin** actions require auth.

Suggested model (adjust per deployment):

- **Public**: catalog browse, generalized tiles, public story nodes
- **Contributor**: create story nodes, submit simulations (bounded)
- **Maintainer**: publish datasets, manage governance labels, approve releases

Auth mechanisms (supported patterns):

- 🔑 **Bearer tokens** (OAuth/OIDC) for user sessions
- 🧾 **API keys** for automation (scoped + rotated)
- ✅ **Signed webhooks** (HMAC/JWT) for inbound triggers

---

## 🧱 API conventions

### Content types

- Requests: `application/json`
- Geo: `application/geo+json` where appropriate
- Binary assets: `image/png`, `image/svg+xml`, `application/x-protobuf` (vector tiles), `application/octet-stream` (PMTiles), `image/tiff` (COGs)

### Standard headers

| Header | Direction | Purpose |
|---|---|---|
| `X-Request-Id` | client → server | Correlate logs across layers |
| `Idempotency-Key` | client → server | Safe retries for POST/PUT |
| `X-KFM-Client` | client → server | Client name/version (UI/pipeline) |
| `ETag` / `If-None-Match` | both | Cache + change detection |
| `Cache-Control` | server → client | Asset caching policies |

### Pagination

Use cursor-based pagination for large lists:

- `page[limit]=100`
- `page[cursor]=<opaque>`

Responses include:

```json
{
  "data": [],
  "meta": {
    "next_cursor": "opaque",
    "count": 100
  }
}
```

### Error format

All errors are JSON and include an audit-friendly envelope:

```json
{
  "error": {
    "code": "KFM_BAD_REQUEST",
    "message": "bbox is invalid",
    "details": { "bbox": "must be 4 numbers" }
  },
  "meta": {
    "request_id": "req_...",
    "trace_id": "trace_..."
  }
}
```

---

## 🧾 Core resource model

### Identifiers

Prefer stable, portable identifiers:

- `id`: short stable string (slug-like) for URLs
- `urn`: optional global ID (e.g., `urn:kfm:item:...`)
- `version`: semantic or date-based version string

### Minimum resource shapes

- 🗂️ **Dataset** (DCAT-aligned)
- 📦 **STAC Collection/Item** (assets + extensions + checksums)
- 🧬 **Provenance** (PROV activity/agent/entity bundles)
- 🕸️ **GraphEntity** (typed nodes: Place/Event/Layer/Document/StoryNode)
- 🧠 **FocusPacket** (summary + citations + provenance pointers)
- 🧪 **SimulationJob** (async lifecycle + artifacts)

---

## 🗂️ Catalog & STAC endpoints (REST)

### Dataset metadata

- `GET /api/v1/datasets/{dataset_id}`  
  Returns DCAT-like dataset descriptor.

### Spatiotemporal search

- `GET /api/v1/catalog/search?bbox=minX,minY,maxX,maxY&datetime=..`  
  Returns STAC Items matching bbox/time.

### STAC native (recommended structure)

- `GET /api/v1/stac/collections`
- `GET /api/v1/stac/collections/{collection_id}`
- `GET /api/v1/stac/items/{item_id}`
- `POST /api/v1/stac/search` (STAC-style search body)

---

## 🧷 STAC Versioning + Story Nodes (lineage, diff, lock)

KFM extends STAC Items with versioning fields:

- `properties.version`
- `properties.deprecated`
- `links[rel=predecessor|successor|latest]`
- optional branching: `links[rel=alternate]`

### Lineage resolution

- `GET /api/v1/stac/items/{id}/lineage`

Returns a stable lineage packet:

```json
{
  "predecessors": [],
  "current": {},
  "successors": [],
  "latest": {}
}
```

### Version diff

- `GET /api/v1/stac/items/{id}/diff?against={otherId}`

Diff should include:

- metadata field deltas
- asset inventory changes
- geometry/extent diffs
- quality flags

### Version lock (Focus Mode reproducibility)

- `POST /api/v1/focus/story-node/{id}/lock-version/{versionId}`

Locking a version must:

- freeze map layers & derived panels to that version
- emit telemetry event `version_locked`
- stamp outputs with:
  - STAC Item ID
  - version string
  - full lineage chain
  - diff manifest hash
  - timestamp
  - user + session fingerprint

---

## 🕸️ Knowledge graph endpoints (REST + GraphQL)

### REST (bounded)

- `GET /api/v1/graph/entities?type=Place&name=...`
- `GET /api/v1/graph/entities/{entity_id}`
- `POST /api/v1/graph/query` (saved/templated queries only)

### GraphQL (UI-friendly)

- `POST /api/v1/graphql`

Rules:
- enforce max depth/complexity
- allow-list fields and relationships
- deterministic ordering and stable pagination

Example (conceptual):

```graphql
query PlaceWithEvents($id: ID!, $limit: Int!) {
  place(id: $id) {
    id
    name
    events(limit: $limit, sort: CHRONO_ASC) {
      id
      title
      when { start end }
      sources { id title href }
    }
  }
}
```

---

## 🧠 Focus Mode endpoints (explainability-first)

Focus Mode returns narrative packets that are:

- provenance-backed
- citation-rich
- governance-aware (redaction/generalization applied)

### Focus summary

- `GET /api/v1/analysis/focus?entity={entity_id}`

Response shape (recommended):

```json
{
  "entity_id": "place:fort-hays",
  "summary_markdown": "…",
  "citations": [
    { "id": "c1", "title": "…", "href": "…", "confidence": 0.82 }
  ],
  "provenance": {
    "prov_activity_id": "prov:activity:focus@<run_id>",
    "inputs": ["stac:item:..."]
  },
  "governance": {
    "care_status": "public",
    "generalized": false
  },
  "meta": {
    "request_id": "req_...",
    "trace_id": "trace_..."
  }
}
```

---

## 🧪 Simulation endpoints (ABM jobs)

Simulations are async (submit → poll → fetch results).

- `POST /api/v1/simulations/abm`  
- `GET /api/v1/simulations/jobs/{job_id}`  
- `GET /api/v1/simulations/jobs/{job_id}/results`

Recommendations for reproducibility:

- accept `seed` and explicit `scenario_id`
- store parameters as an immutable artifact
- publish outputs as STAC assets + PROV activity linkage

---

## 🗺️ Tiles & assets endpoints (MapLibre-ready)

KFM serves geospatial assets in formats optimized for the web:

- **Vector**: PMTiles, vector tiles (`.pbf`)
- **Raster**: COGs (GeoTIFF), PNG previews
- **Analytics**: GeoParquet, NDJSON summaries
- **3D**: GLB scenes (when applicable)

Suggested endpoints:

- `GET /api/v1/tiles/{layer}/{z}/{x}/{y}.pbf`
- `GET /api/v1/assets/{asset_id}` → metadata + download URL (signed if needed)

Asset metadata should include:

- checksum (sha256 or multihash)
- provenance datasets + citations
- CARE status: `public | generalized | restricted`

---

## 🔔 Automation triggers (webhook/poll/object-event friendly)

If KFM exposes inbound trigger endpoints, they must be:

- authenticated (signature verification)
- idempotent (dedupe)
- retry-safe (bounded retries + DLQ)

Suggested endpoint family:

- `POST /api/v1/hooks/{source}`

Hard requirements (apply to all triggers):

- idempotency key derived from stable fields (event id / commit sha / object uri)
- structured retries with caps
- poison-event routing to DLQ
- provenance record linking trigger → pipeline run → artifacts

---

## 🧪 Validation, schemas, and examples

### Schemas

- Requests/responses are validated with **JSON Schema (2020‑12)** (recommended)
- STAC/DCAT/PROV profiles get their own schemas under `docs/specs/api/schemas/`

### CI hooks (recommended)

- ✅ contract tests for OpenAPI + GraphQL
- ✅ docs lint (front‑matter + links)
- ✅ STAC/DCAT validation
- ✅ FAIR+CARE checks (sensitive location inference detection)
- ✅ telemetry export / governance ledger append

---

## 📡 Observability & auditability

Minimum observability expectations:

- every response includes `request_id` + `trace_id`
- long-running tasks expose a `job_id` and status timeline
- publish run artifacts with hashes and provenance pointers
- telemetry events (UI + pipeline) can be aggregated into `focus-telemetry.json`

---

## 📚 Project library (non‑normative references)

> [!NOTE]
> These documents inform the system design (modeling, statistics, geospatial engineering, web rendering, governance, security). They are **not** the API contract, but they influence how we structure contracts, schemas, and constraints.

<details>
<summary><strong>📚 Expand reference shelf</strong></summary>

### 🧠 Core system design docs
- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx` — platform architecture, services, API layer expectations
- 📄 `Latest Ideas.docx` — governance/automation patterns, metadata profiles, pipeline trigger rules, STAC/DCAT/PROV integration
- 📄 `Other Ideas.docx` — STAC versioning ↔ Story Nodes ↔ Focus Mode wiring, lineage/diff/lock endpoints, telemetry concepts
- 📘 `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf` — modular stack, STAC-like cataloging, map/timeline UI architecture

### 🗺️ Geospatial + cartography + mapping UX
- 📘 `making-maps-a-visual-guide-to-map-design-for-gis.pdf` — map design principles that impact tile/layer API metadata
- 📘 `python-geospatial-analysis-cookbook.pdf` — geospatial pipelines and analysis patterns (supports API resource shapes)
- 📘 `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` — remote sensing ingestion + derived product publication
- 📘 `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` — mobile/interactive mapping constraints (latency, tiles, UX)
- 📘 `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` — data store conventions for catalog/asset metadata

### 🧱 Web + visualization implementation references
- 📘 `responsive-web-design-with-html5-and-css3.pdf` — responsive UI consumption expectations for API payloads
- 📘 `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` — 3D asset delivery needs (GLB/tiles/streaming)
- 📘 `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` — image/media considerations for previews, legends, thumbnails

### 🧪 Modeling, simulation, and statistics (analysis endpoints)
- 📘 `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` — reproducibility + validation posture for simulations
- 📘 `Generalized Topology Optimization for Structural Design.pdf` — optimization workflows (influences job/parameter/result patterns)
- 📘 `Spectral Geometry of Graphs.pdf` — graph analytics framing (relevant to graph query constraints)
- 📘 `Scalable Data Management for Future Hardware.pdf` — performance/latency principles (query limits, caching, AQP considerations)
- 📘 `Understanding Statistics & Experimental Design.pdf` — experimental design discipline for evaluation endpoints
- 📘 `regression-analysis-with-python.pdf` — regression methodology references for analytics endpoints
- 📘 `Regression analysis using Python - slides-linear-regression.pdf` — quick reference for regression outputs/diagnostics
- 📘 `graphical-data-analysis-with-r.pdf` — exploratory analysis patterns (supports summary endpoints)
- 📘 `think-bayes-bayesian-statistics-in-python.pdf` — probabilistic reasoning patterns for uncertainty fields

### ⚖️ Ethics, governance, and law
- 📘 `Introduction to Digital Humanism.pdf` — human-centered constraints and responsible AI posture
- 📘 `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` — compliance framing for AI features
- 📘 `Principles of Biological Autonomy - book_9780262381833.pdf` — autonomy/agency framing (useful for ABM + agent modeling)

### 🔐 Security + reliability + systems engineering
- 📘 `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` — defensive posture and threat modeling
- 📘 `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` — security awareness reference (defensive use only)
- 📘 `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` — concurrency patterns for job execution + backpressure

### 🧰 General programming compendia (GoalKicker sets)
- 📘 `A programming Books.pdf`
- 📘 `B-C programming Books.pdf`
- 📘 `D-E programming Books.pdf`
- 📘 `F-H programming Books.pdf`
- 📘 `I-L programming Books.pdf`
- 📘 `M-N programming Books.pdf`
- 📘 `O-R programming Books.pdf`
- 📘 `S-T programming Books.pdf`
- 📘 `U-X programming Books.pdf`

### 🤖 ML practice reference
- 📘 `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` — practical ML workflows (model/feature lifecycle considerations)

</details>

---

## ✅ Definition of Done (DoD) for any API change

- [ ] OpenAPI and/or GraphQL contract updated
- [ ] Examples updated (`docs/specs/api/examples/…`)
- [ ] JSON Schemas updated (if shapes changed)
- [ ] Contract tests added/updated
- [ ] Governance gates satisfied (FAIR+CARE + sensitive-location rules)
- [ ] Determinism verified (stable ordering, bounded queries, reproducible outputs)
- [ ] Provenance pointers present for derived outputs
- [ ] Telemetry/events documented if UI behavior changes

---

<div align="center">

**🛡️ Deterministic · Provenanced · FAIR+CARE**

[⬅ Docs Root](../..) · [📦 Specs](../README.md) · [🌐 Governance](../../governance/ROOT_GOVERNANCE.md)

</div>

