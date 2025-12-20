---
title: "Source Summaries — Books (README)"
path: "docs/research/source_summaries/by_type/books/README.md"
version: "v0.1.0"
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

doc_uuid: "urn:kfm:doc:research:source-summaries:by-type:books:readme:v0.1.0"
semantic_document_id: "kfm-research-source-summaries-by-type-books-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:research:source-summaries:by-type:books:readme:v0.1.0"
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

# Source Summaries — Books

## 📘 Overview

### Purpose
This folder contains **book-type source summaries** used to inform Kansas Frontier Matrix (KFM) decisions.
These summaries are **research artifacts**: they do not directly change runtime behavior, but they can
justify and motivate changes to governed docs, schemas, pipelines, ontology, APIs, UI patterns, and story
work.

### Scope
| In Scope | Out of Scope |
|---|---|
| Summaries of books relevant to KFM architecture, data standards, graph modeling, geospatial workflows, and narrative systems | Reproducing book contents, creating new governance policy, or adding unsourced claims into Story Nodes |
| Capturing bibliographic metadata (author, year, edition, DOI/ISBN if present) | Treating summaries as authoritative standards without promoting to governed docs |
| Extracting actionable takeaways per KFM pipeline stage | “Best practices” claims without clear evidence trail to the source |

### Audience
- Primary: KFM maintainers, pipeline/ontology/API/UI contributors
- Secondary: Researchers producing Story Nodes and Focus Mode narratives

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Source summary**: A structured note capturing what a source says and how it may affect KFM.
  - **Book**: A monograph / edited volume (print or ebook), typically with ISBN and sometimes DOI.
  - **Pipeline**: The canonical KFM ordering from ingest to Focus Mode (see diagram below).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Parent index | `docs/research/source_summaries/by_type/README.md` | Docs | Cross-type index (papers/books/datasets/etc.) |
| This README | `docs/research/source_summaries/by_type/books/README.md` | Docs | Book-specific guidance |
| Book summaries | `docs/research/source_summaries/by_type/books/BOOK__*.md` | Research | One file per book (convention for this folder; draft) |

### Definition of done (for this document)
- [ ] Front-matter complete + `path` matches file location
- [ ] “How this relates to the KFM pipeline” is explained and diagrammed
- [ ] Conventions are clearly labeled as **draft** and do not claim to be governance
- [ ] Footer refs present

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/source_summaries/by_type/books/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Source summary indexes | `docs/research/source_summaries/by_type/` | Type-specific README(s) + summary files |
| Governed docs | `docs/` | Standards, architecture docs, security, governance |
| Pipelines | `src/pipelines/` | ETL, catalog build, graph build |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/telemetry/etc.) |
| Graph | `src/graph/` | Ontology bindings, migrations, constraints |
| APIs | `src/server/` + docs | REST/GraphQL contracts and tests |
| Frontend | `web/` | React + Map UI |
| Story Nodes | `docs/reports/.../story_nodes/` | Provenance-linked narratives |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    └── 📁 source_summaries/
        └── 📁 by_type/
            ├── 📄 README.md
            └── 📁 books/
                ├── 📄 README.md
                ├── 📄 BOOK__example-slug.md
                └── 📄 BOOK__another-example.md
~~~

## 🧭 Context

### Background
Books often provide:
- conceptual frameworks (e.g., “how to think about” a problem),
- established terminology,
- validated approaches from a domain community,
- or practical patterns that can be adapted into KFM’s governed system.

Book summaries help prevent “reinventing the wheel” and provide a traceable rationale for downstream
engineering and narrative decisions.

### Assumptions
- A source summary is **not** a contract: it must not silently become a standard.
- If a book leads to a normative change, that change must be captured in **governed docs** (and/or schemas,
tests, and migration notes).

### Constraints / invariants
- The canonical KFM ordering remains:
  **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
- The UI consumes data via **API contracts** (no direct graph dependency).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do book summaries require a dedicated mini-template file under `docs/templates/`? | TBD | TBD |
| Should we catalog “source summary” files in DCAT as documentation datasets? | TBD | TBD |

### Future extensions
- Extension point A: Add per-book “KFM impact tags” (ETL/Catalog/Graph/API/UI/Story).
- Extension point B: Link book summaries to implementation tickets (not confirmed in repo).

## 🗺️ Diagrams

### How book source summaries relate to the KFM pipeline
~~~mermaid
flowchart LR
  A[Book source] --> B[Book source summary]
  B --> C[Governed docs and standards]
  C --> D[ETL]
  D --> E[STAC DCAT PROV catalogs]
  E --> F[Neo4j graph]
  F --> G[API layer]
  G --> H[React map UI]
  H --> I[Story Nodes]
  I --> J[Focus Mode]

  B --> I
~~~

### Notes on diagrams
- Mermaid labels should avoid embedded HTML to reduce renderer incompatibilities.

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Book (digital) | PDF/EPUB/HTML | External source | License + citation captured |
| Book (citation only) | BibTeX / text | External catalogs | Basic fields present (title/author/year) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Book source summary | Markdown | `docs/research/source_summaries/by_type/books/BOOK__*.md` | This README (draft conventions) |
| Follow-on governed doc | Markdown | `docs/...` | Governed template(s) |
| Follow-on work | code/data | `src/`, `schemas/`, `data/` | Schema/tests required |

### Conventions for individual book summaries
These conventions are **draft** for this folder and may change.

#### File naming
- `BOOK__<short-slug>.md`
  - Example: `BOOK__scalable-data-management-future-hardware.md`

#### Minimal summary structure
~~~text
# <Book title>

## Citation
- Authors:
- Year:
- Publisher:
- Edition:
- DOI/ISBN (if present):
- License/access notes:

## Core thesis (what the book argues)
- ...

## Key concepts and vocabulary (as used by the book)
- ...

## Evidence worth reusing (claims we can cite elsewhere)
- ...

## KFM implications (map to pipeline stages)
- ETL:
- STAC/DCAT/PROV:
- Graph:
- APIs:
- UI:
- Story Nodes / Focus Mode:

## Risks / limitations
- ...

## Follow-on actions
- [ ] Proposed doc changes:
- [ ] Proposed schema changes:
- [ ] Proposed tickets:
~~~

### Sensitivity & redaction
- If a book discusses culturally sensitive locations or restricted knowledge, do not “enrich” it with precise
coordinates or operational detail in summaries. Apply sovereignty and redaction expectations from
governance docs.

### Quality signals
- Include at least one “actionable implication” that maps to a KFM subsystem (or explicitly state “none”).
- Separate **what the book says** from **how KFM might use it**.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not confirmed in repo: whether book sources are represented as STAC Items.
- If a book is ingested as an asset, link any resulting catalog identifiers here.

### DCAT
- Not confirmed in repo: whether documentation assets are published as DCAT datasets.
- If applicable, link the DCAT dataset identifier(s).

### PROV-O
- If a book summary leads to a specific pipeline change, capture lineage at the change site (e.g., a governed
doc or a pipeline run record), and reference the book summary as an input document.

### Versioning
- Book summaries can change as interpretations improve. When a summary meaningfully changes, bump its
version and record the change in its version history section.

## 🧱 Architecture

### Components
This folder is documentation-only, but it influences:
- pipeline architecture and ETL implementation,
- catalog mapping decisions,
- ontology and graph modeling,
- API contracts,
- UI patterns,
- Story Nodes and Focus Mode narratives.

### Interfaces / contracts
- Book summaries do not define API contracts.
- Any contract changes must be defined in API contract docs and tested.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Book summaries are **upstream rationale**.
- If a book is used as narrative evidence, that evidence must be carried into the Story Node with explicit
source linkage and clear “fact vs interpretation” labeling.

### Provenance-linked narrative rule
- Every claim used in Story Nodes must trace to an identifiable source (book + page/section where possible,
or a more directly evidentiary primary source).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter, path consistency)
- [ ] Link checks (relative paths resolve)
- [ ] No prohibited AI actions implied (e.g., “infer sensitive locations”)
- [ ] No policy creation disguised as summaries

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) doc lint / markdown checks
# 2) link check
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If a book summary motivates:
  - new sensitive layers,
  - new public-facing endpoints,
  - or new AI narrative behaviors,
  then it likely requires additional review in the affected subsystem docs.

### CARE / sovereignty considerations
- If a summary touches Indigenous knowledge, sensitive sites, or restricted cultural material, apply CARE
labels and redaction expectations (see governance docs).

### AI usage constraints
- Summaries may be AI-assisted, but must remain evidence-led and must not add speculative content.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-20 | Initial README for book source summaries | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

