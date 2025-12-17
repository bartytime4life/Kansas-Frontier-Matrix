---
title: "KFM Agents — README"
path: "docs/agents/README.md"
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

# KFM Agents — README

## 📘 Overview

### Purpose
This directory (`docs/agents/`) contains **governed documentation** for AI/automation “agents” used in the Kansas Frontier Matrix (KFM) system: what they do, what they are allowed to do, what they consume/produce, and how their outputs remain provenance-linked and reviewable.

This README defines the **minimum documentation contract** for any agent-related contribution (design, runbook, evaluation, or prompt asset).

### Scope
| In Scope | Out of Scope |
|---|---|
| Agent role/spec documentation (capabilities, constraints, I/O) | Implementing agent code (belongs under `src/`) |
| Safety, redaction, and governance notes for agent outputs | Publishing new public-facing endpoints without an API contract doc |
| Evaluation plans (benchmarks, regression tests, red-team notes) | Storing secrets, credentials, or sensitive location details in docs |
| Runbooks for operating agents and reviewing outputs | Replacing human review where governance requires it |

### Audience
- Primary: Contributors designing or implementing agent workflows (AI, data engineering, frontend, and platform).
- Secondary: Maintainers/reviewers (governance, security, sovereignty/CARE, domain experts).

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: **agent**, **agent run**, **evidence artifact**, **specialist agent**, **coordinator/fusion agent**, **context bundle**, **Story Node**, **Focus Mode**, **redaction/generalization**.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (system source of truth) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Pipeline ordering + subsystem contracts |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Use for most agent docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Editorial/Governance | Required for narrative Story Nodes |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API Maintainers | Required if an agent adds/changes an endpoint |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review triggers + authority |
| Ethics | `docs/governance/ETHICS.md` | Governance | Narrative and model behavior constraints |
| Sovereignty / CARE | `docs/governance/SOVEREIGNTY.md` | Governance | Restricted locations + community protections |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Clear definition of what “agents” means in KFM (and what it does *not* mean)
- [ ] Concrete contribution rules (what to document, where to put it)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/agents/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Governed docs | `docs/` | System documentation, templates, runbooks |
| Agent docs | `docs/agents/` | Agent specs, runbooks, eval plans, prompt assets |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/telemetry/etc.) |
| Code | `src/` | Implementation code (agents belong here, not in `docs/`) |
| Derived data | `data/processed/` | Reproducible outputs + artifacts (not source code) |
| Run logs / experiments | `mcp/runs/`, `mcp/experiments/` | Repeatable experiment logs, evaluations, run IDs |
| Tests | `tests/` | Contract/integration tests (API, graph, schemas) |
| Web UI | `web/` | React/MapLibre UI (consumes APIs, not graph directly) |

### Expected file tree for this sub-area
~~~text
docs/
└── 📁 agents/
    ├── 📄 README.md
    ├── 📁 specs/                 # Agent role specs + I/O contracts (add as needed)
    ├── 📁 runbooks/              # Operational runbooks + review workflows (add as needed)
    ├── 📁 eval/                  # Benchmarks + regression tests + red-team notes (add as needed)
    ├── 📁 prompts/               # Governed prompt assets (no secrets; avoid sensitive locations)
    └── 📁 diagrams/              # Mermaid sources / exports (optional)
~~~

## 🧭 Context

### Background
KFM is documentation-first and pipeline-governed. “Agents” are useful when they improve repeatability and reviewability (e.g., triage, evidence synthesis, structured extraction, multi-perspective analysis), but they must remain **bounded by KFM’s contracts**: provenance-first, schema-validated, and safe for sensitive geographies and communities.

A common pattern is **role-based (specialist) analysis**: multiple agents (or modules) each provide a perspective (historical texts, terrain, environment), and a coordinator/fusion step reconciles results into an evidence-backed output.

### Assumptions
- Agents may be LLM-based, non-LLM, or hybrid; the documentation requirements apply either way.
- Agent outputs that influence user-facing narratives must be explainable and provenance-linked.
- Human review remains required where governance or safety dictates it.

### Constraints / invariants
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV catalogs → graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI must not bypass APIs (no direct graph access).
- Any sensitive or restricted locations must be generalized/redacted per sovereignty rules.
- “Predictive” or uncertain outputs must be clearly labeled and must not be treated as confirmed facts without review.

### Open questions
| Question | Owner | Target milestone | Notes |
|---|---|---|---|
| Where is the canonical agent registry (names, IDs, owners, allowed inputs/outputs)? | TBD | TBD | Recommend a single source-of-truth file under `docs/agents/` or `schemas/` |
| What is the standard format for agent run IDs (to map cleanly into PROV)? | TBD | TBD | Align with `prov:Activity` identifiers |
| What evaluations are required before an agent can write Story Nodes or feed Focus Mode? | TBD | TBD | Define minimum regression + red-team gates |

### Future extensions
- Add a governed **agent spec template** under `docs/agents/specs/` (Universal doc template) with: role, permissions, inputs/outputs, provenance behavior, and redaction rules.
- Add a lightweight **agent registry** (YAML/JSON) that is schema-validated in CI.
- Add evaluation harnesses that test for: provenance completeness, hallucination resistance, redaction correctness, and narrative neutrality.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  DS[External data sources] --> ETL[ETL / transforms]
  ETL --> CAT[STAC/DCAT/PROV catalogs]
  CAT --> G[Knowledge graph]
  G --> API[APIs]
  API --> UI[UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]

  subgraph Agentic[Optional agentic workflows]
    SA[Specialist agent(s)] --> CO[Coordinator / fusion]
  end

  CAT --> SA
  G --> SA
  CO --> EA[Evidence artifacts]
  CO --> SN
  EA --> CAT
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Analyst as Analyst/Contributor
  participant Agent as Agent runner
  participant API as KFM API layer
  participant Catalog as STAC/DCAT/PROV
  participant Docs as Story Node / Docs

  Analyst->>Agent: Run agent with a scoped question + inputs
  Agent->>API: Fetch contracted, redacted context bundle
  API-->>Agent: Provenance-linked facts + refs
  Agent->>Catalog: Emit evidence artifact + PROV activity record
  Agent->>Docs: Draft Story Node (if applicable)
  Analyst->>Docs: Review / edit / accept
~~~

## 📦 Data & Metadata

### Inputs
| Input | Required? | Examples | Notes |
|---|---:|---|---|
| Provenance-linked references | Yes | STAC Item IDs, DCAT dataset IDs, graph entity IDs | Inputs should be IDs/refs, not raw copy/paste blobs |
| Configuration | Often | model/prompt version, thresholds, run settings | Must be reproducible (pinned versions, deterministic settings where possible) |
| Scope constraints | Yes | geography/time window, sensitivity class | Enforce redaction/generalization rules up front |

### Outputs
| Output | Required? | Location | Notes |
|---|---:|---|---|
| Evidence artifact(s) | Often | `data/processed/` + catalog entry | Treat as data product with STAC/DCAT/PROV |
| Story Node(s) | Sometimes | `docs/` (story nodes area) | Must follow Story Node template and cite dataset/document IDs |
| Run log | Yes | `mcp/runs/` or `mcp/experiments/` | Includes run ID, inputs, outputs, validation results |

### Sensitivity & redaction
- Do not publish precise coordinates for restricted locations.
- Prefer generalized geometries and descriptive regions over exact points when sensitivity is uncertain.
- Ensure redaction rules are documented *and* testable (CI gates).

### Quality signals
- Provenance completeness (all claims trace to IDs)
- Uncertainty/confidence (explicit, machine-readable when possible)
- Reproducibility (config pinned; run logs recorded)
- Review status (draft/reviewed/approved)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Any agent-generated evidence artifact that becomes a reusable asset should be represented as a STAC Item/Asset with stable IDs.

### DCAT
- Map reusable outputs to a DCAT dataset record (minimum: title, description, license, keywords).

### PROV-O
- Model each agent run as a `prov:Activity` that `prov:used` input entities and `prov:generated` output entities.

### Versioning
- New output versions should link predecessor/successor; the graph should mirror version lineage.

## 🧱 Architecture

### Components
- **Agent specs** (docs): permissions, inputs/outputs, and constraints.
- **Agent runners** (code): orchestrate execution; emit artifacts, logs, and provenance.
- **Validators** (CI): ensure docs, schemas, and outputs conform to KFM contracts.

### Interfaces / contracts
- Agents must consume KFM data through contracted interfaces (catalog + APIs) rather than ad-hoc scraping.
- Any user-facing output must surface: provenance refs, redaction status, and uncertainty metadata (when applicable).
- If an agent introduces or changes an API, document it with the API contract extension template and add contract tests.

### Extension points checklist (for future work)
- [ ] New agent role/spec documented
- [ ] Inputs/outputs mapped to STAC/DCAT/PROV
- [ ] Redaction/generalization rules documented + tested
- [ ] Telemetry signals defined (if user-facing)
- [ ] Governance review triggered (if required)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Agents may support Focus Mode by generating **provenance-linked context bundles** or drafting Story Nodes that are reviewed before publication.

### Provenance-linked narrative rule
- Focus Mode and Story Nodes must not contain uncited factual claims; every factual claim must map to a dataset/document ID.

### Optional structured controls
- `includePredictions` (default: false)
- `confidence` / `uncertainty` fields (required if predictions are included)
- `redactionApplied` (true/false + rule ID)

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Agent runs | Agent runner | `mcp/runs/` |
| Validation results | CI | CI logs + `mcp/` |
| Focus Mode consumption | UI/API | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Require review for: new agent roles that affect narratives, new sensitive layers/outputs, new external data sources, and any new public-facing endpoints.

### CARE / sovereignty considerations
- Identify impacted communities and protection rules early; document redaction/generalization behavior for any restricted locations.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.
- This area must not be used to justify policy changes (“generate_policy”) or to infer restricted site locations (“infer_sensitive_locations”).

## 🕰️ Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial README for `docs/agents/` | TBD |
---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
