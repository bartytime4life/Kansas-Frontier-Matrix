# 📡 07 — Streaming Ingest Stub + PROV (src)

![Example](https://img.shields.io/badge/example-07_streaming__ingest__stub__prov-blue)
![MCP](https://img.shields.io/badge/MCP-dev__prov-8A2BE2)
![Standards](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-orange)
![Pattern](https://img.shields.io/badge/pattern-micro--batch%20%2B%20idempotent-success)
![Governance](https://img.shields.io/badge/governance-OPA%20%2B%20Conftest-important)

> [!IMPORTANT]
> This is a **stub / example provider**: it demonstrates *how* KFM expects streaming ingestion to behave (contracts ✅, provenance ✅, governance ✅), not a production-grade connector.

---

## 🧭 What this example is

This folder contains the **source implementation** for a streaming ingestion pattern that:
- polls or receives **real-time observations** (e.g., sensor readings, GTFS-RT vehicle positions),
- processes them in **micro-batches / windows**,
- writes to a storage adapter (stubbed or local),
- emits the KFM “evidence triplet” artifacts:
  - 🗂️ **STAC** (items/collections for geospatial/time indexing)
  - 🏷️ **DCAT** (dataset/attribution + catalog exposure)
  - 🧬 **PROV** (lineage + chain-of-custody)
- produces an auditable **Run Manifest** per ingestion window,
- stays **append-only** and **idempotent** (exactly-once semantics per logical batch).

If you’re building *any* “live layer” in KFM (rivers, transit, weather stations, traffic, simulations), this is the pattern to copy.

---

## 🧠 Mental model (KFM-style)

### Streaming data is “many small datasets over time”
KFM treats a stream as a rapid series of small ingests — each one must still be:
- validated,
- traceable,
- attributable,
- and safe to surface in the UI.

### Provenance is not optional (even for real-time)
Real-time layers must still have at least a **stub provenance record** before they’re used in graph/UI workflows.

---

## 📁 What’s in this folder

> [!NOTE]
> File names may vary slightly depending on the language/runtime used in your repo; the roles below are the “shape” this example intends.

```text
📦 src/
├─ 📄 README.md                      👈 you are here
├─ 🧠 main.(ts|py)                   entrypoint (CLI/dev runner)
├─ 🛰️ watcher.(ts|py)                poll/subscribe to a live feed (ETag/Last-Modified aware)
├─ 🪟 windowing.(ts|py)              micro-batch/window builder + checkpoints
├─ 🧪 validate.(ts|py)               schema + range checks (pre-policy)
├─ 🧰 policy_gate.(ts|py)            OPA/Conftest hooks (or local equivalent)
├─ 🧬 prov.(ts|py)                   PROV JSON-LD builder (Activity/Entity/Agent)
├─ 🗂️ stac.(ts|py)                   STAC Item/Collection builder
├─ 🏷️ dcat.(ts|py)                   DCAT Dataset + Catalog entries
├─ 🧾 run_manifest.(ts|py)           Run Manifest + canonical digest
├─ 🗃️ adapters/
│  ├─ 🧱 store_stub.(ts|py)          writes to local files (default)
│  └─ 🛰️ postgis.(ts|py)             (optional) PostGIS insert adapter
└─ ✅ __tests__/                      smoke tests: determinism + idempotency + schema
```

---

## 🚀 Quickstart

> [!TIP]
> This example is commonly run in two modes:
> 1) **mock stream** (replay NDJSON/JSON lines)
> 2) **poll a real endpoint** (HTTP, GTFS-RT, sensor API)

### 1) Mock stream replay (recommended)
```bash
# from the example root (one level above src/)
# (choose the package manager/runtime used by the repo)
npm install
npm run dev -- --source mock --in ./fixtures/observations.ndjson --out ./out
```

### 2) Poll a real endpoint
```bash
npm run dev -- \
  --source http \
  --url "https://example.gov/api/live" \
  --poll-interval-ms 60000 \
  --window-seconds 60 \
  --out ./out
```

---

## ⚙️ Configuration

| Variable / Flag | Example | Why it matters |
|---|---:|---|
| `--poll-interval-ms` | `60000` | how often the watcher polls (avoid overloading sources) |
| `--window-seconds` | `60` | window size for micro-batch processing |
| `--state-file` | `./state.json` | checkpoint for last-seen ETag/timestamp/sequence |
| `--out` | `./out` | where artifacts are written (stub store) |
| `--dataset-id` | `usgs_nwis_river_gauges` | stable dataset identity for DCAT/STAC grouping |
| `--sensitivity` | `public` / `restricted` | drives policy gate + API/UI access behaviors |

> [!WARNING]
> **Do not** use “now()” or random IDs in artifact identifiers.  
> Determinism + idempotency are the whole point of this example.

---

## 🏗️ Architecture (end-to-end)

```mermaid
flowchart LR
  A[🌐 Live Source<br/>(API / GTFS-RT / Sensor)] --> B[🛰️ Watcher<br/>(ETag / Last-Modified / since=...)]
  B --> C[🪟 Window Buffer<br/>(micro-batch)]
  C --> D[🧪 Validate<br/>(schema + range)]
  D --> E[🧾 Run Manifest<br/>(canonical digest)]
  E --> F[🧬 PROV JSON-LD<br/>(Activity/Entity/Agent)]
  D --> G[🗃️ Store Adapter<br/>(stub / PostGIS)]
  G --> H[🗂️ STAC Items]
  G --> I[🏷️ DCAT Dataset]
  H --> J[🧠 Graph Update (optional)]
  I --> J
  J --> K[🗺️ UI / API<br/>Real-time Layer + Focus Mode]
  F --> J
```

---

## 🧾 Outputs (what gets emitted)

Each ingestion **window** should produce a small, reviewable “bundle”:

```text
📦 out/
└─ 🧾 audits/
   └─ <run_id>/
      ├─ run_manifest.json          ✅ what/when/inputs/outputs + canonical digest
      ├─ prov.jsonld                ✅ lineage bundle (W3C PROV)
      ├─ stac_item_<...>.json        ✅ one-per-observation or one-per-snapshot
      ├─ stac_collection.json        ✅ optional grouping
      ├─ dcat_dataset.json           ✅ dataset attribution + access + license
      └─ metrics.json               ✅ optional telemetry summary
```

> [!NOTE]
> The *UI* and *Focus Mode* should never have to “guess” source attribution.  
> **DCAT** is where “Source: ___” and licensing comes from.

---

## 🧬 Provenance contract (PROV mapping)

This example keeps provenance simple and consistent.

### Entities (prov:Entity)
- **Input entity**: raw payload retrieved from the live source (or decoded protobuf)
- **Observation entity**: normalized observation record (lat/lon/time/value)
- **Output entity**: inserted row(s) / artifact(s) written for the window

### Activity (prov:Activity)
- `fetch_live_data`
- `decode_and_normalize`
- `validate_window`
- `append_to_store`
- `publish_catalog_artifacts`

### Agent (prov:Agent)
- `watcher_bot` (the automated daemon)
- `pipeline_runtime` (runner identity)
- optional: `ci_bot` / `github_actions` if run via CI

> [!TIP]
> If you later integrate “PR → PROV Graph” dev provenance, you can link:
> - the **run activity** to the **PR activity**, and
> - the **output entities** to the **merge commit entity**.

---

## 🔁 Idempotency + determinism (non-negotiable)

### Idempotency key
Each logical window should have a stable key. Typical recipe:
- stable dataset id
- window start/end timestamps
- source cursor (ETag / Last-Modified / sequence number)
- canonical digest of the run manifest (recommended)

### Deterministic manifest digest
The manifest should be canonicalized (e.g., RFC 8785) before hashing so reruns produce the same digest.

✅ Good outcomes:
- retries don’t duplicate rows
- concurrent triggers don’t overlap
- PR diffs stay clean (reviewable)

---

## 🛡️ Policy gates (OPA/Conftest-friendly)

Even in “real-time,” KFM governance applies.

Recommended checks (keep them cheap and fast):
- ✅ DCAT must include a license + publisher/source attribution
- ✅ STAC items must include geometry + datetime + stable id
- ✅ PROV must connect the Activity to both inputs and outputs (no orphaned lineage)
- ✅ Sensitivity classification present and respected
- ✅ Range checks (e.g., water level not negative; lat/lon valid)
- ✅ Schema validation for the emitted JSON artifacts

> [!IMPORTANT]
> Treat policy gates like tests: failing gates should block promotion to “live.”

---

## 🗺️ UI + API integration (how this becomes a “live layer”)

A “real-time” map layer usually works like this:
- API serves “latest points” or “points since timestamp”
- PostGIS makes the query fast with spatial + time indexes
- UI labels the layer with **source attribution** from DCAT

Optional enhancements:
- push updates via WebSockets instead of polling
- show a “minutes since last seen” health indicator per feed

---

## 🤖 Focus Mode integration (why PROV matters beyond ingest)

When Focus Mode answers a real-time question, it will:
1. find the relevant station/entity in the graph,
2. fetch the latest reading (dynamic query),
3. answer with **citations**,
4. still log a PROV record tying the answer to the specific reading used.

This is how KFM stays “living” *and* auditable.

---

## 🧠 Extension ideas (turn this stub into a powerhouse)

<details>
  <summary><b>📌 Add anomaly detection → Pulse Threads</b></summary>

- attach a lightweight detector to the window output
- when thresholds trigger, generate a draft Pulse Thread:
  - include an **Evidence Manifest**
  - include PROV tying the narrative to the exact windows/observations
- route to human review before publishing
</details>

<details>
  <summary><b>📦 Push artifacts to an OCI registry + sign them</b></summary>

- store STAC/DCAT/PROV + binary artifacts in OCI (ORAS)
- attach PROV JSON-LD as a referrer
- sign with Cosign for chain-of-custody
</details>

<details>
  <summary><b>🛰️ Swap the stub store for PostGIS + Neo4j</b></summary>

- write observations into PostGIS (append-only)
- upsert feed/station nodes into Neo4j
- link artifacts to datasets/places for discovery
</details>

---

## ✅ MCP “Definition of Done” checklist (for extending this example)

- [ ] New source has a **contract** (schema + required metadata)
- [ ] Watcher uses **ETag/Last-Modified/since** to avoid refetching
- [ ] Windowing is deterministic (stable boundaries)
- [ ] Idempotency key prevents duplicates (retry-safe)
- [ ] Run Manifest created + hashed (canonical digest)
- [ ] PROV JSON-LD links inputs → activity → outputs
- [ ] STAC + DCAT emitted (no mystery layers)
- [ ] Policy gate passes locally + in CI
- [ ] Basic telemetry exists (counts, errors, latency)
- [ ] Tests cover “rerun produces identical outputs”

---

## 🧯 Troubleshooting

- **Duplicate rows**  
  → your idempotency key is unstable (often due to timestamps or unordered JSON)

- **Artifacts differ across reruns**  
  → remove randomness/time-based IDs; canonicalize JSON before hashing

- **UI shows a layer but no source attribution**  
  → DCAT dataset is missing or not linked to the layer config

- **Graph has “orphan” PROV nodes**  
  → your PROV bundle is missing `used` or `wasGeneratedBy` edges

---

## 📚 Glossary (quick)

- **Watcher** 🛰️: persistent poller/daemon that collects new observations  
- **Window / Micro-batch** 🪟: a small time slice processed as one unit  
- **Run Manifest** 🧾: auditable record of a pipeline run (inputs/outputs/versions)  
- **Idempotent ingest** 🔁: processing the same logical batch twice does not duplicate it  
- **Evidence triplet** 🧬🗂️🏷️: PROV + STAC + DCAT working together  

---

### 🧡 Motto

> “Real-time is fine. **Mystery layers are not.**”
