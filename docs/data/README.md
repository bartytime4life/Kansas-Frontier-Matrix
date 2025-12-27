---
title: "docs/data — Data Documentation & Catalog Mapping Index"
path: "docs/data/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:docs:data:readme:v1.0.0"
semantic_document_id: "kfm-docs-data-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:docs:data:readme:v1.0.0"
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

# docs/data — Data Documentation & Catalog Mapping Index

## 📘 Overview

### Purpose

- Provide the **canonical entry point** for governed documentation that explains how KFM data domains connect to **STAC/DCAT/PROV catalogs**, the **Graph**, the **API layer**, and downstream **UI/Story Nodes/Focus Mode**.
- Define **what belongs** in `docs/data/` vs what must live in `data/`, `src/`, `schemas/`, etc.
- Act as a **navigation hub** to domain modules (e.g., *Land Treaties*) and domain governance packs (e.g., *Air Quality*).

> **Non-negotiable pipeline ordering (reference):** ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode.

### Scope

| In Scope | Out of Scope |
|---|---|
| Domain documentation and “rules of the road” for data packs | Implementing ETL jobs or API endpoints (belongs in `src/`) |
| Catalog mapping documentation (STAC/DCAT/PROV crosswalks, conventions) | Authoritative STAC/DCAT/PROV JSON outputs (belongs in `data/`) |
| Provenance and governance expectations for data domains | Replacing global governance policy (belongs in `docs/governance/`) |
| Linking narrative requirements to dataset identifiers | Writing Story Nodes themselves (belongs in `docs/reports/story_nodes/`) |

### Audience

- **Primary:** Data contributors, catalog maintainers, governance reviewers
- **Secondary:** Graph/API/UI contributors who need stable identifiers + provenance guarantees
- **Tertiary:** Story Node authors and Focus Mode curators who need resolvable citations

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc (non-exhaustive):
  - **Domain pack:** A dataset’s lifecycle footprint under `data/<domain>/**` (raw/work/processed) plus its catalog/provenance presence.
  - **Domain documentation:** Governed narrative + mapping docs under `docs/data/<domain>/**` (or a single canonical location chosen per domain).
  - **Catalog outputs:** STAC/DCAT/PROV machine-readable artifacts (authoritative outputs belong under `data/`).
  - **Mapping spec / crosswalk:** A doc that maps domain fields and assets to STAC/DCAT/PROV requirements.
  - **Provenance bundle:** PROV records for lineage across raw → work → processed (and any redaction/generalization).

### Quick navigation (common entry points)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal governed doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Data lifecycle index: `data/README.md`
- Catalog outputs:
  - STAC: `data/stac/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical system overview |
| Universal governed doc structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | This README follows this template |
| v13 blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | Target repo layout + invariants |
| Data lifecycle staging | `data/README.md` | Data Eng | Raw/work/processed + publication rules |
| STAC/DCAT/PROV outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Data/Platform | Authoritative catalogs + lineage |
| Example domain module (historical) | `docs/data/historical/land-treaties/README.md` | Domain team | Example “vertical slice” module |
| Example domain governance pack | `data/air-quality/governance/README.md` | Domain team | Domain-local review gates, classification notes |
| API contracts | `src/server/contracts/**` | API Eng | Contract-first boundary (no UI→Neo4j direct reads) |
| Story Nodes | `docs/reports/story_nodes/**` | Narrative | Evidence-linked narrative content |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Clearly distinguishes **docs** vs **data outputs** vs **code**
- [ ] Includes at least one **real domain example** link (e.g., Land Treaties) and one governance example (e.g., Air Quality)
- [ ] Validation steps listed and repeatable (or marked “not confirmed in repo”)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Footer refs present (do not remove)

---

## 🗂️ Directory Layout

### This document

- `path` (must match front-matter): `docs/data/README.md`

### What belongs in `docs/data/`

- Domain documentation that explains *what a dataset is*, *how it is governed*, and *how it maps* into STAC/DCAT/PROV and downstream systems.
- Cross-domain conventions for catalog mappings and provenance expectations.
- “How to contribute” guidance for new domains, including what to link to and what not to duplicate.

### What must **not** be stored in `docs/data/`

- Raw inputs, intermediate files, processed outputs (these belong under `data/`).
- Authoritative STAC/DCAT/PROV JSON outputs (these belong under `data/stac/`, `data/catalog/dcat/`, `data/prov/`).
- Executable pipeline code (belongs under `src/pipelines/` or other repo-defined code roots).
- Secrets, credentials, access tokens, or PII.

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed datasets + domain READMEs |
| Catalog outputs | `data/stac/` | STAC collections + items (authoritative) |
| Catalog outputs | `data/catalog/dcat/` | DCAT outputs (JSON-LD) |
| Provenance bundles | `data/prov/` | PROV records (per run / per dataset) |
| Graph import fixtures | `data/graph/` | CSV + Cypher for Neo4j ingest |
| Pipeline code | `src/pipelines/` | ETL + catalog builders (idempotent/deterministic) |
| Pipeline docs | `docs/pipelines/` | Runbooks / process docs (if present) |
| Graph build + ontology bindings | `src/graph/` | Ontology + ingest logic |
| API layer + contracts | `src/server/` + `src/server/contracts/` | Contract-first access boundary |
| UI layer | `web/` | React/MapLibre UI; consumes APIs only |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative modules |
| MCP runs / experiments | `mcp/runs/` | Run logs + pointers to PROV (no duplicate payloads) |
| Standards | `docs/standards/` | Repo rules, profiles, protocols |
| Templates | `docs/templates/` | Governed doc templates |

### Expected directory tree (pattern)

> This tree is a **pattern**: actual domains may vary. Keep **one canonical location** for mapping docs, and link to it rather than duplicating content.

~~~text
📁 docs/
├── 📁 data/
│   ├── 📄 README.md
│   ├── 📁 historical/
│   │   └── 📁 land-treaties/
│   │       └── 📄 README.md
│   └── 📁 <domain>/
│       ├── 📄 README.md
│       ├── 📁 mappings/
│       │   ├── 📄 stac-crosswalk.md
│       │   ├── 📄 dcat-crosswalk.md
│       │   └── 📄 prov-notes.md
│       └── 📁 governance/
│           └── 📄 decisions.md
~~~

---

## 🧭 Context

### Why `docs/data/` exists

KFM treats “data documentation” as a **governed contract surface**: it explains how a domain pack is expected to behave across the full system, including catalogs, provenance, graph references, and narrative usage.

### Architecture invariants this directory must respect

- **Canonical pipeline ordering** is preserved (ETL → STAC/DCAT/PROV → Graph → API → UI → Story → Focus Mode).
- **UI never reads Neo4j directly** — all access is mediated by contracted APIs.
- **Authoritative catalogs and provenance live under `data/`**; `docs/data/` documents *how they are produced and used*.
- **Graph nodes store references** (IDs/links) back to STAC/DCAT/PROV wherever applicable, rather than duplicating large payloads.

### Notes on “mappings” placement (docs vs data)

- Some designs place domain mapping docs under `data/<domain>/mappings/` (co-located with data packs).
- The Master Guide also references `docs/data/` for “catalog generation + mappings.”
- **Rule for contributors:** choose **one canonical location per domain** for mapping documentation, and ensure this `docs/data/` index links to it.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  S[Upstream Sources] --> E[src/pipelines/**\nETL & normalization]
  E --> W[data/<domain>/work/**]
  W --> P[data/<domain>/processed/**]

  P --> STAC[data/stac/**]
  P --> DCAT[data/catalog/dcat/**]
  E --> PROV[data/prov/**]

  DOCS[docs/data/**\nDomain docs + mapping specs] -.documents.-> STAC
  DOCS -.documents.-> DCAT
  DOCS -.documents.-> PROV

  STAC --> G[src/graph/** + data/graph/**\nGraph ingest fixtures]
  PROV --> G
  G --> API[src/server/**\nContract-first APIs]
  API --> UI[web/**\nReact/MapLibre UI]
  UI --> SN[docs/reports/story_nodes/**\nStory Nodes]
  SN --> FM[Focus Mode\n(provenance-linked context)]
~~~

---

## 📦 Data & Metadata

### What `docs/data/` should document for each domain

Minimum recommended sections for each domain README (domain-level):

- **Source inventory + licenses** (or links to `data/<domain>/governance/SOURCES_AND_LICENSES.md`)
- **Schema expectations** (what must be present, and where schemas live under `schemas/`)
- **Catalog mapping** (how processed artifacts become STAC/DCAT, and where to find them)
- **Provenance expectations** (what PROV must capture; which steps are redactions/generalizations)
- **Stable identifiers** (dataset IDs, STAC collection IDs, STAC item IDs, graph node reference fields)
- **Downstream usage** (how API/UI/Story Nodes should cite the domain)

### Placement rules (canonical locations)

| Artifact type | Canonical location | docs/data should do |
|---|---|---|
| Raw inputs | `data/<domain>/raw/**` | Link; describe provenance + license |
| Intermediate transforms | `data/<domain>/work/**` | Document why it exists; don’t publish |
| Processed outputs | `data/<domain>/processed/**` | Link; describe intended public/private products |
| STAC collections/items | `data/stac/**` | Link to collection/item IDs; document mapping |
| DCAT outputs | `data/catalog/dcat/**` | Link to dataset IDs; document access rights logic |
| PROV bundles | `data/prov/**` | Link to run IDs / bundles; document lineage |
| Schemas | `schemas/**` | Link; document which schema applies to which artifact |
| Graph fixtures | `data/graph/**` | Link; document reference strategy back to catalogs |
| API contracts | `src/server/contracts/**` | Link; document query patterns needed by UI |
| UI layers | `web/**` | Link; document layer registration conventions |

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (discovery + asset inventory)

- Domain docs should state:
  - What constitutes a **Collection** vs an **Item** for the domain.
  - How assets link back to `data/<domain>/processed/**`.
  - How governance labels (sensitivity/classification) are carried into metadata.

### DCAT (dataset discovery + distribution semantics)

- Domain docs should state:
  - How the domain’s datasets are represented in DCAT outputs.
  - What “public vs restricted” publication means for DCAT presence (metadata-only vs omitted, as governed).
  - How DCAT records reference STAC collections or other distributions.

### PROV (lineage + reproducibility)

- Domain docs should state:
  - Which transformations are recorded as PROV Activities.
  - Where redaction/generalization is captured.
  - The rule that outputs must not be “less restricted” than any sensitive/restricted input in their lineage (as governed).

---

## 🧱 Architecture

### How docs/data relates to the runtime system

| Stage | Runtime location | docs/data responsibility |
|---|---|---|
| ETL | `src/pipelines/**` + `data/<domain>/**` | Document inputs/outputs and determinism expectations |
| Catalogs | `data/stac/**` + `data/catalog/dcat/**` + `data/prov/**` | Document mapping rules, versioning, and link strategy |
| Graph | `src/graph/**` + `data/graph/**` | Document how graph nodes reference catalog IDs |
| API | `src/server/**` | Document required queries/endpoints and contract expectations |
| UI | `web/**` | Document what metadata must exist for layers and narratives |
| Story | `docs/reports/story_nodes/**` | Ensure citations resolve to STAC items/doc IDs |

---

## 🧠 Story Node & Focus Mode Integration

- Domain docs should explicitly state what is **citeable**:
  - STAC item IDs, dataset IDs, document IDs, and any stable resolvers.
- Story Nodes must remain evidence-focused:
  - Every factual claim should be traceable to a dataset/document identifier (ideally corresponding to STAC or a graph entity reference).
- Focus Mode should operate on provenance-linked context:
  - Domain docs should call out any required redaction/generalization constraints that must carry through to UI presentations.

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (avoid orphan pointers)
- Secret scanning (no tokens/keys)
- If mapping docs change:
  - ensure schemas are updated (if needed) under `schemas/**`
  - ensure STAC/DCAT/PROV outputs validate in their canonical locations (if applicable)

> Commands/tooling are **not confirmed in repo** — use the repo’s CI workflow and validation tooling as defined under `.github/workflows/` and `tools/` (if present).

---

## ⚖ FAIR+CARE & Governance

### Review gates (examples)

Governance review is typically required when:

- introducing a new dataset source for a domain,
- changing an artifact’s classification/sensitivity,
- publishing any dataset derived from sensitive/restricted inputs,
- adding a new UI layer that could reveal sensitive locations by interaction/zoom.

### CARE / sovereignty considerations

- If a domain intersects with sovereignty-controlled knowledge or sensitive geographies:
  - prefer aggregation/generalization for public outputs,
  - document stewardship decisions in governance notes,
  - follow `docs/governance/SOVEREIGNTY.md`.

### AI usage constraints

- Allowed:
  - summarization, structure extraction, translation, keyword indexing.
- Prohibited:
  - generating new policy,
  - inferring sensitive locations (directly or indirectly).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-27 | Initial `docs/data/` README establishing purpose, placement rules, and mapping responsibilities | (you) |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---
