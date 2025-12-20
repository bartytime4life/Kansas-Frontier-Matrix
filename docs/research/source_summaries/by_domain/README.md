---
title: "Research Source Summaries — By Domain"
path: "docs/research/source_summaries/by_domain/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:research:source-summaries:by-domain:readme:v1.0.0"
semantic_document_id: "kfm-research-source-summaries-by-domain-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:source-summaries:by-domain:readme:v1.0.0"
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

# Research Source Summaries — By Domain

## 📘 Overview

### Purpose
This directory contains **governed Markdown summaries of external sources**, organized by **domain**, so contributors can:
- quickly find prior art (standards, methods, best practices, historical context),
- translate findings into KFM decisions (schemas, contracts, pipelines, UI behaviors),
- and avoid introducing “floating knowledge” (claims without provenance) into downstream docs or narratives.

These summaries are **supporting research artifacts**. They are not a substitute for:
- catalog metadata (STAC/DCAT/PROV),
- graph assertions (Neo4j nodes/edges),
- API contracts,
- or Story Nodes / Focus Mode narratives.

### Scope
| In Scope | Out of Scope |
|---|---|
| Domain-indexed source summaries in Markdown | Storing full source texts (especially copyrighted material) |
| Bibliographic references, identifiers (DOI/URL), and usage notes | Generating new governance/policy (belongs in `docs/governance/`) |
| “KFM implications” mapping to impacted pipeline stages | Treating a secondary source as primary evidence without explicit labeling |
| Action items (tickets/PR refs), open questions, and validation notes | Embedding unsourced narrative intended for Focus Mode |

### Audience
- Primary: KFM contributors (data/ETL, cataloging, graph/ontology, API, UI, story tooling)
- Secondary: reviewers (governance, security, historians/curators), future maintainers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this area (recommended):
  - **Domain**: a topical bucket used for retrieval and maintenance (e.g., “geospatial”, “data_engineering”).
  - **Source summary**: a governed synthesis of a source, focused on KFM-relevant takeaways.
  - **Evidence vs. background**: whether the source directly supports claims about historical reality (evidence) or informs design decisions (background).
  - **Implication**: a concrete constraint, requirement, or caution that affects a KFM subsystem.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `docs/research/source_summaries/by_domain/README.md` | Repo maintainers | Index + conventions |
| Domain folders | `docs/research/source_summaries/by_domain/<domain_slug>/` | Domain owners (TBD) | Domain-specific index + summaries |
| Source summary docs | `docs/research/source_summaries/by_domain/<domain_slug>/<source_slug>.md` | Author listed in file | Use a governed template |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory layout and conventions are clear
- [ ] Safety + governance expectations are explicit (FAIR+CARE, sovereignty, no sensitive location inference)
- [ ] Validation steps listed and repeatable
- [ ] Version history updated

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/source_summaries/by_domain/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline invariants + system map |
| Templates | `docs/templates/` | Governed templates (Universal, Story Node, API Contract Extension) |
| Data domains | `data/` | Raw/work/processed + catalogs per domain |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV artifacts |
| Pipelines | `src/pipelines/` | ETL + catalog build logic |
| Graph | `src/graph/`, `docs/graph/` | Ontology/model docs + graph ingest logic |
| API layer | `src/server/` + `docs/` | Contracted access (REST/GraphQL), never direct UI→Neo4j |
| UI | `web/` + `docs/design/` | Map + Focus Mode UX |
| Story artifacts | `docs/reports/./story_nodes/` | Story Nodes with provenance |

### Expected sub-structure for this area
~~~text
📁 docs/
└── 📁 research/
    └── 📁 source_summaries/
        └── 📁 by_domain/
            ├── 📄 README.md
            ├── 📁 <domain_slug>/
            │   ├── 📄 README.md
            │   ├── 📄 <source_slug>.md
            │   └── 📄 <source_slug>.md
            └── 📁 <domain_slug>/
                ├── 📄 README.md
                └── 📄 <source_slug>.md
~~~

**Domain slug guidance (recommended):**
- Use lowercase + underscores, e.g. `geospatial`, `data_engineering`, `ml_nlp`, `ui_ux`.
- Keep domains **coarse**; prefer cross-linking over duplicating summaries.

## 🧭 Context

### Relationship to the canonical KFM pipeline
Research summaries are upstream inputs to design and implementation work across the pipeline:
- ETL decisions (formats, validation, determinism)
- STAC/DCAT/PROV patterns (metadata modeling, lineage)
- Graph/ontology decisions (entities, relationships, provenance)
- API contract decisions (payload shapes, redaction rules)
- UI decisions (map rendering, Focus Mode constraints)
- Story Node decisions (what counts as evidence, narrative structure)

**Important invariant reminder:** the UI must not read Neo4j directly; all access is through the API contracts.

### How to add a new source summary (workflow)
1. Pick the **primary domain folder** (create it if needed).
2. Create a new Markdown file under that domain:
   - `docs/research/source_summaries/by_domain/<domain_slug>/<source_slug>.md`
3. Use a governed template:
   - Default: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
   - If the summary is intended as a narrative artifact: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
4. In the summary body, include (minimum):
   - **Bibliographic citation** + stable identifier (DOI/URL)
   - **What the source says** (tight summary; avoid large pasted excerpts)
   - **KFM implications** (what decisions it affects; which pipeline stages)
   - **Risks/limitations** (what not to overclaim)
   - **Action items** (tickets/PRs/tests/docs updates)
5. Update the domain `README.md` index (and optionally add to an index table in this file).

### Fact vs inference vs hypothesis (required labeling)
Within summaries, explicitly label:
- **Fact**: directly supported by the source (with a citation/identifier)
- **Inference**: conclusion drawn from source statements (say “inference”)
- **Hypothesis**: speculative, to be validated (say “hypothesis”)

### Copyright and fair use (summaries)
- Prefer paraphrase + citation.
- Keep quotes short and purpose-driven.
- Do not store full PDFs/text unless licensing explicitly allows (and if stored, keep them outside this folder).

## 🗺️ Diagrams

~~~mermaid
graph LR
  SRC["External source - paper, standard, report"] --> SUM["Source summary - this folder"]
  SUM --> DEC["Design decision or ticket"]
  DEC --> IMP["Implementation - ETL, Catalog, Graph, API, UI"]
  IMP --> SN["Story Node artifact"]
  SN --> FM["Focus Mode experience"]
~~~

~~~mermaid
sequenceDiagram
  participant R as Researcher/Contributor
  participant S as Source Summary (docs)
  participant T as Ticket/Issue Tracker
  participant P as PR (code/schemas/docs)
  R->>S: Write/Update summary (with citations + implications)
  S->>T: Record action items (links/IDs)
  T->>P: Implement change + tests + validation notes
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where it comes from | Notes |
|---|---|---|---|
| Papers / books / standards | PDF/HTML | External publishers / standards bodies | Track DOI/URL + access date |
| Internal design references | Markdown/PDF | `docs/` | Prefer canonical docs over ad-hoc notes |
| Dataset documentation | Markdown/JSON | `data/` + `docs/data/` | Link to STAC/DCAT/PROV IDs if applicable |

### Outputs
| Output | Format | Path | Notes |
|---|---|---|---|
| Source summary | Markdown | `docs/research/source_summaries/by_domain/<domain>/<source>.md` | Governed doc with front-matter |
| Domain index | Markdown | `docs/research/source_summaries/by_domain/<domain>/README.md` | Lists sources and status |
| Cross-links | Markdown | inline | Prefer links/IDs over duplication |

### Sensitivity & redaction
- Do not include secrets, access tokens, or private credentials.
- Do not infer or publish precise locations for sensitive sites.
- If a source discusses culturally sensitive materials, document handling expectations and route to governance review.

## 🌐 STAC, DCAT & PROV Alignment

This folder does not produce catalogs directly, but summaries should **point to** relevant catalog artifacts when they exist:
- STAC: reference collection/item IDs where a dataset or asset is discussed
- DCAT: reference dataset IDs for discoverability context
- PROV: reference activity/run IDs when a method impacts lineage expectations

If identifiers are not available yet, record a to-do as an action item rather than inventing IDs.

## 🧱 Architecture

### Components (summary-level view)
| Component | Responsibility | Interface / Contract |
|---|---|---|
| Source summaries (this folder) | Curated research synthesis + implications | Governed Markdown protocol |
| ETL | Deterministic ingest + normalization | Inputs in `data/raw/`, outputs to `data/processed/` |
| STAC/DCAT/PROV | Catalog + dataset metadata + lineage | JSON + profile validations |
| Neo4j graph | Semantic representation + provenance links | Ingested from catalog outputs |
| API layer | Contracted access + redaction | REST/GraphQL contracts + tests |
| UI | Map + narrative UX | Uses API only (no direct graph access) |
| Story Nodes | Provenanced narrative artifacts | Story Node v3 template + evidence links |

### Extension points (use when a summary implies new work)
- [ ] New domain folder required?
- [ ] New dataset or metadata profile required?
- [ ] Ontology/graph label/relationship addition required (with migration plan)?
- [ ] API contract extension required (with contract tests)?
- [ ] UI feature requires provenance pointers + sensitivity handling?
- [ ] Story Node changes required (with evidence mapping)?

## 🧠 Story Node & Focus Mode Integration

- Source summaries are **inputs** to Story Nodes; they should not be treated as a Story Node unless intentionally authored as one.
- Focus Mode content must be provenance-backed; research summaries often serve as **background** and should not replace primary evidence.

**Optional structured controls (for story integrations):**
~~~yaml
# Example only — use in the target Story Node file if applicable
focus_mode:
  allow_ai_generated: false
  provenance_required: true
  sensitive_location_generalization: required
~~~

## 🧪 Validation & CI/CD

### Validation checklist (docs)
- [ ] Front-matter keys present and valid
- [ ] No broken internal references (paths/IDs)
- [ ] No sensitive location inference
- [ ] Clear Fact/Inference/Hypothesis labeling in summaries
- [ ] If the summary drives a change: validation steps for that change are linked (tests, schema validation, etc.)

### Reproduction
If a summary motivates a change that can be tested, record reproducible steps in the affected subsystem doc or PR, for example:
- schema lint + catalog integrity checks
- pipeline unit tests
- contract tests

(Commands are repository-specific; record the exact commands where they are defined.)

### Telemetry signals (if the research drives an observable feature)
| Signal | Where emitted | Purpose | Schema |
|---|---|---|---|
| TBD / N/A | TBD | TBD | `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- If a summary impacts: catalogs, ontology, API contracts, or Focus Mode behavior → requires human review.
- If a summary includes or references culturally sensitive content → requires sovereignty/ethics review.

### CARE considerations
- Record any community-sensitive constraints explicitly.
- Prefer generalization/redaction strategies in downstream contracts and UI when appropriate.

### AI use constraints
Follow the front-matter constraints:
- Allowed: summarization/structuring/translation/indexing
- Prohibited: generating new policy, inferring sensitive locations

## 🕰️ Version History

| Version | Date | Change | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-20 | Initial README for domain-organized source summaries | TBD |

---

### Footer refs
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Templates: `docs/templates/`
- Canonical ordering: `docs/MASTER_GUIDE_v12.md`

