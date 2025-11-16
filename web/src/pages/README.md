---
title: "📄 Kansas Frontier Matrix — Web Pages Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pages/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-pages-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-pages-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/pages/README.md@v10.3.2"
  - "web/src/pages/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebPage"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-pages-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-pages-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-pages-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-pages-readme"
event_source_id: "ledger:web/src/pages/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next web pages system update"
---

<div align="center">

# 📄 **Kansas Frontier Matrix — Web Pages Overview**  
`web/src/pages/README.md`

**Purpose:**  
Provide a complete, FAIR+CARE-aligned overview of the **Page Layer** in the KFM Web Platform  
(`web/src/pages/**`), including layout, routing, A11y constraints, governance visibility,  
data-context wiring, and integration with Focus Mode v2.5, Story Node v3, STAC/DCAT explorers,  
and timeline/map synchronization flows.

</div>

---

# 📘 Overview

Pages in `web/src/pages/` serve as **top-level route containers** in the KFM Web Platform.

They define:

- Primary navigation structure  
- Layout shells for each feature zone  
- Which components render for each route  
- How contexts (Time, Focus, Governance, A11y, Theme) map to full-screen views  
- Entry points for Focus Mode flows  
- Entry points for Story Node narratives  
- Dataset browsing experiences (STAC/DCAT)  
- Global accessibility and governance bindings  

Each page integrates:

- 2D & 3D views  
- Narrative/UI components  
- Timeline + map synchronization  
- Provenance + CARE overlays  
- Telemetry instrumentation  

---

# 🧱 Directory Structure

~~~text
web/src/pages/
├── HomePage.tsx                     # Landing view: intro content + map preview
├── MapPage.tsx                      # 2D map with layers, timeline, and focus triggers
├── CesiumPage.tsx                   # 3D deep-time and terrain view
├── StoryNodePage.tsx                # Full Story Node v3 narrative + spatial overlays
├── FocusPage.tsx                    # Dedicated Focus Mode deep-dive panel
├── DataExplorerPage.tsx             # STAC/DCAT dataset exploration
├── GovernancePage.tsx               # CARE, provenance, sovereignty info center
└── NotFoundPage.tsx                 # 404 fallback (A11y-compliant)
~~~

---

# 🧩 Page Responsibilities

---

## 🏠 **HomePage**
- Introduces KFM  
- Provides accessible navigation entry points  
- Shows map preview  
- Summaries of recent datasets or story nodes  

A11y:
- High-contrast hero  
- Keyboard navigable summaries  

Governance:
- Prominent FAIR+CARE links  

---

## 🗺️ **MapPage**
- Main 2D exploration environment  
- Renders MapLibre layers, legends, overlays  
- Integrates TimeContext + FocusContext  
- Dropoff point for:
  - Focus Mode activation  
  - Story Node highlights  
  - STAC/DCAT previews  

A11y:
- Fully keyboard-operable map controls  
- Visible focus indicators  

Governance:
- CARE masking indicators  
- Provenance chips for layers  

---

## 🌍 **CesiumPage**
- Full-screen 3D visualization  
- Terrain, paleogeography, predictive climate overlays  
- Story Node 3D placement  
- Accessible camera presets  

Governance:
- Warning banners for predictive/AI-based layers  

---

## 📝 **StoryNodePage**
- Dedicated view for Story Node v3  
- Narrative + spatial overlay  
- Provenance chips + CARE flags  
- Timeline integration for temporal segments  
- AI summaries clearly labeled  

---

## 🎯 **FocusPage**
- Focus Mode v2.5 intensive viewer  
- Entity-centered narrative  
- Related entities + story nodes  
- Spatial highlighting  
- AI explainability layer  
- CARE-sensitive redactions clearly shown  

---

## 📦 **DataExplorerPage**
- STAC/DCAT dataset browser  
- Preview footprints & temporal ranges  
- Dataset-level provenance, CARE labeling, governance rules  
- Quick actions: visualize in map, open metadata, view lineage  

---

## 🛡️ **GovernancePage**
- Explanation of FAIR+CARE, sovereignty, licensing  
- Legend for CARE labels  
- Interactive examples of masking/redaction  
- Governance-ledger lookup  

A11y:
- Must be fully screen-reader navigable  
- Uses readable, non-visual descriptions for spatial concepts  

---

## 🚫 **NotFoundPage**
- A11y-compliant 404 fallback  
- Clear navigation options  
- No dead ends  

---

# 🔄 Routing Architecture

Routing is handled via:

- React Router  
- Accessible navigation landmarks  
- Restore-scroll + focus management for A11y  
- Dynamic parameters for:
  - Story Node pages (`/story/:id`)  
  - Focus Mode pages (`/focus/:id`)  
  - Dataset pages (`/data/:id`)  

Routes must:

- Update telemetry  
- Respect CARE boundaries  
- Sync with Timeline + Map contexts  
- Provide graceful loading/error boundaries  

---

# 🔐 Governance & FAIR+CARE Integration

All pages must:

- Display CARE labels when relevant  
- Avoid showing prohibited geometry  
- Annotate model-generated text  
- Link provenance chips  
- Provide user warnings when content is masked or redacted  
- Display licensing for datasets and visual layers  

Pages rendering sensitive/sovereignty data must use:

- H3 r7+ generalization  
- Contextual CARE notes  
- AI prohibition banners where required  

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

Each page must:

- Use semantic HTML landmarks  
- Maintain heading structure  
- Support keyboard-only use  
- Provide visible focus states  
- Respect reduced-motion preferences  
- Use accessible map styling  
- Provide alt text for all imagery  
- Be screen-reader-friendly  

Accessibility regressions **block merges**.

---

# 📈 Telemetry Responsibilities

Each page MUST emit:

- Navigation events  
- Interaction-level telemetry  
- A11y usage signals  
- Performance metrics (WebVitals where relevant)  
- Spatial interaction telemetry on map/3D pages  

Telemetry flows to:

`releases/<version>/focus-telemetry.json`

---

# 🧪 Testing Requirements

Each page MUST have:

- Unit tests (snapshot optional)  
- Integration tests (timeline/map/focus sync)  
- Accessibility tests  
- Governance tests for CARE content  
- Telemetry correctness tests  

Tests live under:

~~~text
tests/unit/web/pages/**
tests/integration/web/pages/**
tests/e2e/web/pages/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Complete rewrite under KFM-MDP v10.4; added routing, governance, A11y, STAC/DCAT, Story Node, telemetry |
| v10.3.2 | 2025-11-14 | Added Focus Mode flows + Story Node interactions |
| v10.3.1 | 2025-11-13 | Initial version of page overview documentation |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>