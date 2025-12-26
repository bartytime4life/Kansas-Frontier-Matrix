---
title: "KFM Web — Parse Utilities"
path: "web/src/utils/parse/README.md"
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
doc_uuid: "urn:kfm:doc:web:utils:parse:readme:v1.0.0"
semantic_document_id: "kfm-web-utils-parse-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:utils:parse:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"
ai_transform_permissions:
  - summarize
  - translate
  - reformat
  - generate_code_snippets
ai_transform_prohibited:
  - generate_policy
  - infer_sensitive_locations
doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Parse utilities (`web/src/utils/parse`)

> **Purpose (required):** Provide a single, governed reference for the parsing + validation utilities used by the KFM web UI. This module exists to safely transform **untrusted inputs** (API payloads, catalog artifacts, URL/query params, Story Node text) into **UI-friendly structures** while preserving provenance, sensitivity, and redaction/generalization constraints.

---

## 📘 Overview

### Scope

In scope:

- Defensive parsing/validation of **API payloads** before rendering.
- Parsing/normalization of **primitives** (strings, numbers, booleans, dates) into stable UI values.
- Parsing of **geospatial payloads** (GeoJSON, bbox, coordinates) without “unmasking” or densifying generalized geometry.
- Extraction + preservation of **provenance identifiers** (STAC/DCAT/PROV IDs, citation tokens) for Focus Mode audit panels.
- Consistent parse error shape for UI display and optional telemetry (if present).

Out of scope:

- Network calls / fetching (belongs in API client/services).
- Graph access (UI never queries Neo4j directly).
- Business logic (ranking, aggregation, summarization, narrative generation).
- Redaction/generalization policy decisions (must be enforced at the API boundary).

### Audience

- Frontend contributors working in `web/`
- API engineers evolving response contracts
- QA/governance reviewers verifying provenance + redaction compliance

### Definitions (link to glossary)

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc include: **runtime validation**, **contract**, **provenance**, **redaction**, **generalization**, **Story Node**, **Focus Mode**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical flow + invariants |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical paths + contract set |
| API contracts | `src/server/contracts/**` | API Eng | Canonical contract artifacts consumed by UI |
| Schemas | `schemas/**` | Data/Platform | JSON Schemas for STAC/DCAT/PROV/UI/telemetry |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Story Node front-matter + citation rules |
| This README | `web/src/utils/parse/README.md` | Frontend | Parse responsibilities, patterns, safety rules |

### Definition of done (for this README)

- [ ] Front-matter complete + `path` matches file location
- [ ] Responsibilities of `parse/` are explicit (what belongs here vs elsewhere)
- [ ] Relationship to API contracts + provenance rules is documented
- [ ] Any commands/examples are either repo-accurate or explicitly marked **not confirmed in repo**
- [ ] Governance + CARE/sovereignty constraints are stated (no unmasking/generalization bypass)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/utils/parse/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| API boundary | `src/server/` | Contracted access layer; redaction + provenance refs |
| Contracts | `src/server/contracts/` | OpenAPI/GraphQL schemas consumed by UI |
| Schemas | `schemas/` | JSON Schemas for catalogs, UI registries, telemetry |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts + lineage used by API/UI |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narratives + assets |
| Tests | `tests/` | Unit/integration/contract tests |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some files/folders may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 utils/
        └── 📁 parse/
            ├── 📄 README.md
            ├── 📄 index.(ts|js)                 # barrel exports (not confirmed in repo)
            ├── 📄 primitives.(ts|js)            # number/date/string helpers (not confirmed in repo)
            ├── 📄 geojson.(ts|js)               # GeoJSON + bbox parsing (not confirmed in repo)
            ├── 📄 stac.(ts|js)                  # STAC item/collection parsing (not confirmed in repo)
            ├── 📄 dcat.(ts|js)                  # DCAT record parsing (not confirmed in repo)
            ├── 📄 prov.(ts|js)                  # PROV reference parsing (not confirmed in repo)
            ├── 📄 citations.(ts|js)             # Story Node citation parsing (not confirmed in repo)
            ├── 📁 __tests__/                    # unit tests (not confirmed in repo)
            │   └── 📄 *.test.(ts|js)
            └── 📁 fixtures/                     # small synthetic fixtures only (not confirmed in repo)
                └── 📄 *.json
~~~

---

## 🧭 Context

### Background

KFM’s web app consumes **contracted** API responses and catalog artifacts to render maps, timelines, and Focus Mode narratives. Parsing helpers exist so the UI can:

- validate external inputs before rendering (avoid runtime crashes),
- keep UI behavior deterministic and auditable,
- preserve provenance links and governance flags end-to-end.

### Assumptions

- The UI consumes responses that conform to canonical API contracts in `src/server/contracts/**`.
- Catalog artifacts (STAC/DCAT/PROV) are schema-validated upstream, but the UI still treats them as untrusted at runtime.
- Parsers here are shared across multiple UI surfaces (map layers, Focus Mode panels, Story Node rendering).

### Constraints / invariants

- Canonical flow is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **API boundary is mandatory:** the UI must never query Neo4j directly; it only consumes APIs and catalog endpoints.
- Focus Mode must display **provenance-linked** content only.
- Parsers must not introduce “helpful” inferences that could defeat sensitivity handling (e.g., reconstructing exact locations from generalized geometry).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which runtime validation pattern is standard in the web app (type guards vs schema library vs discriminated unions)? | Frontend | TBD |
| What is the canonical representation of `kfm:locationGeneralization` in UI models/components? | Frontend + Governance | TBD |
| Should parse failures emit telemetry (and if so, which schema under `schemas/telemetry/**`)? | Platform | TBD |

### Future extensions

- Add a fixture-driven “contract sync” harness: representative API payloads validated by parsers (optional).
- Add a shared parse error taxonomy aligned with contract tests (optional; requires contract owner review).
- Add CI lint rule(s): “no UI direct-to-graph imports” and “parse module cannot import Neo4j drivers” (optional).

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[API responses<br/>src/server] -->|JSON| B[Parse/validate<br/>web/src/utils/parse]
  C[Catalog artifacts<br/>STAC/DCAT/PROV] -->|JSON/JSON-LD| B
  D[URL params / local inputs] -->|strings| B

  B --> E[Typed UI domain objects]
  E --> F[React components<br/>map + timeline + panels]
  F --> G[Focus Mode<br/>provenance-linked only]
~~~

### Optional: sequence diagram (Focus Mode context query)

~~~mermaid
sequenceDiagram
  participant UI as React UI
  participant Parse as web/src/utils/parse
  participant API as API boundary
  participant Graph as Neo4j Graph

  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
  UI->>Parse: validate + normalize bundle before rendering
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

- Story Nodes are curated Markdown artifacts that carry front-matter, entity references, and citations to evidence IDs.
- The UI must render Story Nodes so source references remain visible and auditable.

### Focus Mode rule

- Focus Mode only consumes **provenance-linked** content.
- Any predictive / AI-generated content must be **opt-in** and include uncertainty/confidence metadata.

### What parsers in this folder must preserve

When parsing Story Node or Focus Mode payloads, never drop or silently coerce fields that determine governance behavior, especially:

- Evidence identifiers (STAC Item/Collection IDs, DCAT dataset IDs, PROV activity IDs)
- Redaction/generalization flags such as `kfm:locationGeneralization` (must be respected; never “unmask” in public views)
- Classification/sensitivity markers (if present) used to gate rendering or access

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Type-level checks (TS/JS) for parse module exports
- [ ] Unit tests for parsers (fast, deterministic)
- [ ] Contract tests / fixtures that ensure parsers align to API contract versions
- [ ] UI schema checks (e.g., layer registry validation under `schemas/ui/**`) where applicable
- [ ] Security and sovereignty checks (no secrets; no leakage of restricted locations)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)

# 1) run web unit tests
# pnpm -C web test

# 2) run lint
# pnpm -C web lint

# 3) run typecheck
# pnpm -C web typecheck
~~~

### Telemetry signals

If UI telemetry exists (not confirmed in repo), consider schema-versioned signals for parse health:

| Signal | Source | Where recorded |
|---|---|---|
| ui_parse_failure | `web/src/utils/parse` | `docs/telemetry/` + `schemas/telemetry/` |
| ui_contract_mismatch | `web/src/utils/parse` | `docs/telemetry/` + `schemas/telemetry/` |
| ui_redaction_violation_blocked | UI gating layer | `docs/telemetry/` + `schemas/telemetry/` |

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API payloads | JSON | `src/server/` endpoints | Contract-driven parsing + runtime checks |
| STAC Collections/Items | JSON | `data/stac/**` or catalog endpoint | Validate required keys; preserve IDs/links |
| DCAT records | JSON / JSON-LD | `data/catalog/dcat/**` or API | Validate identifiers, license fields |
| PROV bundles | JSON-LD / PROV-JSON | `data/prov/**` or API | Validate IDs; preserve lineage references |
| Story Nodes | Markdown + front-matter | `docs/reports/story_nodes/**` or API | Validate front-matter keys + citation tokens |
| URL / route params | strings | browser location | strict parsing + explicit defaults |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Parsed primitives | JS values | `web/src/utils/parse/**` | local conventions |
| UI domain models | JS/TS objects | `web/src/**` | derived from contracts |
| Normalized geometry | GeoJSON-like | `web/src/**` | ensure no “unmasking” |
| Parse errors | structured object | `web/src/**` | local conventions |
| Optional telemetry events | JSON/logs | `docs/telemetry/` | `schemas/telemetry/**` (if present) |

### Sensitivity & redaction

- Treat all inbound data as untrusted and potentially policy-gated.
- Never re-derive exact locations from generalized geometry or suppressed coordinates.
- If a payload appears to contain restricted details unexpectedly, prefer failing closed (block rendering) and surface a user-safe error state.

### Quality signals

- Required fields present; stable IDs preserved.
- Geometry validity checks where applicable (bbox shape, coordinate ranges).
- Deterministic normalization (same input → same output object).

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Preserve: `id`, `collection`, `assets`, `links`, `geometry`, `bbox`, `datetime`/`start_datetime`/`end_datetime` (as applicable).
- Do not treat STAC as “optional metadata”; in KFM it is a first-class contract between catalog ↔ UI.

### DCAT

- Preserve dataset identifiers, license, publisher/contact fields as provided.
- Do not fabricate missing license/publisher data in the UI; missing metadata should be reported upstream.

### PROV-O

- Preserve `prov:wasDerivedFrom`, `prov:wasGeneratedBy`, activity IDs, and agent IDs as returned.
- If the UI receives a “context bundle” that includes provenance refs, parsers must keep them intact so Focus Mode can expose lineage/audit.

### Versioning

- When an API or catalog artifact version changes, update parsers in lockstep and bump this README version history if behavior changes.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Parsers (`web/src/utils/parse`) | Validate + normalize untrusted inputs for UI consumption | pure functions returning typed structures or explicit errors |
| UI components (`web/src/**`) | Render map/timeline/panels from parsed data | component props |
| API boundary (`src/server/**`) | Enforce contracts + redaction/generalization; serve provenance refs | REST/GraphQL |
| Contracts (`src/server/contracts/**`) | Canonical response shapes and versions | schema files + contract tests |
| Schemas (`schemas/**`) | Validation for catalogs, UI registries, telemetry | JSON Schema bundles |
| Story Nodes (`docs/reports/story_nodes/**`) | Governed narratives with citations | Markdown template v3 |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/**` | Backward compatible or version bump |
| Catalog schemas | `schemas/stac/**`, `schemas/dcat/**`, `schemas/prov/**` | Semver + changelog |
| Story Node schema/template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` + `schemas/storynodes/**` | Validate before publish |
| UI registry schema | `schemas/ui/**` | Validate before deploy |

### Parsing conventions

Recommended naming conventions (adjust to match existing code):

- `isX(value): value is X` — cheap type guard (no coercion)
- `parseX(value): X` — strict parser; throws or returns errors consistently
- `tryParseX(value): { ok: true; value: X } | { ok: false; error: ParseError }` — no-throw variant
- `coerceX(value): X` — **avoid** unless explicitly approved; coercion can hide contract issues

Recommended behavior:

- Prefer “fail closed” for governance-relevant fields (classification/sensitivity/generalization).
- Keep parsing pure and deterministic; no I/O, no global state, no randomness.
- Keep error messages user-safe (no secrets, no leaking restricted locations).

### Example pattern (illustrative)

> Function names below are examples (**not confirmed in repo**). Align with actual exports.

~~~ts
// Example: parse a bbox from unknown input
type BBox = [number, number, number, number];

export function tryParseBBox(
  input: unknown
): { ok: true; value: BBox } | { ok: false; error: string } {
  if (!Array.isArray(input) || input.length !== 4) {
    return { ok: false, error: "bbox must be an array of 4 numbers" };
  }

  const nums = input.map((x) => Number(x));
  if (nums.some((n) => !Number.isFinite(n))) {
    return { ok: false, error: "bbox values must be finite numbers" };
  }

  return { ok: true, value: nums as BBox };
}
~~~

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Escalate for human review if parse changes could alter what the UI can display or infer, especially:

- New fields that might reveal restricted locations or culturally sensitive knowledge
- Changes in how redaction/generalization flags are interpreted
- Introduction of coercion that could hide contract failures
- Any UI behavior that could display un-cited narrative content by default

### Safety notes

- Treat generalized geometry and withheld attributes as hard boundaries: parsing must not “reconstruct” hidden details.
- Avoid logging raw payloads when they may include sensitive coordinates; prefer logging stable IDs and error codes.

---

## 🕰️ Version History

| Version | Date | Author | Notes |
|---:|---:|---|---|
| v1.0.0 | 2025-12-26 | `<your-name>` | Initial governed README for `web/src/utils/parse`. |

---

### Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

