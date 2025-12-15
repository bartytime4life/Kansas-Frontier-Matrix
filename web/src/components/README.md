---
title: "🧩 Kansas Frontier Matrix — Web Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/README.md"
version: "v11.2.3"
last_updated: "2025-12-15"

review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle_stage: "LTS"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-components-readme-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"
signature_ref: "../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../releases/v11.2.2/slsa-attestation.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

header_profile: "standard"
footer_profile: "standard"
layout_profile: "immediate-one-branch-with-descriptions-and-emojis"
fencing_profile: "outer-backticks-inner-tildes-v1"

status_category: "Overview"
doc_kind: "Overview"
intent: "web-components-overview"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (unless displaying CARE-masked data)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/components/README.md@v10.3.1"
  - "web/src/components/README.md@v10.3.2"
  - "web/src/components/README.md@v10.4.0"
  - "web/src/components/README.md@v10.4.1"
  - "web/src/components/README.md@v11.2.2"

ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/web-components-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-components-readme-shape.ttl"

doc_uuid: "urn:kfm:doc:web-components-readme-v11.2.3"
semantic_document_id: "kfm-doc-web-components-readme"
event_source_id: "ledger:web/src/components/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"

ttl_policy: "Review each release"
sunset_policy: "Superseded upon next component-layer revision"

ai_notes: "Components are presentation-layer only. Do not move API logic into components; do not invent governance states; do not imply spatial/temporal precision beyond what upstream layers provide."
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Web Components Overview (v11.2.3)**
`web/src/components/README.md`

**Purpose**  
Provide the authoritative, FAIR+CARE-aligned directory and structural overview for UI components
within the Kansas Frontier Matrix Web Platform. This document defines the canonical component
hierarchy, responsibilities, accessibility requirements, governance rules, and telemetry expectations
for everything under `web/src/components/**`.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

All UI components inside `web/src/components/**` are **presentation-layer building blocks**:

- They render UI and handle local interactions (keyboard, pointer, focus management).
- They receive **data via props** from higher layers (features, hooks, context, pipelines).
- They must remain **deterministic and testable** (stable rendering for the same props).
- They integrate with the platform’s core UX surfaces:
  - 🗺️ Map views (MapLibre, optional Cesium integration)
  - 🕒 Timeline controls and time filtering
  - 🎯 Focus Mode v3 panels and explainability views
  - 📖 Story Node v3 cards and detail views
  - 📦 STAC/DCAT dataset browsing and preview UI
  - ⚖ Governance overlays (CARE labels, masking/generalization, provenance visibility)

Components MUST NOT:

- Call backend APIs directly (no `fetch`, no GraphQL clients, no service calls).
- Implement business logic, ontology mapping, or data normalization (use `web/src/utils/**` upstream).
- Override governance decisions (masking, CARE labels, sovereignty flags, visibility constraints).

Components SHOULD:

- Surface governance context clearly (not hidden behind optional UI).
- Provide consistent semantics for headings, landmarks, and interaction patterns.
- Preserve user trust by avoiding UI that implies precision not present in the data.

---

## 🗂️ Directory Layout

~~~text
web/src/components/
├── 📄 README.md                 # This file — component architecture & rules
│
├── 📁 map/                      # Map containers, controls, legend UI, overlays (MapLibre/Cesium)
├── 📁 timeline/                 # Timeline axis, range sliders, markers, time filters, A11y helpers
├── 📁 focus/                    # Focus Mode v3 panels, relations views, provenance/explainability UI
├── 📁 story/                    # Story Node v3 cards, detail panes, media shells, relation lists
├── 📁 governance/               # CARE badges, sovereignty notices, masking indicators, provenance UI
├── 📁 stac/                     # Dataset cards, item previews, asset metadata, extent previews
├── 📁 layout/                   # App shells, panels, split views, page wrappers, responsive scaffolds
└── 📁 shared/                   # Low-level UI primitives (buttons, forms, tabs, modals, loaders, etc.)
~~~

Top-level categories are **governed**. New categories require web architecture review and updates to
this README.

---

## 🧭 Context

`web/src/components/**` sits downstream of the web platform’s data and governance layers.

Typical data flow (conceptual):

~~~text
API / Catalog / Static Assets
  → web/src/utils/**           (guards, normalization, temporal/spatial safety, URL rules)
    → web/src/features/**      (business logic + orchestration; e.g., Focus Mode feature module)
      → web/src/components/**  (presentation + interactions only)
~~~

Key boundary rules:

- The frontend may load **static catalogs** (e.g., STAC/DCAT JSON) and/or call lightweight APIs.
- Any data that reaches components must already have:
  - schema validation completed (guards),
  - governance flags attached (CARE, sovereignty, sensitivity),
  - masking/generalization applied where required,
  - provenance identifiers available for display (where policy requires it).

This separation keeps UI modular and reduces the risk of accidental governance bypass.

---

## 🗺️ Diagrams

High-level layering for UI composition:

~~~text
┌────────────────────────────────────────────────────────────────┐
│  Pages / Routes (web/src/*)                                    │
│    └─ Feature Modules (web/src/features/**)                    │
│        └─ Components (web/src/components/**)                   │
│            ├─ domain components (map/timeline/focus/story/…)   │
│            └─ primitives (shared/)                             │
└────────────────────────────────────────────────────────────────┘
             ↑ props/data only        ↓ callbacks/events only
┌────────────────────────────────────────────────────────────────┐
│  Utilities + Guards + Normalizers (web/src/utils/**)           │
│  Governance metadata / masking decisions provided upstream      │
└────────────────────────────────────────────────────────────────┘
~~~

---

## 🧱 Architecture

### Core responsibilities

Components are responsible for:

- Rendering: layout, styling, and visual hierarchy.
- Interaction: keyboard/mouse/pointer events, focus traps, roving tabindex patterns.
- A11y: correct landmark roles, labels, descriptions, and focus indicators.
- Presenting governance: CARE labels, provenance chips/trails, masking notices.

Components are not responsible for:

- entity resolution (graph lookups),
- catalog parsing (STAC/DCAT),
- provenance construction (PROV),
- masking decisions,
- telemetry schema construction (use shared hooks/utilities).

### Integration boundaries

Components should follow these conventions:

- Inputs:
  - typed props only (validated upstream),
  - include governance metadata when rendering governed content.
- Outputs:
  - callbacks for user actions (e.g., `onSelectEntity(id)`),
  - never return raw network responses.
- State:
  - local UI state only (expanded/collapsed, active tab, focused index),
  - feature-level state lives in feature modules or context providers.

### Category guidance

#### `map/` — Map & spatial UI

Responsibilities:

- Mount and layout MapLibre (and optional Cesium viewports where used).
- Provide user controls: zoom, rotate, reset, layer toggles.
- Render overlays supplied by upstream layers:
  - Story Node geometries
  - Focus highlights
  - Dataset footprints
  - Sovereignty masking/generalization grids (if present)

Requirements:

- Respect generalized/masked geometries exactly as provided.
- Avoid UI that implies “exact location” unless governance explicitly allows it.
- Provide screen-reader-friendly summaries where feasible (e.g., “3 layers visible; 2 markers selected”).

#### `timeline/` — Temporal UI

Responsibilities:

- Render timeline axis and selection controls (range sliders, brushes).
- Display markers for events, Story Nodes, and dataset temporal extents.
- Synchronize with map selection via props and callbacks (not via direct imports).

Requirements:

- Full keyboard support (handles, controls, tab order).
- Expose ARIA descriptions for current range, selection, and “play/animate” controls if present.
- Do not sharpen fuzzy/approximate temporal ranges into day-level precision.

#### `focus/` — Focus Mode v3 UI

Responsibilities:

- Present the Focus Mode layout: header, tabs, relation panels, narrative blocks.
- Render provenance and “why am I seeing this?” explainers when supplied.
- Display explainability artifacts if present (without inventing or recomputing them).

Requirements:

- Clearly label AI-assisted content when present.
- Keep the evidence trail visible (provenance chips, source links/IDs).
- Provide safe controls to expand/collapse related entity clusters.

#### `story/` — Story Node v3 UI

Responsibilities:

- Story cards and story detail panes: title, narrative, citations/evidence links.
- Relation lists and context panels (related entities, datasets, documents).
- Media shells (images/figures) when allowed by governance.

Requirements:

- Always render CARE labels / sovereignty notices when provided.
- Never show precise coordinates for restricted Story Nodes; do not imply precision in captions.
- Keep structure consistent: clear headings, short summaries, scannable evidence blocks.

#### `governance/` — Governance & CARE presentation

Responsibilities:

- CARE classification badges and labels.
- License tags (SPDX-style where possible).
- Provenance chips/trails and “source/evidence” display UI.
- Sovereignty notices and masking indicators.

Requirements:

- Governance overlays are non-optional when policy requires them.
- Indicators must be prominent enough to prevent user misunderstanding.
- No “silent downgrade” UI (e.g., hiding a masking notice due to layout constraints).

#### `stac/` — STAC/DCAT dataset exploration UI

Responsibilities:

- Dataset cards, lists, and previews.
- Asset metadata display (type, role, license, size/format when available).
- Spatial/temporal extent visualization (as provided).

Requirements:

- Always show license and governance labels when available.
- Respect dataset-level masking/generalization rules (aggregated footprints, blurred extents).
- Avoid claiming catalog completeness if the catalog is partial.

#### `layout/` — Layout & shell components

Responsibilities:

- App scaffolding: header/nav/main layout, sidebars, drawers, split panes.
- Responsive behavior: mobile-safe panels, focus management for overlays.

Requirements:

- Proper landmarks (`header`, `nav`, `main`, `aside`) and heading hierarchy.
- Works cleanly with screen readers and keyboard navigation.
- Reduced-motion support where animations exist.

#### `shared/` — UI primitives

Responsibilities:

- Buttons, inputs, tabs, modals, tooltips, spinners, badges.
- Form controls and accessibility-first interaction patterns.

Requirements:

- A11y-first primitives reused by higher-level components.
- Small, local state only; no service imports.
- Stable semantics so higher-level components remain predictable.

---

## 🧠 Story Node & Focus Mode Integration

Components that render Story Node v3 and Focus Mode v3 content must preserve the platform’s core
trust contract:

- Distinguish clearly between:
  - facts (supported by evidence),
  - interpretation (reasoned from evidence),
  - speculation (explicitly hypothetical, if permitted).
- Provide visible provenance affordances:
  - provenance chips,
  - “show supporting data” controls,
  - evidence IDs or links supplied upstream.
- Label AI-assisted segments clearly and avoid presenting them as primary evidence.
- Never fabricate relationships, citations, or governance status in the UI.

---

## 🌐 STAC, DCAT & PROV Alignment

When components display catalogs and governed content:

- STAC-facing UI should treat Items/Collections as first-class, not ad-hoc JSON blobs.
- DCAT-facing UI should surface: title, description, publisher/creator, license, temporal/spatial coverage.
- PROV-facing UI should support traceability:
  - what artifact is shown,
  - what it was derived from (if provided),
  - which run/activity generated it (if provided).

UI must remain faithful to upstream metadata:
- do not infer missing licenses,
- do not generate provenance chains in the component layer,
- do not collapse “unknown” into a confident value.

---

## ⚖ FAIR+CARE & Governance

Components that render governed data must:

- Display CARE classification and sovereignty indicators when provided.
- Display provenance and license where policy requires it.
- Respect masking/generalization:
  - do not expose restricted coordinates,
  - do not reveal restricted IDs in copy/pasteable surfaces,
  - do not suggest exactness with UI affordances (pins, “navigate to exact point”, etc.).
- Uphold AI restrictions:
  - Allowed: semantic highlighting, A11y adaptations, diagram/metadata extraction.
  - Prohibited: speculative additions, unverified historical claims, governance override, content alteration.

Any attempt to bypass governance (even accidentally via UI) is a release-blocking issue.

---

## 📦 Data & Metadata

### Telemetry expectations

Components that emit interaction telemetry should:

- Use shared telemetry hooks/utilities (not ad-hoc logging).
- Emit events that:
  - conform to the referenced telemetry schema,
  - contain no PII or sensitive/tribal data,
  - include high-level context only (route, component area, interaction type),
  - avoid embedding raw identifiers when those are governed.

Typical events (examples):

- map layer toggles,
- timeline range changes,
- focus tab switches,
- story node expansion/collapse,
- dataset preview open/close.

### Accessibility metadata

Components that render media must:

- provide alt text (or `alt=""` for decorative imagery),
- ensure captions do not imply restricted precision,
- preserve governance notices near media when relevant.

---

## 🧪 Validation & CI/CD

Components are subject to CI gates for:

- build correctness (TypeScript, bundler checks),
- unit and integration tests,
- accessibility checks (WCAG-aligned audits),
- governance checks (presence and visibility of required labels/notices),
- secret/PII scanning constraints (no sensitive values in committed UI strings).

Testing expectations:

- Unit tests: render + interaction semantics for core primitives and domain components.
- A11y checks: keyboard paths, ARIA roles, focus visibility, reduced motion.
- Governance tests: CARE badges, masking indicators, sovereignty notices appear when required.
- Snapshot tests: only for stable primitives where snapshots add value.

Any new category or major component family must include:
- tests for the core interaction path,
- an A11y check,
- a governance visibility check (if the component can display governed data).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-12-15 | Applied KFM-MDP v11.2.6 structure (approved H2s, ordering, fencing); corrected relative refs; expanded architecture boundaries, governance, telemetry, and STAC/DCAT/PROV alignment guidance without removing existing data. |
| v11.2.2 | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; added telemetry v11 alignment, energy/carbon v2, governance + AI constraints. |
| v10.4.1 | 2025-11-15 | Updated directory structure with labels; aligned MapView, TimelineView, and Focus components. |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4 documentation overhaul; expanded governance & A11y requirements. |
| v10.3.2 | 2025-11-14 | Map + Story Node + governance updates. |
| v10.3.1 | 2025-11-13 | Initial components overview. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0

[⬅️ Back to web/src Architecture](../ARCHITECTURE.md) ·
[🌐 Web Platform Overview](../../README.md) ·
[🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[📄 LICENSE](../../../LICENSE)

</div>
