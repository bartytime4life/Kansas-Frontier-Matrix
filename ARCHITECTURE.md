---
title: "Kansas Frontier Matrix — Architecture"
path: "ARCHITECTURE.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Architecture"
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

doc_uuid: "urn:kfm:doc:architecture:architecture-md:v1.0.0"
semantic_document_id: "kfm-architecture-md-v1.0.0"
event_source_id: "ledger:kfm:doc:architecture:architecture-md:v1.0.0"
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

# Kansas Frontier Matrix — Architecture

## 📘 Overview

### Purpose
This document is the canonical, governed description of the Kansas Frontier Matrix (KFM) system architecture:
- the end-to-end pipeline ordering
- subsystem boundaries and contracts
- invariants (provenance, determinism, API boundary)
- extension points and CI validation expectations

### Scope
| In Scope | Out of Scope |
|---|---|
| Canonical pipeline ordering and handoffs | Detailed implementation of every ETL parser or UI component |
| Directory layout expectations | Deployment topology (cloud provider, cluster layouts) |
| Metadata standards alignment (STAC/DCAT/PROV) | Vendor selection or procurement decisions |
| Contract boundaries (Graph ↔ API ↔ UI) | Private keys, secrets, or operational runbooks |
| Governance and sensitivity expectations | Historical interpretation beyond provenance-backed claims |

### Audience
- Primary: KFM maintainers (DataOps, Graph, API, UI)
- Secondary: contributors (ETL authors, curators, reviewers), integrators consuming APIs

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: ETL, STAC, DCAT, PROV-O, knowledge graph, Story Node, Focus Mode, provenance, redaction, CARE

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | System pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Governed doc structure |
| Story node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Curators | Provenance-linked narrative |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API team | REST/GraphQL contract changes |
| STAC/DCAT/PROV outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | DataOps | Catalog + lineage bundles |
| Graph docs | `docs/graph/` | Graph team | Ontology + migrations |
| Pipeline docs | `docs/pipelines/` | DataOps | ETL/cat/graph build notes |
| API docs | `docs/` + `src/server/` | API team | Contracts + tests |
| UI docs | `docs/design/` + `web/` | UI team | Map layers + Focus Mode UX |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Canonical pipeline ordering preserved and explicitly stated
- [ ] API boundary stated (UI never reads graph directly)
- [ ] Provenance-first rule stated (no unsourced narrative in Focus Mode)
- [ ] Validation steps listed and repeatable (even if commands are TBD)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] “Not confirmed in repo” used where implementation details are unknown

## 🗂️ Directory Layout

### This document
- `path`: `ARCHITECTURE.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed data and catalog outputs |
| Documentation | `docs/` | Canonical governed docs and standards |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| APIs | `src/server/` | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |
| Tests | `tests/` | Unit/integration tests |
| Tools | `tools/` | Dev and validation tooling |

### Expected file tree for this sub-area
~~~text
📄 ARCHITECTURE.md
📁 .github/
│  ├── 📄 SECURITY.md
│  └── 📁 workflows/
├── 📁 data/
│  ├── 📁 raw/
│  ├── 📁 work/
│  ├── 📁 processed/
│  ├── 📁 stac/
│  │  ├── 📁 collections/
│  │  └── 📁 items/
│  ├── 📁 catalog/
│  │  └── 📁 dcat/
│  └── 📁 prov/
├── 📁 docs/
│  ├── 📄 MASTER_GUIDE_v12.md
│  ├── 📁 templates/
│  │  ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│  │  ├── 📄 TEMPLATE__STORY_NODE_V3.md
│  │  └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
│  ├── 📁 standards/
│  ├── 📁 graph/
│  ├── 📁 pipelines/
│  ├── 📁 design/
│  ├── 📁 security/
│  └── 📁 telemetry/
├── 📁 mcp/
│  ├── 📁 runs/
│  └── 📁 experiments/
├── 📁 schemas/
│  └── 📁 telemetry/
├── 📁 src/
│  ├── 📁 pipelines/
│  ├── 📁 graph/
│  └── 📁 server/
├── 📁 tests/
├── 📁 tools/
├── 📁 web/
└── 📁 releases/
~~~

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system with governed data, catalogs, graph semantics, APIs, and a map/narrative UI. Its architecture is pipeline-oriented so that each stage hands off validated artifacts to the next stage.

### Assumptions
- The pipeline ordering is canonical and preserved end-to-end:
  - **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**
- Metadata and lineage are first-class artifacts (not “optional nice-to-haves”).
- Deterministic, idempotent processing is required for reproducibility.
- The UI consumes the graph only through the API layer (no direct graph reads).

### Constraints / invariants
- **Canonical pipeline ordering is non-negotiable.**
- **No unsourced narrative in Focus Mode contexts.**
- **Provenance is first-class** (STAC/DCAT/PROV + graph lineage).
- **Reproducibility:** deterministic pipelines; stable IDs/keys; versioned artifacts.
- **API boundary:** frontend consumes contracts via APIs (no direct graph dependency).
- **Security & governance:** no secrets in repo; sensitivity rules enforced; avoid leaking restricted locations.
- **Fact vs inference:** any predictive/AI content is opt-in and carries uncertainty/confidence metadata.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the authoritative glossary located? | Docs lead | TBD |
| Where is the authoritative UI layer registry schema/file located? | UI lead | TBD |
| Are Story Nodes always stored under `docs/reports/.../story_nodes/`, or is there a newer canonical path? | Curators | TBD |

### Future extensions
- Extension point A: add new data domains under `data/<domain>/...` with matching STAC/DCAT/PROV
- Extension point B: add new “analysis/evidence artifacts” as cataloged assets with provenance links into Focus Mode

## 🗺️ Diagrams

### System dataflow diagram
~~~mermaid
flowchart LR
  subgraph Data
    A[Raw Sources] --> B[ETL + Normalization]
    B --> C[Processed Data]
    C --> D[STAC Items + Collections]
    C --> E[DCAT Dataset Views]
    C --> F[PROV Lineage Bundles]
  end

  D --> G[Neo4j Graph]
  E --> G
  F --> G

  G --> H[API Layer]
  H --> I[React / Map UI]
  I --> J[Story Nodes]
  J --> K[Focus Mode]
~~~

### Optional: focus query sequence
~~~mermaid
sequenceDiagram
  participant UI as Map UI
  participant API as API Layer
  participant Graph as Neo4j Graph
  participant Cat as Catalogs (STAC/DCAT/PROV)

  UI->>API: Focus query(entity_id, time_window?)
  API->>Graph: Fetch subgraph + provenance references
  Graph-->>API: Entity bundle + edges + catalog IDs
  API->>Cat: Resolve catalog refs (STAC/DCAT/PROV)
  Cat-->>API: Metadata + lineage links
  API-->>UI: Narrative bundle + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw sources | PDFs, images, CSV/XLSX, GeoJSON/Shapefile, URLs | `data/raw/` and/or controlled ingest | Checksums; type validation; license metadata |
| Intermediate work | Extracted text/tables, normalized geometry | `data/work/` | Deterministic transforms; warnings logged |
| Curated sources | Curator-reviewed bundles | `data/processed/` | Schema checks; provenance links required |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed datasets | domain-specific | `data/processed/` | Domain schemas (TBD) |
| STAC catalogs | JSON | `data/stac/collections/`, `data/stac/items/` | STAC profile `KFM-STAC v11.0.0` |
| DCAT catalogs | JSON-LD/Turtle | `data/catalog/dcat/` | DCAT profile `KFM-DCAT v11.0.0` |
| PROV bundles | JSON-LD | `data/prov/` | PROV profile `KFM-PROV v11.0.0` |
| Graph build | Neo4j load artifacts | `src/graph/` + run outputs | Ontology protocol `KFM-ONTO v4.1.0` |
| API responses | JSON | `src/server/` | OpenAPI / GraphQL (not confirmed in repo) |
| Story Nodes | Markdown | `docs/reports/.../story_nodes/` (path may vary) | Story Node template v3 |

### Sensitivity & redaction
- Do not expose restricted or sensitive locations or records without applying generalization/redaction rules.
- Ensure Story Nodes and Focus Mode panels never present uncited facts.
- If predictive/AI-generated content is present, it must be clearly labeled and opt-in, with uncertainty metadata.

### Quality signals
- Schema validation (STAC/DCAT/PROV, domain schemas)
- Geometry validity + CRS normalization for geospatial assets
- Stable IDs/keys for entities; referential integrity for relationships
- Provenance completeness: every derived output references inputs + generating activity/run

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: stored under `data/stac/collections/`
- Items involved: stored under `data/stac/items/`
- Extension(s): governed by `stac_profile` in front-matter (additional extensions not confirmed in repo)

### DCAT
- Dataset identifiers: defined per dataset record under `data/catalog/dcat/`
- License mapping: captured per dataset (license policy details not confirmed in repo)
- Contact/publisher mapping: captured per dataset record (not confirmed in repo)

### PROV-O
- `prov:wasDerivedFrom`: list source IDs / STAC assets / dataset IDs used as inputs
- `prov:wasGeneratedBy`: pipeline activity/run ID (format not confirmed in repo)
- Activity/Agent identities: scripts, curators, or service agents (as appropriate)

### Versioning
- Dataset versions link predecessor/successor in catalog metadata.
- Graph mirrors version lineage.
- Schema and contract changes follow SemVer with changelog and tests.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize + enrich | Config-driven runs + deterministic logs |
| Catalogs | STAC/DCAT/PROV outputs | JSON/JSON-LD + validators |
| Graph | Neo4j knowledge graph | Queried through API layer only |
| APIs | Serve contracted access | REST/GraphQL contracts (not confirmed in repo) |
| UI | Map + narrative experience | API calls + a11y + audit affordances |
| Story Nodes | Curated narrative artifacts | Markdown + graph linkage + provenance |
| Focus Mode | Contextual synthesis view | Provenance-linked context bundle |
| Telemetry | Observability + governance signals | `docs/telemetry/` + `schemas/telemetry/` |
| Security | Standards and enforcement | `.github/SECURITY.md` + `docs/security/` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | SemVer + changelog |
| Catalog profiles | front-matter (`KFM-STAC`, `KFM-DCAT`, `KFM-PROV`) | Profile bump when schema expectations change |
| API contracts | `src/server/` + docs | Contract tests required |
| Graph ontology | `docs/graph/` + `src/graph/` | Version bump + migration plan |
| Story Node schema | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Versioned template |

### Extension matrix
| Extension | Data | Catalog | Graph | API | UI | Story/Focus | Telemetry |
|---|---|---|---|---|---|---|---|
| New dataset | ✓ | ✓ | optional | optional | optional | optional | optional |
| New analysis product (e.g., evidence artifacts) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| New narrative node type | optional | optional | ✓ | ✓ | ✓ | ✓ | ✓ |
| New security gate | — | — | — | — | — | — | ✓ |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules (path not confirmed in repo)
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focusable entities must resolve to:
  - graph node(s) with stable IDs
  - catalog references (STAC/DCAT) for evidence assets
  - PROV lineage (how evidence was produced)
- Story Nodes are curated narratives that:
  - reference underlying evidence assets
  - link to graph entities
  - carry explicit citations per claim

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Any AI-generated or predicted content must be opt-in and include uncertainty/confidence metadata.

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
- [ ] Schema validation (STAC/DCAT/PROV + domain schemas)
- [ ] Graph integrity checks (labels/edges constraints, ID uniqueness)
- [ ] API contract tests (OpenAPI/GraphQL as applicable)
- [ ] UI schema checks (layer registry and configuration; location not confirmed in repo)
- [ ] Security and sovereignty checks (secrets scanning, PII checks, sensitive-location rules)

### Reproduction
~~~bash
# Replace placeholders with repo-specific commands.
# 1) validate docs + markdown protocol
# 2) validate STAC/DCAT/PROV schemas
# 3) run pipelines (dry-run if supported)
# 4) run unit + integration tests
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Pipeline run metadata | ETL/catalog jobs | `docs/telemetry/` (not confirmed in repo) |
| Provenance completeness | catalog validation | CI artifacts + reports |
| Sensitivity violations | redaction checks | CI gate + audit logs |
| API contract drift | contract tests | CI reports |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that typically require human review:
  - new sensitive layers or content categories
  - new AI narrative behaviors in Focus Mode
  - new external data sources
  - new public-facing endpoints or expanded access scopes

### CARE / sovereignty considerations
- Identify impacted communities and protection rules when handling culturally sensitive content.
- Apply generalization/redaction for restricted locations and records.

### AI usage constraints
- AI transforms allowed: summarize, structure extraction, translate, keyword indexing.
- Prohibited: generating policy, inferring sensitive locations, or presenting uncited facts.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `ARCHITECTURE.md` aligned to Master Guide v12 | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`