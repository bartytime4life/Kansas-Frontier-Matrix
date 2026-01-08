# KFM data/graph — README

A governed home for **graph import artifacts** used to load and evolve the **Neo4j knowledge graph**.

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose

- Define what belongs in `data/graph/` and what does not.
- Standardize how graph import artifacts:
  - connect back to **STAC/DCAT/PROV** (round‑trip traceability),
  - preserve **ontology‑governed labels/relationships**, and
  - support **API and Focus Mode provenance requirements**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Graph import CSV exports (`data/graph/csv/`) | Raw domain source snapshots (belongs under `data/<domain>/raw/`) |
| Optional post‑import Cypher scripts (`data/graph/cypher/`) | Full Neo4j database store files (deployed instance concern) |
| Import artifacts that reference STAC/DCAT/PROV IDs | Secrets/credentials, connection strings, or operational deployment configs |
| Small, reviewable fixtures that enable tests or examples | UI code or direct UI→graph access patterns |

### Audience

- Data/graph contributors producing import artifacts for new domains
- Graph/ontology maintainers reviewing label/relationship changes
- API and narrative maintainers verifying provenance + governance behavior

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add/repair link if glossary lives elsewhere)*
- Terms used here:
  - **Import artifact**: a CSV/Cypher file used to create/update nodes/edges in Neo4j.
  - **Evidence pointer**: a reference (ID/link) to STAC/DCAT artifacts that hold canonical metadata.
  - **Lineage pointer**: a reference to PROV activities/entities describing how something was produced.

### Key artifacts this README points to

| Artifact | Path / Identifier | Notes |
|---|---|---|
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |
| Ontology docs | `docs/graph/ontology.md` *(or similar; not confirmed)* | Governs labels/relationships |
| Graph code | `src/graph/` | Graph build, ingest, migrations, constraints |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Canonical metadata + lineage |
| API boundary | `src/server/` *(v13 target)* or `src/api/` *(legacy; not confirmed)* | UI must not read Neo4j directly |
| Story Nodes | `docs/reports/story_nodes/` | Provenance‑linked narrative artifacts |

### Definition of done for this document

- [x] Front‑matter complete and `path` matches file location
- [x] Directory responsibilities + placement rules documented
- [x] Expected `data/graph/` tree provided
- [ ] Repo lint / markdown lint run (CI or local)
- [ ] Maintainer review

---

## 🗂️ Directory Layout

### This document

- `path`: `data/graph/README.md` (must match front‑matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts (canonical evidence + lineage) |
| Graph artifacts | `data/graph/` | Import CSVs + optional post‑import Cypher scripts |
| Graph code | `src/graph/` | Ontology bindings, ingest/build code, migrations, constraints, tests |
| Pipelines | `src/pipelines/` | Deterministic transforms and catalog builders |
| API boundary | `src/server/` *(v13 target)* | Contracted access layer + governance enforcement |
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and assets |

### Expected file tree for this sub-area

~~~text
📁 data/
└── 📁 graph/
    ├── 📄 README.md
    ├── 📁 csv/
    │   └── (graph import CSV exports)
    └── 📁 cypher/
        └── (optional post-import scripts)
~~~

> If this tree differs from what exists in the repo today, treat this as the **target layout** and update once the canonical structure is confirmed.

---

## 🧭 Context

### Background

KFM uses Neo4j as the **semantic layer** connecting people, places, events, documents, and artifacts into an interlinked network. This layer is fed by governed outputs from **STAC/DCAT/PROV** and processed domain datasets. The `data/graph/` directory exists to keep **import artifacts reviewable, diffable, and provenance‑linked**.

### What belongs here

- **CSV exports** intended for graph ingest (bulk import or scripted loads).
- **Cypher scripts** used to finalize/patch post‑import state, when needed.

### What must be true

- Graph import artifacts must be **governed by the ontology** (labels and relationships are controlled and stable).
- Graph content must store **references back to STAC/DCAT** and avoid duplicating large data payloads inside the graph.
- Graph access for UI must be **through the API boundary** (no direct UI→Neo4j reads).

### CSV vs Cypher

Use **CSV** when:
- the import is large, repeatable, and naturally tabular,
- you need diffable inputs for a deterministic load.

Use **Cypher** when:
- you need post‑import linking, refactoring, constraints, or controlled patches,
- the operation must be expressed as idempotent graph transformations (prefer `MERGE` patterns over blind `CREATE`).

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph Catalogs
    A["data/<domain>/processed"] --> B["data/stac/ (Collections + Items)"]
    B --> C["data/catalog/dcat/ (Dataset views)"]
    B --> D["data/prov/ (Lineage bundles)"]
  end

  subgraph GraphArtifacts
    B --> E["data/graph/csv/"]
    C --> E
    D --> E
    E --> F["Neo4j Graph (deployed instance)"]
    G["data/graph/cypher/"] --> F
  end

  F --> H["API Layer (contracted)"]
  H --> I["UI (React/Map)"]
  I --> J["Story Nodes"]
  J --> K["Focus Mode"]
~~~

~~~mermaid
flowchart TB
  X["STAC/DCAT/PROV IDs"] --> Y["Graph nodes/edges store pointers"]
  Y --> Z["API returns evidence + provenance pointers"]
  Z --> N["Story Nodes cite datasets + provenance"]
  Z --> M["Focus Mode enforces provenance-linked context"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Traceability contract

To support provenance‑linked narrative (and to prevent “orphan facts”):

- Nodes and relationships created from a dataset should carry **evidence pointers** back to:
  - STAC Item/Collection IDs, and/or
  - DCAT dataset identifiers.
- The ingest process should preserve **lineage pointers** to PROV activities where applicable.
- Story Nodes must be able to cite dataset IDs + provenance pointers; Focus Mode must only render provenance‑linked context.

### Practical implication for `data/graph/`

When you add or update graph import artifacts here, you are implicitly changing what the API can query and what Story Nodes can cite. Keep artifacts:
- small enough to review,
- structured enough to validate,
- and linked enough to trace back to catalogs.

---

## 🧪 Validation & CI/CD

### Minimum checks for PRs touching `data/graph/**`

- [ ] CSV files are UTF‑8 and include headers
- [ ] All node identifiers and relationship endpoints are non‑null
- [ ] Relationship rows do not reference missing node IDs (referential integrity)
- [ ] Any evidence pointer fields are valid IDs that exist in `data/stac/**` and/or `data/catalog/dcat/**`
- [ ] Any lineage pointer fields resolve to `data/prov/**`
- [ ] No restricted/sensitive location precision is introduced unintentionally
- [ ] Cypher scripts are idempotent (safe to re-run) and scoped (no accidental global rewrites)

> Exact CI implementation details are repo‑dependent (not confirmed). This section defines the **expected gates**.

---

## 📦 Data & Metadata

### Inputs consumed by graph import artifacts

| Input | Format | Location | Notes |
|---|---|---|---|
| Processed domain outputs | tabular/geospatial | `data/<domain>/processed/` | Normalized, validated |
| STAC catalogs | JSON | `data/stac/**` | Canonical item/collection metadata |
| DCAT dataset records | JSON-LD | `data/catalog/dcat/**` | Dataset-level discovery metadata |
| PROV bundles | JSON-LD | `data/prov/**` | Lineage + derivation |

### Outputs stored here

| Output | Format | Location | Notes |
|---|---|---|---|
| Graph import CSV exports | CSV | `data/graph/csv/**` | Nodes/edges import tables |
| Optional post-import scripts | Cypher | `data/graph/cypher/**` | Patches/linking/constraints where appropriate |

### Naming guidance

> Not confirmed as an enforced standard in repo; use as a consistent default until a formal convention exists.

Recommended patterns:
- Nodes: `nodes__<Label>__<domain>__<yyyymmdd>.csv`
- Relationships: `rels__<TYPE>__<domain>__<yyyymmdd>.csv`
- Post-import Cypher: `<domain>__<purpose>__<yyyymmdd>.cypher`

### Sensitivity & redaction

- If an input dataset is restricted/sensitive, graph import artifacts must not “launder” that sensitivity:
  - classification must be preserved and enforced via API query-time filtering,
  - sensitive coordinates may require generalization before public-facing outputs.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Graph nodes should store **STAC IDs** (Item/Collection) as references where applicable.
- The graph should not duplicate large assets; STAC remains the canonical asset registry.

### DCAT

- Use DCAT dataset identifiers to link graph content to dataset descriptions and distributions.

### PROV-O

- Preserve derivation by linking nodes/edges to PROV activities/entities where applicable.
- If provenance needs to be queryable inside Neo4j, model Activities/Agents explicitly (balanced against complexity).

### Versioning

- New catalog versions should link predecessor/successor.
- Graph imports should mirror version lineage (e.g., relations expressing revision/derivation), or at minimum preserve pointers sufficient for API to do so.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize sources | configs + run logs |
| Catalogs | Emit STAC/DCAT/PROV | JSON + validators |
| Graph artifacts | Provide import-ready tables/scripts | CSV/Cypher |
| Graph runtime | Neo4j semantic layer | accessed via API |
| API layer | Contracts + governance enforcement | REST/GraphQL contracts |
| UI | Map + narrative UX | API calls only |

### Interfaces / contracts

- **UI never reads Neo4j directly.** All graph access must go through contracted APIs.
- Labels/relationships must remain stable unless a version bump + migration is declared.
- Graph changes that affect API payloads require API contract updates and tests.

### Extension points checklist

- [ ] New label/relationship required → update ontology docs and versioning plan
- [ ] New graph import artifacts added → CSV/Cypher placed under `data/graph/**`
- [ ] Evidence pointers added → verify STAC/DCAT IDs exist
- [ ] Lineage pointers added → verify PROV bundles exist
- [ ] API surfaces updated → contract change documented + tests added

---

## ⚖ FAIR+CARE & Governance

- **FAIR:** Keep artifacts findable and reproducible (stable IDs, deterministic generation, diffable outputs).
- **CARE:** Treat culturally sensitive data as high‑risk by default; do not publish precise sensitive locations without review.
- **Governance expectation:** graph import artifacts must be reviewable and traceable back to catalogs and provenance.

---

## 🕰️ Version History

| Version | Date | Author | Change |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | TBD | Initial `data/graph/README.md` |

---

### Footer refs

- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/graph/ontology.md` *(or equivalent; not confirmed)*
- `data/stac/` + `data/catalog/dcat/` + `data/prov/`
- `src/graph/`
- `src/server/contracts/` *(v13 target; not confirmed)*
- `docs/reports/story_nodes/`
