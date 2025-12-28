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

`web/` is the canonical home for KFM’s **user-facing map + narrative application** (React + a map renderer such as MapLibre/Cesium; repo-specific).

**Canonical pipeline ordering (non-negotiable):**  
**ETL → STAC/DCAT/PROV catalogs → Graph → API boundary → UI → Story Nodes → Focus Mode**

## ✅ UI invariants at a glance

- **API boundary is mandatory:** the UI consumes graph + catalog content **only via contracted APIs and/or published catalog endpoints**. The UI **must not** connect to Neo4j/graph storage directly.
- **No ad-hoc data in UI:** if a UI feature needs additional data, extend **ETL/catalog/graph/API**—do not hard-code new datasets or scrape sources in the browser.
- **Provenance-first rendering:** every story paragraph, statistic, layer, or highlight must have a traceable evidence identifier (STAC/DCAT/PROV + graph IDs where applicable). Missing evidence ⇒ show a “missing provenance” state.
- **Layer registries are contract artifacts:** registries must validate against `schemas/ui/` (if present). No “best-effort” parsing.
- **Focus Mode is provenance-only:** opt-in AI/predictive content must be labeled and include uncertainty metadata; never infer sensitive locations.
- **Security + sovereignty:** treat markdown as untrusted input; sanitize; respect API redaction/generalization; never reconstruct restricted locations client-side.
- **Accessibility is a release gate:** keyboard-first + screen-reader compatible map interactions, Focus Mode, and citations.
- **Telemetry (if enabled) is schema-governed:** never emit PII or precise sensitive coordinates.

## 🔗 Quick links (canonical or expected)

Treat missing paths as **not confirmed in repo** and **do not create duplicates**.

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template v3: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- API boundary: `src/server/` (contracts under `src/server/contracts/**` if present)
- UI schemas: `schemas/ui/` (if present)
- Story Nodes: `docs/reports/story_nodes/` (if present)
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` (if present)

> **Repo reality check (v13-forward):** KFM follows “one canonical home per subsystem.” If a path referenced here does not exist in your checkout, treat it as **not confirmed in repo** and avoid creating duplicates. Fix the link, or open a ticket to align the repo to canonical homes.

---

## 📘 Overview

### Purpose

- Define what belongs in `web/` and how the Web UI participates in the canonical KFM pipeline.
- Make UI invariants **explicit, reviewable, and testable** (API boundary, provenance visibility, Focus Mode rules, layer registry schema validation).

### Scope

| In Scope | Out of Scope |
|---|---|
| Front-end application code under `web/` (map runtime, timelines, Story Node rendering, Focus Mode UI) | ETL / catalog generation (`src/pipelines/`) |
| UI layer registries + UI-side schema validation hooks | Graph build/migrations (`src/graph/`) |
| UI-side contract consumption (API clients, request/response typing, caching policy) | API contract definition/enforcement (`src/server/`) |
| UI testing, accessibility, performance budgets, telemetry hooks (if implemented) | Governance policy authoring (see `docs/governance/`) |

### Audience

- Primary: frontend engineers working in `web/`.
- Secondary: API engineers validating UI→API contracts; curators working on Story Nodes; reviewers for governance/a11y.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(expected; if missing, treat as not confirmed in repo)*

Key terms used in this doc:

- **Story Node** — governed narrative artifact (v3), machine-ingestible, provenance-linked.
- **Focus Mode** — provenance-first deep-dive view; consumes only provenance-linked context bundles.
- **Layer registry** — schema-validated configuration describing map layers/sources/attribution/sensitivity.
- **Evidence artifacts** — STAC/DCAT/PROV products referenced by the UI for traceability and audit.
- **Context bundle** — contracted API payload for Focus Mode (narrative + citations + flags + map/timeline payload).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical homes + contract-first discipline |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Required structure for Story Nodes |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default governed doc structure |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | Use for REST/GraphQL contract changes |
| UI schemas | `schemas/ui/` | TBD | Layer registry schema validation *(if present)* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Canonical pipeline + UI invariants are stated and testable
- [ ] All referenced paths are canonical or explicitly marked “not confirmed in repo”
- [ ] Validation steps listed and repeatable (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations stated (redaction, sensitivity, telemetry)
- [ ] No instructions imply prohibited AI actions (e.g., inferring sensitive locations)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/README.md` *(must match front-matter)*

### Related repository paths (canonical homes)

| Area | Path | What lives here |
|---|---|---|
| Data lifecycle | `data/` | `raw/ → work/ → processed/` (domain modules) |
| Metadata catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV outputs |
| Graph import artifacts | `data/graph/csv/` + `data/graph/cypher/` | Graph import exports + optional scripts |
| Pipelines | `src/pipelines/` | ETL + catalog generation + validation |
| Graph build | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | Contracted access + redaction/generalization |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts consumed by UI *(if present)* |
| Frontend | `web/` | This directory |
| MCP | `mcp/` | Runs, experiments, model cards, SOPs *(if present)* |

### Expected file tree for this sub-area (update if repo differs)

~~~text
📁 web/
├── 📄 README.md
├── 📄 package.json                          # if present
├── 📁 public/                               # if present
├── 📁 src/                                  # if present
│   ├── 📁 api/                              # API client + contract bindings
│   ├── 📁 app/                              # routing + app shell (repo-specific)
│   ├── 📁 map/                              # map runtime (MapLibre/Cesium/other)
│   ├── 📁 story/                            # Story Node rendering + citations
│   ├── 📁 focus/                            # Focus Mode panels + sync logic
│   ├── 📁 layers/                           # registry loader/validators (code)
│   ├── 📁 ui/                               # shared UI components
│   └── 📁 telemetry/                        # optional (schema-governed emitters)
└── 📁 layers/                               # optional: layer registries (config); choose one canonical location
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

---

## 🧭 Context

### Background

KFM’s Web UI is the presentation layer for evidence-backed mapping + narratives. It renders:

- map layers backed by cataloged evidence and governed sensitivity rules
- Story Nodes as “machine-ingestible storytelling”
- Focus Mode as a deep-dive view that packages narrative + citations + context (map + timeline) into one experience

### Assumptions

- Story content shown to users is curator-reviewed, provenance-linked, and versioned as repository artifacts and/or API-served equivalents.
- Redaction/generalization decisions are enforced at the API boundary and must be respected by the UI (no client-side “reconstruction”).
- Layer definitions are expressed as registries/config (not scattered hard-coded layer definitions).

### Constraints / invariants (do not weaken in PRs)

- Preserve ordering: **ETL → STAC/DCAT/PROV → Graph → API boundary → UI → Story Nodes → Focus Mode**
- **No direct graph/Neo4j access from the browser**; the UI is a contract consumer (APIs + catalogs).
- **No ad-hoc data in UI**: extend upstream, don’t hard-code.
- **Focus Mode is provenance-only**: missing evidence ⇒ explicit “missing provenance” state.
- **Registry schemas are mandatory if present** (`schemas/ui/`, `schemas/telemetry/`).
- **Markdown is untrusted input**: sanitize before rendering; prevent script injection.
- **A11y is a release gate** (keyboard-first + screen-reader compatible citations).
- **Telemetry is governed** (if enabled): no PII, no precise sensitive coordinates.

### Working mode (recommended): vertical slice

When in doubt, implement capability as a small vertical slice:

- dataset → catalogs (STAC/DCAT/PROV) → graph links → API contract → UI layer/view → one published Story Node

This avoids UI-only features that lack evidence, contracts, and governance review.

### Common UI change types

| Change | Usually requires | Notes |
|---|---|---|
| Add a new map layer | Layer registry entry + API endpoint/tiles + attribution | Validate registry schema; include sensitivity flags |
| Add a Focus Mode panel | API contract addition + UI component + a11y | Must include evidence IDs + redaction notices |
| Add a new Story Node type | Story Node schema/template change + UI renderer update | Requires doc + schema review; likely governance review |
| Add AI-assisted feature | Opt-in controls + uncertainty metadata + governance review | Must not infer sensitive locations; label inference clearly |

### PR checklists (copy/paste into PR description)

#### Add or change a map layer

- [ ] Upstream evidence exists and is referenced (STAC/DCAT/PROV IDs or resolvable links)
- [ ] API/catalog endpoint exists (or contract change included) and enforces redaction/generalization
- [ ] Layer registry updated with:
  - [ ] stable `layer_id` (no reuse for different meaning)
  - [ ] attribution + license surfaced in UI
  - [ ] sensitivity/classification flags set
- [ ] Layer registry validates against `schemas/ui/` *(if present)*
- [ ] UI interaction is keyboard accessible and screen-reader safe (where applicable)
- [ ] No client logs/telemetry include sensitive coordinates/PII
- [ ] Tests updated (unit + minimal e2e smoke)

#### Add or change a Focus Mode panel/view

- [ ] API contract provides a provenance-linked context bundle (IDs + flags)
- [ ] UI renders explicit missing-provenance and redaction states
- [ ] Any AI/predictive content is opt-in + labeled + has uncertainty metadata
- [ ] Citation UX is keyboard-first and copyable (IDs)
- [ ] Telemetry (if enabled) is schema-governed and does not emit PII

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which renderer is canonical (MapLibre, Cesium, or dual-mode)? | TBD | TBD |
| Where is the single canonical layer registry location (`web/layers/` vs `web/src/layers/`)? | TBD | TBD |
| Is telemetry enabled by default? If yes, which schema path governs it (`schemas/telemetry/`)? | TBD | TBD |
| Are Story Nodes compiled into the UI build, fetched from API, or both? | TBD | TBD |

### Future extensions (v13-forward)

- richer story formats (timeline-driven stories, comparative views), governed via template/schema review
- 3D views (Cesium) where appropriate, preserving provenance + redaction
- AI-assisted summaries in Focus Mode, strictly opt-in and labeled with uncertainty

---

## 🗺️ Diagrams

### System / dataflow diagram (canonical ordering)

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph + data/graph/*"]
  C --> D["API boundary — src/server + contracts"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked only"]
~~~

### Optional: Focus Mode request sequence (contract-first)

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

---

## 🌐 STAC, DCAT & PROV Alignment

The UI must make provenance inspectable (never implicit).

### STAC expectations

- UI views should reference STAC Collection IDs and Item IDs when surfacing datasets and assets.
- Layer UX should surface attribution/license from STAC assets where applicable.

### DCAT expectations

- UI should surface dataset-level metadata when relevant (title, publisher, license, description, keywords).

### PROV expectations

- UI should expose lineage cues: source identifiers, run/activity identifiers, and (where allowed) agent/tool identities.
- If a view lacks evidence identifiers, it must present a missing-provenance state rather than implying certainty.

### Sensitivity & redaction

- Treat API-delivered redaction/generalization as authoritative.
- Do not log PII or sensitive coordinates in client telemetry.
- Avoid persistent client storage of sensitive content unless governance-approved.

---

## 🧱 Architecture

### Major components (UI)

| Component | Responsibility | Interface |
|---|---|---|
| API client | Typed calls to API contracts | REST/GraphQL (repo-specific) |
| Map runtime | Render layers + interactions | Layer registry + API/catalog data |
| Story renderer | Render narrative + citations | Story Node v3 structure |
| Focus Mode | Provenance-first deep-dive UI | Context bundle payload |
| Registry loader | Load/validate layer configs | `schemas/ui/` *(if present)* |
| Telemetry (optional) | Emit governance-safe UX signals | `schemas/telemetry/` *(if present)* |

### Layer registries (configuration as contract)

Layer registries are contract artifacts. At minimum each registry entry must support:

- stable `layer_id` (never reuse IDs for different meaning)
- provenance pointers (STAC/DCAT/PROV identifiers or resolvable references)
- attribution + license surfaced in UI
- sensitivity/classification flags
- API/catalog source binding (how data is fetched/loaded)

If `schemas/ui/` exists, registry validation is mandatory before merge.

### Untrusted content & sanitization

Any markdown or remote content rendered in the UI must be treated as untrusted input:

- sanitize HTML/markdown rendering (no script injection)
- block unsafe links/embeds where required by governance
- do not “enhance” redacted data client-side (no join/zoom reconstruction)

### Contract boundaries (do not cross)

- UI never reads Neo4j directly; all access is via contracted APIs.
- API boundary is responsible for authorization + redaction/generalization decisions.
- UI is responsible for respecting policy flags (zoom gating, tooltip gating, hide/show).

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

Story Nodes are governed Markdown artifacts consumed by the UI. Story Nodes must:

- link to graph entity IDs (Place, Person, Event, Document, Organization, Artifact)
- link to STAC/DCAT/PROV evidence identifiers
- separate fact vs inference vs hypothesis (especially if any AI-generated text is present)
- include citation anchors in a consistent, machine-resolvable format (see Story Node template)

### Focus Mode behavior expectations

Focus Mode should make it obvious:

- what entity/story is in focus (stable ID + canonical name)
- what evidence supports the view (copyable IDs + resolvable links)
- what is missing (explicit missing provenance state)
- what is redacted/generalized (clear notice + reason/category where allowed)

### Focus Mode rule (hard gate)

- Focus Mode consumes only provenance-linked content.
- Any predictive/AI-generated content must be opt-in, visibly labeled, and include uncertainty/confidence metadata.
- AI/predictive features must not infer or reveal sensitive locations.

### Optional Focus Mode controls (from Story Nodes or context bundle)

~~~yaml
focus_layers:
  - "TBD:layer_id"
focus_time: "TBD:YYYY or YYYY-MM-DD/YYYY-MM-DD"
focus_center: [-98.0000, 38.0000] # lon, lat (example only)
~~~

### Citation rendering expectations (UI)

- Citations must be keyboard navigable and screen-reader compatible.
- Evidence identifiers must be copyable.
- Provide a consistent “audit panel” affordance for:
  - provenance links
  - sensitivity/redaction notices
  - missing provenance warnings

---

## 🧪 Validation & CI/CD

### CI behavior contract

- **Validate if present:** if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid:** schema errors, missing links, orphan references fail deterministically.
- **Skip if not applicable:** optional roots absent → skip without failing the overall pipeline.

### Minimum validation steps (expectations)

- [ ] Markdown protocol validation (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers)
- [ ] JSON schema validation (as applicable):
  - STAC/DCAT/PROV
  - Story Node schemas (if present)
  - Telemetry schemas (if present)
  - UI layer registry schemas (if present)
- [ ] API contract tests (OpenAPI/GraphQL schema + integration tests)
- [ ] UI unit tests + basic e2e smoke tests
- [ ] Accessibility checks (keyboard navigation, reduced motion, readable citations)
- [ ] Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Local reproduction (repo-specific)

~~~bash
# Placeholders — replace with repo-specific commands defined in web/package.json (if present)

# 1) install deps
# 2) run lint
# 3) run unit tests
# 4) run e2e smoke tests
# 5) validate layer registry schema
~~~

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers (typical)

- Adding new sensitive layers (restricted locations, cultural knowledge, PII, etc.)
- Introducing/changing AI-generated narrative behavior visible to users
- Adding new external data sources (as surfaced in UI)
- Adding new public-facing endpoints or share links
- Any classification/sensitivity change or publication derived from restricted inputs

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

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/README.md` | TBD |
| v1.1.0 | 2025-12-27 | Aligned to Universal governed-doc structure; tightened UI invariants; added CI expectations | TBD |
| v1.2.1 | 2025-12-28 | Re-structured for v13 “one canonical home”; clarified layer registry contract + Focus Mode context bundle expectations; added PR checklists | TBD |

---

Footer refs (do not remove):

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
