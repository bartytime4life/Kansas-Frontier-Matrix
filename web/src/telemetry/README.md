---
title: "KFM Web — Telemetry (UI Instrumentation)"
path: "web/src/telemetry/README.md"
version: "v0.1.1-draft"
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

doc_uuid: "urn:kfm:doc:web:telemetry:readme:v0.1.1-draft"
semantic_document_id: "kfm-web-telemetry-readme"
event_source_id: "ledger:kfm:doc:web:telemetry:readme:v0.1.1-draft"
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

# 📡 KFM Web Telemetry

**Path:** `web/src/telemetry/`

<img alt="doc_kind" src="https://img.shields.io/badge/doc_kind-README-0b5563?style=for-the-badge" />
<img alt="domain" src="https://img.shields.io/badge/domain-web--telemetry-1f6feb?style=for-the-badge" />
<img alt="status" src="https://img.shields.io/badge/status-Draft-6e7781?style=for-the-badge" />
<img alt="protocol" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-7c3aed?style=for-the-badge" />

</div>

---

> **Purpose (required):** Define how the **KFM web UI** captures and emits **telemetry signals** (client-side events, performance metrics, and error signals) in a way that is **schema-aligned**, **privacy-safe**, and consistent with KFM’s **layered architecture** (UI → APIs; no direct graph access).

## 📘 Overview

### Purpose

This README governs the **frontend telemetry module** under `web/src/telemetry/`, including:

- What telemetry is allowed to be collected in the UI (and what is prohibited).
- How event payloads should be shaped and **redacted** before leaving the client.
- How UI telemetry should reference system artifacts (layer IDs, Story Node IDs, STAC Item IDs) without leaking sensitive data.
- How UI telemetry aligns to **system-level telemetry signals** and CI gates (schema validation + privacy/security scanning).

### Scope

| In Scope | Out of Scope |
|---|---|
| UI event emission (interaction + UX signals) | Backend collector/storage implementation (server-side) |
| Client performance + error instrumentation | ETL/Graph/API telemetry (handled in their subsystems) |
| Redaction + PII/sensitive-location protections | Defining new governance policy (must be in governance docs) |
| Schema-aligned payload shaping (client-side) | Any raw recording of user-entered free text |

### Audience

- Primary: frontend contributors working in `web/`
- Secondary: platform/reliability contributors reviewing observability + governance signals

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo; recommended)*.
- Terms used in this doc:
  - Telemetry (events/metrics/traces/logs)
  - PII (personally identifiable information)
  - “Sensitive locations” (locations protected by governance/sovereignty policy)
  - Schema validation (telemetry JSON schema)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + cross-cutting gates |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Governs structure of this README |
| Telemetry docs | `docs/telemetry/` | TBD | Cross-stack telemetry signals + governance *(expected; not confirmed in repo)* |
| Telemetry schemas | `schemas/telemetry/` | TBD | JSON Schemas for telemetry payloads *(expected; may be v13 target)* |
| UI layer registry schemas | `schemas/ui/` | TBD | Schema for layer registry IDs referenced in telemetry *(expected; not confirmed in repo)* |
| API boundary | `src/server/` (or repo-defined equivalent) | TBD | UI emits via contracted boundary (UI never reads Neo4j directly) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Directory layout section exists with emoji tree
- [ ] Explicit rules for PII + sensitive-location handling (URL + error + map interactions)
- [ ] Event naming + payload shaping guidance is explicit and matches schema conventions
- [ ] Minimal event envelope is defined + example payload included
- [ ] Validation steps listed (and any command examples are clearly marked placeholders)
- [ ] Governance refs included at the end

## 🗂️ Directory Layout

### This document

- `path`: `web/src/telemetry/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI source | `web/src/` | React/MapLibre UI code |
| UI telemetry module | `web/src/telemetry/` | Client telemetry plumbing (this sub-area) |
| Telemetry docs | `docs/telemetry/` | Cross-stack telemetry signals + governance (expected) |
| Telemetry schemas | `schemas/telemetry/` | JSON Schemas for telemetry payloads (expected) |
| UI schemas | `schemas/ui/` | Layer registry + UI contract schemas (expected) |
| API boundary | `src/server/` | Contracted API layer (REST/GraphQL); may include telemetry ingest endpoints |

### Expected file tree for this sub-area

> Recommended structure. Some files may not exist yet (**not confirmed in repo**).

~~~text
web/src/telemetry/
├── 📄 README.md                  # This file (governed module guidance)
├── 📄 index.ts                   # Public exports (recommended)
├── 📄 init.ts                    # Initialize telemetry providers (recommended)
├── 📄 events.ts                  # Event name registry + payload builders (recommended)
├── 📄 redaction.ts               # Redaction helpers (required if telemetry enabled)
├── 📄 transport.ts               # Beacon/batch transport (recommended)
├── 📄 context.ts                 # Correlation + session context helpers (recommended)
├── 📁 providers/                 # Provider adapters (recommended)
│   ├── 📄 noop.ts                # No-op provider (recommended; default in dev)
│   └── 📄 otel.ts                # OpenTelemetry adapter (optional; not confirmed in repo)
└── 📁 __tests__/                 # Unit tests (recommended)
    ├── 📄 redaction.test.ts      # Verify no PII / sensitive coords leak
    └── 📄 envelope.test.ts       # Verify envelope + schema conformance (if schema exists)
~~~

## 🧭 Context

### Background

KFM treats telemetry as a first-class subsystem with contracts and validation gates. The UI module exists to ensure **frontend signals** are:

- consistent with system-level telemetry expectations (signals + CI gates),
- safe under governance (no sensitive location leakage),
- and shaped for schema validation (where schemas exist).

> **Repo reality check:** Client-side JSON schemas for telemetry events may be missing or incomplete (not confirmed in repo). This README defines the *expected envelope and rules* so adding `schemas/telemetry/**` becomes a straightforward follow-on.

### Design goals

- **Schema-first:** telemetry payloads should validate against `schemas/telemetry/**` (if present).
- **Privacy-first:** avoid collecting PII and avoid emitting precise coordinates for sensitive/protected locations.
- **No hidden data leakage:** telemetry must not introduce side-channels that bypass UI/Map safeguards.
- **Low overhead:** telemetry must not materially degrade UI responsiveness.
- **Fail-safe:** telemetry failures must not block core UI functionality.

### Non-goals

- Replacing server-side observability.
- Persisting telemetry locally beyond short buffering needed for transport.
- Capturing raw user input, prompts, or narrative free text.
- Emitting full STAC/DCAT/PROV payloads from the browser.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  U["User interaction"] --> UI["Web UI components"]
  UI --> T["web/src/telemetry: capture + shape"]
  T --> R["Redaction + minimization"]
  R --> X["Transport: batch / beacon"]
  X --> API["Telemetry ingest boundary (API)"]
  API --> S[(Telemetry store / dashboards)]
  S --> G["Governance + reliability review"]
~~~

## 🧱 Architecture

### Layering rule (UI ↔ API boundary)

- UI telemetry is emitted outward via a **contracted boundary** (e.g., API endpoint / collector), never by direct graph access.
- Any telemetry requiring graph context MUST carry only **stable identifiers** (e.g., `story_node_id`, `stac_item_id`) and let the backend resolve details if allowed.

### Event naming and stability

**Naming convention (recommended):**

- `lower_snake_case`
- prefix by subsystem or feature area:
  - `ui_*`
  - `focus_mode_*`
  - `story_node_*`
  - `map_*`

**Use system-recommended signal names verbatim when applicable** (example: `focus_mode_redaction_notice_shown`).

### Minimal event envelope (recommended)

All telemetry MUST be emitted as a *single* envelope shape that supports three kinds of signals:

- `kind: "event"` (user/system actions)
- `kind: "metric"` (performance numbers)
- `kind: "error"` (error signals)

#### Envelope fields

Required fields:

- `event_name` (string, `lower_snake_case`)
- `event_id` (string; random UUID)
- `timestamp` (string; ISO 8601)
- `kind` (`event` | `metric` | `error`)
- `environment` (`dev` | `staging` | `prod` | other env labels)
- `ui_version` (build/version string)
- `correlation_id` (random; per interaction chain)
- `session_id` (random; short-lived; not a user identifier)

Optional fields (safe only):

- `context` (stable IDs + coarse context)
- `metrics` (numbers only; no user content)
- `error` (sanitized error fields only)
- `sampling_rate` (0.0–1.0)

#### Example payload (sanitized)

~~~json
{
  "event_name": "ui_layer_toggle",
  "event_id": "a7f2c8d2-9a5d-4b14-9f1b-3c5b9f0d6a1a",
  "timestamp": "2025-12-28T18:40:00Z",
  "kind": "event",
  "environment": "dev",
  "ui_version": "0.0.0-local",
  "correlation_id": "c17d7af0-9c8a-4cf2-86d1-93a8f7a7c013",
  "session_id": "e4eddf4f-2cf5-43e0-9c4b-2d3f5f9b72c0",
  "sampling_rate": 1.0,
  "context": {
    "layer_id": "land_treaties",
    "enabled": true,
    "route_id": "map",
    "map_zoom_bucket": "z08-z10"
  }
}
~~~

### Context rules (what can go in `context`)

Allowlist guidance:

- ✅ stable identifiers: `layer_id`, `story_node_id`, `dataset_id`, `stac_item_id`, `prov_activity_id`
- ✅ booleans + small enums: `enabled`, `panel_open`, `redaction_method`
- ✅ coarse buckets: `map_zoom_bucket`, `region_bucket`, `viewport_tile_id`
- ✅ numbers that are not identifiers: latency ms, counts

Denylist guidance:

- ❌ user-entered free text (search terms, prompts, notes)
- ❌ URL query strings / hash fragments
- ❌ authentication tokens, cookies, request headers
- ❌ raw coordinates, raw geometries, or high-precision viewport bounds

### URL + route handling (required)

If emitting navigation/page-view telemetry:

- Emit a **route ID** (e.g., `map`, `story`, `focus_mode`) rather than a full URL.
- If a URL is needed for debugging, emit **path only**, stripped of:
  - query parameters (`?…`)
  - fragments (`#…`)
  - any dynamic segments that may contain identifiers

### Location-bearing events (required)

For map interactions (pan/zoom/click):

- NEVER emit raw `lat`/`lon`, raw GeoJSON, or viewport bounds at high precision.
- Prefer **coarse** location encodings:
  - tile IDs / region buckets / generalized cells (e.g., H3 at coarse resolution — exact resolution governed elsewhere)
- If the UI enforces safeguards (e.g., max zoom on sensitive layers), telemetry SHOULD prefer:
  - `max_zoom_enforced: true`
  - `redaction_method: "<enum>"`
  - rather than any high-precision location details.

### Redaction strategy (required)

Telemetry MUST be redacted **before** transport.

Recommended implementation strategy:

- centralize redaction in `redaction.ts`
- use an **allowlist-first** approach:
  - only fields explicitly allowed by schema are emitted
  - any unknown keys are dropped by default
- apply **string scrubbing** for allowed string fields:
  - hard cap lengths (e.g., 256 chars)
  - remove obvious secrets (bearer tokens, API keys) when detected
  - do not emit stack traces unless scrubbed and governance-approved

### Transport (recommended)

- Prefer batching in memory and sending periodically.
- Use `navigator.sendBeacon` for unload-safe emission when available.
- Use `fetch(..., { keepalive: true })` as a fallback where appropriate.
- Never store telemetry in `localStorage` or other persistent client storage by default.
- Telemetry transport failures must not throw uncaught errors.

### Sampling + rate limiting (recommended)

- Apply sampling to high-volume events (e.g., map pan/zoom) to reduce noise and cost.
- Rate limit per session to avoid abusive event storms.
- Errors SHOULD be higher priority (lower sampling) than interaction events.

### Providers (recommended)

- Default provider SHOULD be a no-op (`providers/noop.ts`) for local development or when telemetry is disabled.
- Any third-party SDK or remote collector integration requires governance review and explicit documentation in `docs/telemetry/` (if present).

### Example usage (pseudocode)

~~~ts
// Pseudocode — adapt to your actual telemetry API surface.
//
// import { initTelemetry, emitEvent } from "./telemetry";
//
// initTelemetry({ environment: "dev" });
//
// emitEvent("ui_layer_toggle", {
//   layer_id: "land_treaties",
//   enabled: true,
//   map_zoom_bucket: "z08-z10",
// });
~~~

## 🧠 Story Node & Focus Mode Integration

### Focus Mode UX signals (examples)

This module is expected to support Focus Mode UX signals, such as:

- `focus_mode_opened` / `focus_mode_closed`
- `story_node_loaded` (by `story_node_id`)
- `evidence_panel_opened` (by evidence/stac/prov IDs only)
- `focus_mode_redaction_notice_shown` (by `layer_id` + `redaction_method`)

### Provenance-linked narrative rule (telemetry alignment)

When emitting events tied to narrative or evidence:

- Prefer emitting **identifiers** (`story_node_id`, `dataset_id`, `stac_item_id`) rather than embedding narrative text.
- Never emit full STAC/PROV payloads from the client; emit IDs and let the server resolve if permitted.

### Optional structured controls (registry-style)

~~~yaml
# Optional (if you maintain a Focus Mode instrumentation registry)
focus_layers:
  - "layer:<layer-id>"
focus_time: "<iso8601>"
focus_center: "<coarse-or-redacted>"
~~~

## 🧪 Validation & CI/CD

### Validation steps (recommended)

Align this module to repo-wide “v12-ready” CI gates (see Master Guide), including:

- [ ] Markdown protocol validation (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers)
- [ ] JSON schema validation (if schemas exist):
  - [ ] telemetry schemas (`schemas/telemetry/**`)
  - [ ] UI layer registry schemas (`schemas/ui/**`)
- [ ] Secrets scan (no tokens/keys in client code)
- [ ] PII scan (telemetry payloads must not contain emails, names, etc.)
- [ ] Sensitive-location leakage checks (no precise restricted coords in payloads)
- [ ] Classification propagation checks (no downgrades without review)

UI-level checks (recommended):

- [ ] Unit tests for redaction + payload shaping
- [ ] Unit tests for envelope shaping (and schema conformance if available)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run frontend unit tests
# 2) run lint
# 3) run schema checks (telemetry schemas) if configured
~~~

### Telemetry signals (examples)

> Keep the signal list aligned with canonical telemetry docs/schemas (do not “invent” production signals without updating the schema + docs).

| Signal | Source | Where recorded |
|---|---|---|
| `ui_layer_toggle` | UI layer registry toggles | `docs/telemetry/` + `schemas/telemetry/` |
| `focus_mode_opened` | Focus Mode entry | `docs/telemetry/` + `schemas/telemetry/` |
| `story_node_loaded` | Story Node fetch/render | `docs/telemetry/` + `schemas/telemetry/` |
| `ui_api_request` | API calls (latency/status buckets) | `docs/telemetry/` + `schemas/telemetry/` |
| `ui_error_boundary` | Uncaught UI errors (sanitized) | `docs/telemetry/` + `schemas/telemetry/` |
| `focus_mode_redaction_notice_shown` | Redaction notices shown | `docs/telemetry/` + `schemas/telemetry/` |

## 📦 Data & Metadata

### Allowed identifiers (preferred)

- `layer_id` (UI layer registry ID)
- `story_node_id` (Story Node identifier)
- `dataset_id` / `collection_id` (catalog identifiers)
- `stac_item_id` (STAC Item `id` only; avoid embedding geometry)
- `prov_activity_id` (run/activity ID; if surfaced to UI — not confirmed in repo)

### Prohibited payload fields (default)

- User-entered free text (search terms, prompts, notes)
- Email addresses, phone numbers, names, precise home/work addresses
- Authentication tokens, session cookies, request headers
- Exact coordinates for sensitive/protected locations (unless explicitly allowed by governance policy)
- Full URLs with query strings/fragments
- Full user-agent strings (prefer coarse buckets if needed)

### Redaction strategy (recommended)

- Coarsen location signals (tile/region buckets) instead of raw lat/lon.
- Hash or replace device/user identifiers with short-lived random session identifiers.
- Prefer enumerations (IDs, booleans) over arbitrary strings.

## 🌐 STAC, DCAT & PROV Alignment

This UI telemetry module does not generate STAC/DCAT/PROV artifacts, but it SHOULD support cross-linking by ID:

- If the UI renders a dataset or item, emit the **STAC ID** (not the full JSON).
- If the UI references pipeline runs or evidence artifacts, emit **PROV activity IDs** where available (not confirmed in repo for the UI layer).

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when:

- Adding new telemetry fields that could capture PII
- Adding new location-bearing signals or increasing location precision
- Logging identifiers that could expose sensitive sites by interaction/zoom
- Adding third-party telemetry vendors/SDKs that transmit data off-platform

### CARE / sovereignty considerations

- Follow `docs/governance/SOVEREIGNTY.md` for rules on culturally sensitive content and protected locations.
- When in doubt: **collect less**, generalize more, and document the decision in `docs/telemetry/` (if present).

### AI usage constraints

- Allowed (documentation-only): summarization, structure extraction, translation, keyword indexing
- Prohibited: generating new policy; inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v0.1.0-draft | 2025-12-25 | Initial `web/src/telemetry/` README scaffold | TBD |
| v0.1.1-draft | 2025-12-28 | Upgrade: add envelope contract, naming alignment, and CI/privacy gates | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`