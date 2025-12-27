---
title: "Kansas Frontier Matrix — Web UI"
path: "web/README.md"
version: "v1.2.0"
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

doc_uuid: "urn:kfm:doc:web:readme:v1.2.0"
semantic_document_id: "kfm-web-readme-v1.2.0"
event_source_id: "ledger:kfm:doc:web:readme:v1.2.0"
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

`web/` is the canonical home for KFM’s **user-facing map + narrative UI**, including **Focus Mode** experiences (React + map renderer such as MapLibre/Cesium, repo-specific).

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

> **Repo reality check (v13-forward):** This README follows KFM’s “one canonical home per subsystem” rule. If a path referenced here does not exist in your checkout, treat it as **not confirmed in repo** and **do not create a duplicate**; instead, fix the link/README or file a ticket to align the repo to canonical homes.

## UI non‑negotiables (contract + governance)

- **API boundary is mandatory:** the UI consumes graph + catalog content **only via contracted APIs and/or catalog endpoints**. The UI **must not** connect to Neo4j/graph storage directly.
- **Layer registries are contract artifacts:** layer registries **must** validate against `schemas/ui/` (if present). Don’t ship “best-effort” layer configs.
- **Focus Mode is provenance-only by default:** Focus Mode **must not** surface unsourced narrative. Predictive/AI content (if any) must be **opt‑in**, clearly labeled, and carry uncertainty/confidence metadata.
- **No client-side reconstruction of sensitive locations:** never infer, re-join, or “zoom-reveal” restricted sites from partial coordinates. Treat API redaction/generalization as authoritative.
- **Untrusted content handling:** Story Node markdown and any remote content must be treated as untrusted input (sanitize; prevent script injection).
- **A11y is a release gate:** Focus Mode and citation UX must be keyboard-first and screen-reader compatible.
- **Telemetry (if enabled) must be schema-governed:** no ad-hoc event shapes; never emit PII or precise sensitive coordinates.

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
| UI testing, accessibility, performance budgets, and UI telemetry hooks (if implemented) | API contract definition/enforcement (`src/server/`) |

### Audience

- Primary: frontend engineers working in `web/`.
- Secondary: API engineers validating UI→API contracts; curators working on Story Nodes; reviewers for governance/a11y.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — if missing, add or link to the canonical glossary location)*

Terms used in this doc:

- **Story Node** — governed narrative artifact (v3) rendered by the UI and used in Focus Mode.
- **Focus Mode** — provenance-first deep-dive view that must not present unsourced narrative.
- **Layer registry** — schema-validated configuration describing map layers, sources, attribution, and sensitivity flags.
- **Evidence artifacts** — STAC/DCAT/PROV products referenced by the UI for traceability and audit.
- **Focus context bundle** — contracted API response that packages narrative + evidence references + policy flags for Focus Mode.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical homes + “no mystery duplicates” rule |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Required structure for Story Nodes |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Governed headings + front-matter expectations |
| API boundary | `src/server/` | TBD | Contracted access; redaction; provenance linking |
| API contracts | `src/server/contracts/` | TBD | UI must consume; no direct graph reads *(if present)* |
| UI schemas | `schemas/ui/` | TBD | Layer registry schema validation *(if present)* |
| Story Nodes | `docs/reports/story_nodes/` | TBD | Published narrative content consumed by UI *(if present)* |
| Security docs | `.github/SECURITY.md` + `docs/security/` | TBD | Threat model + security standards *(paths not confirmed in repo)* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] “Non-negotiables” reflect current KFM invariants (API boundary, provenance-first, no leakage)
- [ ] All referenced paths are either canonical or clearly marked “not confirmed in repo”
- [ ] Validation steps listed and repeatable (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No instructions imply prohibited AI actions (e.g., inferring sensitive locations)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/README.md` (must match front-matter)

### Repo top-levels (expected)

~~~text
.github/
data/
docs/
mcp/
schemas/
src/
tests/
tools/
web/
releases/
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs (domain-scoped) |
| Catalogs (v13-forward) | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC Items/Collections, DCAT datasets, PROV bundles |
| Graph | `src/graph/` + `data/graph/` | Ontology-governed ingest + import artifacts |
| API boundary | `src/server/` | Contracted access, redaction, provenance linking |
| Schemas | `schemas/` | JSON Schemas for catalogs, Story Nodes, UI registries |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts consumed by UI *(if present)* |
| Frontend | `web/` | This directory |
| Telemetry (optional) | `docs/telemetry/` + `schemas/telemetry/` | Observability & governance metrics *(if present)* |

### Start here (repo-specific)

If you’re new to KFM UI work, read in this order:

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

### Expected file tree for this sub-area

This is a **target / typical** layout. Update it if the repo differs.

~~~text
📁 web/
├─ 📄 README.md
├─ 📄 package.json                      # if present (build + dev scripts)
├─ 📁 public/                           # if present (static assets)
├─ 📁 src/                              # if present (UI source)
│  ├─ 📁 api/                           # API client + contract bindings
│  ├─ 📁 app/                           # routing/state shell (repo-specific)
│  ├─ 📁 map/                           # map runtime (MapLibre/Cesium/other)
│  ├─ 📁 story/                         # Story Node rendering + citations
│  ├─ 📁 focus/                         # Focus Mode UI state + components
│  ├─ 📁 layers/                        # runtime layer registry loader (code)
│  ├─ 📁 ui/                            # shared UI components
│  └─ 📁 telemetry/                     # optional (event emitters; schema-governed)
└─ 📁 layers/                           # layer registries (config) — choose one canonical location
~~~

---

## 🧭 Context

### What’s driving the next evolution

- Scaling: more domains, more evidence products, more narrative interactivity.
- Governance: stronger provenance + sovereignty enforcement as content grows.
- Contracts: schemas + API contracts become first-class artifacts (reviewed like code).

### Key invariants

- **No unsourced narrative in Focus Mode contexts.**
- **Provenance is first-class** (STAC/DCAT/PROV and graph lineage).
- **Reproducibility and deterministic pipelines** are expected upstream; UI should not “paper over” missing provenance.
- **One canonical home per subsystem** — avoid duplicate folders/configs that drift over time.

### Extension Matrix mindset (when UI work is required)

Adding a capability often touches multiple pipeline stages. Use this as a sanity check:

- New dataset: UI changes **optional** (unless it must be visible in map/Focus Mode).
- New analysis/evidence product: UI changes **often required** to surface provenance responsibly.
- New narrative node type: UI + Focus Mode changes **often required**.

When in doubt: prefer a **vertical slice** (dataset → catalogs → graph → API → UI layer → one published Story Node) over UI-only features that lack provenance and contracts.

---

## 🗺️ Diagrams

### System and dataflow (canonical ordering)

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
| Layer registry | JSON/TS | `web/**/layers/**` | Validate against `schemas/ui/` |
| Story Nodes | Markdown | `docs/reports/story_nodes/**` | Story Node schema + lint |
| Evidence references | IDs/URLs | STAC/DCAT/PROV artifacts | Broken-link + ID integrity checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Web bundle | static build | repo-specific build output | CI build + a11y gates |
| UI telemetry (optional) | JSON events | repo-specific | `schemas/telemetry/` (if present) |

### Sensitivity & redaction

- Treat API-delivered redaction/generalization as authoritative.
- Do not log PII or sensitive coordinates in client telemetry.
- Avoid caching sensitive content in persistent client storage unless governance-approved.

### Quality signals

- Contract adherence (no breaking changes without versioning).
- Layer registry schema validation.
- Citation UX correctness (inspectable evidence IDs; consistent audit panel).
- Accessibility baseline (keyboard navigation, focus management, readable citations).
- Performance budgets (layer load, Focus Mode time-to-interactive).
- Security hygiene (sanitization; no injection; safe handling of external assets).

### Data lifecycle (required staging)

Upstream lifecycle is expected to follow:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ reports/derived outputs as needed)

The UI should consume **published/contracted** representations (API + catalogs), not raw/work artifacts.

---

## 🌐 STAC, DCAT & PROV Alignment

The UI should make provenance **visible and inspectable**, not implicit.

### STAC

- The UI must be able to reference:
  - STAC Collection identifiers (collection-level provenance + metadata)
  - STAC Item identifiers (feature/asset-level provenance + metadata)
- Layer UX should surface attribution/license from STAC assets where applicable.

### DCAT

- The UI should surface dataset-level metadata:
  - dataset identifiers
  - license and publisher/contact mapping
  - keywords/description for discovery and user context

### PROV-O

- The UI should expose lineage cues for auditability:
  - `prov:wasDerivedFrom` (source identifiers)
  - `prov:wasGeneratedBy` (pipeline activity/run identifier)
  - agent/tool identities when relevant (human curator vs pipeline vs model)

### Versioning

- New versions should link predecessor/successor in catalogs; UI should handle versioned evidence gracefully (show “superseded” if applicable).
- Graph and API responses should mirror version lineage; UI should not “merge” versions silently.

If a UI view lacks evidence identifiers, it must present a **missing provenance** state rather than implying certainty.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| API client | Typed calls to API contracts | REST/GraphQL (repo-specific) |
| Map runtime | Render layers + interactions | Layer registry + API data |
| Story Node renderer | Render narrative + citations | Story Node v3 structure |
| Focus Mode | Provenance-first deep-dive view | Focus “context bundle” payload |
| Layer registry loader | Load/validate layer configs | `schemas/ui/` |
| Telemetry (optional) | Emit governance-safe UX signals | `schemas/telemetry/` |

### Subsystem contracts (do not break)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no unsourced narrative |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog (if adopted) |
| API contracts | `src/server/contracts/` | Contract tests required |
| Story Node schema/template | `docs/templates/` (+ schemas if present) | Must validate before publish |
| Layer registry schema | `schemas/ui/` | Must validate before UI build |

### Extension points checklist (for future work)

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
- Story Nodes should link to:
  - graph entity IDs,
  - STAC/DCAT/PROV evidence IDs,
  - local assets with attribution.

### How this work surfaces in Focus Mode

- What entities become focusable (entity/story selection)?
- What evidence must be shown (IDs + resolvable references)?
- What warnings must be shown (missing provenance, redaction notices, version superseded)?

### Focus Mode rule (provenance-only by default)

- Focus Mode only consumes provenance-linked content.
- Any predictive/AI-generated content must be:
  - opt-in,
  - visibly labeled,
  - accompanied by uncertainty/confidence metadata,
  - never used to infer sensitive locations.

### Optional structured controls

These controls may be provided by Story Node metadata and/or the Focus context bundle:

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

### Minimum CI gates (expected)

- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry/UI registries as applicable)
- Graph integrity tests (as applicable to the change)
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)
- Accessibility checks (keyboard navigation, reduced motion, readable citations)

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
| focus_mode_opened | UI | `schemas/telemetry/` + `docs/telemetry/` (if present) |
| layer_load_timing | UI | `schemas/telemetry/` + `docs/telemetry/` (if present) |
| focus_mode_redaction_notice_shown | UI | `schemas/telemetry/` + `docs/telemetry/` (if present) |

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

---

Footer refs (do not remove):

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
