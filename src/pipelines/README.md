# 🧪 KFM Pipelines (`src/pipelines/`) — Evidence Engine ⚙️🗺️

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-6e40c9)
![Contract-First](https://img.shields.io/badge/contract--first-schemas%20%2B%20profiles-blueviolet)
![Evidence](https://img.shields.io/badge/evidence-STAC%20%2B%20DCAT%20%2B%20PROV-success)
![Determinism](https://img.shields.io/badge/determinism-idempotent%20%2B%20manifest--driven-2ea44f)
![Orchestration](https://img.shields.io/badge/orchestration-WPE%20(Watcher%E2%86%92Planner%E2%86%92Executor)-orange)
![Policy](https://img.shields.io/badge/policy-OPA%20%2F%20Conftest-blue)
![Storage](https://img.shields.io/badge/storage-PostGIS%20%2B%20Neo4j%20%2B%20Search-informational)
![Packaging](https://img.shields.io/badge/packaging-GeoParquet%20%2B%20PMTiles%20%2B%20COG-yellowgreen)
![UI](https://img.shields.io/badge/ui-React%20%2B%20MapLibre%20%2B%20Cesium-lightgrey)

> Pipelines are KFM’s **ingestion + ETL + enrichment + packaging + publishing** engine.  
> They turn messy sources into **versioned, queryable, map-ready evidence** — and keep every claim traceable back to its origin 🔎🧾  
>
> **Rule:** *Nothing enters KFM without metadata.* ✅

---

## 🚦 Quick navigation

- [✨ What belongs here](#-what-belongs-here)
- [🧭 Operating principles](#-operating-principles)
- [🗺️ End-to-end flow](#️-end-to-end-flow)
- [🧱 Core contracts](#-core-contracts)
  - [Evidence triplet](#1-evidence-triplet-stac--dcat--prov-)
  - [Data lifecycle + canonical layout](#2-data-lifecycle--canonical-layout-)
  - [RunContext + Run Manifest](#3-runcontext--run-manifest-)
  - [Receipts + checksums](#4-receipts--checksums-)
  - [Determinism + idempotency](#5-determinism--idempotency-)
  - [Clean Architecture boundaries](#6-clean-architecture-boundaries-)
  - [Packaging patterns](#7-packaging-patterns-)
  - [Graph + search ingestion](#8-graph--search-ingestion-)
  - [Artifact registry + signing](#9-artifact-registry--signing-)
- [📁 Repo touchpoints](#-repo-touchpoints)
- [▶️ Running pipelines](#️-running-pipelines)
- [🧰 Creating a new pipeline](#-creating-a-new-pipeline)
- [✅ Validation & policy gates](#-validation--policy-gates)
- [🧩 Pipeline types](#-pipeline-types)
- [📈 Ops: observability, backfills, drift](#-ops-observability-backfills-drift)
- [🔐 Security, privacy, ethics](#-security-privacy-ethics)
- [✅ Definition of Done](#-definition-of-done)
- [📚 References](#-references)
- [📖 Glossary](#-glossary)

---

## ✨ What belongs here

`src/pipelines/` is the home for KFM’s **evidence-producing jobs** — from raw intake to published artifacts and indexes.

### 🧱 Pipeline families

- **Ingestion pipelines** 📥  
  Fetch → verify → stage immutable raw drops → prepare standardized “work” intermediates → publish curated outputs.

- **Validation & contract enforcement** ✅  
  Schema checks, metadata completeness, CRS + bounds sanity, licensing/attribution, sensitivity tags, FAIR+CARE fields.

- **Enrichment pipelines** 🧠  
  OCR/NLP parsing, georeferencing, entity extraction, linking, ontology alignment (e.g., cultural heritage event/place modeling).

- **Packaging pipelines** 📦  
  Produce **map-ready** + **analysis-ready** artifacts together (e.g., **PMTiles + GeoParquet**, COGs, simplified GeoJSON, 3D-ready assets).

- **Graph + search pipelines** 🕸️🔎  
  Deterministically ingest catalogs + PROV into the knowledge graph; maintain constraints; update/search-index unstructured text.

- **Narrative pipelines** 🧵  
  Story Nodes & “Pulse” updates that are *still evidence-first* (narratives are versioned artifacts with provenance).

- **AI support pipelines** 🤖🧭  
  Build retrieval indexes, enforce citation requirements, store governance logs, run drift/bias checks, manage local model runtime hooks (e.g., Ollama).

> [!IMPORTANT]
> **Pipelines are contract-first.** If it can’t be validated, cataloged, and cited — it doesn’t ship. 🚫📦

---

## 🧭 Operating principles

### ✅ Contract-first
Schemas, profiles, and API contracts are first-class repo artifacts. Any change triggers versioning + compatibility checks.

### ✅ Evidence-first
Every published dataset or derived asset must have its **evidence triplet**: **STAC + DCAT + PROV**.

### ✅ Deterministic-by-default
Same inputs + same config + same code ➜ same outputs (same hashes). Pipelines are re-runnable and auditable.

### ✅ Governed by design
Governance is enforced with **policy-as-code** (OPA/Rego + Conftest) and explicit waiver workflows when needed.

### ✅ Clean Architecture separation
Pipeline logic stays testable and portable by depending on interfaces/contracts — not specific infrastructure details.

---

## 🗺️ End-to-end flow

```mermaid
flowchart LR
  S[📡 Sources<br/>(APIs, files, scans, sensors)] --> W[👀 Watcher<br/>detect change]
  W --> P[🧭 Planner<br/>decide runs + deltas]
  P --> X[⚙️ Executor<br/>run steps + open PRs if needed]

  X --> R[📥 Raw Intake<br/>immutable + receipts]
  R --> V[✅ Validate<br/>contracts + policy]
  V --> T[🧪 Transform<br/>standardize + normalize]
  T --> PUB[📤 Publish<br/>artifacts + checksums]

  PUB --> META[🧾 Metadata Publish<br/>STAC + DCAT + PROV]
  META --> G[🕸️ Graph Ingest<br/>Neo4j]
  PUB --> PG[🗄️ Load Spatial Store<br/>PostGIS]
  PUB --> SI[🔎 Search Index<br/>Elastic/alt]

  G --> API[🔌 Governed API<br/>GraphQL + REST]
  PG --> API
  SI --> API

  API --> UI[🗺️ UI Layer<br/>MapLibre + (opt) Cesium]
  API --> FM[🤖 Focus Mode<br/>retrieval + citations]
  PUB --> OFF[📦 Offline Packs<br/>PMTiles/MBTiles + bundles]
  OFF --> UI

  PUB --> REG[📦 Artifact Registry<br/>OCI/ORAS + signatures]
  META --> REG
```

**Mental model:** pipelines create *evidence artifacts* ➜ catalogs + provenance ➜ graph/spatial/search stores ➜ governed API ➜ UI + Focus Mode.

> [!NOTE]
> The UI is **read-only** relative to the pipeline layer: it cannot bypass the API or “write data” directly. Any new data, story, or model output enters through governed pipelines and version control.

---

## 🧱 Core contracts

### 1) Evidence triplet (STAC + DCAT + PROV) 🧾

Every “published” pipeline output should emit:

- **STAC** 🗂️ — spatial/temporal assets (items + collections): vectors, rasters, tiles, time series  
- **DCAT** 🏷️ — dataset discovery metadata: publisher, license, access links, keywords, distributions  
- **PROV** 🧬 — lineage bundle: inputs → activities (runs/steps) → outputs, with agents and parameters

> [!TIP]
> Treat STAC/DCAT/PROV as **boundary artifacts** between pipelines and downstream systems (graph, API, UI, Focus Mode).  
> They are the *interface*, not an afterthought.

✅ **FAIR + CARE**  
Metadata should carry FAIR *and* CARE considerations (e.g., sovereignty, ethics, authority-to-control) as explicit fields — not buried in prose.

---

### 2) Data lifecycle + canonical layout 🗃️

KFM follows a staged lifecycle:

| Stage | Folder | Rule | Typical contents |
|---|---|---|---|
| **Raw** | `data/raw/<domain>/` | Immutable | source drops, receipts, source manifests |
| **Work** | `data/work/<domain>/` | Replaceable | scratch intermediates, temp conversions |
| **Processed** | `data/processed/<domain>/` | Versioned | curated datasets, tiles, bundles |
| **STAC** | `data/stac/collections/` + `data/stac/items/` | Required at publish | STAC JSON artifacts |
| **DCAT** | `data/catalog/dcat/` | Required at publish | DCAT JSON-LD datasets |
| **PROV** | `data/prov/` | Required at publish | provenance bundles |
| **Audits** | `data/audits/<pipeline>/` | Required | run manifests, policy results, telemetry |

> [!IMPORTANT]
> A dataset is not “published” in KFM until it has **both** the data artifacts *and* the evidence triplet (STAC/DCAT/PROV).

---

### 3) RunContext + Run Manifest 🔁

**RunContext** is the in-memory “passport” (config + run metadata) that flows through steps.

**Run Manifest** is the persisted audit record:

- pipeline name + pipeline version (git SHA / release tag)
- run id + mode (incremental/full/backfill/streaming)
- inputs (URIs, receipts, checksums)
- transforms (parameters, CRS decisions, normalization rules)
- outputs (paths + checksums)
- metadata pointers (STAC/DCAT/PROV locations)
- policy decisions (pass/fail + waivers)
- telemetry pointers (NDJSON logs)

<details>
<summary><strong>📄 Example Run Manifest (illustrative)</strong></summary>

```yaml
pipeline: hydro_usgs_waterwatch
pipeline_version: "git:abcd1234"
run:
  run_id: "2026-01-23T18:01:22Z__hydro_usgs_waterwatch__sha256:9f3c..."
  started_at: "2026-01-23T18:01:22Z"
  mode: "incremental"   # full | incremental | backfill | streaming
inputs:
  - uri: "https://example.gov/usgs/waterwatch.csv"
    receipt:
      fetched_at: "2026-01-23T18:01:30Z"
      etag: "\"a1b2c3\""
      last_modified: "Tue, 21 Jan 2026 11:00:00 GMT"
    sha256: "..."
params:
  canonical_crs: "EPSG:4326"
  projected_crs_for_metrics: "EPSG:26914" # example: meters for buffering
  spatial_join: true
outputs:
  processed:
    - path: "data/processed/hydro/usgs_waterwatch/2026-01-23/waterwatch.parquet"
      sha256: "..."
  artifacts:
    - path: "data/processed/hydro/usgs_waterwatch/2026-01-23/checksums.sha256"
    - path: "data/audits/hydro_usgs_waterwatch/2026-01-23/run_manifest.yaml"
catalogs:
  stac_collection: "data/stac/collections/hydro_usgs_waterwatch.json"
  stac_items: "data/stac/items/hydro_usgs_waterwatch/2026-01-23/*.json"
  dcat: "data/catalog/dcat/hydro_usgs_waterwatch.dataset.jsonld"
  prov: "data/prov/hydro_usgs_waterwatch/run_2026-01-23.prov.json"
policy:
  status: "pass"
  waivers: []
telemetry:
  ndjson: "data/audits/hydro_usgs_waterwatch/2026-01-23/telemetry.ndjson"
```

</details>

---

### 4) Receipts + checksums ✅

**Fetch is receipt-based**:
- record URL, timestamp, status, headers (ETag/Last-Modified), and content hash
- support conditional fetch (`If-None-Match` / `If-Modified-Since`) when available

**Publish is checksum-based**:
- write `checksums.sha256` alongside outputs
- downstream steps must be able to verify integrity quickly

---

### 5) Determinism + idempotency 🎯

Pipelines must be safe to re-run:

- **Deterministic outputs**: same inputs + config + code ➜ same digests
- **Idempotent ingest**: avoid duplicates; use manifest digest as idempotency key
- **Canonicalization**: normalize structured outputs (e.g., JSON key order) before hashing

> [!NOTE]
> For geospatial metrics (buffers/distances), use a projected CRS (meters), then publish in the platform’s canonical CRS (commonly EPSG:4326).

---

### 6) Clean Architecture boundaries 🧩

Pipelines should follow the platform’s layering:

- **Domain logic**: schemas, rules, transformations (pure, testable)
- **Ports**: repository interfaces for files, PostGIS, graph, registry, etc.
- **Adapters**: implementations (GDAL, PostGIS client, Neo4j driver, registry client)
- **Infrastructure**: Docker/K8s, storage backends, external services

✅ Result: ingestion logic does **not** depend on specific infrastructure details — adapters can be swapped without rewriting the pipeline.

---

### 7) Packaging patterns 📦

KFM favors **paired outputs** that serve both analytics and UI performance:

- **Analysis-ready**: GeoParquet / Parquet / Arrow (fast filtering + joins)
- **Map-ready**: PMTiles / MBTiles / vector tiles (fast rendering)
- **Raster**: COG (Cloud-Optimized GeoTIFF) + pyramids/overviews
- **3D** (optional): 3D Tiles / glTF-friendly assets for Cesium-like viewers

**Canonical pattern (example):** one dataset publishes both **GeoParquet + PMTiles** under the same metadata and provenance.

> [!TIP]
> If you add a performance artifact (tiles, simplified geometry, cached joins), it must remain **reproducible**: same manifest → same tile archive hash.

---

### 8) Graph + search ingestion 🕸️🔎

KFM’s hybrid data strategy intentionally uses multiple stores:

- **PostGIS** 🗄️ — geospatial + tabular, efficient geometry queries, tile serving inputs
- **Neo4j** 🕸️ — semantic/context graph: people, places, events, datasets, stories, activities (PROV)
- **Search index** 🔎 — full-text and (optionally) semantic retrieval over OCR, narratives, documents

**Graph ingest conventions**
- DCAT datasets become Dataset nodes
- PROV Activities become Run/Activity nodes
- PROV relations become edges (e.g., `wasDerivedFrom`, `wasGeneratedBy`, `wasAssociatedWith`)
- Cultural heritage / historical domains may align to established ontologies (e.g., CIDOC-CRM classes for Event/Place patterns)

> [!IMPORTANT]
> “Graph ingest” is not optional glue — it is part of publishing. Catalog → graph mapping must be deterministic and validated.

---

### 9) Artifact registry + signing 🔏📦

KFM treats data like software packages:

- **OCI registry** patterns for data artifacts (via ORAS-style multi-file manifests)
- **DVC** pointers (or equivalent) to keep Git lean while preserving data version references
- **Cosign/Sigstore** signatures + attestations for official outputs (SLSA-aligned)

✅ Benefits:
- reproducibility (pull exact artifact versions)
- integrity (verify signatures)
- federation (reuse artifacts across regional Frontier Matrix instances)

---

## 📁 Repo touchpoints

Pipelines don’t live in isolation; they connect to contracts, policies, stores, API, and UI.

```text
📦 repo/
├─ 🧠 src/
│  ├─ 🧪 pipelines/                      # ← YOU ARE HERE
│  │  ├─ _kit/                           # shared pipeline kit (context, steps, io, hashing)
│  │  ├─ ingestion/                      # watchers/fetchers/receipts/telemetry
│  │  ├─ packaging/                      # tiling + bundling utilities
│  │  ├─ graph/                          # graph ingest + health checks
│  │  ├─ ai/                             # retrieval indexes + governance logs
│  │  └─ <domain>/                       # e.g., hydro/, climate/, history/, ecology/, treaties/ ...
│  └─ 🤖 reasoning/                      # Focus Mode agents + retrieval adapters (consumes pipeline outputs)
│
├─ 🗂️ data/
│  ├─ raw/                               # immutable source drops + receipts
│  ├─ work/                              # intermediate outputs (replaceable)
│  ├─ processed/                         # published artifacts (versioned)
│  ├─ stac/                              # STAC items/collections (canonical)
│  ├─ catalog/
│  │  └─ dcat/                           # DCAT JSON-LD datasets/distributions (canonical)
│  ├─ prov/                              # PROV bundles (canonical)
│  └─ audits/                            # manifests, telemetry, policy results
│
├─ 📜 schemas/                            # schema contracts (domain + STAC/DCAT/PROV profiles)
├─ 🔐 policies/                           # OPA/Rego + conftest rules (+ waivers)
├─ 🔌 api/                                # governed API (GraphQL + REST; redaction + auth)
├─ 🗺️ ui/                                 # React + TypeScript UI (MapLibre + optional Cesium)
└─ 📚 docs/
   ├─ standards/                          # KFM profiles + doc protocols
   ├─ templates/                          # universal doc + story node templates
   └─ data/<domain>/README.md             # domain runbooks + stewardship notes
```

---

## ▶️ Running pipelines

### 🧑‍💻 Local dev

Most pipelines should expose a thin CLI (commonly **Typer**):

```bash
# discover commands
python src/pipelines/<domain>/<pipeline>/cli.py --help

# run with a manifest/config
python src/pipelines/<domain>/<pipeline>/cli.py run --manifest data/raw/<domain>/<pipeline>/manifest.yaml

# validate only (no publish)
python src/pipelines/<domain>/<pipeline>/cli.py validate --manifest data/raw/<domain>/<pipeline>/manifest.yaml

# backfill a range (chunked + restartable)
python src/pipelines/<domain>/<pipeline>/cli.py backfill --start 1900-01-01 --end 1950-12-31

# dry-run (produce plan + manifests, skip publish)
python src/pipelines/<domain>/<pipeline>/cli.py run --manifest ... --dry-run
```

> [!TIP]
> Keep CLIs “thin”: CLI ➜ `RunContext` ➜ pure steps.  
> CI and WPE should call the *same* pipeline logic you run locally.

### 🐳 Containerized runs

For reproducibility and parity (GDAL versions, system deps), pipelines should run cleanly in containers.

**Target behavior:**
- `docker compose up` for local full-stack (stores + API + UI)
- `docker run ... pipeline-image:tag` for isolated pipeline runs

### 🤖 Orchestrated runs (WPE: Watcher → Planner → Executor)

In production, pipelines are triggered by **Watcher–Planner–Executor**:

- **Watcher** 👀 detects upstream changes, anomalies, schedules
- **Planner** 🧭 decides *what* to run (incremental/backfill/rebuild tiles/schema migrate)
- **Executor** ⚙️ runs steps in governed channels (containers/queues) and opens PRs when human review is required

✅ Therefore pipelines must support:
- incremental runs
- restartability (resume from manifest checkpoints)
- structured telemetry
- contract + policy enforcement

---

## 🧰 Creating a new pipeline

### 🍪 Scaffolding

Preferred: scaffold from the pipeline template/cookiecutter (especially for AI-assisted and governed pipelines).

> [!NOTE]
> Templates should include: contracts, run manifest, receipts/checksums, STAC/DCAT/PROV emission, tests, policy hooks.

### 🧱 Suggested folder skeleton

```text
src/pipelines/<domain>/<pipeline_name>/
├─ cli.py                      # Typer CLI entrypoint (thin)
├─ pipeline.py                  # orchestrates step order + RunContext
├─ config.py                    # typed config (pydantic/dataclass)
├─ contracts/
│  ├─ input_schema.json         # expected input shape (when applicable)
│  └─ output_schema.json        # output shape (plus metadata expectations)
├─ steps/
│  ├─ fetch.py                  # receipts + raw drop
│  ├─ validate.py               # contract validation + policy pre-check
│  ├─ transform.py              # normalization + enrichment
│  ├─ package.py                # tiles/bundles + performance artifacts
│  ├─ publish.py                # write processed outputs + checksums
│  ├─ catalog.py                # STAC/DCAT
│  ├─ prov.py                   # PROV bundle
│  └─ ingest.py                 # PostGIS/Neo4j/Search ingest (adapters)
├─ tests/
│  ├─ test_contracts.py
│  ├─ test_determinism.py        # golden hashes / snapshot checks
│  └─ test_smoke.py
└─ README.md                    # pipeline runbook (inputs/outputs/backfill/failures)
```

> [!IMPORTANT]
> **Canonical ordering:** Fetch → Validate → Transform → Package → Publish → Catalog → PROV → Ingest  
> (“Publish” = artifacts + checksums + versioning — not “push to UI directly”.)

### 🧠 Step design pattern

**Steps should be small, pure, and inspectable.**

```python
# pseudocode (illustrative)
def transform(ctx: RunContext) -> StepResult:
    raw = read_raw(ctx.raw_paths)
    clean = normalize(raw, rules=ctx.config.rules)
    outputs = write_work(clean, ctx.work_dir)

    return StepResult(
        outputs=outputs,
        metrics={"rows_in": len(raw), "rows_out": len(clean)},
        warnings=[],
    )
```

---

## ✅ Validation & policy gates

Pipelines enforce quality **before** anything becomes “official.”

### 📜 Contract validation

- schema validation (domain + STAC/DCAT/PROV profiles)
- required metadata: license, attribution, sensitivity tags, provenance pointers
- CRS correctness + bounds sanity (bbox, geometry validity, units)
- deterministic naming/versioning rules (no silent overwrites)

### 🔐 Policy validation (OPA/Conftest)

Common gate categories:

- **license & attribution** (compatible + complete)
- **sensitivity** (sacred sites, endangered species habitats, archaeological locations, etc.)
- **privacy** (PII, inference risk, aggregation requirements)
- **security** (secrets scanning, dependency policy, SBOM/attestations where required)
- **governance** (FAIR+CARE alignment; review requirements)

### 🤝 CI / automation

Pipelines should be CI-friendly:
- lint/type-check/test
- validate catalogs + provenance bundles
- run policy packs against artifacts produced in PRs
- ensure manifest + checksum rules

> [!NOTE]
> If automation (WPE) runs a pipeline and a policy requires review, the system should generate a **review-ready PR** or change record — never a silent merge.

---

## 🧩 Pipeline types

Below is a practical taxonomy (you can mix types; output rules still apply).

| Type | Best for | Typical outputs | Stores updated |
|---|---|---|---|
| 📥 Batch ingestion | periodic datasets | GeoParquet/COG + STAC/DCAT/PROV | PostGIS + Neo4j |
| 📡 Streaming ingestion | sensors/alerts | incremental partitions + rollups + telemetry | PostGIS + search |
| 🗺️📜 Historic docs/maps | scans, archives | COGs + OCR corpora + entity edges | Search + Neo4j |
| 🧱🌍 Asset builds | performance/offline | PMTiles/MBTiles + simplified geom + bundles | UI offline packs |
| 🕸️🩺 Graph maintenance | health checks | constraint reports + drift alerts | Neo4j |
| 🧵⚡ Narrative/Pulse | timely updates | Story markdown + storyboard JSON + evidence manifest | Neo4j + search |
| 🤖🧭 AI support | retrieval/governance | indexes + model/run records + policy logs | Search + audits |
| 🕰️🧪 Simulation/twins | scenario modeling | datasets + uncertainty + replay manifests | PostGIS + Neo4j |

---

## 📈 Ops: observability, backfills, drift

### 📊 Telemetry

Each run should emit machine-readable telemetry (often NDJSON):
- step timing
- row/feature counts
- anomaly counts
- cache hits/misses
- optional: resource usage

### 🔄 Backfills

Backfills must be:
- manifest-driven (range + parameters)
- chunked and restartable
- idempotent across repeated runs

### 📉 Drift monitoring

For AI and streaming pipelines:
- track data distribution shifts
- track model performance metrics and provenance
- open issues / generate review-ready PRs when thresholds are crossed

---

## 🔐 Security, privacy, ethics

### 🛡️ Sensitive locations & cultural data (CARE)

If data includes sensitive locations (archaeological sites, endangered species habitat, sacred sites, etc.):

- generalize/fuzz coordinates where required
- apply access control (public vs restricted)
- add sensitivity tags in metadata (machine-readable)
- document sovereignty expectations and restrictions

### 🕵️ Privacy-preserving outputs

When outputs could leak private information:

- consider **k-anonymity / l-diversity / t-closeness**
- apply query auditing for inference control
- use differential privacy for public aggregates when needed

### 🔏 Supply-chain integrity

For official releases:

- generate SBOMs (where applicable)
- sign artifacts (Sigstore/Cosign)
- attach attestations tying artifact → pipeline version → run manifest

### 🤖 Focus Mode safety hooks (AI pipelines)

AI support pipelines should assume a **governed execution** environment:

- **Prompt Gate**: validate/shape prompt + context
- **Tool allow-lists**: only approved tools/actions
- **Sandboxing**: isolate execution; protect secrets
- **OPA output policy check**: enforce content + data-handling rules
- **Citations ledger**: every answer ties to datasets/documents/graph nodes

> [!IMPORTANT]
> “No citation → no claim.” Focus Mode must prefer abstaining over hallucinating. ✅

---

## ✅ Definition of Done

A pipeline is “done” when:

- [ ] Purpose + scope are clear (what it ingests, transforms, publishes)
- [ ] Contracts exist (inputs/outputs + schema + sensitivity classification)
- [ ] Deterministic + idempotent (manifest + hashes + reproducible environment)
- [ ] Emits receipts, checksums, telemetry, and run manifest
- [ ] Produces STAC + DCAT + PROV (or documents why not)
- [ ] Updates stores deterministically (PostGIS/Neo4j/search) through adapters
- [ ] Passes policy gates (or includes approved waivers)
- [ ] Has tests (unit + contract + smoke + determinism checks)
- [ ] Documents backfill strategy + known failure modes
- [ ] Is runnable by humans locally and by WPE automation

---

## 📚 References

### 🧭 Canonical KFM docs (design + architecture)
- Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design
- 📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide
- Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide)
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖
- KFM AI Infrastructure – Ollama Integration Overview

### 📦 Resource portfolios (deep dives for pipeline authors)
- AI Concepts & more (agents, governance, ethics, constraints)
- Maps/GoogleMaps/Virtual Worlds/Archaeological GIS/WebGL (geospatial visualization + 3D)
- Data Management theories + architectures + Bayesian ideas (lakehouse/data quality/reproducibility thinking)
- Mapping/Modeling + Python/Git/HTTP/CSS/Docker/GraphQL + security (engineering toolchain)
- Geographic Information + R/SciPy/MATLAB/ArcGIS/Spark/TypeScript/Web Apps (analysis + app stack)
- Various programming languages & resources (polyglot reference)

### 🧩 Repo standards (recommended)
- KFM STAC/DCAT/PROV profiles (docs/standards/)
- Universal doc + Story Node templates (docs/templates/)
- Domain runbooks (docs/data/<domain>/README.md)

---

## 📖 Glossary

- **STAC** 🗂️: SpatioTemporal Asset Catalog (items/collections for geospatial assets)  
- **DCAT** 🏷️: Data Catalog Vocabulary (dataset discovery metadata; often JSON-LD)  
- **PROV** 🧬: W3C provenance model (inputs → activities → outputs, with agents)  
- **WPE** 🤖: Watcher → Planner → Executor automation loop (governed DevOps agents)  
- **OCI/ORAS** 📦: Container registry patterns for storing arbitrary artifacts (not just images)  
- **DVC** 🔁: Data Version Control (pointers + hashes for large artifacts)  
- **FAIR + CARE** 🤝: Findable/Accessible/Interoperable/Reusable + Collective Benefit/Authority to Control/Responsibility/Ethics  
- **PMTiles/MBTiles** 🧱: Offline-friendly tile archives (vector/raster packaging)  
- **COG** 🛰️: Cloud-Optimized GeoTIFF (efficient raster access)  
- **Idempotent** 🎯: safe to rerun without duplicating outputs or drifting results  
- **Run Manifest** 🧾: audit record of inputs/params/outputs/hashes/policy decisions

---