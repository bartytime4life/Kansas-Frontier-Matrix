---
title: "Research Drafts — Literature"
path: "docs/research/drafts/literature/README.md"
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

doc_uuid: "urn:kfm:doc:research:drafts:literature:readme:v1.0.0"
semantic_document_id: "kfm-research-drafts-literature-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:drafts:literature:readme:v1.0.0"
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

# Research Drafts — Literature

## 📘 Overview

### Purpose
This directory holds **working literature notes** that support KFM research and future governed artifacts.
Use it to capture what a source says, why it matters, and which KFM pipeline components it may inform.

This is **not** a public-facing narrative area. Draft content here may be incomplete, exploratory, or later revised.

### Scope

| In Scope | Out of Scope |
|---|---|
| Paper/book reading notes | Final Story Nodes |
| Short summaries + key claims | Public narrative prose intended for Focus Mode |
| Methods notes (e.g., STAC/DCAT/PROV, graph modeling, UI patterns) | API contract changes (use governed API contract docs) |
| Questions, hypotheses (clearly labeled) | “Policy” documents (governance docs live elsewhere) |
| Pointers to source summaries + attachments | Raw datasets / derived datasets (belong under `data/`) |

### Audience
- Primary: KFM contributors preparing evidence products, story nodes, or technical designs.
- Secondary: Reviewers who need to trace how a design/narrative decision was informed by literature.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: literature note, source summary, provenance, claim, evidence, citation, redaction/generalization.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Research drafts index | `docs/research/drafts/README.md` | Research | Higher-level draft conventions |
| Source summaries | `docs/research/source_summaries/` | Research | One-per-source structured summaries |
| Source attachments | `docs/research/source_summaries/_attachments/` | Research | PDFs/assets (license-permitting) |
| Story node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs | For promoted narrative nodes |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Docs | For endpoint/contract additions |

### Definition of done (for a literature note)
- [ ] Source is identifiable (DOI/ISBN/URL + bibliographic fields)
- [ ] A short **neutral summary** is included
- [ ] Key **claims are separated** from your **interpretation**
- [ ] Relevance to KFM is stated (which pipeline stage(s) it informs)
- [ ] If a local attachment is used, license/permissions are checked and recorded
- [ ] No secrets, credentials, or sensitive location inference is included

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/drafts/literature/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Governed docs + research materials |
| Research | `docs/research/` | Working notes, summaries, draft synthesis |
| Templates | `docs/templates/` | Governed templates for docs/contracts |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    ├── 📁 drafts/
    │   ├── 📄 README.md
    │   └── 📁 literature/
    │       ├── 📄 README.md
    │       ├── 📁 by_topic/
    │       │   ├── 📄 README.md
    │       │   └── 📄 <topic>__notes.md
    │       ├── 📁 by_source/
    │       │   ├── 📄 README.md
    │       │   └── 📄 <citekey>__<short-title>__notes.md
    │       └── 📄 literature_log.md
    └── 📁 source_summaries/
        ├── 📄 README.md
        └── 📁 _attachments/
            └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM’s governed pipeline requires provenance-linked outputs.
Literature drafts help bridge:
- “What the world already knows” (published work)
- “What we implement” (KFM pipeline designs, schemas, and narrative UX)

### Assumptions
- Literature can be referenced by DOI/ISBN/URL even when local storage is not permitted.
- Where attachments are stored, licensing/usage rights are respected and recorded.

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Literature notes do **not** bypass governance: promoted artifacts must meet the Story Node / contract templates and provenance rules.
- UI does not read Neo4j directly; all consumable narrative or data access is via API contracts.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should we adopt a single citation key format across drafts + source summaries? | TBD | TBD |
| Do we want an export/import bridge with a bibliography tool (e.g., Zotero)? | TBD | TBD |

### Future extensions
- A lightweight `citations.json` or BibTeX export for cross-linking (requires governance review).
- “Promotion” workflow: literature note → source summary → story node candidate.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Literature source\n(doi/isbn/url)] --> B[Source summary\n(docs/research/source_summaries)]
  B --> C[Literature draft note\n(docs/research/drafts/literature)]
  C --> D[Promoted Story Node\n(governed template)]
  D --> E[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Papers/books/articles | PDF / URL / citation | External sources | License check + bibliographic completeness |
| Your reading notes | Markdown | This directory | Markdown protocol + no secrets |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Literature notes | Markdown | `docs/research/drafts/literature/...` | This README + repo doc lint |
| Candidate extraction list (optional) | Markdown/YAML | Within note | Must not imply graph writes |

### Sensitivity & redaction
- Do not infer or reconstruct sensitive locations from partial evidence.
- If a source discusses culturally sensitive topics, use **generalized** descriptions and refer to governance guidance.

### Quality signals
- Bibliographic completeness (author/year/title/publisher/doi/url).
- Clear separation of: **Facts quoted/paraphrased** vs **Inference** vs **Hypothesis**.
- Explicit “KFM impact” mapping (what this informs).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Literature drafts are **not** automatically STAC items.
If a literature source is also treated as an ingestible document asset, record its STAC item ID in the note.

### DCAT
If a literature source materially informs a dataset design, add a pointer in the relevant dataset’s DCAT mapping docs (when those exist).

### PROV-O
If a literature note results in a generated artifact (e.g., a promoted story node or schema), ensure the promoted artifact records:
- `prov:wasDerivedFrom` (source identifiers)
- `prov:wasGeneratedBy` (pipeline activity/run IDs, if applicable)

### Versioning
- Prefer additive edits; do not rewrite history without noting what changed and why.
- If a note materially changes interpretation, record it in the note’s “Change log” section.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Research drafts | Exploration + synthesis | Markdown docs |
| Governed Story Nodes | Provenance-linked narrative | Story Node template + API retrieval |
| APIs | Contracted access layer | REST/GraphQL |

### Interfaces / contracts
If literature implies an API/contract change, do **not** implement it here; draft a governed contract doc using:
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Literature itself is not shown in Focus Mode unless it becomes part of:
- A cited story node
- A cited design/system document referenced by story nodes

### Provenance-linked narrative rule
If promoting content:
- Every factual claim in a story node must map to a cited dataset/document ID.
- Literature may support interpretation, but should not replace primary evidence where primary evidence is required.

### Optional structured controls (for promoted artifacts only)
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Front-matter `path` matches file location
- [ ] No secrets/credentials embedded
- [ ] Sensitive information handled per governance refs

### Reproduction
~~~bash
# No runtime steps for literature drafts.
# Ensure markdown lint/doc checks pass in CI.
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Historian/editor review: recommended before promotion to story nodes.
- FAIR+CARE council review: required if content touches sensitive communities/topics (per governance).

### CARE / sovereignty considerations
- Do not publish precise sensitive locations.
- Respect community guidance and any applicable restrictions.

### AI usage constraints
- Allowed: summarize, structure extraction, translate, keyword index.
- Prohibited: generating policy, inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for literature drafts | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

