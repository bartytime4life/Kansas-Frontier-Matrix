# 🕸️ `tools/graph` — KFM Graph Toolkit

![Stage](https://img.shields.io/badge/stage-active--design-informational)
![Graph](https://img.shields.io/badge/graph-knowledge%20%26%20provenance-success)
![Store](https://img.shields.io/badge/store-Neo4j%20(Property%20Graph)-brightgreen)
![Geo](https://img.shields.io/badge/geo-PostGIS%20%2B%20COG%20%2B%20GeoParquet-blue)
![API](https://img.shields.io/badge/API-FastAPI%20%2B%20GraphQL-purple)
![Principle](https://img.shields.io/badge/principle-provenance--first%20%7C%20contract--first-orange)

> **Goal:** turn curated datasets + documents into a **queryable, explainable, and time-aware** graph that powers **Focus Mode**, story linking, and semantic queries across Kansas. 🧭

---

<details>
<summary>📚 Contents (click to expand)</summary>

- [✨ What this folder is for](#-what-this-folder-is-for)
- [🧠 Why a graph in KFM?](#-why-a-graph-in-kfm)
- [🧱 Non‑negotiables (project rules)](#-nonnegotiables-project-rules)
- [🗺️ Where `tools/graph` sits in the system](#️-where-toolsgraph-sits-in-the-system)
- [📁 Proposed folder layout](#-proposed-folder-layout)
- [🚀 Quickstart (local dev)](#-quickstart-local-dev)
- [🧩 Graph data model (opinionated defaults)](#-graph-data-model-opinionated-defaults)
- [🧾 Contracts & provenance (how we stay explainable)](#-contracts--provenance-how-we-stay-explainable)
- [⏱️ Time model: “what happened” vs “what we know”](#️-time-model-what-happened-vs-what-we-know)
- [🔎 Querying (Cypher + GraphQL)](#-querying-cypher--graphql)
- [📈 Analytics & graph science](#-analytics--graph-science-optional-but-powerful)
- [🌍 Geospatial + remote sensing integration](#-geospatial--remote-sensing-integration)
- [🖥️ Visualization exports (WebGL-friendly)](#️-visualization-exports-webgl-friendly)
- [🛡️ Security, ethics, and governance](#️-security-ethics-and-governance)
- [🧪 Testing checklist](#-testing-checklist)
- [🧭 Roadmap](#-roadmap-high-impact-next-steps)
- [📚 Project Library Index](#-project-library-index-used-by-this-tool)
- [🤝 Contributing](#-contributing)

</details>

---

## ✨ What this folder is for

This `tools/graph` toolkit is responsible for:

- 🔗 **Linking entities** across sources: *people ↔ places ↔ events ↔ documents ↔ datasets*  
- 🧾 Preserving **end-to-end provenance** (where every node/edge came from)  
- ⏱️ Supporting **time travel** queries (what we *believed* at a moment vs what *occurred*)  
- 🌍 Bridging **geospatial + semantic** views (PostGIS ↔ Neo4j)  
- ⚙️ Feeding the **API layer** (FastAPI + GraphQL) with graph-friendly materialized views

---

## 🧠 Why a graph in KFM?

KFM is built to answer questions like:

- “What happened **here**?” (place → events → evidence)
- “Show me all events in the 1850s involving **people who were governors**.” (role + time + traversal)
- “What datasets and documents support this claim?” (narrative → citations → provenance chain)

A property graph makes these “relationship-first” questions direct, and it keeps the AI honest by making the connections explicit instead of implied. 🧩

---

## 🧱 Non‑negotiables (project rules)

These are the invariants this tool enforces:

1. **Provenance-first**: every record has an origin, a method, and a version.
2. **Contract-first**: nothing enters the graph unless it passes a dataset/doc “contract” (metadata + schema).
3. **Canonical pipeline order**:  
   **Data → Catalogs → Graph → API → UI → Narrative** (stories ride on top of evidence).
4. **Stable, information-free IDs**: no semantic meaning baked into identifiers (so renames don’t break links).
5. **Open standards** where possible (GeoJSON/GeoParquet/COG/STAC/DCAT/PROV-O, etc.).

---

## 🗺️ Where `tools/graph` sits in the system

```mermaid
flowchart LR
  A[📦 Raw / Processed Data] --> B[🗂️ Catalogs<br/>STAC / DCAT]
  B --> C[🕸️ Graph Build<br/>Entities + Edges + Provenance]
  C --> D[🧩 API Layer<br/>FastAPI + GraphQL]
  D --> E[🗺️ UI Layer<br/>Maps + Graph Explorer]
  E --> F[📖 Narrative Layer<br/>Stories + Focus Mode]
```

> ✅ **Rule of thumb:** if it can’t be cataloged + cited, it doesn’t belong in the graph.

---

## 📁 Proposed folder layout

> If the repo already has files here, keep them — this is a target shape, not a hard requirement.

```text
tools/graph/ 🕸️
├─ 🧰 pyproject.toml               # Python packaging + tool config
├─ 🧰 requirements.txt             # pinned deps (optional; CI/dev)
├─ 🐍 kfm_graph/                   # graph build toolkit (Python package)
│  ├─ 🧩 __init__.py               # package init
│  ├─ 🔧 config.py                 # env + settings
│  ├─ 🧾 contracts/                # contract parsing + validation
│  ├─ 🧲 extract/                  # entity extraction (docs, tables, GIS)
│  ├─ 🧠 resolve/                  # entity resolution + dedupe
│  ├─ 🧩 model/                    # labels, rel types, property schemas
│  ├─ 🚚 load/                     # Neo4j upserts + batching
│  ├─ 🧬 provenance/               # PROV graph + lineage utilities
│  ├─ 📤 export/                   # GraphML/CSV/JSON/GeoJSON exports
│  └─ 📈 analytics/                # centrality, communities, spectral tools
├─ 🗃️ queries/                     # saved query artifacts
│  ├─ 🟩 cypher/                   # saved Cypher queries
│  └─ 🟪 graphql/                  # saved GraphQL examples
├─ 🛠️ scripts/                     # developer + ops scripts
│  ├─ 🏗️ build_graph.py            # end-to-end build
│  ├─ ✅ validate_contracts.py     # fail-fast checks
│  ├─ 🧾 backfill_provenance.py    # ensure lineage completeness
│  └─ 📤 export_views.py           # API-ready exports
└─ 📘 README.md                    # you are here
```

---

## 🚀 Quickstart (local dev)

### 1) Bring up Neo4j (example)

```bash
docker run --rm \
  --name kfm-neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password \
  neo4j:5
```

### 2) Configure environment

```bash
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="password"

# Optional (if enriching from PostGIS):
export POSTGRES_DSN="postgresql://user:pass@localhost:5432/kfm"
```

### 3) Validate contracts → build graph

```bash
python -m kfm_graph.contracts.validate ./data/catalogs
python -m kfm_graph.scripts.build_graph --catalog ./data/catalogs --mode upsert
```

> 💡 Keep graph builds **idempotent**: re-running should converge to the same state for the same catalog version.

---

## 🧩 Graph data model (opinionated defaults)

### Node labels (starting set)

| Label | What it represents | Notes |
|---|---|---|
| `Place` | county/city/feature/site | store `geometry` or link to PostGIS |
| `Person` | individuals | support aliases + role/office facts |
| `Organization` | agencies/companies/tribes | treat as first-class entity |
| `Event` | historical or real-time events | attach time bounds + impacted places |
| `Document` | PDFs, scans, articles | citation anchors + page refs |
| `Dataset` | curated dataset entry | contract pointer + versions |
| `Observation` | sensor/remote-sensed measurement | time series friendly |
| `StoryNode` | narrative objects | *never authoritative*; always cites |

### Relationship types (starting set)

- `(:Person)-[:PARTICIPATED_IN]->(:Event)`
- `(:Event)-[:OCCURRED_AT]->(:Place)`
- `(:Document)-[:MENTIONS]->(:Person|:Place|:Event)`
- `(:Dataset)-[:DESCRIBES]->(:Event|:Place)`
- `(:StoryNode)-[:CITES]->(:Document|:Dataset)`
- `(:Any)-[:DERIVED_FROM]->(:Dataset|:Document)` *(provenance chain)*

### “Required everywhere” properties

Every node/edge should carry:

- `id` (stable, information-free)
- `source_id` (dataset/doc id)
- `source_version` (semver/date/hash)
- `confidence` (0–1 or enum)
- `provenance_ref` (pointer to PROV record / contract block)
- `valid_time` + `transaction_time` (when relevant)

---

## 🧾 Contracts & provenance (how we stay explainable)

### Contract = the gatekeeper ✅

A “contract” is a metadata + schema bundle that answers:

- Who produced this?
- Where did it come from?
- What transformations happened?
- What license governs it?
- What spatial/temporal extent does it cover?
- How do I validate its fields?

Minimal contract shape (example):

```json
{
  "id": "dataset:kfm:rainfall_county",
  "version": "2026-01-01",
  "title": "Rainfall by County",
  "source": {
    "publisher": "…",
    "url": "…",
    "retrieved_at": "…",
    "license": "…"
  },
  "spatial_extent": { "type": "Polygon", "crs": "EPSG:4326", "bbox": [ ... ] },
  "temporal_extent": { "start": "1930-01-01", "end": "1940-12-31" },
  "schema": { "format": "parquet", "columns": [ ... ] },
  "lineage": [
    { "step": "download", "tool": "…", "inputs": [ ... ], "outputs": [ ... ] },
    { "step": "clean", "tool": "…", "params": { ... } }
  ]
}
```

### Provenance graph = the receipt chain 🧾

Provenance lives in two places:

- In contracts (human-readable + auditable)
- In graph edges (`DERIVED_FROM`, `CITES`, `USED_IN_STEP`, etc.) that enable **traceback queries**

**Design mantra:** *If Focus Mode can’t cite it, it didn’t happen.* 🧬

---

## ⏱️ Time model: “what happened” vs “what we know”

Most KFM questions are time-sensitive. The graph should support:

- **Valid time:** when the fact/event was true in the world  
- **Transaction time:** when we recorded/ingested/updated the fact

This enables “time travel” like:

- “What did we know about irrigation wells as of 2010?”  
- “What events were happening in 1936, but only discovered via documents digitized in 2024?”

---

## 🔎 Querying (Cypher + GraphQL)

### Cypher (Neo4j) examples 🟩

Find events linked to a place, with evidence:

```cypher
MATCH (p:Place {id:$place_id})<-[:OCCURRED_AT]-(e:Event)
OPTIONAL MATCH (d:Document)-[:MENTIONS]->(e)
RETURN e, collect(DISTINCT d)[0..20] AS evidence
ORDER BY e.start_date
LIMIT 200;
```

### GraphQL examples 🟪

GraphQL is ideal when the client needs **nested traversals** without multiple REST round-trips:

```graphql
{
  person(name: "John Brown") {
    name
    events {
      title
      date
      locations { name }
    }
  }
}
```

> 🧯 Always enforce **pagination + depth limits** to avoid pathological queries.

---

## 📈 Analytics & graph science (optional but powerful)

Once the graph is clean + provenance-complete, we can run:

- ⭐ Centrality (influence/importance)
- 🧭 Shortest paths (e.g., document citation chains)
- 🧱 Community detection (clusters of events/actors)
- 🎼 Spectral methods (Laplacian-based clustering / structure signals)

Attach analytics outputs back to the graph as `(:AnalysisRun)` nodes so results are reproducible.

---

## 🌍 Geospatial + remote sensing integration

KFM is a **hybrid** stack:

- **PostgreSQL + PostGIS**: authoritative spatial tables + indexes  
- **COG / GeoParquet**: big rasters + columnar vectors (kept out of the DB when huge)  
- **Neo4j**: semantic, relationship-rich layer  
- **Google Earth Engine (optional)**: on-demand remote sensing pulls

Graph best practice:

- Don’t duplicate heavy geometries in Neo4j unless required.
- Store a *thin* graph reference: `place_id`, `bbox`, `admin_codes`, `postgis_pk`, `cog_footprint_id`, etc.

---

## 🖥️ Visualization exports (WebGL-friendly)

For UI exploration, this tool should be able to export:

- `GraphML` / `CSV` (bulk interchange)
- `JSON` (node/edge lists for clients)
- `GeoJSON` (place/event overlays)
- “Graph slices” pre-filtered by theme/time/extent (for fast UI)

> Pair with responsive UI + WebGL-based rendering when graph scale grows. 🧊

---

## 🛡️ Security, ethics, and governance

- 🚫 Do not ingest sources without clear licensing.
- 🔐 Keep authn/authz boundaries in the API layer, but the graph must support *access tagging* (public/private/draft).
- 🧑‍⚖️ Prefer human-centered, transparent design: no “black box” graph edits without receipts.
- 🧯 Security research references in this repo are for **defensive hardening** only.

---

## 🧪 Testing checklist

- ✅ Contract validation (schema + required metadata)
- ✅ Deterministic graph builds (same inputs → same outputs)
- ✅ Upsert safety (no accidental fan-out duplicates)
- ✅ Provenance completeness (every node/edge traceable to a contract + version)
- ✅ Performance sanity (batch sizes, indexes, query plans)

---

## 🧭 Roadmap (high-impact next steps)

- [ ] Define canonical labels + relationship types (v1 schema)
- [ ] Implement contract validator + “fail-fast” CI hook
- [ ] Build entity resolution pipeline (aliases, fuzzy matching, geo disambiguation)
- [ ] Add bitemporal support (valid/transaction time) + query helpers
- [ ] Publish “saved queries” library for UI + Focus Mode
- [ ] Add analytics runners (centrality, communities, spectral)
- [ ] Export API-ready graph views (cached query results)

---

## 📚 Project Library Index (used by this tool)

> These files are part of the project’s shared “engineering + research bookshelf.”  
> `tools/graph` uses them as design references and implementation recipes. 📖

### 🧱 Core architecture & system docs
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- **Database Performance at Scale.pdf**
- **Data Spaces.pdf**

### ✍️ Documentation & writing standards
- **MARKDOWN_GUIDE_v13.md.gdoc** (canonical pipeline order + evidence-first writing)
- **Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx**

### 🧠 Graph theory, optimization, and scalable query execution
- **Spectral Geometry of Graphs.pdf**
- **Scalable Data Management for Future Hardware.pdf**
- **Generalized Topology Optimization for Structural Design.pdf**

### 🌍 GIS, mapping, cartography, and 3D
- **python-geospatial-analysis-cookbook.pdf**
- **making-maps-a-visual-guide-to-map-design-for-gis.pdf**
- **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf**
- **Archaeological 3D GIS_26_01_12_17_53_09.pdf**

### 🛰️ Remote sensing
- **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf**

### 📈 Stats, modeling, and inference
- **Understanding Statistics & Experimental Design.pdf**
- **regression-analysis-with-python.pdf**
- **Regression analysis using Python - slides-linear-regression.pdf**
- **think-bayes-bayesian-statistics-in-python.pdf**
- **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf**
- **graphical-data-analysis-with-r.pdf**

### 🧑‍⚖️ Ethics, governance, and society
- **Introduction to Digital Humanism.pdf**
- **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf**
- **Principles of Biological Autonomy - book_9780262381833.pdf**

### 🧰 Engineering references (languages + security + web)
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf**
- **Scipy lecture notes, Edition 2022.1**
- **Implementing Programming Languages: An Introduction to Compilers and Interpreters**
- **Objective-C Notes for Professionals**
- **MATLAB Notes for Professionals**
- **Bash Notes for Professionals**
- **Flexible Software Design**
- **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf**
- **responsive-web-design-with-html5-and-css3.pdf**
- **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf**
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf**
- **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf**
- **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf**
- **A programming Books.pdf**
- **B-C programming Books.pdf**
- **D-E programming Books.pdf**
- **F-H programming Books.pdf**
- **I-L programming Books.pdf**
- **M-N programming Books.pdf**
- **O-R programming Books.pdf**
- **S-T programming Books.pdf**
- **U-X programming Books.pdf**
- **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf**

---

## 🤝 Contributing

- Prefer **small, reviewable** changes.
- Add or update contracts before touching loaders.
- For every new node/edge type: add
  - schema definition
  - example contract excerpt
  - at least one Cypher query proving it’s useful
  - a provenance test proving it’s traceable

If you’re unsure where a feature belongs: **data → catalogs → graph → API → UI → narrative**. ✅

