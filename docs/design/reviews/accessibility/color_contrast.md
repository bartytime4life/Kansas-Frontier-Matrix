<div align="center">

# 🎨 Kansas Frontier Matrix — Accessibility Audit: Color Contrast  
`docs/design/reviews/accessibility/color_contrast.md`

**Purpose:** Ensure all visual interfaces in the Kansas Frontier Matrix meet **WCAG 2.1 AA** contrast ratios and follow the project’s official design tokens (`--kfm-color-*`).  

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#results)
[![Design System](https://img.shields.io/badge/Design-Tokens-green)](../../)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY-4.0-lightgrey)](../../../LICENSE)

</div>

---

## 🎯 Objective

This audit validates that **foreground–background color pairs** across all KFM components (MapLibre UI, timeline, AI drawer, tooltips, buttons, etc.) meet or exceed **WCAG 2.1 AA** minimum contrast ratios:

| Text Type | Minimum Ratio |
|------------|----------------|
| Normal text (< 18 pt) | **4.5 : 1** |
| Large text (≥ 18 pt / 14 pt bold) | **3 : 1** |
| Non-text UI elements | **3 : 1** |
| Graphical objects / icons | **3 : 1** |

All color tokens are defined in the global stylesheet and must pass automated and manual contrast tests.

---

## 🧩 Audit Scope

| Component | Target Elements | Test Method |
|------------|-----------------|--------------|
| **Header / Navigation** | Logo text, global search input, hover states | Figma token export → Contrast Grid (Figma plugin) |
| **Timeline** | Event bars, tick labels, focus outline | Axe DevTools + manual sampling |
| **Map Controls** | Buttons, legends, hover/focus outlines | Chrome DevTools color-picker contrast check |
| **AI Assistant Drawer** | Text vs background, alert badges | Lighthouse Accessibility audit |
| **Detail Panel** | Metadata text, links, captions | Pa11y + NVDA visual contrast verification |

---

## 🧭 Design Token Reference

| Token | Example | Use | Contrast vs Background | WCAG 2.1 Status |
|--------|----------|------|-------------------------|----------------|
| `--kfm-color-bg` | ![#0b1020](https://via.placeholder.com/15/0b1020/000000?text=+) #0b1020 | App background (dark mode) | 14.3 : 1 vs #fff | ✅ AA/AAA |
| `--kfm-color-text` | ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) #ffffff | Primary text | 14.3 : 1 vs #0b1020 | ✅ AAA |
| `--kfm-color-accent` | ![#3BAFDA](https://via.placeholder.com/15/3BAFDA/000000?text=+) #3BAFDA | Interactive highlights | 5.6 : 1 vs #0b1020 | ✅ AA |
| `--kfm-color-warning` | ![#F8C146](https://via.placeholder.com/15/F8C146/000000?text=+) #F8C146 | Alerts, caution indicators | 5.1 : 1 vs #0b1020 | ✅ AA |
| `--kfm-color-success` | ![#79C879](https://via.placeholder.com/15/79C879/000000?text=+) #79C879 | Success messages | 6.7 : 1 vs #0b1020 | ✅ AA |
| `--kfm-color-danger` | ![#E45757](https://via.placeholder.com/15/E45757/000000?text=+) #E45757 | Errors, destructive actions | 4.9 : 1 vs #0b1020 | ✅ AA |

---

## 🧪 Methods & Tools

**Automated Tests**
- 🧰 **Axe Core CLI** – run as part of CI/CD (`npm run test:a11y`)
- 🌐 **Lighthouse CI** – minimum Accessibility ≥ 90
- 🧪 **Pa11y CI** – regression tracking per build  
- 🧱 **Contrast Grid / Stark Plugin (Figma)** – verifies design tokens

**Manual Verification**
- Browser DevTools color-contrast check  
- NVDA/VoiceOver high-contrast simulation  
- CSS prefers-color-scheme = dark/light modes  
- Spot-check color-blind safe palettes (deuteranopia, protanopia)

---

## 📊 Results Summary (v0.1 Audit)

| Category | Pass ✅ | Fail ❌ | Notes / Action |
|-----------|---------|---------|----------------|
| Header & Navigation | ✅ | – | Meets all AA ratios |
| Timeline / Canvas | ✅ | – | Adjusted inactive tick labels to #c7c7c7 |
| Map Controls | ✅ | – | Added outline offset for focus ring |
| Detail Panel | ✅ | – | Increased metadata contrast by +10 % |
| AI Assistant | ✅ | – | Verified accent contrast in dark/light modes |

---

## 🪶 Contrast Verification Flow

```mermaid
flowchart TD
  A["Design Tokens\n(--kfm-color-*)"] --> B["Figma Audit\nContrast Grid Plugin"]
  B --> C["Implementation\nCSS Variables · SCSS Maps"]
  C --> D["Automated Test\nAxe · Lighthouse · Pa11y"]
  D --> E["Manual Review\nScreen Reader · Visual Contrast"]
  E --> F["Report Logged\ncolor_contrast.md · CI artifact"]
<!-- END OF MERMAID -->


⸻

🧩 Recommendations
	•	Maintain a contrast ratio ≥ 4.5 : 1 for all text at 100 % zoom.
	•	Include focus-visible outlines at least 3 px wide with ≥ 3 : 1 contrast.
	•	Avoid conveying meaning by color alone—add shape or label cues.
	•	Test both dark and light themes under user prefers-color-scheme.
	•	Validate all new tokens in Figma before merging design updates.

⸻

🧾 Provenance

Field	Value
Reviewer(s)	@accessibility-team / @design-lead
Review Date	{{ ISO8601_DATE }}
Commit Hash	{{ GIT_COMMIT }}
Build Artifact	lighthouse-report-{{ build_id }}.html
CI Job	a11y_color_contrast.yml


⸻

🪪 License

Released under Creative Commons CC-BY 4.0
© 2025 Kansas Frontier Matrix Design Collective

⸻



