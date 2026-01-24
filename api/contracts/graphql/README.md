# GraphQL Contracts 🧬🌾

![Contract-first](https://img.shields.io/badge/contracts-first-0ea5e9?style=for-the-badge)
![Backwards compatible](https://img.shields.io/badge/backwards--compatible-required-22c55e?style=for-the-badge)
![Provenance-first](https://img.shields.io/badge/provenance-first-8b5cf6?style=for-the-badge)
![Open standards](https://img.shields.io/badge/open%20standards-GeoJSON%20%7C%20STAC%20%7C%20PROV%20%7C%20DCAT-f97316?style=for-the-badge)

> **You’re in** `api/contracts/graphql/` 📁  
> This folder is the **contract surface** for KFM’s GraphQL API: schema (SDL), rules, examples, and contract tests.  
> GraphQL exists in KFM to support *complex, knowledge-graph-style* questions (people/places/events/time) in a single request.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)

---

<details>
<summary>📚 Table of contents</summary>

- [Why GraphQL exists in KFM](#why-graphql-exists-in-kfm)
- [What “contract-first” means here](#what-contract-first-means-here)
- [Folder layout](#folder-layout)
- [Non-negotiables](#non-negotiables)
- [Schema design conventions](#schema-design-conventions)
  - [1) Naming](#1-naming)
  - [2) IDs](#2-ids)
  - [3) Pagination & “expensive query” safety](#3-pagination--expensive-query-safety)
  - [4) Geospatial & raster conventions](#4-geospatial--raster-conventions)
  - [5) Provenance & evidence](#5-provenance--evidence)
- [Contract tests & CI gates](#contract-tests--ci-gates)
- [Example queries](#example-queries)
- [How to change the schema safely](#how-to-change-the-schema-safely)
- [Design sources](#design-sources)

</details>

---

## Why GraphQL exists in KFM

KFM’s back-end is **API-centric** and standards-based (FastAPI + geospatial + knowledge graph). The platform supports REST (OpenAPI/Swagger) and also offers a **GraphQL endpoint** for more flexible, query-based retrieval.  [oai_citation:1‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3) [oai_citation:2‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

GraphQL is primarily for:
- **Knowledge graph navigation**: “find events related to person X and location Y between 1850 and 1900.”  
- **Fewer round trips**: fetch a node + connected subgraph in one request.  
- **Structured interoperability**: schema designed to mirror graph concepts (e.g., `Person`, `Place`, `Event`).  
   [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)

---

## What “contract-first” means here

KFM’s master guide is explicit: contracts (schemas/specs) are **first-class artifacts** and must be versioned + honored by implementations.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

For APIs specifically:
- We maintain **GraphQL schema + contract tests** as the boundary.  
- We stay **backwards-compatible** unless a **version bump** is declared.  
- Any contract change is validated against known inputs/outputs.  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> 🧠 Governance note: these contracts sit inside a larger set of “internal contracts” across the KFM pipeline, and breaking them triggers review/versioning behavior.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## Folder layout

> This is the **recommended contract layout** for GraphQL. If some files don’t exist yet, treat this README as the blueprint.

```text
api/
└─ 📜 contracts/
   └─ 🧬 graphql/
      ├─ ✅📄 README.md                 # 👈 you are here 📌 GraphQL contract overview: versioning, composition, and validation
      ├─ 🧬📄 schema.graphql            # Schema SDL (generated or hand-authored; source of truth for GraphQL surface)
      ├─ 🧪📄 scalars.graphql           # Custom scalars (DateTime, JSON, GeoJSON, BBox, etc.) + serialization notes
      ├─ 🧩📄 directives.graphql        # Directives (auth/policy/sensitive/deprecated) used for enforcement + evolution
      ├─ 🧾 types/                     # Optional split-by-domain SDL (keeps schema modular and reviewable)
      ├─ 🧾 operations/                # Query/mutation examples (used by docs/tests; helps prevent breaking changes)
      ├─ 🧩 fixtures/                  # Golden JSON fixtures for contract tests (expected responses, errors, edge cases)
      ├─ 📌 persisted/                 # Optional persisted-query manifests (ids/hashes → operations)
      ├─ 🧪 tests/                     # Schema/operation contract tests (lint, composition, breaking-change checks)
      └─ 🗞️📄 CHANGELOG.md             # Contract version notes (what changed, why, migration guidance)
```

📌 Repo context: KFM is organized into modular folders (e.g., `api/`, `web/`, `data/`, `pipelines/`, `tools/`, `notebooks/`) so each layer stays isolated and testable.  [oai_citation:8‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

---

## Non-negotiables

✅ **Backwards compatibility**  
- No breaking contract change without a declared version bump.  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

✅ **Schema is the truth (for clients)**  
- Client code should never depend on private resolver behavior; it depends on SDL.

✅ **Expensive query safety**  
- Pagination, limits, and/or query cost rules are required (KFM explicitly notes restricting expensive queries or requiring pagination).  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)

✅ **Provenance-first by design**  
- KFM’s UI philosophy is to expose context + provenance (“map behind the map”). The API must support this by returning provenance hooks in the graph.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)

✅ **Open standards, minimal friction**  
- When returning geospatial/raster/evidence data, prefer standard formats + metadata patterns (GeoJSON, COG, STAC, PROV-O JSON-LD, DCAT).  [oai_citation:12‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

---

## Schema design conventions

### 1) Naming

- **Types**: `PascalCase` (`Person`, `Place`, `Event`, `Dataset`, `Layer`)  
- **Fields**: `camelCase` (`displayName`, `timeRange`, `stacItem`)  
- **Enums**: `SCREAMING_SNAKE_CASE` (`DATASET_STATUS_PUBLISHED`)

### 2) IDs

- Every top-level graph node should have:
  - `id: ID!` (stable, opaque)  
  - `slug: String` (optional, human-friendly, not guaranteed stable)

> Why: GraphQL clients cache heavily; stable IDs reduce client breakage and make federation feasible.

### 3) Pagination & “expensive query” safety

KFM calls out that GraphQL may restrict expensive queries and/or require pagination for performance.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)

Rules:
- Any field that returns a list **must** have pagination (`first/after`, `limit/offset`, or a Connection pattern).
- Any field that can expand to a subgraph must:
  - be paginated, and/or  
  - enforce a query depth/cost limit (server-side).

Recommended pattern (Connection-ish):
- `edges { node cursor }`
- `pageInfo { hasNextPage endCursor }`

### 4) Geospatial & raster conventions

KFM publishes geospatial assets in standard forms:
- Vector data as **GeoJSON**  
- Raster data as **Cloud-Optimized GeoTIFF (COG)**  
- Metadata discovery via **STAC** and **DCAT**  
- Provenance via **PROV-O JSON-LD**  
 [oai_citation:14‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

GraphQL convention:
- **Don’t** embed massive geometries by default.
- **Do** provide:
  - lightweight derived geometry (`bbox`, `centroid`)  
  - a `geojsonUrl` or `tileUrl` reference  
  - a `stacItem` / `assets` pointer for canonical discovery  

### 5) Provenance & evidence

KFM is intentionally **provenance-forward**: UI and narratives must be traceable to sources, and the API is part of that trust chain.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS) [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Schema convention:
- Every major domain object should expose at least one of:
  - `sources: [SourceRef!]!`
  - `provenance: ProvenanceRef`
  - `stac: StacRef`
  - `license: LicenseRef`

Where `SourceRef` should be resolvable into:
- a STAC item / asset
- a DCAT dataset/distribution
- a PROV entity/activity graph

> ⚠️ If the schema can’t expose provenance, the UI can’t reliably “show the map behind the map.”

---

## Contract tests & CI gates

The master contract rule: **any contract change is tested** against known inputs/outputs.  [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Recommended gates for this folder:

### ✅ Gate A — Schema validity
- SDL parses
- No duplicate type names
- No invalid directives / scalars

### ✅ Gate B — Breaking change detection
- Diff current schema vs main branch schema
- Fail on removals/type changes (unless version bump declared)

### ✅ Gate C — Operation contract tests
- Run “golden” queries from `operations/`
- Assert:
  - shape of responses
  - required fields present
  - pagination works
  - permission boundaries respected

### ✅ Gate D — Policy + governance (repo-wide)
KFM’s “Latest Ideas” proposes a **Policy Pack** (Open Policy Agent + Conftest) integrated into CI to enforce governance rules (privacy, sensitive handling, standards).  [oai_citation:18‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

Use that here to enforce rules such as:
- no exposing sensitive coordinates beyond allowed zoom/precision
- no returning private datasets unless authorized
- no schema changes without changelog entry

---

## Example queries

> These are illustrative. Keep real, tested queries in `operations/` and validate them in CI.

### 1) Fetch a person and connected events/places (knowledge graph style)

```graphql
query PersonGraph($id: ID!, $eventsFirst: Int = 20) {
  person(id: $id) {
    id
    displayName
    timeRange { start end }

    events(first: $eventsFirst) {
      edges {
        node {
          id
          title
          dateRange { start end }
          places(first: 10) {
            edges { node { id name } }
          }
          sources { kind ref }
        }
      }
      pageInfo { hasNextPage endCursor }
    }

    provenance { provEntityId }
  }
}
```

### 2) “Between years” query (time window)

```graphql
query EventsBetween($start: DateTime!, $end: DateTime!) {
  eventsBetween(start: $start, end: $end, first: 50) {
    edges {
      node {
        id
        title
        dateRange { start end }
        sources { kind ref }
      }
    }
  }
}
```

### 3) Resolve a dataset into open-standard artifacts

```graphql
query DatasetArtifacts($datasetId: ID!) {
  dataset(id: $datasetId) {
    id
    title
    license { spdxId name }

    stac { itemUrl }
    dcat { datasetUrl }
    provenance { provJsonLdUrl }

    assets {
      kind
      url
      mediaType
    }
  }
}
```

---

## How to change the schema safely

### ✅ The safe path (PR checklist)

- [ ] Update SDL (`schema.graphql` or split files under `types/`)
- [ ] Add/adjust **contract tests** for the new/changed surface (operations + fixtures)  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] If change is breaking: declare version bump + include migration notes
- [ ] Prefer `@deprecated(reason: "...")` over removals
- [ ] Ensure provenance hooks still exist (or document why they can’t)  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)
- [ ] Add a `CHANGELOG.md` entry (what changed, why, client impact)
- [ ] Confirm policy gate passes (privacy/governance)  [oai_citation:21‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

### 🧯 Deprecation policy (recommended)
- Deprecate fields for **at least one minor release** before removal.
- Provide a clear replacement field in the reason.

---

## Design sources

This contract folder is aligned to documented KFM architecture and governance principles:

- **GraphQL exists for complex knowledge graph queries; schema mirrors graph concepts (Person/Place/Event) and must protect performance with pagination/limits.**  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)
- **KFM emphasizes open standards for geospatial/raster assets (GeoJSON, COG) and metadata/provenance (STAC, DCAT, PROV).**  [oai_citation:23‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)
- **APIs are contract artifacts: backwards-compatible unless version bump; contract tests required.**  [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Roadmap includes federation across regions/states → schema/API standardization matters.**  [oai_citation:25‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)
- **Policy-as-code in CI (OPA/Conftest) is proposed to enforce governance rules.**  [oai_citation:26‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

---

🌾 _If you’re adding a new domain type (e.g., `Treaty`, `Watershed`, `RailLine`), start by designing the SDL **as a contract**, then wire resolvers to match it — not the other way around._
