---
title: "🧱 Kansas Frontier Matrix — System Architecture"
path: "ARCHITECTURE.md"
version: "v11.2.6"
last_updated: "2025-12-17"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:architecture:root:v11.2.6"
semantic_document_id: "kfm-architecture-root-v11.2.6"
event_source_id: "ledger:kfm:doc:architecture:root:v11.2.6"
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

# 🧱 Kansas Frontier Matrix — System Architecture

## 📘 Overview

### Purpose
This document defines the **system-level architecture** and **non-negotiable pipeline ordering** for the Kansas Frontier Matrix (KFM) monorepo. It acts as the top-level “map” for how **data, catalogs, graph semantics, APIs, UI, Story Nodes, and Focus Mode** fit together—and where deeper subsystem docs live.

### Scope
| In Scope | Out of Scope |
|---|---|
| Canonical pipeline ordering and system boundaries | Full implementation details for any specific pipeline |
| Repo architecture + responsibility boundaries by subsystem | Endpoint-by-endpoint API reference (see API docs) |
| Data lifecycle staging conventions (`raw → work → processed → stac`) | UI component-level design (see `web/` + design docs) |
| STAC/DCAT/PROV alignment expectations | Dataset-by-dataset domain modeling (see domain docs) |
| Extension patterns for new data domains & narrative products | Any disclosure of protected locations or sensitive sources |

### Audience
- Primary: KFM maintainers, contributors, system integrators
- Secondary: domain researchers, governance reviewers, curriculum / demo builders

### Definitions
- Glossary: `docs/glossary.md`
- Key terms used in this document:
  - **STAC**: SpatioTemporal Asset Catalog (Collections/Items/Assets)
  - **DCAT**: Dataset catalog view for discovery and distribution metadata
  - **PROV-O**: Provenance model for lineage and accountability
  - **Story Node**: Curated narrative artifact referencing evidence + entities
  - **Focus Mode**: Provenance-linked contextual synthesis for a selected focus target

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (baseline) | `docs/MASTER_GUIDE_v11.md` | KFM Maintainers | System inventory + v11 baseline |
| Master Guide (draft evolution) | `docs/MASTER_GUIDE_v12.md` | KFM Maintainers | Extension points + v12-ready gates |
| Markdown Protocol | `docs/standards/kfm_markdown_protocol_v11.2.6.md` | Governance | Canonical Markdown/metadata rules |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Governance | Default governed doc template |
| Schemas | `schemas/` | Maintainers | JSON + telemetry schemas |
| Data lifecycle root | `data/` | Data Stewards | Raw/work/processed/stac organization |
| Core implementation | `src/` | Engineering | Pipelines, graph, services |
| Frontend | `web/` | UI Engineering | Map client + narrative UX |
| MCP workspace | `mcp/` | Maintainers | Experiments, SOPs, model cards |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Canonical pipeline ordering stated (and not contradicted elsewhere)
- [ ] Directory layout reflects current repo top-levels
- [ ] Extension points checklist included
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document
- `path`: `ARCHITECTURE.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub automation & CI | `.github/` | Workflows, policies, templates |
| Data domains | `data/` | Raw/work/processed outputs + catalogs |
| Documentation | `docs/` | Canonical governed docs + standards |
| Pipelines | `src/pipelines/` | ETL + catalog build + transforms |
| Graph | `src/graph/` | Neo4j modeling, loaders, migrations |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map client + narrative UX |
| MCP | `mcp/` | Experiments, model cards, SOPs |
| Tooling | `tools/` | Validators, CI helpers, governance tooling |
| Releases | `releases/` | Signed/attested release packets |

### Expected file tree for the repo top-level
~~~text
📁 Kansas-Frontier-Matrix/
├── 📄 README.md
├── 📄 ARCHITECTURE.md
├── 📄 CONTRIBUTING.md
├── 📄 LICENSE
├── 📁 .github/
├── 📁 data/
├── 📁 docs/
├── 📁 mcp/
├── 📁 schemas/
├── 📁 src/
├── 📁 tests/
├── 📁 tools/
├── 📁 web/
└── 📁 releases/
~~~

---

## 🧭 Context

### Background
KFM is a **geospatial + historical knowledge system** designed to unify many Kansas-relevant layers (historical, environmental, archaeological-science, and future projections) into one governed, explorable platform.

### Assumptions
- The system is **pipeline-first**: new capabilities enter through deterministic ETL and governed metadata, not ad hoc UI patches.
- Provenance is first-class: artifacts must be traceable through **STAC/DCAT/PROV** and/or graph lineage.
- The repo is designed to support both:
  - machine validation (schemas, checksums, CI gates)
  - human narrative (Story Nodes, Focus Mode)

### Constraints / invariants
- **Canonical ordering is preserved:**
  - **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**
- Frontend consumes data via **API contracts** (no direct graph dependency).
- Derived datasets belong in `data/processed/` (not `src/`).
- Run logs and experiment records belong in `mcp/` (e.g., `mcp/experiments/`).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical API contract documentation located (OpenAPI/GraphQL), and what is the versioning policy? | Maintainers | TBD |
| What is the canonical DCAT output location and publishing model? | Data Stewards | TBD |
| How are Story Nodes versioned and linked to graph entities in release packets? | Focus Mode Board | TBD |

### Future extensions
- New data domains under `data/<domain>/...` with matching STAC and validation
- Evidence artifacts (analysis outputs) treated as STAC Assets and surfaced in Focus Mode
- Expanded telemetry signals (security posture, energy/carbon for workloads)
- New Story Node types and ingestion workflows (with explicit provenance)

---

## 🗺️ Diagrams

### System / dataflow diagram
This diagram describes the required subsystem handoff order from ingestion to narrative experience.

~~~mermaid
flowchart LR
A[ETL] --> B[STAC/DCAT/PROV Catalogs]
B --> C[Neo4j Graph]
C --> D[APIs]
D --> E[React/Map UI]
E --> F[Story Nodes]
F --> G[Focus Mode]
~~~

### Optional: sequence diagram
This diagram shows the contract boundary: UI requests context via an API; the API mediates graph and provenance.

~~~mermaid
sequenceDiagram
participant UI
participant API
participant Graph
UI->>API: Focus query(entity_id)
API->>Graph: fetch subgraph + provenance refs
Graph-->>API: context bundle
API-->>UI: narrative + evidence refs + audit flags
~~~

---

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw sources | Mixed (domain-specific) | `data/raw/` | Checksums, schema checks where applicable |
| Pipeline configs | YAML/JSON | `src/pipelines/` | Config lint + CI |
| Governance rules | Markdown + schemas | `docs/standards/`, `docs/governance/` | Markdown protocol + policy review |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed datasets | Domain-specific | `data/processed/` | Domain validators + checksums |
| STAC catalogs | JSON | `data/stac/` | STAC validation |
| Lineage bundles | PROV-O compatible | (project-defined) | PROV validation |
| Graph build artifacts | Neo4j load/migration assets | `src/graph/` | Graph integrity tests |
| Narrative artifacts | Markdown/JSON | `docs/` (project-defined) | Story Node schema + provenance rules |

### Sensitivity & redaction
- Do not include secrets, tokens, or personal data in artifacts.
- Do not publish precise coordinates or identifying details for protected or culturally sensitive sites.
- Apply sovereignty policy redaction/generalization before public outputs.

### Quality signals
- Checksums for staged data (`data/checksums/` if used)
- STAC schema validation for catalog products
- Deterministic pipeline runs (replayable configs + run logs)
- Graph integrity checks (constraints + migration validity)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Each domain dataset should be represented through:
  - STAC **Collections** for dataset grouping
  - STAC **Items** for discrete assets/tiles/features/time slices
  - Assets that point to the authoritative files in `data/processed/` and/or derived products

### DCAT
- Provide a dataset catalog view that supports:
  - dataset identifiers
  - licensing
  - publisher/contact metadata
  - keywords/themes
  - distribution links

### PROV-O
- Record lineage for transformations:
  - Raw sources → ETL activities → processed outputs → catalogs → graph build
- Use stable identifiers for:
  - Activities (pipeline runs)
  - Agents (workflow, maintainer group, automated system)
  - Entities (datasets, collections, releases)

### Versioning
- New dataset versions must link predecessor/successor (where applicable).
- Graph and narrative should mirror dataset lineage where it matters for interpretation.

---

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize sources | Configs + run logs |
| Catalogs | STAC/DCAT/PROV generation | JSON outputs + validators |
| Graph | Semantic integration (Neo4j) | Migration + query layer |
| APIs | Contracted access to graph/catalogs | REST/GraphQL (contract-tested) |
| UI | Map + narrative UX | API calls |
| Story Nodes | Curated narrative artifacts | Graph-linked, provenance-annotated |
| Focus Mode | Contextual synthesis | Provenance-linked context bundle |
| Telemetry | Observability + governance signals | Schemas + logs |
| Governance | Policy + review gates | Standards + review workflow |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | SemVer + changelog discipline |
| Telemetry schemas | `schemas/telemetry/` | Schema-validated + versioned |
| STAC/DCAT/PROV outputs | `data/stac/` + docs | Must validate before merge/release |
| Graph ontology/migrations | `src/graph/` + `docs/graph/` | Backward-safe migrations or explicit version bump |
| Pipeline runbooks | `docs/pipelines/` | Must match executable pipeline behavior |
| UI registries/config | `web/` | Schema validated where applicable |

### Extension points checklist
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] Catalogs: STAC Collection + Items validate cleanly
- [ ] PROV: activity + agent identifiers recorded for the transform
- [ ] Graph: new labels/relations mapped + migration plan documented
- [ ] APIs: contract version bump (or backward-compat proof) + tests
- [ ] UI: layer/config entry + access rules + provenance pointers
- [ ] Focus Mode: every surfaced claim points to evidence identifiers
- [ ] Telemetry: new signals + schema version bump (if introduced)

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus targets should be **stable identifiers** (dataset IDs, entity IDs, asset IDs).
- UI and Focus Mode should always display:
  - what evidence is being used
  - what provenance chain applies
  - what redaction rules were applied (when relevant)

### Provenance-linked narrative rule
- Every factual claim presented in a Story Node or Focus Mode context must trace to a dataset / record / asset ID (and, where applicable, a PROV activity that produced it).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]  # Example only; must not expose protected locations
~~~

---

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (structure + headings + fencing)
- [ ] Schema validation (STAC/DCAT/PROV + telemetry as applicable)
- [ ] Graph integrity checks (constraints + migrations)
- [ ] API contract tests
- [ ] UI configuration/schema checks (where applicable)
- [ ] Security and sovereignty checks (PII/secrets + protected-site masking rules)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas (STAC/DCAT/telemetry)
# 2) run unit/integration tests (pipelines/graph/api)
# 3) run doc lint (markdown protocol)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Pipeline run metadata | ETL workflows | `mcp/` (run records) |
| Schema validation results | CI | CI logs + reports |
| Governance compliance flags | Review workflow | Governance logs / reports (project-defined) |

---

## ⚖ FAIR+CARE & Governance

### Review gates
- Architecture changes that affect:
  - pipeline ordering
  - public-facing contracts (API/UI)
  - sovereignty/redaction rules
  - AI narrative behavior
  should be treated as governance-reviewed changes (council/board review as defined in governance docs).

### CARE / sovereignty considerations
- Do not introduce documentation that enables harm via location disclosure.
- Treat culturally sensitive sites and restricted locations as protected classes of information.
- Prefer generalized descriptions and masking rules over exact coordinates.

### AI usage constraints
- AI may summarize and structure-extract this document.
- AI must not infer protected locations, generate governance policy, or introduce speculative architectural claims without linking to governed artifacts.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v11.2.6 | 2025-12-17 | Initial root-level System Architecture doc scaffolded from the canonical pipeline ordering and governed templates. | TBD |

--Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
