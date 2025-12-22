---
title: "KFM GitHub Issue Templates"
path: ".github/ISSUE_TEMPLATE/README.md"
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

doc_uuid: "urn:kfm:doc:github:issue-templates-readme:v1.0.0"
semantic_document_id: "kfm-github-issue-templates-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:issue-templates-readme:v1.0.0"
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

# KFM GitHub Issue Templates

## 📘 Overview

### Purpose
- Provide a single, governed reference for how to file KFM issues in a way that is pipeline-aware, reproducible, and reviewable.
- Ensure issues collect the minimum information needed for traceability across data, catalogs, graph, APIs, UI, and story outputs.

### Scope

| In Scope | Out of Scope |
|---|---|
| How to choose and use KFM issue templates | Implementing fixes or features |
| The required fields for KFM issues | Security incident response procedures |
| Triage cues: pipeline stage, affected paths, sensitivity | Private project management policy beyond GitHub Issues |

### Audience
- Primary: Contributors filing issues (bugs, data requests, enhancements, documentation gaps).
- Secondary: Maintainers triaging, labeling, and connecting issues to PRs, datasets, and releases.

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc:
  - Pipeline stage
  - STAC, DCAT, PROV
  - Neo4j graph
  - API boundary
  - Story Node
  - Focus Mode
  - Sensitivity and redaction

### Key artifacts

| Artifact | Path | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + invariants |
| Universal Doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Default governed doc scaffold |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Narratives and Focus Mode inputs |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | REST/GraphQL contract changes |
| Governance docs | `docs/governance/` | Governance | If missing, add per Master Guide references |

### Definition of done
- [ ] Front-matter complete and valid
- [ ] Links point to canonical KFM docs and folders
- [ ] Guidance is pipeline-aware and does not imply bypassing the API boundary
- [ ] Sensitivity, PII, and secrets guidance is explicit
- [ ] Validation and review expectations are listed

## 🗂️ Directory Layout

### This document
- `path`: `.github/ISSUE_TEMPLATE/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub meta | `.github/` | Issue templates, PR templates, workflows |
| Documentation | `docs/` | Governed docs and templates |
| Data domains | `data/` | Domain raw/work/processed outputs |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC, DCAT, PROV artifacts |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog generation code |
| Graph | `src/graph/`, `data/graph/` | Ontology, ingest, fixtures/imports |
| API boundary | `src/server/` | Contracted access to graph/catalogs with redaction rules |
| UI | `web/` | Map UI, Focus Mode UI, layer registry |
| Schemas | `schemas/` | Machine-readable validation schemas |
| Tests | `tests/` | Contract/schema/integration tests |

### Expected file tree

~~~text
📁 .github/
└── 📁 ISSUE_TEMPLATE/
    ├── 📄 README.md
    ├── 📄 config.yml
    ├── 📄 <issue_template_1>.yml
    ├── 📄 <issue_template_2>.yml
    └── 📄 ...
~~~

## 🧭 Context

### Why issue templates exist in KFM
Issue templates are designed to prompt for the information reviewers need to maintain:
- traceability (sources, licenses, temporal/spatial coverage, provenance),
- reproducibility (steps to reproduce, validation steps),
- governance (sensitivity, redaction, sovereignty considerations).

### Pipeline-first triage rule
Every issue should name at least one pipeline stage it impacts:

| Stage | Typical issue topics | Typical affected paths |
|---|---|---|
| ETL | Ingest bugs, transforms, new source adapters | `src/pipelines/`, `data/<domain>/{raw,work,processed}/` |
| Catalogs | STAC/DCAT/PROV generation/validation | `data/stac/`, `data/catalog/dcat/`, `data/prov/`, `schemas/` |
| Graph | Ontology, ingest mapping, migrations | `src/graph/`, `data/graph/`, `docs/graph/` |
| API boundary | New endpoints, payload changes, redaction rules | `src/server/`, `schemas/`, `tests/` |
| UI | Layer registry, map/timeline, Focus Mode UX | `web/` |
| Story Nodes | Narrative gaps, missing citations, publishing | `docs/reports/story_nodes/` |
| Focus Mode | Evidence display rules, synthesis constraints | `web/` + story node docs |

### Required fields in every issue
Regardless of template, include:
- What you expected vs what happened
- Pipeline stage(s) impacted
- Affected paths (folders/files if known)
- Evidence and provenance references where applicable
- Sensitivity assessment
- Acceptance criteria

### Data Addition Request minimum checklist
If you are proposing a new dataset or source, include:
- Source link or identifier
- License and redistribution terms
- Temporal coverage
- Spatial coverage
- Data type and format
- Sensitivity and redaction needs
- What you want KFM to produce
  - raw/work/processed artifacts
  - catalog records (STAC/DCAT)
  - provenance (PROV bundle)
  - downstream linkage targets (graph entities, story nodes)

### Bug Report minimum checklist
- Steps to reproduce
- Expected behavior
- Actual behavior
- Logs or error output
- Environment details
- Smallest failing example if possible

### API or contract change minimum checklist
- Proposed change summary and motivation
- Backward compatibility considerations
- Affected schema(s) and tests
- Sensitivity and redaction implications

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  I[GitHub Issue] --> S[Pipeline stage tag]
  S --> P1[ETL and pipelines]
  S --> P2[STAC DCAT PROV catalogs]
  S --> P3[Graph]
  S --> P4[API boundary]
  S --> P5[UI]
  S --> P6[Story Nodes]
  S --> P7[Focus Mode]
  P2 --> E[Evidence artifacts with IDs]
  P3 --> E
  P4 --> U[Contracted payloads]
  P5 --> U
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Issue fields | GitHub issue form | Contributor | Required fields per template |
| Evidence links | URLs or repo paths | Contributor | Must be attributable and license-aware |
| Affected paths | Repo paths | Contributor | Must align with canonical homes |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Issue triage labels | GitHub labels | GitHub | Maintainer conventions |
| Linked artifacts | Links to PRs, docs, datasets | Repo + GitHub | Must reference canonical locations |
| Validation notes | Markdown | Issue comments | Repeatable steps when applicable |

### Sensitivity and redaction
- Do not post secrets, credentials, tokens, or private keys.
- Do not post private personal data.
- If a location or community-sensitive attribute is involved, describe it at an appropriate level of generalization.

### Quality signals
- Repro steps that another contributor can follow
- Sample data or a minimal failing case
- Clear acceptance criteria
- Provenance references for data and narrative claims

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- When issues mention geospatial assets, include relevant STAC collection and item IDs if known.
- If a new dataset is proposed, describe the intended STAC collection grouping and item granularity.

### DCAT
- For dataset-centric issues, include a stable dataset identifier and license mapping expectations.

### PROV-O
- For pipeline-related issues, reference run IDs and provenance fields:
  - `prov:wasDerivedFrom`
  - `prov:wasGeneratedBy`

### Versioning
- When an issue describes changes to existing assets or catalogs, include predecessor links or version notes.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest and normalize | Configs and run logs |
| Catalogs | STAC/DCAT/PROV | JSON plus validators |
| Graph | Neo4j | Cypher behind API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map and narrative | API calls only |
| Story Nodes | Curated narrative | Docs and graph linkage |
| Focus Mode | Contextual synthesis | Provenance-linked rules |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver plus changelog |
| API schemas | `src/server/` plus docs | Contract tests required |
| Layer registry | `web/` | Schema-validated |

### Extension points checklist
- [ ] Data domain adds under `data/<domain>/...`
- [ ] Catalog validation covers new STAC/DCAT/PROV outputs
- [ ] PROV includes run activity and agent identifiers
- [ ] Graph mappings align with ontology and migrations
- [ ] API changes use contract extensions and tests
- [ ] UI changes update layer registry where applicable
- [ ] Story Nodes and Focus Mode keep provenance references enforced

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- If the issue affects Focus Mode behavior, identify:
  - which entities become focusable
  - what evidence must be shown
  - any redaction or uncertainty rules

### Provenance-linked narrative rule
- When issues propose narrative claims, require links to dataset or document identifiers that can be traced through catalogs and provenance.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation for STAC/DCAT/PROV
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks
- [ ] Security and sovereignty checks where applicable

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Identify who should review the issue
- Call out whether the change is expected to require governance or community review

### CARE and sovereignty considerations
- If content impacts a community or contains potentially sensitive cultural or location information, describe required protection rules.

### AI usage constraints
- Do not request prohibited AI actions such as inferring sensitive locations.
- Ensure any AI-related proposals include provenance and uncertainty expectations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial issue template README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
