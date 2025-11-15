---
title: "💻 Kansas Frontier Matrix — Web Application Source Code (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v10.3.2"
last_updated: "2025-11-14"
review_cycle: "Quarterly / Autonomous + FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.3.2/sbom.spdx.json"
manifest_ref: "../../releases/v10.3.2/manifest.zip"
telemetry_ref: "../../releases/v10.3.2/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-readme-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Application Source Code**  
`web/src/README.md`

**Purpose:**  
Define the **source-code architecture** for the KFM v10.3.2 web platform — including React + TypeScript structure, UI composition, Focus Mode v2.5 flows, governance & CARE connections, accessibility patterns, STAC/DCAT adapters, and telemetry instrumentation under **MCP-DL v6.3** and **FAIR+CARE** standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)]()
[![UI Status](https://img.shields.io/badge/UI_Status-Stable-success)]()

</div>

---

## 📘 Overview

`web/src/` contains all **first-class frontend logic** for Kansas Frontier Matrix v10.3.2:

- 2D/3D geospatial viewer (MapLibre + Cesium)  
- Interactive temporal navigation (timeline)  
- Focus Mode v2.5 client flows (narratives, explainability, provenance chips)  
- STAC/DCAT dataset explorer UI  
- Neo4j-backed entity & Story Node panels  
- Governance indicators (CARE labels, sovereignty warnings, license chips)  
- FAIR+CARE-aligned accessibility (WCAG 2.1 AA)  
- Telemetry instrumentation (WebVitals, ethics, sustainability, a11y)

All source modules must pass:

- TypeScript strict mode  
- DTO schema guards  
- FAIR+CARE governance checks  
- A11y gates (axe-core/Lighthouse)  
- Security & build workflows (CodeQL, Trivy, CI build)  
- Telemetry export validation (telemetry-export.yml)

---

## 🗂️ Directory Layout (Authoritative v10.3.2)

```text
web/src/
├── README.md
│
├── components/                        # FAIR+CARE-aligned UI components
│   ├── MapView/                       # MapLibre map + layer stack
│   ├── CesiumView/                    # 3D terrain and globe
│   ├── TimelineView/                  # Temporal navigation widgets
│   ├── FocusPanel/                    # Focus Mode v2.5 narratives
│   ├── StoryNode/                     # Narrative Story Node cards
│   ├── LayerControls/                 # STAC/DCAT layer toggles
│   ├── DetailDrawer/                  # Entity detail side panels
│   ├── Governance/                    # CARE labels, masking indicators
│   ├── Accessibility/                 # A11y helper components
│   └── Shared/                        # Buttons, modals, layout primitives
│
├── context/                           # Global providers (A11y, Focus, Theme, Auth)
│   ├── FocusProvider.tsx
│   ├── A11yProvider.tsx
│   ├── ThemeProvider.tsx
│   └── AppProvider.tsx
│
├── entities/                          # Entity-specific UI logic & view models
│   ├── people/
│   ├── places/
│   ├── events/
│   └── datasets/
│
├── features/                          # Feature slices (cohesive verticals)
│   ├── accessibility/                 # A11y controls, toggles, shortcuts
│   ├── focus-mode/                    # Focus Mode L2 logic & UI wiring
│   ├── map-layers/                    # Layer state, legends, symbology
│   ├── timeline-features/             # Time-window & epoch tools
│   └── governance/                    # CARE/ethics banners & gating
│
├── hooks/                             # Reusable frontend logic
│   ├── useFocus.ts
│   ├── useStac.ts
│   ├── useTelemetry.ts
│   ├── useGovernance.ts
│   └── useA11y.ts
│
├── pages/                             # Route-level pages
│   ├── index.tsx                      # Home
│   ├── explorer.tsx                   # Explore map + timeline + layers
│   ├── focus.tsx                      # Focus Mode entry point
│   └── governance.tsx                 # Governance & FAIR+CARE dashboard
│
├── pipelines/                         # Client-side data orchestration
│   ├── focusPipeline.ts               # Focus Mode UI pipeline
│   ├── stacPipeline.ts                # STAC explorer pipeline
│   ├── entityPipeline.ts              # Graph entity fetch + projection
│   ├── timelinePipeline.ts            # Time series & windows
│   ├── layerPipeline.ts               # Layer stack management
│   └── metadata.json                  # Pipeline registry metadata
│
├── services/                          # API clients & data access
│   ├── apiClient.ts                   # Base REST/GraphQL client
│   ├── stacService.ts                 # STAC search & item fetch
│   ├── dcatService.ts                 # DCAT dataset browsing
│   ├── graphService.ts                # Neo4j-backed endpoints
│   └── telemetryService.ts            # Telemetry event sender
│
├── styles/                            # Design tokens & theme styles
│   ├── globals.css
│   ├── tokens.css                     # Color, spacing, typography tokens
│   └── typography.css
│
├── utils/                             # Helpers & guard utilities
│   ├── schemaGuards.ts                # Runtime validation of DTOs
│   ├── provenance.ts                  # Provenance chip construction
│   ├── formatters.ts                  # Date, number, label formatters
│   └── a11y.ts                        # A11y helper utilities
│
└── types/                             # Shared TypeScript types
    ├── api.ts                         # API response/DTO types
    └── domain.ts                      # Domain & UI-facing types
