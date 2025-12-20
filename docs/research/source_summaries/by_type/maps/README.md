---
title: "Source Summaries — Maps (README)"
path: "docs/research/source_summaries/by_type/maps/README.md"
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

doc_uuid: "urn:kfm:doc:research:source-summaries:by-type:maps:readme:v1.0.0"
semantic_document_id: "kfm-research-source-summaries-by-type-maps-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:source-summaries:by-type:maps:readme:v1.0.0"
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

# Source Summaries — Maps

## 📘 Overview

### Purpose
This README defines how to write and maintain **source summaries for map/cartographic sources** used by Kansas Frontier Matrix (KFM). Map summaries are the “intake lens” that turns a map into a governed, provenance-linked candidate for later **cataloging (STAC/DCAT/PROV), graph linkage, and UI presentation**.

### Scope
| In Scope | Out of Scope |
|---|---|
| Historic maps (scanned sheets, atlas plates, plats), map PDFs, georeferenced rasters (e.g., GeoTIFF), vector map products (e.g., GeoPackage) **when the primary artifact is a map** | Narrative books/papers that merely *contain* maps (put those in `books/` and reference maps as assets), general websites (use `web/`), non-cartographic images without map intent |

### Audience
- Primary: KFM researchers and curators authoring map source summaries.
- Secondary: Pipeline/graph/API/UI contributors needing clear provenance, licensing, and geospatial intent.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: map sheet, atlas plate, georeferencing, CRS, scale, bounding box, provenance.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Parent guidance | `docs/research/source_summaries/by_type/README.md` | Research | Cross-type conventions |
| Maps summaries folder | `docs/research/source_summaries/by_type/maps/` | Research | One source summary per map source |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | DataOps | Created later by pipelines |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Scope clearly distinguishes maps vs books/web
- [ ] Diagram renders (no HTML in Mermaid labels)
- [ ] Checklist enables repeatable map summary creation
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/source_summaries/by_type/maps/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Source summaries | `docs/research/source_summaries/by_type/` | Type-indexed external source summaries |
| Data lifecycle | `data/raw/` → `data/work/` → `data/processed/` | Assets and derived data products (where applicable) |
| STAC | `data/stac/` | Collections + items for spatial/temporal assets |
| DCAT | `data/catalog/dcat/` | Dataset-level catalog entries |
| PROV | `data/prov/` | Lineage bundles and activity/agent traces |
| Pipelines | `src/pipelines/` | ETL + catalog + graph build |
| Graph | `src/graph/` | Ontology bindings + graph build tooling |
| APIs | `src/server/` + `docs/` | Contracted access layer and docs |
| UI | `web/` | React/Map client |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    └── 📁 source_summaries/
        └── 📁 by_type/
            ├── 📄 README.md
            ├── 📁 books/
            │   └── 📄 README.md
            ├── 📁 web/
            │   └── 📄 README.md
            ├── 📁 maps/
            │   ├── 📄 README.md
            │   ├── 📄 <source_slug>.md
            │   └── 📄 <source_slug>__supplemental_notes.md
            └── 📁 datasets/
                └── 📄 README.md
~~~

## 🧭 Context

### Background
Maps are unusually “dual-natured” sources:
- they carry **historical narrative intent** (who made it, why, what it claims),
- and they are **geospatial evidence** (extent, scale, projection, positional accuracy).

A map source summary must capture both aspects so the downstream pipeline can:
- catalog it as an asset (STAC/DCAT),
- record lineage (PROV),
- link entities (graph),
- and present it responsibly (UI overlays + citations + sensitivity rules).

### How map source summaries relate to the KFM pipeline
KFM’s canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

Map source summaries fit as *research intake artifacts* that shape downstream work:
- they clarify what the map is and why it matters,
- they pre-identify licensing, sensitivity, and geospatial specifics,
- they provide stable identifiers and citations for later catalogs and graph nodes.

~~~mermaid
flowchart LR
  A["External map source"] --> B["Map source summary (this folder)"]
  B --> C["ETL + normalization"]
  C --> D["STAC/DCAT/PROV catalogs"]
  D --> E["Neo4j graph"]
  E --> F["API layer"]
  F --> G["React/Map UI"]
  G --> H["Story Nodes"]
  H --> I["Focus Mode"]
~~~

### Assumptions
- Some map metadata may be incomplete (unknown projection, unclear date, partial sheet coverage).
- Publication date may differ from “depicted time” (e.g., a 1900 atlas plate depicting 1870 boundaries).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Do not infer sensitive locations; if the map contains sensitive sites, apply generalization/redaction expectations.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where do we persist georeferencing QA signals (e.g., RMS error) in a governed schema? | TBD | TBD |
| Do we treat atlas plates as one STAC Collection with multiple STAC Items (one per plate)? | TBD | TBD |
| What is the repo-standard naming convention for `<source_slug>`? | TBD | TBD |

### Future extensions
- Map-specific source summary template file (if needed) under `docs/templates/` (**requires human review**).
- A “georeferencing report” artifact type with schema + validation (ties into PROV + telemetry).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  subgraph Intake["Research intake (docs)"]
    SS["Source summary: maps"] --> G0["Governance notes (license + sensitivity)"]
  end

  SS --> ETL["ETL"]
  ETL --> CAT["STAC/DCAT/PROV"]
  CAT --> GR["Neo4j Graph"]
  GR --> API["APIs"]
  API --> UI["React/Map UI"]
  UI --> SN["Story Nodes"]
  SN --> FM["Focus Mode"]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Curator
  participant Repo as Repo Docs
  participant ETL as ETL/Catalog Pipeline
  participant API
  participant UI
  Curator->>Repo: Add map source summary (docs)
  ETL->>Repo: Generate STAC/DCAT/PROV (later)
  API->>Repo: Serve contracted map metadata
  UI->>API: Request map overlay + provenance
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Map artifact | PDF/TIFF/JPEG/GeoTIFF/etc. | Archive/library/agency/publisher | License + citation present; file integrity (hash) |
| Map metadata | Citation text / catalog record | Archive record / bibliographic entry | Title/author/date fields captured (or “unknown”) |
| Geospatial hints | CRS/scale/extent notes | Map marginalia, legends, catalog record | Mark uncertainty explicitly if unknown |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Map source summary | Markdown | `docs/research/source_summaries/by_type/maps/<source_slug>.md` | Markdown protocol (KFM-MDP) |
| (Optional) Extraction notes | Markdown | `.../<source_slug>__supplemental_notes.md` | Same |

### Minimum capture checklist (map-specific)
- [ ] Full citation (creator, title, publisher, year, edition/plate/sheet number if any)
- [ ] Acquisition/provenance: where obtained (archive/repository), accession ID if known
- [ ] License/rights status and usage constraints
- [ ] Map type: atlas plate / plat / survey map / thematic map / topographic map / etc.
- [ ] Date fields: publication date; survey/creation date; depicted time range (if different)
- [ ] Spatial coverage (described in words; bounding box if known)
- [ ] Scale (as printed) and units
- [ ] CRS/projection/datum (if printed or known); otherwise explicitly “unknown”
- [ ] Known distortions/limitations (e.g., schematic, not to scale)
- [ ] Sensitivity flags (restricted sites, culturally sensitive locations) and redaction expectations
- [ ] Candidate KFM entities (Place/Event/Organization/Document) this map could support

### Sensitivity & redaction
- Identify any restricted or culturally sensitive locations, and document the expected generalization/redaction behavior for public outputs.
- Never infer or reconstruct sensitive locations from ambiguous map markings.

### Quality signals
- Scan quality: resolution, legibility, missing margins.
- Georeferencing quality (if performed later): control point count, RMS error, residual distribution.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Maps that become spatial overlays typically become STAC items (raster or vector assets).
- If a source is an atlas: treat as a candidate for a STAC Collection with one or more items (plate/sheet-level).

### DCAT
- Map sets (atlases, map series) often map cleanly to DCAT dataset-level records (publisher, coverage, license).

### PROV-O
- The source summary should preserve enough stable identifiers (catalog IDs, archive links, edition/plate IDs) to support:
  - `prov:wasDerivedFrom` (original source / archive record)
  - `prov:wasGeneratedBy` (future pipeline activity/run ID)

### Versioning
- If map artifacts are updated (better scan, improved georeference), record successor relationships in catalogs and maintain stable IDs where possible.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Research intake | Curate map source summary | Markdown docs |
| ETL | Ingest map files + extract metadata | Config + run logs |
| Catalogs | Produce STAC/DCAT/PROV | JSON/JSON-LD + validators |
| Graph | Link map artifacts to entities | API layer (no UI direct graph reads) |
| APIs | Serve map assets + provenance | REST/GraphQL |
| UI | Render overlays + citations | API calls |
| Story Nodes | Curated narratives referencing map evidence | Docs + graph linkage |
| Focus Mode | Provenance-linked synthesis | Context bundle with citations |

### Interfaces / contracts
- This README does not define or change API contracts; it only shapes intake documentation quality.

### Extension points checklist (for future work)
- [ ] Map-specific STAC extension usage documented (if adopted)
- [ ] Georeferencing QA schema defined (if adopted)
- [ ] UI layer registry entry patterns documented (if needed)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Maps typically surface as:
- a map overlay layer (if georeferenced),
- an evidence asset cited in narratives,
- a provenance “card” (license + repository + transformation chain).

### Provenance-linked narrative rule
Every claim derived from a map must trace back to:
- a map asset ID (catalog) and/or
- a cited map source record.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter keys present, no broken internal links)
- [ ] License present and unambiguous (or explicitly “unknown / needs review”)
- [ ] Sensitivity notes present where applicable (no sensitive inference)
- [ ] If spatial extent is stated: ensure it is plausible and flagged if uncertain

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) markdown lint / protocol checks
# 2) link check (internal docs)
# 3) (optional) catalog validators for related assets
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Map scan quality notes | Curator | `docs/research/source_summaries/...` |
| Georeferencing QA | Pipeline run | `docs/telemetry/` + `schemas/telemetry/` (if adopted) |

## ⚖ FAIR+CARE & Governance

### Review gates
- New sensitive layers: **requires human review**
- New external map sources with unclear licensing: **requires human review**
- Any AI-assisted extraction that could reveal sensitive sites: **prohibited**

### CARE / sovereignty considerations
- Identify communities impacted and protection rules where maps depict culturally sensitive resources.

### AI usage constraints
- Allowed: summarization and structure extraction.
- Prohibited: inferring sensitive locations or fabricating missing geospatial metadata.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial maps source summaries README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

