---
title: "KFM UI Governance Images — README"
path: "web/public/images/governance/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:web:public-images-governance:readme:v1.0.0"
semantic_document_id: "kfm-web-public-images-governance-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public-images-governance:readme:v1.0.0"
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

# KFM UI Governance Images — README

## 📘 Overview

### Purpose

- Provide a governed, stable location for **web UI governance imagery** (e.g., badges, labels, icons) used to communicate governance / audit / sensitivity affordances in the KFM frontend.
- Define **conventions** for adding and maintaining these static assets so UI paths remain stable and reviewable.

### Scope

| In Scope | Out of Scope |
|---|---|
| Static images under `web/public/images/governance/` | Authoring governance policy documents |
| Naming, attribution, and usage conventions for these images | Changes to API payloads, schemas, or graph |
| Guidance to avoid misleading or sensitive-revealing imagery | Any “official” legal/ethics determinations |

### Audience

- Primary: Frontend/UI maintainers; documentation maintainers
- Secondary: Governance reviewers (for changes that affect how governance is represented in the UI)

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: governance badge, sensitivity label, attribution, audit affordance

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/public/images/governance/README.md` | UI maintainers | Directory contract + conventions |
| Governance images | `web/public/images/governance/` | UI maintainers | Static assets served at stable URLs |
| (Optional) attribution file | `web/public/images/governance/attribution.md` | UI maintainers | Use if any third-party assets are included |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory layout includes an emoji tree and matches actual folder structure
- [ ] Conventions are clear (naming, format, attribution)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (no sensitive leakage via imagery)

## 🗂️ Directory Layout

### This document

- `path`: `web/public/images/governance/README.md`

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
📁 web/
└── 📁 public/
    └── 📁 images/
        └── 📁 governance/
            ├── 📄 README.md
            ├── 📄 attribution.md                (optional)
            ├── 🖼️ <governance-icon>.svg         (preferred)
            └── 🖼️ <governance-icon>.png         (only when raster is required)
~~~

## 🧭 Context

### Background

- The UI needs a consistent, reviewable way to show governance and audit signals (e.g., “public vs restricted”, “provenance available”, “care/sovereignty note present”) without embedding policy text into UI code.
- Keeping these assets in a stable public path supports predictable rendering and reduces duplication.

### Assumptions

- These assets are safe for public distribution at their committed resolution.
- Any iconography that could imply a policy outcome is treated as a **UI label**, not an authority statement.

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we need an `attribution.md` now, or only when third-party assets are added? | TBD | TBD |
| Should we standardize light/dark variants (e.g., `*-dark.svg`, `*-light.svg`)? | TBD | TBD |

### Future extensions

- Extension point A: Add a small set of standardized badge variants once the UI layer registry defines the governance fields it renders.
- Extension point B: Add a simple manifest (JSON) if the UI needs to enumerate available icons (only if required by the frontend).

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

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Request (includes governance fields)
  API->>Graph: Query (with redaction rules)
  Graph-->>API: Result + provenance refs
  API-->>UI: Contracted payload (UI renders icons from /public/images/governance/)
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)

- Not applicable: this directory contains **static UI assets**, not staged datasets.

### Domain expansion pattern

- Not applicable: adding images here does not create a new data domain.

## 🌐 STAC, DCAT & PROV Alignment

- Not applicable directly.
- If an icon is used to represent a governance state that originates from catalogs/lineage (e.g., “provenance present”), the **source of truth must remain the API payload**; the icon is only a visual affordance.

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| UI (assets) | Stable public asset paths | do not silently rename/move assets consumed by UI |
| UI (code) | layer registry + a11y + audit affordances | no hidden data leakage |

## 🧠 Story Node & Focus Mode Integration

- If these icons are used in Story Nodes / Focus Mode UI, they must not introduce unsourced claims.
- Any predictive content remains opt-in and must show uncertainty/confidence (icons here should not be used to “launder” uncertainty).

## 🧪 Validation & CI/CD

- [ ] Paths remain stable (no breaking renames without coordinated UI change)
- [ ] SVGs are sanitized (no scripts/foreignObject)
- [ ] File sizes are reasonable for web delivery
- [ ] Any third-party assets have attribution captured (use `attribution.md` if needed)

## ⚖ FAIR+CARE & Governance

### Governance review triggers (for this directory)

- New iconography that changes how sensitivity/governance is communicated in the UI (risk: misrepresentation).
- Any asset that could reveal restricted locations or culturally sensitive information in imagery (avoid; use generalized/abstract symbols instead).

### Sovereignty safety

- Do not add assets that disclose precise locations or identifying details for restricted/sensitive sites.

### AI usage constraints

- Ensure this doc’s AI permissions/prohibitions match intended use (no “generate policy”; no inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for governance image assets | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`