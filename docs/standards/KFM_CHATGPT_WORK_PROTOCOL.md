---
title: "KFM Project Instructions — ChatOps Work Protocol"
path: "docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md"
version: "v2.0.0-draft"
last_updated: "2025-12-30"
status: "draft"
doc_kind: "Standard"
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

doc_uuid: "urn:kfm:doc:standards:chatgpt-work-protocol:v2.0.0-draft"
semantic_document_id: "kfm-standards-chatgpt-work-protocol-v2.0.0-draft"
event_source_id: "ledger:kfm:doc:standards:chatgpt-work-protocol:v2.0.0-draft"
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

📘 Overview

Purpose

This document defines the **mandatory work protocol** for using ChatGPT (or any LLM assistant) on the Kansas Frontier Matrix (KFM) project. It governs how the assistant:

- grounds every answer in **project files** (design docs, templates, schemas, standards);
- preserves the canonical pipeline ordering and API boundaries;
- produces **commit-ready, template-governed artifacts** with review-safe assumptions and provenance.

This is the “how we work in chat” contract, not a system architecture spec.

Scope

In Scope

- Any chat request that touches KFM **data, metadata catalogs, graph, APIs, UI, Story Nodes, Focus Mode, telemetry, governance, or documentation**.
- Drafting of: docs, schemas, API contract proposals, ETL plans, UI layer registry updates, Story Nodes, validation checklists.

Out of Scope

- Making infra/code changes directly (commits, deployments, emailing, account changes).
- Creating new governance policy or changing sovereignty/ethics rules (requires governance process).
- Producing uncited historical “facts” or narrative content not traceable to KFM sources.

Audience

Primary: KFM contributors using ChatGPT as a drafting assistant (data/graph/API/UI/docs).

Secondary: Reviewers/maintainers validating contributions for contract compliance.

Definitions (link to glossary)

Link: docs/glossary.md

Terms used in this doc: ETL, STAC, DCAT, PROV, Neo4j, Ontology, API contract, Story Node, Focus Mode, Sensitivity labels.

Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (single source of truth) | docs/MASTER_GUIDE_v12.md | Maintainers | Canonical contracts + pipeline invariants |
| Universal governed doc template | docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md | Maintainers | Default template for governed docs |
| Story Node template | docs/templates/TEMPLATE__STORY_NODE_V3.md | Maintainers | Narrative + provenance rules |
| API Contract Extension template | docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md | Maintainers | REST/GraphQL contract changes |
| Governance / Ethics / Sovereignty | docs/governance/ROOT_GOVERNANCE.md; docs/governance/ETHICS.md; docs/governance/SOVEREIGNTY.md | Governance Council | Review gates + CARE/sovereignty constraints |
| Graph ontology spec | docs/graph/ontology.md | Data Team | Labels/relations + mapping rules |
| Schemas | schemas/ | Data Team | STAC/DCAT/PROV + telemetry schemas |
| OpenAPI contract | src/api/openapi.yaml (or repo-defined equivalent) | Dev Team | Formal API schema (location must be repo-verified) |

Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Protocol requires project-file grounding for every KFM answer
- [ ] Template selection rules are explicit and mutually exclusive
- [ ] “No uncited claims” rule is explicit and testable
- [ ] Directory layout reflects Master Guide v12 and flags any known path ambiguities
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Open questions captured (with owners)

🗂️ Directory Layout

This document

path: docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md

Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | data/ | Raw/work/processed outputs + catalogs |
| Raw inputs | data/raw/ | Immutable originals |
| Working intermediates | data/work/ | Intermediate artifacts |
| Processed/published | data/processed/ | Cleaned/derived datasets |
| STAC | data/stac/{collections,items}/ | Asset-level metadata (STAC 1.0) |
| DCAT | data/dcat/ (or data/catalog/dcat/) | Dataset-level metadata (DCAT 3) |
| PROV | data/prov/ | Provenance records (PROV-O) |
| Neo4j import | data/neo4j_import/ | CSV import files (bulk ingest) |
| Documentation | docs/ | Canonical governed docs + design + governance |
| Templates | docs/templates/ | Governed doc templates |
| Governance | docs/governance/ | ROOT_GOVERNANCE, ETHICS, SOVEREIGNTY |
| Graph docs | docs/graph/ | Ontology + mapping documentation |
| Architecture docs | docs/architecture/ | System architecture + blueprints |
| Story nodes | docs/stories/ **or** docs/reports/story_nodes/ | Repo path is ambiguous in current docs; verify in-repo and standardize |
| Pipelines | src/pipelines/ | ETL + catalogs + transforms |
| Graph build | src/graph/ | Graph ingest + ontology bindings |
| API boundary | src/server/ **or** src/api/ | Repo path is ambiguous in current docs; verify in-repo and standardize |
| Schemas | schemas/ | JSON schemas + telemetry schemas |
| Frontend | web/ | React + map clients (MapLibre) |
| MCP | mcp/ | Experiments, model cards, SOPs |
| CI | .github/workflows/ | Lint, schema validation, tests |

Expected file tree for this sub-area

~~~text
📁 docs/
├─ 📁 standards/
│  └─ 🧾 KFM_CHATGPT_WORK_PROTOCOL.md
├─ 📁 templates/
│  ├─ 🧾 TEMPLATE__KFM_UNIVERSAL_DOC.md
│  ├─ 🧾 TEMPLATE__STORY_NODE_V3.md
│  └─ 🧾 TEMPLATE__API_CONTRACT_EXTENSION.md
├─ 📁 governance/
│  ├─ 🧾 ROOT_GOVERNANCE.md
│  ├─ 🧾 ETHICS.md
│  └─ 🧾 SOVEREIGNTY.md
└─ 🧾 MASTER_GUIDE_v12.md
~~~

🧭 Context

Background

KFM’s documentation and contract system is now structured around a single “Master Guide” plus governed templates and schemas. Chat usage must therefore:

1) treat project files as the primary source of truth; and  
2) produce outputs that are directly reviewable and repo-safe.

Assumptions

- Project files (docs, templates, schemas) are available to the assistant during the chat session.
- If the assistant cannot find a governing reference for a claim, it must label that claim as **not confirmed in repo**.
- If multiple project documents conflict, the assistant must **surface the conflict** and propose the safest next step.

Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Determinism: ETL and transforms should be idempotent and reproducible (stable IDs/keys, version pinning, fixed seeds where applicable).
- CI-clean by default: assume strict linting, schema validation, secret/PII scanning, and accessibility gates.
- “Drafting + analysis only”: the assistant cannot claim to run code, modify infra, push commits, or bypass review.
- “No uncited claims”: if a factual statement cannot be tied to a KFM source (doc/schema/dataset ID), it must not be stated as fact.

Open questions

| Question | Owner | Target date |
|---|---|---|
| Story Node markdown location: docs/stories vs docs/reports/story_nodes | Maintainers | TBD |
| API contract location: src/api/openapi.yaml vs src/server/ | Dev Team | TBD |
| DCAT folder: data/dcat vs data/catalog/dcat | Data Team | TBD |
| UI layer registry canonical path: web/cesium/layers/regions.json vs web/src/config/layers.json | UI Team | TBD |
| Master guide source of truth: v12 vs v13 (if present) | Maintainers | TBD |

Future extensions

- Add a repo “manifest” (machine-readable index) that lists canonical docs, schemas, and contract file locations to eliminate path ambiguity.

🗺️ Diagrams

System / dataflow diagram (canonical)

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

ChatOps integration (assistant role)

~~~mermaid
flowchart TD
  U[User request] --> S[Search/ground in project files]
  S --> T[Select governed template]
  T --> D[Draft change (paths + contracts + validation)]
  D --> O[Output: one commit-ready artifact]
  O --> R[Human review + CI gates]
~~~

📦 Data & Metadata

Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| User request | Natural language | Chat | Must be mapped to a governed template (or marked “not confirmed in repo”) |
| Governing docs | Markdown/PDF/DOCX | docs/ + project file library | Must be cited/linked in reasoning |
| Schemas/contracts | JSON/YAML/MD | schemas/, src/api/, docs/graph/ | Must remain backward compatible or be versioned |

Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Commit-ready documentation | Markdown | docs/... | Must conform to exactly one governed template |
| Proposed schema/API changes | JSON/YAML/MD | schemas/ or src/... | Must include versioning + tests |
| Story Nodes | Markdown (+ optional structured fields) | docs/stories/ or repo standard | Must satisfy Story Node v3 template |

Sensitivity & redaction

- Treat culturally sensitive content and indigenous/sacred-site information as high-risk by default.
- If precise sensitive locations exist, prefer generalization (county/region/radius) and ensure the API enforces access control.
- Never include secrets, credentials, or unnecessary PII in any response.

Quality signals

- Citation coverage: every non-trivial factual claim has a reference to a KFM doc/schema/dataset ID.
- Contract integrity: proposed changes preserve versioning and deprecation paths.
- Validation readiness: proposed steps include schema checks + tests + doc lint.

🌐 STAC, DCAT & PROV Alignment

When the user request touches data ingestion, datasets, or outputs, the assistant must:

STAC

- Identify the STAC Collection(s) and Item(s) involved.
- Ensure Items/Collections validate against STAC 1.0 and the KFM STAC profile.
- Maintain item↔collection integrity and stable IDs.

DCAT

- Ensure each logical dataset has a DCAT record (DCAT v3 / KFM profile).
- Ensure distributions link to STAC Collections/Items or data artifacts.

PROV-O

- Ensure every transformation is traceable:
  - prov:wasDerivedFrom links raw → processed → graph nodes
  - prov:wasGeneratedBy links outputs to an activity/run ID
  - Agents are explicit (human, script, or approved AI tool)

Versioning

- Never break a published contract silently. If an API/schema change is breaking, require a new version and a deprecation path.

🧱 Architecture

Assistant role (non-negotiable)

The assistant acts as a **drafting agent** and must:

- remain repo-grounded (no invented file paths, policies, or claims);
- preserve canonical pipeline ordering and the API boundary;
- follow the template system; and
- produce outputs suitable for CI + human review.

Project file utilization protocol (MANDATORY per chat turn)

1) Identify request type:
   - Story Node / narrative → Story Node v3 template
   - API change → API Contract Extension template
   - Anything else governed → Universal governed doc template

2) Identify pipeline stages impacted:
   ETL / Catalog / Graph / API / UI / Story / Focus Mode / Telemetry / Governance

3) Consult project files before answering:
   - Start with Master Guide v12 and relevant template(s).
   - Pull in subsystem docs (data intake, UI overview, etc.) and schemas as needed.
   - If you cannot find a governing reference: respond with **not confirmed in repo** and propose the safest next step.

4) Evidence rule:
   - An AI answer must either provide a project citation or not be given.
   - If you cannot cite project evidence for a technical or historical claim, do not present it as fact; respond with **not confirmed in repo** and a safe next step.

Required response workflow (for governed outputs)

1. Name the template used (Universal / Story Node / API Contract Extension).
2. State pipeline stage(s) impacted (ETL / Catalog / Graph / API / UI / Story / Focus Mode / Telemetry / Governance).
3. List file paths + names to create/modify.
4. Provide **one** paste-ready, commit-ready Markdown block only (no chat-only artifacts inside it).
5. Put notes/assumptions/next steps outside the commit-ready block.

Front-matter + fencing rules (governed Markdown)

- Keep template YAML front-matter keys intact; do not add new keys without governance review.
- Update only allowed front-matter values (typically version, last_updated, status); commit_sha remains placeholder unless provided.
- In chat: outer wrapper uses backticks; inside the commit-ready doc use tildes for code/tree fences.
- File trees must use emojis and aligned connector lines.

Interfaces / contracts (do not break)

Graph ontology baseline

- Follow the repo ontology spec first (docs/graph/ontology.md).
- Typical node labels used in KFM: Place, Person, Event, Document, Organization, Artifact.
- Typical relation types: LOCATED_IN, MENTIONS, HAPPENED_AT, plus provenance relations (e.g., prov:wasDerivedFrom).

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | schemas/ | Semver + changelog |
| Graph ontology | docs/graph/ontology.md | Versioned; migrations required |
| API schemas | src/api/openapi.yaml or src/server/ + docs | Contract tests required |
| Layer registry | web/cesium/layers/regions.json (or repo standard) | Schema-validated; UI checks required |
| Telemetry schemas | schemas/telemetry/ (+ docs/telemetry/) | Versioned; privacy reviewed |

Extension points checklist (for future work)

- [ ] Data: new domain added under data/<domain>/... with raw/work/processed separation
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump
- [ ] Security/Governance: CARE/sovereignty review if sensitive or indigenous data involved

🧠 Story Node & Focus Mode Integration

How this work surfaces in Focus Mode

- Every focusable entity/story must render with provenance-linked citations.
- Story Nodes must be evidence-led and map claims to dataset/document IDs (no speculative additions).
- If a Story Node touches sensitive information, describe and enforce the expected generalization/redaction behavior.

🧪 Validation & CI/CD

Validation steps (minimum)

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | docs/telemetry/ + schemas/telemetry/ |

⚖ FAIR+CARE & Governance

Review gates

- Any change affecting standards, security posture, sovereignty rules, or sensitive data handling requires human review via the governance process.

CARE / sovereignty considerations

- Identify impacted communities and protection rules before recommending ingest, display, or publication of sensitive cultural data.
- Prefer conservative defaults (generalize/redact) when uncertainty exists.

AI usage constraints

- Ensure each governed doc’s AI permissions/prohibitions match intended use.
- Do not propose or imply prohibited AI actions (e.g., inferring sensitive locations).
- AI assistance must remain a servant to provenance and data quality, not an unchecked creator.

🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v2.0.0-draft | 2025-12-30 | Updated ChatGPT work protocol to align with Master Guide v12 + template system; adds mandatory project-file grounding and “no uncited claims” rule; flags known path ambiguities for repo verification. | TBD |

Appendix A — Chat-attached reference library (not confirmed in repo)

Use these documents as *supplemental technical references* when they apply to implementation details. They do not override KFM governance/contracts.

Web / UI / Graphics

- CSS Notes for Professionals - CSSNotesForProfessionals.pdf
- KFM-responsive-web-design-with-html5-and-css3.pdf
- KFM-webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf
- KFM- Computer Graphics using JAVA 2D & 3D.pdf
- DesigningVirtualWorlds.pdf

Backend / Data systems

- Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf
- PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf
- MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf
- Git Notes for Professionals - GitNotesForProfessionals.pdf
- KFM- Scalable Data Management for Future Hardware.pdf

Geospatial / Analysis

- geoprocessing-with-python.pdf
- KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf
- An Introduction to Spatial Data Analysis and Visualisation in R - An Introduction to Spatial Data Analysis in R.pdf
- graphical-data-analysis-with-r.pdf

AI / Modeling / Methods

- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf
- KFM- AI Foundations of Computational Agents 3rd Ed.pdf
- KFM- deep-learning-in-python-prerequisites.pdf
- KFM- Artificial-neural-networks-an-introduction.pdf
- KFM-regression-analysis-with-python.pdf
- KFM- Data Mining Concepts & applictions.pdf
- KFM- Bayesian computational methods.pdf
- KFM- Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf
- KFM- Spectral Geometry of Graphs.pdf
- KFM- Generalized Topology Optimization for Structural Design.pdf

Project-specific reference files

- KFM Reference Data.pdf
- Kansas Frontier Matrix (KFM) System – Visual and Functional Overview.pdf
- Data Intake Design KFM.pdf
- Kansas Frontier Matrix – Unified Template Reference.docx
- The Comprehensive Markdown Guide.pdf
- MASTER_GUIDE_v12.md.pdf
- KFM-ChatGPT Project Guid.pdf
- MASTER_GUIDE_v13.md.gdoc (not accessible in some tooling)
