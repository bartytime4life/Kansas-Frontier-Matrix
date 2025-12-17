---
title: "Standard — KFM Assistant Work Protocol"
path: "docs/standards/KFM_ASSISTANT_WORK_PROTOCOL.md"
version: "v2.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:standards:assistant-work-protocol:v2.0.0"
semantic_document_id: "kfm-standard-assistant-work-protocol-v2.0.0"
event_source_id: "ledger:kfm:doc:standards:assistant-work-protocol:v2.0.0"
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

# Standard — KFM Assistant Work Protocol

## 📘 Overview

### Purpose
This standard defines how AI assistants (and human co-authors using AI assistance) must draft, edit, refactor, and review KFM artifacts so outputs remain consistent with KFM’s governed pipeline, contracts, and FAIR+CARE + sovereignty constraints.

This document governs:
- How tasks are classified (doc vs API contract vs story node vs code/design note)
- How outputs are packaged for “paste into repo” use
- What must be checked before proposing changes that affect downstream subsystems (catalogs, graph, APIs, UI, Focus Mode, telemetry)

### Scope

| In Scope | Out of Scope |
|---|---|
| Drafting governed Markdown docs via KFM templates | Claiming to run code, deploy infra, push commits, or change production systems |
| Proposing structured edits and refactors to repo artifacts (docs/schemas/specs) | Creating or altering governance policy text (refer to governance docs instead) |
| Suggesting code-level changes as designs/diffs + test plans | Inferring/deriving sensitive locations or protected site coordinates |
| Building reproducible checklists and validation plans | Producing “unsourced narrative” intended for Focus Mode |

### Audience
- Primary: KFM maintainers, doc stewards, pipeline/API/UI owners
- Secondary: contributors, researchers, students, community reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: Focus Mode, Story Node, STAC/DCAT/PROV, pipeline contract, ontology protocol, layer registry, sensitivity_class, CARE gating.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (system + pipeline “source of truth”) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline, extension matrix, CI gates |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Doc stewards | Default template for non-story docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative stewards | Evidence-led story nodes with provenance |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API owners | Contract-first changes (REST/GraphQL) |
| Standards directory | `docs/standards/` | Maintainers | Includes KFM-MDP and other governed standards |
| Security docs | `.github/SECURITY.md` + `docs/security/` | Security stewards | Security posture + technical controls |
| Governance / sovereignty docs | `docs/governance/*` | Governance council | Policies + review gates |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All normative rules trace to an existing governed artifact path (or explicitly marked “not confirmed in repo”)
- [ ] Validation steps listed and repeatable (placeholders allowed only when repo commands are not confirmed)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No prohibited AI actions implied (see `ai_transform_prohibited`)

### Copy/paste instruction block (short form)
Use this as the default “assistant system prompt” for KFM work.

~~~text
KFM ASSISTANT RULES (SHORT FORM)

1) Repo-grounded only: Use governed KFM artifacts as sources of truth. If a fact/rule/template/path is not verifiable, say “not confirmed in repo” and propose the safest next step.

2) Task classification first:
   - Story Node / Focus Mode narrative → Story Node template
   - API contract / endpoint/schema change → API Contract Extension template
   - Everything else (guides, SOPs, design notes) → Universal template
   Always consult MASTER_GUIDE_v12.md for pipeline alignment.

3) Pipeline invariants (non-negotiable):
   - Preserve: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode
   - No unsourced narrative in Focus Mode contexts
   - Provenance is first-class
   - Pipelines must be deterministic/replayable

4) Extension Matrix completeness:
   When proposing a new capability, check impacts across Data, Catalog, Graph, API, UI, Story/Focus, Telemetry. Don’t “skip layers” silently.

5) Security + sovereignty defaults:
   - No secrets/credentials in outputs
   - Don’t infer sensitive locations; generalize/redact protected sites
   - Follow CARE and sovereignty rules; flag review triggers

6) Output packaging:
   - Provide commit-ready Markdown as one clean block (no chat-only citations/markers inside)
   - Put notes/assumptions/next steps outside the commit-ready block
   - Outer chat fence uses backticks; inner code/tree fences use tildes in committed docs
~~~

## 🗂️ Directory Layout

### This document
- `path`: `docs/standards/KFM_ASSISTANT_WORK_PROTOCOL.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |
| Tests | `tests/` | Unit/integration/e2e tests |
| Tooling | `tools/` | Validators, linters, build helpers |
| Security policy | `.github/` + `docs/security/` | Security standards + procedures |

### Expected file tree for this sub-area
~~~text
docs/
  standards/
    KFM_ASSISTANT_WORK_PROTOCOL.md
    <other-standards-here>          # e.g., KFM-MDP (not listed here by name unless confirmed)
~~~

## 🧭 Context

### Background
KFM’s pipeline is intentionally “contract-governed” to ensure provenance, reproducibility, and sovereignty-safe outputs as the system scales across datasets and narrative experiences.

AI assistance is valuable, but it must be constrained by KFM’s governed artifacts to avoid:
- Contract drift (breaking APIs, schema mismatches)
- Governance violations (policy invention, sensitive location inference)
- Focus Mode integrity failures (unsourced narrative, missing provenance)

### Assumptions
- MASTER_GUIDE_v12.md + docs/templates are authoritative for workflow and doc structure.
- Where external standards are referenced (STAC/DCAT/PROV), KFM’s pinned profiles take precedence.
- If a requested output cannot be mapped to a governed template, the assistant must respond with “not confirmed in repo” and propose the safest next step.

### Constraints / invariants
- Preserve canonical pipeline ordering: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Focus Mode content must be provenance-linked; no hallucinated sources.
- API changes must be backward compatible or require a version bump.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should this doc be “draft” or “active” by default? | Maintainers | TBD |
| What CARE label should apply to assistant outputs by default? | Governance council | TBD |
| What are the repo’s exact validation commands for KFM-MDP and schema checks? | Tooling owner | TBD |

### Future extensions
- Add a governed “assistant prompt library” for common tasks (dataset onboarding, story node authoring, API extension).
- Add a repo-confirmed “validation command index” for docs/schemas/APIs/UI checks.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  U[User request] --> C[Classify task type]
  C --> T{Template or artifact?}
  T -->|Story Node| SN[Story Node v3]
  T -->|API change| AC[API Contract Extension]
  T -->|Other doc| UD[Universal Doc]
  T -->|Code/design| CD[Design note + diffs + tests]

  UD --> V[Validation checklist]
  SN --> V
  AC --> V
  CD --> V

  V --> G[Governance & CARE/Sovereignty gates]
  G --> O[Commit-ready output block + notes]
~~~

### Optional: sequence diagram (assistant output lifecycle)
~~~mermaid
sequenceDiagram
  participant User
  participant Assistant
  participant Repo as "KFM governed artifacts"
  User->>Assistant: Request change/draft
  Assistant->>Repo: Consult Master Guide + templates + standards
  Assistant-->>User: Commit-ready artifact + validation + governance notes
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| User task request | Text | Chat | N/A |
| Governed references | Markdown/PDF | `docs/` + templates | Must be cited by path/ID |
| Dataset IDs / schema refs | IDs + JSON schema | `data/stac/`, `schemas/` | Schema-validated |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Governed doc | Markdown | `docs/...` | Must follow a governed template |
| Story node | Markdown | `docs/.../story_nodes/...` | Must follow Story Node v3 template |
| API change doc | Markdown | `docs/...` | Must follow API Contract Extension template |
| Validation plan | Markdown | `docs/...` or PR notes | Must be reproducible |

### Sensitivity & redaction
- Do not output high-precision coordinates for protected/sensitive sites.
- Do not infer sensitive locations from context; apply generalization/redaction patterns per sovereignty policy.
- If sensitivity rules are unclear, stop and mark “not confirmed in repo” + recommend governance review.

### Quality signals
- Evidence completeness: every factual claim maps to a dataset/document ID (especially in Story Nodes / Focus Mode).
- Range/format checks for predictive outputs (scores, uncertainty, confidence) when relevant.
- Deterministic/replayable steps for pipelines and transforms.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Every new dataset should be represented as STAC Collection + Item(s).
- Catalog outputs should be machine-validated against KFM profiles.

### DCAT
- Provide dataset-level discovery metadata (title/description/license/keywords minimum).
- Ensure DCAT records map cleanly to KFM’s catalog views.

### PROV-O
- `prov:wasDerivedFrom`: record source IDs (datasets/documents/assets).
- `prov:wasGeneratedBy`: record pipeline activity/run identifiers.

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships where applicable.
- Don’t overwrite history without a version lineage plan.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |
| Telemetry | Governance signals | JSON schema + dashboards |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/...` | Schema-validated |
| Story Node schema | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Must remain stable for ingestion |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- What entities become focusable?
- What evidence must be shown?
- What redaction/generalization is required under CARE gating?

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Focus Mode must not include unsourced narrative.
- Predictive content must be opt-in and include uncertainty/confidence metadata.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (KFM-MDP)
- [ ] Schema validation (STAC/DCAT/PROV/telemetry)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands once confirmed.
# 1) validate markdown protocol (KFM-MDP)
# 2) validate JSON schemas (STAC/DCAT/PROV/telemetry)
# 3) run unit/integration tests
# 4) build docs / lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Validation coverage | CI | `docs/telemetry/` + `schemas/telemetry/` |
| Security scanning status | CI/security tooling | `docs/telemetry/` |
| Sovereignty/CARE gating checks | Pipeline/UI gating | `docs/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that introduce new sensitive layers, new AI narrative behaviors, new external data sources, or new public-facing endpoints must be flagged for governance review.

### CARE / sovereignty considerations
- Identify impacted communities and protection rules.
- Document redaction/generalization rules for restricted locations or sensitive content.
- Default to safety: if unsure, do not emit precise locations and request governance input.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- Do not generate policy text; refer to governance docs instead.
- Do not infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v2.0.0 | 2025-12-17 | Proposed assistant work protocol standard | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
