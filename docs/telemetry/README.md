---
title: "Telemetry — README"
path: "docs/telemetry/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:telemetry:readme:v1.0.0"
semantic_document_id: "kfm-telemetry-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:telemetry:readme:v1.0.0"
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

# Telemetry

## 📘 Overview

### Purpose
This directory contains **governed documentation for KFM telemetry**: what signals are collected, how they are validated, and how they support observability, security posture, and governance metrics across the canonical pipeline.

Telemetry is treated as a first-class subsystem that:
- supports reproducibility and auditability (run IDs, validations, redaction actions),
- helps enforce “no unsourced narrative” by recording provenance-linking behaviors,
- provides CI/CD-visible quality and integrity signals.

### Scope

| In Scope | Out of Scope |
|---|---|
| Telemetry signal definitions and naming conventions | Vendor selection for logging/metrics infrastructure |
| Telemetry schema locations + versioning expectations | Operational SRE runbooks not checked into this repo |
| CI/CD validation expectations for telemetry artifacts | Runtime secrets/keys, deployment configuration |
| Guidance on sensitivity, redaction, and “do not log” rules | Collecting or storing end-user PII |

### Audience
- Primary: Data pipeline engineers, backend/API engineers, frontend engineers, governance/security reviewers
- Secondary: historians/editors reviewing narrative provenance + audit panels

### Definitions
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc (intended meanings):
  - **signal**: a named telemetry event/metric/tracing span emitted by a subsystem
  - **producer**: component that emits telemetry
  - **schema**: JSON schema that validates a telemetry payload (versioned)
  - **run_id**: stable identifier for a deterministic pipeline execution (ETL/catalog/graph build)
  - **audit flag**: a UI/API surfaced warning tied to provenance/sensitivity

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Telemetry docs (this area) | `docs/telemetry/` | Repo maintainers | Narrative + governance for telemetry |
| Telemetry schemas | `schemas/telemetry/` | DataOps / Platform | Schema validation + SemVer |
| Pipeline run artifacts | `mcp/runs/` | DataOps / MCP | Run logs + evidence products (if used) |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Directory map points to canonical locations (docs/schemas/mcp)
- [ ] Signal definitions do not require logging sensitive data
- [ ] Validation steps are explicit and repeatable
- [ ] Any changes that affect governance/sensitivity are marked **requires human review**

## 🗂️ Directory Layout

### This document
- `path`: `docs/telemetry/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Telemetry docs | `docs/telemetry/` | Human-readable standards and indexes for telemetry |
| Telemetry schemas | `schemas/telemetry/` | JSON Schemas for telemetry payloads |
| Pipelines | `src/pipelines/` | Telemetry producers for ETL/catalog/graph builds |
| APIs | `src/server/` | Telemetry for contracted endpoints and redaction behavior |
| Frontend | `web/` | UX telemetry for Focus Mode and audit panel interactions |
| MCP runs | `mcp/runs/` | Run bundles, logs, experiment metadata (if applicable) |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 telemetry/
    ├── 📄 README.md
    ├── 📄 SIGNALS.md              # not confirmed in repo (recommended index of signals)
    ├── 📄 SCHEMAS.md              # not confirmed in repo (recommended schema map)
    ├── 📄 GOVERNANCE_NOTES.md     # not confirmed in repo (review triggers, redaction rules)
    └── 📄 CHANGELOG.md            # not confirmed in repo (telemetry changes, SemVer notes)

📁 schemas/
└── 📁 telemetry/
    ├── 📄 README.md               # not confirmed in repo (schema index + ownership)
    └── 📁 v1/
        ├── 📄 telemetry.event.schema.json   # not confirmed in repo
        └── 📄 telemetry.metric.schema.json  # not confirmed in repo
~~~

## 🧭 Context

### Background
KFM’s canonical pipeline requires strong provenance and deterministic processing. Telemetry provides:
- operational visibility (did a run succeed, what validations failed),
- governance visibility (did redaction occur, was content served with provenance),
- quality visibility (schema checks, integrity checks, contract tests).

### Assumptions
- Telemetry documentation is stored under `docs/telemetry/`, and schema definitions live under `schemas/telemetry/` (as a canonical pairing).  
- Telemetry is cross-cutting, i.e., every pipeline stage may emit telemetry.

### Constraints and invariants
- Canonical ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumes data through the API layer (no direct graph access).
- Telemetry must not introduce leakage of secrets or sensitive locations.
- Telemetry events that involve sensitivity decisions must record *that a redaction occurred*, not the raw sensitive value.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What telemetry schema set is v1 baseline for this repo? | TBD | TBD |
| Where are telemetry events stored/aggregated at runtime? | TBD | TBD |
| What is the minimal signal set required for “v12-ready” CI? | TBD | TBD |

### Future extensions
- Telemetry dashboards / audit reports linked from this directory (not confirmed in repo)
- Focus Mode “audit panel” telemetry standardization for citations and warnings (not confirmed in repo)
- Energy/carbon telemetry for workloads (mentioned as an extension area; not confirmed in repo)

## 🗺️ Diagrams

### System and telemetry dataflow diagram
~~~mermaid
flowchart LR
  subgraph Pipeline
    A[ETL] --> B[STAC/DCAT/PROV Catalogs]
    B --> C[Neo4j Graph]
    C --> D[APIs]
    D --> E[React/Map UI]
    E --> F[Story Nodes]
    F --> G[Focus Mode]
  end

  A --> T[Telemetry Events]
  B --> T
  C --> T
  D --> T
  E --> T
  F --> T
  G --> T

  T --> S[Schemas: schemas/telemetry/]
  T --> H[Docs: docs/telemetry/]
~~~

## 📦 Data and Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Telemetry event payloads | JSON | Pipeline/API/UI producers | JSON Schema in `schemas/telemetry/` |
| CI telemetry summaries | JSON/Markdown | CI workflows | Markdown + schema validation (where applicable) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Telemetry documentation | Markdown | `docs/telemetry/` | KFM-MDP governed docs |
| Telemetry schemas | JSON Schema | `schemas/telemetry/` | SemVer + schema lint |
| Optional run summaries | Markdown/JSON | `mcp/runs/` | Repo conventions (TBD) |

### Sensitivity and redaction
Telemetry must never require:
- raw secrets (tokens/keys),
- raw user identifiers (PII),
- sensitive location coordinates.

Telemetry may include:
- boolean flags (e.g., `redaction_applied: true`),
- stable internal run identifiers,
- counts/aggregates (e.g., “items processed”, “errors by type”).

### Quality signals
Recommended telemetry quality checks (examples; not confirmed as implemented):
- payload validates against the referenced schema version
- required IDs present (run_id, dataset_id, stac_item_id, prov_activity_id) when applicable
- timestamps are present and ISO-8601 formatted
- geometry is never emitted in telemetry unless explicitly governed

## 🌐 STAC, DCAT and PROV Alignment

Telemetry events should include **references** (not copies) to catalog and lineage artifacts:
- STAC: include STAC Collection/Item IDs when a signal pertains to catalog creation/validation.
- DCAT: include dataset identifier when signal pertains to dataset-level changes.
- PROV-O: include provenance activity/run identifiers for transforms and builds.

Versioning expectations:
- Telemetry schema versions follow SemVer and are referenced in each event payload.
- New schema versions must be backward compatible or require an explicit version bump.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Telemetry producers | Emit events/metrics | Code in pipeline/API/UI subsystems |
| Schema validators | Validate payload shape | JSON Schemas in `schemas/telemetry/` |
| Governance reviewers | Ensure compliance | `docs/governance/*` (not confirmed in repo) |
| CI checks | Fail builds on invalid telemetry artifacts | GitHub workflows (not confirmed in repo) |

### Interfaces and contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Telemetry event schema | `schemas/telemetry/` | SemVer + changelog recommended |
| Telemetry docs | `docs/telemetry/` | Governed docs, link to schemas |
| CI validation | `.github/workflows/` | Contract tests must pass |

### Extension points checklist
- [ ] Add a new telemetry signal: update `docs/telemetry/SIGNALS.md` (recommended) and schema (if needed)
- [ ] Add a new schema version: place under `schemas/telemetry/v<major>/` and document changes
- [ ] Add pipeline stage telemetry: ensure run IDs and provenance references are included
- [ ] Add UI telemetry: ensure aggregation-only and no PII

## 🧠 Story Node and Focus Mode Integration

Telemetry may be used to confirm that Focus Mode behavior remains provenance-linked:
- when a narrative is displayed, the payload should record which evidence references were available (IDs only)
- when redaction/generalization is applied, log a non-sensitive flag and the policy reference (ID/path only)
- if predictive content is used (opt-in), record that predictions were included and include uncertainty fields (IDs/metrics only)

## 🧪 Validation and CI/CD

### Validation steps
- [ ] Markdown protocol checks for docs under `docs/`
- [ ] JSON schema validation for `schemas/telemetry/`
- [ ] Contract tests for APIs that emit telemetry-relevant responses
- [ ] Security and sovereignty scanning gates where applicable

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate telemetry schemas
# 2) run unit/integration tests
# 3) run doc lint / markdown protocol validation
~~~

### Telemetry signals
This repo has not confirmed a canonical signal catalog yet. Recommended baseline categories:
| Category | Producer(s) | Example purpose |
|---|---|---|
| pipeline.run | ETL/catalog/graph builders | Start/end, counts, warnings |
| catalog.validation | STAC/DCAT/PROV builders | Schema validity, broken links |
| graph.integrity | Graph build | Constraint violations, missing refs |
| api.contract | API layer | Contract-test result, response shape |
| ui.audit | UI / Focus Mode | Citation rendered, warnings shown (no PII) |

## ⚖ FAIR+CARE and Governance

### Review gates
Telemetry changes should be flagged for review when they:
- add new fields that could leak sensitive location or identity
- expand logging around restricted datasets
- affect the audit panel and provenance visibility

### CARE and sovereignty considerations
- Telemetry must not be a backchannel for sensitive location disclosure.
- Redaction/generalization actions should be observable, but not reversible from telemetry alone.

### AI usage constraints
This document does not authorize any prohibited AI transformations. Telemetry must not encourage:
- speculative additions
- inference of sensitive locations
- generation of new policy outside governed docs

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial telemetry README scaffold | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`