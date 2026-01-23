# 🕸️ KFM Graph Subsystem (Neo4j) — `src/graph`

![Neo4j](https://img.shields.io/badge/Neo4j-knowledge%20graph-008CC1?logo=neo4j&logoColor=white)
![STAC](https://img.shields.io/badge/STAC-catalogs-informational)
![DCAT](https://img.shields.io/badge/DCAT-metadata-informational)
![PROV](https://img.shields.io/badge/PROV-lineage-informational)
![PostGIS](https://img.shields.io/badge/PostGIS-spatial%20DB-informational)

> **What this folder is:** the **semantic backbone** of Kansas Frontier Matrix (KFM).  
> It builds and maintains the **Neo4j knowledge graph** used to connect **datasets ↔ places ↔ events ↔ people ↔ documents ↔ stories**, power **Focus Mode** multi-hop reasoning, and keep **provenance-first** guarantees intact. 🧭🤖

---

## 🧠 Why a Graph?

KFM uses **two “truthy” storage backends** for different kinds of questions:

- 🗺️ **PostGIS**: the heavy geospatial lifting (bbox filters, distance, tiling, geometry ops).
- 🕸️ **Neo4j (Graph)**: semantic relationships, lineage chains, narratives, entity linking, and multi-hop exploration.

The graph exists so the system can answer questions like:

- “What datasets are related to **event X** in **place Y**?”
- “What happened **here** during **the 1930s**?”
- “Show me the **story nodes** that reference these layers and this county.”

---

## 🔗 Quick Links (Repo)

- `../../data/graph/csv/README.md` 📄 (import-ready CSV contracts)
- `../../docs/MASTER_GUIDE_v13.md` 🧱 (repo conventions + pipeline ordering)
- `../../docs/architecture/` 🏛️ (system architecture)
- `../../api/` 🔌 (API layer that runs Cypher/SQL and enforces policy)

> **Golden rule:** ✅ UI talks to the graph **only via the API** (never direct Cypher).  
> This is how we enforce access control, provenance requirements, and redaction rules.

---

## 🧭 Responsibilities (What `src/graph` owns)

✅ This module owns:

- 🧬 **Ontology bindings & mapping rules** (e.g., CIDOC-CRM / OWL-Time / GeoSPARQL / PROV-O alignment)
- 🧱 **Graph schema contract** (labels, relationship types, key properties)
- 🧰 **Ingest tooling** from `data/graph/csv/` (bulk load, incremental sync if supported)
- 🧷 **Constraints & indexes** (uniqueness, required fields, search indexes)
- 🩺 **Graph Health Check** routines (integrity, drift, orphan detection, counts)
- 🔎 **Query helpers** used by the API + Focus Mode (curated traversals, not “free-form”)

🚫 This module does **not** own:

- Heavy geometry computations (belongs in PostGIS)
- UI-specific view state (belongs in web client)
- Raw data fetching (belongs in pipeline intake)

---

## 📦 Folder Map (Recommended Layout)

> Your tree may vary, but `src/graph` should feel like a **mini product**: schema → ingest → constraints → health → queries.

```text
📁 src/graph/
├─ 📄 README.md                     # you are here
├─ 📁 ontology/                     # 🧬 ontology bindings (CIDOC, PROV, OWL-Time, GeoSPARQL…)
│  ├─ 📄 cidoc_crm.yaml|json|ttl
│  ├─ 📄 prov_o.yaml|json|ttl
│  └─ 📄 mapping_rules.md
├─ 📁 schema/                       # 🧱 label + rel contract (and invariants)
│  ├─ 📄 labels.md
│  ├─ 📄 relationships.md
│  └─ 📄 property_keys.md
├─ 📁 constraints/                  # 🧷 Neo4j constraints + indexes (Cypher)
│  ├─ 📄 001_constraints.cypher
│  └─ 📄 002_indexes.cypher
├─ 📁 ingest/                       # 🧰 CSV → Neo4j (bulk import / sync)
│  ├─ 📄 ingest_csv.py|ts
│  ├─ 📄 upsert_strategies.md
│  └─ 📄 id_strategy.md
├─ 📁 queries/                      # 🔎 curated Cypher templates (used by API)
│  ├─ 📄 search_entities.cypher
│  ├─ 📄 expand_neighbors.cypher
│  └─ 📄 provenance_chain.cypher
└─ 📁 health/                       # 🩺 integrity + drift detection
   ├─ 📄 graph_health_check.py|ts
   └─ 📄 health_checks.cypher
```

---

## 🔁 Data Flow & Ordering Invariants (KFM-wide)

KFM’s pipeline order matters because it enforces reproducibility and provenance:

1. 🧱 `data/raw/` — source data (immutable inputs)
2. 🧪 `data/processed/` — derived data products (versioned)
3. 🗂️ `data/stac/`, `data/catalogs/`, `data/prov/` — catalogs + lineage
4. 🕸️ `data/graph/csv/` → **Neo4j import** (derived semantic layer)

### Mermaid: end-to-end flow

```mermaid
flowchart LR
  raw[🧱 data/raw] --> processed[🧪 data/processed]
  processed --> catalogs[🗂️ STAC/DCAT/PROV]
  catalogs --> csv[📄 data/graph/csv]
  csv --> neo4j[(🕸️ Neo4j)]
  processed --> postgis[(🗺️ PostGIS)]
  neo4j --> api[🔌 API (FastAPI/GraphQL)]
  postgis --> api
  api --> ui[🖥️ Web UI]
  api --> ai[🧠 Focus Mode AI]
```

---

## 🚀 Quickstart (Local Dev)

### 1) Start Neo4j (Docker-first)

> If the repo has a Neo4j service, use it. Otherwise, Neo4j Desktop is fine.

```bash
docker compose up -d neo4j
```

### 2) Configure env

```bash
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="password"
# export NEO4J_DATABASE="neo4j"   # optional
```

### 3) Generate import CSVs

The **authoritative import contract** is `data/graph/csv/`.  
These CSVs are typically generated **after** STAC/DCAT/PROV exists.

```bash
# Example (adjust to actual pipeline tooling):
python -m src.pipelines.build_graph_csv --out data/graph/csv
```

### 4) Apply constraints + indexes

```bash
# Example (adjust to actual tooling):
python -m src.graph.constraints.apply
```

### 5) Ingest into Neo4j

```bash
# Example (adjust to actual tooling):
python -m src.graph.ingest.ingest_csv --csv-dir data/graph/csv
```

✅ **Rebuild-friendly:** the graph is a **derived store**.  
If you get into a bad state, it’s usually acceptable to **drop + reimport** (assuming the CSVs are correct and complete).

---

## 🧬 Modeling Rules (Schema Contract)

KFM’s graph is intended to be **ontology-aware**, not just “random nodes and edges”.

### 🏷️ Labels (canonical examples)

- `Dataset` — a layer/data product (ties to DCAT + STAC)
- `StacCollection`, `StacItem`, `Asset` — catalog structure
- `Place` — gazetteer-backed locations (counties, towns, rivers…)
- `Event` — historical events, observations, incidents
- `Person`, `Organization` — people/institutions
- `Document` — text sources (newspapers, reports, treaties)
- `StoryNode` — narrative object referencing datasets + places + docs
- `Concept` — topic/theme nodes (used for clustering + browsing)
- `Activity`, `Agent`, `Entity` — provenance (PROV-style)

### 🔗 Relationships (canonical examples)

Use **UPPER_SNAKE_CASE** for relationships:

- `LOCATED_IN`, `HAPPENED_AT`
- `MENTIONS`, `CITES`, `DERIVED_FROM`
- `HAS_ITEM`, `HAS_ASSET`
- `REFERENCES_DATASET`, `REFERENCES_PLACE`
- `WAS_GENERATED_BY`, `USED` (PROV-ish)
- `TAGGED_WITH` (concept/topic)

### 🆔 Identity & Keys

Every node that’s “real” must have:

- `id` — stable unique ID (prefer **ULID** or deterministic composite keys)
- `source` — where it came from (DCAT distribution, archive, pipeline)
- `version` / `valid_time` where applicable
- `classification` / `sensitivity` when needed (privacy + cultural protocols)

---

## 🧰 Ingestion Strategy (CSV → Neo4j)

### ✅ Principle: “No mystery nodes”

All graph content should be traceable to:

- STAC/DCAT/PROV metadata, or
- curated narrative content (Story Nodes) with citations, or
- controlled enrichments (NLP entity linking / embeddings) that remain **auditable**

### 📄 CSV Contract Expectations

Your CSV set should typically include:

- `nodes_*.csv` (e.g., `nodes_dataset.csv`, `nodes_place.csv`, `nodes_event.csv`)
- `rels_*.csv` (e.g., `rels_mentions.csv`, `rels_located_in.csv`, `rels_prov_used.csv`)
- optional `meta_import_manifest.json` (build id, timestamp, git sha)

> Tip: keep “CSV generation” deterministic so graph rebuilds are repeatable.

---

## 🩺 Graph Health Check (Integrity + Drift)

KFM design docs propose a recurring graph QA routine. This folder should own it.

### What to check (minimum viable)

- ✅ Constraint presence (uniqueness / required keys)
- ✅ Index presence (common lookup keys)
- ✅ Orphan detection (nodes with zero meaningful relationships)
- ✅ Broken foreign keys (e.g., `county_id` exists in graph but not in PostGIS)
- ✅ Provenance completeness for published nodes
- ✅ Drift vs CSV export (graph contains nodes not present in current export)

### Example Cypher checks

```cypher
// Orphaned nodes (excluding allowed singletons)
MATCH (n)
WHERE size((n)--()) = 0 AND NOT n:ImportManifest
RETURN labels(n) AS labels, count(*) AS orphans
ORDER BY orphans DESC;
```

```cypher
// Duplicate IDs (should be prevented by constraint, but useful as a smoke test)
MATCH (n)
WITH n.id AS id, count(*) AS c
WHERE id IS NOT NULL AND c > 1
RETURN id, c
ORDER BY c DESC;
```

---

## 🧠 Focus Mode Integration (AI + Graph)

Focus Mode should be able to:

- translate a user question into **graph traversals**
- find the right **datasets / places / events / docs**
- merge structured graph context with unstructured document retrieval (RAG-style)
- always return **traceable citations** back to sources

> The graph is the “multi-hop context engine” that prevents the LLM from guessing. ✅

---

## 🖥️ UI Integration (Graph-backed features)

Even if the UI never hits Neo4j directly, the graph should enable:

- 🧾 “Entity panels” (what is this place/person/dataset?)
- 🧭 “Related items” (neighbors by concept, time, location, citations)
- 🧵 Story Nodes with links to datasets + map features
- 🧠 AI “why this result?” explainability (show traversal + provenance)

---

## 🧩 Extending the Graph (Developer Playbook)

When adding a new concept, node type, or relationship:

1. 🧱 **Define** label + relationship in `schema/`
2. 🧬 **Map** it to an ontology class/property when appropriate
3. 📄 **Update** CSV generation (in pipeline) → `data/graph/csv/`
4. 🧷 **Add** constraints/indexes
5. 🔌 **Expose** via API (curated endpoints; no raw Cypher from UI)
6. 🩺 **Update** health checks + tests
7. 📝 **Document** in this README + relevant design docs

---

## 🛡️ Governance: Provenance-first + Safe-by-default

The graph must support:

- ✅ provenance chains (what produced what, using which inputs)
- ✅ auditability (who/what created nodes, when)
- ✅ access control & redaction (sensitive places, private stations, protected knowledge)

**Rule of thumb:**  
If something doesn’t have a provenance record (even a stub), it shouldn’t be promoted for UI/AI use.

---

## 🧪 Testing Guidance

Minimum recommended coverage:

- ✅ unit tests for CSV parsing + type coercion
- ✅ golden-file tests for CSV exports (deterministic ordering)
- ✅ integration test: spin up Neo4j container → ingest → run smoke queries
- ✅ contract tests: API endpoints return same node IDs as graph export
- ✅ health-check tests: corrupted fixtures fail loudly

---

## 🗺️ Roadmap Ideas (From project proposals)

- 🧵 **Pulse Threads**: lightweight “micro-story” nodes capturing emerging signals & references
- 🧠 **Conceptual Attention Nodes**: curated theme nodes that help browsing + clustering
- 🔍 **Narrative pattern detection** using graph analytics (hubs, bridges, communities)
- 🌐 **Federated graph** (multi-institution, policy-controlled sharing)
- 🧾 **Explainable traversals** (“why did we link these?”)

---

## 📚 Project Docs & Reference Library (What informed this module)

### Core KFM Docs (must-read)
- **Comprehensive Architecture, Features, and Design** — stack + boundaries
- **Comprehensive Technical Documentation** — deep system design + graph analytics ideas
- **AI System Overview** — Focus Mode graph usage and RAG orchestration
- **UI System Overview** — how graph-backed entity linking shows up in UI
- **Data Intake Guide** — catalogs → CSV → graph pipeline expectations

### Proposals & Future Work
- **Latest Ideas & Future Proposals** — OCR/document ingestion into graph + vectors
- **Additional Project Ideas** — graph health checks, pulse threads, attention nodes
- **Innovative Concepts to Evolve KFM** — governance, community, AI explainability

### Research Libraries (background)
- **AI Concepts & more** — AI/ML theory base for retrieval + reasoning
- **Data Management / Architecture / Bayesian Methods** — performance + reliability thinking
- **Maps / WebGL / Geospatial** — map rendering + spatial computation references
- **Programming Languages & Resources** — Python/TypeScript reference material

---

## ✅ “Done” Definition for `src/graph`

This folder is “healthy” when:

- [ ] Graph can be rebuilt **entirely** from `data/graph/csv/`
- [ ] Constraints + indexes are applied consistently
- [ ] Health checks run and fail on drift/corruption
- [ ] API exposes curated graph traversals
- [ ] Focus Mode can cite sources via graph traversal paths
- [ ] Sensitive content is classified + enforceable through the API

---

🧭 If you’re unsure where to implement something:
- **Is it semantic relationships / provenance / narrative linking?** → `src/graph/`
- **Is it geometry / spatial filtering / tiles?** → PostGIS + spatial adapters
- **Is it presentation / interaction?** → web UI
- **Is it policy / redaction / permissioning?** → API + policy pack