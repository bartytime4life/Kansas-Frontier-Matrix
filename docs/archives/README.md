---
title: "Documentation Archives"
path: "docs/archives/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:archives:readme:v1.0.0"
semantic_document_id: "kfm-archives-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:archives:readme:v1.0.0"
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

# Documentation Archives

## 📘 Overview

### Purpose
This directory is reserved for **archived documentation artifacts** that are no longer the active, canonical
source of truth, but are retained for reference, auditability, or historical context.

### Scope
| In Scope | Out of Scope |
|---|---|
| Superseded versions of governed docs (kept for traceability) | Canonical “current” docs that define active contracts |
| Historical drafts or discontinued proposals (clearly labeled) | Data products and catalogs (use `data/` + STAC/DCAT/PROV paths) |
| Archived story node snapshots (when intentionally frozen) | Anything required by runtime systems unless explicitly referenced by current contracts |

### Audience
- Primary: Repo maintainers, reviewers, and contributors who need to preserve documentation lineage.
- Secondary: Researchers/auditors who need to inspect historical decisions and document evolution.

### Definitions
- Glossary: `docs/glossary.md`
- Terms used in this doc: archive, canonical, superseded, deprecated, provenance, lineage.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | For narrative artifacts |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | For REST/GraphQL changes |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Archived items are clearly labeled as archived/superseded (no ambiguity vs canonical docs)
- [ ] Links from canonical docs to archived predecessors are present (when applicable)
- [ ] No sensitive content is moved here without proper classification and governance review

## 🗂️ Directory Layout

### This document
- `path`: `docs/archives/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs (active) |
| Templates | `docs/templates/` | Canonical governed templates |
| Reports / Story nodes | `docs/reports/` | Narrative artifacts tied to evidence (active) |
| Data + catalogs | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 archives/
    ├── 📄 README.md
    └── 📁 <archive-buckets-TBD>/
        └── 📄 <archived-documents>.md
~~~

## 🧭 Context

### Background
KFM documentation evolves (templates, contracts, design decisions). Without a clearly defined archive
location, older artifacts can be mistaken for canonical documents, which risks breaking governance,
contracts, and contributor workflows.

### Assumptions
- Archived documents are retained for reference and are **not** the canonical contract unless explicitly
  referenced by an active doc (requires human review).
- Archival structure (subfolders, naming conventions, retention) may evolve under governance.

### Constraints and invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No unsourced narrative should be introduced via archives; provenance expectations remain in force.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What qualifies a doc for archiving vs deletion? | TBD | TBD |
| What naming scheme should archived docs use (date, version, predecessor id)? | TBD | TBD |
| What retention policy applies (if any), and who approves? | TBD | TBD |
| Should there be an index file (machine-readable) of archived docs? | TBD | TBD |

### Future extensions
- Add a machine-readable index (e.g., `docs/archives/index.json`) generated by a doc tool (requires human review).
- Define an “archived-by / archived-at / superseded-by” convention that aligns with version history and governance (requires human review).

## 🗺️ Diagrams

### System and invariants alignment
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  H[Governed Docs] -.-> A
  H -.-> D
  H -.-> E
  I[Docs Archives] -.-> H
~~~

## 📦 Data and metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Superseded docs | `.md` / `.pdf` | `docs/` history | Markdown protocol checks (if `.md`) |
| Archived narrative snapshots | `.md` | `docs/reports/` history | Story Node validation (if applicable) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Archived doc | `.md` / `.pdf` | `docs/archives/...` | N/A (doc governance applies) |
| Pointer/link from canonical doc | `.md` link | original canonical location | Markdown lint |

### Sensitivity and redaction
- If an archived document contains restricted or sensitive content, ensure:
  - `sensitivity` and `classification` in front-matter reflect the correct status.
  - Any required redaction/generalization is applied before moving content into archives.
  - Governance review triggers are followed.

### Quality signals
- Clear “ARCHIVED” labeling in the document title or opening section.
- Working links to predecessor/successor/canonical references (when applicable).
- No duplicated “canonical” guidance in archives without an explicit pointer to current docs.

## 🌐 STAC, DCAT & PROV alignment

### STAC
- Not applicable for this directory by default.
- If an archived doc references STAC assets, retain the referenced IDs/paths without modification.

### DCAT
- Not applicable for this directory by default.

### PROV-O
- Not applicable for this directory by default.
- If an archived doc includes provenance statements, preserve them.

### Versioning
- Prefer explicit version history in archived documents (see “Version History” section).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Docs | Govern contracts, standards, and system descriptions | Markdown in repo |
| Archives | Preserve historical docs without confusing canonical contracts | Markdown/PDF in repo |

### Interfaces and contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Markdown protocol + template requirements | `docs/templates/` | Follow template semver and doc version history |
| System invariants | `docs/MASTER_GUIDE_v12.md` | Canonical reference; changes require review |

### Extension points checklist
- [ ] Add archive indexing (automation + schema) — requires human review
- [ ] Add deprecation workflow (policy) — requires human review

## 🧠 Story Node & Focus Mode integration

### How this surfaces in Focus Mode
- Archives should **not** be used by Focus Mode unless an active, canonical Story Node or contract
  explicitly references an archived artifact.

### Provenance-linked narrative rule
- Archived narrative content must not be treated as a source of new claims without evidence links.

## 🧪 Validation and CI/CD

### Validation steps
- [ ] Markdown protocol checks (where enforced)
- [ ] Link integrity checks (recommended)
- [ ] Confirm no sensitive content is unintentionally published
- [ ] Confirm canonical docs still point to the correct current versions

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run markdown lint
# 2) run link checker
# 3) run docs build (if applicable)
~~~

## ⚖ FAIR+CARE & governance

### Review gates
- Archive actions involving sensitive content: governance review required (see refs in front-matter).
- Archive actions that could affect public-facing narratives: historian/editor review recommended.

### CARE and sovereignty considerations
- If archived content impacts protected communities or includes culturally sensitive locations/details,
  apply generalization/redaction rules before archiving and label sensitivity appropriately.

### AI usage constraints
- Archives do not change the system rule: no speculative additions and no inference of sensitive locations.

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial archives README scaffold | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`