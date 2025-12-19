---
title: "KFM Standards — README"
path: "docs/standards/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:standards:readme:v1.0.0"
semantic_document_id: "kfm-standards-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:standards:readme:v1.0.0"
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

# KFM Standards — README

## 📘 Overview

### Purpose
This folder (`docs/standards/`) is the canonical home for **governed standards** that apply across the Kansas Frontier Matrix (KFM) system: documentation rules, metadata/contract conventions, validation expectations, and cross-cutting invariants that must remain stable as the system evolves.

This README is the **index + usage guide** for the standards area and should stay aligned with:
- `docs/MASTER_GUIDE_v12.md` (pipeline ordering + subsystem map)
- `docs/templates/` (the governed document templates)

### Scope

| In Scope | Out of Scope |
|---|---|
| Markdown governance (format, front-matter, fences, doc structure) | Narrative content (Story Nodes) |
| Cross-cutting invariants (pipeline ordering, API boundary) | API endpoint contracts (live in dedicated contract docs) |
| Standards indexing + where-to-find-what | Implementation details of ETL/Graph/API/UI |
| Validation expectations and review gates | Ad hoc team notes / meeting minutes |

### Audience
- Primary: Contributors writing or editing governed docs, reviewers, maintainers
- Secondary: Engineers implementing validators/CI checks, authors creating Story Nodes

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc: governed doc, profile, provenance, redaction/generalization, contract, invariant

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + subsystem map |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default template for most docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Focus Mode narratives (provenance-linked) |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | REST/GraphQL contract changes |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | TBD | **not confirmed in repo** (add if missing) |
| Governance roots | `docs/governance/*` | TBD | **not confirmed in repo** (referenced by templates) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Links point to canonical docs/templates (or clearly marked **not confirmed in repo**)
- [ ] Invariants preserved: ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode
- [ ] No new policies invented here (standards must point to governance docs, not replace them)
- [ ] Validation steps listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `docs/standards/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | System map + canonical pipeline ordering |
| Standards | `docs/standards/` | Governed standards, protocols, style rules |
| Templates | `docs/templates/` | Governed doc templates (choose exactly one per doc) |
| Governance | `docs/governance/` | Ethics, sovereignty, review gates (**not confirmed in repo**) |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Standards-aligned outputs |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📁 standards/
│   ├── 📄 README.md
│   ├── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md           (not confirmed in repo)
│   ├── 📄 KFM_STAC_PROFILE.md                     (not confirmed in repo)
│   ├── 📄 KFM_DCAT_PROFILE.md                     (not confirmed in repo)
│   ├── 📄 KFM_PROV_PROFILE.md                     (not confirmed in repo)
│   └── 📄 KFM_ONTology_PROTOCOL.md                (not confirmed in repo)
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
└── 📁 governance/
    ├── 📄 ROOT_GOVERNANCE.md                      (not confirmed in repo)
    ├── 📄 ETHICS.md                               (not confirmed in repo)
    └── 📄 SOVEREIGNTY.md                          (not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM is a pipeline-based geospatial + historical knowledge system. Because many subsystems contribute content that becomes user-facing (map layers, narratives, evidence panels), **standards** are necessary to ensure consistency, provenance traceability, and safe handling of sensitive data.

### Assumptions
- Governed docs use YAML front-matter with shared profile/version fields.
- The system’s canonical ordering is maintained:
  **ETL → STAC/DCAT/PROV → Neo4j Graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
- The UI **never** queries Neo4j directly; it consumes contracts from the API layer.

### Constraints / invariants
- Canonical pipeline ordering is preserved.
- Provenance is first-class: Story Nodes and Focus Mode must be evidence-linked.
- No sensitive locations are inferred or revealed by documentation standards.
- CI is assumed strict (lint/schema/secret/PII/a11y checks).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical glossary? | TBD | TBD |
| Which standards are separate docs vs embedded in the Master Guide? | TBD | TBD |
| Where are schema validators invoked (scripts/CI)? | TBD | TBD |

### Future extensions
- Add explicit, governed standards docs (profiles + checklists) under `docs/standards/`.
- Add a lightweight “Standards change log” doc if frequent updates occur.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Standards placement in the workflow
~~~mermaid
flowchart TB
  S[docs/standards/*] --> T[docs/templates/*]
  T --> W[Governed docs across repo]
  S --> V[CI validators / schema checks]
  W --> V
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Standards proposals | Markdown | PRs / issues | Doc lint + reviewer checklist |
| Profile updates | Markdown / Schema refs | PRs | Versioning + compatibility review |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Standards docs | Markdown | `docs/standards/` | Template + lint rules |
| Referenced schemas | JSON / JSON-LD | `schemas/` | Schema validation in CI |

### Sensitivity & redaction
- Standards must define how to **avoid leaking** sensitive locations or culturally sensitive context.
- If redaction/generalization rules exist, they must live in governance docs and be referenced here (not duplicated).

### Quality signals
- Consistent front-matter keys and values across governed docs.
- Links resolve (no broken internal references).
- No contradictory pipeline ordering or API-boundary violations.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Standards docs should describe:
  - Where STAC collections and items live (`data/stac/collections/`, `data/stac/items/`)
  - Which profile version is authoritative (from front-matter fields)

### DCAT
- Standards docs should describe:
  - Where DCAT dataset views live (`data/catalog/dcat/`)
  - Minimum required dataset metadata for publishing

### PROV-O
- Standards docs should describe:
  - Where provenance bundles live (`data/prov/`)
  - Required lineage links for derived artifacts (including Story Nodes)

### Versioning
- Prefer SemVer for schemas and contract documents.
- Profile identifiers in front-matter should be updated intentionally and reviewed.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Standards docs | Define governed rules + invariants | Markdown (this folder) |
| Templates | Enforce doc structure | `docs/templates/` |
| Validators | Enforce consistency in CI | Linters + schema validation |
| Governance docs | Define policy/ethics/sovereignty | `docs/governance/` (**not confirmed in repo**) |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Document templates | `docs/templates/` | SemVer; template changes require reviewer sign-off |
| Schema files | `schemas/` | SemVer + changelog |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Machine-validated |

### Extension points checklist (for future work)
- [ ] Add missing standards docs (if not present) under `docs/standards/`
- [ ] Add validator pointers (where checks run) once confirmed in repo
- [ ] Add a glossary (if missing) and link from here

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Standards define what “provenance-linked narrative” means and how citations must work.
- Story Nodes must follow the Story Node template and connect to catalog IDs and graph entities.

### Provenance-linked narrative rule
- Every factual claim must trace to a dataset / record / asset ID (or be labeled as hypothesis).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter keys, fence rules, headings)
- [ ] Schema validation (STAC/DCAT/PROV where applicable)
- [ ] Graph integrity checks (when graph artifacts are changed)
- [ ] API contract tests (when contracts are changed)
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) lint docs
# 2) validate schemas (STAC/DCAT/PROV)
# 3) run unit/integration tests
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Standards changes should be reviewed by maintainers responsible for:
  - Docs + templates
  - Catalog/schema validation
  - Governance/ethics (when standards touch sensitivity)

### CARE / sovereignty considerations
- Any guidance related to culturally sensitive content must be anchored in governance docs.
- Avoid naming or mapping restricted locations in public docs unless explicitly permitted.

### AI usage constraints
- This doc allows AI transformations like summarize/structure_extract, but prohibits:
  - generating policy (policy belongs in governance docs)
  - inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial standards README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
