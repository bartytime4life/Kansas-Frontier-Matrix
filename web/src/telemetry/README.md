---
title: "KFM Web — Telemetry (UI Instrumentation)"
path: "web/src/telemetry/README.md"
version: "v0.1.0-draft"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:telemetry:readme:v0.1.0-draft"
semantic_document_id: "kfm-web-telemetry-readme"
event_source_id: "ledger:kfm:doc:web:telemetry:readme:v0.1.0-draft"
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

### Scope

| In Scope | Out of Scope |
|---|---|
| UI event emission (interaction + UX signals) | Backend collector/storage implementation (server-side) |
| Client performance + error instrumentation | ETL/Graph/API telemetry (handled in their subsystems) |
| Redaction + PII/sensitive-location protections | Defining new governance policy (must be in governance docs) |
| Schema-aligned payload shaping | Any raw recording of user-entered free text |

### Audience

- Primary: frontend contributors working in `web/`
- Secondary: platform/reliability contributors reviewing observability + governance signals

### Definitions (link to glossary)

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - Telemetry (events/metrics/traces/logs)
  - PII (personally identifiable information)
  - “Sensitive locations” (locations protected by governance/sovereignty policy)
  - Schema validation (telemetry JSON schema)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + extension matrix |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Governs structure of this README |
| Telemetry docs | `docs/telemetry/` | TBD | Signals, retention, review gates (directory referenced by Master Guide) |
| Telemetry schemas | `schemas/telemetry/` | TBD | JSON Schemas for telemetry payloads (directory referenced by Master Guide) |
| API boundary | `src/server/` (or repo-defined equivalent) | TBD | UI must emit via API/collector boundary (UI never reads Neo4j directly) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Directory layout section exists with emoji tree
- [ ] Clear rules for PII + sensitive-location handling
- [ ] Event naming + payload shaping guidance is explicit
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
| API boundary | `src/server/` | Contracted API layer (REST/GraphQL); may include telemetry ingest endpoints |

### Expected file tree for this sub-area

> Recommended structure. Some files may not exist yet (**not confirmed in repo**).

~~~text
web/src/telemetry/
├── 📄 README.md                  # This file (governed module guidance)
├── 📄 index.ts                   # Public exports (recommended)
├── 📄 init.ts                    # Initialize telemetry providers (recommended)
├── 📄 events.ts                  # Event name registry + payload builders (recommended)
├── 📄 redaction.ts               # Redaction helpers (recommended; required if telemetry enabled)
├── 📄 transport.ts               # Beacon/batch transport (recommended)
├── 📄 context.ts                 # Correlation + session context helpers (recommended)
├── 📁 providers/                 # Vendor adapters (recommended)
│   ├── 📄 noop.ts                # No-op provider (recommended)
│   └── 📄 otel.ts                # OpenTelemetry adapter (optional; not confirmed in repo)
└── 📁 __tests__/                 # Unit tests (recommended)
    └── 📄 redaction.test.ts      # Verify no PII / sensitive coords leak (recommended)
~~~

## 🧭 Context

### Background

KFM treats telemetry as a first-class subsystem (alongside data/catalog/graph/api/ui/story) with canonical references in `docs/telemetry/` and `schemas/telemetry/`. This UI module exists to ensure **frontend signals** are consistent with those system-wide contracts.

### Design goals

- **Schema-first:** telemetry payloads should be shaped to match `schemas/telemetry/**` (if present).
- **Privacy-first:** avoid collecting PII and avoid emitting precise coordinates for sensitive locations.
- **Low overhead:** telemetry must not materially degrade UI responsiveness.
- **Fail-safe:** telemetry failures must not block core UI functionality.

### Non-goals

- Replacing server-side observability.
- Persisting telemetry locally beyond short buffering needed for transport.
- Capturing raw user input, prompts, or narrative free text.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  U["User interaction"] --> UI["Web UI components"]
  UI --> T["web/src/telemetry: event and metric capture"]
  T --> R["Redaction and minimization"]
  R --> X["Transport: batch and beacon"]
  X --> API["Telemetry ingest boundary (API)"]
  API --> S[(Telemetry store and dashboards)]
  S --> G["Governance and reliability review"]
~~~

## 🧱 Architecture

### Layering rule (UI ↔ API boundary)

- UI telemetry is emitted outward via a **contracted boundary** (e.g., API endpoint / collector), never by direct graph access.
- Any telemetry requiring graph context should carry only **stable identifiers** (e.g., `story_node_id`, `stac_item_id`) and let the backend resolve details if allowed.

### Event naming and stability

Recommended pattern:

- Use stable, namespaced event names such as:
  - `ui.page_view`
  - `ui.layer_toggle`
  - `ui.focus_mode_open`
  - `ui.story_node_loaded`
  - `ui.api_request`
  - `ui.error_boundary`

> Event names above are examples; align to the repo’s canonical telemetry schema(s) if they exist.

### Minimal event envelope (recommended)

All events SHOULD carry:

- `event_name`
- `timestamp`
- `environment` (dev/staging/prod)
- `ui_version` (build/version string)
- `correlation_id` (random, per session or per interaction chain)
- `context` (safe identifiers only: layer IDs, Story Node IDs, STAC IDs)

### Example usage (pseudocode)

~~~ts
// Pseudocode — adapt to your actual telemetry API surface.
//
// import { initTelemetry, emitEvent } from "./telemetry";
//
// initTelemetry({ environment: "dev" });
//
// emitEvent("ui.layer_toggle", {
//   layer_id: "land-treaties",
//   enabled: true,
// });
~~~

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

This module is expected to support **Focus Mode UX signals**, such as:

- Focus Mode opened / closed
- Story Node loaded / rendered
- Evidence panel shown (by ID only)
- Redaction notice shown (when sensitive layers are generalized/masked)

### Provenance-linked narrative rule (telemetry alignment)

When emitting events tied to narrative or evidence:

- Prefer emitting **identifiers** (e.g., `story_node_id`, `dataset_id`, `stac_item_id`) rather than embedding narrative text.
- Never emit full STAC/PROV payloads from the client; emit IDs and let the server resolve if permitted.

### Optional structured controls

~~~yaml
# Optional (if you maintain a Focus Mode instrumentation registry)
focus_layers:
  - "layer:<layer-id>"
focus_time: "<iso8601>"
focus_center: "<coarse-or-redacted>"
~~~

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] Secrets scan (no tokens/keys in client code)
- [ ] PII scan (telemetry payloads must not contain emails, names, etc.)
- [ ] Sensitive-location scan (no precise restricted coords in payloads)
- [ ] Schema validation against `schemas/telemetry/**` (if present)
- [ ] Unit tests for redaction + payload shaping

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run frontend unit tests
# 2) run lint
# 3) run schema checks (telemetry schemas) if configured
~~~

### Telemetry signals (examples)

| Signal | Source | Where recorded |
|---|---|---|
| `ui.layer_toggle` | UI layer registry toggles | `docs/telemetry/` + `schemas/telemetry/` |
| `ui.focus_mode_open` | Focus Mode entry | `docs/telemetry/` + `schemas/telemetry/` |
| `ui.story_node_loaded` | Story Node fetch/render | `docs/telemetry/` + `schemas/telemetry/` |
| `ui.api_request` | API calls (latency/status) | `docs/telemetry/` + `schemas/telemetry/` |
| `ui.error_boundary` | Uncaught UI errors | `docs/telemetry/` + `schemas/telemetry/` |

> Keep the signal list aligned with the canonical telemetry docs/schemas (do not “invent” production signals without updating the schema + docs).

## 📦 Data & Metadata

### Allowed identifiers (preferred)

- `layer_id` (UI layer registry ID)
- `story_node_id` (Story Node identifier)
- `dataset_id` / `collection_id` (catalog identifiers)
- `stac_item_id` (STAC Item `id` only; avoid embedding full geometry)

### Prohibited payload fields (default)

- User-entered free text (search terms, prompts, notes)
- Email addresses, phone numbers, names, precise home/work addresses
- Authentication tokens, session cookies, request headers
- Exact coordinates for sensitive/protected locations (unless explicitly allowed by governance policy)

### Redaction strategy (recommended)

- Coarsen location signals (e.g., tile/region buckets) instead of raw lat/lon.
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
- When in doubt: **collect less**, generalize more, and document the decision in `docs/telemetry/`.

### AI usage constraints

- Allowed (documentation-only): summarization, structure extraction, translation, keyword indexing
- Prohibited: generating new policy; inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v0.1.0-draft | 2025-12-25 | Initial `web/src/telemetry/` README scaffold | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
