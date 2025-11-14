---
title: "💻 Kansas Frontier Matrix — Web Source Architecture Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/ARCHITECTURE.md"
version: "v10.3.1"
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
├── README.md
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
├── pages/                          # Route-level pages
│   ├── index.tsx                   # Home
│   ├── explorer.tsx                # Dataset explorer + map
│   ├── focus.tsx                   # Focus Mode full-page view
│   └── governance.tsx              # Governance dashboards + telemetry
│
├── hooks/                          # App logic and state contracts
│   ├── useFocus.ts                 # Central entity-focus orchestration
│   ├── useStac.ts                  # Catalog queries & filters
│   ├── useTelemetry.ts             # WebVitals, energy, CO₂e, ethics metrics
│   ├── useGovernance.ts            # CARE flags, redaction logic
│   └── useA11y.ts                  # Keyboard-first UI, reduced motion
│
├── context/                        # App-wide providers
│   ├── FocusProvider.tsx
│   ├── A11yProvider.tsx
│   ├── ThemeProvider.tsx
│   └── AppProvider.tsx
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

  F --> API["apiClient (REST/GraphQL/JSON-LD)"]
  M --> API
  T --> API

  API --> S1["stacService"]
  API --> S2["dcatService"]
  API --> S3["graphService"]

  S3 --> FP["FocusPanel (narratives + citations + explainability)"]
  S1 --> M
~~~~~

---

## 🧠 Focus Mode v2.4 — Client Architecture

The frontend does **not** run models. It renders server responses.

### Responsibilities:

- Render narrative paragraphs  
- Display SHAP-based explainability chips  
- Render provenance:
  - citations  
  - dataset references  
  - StoryNode → Entity mappings  
- Show CARE flags (e.g., sensitive geomasking)  
- Highlight entity locations on map + timeline  
- Log Focus Mode telemetry (non-PII)

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

The UI must fail gracefully if any required fields are missing (schemaGuards.ts).

---

## 🌍 Mapping Tier (MapLibre + Cesium)

### Features

- 2D/3D map switching  
- Layer stacking (raster/vector/COG)  
- Treaty boundaries, hydrology, climate layers  
- Predictive overlays (2030–2100 SSP scenarios)  
- Keyboard controls (arrows/WASD), screen-reader cues  
- High-contrast basemap modes  

Map layers consume **typed STAC/DCAT DTOs**.

---

## 📊 Timeline Engine

- D3/Recharts scales  
- Brushable ranges + zoom  
- Density bars + event clusters  
- Predictive band overlays  
- Focus-linked year markers  
- WCAG AA accessible markers  

---

## ⚙️ API Client & Service Contracts

### apiClient.ts Handles:

- Retry logic  
- ETags  
- JSON-LD provenance merging  
- Rate-limiting  
- Standard error normalization  

### STAC / DCAT Services

Provide typed interfaces to:

- STAC search  
- DCAT export browsing  
- Layer metadata (roles, media types, projections)

### Graph Service

Handles:

- `entityById` queries  
- Linked documents/places/events  
- StoryNode retrieval  

---

## ♿ Accessibility Requirements (WCAG 2.1 AA)

- Mandatory ARIA landmarks  
- Skip links  
- Keyboard-first control patterns  
- Reduced-motion detection  
- High-contrast color tokens  
- Visible focus rings  
- All icons require alt/aria-label  
- UI dynamically announces updates to screen readers  

A11y tokens live in:

```
docs/design/tokens/accessibility-tokens.md
```

---

## 🔐 Governance & CARE Integration

UI must:

- Show CARE flags (public, sensitive, restricted)  
- Mask sensitive spatial data  
- Attach license chips everywhere assets appear  
- Annotate StoryNodes with sovereignty notes  
- Deep-link all provenance references to governance ledgers  

Governance logs written to:

```
../../docs/reports/audit/web-governance-ledger.json
```

---

## 📡 Telemetry & Sustainability

Collected via `useTelemetry.ts`:

- LCP, CLS, FID  
- A11y violations  
- Ethics events (masked geometry triggers)  
- Layer toggles  
- Focus Mode usage  
- Energy & CO₂e (approximate model from client activity)

Primary export target:

```
../../releases/v10.3.0/focus-telemetry.json
```

---

## ⚙️ Validation & CI Contracts

| Contract | Validator |
|----------|-----------|
| DTOs (TypeScript) | Typechecker + schemaGuards.ts |
| STAC/DCAT | stacService/dcatService + CI |
| A11y | axe-core + Lighthouse |
| Code quality | ESLint + Prettier |
| Build | `build-and-deploy.yml` |
| Security | `codeql.yml`, `trivy.yml` |

Any failure blocks merge under MCP.

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
| v10.3.1 | 2025-11-13 | Web Architecture Team | Created full source architecture spec for v10.3; aligned with new telemetry & Focus Mode. |
| v10.2.2 | 2025-11-12 | Web Architecture Team | Updated API client and governance hooks. |

---

<div align="center">

**Kansas Frontier Matrix — Web Source Architecture**  
🤝 Ethical UX · 🧠 Explainable AI · 🌐 FAIR+CARE · 🔍 Provenance by Design  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Web Source README](README.md) · [Web Architecture](../ARCHITECTURE.md)

</div>

