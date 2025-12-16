---
title: "📂 Kansas Frontier Matrix — DetailDrawer Component Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/DetailDrawer/README.md"
version: "v11.2.2"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/web-detaildrawer-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-detaildrawer-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public with CARE/sovereignty exceptions"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-detaildrawer"
semantic_intent:
  - "UI-component"
  - "contextual-detail"
  - "governance-ui"
  - "provenance-ui"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (content-dependent)"
sensitivity_level: "Variable"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/DetailDrawer/README.md@v10.4.0"
  - "web/src/components/DetailDrawer/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../schemas/json/web-components-detaildrawer-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-detaildrawer-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-detaildrawer-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-detaildrawer-readme-v11"
event_source_id: "ledger:web/src/components/DetailDrawer/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict safeguards"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"
---

<div align="center">

# 📂 **Kansas Frontier Matrix — DetailDrawer Component Overview**
`web/src/components/DetailDrawer/README.md`

**Purpose**  
Document the **DetailDrawer** component suite — the KFM Web UI’s governed, “stay‑on‑page” pattern for
presenting contextual detail (metadata, provenance, CARE/sovereignty context) without navigating away
from maps, Story Nodes, or Focus Mode surfaces.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange" />
<img src="https://img.shields.io/badge/A11y-WCAG_2.1_AA%2B-blueviolet" />

</div>

---

## 📘 Overview

The **DetailDrawer** provides a governed, accessible slide‑out panel used across the KFM Web Platform to
render deep context alongside map and narrative workflows.

It is commonly used for:

- Dataset and asset detail views (STAC/DCAT‑backed)
- Story Node “deep dive” panels (narrative + sources)
- Governance and CARE explanations (what is shown, what is masked, and why)
- Focus Mode supplemental panes (supporting detail; not policy‑rewriting)

Core properties:

- **Governance‑aware rendering**: CARE/sovereignty flags can require masking, generalization, or warnings
- **Accessible interaction**: keyboard focus management, screen‑reader labeling, reduced‑motion handling
- **Provenance‑aware display**: surfaces recorded lineage and links to governance artifacts (SBOM/manifest)
- **Telemetry‑emitting UI**: emits non‑PII events for reliability and usage monitoring

Note: the repo snapshot confirms the web app is a React frontend with map/visualization tooling, and the UI is designed around modular components and contextual panels. This README documents the DetailDrawer suite as one of those governed contextual panels.

---

## 🗂️ Directory Layout

~~~text
📁 web/
└── 📁 src/
    └── 📁 components/
        └── 📁 DetailDrawer/
            ├── 📄 README.md                 — This document
            ├── 📄 DetailDrawer.tsx          — Drawer container (layout, lifecycle, focus mgmt)
            ├── 📄 DrawerHeader.tsx          — Title/type, close control, governance badges
            ├── 📄 DrawerSection.tsx         — Reusable semantic section wrapper
            ├── 📄 DrawerMetadata.tsx        — Metadata rendering + masking indicators
            ├── 📄 DrawerProvenance.tsx      — Lineage view (PROV-aligned display + export links)
            ├── 📄 DrawerCAREBlock.tsx       — CARE/sovereignty warnings + explanations
            ├── 📄 DrawerFooter.tsx          — Action bar (contextual navigation + safe actions)
            └── 📄 DrawerA11yHelpers.tsx     — Shared ARIA + keyboard + announcement helpers
~~~

If filenames differ in your working branch, update this layout to reflect the actual directory content.

---

## 🧭 Context

### Where DetailDrawer appears

DetailDrawer is expected to appear in map and narrative contexts where users need **additional, governed**
detail without leaving the current view:

- Map feature selection (layers, assets, sites, events)
- Search results and entity “inspect” actions
- Story Node panels (read‑only, evidence‑led display)
- Focus Mode supporting panels (guardrails applied)

### How data should reach the component

DetailDrawer content must be **fed via APIs / catalog outputs** (STAC/DCAT/PROV‑derived payloads),
not via direct graph access from the browser. The frontend is a client: governance and redaction decisions
must be enforced by the platform contracts and validated outputs before the UI renders.

---

## 🧱 Architecture

### DetailDrawer.tsx

Responsibilities:

- Open/close lifecycle and viewport layout
- Focus handling:
  - trap focus while open (dialog‑style)
  - restore focus to invoking element on close
- Reduced motion:
  - honor user preference for reduced motion in transitions
- ARIA semantics:
  - `role="dialog"` / `aria-modal="true"` when acting as modal
  - `role="complementary"` when acting as a side panel supplement
  - `aria-labelledby` bound to the header title

Telemetry (non‑PII):

- `drawer:open`
- `drawer:close`
- `drawer:section-toggle`

### DrawerHeader.tsx

Responsibilities:

- Clear, accessible title and entity type
- Close button:
  - keyboard reachable
  - labeled (e.g., “Close detail drawer”)
- Governance badges:
  - CARE label and/or governance classification chip(s)

### DrawerSection.tsx

Responsibilities:

- Provides consistent section semantics (`<section>`) and heading structure
- Prevents heading order regressions inside the drawer
- Hosts content blocks such as metadata, narrative excerpts, and provenance panels

### DrawerMetadata.tsx

Responsibilities:

- Render display‑safe metadata fields (rights, license, source, temporal/spatial extent)
- If redaction is required:
  - do not render raw sensitive values
  - render a clear “masked/generalized” indicator with accessible text

### DrawerProvenance.tsx

Responsibilities:

- Render lineage/provenance views based on recorded references only
- Provide inspection affordances (e.g., “view provenance JSON‑LD”) if available
- Must not “fill gaps” in provenance with assumptions

### DrawerCAREBlock.tsx

Responsibilities:

- Render CARE/sovereignty warnings early and prominently
- Explain why certain fields are masked or generalized (without speculation)
- Must appear before sensitive sections when `redaction_required: true`

### DrawerFooter.tsx

Responsibilities:

- Render only safe actions for the current entity’s governance state
- Disable/hide actions that would violate CARE/sovereignty constraints, with explanation text
- Example action types:
  - open dataset detail
  - open in map view
  - export metadata (if allowed)
  - open Focus Mode context panel (if allowed)

### DrawerA11yHelpers.tsx

Responsibilities:

- Centralize ARIA labeling patterns, keyboard scaffolding, and live announcements
- Prevent ad‑hoc accessibility logic from diverging across sections

---

## 📦 Data & Metadata

### Typical metadata fields (display‑safe)

- Title, entity type, and stable identifier
- License and attribution (SPDX‑style where applicable)
- Temporal extent (generalized when required)
- Spatial extent (generalized when required)
- Provenance references (SBOM/manifest pointers, lineage IDs)

### Redaction and generalization

When the payload indicates redaction/generalization requirements:

- Prefer “show that something exists” over “show nothing”
- Present a clear indicator:
  - “Location generalized for sovereignty”
  - “Exact timestamp hidden due to sensitivity”
- Do not render raw coordinates or raw sensitive identifiers in the UI

### Telemetry

DetailDrawer interactions should emit telemetry that is:

- schema‑conformant to `telemetry_schema`
- non‑PII (no raw user queries, no identifiers that can re‑identify individuals)
- version‑tagged (component version, environment)

Recommended event names:

- `drawer:open`
- `drawer:close`
- `drawer:section-toggle`
- `drawer:provenance-visible`
- `drawer:care-warning-shown`
- `drawer:action`

---

## 🧠 Story Node & Focus Mode Integration

DetailDrawer is a safe surface for **evidence‑led** context:

- Story Node excerpts shown here must be sourced and must not introduce new claims
- Focus Mode content rendered here must not rewrite governance status or provenance
- If the drawer renders AI‑assisted highlights:
  - label them as AI‑assisted
  - keep them strictly non‑speculative
  - never present them as authoritative records

---

## 🧪 Validation & CI/CD

The DetailDrawer suite is governance‑critical and should be covered by:

### Automated checks

- Type checking and linting for component code
- Unit tests for:
  - redaction/masking behaviors (given flags/props)
  - focus‑trap and focus‑restore behavior
  - accessibility attributes present and correct
- Integration tests for:
  - map feature → drawer open → close focus return
  - Story Node / Focus Mode contexts where the drawer is used
- Telemetry shape tests:
  - required events emitted
  - payload conforms to `telemetry_schema`

### Security and privacy checks

- No secrets in code or docs
- No raw sensitive coordinates in snapshots/tests
- No PII in telemetry payloads

---

## ⚖ FAIR+CARE & Governance

DetailDrawer must:

- honor CARE and sovereignty flags and display requirements
- surface “why this is masked” explanations in plain language
- avoid exposing sensitive values through:
  - UI text
  - DOM attributes
  - logs or telemetry payloads
  - copy/export affordances

DetailDrawer must not:

- invent provenance links
- claim governance approval where none exists
- bypass redaction rules via hidden routes or “advanced” toggles

---

## 🕰️ Version History

| Version | Date       | Summary |
|---:|:---|:---|
| v11.2.2 | 2025-12-16 | Reformatted to comply with KFM‑MDP v11.2.6 (approved H2s, directory layout rules, fencing profile). |
| v11.2.2 | 2025-11-30 | Prior v11.2.2 revision (governance + A11y documentation). |
| v10.4.0 | 2025-11-15 | Full drawer documentation with governance/A11y emphasis. |
| v10.3.2 | 2025-11-14 | Added CARE/provenance improvements. |
| v10.3.1 | 2025-11-13 | Initial DetailDrawer overview. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
**DetailDrawer Component Overview**  
Governance‑Aligned UI · Provenance‑Aware Rendering · WCAG 2.1 AA+

[Docs Root](../../../../../README.md) ·
[Web Architecture](../../../../ARCHITECTURE.md) ·
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
