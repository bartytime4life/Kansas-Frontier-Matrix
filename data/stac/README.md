---
title: "KFM STAC Catalog Outputs — data/stac README"
path: "data/stac/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:data:stac:readme:v1.0.1"
semantic_document_id: "kfm-data-stac-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:data:stac:readme:v1.0.1"
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

# KFM STAC Catalog Outputs

## 📘 Overview

### Purpose
- This README defines **what lives in `data/stac/`**, why it exists, and how downstream stages should interpret it.
- `data/stac/` is the canonical home for **STAC Collections and STAC Items** emitted by the KFM **Catalog** stage.
- These artifacts are treated as **evidence metadata** consumed downstream via the canonical pipeline ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

> Parent context: `data/README.md`

### Scope

| In Scope | Out of Scope |
|---|---|
| Directory layout contract for STAC outputs under `data/stac/` | Full STAC field-by-field specification |
| Collection vs Item expectations (foldering + minimal invariants) | Domain-specific mapping rules for each dataset |
| File naming and ID alignment expectations (stable IDs, predictable filenames) | Implementing ETL / catalog build code (belongs under `src/pipelines/`) |
| Validation expectations and governance notes | UI design details (belongs under `web/`) |
| How STAC outputs connect to DCAT + PROV + Graph + API (at a contract level) | “Business logic” narratives (belongs in Story Nodes and governed story workflows) |

### Audience
- Primary: Catalog maintainers, data engineers producing STAC outputs.
- Secondary: Graph/ontology builders, API developers, Story Node authors, governance reviewers.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (non-exhaustive): STAC, Collection, Item, Asset, extent, geometry generalization, DCAT, PROV, evidence artifact, provenance, redaction.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/stac/README.md` | Catalog maintainers | Documents the STAC output area |
| Parent data README | `data/README.md` | Data maintainers | Canonical data staging + catalog roots |
| STAC Collections | `data/stac/collections/` | Catalog stage | One JSON file per Collection |
| STAC Items | `data/stac/items/` | Catalog stage | One JSON file per Item (often grouped by Collection) |
| DCAT outputs | `data/catalog/dcat/` | Catalog stage | Dataset discovery records |
| PROV bundles | `data/prov/` | Catalog + ETL | Lineage bundles per run / dataset |
| STAC schemas | `schemas/stac/` | Schemas/CI | JSON Schema validation targets *(may be missing until v13 roots are created)* |
| STAC profile | `docs/standards/KFM_STAC_PROFILE.md` | Standards owners | KFM constraints/extension conventions *(may be missing until v13 standards are created)* |
| Master pipeline invariant | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Pipeline ordering + non-negotiables |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Canonical roots + contract-first readiness targets |

### Definition of done (for this document)
- [ ] Front-matter complete and `path` matches `data/stac/README.md`.
- [ ] Scope clearly distinguishes “layout/contract guidance” vs implementation details.
- [ ] File tree reflects the intended `data/stac/` organization and is visually aligned.
- [ ] Mermaid diagrams render (no parse errors).
- [ ] Validation expectations are clear and repeatable (even if exact commands live elsewhere).
- [ ] Governance + CARE/sovereignty considerations explicitly stated (even if “not applicable” for a specific dataset).
- [ ] Downstream linkage expectations are documented (Graph/API/Story Nodes).

---

## 🗂️ Directory Layout

### This document
- `path`: `data/stac/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| **Data staging** | `data/<domain>/{raw,work,processed}/` | Domain staging: raw → work → processed |
| **Catalog outputs (STAC)** | `data/stac/` | STAC Collections + Items (this folder) |
| **Catalog outputs (DCAT)** | `data/catalog/dcat/` | DCAT outputs (JSON-LD / TTL as adopted) |
| **Provenance (PROV)** | `data/prov/` | PROV bundles (per run / per dataset) |
| **Graph** | `src/graph/` | Graph build + ontology bindings |
| **Pipelines** | `src/pipelines/` | ETL + catalog build + transforms |
| **Schemas** | `schemas/` | JSON schemas for STAC/DCAT/PROV + telemetry |
| **Frontend** | `web/` | React + map clients (API-only; no direct graph reads) |
| **Story Nodes** | `docs/reports/story_nodes/` | Draft/published story artifacts (evidence-first) |

### Expected file tree for this sub-area (v13+)

> Notes:
> - The v13 target layout standardizes `data/stac/collections/` and `data/stac/items/`.
> - `catalog.json` at this level is **optional**; only add it if you need a browseable STAC root Catalog (e.g., for STAC tooling). If present, it must link to Collections and must not contain Items directly.

~~~text
📁 data/
└── 📁 stac/
    ├── 📄 README.md
    ├── 📄 catalog.json                     # (optional) STAC root Catalog index
    ├── 📁 collections/
    │   ├── 📄 <collection-id>.collection.json
    │   └── 📄 ...
    └── 📁 items/
        ├── 📁 <collection-id>/             # preferred grouping (scales better)
        │   ├── 📄 <item-id>.item.json
        │   └── 📄 ...
        └── 📄 <item-id>.item.json          # allowed for small sets (avoid at scale)
~~~

### Naming and ID invariants (layout contract)
These rules exist to keep STAC outputs deterministic, diffable, and resolvable downstream:

- **Collection file naming (recommended):**
  - Filename: `<collection-id>.collection.json`
  - JSON `id` value MUST equal `<collection-id>`.
- **Item file naming (recommended):**
  - Filename: `<item-id>.item.json`
  - JSON `id` value MUST equal `<item-id>`.
- **Item → Collection linkage (required):**
  - Each Item MUST declare its parent Collection via `"collection": "<collection-id>"`.
  - If Items are grouped under `items/<collection-id>/`, the folder name MUST match the Item’s `"collection"` value.
- **Do not fork subsystem homes:**
  - In v13+ layout, STAC outputs belong in `data/stac/`. Domain folders may contain *mapping docs* and *domain notes*, but should not become alternate STAC output roots.

---

## 🧭 Context

### Background
- The KFM pipeline treats **catalog + provenance outputs as evidence artifacts** consumed downstream (Graph, API, UI, Story Nodes).
- The canonical ordering is preserved end-to-end:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

### Assumptions
- STAC outputs in `data/stac/` are produced from upstream domain processing (typically `data/<domain>/processed/`) by a deterministic catalog-build process.
- Validation targets are expected to exist under `schemas/` (STAC/DCAT/PROV), and CI enforces these contracts where present.

### Constraints and invariants
- Pipeline order is non-negotiable.
- Frontend consumes data via the API boundary and does not read Neo4j directly.
- Sensitivity and sovereignty concerns must be handled through redaction/generalization and governance gates; do not publish precise sensitive locations unless policy explicitly allows.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the authoritative KFM STAC profile content beyond base STAC 1.0 | TBD | TBD |
| What are the stable ID conventions for Collections and Items across domains | TBD | TBD |
| Do we require `data/stac/catalog.json` (root Catalog) as a standard artifact, or keep it optional | TBD | TBD |

### Future extensions
- Add/extend domain-specific STAC extensions via the governed STAC profile and matching JSON Schemas.
- Add CI lint rules for link integrity and orphan detection across STAC/DCAT/PROV.
- Add optional STAC “root catalog” output if a STAC browser/tooling path is adopted.

---

## 🗺️ Diagrams

### System and dataflow diagram

~~~mermaid
flowchart LR
  A[ETL and transforms] --> B[Processed domain outputs]
  B --> C[Catalog build]
  C --> D[STAC Collections and Items]
  C --> E[DCAT datasets]
  C --> F[PROV bundles]

  D --> G[Neo4j Graph]
  E --> G
  F --> G

  G --> H[APIs]
  H --> I[UI]
  I --> J[Story Nodes]
  J --> K[Focus Mode]
~~~

### Optional sequence diagram

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Request narrative or entity context
  API->>Graph: Fetch subgraph + provenance refs
  Graph-->>API: Context bundle with evidence IDs
  API-->>UI: Response with citations and audit flags
~~~

---

## 📦 Data and Metadata

### Inputs

| Input | Path | Contract / schema | Notes |
|---|---|---|---|
| Domain processed outputs | `data/<domain>/processed/` | Domain-specific | Source material for catalog build |
| Domain mapping docs (optional) | `data/<domain>/mappings/` | Governed docs | Explains dataset → STAC/DCAT/PROV mappings |
| STAC profile and schemas | `docs/standards/KFM_STAC_PROFILE.md` and `schemas/stac/` | KFM-STAC | Profile + JSON Schema validation targets |

### Outputs

| Output | Path | Contract / schema | Notes |
|---|---|---|---|
| STAC Collections | `data/stac/collections/` | `schemas/stac/` | Discoverable groupings for Items |
| STAC Items | `data/stac/items/` | `schemas/stac/` | Evidence-level metadata with assets/links |
| Optional root Catalog | `data/stac/catalog.json` | STAC core | Only if adopting a browseable STAC root |
| Cross-catalog alignment | `data/catalog/dcat/` + `data/prov/` | `schemas/dcat/` + `schemas/prov/` | Required pairing with STAC outputs |

### Asset `href` expectations (repo-safe)
- Prefer **relative `href` values** to keep the repo portable and reviewable.
- When an Item references a local artifact, prefer pointing into canonical data roots (typically `data/<domain>/processed/` and/or versioned release bundles under `releases/`, if adopted).
- Do not point assets at UI runtime paths under `web/` (UI assets are not evidence sources).

### Sensitivity and redaction
- If an Item contains sensitive geometry, culturally sensitive knowledge, or restricted site locations:
  - apply redaction/generalization consistent with governance and sovereignty policy **before** publishing artifacts here,
  - ensure downstream UI exposure occurs only through the API boundary with classification enforcement.

### Quality signals
- Outputs validate against schemas where applicable.
- Catalog build is deterministic and repeatable.
- No orphan references between STAC, DCAT, PROV, Story Nodes, and Graph ingestion.
- Item assets have resolvable `href` targets (or explicitly documented external references).

---

## 🌐 STAC, DCAT and PROV Alignment

### Required alignment rule
Each new dataset or evidence product is expected to have:
- STAC catalog entry (Collection + Item(s))
- DCAT dataset description
- PROV activity describing how it was produced

### Linkage conventions
- The exact mechanism for linking STAC ↔ DCAT ↔ PROV (properties vs links vs extensions) is defined by the governed **KFM STAC profile** and schema set.
- Downstream systems (Graph/API/UI/Story Nodes) should be able to resolve a STAC Item ID into:
  - a DCAT dataset identifier, and
  - a PROV activity/bundle identifier.

### Versioning and lineage
- Version relationships should be represented as explicit metadata links and mirrored in the graph so users can trace how evidence evolves over time.

---

## 🏗️ Architecture

### Components

| Layer / component | Responsibility | Owned by | Notes |
|---|---|---|---|
| Catalog outputs | Emit STAC/DCAT/PROV evidence artifacts | Data/Catalog maintainers | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Graph ingestion | Read catalog outputs and build graph | Graph maintainers | Uses STAC/DCAT/PROV as inputs |
| API boundary | Contracted access + redaction | Server maintainers | UI consumes via APIs only |
| UI | Map + narrative interface | Web maintainers | Uses API results and citations |
| Story Nodes | Evidence-led narratives | Curators | Must cite evidence IDs |

### Interfaces and contracts

| Interface | Canonical location | Schema / contract |
|---|---|---|
| STAC JSON | `data/stac/` | `schemas/stac/` |
| DCAT JSON-LD | `data/catalog/dcat/` | `schemas/dcat/` |
| PROV JSON-LD | `data/prov/` | `schemas/prov/` |
| API payloads | `src/server/` | OpenAPI / GraphQL |

### Extension points checklist
- [ ] New dataset added under `data/<domain>/...`
- [ ] STAC Collections and Items generated and validated
- [ ] DCAT dataset record created or updated
- [ ] PROV activity recorded
- [ ] Graph ingest updated if needed
- [ ] API endpoints expose new artifacts as needed
- [ ] UI layer and Story Nodes updated only via API contracts

---

## 🧠 Story Node and Focus Mode Integration

### How STAC artifacts surface downstream
- Story Nodes should reference evidence IDs that resolve to STAC/DCAT/PROV artifacts.
- Focus Mode narratives must only present provenance-linked content; any AI-derived narrative must include auditability and uncertainty metadata where required.

---

## ✅ Validation and CI

### Validation steps
- [ ] STAC JSON validates against `schemas/stac/` where applicable
- [ ] Link integrity checks pass (no broken internal references)
- [ ] No orphan references across STAC/DCAT/PROV/Graph/Story Nodes
- [ ] Determinism checks pass for catalog build outputs (diffable reruns)

### Reproduction

~~~bash
# Placeholder: replace with repo-specific commands.
# Suggested structure (not commands):
# 1) Run catalog build for one domain.
# 2) Validate STAC/DCAT/PROV outputs against schemas.
# 3) Verify deterministic outputs across two runs.
~~~

---

## 📡 Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Catalog validation pass/fail | CI | `docs/telemetry/` + `schemas/telemetry/` *(if adopted)* |
| Orphan reference count | CI | `docs/telemetry/` + `schemas/telemetry/` *(if adopted)* |
| Link integrity failures | CI | CI logs + validation reports *(location varies by repo)* |

---

## ⚖ FAIR+CARE and Governance

### Review gates
- Changes that affect schema validation, redaction rules, or sensitive data handling require human review.
- Any expansion of catalog fields that could expose sensitive locations must be reviewed under sovereignty policy.

### CARE and sovereignty considerations
- Identify communities impacted and protection rules in domain documentation.
- Use generalization or redaction where required by sovereignty and ethics policy.

### AI usage constraints
- AI must not infer sensitive locations.
- AI outputs used in downstream narrative must remain provenance-linked and auditable.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for `data/stac/` | TBD |
| v1.0.1 | 2025-12-24 | Align layout + naming invariants with v13 contract-first STAC outputs guidance | TBD |

---

Footer refs:
- Parent data README: `data/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- STAC profile: `docs/standards/KFM_STAC_PROFILE.md`