---
title: "Telemetry Schemas"
path: "schemas/telemetry/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:schemas:telemetry:readme:v1.0.0"
semantic_document_id: "kfm-schemas-telemetry-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:schemas:telemetry:readme:v1.0.0"
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

# Telemetry Schemas

## 📘 Overview

### Purpose

- Define what belongs in `schemas/telemetry/` and how it pairs with `docs/telemetry/` (human-readable signal docs).
- Establish minimum expectations for telemetry schema versioning, validation, and governance review.

### Scope

| In Scope | Out of Scope |
|---|---|
| JSON Schemas for telemetry payloads (“signals”) emitted by KFM components (UI, API, ETL/pipelines, CI) | Collector/agent infrastructure (APM vendors, log sinks), dashboards, alerting |
| Contract discipline: schema-defined + documented signals; schema evolution managed intentionally | User tracking, PII capture, or any non-anonymized telemetry |
| Auditability: what is collected is explicitly documented | Operational runbooks for telemetry backends (belongs under `docs/ops/` or `tools/` if present) |

### Audience

- Primary: contributors adding/changing telemetry signals and payloads.
- Secondary: reviewers/auditors verifying minimization, anonymization, and compliance.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: telemetry signal, event schema, schema version (SemVer), contract test, audit log, redaction.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Telemetry signal docs | `docs/telemetry/` | TBD | Human-readable “what we collect” inventory + per-signal rationale |
| Telemetry JSON Schemas | `schemas/telemetry/` | TBD | Machine-validated contracts for telemetry payloads |
| Master system guide | `docs/MASTER_GUIDE_v12.md` | KFM core team | Canonical pipeline + system inventory |
| Architecture vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture team | Describes telemetry as documented + schema-defined |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture team | Contracts-first constraints; schema validation in CI |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Telemetry signals listed in this README match files in `docs/telemetry/` + `schemas/telemetry/`
- [ ] Each telemetry schema change has an explicit version bump + changelog entry (location: TBD)
- [ ] Validation steps listed and repeatable (local + CI)
- [ ] Governance + CARE/sovereignty considerations explicitly stated for any new/changed fields

## 🗂️ Directory Layout

### This document

- `path`: `schemas/telemetry/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Telemetry docs | `docs/telemetry/` | Signal definitions, rationale, “what is collected” statements |
| Telemetry schemas | `schemas/telemetry/` | JSON Schemas for telemetry payloads (this folder) |
| APIs | `src/server/` | API boundary; any telemetry ingestion endpoints (if used) live here |
| UI | `web/` | Telemetry producers in the frontend (if used) |
| Pipelines | `src/pipelines/` | Pipeline telemetry producers (run duration, failures, etc.) |
| Governance | `docs/governance/` | FAIR+CARE, ethics, sovereignty policies + review gates |
| CI | `.github/` | Validation gates (schema checks, doc lint, tests) |

### Expected file tree for this sub-area

~~~text
📁 schemas/
└── 📁 telemetry/
    ├── 📄 README.md
    ├── 📄 focus_mode_event.json                 (example from architecture docs; may not exist yet)
    └── 📄 <signal_schema>.json                  (one file per signal; naming convention TBD)
~~~

## 🧭 Context

### Background

- Telemetry is treated as a first-class interface contract: operational signals collected are **documented and schema-defined** and stored in logs intended to support audit.
- Telemetry is expected to support observability, security, and governance metrics, without compromising privacy.

### Assumptions

- Telemetry payloads are JSON and validated with JSON Schema.
- Each signal has a matching Markdown description in `docs/telemetry/`.

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- UI must not read Neo4j directly; all graph access is via the API layer.
- Telemetry remains anonymized; do not add personal identifiers to signal payloads.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the minimum telemetry schema set required for “CI green” (v13 contracts gate)? | Contracts owners | v13.0.0 |
| Where is the canonical telemetry schema changelog stored (per “SemVer + changelog” rule)? | TBD | TBD |
| Do we standardize a common telemetry event envelope (shared fields across all signals)? | TBD | TBD |

### Future extensions

- Add schemas for additional operational metrics (ETL duration, API latency) and security/governance audit signals.
- Add a telemetry schema “registry” file if signal discovery becomes difficult (not confirmed in repo).

## 🗺️ Diagrams

### System / telemetry dataflow diagram (conceptual)

~~~mermaid
flowchart LR
  UI[web/ (UI)] -->|emit signal| V[Schema validation\n(schemas/telemetry)]
  API[src/server/ (API)] -->|emit signal| V
  ETL[src/pipelines/ (ETL)] -->|emit signal| V
  V --> L[Append-only logs\n(location TBD)]
  L --> A[Audit / governance review]
~~~

### Optional: sequence diagram (conceptual)

~~~mermaid
sequenceDiagram
  participant Producer as Producer (UI/API/ETL)
  participant Validator as Schema Validator
  participant Log as Telemetry Log (append-only)

  Producer->>Validator: Emit event payload (JSON)
  Validator-->>Producer: Accept/Reject (schema)
  Validator->>Log: Write validated event
  Log-->>Validator: ACK
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Telemetry event payloads (“signals”) | JSON | UI / API / ETL components | JSON Schema under `schemas/telemetry/` |
| Telemetry signal documentation | Markdown | `docs/telemetry/` | Markdown protocol validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validated telemetry events | JSON lines / log entries | (location TBD) | Corresponding schema in `schemas/telemetry/` |
| Telemetry collection inventory | Markdown | `docs/telemetry/` | Signal docs + this README |

### Sensitivity & redaction

- Telemetry is intended to be **fully anonymized** and should not include personal identifiers.
- If a signal needs to reference a system object, prefer stable non-person identifiers (e.g., `story_id`, `run_id`) and apply redaction/generalization rules where required by governance policy.

### Quality signals

- Schemas should prevent “silent drift” (required fields, types, `additionalProperties` policy).
- CI should fail if a signal doc references a missing schema file, or if a schema is invalid (mechanism TBD).

## 🌐 STAC, DCAT & PROV Alignment

Telemetry schemas are not STAC/DCAT outputs, but they can reference pipeline provenance where appropriate.

### STAC

- Not applicable (telemetry is not a catalog artifact).

### DCAT

- Not applicable (telemetry signals are not published datasets by default).

### PROV-O

- Recommended (not confirmed in repo): when telemetry describes an ETL/API action, include a pointer to the relevant PROV activity/run identifier so telemetry can be audited alongside provenance bundles under `data/prov/`.

### Versioning

- Telemetry schemas follow the same rule as other JSON schemas: **semantic versioning** with a maintained changelog.
- Any breaking change to a telemetry payload schema requires a version bump and (if applicable) parallel support for older schema versions until consumers migrate.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Telemetry producers | Emit signal payloads at runtime | Schema-defined JSON payloads |
| Telemetry schema set | Define and validate payload contracts | `schemas/telemetry/*.json` |
| Telemetry documentation | Describe what is collected and why | `docs/telemetry/*.md` |
| Storage / logging | Persist telemetry for audit | Append-only logs (location TBD) |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Telemetry JSON schemas | `schemas/telemetry/` | SemVer + changelog |
| Signal documentation | `docs/telemetry/` | Must stay in sync with schema |

### Extension points checklist (telemetry-specific)

- [ ] Add/modify signal doc in `docs/telemetry/`
- [ ] Add/modify JSON schema in `schemas/telemetry/` **with version bump**
- [ ] Update CI validation/contract tests (location TBD)
- [ ] Confirm governance review triggers if new fields touch sensitive domains

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Telemetry may record **anonymous** usage signals related to Focus Mode entry/exit and story navigation to help assess adoption and performance.
- Telemetry must not be used to generate or alter narrative content; Story Nodes remain provenance-linked and evidence-first.

### Provenance-linked narrative rule

- Unchanged: published narratives must remain evidence-backed; telemetry is operational metadata only.

### Optional structured controls

- Not applicable.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks for `schemas/telemetry/README.md` (and `docs/telemetry/*.md`)
- [ ] JSON Schema validation for `schemas/telemetry/*.json`
- [ ] Optional: contract tests validating sample events against schemas (recommended; location TBD)
- [ ] Security and sovereignty checks for any new fields that could be sensitive

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate JSON schemas
# <tooling TBD>

# 2) run contract tests for telemetry payloads
# <tooling TBD>

# 3) run doc lint / markdown protocol validation
# <tooling TBD>
~~~

### Telemetry signals

| Signal | Source | Where recorded | Notes |
|---|---|---|---|
| FocusModeEnter (example) | Frontend UI event | `docs/telemetry/focus_mode_events.md` + `schemas/telemetry/focus_mode_event.json` | Example signal referenced in architecture docs; do not include personal info |

## ⚖ FAIR+CARE & Governance

### Review gates

- Any telemetry schema change that introduces potentially sensitive fields (PII, culturally sensitive locations, etc.) requires governance review per:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/ETHICS.md`
  - `docs/governance/SOVEREIGNTY.md`

### CARE / sovereignty considerations

- Avoid collecting or emitting telemetry that could infer sensitive locations or protected community information.
- Prefer aggregated, anonymized signals and document exactly what is collected and why.

### AI usage constraints

- This document inherits its AI transform permissions/prohibitions from front-matter.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial telemetry schemas README | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

