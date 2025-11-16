---
title: "🧩 Kansas Frontier Matrix — Web Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-components-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-components-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (unless displaying CARE-masked data)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/components/README.md@v10.3.2"
  - "web/src/components/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-components-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-components-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-readme"
event_source_id: "ledger:web/src/components/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review each release"
sunset_policy: "Superseded upon next component-layer revision"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Web Components Overview**  
`web/src/components/README.md`

**Purpose:**  
Define the structure, responsibilities, accessibility rules, governance requirements,  
and telemetry expectations for all reusable **React UI components** used across the  
KFM Web Platform (`web/src/components/**`).  
Components are the atomic UI building blocks from which features, pipelines,  
and pages are constructed.

</div>

---

# 📘 Overview

Components in this directory:

- Render **visual UI elements** only  
- Consume hook/state/pipeline outputs  
- Must remain **pure and deterministic**  
- Must not contain business logic  
- Must follow **FAIR+CARE governance rules**  
- Must be fully **WCAG 2.1 AA–compliant**  
- Must emit relevant **telemetry events** (via props or hooks)  
- Must avoid storing internal mutable state except for UI-only interaction patterns  
- Must integrate with MapLibre, Cesium, Focus Mode, Story Node v3, STAC/DCAT flows, and governance overlays  

Components are responsible for **presentation**, not computation.

---

# 🧱 Directory Structure

~~~text
web/src/components/
├── map/                           # 2D MapLibre components
│   ├── MapContainer.tsx           # Base map instance
│   ├── LayerToggle.tsx            # Layer controls
│   ├── Legend.tsx                 # Accessible legend UI
│   ├── FeatureHighlight.tsx       # Highlight for Focus Mode + Story Nodes
│   └── ProvenanceOverlay.tsx      # CARE/licensing/provenance indicators
│
├── timeline/                      # Timeline UI primitives
│   ├── TimelineBar.tsx
│   ├── TimelineHandle.tsx
│   ├── TimelineMarkers.tsx
│   └── GranularityControls.tsx
│
├── focus/                         # Focus Mode v2.5 UI elements
│   ├── FocusPanel.tsx
│   ├── RelatedEntityCard.tsx
│   ├── FocusNarrative.tsx
│   ├── ExplanationBlock.tsx       # SHAP/LIME explanations
│   └── CARENotices.tsx            # Ethical context + data sovereignty
│
├── story/                         # Story Node v3 UI components
│   ├── StoryCard.tsx
│   ├── StoryDetail.tsx
│   ├── StoryMedia.tsx
│   ├── StoryMapPreview.tsx
│   └── StoryRelations.tsx
│
├── governance/                    # Governance & CARE UI components
│   ├── CAREBadge.tsx
│   ├── LicenseTag.tsx
│   ├── ProvenanceChip.tsx
│   └── GovernanceDrawer.tsx
│
├── stac/                          # STAC/DCAT dataset exploration UI
│   ├── DatasetCard.tsx
│   ├── ItemPreview.tsx
│   ├── AssetMetadata.tsx
│   └── ExtentPreview.tsx
│
├── layout/                        # Layout and global shell components
│   ├── Header.tsx
│   ├── Sidebar.tsx
│   ├── Panel.tsx
│   └── PageContainer.tsx
│
└── shared/                        # Cross-platform shared UI primitives
    ├── Button.tsx
    ├── Modal.tsx
    ├── Dropdown.tsx
    ├── Tabs.tsx
    └── Spinner.tsx
~~~

---

# 🧩 Component Responsibilities

## 1. **Rendering**
Components must render UI with:

- Deterministic patterns  
- Clear state boundaries  
- No side effects outside UI  

## 2. **Accessibility (WCAG 2.1 AA)**  
Components *must* have:

- Semantic HTML  
- ARIA roles/labels  
- Keyboard navigation  
- Reduced-motion support  
- High-contrast token usage  
- Alt text for images  
- Screen-reader-safe content  

## 3. **Governance**
Components must:

- Display CARE flags  
- Show provenance chips where required  
- Obey sovereignty masking rules  
- Annotate AI-generated text  

## 4. **Telemetry**
Components must emit contextual events such as:

- `"ui:click"`  
- `"ui:open"` / `"ui:close"`  
- `"ui:navigation"`  
- `"focus:entity-selected"`  
- `"story:card-open"`  
- `"map:layer-toggle"`  

All telemetry must be:

- Non-PII  
- Schema-valid  
- Version-linked  
- Stored via the telemetry pipeline  

---

# 🔐 Governance Enforcement

Every component that displays:

- Dataset info  
- Story Node content  
- Focus Mode narrative  
- Spatial overlays  
- Historical material  

Must apply:

- CARE metadata  
- Provenance metadata  
- Rights-holder labels  
- Sovereignty masking indications  

Governance failures **block merges** via CI workflows.

---

# ♿ Accessibility Enforcement

A component cannot ship unless:

- Keyboard navigation works  
- ARIA tags are correct  
- Color contrast meets AA  
- Reduced-motion animations tested  
- Screen-reader announcements validated  

Accessibility failures **fail CI**.

---

# 🔗 Interaction With Other Layers

Components receive inputs from:

- Hooks (`useMap`, `useTimeline`, `useFocus`, etc.)
- Feature slices (`focus-mode/**`, `story-nodes/**`)
- Pipelines (`focusPipeline`, `timelinePipeline`)
- Services (`stacService`, `apiClient`)
- Context providers (Time, Focus, A11y, Theme, Governance)

They should **never** directly call backend APIs or modify global state.

---

# 🧪 Testing Expectations

Every component must have:

- Unit tests  
- Accessibility tests  
- Visual regression tests (optional)  
- Governance metadata tests (if applicable)  
- Telemetry emission tests  
- Snapshot tests (only for stable visual components)  

Tests live under:

~~~text
tests/unit/web/components/**
tests/integration/web/components/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 rewrite; governance, A11y, telemetry rules; expanded component taxonomy |
| v10.3.2 | 2025-11-14 | Map + Story Node + governance UI updates |
| v10.3.1 | 2025-11-13 | Initial components overview documentation |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Reviewed under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>