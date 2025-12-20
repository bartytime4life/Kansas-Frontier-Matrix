---
title: "KFM Research Drafts — README"
path: "docs/research/drafts/README.md"
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

doc_uuid: "urn:kfm:doc:research:drafts:readme:v1.0.0"
semantic_document_id: "kfm-research-drafts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:drafts:readme:v1.0.0"
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

# KFM Research Drafts — README

## 📘 Overview

### Purpose
This directory is the **staging area for early, exploratory work**: draft notes, hypotheses, literature summaries, experiment plans/results, and design sketches.

Drafts are **not** treated as canonical system documentation and **must not** be used as authoritative sources for:
- Focus Mode narrative
- public-facing UI content
- API contracts
- governance requirements

Drafts exist to **incubate** ideas before promotion into governed artifacts that follow the canonical KFM pipeline and documentation standards.

### Scope

| In Scope | Out of Scope |
|---|---|
| Literature notes and summaries | Final governance policies or standards |
| Hypotheses and open questions | Story Nodes intended for user-facing narrative |
| Experiment plans and results writeups | API/contract changes without contract docs + tests |
| Design sketches (data/graph/API/UI) | Secrets, credentials, private keys |
| Evidence triage and “what to verify next” | Large/derived datasets (belongs under `data/`) |
| Links to sources with brief annotations | Precise sensitive locations that require redaction/generalization |

### Audience
- Primary: contributors doing exploratory research, prototyping, or evidence review.
- Secondary: maintainers/reviewers promoting drafts into governed docs and implementation work.

### Definitions (link to glossary)
- Link: `docs/glossary.md` (if present)
- Terms used in this doc:
  - **Draft**: non-canonical working document
  - **Promotion**: moving a draft into a governed doc or implementation plan
  - **Evidence**: a source asset/record that can be referenced via STAC/DCAT/PROV and/or a document ID
  - **Provenance**: lineage links (STAC/DCAT/PROV + graph references) that back claims

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + “do not break” rules |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Default template for governed documentation |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Required for narrative nodes |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | Required when proposing endpoint/contract changes |

### Definition of done (for this document)
- [ ] Clearly distinguishes drafts vs governed docs
- [ ] Provides naming + organization conventions for drafts
- [ ] Defines a promotion path into governed artifacts
- [ ] Includes sensitivity + sovereignty reminders
- [ ] Links to the canonical KFM pipeline + templates

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/drafts/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Research index (recommended) | `docs/research/` | Entry points for research themes + links |
| Drafts (this folder) | `docs/research/drafts/` | Early-stage notes, experiments, sketches |
| Documentation templates | `docs/templates/` | Governed doc templates (universal/story/api) |
| Data lifecycle | `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` | Source data + derived datasets + catalogs |
| Experiments / runs | `mcp/` | Experimental artifacts, model cards, SOPs (when applicable) |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    ├── 📄 README.md
    └── 📁 drafts/
        ├── 📄 README.md
        ├── 📁 literature/
        │   └── 📄 YYYY-MM-DD__topic__notes.md
        ├── 📁 experiments/
        │   └── 📄 YYYY-MM-DD__experiment__log.md
        ├── 📁 design/
        │   └── 📄 YYYY-MM-DD__proposal__sketch.md
        └── 📁 assets/
            ├── 📁 figures/
            └── 📁 snippets/
~~~

## 🧭 Context

### Background
KFM work spans multiple domains (ETL, catalogs, graph, APIs, UI, story/narrative). Research drafts let contributors explore ideas quickly while preserving the “do not break” invariants of the system.

### Assumptions
- Drafts may contain incomplete reasoning and must be explicitly labeled as such.
- Claims intended to become user-facing must be backed by provenance (dataset/document IDs), and promoted out of drafts.

### Constraints / invariants
- The canonical pipeline ordering is preserved:
  **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.**
- Frontend consumes contracts via APIs (no direct graph dependency).
- Drafts must not introduce sensitive leakage (follow governance + sovereignty constraints).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| TBD | TBD | TBD |

### Future extensions
- Optional: add a lightweight “Draft Note” template under `docs/templates/` (requires human review + governance alignment).

## 🗺️ Diagrams

### How drafts become governed artifacts
~~~mermaid
flowchart LR
  A[Draft note in docs/research/drafts/] --> B[Promotion PR: governed doc or implementation plan]
  B --> C[ETL configs / transforms]
  C --> D[STAC/DCAT/PROV catalogs]
  D --> E[Graph build]
  E --> F[API contract]
  F --> G[UI integration]
  G --> H[Story Node + Focus Mode]
~~~

### Optional: sequence diagram (promotion path)
~~~mermaid
sequenceDiagram
  participant Author as Draft Author
  participant Review as Maintainer/Reviewer
  participant Repo as Repo (docs/data/code)
  Author->>Repo: Add draft note (this folder)
  Author->>Review: Open promotion PR
  Review->>Repo: Request provenance + template compliance
  Repo-->>Review: Validation gates pass (docs/schemas/tests as needed)
  Review-->>Author: Approved → merged into governed location
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Literature references | Markdown list + short annotations | Papers, books, archives | Provide citation info; avoid long verbatim quotes |
| Evidence notes | Markdown | STAC/DCAT/PROV IDs, document IDs | Must include identifiers when available |
| Experiment logs | Markdown / notebook summary | Local runs | Repro steps + parameters if intended for promotion |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Draft notes | Markdown | `docs/research/drafts/...` | Best effort; promote to governed template before production use |
| Figures for drafts | PNG/SVG | `docs/research/drafts/assets/figures/` | Keep small + referenced from draft |
| Promotion-ready doc | Markdown | Governed location (e.g., `docs/...`) | Must use an approved template |

### Sensitivity & redaction
- Do not include secrets, private keys, access tokens, or personal data.
- Do not publish precise locations of protected/sensitive sites; generalize when in doubt.
- If a draft touches restricted data, mark it clearly and follow the sovereignty policy referenced in front-matter.

### Quality signals
- Use explicit markers near the top of each draft:
  - **Status:** DRAFT / NEEDS_CITATIONS / READY_TO_PROMOTE
  - **Confidence:** low/medium/high (for claims)
  - **Evidence:** list identifiers (STAC/DCAT/PROV/document IDs) when available

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If a draft proposes new spatial/temporal assets, include the intended:
  - Collection name + intended ID
  - Item ID patterns
  - Asset list (files, thumbnails) and licensing notes

### DCAT
- If a draft proposes a new dataset, include a draft dataset identifier and minimum metadata:
  title, description, license, keywords, spatial/temporal coverage.

### PROV-O
- If a draft proposes a transform or model run, capture:
  - `prov:wasDerivedFrom` (source IDs)
  - `prov:wasGeneratedBy` (planned activity/run ID pattern)
  - Agents (script/person) responsible

### Versioning
- Treat drafts as mutable; treat promoted artifacts as versioned and linked (predecessor/successor) where applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Draft docs (this folder) | Incubate ideas + capture open questions | Markdown only |
| Governed docs | Define contracts + decisions | Template-driven docs under `docs/` |
| Data + catalogs | Store datasets and metadata | `data/` + STAC/DCAT/PROV outputs |
| Graph/APIs/UI/Story | Production pipeline stages | Governed by subsystem docs + contracts |

### Interfaces / contracts
- If a draft proposes an API change: write a promotion doc using `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`.
- If a draft proposes story content intended for Focus Mode: promote into a Story Node using `docs/templates/TEMPLATE__STORY_NODE_V3.md`.

### Extension points checklist (for future work)
- [ ] Data: dataset placement under `data/<domain>/...`
- [ ] STAC/DCAT/PROV: identifiers + validation plan
- [ ] Graph: labels/relations mapped + migration notes
- [ ] APIs: contract doc + contract tests
- [ ] UI: layer registry updates + a11y considerations
- [ ] Story/Focus: provenance-linked narrative only

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Drafts do not surface in Focus Mode directly. Promotion is required so that:
- provenance references are present,
- sensitivity handling is reviewed,
- contracts and rendering expectations are defined.

### Provenance-linked narrative rule
Any narrative intended for Focus Mode must trace every factual claim to a dataset/record/asset identifier.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (style + fenced blocks)
- [ ] No secrets/PII in committed drafts
- [ ] If promoting: schema validation (STAC/DCAT/PROV), graph integrity checks, API contract tests, UI checks (as applicable)

### Reproduction
~~~bash
# Drafts are documentation-only.
# If a draft describes an experiment, include reproduction steps *inside the draft*:
# 1) inputs
# 2) exact commands
# 3) parameters + seeds
# 4) expected outputs + checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Drafts: peer review recommended for clarity and sensitivity.
- Promotion: required when drafts become governed docs, datasets, story nodes, or public endpoints.

### CARE / sovereignty considerations
- Treat culturally sensitive content with care; do not infer or publish sensitive locations.
- If unsure, mark as sensitive and request appropriate review.

### AI usage constraints
- Drafts may summarize sources, but must not introduce speculative claims as if factual.
- Any AI-derived content intended for user-facing use must be provenance-linked and reviewable.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for research drafts | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

