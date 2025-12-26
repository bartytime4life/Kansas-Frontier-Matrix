---
title: "UI Formatting Utilities — web/src/utils/format"
path: "web/src/utils/format/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:web:utils:format:readme:v1.0.0"
semantic_document_id: "kfm-web-utils-format-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:utils:format:readme:v1.0.0"
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

<div align="center">

# 🧩 UI Formatting Utilities

`web/src/utils/format/`

**Purpose:** Shared, deterministic formatting helpers for the KFM web UI (numbers, dates/times, units, IDs, citations) with governance-aware redaction handling.

</div>

---

## 📘 Overview

### Purpose

- Provide consistent formatting for user-facing UI text (tooltips, legends, Focus Mode panels, Story Node rendering).
- Keep formatting logic **pure**, **reusable**, and **testable** across components.

### Scope

| In Scope | Out of Scope |
|---|---|
| String/number/date/unit formatting for UI display | ETL/data transformation, catalog generation, schema authoring |
| Formatting provenance/citation references *for display* | Fetching data, calling APIs, caching, or querying the graph |
| Deterministic, locale-aware rendering conventions | CSS/styling, component layout, map layer styling rules |

### Audience

- Primary: contributors working in `web/` (React/MapLibre UI).
- Secondary: API/graph contributors who need to understand how values appear in the UI.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo)*
- Terms commonly used here:
  - **Locale** — language/region formatting rules (e.g., `en-US`, `es-MX`)
  - **Timezone** — time rendering reference (e.g., `America/Chicago`)
  - **Precision** — how many decimals / significant digits are displayed
  - **Redaction / generalization** — controlled withholding or coarsening of sensitive details

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/src/utils/format/README.md` | UI | Folder contract & conventions |
| Master pipeline guide | `docs/MASTER_GUIDE_v12.md` | Core | Canonical ordering & invariants |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch | UI invariants + boundary rules *(path not confirmed in repo)* |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story | Citation token & narrative structure |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governed README structure |

### Definition of done (for this document)

- [ ] Front-matter complete + valid; `path:` matches file location
- [ ] Folder conventions are documented without claiming files exist unless they do
- [ ] Locale/timezone rules documented (no unintentional reliance on browser defaults)
- [ ] Redaction/generalization display rules documented (no UI leakage of restricted detail)
- [ ] Validation steps listed (lint + unit tests)
- [ ] Footer refs present

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/utils/format/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React + map clients (MapLibre/Cesium as applicable) |
| API boundary | `src/server/` | REST/GraphQL boundary; redaction/generalization enforcement |
| Graph | `src/graph/` | Ontology bindings + graph build (Neo4j ingest) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts consumed by UI |
| Templates | `docs/templates/` | Governed Markdown templates |
| Schemas | `schemas/` | JSON Schemas (UI registry, Story Nodes, telemetry, etc.) |

### Expected file tree for this sub-area

> The tree below includes **suggested** files; entries marked “not confirmed in repo” are placeholders only.

~~~text
web/
└── 📁 src/
    └── 📁 utils/
        └── 📁 format/
            ├── 📄 README.md
            ├── 📄 index.ts                          # public exports (not confirmed in repo)
            ├── 📄 formatNumber.ts                   # Intl.NumberFormat wrappers (not confirmed in repo)
            ├── 📄 formatDateTime.ts                 # Intl.DateTimeFormat wrappers (not confirmed in repo)
            ├── 📄 formatDuration.ts                 # seconds → "2h 13m" (not confirmed in repo)
            ├── 📄 formatDistance.ts                 # meters → "3.2 km" (not confirmed in repo)
            ├── 📄 formatCoordinate.ts               # redaction-aware lat/lon (not confirmed in repo)
            ├── 📄 formatId.ts                       # stable ID display helpers (not confirmed in repo)
            ├── 📄 formatCitationToken.ts            # Story Node citation token parsing (not confirmed in repo)
            └── 📁 __tests__/                        # unit tests (not confirmed in repo)
                └── 📄 *.test.ts
~~~

---

## 🧭 Context

### Background

KFM’s UI is designed to render contracted content coming from the **API boundary** (and catalog endpoints), including provenance-linked narrative content in Focus Mode. This folder exists to centralize formatting decisions so they are consistent across the UI and easy to test/review.

### Assumptions

- Prefer ECMAScript `Intl.*` APIs for locale-aware formatting.
- Formatting helpers should be:
  - **Pure**: no network calls, no file IO, no graph access, no hidden global state.
  - **Deterministic**: same input → same output.
  - **Fail-closed**: invalid inputs produce visible placeholders rather than misleading values.

### Constraints / invariants

- Preserve canonical pipeline ordering in system thinking: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **No UI direct-to-graph reads:** this folder must not import Neo4j drivers or perform Cypher queries.
- UI reads only from API endpoints and catalog endpoints; redaction/generalization is enforced at the API boundary.
- Formatting must not undo redaction/generalization:
  - Do not “pretty print” generalized geometry into higher precision.
  - If an upstream field is redacted, preserve that in UI output.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the default locale/timezone fallback (`en-US`, `America/Chicago`, etc.)? | UI | TBD |
| Do we support a unit system selector (metric/imperial) for distances/areas? | UI + Product | TBD |
| How should uncertain/predicted values be labeled (confidence, intervals) in UI strings? | UI + Story | TBD |

### Future extensions

- Add a single “format registry” export surface to reduce ad-hoc formatting scattered across components.
- Snapshot tests for key formats across 2–3 locales/timezones.
- Helpers to render provenance IDs (STAC Item IDs, PROV activity IDs) as short-but-stable labels.

---

## 🗺️ Diagrams

### Where `format/` sits in the UI

~~~mermaid
flowchart LR
  A[API responses<br/>src/server contracts] --> B[React components<br/>web/]
  B --> C[format utils<br/>web/src/utils/format]
  C --> D[Rendered UI text<br/>tooltips · legends · Focus Mode]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Numeric values (counts, rates, percentages) | `number` | API payloads, computed UI state | TypeScript types + runtime guards |
| Temporal values (ISO timestamps, years) | `string` / `number` | API, Story Node metadata | Parse/validate before formatting |
| Units + magnitude (m, km, acres, etc.) | structured object | API payloads *(preferred)* | Ensure unit is explicit |
| Coordinates / geometries | `number[]` / geojson-like | API payloads (already generalized/redacted) | Do not increase precision |
| Citation tokens | `string` | Story Node Markdown | Parse-only; never “invent” sources |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Display strings | `string` | `web/src/utils/format/*` | UI-only |
| Render-ready citation model | object | `formatCitationToken` *(not confirmed in repo)* | Must preserve token semantics |
| Accessibility-friendly labels | `string` | `format*` | Must remain WCAG-friendly |

### Sensitivity & redaction

- If an input is labeled/flagged as **restricted** or **redacted**, formatting must:
  - return a neutral placeholder (`"—"`, `"redacted"`, `"generalized"`) as configured,
  - optionally attach a UI-safe hint (e.g., “Location generalized for governance”) **without** revealing details.
- Do not derive sensitive information by combining multiple generalized hints (no reconstruction).

### Quality signals

- Unit tests cover:
  - invalid inputs (`null`, `undefined`, `NaN`)
  - boundary conditions (0, negative values, very large values)
  - locale variations (decimal separators, month/day order)
- Snapshot tests exist for high-visibility formats (Focus Mode metadata strings).

---

## 🌐 STAC, DCAT & PROV Alignment

Formatting utilities do **not** generate catalog artifacts, but they often **display** catalog/provenance identifiers in the UI.

Rules:

- Do not rewrite identifiers (STAC Item IDs, DCAT dataset IDs, PROV activity IDs).
- If IDs are shortened for UI, ensure:
  - the mapping is reversible, and
  - the full ID remains accessible (tooltip/copy/details panel).

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| API boundary (`src/server/`) | Returns redacted/generalized payloads + provenance links | REST/GraphQL contracts |
| UI (`web/`) | Renders map + narratives + Focus Mode panels | API calls + catalog endpoints |
| Formatting utils (`web/src/utils/format/`) | Deterministic formatting for UI display | Pure functions |
| Story Nodes (`docs/reports/story_nodes/`) | Governed narrative artifacts with citations | Markdown + references |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/**` | Semver + contract tests |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Semver + validation |
| UI layer registry schema | `schemas/ui/**` | Semver + schema validation |

---

## 🧠 Story Node & Focus Mode Integration

### Why formatting matters here

In Focus Mode, the UI renders narrative + citations + audit/provenance affordances. Formatting helpers should make it easy to:

- display story metadata (time ranges, entities, places),
- render citation references consistently and accessibly,
- avoid “uncited” or ambiguous output (e.g., unlabeled AI insight blocks).

### Citation rendering note

Story Nodes are written in Markdown with citation markers in a `【…†Lx-Ly】` style, and the frontend should render these with special care (Markdown parse + citation token handling). *(Exact parsing approach depends on the chosen Markdown library — not confirmed in repo.)*

Suggested utilities *(not confirmed in repo)*:

- `isCitationToken(str: string): boolean`
- `parseCitationToken(token: string): { sourceId: string; lineStart: number; lineEnd: number } | null`
- `formatCitationLabel(parsed): string`

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Typecheck: formatting APIs are typed; avoid `any` in public exports.
- [ ] Unit tests: deterministic outputs across environments.
- [ ] Lint: consistent naming; no unused exports.
- [ ] Dependency review: avoid heavy date/format libraries unless justified.

### Reproduction (deterministic)

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run unit tests
# npm test

# 2) typecheck
# npm run typecheck

# 3) lint
# npm run lint
~~~

### Telemetry signals (optional)

| Signal | Source | Where recorded |
|---|---|---|
| `ui_redaction_notice_shown` | UI | `docs/telemetry/` + `schemas/telemetry/` *(if present)* |
| `ui_citation_interaction` | UI | same |

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers (UI-facing)

- Introducing a new formatter that could reveal restricted details (e.g., coordinates, small-area aggregations).
- Changing provenance/citation rendering in a way that weakens evidence visibility or auditability.

### CARE considerations

If formatted UI output involves culturally sensitive knowledge or Indigenous data:

- follow redaction/generalization guidance,
- avoid implying authority-to-control where it is not warranted,
- never display sensitive location precision in public views.

---

## 🕰️ Version History

| Version | Date | Change summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-26 | Initial README establishing formatting utilities conventions | TBD | TBD |

---

### Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

