# 🕸️ KFM Graph Subsystem (Neo4j) — `src/graph`

![Neo4j](https://img.shields.io/badge/Neo4j-knowledge%20graph-008CC1?logo=neo4j&logoColor=white)
![PostGIS](https://img.shields.io/badge/PostGIS-spatial%20DB-4169E1?logo=postgresql&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Search-Elasticsearch-005571?logo=elasticsearch&logoColor=white)
![STAC](https://img.shields.io/badge/STAC-catalogs-informational)
![DCAT](https://img.shields.io/badge/DCAT-metadata-informational)
![PROV](https://img.shields.io/badge/PROV-lineage-informational)
![GraphQL](https://img.shields.io/badge/GraphQL-semantic%20traversals-E10098?logo=graphql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-governed%20API-009688?logo=fastapi&logoColor=white)
![OPA](https://img.shields.io/badge/OPA-policy%20gates-7D3C98?logo=openpolicyagent&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-local%20stack-2496ED?logo=docker&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-local%20LLM%20RAG-000000)

> **What this folder is:** the **semantic backbone** of Kansas Frontier Matrix (KFM).  
> It builds and maintains the **Neo4j knowledge graph** that connects **datasets ↔ places ↔ events ↔ people ↔ organizations ↔ documents ↔ story nodes**, powers **Focus Mode** multi-hop reasoning, and upholds **provenance-first** guarantees. 🧭🤖

---

## ✅ Non‑Negotiables (KFM Invariants)

These are the “won’t regress” rules this subsystem must enforce:

- 🔌 **UI never talks to Neo4j directly** (no browser Cypher).  
  ✅ All graph access is **via the API layer** (REST/GraphQL) so governance can be enforced.
- 🧾 **No Mystery Nodes:** every node/edge must trace to **STAC/DCAT/PROV** artifacts *or* curated Story content with citations.
- 🧬 **Graph is a derived store** (rebuildable from export contracts), **except** explicitly curated “content” nodes (e.g., Story Nodes / editorial notes) which must still be versioned + provenance-linked.
- 🛡️ **Safe‑by‑default:** sensitivity & classification tags must be queryable and enforceable at the API layer (redaction/generalization).
- 🧠 **Focus Mode** requires citations: **“No Source, No Answer.”** If retrieval fails, answers must fail safely (no guessing).

---

## 🧠 Why a Graph?

KFM uses a **hybrid storage trio** (and a vector extension) because no single datastore is “best” at everything:

- 🗺️ **PostGIS** → heavy geospatial compute (bbox filters, joins, tiling, geometry ops).
- 🕸️ **Neo4j** → semantic relationships, provenance chains, narrative linking, multi-hop exploration.
- 🔎 **Search Index (e.g., Elasticsearch)** → full-text search over documents, story text, OCR corpora.
- 🧲 **Vector store (optional)** → embedding-based retrieval for semantic similarity (RAG).

The graph exists so KFM can answer questions like:

- “What datasets are related to **Event X** in **Place Y**?”
- “What happened **here** during **the 1930s**?”
- “Show **Story Nodes** that reference these layers and this county.”
- “Why did Focus Mode cite **these** sources?” (explainable traversals)

---

## 🔗 Quick Links (Repo)

> Paths shown here are **canonical intents**; exact filenames may vary by repo version.

- `../../data/graph/csv/README.md` 📄 — import-ready CSV contracts
- `../../docs/MASTER_GUIDE_v13.md` 🧱 — pipeline ordering + invariants (v13+)
- `../../docs/architecture/` 🏛️ — system architecture blueprints
- `../../docs/governance/` ⚖️ — ethics / sovereignty / policy triggers
- `../../api/` 🔌 — governed REST/GraphQL gateway (Cypher/SQL lives here)

---

## 🧭 What `src/graph` Owns

✅ This module owns:

- 🧬 **Ontology bindings & mapping rules** (CIDOC‑CRM / PROV‑O / OWL‑Time / GeoSPARQL alignment)
- 🧱 **Graph schema contract** (labels, rel types, required properties, invariants)
- 🧰 **Ingest tooling** (CSV bulk load + deterministic rebuilds; incremental sync if supported)
- 🧷 **Constraints & indexes** (uniqueness, required fields, full-text indexes)
- 🩺 **Graph Health Checks** (integrity, drift detection, orphan detection, cross-store checks)
- 🔎 **Curated query templates** used by API + Focus Mode (no “free-form Cypher” for UI)

🚫 This module does **not** own:

- Heavy geometry calculations → **PostGIS**
- UI state / Story playback controls → **web client**
- Raw data fetching / scraping → **pipeline intake**
- Authorization decisions → **API policy pack** (OPA or internal policy engine)

---

## 📦 Folder Map (Recommended Layout)

> Treat `src/graph` like a mini product: **schema → ingest → constraints → health → queries → governance hooks**.

```text
📁 src/graph/
├─ 📄 README.md                         # you are here
├─ 📁 ontology/                         # 🧬 ontology bindings (CIDOC / PROV / OWL-Time / GeoSPARQL…)
│  ├─ 📄 cidoc_crm.(yaml|json|ttl)
│  ├─ 📄 prov_o.(yaml|json|ttl)
│  ├─ 📄 owl_time.(yaml|json|ttl)
│  ├─ 📄 geosparql.(yaml|json|ttl)
│  └─ 📄 mapping_rules.md               # “how KFM maps standards → labels/props”
├─ 📁 schema/                           # 🧱 labels + rels + required keys + schema versioning
│  ├─ 📄 labels.md
│  ├─ 📄 relationships.md
│  ├─ 📄 property_keys.md
│  └─ 📄 schema_versioning.md
├─ 📁 constraints/                      # 🧷 Neo4j constraints + indexes (Cypher migrations)
│  ├─ 📄 001_constraints.cypher
│  ├─ 📄 002_indexes.cypher
│  └─ 📄 003_fulltext_indexes.cypher
├─ 📁 ingest/                           # 🧰 CSV → Neo4j (bulk import / upsert strategies)
│  ├─ 📄 ingest_csv.(py|ts)
│  ├─ 📄 id_strategy.md
│  ├─ 📄 upsert_strategies.md
│  └─ 📄 import_manifest.md             # contract for build_id/git_sha/timestamps
├─ 📁 queries/                          # 🔎 curated Cypher templates (used by API only)
│  ├─ 📄 search_entities.cypher
│  ├─ 📄 expand_neighbors.cypher
│  ├─ 📄 provenance_chain.cypher
│  ├─ 📄 storynode_context.cypher
│  └─ 📄 governance_filtered_view.cypher
├─ 📁 health/                           # 🩺 integrity + drift detection + smoke checks
│  ├─ 📄 graph_health_check.(py|ts)
│  ├─ 📄 drift_checks.cypher
│  ├─ 📄 referential_checks.cypher       # PostGIS/catalog ID sanity checks
│  └─ 📄 health_report_schema.json
└─ 📁 tests/                            # 🧪 contract + integration tests (Neo4j container)
   ├─ 📄 test_csv_contracts.py
   ├─ 📄 test_ingest_smoke.py
   ├─ 📄 test_health_checks.py
   └─ 📁 fixtures/
```

---

## 🔁 Data Flow & Ordering Invariants (KFM-wide)

KFM’s pipeline ordering exists to enforce **reproducibility** and **chain-of-custody**:

1. 🧱 `data/raw/` — source data (immutable inputs)
2. 🧪 `data/processed/` — derived products (versioned artifacts)
3. 🗂️ `data/stac/`, `data/catalogs/`, `data/prov/` — STAC/DCAT/PROV metadata
4. 🕸️ `data/graph/csv/` — graph import exports (derived semantic layer)
5. 🧠 (optional) `data/embeddings/` — vector index inputs (also provenance-tracked)

### Mermaid: end-to-end flow

```mermaid
flowchart LR
  raw[🧱 data/raw] --> processed[🧪 data/processed]
  processed --> catalogs[🗂️ STAC/DCAT/PROV]
  catalogs --> csv[📄 data/graph/csv]
  csv --> neo4j[(🕸️ Neo4j)]
  processed --> postgis[(🗺️ PostGIS)]
  catalogs --> search[(🔎 Search Index)]
  processed --> search
  search --> ai[🧠 Focus Mode AI]
  neo4j --> api[🔌 API (FastAPI + GraphQL)]
  postgis --> api
  ai --> api
  api --> ui[🖥️ Web UI]
  api --> notebooks[📓 Notebooks / External Clients]
```

---

## 🚀 Quickstart (Local Dev)

> Commands are **examples**. Adjust to the repo’s actual CLI/module names.

### 1) Start Neo4j (Docker-first)

```bash
docker compose up -d neo4j
```

**Common dev URLs**
- Neo4j Browser: `http://localhost:7474`
- Bolt: `bolt://localhost:7687`

### 2) Configure environment variables

```bash
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="password"
# export NEO4J_DATABASE="neo4j"   # optional (Neo4j multi-db)
```

### 3) Generate graph CSV exports

The authoritative import contract is: `data/graph/csv/`

```bash
# Example (pipeline step):
python -m src.pipelines.build_graph_csv --out data/graph/csv
```

### 4) Apply constraints + indexes (migrations)

```bash
python -m src.graph.constraints.apply
```

### 5) Ingest into Neo4j

```bash
python -m src.graph.ingest.ingest_csv --csv-dir data/graph/csv
```

### 6) Run health checks (required)

```bash
python -m src.graph.health.graph_health_check --format markdown
```

✅ **Rebuild-friendly:** Neo4j is a **derived store**.  
If you hit a bad state, it’s usually correct to **drop + reimport** (as long as CSV exports are correct).

---

## 🧬 Modeling Rules (Schema Contract)

KFM’s graph is **ontology-aware** and built to serve **explainable retrieval**.

### 🏷️ Canonical labels (examples)

- `Dataset` — ties to DCAT + STAC IDs (do not store payloads)
- `StacCollection`, `StacItem`, `Asset` — catalog structure
- `Place` — gazetteer-backed locations (counties, towns, rivers…)
- `Event` — historical events, observations, incidents
- `Person`, `Organization` — people/institutions
- `Document` — text sources (newspapers, reports, treaties; often indexed in search)
- `StoryNode` — narrative objects referencing datasets + places + docs
- `Concept` — topics/themes for browsing + clustering
- `Activity`, `Agent`, `Entity` — provenance (PROV-style backbone)
- `AIAnswer` (optional) — stored responses with explicit provenance + citations

### 🔗 Relationship naming

Use **UPPER_SNAKE_CASE**:

- Spatial-ish: `LOCATED_IN`, `CONTAINS`, `HAPPENED_AT`
- Text-ish: `MENTIONS`, `CITES`, `DESCRIBES`
- Data-ish: `REFERENCES_DATASET`, `HAS_ITEM`, `HAS_ASSET`
- Provenance-ish: `USED`, `WAS_GENERATED_BY`, `WAS_DERIVED_FROM`, `WAS_ASSOCIATED_WITH`
- Governance-ish: `HAS_POLICY_TAG`, `REDACTS_TO` (optional)

### 🆔 Identity, Keys & Versioning (required)

Every “real” node should have:

- `id` — stable unique ID (prefer **ULID** or deterministic composite keys)
- `kind` or `type` — stable category if label multiplexing exists
- `source_id` — the canonical external reference (STAC Item ID, DCAT identifier, DOI, archive ID…)
- `prov_id` — pointer to PROV record (or prov bundle ID)
- `created_at`, `updated_at` (or equivalent)
- `valid_time_start`, `valid_time_end` when temporal validity matters
- `classification` / `sensitivity` — required where governance applies (e.g., protected sites)

> 🧠 Tip: store **references**, not bulky artifacts. Neo4j should not hold rasters, full PDFs, or large geometries.

---

## 🧬 Ontology Alignment (How We Stay “Meaningful”)

KFM aligns the graph with established standards:

- 🏺 **CIDOC‑CRM** for cultural heritage entities (events, actors, places, documents)
- ⛓ **PROV‑O** for lineage chains (entities, activities, agents)
- 🕰 **OWL‑Time** for time instants/intervals (timeline-friendly modeling)
- 🌍 **GeoSPARQL** concepts for spatial semantics (even if heavy geometry stays in PostGIS)

📌 **Rule:** if you create a new node type that maps cleanly to an ontology class/property, add it to:
- `ontology/…` (bindings)
- `schema/…` (labels/rels/props)
- `mapping_rules.md` (how metadata maps into the graph)

---

## 🧰 Ingestion Strategy (CSV → Neo4j)

### ✅ Principle: “No Mystery Nodes”

Graph content must be traceable to one of:

- STAC/DCAT/PROV metadata (preferred)
- curated narrative content (Story Nodes) with citations
- controlled enrichments (NLP linking / embeddings) that are auditable and provenance-linked

### 📄 CSV contract expectations (typical)

- `nodes_*.csv` (e.g., `nodes_dataset.csv`, `nodes_place.csv`, `nodes_event.csv`)
- `rels_*.csv` (e.g., `rels_mentions.csv`, `rels_located_in.csv`, `rels_prov_used.csv`)
- `meta_import_manifest.json` (build_id, timestamp, git sha, profile versions)

💡 Determinism matters: CSV generation should be stable across rebuilds (sorted ordering, stable IDs).

### ⚙️ Bulk import vs upsert

Use the right tool for the job:

- 🧱 **Bulk import** (fastest): great for full rebuilds from scratch.
- 🔁 **Upsert/merge** (incremental): safer for partial refreshes, but must be carefully constrained.

> Whichever path you use: constraints/indexes must be applied consistently, and health checks must verify integrity afterward.

---

## 🧷 Constraints & Indexes (Minimum Baseline)

At minimum, expect:

- Uniqueness constraints on `:Label(id)`
- Indexes on common keys (`name`, `source_id`, `stac_id`, `dcat_id`, `prov_id`)
- Full-text indexes for `Document`, `StoryNode`, `Concept`, and entity names/aliases

<details>
<summary>🧷 Example Cypher (baseline constraints)</summary>

```cypher
// Unique IDs
CREATE CONSTRAINT dataset_id IF NOT EXISTS
FOR (n:Dataset) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT place_id IF NOT EXISTS
FOR (n:Place) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT event_id IF NOT EXISTS
FOR (n:Event) REQUIRE n.id IS UNIQUE;

// Required fields (Neo4j 5+ supports property existence constraints)
CREATE CONSTRAINT dataset_source_id IF NOT EXISTS
FOR (n:Dataset) REQUIRE n.source_id IS NOT NULL;
```
</details>

---

## 🔎 Query Design (Curated Traversals Only)

The graph is powerful, but **unbounded traversals** are how you get slow queries and governance leaks.

**Rule of thumb:** the API should call **curated Cypher templates** that:
- enforce max-depth
- enforce label/rel allowlists
- enforce governance filters
- return stable IDs + provenance pointers

Examples of “safe” query helpers:

- `search_entities` — entity lookup by name/alias/id
- `expand_neighbors` — bounded neighbor expansion with allowlisted rels
- `provenance_chain` — bounded lineage walk (PROV-style)
- `storynode_context` — gather a Story Node’s referenced entities + citations

---

## 🩺 Graph Health Check (Integrity + Drift)

KFM expects recurring QA routines that validate:

- ✅ constraints/indexes are present
- ✅ orphan detection (unconnected nodes that should not exist)
- ✅ provenance completeness for publishable nodes
- ✅ drift vs current CSV export (graph contains nodes not in current export)
- ✅ cross-store referential checks (e.g., Place IDs align with PostGIS/canonical catalogs)

<details>
<summary>🧪 Example Cypher checks</summary>

```cypher
// Orphaned nodes (excluding allowed singletons)
MATCH (n)
WHERE size((n)--()) = 0 AND NOT n:ImportManifest
RETURN labels(n) AS labels, count(*) AS orphans
ORDER BY orphans DESC;
```

```cypher
// Duplicate IDs (should be prevented by constraint, but useful as smoke test)
MATCH (n)
WITH n.id AS id, count(*) AS c
WHERE id IS NOT NULL AND c > 1
RETURN id, c
ORDER BY c DESC;
```
</details>

---

## 🧠 Focus Mode Integration (AI + Graph + Search)

Focus Mode is designed to be **retrieval-first**:

1. Parse user question (intent, entities, time/place constraints)
2. Retrieve evidence:
   - 🕸️ Neo4j graph traversals (entities + relationships)
   - 🔎 search index results (documents/story text/OCR)
   - 🧲 optional embeddings (vector similarity)
3. Compose answer with **citations**
4. Run governance gate:
   - block unsafe content
   - **block uncited assertions** (“No Source, No Answer”)
5. Return structured answer to UI (text + citation mapping)

📌 The graph is the “multi-hop context engine” that prevents the LLM from guessing.

---

## 🛡️ Governance: Provenance‑First + Safe‑By‑Default

This module must support:

- ✅ provenance chains (what produced what, using which inputs)
- ✅ auditability (who/what created nodes, when)
- ✅ sensitivity tagging and enforceable redaction pathways

**Rule of thumb:**  
If something lacks provenance (even a stub), it shouldn’t be promoted for UI/AI use.

### 🔐 How governance should work in practice

- Graph stores `classification` / `sensitivity` tags on nodes/edges.
- API enforces access based on user roles + policy pack.
- Sensitive nodes may be:
  - excluded
  - generalized (e.g., coarse location)
  - returned with limited fields

---

## 🖥️ UI Integration (Graph-backed Features)

Even though UI never queries Neo4j directly, the graph should enable:

- 🧾 **Entity panels** (place/person/dataset summaries + provenance)
- 🧭 **Related items** (“neighbors” by concept/time/place/citations)
- 🧵 **Story Nodes** with explicit references to datasets + places + docs
- 🧠 **Explainability** (“why this result?” via traversal + provenance chain)
- 🧷 **Citations** as clickable links (mapped back to stable IDs)

---

## 🧩 Extending the Graph (Developer Playbook)

When adding a new concept, label, or relationship:

1. 🧱 Define label/rel + required properties in `schema/`
2. 🧬 Map it to an ontology class/property (when appropriate)
3. 📄 Update CSV generation → `data/graph/csv/`
4. 🧷 Add constraints/indexes (migration file)
5. 🔌 Expose via API (curated endpoints; no raw Cypher from UI)
6. 🩺 Update health checks + tests
7. 📝 Update this README + any architecture/governance docs

---

## 🧪 Testing Guidance (Minimum Coverage)

Recommended coverage for `src/graph`:

- ✅ unit tests for CSV parsing + type coercion
- ✅ golden-file tests for CSV exports (deterministic ordering)
- ✅ integration test: spin up Neo4j container → ingest → run smoke queries
- ✅ contract tests: API returns same node IDs as graph export
- ✅ health-check tests: corrupted fixtures fail loudly

---

## 🗺️ Roadmap Hooks (Graph-Centric)

From the broader KFM roadmap and proposals, graph-adjacent “next wins” include:

- 🧵 **Pulse Threads**: lightweight micro-story nodes capturing emerging signals & references
- 🧠 **Conceptual Attention Nodes**: curated theme nodes for clustering + browsing
- 🔍 **Graph analytics** (hubs, bridges, communities) for narrative pattern detection
- 🌐 **Federated graph** / **GraphQL federation** for multi-region “Frontier Matrix” networks
- 🧾 **Explainable traversals** (“why did we link these?”) as first-class UI artifacts

---

## 📚 Project Docs & Reference Library (What Informs This Module)

### Core KFM system docs (architecture + behavior)
- **KFM – Comprehensive Platform Overview and Roadmap** 🗺️
- **KFM – Comprehensive UI System Overview (Technical Architecture Guide)** 🎛️
- **KFM – Comprehensive Architecture, Features, and Design** 🏛️
- **KFM – AI System Overview 🧭🤖** 🤖
- **📚 KFM – Expanded Technical & Design Guide** 📚
- **KFM – Comprehensive Technical Documentation** 🧱
- **KFM AI Infrastructure – Ollama Integration Overview** 🧠

### Engineering & research libraries (PDF portfolios / multi-doc bundles)
These are “grab bag” knowledge packs that influence implementation patterns, modeling approaches, and operational rigor:

- **AI Concepts & more** 🤖📦 — AI foundations & retrieval thinking
- **Maps / GoogleMaps / Virtual Worlds / Archaeological / WebGL** 🌍🛰️ — mapping + 2D/3D web visualization context
- **Data Management / Theories / Architectures / Bayesian Methods** 🧠📚 — robustness + uncertainty + data lifecycle ideas
- **Mapping / Modeling / Python / Git / HTTP / Docker / GraphQL / Security** 🧰🔐 — full-stack patterns & hardening
- **Geographic Information / Security / SciPy / ArcGIS / Spark / TypeScript** 🗺️⚙️ — GIS + compute + web app tooling
- **Various programming languages & resources** 🧩📚 — language ecosystem references

> 🧭 If you’re unsure where to implement something:
> - **Semantic relationships / provenance / narrative linking?** → `src/graph/`
> - **Geometry / spatial filtering / tiles?** → PostGIS + spatial adapters
> - **Presentation / interaction?** → web UI
> - **Policy / redaction / permissioning?** → API + policy pack

---

## ✅ “Done” Definition for `src/graph`

This folder is “healthy” when:

- [ ] Graph can be rebuilt **entirely** from `data/graph/csv/`
- [ ] Constraints + indexes are applied consistently
- [ ] Health checks run and fail on drift/corruption
- [ ] API exposes curated graph traversals (GraphQL + REST)
- [ ] Focus Mode can cite sources via graph traversal paths
- [ ] Sensitive content is classified + enforceable through the API
- [ ] “No Mystery Nodes” invariant holds (everything traceable)