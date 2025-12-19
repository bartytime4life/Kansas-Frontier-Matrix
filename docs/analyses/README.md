---
title: "Analyses — README"
path: "docs/analyses/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:analyses:readme:v1.0.0"
semantic_document_id: "kfm-analyses-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:analyses:readme:v1.0.0"
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

# Analyses — README

## 📘 Overview

### Purpose
This directory holds **governed analysis documentation**: reproducible, provenance-linked write-ups that
justify or explain analytical methods and results used elsewhere in KFM (catalogs, graph, APIs, UI, Story
Nodes, Focus Mode).

Analyses are **documentation artifacts**. If an analysis produces a **derived dataset** or a **new evidence
artifact**, those outputs belong in the appropriate pipeline locations (e.g., `data/processed/`, `data/stac/`,
`data/prov/`), and the analysis doc should link to them.

### Scope

| In Scope | Out of Scope |
|---|---|
| Method descriptions, assumptions, limitations, and results summaries | Raw datasets (store under `data/`) |
| Links to STAC item IDs, DCAT dataset IDs, PROV activity/run IDs | API contract changes (use API Contract Extension template) |
| “Evidence product” documentation that can be referenced by Story Nodes / Focus Mode | Story Nodes themselves (use Story Node template) |
| Validation steps and reproducibility notes | Sensitive location inference or ungrounded narrative |

### Audience
- Primary: Analysts (GIS / data / ML), pipeline maintainers, reviewers
- Secondary: Historians/editors, educators, UI/UX implementers consuming evidence

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (non-exhaustive):
  - **Analysis product**: a documented analytical result intended to support downstream evidence, narrative,
    or decisions.
  - **Evidence artifact**: a derived output (table, geometry, raster, model output) that must be cataloged
    and provenance-traceable.
  - **Provenance**: recorded lineage via STAC/DCAT identifiers and PROV activities/runs.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Analyses README (this) | `docs/analyses/README.md` | Docs/Analyses maintainers | Governs layout + rules |
| Analysis write-up | `docs/analyses/<analysis_slug>/ANALYSIS.md` | Analysis author | Uses governed template headers + provenance refs |
| Figures (optional) | `docs/analyses/<analysis_slug>/assets/` | Analysis author | Keep small + cite sources |
| Derived dataset (if any) | `data/processed/...` | Data domain owner | Must be reproducible + referenced |
| STAC catalog entries (if any) | `data/stac/...` | Catalog owner | Items/Collections for spatial/temporal assets |
| PROV lineage (if any) | `data/prov/...` | Pipeline owner | Activity + agents + derivations |

### Definition of done (for an analysis doc in this directory)
- [ ] Front-matter complete + valid
- [ ] Every quantitative/geospatial claim links to dataset IDs / record IDs / STAC item IDs (or is explicitly labeled as a hypothesis)
- [ ] PROV run/activity identifier recorded (when outputs are derived)
- [ ] Validation steps are listed and repeatable
- [ ] Sensitivity + sovereignty considerations stated (even if “none known”)
- [ ] No prohibited AI actions implied (e.g., no “infer sensitive locations”)

## 🗂️ Directory Layout

### This document
- `path`: `docs/analyses/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs per domain |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
This is a **target layout** for organizing analysis write-ups (create folders as needed).

~~~text
📁 docs/
└── 📁 analyses/
    ├── 📄 README.md
    ├── 📁 <analysis_slug>/
    │   ├── 📄 ANALYSIS.md
    │   └── 📁 assets/
    │       └── 📄 <figure_or_table>.<ext>
    └── 📁 _archive/
        └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM’s architecture treats provenance and reproducibility as first-class constraints. Analyses exist to make
the “why” behind derived evidence explicit and reviewable.

### Assumptions
- The canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI consumes data through the API layer (no direct graph access).
- Derived outputs should be deterministically reproducible from declared inputs/configuration.

### Constraints / invariants
- Frontend consumes contracts via APIs (no direct graph dependency).
- No unsourced narrative: analysis results must be traceable to identifiers or clearly labeled as inference/hypothesis.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we want a top-level index of analysis slugs with tags (domain, method, time range)? | TBD | TBD |
| Where should larger figures live (docs vs data assets)? | TBD | TBD |

### Future extensions
- Auto-generated index page for `docs/analyses/` (linted and CI-checked).
- Optional schema for analysis metadata (inputs/outputs/run_id) if this directory becomes machine-ingestible.

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

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source datasets | varies | `data/raw/` or external refs | domain checks + hashes |
| STAC items/collections | JSON | `data/stac/` | STAC schema validation |
| DCAT records | JSON-LD/Turtle | `data/catalog/dcat/` | DCAT profile validation |
| PROV lineage | JSON-LD/RDF/etc | `data/prov/` | PROV profile validation |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Analysis write-up | Markdown | `docs/analyses/<analysis_slug>/ANALYSIS.md` | Markdown protocol + doc lint |
| Figures (optional) | png/svg/pdf | `docs/analyses/<analysis_slug>/assets/` | link checks |
| Derived dataset (optional) | csv/parquet/geojson/etc | `data/processed/...` | domain schema + QC |
| Catalog entries (optional) | JSON/JSON-LD | `data/stac/...`, `data/catalog/dcat/...`, `data/prov/...` | schema validation |

### Sensitivity & redaction
- Analyses must not publish restricted locations or culturally sensitive details without following
  `docs/governance/SOVEREIGNTY.md` and `docs/governance/ETHICS.md`.
- If an analysis requires restricted inputs, document redaction/generalization rules and access boundaries.

### Quality signals
- Completeness (missing values, missing geometries)
- Valid ranges and units
- Geometry validity + CRS consistency (if spatial)
- Reproducibility (pinned inputs/configs; deterministic runs)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If an analysis generates/uses spatiotemporal assets, reference:
  - STAC Collection ID(s)
  - STAC Item ID(s)
  - Asset keys (e.g., `visual`, `data`, `thumbnail`) as applicable

### DCAT
- If an analysis depends on a named dataset product, reference its DCAT identifier and license metadata.

### PROV-O
- If an analysis produces a derived artifact:
  - `prov:wasDerivedFrom`: list source IDs (STAC/DCAT/document IDs)
  - `prov:wasGeneratedBy`: pipeline activity/run ID
  - `prov:wasAssociatedWith`: agent(s) (person/tool) if modeled

### Versioning
- Use semver for analysis doc versions when changes affect interpretation.
- When results change, document *why* (new inputs, bug fix, method change) and link predecessor/successor if applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON/JSON-LD + validators |
| Graph | Neo4j | Cypher behind API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Provenance-linked docs |
| Focus Mode | Context synthesis | Provenance-linked bundles |

### Interfaces / contracts
- If an analysis output becomes a **served evidence product**, define the contract at the **API layer**
  (not directly from the graph).
- Any new schema must live under `schemas/` with validation and versioning.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Analyses can be referenced by:
  - Story Nodes as supporting evidence (link to analysis slug + cited dataset IDs)
  - Audit panels as “method / limitations” documentation for derived layers (if implemented)

### Provenance-linked narrative rule
- Every claim in downstream narratives must trace to a dataset / record / asset ID.
- Analyses should make that trace easy by listing:
  - inputs
  - transformations
  - outputs
  - run IDs
  - known limitations

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Internal link checks (paths, anchors)
- [ ] Schema validation for any referenced STAC/DCAT/PROV artifacts
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Placeholder examples — replace with repo-specific commands.
# 1) validate catalogs (STAC/DCAT/PROV)
# 2) run pipeline steps needed to reproduce outputs
# 3) run doc lint / link checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Analysis run identifier(s) | pipeline runner | `data/prov/` + telemetry (if configured) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Historian/editor review: recommended when analyses influence Story Nodes
- Security council review: required if restricted sources or sensitive layers are involved
- FAIR+CARE council review: required if sovereignty-sensitive content is touched

### CARE / sovereignty considerations
- Identify impacted communities and protection rules if the analysis touches Indigenous or culturally sensitive locations.

### AI usage constraints
- Analyses may use allowed AI transforms (summarize/structure_extract/translate/keyword_index) but must not:
  - generate policy
  - infer sensitive locations
  - introduce uncited factual claims

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `docs/analyses/` README scaffold | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`