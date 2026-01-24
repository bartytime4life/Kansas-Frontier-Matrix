<!-- File: src/pipelines/<domain_or_product>/README.md -->

<div align="center">

# 🧩 KFM Pipeline — `<domain_or_product>`

_Evidence-first, policy-guarded pipeline for the Kansas Frontier Matrix (KFM)_

[![Stage](https://img.shields.io/badge/pipeline-domain%2Fproduct-blue)](#-what-this-pipeline-does)
[![Contract](https://img.shields.io/badge/contract-raw%E2%86%92work%E2%86%92processed%E2%86%92catalogs%E2%86%92graph%E2%86%92api%E2%86%92ui%E2%86%92story%2Ffocus-informational)](#-pipeline-contract-non-negotiables)
[![Catalogs](https://img.shields.io/badge/catalogs-STAC%20%7C%20DCAT%20%7C%20PROV-7a5cff)](#-catalogs-stacdcatprov)
[![Stores](https://img.shields.io/badge/stores-PostGIS%20%2B%20Neo4j-0aa)](#-postgis--neo4j-integration)
[![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-success)](#-governance--policy)
[![Determinism](https://img.shields.io/badge/runs-idempotent%20%26%20reproducible-important)](#-determinism--idempotency)

</div>

> [!TIP]
> This README is meant to live **inside** `src/pipelines/<domain_or_product>/`.  
> Replace every `<domain_or_product>` placeholder with your real folder name (example: `hydrology`, `cultural_heritage`, `landcover`, `infrastructure`, `public_health`).

---

## 🧠 What this pipeline does

This pipeline ingests, validates, enriches, and publishes data for the **`<domain_or_product>`** domain so it can be:

- 🗺️ **Rendered interactively** (2D MapLibre / 3D Cesium)
- 🧬 **Queried semantically** (Neo4j knowledge graph)
- 🧱 **Queried spatially at scale** (PostGIS)
- 📚 **Discovered & trusted** (STAC + DCAT catalogs + PROV lineage)
- 🤖 **Used safely by AI** (Focus Mode / RAG with citations + governance checks)
- 🧵 **Turned into narrative outputs** (Story Nodes + optional Pulse Threads)

---

## 🧭 Pipeline contract (non‑negotiables)

KFM enforces a canonical ordering:

**Raw → Work (ETL) → Processed → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story/Focus**

✅ No stage can be skipped.  
✅ UI must never “reach around” governance (no direct graph/DB access from UI).  
✅ Everything published must be traceable back to sources (auditability over convenience).

```mermaid
flowchart LR; A[📥 Raw Sources] --> B[🛠️ Work - ETL]; B --> C[📦 Processed Data]; C --> D[🧾 Catalogs - STAC DCAT PROV]; D --> E[🧠 Knowledge Graph - Neo4j]; E --> F[🧩 API - FastAPI GraphQL]; F --> G[🗺️ UI - MapLibre Cesium]; G --> H[📖 Story Nodes + 🤖 Focus Mode];
```

---

## 🚀 Quickstart

### Prereqs (typical)
- 🐍 Python (recommend 3.11+)
- 🗄️ Postgres + PostGIS
- 🧠 Neo4j
- 🧰 GDAL (often needed for raster/vector conversions)
- 🧪 Node tooling **only if** you are touching Story Nodes/UI assets
- 🧲 Redis **optional** (recommended for idempotency keys in streaming/high-frequency pipelines)

### Env vars (example)
```bash
export POSTGIS_URL="postgresql://user:pass@localhost:5432/kfm"
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="password"
export KFM_ENV="local"
```

### Run (typical patterns)
> Adjust these to match your repo’s execution style (Typer CLI, Make, or task runner).

```bash
# From repo root
python -m src.pipelines.<domain_or_product>.cli run --config config/local.yaml

# Or: “single run” for one dataset
python -m src.pipelines.<domain_or_product>.cli run-dataset --dataset kfm.ks.<domain_or_product>.example.v1
```

---

## 🗂️ Directory layout

```text
src/pipelines/<domain_or_product>/
├─ ✅📄 README.md                 # 👈 you are here 📌 Pipeline purpose, inputs/outputs, run order, and how to execute locally/CI
├─ 🐍 __init__.py                 # Python package marker (exports/version info for this pipeline module)
├─ 🧩 cli.py                      # Typer/Click entrypoint (recommended): flags, subcommands, and safe defaults
├─ 🧠 pipeline.py                  # Orchestrates stages; wires steps; emits run manifest + telemetry + receipts
├─ ⚙️ config/                      # Environment configs (never store secrets; override via env vars)
│  ├─ 🧪 local.yaml                # Local defaults (paths, small sample mode, verbose logging)
│  ├─ 🧰 dev.yaml                  # Dev/staging settings (test endpoints, reduced cadence, feature flags)
│  └─ 🏭 prod.yaml                 # Production settings (schedules, strict policies, resource limits)
├─ 🧱 steps/                       # Ordered pipeline stages (keep deterministic; each step records receipts)
│  ├─ 👀 01_watch.py               # (optional) Watch/trigger step (stream/schedule triggers, change detection)
│  ├─ 🌐 02_fetch.py               # Acquire inputs (fetch receipts: headers, etags, byte counts, checksums)
│  ├─ ✅ 03_validate.py            # Validate inputs (schema checks, link checks, policy preflight)
│  ├─ 🧪 04_transform.py           # Transform/normalize (raw→work→processed; records params + hashes)
│  ├─ 📦 05_publish.py             # Publish artifacts (write outputs; optional OCI/ORAS push; produce digests)
│  ├─ 🛰️ 06_catalog.py             # Catalog writers (STAC/DCAT/PROV) + evidence triplet linking
│  └─ 🕸️ 07_graph.py               # Graph exports/loads (Neo4j CSV export, mapping, optional health checks)
├─ 🔌 adapters/                    # Integrations (IO boundaries; isolate external deps here)
│  ├─ 📥 inbound/                  # Inbound connectors (API clients, scrapers, sensors, file drops)
│  └─ 📤 outbound/                 # Outbound connectors (PostGIS, STAC, DCAT, PROV, OCI registry)
├─ 🧪 tests/                       # Pipeline tests (deterministic; fixtures tiny; no network by default)
│  ├─ 🧪 test_contracts.py          # Contract-level tests (input/output shapes, invariants, gate expectations)
│  ├─ 📐🧪 test_schema_validation.py # Schema validation tests (examples/fixtures validate cleanly)
│  └─ 🧩 fixtures/                 # Tiny fixtures used by tests (raw snippets + expected outputs)
└─ 📚 schemas/                      # Pipeline-specific schemas (beyond shared contracts)
   ├─ 📥📐🧾 input.schema.json       # Input contract for this pipeline (what it expects from sources/inbound)
   └─ 📤📐🧾 output.schema.json      # Output contract (what it produces for processed/catalog/graph layers)
```

> [!NOTE]
> Many pipelines reuse shared ingestion utilities. If you have a central ingestion framework, link it here:
> - `src/pipelines/ingestion/README.md` (example shared base)

---

## 🧱 Inputs & outputs (contract table)

| Category | Where it lives | Example | Must be immutable? |
|---|---|---|---|
| Raw inputs | `data/raw/<domain_or_product>/...` | source downloads, agency exports, scans | ✅ Yes |
| Work/ETL | `data/work/<domain_or_product>/...` | temporary transforms, staging | ⚠️ No (ephemeral) |
| Processed outputs | `data/processed/<domain_or_product>/...` | cleaned GeoParquet, COG, PMTiles | ✅ Yes (versioned) |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC Items/Collections, DCAT JSON, PROV JSON‑LD | ✅ Yes |
| Graph load | `data/graph/csv/` | nodes + relationships CSVs | ✅ Yes (per run) |
| API exposure | via KFM API | `/api/v1/query?table=...` | governed |
| UI layers | via API endpoints | MVT tiles, GeoJSON slices | governed |
| Narratives | `web/story_nodes/` or equivalent | story md + story json | versioned |

---

## ⚙️ Configuration

### Minimal config shape (recommended)
```yaml
pipeline:
  id: "kfm.ks.<domain_or_product>.pipeline"
  version: "v1"
  mode: "batch"   # batch | streaming
  schedule: null  # cron string if used by scheduler
paths:
  raw: "data/raw/<domain_or_product>"
  work: "data/work/<domain_or_product>"
  processed: "data/processed/<domain_or_product>"
  stac: "data/stac"
  dcat: "data/catalog/dcat"
  prov: "data/prov"
  graph_csv: "data/graph/csv/<domain_or_product>"
postgis:
  schema: "<domain_or_product>"
neo4j:
  enabled: true
observability:
  telemetry_ndjson: "data/audits/telemetry.ndjson"
policy:
  enforce: true
```

### Dataset metadata file (recommended)
Keep each dataset self-describing at the edge (raw stage):

```text
data/raw/<domain_or_product>/<dataset_id>/
├─ source.json          # provenance + licensing + sensitivity + checksums
└─ payload/...          # downloaded files (as-received)
```

Example `source.json` (template):
```json
{
  "dataset_id": "kfm.ks.<domain_or_product>.example.v1",
  "title": "Example Dataset",
  "description": "What this dataset represents and why it exists.",
  "source": {
    "publisher": "Agency / Archive / Collector",
    "access_url": "https://example.org/data",
    "retrieved_at": "2026-01-23T00:00:00Z",
    "license": "CC-BY-4.0"
  },
  "sensitivity": {
    "classification": "public",
    "notes": "If restricted, include rationale + handling rules."
  },
  "integrity": {
    "files": [
      { "path": "payload/file1.zip", "sha256": "<fill>" }
    ]
  },
  "spatiotemporal": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00],
    "time_start": "1930-01-01",
    "time_end": "1939-12-31"
  }
}
```

---

## 🧭 Stage-by-stage flow

> [!IMPORTANT]
> Every stage should be **idempotent** and emit **structured logs + a run manifest**.

### 01) 👀 Watch (optional)
Used for streaming or scheduled triggers:
- sensor feeds (USGS gauges, air quality, weather stations)
- file drops (SFTP, bucket notifications)
- webhooks
- periodic polling (cron)

**Outputs:**
- an immutable “event” envelope (timestamp, trigger type, scope)

### 02) 📥 Fetch
- download raw assets
- record checksums + HTTP headers
- write into `data/raw/<domain_or_product>/<dataset_id>/payload/...`

**Never:** overwrite prior raw files.

### 03) ✅ Validate
Validation is multi-layer:
- schema (tabular/raster/vector expectations)
- geometry validity (for vectors)
- CRS correctness / reprojection requirements
- temporal bounds sanity
- licensing + sensitivity completeness

> [!NOTE]
> Treat validation failures as “hard stops” unless an explicit waiver exists.

### 04) 🛠️ Transform (ETL)
Transform into KFM-standard deliverables, commonly:
- 🧊 **COG** for rasters (cloud-optimized)
- 🧱 **GeoParquet** for tabular + vector geometries
- 🧩 **PMTiles** for vector tile archives (offline / distribution)
- 🧰 derived indexes (spatial indexes, time partitions)

Write only to:
- `data/work/...` during intermediate transforms
- `data/processed/...` when final

### 05) 📤 Publish
Publish means:
- load or upsert into PostGIS tables (for spatial querying/tiling)
- generate tiles endpoints (MVT pattern) via API configuration
- generate any static artifacts for distribution (PMTiles, COG)

### 06) 🧾 Catalog (STAC/DCAT/PROV)
Generate the **evidence triplet**:

- **STAC**: Items/Collections for geospatial assets
- **DCAT**: dataset catalog entry + distributions (including API `accessURL`)
- **PROV**: lineage describing what produced what (inputs → activities → outputs)

### 07) 🧠 Graph (Neo4j)
Export graph-ready CSVs and/or load them:
- nodes: `Dataset`, `Place`, `Event`, `StoryNode`, `PulseThread`, `Concept`
- relationships: `COVERS_PLACE`, `ABOUT`, `DERIVED_FROM`, `MENTIONS`, etc.

---

## 🗺️ PostGIS + Neo4j integration

### Why both?
- **PostGIS**: heavy spatial lifting (bbox filters, spatial joins, area/distance, vector tile assembly)
- **Neo4j**: semantic context + relationships + provenance links (multi-hop reasoning)

### Operational rule of thumb
- **Counting, intersecting, tiling** → PostGIS  
- **Connecting, explaining, traversing** → Neo4j  
- **Orchestration and permissioning** → API layer

> [!IMPORTANT]
> The UI must not query PostGIS/Neo4j directly.  
> The API mediates access to apply governance, redaction, and consistent query patterns.

---

## 🧾 Catalogs (STAC/DCAT/PROV)

### STAC (geospatial discoverability)
Best practice for `<domain_or_product>`:
- one Collection per dataset family
- one Item per time slice / tile / region (as appropriate)
- assets include `href`, `type`, checksums, and roles (data/thumbnail/metadata)

### DCAT (catalog discoverability)
Your DCAT entry should include distributions like:
- downloadable artifacts (COG/GeoParquet/PMTiles)
- **API accessURL** for PostGIS-backed querying (example: `/api/v1/query?table=...`)

### PROV (lineage)
PROV should connect:
- raw artifacts (entities)
- transforms (activities)
- processed artifacts (entities)
- publishers (agents: pipeline, maintainer, CI)

---

## 🧬 Determinism & idempotency

### Run manifest (recommended)
Each run produces a manifest such as:

```json
{
  "run_id": "2026-01-23T00:00:00Z__kfm.ks.<domain_or_product>.pipeline__v1",
  "pipeline_id": "kfm.ks.<domain_or_product>.pipeline",
  "pipeline_version": "v1",
  "config_fingerprint": "<sha256-of-canonical-config>",
  "inputs": ["kfm.ks.<domain_or_product>.example.v1"],
  "outputs": [
    "data/processed/<domain_or_product>/example_v1/example.parquet",
    "data/stac/collections/kfm.ks.<domain_or_product>.example.v1.json"
  ],
  "started_at": "2026-01-23T00:00:00Z",
  "finished_at": "2026-01-23T00:02:12Z",
  "status": "success"
}
```

### Exactly-once pattern (streaming)
If polling every minute/hour:
- use a dedupe key like: `kfm:<dataset_id>:<time_bucket>`
- store it in Redis via `SETNX` (or equivalent)
- write outputs with deterministic naming
- upsert into PostGIS using stable primary keys

---

## 🔐 Governance & policy

KFM’s posture: **trust is engineered**, not assumed.

### Policy-as-code (OPA + Conftest)
Typical policy gates for pipelines:
- ✅ canonical stage order respected
- ✅ provenance exists before publish
- ✅ sensitivity/license metadata present
- ✅ secrets scanning passes (no keys in repo/artifacts)
- ✅ “output openness” is never broader than input rules
- ✅ API boundary respected (no UI direct graph access)
- ✅ energy/carbon tracking hooks (where applicable)

> [!NOTE]
> Policies should be runnable locally and in CI. The goal is fast feedback + consistent enforcement.

### FAIR + CARE principles
When in doubt:
- make it **findable and reusable** via catalogs + IDs (FAIR)
- respect **authority, benefit, ethics** for communities and sensitive content (CARE)

---

## 📦 Artifact packaging (optional, recommended for distribution)

For offline packs, replication, and supply-chain integrity:
- push **PMTiles / GeoParquet / COG** to an OCI registry (via ORAS)
- sign with **Cosign**
- attach **PROV JSON‑LD** and checksums as referrers/attestations

Example (conceptual):
```bash
oras push ghcr.io/<org>/kfm-data/<dataset_id>:2026-01-23 \
  dataset.pmtiles:application/vnd.pmtiles \
  dataset.parquet:application/vnd.geo+parquet \
  prov.jsonld:application/ld+json

cosign sign --keyless ghcr.io/<org>/kfm-data/<dataset_id>:2026-01-23
```

---

## 🤖 AI + Story integration

### Focus Mode (AI)
Focus Mode benefits when your pipeline emits:
- strong DCAT descriptions + themes
- clean graph links (place/time/topic)
- stable dataset IDs + citations (asset hrefs + checksums)
- optional embeddings for text-heavy assets (governed)

### Story Nodes (guided narratives)
Story Nodes are typically:
- `story.md` (narrative + citations)
- `story.json` (map camera steps, layers, timeline cues)

Your pipeline can optionally generate:
- story skeletons for newly ingested data
- “narrative templates” that point at the new STAC/DCAT identifiers

### Pulse Threads (optional content type)
A Pulse Thread is a **timely, geotagged micro‑story**:
- triggered by an anomaly watcher or curator
- always includes an evidence manifest (dataset IDs, query params, timestamps)

---

## ✅ QA checklist (Definition of Done)

Before merging changes to this pipeline:

- [ ] Raw inputs stored immutably with checksums
- [ ] Validation suite covers schema + CRS + geometry validity
- [ ] Processed outputs are deterministic (stable naming)
- [ ] STAC/DCAT/PROV emitted and cross-linked
- [ ] Graph CSV export matches schema expectations
- [ ] PostGIS tables load via upsert + keys
- [ ] Policy checks pass locally + in CI
- [ ] Telemetry includes run_id, dataset_id(s), output list, timings
- [ ] README updated if behavior changed 🙌

---

## 🧯 Troubleshooting

<details>
<summary><b>Common issues</b></summary>

- **CRS mismatch** → enforce reprojection rule in Validate step (fail fast).
- **Invalid geometries** → repair in Transform step (buffer(0)/makevalid) but record it in PROV.
- **Tile performance** → ensure spatial index + consider generalized geometry tables.
- **Graph bloat** → avoid per-feature nodes unless truly needed; aggregate at dataset/time/place levels.
- **Streaming duplicates** → implement idempotency keys + stable primary keys.

</details>

---

## 📚 Project references used to design this pipeline

These files informed the pipeline conventions, governance posture, UI/AI integration, and roadmap:

### Core KFM design docs
- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- 🧭 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**
- 🤖 **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf**
- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf**
- 📥 **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf**

### Roadmap & extensions
- 💡 **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf**
- 🌟 **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf**
- 🧠 **Additional Project Ideas.pdf** (Pulse Threads, Conceptual Attention Nodes, OCI artifacts, determinism patterns)

### Reference libraries (PDF portfolios / collections)
> Some reference bundles are PDF “portfolios” that open best in Adobe Reader.

- 🗺️ **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf**
- 🧠 **AI Concepts & more.pdf**
- 🧰 **Various programming langurages & resources 1.pdf**
- 🗄️ **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf**

---

## 🧾 Glossary (quick)

- **STAC** — SpatioTemporal Asset Catalog (geospatial assets + metadata)
- **DCAT** — Data Catalog Vocabulary (dataset discovery + distributions)
- **PROV** — W3C provenance model (lineage, activities, agents)
- **MVT** — Mapbox Vector Tiles (fast map rendering)
- **COG** — Cloud Optimized GeoTIFF (efficient raster access)
- **PMTiles** — Single-file tile archive (offline-friendly)
- **RAG** — Retrieval-Augmented Generation (LLM + structured/unstructured retrieval)
- **OPA** — Open Policy Agent (policy-as-code)

---

## 🤝 Ownership & contacts (fill in)

- **Pipeline owner:** `<name / handle>`
- **Domain SMEs:** `<names>`
- **On-call / escalation:** `<channel or procedure>`
