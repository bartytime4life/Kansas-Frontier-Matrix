---
title: "Reference Library — docs/reference"
path: "docs/reference/README.md"
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

doc_uuid: "urn:kfm:doc:reference:library-readme:v1.0.0"
semantic_document_id: "kfm-reference-library-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:reference:library-readme:v1.0.0"
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

# Reference Library — docs/reference

## 📘 Overview

### Purpose
- `docs/reference/` is a **curated index** of supportive materials (standards, textbooks, papers, design notes, and internal PDFs) that help contributors implement Kansas Frontier Matrix (KFM) consistently.
- This folder is **non-normative**: it should *support* decisions, not *be* the decision record. Canonical contracts and policies live in `docs/standards/`, `docs/governance/`, and `docs/MASTER_GUIDE_v12.md`.

### Scope
| In Scope | Out of Scope |
|---|---|
| Reading list + reference index, pointers to project “reference files” used in MCP/LLM sessions, optional vendored copies when licensing permits | Authoritative project policy/standards (use `docs/standards/` + `docs/governance/`), primary architecture contracts (use `docs/MASTER_GUIDE_v12.md`), datasets/assets (use `data/` + STAC/DCAT/PROV), code (use `src/` / `web/`) |
| Lightweight “how to use” notes (authored by contributors) | Story Nodes themselves (use `docs/reports/story_nodes/` + graph), raw research dumps without metadata |

### Audience
- Primary: Contributors implementing **ETL → Catalogs → Graph → APIs → UI → Story/Focus** workstreams.
- Secondary: Reviewers doing governance, provenance audits, and “why did we choose this approach?” traceability.

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Reference file**: A supportive document used to inform implementation (not automatically evidence).
  - **Vendored copy**: A local copy stored in-repo (only if licensing allows).
  - **Pointer-only entry**: Index metadata without storing the file in-repo.
  - **Evidence source**: A dataset/document ingested into STAC/DCAT/PROV + Graph and therefore citeable in Story Nodes.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | Maintainers | Source of truth for ordering + boundaries |
| Markdown/doc governance | `docs/standards/` | Maintainers | Normative doc standards (CI-clean) |
| Document templates | `docs/templates/` | Maintainers | Universal / Story Node / API Contract templates |
| Reference index | `docs/reference/README.md` | Maintainers | This file |
| Optional reference catalog | `docs/reference/REFERENCE_CATALOG.yml` | TBD | **Planned** (not created here) |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] “Non-normative” status stated (no new policy invented here)
- [ ] Reference entries include minimal metadata (title, purpose, license status, storage decision)
- [ ] Clear rules for when a reference can become evidence (STAC/DCAT/PROV + graph ingestion)
- [ ] Validation checklist included (license + size + link integrity)

## 🗂️ Directory Layout

### This document
- `path`: `docs/reference/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |
| Documentation | `docs/` | Canonical governed docs |
| Standards | `docs/standards/` | Normative project standards |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |
| Reference library | `docs/reference/` | Supportive docs index + (optional) vendored copies |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 reference/
    ├── 📄 README.md
    ├── 📄 REFERENCE_CATALOG.yml                 (planned; optional)
    ├── 📁 library/                              (optional; vendored PDFs when allowed)
    │   ├── 📄 <third_party_doc>.pdf
    │   └── 📄 LICENSES.md                       (optional; per-file license notes)
    ├── 📁 standards/                            (optional; non-normative local copies)
    │   └── 📄 <spec_copy>.pdf
    └── 📁 notes/                                (optional; contributor-authored notes)
        └── 📄 <topic_note>.md
~~~

## 🧭 Context

### Background
- KFM work spans multiple domains (geospatial ETL, catalogs, graph semantics, APIs, UI, narrative). Without a reference index, “why/how” context tends to fragment across chats, tickets, and ad-hoc links.
- `docs/reference/` exists to keep *support materials discoverable* while keeping **normative** docs in governed locations.

### Assumptions
- Some reference files may be large; storage may require Git LFS or pointer-only approaches.
- Not all documents can be stored in-repo due to licensing restrictions; license status must be recorded.

### Constraints / invariants
- The canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes data via **APIs** (no direct graph dependency).
- **Reference docs are not automatically evidence**. If a reference is used to justify a factual claim in Story/Focus Mode, it must be represented through governed data artifacts and provenance.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we vendor PDFs in-repo, use pointer-only entries, or store in object storage with stable IDs? | TBD | TBD |
| Should `REFERENCE_CATALOG.yml` be required (CI check) once introduced? | TBD | TBD |
| Do we standardize Git LFS for `docs/reference/library/`? | TBD | TBD |
| What is the minimum metadata for each reference entry (license, edition, tags, pipeline stages)? | TBD | TBD |

### Future extensions
- Add `docs/reference/REFERENCE_CATALOG.yml` with schema validation (license, tags, source, local_path).
- Add CI checks for:
  - broken internal links
  - missing license metadata for vendored copies
  - excessive file size without LFS

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  R["Reference Library - non normative"] --> D["Docs and Standards - governed"]
  D --> A[ETL]
  A --> B["STAC DCAT PROV Catalogs"]
  B --> C["Neo4j Graph"]
  C --> E[APIs]
  E --> F["React Map UI"]
  F --> G["Story Nodes"]
  G --> H["Focus Mode"]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Reference documents | PDF/MD | Third-party sources or internal drafts | License check, malware scan (if applicable), filename conventions |
| Reference metadata | Markdown tables / YAML (planned) | Maintainers | Required fields present; broken-link check |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Reference index | Markdown | `docs/reference/README.md` | KFM-MDP |
| Optional catalog | YAML | `docs/reference/REFERENCE_CATALOG.yml` | (planned; add schema later) |
| Optional vendored copies | PDF | `docs/reference/library/` | License must allow |

### Sensitivity & redaction
- Do not add documents containing private data, restricted site locations, or culturally sensitive information without explicit governance approval.
- If a reference touches sensitive locations, it must not be used to infer or disclose precise coordinates in public outputs.

### Quality signals
- Every entry includes: **title**, **why it’s relevant**, **storage decision**, **license status**.
- The index remains navigable (grouped by pipeline stage + topic).

### Curated reference catalog seed
> This is an initial seed list. **License status is not confirmed in repo**; verify before vendoring.

| Category | Reference (title / filename) | Suggested location | Supports | Notes |
|---|---|---|---|---|
| KFM architecture | Kansas Frontier Matrix 1.0 — System Documentation (PDF) | `docs/architecture/` or `docs/reference/library/` | All stages | High-level system + directory roles |
| KFM architecture | Kansas Frontier Matrix — System Structure and Scope (PDF) | `docs/architecture/` or `docs/reference/library/` | All stages | UX concepts (Story Nodes, Focus Mode) + governance framing |
| KFM design | Kansas-Frontier-Matrix — Open-Source Geospatial Historical Mapping Hub Design (PDF) | `docs/design/` or `docs/reference/library/` | UI/Story | Design rationale; not normative |
| Research protocol | Scientific Method — Research — Master Coder Protocol Documentation (PDF) | `docs/reference/library/` | ETL/AI/CI | General QA/reproducibility ideas |
| Standards (writing) | Comprehensive Guide to Markdown in Programming and Documentation (PDF) | `docs/reference/library/` | Docs | General Markdown guidance (non-normative) |
| Geospatial | Python Geospatial Analysis Cookbook (PDF) | `docs/reference/library/` | ETL/Catalog/UI | Recipes for geospatial operations |
| Geospatial | Introduction to Spatial Data Analysis and Visualisation in R (PDF) | `docs/reference/library/` | ETL/Analysis | Spatial analysis concepts |
| Stats | Understanding Statistics & Experimental Design (PDF) | `docs/reference/library/` | AI/Validation | Experimental design, validation habits |
| Stats/ML | Data Science & Machine Learning (Mathematical & Statistical Methods) (PDF) | `docs/reference/library/` | AI/Validation | Statistical grounding for models |
| Bayesian | Bayesian Computational Methods (PDF) | `docs/reference/library/` | AI/Uncertainty | Useful for uncertainty metadata thinking |
| ML | Artificial Neural Networks — An Introduction (PDF) | `docs/reference/library/` | AI | Background |
| ML | Deep Learning in Python — Prerequisites (PDF) | `docs/reference/library/` | AI | Background |
| Agents | AI Foundations of Computational Agents (3rd Ed) (PDF) | `docs/reference/library/` | AI | Agent reasoning background |
| Data mining | Data Mining Concepts & Applications (PDF) | `docs/reference/library/` | ETL/AI | Pattern discovery background |
| Graph theory | Spectral Geometry of Graphs (PDF) | `docs/reference/library/` | Graph/AI | Graph methods background |
| Systems | Scalable Data Management for Future Hardware (PDF) | `docs/reference/library/` | API/Graph | Scalability + system design background |
| UI/UX | Designing Virtual Worlds (PDF) | `docs/reference/library/` | UI/Story | Useful for “immersive” narrative UX thinking |
| Frontend | CSS Notes for Professionals (PDF) | `docs/reference/library/` | UI | CSS reference |
| Modeling | Scientific Modeling and Simulation — NASA-grade guide (PDF) | `docs/reference/library/` | Modeling/Validation | Modeling + simulation mindset |
| Optimization | Generalized Topology Optimization for Structural Design (PDF) | `docs/reference/library/` | (optional) | Background; only keep if used |

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- This reference library does **not** directly create STAC Items/Collections.
- If any reference document becomes an **evidence source** (i.e., cited in Story Nodes), it should be handled as a governed document asset with appropriate catalog + provenance.

### DCAT
- If reference documents are distributed to users as part of a dataset package, consider describing that package as a DCAT Dataset/Distribution (optional).

### PROV-O
- If a reference document is transformed (e.g., summarized into a governed note used downstream), record that as a PROV activity in the relevant pipeline logs/artifacts (not in this README).

### Versioning
- Prefer stable filenames that encode edition/year:
  - Example: `topic__author__year__edition.pdf`
- Record “source edition” in metadata for any vendored copy.

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

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| UI layer registry | `web/` | Schema-validated (path TBD) |

### Extension points checklist
- [ ] Add new reference entry with metadata + tags
- [ ] Confirm license and storage approach (pointer vs vendored)
- [ ] If used as evidence: ingest as governed asset (catalog + provenance) before citing

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Indirectly. These references support implementation decisions, but **Focus Mode must remain provenance-first**.
- A reference is only citeable in Story/Focus contexts if it is represented as a governed source asset (catalog + provenance) or otherwise explicitly approved.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
# Not applicable for docs/reference/README.md.
# Use Story Node template controls when authoring Story Nodes.
~~~

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] Entries are grouped and readable (no “dump list”)
- [ ] Internal paths referenced here exist or are clearly marked planned/TBD
- [ ] Vendored copies (if any) have license notes recorded
- [ ] No sensitive locations or restricted info introduced
- [ ] No policy is created here (policy belongs in governance/standards docs)

## ⚖ FAIR+CARE & Governance

### Governance approvals required
- Adding a pointer-only entry: usually **no**, unless it concerns sensitive topics.
- Vendoring a document: **license review required**.
- Any reference containing culturally sensitive info: **FAIR+CARE review required**.
- Any reference that could expose restricted locations: **sovereignty + security review required**.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `docs/reference/README.md` scaffold + seed list | TBD |

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Footer refs:
- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

