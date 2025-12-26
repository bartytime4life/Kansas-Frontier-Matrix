---
title: "KFM web/public — Public Static Assets"
path: "web/public/README.md"
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

doc_uuid: "urn:kfm:doc:web:public:readme:v1.0.0"
semantic_document_id: "kfm-web-public-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public:readme:v1.0.0"

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

# web/public — Public Static Assets

> **Purpose (required):** Define what is allowed in `web/public/` (static, client-reachable assets), how to keep those assets safe and license-clean, and how they connect to KFM provenance, Story Nodes, and Focus Mode.

## 📘 Overview

### Purpose

- `web/public/` is the **public static asset root** for the KFM web UI (exact behavior depends on the web build tooling — not confirmed in repo).
- This README governs:
  - what can be placed here,
  - what must never be placed here,
  - and what review gates apply before an asset becomes public.

### Scope

| In Scope | Out of Scope |
|---|---|
| Favicons, robots, web manifest (if used) | Secrets (API keys), credentials, tokens |
| Static images/icons/fonts used by the UI | Raw or processed datasets (`data/**`) |
| Map/UI style assets (sprites, glyphs, style JSON) when intentionally public | Anything requiring access control or redaction |
| Publication-cleared Story Node media (non-sensitive) | Dropping “data dumps” here to bypass the API boundary |

### Audience

- Primary: UI engineers working in `web/`
- Secondary: data stewards / governance reviewers verifying what becomes public-facing

### Definitions

- Glossary link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Public asset**: any file reachable by a user’s browser without authentication.
  - **Evidence artifact**: downstream outputs (STAC/DCAT/PROV) that must remain traceable to upstream sources.
  - **Story Node asset**: an image/icon used inside a Story Node page or Focus Mode UI.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical homes by stage |
| UI home | `web/` | UI owners | Map UI + Focus Mode UI |
| API boundary | `src/server/` | API owners | Redaction + contracts; UI does not read Neo4j directly |
| Governance rules | `docs/governance/*.md` | Governance | Public exposure + sovereignty |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story owners | Provenance-linked narrative |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] Directory guidance clearly separates “safe public assets” vs “never here”
- [ ] Review triggers + sovereignty cautions stated
- [ ] Guidance links to pipeline invariants (API boundary, provenance, Story Nodes)

## 🗂️ Directory Layout

### This document

- `path`: `web/public/README.md` (must match front-matter)

### Typical structure

> Exact contents depend on the UI build system and enabled UI features (not confirmed in repo). This tree shows a recommended pattern for KFM.

~~~text
📁 web/
└─ 📁 public/
   ├─ 📄 README.md
   ├─ 📄 favicon.ico                         (example; not confirmed in repo)
   ├─ 📄 robots.txt                           (example; not confirmed in repo)
   ├─ 📄 manifest.webmanifest                 (example; not confirmed in repo)
   ├─ 📁 assets/                              (recommended)
   │  ├─ 📁 images/                           (logos, story images, UI illustrations)
   │  ├─ 📁 icons/                            (static SVG/PNG icons)
   │  ├─ 📁 fonts/                            (self-hosted fonts; license-cleared)
   │  └─ 📁 map/                              (sprites/glyphs/styles if self-hosted)
   └─ 📁 config/                              (optional runtime config; see rules below)
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React/MapLibre UI + Focus Mode UI |
| Public assets | `web/public/` | Static files reachable by browsers |
| API boundary | `src/server/` | Public endpoints, redaction, auth/RBAC |
| Graph | `src/graph/` | Ontology-governed ingest/migrations |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence + provenance outputs |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published stories + citations |

## 🧭 Context

### Why `web/public/` is high-risk

Everything in `web/public/` should be treated as:
- publicly accessible,
- cacheable,
- and mirrorable.

If it contains sensitive coordinates, restricted locations, or PII, it is already a leak.
If it contains “data dumps”, it can silently bypass API-based redaction, rate limits, and auditing.

### KFM pipeline boundary reminder

KFM canonical flow:

ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode

`web/public/` is part of the **UI delivery mechanism**, not part of the data pipeline.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL / Pipelines] --> B[STAC / DCAT Catalogs]
  B --> C[PROV Lineage]
  C --> D[Graph (Neo4j)]
  D --> E[API Layer]
  E --> F[UI (web/)]
  F --> G[Story Nodes]
  G --> H[Focus Mode]
~~~

## 📦 Data & Metadata

### Data lifecycle

Authoritative data + evidence artifacts live under:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` + `data/catalog/dcat/` + `data/prov/`

`web/public/` is not an alternative to `data/**`.

### What is allowed in `web/public/`

Allowed (typical):
- App shell assets (favicon/manifest/robots, if used).
- UI media: images, icons, fonts.
- Map style resources (sprites/glyphs/styles) only if intentionally public and license-cleared.
- Story Node media already approved for public release (e.g., non-sensitive hero images).

Allowed with caution:
- Small runtime config JSON (feature flags, public base URLs).
  - Must not include secrets.
  - Must not include hidden endpoints or credentials.
  - Prefer bundling configuration at build-time where possible (build system details not confirmed in repo).

Not allowed:
- Anything that should be access-controlled, even “temporarily”.
- Raw/processed datasets, CSV/GeoJSON exports, or any file that duplicates `data/**`.
- Private PDFs/images used for internal review.

## 🌐 STAC, DCAT & PROV Alignment

### Linking public assets back to evidence

If a public asset is derived from a dataset (e.g., a preview image of a processed layer):
- provenance must exist in `data/prov/` (transform activity + inputs + outputs),
- the dataset should remain discoverable via STAC/DCAT when applicable,
- Story Nodes should cite dataset/item identifiers, not the image alone.

### Avoid shadow datasets

Do not publish GeoJSON/CSV “for convenience” in `web/public/`.
If the UI needs data:
- expose it through `src/server/` as an API endpoint,
- apply redaction/generalization where required,
- and keep contract tests + logging at the API boundary.

## 🧱 Architecture

### Subsystem contract

| Subsystem | Contract artifacts | Do not break rule |
|---|---|---|
| UI public assets | `web/public/**` + this README | No secrets; no sensitive location leakage |
| API boundary | OpenAPI/GraphQL + tests | UI never reads Neo4j directly |
| Governance | review gates + policy docs | Public exposure & sovereignty enforced |

### API boundary rule

Even if it is “easier” to drop JSON into `web/public/`, do not do it if that data:
- could be sensitive now or later,
- needs versioning and provenance,
- needs access control,
- or needs redaction.

Route it through the API.

## 🧠 Story Node & Focus Mode Integration

### How this surfaces in Story Nodes

Story Nodes may reference static illustrative media from `web/public/assets/...` (if this convention is adopted — not confirmed in repo).
Requirements:
- media must be publication-cleared (license + sensitivity),
- media must not introduce new factual claims without citations,
- any data-derived figures/visualizations must be traceable to dataset identifiers.

### Focus Mode rule

Focus Mode must only consume provenance-linked content.
If a public asset is used in Focus Mode:
- link it to an evidence artifact (STAC/DCAT/PROV),
- do not treat the asset itself as the “source of truth”.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown lint / protocol checks for this README
- [ ] Secret scan / credential scan on `web/public/**`
- [ ] License compliance spot-check for newly added assets
- [ ] Accessibility checks where assets are referenced in UI
- [ ] Governance review if any asset could reveal sensitive locations

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run markdown / doc lint
# 2) run secret scan
# 3) run UI build + basic smoke tests
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

Any of the following changes should trigger governance review:
- adding or changing public assets that could reveal restricted locations by interaction/zoom/metadata,
- adding assets derived from sensitive/restricted inputs,
- adding runtime config that changes data access patterns or endpoints.

### CARE / sovereignty considerations

- Treat location-bearing content as high-risk by default.
- Apply `docs/governance/SOVEREIGNTY.md` when assets intersect with tribal jurisdictions or culturally sensitive sites.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy; inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `web/public/` README in governed-doc format | TBD |

---

## Footer refs

Do not remove.

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
