---
title: "💻 Kansas Frontier Matrix — Web Source Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-readme-v1.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-src-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/README.md@v10.0.0"
  - "web/src/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../schemas/json/web-src-readme.schema.json"
shape_schema_ref: "../../schemas/shacl/web-src-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-src-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-src-readme"
event_source_id: "ledger:web/src/README.md"
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
sunset_policy: "Superseded upon next web/src overhaul"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Source Overview**  
`web/src/README.md`

**Purpose:**  
Provide a clear, architecture-aligned, FAIR+CARE-compliant overview of the **web source directory**  
(`web/src/**`) powering the Kansas Frontier Matrix (KFM) Web Platform:  
React, MapLibre, Cesium, Focus Mode v2.5, Story Node v3, accessibility, governance layers,  
state management, services, pipelines, and utilities.

</div>

---

# 📘 Overview

The `web/src/` directory contains **all frontend application logic** for the KFM Web Platform, including:

- React 18 + TypeScript (strict mode)  
- Tailwind-based design system  
- **MapLibre GL** for 2D rendering  
- **CesiumJS** for 3D terrain & deep-time visualization  
- **Focus Mode v2.5** reasoning UI  
- **Story Node v3** rendering engine  
- Timeline & time-based filtering  
- STAC/DCAT explorers  
- Governance overlays (CARE, provenance, licensing)  
- Accessibility-first UI (WCAG 2.1 AA)  
- Telemetry hooks (energy, carbon, A11y, usage, Focus Mode traces)

This directory is where **all web UI features** are implemented.

---

# 🧱 Directory Structure

~~~text
web/src/                           # Frontend application source code
├── README.md                      # This overview
├── ARCHITECTURE.md                # Full source architecture specification
│
├── components/                    # Reusable React components
│   ├── map/                       # MapLibre layers, controls, overlays
│   ├── timeline/                  # Timeline, scrubbing, markers
│   ├── focus/                     # Focus Mode panels & controls
│   ├── story/                     # Story Node v3 cards & details
│   ├── governance/                # CARE/provenance/UI overlays
│   ├── stac/                      # STAC/DCAT UI components
│   └── layout/                    # Headers, shells, responsive containers
│
├── pages/                         # Top-level route views
│
├── hooks/                         # Custom hooks (data + state + UI logic)
│   ├── useMap.ts                  # MapLibre synchronization  
│   ├── useTimeline.ts             # Timeline → map → focus sync  
│   ├── useFocus.ts                # Focus Mode v2.5 orchestration  
│   ├── useStac.ts                 # STAC/DCAT API integration  
│   └── useTelemetry.ts            # WebVitals + A11y telemetry  
│
├── context/                       # React Context providers
│   ├── TimeContext.tsx
│   ├── FocusContext.tsx
│   ├── ThemeContext.tsx
│   ├── A11yContext.tsx
│   └── GovernanceContext.tsx
│
├── services/                      # API and backend communication
│   ├── apiClient.ts               # REST + GraphQL wrapper
│   ├── stacService.ts             # STAC integration
│   ├── dcatService.ts             # DCAT integration
│   ├── telemetryService.ts        # Telemetry export
│   └── governanceService.ts       # Licence/CARE/provenance lookup
│
├── pipelines/                     # Frontend orchestration pipelines
│   ├── focusPipeline.ts           # Focus Mode v2.5 logic composition
│   ├── stacPipeline.ts            # STAC dataset flows
│   ├── storyPipeline.ts           # Story Node + focus interactions
│   └── timelinePipeline.ts        # Timeline → map → narrative sync
│
├── utils/                         # Utility helpers
│   ├── formatters.ts              # String/number/date utilities
│   ├── jsonld.ts                  # JSON-LD generators
│   ├── guards.ts                  # Type + schema guards
│   ├── bbox.ts                    # Spatial helpers
│   └── a11y.ts                    # Accessibility helpers
│
├── styles/                        # Global styling system
│   ├── tokens/                    # Design tokens
│   ├── themes/                    # Light/dark themes
│   ├── mixins/                    # Layout + component CSS utilities
│   └── maps/                      # MapLibre-specific CSS
│
├── types/                         # Shared TypeScript types
│   ├── api.ts                     # API DTO typings
│   ├── domain.ts                  # Story Nodes, Focus, timelines
│   └── stac.ts                    # STAC/DCAT typings
│
├── main.tsx                       # Entry point (React DOM mount)
└── App.tsx                        # Root layout, routing, theme provider
~~~

---

# 🧩 Responsibilities of `web/src/**`

### 1. UI Rendering  
- MapLibre overlays  
- Cesium globe  
- Story Node cards & detail views  
- Focus Mode interactive panels  
- STAC/DCAT dataset views  

### 2. State Synchronization  
- TimeContext → timeline, map, story nodes, focus  
- FocusContext → map highlight + narrative update  
- Theme + A11y → CSS token propagation  

### 3. Data Integration  
- REST / GraphQL  
- STAC/DCAT endpoints  
- Telemetry ingest/output  
- Governance metadata (CARE, licenses, provenance)  

### 4. Accessibility Architecture  
- ARIA-first UI  
- High contrast + reduced motion  
- Keyboard accessibility  
- A11y tokens  

### 5. Governance & Ethics  
- Display CARE labels  
- No rendering of protected coordinates  
- Masking via H3 generalization  
- Annotate AI-derived content  

---

# 🔐 FAIR+CARE Integration

Every component in `web/src/**` must:

- Respect CARE metadata  
- Apply masking for sensitive sites  
- Display provenance chips  
- Mark AI-generated content  
- Avoid speculative claims  
- Support ethical visualization  
- Use accessible map layers  

Governance violations **block merges in CI**.

---

# ♿ Accessibility (WCAG 2.1 AA)

Required across all components:

- Keyboard operability  
- ARIA labels + roles  
- High contrast visual tokens  
- Reduced motion mode  
- Proper heading structure  
- Alt-text for images  
- Accessible map interactions  

---

# 📈 Telemetry Responsibilities

Telemetry collected in this layer includes:

- WebVitals (LCP, CLS, FID, TTI)  
- Focus Mode interactions  
- Story Node usage  
- Map interactions (pan/zoom/layer toggles)  
- A11y usage  
- Sustainability metrics  

Data is exported to the release bundle:

`releases/<version>/focus-telemetry.json`

---

# 🧪 Testing Expectations

All code within `web/src/**` must satisfy:

- Unit tests  
- Integration tests  
- Visual UI tests (optional)  
- A11y tests  
- Schema/type guards  
- Governance checks  
- Timeline/map synchrony tests  

Testing failures **block PRs**.

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full compliant rewrite for KFM-MDP v10.4; aligned with web/src architecture |
| v10.3.2 | 2025-11-14 | Updated with governance/Focus Mode v2.5 flows |
| v10.3.1 | 2025-11-13 | Initial baseline README |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Reviewed under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>