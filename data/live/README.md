# 📡 `data/live/` — Live & Streaming Data

<p align="center">
  <b>⏱️ near‑real‑time • 🧾 contract‑first • 🧬 provenance‑first • 🛡️ policy‑gated</b>
</p>

<p align="center">
  <img alt="purpose" src="https://img.shields.io/badge/purpose-live%20data%20window-blue" />
  <img alt="governance" src="https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-7fdbca" />
  <img alt="policy" src="https://img.shields.io/badge/policy-fail--closed-critical" />
  <img alt="metadata" src="https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-informational" />
</p>

> A **hot-window landing zone** for continuously updating feeds (sensor streams, polling APIs, near-real-time dashboards, rapid simulations).  
> Designed to power **live map layers**, **dashboards**, and **Pulse-style narrative updates** — *without breaking KFM’s evidence-first governance*.

> [!IMPORTANT]
> **Keep `data/live/` operational.** Commit **configs + schemas + tiny “golden samples”** only.  
> Store high-frequency payloads in a runtime volume/object store, and **promote** curated snapshots into `data/raw/` + `data/catalog/`.

🔗 Quick links: [`data/raw`](../raw) • [`data/processed`](../processed) • [`data/catalog`](../catalog) • [`docs`](../../docs)

---

## ✅ TL;DR rules (print this on your forehead 😄)

1. **Append-only**: Live facts are time-stamped events. Don’t rewrite history — publish new observations.
2. **Contract-first**: Every live source has a **data contract** (schema + metadata + license + sensitivity).
3. **Provenance-first**: Every ingest run writes **who/what/when/how** (checksums + manifests + run context).
4. **Fail closed**: If validation/policy fails → **quarantine + alert**, never “best-effort publish.”
5. **Sensitive by design**: Classification + redaction/generalization is part of the pipeline (not a UI patch).
6. **UI/AI never bypass**: Nothing appears in UI/Focus Mode without at least stub **STAC/DCAT/PROV**.

---

## 🎯 Why this folder exists

KFM needs two truths at once:

- **Live systems change fast** (minutes/seconds): sensors update, indicators shift, simulations rerun.
- **Knowledge systems must be auditable**: every map pixel and narrative sentence must trace back to evidence.

`data/live/` is the bridge: it holds the *hot window* + checkpoints that make real-time features possible, while staying compatible with downstream reproducible publishing.

Typical use cases 🧩

- 📡 Real-time sensor layers (e.g., gauges, weather stations, environmental monitors)
- 🔄 Incremental polling APIs (delta updates, “latest reading,” “since last seen”)
- 🧪 Rapid simulations / “nowcasts” feeding dashboards
- 🧠 Automated anomaly → **Pulse Thread** drafting (with evidence manifests)

---

## 🧭 Where `data/live/` sits in the KFM data lifecycle

```mermaid
flowchart LR
  EXT[External feeds<br/>(APIs • sensors • sims)] --> W[Watcher<br/>(observe + record)]
  W --> G[Ingestion Gate<br/>(basic validation + policy)]
  G -->|pass| LIVE[data/live<br/>(hot window + checkpoints)]
  G -->|fail| Q[Quarantine + Alert]

  LIVE --> X[Deterministic Transform<br/>(config-driven)]
  X --> DB[(PostGIS / time-series store)]
  X --> KG[(Knowledge Graph / Neo4j)]
  DB --> CAT[Catalog Updates<br/>(STAC/DCAT + PROV)]
  KG --> CAT

  CAT --> UI[UI live layers<br/>+ dashboards]
  CAT --> FM[Focus Mode<br/>(RAG + citations)]

  LIVE -->|scheduled snapshots| RAW[data/raw<br/>(immutable evidence)]
  X -->|stable derivatives| PROC[data/processed<br/>(standardized)]
```

**Mental model:** streaming data is “many small datasets over time.”  
We keep it windowed + fast in `data/live/`, and we publish durable, curated slices via normal KFM pathways.

---

## 📁 Directory layout (recommended)

> [!NOTE]
> This is a **recommended** structure. If your deployment uses object storage + DB only, keep the *shape* (contracts, telemetry, checkpoints) even if the payloads live elsewhere.

```text
data/live/
  README.md
  .gitignore                 # 👈 recommended: keep payloads out of git
  _schemas/                  # JSON Schema / Avro / Proto / validators
  _telemetry/                # append-only ingest logs (NDJSON)
  sources/
    <source_id>/
      README.md              # source-specific notes & SLA
      source.json            # contract: license + sensitivity + cadence + upstream
      checkpoints/           # cursors, offsets, watermarks (idempotency helpers)
      raw/                   # hot-window payloads (windowed, not forever)
      derived/               # quick-turn derivatives (UI-friendly, small)
      manifests/             # checksums + fetch manifests + evidence lists
      prov/                  # optional: run-level PROV bundles
      stac/                  # optional: rolling STAC Items/Collection stubs
```

---

## 🧱 Windowing, retention & naming (recommended)

Because live streams are high-frequency, `data/live/` should be **windowed** and **partitioned**.

### Suggested defaults

- **Hot window**: keep the most recent `P7D` (7 days) of raw payloads *(tune per source & storage)*
- **Derived window**: keep `P30D` (30 days) of lightweight derivatives (for UI trends & QA)
- **Promotion cadence**: snapshot hourly/daily into `data/raw/` for durable evidence
- **Never delete without a manifest**: deletions/rollups should be logged (telemetry + PROV)

### Naming conventions 🏷️

Prefer **time-partitioned, append-only** paths:

```text
raw/YYYY/MM/DD/HH/<source_id>__<observed_at>__<cursor_or_etag>.json
derived/YYYY/MM/DD/<source_id>__latest.geojson
manifests/YYYY/MM/DD/HH/run__<run_id>.manifest.json
```

Rules of thumb:

- Use **UTC ISO-8601** timestamps (`2026-01-24T06:15:00Z`)
- Include a **cursor/etag** (or hash) when available (idempotency + dedupe)
- Never rely on a single mutable `latest.json` *without also writing time-stamped history*

---

## 🧾 Live source contract (`source.json`)

Every live source MUST ship with a contract that answers:

- **What is it?** (`id`, `title`, `description`, `owner/contact`)
- **Can we use it?** (`license`, `attribution`, `terms`, `rate_limit`)
- **How often should it update?** (`cadence`, `sla_minutes`)
- **What’s the schema?** (`schema_ref`, `fields`, `units`, `CRS`)
- **How do we fetch it reproducibly?** (`upstream`, `auth_ref`, `idempotency`)
- **Is it sensitive?** (`sensitivity_class`, `geo_obfuscation`, `access_rules`)
- **How does it publish?** (`catalog_ids`, `output_assets`, `promotion_rules`)

Example (trim as needed):

```json
{
  "id": "river_gauges_live",
  "title": "River Gauge Readings (Live)",
  "description": "Near-real-time point observations for gauge stations.",
  "license": "TBD",
  "attribution": "TBD",
  "cadence_minutes": 15,
  "sla_minutes": 180,

  "sensitivity": {
    "class": "public",
    "geo_obfuscation": null,
    "access": "public"
  },

  "upstream": {
    "type": "api",
    "base_url": "https://example.org/api",
    "docs": "TBD",
    "auth": { "mode": "none", "secret_ref": null }
  },

  "idempotency": {
    "strategy": "etag_or_last_modified",
    "cursor_path": "checkpoints/cursor.json"
  },

  "schema": {
    "format": "json",
    "schema_ref": "../../_schemas/obs_point_v1.schema.json"
  },

  "catalog": {
    "dcat_dataset_id": "dcat:dataset:river_gauges_live",
    "stac_collection_id": "stac:collection:river_gauges_live"
  }
}
```

---

## ⚙️ Formats & performance (choose the smallest thing that works)

Live data wants **low-latency** *and* **repeatability**. Use formats that match the job:

- 🧾 **Telemetry / logs**: `*.ndjson` (append-only, streamable)
- 📍 **Point observations** (small/medium): `GeoJSON` (easy for UI)
- 🧱 **Large vectors**: vector tiles (`MVT`) packaged as `PMTiles` (fast map rendering)
- 🗃️ **Analytics snapshots**: `Parquet / GeoParquet` (columnar, compressible)
- 🛰️ **Rasters**: `COG` (Cloud-Optimized GeoTIFF) for efficient tile/overview reads
- 🌍 **3D / volumetrics**: `3D Tiles` (Cesium-friendly streaming)

> [!TIP]
> If a “live layer” is getting heavy, **don’t ship GeoJSON** — ship vector tiles and keep GeoJSON for debug/QA.

---

## 🔄 Ingestion loop (the happy path)

> [!NOTE]
> KFM ingestion commonly follows a **Watcher → Planner → Executor (W‑P‑E)** pattern:
> - **Watcher**: observes change / SLA breaches / anomalies and opens a run
> - **Planner**: builds an explicit run plan (what to fetch, validate, transform, publish)
> - **Executor**: executes deterministically, writing manifests + PROV + catalog updates

A live source typically follows this loop:

1. 🕵️ **Watcher** observes: “new data available” OR “SLA breach” OR “anomaly detected”
2. 📥 **Fetch** raw payload (prefer idempotent fetch using ETag/Last‑Modified/cursors)
3. 🛡️ **Ingestion gate** (lightweight but strict):
   - integrity (hashes/checksums)
   - schema sanity (parseable, required fields exist)
   - governance checks (license present, sensitivity known, size limits, etc.)
   - policy-as-code checks (OPA/Conftest style), **fail closed**
4. 🧾 Write **manifest + telemetry** (append-only)
5. 🔧 **Deterministic transform** to:
   - UI-friendly derivative (small GeoJSON, pre-joined attributes, etc.)
   - DB ingest (PostGIS/time-series store)
   - graph update (entities + PROV links)
6. 🗂️ Update **STAC/DCAT/PROV** (at least stubs) so UI/AI can cite & trace
7. 🧠 Optional: trigger **Pulse Thread** drafting when patterns/anomalies fire

---

## 📊 Telemetry & observability (don’t fly blind)

### Recommended telemetry: append-only NDJSON

Put ingest events in:

- `data/live/_telemetry/<source_id>.ndjson` (or per-run files)

Example event:

```json
{
  "ts": "2026-01-24T06:15:00Z",
  "source_id": "river_gauges_live",
  "event": "fetch_success",
  "bytes": 582134,
  "http": { "status": 200, "etag": "\"abc123\"" },
  "checksums": { "sha256": "..." },
  "cursor": { "since": "2026-01-24T06:00:00Z" },
  "policy": { "passed": true, "rules": ["license_present", "sensitivity_labeled"] }
}
```

### Health signals to compute ✅

- ⏱️ **Minutes since last seen** (per source) vs. expected SLA  
- 🧵 **Orphan detection** in the knowledge graph (STAC/PROV nodes missing required links)
- 🚦 **Gate failure rate** (spikes = upstream format changes or policy regressions)
- 🧠 **Anomaly triggers** (count + severity + review status)

---

## 🧠 Live data → UI & Focus Mode

### Live layers in the map 🗺️

A “Real-time” layer should behave like:

- UI requests **latest** reading per station/feature (plus small recent history on demand)
- API serves **GeoJSON** points/lines/polys (or vector tiles) with `value`, `observed_at`
- UI layer panel shows:
  - **Source attribution** (from DCAT/STAC metadata)
  - **Sensitivity warnings** (lock icon / generalized geometry / gated access)
  - **“Map behind the map”**: click through to evidence + provenance

### Focus Mode expectations 🤖

When users ask questions like:

- “What’s the current water level at X?”
- “Are any gauges trending unusually low in the last 7 days?”

Focus Mode should:

- detect it’s a **live query**
- retrieve relevant entities (graph) + latest readings (DB)
- return an answer with **citations** (dataset + station + timestamp)
- optionally surface an **Explainable AI** panel (retrieved context + why these sources)
- log a PROV record for the AI answer (derived entity) — so the answer is auditable

---

## 🧵 Pulse Threads (optional but 🔥)

Pulse Threads are **timely, geotagged narratives** tied to live patterns.

Pattern → narrative example:

- Watcher notices: “cluster of gauges in lowest 10th percentile”
- Planner prepares: evidence bundle + draft narrative
- Human curator reviews → publish

Minimum requirements for a Pulse Thread:

- short narrative (Markdown/JSON)
- geotags (region/place entities)
- **evidence manifest** (exact datasets/queries/timestamps backing the claims)
- versioning + provenance links

---

## 🔐 Governance, privacy, and ethics (FAIR + CARE)

Live data can be the riskiest data. Apply these defaults:

- **Sensitivity classification is mandatory** (public / restricted / confidential)
- **Geo-obfuscation** for protected locations when required (rounding/generalization)
- **Access control** for restricted layers (UI should hide or gate them)
- **No secrets in repo**: use secret refs and deployment secrets managers
- **Cultural protocols**: support “community rules” where contributors specify how data can be accessed/shared

> [!TIP]
> If you don’t know sensitivity, treat it as **restricted** until reviewed.

---

## 📦 Promotion & publishing (making live data durable)

### Snapshot promotion (recommended)

Because live streams are high-frequency, promote *curated slices* on a schedule:

- hourly/daily snapshots → `data/raw/<source_id>/<YYYY-MM-DD>/...`
- stable derivatives → `data/processed/`
- published metadata → `data/catalog/` (STAC/DCAT) + graph PROV

### Artifact distribution (optional, for big deliverables)

For large map artifacts (PMTiles, GeoParquet, COGs), consider content-addressed publishing:

- push artifacts to an **OCI registry** (ORAS)
- sign with **Cosign**
- (optional) attach **SLSA-style provenance attestations** for build/publish steps
- reference immutable digests from catalog metadata

This keeps artifacts reproducible, verifiable, and easy to “pull by digest.”

---

## 🧪 Add a new live source (checklist)

- [ ] Create `data/live/sources/<source_id>/source.json` (license + sensitivity included)
- [ ] Add/verify schema in `data/live/_schemas/`
- [ ] Implement fetch method (idempotent; cursors/ETag supported)
- [ ] Implement ingestion gate checks (parseable + hash + policy)
- [ ] Write telemetry (NDJSON) and manifests (checksums, evidence list)
- [ ] Map to STAC/DCAT/PROV IDs (even if stubs at first)
- [ ] Add UI layer config + attribution and sensitivity UX
- [ ] Add monitoring: “minutes since last seen” + failure alerts
- [ ] (Optional) Add Pulse Thread trigger + review workflow

---

## 🚫 Anti-patterns (please don’t 🙃)

- ❌ “Just drop it in PostGIS” (no catalog, no provenance, no sensitivity labels)
- ❌ Manually editing live payloads (breaks determinism + auditability)
- ❌ Storing API keys or credentials in `source.json`
- ❌ Publishing sensitive coordinates “temporarily”
- ❌ Overwriting “latest.json” without keeping time-stamped history

---

## 📚 Project reference docs (recommended reading)

> If you’re implementing or redesigning live ingestion, skim these first:

- 📚 **KFM Data Intake – Technical & Design Guide** (provenance-first ingestion patterns)
- 🧭 **KFM AI System Overview** (Focus Mode, citations, governance checks)
- 🗺️ **KFM Comprehensive UI System Overview** (live layers, dashboards, sensitivity UX)
- 🏗️ **KFM Architecture / Technical Documentation** (policy gates, contracts, trust model)
- 🚀 **Latest Ideas & Future Proposals** (W‑P‑E agents, FAIR/CARE automation, supply chain attestation)
- 💡 **Innovative Concepts** (4D digital twin thinking, cultural protocols, sensitivity-aware access)
- 🧵 **Additional Project Ideas** (Pulse Threads, graph health checks, OCI artifact distribution)
- 🧱 **Open‑Source Geospatial Mapping Hub Design** (MapLibre/Leaflet + time slider patterns)
- 📊 **Data Mining + Geospatial Cookbooks** (data cleansing + PostGIS/GeoJSON implementation recipes)
- 📦 **PDF Portfolios** (AI, data management, mapping/WebGL, programming resources) — open in Acrobat/Reader for embedded books

<details>
<summary>📦 Full project file bundle (PDFs & portfolios)</summary>

- 🧠 `AI Concepts & more.pdf` (PDF portfolio of AI/ML readings)
- 📊 `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` (PDF portfolio of data engineering / performance / architecture readings)
- 🧰 `Various programming langurages & resources 1.pdf` (PDF portfolio of language + tooling references)
- 🗺️ `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` (PDF portfolio of mapping/WebGL/virtual-world references)

- 📚 `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`
- 🧭 `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`
- 🏗️ `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`
- 🧾 `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- 🎛️ `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`
- 🌟 `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`
- 💡 `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`
- 🧵 `Additional Project Ideas.pdf`

- 🧱 `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`
- 🐍 `KFM- python-geospatial-analysis-cookbook-... .pdf` (implementation recipes)
- 🧼 `Data Mining Concepts & applictions.pdf` (data prep + ethics notes)
- 🧪 `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf` (reproducibility + coding standards)

</details>

