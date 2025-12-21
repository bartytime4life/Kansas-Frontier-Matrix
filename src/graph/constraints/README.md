---
title: "KFM Graph Constraints — README"
path: "src/graph/constraints/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:graph:constraints:readme:v1.0.0"
semantic_document_id: "kfm-graph-constraints-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:graph:constraints:readme:v1.0.0"
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

# KFM Graph Constraints

## 📘 Overview

### Purpose
This directory documents the **constraints and indexes** that enforce (and help validate) KFM’s **knowledge graph invariants** in Neo4j.

In KFM’s pipeline, the graph sits between **catalog outputs** (STAC/DCAT/PROV) and the **API layer**. Constraints are part of the graph’s contract surface that protects downstream stability and query correctness.

### Scope
| In Scope | Out of Scope |
|---|---|
| Defining and documenting Neo4j constraints and indexes needed to keep graph identifiers stable and to prevent obvious integrity regressions. | ETL validation logic (handled in pipelines/catalog build). |
| Constraint lifecycle guidance: naming, idempotency, migration/versioning expectations, and how constraints are validated in CI. | API contract definitions (OpenAPI/GraphQL) and UI behavior. |
| Cross-reference points to ontology/migrations/tests so changes are traceable. | Access control and redaction enforcement (belongs at API boundary and governance tooling). |

### Audience
- Graph/ontology maintainers working in `src/graph/`
- Data pipeline maintainers who load/upsert data into Neo4j
- API maintainers who rely on stable labels/edges and stable IDs
- CI/test maintainers responsible for graph integrity gates

### Definitions
- Link: `docs/glossary.md`
- Terms used here include: **constraint**, **index**, **ontology**, **migration**, **stable ID**, **graph integrity test**, **STAC**, **DCAT**, **PROV-O**.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master system contract | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline + subsystem contracts (graph includes constraints). |
| Graph ontology | `docs/graph/ontology.md` | Graph/ontology maintainers | Defines allowed labels/relationships and naming conventions. Confirm exact filename if different. |
| Graph migrations | `src/graph/migrations/` | Graph/ontology maintainers | Versioned Cypher migrations for schema evolution and data backfills. |
| Graph constraints | `src/graph/constraints/` | Graph/ontology maintainers | This directory; constraints and indexes documentation + (optional) runnable artifacts. |
| Graph change log | `docs/graph/` | Graph/ontology maintainers | Expected location for governed graph change tracking. Confirm exact file naming. |
| Graph tests | `tests/` | QA/CI maintainers | Expected home for graph integrity tests. Confirm test subfolder structure. |

### Definition of done
- [ ] Front-matter complete and `path` matches this file location
- [ ] Clear statement of what “constraints” mean in KFM (and what they do not)
- [ ] Directory layout + expected artifacts documented
- [ ] Guidance included for adding/updating constraints without breaking stable labels/edges
- [ ] Validation steps are listed and repeatable
- [ ] Governance/CARE considerations are explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `src/graph/constraints/README.md` (must match front matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Graph | `src/graph/` | Graph scripts, ontology-related assets, migrations, constraints. |
| Graph docs | `docs/graph/` | Ontology docs, graph change log, query patterns, decisions. |
| Pipelines | `src/pipelines/` | ETL + catalog builders that feed graph loads. |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Machine-validated catalog and lineage outputs that graph nodes should reference. |
| API layer | `src/api/` | Graph access boundary. UI must not read Neo4j directly. |
| UI | `web/` | React/Map UI + Story browsing surfaces. |
| Tests | `tests/` | Contract and integrity tests (including graph invariants). |
| Schemas | `schemas/` | JSON Schemas (and optionally SHACL bundles) used for validation and contracts. |

### Expected file tree for this sub-area
~~~text
📁 src/
└── 📁 graph/
    ├── 📁 constraints/
    │   └── 📄 README.md
    ├── 📁 migrations/
    │   └── 📄 README.md
    └── 📄 ... (graph loaders, ontology helpers, query utilities)
~~~

## 📦 Data & Metadata

### Inputs
- A Neo4j graph instance (local/dev/CI) where constraints/indexes are applied.
- The KFM ontology conventions for labels, relationship types, and identifier strategy.
- Stable identifiers derived from catalog outputs (STAC/DCAT/PROV) that are expected to remain unique and referable over time.

### Outputs
- Installed Neo4j constraints and indexes that:
  - prevent obvious integrity regressions (duplicate IDs, missing required identifiers where used),
  - improve query performance for frequently searched properties.
- CI signals (test pass/fail) for graph integrity and invariant enforcement.

### Sensitivity & redaction
Constraints and indexes must **not** be used as a substitute for:
- governance redaction decisions,
- API authorization and access control,
- policy enforcement.

If constraints would require storing or exposing sensitive fields (e.g., requiring high-precision locations), prefer governance-approved, generalized fields and enforce those instead.

### Quality signals
- No duplicate stable IDs for entities where uniqueness is required.
- Constraints are idempotent to apply repeatedly in migrations/CI.
- Graph integrity tests cover key invariants and fail loudly on regression.
- Indexes support expected query patterns (search, lookup, traversal anchors) without creating unnecessary write overhead.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Graph entities should be able to reference STAC Collection/Item identifiers where appropriate (e.g., “source document” items, derived raster/vector evidence artifacts).
- Constraints typically help ensure that whatever identifier field is chosen for STAC linkage is unique and consistently shaped.

### DCAT
- Dataset-level entities in the graph should remain linkable to DCAT dataset views (title/license/keywords/landing page).
- If dataset nodes exist, constraints should protect the dataset identifier from duplication.

### PROV-O
- Provenance (activities/agents/entities) may be represented as nodes and edges.
- Constraints should support stable provenance IDs where provenance nodes are used, enabling traceability across runs.

### Versioning
- Constraint changes are part of the graph’s contract surface.
- If a constraint change implies a label/edge semantic change, coordinate with:
  - ontology versioning,
  - migration scripts/backfills,
  - and any API contract changes (or version bump).

## 🧱 Architecture

### Components
| Component | Responsibility |
|---|---|
| Ontology | Defines graph labels, relationship types, and naming conventions. |
| Constraints | Enforce uniqueness/existence rules the database can enforce; provide baseline integrity guardrails. |
| Indexes | Improve query performance for known API and narrative query patterns. |
| Migrations | Provide repeatable, versioned graph changes and any required backfills. |
| Tests | Validate constraints and higher-level invariants the DB cannot enforce alone. |

### Interfaces and contracts
| Interface | Contract doc | Notes |
|---|---|---|
| Graph schema surface | `docs/MASTER_GUIDE_v12.md` + `docs/graph/` | Graph contract includes ontology + migrations + constraints; labels/edges must remain stable unless version bump. |
| Graph ↔ API layer | API contract docs under `docs/` + `src/api/` | API is the boundary; UI must not read Neo4j directly. |
| Graph ↔ catalogs | STAC/DCAT/PROV profiles | Graph identifiers and lineage should align with catalogs; graph mirrors version lineage. |
| Graph ↔ Story Nodes | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story nodes must remain provenance-backed; tests can enforce graph connectivity invariants. |

### Extension points checklist
- [ ] New constraint or index is motivated by a concrete invariant or query pattern
- [ ] Naming is deterministic and sortable (supports migration ordering)
- [ ] The change is idempotent and safe to apply repeatedly
- [ ] A test is added that fails if the constraint is missing or violated
- [ ] Ontology docs updated if label/property expectations changed
- [ ] If the API depends on the constraint, contract tests are updated
- [ ] Governance review triggered if the change affects sensitive fields or narrative exposure

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Story Nodes and Focus Mode
Constraints and graph integrity tests support narrative reliability by ensuring:
- stable entity identifiers (so citations and cross-links don’t break),
- predictable traversal anchors for “who/what/where/when” views.

### Provenance-linked narrative rule
Constraints do not “create provenance,” but they can help ensure that key identifiers used to join Story Nodes to evidence and provenance references remain unique and present where required.

### Optional structured controls
If Story Nodes require “minimum linkage” invariants (example: a Story Node must connect to at least one Place or Event), enforce via **tests** and/or **migration checks** rather than attempting to encode this exclusively as a DB constraint.

## 🧪 Validation and CI/CD

### Validation steps
- Apply constraints and indexes to a clean test Neo4j instance.
- Run graph integrity tests that:
  - attempt to create duplicate IDs and expect failure,
  - verify key traversal/query expectations,
  - validate higher-level invariants the DB cannot enforce alone.

### Reproduction
- Record constraint changes as versioned artifacts alongside migrations.
- Ensure CI uses pinned Neo4j and driver versions (where specified elsewhere).
- Store run metadata under `mcp/runs/` when applicable.

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| Graph constraint apply success/failure | CI logs | `mcp/runs/` or CI artifacts |
| Graph integrity test pass/fail | CI | `tests/` reports + CI artifacts |
| Query performance regression flags | Optional benchmarking | `mcp/experiments/` (if enabled) |

## ⚖ FAIR+CARE & Governance

### Review gates
Constraint changes require review when they:
- change required identifiers or label semantics,
- introduce new required fields that may impact sensitive content handling,
- affect downstream API contract expectations.

### CARE and sovereignty considerations
- Avoid constraints that force storage of disallowed sensitive attributes.
- Respect sovereignty policies for culturally sensitive content; prefer generalized representations when required.

### AI usage constraints
Ensure this document’s AI permissions and prohibitions match intended use, and do not use AI-generated policy text as a substitute for governed policy documents.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial constraints README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

