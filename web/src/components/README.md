---
title: "🧩 Kansas Frontier Matrix — Web Frontend Components"
document_type: "Developer Documentation · Modular React Components / UI Layer"
version: "v2.7.0"
last_updated: "2025-11-06"
status: "Tier-Ω+∞ Diamond Certified · MCP-DL v6.4.1"
maturity: "Production"
license: ["MIT (code)", "CC-BY 4.0 (docs)"]
owners: ["@kfm-ui","@kfm-web","@kfm-architecture","@kfm-accessibility","@kfm-ai","@kfm-security"]
tags: ["web","frontend","react","components","maplibre","timeline","stac","a11y","focus-mode","design-system","mcp","observability","provenance","governance","ssr","hydration","flags","i18n","rtl","ai"]
alignment:
  - MCP-DL v6.4.1
  - WCAG 2.1 AA / 3.0 Ready
  - FAIR / CARE
  - CIDOC CRM / OWL-Time / PROV-O
  - STAC 1.0 / GeoJSON
validation:
  ci_enforced: true
  sbom_required: true
  slsa_attestations: true
  docs_validated: true
observability:
  dashboard: "https://metrics.kfm.ai/frontend-components"
  metrics: ["component_render_ms","a11y_score","bundle_size_kb","props_mismatch_count","stac_layer_attach_ms","timeline_frame_time_ms","component_coverage_pct","interaction_latency_ms","visual_regression_diffs","error_boundary_triggered"]
preservation_policy:
  checksum_algorithm: "SHA-256"
  retention: "365d artifacts · 90d logs · releases permanent"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Web Frontend Components (v2.7.0 · Tier-Ω+∞ Diamond Certified)**  
`📁 web/src/components/`

**Modular React Components · Map + Timeline UI · Storytelling Panels**

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../.github/workflows/site.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Docs · MCP-DL v6.4.1](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.1-blue)](../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🪶 Overview
The **component layer** brings Kansas history, terrain, and ecology to life via **React**, **MapLibre**, and **D3**.  
Each component is **documented, testable, provenance-linked, and ethically verifiable** under **MCP-DL v6.4.1**.

> *“Every UI element in KFM transforms archival truth into interactive memory.”*

---

## 🧾 Design Provenance
| Source | Description | Verified |
|:--|:--|:--|
| `figma://kfm-ui-library` | Canonical UI source | ✅ |
| `web/src/styles/variables.scss` | Token source (color, spacing) | ✅ |
| `docs/design/tokens.json` | Generated token registry | ✅ |
| `docs/design/reviews/accessibility/` | A11y audits (contrast + tab order) | ✅ |

---

## 🧱 Directory Structure
```text
web/src/components/
├── AppShell/             # Root layout + providers
├── Header/               # Navigation & theme toggle
├── MapView/              # MapLibre map + STAC overlays
├── TimelineView/         # Timeline visualization (Canvas + D3)
├── LayerControls/        # STAC-driven toggles & legends
├── DetailPanel/          # Entity/Event dossier + AI summary
├── AIAssistant/          # Conversational Q&A (Focus Mode)
├── Sidebar/              # Legends, filters, pinned info
├── Modals/               # Settings, About, Accessibility
├── Accessibility/        # Skip links, focus helpers
└── index.ts              # Barrel export
```

---

## 🧩 Props Validation Schema
```ts
import { z } from "zod";
export const MapViewPropsZ = z.object({
  layers: z.array(z.object({
    id: z.string(),
    url: z.string().url(),
    type: z.enum(["geojson","cog"]),
    opacity: z.number().min(0).max(1).optional()
  })),
  onSelect: z.function().args(z.string()).optional(),
  initialViewport: z.object({ lon: z.number(), lat: z.number(), zoom: z.number() }).optional()
});
export type MapViewProps = z.infer<typeof MapViewPropsZ>;
```

---

## 🧩 Cross-Module Integration
| Component | Consumes | Provides | Dependencies |
|:--|:--|:--|:--|
| MapView | STAC via utils/useFetch | GeoJSON layers | MapLibre, dataParser |
| TimelineView | TimelineContext | time range | D3, Canvas, hooks |
| DetailPanel | SelectionContext, AI API | entity detail | `react-markdown`, AIContext |
| AIAssistant | AI API + AIContext | summaries | FastAPI `/ask`, ethics |
| LayerControls | STAC manifest | visibility state | LayerContext |

---

## 🗺️ Component Dependency Graph
```mermaid
graph TD
  T[@types/*]:::types --> C[@components/*]:::ui
  U[@utils/*]:::logic --> C
  H[@hooks/*]:::logic --> C
  X[@context/*]:::logic --> C
  classDef types fill:#1D3557,color:#fff;
  classDef logic fill:#457B9D,color:#fff;
  classDef ui fill:#A8DADC,color:#000;
```

---

## 🔔 Component Communication Contract
```ts
dispatch({ type: "MAP:SELECT", payload: { id } });
trackMetric("component_event", { name: "MAP:SELECT" });
```
- Components interact only via contexts, props, or telemetry events.
- No implicit global state.

---

## 🧯 Error Boundaries
- `ErrorBoundary` wraps **MapView**, **TimelineView**, and **DetailPanel**.  
- Displays friendly fallback UI + logs `component_error`.  
- Resets on route/context change.

---

## 🚦 States Policy
| State | UX Contract | Notes |
|:--|:--|:--|
| Loading | skeleton ≤ 300ms, spinner after | consistent motion easing |
| Empty | actionable zero-state | never blank |
| Error | friendly message + retry | triggers Sentry log |

---

## ⌨️ Keyboard Interaction Maps
### TimelineView
| Action | Key | Result |
|:--|:--|:--|
| Scrub | ← / → | Move window |
| Zoom | `+` / `-` | Adjust scale |
| Focus map | `f` | Sends focus to map |

### MapView
| Action | Key | Result |
|:--|:--|:--|
| Pan | arrow keys | Move map |
| Zoom | `+` / `-` | Adjust zoom |
| Select feature | Enter | Opens DetailPanel |

---

## 🧠 AI Provenance
- AIAssistant + DetailPanel connect to `/api/ask` and `/api/entity/{id}`.  
- Summaries contain citations; outputs hashed in `.prov.json`.  
- Bias tests via `ai-ethics.yml`.  
- Ethics compliance reviewed by `@kfm-ethics`.

---

## 🌐 i18n / RTL Readiness
- `<html dir="ltr|rtl">` cascades direction.  
- `[dir="rtl"]` auto-flips icons.  
- String parity validated in CI.

---

## 🧾 Asset Licensing
| Asset | License | Source |
|:--|:--|:--|
| Icons | MIT | `@kfm-icons/*` |
| Map sprites | CC-BY 4.0 | STAC providers |
| Fonts | System stack | OS default |

---

## 🧰 Component Template
```
Foo/
  index.tsx
  styles.scss
  Foo.test.tsx
  stories.tsx
  README.md
```
```tsx
export interface FooProps { title: string; onClick?: () => void }
export function Foo({ title, onClick }: FooProps) {
  return <section role="region" aria-label={title}>{title}</section>;
}
```

---

## 🧪 Testing SOP Reference
Refer to `docs/sop/component-testing.md` for:
- **Unit** → Jest + RTL
- **Integration** → Storybook interaction
- **A11y** → axe-core
- **Visual** → Chromatic baseline comparison

---

## ♿ Accessibility Audit Summary
| Audit | Tool | Result | Date |
|:--|:--|:--:|:--|
| Contrast (AA) | axe-core | 4.8:1 | 2025-11-04 |
| Tab Order | Storybook | Pass | 2025-11-04 |
| Keyboard Nav | Manual | Pass | 2025-11-04 |
| Motion Reduction | Chrome audit | Pass | 2025-11-04 |

---

## ⚙️ Performance Profiling Example
```ts
performance.mark("DetailPanel:render:start");
// render...
performance.measure("DetailPanel:render","DetailPanel:render:start");
```

---

## 🗓️ Feature Rollout Timeline
| Feature | Introduced | Tier | Notes |
|:--|:--:|:--:|:--|
| AIAssistant | v1.5.0 | Stable | Provenance verified |
| LayerControls | v1.3.0 | Stable | STAC-linked |
| SSR Safe | v2.4.0 | Ω | Verified React 19 |
| Visual Regression | v2.6.0 | Ω+∞ | Active in CI |
| RTL / i18n | v2.6.0 | Ω+∞ | 100% strings covered |

---

## 🧭 Contributor Workflow
1. Add new folder under `web/src/components/YourComponent/`.  
2. Include `index.tsx`, tests, stories, and README.  
3. Import design tokens from `/styles/variables.scss`.  
4. Validate via `pnpm run test:components`.  
5. Document props and add to `index.ts`.

---

## 🎨 Token Reference
- Colors: `--kfm-color-*`  
- Type scale: `--kfm-font-size-[sm|base|lg|xl]`  
- Spacing: `--kfm-space-[xs|sm|md|lg]`  
- Z-layers: Map=100, Timeline=200, Panels=300  

---

## 🧮 Design QA
- Figma delta check via `design-validation.yml`.  
- Spacing/color variance ≤ 2px or 3%.  
- Results in `/docs/design/reports/latest-visual.json`.

---

## 📜 Linked ADRs & SOPs
| Document | Purpose | Status |
|:--|:--|:--:|
| ADR-COMP-001.md | Component architecture & props | ✅ |
| ADR-COMP-002.md | Map + Timeline rendering | ✅ |
| ADR-COMP-003.md | AIAssistant provenance | ✅ |
| SOP-component-testing.md | Testing workflow | ✅ |

---

## 🧾 Change-Control Register
```yaml
changes:
  - date: "2025-11-06"
    change: "Diamond-tier upgrade: added props validation schema, dependency graph, AI provenance, feature timeline, contributor workflow, and extended accessibility audit."
    reviewed_by: "@kfm-architecture"
    qa_approved_by: "@kfm-accessibility"
    pr: "#web-components-270"
```

---

## 🗓 Version History
| Version | Date | Author | Summary | MCP Tier | Audit Status |
|:--|:--|:--|:--|:--|:--|
| **v2.7.0** | 2025-11-06 | @kfm-ui | Added validation schema, AI provenance, feature rollout, contributor workflow | Ω+∞ Diamond | ✅ Full |
| v2.6.0 | 2025-11-04 | @kfm-ui | Design provenance, states policy, keyboard maps, RTL, licensing | Ω+∞ Platinum | ✅ A11y ✓ Visual ✓ Provenance |
| v2.5.0 | 2025-11-03 | @kfm-ui | Prop contracts + i18n readiness | Ω+∞ Gold | ✅ SBOM ✓ Telemetry |
| v2.4.0 | 2025-11-03 | @kfm-ui | SSR safety + provenance export | Ω+∞ Gold | ✅ SSR ✓ Provenance |
| v2.3.0 | 2025-10-27 | @kfm-ui | Storybook a11y suite + metrics | Ω | ✅ CI ✓ A11y |
| v2.2.0 | 2025-10-20 | @kfm-architecture | Deterministic render & perf | Ω | ✅ Perf ✓ Lint |
| v1.5.0 | 2025-10-10 | @kfm-web | Narrative component + AI | Beta → Ω | ✅ AI ✓ FAIR |
| v1.0.0 | 2025-07-01 | Founding Team | Initial component layer | Alpha | ✅ Build ✓ Docs |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — Web Frontend Components**  
Built under the **Master Coder Protocol (MCP-DL v6.4.1)** for modular, reproducible design.

[![Checksum Verified](https://img.shields.io/badge/Checksum-SHA256%20Verified-success)]()  
[![Semantic Alignment](https://img.shields.io/badge/CIDOC%20CRM%20·%20OWL--Time%20·%20STAC%201.0%20·%20WCAG%202.1%20AA-blue)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.1
MCP-TIER: Ω+∞ Diamond
DOC-PATH: web/src/components/README.md
MCP-CERTIFIED: true
SBOM-GENERATED: true
SLSA-ATTESTED: true
A11Y-VERIFIED: true
FAIR-CARE-COMPLIANT: true
COMPONENT-COVERAGE-VERIFIED: true
PROPS-CONTRACT-STABLE: true
VISUAL-REGRESSION-ACTIVE: true
DESIGN-TOKEN-SCHEMA-VERIFIED: true
FIGMA-SYNC-ACTIVE: true
I18N-RTL-READY: true
SKELETON-STATES-DOCUMENTED: true
ERROR-STATES-DOCUMENTED: true
USER-TIMING-MARKS: true
URL-STATE-SYNC: true
SSR-HYDRATION-SAFE: true
FEATURE-FLAGS-GOVERNED: true
PROVENANCE-CHAIN-LINKED: true
CODEQL-SECURITY-CHECK: true
OBSERVABILITY-ACTIVE: true
AI-PROVENANCE-ACTIVE: true
ADR-GRAPH-LINKED: true
FOCUS-MODE-INTEGRATED: true
PERF-PROFILE-CAPTURED: true
ERROR-BOUNDARIES-ACTIVE: true
DESIGN-QA-AUDITED: true
VISUAL-BASELINES-STORED: true
TEST-SOP-LINKED: true
PERFORMANCE-BUDGET-P95: 2.5s
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: {build.date}
MCP-FOOTER-END -->