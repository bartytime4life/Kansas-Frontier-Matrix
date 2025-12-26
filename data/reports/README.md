---
title: "KFM Data Reports — README"
path: "data/reports/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:data:reports:readme:v1.0.0"
semantic_document_id: "kfm-data-reports-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:reports:readme:v1.0.0"
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

# KFM Data Reports — README

`data/reports/` is the canonical home for **optional evidence products / analysis outputs** generated from KFM data domains (e.g., charts, summaries, validation reports, export bundles) when those outputs are meant to be reviewed, shared, or referenced downstream.

**Non‑negotiable alignment rule:** `data/reports/` must not bypass KFM’s canonical pipeline ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Reports may be generated at any point, but if a report becomes a *public-facing* or *decision-significant* evidence artifact, it must be made **discoverable + traceable** via the catalogs (STAC/DCAT/PROV) and referenced through the contracted API boundary.

---

## 📘 Overview

### Purpose

- Provide a predictable, governed place to store **report-style artifacts** that are derived from KFM datasets.
- Clarify how reports relate to:
  - domain staging (`data/raw/`, `data/work/`, `data/processed/`)
  - catalog outputs (`data/stac/`, `data/catalog/dcat/`, `data/prov/`)
  - narrative outputs (`docs/reports/story_nodes/`)
- Prevent “mystery outputs” that are not traceable to inputs, runs, and catalogs.

### Scope

| In Scope | Out of Scope |
|---|---|
| Human-facing evidence outputs (tables, figures, report PDFs/HTML/MD, validation summaries) | Raw source snapshots (belongs in `data/raw/<domain>/`) |
| Automated QA / validation reports emitted by pipelines or CI | Intermediate transforms (belongs in `data/work/<domain>/`) |
| Export bundles intended for reviewers or release candidates | Canonical processed datasets (belongs in `data/processed/<domain>/`) |
| Evidence artifacts that are referenced by Story Nodes (via catalog IDs) | Story Nodes themselves (belongs in `docs/reports/story_nodes/`) |
| Optional derived outputs explicitly treated as catalog assets | API/UI code or graph migrations |

### Audience

- Data + pipeline contributors producing analysis outputs
- Curators/reviewers verifying traceability before publication
- Governance/security reviewers validating sensitivity + sovereignty handling
- API/UI maintainers ensuring evidence can be served with redaction rules (as applicable)

### Definitions (link to glossary)

- Link: `docs/glossary.md` (not confirmed in repo)

Terms used in this README:

- **report**: a presentation-oriented artifact (tables/figures/summary) derived from canonical datasets
- **evidence product**: a report/output that is intended to be referenced downstream (graph, API, UI, Story Nodes)
- **catalog linkage**: an explicit mapping from report outputs to STAC/DCAT/PROV identifiers
- **provenance pointer**: a reference to the generating PROV activity (and its used/generated entities)

### Key artifacts (what this README points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering | `docs/MASTER_GUIDE_v12.md` | KFM Maintainers | ETL → catalogs → graph → APIs → UI → story → focus |
| Data lifecycle rules | `data/README.md` | Data/Pipeline Maintainers | Governs raw/work/processed/stac semantics |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Data/Catalog Maintainers | Evidence + lineage source of truth |
| Story Nodes | `docs/reports/story_nodes/` | Editors/Curators | Evidence-first narrative artifacts |
| MCP runs/experiments | `mcp/runs/`, `mcp/experiments/` | Contributors | Run manifests + reproducibility artifacts |

### Definition of done (for this README)

- [ ] Front-matter complete + valid (path matches)
- [ ] `data/reports/` responsibilities and placement rules documented
- [ ] Relationship to catalogs + provenance is explicit
- [ ] Sensitivity + governance constraints stated (reports may contain sensitive derivatives)
- [ ] Validation expectations listed (even if commands are placeholders)
- [ ] Maintainer review

---

## 🗂️ Directory Layout

### This document

- `path`: `data/reports/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| Data staging (required) | `data/raw/`, `data/work/`, `data/processed/` | Raw → intermediate → certified outputs |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV evidence + lineage |
| Pipelines | `src/pipelines/` | Deterministic ETL + transforms + catalog builders |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings + ingest fixtures |
| API boundary | `src/server/` | Contracted access + redaction + provenance mediation |
| UI | `web/` | Map + narrative UX (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts + assets |
| MCP | `mcp/` | Experiments, model cards, run manifests |

### Expected file tree for this sub-area

> Notes:
> - Items marked **(recommended)** may not exist yet (not confirmed in repo).
> - `data/reports/` is optional; if present, it must remain governed and provenance-linked.

~~~text
📁 data/
└── 📁 reports/
    ├── 📄 README.md
    ├── 📁 <domain>/
    │   ├── 📄 README.md (recommended)
    │   ├── 📁 <report_slug>/ (recommended)
    │   │   ├── 📄 README.md (required for report bundles)
    │   │   ├── 📄 report.md (optional)
    │   │   ├── 📄 report.pdf (optional)
    │   │   ├── 📁 assets/ (optional)
    │   │   │   ├── 🖼️ figure-*.png
    │   │   │   └── 🎞️ animation-*.mp4
    │   │   ├── 📁 tables/ (optional)
    │   │   │   └── 📄 *.csv
    │   │   └── 📄 checksums.sha256 (recommended)
    │   └── 📁 validation/ (optional)
    │       └── 📄 *.md
    └── 📁 _shared/ (optional; use sparingly)
        └── 📄 README.md
~~~

---

## 🧭 Context

### Background

KFM’s system design prioritizes **auditability** and **traceability**. The core invariant is that anything consumed by UI/Story/Focus must be resolvable through **catalog + provenance** artifacts and served via the API boundary (no direct UI → graph reads).

`data/reports/` exists to capture “analysis outputs” *without* mixing them into the canonical staging folders. When reports become evidence products, they must still connect back to the evidence chain (STAC/DCAT/PROV + run IDs).

### Assumptions

- Not all domains will have reports.
- Not all reports are “evidence products” — some are internal review artifacts.
- When a report is used in Story Nodes or UI, it must be provenance-linked and reviewable.

### Constraints / invariants

- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- **No UI direct-to-graph reads:** all graph access is via `src/server/`.
- Reports must not “hide” derived datasets:
  - derived datasets → `data/processed/<domain>/`
  - presentation outputs → `data/reports/<domain>/`
- Do not store secrets, tokens, credentials, or personal data in this area.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we standardize a minimal `report_manifest.json` schema for report bundles? | TBD | TBD |
| Do we require every report bundle to have a PROV activity pointer file? | TBD | TBD |
| Do we publish certain reports via Releases (`releases/`)? | TBD | TBD |

### Future extensions

- Automated linking from `data/reports/**` → STAC assets → PROV activities
- CI gate that flags report bundles lacking provenance pointers when referenced by Story Nodes
- Optional report registry schema under `schemas/` (not confirmed in repo)

---

## 🗺️ Diagrams

### Where `data/reports/` fits in the canonical pipeline

~~~mermaid
flowchart LR
  A["ETL<br/>src/pipelines"] --> B["Catalogs<br/>data/stac + data/catalog/dcat + data/prov"]
  B --> C["Graph<br/>src/graph (+ data/graph if present)"]
  C --> D["API boundary<br/>src/server"]
  D --> E["UI<br/>web"]
  E --> F["Story Nodes<br/>docs/reports/story_nodes"]
  F --> G["Focus Mode<br/>provenance-linked only"]

  P["Presentation outputs<br/>data/reports"] -. optional evidence assets .-> B
  P -. referenced by .-> F
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Where from | Notes |
|---|---|---|
| Certified datasets | `data/processed/<domain>/` | Prefer to derive reports from certified outputs |
| Catalog IDs | `data/stac/**`, `data/catalog/dcat/**` | Use stable IDs in report metadata and links |
| Provenance bundles | `data/prov/**` | Reports should reference the generating activity |
| Run manifests / configs | `mcp/runs/**`, `src/pipelines/**` | Keep generation reproducible |

### Outputs

| Output | Typical formats | Destination | Notes |
|---|---|---|---|
| Report artifacts | PDF/MD/HTML/PNG/CSV/MP4 | `data/reports/<domain>/...` | Presentation-first outputs |
| Validation summaries | MD/JSON | `data/reports/<domain>/validation/` | Optional, but recommended for review |
| Checksums | sha256 list | alongside report outputs | Recommended for integrity |

> Format allowance: KFM catalogs commonly reference assets such as COG, GeoJSON, CSV, NetCDF, and MP4; if reports introduce additional formats (PDF/PNG/HTML), ensure catalog + schema expectations support them (not confirmed in repo).

### Placement rules

- If the artifact is a **dataset** intended for downstream computation:
  - land it in `data/processed/<domain>/` and catalog it.
- If the artifact is a **presentation/report** derived from certified datasets:
  - land it under `data/reports/<domain>/`.
- If a report is used in Story Nodes or UI:
  - it must be traceable through the catalogs and provenance chain (see below).

### Naming conventions (recommended)

Not confirmed in repo. Recommended pattern for report bundle folder names:

- `<YYYY-MM-DD>__<short-slug>__v<semver>`
- Example: `2025-12-26__air-quality-summary__v1.0.0`

Avoid ambiguous names like `final/` or `new/`.

---

## 🌐 STAC, DCAT & PROV Alignment

### Policy for every dataset / evidence product

For each dataset or evidence product:

- STAC Collection + Item(s)
- DCAT mapping record (minimum title/description/license/keywords)
- PROV activity describing lineage (sources + run/activity identifiers)
- Version lineage links reflected in catalogs and (where applicable) the graph

### How reports connect to catalogs (recommended)

When a report becomes an evidence product, ensure at least one of the following (project-specific choice; not confirmed in repo):

- **Option A:** Add the report files as **STAC Assets** on an existing relevant STAC Item.
- **Option B:** Create a dedicated **STAC Item** whose primary asset(s) are the report artifacts.

When using STAC Assets, prefer the required + recommended fields used across KFM:

- Required: `href`, `type`, `roles`
- Recommended: checksum (sha256), `title`, `description`

### Identifier linkage expectation

Graph nodes and APIs should reference:

- STAC Item IDs
- DCAT dataset ID
- PROV activity ID

This enables Focus Mode to resolve “what is this?” into a traceable lineage bundle.

---

## 🧱 Architecture

### Components and contracts

| Component | Responsibility | Interface |
|---|---|---|
| `data/reports/**` | Store report-style derived outputs | Files + README metadata |
| Catalogs | Provide discoverable evidence + lineage | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` |
| Graph | Reference evidence IDs; enforce semantics | `src/graph/**` (+ ingest fixtures) |
| API boundary | Serve report links with provenance + redaction | `src/server/**` + contracts |
| UI | Render evidence-first views | `web/**` |
| Story Nodes | Cite evidence IDs and link to report assets | `docs/reports/story_nodes/**` |

### API boundary rule

- The UI does **not** connect to Neo4j directly.
- The API boundary mediates access and enforces provenance + redaction/generalization rules.

### Story Node & Focus Mode integration

- Story Nodes should cite **graph entity IDs** and **STAC/DCAT/PROV evidence IDs**.
- Focus Mode must only consume **provenance-linked** content (no hallucinated sources).

---

## 🧪 Validation & CI/CD

### CI behavior contract

- **Validate if present**: if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid**: schema errors, missing links, or orphan references fail deterministically.
- **Skip if not applicable**: optional roots absent → skip without failing the overall pipeline.

### Minimum checks (recommended)

- [ ] Markdown protocol checks (for governed docs)
- [ ] Link integrity checks for docs (if tooling exists)
- [ ] If reports are cataloged: STAC/DCAT/PROV schema validation
- [ ] Provenance linkage checks (no dangling PROV refs for published evidence products)
- [ ] Security and sovereignty checks (as applicable)

### Local reproduction (placeholders)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# 1) validate schemas
# make validate-schemas

# 2) validate provenance bundles / lineage
# make validate-lineage

# 3) lint docs / link checks
# make lint-docs
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that typically require elevated review:

- Adding new sensitive layers (restricted locations, cultural knowledge, PII, etc.)
- Introducing/changing AI-generated narrative behavior visible to users
- Adding new external data sources
- Adding new public-facing endpoints
- Publishing report outputs that include high-precision locations or culturally sensitive interpretations

### CARE / sovereignty considerations

Reports can unintentionally increase risk (e.g., by combining datasets into more precise location inference). Treat location-bearing or culturally sensitive derivatives conservatively:

- avoid inferring private/sensitive locations
- apply generalization where required
- require explicit review before publication

### AI usage constraints

This README allows AI transforms like summarization and structure extraction, but prohibits generating new policy or inferring sensitive locations (see front matter). Any AI-derived report intended as evidence must be explicitly marked and linked to source evidence IDs and provenance.

---

## 🧾 Version History

| Version | Date | Change | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `data/reports/` README | TBD |

---

## Footer refs

- `docs/MASTER_GUIDE_v12.md`
- `data/README.md`
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/reports/story_nodes/` (if present)
- `schemas/` (if present; for catalog/story validation)
- `src/pipelines/`, `src/graph/`, `src/server/`, `web/`
- `mcp/runs/`, `mcp/experiments/`

