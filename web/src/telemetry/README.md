---
title: "KFM Web Telemetry — README"
path: "web/src/telemetry/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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



doc_uuid: "urn:kfm:doc:web:telemetry:readme:v1.0.0"
semantic_document_id: "kfm-web-telemetry-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:telemetry:readme:v1.0.0"
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

# KFM Web Telemetry — README

## 📘 Overview

### Purpose

- Define the **frontend telemetry responsibilities** for the KFM web UI under `web/src/telemetry/`.
- Ensure all client-side telemetry is **schema-defined**, **auditable**, and **safe-by-default** (data minimization + sovereignty-aware).
- Provide a single integration point so UI features (Map, Search, Story Nodes, Focus Mode) emit **consistent, governed signals** without ad-hoc analytics.

### Scope

| In Scope | Out of Scope |
|---|---|
| Client-side telemetry event capture, redaction/minimization rules, schema linkage, and sending events to a server/API boundary. | Defining server-side ingestion/storage/retention implementation (belongs to API/ops). |
| Event naming + payload conventions, and how to add/change a signal. | Any telemetry that includes PII, user-entered free text, or precise sensitive locations. |
| Focus Mode usage signals (enter/exit, entity/story references). | “Product analytics” that tracks individuals, advertising IDs, or fingerprinting. |

### Audience

- Primary: Frontend engineers working in `web/` (React/Map UI + Focus Mode UI).
- Secondary: API maintainers (telemetry ingest boundary), governance/security reviewers, QA.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Telemetry signal**: a named event type emitted by the UI (e.g., “Focus Mode entered”).
  - **Event schema**: JSON Schema governing a signal payload in `schemas/telemetry/`.
  - **Envelope**: common wrapper fields applied to every event (timestamp, app build, etc.).
  - **Redaction/minimization**: transforming or omitting fields to avoid sensitive collection.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Web telemetry module README | `web/src/telemetry/README.md` | Web team | This document |
| Telemetry canonical docs | `docs/telemetry/` | Governance + Eng | Public description of what we collect and why |
| Telemetry schemas | `schemas/telemetry/` | Eng | JSON schemas that define event payload contracts |
| Focus Mode telemetry doc | `docs/telemetry/focus_mode_events.md` | Eng | If missing, create (expected canonical location) |
| Focus Mode event schema | `schemas/telemetry/focus_mode_event.json` | Eng | If missing, create (expected canonical location) |
| Telemetry ingest API contract | `docs/api/` + `src/server/` | API team | not confirmed in repo (define via API contract template if absent) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] All telemetry signals referenced here link to `docs/telemetry/` + `schemas/telemetry/`
- [ ] Redaction/minimization rules explicitly stated (including “never collect” fields)
- [ ] Validation + test steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/src/telemetry/README.md` (must match front-matter)

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

> The exact filenames beyond `README.md` are **not confirmed in repo**; the tree below is the recommended “shape” for a telemetry module that is schema-driven and testable.

~~~text
📁 web/
└── 📁 src/
    └── 📁 telemetry/
        ├── 📄 README.md
        ├── 📄 index.ts                # optional barrel exports
        ├── 📄 types.ts                # TelemetryEvent, TelemetryEnvelope, etc.
        ├── 📄 allowlist.ts            # allowed fields per event + schema mapping
        ├── 📄 redact.ts               # redaction/minimization helpers
        ├── 📄 client.ts               # emit(), batch(), flush(), disable()
        ├── 📄 transport.ts            # sendBeacon/fetch wrapper (API boundary)
        ├── 📄 consent.ts              # user consent gate + sampling switches
        └── 📁 __tests__/
            └── 📄 telemetry.test.ts   # schema + redaction + transport behavior
~~~

## 🧭 Context

### Background

KFM’s architecture requires **provenance-first, contract-first** boundaries across the pipeline:
ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.

Telemetry is part of KFM’s governance posture: it should be possible to answer “what happened in the UI?” and “what signals do we collect?” without hidden collection, and without collecting sensitive/identifying data.

### Assumptions

- The web client is a React/Map UI and interacts with the backend via an API boundary (no direct graph access).
- Telemetry signals are **documented in `docs/telemetry/`** and **validated by JSON Schemas in `schemas/telemetry/`**.
- Telemetry is **opt-in or otherwise explicitly gated** per governance policy (exact consent UX is not defined here).

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Telemetry must not enable inference of restricted/sensitive locations.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical ingest endpoint path + auth model for telemetry? | API team | TBD |
| What consent UX is required (opt-in vs opt-out), and where is it stored? | Governance + Web | TBD |
| What retention window + access controls apply to telemetry logs? | Governance + Ops | TBD |
| Do we need offline buffering and retry semantics (and limits)? | Web + Ops | TBD |

### Future extensions

- Support multiple sinks (e.g., audit log + analytics store) behind the API boundary.
- Add additional performance measurements (e.g., map render timings) if they do not increase sensitivity risk.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  subgraph Client["Web UI (React/Map)"]
    C1["UI Components (Map / Search / Focus Mode)"] --> T["web/src/telemetry (emit + redact + batch)"]
  end

  T -->|schema-aligned events| API["Telemetry ingest API (contracted)"]
  API --> L["Telemetry logs / store (auditable)"]
  L --> D["Dashboards / audits / QA analysis"]

  T -. no direct dependency .-> G["Neo4j Graph (prohibited)"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant User
  participant UI as Web UI
  participant Tel as Telemetry module
  participant API as Telemetry API

  User->>UI: Enter Focus Mode (entity/story)
  UI->>Tel: emit(focus_mode_entered, {story_node_id, entity_id, ...})
  Tel->>Tel: redact/minimize + validate against schema
  Tel->>API: POST /telemetry (batched envelope)
  API-->>Tel: 202 Accepted
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| UI interaction | in-memory event payload | React components/hooks | type guard + field allowlist; optional JSON schema validation |
| Focus Mode transitions | `{story_node_id, entity_id, mode}` | Focus Mode UI | schema + allowlist; IDs only (no narrative text) |
| Performance timings | numeric durations | browser timing APIs | range checks (non-negative), sampling |
| UI errors | error category + code | error boundary / fetch wrapper | categorical-only; never include raw stack traces unless explicitly allowed |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Telemetry event envelope | JSON | network to API boundary | `schemas/telemetry/<event>.json` + envelope contract (TBD) |
| Batched events | JSON array | network to API boundary | schema(s) for event + batch wrapper (TBD) |
| Local debug logging (dev-only) | console output | browser console | disabled in prod builds (recommended) |

### Sensitivity & redaction

**Never collect (hard prohibition):**
- PII (names, emails, phone numbers, account IDs, IPs).
- User-entered free text (search queries, notes, form fields).
- Authentication tokens, headers, cookies.
- Precise coordinates or geometries that could expose restricted locations (unless governance-approved + generalized).

**Allowed (typical safe fields):**
- **Opaque IDs** already public in KFM artifacts (e.g., `story_node_id`, `entity_id`, `layer_id`, `dataset_id`).
- Coarse UI state: booleans, enums, counts, durations.
- Map state: *zoom level* and *viewport category* (avoid exact center coordinate; prefer coarse tile or bounding-box bucket if needed).

**Implementation rule:**
- Use an **allowlist-by-event**: drop unknown fields by default, rather than trying to redact after the fact.

### Quality signals

- Schema conformance rate (% accepted vs dropped).
- Drop reasons (missing required field, disallowed field present, invalid enum).
- Client-side queue depth (if buffering) and flush outcomes (success/failure counts).
- Sampling rate applied (if sampling is enabled).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Telemetry events may reference STAC item IDs **as identifiers only** (e.g., “user opened asset X”), but telemetry itself is **not** a STAC item/collection.

### DCAT

- Telemetry may reference DCAT dataset identifiers to measure dataset-layer usage (e.g., “layer toggled for dataset Y”).

### PROV-O

- Telemetry is not a substitute for PROV lineage.
- Telemetry may *reference* PROV activity/run IDs when measuring operational UX around data freshness or run availability.

### Versioning

- Telemetry schemas follow **semantic versioning**.
  - Backward-compatible additions: minor bump.
  - Required-field changes or meaning changes: major bump.
- Every emitted event includes an **event schema version** (field name is implementation-defined; recommended).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts (and telemetry ingest) | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| Telemetry event schemas | `schemas/telemetry/` | Semver + changelog; changes require review |
| Telemetry docs (human-readable) | `docs/telemetry/` | Must match emitted signals + schema versions |
| API schemas | `src/server/` + `docs/api/` | Contract tests required |
| Layer registry | `web/**` | Schema-validated (where applicable) |

### Extension points checklist (for future work)

- [ ] Telemetry: new signals added + schema version bump
- [ ] Telemetry: update `docs/telemetry/` to reflect any new/changed signals
- [ ] UI: call-sites updated to use telemetry module (no ad-hoc emits)
- [ ] Governance: review if any signal increases sensitivity risk
- [ ] Tests: add/update schema + redaction tests

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Telemetry may record:
  - Focus Mode entry/exit events
  - IDs of the entity/story displayed
  - UI actions (expand evidence, follow citation link, toggle timeline)
- Telemetry must **not** record:
  - The narrative text shown to the user
  - User-entered annotations or free text
  - Any derived “inference” about sensitive locations

### Provenance-linked narrative rule

- Focus Mode content is provenance-linked; telemetry only references **IDs** for auditing usage patterns.
- Telemetry must not become an input that changes historical claims.

### Optional structured controls

~~~yaml
# Telemetry should prefer IDs + enums over raw strings.
example_focus_mode_event_payload:
  event_name: "focus_mode_entered"
  event_version: "v1"
  story_node_id: "kfm-story-<id>"
  entity_id: "kfm-entity-<id>"
  entry_source: "map_click"  # enum
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] JSON schema validation (telemetry schemas)
- [ ] Unit tests for:
  - allowlist behavior
  - redaction behavior
  - batching/flush behavior
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate telemetry schemas (if a validator task exists)
# npm run validate:schemas

# 2) run web unit tests
# npm test

# 3) run doc lint / markdown protocol validation
# npm run lint:docs
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| focus_mode_entered | Focus Mode UI | `docs/telemetry/` + `schemas/telemetry/` |
| focus_mode_exited | Focus Mode UI | `docs/telemetry/` + `schemas/telemetry/` |
| layer_toggled | Map UI layer controls | `docs/telemetry/` + `schemas/telemetry/` |
| api_request_failed | API fetch wrapper | `docs/telemetry/` + `schemas/telemetry/` |
| performance_timing | browser timing APIs | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- Any new telemetry signal or schema change that:
  - adds fields,
  - changes meaning,
  - increases sensitivity risk,
  must be reviewed against:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/ETHICS.md`
  - `docs/governance/SOVEREIGNTY.md`

### CARE / sovereignty considerations

- Telemetry must be designed to avoid creating a “shadow dataset” of sensitive locations or community-sensitive activity.
- Prefer coarse summaries and ID references over raw geography.
- If a signal could enable inference of restricted sites, it requires explicit governance approval and documented generalization rules.

### AI usage constraints

- This document allows summarization/structure extraction/translation/keyword indexing, but prohibits generating new policies or inferring sensitive locations (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for `web/src/telemetry/` | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

