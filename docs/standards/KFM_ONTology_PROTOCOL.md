---
title: "KFM Ontology Protocol (Neo4j Graph Semantics)"
path: "docs/standards/KFM_ONTology_PROTOCOL.md"
version: "v4.1.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Standard"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:standards:ontology-protocol:v4.1.0"
semantic_document_id: "kfm-ontology-protocol-v4.1.0"
event_source_id: "ledger:kfm:doc:standards:ontology-protocol:v4.1.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Ontology Protocol (Neo4j Graph Semantics)

## 📘 Overview

### Purpose
This document defines the governed ontology conventions for the Kansas Frontier Matrix (KFM) **Graph stage** (Neo4j). It standardizes how entities, relationships, identifiers, and provenance are represented so that:
- Graph semantics remain stable across datasets and releases.
- Catalog-first architecture is preserved (**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**).
- API consumers and UI experiences never depend on implementation-specific graph quirks.

This protocol is the normative reference for any change that introduces or modifies **node labels**, **relationship types**, **property keys**, **ID conventions**, and **provenance linkages**.

### Scope
| In Scope | Out of Scope |
|---|---|
| Core entity labels + relationship vocabulary | Dataset-specific modeling (belongs in domain docs) |
| Required node/edge properties + naming conventions | UI design / components |
| Stable ID rules + versioning & deprecation | Direct Neo4j access patterns from the UI (explicitly prohibited) |
| STAC/DCAT/PROV linkage expectations | Runtime infra / deployment config |
| Governance gates for ontology changes | Detailed ETL extraction heuristics |

### Audience
- Primary: Graph/ontology maintainers, pipeline engineers, API engineers
- Secondary: Data curators, historians/editors, UI engineers (for consuming semantics via API)

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **Entity**: A real-world or conceptual thing modeled as a graph node (Place, Person, Event, etc.)
  - **Evidence / Provenance**: Source references and lineage ties (STAC/DCAT/PROV identifiers)
  - **Canonical ID**: Stable identifier for an entity that does not change across pipeline runs

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline invariants | `docs/MASTER_GUIDE_v12.md` | KFM core maintainers | Pipeline ordering + API boundary |
| Markdown governance protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs governance | Doc lint + fencing rules |
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | Data catalog owners | Dataset identifiers + metadata mapping |
| STAC profile | `KFM-STAC v11.0.0` | Catalog owners | Collection/item expectations |
| PROV profile | `KFM-PROV v11.0.0` | Catalog owners | Lineage requirements |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Canonical label + relationship vocabulary defined
- [ ] Stable ID rules are explicit and testable
- [ ] Provenance linkage rules are explicit (STAC/DCAT/PROV IDs)
- [ ] Change-management rules defined (versioning + review gates)
- [ ] Validation steps listed and repeatable
- [ ] No implications of prohibited AI actions (e.g., inferring sensitive locations)

## 🗂️ Directory Layout

### This document
- `path`: `docs/standards/KFM_ONTology_PROTOCOL.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Standards | `docs/standards/` | Governed protocols and profiles |
| Graph | `src/graph/` | Graph build + ontology bindings (**not confirmed in repo**) |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV outputs |
| APIs | `src/server/` or `src/api/` | Contracted access to graph (**not confirmed in repo**) |
| Story nodes | `docs/reports/.../story_nodes/` | Provenance-linked narratives (**pattern in Master Guide**) |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 standards/
    ├── 📄 README.md
    ├── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md
    ├── 📄 KFM_DCAT_PROFILE.md
    └── 📄 KFM_ONTology_PROTOCOL.md
~~~

## 🧭 Context

### Background
KFM integrates diverse historical and geospatial sources. Without a governed ontology, entity extraction and graph builds can drift (inconsistent labels, mismatched IDs, ambiguous relationships), which breaks:
- API contracts and downstream UI assumptions,
- provenance traceability,
- deterministic re-runs and reproducibility.

### Assumptions
- The graph database is Neo4j (property graph).
- Catalog artifacts (STAC/DCAT/PROV) are the canonical metadata layer; the graph links to them rather than replacing them.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes graph-derived information **only** through APIs (no direct Neo4j dependency).
- Every narrative claim must trace to a dataset/document/asset identifier.
- No policy or modeling change may require inferring sensitive locations.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where should ontology “machine-readable” exports live (e.g., JSON schema, CSV vocab)? | Graph maintainers | TBD |
| Do we standardize Neo4j relationship type casing (snake_case vs UPPER_SNAKE)? | Graph maintainers | TBD |
| Do we require PROV nodes in the graph, or only PROV references? | Catalog + graph owners | TBD |

### Future extensions
- Extension point A: domain-specific ontology modules under `docs/graph/` (**not confirmed in repo**)
- Extension point B: “Claim” and “Evidence” modeling for fine-grained citation anchoring (document offsets, bounding boxes)
- Extension point C: formal mapping to RDF/PROV-O for interchange

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL Outputs] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph (Ontology-governed)]
  C --> D[API Layer (Contracts + Redaction)]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant ETL as ETL
  participant CAT as STAC/DCAT/PROV
  participant G as Neo4j Graph
  participant API as API Layer
  participant UI as UI

  ETL->>CAT: Generate STAC/DCAT/PROV (validated)
  CAT->>G: Graph build consumes catalog IDs + normalized entities
  UI->>API: Focus query(entity_id)
  API->>G: Fetch context bundle (subgraph + provenance refs)
  G-->>API: Entities + relationships + provenance pointers
  API-->>UI: Contracted payload (redaction + audit flags)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Entity extractions / normalized records | JSON/CSV | `data/processed/...` | Deterministic transform logs |
| STAC items + collections | JSON | `data/stac/...` | STAC schema validation |
| DCAT datasets | JSON-LD/Turtle | `data/catalog/dcat/...` | DCAT profile checks |
| PROV bundles | JSON-LD/Turtle | `data/prov/...` | PROV profile checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Ontology-governed graph | Neo4j | runtime | API-only access |
| Ontology vocabulary documentation | Markdown | `docs/standards/` | This doc |
| Optional vocabulary export | JSON/CSV | `schemas/graph/` (**not confirmed**) | schema lint |

### Sensitivity & redaction
- If an entity includes sensitive location or culturally protected information, the **graph must support**:
  - classification fields (public/restricted),
  - generalized geometry where required,
  - API-enforced redaction rules.
- AI systems must not infer or reconstruct sensitive locations.

### Quality signals
- Uniqueness of canonical IDs
- No orphan provenance references (catalog IDs must resolve)
- Geometry validity and CRS normalization (if geometry is stored)
- Time bounds validity (ISO-8601 parsing; start ≤ end)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Graph nodes should reference STAC **Item IDs** for any spatiotemporal assets they represent or derive from.
- Recommended pattern:
  - Store `stac_item_ids: [ ... ]` as a property, and/or
  - Add a relationship to an `Artifact` node that carries `stac_item_id`.

### DCAT
- Graph nodes should reference DCAT dataset identifiers where applicable:
  - `dcat_dataset_id` (single) or `dcat_dataset_ids` (list).
- Use DCAT identifiers to group entities back to the dataset-of-origin (for audits and filtering).

### PROV-O
This protocol allows two acceptable compliance levels (choose one per graph build and document it in run logs):
1) **PROV References Only (Minimum)**:
   - Entities/relationships carry `prov_wasDerivedFrom` references as ID strings (document IDs, STAC IDs, etc.).
2) **PROV Nodes in Graph (Preferred for Rich Audit)**:
   - Add nodes for `ProvEntity`, `ProvActivity`, `ProvAgent` and link via PROV-aligned edges.

### Versioning
- Ontology vocabulary changes follow semver:
  - **Major**: breaking rename/removal of labels/relations or property keys used by APIs
  - **Minor**: additive labels/relations/properties
  - **Patch**: clarifications, examples, non-breaking doc improvements
- Dataset/entity versioning must preserve stable IDs and use explicit predecessor/successor links when revisions occur.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize content | Config + deterministic run logs |
| Catalogs | STAC/DCAT/PROV generation | JSON(-LD) + validators |
| Graph | Ontology-governed semantics | Neo4j (internal) |
| APIs | Contracted access + redaction | REST/GraphQL |
| UI | Map + narrative experiences | API calls only |
| Story Nodes | Curated narrative + citations | Docs + graph entity IDs |
| Focus Mode | Contextual synthesis | Provenance-linked bundles |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Ontology vocabulary | This doc (+ optional export) | Semver |
| API schemas | API docs + tests | Backward compat or version bump |
| Catalog profiles | `KFM-STAC`, `KFM-DCAT`, `KFM-PROV` docs | Profile version bump |

### Ontology naming conventions (normative)
- **Node labels**: `PascalCase`, singular (e.g., `Place`, `Person`, `Event`).
- **Relationship types (canonical)**: `lower_snake_case` (e.g., `located_in`, `happened_at`, `mentions`).
- **Property keys**: `lower_snake_case` (e.g., `canonical_name`, `start_date`).

> Implementation note: if Neo4j relationship casing differs (e.g., `LOCATED_IN`), a single mapping layer must exist in graph-build code and API serialization to preserve canonical names externally.

## 📚 Core Ontology Vocabulary (v4.1.0)

### Core node labels (required baseline)
| Label | Meaning | Minimum required properties |
|---|---|---|
| Place | Geographic place or region | `kfm_id`, `canonical_name` |
| Person | Human individual | `kfm_id`, `canonical_name` |
| Organization | Group/institution | `kfm_id`, `canonical_name` |
| Event | Dated occurrence | `kfm_id`, `canonical_name` *(or `event_type` + `start_date`)* |
| Document | Source document (text/image/PDF) | `kfm_id`, `title` *(or `canonical_name`)* |
| Artifact | Digital asset (map, image, dataset file, STAC item) | `kfm_id`, `asset_kind` |

Notes:
- `kfm_id` is mandatory for all nodes.
- If a node is extracted/AI-assisted, `confidence` and `extraction_method` are recommended.

### Canonical relationships (required baseline)
| Relationship | From → To | Meaning | Provenance requirement |
|---|---|---|---|
| `mentions` | `Document` → *Any Entity* | The document mentions the entity | Must include source refs |
| `located_in` | `Place` → `Place` | Containment / hierarchy (e.g., town in county) | Source refs if asserted |
| `happened_at` | `Event` → `Place` | Event location | Source refs if asserted |
| `participated_in` | `Person/Organization` → `Event` | Participation | Source refs if asserted |
| `derived_from` | *Any Entity* → `Document/Artifact` | Lineage/evidence tie | Must include source refs |

Recommended relationships (non-breaking, optional):
- `about` (`Document/Artifact` → *Any Entity*)
- `part_of` (*Any* → *Any*)
- `has_time_span` (`Event` → `TimeSpan`) (**TimeSpan label not confirmed in repo; optional extension**)
- `has_geometry` (`Place` → `Geometry`) (**Geometry label not confirmed; optional extension**)

### Required properties (normative)
Every node MUST include:
- `kfm_id` (string, stable)
- `canonical_name` (string) OR a documented equivalent (`title` for Document, etc.)
- `classification` (string: `open`/`restricted`/`internal`) — align with doc classification, if applicable
- `source_ids` (array of strings) OR `prov_wasDerivedFrom` (array of strings)

Every relationship SHOULD include:
- `source_ids` OR `prov_wasDerivedFrom` (array of strings)
- `confidence` (0–1) if machine-extracted

### Stable ID rules (normative)
- IDs are **immutable**, **globally unique**, and **never reused**.
- IDs MUST be deterministic given the same canonical source and normalization rules.
- Preferred format (URN-style):
  - `urn:kfm:entity:<Label>:<namespace>:<local_id>`
  - Examples:
    - `urn:kfm:entity:Place:gnis:123456`
    - `urn:kfm:entity:Document:archive:abc-001`
- If deterministic IDs cannot be derived from a source authority, assign a minted UUID-based ID:
  - `urn:kfm:entity:<Label>:kfm:<uuid>`
- When merging duplicates:
  - Preserve one canonical `kfm_id`
  - Record merged IDs in `alternate_ids: [ ... ]`
  - Add `supersedes` / `superseded_by` links if supported (**relationship not required**)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Any focusable entity must have:
  - a stable `kfm_id`,
  - resolvable provenance references (STAC/DCAT/PROV IDs or document IDs),
  - a classification compatible with the request context (public vs restricted).

### Provenance-linked narrative rule
- Story Nodes MUST reference entities by `kfm_id`.
- Story Nodes MUST include citations that map to dataset/document/asset IDs (no free-floating claims).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] STAC/DCAT/PROV schema validation (where catalogs are referenced)
- [ ] Graph integrity checks:
  - [ ] uniqueness of `kfm_id`
  - [ ] no dangling provenance references
  - [ ] relationship vocabulary constrained to allowed set
- [ ] API contract tests (ensure ontology changes do not break responses)
- [ ] Security and sovereignty checks (redaction rules where applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate catalogs
# 2) validate ontology vocabulary export (if present)
# 3) run graph build + integrity tests
# 4) run API contract tests
# 5) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| ontology_version | graph build | `mcp/runs/` or `docs/telemetry/` (**not confirmed**) |
| entity_id_collisions | graph integrity tests | test logs |
| provenance_resolution_rate | validation | test logs |

## ⚖ FAIR+CARE & Governance

### Review gates
Ontology changes require human review when they:
- add or change a core label or core relationship
- change ID rules
- introduce new sensitive fields or geometry handling
- affect API contracts or Focus Mode behavior

### CARE / sovereignty considerations
- Any culturally sensitive locations, sacred sites, or protected knowledge MUST follow `docs/governance/SOVEREIGNTY.md`.
- Do not store or expose precise coordinates if classification is restricted.

### AI usage constraints
- AI may summarize and structure-extract.
- AI must not infer sensitive locations or fabricate relationships without provenance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v4.1.0 | 2025-12-19 | Initial governed ontology protocol (baseline labels/relations + ID rules) | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

