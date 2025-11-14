---
title: "💻 Kansas Frontier Matrix — Web Application Source Code (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-src-readme-v2.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💻 **Kansas Frontier Matrix — Web Application Source Code**  
`web/src/README.md`

**Purpose:**  
Document the **React + TypeScript** source architecture for the KFM web platform.  
Defines module boundaries, accessibility (WCAG 2.1 AA) patterns, Focus Mode v2.4 integration, STAC/DCAT adapters, governance bindings, telemetry instrumentation, and MCP-DL v6.3 compliance.

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="UI Status" src="https://img.shields.io/badge/UI_Components-Stable-success" />

</div>

---

## 📘 Overview

`web/src/` contains the **complete web-tier application code** responsible for:

- 2D/3D mapping (MapLibre + Cesium)
- Timeline navigation & historical forecasting overlays
- Focus Mode v2.4 narrative rendering (server-side AI → client display)
- STAC/DCAT dataset browsing
- Neo4j-backed entity inspectors
- Accessibility-first UI (keyboard-first, high-contrast, ARIA)
- Governance signage (CARE flags, provenance badges, license indicators)
- OpenTelemetry-backed performance & ethics telemetry

All logic complies with the **FAIR+CARE**, **MCP-DL v6.3**, and **Diamond⁹ Ω / Crown∞Ω** governance standards.

---

## 🗂️ Directory Layout (Authoritative)

~~~~~text
web/src/
├── README.md
│
├── components/
│   ├── MapView/                 # 2D/3D map rendering + layers
│   ├── TimelineView/            # Temporal navigation + forecasting bands
│   ├── FocusPanel/              # AI narratives + explainability + CARE warnings
│   ├── StoryNode/               # Story Node cards + narrative graphs
│   ├── LayerControls/           # STAC/DCAT layer toggles + style presets
│   ├── DetailDrawer/            # Entity metadata, citations, provenance
│   ├── Accessibility/           # Skip links, focus traps, ARIA wrappers
│   └── Shared/                  # Buttons, modals, dialogs, layout primitives
│
├── pages/
│   ├── index.tsx                # Home
│   ├── explorer.tsx             # Catalog + map explorer
│   ├── focus.tsx                # Focus Mode UI
│   └── governance.tsx           # Governance dashboards
│
├── hooks/
│   ├── useFocus.ts              # Centralized focus mode state + interactions
│   ├── useStac.ts               # STAC/DCAT search + filtering
│   ├── useTelemetry.ts          # WebVitals + ethics + energy telemetry
│   ├── useGovernance.ts         # CARE labels, consent, sovereignty logic
│   └── useA11y.ts               # WCAG flows, keyboard nav, reduced motion
│
├── context/
│   ├── A11yProvider.tsx
│   ├── FocusProvider.tsx
│   ├── ThemeProvider.tsx
│   └── AppProvider.tsx
│
├── services/
│   ├── apiClient.ts             # REST/GraphQL client + ETag + retry
│   ├── stacService.ts           # STAC item/collection fetcher
│   ├── dcatService.ts           # DCAT dataset interface
│   ├── graphService.ts          # GraphQL-based entity lookup
│   └── telemetryService.ts      # Build/runtime metrics export
│
├── utils/
│   ├── schemaGuards.ts          # Strong runtime guards for API DTOs
│   ├── provenance.ts            # Citation chips, lineage, ledger links
│   ├── formatters.ts            # Dates, numbers, labels
│   └── a11y.ts                  # Focus management & ARIA helpers
│
├── styles/
│   ├── globals.css
│   ├── tokens.css               # Design tokens (contrast, spacing)
│   └── typography.css
│
└── types/
    ├── api.ts                   # DTO definitions from backend schemas
    └── domain.ts                # Entities: Place, Event, Person, Dataset, Layer
~~~~~

---

## 🔌 Module Interactions (Web Flow Diagram)

~~~~~mermaid
flowchart TD
  UI["UI Components"] --> FOC["useFocus<br/>(Focus Provider)"]
  UI --> MAP["MapView"]
  UI --> TIME["TimelineView"]

  FOC --> API["API Client (REST/GraphQL/JSON-LD)"]
  MAP --> API
  TIME --> API

  API --> STAC["STAC/DCAT Services"]
  API --> GRAPH["Graph Service (Neo4j Entities)"]

  GRAPH --> PANEL["FocusPanel<br/>Narratives + Provenance"]
  STAC --> MAP
~~~~~

---

## 🧠 Focus Mode v2.4 (Client Responsibilities Only)

The **client never performs model inference**.  
Server returns narrative + explainability metadata; this UI renders:

- Narrative paragraphs with citation badges  
- “Why this?” SHAP chips for explainability  
- Ethical warnings (CARE-sensitive narratives, heritage masking)  
- Related StoryNodes, Places, Events  
- Provenance panels with lineage + STAC/DCAT links  
- Timeline synchronization highlights

Example server response:

~~~~~text
GET /api/focus/{id}
→ {
  narrative,
  subgraph,
  explainability,
  ethics_flags,
  provenance,
  telemetry
}
~~~~~

---

## ♿ Accessibility (WCAG 2.1 AA Certified)

Accessibility patterns implemented:

- Skip links (`<a href="#main">Skip to content</a>`)
- ARIA roles for map/timeline/navigation  
- Keyboard-first flows (WASD + arrow keys for map if supported)  
- Focus ring + tab indexing  
- High-contrast mode via tokens.css  
- Reduced-motion auto-detection  
- A11y CI checks (axe-core + Lighthouse ≥ 95)

Tokens stored in:

```
docs/design/tokens/accessibility-tokens.md
```

---

## 📡 Telemetry (Web Vitals + Ethics Metrics)

Collected via `useTelemetry.ts`:

- CLS, LCP, FID, TTFB  
- A11y violations caught client-side  
- Ethics-related UI events (sensitive-layer warnings)  
- Focus Mode usage metrics  
- Layer toggles, dataset exploration stats  

Published to:

```
../../releases/v10.3.0/focus-telemetry.json
```

Telemetry is required for governance & sustainability dashboards.

---

## 🔐 Governance & CARE Enforcement

Governance integration:

- CARE-sensitive flags filter or mask UI elements  
- Sovereignty rules applied (no precise coordinates for heritage sites)  
- License & consent chips rendered on datasets & Story Nodes  
- Provenance and lineage always visible

Governance ledger reference:

```
../../docs/reports/audit/web-governance-ledger.json
```

---

## ⚙️ Contract Enforcement & Schema Guards

### Enforced via:

- **`schemaGuards.ts`** → Fails UI rendering if API payload invalid  
- **TypeScript DTOs** → Compile-time guarantees  
- **STAC/DCAT integration tests**  
- **A11y unit tests** (jest/axe)  

Failure in any → CI blocks merge.

---

## 🚀 Local Development

~~~~~bash
npm --prefix web install
npm --prefix web run dev        # http://localhost:3000
npm --prefix web run typecheck
npm --prefix web run lint
npm --prefix web run build
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-13 | Web Architecture Team | Updated for Focus v2.4, new telemetry, CARE signals, full MCP alignment. |
| v10.2.2 | 2025-11-12 | Web Architecture Team | Predictive layers, governance dashboards, schema guard expansion. |
| v10.0.0 | 2025-11-09 | Web Architecture Team | Initial v10 React/MapLibre/Cesium integration. |

---

<div align="center">

**Kansas Frontier Matrix — Web Source Architecture**  
Ethical UX × FAIR+CARE × Provenance × Explainable AI  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Web Overview](../README.md) · [Web Architecture](../ARCHITECTURE.md)

</div>
