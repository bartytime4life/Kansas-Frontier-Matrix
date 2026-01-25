# 🕸️ Graph Request Examples (KFM)

![Contract First](https://img.shields.io/badge/contracts-contract--first-blueviolet)
![Provenance First](https://img.shields.io/badge/publishing-provenance--first-success)
![API](https://img.shields.io/badge/API-REST%20%2B%20GraphQL-informational)
![Graph](https://img.shields.io/badge/graph-Neo4j-018bff)
![Spatial](https://img.shields.io/badge/spatial-PostGIS-2E7D32)
![Backend](https://img.shields.io/badge/backend-FastAPI-009688)

> 📌 Copy/paste-ready request examples for traversing the **Kansas Frontier Matrix (KFM)** knowledge graph and graph-adjacent services.  
> Built for **UI integration**, **contract tests**, and **developer sanity checks**. ✅

---

## 📚 Table of Contents

- [🎯 What lives in this folder](#-what-lives-in-this-folder)
- [🧠 Mental model: “evidence → graph → API → UI”](#-mental-model-evidence--graph--api--ui)
- [📦 Suggested layout (contract-friendly)](#-suggested-layout-contract-friendly)
- [🚀 Quickstart (run requests)](#-quickstart-run-requests)
  - [GraphQL](#graphql)
  - [REST](#rest)
- [🧩 GraphQL request patterns](#-graphql-request-patterns)
- [🧪 Example cookbook](#-example-cookbook)
  - [001 — Person → Events → Places](#001--person--events--places)
  - [002 — Dataset card (STAC assets + lineage)](#002--dataset-card-stac-assets--lineage)
  - [010 — Place → Datasets (REST)](#010--place--datasets-rest)
  - [011 — Dataset metadata / data access (REST)](#011--dataset-metadata--data-access-rest)
  - [020 — Provenance trail (conceptual)](#020--provenance-trail-conceptual)
  - [030 — Focus Mode (graph-backed Q&A)](#030--focus-mode-graph-backed-qa)
  - [040 — Real-time graph-adjacent feeds (optional)](#040--real-time-graph-adjacent-feeds-optional)
- [🔒 Guardrails (policy + performance)](#-guardrails-policy--performance)
- [🧰 How to add a new example](#-how-to-add-a-new-example)
- [🧭 Related project docs (high-signal)](#-related-project-docs-high-signal)

---

## 🎯 What lives in this folder

This folder is for **request examples** that interact with KFM’s **graph layer** (and graph-driven endpoints):

- 🧬 **GraphQL** requests for multi-hop traversal (Person → Event → Place, Dataset → Lineage, etc.)
- 🗺️ **Graph-centric REST** endpoints (e.g., “datasets linked to a place”)
- 🤖 **Graph-backed Q&A** requests (Focus Mode) where the graph helps decide *which* evidence to fetch

The goal is to keep **living examples** that are:
- ✅ easy to run (curl / VS Code REST Client / Postman)
- ✅ stable enough to be used in CI as “contract vectors”
- ✅ aligned with KFM’s “**map behind the map**” philosophy (provenance + traceability)

---

## 🧠 Mental model: “evidence → graph → API → UI”

KFM treats publishable data as **evidence** with strong metadata:

- **STAC** for geospatial assets & observations 🛰️  
- **DCAT** for dataset-level catalog metadata 🗂️  
- **PROV** for lineage (inputs + processing + outputs) 🧾  

That evidence becomes nodes/edges in a **Neo4j knowledge graph**, while spatial features and queries live in **PostGIS**. The **API layer** (REST + GraphQL) is the *only* supported access path for UI and automation.

> [!NOTE]
> Many deployments put the API under `/api` (e.g., `/api/datasets`, `/api/focus`).  
> Some graph endpoints may be exposed without `/api` depending on routing—treat this README as a contract-oriented guide, and configure your base paths via env vars below.

---

## 📦 Suggested layout (contract-friendly)

If you’re expanding this directory, keep examples organized and testable:

```text
api/contracts/examples/requests/graph/
├── 📄 README.md                       # 📘 Graph request examples: how to run, auth headers, and expected response shapes
├── 🧬 graphql/                        # GraphQL operations (queries + variables) used by docs/tests/persisted queries
│   ├── 🧬📄 001_person_by_name.graphql         # Query: resolve a Person by name (search/lookup pattern)
│   ├── 🧾 001_person_by_name.variables.json   # Variables for 001 (input parameters)
│   ├── 🧬📄 002_dataset_card.graphql           # Query: dataset “card” summary (UI-friendly fields)
│   ├── 🧾 002_dataset_card.variables.json     # Variables for 002 (dataset_id, options)
│   ├── 🧬📄 020_provenance_trail.graphql       # Query: provenance trail for an entity/dataset/run (lineage view)
│   └── ➕ …                                    # Additional operations (numbered; keep stable for regression tests)
└── 🌐 rest/                           # REST request examples for graph-backed endpoints (raw HTTP)
    ├── 🗺️📥 010_place_datasets.http    # REST: datasets relevant to a place (graph-backed context)
    ├── 🗂️📥 011_dataset_metadata.http  # REST: dataset metadata (graph-enriched fields)
    ├── 🔎📥 030_focus_mode.http        # REST: Focus Mode via graph context (retrieval + citations required)
    └── ➕ …                            # Additional REST examples (numbered; include auth + paging headers)
```

**Why this split?**
- `.graphql` + `.variables.json` stays environment-agnostic ✅
- `.http` works great with VS Code “REST Client” and doubles as documentation ✅

---

## 🚀 Quickstart (run requests)

### GraphQL

Set your base + endpoint:

```bash
export KFM_API_BASE="http://localhost:8000"
export KFM_GRAPHQL_PATH="/graphql"    # or "/api/graphql" depending on your router
export KFM_GRAPHQL_ENDPOINT="${KFM_API_BASE}${KFM_GRAPHQL_PATH}"
```

Run a GraphQL request using an inline JSON payload:

```bash
curl -sS "$KFM_GRAPHQL_ENDPOINT" \
  -H "content-type: application/json" \
  -d '{"query":"{ __typename }"}'
```

> [!TIP]
> For real work: prefer named operations + variables (examples below).  
> It’s more cache-friendly, safer, and easier to diff in contract tests.

---

### REST

Set base path:

```bash
export KFM_API_BASE="http://localhost:8000"
```

Example:

```bash
curl -sS "${KFM_API_BASE}/api/datasets" | head
```

---

## 🧩 GraphQL request patterns

Use these patterns to keep graph queries safe, fast, and contract-stable:

- ✅ **Always use variables** (no string interpolation in queries)
- ✅ **Request only what you need** (UI components should keep payloads small)
- ✅ **Bound list fields** (pagination, limits, shallow nesting)
- ✅ **Prefer IDs** for joins (especially when linking graph nodes ↔ PostGIS features)
- ✅ **Assume guardrails** (depth limits, result-size limits, pagination requirements)

> [!WARNING]
> GraphQL can be abused with deep recursion / huge fanout.  
> Treat these examples as **“safe-by-default”** templates.

---

## 🧪 Example cookbook

### 001 — Person → Events → Places

Use case: *Build a person profile page or story sidebar (Person → related Events → Places).*

#### GraphQL query

```graphql
query PersonByName($name: String!) {
  person(name: $name) {
    id
    name
    events {
      id
      title
      date
      locations {
        id
        name
      }
    }
  }
}
```

#### Variables

```json
{
  "name": "John Brown"
}
```

#### curl runner

```bash
curl -sS "$KFM_GRAPHQL_ENDPOINT" \
  -H "content-type: application/json" \
  -d @- <<'JSON'
{
  "query": "query PersonByName($name: String!) { person(name: $name) { id name events { id title date locations { id name } } } }",
  "variables": { "name": "John Brown" }
}
JSON
```

---

### 002 — Dataset card (STAC assets + lineage)

Use case: *Dataset detail panel (metadata + assets + “derived from” lineage).*

#### GraphQL query

```graphql
query DatasetCard($id: ID!) {
  dataset(id: $id) {
    id
    title
    description

    # STAC-style asset inventory (COGs, PDFs, GeoJSON, tiles, etc.)
    stac {
      assets {
        key
        href
        type
        roles
      }
    }

    # Minimal lineage (keep it shallow to avoid fanout)
    relations {
      derivedFrom {
        id
        title
      }
    }
  }
}
```

#### Variables

```json
{
  "id": "kfm.ks.landcover.2020"
}
```

> [!TIP]
> For UI “cards”, keep lineage to 1 hop by default.  
> Provide an “Expand lineage” UX that fetches more on demand.

---

### 010 — Place → Datasets (REST)

Use case: *User clicks a county/place → show relevant datasets (catalog filtered by place link).*

#### REST request (VS Code REST Client style)

```http
### Place → datasets
GET {{KFM_API_BASE}}/graph/places/{{placeId}}/datasets
Accept: application/json
```

Example variables:

```text
KFM_API_BASE = http://localhost:8000
placeId      = kfm.place.ks.douglas_county
```

> [!NOTE]
> Some deployments may expose this as `/api/graph/places/...` instead.  
> Keep your `.http` files using `{{KFM_API_BASE}}` so the same request runs in any environment.

---

### 011 — Dataset metadata / data access (REST)

Use case: *Fetch DCAT-level metadata quickly; then fetch actual data as authorized.*

```http
### Dataset metadata (DCAT + distributions)
GET {{KFM_API_BASE}}/datasets/{{datasetId}}
Accept: application/json

### Dataset data (may require auth, may stream, may return signed URL)
GET {{KFM_API_BASE}}/datasets/{{datasetId}}/data
Accept: application/octet-stream
```

Example variables:

```text
datasetId = kfm.ks.landcover.2020
```

> [!WARNING]
> `/data` may be gated by license, sensitivity classification, auth role, or rate limits.  
> Expect “fail closed” behavior when policy gates are triggered.

---

### 020 — Provenance trail (conceptual)

Use case: *Show a “Lineage” panel for a dataset, including PROV activities and inputs.*

Because schemas differ across iterations, treat this as a **shape template**:

```graphql
query ProvenanceTrail($datasetId: ID!) {
  dataset(id: $datasetId) {
    id
    title

    prov {
      generatedBy {
        id
        type
        startedAt
        endedAt
        wasAssociatedWith {
          id
          name
        }
        used {
          id
          title
        }
      }
    }
  }
}
```

> [!TIP]
> If you adopt “dev provenance” (PRs/commits as PROV), this same pattern can trace:
> dataset → pipeline run → code version → PR/reviewers ✅

---

### 030 — Focus Mode (graph-backed Q&A)

Use case: *Ask a question with spatial/temporal context; API uses graph + PostGIS + catalogs to respond with citations.*

```http
### Focus Mode (Q&A)
POST {{KFM_API_BASE}}/api/focus
Content-Type: application/json
Accept: application/json

{
  "question": "What happened in Seward County in the 1930s?",
  "context": {
    "placeId": "kfm.place.ks.seward_county",
    "time": { "start": "1930-01-01", "end": "1939-12-31" }
  }
}
```

Expected **response shape** (example):

```json
{
  "answer": "…",
  "citations": [
    { "sourceId": "kfm.dataset.pdsi.1895_2000", "locator": "…" }
  ],
  "subgraph": {
    "nodes": [{ "id": "…", "type": "Event" }],
    "edges": [{ "from": "…", "to": "…", "rel": "AFFECTS" }]
  }
}
```

> [!NOTE]
> Internally, Focus Mode may use GraphQL (or graph-specific services) to fetch a **relevant subgraph** and then pull the evidence needed to answer.

---

### 040 — Real-time graph-adjacent feeds (optional)

Use case: *Graph helps locate the correct station/vehicle feed; PostGIS serves the latest points efficiently.*

Example (transit):

```http
### Transit vehicles since timestamp (example pattern)
GET {{KFM_API_BASE}}/api/transport/buses?since={{since}}
Accept: application/json
```

Example values:

```text
since = 2026-01-24T12:00:00Z
```

> [!TIP]
> If you store each observation as a STAC item and link it into the graph,
> you can keep **live layers** provenance-safe without changing the core model.

---

## 🔒 Guardrails (policy + performance)

KFM’s graph-access philosophy is:

- 🧱 **API-only access** (UI never runs raw Cypher / direct DB queries)
- 🧾 **Provenance-first publishing** (no “mystery nodes” used by UI)
- ✅ **Policy gates** at ingestion + inference + publication (schema, STAC/DCAT/PROV completeness, license presence, sensitivity classification, and citation requirements)
- 🛡️ **GraphQL safety** (depth/result-size limits + required pagination)

Quick checklist when you add/modify examples:

- [ ] Does the request stay bounded (limits/pagination, shallow nesting)?
- [ ] Does it avoid sensitive attributes unless explicitly authorized?
- [ ] Does it request provenance/citations when presenting “answers” to humans?
- [ ] Could it be used as a CI contract test vector (stable shape)?

---

## 🧰 How to add a new example

1. **Pick a number + slug**  
   - `050_storynode_playback.graphql`  
   - `050_storynode_playback.variables.json`

2. **Keep it UI-shaped**  
   Prefer “card-sized” payloads that map to a component (sidebar, modal, panel).

3. **Add a runner-friendly variant**  
   - GraphQL: query + variables  
   - REST: `.http` file with `{{KFM_API_BASE}}`

4. **(Optional but recommended) add an expected shape**  
   - `050_storynode_playback.expected.json` (snapshot / schema-driven)

5. **Update this README** with a short “use case” + one command to run it ✅

---

## 🧭 Related project docs (high-signal)

If you’re editing graph contracts, these docs are the closest “north star”:

- 📚 Data Intake – Technical & Design Guide (evidence triplet, ingestion, API examples)
- 🧭 AI System Overview (Focus Mode, explainability, citations)
- 🧩 UI System Overview (“map behind the map”, REST/GraphQL integration)
- 🏗️ Architecture / Blueprint docs (policy gates, governance, scaling)
- 💡 Latest Ideas & Future Proposals (dev provenance, real-time feeds, long-horizon roadmap)

---

_That’s it — keep examples small, safe, and provenance-rich._ 🌾🧠🗺️
