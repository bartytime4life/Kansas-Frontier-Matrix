---
title: "Source Summary — Scalable Data Management for Future Hardware"
path: "docs/research/source_summaries/scalable-data-management-for-future-hardware.md"
version: "v0.1.0"
last_updated: "2025-12-20"
status: "draft"
doc_kind: "SourceSummary"
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

doc_uuid: "urn:kfm:doc:research:source-summary:scalable-data-management-for-future-hardware:v0.1.0"
semantic_document_id: "kfm-source-summary-scalable-data-management-for-future-hardware-v0.1.0"
event_source_id: "ledger:kfm:doc:research:source-summary:scalable-data-management-for-future-hardware:v0.1.0"
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

# Source Summary — Scalable Data Management for Future Hardware

## 📘 Overview

### Purpose
- Capture **governed bibliographic metadata** and a **KFM-aligned technical synopsis** for the open-access book *Scalable Data Management for Future Hardware* (Sattler, Kemper, Neumann, Teubner — eds.).
- Provide a **repeatable mapping plan** to KFM’s canonical pipeline (ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode), without implying implementation work.

### Scope
| In Scope | Out of Scope |
|---|---|
| Bibliographic metadata (title/editors/DOI/ISBN/license) | Full-text reproduction of the book |
| High-level topical summary + chapter outline | Chapter-by-chapter technical deep summaries |
| Proposed catalog + graph linkage plan (STAC/DCAT/PROV + Document node) | Implementing pipelines, parsers, endpoints, or UI features |
| Governance/sensitivity notes (license, attribution, provenance) | Any policy changes (requires human review) |

### Audience
- Primary: KFM maintainers (data/catal og/graph/API/docs)
- Secondary: Curators building technical reference panels in Focus Mode; educators using KFM’s “evidence library”

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: STAC, DCAT, PROV-O, HTAP, GPU, FPGA, RDMA, PMem, CXL, NVMe, NVRAM

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Book (primary) | DOI: `10.1007/978-3-031-74097-8` | External | Open access; CC-BY 4.0 stated in the source |
| ISBN (print) | `978-3-031-74096-1` | External | As stated in the source |
| ISBN (eBook) | `978-3-031-74097-8` | External | As stated in the source |
| Source PDF (repo) | `data/sources/...` | KFM | **TBD** (recommended placement below) |
| This summary | `docs/research/source_summaries/scalable-data-management-for-future-hardware.md` | KFM | Governed metadata + mapping plan |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Bibliographic identifiers captured (DOI, ISBNs, editors, year)
- [ ] License/attribution captured (CC-BY 4.0)
- [ ] Proposed KFM catalog + provenance mapping stated with **TBD IDs** where not confirmed in repo
- [ ] Validation steps listed and repeatable
- [ ] No prohibited AI actions implied (no sensitive location inference; no new policy generation)

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/source_summaries/scalable-data-management-for-future-hardware.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    └── 📁 source_summaries/
        └── 📄 scalable-data-management-for-future-hardware.md
~~~

## 🧭 Context

### Background
- The book frames database/data-management research in the context of major hardware and systems shifts: increased multi-core parallelism, heterogeneous accelerators (e.g., GPUs/FPGAs), evolving memory/storage hierarchies (including persistent-memory-era lessons and newer disaggregation trends), and high-speed networking (e.g., RDMA and programmable NICs).
- It summarizes outcomes of the DFG priority program SPP 2037 “Scalable Data Management for Future Hardware,” describing a multi-year, multi-project research program and a set of chapters capturing results and system implications.

### Assumptions
- This source is treated as **public** and **redistributable** under the license stated in the source (CC-BY 4.0).
- KFM will reference this source primarily as **technical background** (evidence/supporting context), not as a primary Kansas historical dataset.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Any ingestion must be deterministic and reproducible (run logs + checksums).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should technical literature be modeled as a STAC Collection (“reference-library”) or only as Document nodes + DCAT records? | TBD | TBD |
| Do we need a lightweight schema for “reference sources” in `schemas/` or reuse existing Document/Artifact schemas? | TBD | TBD |
| Should chapter-level entries become separate graph nodes (DocumentPart) for finer citation? | TBD | TBD |

### Future extensions
- Extension point A: Chapter-level metadata extraction (titles, keywords) into structured JSON.
- Extension point B: Link this source to internal KFM design docs (e.g., hardware/throughput scaling notes) with explicit provenance.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A["Source PDF (external)"] --> B["ETL: extract metadata + text (optional)"]
  B --> C["STAC item (asset) + DCAT dataset view (bibliographic)"]
  B --> D["PROV activity bundle (extraction run)"]
  C --> E["Graph: Document node (+ optional chapter nodes)"]
  E --> F["APIs: evidence/reference endpoints"]
  F --> G["UI: reference panels / citations"]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Request reference(source_id)
  API->>Graph: Fetch Document + provenance refs
  Graph-->>API: Metadata + linked identifiers
  API-->>UI: Contracted payload + citations
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Book PDF | PDF | DOI: `10.1007/978-3-031-74097-8` | checksum + license statement presence |
| Bibliographic identifiers | text | front-matter pages | DOI/ISBN formatting checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Source summary (this doc) | Markdown | `docs/research/source_summaries/...` | KFM-MDP governed doc |
| (Optional) STAC Item | JSON | `data/stac/items/...` | STAC 1.0 + KFM-STAC profile |
| (Optional) DCAT dataset record | JSON-LD | `data/catalog/dcat/...` | DCAT 3 + KFM-DCAT profile |
| (Optional) PROV bundle | JSON-LD | `data/prov/...` | PROV-O + KFM-PROV profile |

### Sensitivity & redaction
- None expected (public/open). If the source is redistributed, preserve attribution and license notice.

### Quality signals
- DOI and ISBNs captured exactly as stated.
- License captured and mapped to DCAT license fields.
- If full-text extraction occurs: verify completeness (page count) and store extraction warnings in run logs.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `TBD` (candidate: `data/stac/collections/reference-library.json`)
- Items involved: `TBD` (candidate: `.../scalable-data-management-for-future-hardware.json`)
- Extension(s): `TBD` (only if repo defines a reference-document extension)

### DCAT
- Dataset identifiers: `TBD` (candidate: `dcat:dataset:reference:scalable-data-management-for-future-hardware`)
- License mapping: CC-BY 4.0 (as stated in the source)
- Contact / publisher mapping: publisher statement present in the source; map to DCAT publisher fields if adopted

### PROV-O
- `prov:wasDerivedFrom`: DOI + local source asset hash
- `prov:wasGeneratedBy`: `TBD` pipeline activity/run ID (must be recorded if ingestion occurs)
- Activity / Agent identities: `TBD` (use repo’s standard agent naming)

### Versioning
- If ingested as a STAC Item: use predecessor/successor links when updated (e.g., re-extracted text or updated metadata).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Docs | Governed reference summary | Markdown protocol |
| (Optional) ETL | Extract metadata/text | Config + run logs |
| (Optional) Catalogs | STAC/DCAT/PROV records | JSON + validation |
| (Optional) Graph | Document node linkage | API-mediated access only |
| (Optional) APIs | Serve reference contracts | REST/GraphQL (contracted) |
| (Optional) UI | Render reference panels | API calls |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Reference source schema | `schemas/` | Semver + changelog (if introduced) |
| API contract for references | `docs/` + `src/server/` | Backward compat or version bump |
| Citation rendering rules | `web/` + `docs/design/` | UI contract tests (if applicable) |

### Extension points checklist (for future work)
- [ ] Data: add to `data/sources/` under a documented convention
- [ ] STAC: add collection + item with schema validation
- [ ] PROV: record extraction activity + agent
- [ ] Graph: add Document node and link to relevant internal docs
- [ ] APIs: add contracted endpoint(s) if needed
- [ ] UI: render as “Reference / Evidence” panel (optional)
- [ ] Focus Mode: only if this source becomes evidence for a narrative claim
- [ ] Telemetry: record ingestion/extraction metrics (optional)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- This source should only appear as **supporting evidence** for technical design claims (e.g., “hardware acceleration trends”) and must be attached via explicit provenance links.

### Provenance-linked narrative rule
- Every claim referencing this source must cite: DOI + (optional) chapter/section locator or extracted artifact ID.

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
- [ ] Ensure identifiers are correct (DOI/ISBN)
- [ ] If cataloged: STAC/DCAT/PROV schema validation
- [ ] If graphed: graph integrity checks (labels/edges)
- [ ] If served: API contract tests
- [ ] Security and sovereignty checks (not expected to trigger for this public source)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate markdown
# 2) validate catalogs (if created)
# 3) run graph integrity tests (if linked)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Ingestion/extraction run id | ETL | `mcp/runs/` + telemetry schema (if adopted) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Historian/editor review: recommended (doc correctness)
- Security council review: not expected
- FAIR+CARE council review: not expected (public technical literature)

### CARE / sovereignty considerations
- None expected for this source.

### AI usage constraints
- Allowed: summarize, structure extraction.
- Prohibited: generating policy, inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-20 | Initial governed source summary + proposed KFM alignment | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
