---
title: "Agents — Runbooks (README)"
path: "docs/agents/runbooks/README.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:agents:runbooks:readme:v1.0.0"
semantic_document_id: "kfm-agents-runbooks-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:agents:runbooks:readme:v1.0.0"
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

# Agents — Runbooks (README)

## 📘 Overview

### Purpose
This folder contains **runbooks**: step-by-step operational procedures for executing and troubleshooting agent-driven (or human-assisted) tasks across the KFM pipeline. Runbooks are intended to be **deterministic, auditable, and governance-aware**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Operational steps for repeatable tasks (ETL runs, catalog validation, graph loads, API contract checks, story node publication workflows) | “How the agent is implemented” (belongs in `docs/agents/specs/`) |
| Safety, redaction, licensing, and escalation steps | Policy creation (handled by governance docs; this area references them) |
| Validation steps (what “done” means) | Secrets/credentials or any non-redacted sensitive information |

### Audience
- Primary: contributors operating the pipeline (maintainers, data stewards, reviewers).
- Secondary: agent authors who need an executable operational contract to target.

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo; create if missing)*  
- Terms used in this doc:
  - **Runbook**: a documented, repeatable procedure with explicit preconditions, steps, validation, and rollback.
  - **Agent spec**: the contract describing an agent’s responsibilities and interfaces (see `docs/agents/specs/`).
  - **Evidence artifacts**: outputs (logs, reports, derived data) that support a claim about successful execution.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical stage order + invariants |
| Agent specifications | `docs/agents/specs/` | Agent maintainers | Contract for behavior and inputs/outputs |
| Agent assets | `docs/agents/specs/_assets/` | Agent maintainers | Diagrams/images used by specs/runbooks |
| Runbooks (this area) | `docs/agents/runbooks/` | Operators + maintainers | Operational procedures and checklists |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory intent and boundaries are clear
- [ ] File tree indicates where new runbooks should live
- [ ] A “runbook format” is defined (so all runbooks are consistent)
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/agents/runbooks/README.md` (must match front-matter)

### Related repository paths (common touchpoints)
| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs (this runbook set is docs-only) |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog build + graph build |
| Schemas | `schemas/` | JSON schemas, telemetry schemas, contract schemas |
| Tests | `tests/` | Pipeline and contract tests |
| MCP | `mcp/` | Experiments, model cards, SOPs (if agents use models) |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 agents/
    ├── 📄 README.md
    ├── 📁 specs/
    │   ├── 📄 README.md
    │   ├── 📁 _assets/
    │   │   └── 📄 README.md
    │   └── 📄 <agent_id>.md
    └── 📁 runbooks/
        ├── 📄 README.md
        ├── 📁 etl/
        │   └── 📄 RB__ETL__<operation>.md
        ├── 📁 catalogs/
        │   └── 📄 RB__CATALOGS__<operation>.md
        ├── 📁 graph/
        │   └── 📄 RB__GRAPH__<operation>.md
        ├── 📁 api/
        │   └── 📄 RB__API__<operation>.md
        └── 📁 ui_story/
            └── 📄 RB__STORY__<operation>.md
~~~

> Notes:
> - Subfolders and naming are **recommended conventions** for discoverability; adjust to existing repo patterns if they differ.
> - Keep runbooks **docs-only**. Any implementation belongs in `src/` and must be referenced, not embedded.

## 🧭 Context

### Background
KFM’s pipeline is staged and governed. When tasks are executed inconsistently (different flags, different validation checks, missing provenance), outputs become hard to reproduce and hard to trust. Runbooks make operational work **repeatable** and make agent behavior **verifiable**.

### Assumptions
- Agents operate under an explicit spec (see `docs/agents/specs/`).
- Runbooks are safe to publish in the open repository (no secrets; no raw sensitive locations; no unredacted PII).
- Any pipeline step described is either:
  - already implemented, or
  - clearly marked as “not confirmed in repo” and treated as a proposal.

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
- Frontend consumption is via APIs (no direct graph access from UI code).
- Runbooks must include **validation + rollback** (or explicitly state why rollback is not applicable).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should runbooks be linted/validated in CI (links + mermaid + front-matter)? | Maintainers | TBD |
| Do we standardize a runbook ID scheme (semantic ID + doc_uuid convention)? | Maintainers | TBD |
| Do we maintain an index file listing all runbooks + owners? | Maintainers | TBD |

### Future extensions
- Add a lightweight “runbook index” generator (docs-only) that lists runbooks, owners, and last_updated.
- Add optional “automation mapping” sections that map runbooks to agent capabilities (without implying autonomous execution).

## 🗺️ Diagrams

### System / dataflow diagram (runbooks in context)
~~~mermaid
flowchart LR
  A["Contributor / Operator"] --> B["Runbook (.md)"]
  B --> C["Execution (human or agent-assisted)"]
  C --> D["Pipeline stage output (data/catalog/graph/api/ui/story)"]
  C --> E["Evidence artifacts (logs/reports/checksums)"]
  E --> F["Review (governance + redaction + licensing)"]
  F --> G["Merge / Release"]
~~~

### Optional: runbook → spec relationship
~~~mermaid
flowchart LR
  S["Agent spec (contract)"] -->|constrains| R["Runbook (procedure)"]
  R -->|produces| O["Outputs + evidence"]
  O -->|must satisfy| S
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Runbook file | Markdown | `docs/agents/runbooks/**` | Front-matter present + links valid |
| Referenced commands/config | Text | `src/`, `tools/`, or `schemas/` | Must be pinned, replayable |
| Source data references | IDs/paths | `data/` / STAC IDs | Must resolve to catalog entries (when required) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Run result evidence | logs / summaries | `mcp/runs/` or `mcp/experiments/` *(preferred)* | (use existing telemetry schema if present) |
| Derived datasets | files | `data/processed/` | STAC item(s) + DCAT + PROV alignment |
| Graph changes | migrations / load outputs | `src/graph/` + evidence logs | Must preserve ontology constraints |

### Sensitivity & redaction
- Do not include raw coordinates or precise locations for sensitive resources; use generalized representations.
- Do not embed credentials, API keys, or tokens.
- If a runbook touches restricted domains, include a “redaction rules” section and refer to governance docs.

### Quality signals
Runbooks should define explicit “green checks,” e.g.:
- schema validation passes
- geometry validity checks
- row counts within expected ranges
- checksums recorded for outputs
- provenance fields present and consistent

## 🌐 STAC, DCAT & PROV Alignment

### STAC
If a runbook produces or modifies datasets:
- It must specify **which STAC Collection/Item(s)** are expected to change or be added.
- It must specify **validation** (validator invocation and expected pass criteria).

### DCAT
If a runbook produces or updates catalog views:
- It must specify dataset identifiers and license mapping expectations.

### PROV-O
If a runbook describes a pipeline execution:
- It must record or reference:
  - `prov:used` inputs
  - `prov:wasGeneratedBy` activity/run identifier
  - timestamps and responsible agent/operator identity (as appropriate for the repo’s policies)

### Versioning
- Runbooks should instruct how to record version/lineage (checksums, run IDs, etc.).
- Runbooks should avoid “floating” dependencies (e.g., “latest model,” “most recent dataset”) unless an explicit pinning mechanism exists.

## 🧱 Architecture

### Runbook format (recommended)
Each runbook should follow a predictable structure (use the Universal template unless a more specific governed template is introduced):

1. **Overview** (what/why, which pipeline stage)
2. **Trigger** (when to run; symptoms)
3. **Preconditions** (access, environment, required inputs)
4. **Procedure** (step-by-step, deterministic)
5. **Validation** (commands/checks + expected results)
6. **Rollback / Recovery** (how to revert or mitigate)
7. **Evidence & logging** (where outputs go; what to capture)
8. **Governance & sensitivity** (redaction, licensing, approvals)
9. **Version history** (what changed in the runbook)

### Example skeleton (for new runbooks)
~~~text
# RB — <Domain> / <Operation>

## Overview
## Trigger
## Preconditions
## Procedure
## Validation
## Rollback / Recovery
## Evidence & logging
## Governance & sensitivity
## Version history
~~~

## 🧠 Story Node & Focus Mode Integration
If a runbook produces narrative artifacts (e.g., story nodes):
- It must enforce evidence-led writing and list required dataset/document IDs.
- It must ensure any claim in a narrative artifact can be traced back through catalogs and provenance.

## 🧪 Validation & CI/CD

### Validation checklist (for every runbook)
- [ ] Commands are copy/paste runnable and deterministic (no hidden state assumptions)
- [ ] References point to repo paths or catalog identifiers (no ephemeral URLs unless required)
- [ ] Evidence capture is defined (where logs live, how to name them)
- [ ] Security/sensitivity notes are explicit
- [ ] Rollback steps exist (or are explicitly “not applicable” with rationale)

### Suggested CI hooks (optional)
- Markdown lint + link check for `docs/agents/runbooks/**`
- Mermaid rendering check (where supported)
- Front-matter key validation against KFM-MDP expectations (if tooling exists)

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- FAIR+CARE council review: **TBD**
- Security council review: **TBD**
- Historian/editor review: **TBD**

> Runbooks that affect restricted/sensitive domains should explicitly list the reviewer role(s) required before execution or publication of outputs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial runbooks README | TBD |
