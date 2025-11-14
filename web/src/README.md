---
title: "💻 Kansas Frontier Matrix — Web Application Source Code (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v10.3.2"
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
Define the **source-code architecture** for the KFM web platform.  
Documents React + TypeScript structures, UI modules, Focus Mode v2.4 flows, governance connections, accessibility patterns, STAC/DCAT adapters, and telemetry instrumentation per **MCP-DL v6.3** and **FAIR+CARE** standards.

<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="Status" src="https://img.shields.io/badge/UI_Status-Stable-success" />

</div>

---

## 📘 Overview

`web/src/` contains all **first-class frontend logic** for Kansas Frontier Matrix v10.3:

- 2D/3D geospatial viewer (MapLibre + Cesium)
- Interactive timeline engine
- Focus Mode v2.4 (AI narratives, explainability, provenance)
- STAC/DCAT dataset explorer
- Neo4j-backed entity & Story Node panels
- Governance indicators (CARE labels, sovereignty warnings)
- FAIR+CARE-aligned accessibility (WCAG 2.1 AA)
- Telemetry instrumentation (WebVitals, ethics, sustainability)

All source modules must pass:

- TypeScript strict mode  
- DTO schema guards  
- FAIR+CARE governance checks  
- Accessibility gates  
- CI/CD workflows (CodeQL, Trivy, Lighthouse, telemetry-export)

---

## 🗂️ Directory Layout (Authoritative v10.3.2)

~~~~~text
web/src/
├── README.md
│
├── components/                        # FAIR+CARE-aligned UI components
│   ├── MapView/
│   ├── TimelineView/
│   ├── FocusPanel/
│   ├── StoryNode/
│   ├── LayerControls/
│   ├── DetailDrawer/
│   ├── Accessibility/
│   └── Shared/
│
├── context/                           # Global providers (A11y, Focus, Theme)
│   ├── FocusProvider.tsx
│   ├── A11yProvider.tsx
│   ├── ThemeProvider.tsx
│   └── AppProvider.tsx
│
├── entities/                          # NEW: entity-specific UI logic & view models
│   ├── people/
│   ├── places/
│   ├── events/
│   └── datasets/
│
├── features/                          # NEW: modular feature slices (v10.3+)
│   ├── accessibility/
│   ├── focus-mode/
│   ├── map-layers/
│   ├── timeline-features/
│   └── governance/
│
├── hooks/                             # Reusable logic modules
│   ├── useFocus.ts
│   ├── useStac.ts
│   ├── useTelemetry.ts
│   ├── useGovernance.ts
│   └── useA11y.ts
│
├── pages/                             # Route-level screens
│   ├── index.tsx
│   ├── explorer.tsx
│   ├── focus.tsx
│   └── governance.tsx
│
├── pipelines/                         # Client-side dataflow orchestrators
│   ├── focusPipeline.ts
│   ├── stacPipeline.ts
│   ├── entityPipeline.ts
│   ├── timelinePipeline.ts
│   ├── layerPipeline.ts
│   └── metadata.json
│
├── services/                          # Data access & API clients
│   ├── apiClient.ts
│   ├── stacService.ts
│   ├── dcatService.ts
│   ├── graphService.ts
│   └── telemetryService.ts
│
├── styles/                            # Global design system
│   ├── globals.css
│   ├── tokens.css
│   └── typography.css
│
├── utils/                             # Helper utilities
│   ├── schemaGuards.ts
│   ├── provenance.ts
│   ├── formatters.ts
│   └── a11y.ts
│
└── types/                             # Shared TypeScript types
    ├── api.ts
    └── domain.ts
~~~~~

---

## 🧩 Web Source Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  UI["UI Components"] --> FOC["useFocus / FocusProvider"]
  UI --> MAP["MapView"]
  UI --> TIME["TimelineView"]
  UI --> FEAT["Feature Slices (v10.3)<br/>accessibility · layers · governance"]

  FOC --> API["apiClient (REST + GraphQL + JSON-LD)"]
  MAP --> API
  TIME --> API
  FEAT --> API

  API --> STAC["stacService<br/>Layer Metadata"]
  API --> GRAPH["graphService<br/>Entity + StoryNode Queries"]
  GRAPH --> PANEL["FocusPanel<br/>Narratives · Explainability · Provenance"]
  STAC --> MAP
~~~~~

---

## 🧠 Focus Mode v2.4 — Client Responsibilities Only

The UI **never performs AI inference.**  
All narratives and explainability metadata come from the backend.

UI duties:

- Render narratives with citations  
- Display “Why this?” SHAP chips  
- Show sovereignty/CARE warnings  
- Highlight entities on map + timeline  
- Render provenance chips  
- Emit non-PII telemetry events  

API contract:

~~~~~text
GET /api/focus/{id}
→ { narrative, subgraph, explainability, citations, ethics_flags, provenance, telemetry }
~~~~~

All payloads validated using `schemaGuards.ts`.

---

## ♿ Accessibility (WCAG 2.1 AA)

UI must:

- Use ARIA roles + landmarks  
- Provide skip links + focus-visible rings  
- Support colorblind-safe palettes  
- Respect reduced-motion  
- Achieve Lighthouse A11y ≥ **95**  
- Pass axe-core A11y CI scans  

Tokens documented under:

```
docs/design/tokens/accessibility-tokens.md
```

---

## 📡 Telemetry & Sustainability

Collected via `useTelemetry.ts`:

- LCP, CLS, FID, TTFB  
- A11y violations  
- Ethics event triggers  
- Layer toggles  
- Focus Mode usage  
- Estimated energy + CO₂e impact  

Telemetry written to:

```
../../releases/v10.3.0/focus-telemetry.json
```

Governance events recorded to:

```
../../docs/reports/audit/web-governance-ledger.json
```

---

## 🔐 Governance Integration

UI enforces:

- CARE labels  
- Sovereignty masking  
- License chips  
- Provenance visibility  
- Restricted dataset controls  

All violations block display and emit governance telemetry.

---

## ⚙️ Validation Rules (MCP-DL v6.3)

| Area | Validator |
|------|----------|
| Type Safety | TypeScript strict mode + schemaGuards.ts |
| API Stability | DTO version checks |
| A11y | axe-core + Lighthouse |
| Ethics | CARE governance hooks |
| Security | CodeQL + Trivy |
| Build | build-and-deploy.yml |
| Telemetry | telemetry-export.yml |

---

## 🚀 Local Development

~~~~~bash
npm --prefix web install
npm --prefix web run dev
npm --prefix web run typecheck
npm --prefix web run lint
npm --prefix web run build
~~~~~

Local URL:

```
http://localhost:3000
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.2 | 2025-11-13 | Web Architecture Team | Added new `features/` folder to directory layout; aligned with repo structure. |
| v10.3.1 | 2025-11-13 | Web Architecture Team | Full v10.3 rewrite; telemetry v3; governance hooks. |
| v10.2.2 | 2025-11-12 | Web Architecture Team | Predictive overlays; governance dashboards; DTO guards. |
| v10.0.0 | 2025-11-09 | Web Architecture Team | Initial v10 web-tier architecture. |

---

<div align="center">

**Kansas Frontier Matrix — Web Source Architecture**  
Ethical UX × FAIR+CARE × Explainable AI × Provenance by Design  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Web Index](../README.md) · [Web Architecture](../ARCHITECTURE.md)

</div>
