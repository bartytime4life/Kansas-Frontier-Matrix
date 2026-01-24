# 🧬 GraphQL Examples — KFM API Contracts

![GraphQL](https://img.shields.io/badge/GraphQL-Examples-E10098?logo=graphql&logoColor=white)
![Contract First](https://img.shields.io/badge/Contract--First-Yes-2ea44f)
![Evidence Triplet](https://img.shields.io/badge/Evidence--First-STAC%20%2B%20DCAT%20%2B%20PROV-0ea5e9)
![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-8b5cf6)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)
![Neo4j](https://img.shields.io/badge/Graph-Neo4j-018bff?logo=neo4j&logoColor=white)
![PostGIS](https://img.shields.io/badge/Geospatial-PostGIS-336791?logo=postgresql&logoColor=white)

> [!IMPORTANT]
> **These operations are “living contract examples”** ✅  
> They exist to keep KFM’s GraphQL layer **predictable, testable, and evidence-first**. Every example should be runnable, paginated where relevant, and should surface provenance (STAC/DCAT/PROV) wherever the schema supports it.

---

## 📌 What this folder is

This directory is the home for **GraphQL request examples** that act as:

- 📜 **Documentation** for developers, UI clients, and external integrators
- 🧪 **Contract tests** (examples that can be executed in CI against a running API)
- 🧭 **Reference patterns** for graph traversal queries across **Person / Place / Event / Dataset** and related evidence artifacts

📁 You are here:

```
🗂️ api/
  🗂️ contracts/
    🗂️ examples/
      🗂️ graphql/
        📄 README.md  ← you are here
```

> [!NOTE]
> In the v13 architecture guidance, canonical API code + contract definitions may live under `src/server/…` (including OpenAPI + GraphQL SDL).  
> This `api/contracts/...` tree is treated as a **stable, tool-friendly contract surface** for examples and tests. If you reorganize, keep consumers in mind.

---

## 🧭 Where GraphQL fits in KFM

KFM uses **both REST and GraphQL** because they solve different problems well:

| Need | Prefer | Why |
|---|---|---|
| Traverse relationships (Person → Events → Places) | 🧬 GraphQL | One request can traverse the **knowledge graph** with precise field selection |
| Fetch heavy geospatial payloads (lots of geometries) | 🌍 REST (PostGIS-backed) | Better for caching/streaming; avoids overfetch; keeps GraphQL lean |
| Download assets (COGs / GeoParquet / PMTiles / docs) | 📦 REST | Stream-friendly and CDN-friendly; GraphQL returns references/IDs/URLs |
| Power UI exploration (map, timeline, story nodes) | 🤝 Both | GraphQL for relationship slices; REST for tiles/data subsets |

---

## ✨ Design principles these examples should reflect

### 1) 🧾 Contract-first
- Update the **GraphQL SDL** (schema) first.
- Then update/add **example operations** here.
- Treat examples as part of the contract: if the schema changes, examples must be updated.

### 2) 🧷 Evidence-first (STAC + DCAT + PROV)
KFM’s core publishing stance is that data is not “official” until the evidence triplet exists:

- 🛰️ **STAC** → assets & spatial/temporal indexing
- 📦 **DCAT** → dataset discovery + distributions/licensing
- 🧬 **PROV** → lineage, derivations, activities, agents

So examples should **prefer fields that keep the “map behind the map” visible** (IDs, lineage, and source metadata).

### 3) 🛡️ Policy-first
Examples should assume the API enforces:

- depth/complexity limits + pagination (avoid “infinite graph walks”)
- redaction/classification rules (especially for sensitive coordinates/attributes)
- FAIR+CARE governance expectations (licensing, attribution, community authority)

---

## 📦 Suggested structure (recommended)

You can keep examples tidy and testable by pairing queries with fixtures:

```
api/contracts/examples/graphql/
├─ README.md
├─ queries/
│  ├─ person__events_places.graphql
│  ├─ dataset__evidence_triplet.graphql
│  └─ ...
├─ mutations/
│  └─ ...
├─ fragments/
│  └─ ...
└─ fixtures/
   ├─ person__events_places.variables.json
   ├─ dataset__evidence_triplet.variables.json
   └─ ...
```

> [!TIP]
> If your CI supports it, add `*.expected.json` fixtures (or snapshots) so examples become **assertable contract tests**.

---

## 🚀 How to run an example (minimal)

### Option A — `curl` (works everywhere)

1) Set your endpoint (common defaults are shown; confirm for your deployment):

```bash
export KFM_GRAPHQL_URL="http://localhost:8000/graphql"
# or: export KFM_GRAPHQL_URL="http://localhost:8000/api/graphql"
```

2) Execute a named operation with variables:

```bash
curl -sS -X POST "$KFM_GRAPHQL_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query PersonByName($name: String!) { person(name: $name) { name events { title date locations { name } } } }",
    "variables": { "name": "John Brown" }
  }'
```

### Option B — GraphiQL / Playground (if enabled)
Paste the query + variables into your GraphQL UI, then run.  
(If it’s disabled in production, that’s normal—use it locally/dev only.)

---

## 🧱 Conventions for all examples

- ✅ **Always name** your operation (`query Name` / `mutation Name`)
- ✅ Prefer **variables** over hard-coded values (more reusable + testable)
- ✅ Use **pagination** on list fields if available (`first/after`, `limit/offset`, etc.)
- ✅ Keep responses **lightweight** (don’t pull full geometries unless necessary)
- 🌍 Geospatial defaults: prefer **GeoJSON** and WGS84/EPSG:4326 unless explicitly stated otherwise
- 🧾 Ask for provenance when meaningful: dataset IDs, lineage hooks, asset references

---

## 📚 Implemented example queries (grounded patterns)

> [!NOTE]
> The following examples align with patterns explicitly described across KFM documentation:  
> Graph traversal (Person→Event→Place) and dataset evidence retrieval (STAC assets + derivedFrom).

### 1) 👤 Person → Events → Places (single traversal)

**File (suggested):** `queries/person__events_places.graphql`

```graphql
query PersonByName($name: String!) {
  person(name: $name) {
    name
    events {
      title
      date
      locations {
        name
      }
    }
  }
}
```

**Variables (suggested):** `fixtures/person__events_places.variables.json`

```json
{
  "name": "John Brown"
}
```

**Why it matters:** one request replaces multiple REST calls for interconnected entities.

---

### 2) 📦 Dataset evidence slice (STAC assets + derivedFrom)

**File (suggested):** `queries/dataset__evidence_triplet.graphql`

```graphql
query DatasetEvidenceSlice($id: ID!) {
  dataset(id: $id) {
    title
    description
    stac {
      assets {
        href
      }
    }
    relations {
      derivedFrom {
        id
      }
    }
  }
}
```

**Variables (suggested):** `fixtures/dataset__evidence_triplet.variables.json`

```json
{
  "id": "kfm.ks.landcover.2020"
}
```

**Why it matters:** encourages **evidence-first consumption**—your client sees *what the dataset is* and *where to retrieve the assets*, plus *lineage*.

---

## 🧪 Draft / proposed examples (roadmap-aligned)

These are **intentionally marked as draft** because field names/types will depend on the evolving schema.  
They’re included here because multiple KFM documents describe these capabilities conceptually.

> [!WARNING]
> Treat these as **design targets**, not guaranteed schema.  
> If you implement them, convert them into runnable examples and remove “draft” labeling.

### A) 💬 Focus Mode “context subgraph” request
Goal: allow the AI layer (or UI) to fetch a **bounded subgraph** relevant to a question + viewport/timeframe.

Draft shape (illustrative):

```graphql
# query FocusContext($question: String!, $viewport: ViewportInput!, $time: TimeRangeInput) { ... }
```

**Design guardrails:**
- must enforce depth/size limits
- must return citations/provenance for any claims
- must obey governance screens (OPA/policy gates)

---

### B) 📍 Pulse Threads (geotagged micro-stories with citations)
Pulse Threads are described as **rapid insight dissemination** linked to Places/Regions, authored by humans or generated by watchers (with review) and kept FAIR+CARE aligned.

Draft shape (illustrative):

```graphql
# query PulseThreads($bbox: BBoxInput!, $since: DateTime!, $limit: Int) { ... }
```

**What to insist on in the contract:**
- geotag linkage (Place/Region IDs)
- explicit evidence/citation bundle
- author/reviewer + provenance edge(s)

---

### C) 🧾 “Which stories used this dataset?”
Story Nodes are intended to be queryable, provenance-connected narrative artifacts.

Draft shape (illustrative):

```graphql
# query StoriesUsingDataset($datasetId: ID!) { ... }
```

**Contract expectation:**
- Story Nodes should reference stable graph IDs for entities they mention
- evidence manifests should be machine-resolvable

---

## 🛡️ Security & performance expectations

GraphQL is powerful—so KFM assumes guardrails are present:

- 🧱 **Depth / complexity limits** to prevent runaway traversal
- 📏 **Result size caps** + mandatory pagination on lists where applicable
- 🚦 **Rate limiting** when exposed publicly
- 🧽 **Redaction/classification** at resolver level (especially for sensitive coordinates)
- 🧪 Policy-as-code checks (e.g., OPA/Conftest) applied to schemas and governance rules

> [!TIP]
> A good example query is not just “does it work?”—it demonstrates safe usage:
> bounded traversal + pagination + provenance.

---

## ✅ Adding a new example (Definition of Done)

When you add/modify an example:

- [ ] Operation is named + placed under the right folder (`queries/`, `mutations/`, etc.)
- [ ] Variables live in `fixtures/*.variables.json` (when applicable)
- [ ] The query is **bounded** (pagination / limits) and respects cost controls
- [ ] Provenance fields are requested where meaningful (STAC/DCAT/PROV hooks)
- [ ] If the schema changed, contract versioning + compatibility checks are updated
- [ ] If the example reflects a UI need, ensure it supports “map behind the map” transparency

---

## 🔗 Related references (recommended reading)

- 📘 System architecture & API overview
- 📥 Data intake & evidence-first publishing (STAC/DCAT/PROV)
- 🧠 Focus Mode / explainable AI guidance
- 🧭 UI overview (REST/GraphQL separation + provenance surfacing)
- 🧰 Governance + policy-as-code patterns (FAIR+CARE)

> Tip: keep this README link list updated as the repo structure stabilizes in v13.

---

## 🧯 Troubleshooting

### “Query too deep / too expensive”
- Reduce nesting depth
- Add pagination
- Request fewer fields
- Consider a REST endpoint for heavy payloads

### “Field not found”
- Your example is out of sync with the SDL  
  ✅ update the schema or update the example to match the contract version you’re targeting

### “Unauthorized / redacted”
- Expected for restricted datasets or sensitive attributes  
  ✅ do not “work around” redaction in GraphQL—fix policy and governance intentionally instead
