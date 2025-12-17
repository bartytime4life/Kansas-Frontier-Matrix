---
title: "Agents — Specifications"
path: "docs/agents/specs/README.md"
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

doc_uuid: "urn:kfm:doc:agents:specs:readme:v1.0.0"
semantic_document_id: "kfm-agents-specs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:agents:specs:readme:v1.0.0"
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

# Agents — Specifications

## 📘 Overview

### Purpose
- Define the governed, reviewable specifications for KFM agents.
- Provide a stable contract for what an agent **does**, what it **consumes/produces**, and what it is **allowed** to do.
- Make agent behavior auditable against KFM’s provenance, catalog, graph, API, and UI expectations.

### Scope
| In Scope | Out of Scope |
|---|---|
| Per-agent specification documents | Implementation code and runtime deployment details |
| Agent responsibilities, inputs/outputs, permissions, provenance requirements | Secrets, credentials, tokens, or operational incident response |
| Cross-links to datasets, schemas, catalogs, APIs, and tests | Replacing governance documents or redefining policy |

### Audience
- Primary: KFM engineers building pipeline, graph, API, UI, and telemetry components
- Secondary: Governance reviewers, Story Node authors, QA/CI maintainers

### Definitions
- Link: `docs/glossary.md`
- Terms used in this directory:
  - **Agent**: A bounded actor (human or software) associated with pipeline activities.
  - **Agent spec**: A governed document that describes an agent’s contract and constraints.
  - **Agent ID**: A stable slug used to reference the agent across docs, logs, and provenance.
  - **Run ID**: A stable identifier for a single execution of an agent (used for traceability).

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Agents overview | `docs/agents/README.md` | TBD | Top-level orientation and index of agents |
| Agent specs directory | `docs/agents/specs/` | TBD | Canonical specs (this area) |
| Master pipeline ordering | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default template for agent specs until a dedicated template exists |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Used when an agent produces Story Nodes |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | TBD | Source-of-truth for review + governance controls |

### Definition of done
- [ ] Front-matter complete and valid
- [ ] Each spec has a stable **Agent ID** and clear ownership/maintainer contact
- [ ] Inputs/outputs are explicit (schemas, IDs, and formats where possible)
- [ ] Provenance requirements are explicit (PROV identifiers, run IDs, and where logs land)
- [ ] Validation steps listed and repeatable
- [ ] Security, ethics, CARE/sovereignty considerations explicitly stated or linked

## 🗂️ Directory Layout

### This document
- `path`: `docs/agents/specs/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Agents overview | `docs/agents/` | Orientation, conventions, and links to specs |
| Templates | `docs/templates/` | Governed templates for docs and Story Nodes |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering and invariants |
| Pipelines | `src/pipelines/` | ETL, transforms, catalog build, graph build (implementation) |
| Graph | `src/graph/` + `docs/graph/` | Ontology, labels/relations, migrations |
| APIs | `src/server/` + `docs/api/` | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` + `docs/design/` | UI, map layers, Focus Mode UX |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Observability and governance metrics |
| MCP runs | `mcp/` | Experiments and run artifacts (if applicable) |
| Data | `data/` | Raw/work/processed and catalogs (STAC/DCAT/PROV) |

### Expected file tree for this sub-area
~~~text
📁 docs/agents/specs/
├── 📄 README.md
├── 📄 <agent_id>.md
└── 📁 _assets/ (optional)
    └── 🖼️ <diagrams-and-figures>
~~~

## 🧭 Context

### Why agent specs exist
Agent specifications are the **documentation contract layer** for KFM agents. They exist to:
- Make agent behavior reviewable before implementation changes ship.
- Prevent “silent” contract drift (inputs/outputs changing without updating downstream consumers).
- Support reproducibility: a reader can understand what an agent did, with what inputs, and what it produced.

### How this fits into the KFM pipeline
KFM’s canonical pipeline ordering is:

- ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

Agent specs should explicitly state **which stage(s)** an agent operates in and what contracts it touches.

### Adding a new agent specification
1. Create `docs/agents/specs/<agent_id>.md`.
2. Use `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` as the base structure (until an agent-spec template is introduced).
3. In the spec, include at minimum:
   - Agent ID (stable slug)
   - Owner/maintainer
   - Pipeline stage(s)
   - Inputs (dataset IDs, STAC IDs, schemas, API endpoints)
   - Outputs (datasets, STAC items, graph mutations, API artifacts, docs)
   - Provenance requirements (PROV identifiers; run/log location)
   - Safety and governance constraints (including sovereignty rules when applicable)
4. If the agent changes a public-facing contract (API, Story Node format, published dataset), bump the spec version and update downstream references.

### Non-negotiables to reflect in specs
- Agents must not embed credentials, tokens, or secrets in documentation.
- Agents must not bypass the contracted access layer (frontend stays behind APIs; no direct graph access from UI).
- Any location-sensitive content must follow sovereignty and redaction requirements; avoid “inferring” sensitive locations from partial evidence.

### Open questions
- A dedicated agent-spec template and/or schema is **not confirmed in repo**; until then, use the Universal Doc template and keep specs consistent.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  Spec["Agent spec (docs/agents/specs/<agent_id>.md)"] --> Review["Review + governance gates"]
  Review --> Impl["Implementation (src/... and/or mcp/...)"]
  Impl --> Run["Run artifacts (run_id, logs, metrics)"]
  Run --> Catalog["Catalog build (STAC/DCAT/PROV)"]
  Catalog --> Graph["Graph build (Neo4j)"]
  Graph --> API["APIs (REST/GraphQL)"]
  API --> UI["React/Map UI"]
  UI --> Story["Story Nodes"]
  Story --> Focus["Focus Mode"]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where it comes from | Validation |
|---|---|---|---|
| Agent requirements | Markdown / tickets | Design docs and issues | Review + doc lint |
| Referenced datasets/assets | IDs + metadata | `data/` + catalogs | Schema validation (as applicable) |
| Referenced interfaces | IDs + contracts | `src/server/` + `docs/api/` | Contract tests (as applicable) |

### Outputs
| Output | Format | Where it goes | Validation |
|---|---|---|---|
| Agent spec document | Markdown | `docs/agents/specs/` | Markdown protocol checks |
| Optional diagrams/assets | PNG/SVG/Mermaid | `docs/agents/specs/_assets/` | Link + render checks (as applicable) |

### Sensitivity and redaction
- Do not include secrets or operational credentials.
- If examples include real-world locations tied to sensitive contexts, generalize/redact per `docs/governance/SOVEREIGNTY.md`.
- Do not infer sensitive locations from incomplete evidence; describe uncertainty and cite sources.

### Quality signals
- Every “input” and “output” claim should link to a dataset ID, schema, or contract doc when available.
- Prefer stable identifiers over informal names.

## 🌐 STAC, DCAT & PROV Alignment

### STAC alignment
If an agent consumes or produces assets that belong in STAC:
- Reference STAC **Collection** and **Item** IDs in the agent spec.
- Document any required STAC extensions or profiles used.

### DCAT alignment
If an agent publishes a dataset, distribution, or service:
- Reference the relevant DCAT dataset/service identifiers and where they are declared.
- Ensure the spec clarifies how discovery metadata is generated and validated.

### PROV alignment
Agent specs should be PROV-friendly:
- Use a stable Agent ID suitable for provenance graphs.
- Specify how each run records provenance (activity IDs, timestamps, inputs used, outputs generated).
- Specify where run artifacts (logs, manifests) are stored for auditability.

### Versioning
- Specs are versioned via git and the `version:` front-matter field.
- Breaking changes to agent outputs/contracts should bump spec version and update dependent docs/tests.
- Where applicable, link to predecessor/successor artifacts (STAC versioning, graph lineage, API contract versions).

### Extension points checklist
- [ ] Data: new domain added under `data/<domain>/`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How agent work surfaces in Focus Mode
If an agent produces narrative artifacts (Story Nodes) or evidence panels:
- Identify which entities become focusable.
- Identify which evidence assets must be shown in the UI.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV), if the agent touches catalogs
- [ ] Graph integrity checks, if the agent writes to graph
- [ ] API contract tests, if the agent changes APIs
- [ ] UI schema checks (layer registry), if the agent changes UI-facing configs
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run doc lint / markdown protocol checks
# 2) validate schemas (STAC/DCAT/PROV)
# 3) run unit/integration tests
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| run_id | Agent runner | `mcp/` and/or `docs/telemetry/` (as applicable) |
| success/failure | Agent runner | `schemas/telemetry/` (as applicable) |
| input/output counts | Agent runner | `schemas/telemetry/` (as applicable) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Follow `docs/governance/ROOT_GOVERNANCE.md` for approvers and escalation paths.
- This README does not redefine governance policy.

### CARE and sovereignty considerations
- If an agent touches Indigenous knowledge, sensitive sites, or culturally sensitive narratives:
  - Apply `docs/governance/SOVEREIGNTY.md` rules.
  - Prefer generalized locations and explicit uncertainty where needed.

### AI usage constraints
- Ensure each spec’s `ai_transform_permissions` and `ai_transform_prohibited` match intended use.
- Do not use AI to infer sensitive locations or to invent evidence.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial README for agent specifications directory | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
