---
title: "💻 Kansas Frontier Matrix — Web Source Architecture Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/ARCHITECTURE.md"
version: "v10.3.2"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-architecture-v2.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Source Architecture Specification**  
`web/src/ARCHITECTURE.md`

**Purpose:**  
Define the **internal technical architecture** of the KFM web source layer (`web/src/`).  
Specifies module boundaries, contract validation rules, accessibility patterns, ethics integration (FAIR+CARE), data loading architecture, service adapters, AI-aware rendering, and telemetry instrumentation.

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-UI_Certified-orange" />
<img alt="Status: Stable" src="https://img.shields.io/badge/Status-Stable-success" />

</div>

---

## 📘 Overview

`web/src/` hosts **all UI logic** for KFM v10.3:

- React 18 + TypeScript  
- Tailwind + design tokens  
- MapLibre (2D) + Cesium (3D)  
- Timeline + Focus Mode v2.4  
- Governance & provenance indicators  
- STAC/DCAT service bindings  
- JSON-LD entity + provenance injection  
- FAIR+CARE enforcement in UI  
- Telemetry instrumentation (ethics, performance, WebVitals, A11y)

**Guiding Principles**

- Accessibility-first (WCAG 2.1 AA)  
- Ethics-first (CARE-compliant UI masking & flags)  
- Provenance-visible (always show source paths & citations)  
- Deterministic + testable (schema guards, DTO validation)  
- Fully MCP-aligned  

---

## 🗂️ Directory Layout (Formal Schema)

~~~~~text
web/src/
├── ARCHITECTURE.md                 # This document
├── README.md                       # Source-level overview
│
├── components/
│   ├── MapView/                    # MapLibre/Cesium rendering & gestures
│   ├── TimelineView/               # D3/Recharts timeline logic
│   ├── FocusPanel/                 # Narrative rendering + explainability
│   ├── StoryNode/                  # Narrative cards & modal flows
│   ├── DetailDrawer/               # Entity info + lineages + citations
│   ├── LayerControls/              # STAC/DCAT layer toggles + presets
│   ├── Accessibility/              # A11y primitives (ARIA wrappers, skip links)
│   └── Shared/                     # Buttons, modals, UI primitives
│
├── context/                        # App-wide providers
│   ├── FocusProvider.tsx
│   ├── A11yProvider.tsx
│   ├── ThemeProvider.tsx
│   └── AppProvider.tsx
│
├── entities/                       # Entity-specific view models & logic
│   ├── people/
│   ├── places/
│   ├── events/
│   └── datasets/
│
├── features/                       # Feature slices (v10.3+) built on entities + pipelines
│   ├── accessibility/
│   ├── focus-mode/
│   ├── map-layers/
│   ├── timeline-features/
│   └── governance/
│
├── hooks/                          # App logic and state contracts
│   ├── useFocus.ts                 # Central entity-focus orchestration
│   ├── useStac.ts                  # Catalog queries & filters
│   ├── useTelemetry.ts             # WebVitals, energy, CO₂e, ethics metrics
│   ├── useGovernance.ts            # CARE flags, redaction logic
│   └── useA11y.ts                  # Keyboard-first UI, reduced motion
│
├── pages/                          # Route-level pages
│   ├── index.tsx                   # Home
│   ├── explorer.tsx                # Dataset explorer + map
│   ├── focus.tsx                   # Focus Mode full-page view
│   └── governance.tsx              # Governance dashboards + telemetry
│
├── pipelines/                      # Client-side dataflow orchestrators
│   ├── focusPipeline.ts
│   ├── stacPipeline.ts
│   ├── entityPipeline.ts
│   ├── timelinePipeline.ts
│   ├── layerPipeline.ts
│   └── metadata.json
│
├── services/
│   ├── apiClient.ts                # REST/GraphQL base client
│   ├── stacService.ts              # STAC search + asset fetch
│   ├── dcatService.ts              # DCAT export reader
│   ├── graphService.ts             # GraphQL entity requests
│   └── telemetryService.ts         # Aggregated telemetry exporter
│
├── utils/
│   ├── schemaGuards.ts             # Strong DTO guards (runtime verification)
│   ├── provenance.ts               # Provenance chips + ledger deep-links
│   ├── a11y.ts                     # ARIA helpers + focus manager
│   └── formatters.ts               # Dates, numbers, labels
│
├── styles/
│   ├── globals.css
│   ├── tokens.css
│   └── typography.css
│
└── types/
    ├── api.ts                      # Typed API DTOs based on backend schemas
    └── domain.ts                   # Entities: Person, Place, Event, Document, Layer
~~~~~

---

## 🧩 Architecture Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  UI["UI Components"] --> F["useFocus (FocusProvider)"]
  UI --> M["MapView (2D/3D)"]
  UI --> T["TimelineView"]
  UI --> FEAT["Feature Slices<br/>(features/*)"]

  F --> API["apiClient (REST/GraphQL/JSON-LD)"]
  M --> API
  T --> API
  FEAT --> API

  API --> S1["stacService"]
  API --> S2["dcatService"]
  API --> S3["graphService"]

  S3 --> FP["FocusPanel (narratives + citations + explainability)"]
  S1 --> M
~~~~~

---

## 🧠 Focus Mode v2.4 — Client Architecture

The frontend does **not** run AI models. It renders server responses and applies governance rules.

### Responsibilities

- Render narrative paragraphs with citations  
- Display SHAP-based explainability chips  
- Render provenance:
  - citations  
  - dataset references  
  - StoryNode → Entity mappings  
- Show CARE flags (sensitivity, sovereignty, masking)  
- Highlight entity locations on map + timeline  
- Log Focus Mode telemetry (non-PII, consent-aware)

### Required Server Contract

```
GET /api/focus/{id}
→ {
  narrative: string,
  subgraph: {...},
  explainability: [...],
  citations: [...],
  ethics_flags: [...],
  provenance: {...},
  telemetry: {...}
}
```

The UI must fail gracefully if any required fields are missing (`schemaGuards.ts`).

---

## 🌍 Mapping Tier (MapLibre + Cesium)

### Features

- 2D/3D map switching  
- Layer stacking (raster/vector/COG)  
- Treaty boundaries, hydrology, climate, ecology, archaeology layers  
- Predictive overlays (2030–2100 SSP scenarios)  
- Keyboard controls (arrows/WASD), screen-reader cues  
- High-contrast basemap modes  

Map layers consume **typed STAC/DCAT DTOs** and are configured via `pipelines/layerPipeline.ts` and design tokens in `styles/`.

---

## 📊 Timeline Engine

- D3/Recharts-based scale abstractions  
- Brushable ranges + zoom  
- Density bars + event clusters  
- Predictive bands & scenario intervals  
- Focus-linked markers (birth/death, treaty, hazard, etc.)  
- WCAG AA accessible markers and text  

Timeline data produced by `timelinePipeline.ts`.

---

## ⚙️ API Client & Service Contracts

### `apiClient.ts`

- Handles retries, ETags, JSON-LD provenance merges  
- Unified error mapping  
- Injects CARE/ethics headers when required  

### STAC / DCAT Services

- `stacService.ts` — STAC search + item fetch  
- `dcatService.ts` — DCAT dataset browsing  

### Graph Service

- `graphService.ts` — Entity fetches, StoryNode queries, Focus Mode subgraphs  

All responses validated via `schemaGuards.ts` before reaching UI.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA)

The architecture enforces:

- ARIA landmarks and roles  
- Skip links for navigation  
- Keyboard-first interaction patterns  
- Reduced-motion consistency  
- High-contrast theme tokens  
- Visual focus outlines  
- Screen-reader update announcements  

A11y design rules in:

```
docs/design/tokens/accessibility-tokens.md
```

---

## 🔐 Governance & CARE Integration

UI and feature slices must:

- Show CARE labels (`public`, `sensitive`, `restricted`)  
- Mask sensitive spatial data (H3 generalization, fuzzing)  
- Attach license chips for all datasets and StoryNodes  
- Annotate sovereignty and consent status  
- Deep-link provenance references to governance ledgers  

Key governance ledger for web tier:

```
../../docs/reports/audit/web-governance-ledger.json
```

---

## 📡 Telemetry & Sustainability

Collected via hooks and services:

- WebVitals (LCP, CLS, FID, TTFB)  
- A11y violations & coverage  
- CARE masking & ethics events  
- Focus Mode usage and reasoning depth  
- Layer toggles and path usage  
- Energy & CO₂e approximations per session  

Export target:

```
../../releases/v10.3.0/focus-telemetry.json
```

---

## ⚙️ Validation & CI Contracts

| Contract | Validator / Workflow |
|----------|----------------------|
| DTOs | TypeScript strict mode + `schemaGuards.ts` |
| STAC/DCAT | Tests using `stacService.ts` / `dcatService.ts` |
| A11y | axe-core + Lighthouse (`accessibility_scan.yml`) |
| Code Quality | ESLint + Prettier |
| Build | `build-and-deploy.yml` |
| Security | `codeql.yml` + `trivy.yml` |
| Telemetry | `telemetry-export.yml` |
| Docs | `docs-lint.yml` |

Any contract failure blocks merge as per MCP-DL v6.3.

---

## 🚀 Local Development

~~~~~bash
npm --prefix web install
npm --prefix web run dev        # http://localhost:3000
npm --prefix web run lint
npm --prefix web run typecheck
npm --prefix web run build
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author              | Summary |
|---------|------------|---------------------|---------|
| v10.3.2 | 2025-11-13 | Web Architecture Team | Updated directory layout to include `entities/` and `features/` to match current repo; architecture flow adjusted. |
| v10.3.1 | 2025-11-13 | Web Architecture Team | Created full source architecture spec for v10.3; aligned with telemetry & Focus Mode. |
| v10.2.2 | 2025-11-12 | Web Architecture Team | Updated API client and governance hooks. |

---

<div align="center">

**Kansas Frontier Matrix — Web Source Architecture**  
🤝 Ethical UX · 🧠 Explainable AI · 🌐 FAIR+CARE · 🔍 Provenance by Design  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Web Source README](README.md) · [Web Architecture Overview](../ARCHITECTURE.md)

</div>
