---
title: "Kansas Frontier Matrix — Web UI"
path: "web/README.md"
version: "v1.2.1"
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

doc_uuid: "urn:kfm:doc:web:readme:v1.2.1"
semantic_document_id: "kfm-web-readme-v1.2.1"
event_source_id: "ledger:kfm:doc:web:readme:v1.2.1"
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

# Kansas Frontier Matrix — Web UI

`web/` is the canonical home for KFM’s **user-facing map + narrative UI**, including **Focus Mode** experiences (React + a map renderer such as MapLibre/Cesium; repo-specific).

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV catalogs → Graph → API boundary → UI → Story Nodes → Focus Mode**

Quick links (canonical or expected; treat missing paths as *not confirmed in repo*):

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template v3: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contracts: `src/server/contracts/` *(if present)*
- UI schemas: `schemas/ui/` *(if present)*

> **Repo reality check (v13-forward):** KFM follows “one canonical home per subsystem.” If a path referenced here does not exist in your checkout, treat it as **not confirmed in repo** and **do not create a duplicate**. Fix the link, or open a ticket to align the repo to the canonical homes.

## UI non‑negotiables (contract + governance)

- **API boundary is mandatory:** the UI consumes graph + catalog content **only via contracted APIs and/or catalog endpoints**. The UI **must not** connect to Neo4j/graph storage directly.
- **No ad‑hoc data:** if a UI feature needs additional data, the correct fix is to extend the **ETL/catalogs/graph/API**—not to hard-code data or scrape sources in the UI.
- **Layer registries are contract artifacts:** layer registries **must** validate against `schemas/ui/` *(if present)*. Do not ship “best-effort” layer configs.
- **Focus Mode is provenance-first by default:** Focus Mode must not surface unsourced narrative. Predictive/AI content (if any) must be **opt‑in**, clearly labeled, and carry uncertainty/confidence metadata.
- **No client-side reconstruction of sensitive locations:** never infer, re-join, or “zoom‑reveal” restricted sites from partial coordinates. Treat API redaction/generalization as authoritative.
- **Untrusted content handling:** Story Node markdown and any remote content must be treated as untrusted input (sanitize; prevent script injection).
- **A11y is a release gate:** map interactions, Focus Mode, and citations must be keyboard-first and screen-reader compatible.
- **Telemetry (if enabled) is schema-governed:** no ad-hoc event shapes; never emit PII or precise sensitive coordinates.

---

## 📘 Overview

### Purpose

- Define what belongs in `web/` and how the Web UI participates in the canonical KFM pipeline.
- Make UI invariants **explicit, reviewable, and testable** (API boundary, provenance visibility, Focus Mode rules, layer registry schema validation).

### Scope

| In Scope | Out of Scope |
|---|---|
| Front-end application code under `web/` (map runtime, timelines, Story Node rendering, Focus Mode UI state) | ETL/pipelines (`src/pipelines/`) |
| UI layer registries + UI-specific schemas/validation hooks | Catalog generation implementations (owned by pipelines) |
| UI-side contract consumption (API clients, request/response typing, caching policy) | Graph build/migrations (`src/graph/`) |
| UI testing, accessibility, performance budgets, and telemetry hooks (if implemented) | API contract definition/enforcement (`src/server/`) |

### Audience

- Primary: frontend engineers working in `web/`.
- Secondary: API engineers validating UI→API contracts; curators working on Story Nodes; reviewers for governance/a11y.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(expected; if missing, treat as not confirmed in repo and do not fork duplicates)*

Key terms used in this document:

- **Story Node** — governed narrative artifact (v3) rendered by the UI and used in Focus Mode.
- **Focus Mode** — provenance-first deep-dive experience that must not present unsourced narrative.
- **Layer registry** — schema-validated configuration describing map layers, sources, attribution, and sensitivity flags.
- **Evidence artifacts** — STAC/DCAT/PROV products referenced by the UI for traceability and audit.
- **Focus context bundle** — contracted API response that packages narrative + evidence references + policy flags for Focus Mode.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical homes + contract-first discipline |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Required structure for Story Nodes |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default governed doc structure |
| API boundary | `src/server/` | TBD | Contracted access; redaction; provenance linking |
| API contracts | `src/server/contracts/` | TBD | UI must consume; no direct graph reads *(if present)* |
| UI schemas | `schemas/ui/` | TBD | Layer registry schema validation *(if present)* |
| Story Nodes | `docs/reports/story_nodes/` | TBD | Published narrative content consumed by UI *(if present)* |
| Governance docs | `docs/governance/` | TBD | ROOT_GOVERNANCE + ETHICS + SOVEREIGNTY *(paths expected by template)* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Non-negotiables reflect current KFM invariants (API boundary, provenance-first, no leakage)
- [ ] All referenced paths are either canonical or clearly marked “not confirmed in repo”
- [ ] Validation steps listed and repeatable (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No instructions imply prohibited AI actions (e.g., inferring sensitive locations)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/README.md` *(must match front-matter)*

### Related repository paths (canonical homes)

| Area | Path | What lives here |
|---|---|---|
| Data domains + catalogs | `data/` | `raw/ → work/ → processed/`, plus STAC/DCAT/PROV outputs |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Published metadata products the UI can reference |
| Graph | `src/graph/` + `data/graph/` | Ontology-governed ingest + import artifacts |
| API boundary | `src/server/` | Contracted access, redaction, provenance linking |
| Schemas | `schemas/` | JSON Schemas for catalogs, Story Nodes, UI registries |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts consumed by UI *(if present)* |
| Frontend | `web/` | This directory |
| MCP runs/experiments | `mcp/` | Runs, experiments, model cards, SOPs *(if present)* |

### Repo top-levels (expected)

~~~text
📁 .github/
├── 📁 workflows/
└── 📄 SECURITY.md                         # if present

📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📄 glossary.md                         # if present
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md    # if present
│   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md # if present
└── 📁 reports/
    └── 📁 story_nodes/                    # if present

📁 mcp/
├── 📁 runs/                               # if present
└── 📁 experiments/                        # if present

📁 schemas/
📁 src/
├── 📁 pipelines/
├── 📁 graph/
└── 📁 server/
📁 tests/
📁 tools/
📁 web/
└── 📄 README.md                           # this file
📁 releases/                               # if used
~~~

### Start here (recommended reading order)

1) `docs/MASTER_GUIDE_v12.md` — canonical pipeline + invariants  
2) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — canonical homes + v13 readiness  
3) `docs/templates/TEMPLATE__STORY_NODE_V3.md` — Story Node structure consumed by UI  
4) `src/server/contracts/` — API contracts the UI must consume *(if present)*  
5) `schemas/ui/` — layer registry schemas *(if present)*  
6) `docs/reports/story_nodes/` — Story Nodes rendered in Focus Mode *(if present)*

### Quickstart (repo-specific)

Commands and tooling are repo-specific. Prefer `web/package.json` scripts if present.

~~~bash
# Placeholders — replace with repo-approved tooling defined in web/package.json.

# cd web
# <install deps>         # e.g., npm ci / pnpm i / yarn
# <run dev server>       # e.g., npm run dev
# <run unit tests>       # e.g., npm test
# <run e2e tests>        # e.g., npm run e2e
# <validate registries>  # schema validation for layer registries (if wired)
~~~

### Typical `web/` sub-tree (update if repo differs)

~~~text
📁 web/
├── 📄 README.md
├── 📄 package.json                      # if present (build + dev scripts)
├── 📁 public/                           # if present (static assets)
├── 📁 src/                              # if present (UI source)
│   ├── 📁 api/                          # API client + contract bindings
│   ├── 📁 app/                          # routing/state shell (repo-specific)
│   ├── 📁 map/                          # map runtime (MapLibre/Cesium/other)
│   ├── 📁 story/                        # Story Node rendering + citations
│   ├── 📁 focus/                        # Focus Mode UI state + components
│   ├── 📁 layers/                       # runtime layer registry loader (code)
│   ├── 📁 ui/                           # shared UI components
│   └── 📁 telemetry/                    # optional (schema-governed event emitters)
└── 📁 layers/                           # layer registries (config) — choose one canonical location
~~~

---

## 🧭 Context

### What the Web UI is responsible for

- Rendering interactive maps and narrative experiences backed by KFM’s governed evidence.
- Making provenance **inspectable** (citations, dataset IDs, lineage cues, redaction notices).
- Staying strictly within the API boundary: the UI is a contract consumer, not a graph client.

### What’s driving the next evolution (v13-forward)

- Scaling: more domains, more evidence products, richer narrative interactivity.
- Governance: stronger provenance + sovereignty enforcement as content grows.
- Contracts: schemas + API contracts become first-class artifacts (reviewed like code).

### Key invariants (do not weaken in PRs)

- **No direct graph access from the browser.**
- **No unsourced narrative in Story Nodes or Focus Mode.**
- **No ad‑hoc data in the UI (extend upstream; don’t hard-code).**
- **Schema validation for layer registries is mandatory (if schemas exist).**
- **Redaction/generalization decisions are enforced at the API boundary and respected in UI.**
- **Accessibility is not optional.**

### “Vertical slice” mindset (recommended)

When in doubt, implement capabilities as a small vertical slice:

- dataset → catalogs (STAC/DCAT/PROV) → graph links → API contract → UI layer/view → one published Story Node

This avoids UI-only features that lack evidence, contracts, and governance review.

### Common UI change types

| Change | Usually requires | Notes |
|---|---|---|
| Add a new map layer | Layer registry entry + API endpoint/cached tiles + attribution | Validate registry schema; include sensitivity flags |
| Add a Focus Mode panel | API contract addition + UI component + a11y | Must include evidence IDs + redaction notices |
| Add a new Story Node type | Story Node schema/template change + UI renderer update | Requires doc + schema review; likely governance review |
| Add AI-assisted feature | Opt-in controls + uncertainty metadata + governance review | Must not infer sensitive locations; label inference clearly |

### PR “vertical slice” checklists (copy/paste into PR description)

#### Add or change a map layer

- [ ] Upstream evidence exists and is referenced (STAC/DCAT/PROV IDs or resolvable links)
- [ ] API/cat endpoint exists (or contract change included) and enforces redaction/generalization
- [ ] Layer registry updated with:
  - [ ] stable `layer_id` (no reuse for different meaning)
  - [ ] attribution + license surfaced in UI
  - [ ] sensitivity/classification flags set
- [ ] Layer registry validates against `schemas/ui/` *(if present)*
- [ ] UI interaction is keyboard accessible and screen-reader safe (where applicable)
- [ ] No client logs include sensitive coordinates/PII
- [ ] Tests updated (unit + minimal e2e smoke)

#### Add or change a Focus Mode panel/view

- [ ] API contract provides a provenance-linked context bundle (IDs + flags)
- [ ] UI renders explicit missing-provenance and redaction states
- [ ] Any AI/predictive content is opt-in + labeled + has uncertainty metadata
- [ ] Citation UX is keyboard-first and copyable (IDs)
- [ ] Telemetry (if enabled) is schema-governed and does not emit PII

---

## 🗺️ Diagrams

### System dataflow (canonical ordering)

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph + data/graph"]
  C --> D["API boundary — src/server + contracts"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked only"]
~~~

### Focus Mode request sequence (contract-first)

~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API Boundary
  participant Graph as Graph + Catalogs

  UI->>API: Focus query(entity_id, options)
  API->>Graph: fetch subgraph + evidence refs (STAC/DCAT/PROV IDs)
  Graph-->>API: context bundle + provenance identifiers
  API-->>UI: contracted payload (narrative + citations + flags)
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API responses | JSON | `src/server/` endpoints | Contract tests + runtime guards |
| Catalog endpoints | JSON | STAC/DCAT/PROV outputs | Schema validation + link integrity |
| Layer registry | JSON/TS | `web/**/layers/**` | Validate against `schemas/ui/` *(if present)* |
| Story Nodes | Markdown | `docs/reports/story_nodes/**` | Story Node schema + lint *(if present)* |
| Evidence references | IDs/URLs | STAC/DCAT/PROV artifacts | Broken-link + ID integrity checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Web bundle | static build | repo-specific build output | CI build + a11y gates |
| UI telemetry (optional) | JSON events | repo-specific | `schemas/telemetry/` *(if present)* |

### Provenance alignment (STAC, DCAT, PROV)

The UI must make provenance visible and inspectable (never implicit).

#### STAC expectations

- UI views should be able to reference:
  - STAC Collection IDs (collection-level provenance + metadata)
  - STAC Item IDs (feature/asset-level provenance + metadata)
- Layer UX should surface attribution/license from STAC assets where applicable.

#### DCAT expectations

- UI should surface dataset-level metadata when relevant:
  - dataset identifiers
  - license and publisher/contact mapping
  - keywords/description for discovery and user context

#### PROV-O expectations

- UI should expose lineage cues for auditability:
  - `prov:wasDerivedFrom` (source identifiers)
  - `prov:wasGeneratedBy` (pipeline activity/run identifier)
  - agent/tool identities when relevant (human curator vs pipeline vs model)

If a UI view lacks evidence identifiers, it must present a **missing provenance** state rather than implying certainty.

### Sensitivity & redaction

- Treat API-delivered redaction/generalization as authoritative.
- Do not log PII or sensitive coordinates in client telemetry.
- Avoid caching sensitive content in persistent client storage unless governance-approved.

### Versioning expectations

- New versions should link predecessor/successor in catalogs; UI should handle versioned evidence gracefully (show “superseded” if applicable).
- Graph and API responses should mirror version lineage; UI should not merge versions silently.

---

## 🧱 Architecture

### Major components (UI)

| Component | Responsibility | Interface |
|---|---|---|
| API client | Typed calls to API contracts | REST/GraphQL (repo-specific) |
| Map runtime | Render layers + interactions | Layer registry + API data |
| Story Node renderer | Render narrative + citations | Story Node v3 structure |
| Focus Mode | Provenance-first deep-dive view | Focus “context bundle” payload |
| Layer registry loader | Load/validate layer configs | `schemas/ui/` *(if present)* |
| Telemetry (optional) | Emit governance-safe UX signals | `schemas/telemetry/` *(if present)* |

### Subsystem contracts (do not break)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation notes | deterministic + replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated outputs |
| Graph | ontology + migrations + constraints | stable labels/edges (unless migrated) |
| APIs | OpenAPI/GraphQL schema + contract tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story/Focus | provenance-linked context bundle | no unsourced claims |

### Layer registries (configuration as contract)

Layer registries are not “nice to have” config files—they are contract artifacts. At minimum, each registry must support:

- provenance pointers (STAC/DCAT/PROV identifiers or resolvable references)
- attribution and licensing display
- sensitivity/classification flags
- stable layer identifiers (do not reuse IDs for different meaning)

Do not guess fields: validate against `schemas/ui/` *(if present)* and treat schema as source of truth.

### Untrusted content and sanitization

Any markdown or remote content rendered in the UI must be treated as untrusted input:

- sanitize HTML/markdown rendering (no script injection)
- block unsafe links/embeds where required by governance
- do not “enhance” redacted data client-side (no join/zoom reconstruction)

### Extension points checklist (for adding capability)

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules + attribution + sensitivity flags
- [ ] Focus Mode: provenance references enforced and visible
- [ ] Telemetry: new signals + schema version bump (if telemetry is enabled)

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

- Story Nodes are governed Markdown artifacts consumed by the UI.
- Story Nodes must link to:
  - graph entity IDs,
  - STAC/DCAT/PROV evidence IDs,
  - local assets with attribution.
- Story Nodes must separate **fact vs inference vs hypothesis** where applicable.

### Focus Mode behavior expectations

Focus Mode should make it obvious:

- what entity is in focus (stable ID + canonical name),
- what evidence supports the view (copyable IDs + resolvable links),
- what is missing (explicit missing provenance state),
- what is redacted/generalized (clear notice + reason/category where allowed).

### Provenance-only rule (hard gate)

- Focus Mode consumes only provenance-linked content.
- Any predictive/AI-generated content must be:
  - opt-in,
  - visibly labeled,
  - accompanied by uncertainty/confidence metadata,
  - never used to infer sensitive locations.

### Optional structured controls (from Story Nodes or Focus context bundle)

~~~yaml
focus_layers:
  - "TBD:layer_id"
focus_time: "TBD:YYYY or YYYY-MM-DD/YYYY-MM-DD"
focus_center: [-98.0000, 38.0000] # lon, lat (example only)
~~~

### Citation rendering expectations (UI)

- Citations must be navigable by keyboard and screen readers.
- Evidence identifiers must be copyable.
- Provide a consistent “audit panel” affordance for:
  - provenance links,
  - sensitivity/redaction notices,
  - missing provenance warnings.

---

## 🧪 Validation & CI/CD

### CI behavior contract

- **Validate if present:** if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid:** schema errors, missing links, orphan references fail deterministically.
- **Skip if not applicable:** optional roots absent → skip without failing the overall pipeline.

### Validation steps (minimum expectations)

- [ ] Markdown protocol validation (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers)
- [ ] JSON schema validation (as applicable):
  - STAC/DCAT/PROV
  - Story Node schemas (if present)
  - Telemetry schemas (if present)
  - UI layer registry schemas (if present)
- [ ] API contract tests (OpenAPI/GraphQL schema + resolver tests)
- [ ] UI unit tests + basic e2e smoke tests
- [ ] Accessibility checks (keyboard navigation, reduced motion, readable citations)
- [ ] Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Local reproduction

~~~bash
# Placeholders — replace with repo-specific commands defined in web/package.json (if present)

# 1) install deps
# 2) run lint
# 3) run unit tests
# 4) run e2e smoke tests
# 5) validate layer registry schema
~~~

### Telemetry signals (optional)

| Signal | Source | Where recorded |
|---|---|---|
| focus_mode_opened | UI | `schemas/telemetry/` + `docs/telemetry/` *(if present)* |
| layer_load_timing | UI | `schemas/telemetry/` + `docs/telemetry/` *(if present)* |
| focus_mode_redaction_notice_shown | UI | `schemas/telemetry/` + `docs/telemetry/` *(if present)* |

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

UI changes that typically require elevated review:

- Adding new sensitive layers (restricted locations, cultural knowledge, PII, etc.)
- Introducing/changing AI-generated narrative behavior visible to users
- Adding new external data sources (as surfaced in UI)
- Adding new public-facing endpoints or share links

### CARE / sovereignty considerations

- Identify communities impacted and protection rules.
- Use generalization/redaction for restricted locations (enforced at the API boundary).
- Ensure sensitive assets (images/docs) follow review gates before publication.

### AI usage constraints (UI)

If the UI renders predictive/AI-generated content:

- it must be opt-in,
- must show uncertainty/confidence metadata,
- must not appear as unmarked fact,
- must not be used to infer sensitive locations.

### Governance approvals required (if any)

- FAIR+CARE council review: TBD
- Security council review: TBD
- Historian/editor review: TBD

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/README.md` | TBD |
| v1.0.1 | 2025-12-24 | Clarified layer registry contract pattern; strengthened Focus Mode provenance + audit expectations; aligned directory language to canonical homes | TBD |
| v1.1.0 | 2025-12-27 | Aligned to Universal governed-doc structure; tightened UI invariants (API-only, registry schema validation, provenance-only Focus Mode); added CI behavior contract + checklists | TBD |
| v1.2.0 | 2025-12-27 | Re-structured for v13-forward “one canonical home” discipline; clarified contract-first UI responsibilities; tightened provenance/a11y/security language; reduced repo-guessing via “not confirmed in repo” patterns | TBD |
| v1.2.1 | 2025-12-28 | Editorial pass: reduced duplication, clarified “no ad‑hoc data” rule, tightened checklists and contract language | TBD |

---

Footer refs (do not remove):

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
