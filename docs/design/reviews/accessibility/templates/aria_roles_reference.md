<div align="center">

# 🧭 Kansas Frontier Matrix — **ARIA Roles & Landmark Reference (Tier-Ω+∞ Certified)**  
`docs/design/reviews/accessibility/templates/aria_roles_reference.md`

**Mission:** Define **canonical ARIA + semantic HTML patterns** for the Kansas Frontier Matrix (KFM) — spanning **React**, **MapLibre**, and **HTML5 Canvas** — so every UI exposes correct **Name · Role · State (NRS)** to assistive tech.  
This guide is **MCP-DL v6.3+** compliant, audit-ready, and wired for CI validation, observability, and FAIR/CARE traceability.

[![WCAG 2.1 AA | 3.0 ready](https://img.shields.io/badge/WCAG-2.1%20AA%20%7C%203.0%20ready-yellow)](../wcag_checklist.md)  
[![WAI-ARIA 1.2](https://img.shields.io/badge/WAI--ARIA-1.2-blue)](https://www.w3.org/TR/wai-aria-1.2/)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../standards/documentation.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM — ARIA Roles & Landmark Reference"
document_type: "A11y Reference"
version: "v3.0.0"
last_updated: "2025-11-11"
owners: ["@kfm-accessibility","@kfm-web","@kfm-design"]
reviewed_by: ["@kfm-design-council","@kfm-ethics"]
status: "Stable"
maturity: "Production"
license: "CC-BY-4.0"
tags: ["aria","landmarks","live-regions","maplibre","canvas","react","wcag","a11y","observability","ci"]
alignment:
  - MCP-DL v6.3
  - WCAG 2.1 AA
  - WAI-ARIA 1.2
  - Section 508
  - EN 301 549
  - ISO 9241-171
validation:
  ci_enforced: true
  zero_critical_aria_violations: true
  nrs_required: true   # Name·Role·State
observability:
  endpoint: "https://metrics.kfm.ai/a11y/aria"
  metrics_exported: ["aria_violations", "duplicate_labels", "live_region_misuse", "nrs_coverage"]
---
```

---

## 🎯 Objective
Establish **do/don’t** patterns for landmarks, widgets, and live regions that guarantee:
- Correct **landmark structure** for SR rotors (NVDA/JAWS/VO/Orca).  
- Accurate **Name · Role · State** for every interactive control.  
- Predictable **announcement behavior** for dynamic updates (AI streaming, timeline scrubs, map layer changes).  
- Minimal **over-announcement** and zero **keyboard/SR traps**.

---

## 🗺️ Landmark Roles (Page Structure · one source of truth)

> **Rule of 1:** Only one `<main>` and typically one `banner` and `contentinfo` per page/app shell.

| Region | HTML | Role | Required Labeling | Notes |
|:--|:--|:--|:--|:--|
| Header | `<header>` | `banner` | Optional | Top-level brand & global actions. |
| Navigation | `<nav>` | `navigation` | `aria-label="Primary Navigation"` | Use additional labeled navs for sidebars. |
| Main | `<main>` | `main` | — | Only once. Houses primary content. |
| Sidebar / Layers | `<aside>` | `complementary` | `aria-label="Layer Controls"` | Contextual tools, not core content. |
| Timeline | `<section>` | `region` | `aria-labelledby="timeline-title"` | Region must be named by visible heading. |
| AI Assistant | `<section>` | `complementary` | `aria-label="AI Assistant"` | Non-blocking drawer; return focus on close. |
| Footer | `<footer>` | `contentinfo` | — | Ownership, license, and meta links. |

**Anti-patterns**
- ❌ Multiple `<main>`.  
- ❌ Empty landmark containers (no content / no label).  
- ❌ Using `role="main"` on elements without being the primary content.

---

## 🔘 Widget & Control Roles (with NRS patterns)

| Control | Prefer | ARIA / Attributes | Keyboard | Notes |
|:--|:--|:--|:--|:--|
| Button | `<button>` | `role="button"` (only if custom) | `Enter/Space` | Use native first; ensure visible label. |
| Toggle | `<button aria-pressed>` | `aria-pressed="true/false"` | `Enter/Space` | For layer on/off. |
| Checkbox | `<input type="checkbox">` | `role="checkbox"` (custom) + `aria-checked` | `Space` | Use for multi-select filters. |
| Radio group | `<fieldset>` + radios | parent `role="radiogroup"` | Arrow keys | Use for basemap choice. |
| Slider | `<input type="range">` | `role="slider"` + `aria-valuemin/max/now` | Arrows / Pg / Home/End | Timeline scrubber exposes `aria-valuetext`. |
| Menu / Menuitem | Native list | `role="menu"` / `menuitem` (only for app menus) | Arrows | Prefer `navigation` + links for site menus. |
| Dialog | `<dialog>` / `<div>` | `role="dialog"` + `aria-modal="true"` + labeledby | Trap focus · `Esc` closes | Restore focus to opener. |
| Tooltip | `<div>` | `role="tooltip"` + id; trigger `aria-describedby=id` | Focus/hover | Tooltips must appear on **focus**. |
| Search | `<form role="search">` | `role="search"` + labeled input | `Enter` | Autocomplete uses combobox pattern (below). |
| Combobox | `<input>` + listbox | `role="combobox"` + `aria-expanded`, `aria-controls`, `aria-activedescendant` | Arrows / `Enter` | For global search suggestions. |

**Name · Role · State (NRS) checklist**
- **Name**: visible text or `aria-label`/`aria-labelledby`.  
- **Role**: native element or ARIA role for custom.  
- **State**: `aria-pressed`, `aria-checked`, `aria-selected`, `aria-expanded`, `aria-busy`, etc.

---

## 📢 Live Regions (Dynamic Update Taxonomy)

> **Golden rule:** *Buffer then summarize.* Avoid token-by-token announcements for streaming content.

| Use Case | Role/Property | Priority | Example Announcement |
|:--|:--|:--:|:--|
| Status info (non-critical) | `role="status"` or `aria-live="polite"` | 🟡 | “Layer ‘Treaties’ enabled.” |
| Alerts (critical) | `role="alert"` (assertive) | 🔴 | “Connection lost. Retry available.” |
| AI streaming | container `aria-live="polite"` (buffered) | 🟡 | “Assistant response ready.” (summary) |
| Loading region | `aria-busy="true"` → `false` | 🟡 | “Loading timeline events…” then clear. |
| Search results | Combobox pattern | 🟡 | “5 results. Use up/down arrows to navigate.” |

**Anti-patterns**
- ❌ Announcing every keystroke or token.  
- ❌ Nesting multiple live regions that compete.  
- ❌ Using assertive for routine updates.

---

## 🗺️ MapLibre & Canvas Accessibility (KFM contracts)

| Area | Implementation | ARIA Strategy |
|:--|:--|:--|
| Map container | `<div>` | Only region using `role="application"`. Provide help text: “Press Esc to exit map.” |
| Map toolbar | `<div role="toolbar">` | Group zoom, locate, layers; each control focusable; labeled by text. |
| Zoom / locate / layer buttons | Native `<button>` | Visible label or `aria-label`; 2px+ focus ring; `title` is **supplemental** only. |
| Marker popups | `<div role="dialog" aria-modal="true">` | Provide `aria-labelledby` + `aria-describedby`. |
| Map summary | SR-only `<section role="region">` | Lists visible layers, selected features, and textual extent. |
| Timeline (Canvas) | `<div role="region">` + slider | Slider exposes `aria-valuemin/max/now` + `aria-valuetext`. Provide hidden summary of visible range. |

**Do**: Keep semantics outside the map standard (no `application` on the whole app).  
**Don’t**: Trap focus inside map without **Esc** escape & restore.

---

## 🧠 Patterns for Complex Widgets

### A. Roving Tabindex (grid, toolbar)
- Only **one** child has `tabindex="0"` at a time; others `-1`.  
- Arrow keys move focus; Tab moves **out** of the widget.  
- Announce position: `aria-posinset` / `aria-setsize` if applicable.

### B. Disclosures & Accordions
- Button with `aria-expanded` + `aria-controls="#panelId"`.  
- Panel is focusable only if interactive content exists.  
- Heading structure remains logical (`h2`/`h3`).

### C. Combobox + Listbox (Search)
```html
<input
  role="combobox"
  aria-expanded="false"
  aria-controls="search-list"
  aria-autocomplete="list"
  aria-activedescendant=""
/>
<ul id="search-list" role="listbox">
  <li role="option" id="opt-1" aria-selected="false">Treaties 1867</li>
</ul>
```

---

## 🌍 Localization, RTL & High-Contrast

- Set document language (`<html lang="en">`) and per-element `lang` for localized quotes.  
- RTL: use **logical properties** (`margin-inline-start`) and verify **focus flow mirrors layout**.  
- High Contrast Mode (Windows): ensure outline and icon glyphs remain visible; avoid color-only focus cues.

---

## ⚠️ ARIA Anti-Patterns (Never do)

- ❌ Add `role="button"` to a link that **navigates**; use a `<a>` with clear text instead.  
- ❌ Use `role="presentation"` on focusable or interactive content.  
- ❌ Hide required content with `aria-hidden="true"` to “fix” duplicate announcements — fix redundancy instead.  
- ❌ Overuse `role="application"`; reserve for map canvas interactions only.

---

## 🛠️ Code Snippets (React)

**Accessible Toggle Button**
```tsx
function LayerToggle({label, pressed, onToggle}) {
  return (
    <button
      type="button"
      aria-pressed={pressed}
      aria-label={label}
      onClick={onToggle}
      className="focus-visible:outline-2 focus-visible:outline-offset-2"
    >
      {label}
    </button>
  );
}
```

**Dialog with Focus Restore**
```tsx
const openerRef = useRef<HTMLButtonElement>(null);
const [open, setOpen] = useState(false);

return <>
  <button ref={openerRef} onClick={()=>setOpen(true)}>Open details</button>
  {open && (
    <div role="dialog" aria-modal="true" aria-labelledby="dlg-title">
      <h2 id="dlg-title">Entity details</h2>
      <button onClick={()=>{ setOpen(false); openerRef.current?.focus(); }}>Close</button>
    </div>
  )}
</>;
```

---

## 🧪 CI Validation (eslint + axe + testing-library)

```yaml
# .github/workflows/a11y_aria_validate.yml
on:
  pull_request:
    paths:
      - "web/src/**/*.tsx"
      - "docs/design/reviews/accessibility/templates/aria_roles_reference.md"
jobs:
  aria:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install a11y toolchain
        run: npm i -D eslint-plugin-jsx-a11y @testing-library/react @testing-library/jest-dom axe-core jest-axe
      - name: Lint ARIA usage (JSX)
        run: npx eslint "web/src/**/*.{ts,tsx}" --max-warnings=0
      - name: Unit a11y tests (jest-axe)
        run: npx jest --config=jest.a11y.config.cjs
      - name: Axe e2e (Playwright)
        run: node tools/a11y/run-axe-routes.mjs --routes "/,/map,/story/1"
```

> **Gate:** Merge only if **0 critical ARIA violations** and NRS coverage = **100%** on changed routes.

---

## 📈 Observability Hook (ARIA Metrics)

```yaml
aria_metrics:
  export_to: "https://metrics.kfm.ai/a11y/aria"
  fields: ["aria_violations","duplicate_labels","live_region_misuse","nrs_coverage"]
  retention_days: 180
```

---

## 🧾 Provenance Metadata (example)

```yaml
review_id: "aria_roles_ref_v3.0.0"
reviewed_by: ["@kfm-accessibility","@kfm-web"]
commit: "{{ GIT_COMMIT }}"
wcag_level: "AA"
aria_version: "1.2"
conformance: "Pass"
notes: "Landmarks, widgets, and live regions validated for React + MapLibre + Canvas."
```

---

## 🔄 FAIR / CARE JSON-LD

```json
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "KFM — ARIA Roles & Landmark Reference",
  "license": "CC-BY-4.0",
  "version": "v3.0.0",
  "dateModified": "2025-11-11",
  "creator": "Kansas Frontier Matrix Accessibility Council",
  "alignment": ["MCP-DL v6.3","WCAG 2.1 AA","WAI-ARIA 1.2","FAIR","CARE"]
}
```

---

## 🧾 Governance Ledger & Version History

| Date | Reviewer | Area | Outcome | SHA-256 |
|:--|:--|:--|:--|:--|
| 2025-11-11 | @kfm-accessibility | Landmarks/Widgets | ✅ | `sha256:ab1…` |
| 2025-11-11 | @kfm-design | Tokens & focus visuals | ✅ | `sha256:c23…` |
| 2025-11-11 | @kfm-web | Implementation QA | ✅ | `sha256:d44…` |

| Version | Date | Author | Summary | Type |
|:--|:--|:--|:--|:--|
| **v3.0.0** | 2025-11-11 | @kfm-accessibility | Tier-Ω+∞: added anti-patterns, MapLibre/Canvas contracts, NRS policy, CI lint/tests, observability, FAIR/CARE metadata. | Major |
| v2.0.0 | 2024-10-05 | @kfm-accessibility | Expanded live-region taxonomy & combobox patterns. | Minor |
| v1.0.0 | 2023-06-20 | Founding Team | Initial ARIA landmarks & widget roles guide. | Major |

---

<div align="center">

### 🧭 Kansas Frontier Matrix — Semantic Accessibility Framework  
**Structured · Auditable · Inclusive · Observable**

<!-- MCP-CERTIFIED: TIER Ω+∞ -->
<!-- VERIFIED-STANDARDS: [MCP-DL v6.3, WCAG 2.1 AA, WAI-ARIA 1.2, Section 508, EN 301 549, ISO 9241-171, FAIR, CARE] -->
<!-- VALIDATION-HASH: sha256:a11y-aria-roles-ref-v3-0-0-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -->

</div>
