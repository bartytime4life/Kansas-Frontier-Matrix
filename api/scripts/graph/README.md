# 🕸️ `api/scripts/graph` — Graph Build, Load & QA (KFM)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-1f6feb)
![Graph](https://img.shields.io/badge/Graph-Knowledge%20Graph%20%2F%20Neo4j-00a3e0)
![Geospatial](https://img.shields.io/badge/Geo-PostGIS%20%2F%20STAC%20%2F%20DCAT-2ea44f)
![Ops](https://img.shields.io/badge/Ops-Idempotent%20Scripts%20%26%20Snapshots-orange)
![Status](https://img.shields.io/badge/Status-Contract%20%2B%20Runbook-purple)

> **Goal:** turn KFM catalogs + curated story evidence into a **queryable knowledge graph** (property graph) that powers search, linking, provenance, and UI exploration—**without duplicating** catalog metadata.

---

## 🧭 Quick Links

- [🎯 What this folder is for](#-what-this-folder-is-for)
- [🧩 Pipeline position](#-pipeline-position)
- [📦 Inputs & outputs](#-inputs--outputs)
- [🚀 Quickstart](#-quickstart)
- [🧰 Script catalog](#-script-catalog)
- [🧬 Graph model](#-graph-model)
- [✅ Quality gates](#-quality-gates)
- [⚡ Performance notes](#-performance-notes)
- [🔐 Security & governance](#-security--governance)
- [🗺️ UI & visualization hooks](#-ui--visualization-hooks)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 Project library used](#-project-library-used)

---

## 🎯 What this folder is for

This directory contains **operational scripts** (repeatable + safe) for the **Graph subsystem**:

- 🏗️ **Build** graph node/edge sets from STAC/DCAT/PROV catalogs + Story Nodes
- 📤 **Export** to Neo4j-friendly formats (CSV + Cypher)
- 📥 **Load** (bulk import or online ingestion)
- 🧪 **Validate** schema, constraints, and “evidence-first” provenance rules
- 📸 **Snapshot** reproducible graph states for APIs and UI

> **Philosophy:** the graph is an **index** and **linker**, not a second metadata store. Keep it lean, reference the catalogs, and attach provenance/evidence to anything that looks like a “claim.”

---

## 🧩 Pipeline position

The graph is intentionally **downstream** of your catalogs and upstream of API/UI layers.

```mermaid
flowchart LR
  A[ETL & Ingestion] --> B[STAC / DCAT / PROV Catalogs]
  B --> C[Neo4j Knowledge Graph]
  C --> D[API Layer]
  D --> E[UI / Map Explorer]
  E --> F[Story Nodes (curated)]
  F --> G[Focus Mode outputs (citation-first)]
```

**Why it matters:** if catalog metadata changes, the graph should remain consistent because it **references** canonical IDs rather than copying fields.

---

## 📦 Inputs & outputs

### Inputs (typical)
- 📚 **Catalogs**: STAC items/collections, DCAT dataset listings, PROV lineage
- 🧾 **Story Nodes**: curated narratives + citations (human/AI-assisted, but evidence-locked)
- 🗺️ **Geospatial sources**: PostGIS tables, GeoJSON, GPKG, tilesets, gazetteers
- 🛰️ **Remote sensing outputs** (optional): raster/vector summaries produced elsewhere

### Outputs (recommended conventions)
- 📁 `data/graph/csv/` → Neo4j bulk import CSVs (nodes + relationships)
- 📁 `data/graph/cypher/` → constraints + indexes + migrations
- 📁 `data/graph/snapshots/<run_id>/` → immutable build artifacts + manifests
- 📁 `data/graph/reports/<run_id>/` → QA metrics, coverage, and diffs

> ✅ **Tip:** treat every graph build as a “scientific run” with a `run_id`, manifest, and QA report.

---

## 🚀 Quickstart

### 1) Prereqs
- ✅ Neo4j (local Docker or hosted)
- ✅ Python/Node runtime (depending on implementation)
- ✅ Access to catalogs + PostGIS (if building geo-derived edges)

### 2) Environment variables
Create a `.env` (or equivalent secrets mechanism):

| Variable | Purpose |
|---|---|
| `NEO4J_URI` | Neo4j bolt/http endpoint |
| `NEO4J_USER` | username |
| `NEO4J_PASSWORD` | password |
| `KFM_CATALOG_ROOT` | path to STAC/DCAT/PROV catalogs |
| `KFM_GRAPH_OUT` | output dir (default `data/graph/`) |
| `POSTGRES_DSN` | Postgres/PostGIS connection string (optional) |
| `RUN_ID` | reproducible run label (recommended) |

### 3) Minimal run (conceptual)
```bash
# 0) Ensure catalogs exist and are current
# 1) Build export artifacts (CSV + Cypher)
python -m api.scripts.graph.build \
  --catalog "$KFM_CATALOG_ROOT" \
  --out "$KFM_GRAPH_OUT" \
  --run-id "${RUN_ID:-local}"

# 2) Apply schema constraints / indexes
python -m api.scripts.graph.migrate \
  --cypher "$KFM_GRAPH_OUT/cypher" \
  --run-id "${RUN_ID:-local}"

# 3) Load into Neo4j (bulk or online)
python -m api.scripts.graph.load \
  --csv "$KFM_GRAPH_OUT/csv" \
  --run-id "${RUN_ID:-local}"

# 4) Run QA gates
python -m api.scripts.graph.qa \
  --run-id "${RUN_ID:-local}"
```

> 🧠 If your repo uses different filenames, map these steps to the closest equivalents: **build → migrate → load → qa → snapshot**.

---

## 🧰 Script catalog

> This README defines a **contract**. If the exact scripts differ, keep the intent, flags, and outputs consistent.

### Recommended structure

```text
📁 api/scripts/graph/
  📄 README.md
  📄 build.(py|ts)              # catalog → nodes/edges exports
  📄 load.(py|ts|sh)            # CSV/Cypher → Neo4j
  📄 migrate.(py|ts)            # constraints/indexes/migrations
  📄 qa.(py|ts)                 # quality gates + reports
  📄 snapshot.(py|ts)           # pin run_id → immutable snapshot
  📁 cypher/
  │   ├─ 001_constraints.cypher
  │   ├─ 002_indexes.cypher
  │   └─ 100_migrations.cypher
  📁 schemas/
  │   ├─ ontology.yml
  │   └─ property_contract.json
  📁 queries/
  │   ├─ search.cypher
  │   ├─ provenance.cypher
  │   └─ coverage.cypher
```

### Script interface contract ✅
All scripts **should** support:

- `--run-id` (string, required in CI)
- `--dry-run` (no DB writes)
- `--log-json` (structured logs)
- `--fail-fast` (stop on first violation)
- `--out` (where outputs go)
- `--config` (optional config file)

---

## 🧬 Graph model

### Core idea: **IDs are canonical**
- Nodes that represent real catalog entities (datasets, maps, layers) use the **same ID** as STAC/DCAT.
- The graph stores **references**, plus:
  - derived metrics (e.g., degree, centrality)
  - thin searchable text
  - provenance pointers (what source supports this edge?)

### Baseline node labels (suggested)
| Label | Example | Notes |
|---|---|---|
| `Dataset` | STAC/DCAT dataset | **ID must match catalog** |
| `Map` | historical map sheet | points to STAC asset(s) |
| `Layer` | vector/raster layer | references tiles/COG |
| `Place` | county, town, river | ideally linked to gazetteer |
| `Person` | explorer, cartographer | should be evidence-backed |
| `Org` | agency, publisher | evidence-backed |
| `Event` | treaty, battle | time-bounded |
| `Document` | scanned doc, PDF | stored as pointer + hash |
| `StoryNode` | curated narrative | must cite sources |
| `Claim` | atomic statement | always has provenance |
| `Citation` | source pointer | ties claims to evidence |
| `Run` | build run metadata | reproducibility anchor |

### Relationship types (suggested)
| Type | From → To | Meaning |
|---|---|---|
| `HAS_ASSET` | Dataset → Layer/Map | catalog assets |
| `MENTIONS` | StoryNode/Document → Place/Person/Org/Event | entity linking |
| `ABOUT` | Document → Event/Place | thematic link |
| `DERIVED_FROM` | Layer → Dataset | lineage |
| `SUPPORTED_BY` | Claim/Edge → Citation | evidence requirement |
| `LOCATED_IN` | Place → Place | admin containment |
| `INTERSECTS` | Layer → Layer | spatial overlap edge |
| `NEAR` | Place → Place | proximity relationship |
| `IN_RUN` | Node/Edge → Run | build provenance |

> 🧷 **Rule of thumb:** if a relationship implies something a historian could dispute, it must be `SUPPORTED_BY` at the claim level.

---

## 🗺️ Geospatial edge generation (PostGIS-first)

Many KFM edges can be produced deterministically from geometry:

- `INTERSECTS`
- `WITHIN`
- `CONTAINS`
- `NEAR` (distance-threshold)
- `ROUTE_CONNECTS` (network topology)

**Pattern:** compute in PostGIS ➜ export IDs ➜ load into Neo4j as relationships.

### Example: proximity edges
- Use PostGIS to compute nearby features (`ST_DWithin`)
- Export `(src_id, dst_id, distance_m)` rows
- Load into Neo4j as `(:Place)-[:NEAR {meters:...}]->(:Place)`

### Example: routing edges (optional)
If you have a routable network, generate shortest paths or travel-time edges and store **summaries** (not full routes). Routes can be recomputed on demand.

---

## 📈 Analytics hooks (graph math without the drama)

This folder may include QA/analytics scripts for:

- 🧩 **Connected components** (detect accidental fragmentation)
- 📏 **Degree distributions** (spot bad joins)
- 🎛️ **Spectral checks** (graph Laplacian health signals)
- 🧭 **Centrality & hubs** (useful for UI suggestions)
- 🧠 **Uncertainty tagging** (Bayesian credibility for inferred edges)

> ✅ Keep analytics *derived* and reproducible—never let analytics overwrite canonical truth.

---

## ✅ Quality gates

Every graph build should emit a QA report and fail CI if any gate fails.

### Gate A — Referential integrity
- Every `Dataset/Map/Layer` node must map back to a real STAC/DCAT ID
- Orphans are errors unless explicitly whitelisted

### Gate B — No metadata duplication
- Graph must not drift from catalogs by copying large catalog fields
- Store only **IDs**, **pointers**, and **derived** attributes

### Gate C — Provenance required
- Any `Claim` or “interpretive” edge requires at least one citation
- Story Nodes must be citation-backed (focus-mode compatible)

### Gate D — Determinism
- Exports must be stable across runs given identical inputs
- Sort outputs; do not rely on hash/dict iteration order

### Gate E — Scientific rigor
- If you attach scores/weights, ship:
  - model version
  - training/eval summary
  - residual diagnostics / sanity plots (where applicable)

---

## ⚡ Performance notes

When graphs get big, performance is a feature:

- 🧱 Prefer bulk imports for initial loads
- 🧰 Create constraints/indexes early (especially on IDs)
- 🧵 Use chunked processing for exports and QA
- 🧠 Cache high-cost geospatial joins (store intermediate tables/views)

**Anti-patterns**
- Loading millions of edges row-by-row online
- Recomputing spatial joins every run without caching
- Storing huge blobs of metadata inside the graph

---

## 🔐 Security & governance

Graph pipelines touch “powerful” data surfaces (catalogs, DBs, entity linking). Keep these non-negotiable:

- ✅ Use parameterized queries (Postgres/Neo4j)
- ✅ Treat Story Nodes as **evidence-based** to prevent hallucinated claims entering the graph
- ✅ Redact secrets from manifests/logs
- ✅ Enforce least privilege for DB accounts (read catalogs, write graph, nothing else)
- ✅ Keep a clear audit trail per `run_id`

---

## 🖥️ UI & visualization hooks

The graph exists to serve exploration:

- 🗺️ **Map UI:** graph edges should support map-centric exploration (place → map → layer → story)
- 🧊 **3D/2D Graph Views:** export lightweight graph slices as JSON (nodes+edges) for WebGL renderers
- 📱 **Responsive UI:** keep payloads slim and paginated

### Recommended exports for UI
- `graph_slice.json` (bounded node/edge subset)
- `entity_card.json` (summary for Place/Person/Map)
- `provenance_chain.json` (why is this edge here?)

---

## 🧯 Troubleshooting

### “Graph loads but search is empty”
- Check constraints/indexes exist
- Confirm IDs match STAC/DCAT exactly (case, prefixes, namespaces)

### “QA fails: too many orphans”
- Catalog path mismatch
- Changed ID scheme without migrations
- Missing mapping layer between external IDs and KFM canonical IDs

### “Bulk import is slow”
- Split files by label/type
- Increase heap/page cache (Neo4j)
- Pre-sort CSVs and dedupe edges before import

---

## 📚 Project library used

This README is intentionally cross-disciplinary 🧩  
KFM’s graph work touches: **geospatial catalogs**, **graph theory**, **data engineering**, **UX**, **security**, and **ethics**.

<details>
<summary><strong>📦 Library touchpoints (how they inform Graph scripts)</strong></summary>

- 🛰️ Remote sensing → feature extraction + built-environment layers feeding the graph  
- 🗺️ Map design → graph outputs must support legible mapping & storytelling  
- 🕸️ Spectral graph theory → QA invariants + analytics hooks  
- 🧰 PostGIS/PostgreSQL → deterministic spatial joins that become graph edges  
- ⚡ Scalable data mgmt → chunked, parallel, cache-friendly builds  
- 🧪 Modeling & statistics → verification/validation, uncertainty tagging  
- 🔐 Security & humanism → privacy, integrity, safe-by-default scripts  
- 🌐 WebGL + responsive UI → graph slices tailored for frontend exploration  

</details>

---

## 🤝 Contributing

- Keep scripts **idempotent**
- Always emit a `manifest.json` per run
- Add a QA gate when you add a new edge type
- Prefer **derivation** over “manual truth” unless it’s a curated Story Node
- Write migrations when schema changes

---

## ✅ Checklist (before you ship)

- [ ] Node IDs match catalogs (STAC/DCAT)
- [ ] Constraints/indexes applied
- [ ] QA report generated and clean
- [ ] Snapshot saved with `run_id`
- [ ] Provenance is attached for any interpretive links
- [ ] Logs are safe (no secrets, no PII unless explicitly allowed)

---

_🕸️ Build graphs like a scientist, load them like an engineer, and present them like a cartographer._

