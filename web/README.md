---
title: "🌐 Kansas Frontier Matrix — Web Application & Focus Mode Platform (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"

review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle_stage: "LTS"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../releases/v11.2.6/manifest.zip"
telemetry_ref: "../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-readme-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"
signature_ref: "../releases/v11.2.6/signature.sig"
attestation_ref: "../releases/v11.2.6/slsa-attestation.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status_category: "Architecture"
doc_kind: "Architecture"
intent: "web-platform"
role: "architecture"
category: "Web · Architecture · UI · Focus Mode"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/README.md@v11.2.2"
  - "web/README.md@v11.2.1"
  - "web/README.md@v11.0.1"
  - "web/README.md@v11.0.0"
  - "web/README.md@v10.4.0"
  - "web/README.md@v10.3.2"
  - "web/README.md@v10.3.1"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/web-readme-v11.schema.json"
shape_schema_ref: "../schemas/shacl/web-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-readme-v11.2.6"
semantic_document_id: "kfm-doc-web-platform"
event_source_id: "ledger:web/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major KFM web platform protocol release"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application & Focus Mode Platform (v11)**  
`web/README.md`

Defines the **web-platform architecture + behavioral contract** for KFM v11, including:
React/TypeScript UI, 2D/3D rendering pipelines, **Focus Mode v3**, Story Node integration, STAC/DCAT exploration,
provenance overlays, accessibility-first patterns, governance hooks, and telemetry instrumentation.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../mcp/MCP-README.md)
· [![KFM‑MDP v11.2.6](https://img.shields.io/badge/KFM--MDP-v11.2.6-6b5b95)](../docs/standards/README.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-green)](../LICENSE)

</div>

---

## 📘 Overview

The **KFM Web Application** is the public-facing, governance-aware interface for exploring Kansas history and geospatial knowledge across **space + time + evidence**.

It integrates:

- 🗺️ **MapLibre GL** for 2D vector/raster cartography
- 🌍 **CesiumJS** for high-fidelity 3D terrain and deep-time exploration
- 🎯 **Focus Mode v3** for entity-centric reasoning and explainability (governance-filtered)
- 📖 **Story Nodes** as narrative units synchronized with map and timeline
- 📦 **STAC/DCAT Explorer** for dataset discovery, temporal slicing, and provenance-aware previews
- 🧠 **Graph-backed context** via **APIs** (no direct database access from the browser)
- 🕒 **Timeline Engine** with linked filtering across map, story, and datasets
- ♿ **A11y-first UI** targeting **WCAG 2.1 AA+**
- ⚖️ **Governance overlays** (CARE labels, provenance, masking indicators, SBOM/SLSA confidence cues)
- 📈 **Telemetry instrumentation** (performance + reliability + energy/carbon + governance signals)

### Purpose

This document defines the **non-negotiable contracts** for `web/**`:

- **Architecture contract**: what the web app is responsible for (and what it must not do).
- **Integration contract**: how the web app consumes KFM catalogs and APIs.
- **Governance contract**: how CARE, sovereignty, sensitivity, and provenance are surfaced and enforced.
- **Behavior contract**: canonical interactions (Explore → Focus → Story Node → Dataset).
- **Observability contract**: what events/metrics are emitted and what is prohibited.

### In scope

- UI pages, components, state management, and routing under `web/src/**`
- MapLibre + Cesium integration and visualization layers
- Focus Mode + Story Node presentation logic (UI-side)
- STAC/DCAT exploration and preview UX
- Governance overlays and user-facing explanations
- Telemetry emission from the browser (schema-governed)

### Out of scope

- ETL/AI pipelines and catalog generation (see `src/pipelines/**`, `mcp/**`, `tools/**`)
- Neo4j internals and graph write logic
- CI/CD definitions and release packaging details (`.github/**`, `releases/**`)
- Backend API implementation (see system/backend docs)

---

## 🗂️ Directory Layout

~~~text
📁 web/
├── 📄 README.md                       — Web platform architecture & behavioral contract (this file)
├── 📄 ARCHITECTURE.md                 — Detailed web/frontend architecture spec (implementation-level)
│
├── 📁 public/                         — Static assets (publicly served)
│   ├── 📁 images/                     — Images, screenshots, logos
│   ├── 📁 icons/                      — Icons & favicons
│   ├── 🧾 manifest.json               — PWA manifest (if applicable)
│   ├── 📄 robots.txt                  — Crawler rules
│   └── 📄 favicon.ico                 — Default favicon
│
├── 📁 src/                            — React/TypeScript SPA
│   ├── 📁 components/                 — Map, Focus, Story Nodes, overlays, dialogs
│   ├── 📁 pages/                      — Route-level containers (Explore, Focus, About, etc.)
│   ├── 📁 hooks/                      — Map/timeline/focus/story/data hooks
│   ├── 📁 context/                    — Theme, Focus, Time, A11y, Governance providers
│   ├── 📁 services/                   — API/STAC/DCAT clients + telemetry emitters
│   ├── 📁 utils/                      — Formatting, schema helpers, JSON-LD builders
│   └── 📁 styles/                     — CSS + design tokens + Map/3D theme glue
│
├── 🧾 package.json                    — Dependencies & npm scripts (authoritative)
├── 🧾 package-lock.json               — Deterministic dependency lock
└── 📄 vite.config.ts                  — Build configuration
~~~

If this layout changes, **update both**:

- `web/README.md` (this file)
- `web/ARCHITECTURE.md` (implementation-level details)

---

## 🧭 Context

KFM is pipeline-driven and documentation-dependent:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

The web layer sits at the final stage of this chain and has one overriding rule:

- **The browser never talks to Neo4j directly.** Graph access occurs only through governed APIs.

### Primary integration points (monorepo)

- `schemas/**` — JSON/SHACL schemas (docs + Story Nodes + telemetry)  
- `docs/standards/**` — Governance + FAIR+CARE + sovereignty + accessibility standards  
- `releases/**` — Certified release artifacts (SBOM, manifest, signatures, telemetry snapshots)  
- `data/**` — Canonical datasets + STAC/DCAT catalogs (served via APIs or static hosting)  
- `src/**` — Backend services, pipelines, graph loaders, shared theming/tokens  
- `.github/**` — CI/CD pipelines and validation gates  

---

## 🧱 Architecture

### Architectural invariants (MUST)

1. **No direct graph access:** the UI MUST NOT ship Neo4j credentials or connect to Neo4j from the browser.
2. **Governance-first rendering:** any governed content MUST be accompanied by:
   - provenance affordances (source / dataset references), and
   - visible CARE + sensitivity cues when applicable.
3. **Clear content-type separation:** the UI MUST visually distinguish:
   - archival/source material,
   - derived/model outputs,
   - AI-generated text (Focus Mode).
4. **A11y baseline:** core flows MUST be usable with keyboard-only navigation and screen readers.
5. **Telemetry discipline:** telemetry MUST be schema-governed, aggregated, and avoid PII.

### Major UI subsystems

- **MapView (MapLibre GL)**  
  2D map rendering, layer compositing, selection/highlight, and footprint display.

- **CesiumView (3D)**  
  Terrain and 3D/temporal visualization for deep-time exploration and narrative fly-throughs.

- **TimelineView**  
  Temporal brushing, zooming, and linked filtering across map, datasets, and narratives.

- **FocusPanel (Focus Mode v3)**  
  Governance-filtered “explain the focus” interface: summary, evidence, provenance, and user actions.

- **Story Node UI**  
  Narrative units rendered as cards/overlays tied to time ranges, spatial footprints, and graph relations.

- **Catalog Explorer (STAC/DCAT)**  
  Dataset discovery + preview with license, lineage, and time slicing.

- **Governance Overlay Layer**  
  CARE labels, sovereignty notices, masking indicators, and user-facing “why limited” explanations.

### Data access pattern

The web app accesses KFM through **governed API surfaces**:

- REST endpoints (typical for read-only resources and catalog search)
- GraphQL (typical for entity-centric queries and Focus Mode context bundles)
- JSON-LD (typical for semantically meaningful exports and provenance bundles)
- STAC/DCAT endpoints (collection/item/dataset browsing)

Caching and prefetching MAY be used for performance, but MUST NOT bypass governance enforcement.

---

## 🗺️ Diagrams

### System boundary and data flow

~~~mermaid
flowchart TD
  subgraph UI["UI Layer · web/ · React/TypeScript"]
    MV["MapView · MapLibre GL"]
    CV["CesiumView · 3D"]
    TL["TimelineView"]
    FP["FocusPanel · Focus Mode v3"]
    SN["Story Nodes · Cards/Overlays"]
    LX["Catalog Explorer · STAC/DCAT"]
    GOV["Governance Overlay"]
  end

  UI --> AC["API Client Layer · REST/GraphQL/JSON-LD"]
  UI --> SC["Catalog Client · STAC/DCAT"]

  AC --> API["Backend APIs · governed access"]
  API --> KG["Knowledge Graph · Neo4j (server-side only)"]
  API --> LEDGER["Governance ledgers · FAIR+CARE / SBOM / SLSA"]

  SC --> CATALOGS["Catalogs · STAC 1.0 / DCAT 3.0"]
  API --> CATALOGS

  UI --> OTEL["Telemetry Emitters · browser events"]
  OTEL --> TEL["Telemetry Backend · focus-telemetry.json (release snapshot)"]
~~~

### Interaction loop (Explore → Focus → Evidence)

~~~mermaid
sequenceDiagram
  autonumber
  participant U as User
  participant M as Map/Timeline
  participant F as FocusPanel
  participant A as API Layer
  participant C as STAC/DCAT

  U->>M: Select feature / time range
  M->>A: Request focus context (entity + relations + governance flags)
  A-->>F: Return context bundle (governed)
  F->>C: Request supporting datasets (STAC/DCAT refs)
  C-->>F: Dataset metadata + preview links
  F-->>U: Summary + evidence + provenance + "why limited" (if needed)
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes (UI contract)

Story Nodes are the narrative glue between map, timeline, and evidence. The UI MUST:

- Render Story Nodes as **structured narrative units** (title + body + metadata).
- Treat Story Node properties as **data**, not free-form markup:
  - display provenance annotations and dataset references as first-class affordances
  - reflect masking/generalization flags in both map footprints and narrative copy
- Support linked interaction:
  - hover/click Story Node ↔ highlight footprint on map
  - select Story Node ↔ align timeline to Story Node time range
  - open Story Node ↔ reveal supporting datasets and relations

### Focus Mode v3 (UI contract)

Focus Mode is AI-assisted but governance-constrained. The UI MUST:

- Clearly label AI-generated text and provide:
  - “Show supporting data”
  - “Why am I seeing this?”
  - provenance chips (dataset IDs / sources)
- Display fallbacks when content is limited:
  - “Content is generalized/redacted due to sovereignty/sensitivity policy.”
  - “This summary is limited to permitted transforms.”
- Enforce the declared transform policy:
  - Allowed: summaries, semantic highlighting, a11y adaptations, diagram/metadata extraction
  - Prohibited: speculation, unverified claims, governance override, altering governed content

### Error handling and safe degradation

When APIs or catalogs fail:

- The UI MUST fail “softly” (error boundary + retry) without showing partial/unsafe content.
- The UI MUST keep governance overlays visible even in degraded states.
- Telemetry SHOULD record:
  - error type (coarse, non-sensitive)
  - component boundary where it occurred
  - whether fallbacks were used

---

## 🌐 STAC, DCAT & PROV Alignment

The web app is a first-class catalog consumer.

### STAC browsing (spatiotemporal assets)

The UI SHOULD support:

- Collection browsing and Item search (space + time filters)
- Footprint display and temporal slicing
- Asset preview where permitted (thumbnails/tiles) and clear affordances for downloads
- Linking from assets back to provenance and governance summaries

### DCAT browsing (dataset-level metadata)

The UI SHOULD support:

- Dataset discovery by keyword, theme, license, and steward
- Visible licensing and use constraints
- Clear mapping from dataset metadata to the underlying STAC Collections/Items

### PROV (lineage and explainability)

When provenance is available, the UI SHOULD surface:

- derivation chains (what this came from)
- generating activities (what process produced it)
- version relationships (predecessor/successor where provided)

This section is contract-level; implementation details belong in `web/ARCHITECTURE.md`.

---

## 📦 Data & Metadata

### Machine-extractable document metadata

This README includes front-matter intended for:

- governance review workflows
- automated schema validation
- release packaging and integrity checks

Do not remove required fields. If fields are unknown at author time (e.g., `commit_sha`), keep approved placeholders.

### UI metadata principles

- Prefer **IDs and references** over duplicated titles/labels.
- Preserve stable identifiers across releases for:
  - Story Nodes
  - dataset references
  - provenance entities
- Treat any coordinate-like data as potentially sensitive and render it through the governance layer.

---

## 🧪 Validation & CI/CD

Changes under `web/**` MUST remain CI-clean.

Required validation categories typically include:

- **Type safety** (TypeScript compilation)
- **Linting** (style + a11y + unsafe patterns)
- **Unit + integration tests** (map–timeline–focus–story interactions)
- **E2E tests** for canonical flows (Explore → Focus → Story Node → Dataset)
- **Telemetry schema validation** (events conform to governed schemas)
- **Accessibility checks** (automated + spot manual on critical paths)
- **Supply-chain checks** (SBOM, signatures, attestations at release time)

See `.github/workflows/**` and `web/package.json` for authoritative commands and gates.

---

## ⚖ FAIR+CARE & Governance

The web platform is a governance surface, not just a UI.

### Required user-facing governance cues

When content is governed, the UI MUST make it legible:

- CARE label + sensitivity cues
- provenance and steward cues
- masking/generalization indicators
- “why limited” explanations (actionable, not cryptic)

### Sovereignty and protected knowledge

Where sovereignty policy applies:

- Default to **generalization over precision**
- Avoid UI affordances that imply hidden precision can be extracted
- Ensure any export/download actions reflect the same governance rules

### Telemetry privacy

Telemetry MUST:

- avoid PII (including raw identifiers, exact user paths, or precise protected coordinates)
- favor aggregated counts and coarse buckets
- remain schema-governed and versioned per release

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-15 | Updated to KFM‑MDP v11.2.6 heading/section rules; tightened web→API boundary language; expanded governance + catalog + telemetry contracts. |
| v11.2.2 | 2025-11-30 | Aligned with KFM‑MDP v11.2.2; added signature/attestation, energy/carbon v2, AI behavior constraints. |
| v11.2.1 | 2025-11-28 | Updated metadata, directory layout, and architecture narrative; synced with Focus Mode v3. |
| v11.0.1 | 2025-11-27 | Web platform refinement; clarified Focus Mode v3 + Story Node contracts. |
| v11.0.0 | 2025-11-24 | v11 upgrade; integrated Focus Mode v3, Story Node integration, STAC/DCAT explorer, and telemetry v11. |
| v10.4.0 | 2025-11-15 | v10.4 architecture; Focus v2.5, Story Node v3, telemetry v3, FAIR+CARE overlays. |
| v10.3.2 | 2025-11-14 | Deep rebuild; 3D integration and initial STAC/DCAT explorer flows. |
| v10.3.1 | 2025-11-13 | Early v10.3 web architecture and accessibility improvements. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[⬅️ Back to Repo Root](../README.md) · [🧭 System Architecture](../ARCHITECTURE.md) · [🧱 Web Architecture](./ARCHITECTURE.md) · [⚖ Governance](../docs/standards/governance/ROOT-GOVERNANCE.md) · [🧑🏽‍⚖️ FAIR+CARE](../docs/standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Sovereignty](../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>