---
title: "🌐 Kansas Frontier Matrix — Web Application Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/ARCHITECTURE.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../releases/v10.3.0/manifest.zip"
telemetry_ref: "../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-architecture-v2.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application Architecture**  
`web/ARCHITECTURE.md`

**Purpose:**  
Define the FAIR+CARE-aligned **technical architecture** of the KFM Web Application — a modular, accessible, AI-aware frontend for exploring historical, geospatial, and environmental data.  
Specifies stack, module boundaries, data/telemetry contracts, governance integration, and CI/CD touchpoints for the web tier in **KFM v10.3.x**.

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="Status: Stable" src="https://img.shields.io/badge/Status-Stable-success" />

</div>


---

## 📘 Overview

The **KFM Web Application** implements the **timeline + map + Focus Mode** experience over a Neo4j-backed knowledge graph served by **FastAPI/GraphQL** and MCP-connected services.

The web tier is:

- **Standards-first:** STAC 1.0, DCAT 3.0, JSON-LD/RDF, WCAG 2.1 AA  
- **Governed by MCP-DL v6.3:** explicit contracts, telemetry, SBOMs, and CI gates  
- **Ethics-aware:** FAIR+CARE, CARE-aligned visual cues, heritage masking, consent-aware panels  

**Design Goals**

- Accessibility by default — WCAG 2.1 AA, semantic HTML, ARIA, keyboard-first  
- Ethical AI — explainable Focus Mode v2.4, CARE guardrails, provenance chips  
- Interoperability — STAC/DCAT catalogs, JSON-LD semantics, stable APIs  
- Reproducibility — pinned toolchain, SBOM, deterministic builds, telemetry

---

### 🗂️ Directory Layout

    web/
    ├── README.md                          # Web tier index
    ├── ARCHITECTURE.md                    # This file
    │
    ├── public/                            # Static assets (no secrets)
    │   ├── images/                        # PNG/SVG with documented alt text
    │   ├── icons/                         # App/feature icons (a11y-ready)
    │   └── manifest.json                  # PWA metadata (name, theme, icons)
    │
    ├── src/                               # React + TypeScript application
    │   ├── components/                    # Presentational & a11y-first components
    │   │   ├── MapView/                   # MapLibre (2D) + Cesium (3D)
    │   │   ├── TimelineView/              # Time navigation + density bands
    │   │   ├── FocusPanel/                # AI summaries + links + explainability
    │   │   ├── LayerControls/             # STAC/DCAT toggles, opacity, presets
    │   │   ├── Accessibility/             # Skip links, focus traps, ARIA helpers
    │   │   └── Shared/                    # Buttons, cards, modals, layout primitives
    │   │
    │   ├── pages/                         # Routes: Home, Explore, Governance, About
    │   ├── hooks/                         # useTelemetry, useGovernance, useFocus, useStac
    │   ├── context/                       # Providers (Theme, Focus, Auth, A11Y)
    │   ├── services/                      # API clients (REST/GraphQL, STAC/DCAT adapters)
    │   ├── utils/                         # Formatters, i18n, schema guards, helpers
    │   └── styles/                        # Tailwind config, tokens, variables
    │
    ├── package.json                       # Pinned deps + scripts
    ├── vite.config.ts                     # Vite build config
    └── telemetry.json                     # Optional local web telemetry cache (dev-only)

---

## 🧩 Frontend Stack & Responsibilities

| Layer        | Technology                    | Responsibility                                              |
|-------------|--------------------------------|-------------------------------------------------------------|
| Framework   | React 18 + TypeScript          | Component model, routing, high-level state                 |
| Styling     | Tailwind CSS                  | Tokenized, responsive, accessible UI                       |
| Map         | MapLibre GL / Cesium          | Vector rendering, COG overlays, 3D scenes                  |
| Charts      | D3 / Recharts                 | Timeline densities, histograms, KPIs                       |
| State       | React Context + local store   | Focus, theme, a11y, layer state, auth                      |
| Data        | STAC/DCAT, GraphQL, JSON-LD   | Catalog discovery + entity detail + provenance             |
| AI          | Focus v2.4 (server-side)      | Narratives, relatedness, explainability                    |
| A11y        | Semantics + ARIA + axe CI     | WCAG 2.1 AA compliance                                     |
| Telemetry   | Web Vitals + custom hooks     | Perf, a11y, energy & ethics metrics                        |

---

## 🧱 Component Boundaries

    flowchart LR
      map[MapView] --- timeline[TimelineView]
      timeline --- focus[FocusPanel]
      map --- layers[LayerControls]
      focus --- drawer[DetailDrawer]
      map --- legend[Legend]

Roles:

- **MapView:** base map (2D/3D), layer stacking, focus markers, keyboard ops  
- **TimelineView:** zoomable temporal scale, densities, forecast bands  
- **FocusPanel:** AI insights, relationships, provenance & citations, ethics chips  
- **LayerControls:** STAC/DCAT toggles, opacity, presets, layer groups  
- **DetailDrawer / Legend:** context metadata, symbology, a11y tooltips  

---

## 🧠 Focus Mode (Ethical AI v2.4)

Focus Mode centers exploration around a **person, place, event, dataset, or story node** and provides explainable narratives.

Key aspects:

| Aspect          | Implementation                                                                 |
|-----------------|-------------------------------------------------------------------------------|
| API             | `GET /api/focus/{entity_id}` → narrative + subgraph + citations + ethics flags |
| Model           | `focus_transformer_v2.4` (server-side); UI is strictly presentational         |
| Explainability  | SHAP-based “Why this?” chips, cause/effect hints in panel + map               |
| CARE Safeguards | Sensitive content gating; consent & license badges; heritage masking cues     |
| Telemetry       | Focus interactions log to `../releases/v10.3.0/focus-telemetry.json`         |

UI responsibilities:

- Highlight relevant entities on map + timeline  
- Render provenance chips with source IDs + catalog links  
- Provide reason phrases (e.g., “included because of X/Y/Z evidence”)  
- Surface ethical warnings when content is sensitive or restricted  

---

## 🧩 Data Contracts & Catalog Integrations

| Contract         | Purpose                                | Location / Validator                         |
|------------------|----------------------------------------|----------------------------------------------|
| STAC v1.0        | Layer registration & temporal search   | `data/stac/**` · STAC validator in CI        |
| DCAT 3.0         | Dataset cataloging                     | STAC↔DCAT bridge workflows                   |
| API DTOs         | Strongly typed responses for UI        | `src/services/**` schema guards              |
| A11y Contract    | Route-level a11y thresholds            | `accessibility_scan.yml`                     |
| Ethics Contract  | CARE flags + consent metadata          | `docs/standards/faircare.md` + telemetry     |

CI validates:

- Schemas for STAC, DCAT, and internal DTOs  
- A11y budgets (Lighthouse/axe)  
- Telemetry wiring (no missing required fields)

---

## ⚙️ Build, Environment & Security

| Area      | Standard / Tool   | Notes                                                        |
|-----------|-------------------|--------------------------------------------------------------|
| Build     | Vite + Node LTS   | Deterministic builds, pinned lockfile                       |
| Images    | Non-root base     | CI blocks on CRITICAL (Trivy)                               |
| Headers   | CSP / CORP / COEP | Applied by CDN/reverse proxy                                |
| Secrets   | None in client    | All secrets remain backend-side                             |
| SBOM      | SPDX              | Web deps recorded in `../releases/v10.3.0/sbom.spdx.json`  |

---

## 🔁 CI/CD (Web Tier) — Workflow → Artifact Mapping

| Workflow                 | Enforces                                           | Primary Artifacts                                                     |
|--------------------------|----------------------------------------------------|------------------------------------------------------------------------|
| `docs-lint.yml`          | Markdown/front-matter style consistency            | `docs/reports/self-validation/docs/lint_summary.json`                 |
| `build-and-deploy.yml`   | Web build integrity & deployment health            | `docs/reports/telemetry/build_metrics.json`                           |
| `telemetry-export.yml`   | Merge telemetry metrics across jobs                | `../releases/v10.3.0/focus-telemetry.json`                            |
| `codeql.yml` / `trivy.yml` | Code and dependency security scans              | `docs/reports/security/*.{sarif,json}`                                |
| `accessibility_scan.yml` | Lighthouse/axe-based a11y gating                   | `docs/reports/self-validation/web/a11y_summary.json`                  |

---

## ♿ Accessibility & Inclusive Design

Core practices:

- Semantic HTML + ARIA landmarks  
- Visible focus rings, logical tab order, skip links  
- ≥ 4.5:1 contrast for text; colorblind-safe palettes  
- Proper alt text and `aria-label` usage for non-text UI elements  
- Reduced-motion opt-in; responsive layout for narrow screens  
- Automated CI scanning using axe/Lighthouse  

A11y design tokens and rules are documented in:

    docs/design/tokens/accessibility-tokens.md

---

## 📊 Telemetry & Governance

Web tier telemetry captures:

- Web Vitals (CLS, LCP, FID, etc.)  
- Accessibility metrics (contrast, keyboard coverage, errors)  
- Ethics metrics (CARE flags, sensitive data gating)  
- User interaction summaries (layers toggled, focus queries)  

Runtime telemetry is exported to:

    ../releases/v10.3.0/focus-telemetry.json

Governance events (e.g., sensitive layer activations, consent warnings) are written to:

    ../docs/reports/audit/web-governance-ledger.json

---

## 🧭 Integration with Backend

    flowchart TD
      UI["React UI Layer"] --> API["API Client (REST/GraphQL)"]
      API --> SVC["FastAPI/GraphQL Service Layer"]
      SVC --> GOV["Governance Middleware"]
      GOV --> KG["Neo4j Graph / STAC / DCAT"]
      SVC --> TEL["Telemetry & Logging"]

Data flow:

- UI requests come through API client → backend services  
- Governance middleware enforces CARE and auth constraints  
- Neo4j + STAC/DCAT respond with data + provenance  
- Telemetry and governance logs mirror all critical actions  

---

## 🚀 Local Development

    npm --prefix web install
    npm --prefix web run dev
    npm --prefix web run typecheck
    npm --prefix web run lint
    npm --prefix web run build

Development server runs at:

    http://localhost:3000

---

## 🕰️ Version History

| Version  | Date       | Author              | Summary                                                                     |
|----------|------------|---------------------|-----------------------------------------------------------------------------|
| v10.3.1  | 2025-11-13 | Web Architecture Team | Upgraded to Focus v2.4, aligned with agent-first backend, rule-compliant doc. |
| v10.2.2  | 2025-11-12 | Web Architecture Team | Focus v2.1, streaming catalog UI, a11y & energy telemetry expansion.       |
| v10.0.0  | 2025-11-09 | Web Architecture Team | Initial v10 web architecture (2D/3D, Focus, STAC bridge).                  |
| v9.7.0   | 2025-11-05 | KFM Core Team       | MCP alignment, workflow→artifact mapping, a11y/ethics telemetry.           |