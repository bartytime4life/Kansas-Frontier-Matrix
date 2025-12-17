---
title: "Agent Spec — <agent_id>"
path: "docs/agents/specs/<agent_id>.md"
version: "v1.0.0-draft"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "AgentSpec"
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

doc_uuid: "urn:kfm:doc:agents:specs:<agent_id>:v1.0.0-draft"
semantic_document_id: "kfm-agent-spec-<agent_id>-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:agents:specs:<agent_id>:v1.0.0-draft"
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

# Agent Spec — <agent_id>

## 📘 Overview

### Purpose
- Define the responsibilities, boundaries, and expected outputs of agent `<agent_id>` within KFM.
- Make agent behavior auditable and reviewable (governance-first, docs-first).
- Provide a stable contract for contributors and maintainers to understand what this agent may (and may not) do.

### Scope

| In Scope | Out of Scope |
|---|---|
| Agent identity + ownership | Runtime deployment details (unless documented elsewhere) |
| Allowed tasks + deliverables | Any “auto-merge” or bypass of review/governance |
| Allowed tools + access boundaries | Secrets, credentials, private keys, tokens |
| Input/Output contract (formats, schemas) | Making policy (must only reference existing governed policy docs) |
| Provenance + citation expectations | Inferring or disclosing sensitive locations |

### Audience
- Primary: KFM maintainers, reviewers, governance stakeholders
- Secondary: Contributors authoring or updating agents, CI/CD maintainers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - Agent spec
  - Tool access
  - Provenance / lineage
  - Redaction / generalization
  - Focus Mode
  - Story Node

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Agent registry overview | `docs/agents/README.md` | TBD | Directory entrypoint |
| Agent specs index | `docs/agents/specs/README.md` | TBD | Lists available agents + IDs |
| Assets rules | `docs/agents/specs/_assets/README.md` | TBD | Docs-only assets guidance |
| This agent spec | `docs/agents/specs/<agent_id>.md` | TBD | This file |
| Governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Governs structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | KFM Core | Use when agent outputs Story Nodes |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (path/title/version/status)
- [ ] Agent `<agent_id>` is uniquely defined and referenced in `docs/agents/specs/README.md`
- [ ] Allowed tasks and prohibited actions are explicit and non-contradictory
- [ ] Tool access matrix is complete and least-privilege
- [ ] Provenance + citation expectations are explicit for any output that can reach Focus Mode
- [ ] Sensitivity and sovereignty considerations are explicit
- [ ] Validation steps listed and repeatable (no “trust me” steps)

## 🗂️ Directory Layout

### This document
- `path`: `docs/agents/specs/<agent_id>.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Agents | `docs/agents/` | Agent docs, indices, governance notes for agent work |
| Agent specs | `docs/agents/specs/` | One spec per agent ID |
| Spec assets | `docs/agents/specs/_assets/` | Docs-only assets referenced by specs |
| Documentation templates | `docs/templates/` | Governed templates (universal, story node, API contract) |
| MCP artifacts | `mcp/` | Model cards, experiments, run logs (if applicable) |

### Expected file tree for this sub-area
~~~text
📁 docs/
└─📁 agents/
  ├─📄 README.md
  └─📁 specs/
    ├─📄 README.md
    ├─📄 <agent_id>.md
    └─📁 _assets/
      └─📄 README.md
~~~

## 🧭 Context

### Background
KFM uses a governed pipeline where outputs must remain reproducible, provenance-linked, and safe to publish. This agent spec exists to ensure that any “agent-like” contributor (human or automated) behaves within KFM’s governance boundaries and does not bypass contracts or sensitivity rules.

### Assumptions
- Agent outputs are reviewable artifacts (docs, proposed diffs, analyses), not autonomous production changes.
- If an agent’s output influences UI-facing narratives, provenance is mandatory and speculative additions are disallowed.
- The canonical pipeline ordering remains intact:
  - ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode

### Constraints / invariants
- Frontend consumes contracts via APIs (no direct graph access assumptions in UI artifacts).
- No unsourced narrative is introduced into Focus Mode contexts.
- Sensitive information must be redacted/generalized per governance and sovereignty requirements.
- No credentials/secrets are stored in agent specs or referenced as plaintext.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the runtime/orchestrator for agents defined (if any)? | TBD | TBD |
| Is there a machine-readable agent registry schema? | TBD | TBD |
| What is the standard evaluation harness for agent outputs? | TBD | TBD |

### Future extensions
- Define a machine-readable `schemas/agents/agent_spec.schema.json` (if/when governed).
- Add a consistent “agent run log” format under `mcp/runs/` (if/when governed).
- Add contract tests that verify each agent spec passes front-matter and lint rules.

## 🗺️ Diagrams

### System / dataflow diagram (agent contributions within KFM’s governed flow)
~~~mermaid
flowchart LR
  Request["Contributor request"] --> Agent["Agent <agent_id>"]
  Agent --> Draft["Draft output (docs / patches / analysis)"]
  Draft --> Review["Review (governance + maintainers)"]
  Review --> Merge["Merge (if approved)"]
  Merge --> Downstream["Downstream pipeline (as applicable)"]
~~~

### System / dataflow diagram (docs-only asset lifecycle for agent specs)
~~~mermaid
flowchart LR
  Author["Contributor"] --> Spec["Agent spec (Markdown)"]
  Author --> Asset["Spec assets folder (docs/agents/specs/_assets)"]
  Spec -->|references| Asset
  Spec --> Review["Review (governance, redaction, licensing)"]
  Asset --> Review
  Review --> Merge["Merge"]
  Merge --> Render["Docs render (GitHub or site)"]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| User/contributor request | Text | Issues/PRs/chat | Must be recorded/linked if used |
| Repo artifacts | Files | `docs/`, `schemas/`, `src/` | Must reference exact paths/versions |
| Datasets (if referenced) | STAC/DCAT/PROV IDs | `data/stac/` + catalog docs | IDs must resolve to catalog entries |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Agent spec updates | Markdown | `docs/agents/specs/<agent_id>.md` | KFM governed doc template |
| Supporting diagrams/assets | PNG/SVG/PDF | `docs/agents/specs/_assets/` | Docs-only assets rules |
| Suggestions for code/schema changes | Text / diff snippets | PR description / issue | Must point to governed templates/contracts |

### Sensitivity & redaction
- If the agent may touch content that includes:
  - sensitive site coordinates
  - culturally sensitive narratives
  - restricted archival material
  - personal data
  then this spec must state the generalization/redaction behavior and required review gates.
- Do not encode sensitive locations directly in examples; use placeholders and generalized coordinates.

### Quality signals
- Reproducibility: steps should be replayable; avoid ambiguous instructions.
- Traceability: reference dataset/document identifiers rather than prose-only attributions.
- Determinism: if computations are described, state seed/version pinning expectations.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If the agent references datasets, it must use resolvable STAC Item/Collection IDs (no invented IDs).
- If the agent produces new derived data artifacts, it must route them through:
  - ETL → catalog generation → graph ingestion (if applicable), preserving the canonical order.

### DCAT
- If the agent updates dataset descriptions, it must maintain license and publisher/contact mapping as governed by DCAT profile.

### PROV-O
- If the agent claims an output is “derived”, the spec must require a provenance trail:
  - `prov:wasDerivedFrom` (inputs)
  - `prov:wasGeneratedBy` (activity/run)
  - agent identity attribution (human/org/software agent), if captured by the system

### Versioning
- Any agent-driven change to catalog/graph/API/UI contracts must respect backward compatibility rules for the affected subsystem.

## 🧱 Architecture

### Agent identity
| Field | Value |
|---|---|
| Agent ID | `<agent_id>` |
| Display name | `TBD` |
| Owner / maintainer | `TBD` |
| Status | `draft / active / deprecated` |
| Primary pipeline stage(s) | `TBD` |
| Model/runtime | `TBD (not confirmed in repo)` |

### Responsibilities
- R1: `TBD`
- R2: `TBD`
- R3: `TBD`

### Explicit non-goals / prohibited actions
- Do not claim to execute code, deploy services, or modify infrastructure.
- Do not bypass governance/review steps.
- Do not invent dataset IDs, citations, or provenance.
- Do not infer or reveal sensitive locations.

### Tool access matrix (least privilege)
| Tool / capability | Allowed | Constraints |
|---|---:|---|
| Read repo docs | TBD | Must cite exact file paths |
| Read schemas | TBD | Must not “invent” fields; follow governed schemas |
| Generate Markdown docs | Yes | Must follow KFM templates + fencing rules |
| Propose code changes | TBD | Output must be reviewable (patch snippet) |
| Web browsing | TBD | If allowed, must cite sources and avoid policy invention |
| Running pipelines | No | Out of scope; human/CI executed only |

### Input contract (example)
~~~yaml
agent_request:
  agent_id: "<agent_id>"
  user_intent: "TBD"
  inputs:
    - path: "TBD"
      kind: "doc|schema|code|data"
  constraints:
    - "no_sensitive_location_inference"
    - "no_policy_generation"
  expected_outputs:
    - "TBD"
~~~

### Output contract (example)
- Primary deliverable(s):
  - Markdown doc(s) under `docs/` (commit-ready)
  - Optional: patch snippets as fenced text (no secrets)
- If producing Story Nodes: must use `docs/templates/TEMPLATE__STORY_NODE_V3.md` and require dataset/document IDs per claim.

## 🧠 Story Node & Focus Mode Integration

- If `<agent_id>` generates or edits Story Nodes:
  - every factual claim must map to a dataset/document ID
  - include provenance references (STAC/DCAT/PROV) and avoid speculation
- If `<agent_id>` influences Focus Mode outputs:
  - ensure content is provenance-linked and auditable
  - ensure sensitivity redactions are applied before UI exposure

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] Front-matter conforms to governed keys and `path` matches file location
- [ ] Mermaid diagrams render (no illegal characters; keep node labels simple)
- [ ] Links to other repo paths are valid
- [ ] No prohibited AI actions implied (policy generation, sensitive location inference)
- [ ] Tool access matrix is least-privilege and consistent with responsibilities

### Validation commands
- `not confirmed in repo`: add the canonical lint/validation commands used by KFM CI once located.

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- FAIR+CARE council review: `TBD`
- Security council review: `TBD`
- Historian/editor review: `TBD`

### Governance triggers
- Any handling of restricted/sensitive locations
- Any narrative content intended for UI/Focus Mode
- Any license/rights changes for referenced assets
- Any contract change affecting APIs, schemas, or ontology

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-17 | Initial agent spec scaffold | TBD |
