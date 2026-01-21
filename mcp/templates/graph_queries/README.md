# 🕸️ Graph Query Templates (MCP) — `mcp/templates/graph_queries`

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-blue)
![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-6f42c1)
![Neo4j](https://img.shields.io/badge/Graph-Neo4j-00b3b3)
![GraphQL](https://img.shields.io/badge/API-GraphQL-e10098)
![Evidence First](https://img.shields.io/badge/Principle-Evidence--First-success)

Reusable **graph query templates** (Cypher + GraphQL) for the KFM knowledge graph. These templates exist to keep KFM querying:

- ✅ **Reproducible** (MCP-friendly)
- ✅ **Contract-first** (stable shapes + versioned IDs)
- ✅ **Provenance-first** (everything links back to cataloged sources)
- ✅ **Secure** (RBAC + redaction + auditability)
- ✅ **Performant** (pagination + caching + “don’t do geometry in Neo4j”)

> [!IMPORTANT]  
> **Non‑negotiable KFM rule:** the UI must **never** execute direct Neo4j/Cypher (or Neo4j REST/Bolt) calls.  
> Graph access is mediated by the **API layer** so policy, redaction, and audit rules always apply. 🔐

---

<details>
<summary>📚 Table of contents</summary>

- [✨ What this folder is](#-what-this-folder-is)
- [🧠 Where these templates fit](#-where-these-templates-fit)
- [🗂️ Recommended layout](#️-recommended-layout)
- [🧩 Template anatomy](#-template-anatomy)
- [📦 Query packs](#-query-packs)
- [🧪 How these templates get executed](#-how-these-templates-get-executed)
- [🔐 Governance, safety, and redaction](#-governance-safety-and-redaction)
- [⚡ Performance & correctness checklist](#-performance--correctness-checklist)
- [🧭 Federation readiness](#-federation-readiness)
- [🧰 Adding a new template](#-adding-a-new-template)
- [📎 Project docs & reference packs used](#-project-docs--reference-packs-used)

</details>

---

## ✨ What this folder is

This folder is a **library of parameterized graph queries** used across KFM to:

- power **Focus Mode** retrieval (AI → structured graph traversal → evidence-linked answers)
- support **UI discovery** (search results, “related layers”, “related stories”, “what happened here?”)
- drive **backend services** (GraphQL resolvers / REST endpoints)
- run **QA health checks** (graph integrity, schema drift, runaway hubs)
- enable **research experiments** under MCP (repeatable query runs + reports)

These templates are part of the “**living knowledge base**” approach: not only code + data, but also method artifacts and standard operating procedures. 🧪📓

---

## 🧠 Where these templates fit

```mermaid
flowchart LR
  UI[🗺️ UI: Map + Timeline + Story Nodes + Focus Mode] -->|REST / GraphQL| API[🧠 API Layer<br/>(policy + redaction + caching)]
  API -->|Cypher Templates| KG[(🕸️ Neo4j Knowledge Graph)]
  API -->|SQL / Tiles| PG[(🗺️ PostGIS + Tile/COG stack)]
  API -->|Full-text / embeddings| IDX[(🔎 Search Index)]
  MCP[🧪 MCP Experiments<br/>reports + SOPs] -->|run templates| API
  MCP -->|offline audits| KG
  API -->|Evidence-linked responses| UI
```

### Why a dedicated template library?
Because KFM’s architecture relies on **stable contracts** and **auditability**:

- The **metadata backbone** (STAC + DCAT + PROV) is the source of truth for provenance.
- Neo4j is the **semantic layer** (relationships, context, lineage, discovery).
- PostGIS is the **geometry + heavy lifting** engine (bbox filters, tiles, counts, distances).
- The AI and UI depend on **predictable graph shapes** (no “ad hoc Cypher in prod”). 🧱

---

## 🗂️ Recommended layout

> This is a recommended structure. If your repo differs, adapt it — but keep the *contract* ideas intact.

```text
mcp/
  templates/
    graph_queries/
      README.md
      index.yaml                # template registry (IDs → files)
      manifests/                # per-template specs (YAML)
        kfm.graph.place_context.v1.yaml
        kfm.graph.dataset_lineage.v1.yaml
      cypher/                   # Cypher templates (Neo4j)
        kfm.graph.place_context.v1.cypher
        kfm.graph.dataset_lineage.v1.cypher
        qa.top_degree_nodes.v1.cypher
      graphql/                  # GraphQL operation templates (API schema)
        kfm.place_context.v1.graphql
      tests/                    # fixtures + expected shapes
        fixtures/
        snapshots/
      docs/                     # optional: narrative docs per query pack
        packs.md
```

---

## 🧩 Template anatomy

Every template should have **three** things:

### 1) 🧠 Query template file (`.cypher` or `.graphql`)
- Must be **parameterized** (no string concatenation)
- Must include **sane defaults** (limit, depth, timeframe)
- Must return **provenance pointers** where applicable (dataset IDs + catalog refs)

### 2) 🧾 Manifest (`.yaml`)
A manifest is the **contract** for humans + tools:

- how to execute it
- which parameters it accepts
- what it returns
- governance + performance limits
- caching and pagination behavior
- “expected indexes / constraints” notes

Example manifest:

```yaml
id: kfm.graph.place_context.v1
engine: cypher              # cypher | graphql
status: stable              # draft | stable | deprecated
purpose: discovery
tags: [place, events, documents, datasets, focus_mode]

description: >
  Return a place-centric context bundle:
  events + related documents + related datasets, within a time window.

params:
  place_id:
    type: string
    required: true
    example: "kfm.place.douglas_county.ks"
  time_start:
    type: date
    required: false
    example: "1930-01-01"
  time_end:
    type: date
    required: false
    example: "1939-12-31"
  limit:
    type: integer
    required: false
    default: 50
    max: 200

returns:
  shape: "PlaceContextBundle"
  schema_ref: "schemas/place_context_bundle.v1.json"

governance:
  min_role: "public"        # public | contributor | maintainer | admin
  classification_max: "public"
  requires_provenance: true
  pii_safe: true

performance:
  cache_ttl_seconds: 3600
  max_hops: 4
  notes:
    - "Use Place(id) index"
    - "Avoid returning geometry; use PostGIS for shapes"
```

### 3) 📦 Output contract (schema + shape)
- Provide a JSON Schema (or Pydantic model) for “what comes out”
- Keep it **stable** unless you bump template version
- Include **evidence hooks** (IDs + catalog references)

---

## 📦 Query packs

To keep the library navigable, organize templates into packs. Each pack has a **design purpose** and a **limit profile**.

### 🔎 1) Discovery & Search
Used by UI search, “related content”, and Focus Mode “what data do we have?”.

✅ Good for:
- datasets by theme/time/place
- “related datasets” recommendations
- “show me all layers for this timeframe”

💡 Template ideas:
- `kfm.search.datasets_by_theme_time_place.v1`
- `kfm.search.related_datasets_by_shared_prov.v1`

---

### 📍 2) Place context bundles
Used for “what happened here?”, map click popovers, and Focus Mode contextual grounding.

💡 Template ideas:
- `kfm.graph.place_context.v1`
- `kfm.graph.place_events.v1`
- `kfm.graph.place_documents.v1`

**Cypher example (illustrative — align relationship names with your ontology):**
```cypher
// kfm.graph.place_context.v1.cypher
MATCH (p:Place {id: $place_id})
OPTIONAL MATCH (e:Event)-[:AFFECTED]->(p)
WHERE ($time_start IS NULL OR e.start_date >= date($time_start))
  AND ($time_end   IS NULL OR e.end_date   <= date($time_end))
OPTIONAL MATCH (d:Document)-[:MENTIONS]->(e)
OPTIONAL MATCH (ds:Dataset)-[:DOCUMENTS]->(e)
RETURN
  p { .id, .name }                       AS place,
  collect(DISTINCT e { .id, .label, .start_date, .end_date })[0..$limit] AS events,
  collect(DISTINCT d { .id, .title, .source_url })[0..$limit]           AS documents,
  collect(DISTINCT ds { .id, .title, .dcat_ref, .stac_ref, .prov_ref })[0..$limit] AS datasets;
```

---

### 🧬 3) Provenance & lineage
Used for “how was this made?”, reproducibility checks, and audit trails.

💡 Template ideas:
- `kfm.graph.dataset_lineage.v1`
- `kfm.graph.dataset_inputs_outputs.v1`
- `kfm.graph.prov_activity_by_run_id.v1`

What “good” looks like:
- lineage is navigable in **both directions** (inputs → activity → outputs)
- results include **PROV identifiers** and/or pointers to PROV JSON artifacts
- safe to show in UI (redaction aware)

---

### 🧠 4) Focus Mode retrieval helpers
Focus Mode typically needs **tight**, **evidence-rich**, **UI-aware** bundles:
- prioritize the user’s map extent/timeframe
- return short text snippets + IDs for deeper fetch
- return citations/provenance hooks so the model can’t “freewheel”

💡 Template ideas:
- `kfm.focus.entity_disambiguation.v1` (e.g., “Jordan” place vs person)
- `kfm.focus.event_summary_sources.v1`
- `kfm.focus.story_node_evidence_bundle.v1`

---

### 📖 5) Story Nodes & Narrative Graph
KFM supports narrative layers (“Story Nodes”) that link:
- datasets
- places
- documents
- time periods
- curated explanations

Graph templates here should support:
- listing story nodes relevant to a place/time
- enumerating the evidence bundle a story node references
- linking “Pulse Threads” / “Conceptual Attention Nodes” (advanced ideas)

💡 Template ideas:
- `kfm.story.nodes_by_place_time.v1`
- `kfm.story.node_evidence_manifest.v1`
- `kfm.pulse.thread_snapshot.v1`
- `kfm.concept.node_neighbors.v1`

---

### 🧪 6) QA & Graph Health Checks
Automated graph integrity checks act like CI for data reliability.

💡 Template ideas:
- `qa.orphan_nodes.v1`
- `qa.top_degree_nodes.v1`
- `qa.schema_drift_sample.v1`
- `qa.backup_verification_metadata.v1`

**Cypher example (top-degree nodes):**
```cypher
// qa.top_degree_nodes.v1.cypher
MATCH (n)
WITH n, size((n)--()) AS degree
ORDER BY degree DESC
RETURN labels(n) AS labels, n.id AS id, degree
LIMIT $top_n;
```

Expected outputs from these checks should be saved into a timestamped folder, e.g.:
- `docs/reports/qa/graph_health/<YYYY-MM-DD>/`
  - `summary.md`
  - `metrics.csv`
  - `orphans.csv`
  - `top_degree.csv`

---

## 🧪 How these templates get executed

These templates are designed to be executed by:

1) **API resolvers / service layer**  
   - GraphQL resolvers or REST controllers load a template by ID  
   - Apply policy gates (role, classification, rate limits)  
   - Execute with Neo4j driver (or through a repository abstraction)  
   - Return stable JSON shape to UI / Focus Mode

2) **MCP experiments**  
   - Researchers run templates against snapshots of the graph  
   - Store results + interpretations as **experiment reports**  
   - Keep inputs, params, and outputs reproducible (commit SHA + run manifest)

3) **CI / Nightly QA jobs**  
   - Run health check templates  
   - Persist artifacts for trending + audit history  
   - Escalate failures into issues if thresholds are exceeded

---

## 🔐 Governance, safety, and redaction

### ✅ Always parameterize
- Use `$param` (Cypher) or GraphQL variables — never concatenate user input.

### ✅ Return provenance hooks by default
Where applicable, include:
- dataset IDs
- DCAT/STAC/PROV references
- source URLs and licenses (if safe)

### ✅ Respect role-based access & classification
Every template should declare:
- `min_role`
- `classification_max`
- whether it can return sensitive fields

### ✅ Auditability & inference control
Even non-sensitive graphs can leak sensitive info through aggregation or repeated querying.  
Adopt guardrails:
- request logging (template ID + params + role)
- rate limits / quotas
- “max_hops” / “max_depth” / “max_limit”
- caching where safe (reduces repeated probing)
- redaction filters enforced in the API, not UI

> [!TIP]  
> If you’re adding a template that can be used with natural language (“ask anything”), treat it as **high risk** and keep it **strictly whitelisted**.

---

## ⚡ Performance & correctness checklist

### Limits & pagination 🧯
- [ ] default `limit` and hard `max`
- [ ] pagination strategy (`offset`/`cursor`) is declared
- [ ] avoid returning huge nested trees (cap depth)

### Index-awareness 🧠
- [ ] match starting nodes by indexed keys (e.g., `Place.id`, `Dataset.id`)
- [ ] avoid scanning entire graph unless it’s a QA template

### Use the right store 🧭
- ✅ Neo4j: relationships, context, lineage, discovery
- ✅ PostGIS: bbox filters, counts, distances, geometry transforms, tiles
- ❌ Don’t ship geometry blobs out of Neo4j

### Stable output contracts 🧱
- [ ] JSON keys are stable (no ad hoc reshaping)
- [ ] version bump on breaking change
- [ ] schema reference exists (or a documented “shape”)

---

## 🧭 Federation readiness

KFM is designed to generalize beyond Kansas (multi-region deployments / federation).  
To keep templates portable:

- **Namespace your IDs** (e.g., `kfm.<region>.<domain>...`)
- **Avoid Kansas-specific assumptions** in query logic when possible
- Prefer **ontology-aligned labels/relationships** (CIDOC-CRM / OWL-Time / GeoSPARQL style mappings)
- Keep query templates **versioned** and compatible (migrations are explicit)

---

## 🧰 Adding a new template

1) **Pick the pack** (discovery, place, lineage, story, QA, federation) 📦  
2) Create files:
   - `cypher/<id>.cypher` *or* `graphql/<id>.graphql`
   - `manifests/<id>.yaml`
   - `schemas/<shape>.json` (recommended)
3) Add the template to `index.yaml` 🧭  
4) Add tests:
   - fixtures (small)
   - snapshot expected output shape
5) If the template is used by Focus Mode:
   - ensure it returns evidence hooks
   - keep result size bounded
   - confirm it can’t be used to bypass redaction

> [!NOTE]  
> If you need new node labels / relationship types, that’s a **graph schema change** → treat it as a migration + versioned contract update (not “just a query tweak”).

---

## 📎 Project docs & reference packs used

These templates are aligned with (and informed by) the project’s design docs & reference packs:

### Core KFM platform docs 🧭
- 📄 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- 🧱 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design**
- 🤖 **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖**
- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview**
- 📚 **Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide**
- 🌟 **Kansas Frontier Matrix – Latest Ideas & Future Proposals**
- 💡 **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)**
- 🧠 **Additional Project Ideas**

### Method + documentation standards 📓
- 📘 **Master Coder Protocol / Scientific Method documentation**
- 🧾 **KFM Markdown Guide / Master Guide (contracts, invariants, versioning)**

### Reference packs (PDF portfolios / libraries) 📦
- 🤖 **AI Concepts & more** (AI/RAG/LLM/NLP references)
- 🗺️ **Maps / Google Maps / Virtual Worlds / Archaeological CG / Geospatial WebGL** (visualization + mapping references)
- 🧠 **Data Management / Theories / Architectures / Bayesian Methods** (data systems + governance references)
- 🧰 **Various programming languages & resources** (language/tool references)

---

🧭 **If you’re here for “what query should I write?”** start with:
- `kfm.graph.place_context.v1` (place/time → events/docs/datasets)
- `kfm.graph.dataset_lineage.v1` (lineage and provenance)
- `qa.top_degree_nodes.v1` (health check)
- then extend with a new template following the manifest contract ✍️

