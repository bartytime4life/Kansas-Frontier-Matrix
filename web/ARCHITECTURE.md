---
title: "🌐 Kansas Frontier Matrix — Web Application Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/ARCHITECTURE.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../releases/v10.0.0/manifest.zip"
telemetry_ref: "../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-architecture-v2.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Application Architecture**
`web/ARCHITECTURE.md`

**Purpose:**  
Define the FAIR+CARE-aligned technical architecture of the **KFM Web Application** — a modular, accessible, and AI-aware frontend for exploring historical, geospatial, and environmental data.  
Specifies stack, module boundaries, data/telemetry contracts, governance integration, and CI/CD touchpoints for the web tier.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview
The **KFM Web Application** renders the **timeline + map** experience and **Focus Mode v2** insights over a **Neo4j-backed knowledge graph** served via **FastAPI/GraphQL**.  
The web tier is **standards-first** (STAC 1.0, DCAT 3.0, JSON-LD, WCAG 2.1 AA) and **MCP-governed** with telemetry and governance ledgers for every build and release.

**Design goals**
- **Accessibility by default:** WCAG 2.1 AA, semantic HTML, ARIA, keyboard ops  
- **Ethical AI:** Explainable Focus Mode, CARE safeguards, opt-out surfaces  
- **Interoperability:** STAC/DCAT catalogs, JSON-LD semantics, stable APIs  
- **Reproducibility:** Pinned toolchain, SBOM, deterministic builds, telemetry

---

## 🗂️ Directory Layout
```
web/
├── README.md                          # Web tier index
├── ARCHITECTURE.md                    # This file
│
├── public/                            # Static assets (no secrets)
│   ├── images/                        # PNG/SVG with alt text in docs
│   ├── icons/                         # App/feature icons (a11y-ready)
│   └── manifest.json                  # PWA metadata (name, theme, icons)
│
├── src/                               # React + TypeScript application
│   ├── components/                    # Presentational & a11y components
│   │   ├── MapView/                   # MapLibre map + layers (2D) & Cesium (3D)
│   │   ├── TimelineView/              # Time navigation + density bands
│   │   ├── FocusPanel/                # AI summaries + related links + explainability
│   │   ├── LayerControls/             # STAC/DCAT layer toggles
│   │   └── Accessibility/             # Skip links, focus traps, helpers
│   ├── pages/                         # Route-level screens (Home, Explore, Governance)
│   ├── hooks/                         # useTelemetry, useGovernance, useFocus
│   ├── context/                       # App providers (Theme, Focus, Auth)
│   ├── services/                      # API clients (REST/GraphQL, STAC/DCAT)
│   ├── utils/                         # Formatters, intl, schema guards
│   └── styles/                        # Tailwind config, tokens, variables
│
├── package.json                       # Pinned deps + scripts
├── vite.config.ts                     # Vite build config (or next.config.js)
└── telemetry.json                     # Optional local web telemetry cache
```

---

## 🧩 Frontend Stack & Responsibilities
| Layer | Technology | Responsibility |
|---|---|---|
| **Framework** | React 18 + TypeScript | Component model, state, routing |
| **Styling** | Tailwind CSS | Responsive, tokenized, accessible UI |
| **Map** | MapLibre GL JS (+ Cesium) | Vector map rendering, tiled COG overlays, 3D scenes |
| **Charts** | D3 / Recharts | Timeline density, histograms, KPI charts |
| **State** | React Context + lightweight store | Focus Mode, theme, a11y mode |
| **Data** | STAC/DCAT (HTTP), GraphQL, JSON-LD | Catalog discovery + entity details |
| **AI** | Focus Mode v2 (backend inference) | Narratives, relatedness, explainability |
| **A11y** | Semantics + ARIA + Headless patterns | WCAG 2.1 AA conformance |
| **Telemetry** | Web Vitals + custom hooks | Perf, a11y, and ethics metrics export |

---

## 🧱 Component Boundaries
```mermaid
flowchart LR
  map[MapView] --- timeline[TimelineView]
  timeline --- focus[FocusPanel]
  map --- layers[LayerControls]
  focus --- drawer[DetailDrawer]
  map --- legend[Legend]
```

- **MapView:** Base map (2D/3D), layer management, selections, keyboard ops  
- **TimelineView:** Zoomable time scale, focus markers, range brushing  
- **FocusPanel:** AI insights, related People/Places/Events, provenance & citations  
- **LayerControls:** STAC/DCAT layer toggles, opacity, style presets  
- **DetailDrawer/Legend:** Context metadata and symbology

---

## 🧠 Focus Mode (Ethical AI v2)
**Objective:** contextually center on an entity and **explain** the connections.

| Aspect | Implementation |
|---|---|
| API | `GET /api/focus/{entity_id}` → narrative + subgraph + citations + ethics flags |
| Model | `focus_transformer_v2` (server-side); UI renders outputs only |
| Explainability | SHAP/LIME views linkable from FocusPanel; “Why this?” chips |
| CARE Safeguards | Suppress/gate sensitive content; consent & source attribution |
| Telemetry | `focus` events → `../releases/v10.0.0/focus-telemetry.json` with a11y & ethics flags |

---

## 🧩 Data Contracts & Catalogs
| Contract | Purpose | Source |
|---|---|---|
| **STAC Items/Collections** | Geospatial layers, temporal bounds | `data/stac/**` |
| **DCAT 3.0** | Dataset catalog for search & metadata | STAC↔DCAT bridge |
| **Web → API DTOs** | Strongly typed responses for UI | `src/services/*` |
| **A11y Contract** | Route-level a11y test gates | `accessibility_scan.yml` |

**Validation:** CI enforces schema/contract compliance before deploy.

---

## ⚙️ Build, Env & Security
| Area | Standard | Notes |
|---|---|---|
| Build | Vite / Next | Deterministic, pinned deps |
| Images | Non-root base | CI fails on **CRITICAL** (Trivy) |
| Headers | CSP / CORP / COEP | Enforced at hosting layer |
| Secrets | None client-side | All keys server-side only |
| SBOM | SPDX for web deps | Referenced in release manifest |

---

## 🔁 CI/CD (Web Tier) — Workflow → Artifact Mapping
| Workflow | Enforces | Primary Artifacts |
|---|---|---|
| `docs-lint.yml` | Markdown/YAML/JSON style + front-matter | `reports/self-validation/docs/lint_summary.json` |
| `build-and-deploy.yml` | Build + deploy web app | `docs/reports/telemetry/build_metrics.json` |
| `telemetry-export.yml` | Merge metrics from all jobs | `../releases/v10.0.0/focus-telemetry.json` |
| `codeql.yml` / `trivy.yml` | Static/code & CVE scans | `reports/security/*` |
| `accessibility_scan.yml` | A11y budget (axe/Lighthouse) | `reports/self-validation/web/a11y_summary.json` |

---

## ♿ Accessibility & Inclusive Design
**Core rules**
- Keyboard navigation: tab order, focus rings, skip links  
- Contrast ≥ **4.5:1** (text), **3:1** (large)  
- Alt text for all non-text assets; ARIA labels for landmarks & controls  
- Reduced motion option; content reflow for narrow viewports  
- Lighthouse/axe checks per release (`accessibility_scan.yml`)

**Docs:** see `../docs/standards/ui_accessibility.md`.

---

## 📊 Telemetry & Governance
- **Web Vitals** and custom **a11y/ethics** metrics exported via hooks  
- Build metrics recorded in `docs/reports/telemetry/build_metrics.json`  
- Release snapshot aggregates to `../releases/v10.0.0/focus-telemetry.json`  
- Governance events (e.g., sensitive layer flags) are ledgered under `docs/reports/audit/`

**Example Telemetry Snippet**
```json
{
  "component": "MapView",
  "web_vitals": { "cls": 0.03, "lcp_ms": 1340, "fid_ms": 8 },
  "a11y": { "contrast_ok": true, "keyboard_ok": true },
  "ethics": { "care_flag": false },
  "timestamp": "2025-11-09T18:11:03Z"
}
```

---

## 🧭 Integration with Backend
```mermaid
flowchart TD
"React UI" --> "API Client (REST/GraphQL)"
"API Client (REST/GraphQL)" --> "FastAPI (server)"
"FastAPI (server)" --> "Neo4j (graph)"
"FastAPI (server)" --> "STAC/DCAT (catalog)"
"FastAPI (server)" --> "Telemetry & Ledgers"
```

- UI fetches **entities** (GraphQL) and **layers** (STAC/DCAT).  
- Focus Mode runs server-side; only summarized outputs return to UI.  
- Provenance chips link to ledger entries and catalog metadata.

---

## 🕰️ Version History
| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-09 | Web Architecture Team | Upgraded to v10: Focus v2, 3D scenes, streaming catalog, a11y budgets, telemetry v2. |
| v9.7.0 | 2025-11-05 | KFM Core Team | MCP v6.3 alignment; workflow→artifact map, a11y/ethics telemetry, contracts table. |
| v9.6.0 | 2025-11-03 | KFM Core Team | Sustainability & a11y telemetry; Focus safeguards. |
| v9.5.0 | 2025-11-02 | KFM Core Team | Explainability and governance middleware. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Web Index](README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
