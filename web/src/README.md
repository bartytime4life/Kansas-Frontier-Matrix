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
Define the **source-code architecture** for the KFM web platform.  
Documents React + TypeScript structures, UI modules, Focus Mode v2.4 flows, governance connections, accessibility patterns, STAC/DCAT adapters, and telemetry instrumentation per **MCP-DL v6.3** and **FAIR+CARE** standards.

[![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![License](https://img.shields.io/badge/License-MIT-green)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)]()  
[![Status](https://img.shields.io/badge/UI_Status-Stable-success)]()

</div>

---

## 📘 Overview

`web/src/` contains **all source code** for the Kansas Frontier Matrix web platform:

- **2D/3D geospatial viewer** (MapLibre + Cesium)
- **Interactive timeline engine**
- **Focus Mode v2.4 UI**, including narrative rendering & explainability
- **STAC/DCAT dataset explorer**
- **Neo4j-backed entity detail panels**
- **Governance indicators** (care labels, license chips, sovereignty warnings)
- **Accessibility-first UI** (WCAG 2.1 AA)
- **Telemetry & sustainability metrics**

All modules must pass:

- MCP-DL v6.3 docs & metadata checks  
- A11y thresholds  
- TypeScript strict typechecking  
- STAC/DCAT schema guards  
- CI/CD validation flows  

---

## 🗂️ Directory Layout (Authoritative)

~~~~~text
web/src/
├── README.md
│
├── components/                        # FAIR+CARE-compliant UI components
│   ├── MapView/                       # MapLibre + Cesium + layers + events
│   ├── TimelineView/                  # Time navigation, forecasting bands
│   ├── FocusPanel/                    # Narratives, explainability, citations
│   ├── StoryNode/                     # Story Node cards + linked entities
│   ├── LayerControls/                 # STAC/DCAT explorer + toggles
│   ├── DetailDrawer/                  # Entity metadata panels
│   ├── Accessibility/                 # ARIA helpers, focus traps
│   └── Shared/                        # Buttons, modals, panels, layout primitives
│
├── pages/                             # Route-level screen modules
│   ├── index.tsx                      # Home
│   ├── explorer.tsx                   # Data explorer & map browser
│   ├── focus.tsx                      # Focus Mode page
│   └── governance.tsx                 # Governance dashboards + reports
│
├── hooks/                             # Reusable logic modules
│   ├── useFocus.ts                    # Focus Mode state handling
│   ├── useStac.ts                     # STAC/DCAT searching & layer metadata
│   ├── useTelemetry.ts                # WebVitals + ethics metrics
│   ├── useGovernance.ts               # CARE flags, sovereignty warnings
│   └── useA11y.ts                     # Keyboard navigation, reduced motion
│
├── context/                           # Global providers
│   ├── FocusProvider.tsx
│   ├── A11yProvider.tsx
│   ├── ThemeProvider.tsx
│   └── AppProvider.tsx
│
├── services/                          # Data access & API logic
│   ├── apiClient.ts                   # REST/GraphQL + errors + JSON-LD merge
│   ├── stacService.ts                 # STAC item/collection queries
│   ├── dcatService.ts                 # DCAT catalog browser
│   ├── graphService.ts                # GraphQL entity interactions
│   └── telemetryService.ts            # Build/runtime telemetry export
│
├── utils/                             # Helper functions
│   ├── schemaGuards.ts                # Strict type validation of DTO payloads
│   ├── provenance.ts                  # Provenance chips + lineage links
│   ├── formatters.ts                  # Numbers, dates, labels
│   └── a11y.ts                        # ARIA helpers & keyboard focus logic
│
├── styles/
│   ├── globals.css
│   ├── tokens.css                     # Color, spacing, typography tokens
│   └── typography.css
│
└── types/
    ├── api.ts                         # API DTOs (Focus, STAC/DCAT, Graph)
    └── domain.ts                      # People, Places, Events, Documents, Layers
~~~~~

---

## 🧩 Web Source Flow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  UI["UI Components"] --> FOC["useFocus / FocusProvider"]
  UI --> MAP["MapView"]
  UI --> TIME["TimelineView"]

  FOC --> API["apiClient (REST + GraphQL + JSON-LD)"]
  MAP --> API
  TIME --> API

  API --> STAC["stacService<br/>Dataset & Layer Metadata"]
  API --> GRAPH["graphService<br/>Entity & Subgraph"]
  GRAPH --> PANEL["FocusPanel<br/>Narratives · Explainability · Provenance"]
  STAC --> MAP
~~~~~

---

## 🧠 Focus Mode v2.4 — Client Responsibilities

The UI **does not run models** — all AI inference occurs server-side.

Frontend duties:

- Render AI narrative paragraphs  
- Display SHAP “Why this?” chips  
- Surface CARE/ethics warnings  
- Link entities to map & timeline  
- Display provenance chips & lineage  
- Synchronize focus selections across view components  
- Emit non-PII telemetry events  

**Server contract:**

~~~~~text
GET /api/focus/{id}
→ {
  narrative,
  subgraph,
  explainability,
  citations,
  ethics_flags,
  provenance,
  telemetry
}
~~~~~

Schema guards (`schemaGuards.ts`) enforce structural correctness.

---

## ♿ Accessibility (WCAG 2.1 AA Guaranteed)

Patterns enforced in `web/src/`:

- ARIA roles on interactive components  
- Skip links & structure landmarks  
- Keyboard-first navigation  
- Visible focus rings & tab indexing  
- Colorblind-safe palettes (tokens.css)  
- Reduced motion modes  
- Screen-reader-friendly layouts  
- Automated CI scanning: axe-core + Lighthouse

Accessibility tokens documented in:

```
docs/design/tokens/accessibility-tokens.md
```

---

## 📡 Telemetry & Sustainability Metrics

Collected via `useTelemetry.ts`:

- Web Vitals (LCP, FID, CLS, TTFB)
- A11y violations
- Ethics events (masking, sovereignty checks)
- Focus Mode interactions
- Layer toggle statistics
- Approximated energy & CO₂e metrics

Written to:

```
../../releases/v10.3.0/focus-telemetry.json
```

And into audit logs:

```
../../docs/reports/audit/web-governance-ledger.json
```

---

## 🔐 Governance Integration & CARE Enforcement

UI must:

- Show care_label metadata  
- Mask protected coordinates  
- Display license chips & consent metadata  
- Link to governance-ledger entries  
- Obey sovereignty rules returned by the backend  
- Highlight restricted content warnings  

Governance is non-optional and enforced at render time.

---

## ⚙️ Validation Rules (MCP-DL v6.3)

| Area | Validator |
|------|-----------|
| Type Safety | TypeScript strict mode + schemaGuards.ts |
| API Stability | DTO version checks |
| A11y | Axe + Lighthouse (CI) |
| Ethics | Governance + care_label tests |
| Security | `codeql.yml`, dependency scanning |
| Build Integrity | `build-and-deploy.yml` |
| Telemetry | `telemetry-export.yml` |

Any violation **blocks merge**.

---

## 🚀 Local Development

~~~~~bash
npm --prefix web install
npm --prefix web run dev
npm --prefix web run typecheck
npm --prefix web run lint
npm --prefix web run build
~~~~~

Local dev URL:

```
http://localhost:3000
```

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-13 | Web Architecture Team | Full v10.3 rewrite; new focus architecture; telemetry v3; CARE enforcement. |
| v10.2.2 | 2025-11-12 | Web Architecture Team | Predictive overlays; governance dashboards; improved DTO guards. |
| v10.0.0 | 2025-11-09 | Web Architecture Team | Initial v10 web-tier source architecture. |

---

<div align="center">

**Kansas Frontier Matrix — Web Source Architecture**  
Ethical UX × FAIR+CARE × Explainable AI × Provenance by Design  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Web Index](../README.md) · [Web Architecture](../ARCHITECTURE.md)

</div>
