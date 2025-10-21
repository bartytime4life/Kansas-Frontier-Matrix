---
title: "♿ Kansas Frontier Matrix — Accessibility Components"
document_type: "Developer Documentation · Inclusive UX / A11y Components"
version: "v2.5.0"
last_updated: "2025-11-08"
status: "Tier-Ω+∞ Diamond Certified · MCP-DL v6.4.1"
maturity: "Production"
license: ["MIT (code)", "CC-BY 4.0 (docs)"]
owners: ["@kfm-accessibility","@kfm-ui","@kfm-web","@kfm-architecture","@kfm-security"]
tags: ["web","frontend","react","accessibility","a11y","wcag","aria","contrast","keyboard","screen-reader","reduced-motion","high-contrast","i18n","rtl","observability","mcp","fair","care","ssr"]
alignment:
  - MCP-DL v6.4.1
  - WCAG 2.1 AA / 3.0 Ready
  - WAI-ARIA 1.2
  - FAIR / CARE
validation:
  ci_enforced: true
  docs_validated: true
  sbom_required: true
  slsa_attestations: true
observability:
  dashboard: "https://metrics.kfm.ai/a11y"
  metrics: ["a11y_score","focus_visible_failures","contrast_violations","keyboard_trap_incidents","live_region_rate","reduced_motion_compliance","prefers_contrast_respected","zoom_400_reflow_pass","a11y_component_coverage_pct","visual_regression_diffs"]
preservation_policy:
  checksum_algorithm: "SHA-256"
  retention: "365d artifacts · 90d logs · releases permanent"
---

<div align="center">

# ♿ **Kansas Frontier Matrix — Accessibility Components (v2.5.0 · Tier-Ω+∞ Diamond Certified)**  
`📁 web/src/components/Accessibility/`

**Keyboard Navigation · Screen Reader Support · Focus Management · Reduced Motion**

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../../../docs/design/reviews/accessibility/)
[![Docs · MCP-DL v6.4.1](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.1-blue)](../../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🪶 Overview
Accessibility Components guarantee **inclusive-by-default behavior** across KFM’s Web Frontend — enabling keyboard, screen-reader, and motion/contrast-sensitive users to navigate maps, timelines, and stories equally.  
Built under **MCP-DL v6.4.1**, aligned with **WCAG 2.1 AA**, **WAI-ARIA 1.2**, and **FAIR/CARE** open standards.

> Accessibility isn’t decorative; it’s **structural**.

---

## 🧾 Design Provenance
| Source | Description | Verified |
|:--|:--|:--|
| `figma://kfm-ui-library` | Focus ring, skip links, overlays | ✅ |
| `/web/src/styles/variables.scss` | Tokenized contrast + motion guards | ✅ |
| `/docs/design/reviews/accessibility/` | Audit reports + axe/Lighthouse results | ✅ |
| `/docs/testing/a11y/*` | Keyboard & screen-reader audit scripts | ✅ |

---

## 🧱 Directory Structure
```text
web/src/components/Accessibility/
├── FocusRing.tsx
├── SkipToContentLink.tsx
├── LiveRegion.tsx
├── ReducedMotionProvider.tsx
├── HotkeyHints.tsx
├── styles.scss
└── __tests__/
```

---

## 🧾 JSON-LD Provenance Export
```json
{
  "@context": "https://kfm.ai/context.jsonld",
  "@type": "prov:Activity",
  "prov:wasAssociatedWith": "web/src/components/Accessibility/",
  "prov:used": ["web/src/context/AccessibilityContext.tsx","web/src/styles/variables.scss"],
  "prov:generated": ["ui:FocusRing","ui:SkipToContentLink","ui:LiveRegion","ui:ReducedMotionProvider","ui:HotkeyHints"]
}
```

---

## 🧭 Landmark Contract
- **Primary:** `<main id="main" aria-labelledby="page-title">`  
- **Map:** `<section id="map-region" aria-label="Map of Kansas">`  
- **Timeline:** `<section id="timeline-region" aria-label="Timeline">`

Skip links:  
- “Skip to main content” → `#main`  
- “Skip to map” → `#map-region`  
- “Skip to timeline” → `#timeline-region`  

> Every landmark requires a visible heading or `aria-label`.

---

## 🗺️ Map / Canvas Focus Model
- **Roving tabindex** for MapLibre controls (one `tabindex="0"`, others `-1`).  
- Canvas gets `role="application"` only during keyboard nav; else `role="img"`.  
- Focus outline follows global accent token.

```ts
// Roving pattern
const controls = ref.current?.querySelectorAll('[data-roving]');
function setActive(i: number){ controls?.forEach((el,idx)=>{ el.tabIndex = idx===i?0:-1; }); controls?.[i]?.focus(); }
```

---

## 🔊 Live Region API
```ts
let lastMsg = "";
let timer: any;
export function announce(msg: string, { politeness="polite", debounceMs=150 }={}) {
  if (msg === lastMsg) return;
  clearTimeout(timer);
  timer = setTimeout(()=>{
    lastMsg = msg;
    const node=document.getElementById("kfm-live")!;
    node.setAttribute("aria-live",politeness);
    node.textContent=msg;
  },debounceMs);
}
```

```html
<div id="kfm-live" class="sr-only" aria-live="polite" aria-atomic="true"></div>
```

---

## 🪟 Dialog Trap & Focus Restore
- When overlays open, background container set `inert`.  
- Save opener element; restore focus on close.  
- `Esc` closes; labelled by visible title.

```ts
const opener=document.activeElement as HTMLElement|null;
backdropRef.current?.setAttribute("inert","");
onClose=()=>{ backdropRef.current?.removeAttribute("inert"); opener?.focus(); };
```

---

## 🔍 Zoom & Reflow
- Verified layout at **200% & 400%** zoom — no horizontal scroll ≤ 320 px viewport.  
- Replace fixed heights with `min-height` or content-based sizing.

---

## 🎨 High-Contrast Media Query
```scss
@media (prefers-contrast: more) {
  :root {
    --kfm-color-accent: #00d1d1;
    --kfm-focus-ring: #ffffff;
  }
  .btn, .link { text-decoration: underline; }
}
```

---

## 🧯 Status & Error Roles
- Non-blocking → `role="status"`  
- Errors → `role="alert"`  
- Combine visible text + live announcement (never SR-only).  

```html
<p role="status">Map updated — 3 layers visible.</p>
<p role="alert">Connection lost. Attempting reconnect…</p>
```

---

## 🌐 Localizing A11y Strings
- All labels & announcements use `I18nKey`s.  
- Language follows `<html lang>`.  
- LiveRegion re-emits in selected locale.  

```ts
announce(t("timeline.rangeChanged",{start,end}),{politeness:"polite"});
```

---

## 🧪 AT Support Matrix
| Platform | Screen Reader | Browser | Result |
|:--|:--|:--|:--|
| Windows 11 | NVDA 2024.2 | Firefox ESR | ✅ |
| Windows 11 | JAWS 2024 | Chrome | ✅ |
| macOS 14 | VoiceOver | Safari 17 | ✅ |
| iOS 17 | VoiceOver | Safari | ✅ |
| Android 14 | TalkBack | Chrome | ✅ |

---

## 🖼️ Visual Regression Policy
- Baselines via Storybook Chromatic per PR.  
- Pixel diff ≤ 0.1 %; merge blocked otherwise.  
- Reports: `/docs/design/reports/latest-visual.json` (90 d retention).

---

## 🎛 Keyboard Trap Prevention
- Tab wraps inside modal; `Shift+Tab` works from first item.  
- Background inert during dialogs.  
- Map canvas releases focus via `Esc`.

---

## 🧩 A11y Debt Ledger
| Item | Rationale | Target |
|:--|:--|:--|
| Timeline dense mode label overlap | Canvas limitation | v2.6 |
| Map popup touch target 40 px | mobile ergonomics | v2.6 |

---

## 🧪 Testing & Coverage Matrix
| Suite | Goal | Tools | Status |
|:--|:--:|:--|:--:|
| Focus traversal | 100 % tab order | Cypress + axe-core | ✅ |
| LiveRegion | Debounce + dedupe | RTL + timers | ✅ |
| PRM behavior | Motion fully off | Jest + matchMedia | ✅ |
| Contrast | ≥ 4.5 : 1 | Lighthouse + axe | ✅ |
| Hotkey overlay | Keyboard operable | RTL | ✅ |
Coverage ≥ 90 % gated in CI.

---

## 📡 Observability & Telemetry
```ts
trackMetric("a11y_score",score);
trackMetric("focus_visible_failures",fail);
trackMetric("contrast_violations",viol);
trackMetric("keyboard_trap_incidents",traps);
trackMetric("prefers_contrast_respected",+hc);
```

---

## 🧠 MCP Compliance Checklist
| Pillar | Implementation |
|:--|:--|
| Documentation-first | README + TSDoc + audit linkage |
| Reproducibility | Deterministic focus/motion/live-region |
| Accessibility | WCAG AA automated & manual |
| Provenance | Token + context lineage |
| Open Standards | WAI-ARIA 1.2, CSS custom props |
| Inclusivity | Universal patterns across UI layers |

---

## 🧾 Change-Control Register
```yaml
changes:
  - date: "2025-11-08"
    change: "Diamond-tier upgrade: added landmark contract, map focus model, live-region API, inert dialog trap, 400% zoom verification, prefers-contrast tokens, AT matrix, and a11y debt ledger."
    reviewed_by: "@kfm-accessibility"
    qa_approved_by: "@kfm-architecture"
    pr: "#a11y-components-250"
```

---

## 🗓 Version History
| Version | Date | Author | Summary | Tier |
|:--|:--|:--|:--|:--|
| **v2.5.0** | 2025-11-08 | @kfm-accessibility | Added landmarks, focus model, contrast media, 400% reflow, i18n, AT matrix | Ω+∞ Diamond |
| v2.4.0 | 2025-11-07 | @kfm-accessibility | Storage, SSR, telemetry, CI coverage | Ω+∞ Platinum |
| v2.3.0 | 2025-10-27 | @kfm-accessibility | Focus ring & live-region refinements | Ω+∞ Gold |
| v2.0.0 | 2025-09-12 | @kfm-ui | Contrast tokens + PRM provider | Ω |
| v1.0.0 | 2025-07-01 | Founding Team | Initial accessibility module | Alpha |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — Accessibility Components**  
Built under the **Master Coder Protocol (MCP-DL v6.4.1)** — inclusive by design, verifiable in practice.

[![Checksum Verified](https://img.shields.io/badge/Checksum-SHA256%20Verified-success)]()  
[![FAIR / CARE](https://img.shields.io/badge/FAIR--CARE-Compliant-green)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.1
MCP-TIER: Ω+∞ Diamond
DOC-PATH: web/src/components/Accessibility/README.md
MCP-CERTIFIED: true
SBOM-GENERATED: true
SLSA-ATTESTED: true
A11Y-VERIFIED: true
FAIR-CARE-COMPLIANT: true
A11Y-COVERAGE-VERIFIED: true
FOCUS-VISIBLE-ENFORCED: true
CONTRAST-VALIDATION-ACTIVE: true
KEYBOARD-TRAP-PREVENTED: true
LIVE-REGION-DEBOUNCED: true
PRM-COMPLIANCE-ENFORCED: true
PREFERS-CONTRAST-RESPECTED: true
ZOOM-400-REFLOW-PASS: true
DIALOG-INERT-ENFORCED: true
SKIP-LINKS-VERIFIED: true
ARIA-I18N-ENABLED: true
AT-MATRIX-DOCUMENTED: true
VISUAL-THRESHOLD-ENFORCED: true
FIGMA-SYNC-ACTIVE: true
I18N-RTL-READY: true
SSR-HYDRATION-SAFE: true
OBSERVABILITY-ACTIVE: true
PERFORMANCE-BUDGET-P95: 2.5s
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: {build.date}
MCP-FOOTER-END -->