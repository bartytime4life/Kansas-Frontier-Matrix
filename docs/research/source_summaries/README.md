---
title: "Research — Source Summaries"
path: "docs/research/source_summaries/README.md"
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

doc_uuid: "urn:kfm:doc:research:source-summaries:readme:v1.0.0"
semantic_document_id: "kfm-research-source-summaries-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:source-summaries:readme:v1.0.0"
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

# Research — Source Summaries

## 📘 Overview

### Purpose
`docs/research/source_summaries/` is a **curation workspace** for capturing structured notes about candidate sources (papers, datasets, maps, PDFs, archives, etc.) before or during ingestion into KFM.

Source summaries are **not** authoritative story content. They are intended to:
- speed up ingestion planning (ETL parsing, licensing, coverage, format)
- capture provenance metadata early (what, where from, when retrieved, license)
- support later catalog/graph/story work by recording candidate entities, events, places, and links

This work must respect the canonical KFM pipeline ordering:
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode.**

### Scope
| In Scope | Out of Scope |
|---|---|
| Summaries of candidate sources + ingestion notes | Public narrative/storytelling without provenance |
| Format/license/provenance capture | Any attempt to bypass catalogs/graph/API layers |
| Candidate entity lists + keywords | Inference of sensitive locations or identities |

### Audience
- Primary: Curators, researchers, ingestion/ETL maintainers
- Secondary: Story Node authors, graph/modeling contributors

### Definitions
- Glossary: `docs/glossary.md` (**not confirmed in repo** — update link if the glossary lives elsewhere)

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `docs/research/source_summaries/README.md` | Docs | Index + conventions for this area |
| Source summary files | `docs/research/source_summaries/**/*.md` | Research | One per source (or per bundle) |
| Source files (if imported) | `data/raw/...` | ETL | Raw copies should live under `data/` once accepted |

### Definition of done
- [ ] This README follows the governed doc template
- [ ] Each source summary is provenance-first (what/where/when/license)
- [ ] No unsourced narrative claims are presented as facts
- [ ] Any sensitive content is flagged and handled per sovereignty guidance

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/source_summaries/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV artifacts |
| Graph | `src/graph/` | Ontology bindings + graph build |
| Pipelines | `src/pipelines/` | ETL + catalog build |
| Story Nodes | `docs/reports/.../story_nodes/` | Provenance-linked narrative artifacts |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 research/
│   └── 📁 source_summaries/
│       ├── 📄 README.md
│       ├── 📁 by_domain/
│       │   └── 📄 <domain>__<source-slug>.md
│       ├── 📁 by_type/
│       │   ├── 📁 papers/
│       │   ├── 📁 datasets/
│       │   ├── 📁 maps/
│       │   └── 📁 archives/
│       └── 📁 _attachments/        # optional: small non-source artifacts (notes, thumbnails)
~~~

> Folder names above are a suggested layout. Keep organization deterministic and avoid duplicate copies of raw source files here; raw sources belong under `data/raw/`.

## 🧭 Context

### Background
KFM grows by adding new data domains and evidence products. Source summaries provide a lightweight, provenance-first staging area to evaluate and plan ingestion without prematurely committing to catalog/graph changes.

### Assumptions
- Source summaries may be AI-assisted, but remain **human-reviewed** before being used to justify ingestion or narrative.
- When a source becomes “real” KFM content, it should be represented through the canonical pipeline (catalogs → graph → API → UI).

### Constraints / invariants
- Canonical ordering is preserved: ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumers access the graph **only through APIs** (no direct Neo4j dependency).
- Summaries must not infer sensitive locations; when in doubt, generalize or omit.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we want a dedicated “Source Summary” template file? | TBD | TBD |
| Do we want automated indexing of summaries into a catalog-like registry? | TBD | TBD |

### Future extensions
- Add `docs/templates/TEMPLATE__SOURCE_SUMMARY.md` (**not confirmed in repo**)
- Add a lightweight validator for required summary fields (license/provenance)

## 🗺️ Diagrams

### How source summaries fit into the system
~~~mermaid
flowchart LR
  A[Candidate source identified] --> B[Source summary written here]
  B --> C{Accepted for ingestion?}
  C -- No --> D[Archive / keep as research note]
  C -- Yes --> E[ETL + Normalization]
  E --> F[STAC/DCAT/PROV]
  F --> G[Neo4j Graph]
  G --> H[APIs]
  H --> I[UI]
  I --> J[Story Nodes]
  J --> K[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Candidate source | PDF / Web / CSV / GeoPackage / etc. | external or `data/raw/` | license known; retrieval date recorded |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Source summary | Markdown | `docs/research/source_summaries/.../*.md` | governed doc structure (recommended) |

### Sensitivity & redaction
- If a source includes culturally sensitive sites, restricted locations, or personally identifying details, note it explicitly in the summary and avoid copying sensitive coordinates into the repo.
- Follow `docs/governance/SOVEREIGNTY.md` redaction/generalization rules.

### Quality signals
- Provenance completeness (source URL or citation, retrieval date, license)
- Coverage completeness (time range and/or spatial extent if known)
- Traceability (hash or stable identifier once ingested)

## 🌐 STAC, DCAT & PROV Alignment

### When a source becomes an ingested artifact
Create/attach:
- STAC Item(s) for spatiotemporal assets
- DCAT dataset record for the dataset/product
- PROV activity describing extraction/transform runs

### What to reference from a summary (when available)
- STAC item/collection IDs
- DCAT dataset identifiers
- PROV activity/run IDs

## 🧱 Architecture

### How this area is served
This directory is documentation-only. It should not be treated as an API contract or a public narrative surface by default.

If a summary is used to support Focus Mode or Story Nodes, it must first be converted into a provenance-linked artifact (e.g., Story Node, cataloged evidence asset) served via the API layer.

## 🧠 Story Node & Focus Mode Integration

### Provenance-linked narrative rule
- **Every factual claim that ships to UI/Focus Mode must trace to a dataset / record / asset ID.**
- Source summaries can list candidate claims, but must clearly label them as *notes* until linked to ingested assets.

### Suggested “source summary” skeleton
~~~markdown
# <Source Title>

## Citation
- Author / org:
- Year:
- URL / archive ref:
- Retrieved:
- License / rights:

## What it contains
- Data type(s):
- Coverage (time/spatial):
- Primary themes:

## Why it matters for KFM
- Potential domains:
- Candidate Story Nodes:

## Candidate entities
| Type | Canonical name | Notes |
|---|---|---|
| Place | ... | ... |
| Person | ... | ... |
| Event | ... | ... |

## Ingestion notes
- Suggested parser/extractor:
- File formats:
- Known issues / OCR needs:

## Sensitivity notes
- CARE / sovereignty considerations:
- Redaction/generalization:
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter keys present and valid)
- [ ] No prohibited AI actions implied (e.g., sensitive location inference)
- [ ] Links resolve (where applicable)
- [ ] If referencing IDs (STAC/DCAT/PROV/graph), ensure they exist or have tickets

## ⚖ FAIR+CARE & Governance

### Review gates
- If summaries are used to justify ingestion of sensitive data, route through appropriate governance review.

### AI usage constraints
- Allowed: summarization, structure extraction, translation, keyword indexing
- Prohibited: policy generation, inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for source summaries area | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

