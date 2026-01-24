# 🧬 KFM GraphQL Types (Contracts)

![Contract-First](https://img.shields.io/badge/contract--first-✅-blue)
![Provenance](https://img.shields.io/badge/provenance--first-🧾-success)
![Governance](https://img.shields.io/badge/governance-OPA%2FConftest-orange)
![GraphQL](https://img.shields.io/badge/graphql-types-ff69b4)

Welcome to the **canonical GraphQL type system** for Kansas Frontier Matrix (KFM) — the contract that lets the UI, Focus Mode, and external clients query *connected* geospatial + historical knowledge safely and efficiently. KFM exposes a GraphQL endpoint specifically because it’s great at relationship-heavy queries across the knowledge graph.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✨ Why this folder exists

KFM’s UI is intentionally **decoupled** from the backend through **REST + GraphQL endpoints** so the interface can evolve without rewriting core data logic.  [oai_citation:1‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
This folder is the **schema contract surface** for that GraphQL lane (especially the “graph traversal” use-cases).  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

> **Design intent:** GraphQL types should feel like a “map of meaning” — clear, stable, provenance-aware, and policy-safe. ✅

---

## 🧭 Quick map

- **Core entities** (Person, Place, Event, Dataset, …) mirror the semantic graph domain.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Resolvers** translate graph requests into Neo4j and/or Postgres/PostGIS queries.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Safety**: guard against expensive queries (depth/size limits + pagination).  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Governance**: enforce schema validation, STAC/DCAT/PROV completeness, license presence, sensitivity labeling, provenance completeness, and citation requirements for AI outputs.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 📁 Folder layout (suggested)

> The goal is “one obvious place” for each kind of type. Keep it boring and consistent. 😌

```text
api/contracts/graphql/
  ├─ schema.graphql                  # 🧩 root schema (Query/Mutation + imports)
  ├─ types/                           # 🧬 you are here
  │  ├─ README.md
  │  ├─ scalars/                      # 🧪 custom scalars (GeoJSON, DateTime, JSON…)
  │  ├─ enums/                        # 🏷️ enums (SensitivityLevel, SortDirection…)
  │  ├─ core/                         # 🧱 domain objects (Person, Place, Dataset…)
  │  ├─ inputs/                       # 🎛️ filters, sorts, creation inputs
  │  ├─ connections/                  # 🔗 Relay-style Connection / Edge patterns
  │  ├─ payloads/                     # 📦 mutation payloads / result unions
  │  └─ shared/                       # 🧷 shared fragments (Provenance, Citation…)
  └─ README.md                        # 📘 GraphQL overview (optional)
```

---

## 🧱 Contract principles (non‑negotiables)

### 1) Contract-first & version-safe
- Treat the GraphQL schema as a **public contract artifact** (alongside OpenAPI).  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **Breaking changes require versioning** (new path/version or negotiation strategy).  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

✅ Rules of thumb:
- New fields: **additive** and typically **nullable**.
- Never rename/remove types or fields without a planned migration window.
- Deprecate before removing.

### 2) Provenance-first (the “map behind the map”)
KFM’s pipeline expects datasets to publish **boundary artifacts** (STAC + DCAT + PROV) and treat them as the interface between stages (catalog → graph → API → UI).  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
GraphQL types should surface this, not bury it.

**Every relevant “thing” should have:**
- Stable `id`
- `provenance` link(s) or `citations` link(s)
- Optional `license` / `source` summary (if applicable)

### 3) Governance-first (fail closed 🔒)
KFM uses policy gates (CI + runtime) to ensure schema validity, provenance, sensitivity handling, and citation rules are enforced.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
There’s an explicit intent to encode these rules using **OPA + Conftest** policies.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 4) Query safety (performance + abuse resistance)
GraphQL is powerful, so we must guard it:
- **Pagination for lists**
- **Depth / complexity limits**
- **Max page sizes**

KFM explicitly calls out guarding against “extremely expensive queries” via limits and pagination.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧪 Type families (what belongs where)

### 🧱 Core domain (`core/`)
The schema commonly includes types like `Person`, `Place`, `Event`, `Dataset`, etc.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
Suggested (KFM-aligned) expansions:

- `StoryNode` — narrative content paired with map/timeline behavior (often Markdown + JSON configs).  [oai_citation:14‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- `PulseThread` — geotagged, timely narrative updates stored as a graph node (e.g., `:PulseThread`) with evidence manifests.  [oai_citation:15‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- `Concept` — “Conceptual Attention Nodes” used as thematic hubs to guide AI/UI exploration.  [oai_citation:16‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### 🎛️ Inputs (`inputs/`)
- `FilterInput` (time, bbox, text query, concept tags)
- `SortInput`
- `PaginationInput` (cursor-based preferred)

### 🔗 Connections (`connections/`)
Use Relay-style patterns for *any* potentially large relationship list:
- `XConnection { edges, nodes, pageInfo, totalCount? }`
- `XEdge { node, cursor }`

### 🧪 Scalars (`scalars/`)
Common custom scalars for KFM:
- `DateTime` — timeline / temporal navigation
- `GeoJSON` — geometries and features
- `BBox` — spatial queries
- `URI` / `URL`
- `JSON` — safe structured payloads
- `Markdown` — narrative content (Story Nodes, etc.)

> Note: KFM’s backend uses PostGIS for spatial data and Neo4j for semantic graph queries, so types should represent geo/time in ways those stores can serve efficiently.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🏷️ Enums (`enums/`)
Must include governance-related enums:
- `SensitivityLevel` (or similar)
- `AccessTier` / `Visibility`
- `SortDirection`

KFM’s governance explicitly requires **sensitivity classification** and proper handling.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧾 Provenance & citations in the schema

### Provenance triplet (recommended shape)
KFM publishes STAC/DCAT/PROV as required “boundary artifacts.”  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
A clean GraphQL pattern is to make this explicit:

- `Dataset { stac, dcat, prov, distributions }`
- `Provenance { provRef, inputs, activities, agents }`
- `Citation { label, href, sourceId }`

### AI outputs MUST be cited
Focus Mode is designed to **always cite sources**; if it can’t, it should refuse or state uncertainty.  [oai_citation:20‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
Additionally, governance gates require citations for AI outputs (policy violation otherwise).  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

✅ Schema implication:
- Any `FocusAnswer` type should include `citations: [Citation!]!` and `provenance: Provenance!`

---

## 🔐 Sensitivity, redaction, and “don’t leak data”

KFM aims to support **tiered access and sensitivity-aware handling**, including geo-obfuscation for sensitive locations.  [oai_citation:22‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
Example strategy described in research-inspired patterns: **rounding/obfuscating location coordinates** for sensitive records so users see presence without precise coordinates.  [oai_citation:23‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

✅ Schema patterns that help:
- `Location { point, pointGeneralized, precisionMeters, redactionReason? }`
- `geometry` fields gated by `SensitivityLevel` + user role
- Add `governanceFlags: [GovernanceFlag!]!` on types that may be restricted

---

## 🧯 Pagination & query guards (recommended contract)

Because GraphQL can explode in cost, enforce **standard knobs**:

- Lists **must** be paginated (prefer cursor pagination)
- Default `first` (e.g., 25), max `first` (e.g., 100)
- Max depth / max complexity at the server layer
- No unbounded recursive graph traversals

This aligns with KFM’s explicit need for pagination and depth/result-size limits.  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧩 Example queries (contract sanity checks)

### 1) Relationship traversal (Person → Events → Locations)
This mirrors KFM’s “why GraphQL” example.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

```graphql
{
  person(name: "John Brown") {
    name
    events(first: 25) {
      nodes {
        title
        date
        locations(first: 10) { nodes { name } }
      }
      pageInfo { hasNextPage endCursor }
    }
  }
}
```

### 2) Dataset with catalog + lineage hints
KFM explicitly describes queries that return dataset metadata and relationships like `derivedFrom`.  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

```graphql
{
  dataset(id: "kfm.ks.landcover.2020") {
    title
    description
    stac { assets { href } }
    relations {
      derivedFrom { id }
    }
  }
}
```

---

## 🧰 Adding or changing a type (checklist)

### ✅ Add a new type
1. **Create SDL**: `core/<Thing>.graphql` (or the appropriate folder).
2. **Wire references** in `schema.graphql` (or your schema builder’s import list).
3. **Add provenance hooks** (citations + PROV references) if the type represents knowledge, narrative, or derived data.  [oai_citation:27‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
4. **Add policy expectations**:
   - sensitivity classification paths  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
   - AI outputs must be labeled + cited (if applicable)  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
5. **Add contract tests** (schema snapshot + query fixtures).  [oai_citation:30‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

### ✅ Modify an existing type
- Add fields, don’t break fields.
- Use `@deprecated(reason: "...")` before removals.
- If you must break: version the API surface.  [oai_citation:31‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

---

## 🧠 Future-ready: schema hooks for “what’s next”

KFM’s roadmap includes AR and hybrid 2D/3D storytelling experiences that could be powered by the *same* data services.  [oai_citation:32‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
This suggests new type families over time:

- `Scene` / `Overlay` / `ARAnchor`
- `SimulationRun` / `Scenario` / `Forecast`
- `DigitalTwinSlice(time: DateTime!, bbox: BBox!)`

Similarly, future “natural language query” copilots should remain evidence-based and cite sources.  [oai_citation:33‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 📚 Glossary (tiny but mighty)

- **STAC/DCAT/PROV**: required catalog + provenance boundary artifacts for published datasets.  [oai_citation:34‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **PulseThread**: geotagged, versioned narrative update stored as a graph node with evidence manifest.  [oai_citation:35‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Conceptual Attention Node**: concept hub type that links datasets/events/stories and guides AI/UI attention.  [oai_citation:36‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

---

## ✅ “Definition of Done” for GraphQL types

Before merging changes in `api/contracts/graphql/types/`:

- [ ] Schema compiles (SDL) and passes contract tests  [oai_citation:37‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] New lists are paginated and query-safe  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Provenance fields exist where appropriate  [oai_citation:39‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Sensitivity/redaction behavior is representable in the contract  [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] AI-facing outputs include citations or refuse  [oai_citation:41‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] No breaking changes without versioning plan  [oai_citation:42‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

🧭 **North Star:** GraphQL types are not just “API shapes” — they are the *governed language* of KFM’s knowledge, grounded in evidence and safe to share.
