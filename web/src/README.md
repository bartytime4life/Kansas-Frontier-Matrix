---
title: "💻 Kansas Frontier Matrix — Web Application Source Code (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../releases/v10.0.0/focus-telemetry.json"
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
Aligns web modules with **MCP v6.3**, **FAIR+CARE**, **WCAG 2.1 AA**, and the v10 telemetry/spec updates.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview
`web/src/` contains the code that renders the **timeline + map** experience and the **Focus Mode v2** entity context engine.  
The codebase is **standards-first** (STAC/DCAT/JSON-LD) with **accessibility** and **ethics** mechanisms wired into components, hooks, and services.

**Responsibilities**
- Accessible, performant UI for geospatial storytelling  
- Focus Mode v2 summaries + explainability views (UI-only rendering)  
- STAC/DCAT catalog browsing and entity detail retrieval  
- Provenance, telemetry, and governance ledger surfacing

---

## 🗂️ Directory Layout
```
web/src/
├── README.md
│
├── components/                        # FAIR+CARE-compliant UI
│   ├── MapView/                       # MapLibre map and Cesium 3D layers
│   ├── TimelineView/                  # Time navigation + density
│   ├── FocusPanel/                    # AI narratives + relations + explainability
│   ├── LayerControls/                 # STAC/DCAT toggles
│   ├── DetailDrawer/                  # Entity metadata + citations
│   └── Accessibility/                 # Skip links, focus management
│
├── pages/                             # Route-level screens
│   ├── index.tsx                      # Home
│   ├── explorer.tsx                   # Data Explorer
│   ├── focus.tsx                      # Focus Mode UI
│   └── governance.tsx                 # Governance dashboard
│
├── hooks/                             # Shared logic
│   ├── useTelemetry.ts
│   ├── useFocus.ts
│   ├── useGovernance.ts
│   └── useA11y.ts
│
├── context/                           # App providers
│   ├── FocusProvider.tsx
│   ├── ThemeProvider.tsx
│   └── AppProvider.tsx
│
├── services/                          # Data/API clients
│   ├── apiClient.ts                   # REST/GraphQL base (ETag, retries)
│   ├── stacService.ts                 # STAC discovery
│   ├── dcatService.ts                 # DCAT catalog
│   ├── graphService.ts                # Entity details (GraphQL)
│   └── telemetryService.ts            # Build & usage metrics export
│
├── utils/                             # Helpers and guards
│   ├── schemaGuards.ts
│   ├── formatters.ts
│   ├── provenance.ts
│   └── a11y.ts
│
├── styles/                            # Design tokens and themes
│   ├── globals.css
│   ├── tokens.css
│   └── typography.css
│
└── types/                             # Shared TS types for DTOs and entities
    ├── api.ts
    └── domain.ts
```

---

## 🧩 Web Flow (Modules & Data)
```mermaid
flowchart TD
"UI Components" --> "Focus Context (hooks/useFocus)"
"UI Components" --> "MapView / TimelineView"
"Focus Context (hooks/useFocus)" --> "API Client (services/apiClient.ts)"
"MapView / TimelineView" --> "API Client (services/apiClient.ts)"
"API Client (services/apiClient.ts)" --> "Graph Service (entities)"
"API Client (services/apiClient.ts)" --> "STAC/DCAT Services (layers)"
"Graph Service (entities)" --> "FocusPanel (summary + links + provenance)"
```

- **API client** centralizes headers, ETags, and retries.  
- **Schema guards** validate DTOs; fail fast on incompatible responses.  
- **Provenance** utilities attach ledger links and citation chips in UI.

---

## 🧠 Focus Mode (UI Rendering Only)
- **Server** performs inference; UI renders **summaries, relations, explainability links**, and **citations**.  
- CARE-sensitive content is **gated** with consent/citation UI and obfuscation for protected sites.  
- All interactions emit **non-PII telemetry events** (opt-out respected).

---

## ⚙️ Contracts & Validations
| Contract | Purpose | Location |
|---|---|---|
| API DTOs | Typed request/response models | `types/api.ts` |
| Entity Types | People/Places/Events/Documents | `types/domain.ts` |
| STAC/DCAT | Layer/catalog compatibility | `services/{stac,dcat}Service.ts` |
| A11y Contract | Route/page a11y assertions | `hooks/useA11y.ts` (axe/Lighthouse in CI) |

**CI Enforcements:** `docs-lint.yml`, `build-and-deploy.yml`, `telemetry-export.yml`, `codeql.yml`, `trivy.yml`, `accessibility_scan.yml`.

---

## ♿ Accessibility & Inclusive Design
- Keyboard-first navigation, visible focus, skip-to-content.  
- Contrast ≥ 4.5:1; motion-reduced alternatives; descriptive alt text.  
- Live regions and ARIA labels on dynamic elements.  
- **Axe/Lighthouse** checks run per release; results published to telemetry.

---

## 📊 Telemetry & Governance
- **Build metrics:** `docs/reports/telemetry/build_metrics.json`  
- **Release snapshot:** `../../releases/v10.0.0/focus-telemetry.json`  
- **Governance ledgers:** `../../docs/reports/audit/` (workflow runs, approvals)

Telemetry includes workflow durations, a11y scores, STAC/DCAT counts, and commit metadata.

---

## ⚖️ Retention & Policy
| Asset | Retention | Policy |
|---|---|---|
| Build logs | 90 days | CI artifact policy |
| Accessibility scans | 365 days | Certification archive |
| Metadata/Manifests | Permanent | Governance ledger |
| Telemetry JSON | 90 days | Rotating snapshots |

---

## 🕰️ Version History
| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-09 | Web Architecture Team | Upgraded & aligned for v10: Focus v2 UI, Cesium layers, telemetry v2, accessibility budgets. |
| v9.7.0 | 2025-11-05 | KFM Core Team | Contracts, telemetry, CI mappings, a11y hooks. |
| v9.6.0 | 2025-11-03 | KFM Core Team | FAIR+CARE telemetry and Focus Mode UI safeguards. |
| v9.5.0 | 2025-11-02 | KFM Core Team | Explainability and sustainability logging. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Web Architecture](../ARCHITECTURE.md) · [Docs Index](../../docs/README.md)

</div>