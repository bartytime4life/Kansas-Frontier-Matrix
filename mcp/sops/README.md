---
title: "MCP SOPs — README"
path: "mcp/sops/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:mcp:sops:readme:v1.0.0"
semantic_document_id: "kfm-mcp-sops-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:mcp:sops:readme:v1.0.0"
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

# MCP SOPs

## 📘 Overview

### Purpose
- Provide an index and authoring/maintenance guidance for Standard Operating Procedures (SOPs) under `mcp/sops/`.
- SOPs are step-by-step workflows intended to make recurring tasks reproducible, reviewable, and auditable.

### Scope
| In Scope | Out of Scope |
|---|---|
| Recurring, repeatable operational workflows that touch KFM data, catalogs, graph, APIs, UI, or story content | One-off exploratory notes, design pitches, long-form narrative reports (use Story Node template), or API changes (use API Contract Extension template) |
| Verification and troubleshooting checklists for workflows | Policy creation (governance lives under `docs/governance/`) |

### Audience
- Primary: Contributors executing repeatable workflows (ETL, catalog build, graph build, API/UI releases, story node publication).
- Secondary: Reviewers validating provenance, reproducibility, and governance requirements.

### Definitions (link to glossary)
- Link: `docs/glossary.md` (if present)
- Terms used in this doc: SOP, MCP, run log, provenance, STAC, DCAT, PROV

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This SOP index | `mcp/sops/README.md` | Maintainers | Update when SOPs are added/retired |
| KFM Master Guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + invariants |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Default governed doc format |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Narrative artifacts |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | REST/GraphQL contracts |

### Definition of done (for this README)
- [ ] This README exists and describes how SOPs are organized and maintained
- [ ] Each SOP has: Purpose, Prerequisites/Tools, Procedure steps, Verification, Troubleshooting/Notes
- [ ] Each SOP references the affected pipeline stage(s) and the artifact(s) it creates/updates
- [ ] No secrets/credentials/PII are included
- [ ] SOPs that touch sensitive data declare redaction/generalization expectations and required reviewers

## 🗂️ Directory Layout

### This document
- `path`: `mcp/sops/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| MCP | `mcp/` | Experiments, model cards, SOPs, run artifacts |
| MCP runs | `mcp/runs/` | Run logs and reproducibility bundles (if used) |
| Pipelines | `src/pipelines/` | ETL + catalog + graph build code (if present) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Standards-aligned outputs |
| Story Nodes | `docs/reports/.../story_nodes/` | Provenance-linked narratives |

### Expected file tree for this sub-area
~~~text
📁 mcp/
└── 📁 sops/
    ├── 📄 README.md
    ├── 📄 <sop-name>.md
    └── 📁 _assets/ (optional)
        └── 📄 <images-diagrams-etc>
~~~

## 🧭 Context

### Background
SOPs exist to reduce ambiguity and variance in recurring tasks (e.g., ingesting a new source, producing catalogs, updating a model, or publishing a story node). They make work:
- Reproducible (same inputs → same outputs)
- Reviewable (clear checkpoints + verification)
- Auditable (clear provenance + change traceability)

### Assumptions
- SOPs are written in Markdown and committed to version control.
- SOP steps are deterministic or explicitly record any non-deterministic parameters (seeds, model versions, etc.).
- Where a workflow produces artifacts, it records IDs/paths and the relevant STAC/DCAT/PROV references.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct Neo4j access).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we want a dedicated SOP template under `docs/templates/`? | TBD | TBD |
| Should SOPs be versioned per-file (SemVer) or via git history only? | TBD | TBD |

### Future extensions
- Add a dedicated SOP template document if needed.
- Add CI checks to ensure SOPs include required headings and no secrets.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A["SOP (mcp/sops/*.md)"] --> B["Contributor executes workflow"]
  B --> C["Artifacts updated (data/, docs/, src/, web/)"]
  C --> D["Validation + CI checks"]
  D --> E["Merge + release (as applicable)"]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source material | files/URLs | `data/raw/` or external | checksum + license recorded |
| Configs | YAML/JSON | `src/pipelines/` / `tools/` | schema + lint |
| Schemas | JSON Schema | `schemas/` | schema validation |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| SOP document | Markdown | `mcp/sops/<name>.md` | Markdown protocol checks |
| Catalog entries (if applicable) | JSON / RDF | `data/stac/`, `data/catalog/dcat/` | STAC/DCAT validators |
| Provenance bundle (if applicable) | PROV (JSON-LD) | `data/prov/` | PROV profile checks |
| Run log (if applicable) | JSON/MD | `mcp/runs/` | telemetry schema (if present) |

### Sensitivity & redaction
- SOPs that touch restricted/sensitive sources must document:
  - what should be generalized/redacted in outputs
  - access controls or approvals required
  - where audit logs are recorded

### Quality signals
- Include step-level checkpoints (e.g., “schema validates”, “geometry valid”, “no broken STAC links”, “unit tests pass”).
- Record warnings and how they were resolved (or why they are acceptable).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If the workflow creates/updates geospatial assets, the SOP must specify:
  - the target collection and item IDs
  - validation steps and link integrity checks

### DCAT
- If the workflow introduces a dataset view, the SOP must specify:
  - dataset identifier
  - license and publisher mapping requirements

### PROV-O
- If the workflow produces derived artifacts, the SOP must specify:
  - `prov:wasDerivedFrom` source identifiers
  - `prov:wasGeneratedBy` run/activity identifier

### Versioning
- Where artifacts are versioned, SOPs should describe how predecessor/successor links are recorded (STAC + graph lineage as applicable).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| SOP docs | Human-readable, repeatable workflows | Markdown + PR review |
| Pipelines | Deterministic transforms | configs + run logs |
| Validators | Schema + integrity checks | CLI / CI gates |
| API boundary | Contracted access to graph and catalogs | REST/GraphQL |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | SemVer + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Story node format | `docs/templates/` | Template versioned |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- SOPs that publish/update Story Nodes must ensure:
  - every claim links to a dataset/document ID
  - required citations render in UI
  - sensitive information is generalized/redacted as required

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) when applicable
- [ ] Graph integrity checks when applicable
- [ ] API contract tests when applicable
- [ ] UI schema checks when applicable
- [ ] Security and sovereignty checks when applicable

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run validators (schemas + link checks)
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| SOP execution run ID | workflow runner | `mcp/runs/` |
| Validation results | CI | CI logs + artifacts |
| Provenance completeness | catalog validator | `data/prov/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- SOPs affecting sensitive data or public-facing outputs may require:
  - Security review
  - FAIR+CARE / sovereignty review
  - Historian/editor review (for narrative outputs)

### CARE / sovereignty considerations
- Identify communities impacted and protection rules when SOPs handle culturally sensitive content.
- Do not include precise sensitive locations in public artifacts if prohibited.

### AI usage constraints
- SOPs must not instruct prohibited AI actions (e.g., generating policy or inferring sensitive locations).
- When SOPs involve AI outputs, require provenance-linked evidence and record model versions.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial SOPs README scaffold | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`