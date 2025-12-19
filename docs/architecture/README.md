---
title: "KFM Architecture Docs — README"
path: "docs/architecture/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:architecture:readme:v1.0.0"
semantic_document_id: "kfm-architecture-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:architecture:readme:v1.0.0"
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

# KFM Architecture Docs — README

## 📘 Overview

### Purpose
This directory contains *governed architecture documentation* for Kansas Frontier Matrix (KFM).
It is the canonical place for system-level diagrams, subsystem responsibilities, and cross-cutting
constraints (contracts, security posture, provenance requirements) that must remain stable as
features evolve.

This folder complements (and should not contradict) the system-wide invariants described in
`docs/MASTER_GUIDE_v12.md`.

### Scope
| In Scope | Out of Scope |
|---|---|
| End-to-end pipeline architecture (ETL → Catalogs → Graph → APIs → UI → Story → Focus Mode) | Implementation details best kept close to code (e.g., function-by-function API internals) |
| Subsystem boundaries, responsibilities, and “do not break” rules | Dataset-specific domain documentation (belongs under `docs/data/<domain>/...` or other governed domain paths) |
| Deployment + runtime architecture (where documented) | Ad-hoc design notes without governance/provenance links |
| Security, sovereignty, and redaction architecture (at a system level) | Sensitive operational details, secrets, credentials, or internal-only procedures |

### Audience
- Primary: platform engineers, data engineers, graph engineers, API/frontend engineers
- Secondary: reviewers, governance councils, contributors authoring new pipeline extensions

### Definitions
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: pipeline stage, STAC, DCAT, PROV-O, “Focus Mode”, “Story Node”, contract

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline invariants) | `docs/MASTER_GUIDE_v12.md` | Docs | Canonical ordering + subsystem map |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default template for architecture docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs | Use for narrative nodes (NOT for architecture docs) |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Use when changing REST/GraphQL contracts |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Links resolve or are explicitly marked “not confirmed in repo”
- [ ] Architecture invariants match `docs/MASTER_GUIDE_v12.md`
- [ ] No prohibited AI actions implied (e.g., “infer sensitive locations”)
- [ ] Validation steps listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `docs/architecture/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + catalog outputs per domain |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
> NOTE: Aside from `README.md`, the following files are **planned placeholders** and may be
> **not confirmed in repo** until created and linked from the Master Guide.

~~~text
📁 docs/
└── 📁 architecture/
    ├── 📄 README.md
    ├── 📄 ARCHITECTURE_OVERVIEW.md                (not confirmed in repo)
    ├── 📄 PIPELINE_DATAFLOW.md                     (not confirmed in repo)
    ├── 📄 GRAPH_ARCHITECTURE.md                    (not confirmed in repo)
    ├── 📄 API_ARCHITECTURE.md                      (not confirmed in repo)
    ├── 📄 UI_ARCHITECTURE.md                       (not confirmed in repo)
    ├── 📄 SECURITY_ARCHITECTURE.md                 (not confirmed in repo)
    ├── 📄 DEPLOYMENT_RUNTIME_ARCHITECTURE.md       (not confirmed in repo)
    └── 📄 KFM_1_0_SYSTEM_DOCUMENTATION.pdf         (not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system built around a strict, staged pipeline that
prioritizes provenance, reproducibility, and contract boundaries.

### Assumptions
- The system’s canonical flow is preserved:
  **ETL → STAC/DCAT/PROV → Neo4j Graph → APIs → React/Map UI → Story Nodes → Focus Mode**
- The frontend never queries the graph directly; it consumes **API contracts** only.

### Constraints / invariants
- **Provenance-first:** narrative content must be traceable to cataloged sources.
- **Determinism:** ETL and transforms are intended to be replayable/idempotent.
- **Contract boundaries:** schema/contract changes require versioning and tests.
- **Sovereignty & sensitivity:** restricted locations/content must not be inferred or exposed.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical glossary (`docs/glossary.md`)? | TBD | TBD |
| Which deployment model is the baseline (local/dev, cloud, hybrid)? | TBD | TBD |
| What is the approved list of architecture artifacts for “v12-ready”? | TBD | TBD |

### Future extensions
- Architecture Decision Records (ADRs) under `docs/architecture/decisions/` (not confirmed in repo)
- Threat modeling + redaction matrix for sensitive layers (requires human review)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A["ETL (Extract/Normalize)"] --> B["STAC/DCAT/PROV Catalogs"]
  B --> C["Neo4j Graph"]
  C --> D["API Layer (REST/GraphQL)"]
  D --> E["React/Map UI (MapLibre/Cesium)"]
  E --> F["Story Nodes"]
  F --> G["Focus Mode"]
~~~

### Optional: sequence diagram (Focus Mode request)
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: Fetch subgraph + provenance refs
  Graph-->>API: Context bundle
  API-->>UI: Narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Architecture invariants | Markdown | `docs/MASTER_GUIDE_v12.md` | Markdown protocol checks |
| Subsystem docs | Markdown | `docs/<subsystem>/...` | Link checks |
| Contracts | JSON / YAML | `schemas/`, `docs/` | Schema validation + contract tests |
| Provenance standards | Spec refs | STAC/DCAT/PROV profiles | Conformance checks (where implemented) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Architecture docs | Markdown | `docs/architecture/*.md` | KFM-MDP checks |
| Diagrams | Mermaid | Inline in Markdown | Lint/render checks (CI) |
| Threat model notes | Markdown | `docs/architecture/` | Requires human review |

### Sensitivity & redaction
- Architecture documentation must not include secrets, credentials, internal-only endpoints, or
  precise restricted locations.
- Any restricted layer handling must describe *policy-compliant behavior* (generalization/redaction)
  without leaking sensitive coordinates or identifiers.

### Quality signals
- Link integrity (no broken internal links)
- Consistency with Master Guide invariants
- No “UI reads Neo4j directly” anti-patterns described

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Architecture docs should reference STAC **Collections** and **Items** as the standard for spatiotemporal assets.

### DCAT
- Architecture docs should treat DCAT as the dataset-level metadata view and ensure dataset identifiers are stable.

### PROV-O
- Architecture docs should describe lineage expectations using:
  - `prov:wasDerivedFrom` (inputs)
  - `prov:wasGeneratedBy` (pipeline run/activity)

### Versioning
- Where architecture docs define contracts, they should specify versioning rules (semver + deprecation).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize sources | Configs + deterministic run logs |
| Catalogs | STAC/DCAT/PROV metadata | JSON/JSON-LD + validators |
| Graph | Semantic entity linking | API-mediated queries (no direct UI access) |
| APIs | Serve stable contracts | REST/GraphQL + contract tests |
| UI | Map + narrative experience | API calls + layer registry |
| Story Nodes | Curated narrative artifacts | Provenance-linked docs + graph references |
| Focus Mode | Contextual synthesis | Evidence bundle + citations + audit flags |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Document templates | `docs/templates/` | Governed template updates |

### Extension points checklist (for future work)
- [ ] New domain added under `data/<domain>/...`
- [ ] New STAC collection + item validation
- [ ] PROV activity + agent identities recorded
- [ ] Graph labels/relations mapped + migration plan
- [ ] API contract version bump + tests
- [ ] UI layer registry entry + access rules
- [ ] Focus Mode provenance references enforced
- [ ] Telemetry signals captured (if applicable)

## 🧠 Story Node & Focus Mode Integration

### How architecture work surfaces in Focus Mode
- Focus Mode must only consume provenance-linked content, delivered through the API layer.
- Predictive/AI-generated content must be opt-in and include uncertainty/confidence metadata.

### Provenance-linked narrative rule
- Every claim shown to users must trace to an ID in STAC/DCAT/PROV and/or a governed document identifier.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (KFM-MDP)
- [ ] Link checks for internal references
- [ ] Schema validation (STAC/DCAT/PROV where applicable)
- [ ] API contract tests (if this doc drives contract changes)
- [ ] Security & sovereignty checks (no secrets, no sensitive coordinate leakage)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) doc lint / markdown protocol validation
# 2) link checker
# 3) schema validation (if schemas changed)
# 4) unit/integration tests (if code/contracts changed)
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Architecture changes that affect:
  - public endpoints
  - sensitive layers/redaction
  - identity/auth
  - provenance guarantees
  require human review (security + governance).

### CARE / sovereignty considerations
- Do not infer or publish sensitive locations.
- When describing restricted content, document the *rule* (generalize/redact) and the *audit behavior*,
  not the sensitive values.

### AI usage constraints
- This document may be summarized/structured, but must not introduce new policy or invent
  sensitive inferences.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial architecture README scaffolding | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`