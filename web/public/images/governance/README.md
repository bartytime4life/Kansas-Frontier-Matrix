---
title: "KFM Governance Images — README"
path: "web/public/images/governance/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:web:public-images-governance-readme:v1.0.0"
semantic_document_id: "kfm-web-public-images-governance-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public-images-governance-readme:v1.0.0"
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

# KFM Governance Images — README

## 📘 Overview

### Purpose
- This README governs what belongs in `web/public/images/governance/` and how to add/maintain those assets.
- It exists to keep governance-related visuals (badges/icons/diagrams used by the UI) consistent, licensed, and safe to publish.

### Scope

| In Scope | Out of Scope |
|---|---|
| Governance UI icons/badges (e.g., provenance, audit, sensitivity indicators) | Evidence imagery or “source artifacts” that should be packaged and referenced as STAC/DCAT/PROV assets |
| Governance diagrams used by UI/help pages | User uploads, private screenshots, or any content containing PII |
| Placeholder visuals for governance/audit panels | Anything implying restricted locations, culturally sensitive knowledge, or redacted details |

### Audience
- Primary: Frontend/UI maintainers working under `web/`.
- Secondary: Curators, governance reviewers, and doc writers referencing governance visuals.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Public static asset**: A file placed under `web/public/` intended to be shipped to browsers.
  - **Governance visual**: A non-evidence UI affordance (badge/icon/diagram) that communicates governance state (e.g., “provenance available”, “redaction applied”).
  - **Attribution**: The minimal credit/license record needed for any third‑party asset.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Governance images directory | `web/public/images/governance/` | UI maintainers | Public/static distribution area |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance council | Canonical governance policies |
| Ethics policy | `docs/governance/ETHICS.md` | Governance council | Ethics constraints |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance council | CARE/sovereignty constraints |
| Story Nodes (canonical) | `docs/reports/story_nodes/` | Curators | May reference local assets with attribution |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Scope clearly separates UI visuals from evidence assets
- [ ] Addition rules include licensing/attribution requirements
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `web/public/images/governance/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Governed docs and story nodes |
| Governance | `docs/governance/` | Root governance + ethics + sovereignty policies |
| Frontend | `web/` | UI code + runtime assets |
| Public static assets | `web/public/` | Files shipped publicly by the UI build/deploy |
| Story Nodes | `docs/reports/story_nodes/` | Narrative nodes (may embed local assets with attribution) |
| Schemas | `schemas/` | JSON schemas (UI registries, story nodes, catalogs, telemetry) |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL + contract tests (UI consumes APIs, not graph) |

### Expected file tree for this sub-area

~~~text
web/public/images/governance/
  README.md
  badges/
  icons/
  diagrams/
  placeholders/
  third_party/
~~~

Notes:
- Subfolders are optional, but recommended to keep assets organized.
- Prefer **SVG** for icons/badges when possible; use raster formats only when necessary.

## 🧭 Context

### Background
Governance concepts (provenance, redaction, sensitivity, audit warnings) need consistent visual language in the UI. This directory provides a controlled location for those visuals.

### Assumptions
- Files under `web/public/` are treated as **public** outputs. Do not place sensitive content here.
- Governance visuals are **decorative/communicative**, not evidence-bearing.

### Constraints / invariants
- The canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The frontend consumes contracts via **APIs** (no direct graph dependency).
- This directory must **not** become an evidence store. Evidence images belong in cataloged assets (STAC/DCAT/PROV) and are rendered via API-delivered, provenance-linked references.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we want a single attribution registry file (e.g., `ATTRIBUTION.md`) for all non-original assets here? | TBD | TBD |
| Should CI enforce file-size ceilings and SVG optimization checks for this directory? | TBD | TBD |

### Future extensions
- Add an optional `ATTRIBUTION.md` and/or `manifest.json` mapping filenames → license/source/author.
- Add CI checks for:
  - broken references (docs/UI paths),
  - file-size limits,
  - SVG/raster optimization.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  subgraph CanonicalPipeline["Canonical pipeline (context)"]
    A[ETL] --> B[STAC/DCAT/PROV Catalogs]
    B --> C[Neo4j Graph]
    C --> D[APIs]
    D --> E[React/Map UI]
    E --> F[Story Nodes]
    F --> G[Focus Mode]
  end

  subgraph StaticAssets["UI static assets (this directory)"]
    H["web/public/images/governance/**"] --> E
  end
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant User as Browser/User
  participant UI as Web UI
  participant API as API Layer

  User->>UI: Load governance/audit panels
  UI->>UI: Render icons/badges from web/public/images/governance/**
  UI->>API: Request provenance-linked context (when needed)
  API-->>UI: Context bundle (citations + flags)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Source | Validation |
|---|---|---|---|
| Governance icons | SVG | KFM-original or permissively licensed | License recorded; SVG optimized; no embedded sensitive info |
| Governance badges | SVG/PNG/WebP | KFM-original or permissively licensed | License recorded; naming convention; size checked |
| Diagrams | SVG/PNG/WebP | KFM-original preferred | Ensure legibility + accessibility; no sensitive maps/locations |

### Outputs

| Output | Location | Consumers | Notes |
|---|---|---|---|
| Static governance visuals | `web/public/images/governance/**` | Web UI + docs (optional) | Public distribution; must be safe and licensed |

### Naming and organization rules
- Use `kebab-case` filenames.
- Recommended prefixes:
  - `icon-<name>.svg`
  - `badge-<name>.svg`
  - `diagram-<name>.png|svg`
- Avoid renames once referenced by UI/docs. If a rename is required, keep a compatibility copy until references are updated.

### Sensitivity & redaction
- Do not add images that reveal restricted locations or culturally sensitive knowledge.
- Do not embed PII in diagrams (names, emails, phone numbers, private addresses).
- If a governance diagram needs to illustrate a geography concept, keep it abstract and non-identifying.

## 🌐 STAC, DCAT & PROV Alignment

### STAC (geospatial assets)
- Governance UI visuals in this directory are **not** STAC assets.
- If an image is evidence (historical photo, map scan, dataset preview), it must be managed as a STAC asset and referenced through provenance-linked IDs—not stored here.

### DCAT (dataset cataloging)
- Not applicable for governance UI visuals, but licensing/attribution must still be tracked for reuse.

### PROV-O (lineage)
- Not applicable for these static UI visuals as provenance artifacts; repository history serves as change tracking.

### Versioning expectations
- Stable filenames are part of the UI contract.
- Increment this document’s `version` when:
  - the directory contract changes (new required subfolders, new mandatory attribution process),
  - naming conventions change,
  - governance rules for this directory change.

## 🧱 Architecture

### Components

| Component | Responsibility | Notes |
|---|---|---|
| `web/public/images/governance/**` | Static, publicly served UI assets | Governance visuals only |
| UI components (within `web/`) | Reference/render governance visuals | Should not embed evidence here |
| API layer | Provides provenance-linked content for Focus Mode/audit panels | UI consumes via APIs, not graph |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Governance image path convention | `web/public/images/governance/**` | Avoid breaking renames; treat paths as a UI contract |
| Attribution requirements for non-original assets | This README + consuming doc/PR metadata | Must be satisfied before merge |
| Separation of evidence vs UI visuals | Canonical pipeline + governance rules | Evidence must remain provenance-linked and cataloged |

### Extension points checklist (for future work)
- [ ] If adding new visuals that behave like “policy,” ensure governance review and alignment with `docs/governance/**`.
- [ ] If adding UI that displays evidence images, ensure the evidence is referenced via STAC/DCAT/PROV IDs and served via API (not stored here).
- [ ] If adding automated checks, document them under `docs/` and wire into CI.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Governance images may appear in:
  - audit panels (warnings, citations, sensitivity notices),
  - provenance indicators,
  - “redaction applied” UI states.
- These visuals must never substitute for evidence or citations; they only communicate state.

### Provenance-linked narrative rule
- Any narrative or claim rendered in Focus Mode must be provenance-linked (dataset/record/asset IDs).
- If Story Nodes embed local assets, ensure attribution is present in the node and the asset is appropriate for public distribution.

### Optional structured controls
~~~yaml
# Not applicable for this README (no Focus Mode parameters).
focus_layers: []
focus_time: "N/A"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + structure)
- [ ] Broken-link checks (docs/UI references to images)
- [ ] License/attribution check for any non-original assets
- [ ] Basic size/format checks (keep assets lightweight for web)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run markdown lint / protocol validation
# 2) run broken-link checks (if present)
# 3) run frontend build to confirm assets resolve
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Adding third-party assets (icons/logos/illustrations) requires:
  - license compatibility verification,
  - attribution record,
  - (if relevant) governance review.
- Any image that could imply restricted locations or culturally sensitive knowledge requires sovereignty review before inclusion.

### CARE / sovereignty considerations
- Avoid using imagery that depicts or references culturally restricted knowledge unless permission and governance controls are confirmed.
- Prefer abstract, non-identifying symbols for sensitivity/redaction indicators.

### AI usage constraints
- Ensure any AI assistance used to create/modify assets does not introduce:
  - copyrighted or non-redistributable content,
  - hidden sensitive location cues,
  - misleading “policy-like” graphics that are not backed by governance docs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for governance images directory | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master Guide (pipeline invariants): `docs/MASTER_GUIDE_v12.md`