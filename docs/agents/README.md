---
title: "Agents — Documentation & Governance"
path: "docs/agents/README.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:agents:readme:v1.0.0"
semantic_document_id: "kfm-agents-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:agents:readme:v1.0.0"
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

# Agents — Documentation & Governance

## 📘 Overview

### Purpose
- This README is the entry point for **agent specifications** in KFM.
- It defines how agents are documented so their behavior is **auditable**, **repeatable**, and **reviewable**.
- It standardizes what must be captured for each agent: role, stage alignment, allowed inputs, outputs, provenance expectations, safety constraints, and review gates.

### Scope
| In Scope | Out of Scope |
|---|---|
| Agent role/spec documentation, prompt packages (if stored as docs), operational runbooks, evaluation notes/rubrics, safety/governance constraints, telemetry expectations | Implementing agent code, changing platform governance policy text, storing secrets/credentials, bypassing contracted APIs, publishing sensitive site coordinates |

### Audience
- Contributors defining or updating agents
- Reviewers (governance/security/editorial) validating agent outputs
- Pipeline/API/UI maintainers integrating or consuming agent outputs

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used here:
  - **Agent**: a bounded automation component (LLM-based or rule-based) with defined inputs/outputs and constraints.
  - **Agent Spec**: the governed document describing the agent’s contract and constraints.
  - **Prompt Package**: versioned prompt text (and examples) used by an LLM-based agent.
  - **Run**: a single execution producing outputs with provenance + telemetry.
  - **Evidence Artifact**: structured output intended to support Story Nodes / Focus Mode.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Notes |
|---|---|---|
| Master guide (pipeline invariants + extension matrix) | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering and “Extension Matrix” |
| Universal doc template (default) | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Use for agent specs/runbooks/eval notes unless a narrower template applies |
| Story Node template (narratives) | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Use only for Story Nodes / Focus Mode narrative artifacts |
| API contract template (if agent adds/changes endpoints) | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Required for REST/GraphQL contract changes |
| AI governance reference (if present) | `docs/guides/ai/` | Model cards, governance + explainability expectations |
| Telemetry docs + schemas | `docs/telemetry/` + `schemas/telemetry/` | Required run/audit signals |
| Security docs | `.github/SECURITY.md` + `docs/security/` | Sensitive handling, logging, threat model practices |

### Definition of done (for this directory)
- [ ] Every agent has a spec document (governed template, versioned)
- [ ] Every agent spec states: stage alignment, allowed inputs, outputs, provenance requirements, safety constraints, review gates
- [ ] Any user-facing narrative artifacts are produced only via Story Node conventions (evidence-led + source-linked)
- [ ] Any agent impacting user-facing content has telemetry + audit expectations documented
- [ ] No duplicated policy text—link to governance/security docs instead

## 🗂️ Directory Layout

### This document
- `docs/agents/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Agent documentation | `docs/agents/` | Specs, prompt packages (if documented here), runbooks, eval notes |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL, transforms, catalog build, graph build |
| Catalogs | `data/stac/` + `docs/data/` | STAC/DCAT/PROV generation + mappings |
| Graph | `src/graph/` + `docs/graph/` | Ontology, labels, migrations |
| APIs | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| UI | `web/` + `docs/design/` | Map layers, Focus Mode UX, a11y |
| Story Nodes | `docs/reports/.../story_nodes/` | Narrative artifacts with provenance pointers |
| MCP / experiments | `mcp/` | Experiments, model cards, SOPs, run logs |
| Schemas | `schemas/` | JSON schemas, telemetry schemas |

### Expected file tree for this sub-area
~~~text
docs/agents/
  README.md                         📘 Entry point + conventions for agent documentation
  specs/                            🧩 Agent specifications (one file per agent)
    <agent_id>.md                   🧾 Governed “Agent Spec” (use Universal template)
  prompts/                          🧠 Prompt packages (versioned; if stored in docs)
    <agent_id>/
      system.md                     🧠 System prompt (if used)
      instructions.md               🧠 Operating instructions / guardrails
      examples/                     🧪 Few-shot examples (if allowed)
  runbooks/                         🧪 Operational runbooks (how to run + verify)
    <agent_id>.md
  evaluations/                      📊 Offline/online eval notes + rubrics
    <agent_id>.md
  adr/                              🏛️ Local agent decisions (optional)
    ADR-0001-<topic>.md
~~~

### Agent registry (fill as specs land)
| Agent ID | Spec | Primary Stage(s) | Owner | Status |
|---|---|---|---|---|
| (add) | `docs/agents/specs/<agent_id>.md` | TBD | TBD | TBD |

## 🧭 Context

### Background
KFM’s canonical pipeline is staged and governed: **ETL → STAC/DCAT/PROV catalogs → graph → APIs → UI → Story Nodes → Focus Mode**. Agents must fit into this ordering and must not bypass contracts or governance.

Agents are useful in two common patterns:
- **Dev-time agents**: help with drafting docs, validating schemas, mapping sources to catalog structures, and preparing PR-ready artifacts.
- **Product-facing agents**: synthesize evidence artifacts or explanations used in Focus Mode while preserving provenance and explainability.

### Assumptions
- Agent outputs that affect user-visible behavior or narrative require stronger governance (telemetry, review gates, explainability).
- Agent outputs should not overwrite underlying factual data; they may only propose derived artifacts (with citations/provenance pointers).

### Constraints / invariants
- Preserve canonical pipeline ordering; do not introduce “shortcuts” that skip catalogs/provenance.
- The frontend consumes data only via contracted APIs (no direct graph coupling).
- Agents must not introduce secrets, credentials, or sensitive site coordinates into docs/logs.
- Where sovereignty/sensitive-site rules apply: prefer generalized/redacted representations and document the rule used.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which agents are currently in use (dev and/or product), and where are they invoked? | TBD | TBD |
| What is the minimum telemetry record required for an agent “run”? | TBD | TBD |
| Where should prompts live for runtime use (docs vs source tree)? | TBD | TBD |

### Future extensions
- A standard “Agent Registry” manifest (machine-readable) alongside the human-readable table above.
- A common evaluation harness and regression suite for LLM prompt changes.
- Role-based “virtual expert team” agents (specialists + coordinator) for multi-perspective evidence synthesis.

## 🗺️ Diagrams

### Agents in canonical context
~~~mermaid
flowchart LR
  subgraph Pipeline["Canonical KFM Pipeline"]
    A[ETL] --> B[STAC/DCAT/PROV Catalogs]
    B --> C[Neo4j Graph]
    C --> D[APIs]
    D --> E[React/Map UI]
    E --> F[Story Nodes]
    F --> G[Focus Mode]
  end

  subgraph Agents["Agents (bounded + governed)"]
    X[Dev-time Agents] --> A
    X --> B
    Y[Product-facing Agents] --> D
    Y --> F
    Y --> G
  end

  Agents -. "must not bypass contracts / governance" .-> Pipeline
~~~

## 📦 Data & Metadata

### Inputs
| Input type | Examples | Allowed? | Notes |
|---|---|---:|---|
| Governed docs | `docs/MASTER_GUIDE_v12.md`, templates, standards | ✅ | Prefer linking to canonical docs rather than re-authoring policy text |
| Catalog metadata | STAC/DCAT/PROV assets | ✅ | Must preserve IDs and provenance pointers |
| Graph facts | entity IDs, relationships | ✅ | Must be accessed through contracted services/tools per architecture |
| Unvetted external text | random web text pasted into prompts | ⚠️ | Allowed only if captured as a governed source artifact first |

### Outputs
| Output type | Where it should land | Notes |
|---|---|---|
| Agent spec | `docs/agents/specs/<agent_id>.md` | Governed; versioned |
| Prompt package | `docs/agents/prompts/<agent_id>/...` | Versioned; reviewable; keep examples minimal |
| Runbook | `docs/agents/runbooks/<agent_id>.md` | How to run + validate + rollback |
| Eval notes / rubric | `docs/agents/evaluations/<agent_id>.md` | Define what “good” looks like; include regression checks |
| Run logs / experiments | `mcp/runs/` or `mcp/experiments/` | Include run_id and provenance pointers |

### Sensitivity & redaction
- Treat location-sensitive content as sensitive by default unless explicitly marked otherwise by governance.
- If outputs reference sensitive locations, publish only generalized/redacted geometry and record the redaction rule.

### Quality signals & confidence
- Prefer structured outputs with explicit input references.
- If uncertainty exists, label it (e.g., confidence levels, competing hypotheses) and keep narrative claims evidence-led.

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements
Agents that generate or transform artifacts must:
- Preserve stable identifiers for inputs and outputs.
- Record `prov:used` (inputs), `prov:wasGeneratedBy` (run/activity), and `prov:wasAssociatedWith` (agent/software identity) for each run.
- Provide a run identifier (e.g., `run_id`) that links telemetry, outputs, and catalog/graph lineage.

### STAC Items & Collections touched
- Documentation-only changes: **none**.
- If an agent creates/updates catalog assets, the agent spec must explicitly state which:
  - STAC collections are in scope
  - item ID patterns and versioning expectations
  - required extensions and validation steps

### DCAT fields
- If agent outputs are published as discoverable datasets or distributions, document DCAT mapping in the agent spec (do not invent new fields without governance review).

### PROV bundles and run IDs
- Prefer storing provenance as sidecar bundles (or a linked store) so outputs can be traced and audited across pipeline stages.

## 🧱 Extension Points Checklist

Use this checklist when adding or materially changing an agent. It is derived from KFM’s “Extension Matrix” framing.

| Change type | Data | Catalog | Graph | API | UI | Story/Focus | Telemetry |
|---|---:|---:|---:|---:|---:|---:|---:|
| Dev-time agent (docs / validation only) | — | — | — | optional | — | — | optional |
| Product agent producing evidence artifacts | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Narrative agent producing Story Nodes | optional | optional | ✓ | ✓ | ✓ | ✓ | ✓ |
| New governance/security gate | — | — | — | — | — | — | ✓ |

## 🧠 Story Node & Focus Mode Integration

### Focus Mode touchpoints
If an agent’s outputs appear in Focus Mode:
- Outputs must be citeable (link back to source artifacts or catalog entries).
- Outputs must support explainability (what inputs contributed; what rules were applied).
- The UI should be able to display governance flags (e.g., redaction applied, sensitivity notices).

### Story Node expectations
- Story Nodes are evidence-led; narrative claims should map back to dataset/document IDs and provenance pointers.
- Use the Story Node template for story artifacts; do not embed Story Node narratives inside agent specs.

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] Agent spec uses a governed template and has valid front-matter
- [ ] Stage alignment is explicit and matches canonical pipeline ordering
- [ ] Inputs/outputs are typed; allowed inputs are scoped to governed artifacts
- [ ] Review gates are defined (especially for user-facing outputs)
- [ ] Telemetry requirements are documented for runs
- [ ] No secrets/credentials or sensitive coordinates are present

### CI expectations (project-level)
- Docs and schema changes are expected to be validated by CI checks (documentation standards, schema validation, and governance policy checks as applicable).

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- FAIR+CARE council review: **required** when an agent generates user-facing interpretations or prioritizations affecting sensitive domains.
- Security review: **required** when an agent changes logging/telemetry, touches authentication/authorization, or handles sensitive locations.
- Historian/editor review: **required** when an agent proposes narrative content intended for publication.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial README for `docs/agents/` | TBD |

## 🔚 Footer References
- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- `docs/governance/ROOT_GOVERNANCE.md`
- `.github/SECURITY.md`
