---
title: "💻 Kansas Frontier Matrix — Web Source Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"

review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-src-overview"
role: "overview"
category: "Web · Source · Architecture · UI"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-readme-v11.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

data_contract_ref: "../../docs/contracts/data-contract-v3.json"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/README.md@v11.2.2"
  - "web/src/README.md@v11.0.0"
  - "web/src/README.md@v10.4.2"
  - "web/src/README.md@v10.3.2"
  - "web/src/README.md@v10.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../schemas/json/web-src-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/web-src-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-src-readme:v11.2.6"
semantic_document_id: "kfm-doc-web-src-readme"
event_source_id: "ledger:web/src/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next web/src overhaul"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Source Overview (v11.2.6)**
`web/src/README.md`

**Purpose**  
Provide a FAIR+CARE-governed overview of `web/src/**`, the **frontend application layer** of the Kansas Frontier Matrix (KFM) Web Platform.

This directory is the **UI stage** of the KFM system flow:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI (this directory) → Story Nodes / Focus Mode**

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../mcp/MCP-README.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)

</div>

---

## 📘 Overview

`web/src/**` contains the **core React/TypeScript source** for the KFM Web Platform. It is responsible for:

- **Interactive mapping and visualization**
  - 2D cartography (MapLibre GL or equivalent)
  - Optional 3D exploration (CesiumJS or equivalent)
- **Timeline-driven navigation**
  - Filtering map layers and narrative elements by time (year/era/range)
- **Narrative systems**
  - **Story Nodes (v3)** rendered as cards, detail views, and overlays
  - **Focus Mode (v3)** entity-centric reasoning UI with explorable explanations
- **Catalog discovery**
  - STAC Collections/Items and DCAT Datasets browsing, preview, and attribution
- **Governed presentation**
  - CARE labels, sovereignty signals, provenance visibility, and masking/generalization indicators
- **Accessibility**
  - WCAG 2.1 AA+ interaction patterns and alternatives for map/3D experiences
- **Telemetry**
  - Performance + interaction telemetry (schema-validated, aggregated, non-PII)

This overview is intentionally **source-focused**. For architecture enforcement details, see:

- `web/src/ARCHITECTURE.md` (source-level architecture)
- `web/ARCHITECTURE.md` (web subsystem architecture)
- `web/README.md` (platform behavioral contract)

---

## 🗂️ Directory Layout

The `web/src/` subtree is organized around a **layered + feature-oriented** model.

~~~text
web/src/
├── 📄 README.md                          # This overview (governed)
├── 🧱 ARCHITECTURE.md                    # Source-level architecture spec (governed)
│
├── 🚀 main.tsx                           # SPA bootstrap
├── 🧩 App.tsx                            # App shell + routing composition
│
├── 📄 pages/                             # Route-level views (Explore, Focus, About, etc.)
│
├── 🧱 components/                        # UI components (React)
│   ├── 🗺️ map/                           # Map views + map controls + layer rendering
│   ├── 🌍 cesium/                        # 3D view + deep-time camera controls (if enabled)
│   ├── 🕒 timeline/                      # Timeline UI + brushes + playback (if enabled)
│   ├── 🎯 focus/                         # Focus Mode panels + explainability widgets
│   ├── 📖 story/                         # Story Node cards + detail views + relations
│   ├── 📦 catalogs/                      # STAC/DCAT explorer widgets + dataset previews
│   ├── ⚖️ governance/                    # CARE labels + provenance chips + masking notices
│   ├── ♿ a11y/                           # Accessible primitives + map/3D alternatives
│   └── 🧩 shared/                        # Reusable primitives (buttons, dialogs, tabs, icons)
│
├── 🧠 context/                           # Shared state providers (Time/Focus/Governance/A11y/etc.)
├── 🧵 hooks/                             # Side-effect logic + orchestration helpers (React hooks)
├── 🔁 pipelines/                         # Multi-step flows (Focus/Story/Catalog/Timeline coordination)
├── 🌐 services/                          # Typed API clients (REST/GraphQL/STAC/DCAT/Telemetry)
├── 🧾 types/                             # TypeScript domain + DTO contracts
├── 🛠 utils/                             # Pure helpers (guards, formatters, geo/time helpers)
└── 🎨 styles/                            # Design tokens + themes + global/map styles
~~~

**Structural governance:** If the tree changes, it must be updated here **and** in:

- `web/src/ARCHITECTURE.md`
- `web/ARCHITECTURE.md`
- `web/README.md`

---

## 🎯 Purpose

This README exists to make `web/src/**` **safe to evolve** while staying compliant with KFM’s governed constraints.

It defines:

- What belongs in `web/src/**` (and what must live elsewhere)
- Layer boundaries (components ↔ hooks ↔ services ↔ APIs)
- Data-flow expectations (static-first + API fallback)
- Non-negotiables for governance, accessibility, telemetry, and determinism

### Scope boundaries

**In scope (this directory):**

- Presentation/UI logic, theming, and accessible interaction patterns
- Client-side coordination of map/timeline/story/focus state
- Typed clients for backend endpoints and catalogs
- Telemetry instrumentation and error boundaries

**Out of scope (elsewhere in repo):**

- ETL processing and catalog generation (see `src/pipelines/**`, `data/**`)
- Knowledge graph storage or direct Cypher/Neo4j access (backend only)
- Governance decision logic (server/ledger; UI only renders outcomes)
- Release packaging and attestations (see `releases/**`, `.github/**`)

---

## 🧱 Architecture

`web/src/**` follows a strict “UI behind APIs” and “governed rendering” model.

### Layering contract

1. **Presentation layer** (`components/`, `pages/`)
   - Renders UI from typed inputs and context state
   - No direct backend calls

2. **State layer** (`context/`, selected `hooks/`)
   - Owns shared state and synchronization rules:
     - time ↔ map ↔ story ↔ focus ↔ catalogs
   - Prevents “shadow state” drift across features

3. **Orchestration layer** (`pipelines/`)
   - Multi-step flows (fetch → validate → reconcile → update contexts)
   - Centralizes non-trivial coordination logic

4. **Integration layer** (`services/`)
   - Typed DTO boundaries for:
     - REST/GraphQL APIs
     - STAC/DCAT catalogs
     - Telemetry emission
   - Normalizes errors and enforces schema/guard checks

5. **Support layer** (`types/`, `utils/`, `styles/`)
   - Types, runtime guards, formatting helpers, theming primitives
   - Must remain deterministic and testable

### Cross-repo alignment

`web/src/**` must remain aligned with:

- Shared **design tokens** and theming standards (see `src/design-tokens/**` and `src/theming/**`)
- Shared iconography where applicable (see `src/icons/**`)
- Catalog standards and generated assets (see `data/stac/**`, DCAT materializations, and release artifacts)

### Architecture invariants

- **No direct graph access:** frontend never connects to Neo4j or runs Cypher.
- **No governance overrides:** if the backend masks/denies content, the UI must not reconstruct it.
- **No speculative UI fabrication:** UI may not “fill gaps” for governed historical claims.
- **Determinism:** given the same inputs, UI state transitions should be repeatable.

---

## 🧩 Components

The component system is organized around KFM’s core experiences.

### Map experience

- 2D map view with:
  - base maps (modern imagery, historical map layers)
  - vector/raster overlays and legends
  - selection and hover behavior tied to Focus/Story state
- Optional 3D view (if enabled) with reduced-motion compliance

### Timeline experience

- Time range selection and brushing
- Timeline-driven filtering for:
  - map layers
  - Story Node lists and highlights
  - Focus Mode context inputs

### Narrative experience

- Story Node lists/cards (overview) and detail views (full narrative + provenance)
- Relationship panels linking story ↔ entities ↔ datasets

### Catalog experience

- STAC/DCAT explorers with:
  - filtering (time/space/category/license)
  - previews (tiles/COGs/vector tiles)
  - attribution and provenance surfacing

### Governance experience

- Unified “governance overlay” patterns:
  - CARE label chips
  - sovereignty flags/heritage notices
  - masking/generalization notices (including “why” affordances)
  - license and attribution display

---

## 🗺️ Data Flows

The KFM frontend is designed to be fast, portable, and reproducible by prioritizing **static artifacts** generated by pipelines, with **API fallback** for dynamic queries.

### Static-first ingestion

Primary data consumption patterns include (depending on dataset type):

- Pre-generated JSON/JSON-LD indexes and catalogs
- Vector tiles / tile manifests
- Raster assets optimized for web delivery (e.g., COG-like patterns)
- STAC Collections/Items and derived DCAT views

Static-first enables:

- Lightweight deployment (static hosting compatible)
- Predictable caching behavior
- Reduced backend dependency for common exploration flows

### Dynamic API fallback

When dynamic querying is required (e.g., complex graph traversal, spatial proximity, filtered search), the UI calls approved endpoints via the `services/` layer:

- Time-range queries (entities/events within an interval)
- Location queries (viewport bbox, region, proximity)
- Search queries (full-text or relevance-scored results)
- Focus Mode retrieval (governance-filtered narratives and evidence lists)

### Search index pattern

Where supported, the UI may load a pre-built search index (as static JSON) for fast client-side filtering, and fall back to an API endpoint when query complexity exceeds client-side constraints.

### Validation and safety

All inbound data must be treated as untrusted:

- Validate DTOs at runtime (guards/schemas) before rendering
- Apply governance metadata as a first-class input to rendering decisions
- Never render disallowed precision (coordinates, media, identifiers) when policy indicates masking/generalization

~~~mermaid
flowchart LR
  A["Pipeline Outputs · data/**"] --> B["Static Artifacts · JSON · Tiles · STAC/DCAT"]
  B --> C["web/src Services · Typed Clients"]
  C --> D["Pipelines · Orchestrators"]
  D --> E["Contexts · Time · Focus · Governance · A11y"]
  E --> F["Components · Map · Timeline · Story · Focus · Catalogs"]

  C --> G["Backend APIs · REST/GraphQL/JSON-LD"]
  G --> D
~~~

---

## 🧠 Focus Mode

`web/src/**` implements the **Focus Mode v3 UI surface** (selection, navigation, presentation), while the **governed reasoning output** is produced and filtered server-side.

### UI responsibilities

- Render Focus narratives with clear labeling:
  - archival / curated text
  - AI-generated or AI-assisted explanations
- Always show evidence affordances:
  - provenance chips
  - supporting datasets/documents list
  - “Why am I seeing this?” explanations

### Guardrails

- No client-side invention of historical facts
- No “shadow” reasoning that bypasses backend governance filters
- No exposure of masked/denied identifiers (including precise location leakage through UI affordances)

---

## 📖 Story Nodes

Story Nodes are the system’s primary narrative unit and must be rendered as governed, evidence-led artifacts.

### Required UI elements

- Title, summary, temporal range
- Spatial footprint preview (with masking/generalization when required)
- Provenance and attribution
- Governance signals (CARE label, sovereignty flags, sensitivity)

### Synchronization contract

Story selection must synchronize:

- Timeline time window → story’s temporal range
- Map highlight → story footprint
- Focus context → optional (depending on current mode)

---

## 📦 STAC & DCAT

The web source layer supports dataset discovery and preview through STAC/DCAT-aligned experiences.

### STAC (asset-level)

- Browse Collections/Items
- Preview assets on the map/3D view (subject to governance)
- Link Items to provenance and derived outputs

### DCAT (dataset-level)

- Browse datasets/distributions
- Surface license and attribution requirements
- Highlight FAIR+CARE metadata fields when available

### Governance-aligned previews

- Sensitive layers must preview only with approved generalization/masking
- License and provenance must remain visible at preview time (not hidden in secondary screens)

---

## ⚖️ Governance

The UI layer **renders** governance outcomes; it does not decide them.

### Required governance behaviors

- CARE labels visible wherever governed content is displayed
- Sovereignty notices rendered where applicable
- Masking/generalization clearly indicated and not user-disableable when policy requires

### Prohibited behaviors

- “Hide governance overlay” toggles for governed assets
- UI features that reconstruct sensitive detail from derived cues
- Downplaying or suppressing license/attribution visibility

---

## ♿ Accessibility

`web/src/**` must uphold **WCAG 2.1 AA+** with special attention to map and 3D experiences.

### Core requirements

- Full keyboard navigation (no trapped focus)
- Screen reader support with semantic landmarks and robust labels
- Reduced motion support for:
  - animations
  - timeline playback (if enabled)
  - camera fly-throughs (3D)

### Map and 3D accessibility

- Provide accessible alternatives where direct canvas interaction is insufficient:
  - textual summaries
  - list-based navigation for selected features
  - keyboard-operable controls where feasible

---

## 📈 Telemetry

Telemetry is mandatory and schema-governed.

### What is emitted

- Performance metrics (route transitions, render cost, WebVitals where available)
- Feature usage events (aggregated)
- A11y preference signals (high contrast, reduced motion)
- Focus Mode success/failure and fallback events
- Governance-dependent masking events (aggregated)

### Privacy + governance rules

- No PII
- No user-identifying session fingerprints
- No raw content capture from governed narratives
- Validate payloads against `telemetry_schema` before emission

---

## 🧪 Testing

`web/src/**` changes must be supported by tests aligned to the risk profile of the change.

### Minimum expectations

- Unit tests for components/hooks/utils (deterministic behavior)
- Integration tests for cross-feature synchronization:
  - map ↔ timeline ↔ story ↔ focus ↔ catalogs
- Accessibility checks (automated + targeted manual checks for key flows)
- Telemetry event shape validation (schema conformance)
- Governance rendering checks (masking and labels appear when required)

No PR should merge if it breaks:

- governance overlays
- accessibility baselines
- telemetry schema validation
- time/focus/story synchronization invariants

---

## 🕰️ Version History

| Version  | Date       | Summary |
|---------:|------------|---------|
| v11.2.6  | 2025-12-15 | KFM-MDP v11.2.6 compliance update (heading registry + fence profile); clarified static-first data flows + API fallback; strengthened governance/A11y/telemetry invariants. |
| v11.2.2  | 2025-11-28 | Upgraded metadata & directory layout to v11.2.2; aligned with root & web READMEs; clarified governance/A11y/telemetry roles. |
| v11.0.0  | 2025-11-24 | Upgraded to KFM-MDP v11; clarified layers, enforcement rules, telemetry v11 references. |
| v10.4.2  | 2025-11-15 | Expanded directory descriptions; labeled sources; aligned with KFM-MDP v10.4.1. |
| v10.3.2  | 2025-11-14 | Added governance & accessibility enhancements; improved Focus/Story integration. |
| v10.0.0  | 2025-11-09 | Initial v10 Web Source overview; base React/TS structure and map/timeline scaffolding. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned

[⬅️ Back to Web Platform Overview](../README.md) ·
[🧱 Source Architecture Spec](ARCHITECTURE.md) ·
[🧭 System Architecture](../../ARCHITECTURE.md) ·
[🛡 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>