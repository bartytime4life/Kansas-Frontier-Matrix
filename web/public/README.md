---
title: "KFM web/public — Public Static Assets"
path: "web/public/README.md"
version: "v1.0.1"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:web:public:readme:v1.0.1"
semantic_document_id: "kfm-web-public-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:public:readme:v1.0.1"

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

- `web/public/` is the **public static asset root** for the KFM web UI.
- Treat **every file in this folder as browser-reachable, cacheable, and mirrorable**.
- This README governs:
  - what can be placed here,
  - what must never be placed here,
  - what review/validation gates apply before an asset becomes public.

> Build tooling details (e.g., Vite/Next/etc.) determine exact behavior and routing; this is **not confirmed in repo**. Operate under the safest assumption: **if it’s in `web/public/`, it is public**.

### Non-negotiables

- **No secrets, ever** (tokens, credentials, private keys, `.env` files).
- **No restricted/sensitive location leakage** (direct coordinates, detailed site maps, EXIF geotags, hidden metadata).
- **No “shadow datasets”** (CSV/GeoJSON dumps, tiles, or exports that bypass catalogs and the API boundary).
- **No policy bypass**: if the UI needs data, it goes through the API (redaction + auditability), not `web/public/`.

### Scope

| In Scope | Out of Scope |
|---|---|
| Favicons, robots, web manifest **if used** | Secrets (API keys), credentials, tokens |
| Static images/icons/fonts used by the UI | Raw/work/processed datasets (`data/**`) |
| Self-hosted map style assets (sprites/glyphs/style JSON) **only if intentionally public** | Anything requiring access control or redaction |
| Publication-cleared, non-sensitive media used in Story Nodes / Focus Mode UI | “Convenience” data dumps that bypass the API boundary |
| Public, non-secret build/runtime config **only if explicitly intended** | Internal-only PDFs/images used for review or governance |

### Audience

- Primary: UI engineers working in `web/`
- Secondary: data stewards / governance reviewers verifying what becomes public-facing
- Tertiary: Story Node editors ensuring media is publishable and provenance-aligned

### Definitions

- Glossary link: `docs/glossary.md` *(expected by architecture docs; not confirmed in repo)*
- Terms used in this doc:
  - **Public asset**: any file reachable by a user’s browser without authentication.
  - **Derived visual asset**: an image/graphic generated from a dataset (preview tiles, chart exports, rendered maps).
  - **Evidence artifact**: downstream outputs (STAC/DCAT/PROV) that remain traceable to upstream sources.
  - **Shadow dataset**: a dataset-like file published in `web/public/` that duplicates or bypasses `data/**` and/or API controls.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Docs/Core | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governing structure for this README |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Provenance-linked narrative |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Contract-first boundary |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical homes + constraints *(if present)* |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] Directory guidance clearly separates “safe public assets” vs “never here”
- [ ] Rules reinforce canonical pipeline ordering + API boundary
- [ ] New/changed assets pass: secret scan, license check, metadata hygiene check (EXIF), and governance review triggers
- [ ] Derived visual assets (if any) are traceable to STAC/DCAT/PROV identifiers (asset is not treated as source-of-truth)

## 🗂️ Directory Layout

### This document

- `path`: `web/public/README.md` *(must match front-matter)*

### Typical structure

> Exact contents depend on the UI build system and enabled features (not confirmed in repo). This tree shows a recommended pattern for KFM.

~~~text
📁 web/
└─ 📁 public/
   ├─ 📄 README.md
   ├─ 📄 favicon.ico                         # example; not confirmed in repo
   ├─ 📄 robots.txt                           # example; not confirmed in repo
   ├─ 📄 manifest.webmanifest                 # example; not confirmed in repo
   ├─ 📁 assets/                              # recommended
   │  ├─ 📁 images/                           # logos, story media, UI illustrations
   │  ├─ 📁 icons/                            # static SVG/PNG icons
   │  ├─ 📁 fonts/                            # self-hosted fonts; license-cleared
   │  ├─ 📁 map/                              # sprites/glyphs/styles if self-hosted
   │  └─ 📁 previews/                         # dataset-derived preview images (if approved)
   └─ 📁 config/                              # optional public config; see rules below
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React/Map UI + Focus Mode UI |
| Public assets | `web/public/` | Static files reachable by browsers |
| API boundary | `src/server/` | Public endpoints, redaction, auth/RBAC, contracts |
| Graph | `src/graph/` | Ontology-governed ingest/migrations |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence + provenance outputs |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published stories + citations (canonical home) |

## 🧭 Context

### Why `web/public/` is high-risk

Everything in `web/public/` should be treated as:

- **publicly accessible** (no auth),
- **cacheable** (CDNs, service workers),
- **mirrorable** (copied and redistributed).

If it contains sensitive coordinates, restricted locations, or PII, it is already a leak.
If it contains “data dumps”, it can silently bypass API-based redaction, rate limits, and auditing.

### Canonical pipeline reminder

KFM canonical flow:

ETL → STAC/DCAT/PROV → Graph (Neo4j) → API → UI → Story Nodes → Focus Mode

`web/public/` is part of the **UI delivery mechanism**, not part of the data pipeline.

### API boundary reminder

Even if it’s “easier” to drop JSON/GeoJSON into `web/public/`, do not do it when the content needs:

- redaction/generalization,
- provenance/versioning,
- access control,
- auditability/telemetry,
- or future re-classification.

Route it through the API.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["ETL / Pipelines"] --> B["STAC / DCAT Catalogs"];
  B --> C["PROV Lineage"];
  C --> D["Graph (Neo4j)"];
  D --> E["API Layer"];
  E --> F["UI (web/)"];
  F --> G["Story Nodes"];
  G --> H["Focus Mode"];
  F --> P["web/public — static assets"];
~~~

## 📦 Data & Metadata

### Data lifecycle

Authoritative data + evidence artifacts live under:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` + `data/catalog/dcat/` + `data/prov/`

`web/public/` is **not** an alternative to `data/**`.

### Allowed assets (and required hygiene)

| Asset type | Allowed? | Minimum requirements (before merge) |
|---|---:|---|
| Favicons / manifest / robots | ✅ | Confirm no sensitive URLs or disallowed crawling directives for restricted areas |
| UI images / icons | ✅ | License-cleared; remove EXIF/metadata; no sensitive location detail |
| Fonts (self-hosted) | ✅ | License-cleared; keep attribution info somewhere discoverable |
| Map style assets (sprites/glyphs/style JSON) | ⚠️ | Intentionally public; license-cleared; do not encode restricted locations or “hidden layers” |
| Small public config JSON | ⚠️ | No secrets; no internal hostnames; no access-controlled endpoints; documented purpose |
| PDFs | ⚠️ | Only if explicitly intended for public release; treat as content that can leak metadata |
| CSV/GeoJSON/tiles (data exports) | ❌ | Use `data/**` + catalogs + API instead |

### Prohibited content (hard fail)

- Any secrets: API keys, OAuth client secrets, private keys, tokens, credentials.
- Any raw/work/processed datasets or dataset-like exports (CSV, GeoJSON, tiles, parquet, etc.).
- Any restricted location content (coordinates, detailed maps, site plans) not explicitly approved.
- Any internal-only governance artifacts, reviews, or “temporary” redaction files.

### Metadata hygiene (images + documents)

Before merging new media into `web/public/`:

- Strip EXIF (GPS, device IDs, author names).
- Confirm filenames and embedded metadata do not contain personal names/emails.
- Prefer optimized formats and sizes (performance + bandwidth).
- For PDFs: check document properties (title/author/producer) and embedded links.

### Licensing hygiene (minimum)

For any third-party asset:

- Ensure it is license-compatible with project distribution.
- Preserve required attribution and notices (where required by the license).
- Do not remove copyright headers from licensed SVG/JS assets.

> Exact location/format for attribution (NOTICE file vs central registry) is **not confirmed in repo**. Use the repo’s established convention if present; otherwise add attribution adjacent to the asset and reference it from this README.

## 🌐 STAC, DCAT & PROV Alignment

### Linking derived visuals back to evidence

If a public asset is derived from a dataset (e.g., a preview image of a processed layer):

- provenance must exist in `data/prov/` (transform activity + inputs + outputs),
- the dataset should remain discoverable via STAC/DCAT when applicable,
- Story Nodes should cite dataset/item identifiers (STAC/DCAT/PROV), not the image alone.

**Rule of thumb:** the image is a *rendering*, not the *record*.

### Avoid shadow datasets

Do not publish GeoJSON/CSV “for convenience” in `web/public/`.
If the UI needs data:

- expose it through `src/server/` as an API endpoint,
- apply redaction/generalization where required,
- keep contract tests + logging at the API boundary.

## 🧱 Architecture

### Subsystem contract

| Subsystem | Contract artifacts | Do not break rule |
|---|---|---|
| UI public assets | `web/public/**` + this README | No secrets; no sensitive location leakage; no dataset bypass |
| API boundary | OpenAPI/GraphQL + tests | UI never reads Neo4j directly |
| Governance | review gates + policy docs | Public exposure & sovereignty enforced |

### Public config rules (`web/public/config/`)

If you use a `config/` folder:

- Only include **non-secret** values intended for public consumption.
- Treat config changes as **API/UI contract changes** (review + version awareness).
- Do not publish:
  - internal hostnames,
  - non-public endpoints,
  - “hidden” feature flags that imply restricted functionality,
  - any identifier that can be used as a credential.

If unsure: do not publish config here; prefer build-time configuration or an API-mediated config endpoint.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes

Story Nodes may reference static illustrative media from `web/public/assets/...` (if this convention is adopted — not confirmed in repo).

Requirements:

- media must be publication-cleared (license + sensitivity),
- media must not introduce new factual claims without citations,
- any data-derived figures/visualizations must be traceable to dataset identifiers (STAC/DCAT/PROV),
- do not embed restricted coordinates in images, captions, or metadata.

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
- [ ] Metadata hygiene check (EXIF/PDF properties) for new media
- [ ] Accessibility checks where assets are referenced in UI (alt text, contrast, etc.)
- [ ] Governance review if any asset could reveal sensitive locations

### Telemetry signals (if telemetry is implemented)

| Signal | Source | Where recorded |
|---|---|---|
| `promotion_blocked` | CI / governance gate | `docs/telemetry/` + `schemas/telemetry/` *(paths not confirmed in repo)* |
| `classification_assigned` | governance workflow | `docs/telemetry/` + `schemas/telemetry/` *(paths not confirmed in repo)* |
| `redaction_applied` | pipeline/API | `data/prov/**` and/or telemetry *(implementation-dependent)* |

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands.

# 1) markdown/doc lint
# 2) secret scan
# 3) UI build + smoke test
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

Any of the following changes should trigger governance review:

- adding/changing assets that could reveal restricted locations (directly or via zoom/detail),
- adding assets derived from sensitive/restricted inputs,
- publishing Story Node media that introduces new factual claims without evidence IDs,
- adding runtime config that changes data access patterns or endpoints.

### CARE / sovereignty considerations

- Treat location-bearing content as high-risk by default.
- Apply `docs/governance/SOVEREIGNTY.md` when assets intersect with tribal jurisdictions or culturally sensitive sites.
- If there is any doubt about sensitivity: do not publish in `web/public/`.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy; inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.1 | 2025-12-28 | Tightened rules (no shadow datasets), added asset hygiene + telemetry hints, aligned wording to canonical invariants | TBD |
| v1.0.0 | 2025-12-26 | Initial `web/public/` README in governed-doc format | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
