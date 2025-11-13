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
Describe the **React + TypeScript** source structure, contracts, and governance integrations for the KFM web tier.  
Aligns web modules with **MCP v6.3**, **FAIR+CARE**, **WCAG 2.1 AA**, and v10.3 agent/telemetry updates.

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="Status: Stable" src="https://img.shields.io/badge/Status-Stable-success" />

</div>


---

## 📘 Overview

`web/src/` implements the **timeline + map + Focus Mode v2.4** experience for entity-centric exploration over the KFM knowledge graph.

The codebase is:

- **Standards-first** — STAC/DCAT/JSON-LD, GraphQL, stable DTOs  
- **Accessibility-first** — WCAG 2.1 AA, semantic HTML, ARIA, keyboard-first flows  
- **Ethics-aware** — CARE-informed patterns, heritage masking cues, consent-aware UI  
- **Telemetry-bound** — all builds & runtime interactions contribute to governance ledgers and metrics under MCP v6.3

**Responsibilities**

- Render an accessible, performant UI for geospatial storytelling  
- Display Focus Mode summaries + explainability (client is display-only)  
- Browse STAC/DCAT catalogs and fetch graph-linked entity details  
- Surface provenance, telemetry, and governance status to users  

---

## 🗂️ Directory Layout

    web/src/
    ├── README.md
    │
    ├── components/                        # FAIR+CARE-compliant UI components
    │   ├── MapView/                       # MapLibre (2D) + Cesium (3D) layers & interactions
    │   ├── TimelineView/                  # Time navigation, density, break markers, forecasts
    │   ├── FocusPanel/                    # AI narratives, related links, explainability chips
    │   ├── LayerControls/                 # STAC/DCAT toggles, opacity, style presets
    │   ├── DetailDrawer/                  # Entity metadata, citations, provenance views
    │   ├── Accessibility/                 # Skip links, focus traps, ARIA helpers
    │   └── Shared/                        # Buttons, modals, layout primitives
    │
    ├── pages/                             # Route-level screens
    │   ├── index.tsx                      # Home
    │   ├── explorer.tsx                   # Data Explorer (catalog + map)
    │   ├── focus.tsx                      # Focus Mode UI (entity-centric view)
    │   └── governance.tsx                 # Governance dashboards & reports
    │
    ├── hooks/                             # Shared logic & UI contracts
    │   ├── useTelemetry.ts                # Web vitals, a11y, energy metrics
    │   ├── useFocus.ts                    # Entity focus state & interactions
    │   ├── useGovernance.ts               # CARE flags, consent indicators
    │   └── useA11y.ts                     # Keyboard nav, skip links, reduced motion
    │
    ├── context/                           # App-wide providers
    │   ├── FocusProvider.tsx
    │   ├── ThemeProvider.tsx
    │   ├── A11yProvider.tsx
    │   └── AppProvider.tsx
    │
    ├── services/                          # Data/API clients (strongly typed)
    │   ├── apiClient.ts                   # REST/GraphQL base (ETag, retries, JSON-LD)
    │   ├── stacService.ts                 # STAC discovery & item fetch
    │   ├── dcatService.ts                 # DCAT catalog integration
    │   ├── graphService.ts                # GraphQL entity queries
    │   └── telemetryService.ts            # Build & runtime metrics export
    │
    ├── utils/                             # Helpers & guards
    │   ├── schemaGuards.ts                # DTO guards; fail-fast on invalid payloads
    │   ├── formatters.ts                  # Dates, numbers, legend labels
    │   ├── provenance.ts                  # Citation chips & ledger deep-links
    │   └── a11y.ts                        # Focus rings, aria helpers, reduced motion
    │
    ├── styles/                            # Design tokens & themes
    │   ├── globals.css
    │   ├── tokens.css
    │   └── typography.css
    │
    └── types/                             # Shared TS types
        ├── api.ts                         # API DTOs
        └── domain.ts                      # People, Places, Events, Documents, Layers

---

## 🧩 Web Flow (Modules & Data)

    flowchart TD
      UI["UI Components"] --> FOCUS["Focus Context (hooks/useFocus)"]
      UI --> MAP["MapView / TimelineView"]
      FOCUS --> API["API Client (services/apiClient.ts)"]
      MAP --> API
      API --> GRAPH["Graph Service (entities)"]
      API --> CATALOG["STAC/DCAT Services (layers)"]
      GRAPH --> PANEL["FocusPanel (summary + links + provenance)"]

Flow description:

- UI components call hooks (e.g., `useFocus`, `useStac`, `useTelemetry`)  
- Hooks converge into the `apiClient` (REST/GraphQL + JSON-LD)  
- Services fetch entities, datasets, and layers, run through `schemaGuards`  
- FocusPanel renders narratives, related links, and provenance chips  
- MapView and TimelineView consume the same typed DTOs for synchronized views  

---

## 🧠 Focus Mode (UI Rendering Only)

**Important:** all AI inference runs **server-side**; `web/src/` is strictly responsible for:

- Rendering Focus Mode v2.4 output  
- Linking entities on map and timeline  
- Displaying explainability and provenance metadata  
- Enforcing CARE-aware views and masking indicators  

Server API (conceptual):

    GET /api/focus/{entity_id}
    → Returns: subgraph, narrative, citations, CARE flags, lineage references

UI responsibilities:

- Show the narrative with inline citations  
- Render “Why this?” chips based on explainability metadata  
- Highlight related entities on map and timeline  
- Obfuscate or mask sensitive content according to CARE flags  
- Emit non-PII telemetry about interactions (respected opt-out when configured)

---

## ⚙️ Contracts & Validations

| Contract        | Purpose                              | Location           |
|-----------------|--------------------------------------|--------------------|
| API DTOs        | Typed request/response models        | `types/api.ts`     |
| Domain Types    | Domain-level entities                | `types/domain.ts`  |
| STAC/DCAT Layer | Layer metadata + catalog integration | `services/stacService.ts`, `services/dcatService.ts` |
| A11y Contract   | Route-level accessibility expectations | `hooks/useA11y.ts` |
| Ethics/CARE     | CARE flags + consent metadata        | `hooks/useGovernance.ts` + backend responses |

CI ensures:

- DTOs are respected (type errors fail builds)  
- STAC/DCAT integration tests pass  
- A11y budgets pass thresholds (axe/Lighthouse)  
- Ethics-related telemetries are present for Focus flows  

---

## ♿ Accessibility & Inclusive Design

Core patterns:

- Keyboard-first navigation, tab order, visible focus outlines  
- Skip links, semantic landmarks (header/nav/main/aside/footer)  
- Contrast ≥ 4.5:1 for text; colorblind-safe palettes  
- Reduced-motion settings honored by animations and transitions  
- Screen reader-friendly content: alt text, labels, descriptions  
- A11y hooks to manage focus, ARIA attributes, and announced updates  

A11y tokens and patterns are defined in:

    docs/design/tokens/accessibility-tokens.md

---

## 📊 Telemetry & Governance

Telemetry responsibilities in `web/src/`:

- Capture Web Vitals (CLS, LCP, FID, etc.) via `useTelemetry`  
- Log A11y metrics and errors (derived from hooks and CI outputs)  
- Send event summaries (e.g., focus viewed, layer toggled) to telemetry endpoints  

Primary sinks:

- Build metrics: `../../docs/reports/telemetry/build_metrics.json`  
- Aggregated release snapshot: `../../releases/v10.3.0/focus-telemetry.json`  
- Governance: `../../docs/reports/audit/` (web-governance-ledgers, review logs)

Telemetry fields are used for:

- Release gating  
- Accessibility certification  
- FAIR+CARE reporting  
- Energy and performance tracking  

---

## ⚖️ Retention & Policy

| Asset Type        | Retention   | Notes                                      |
|-------------------|------------|--------------------------------------------|
| Build telemetry   | 90 days    | Rolling CI metrics                         |
| A11y scan results | 365 days   | For certification and regression analysis  |
| Governance ledgers| Permanent  | Immutable audit trail                      |
| Telemetry summary | 90 days    | Aggregated per release; summarized later   |

---

## 🚀 Local Development (Front-End Only)

    # Install dependencies
    npm --prefix web install

    # Run dev server
    npm --prefix web run dev    # http://localhost:3000

    # Typecheck & lint
    npm --prefix web run typecheck
    npm --prefix web run lint

    # Build for production
    npm --prefix web run build

> 🔐 **Secrets:** Use `.env.local` only; never commit. Key parity with CI is defined in `.github/workflows/build-and-deploy.yml`.

---

## 🕰️ Version History

| Version  | Date       | Author              | Summary                                                                 |
|----------|------------|---------------------|-------------------------------------------------------------------------|
| v10.3.1  | 2025-11-13 | Web Architecture Team | Aligned with v10.3 (Focus v2.4, agent-ready web tier, strict rule format). |
| v10.2.2  | 2025-11-12 | Web Architecture Team | Focus v2.1 UI, schema guards, JSON-LD provenance, a11y & energy telemetry. |
| v10.0.0  | 2025-11-09 | Web Architecture Team | Focus v2 UI, Cesium integration, telemetry v2, a11y budgets.            |
| v9.7.0   | 2025-11-05 | KFM Core Team       | MCP alignment, telemetry contracts, web governance mappings.            |