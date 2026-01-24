# 🧬 GraphQL Operations (Contracts) 🗺️✨

![contract](https://img.shields.io/badge/contract-graphql-blue)
![kfm](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-6f42c1)
![evidence-first](https://img.shields.io/badge/principle-evidence--first-0aa)
![FAIR+CARE](https://img.shields.io/badge/governance-FAIR%2BCARE-success)

📍 **Path:** `api/contracts/graphql/operations/`  
🎯 **Purpose:** A **single source of truth** for **approved** GraphQL operations (queries/mutations/subscriptions) used by KFM clients (UI, AI/Focus Mode, automation).

> [!NOTE]
> KFM uses GraphQL specifically for **semantic / relationship-heavy queries** over the knowledge graph (Person ↔ Event ↔ Place ↔ Dataset, etc.). GraphQL operations here should reflect that strength and stay **evidence-first**.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🔗 Quick Links

- [What lives here](#-what-lives-here)
- [Golden rules](#-golden-rules)
- [Folder layout](#-folder-layout)
- [Operation conventions](#-operation-conventions)
- [Evidence & provenance selections](#-evidence--provenance-selections)
- [Templates](#-templates)
- [Governance, security & safety](#-governance-security--safety)
- [Federation readiness](#-federation-readiness)
- [Reference library](#-reference-library)

---

## 📦 What lives here

KFM provides **REST + GraphQL** access, with GraphQL optimized for **graph traversal** use cases (e.g., fetch a Person and all related events and locations in one request).  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Typical operation categories include:

- 🧬 **Knowledge Graph**: people, places, events, and their relationships (Neo4j-backed).
- 📚 **Catalog & Datasets**: dataset metadata + STAC/DCAT/PROV evidence surfaces (catalog-backed).
- 🧭 **Focus Mode**: “return a subgraph of relevant info given a question context” (AI retrieval pipeline).  [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🧾 **Story Nodes**: narrative tours, references, annotations (UI ↔ API flows).  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- 🧵 **Pulse Threads / Live Feeds**: region-tagged updates, alerts, change streams (optional/expanding).  [oai_citation:4‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧱 Golden rules

1) 🔐 **API is the governed gateway**  
All clients access data **through the API**; the UI must **not** bypass the API to hit databases directly.  [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

2) 🧾 **Evidence-first publishing**  
Published data in KFM is “official” only when the **evidence triplet** is present:  
- **DCAT** (`data/catalogs/`)  
- **STAC** (`data/stac/`)  
- **PROV** (`data/prov/`)  
…and everything is version-controlled and auditable.  [oai_citation:6‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

3) 🕵️‍♀️ **No mystery nodes**  
Nothing goes into the graph without provenance and catalog lineage; sensitive attributes must be flagged and respected at query time.  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

4) 🧭 **Provenance stays visible in UX**  
KFM’s UI philosophy is “the map behind the map” — every visualization is traceable to its source data/metadata, and AI answers include citations.  [oai_citation:8‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:9‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

5) 🧨 **Guard against expensive GraphQL**  
GraphQL resolvers must defend against deep recursion and giant result sets (depth limits + pagination).  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

6) 🧷 **Append-only mindset for streams**  
For real-time/streaming data, KFM favors append-only records with timestamps (no silent rewrites).  [oai_citation:11‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🗂 Folder layout

> [!TIP]
> If you’re still building out the directory tree, this is the recommended “contract-first” layout.

```text
api/
  contracts/
    graphql/
      schema/                    # (optional) schema.graphql + federation directives
      operations/
        queries/                 # ✅ read-only operations
        mutations/               # ✅ write operations (governed + auditable)
        subscriptions/           # ✅ real-time (optional)
        fragments/               # ♻️ shared selection sets (provenance, ids, etc.)
        README.md                # 👈 you are here
```

---

## 🧩 Operation conventions

### 1) Naming & file style 🏷️

- **Operation names**: `PascalCase` (GraphQL convention)
  - `GetDatasetEvidence`
  - `SearchDatasets`
  - `GetPersonTimeline`
- **File names**: `lower_case_with_underscores` (repo-wide convention)  
  Example dataset IDs follow the same “structured naming” spirit (e.g., `kfm.ks.landcover.2000_2020.v1`).  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

✅ Example mapping:

| Domain | Operation Name | File |
|---|---|---|
| Catalog | `GetDatasetEvidence` | `queries/get_dataset_evidence.graphql` |
| Graph | `GetPersonTimeline` | `queries/get_person_timeline.graphql` |
| Story | `CreateStoryNode` | `mutations/create_story_node.graphql` |

---

### 2) Variables over literals 🎛️

- Prefer `$variables` over embedding IDs/filters directly.
- This improves caching, re-use, and reduces accidental PII leakage via hard-coded literals.

---

### 3) Pagination, limits & safety rails 🧯

GraphQL is powerful, but KFM must stay fast and safe. Use schema-supported pagination patterns and enforce limits in resolvers.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Minimum expectations:**
- Every list field should be paginated (cursor/offset/etc.)
- Provide “light” variants for UI lists vs “deep” variants for detail panels
- Avoid multi-hop list expansions unless explicitly needed

---

### 4) Geospatial + large assets: return *links*, not blobs 🛰️

KFM stores large artifacts (rasters, PDFs, tilesets) in file storage/object storage and serves them via links/streams (including potential signed URLs). GraphQL operations should typically return **metadata + hrefs**, not massive payloads.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Also, PostGIS is used for “heavy lifting” geodata operations and efficient spatial querying; keep GraphQL focused on semantic joins and high-level retrieval.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### 5) Caching & real-time patterns ⚡

- Consider GraphQL query caching (or HTTP cache headers) for frequent queries.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Real-time can evolve via GraphQL subscriptions or WebSockets (especially for live layers).  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Streaming UI patterns may also use “rolling window” REST calls such as:
  `GET /api/transport/buses?since=<timestamp>` (conceptual example).  [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧾 Evidence & provenance selections

KFM’s contract philosophy expects operations to surface enough metadata to keep everything **traceable** (FAIR+CARE, licenses, provenance, etc.). Dataset contracts validate license/sensitivity fields, and provenance standards include STAC/DCAT/PROV.  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Recommended “minimum evidence” selection (Dataset)

When retrieving a dataset for UI detail panels or AI citations, include at least:

- `id`
- `title`
- `description`
- `stac { assets { href } }`
- lineage/relationships (`derivedFrom`, etc.)

Example shape is explicitly referenced in KFM intake docs:  [oai_citation:21‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

> [!TIP]
> Put this into a shared fragment if your schema supports it (`fragments/dataset_evidence.graphql`) so it’s hard to forget.

---

## 🧪 Templates

<details>
<summary>🧬 Query: Person → Events → Places (graph traversal)</summary>

```graphql
query GetPersonTimeline($name: String!) {
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

Why this exists: GraphQL is ideal for traversing Person → Event → Place relationships in one call.  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
</details>

<details>
<summary>📚 Query: Dataset evidence (STAC assets + lineage)</summary>

```graphql
query GetDatasetEvidence($id: ID!) {
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

This mirrors the documented “GraphQL could allow queries like …” example in the intake guide.  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
</details>

<details>
<summary>🧭 Query: Focus Mode context subgraph (conceptual contract)</summary>

```graphql
query GetFocusContext($question: String!, $mapContext: FocusMapContextInput) {
  focusContext(question: $question, mapContext: $mapContext) {
    nodes { id type label }
    edges { from to predicate }
    citations { datasetId stacHref provHref }
  }
}
```

KFM documents the idea that Focus Mode may use GraphQL “to return a subgraph of relevant info given a question context.”  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
</details>

<details>
<summary>🧵 Query: Pulse Threads (conceptual contract)</summary>

```graphql
query GetPulseThreads($regionId: ID!, $after: String, $first: Int = 20) {
  pulseThreads(regionId: $regionId, after: $after, first: $first) {
    pageInfo { endCursor hasNextPage }
    nodes {
      id
      title
      summary
      createdAt
      relatedPlaces { id name }
      relatedDatasets { id title }
      evidence { stacHref provHref }
    }
  }
}
```

Pulse Threads are proposed as geotagged, context-rich updates linked to places/datasets, with evidence tracking.  [oai_citation:25‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
</details>

---

## 🛡️ Governance, security & safety

### 🔐 API security expectations

KFM’s API is described as stateless and secured by design, with planned auth (OAuth2/token) and rate limiting/throttles.  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Operational implication for GraphQL contracts:
- Prefer operations that can be authorized cleanly (role scopes, dataset classification, sensitivity)
- Avoid “wildcard” operations that are hard to policy-check

---

### 🧾 Policy gates (CI) for contracts ✅

KFM governance is designed to be enforced in code via **policy gates** (Conftest + OPA/Rego), failing CI when rules are violated (license required, forbidden secrets, required metadata fields, etc.).  [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

✅ Recommended extensions for *this* folder:
- Enforce a **provenance selection** for dataset-facing operations
- Ban operations that request restricted fields without proper roles
- Enforce pagination arguments for list fields

---

### 🕵️ Query auditing & inference control 🧠

Even when raw data is protected, query outputs can leak sensitive information. Query auditing can deny queries that would disclose confidential data.  [oai_citation:28‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

✅ Practical GraphQL takeaways:
- Detect “difference attacks” by limiting repeated near-identical aggregation queries
- Deny (or coarsen) results when they risk disclosure (e.g., exact artifact coordinates)

---

### 🪶 Indigenous data sovereignty & cultural protocols (CARE-ready)

KFM’s evolution includes cultural protocol layers (e.g., Mukurtu/TK-style labels) and fine-grained access levels for sensitive Indigenous materials.  [oai_citation:29‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

✅ Contract implications:
- Include `classification` / `accessLevel` fields where appropriate
- Prefer “generalized location” fields for restricted data (with role-gated precise fields)
- Provide explicit provenance context to avoid misuse

---

### 🧾 Governance ledger & traceability (AI + retrieval)

KFM’s AI approach emphasizes traceability: results link back to sources, and graph queries are integrated into retrieval.  [oai_citation:30‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

> [!NOTE]
> The AI system also describes an “Immutable Governance Ledger” for logging sources and why results were returned.  [oai_citation:31‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

✅ Contract implication:
- Prefer operations that return **source handles** (dataset IDs + hrefs) so responses can be cited.

---

## 🌐 Federation readiness

KFM is designed to be reusable beyond Kansas (shared UI + standardized schemas), and federation may include **GraphQL schema stitching** or a global endpoint that queries multiple instances.  [oai_citation:32‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:33‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

✅ Federation-friendly operation tips:
- Avoid Kansas-specific naming in operation semantics (use `regionId`, not hard-coded “ks”)
- Keep IDs and filters consistent across regions
- Prefer stable contract shapes over “clever” one-off query structures

---

## 🧠 Bonus: DevOps provenance (future-facing)

One proposal is to generate PROV JSON-LD for GitHub PRs and ingest it into Neo4j so provenance is queryable (and CI invariants are enforceable). This can eventually surface in contracts as “where did this dataset come from in code history?”  [oai_citation:34‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 📚 Reference library

These project files informed this contract README (and should remain aligned as the schema evolves):

- 📘 KFM Data Intake – Technical & Design Guide  [oai_citation:35‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 💡 Innovative Concepts to Evolve KFM  [oai_citation:36‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 🧠 Additional Project Ideas  [oai_citation:37‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- 🧱 KFM Comprehensive Architecture, Features, and Design  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 🧭 KFM AI System Overview  [oai_citation:39‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 🖥️ KFM UI System Overview  [oai_citation:40‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 🧾 KFM Comprehensive Technical Documentation  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- 🔎 Data Mining Concepts & Applications (privacy / auditing patterns)  [oai_citation:42‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  
- 🧪 Latest Ideas & Future Proposals  [oai_citation:43‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- 🧰 Master Coder / Scientific Method Protocol  [oai_citation:44‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- 📝 Markdown Guide v13  [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 📚 AI Concepts & More (PDF portfolio)  [oai_citation:46‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- 🗺️ Maps/Geospatial/WebGL Portfolio  [oai_citation:47‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- 💾 Data Management Theories Portfolio  [oai_citation:48‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  
- 👩‍💻 Programming Languages & Resources Portfolio  [oai_citation:49‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  

---

## ✅ Contribution checklist (add a new operation)

- [ ] File created under the correct category folder (`queries/`, `mutations/`, etc.)
- [ ] Operation name is `PascalCase`; file is `lower_case_with_underscores`
- [ ] Uses variables (no hard-coded IDs)
- [ ] Lists are paginated and bounded
- [ ] Includes minimum provenance/evidence selections when returning datasets
- [ ] Passes schema validation + policy gates (OPA/Conftest)
- [ ] Includes a short doc comment at top explaining intent + sensitivity

🎉 That’s it — ship contracts that keep KFM fast, traceable, and trustworthy.
