---
title: "Research Evaluations — Diagram Assets"
path: "docs/research/evaluations/assets/diagrams/README.md"
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

doc_uuid: "urn:kfm:doc:research:evaluations:assets:diagrams:readme:v1.0.0"
semantic_document_id: "kfm-research-evaluations-assets-diagrams-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:evaluations:assets:diagrams:readme:v1.0.0"
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

# Research Evaluations — Diagram Assets

## 📘 Overview

### Purpose
- Provide a single, predictable place for **visual diagrams** used in research evaluation documentation (plans, experiment designs, metric definitions, pipeline diagrams, model/comparison figures).
- Keep **editable sources** and **rendered exports** together so evaluations remain reproducible and reviewable.

### Scope
| In Scope | Out of Scope |
|---|---|
| Diagrams for evaluation docs under `docs/research/evaluations/` | Dataset artifacts (those live under `data/` and catalogs) |
| Mermaid, Draw.io, SVG/PNG/PDF exports | UI screenshots for bug reports (use an issue/PR attachment workflow instead) |
| Architecture/pipeline diagrams illustrating KFM boundaries | Any diagram containing restricted location detail or PII |

### Audience
- Primary: contributors writing or reviewing evaluation docs
- Secondary: maintainers validating governance, reproducibility, and diagram provenance

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: evaluation, asset, diagram, export, provenance

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Evaluation docs | `docs/research/evaluations/` | Research | Where diagrams are referenced from |
| Diagram assets | `docs/research/evaluations/assets/diagrams/` | Research | This directory |
| Diagram exports | `docs/research/evaluations/assets/diagrams/exports/` | Research | Rendered formats (SVG/PNG/PDF) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory tree matches actual repo layout
- [ ] Conventions describe what lives here without inventing system behavior
- [ ] Sensitivity guidance is explicit (no restricted detail, no PII)

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/evaluations/assets/diagrams/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Research | `docs/research/` | Research notes, drafts, and evaluations |
| Evaluation assets | `docs/research/evaluations/assets/` | Non-code assets used by evaluation docs |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    └── 📁 evaluations/
        └── 📁 assets/
            └── 📁 diagrams/
                ├── 📄 README.md
                ├── 📁 mermaid/
                │   └── 📄 kfm-eval__<slug>.mmd
                ├── 📁 drawio/
                │   └── 📄 kfm-eval__<slug>.drawio
                ├── 📁 source/
                │   └── 📄 kfm-eval__<slug>.<edit-format>
                └── 📁 exports/
                    ├── 🖼️ kfm-eval__<slug>.svg
                    ├── 🖼️ kfm-eval__<slug>.png
                    └── 📄 kfm-eval__<slug>.pdf
~~~

## 🧭 Context

### Background
Evaluations often need diagrams to communicate:
- experimental design (datasets, splits, controls)
- metric definitions (how scores are computed)
- pipeline boundaries (what is inside/outside KFM, where contracts live)

Storing these alongside evaluation docs makes review and maintenance easier.

### Assumptions
- Evaluation documentation is stored under `docs/research/evaluations/`.
- This directory is used for **diagrams** only; other assets should be placed alongside their own subfolders under `docs/research/evaluations/assets/`.

### Constraints / invariants
- Canonical system ordering is preserved in diagrams: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI diagrams should never imply direct reads from Neo4j; contracts live at the API boundary.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should diagram source metadata be standardized (e.g., sidecar YAML)? | TBD | TBD |

### Future extensions
- Optional: add a lightweight “diagram manifest” per evaluation if reviewers need strict traceability (not confirmed in repo).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Diagram source files] --> B[Exports rendered (SVG/PNG/PDF)]
  B --> C[Evaluation docs reference exports]
  C --> D[Review + CI link checks]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Author
  participant Repo
  participant Reviewer
  Author->>Repo: Add/Update diagram source + export
  Reviewer->>Repo: Review diffs (source + export)
  Reviewer-->>Author: Request changes (naming, clarity, sensitivity)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Diagram sources | `.mmd`, `.drawio`, `.svg` (editable) | Authors | Open and render locally |
| Diagram exports | `.svg`, `.png`, `.pdf` | Authors/CI | Link + render checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered diagram exports | SVG/PNG/PDF | `docs/research/evaluations/assets/diagrams/exports/` | N/A (docs asset) |

### Sensitivity & redaction
- Do **not** include precise restricted locations, private addresses, or other sensitive details.
- Prefer generalized maps/geometry or schematic diagrams.
- If a diagram must reference sensitive content, add a clear note in the evaluation doc and follow governance guidance (not confirmed in repo).

### Quality signals
- Exports render correctly in common Markdown viewers.
- Text remains legible when embedded in docs.
- Diagram filenames are stable and descriptive.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable by default (these are documentation assets).
- If an evaluation diagram is promoted to a discoverable “evidence artifact,” consider representing it as a STAC Asset linked from the relevant Item/Collection (not confirmed in repo).

### DCAT
- Not applicable by default.

### PROV-O
- Not applicable by default.
- Evaluations that cite runs/experiments should track those in evaluation docs; diagrams can reference run IDs in captions when relevant.

### Versioning
- Version via Git history; keep source + export in the same PR to make diffs reviewable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Evaluation docs | Explain evaluation method + results | Markdown links |
| Diagram assets | Provide visuals for evaluations | Relative paths |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| N/A | N/A | N/A |

### Extension points checklist (for future work)
- [ ] Add a standard naming convention doc under `docs/standards/` (not confirmed in repo)
- [ ] Add CI link-check for diagram references (not confirmed in repo)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Generally none. These are internal research/evaluation assets.

### Provenance-linked narrative rule
- If a diagram is embedded in a story-facing doc, ensure the doc’s narrative claims still trace to dataset/record IDs.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter, fenced blocks)
- [ ] All links to `exports/` targets resolve
- [ ] No sensitive details included
- [ ] Source + export are both present for new diagrams (preferred)

### Reproduction
~~~bash
# Example placeholder commands — replace with repo-specific commands
# 1) markdown lint
# 2) link check
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| N/A | N/A | N/A |

## ⚖ FAIR+CARE & Governance

### Review gates
- Any diagram used in public-facing story content may require historian/editor review.
- Any diagram touching sensitive locations/content may require sovereignty review (not confirmed in repo).

### CARE / sovereignty considerations
- Default posture: minimize harm and avoid exposing sensitive cultural locations.

### AI usage constraints
- Do not infer or add sensitive location detail when generating or refining diagrams.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial scaffold for evaluation diagram assets | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

