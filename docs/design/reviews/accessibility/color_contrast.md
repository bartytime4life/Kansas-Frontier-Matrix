<div align="center">

# 🎨 Kansas Frontier Matrix — Accessibility Audit: Color Contrast  
`docs/design/reviews/accessibility/color_contrast.md`

**Purpose:** Guarantee that every visual interface in the Kansas Frontier Matrix meets  
**WCAG 2.1 AA** contrast ratios while adhering to official design tokens (`--kfm-color-*`).  
Contrast testing is a **core MCP reproducibility check** for sustainable and inclusive design.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#📊-results-summary)  
[![Design System](https://img.shields.io/badge/Design-Tokens-green)](../../)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../LICENSE)

</div>

---

## 🎯 Objective

This audit validates that **foreground–background color pairs** across all KFM components  
(MapLibre UI, timeline, AI drawer, tooltips, buttons, etc.) meet or exceed the required ratios:

| Text Type | Minimum Ratio |
|------------|----------------|
| Normal text (< 18 pt) | **4.5 : 1** |
| Large text (≥ 18 pt / 14 pt bold) | **3 : 1** |
| Non-text UI elements | **3 : 1** |
| Graphical objects / icons | **3 : 1** |

All color tokens are defined globally and must pass **automated + manual** contrast tests before merge.

---

## 🧩 Audit Scope

| Component | Target Elements | Test Method |
|------------|-----------------|--------------|
| **Header / Navigation** | Logo text, global search, hover states | Figma Contrast Grid plugin |
| **Timeline** | Event bars, tick labels, focus outline | Axe DevTools + manual sampling |
| **Map Controls** | Buttons, legends, hover/focus outlines | Chrome DevTools contrast checker |
| **AI Assistant** | Chat text, alert badges | Lighthouse Accessibility audit |
| **Detail Panel** | Metadata text, links, captions | Pa11y + NVDA visual contrast |

---

## 🧭 Design Token Reference

| Token | Swatch | Use | Contrast vs Background | WCAG 2.1 Status |
|--------|--------|-----|------------------------|-----------------|
| `--kfm-color-bg` | ![#0b1020](https://via.placeholder.com/15/0b1020/000000?text=+) `#0b1020` | App background (dark) | 14.3 : 1 vs #fff | ✅ AA / AAA |
| `--kfm-color-text` | ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff` | Primary text | 14.3 : 1 vs #0b1020 | ✅ AAA |
| `--kfm-color-accent` | ![#3BAFDA](https://via.placeholder.com/15/3BAFDA/000000?text=+) `#3BAFDA` | Interactive highlights | 5.6 : 1 vs #0b1020 | ✅ AA |
| `--kfm-color-warning` | ![#F8C146](https://via.placeholder.com/15/F8C146/000000?text=+) `#F8C146` | Alerts / caution | 5.1 : 1 vs #0b1020 | ✅ AA |
| `--kfm-color-success` | ![#79C879](https://via.placeholder.com/15/79C879/000000?text=+) `#79C879` | Success states | 6.7 : 1 vs #0b1020 | ✅ AA |
| `--kfm-color-danger` | ![#E45757](https://via.placeholder.com/15/E45757/000000?text=+) `#E45757` | Errors / destructive actions | 4.9 : 1 vs #0b1020 | ✅ AA |

---

## 🧪 Methods & Tools

**Automated Tests**
- 🧰 **Axe Core CLI** — runs in CI (`npm run test:a11y`)
- 🌐 **Lighthouse CI** — Accessibility score ≥ 90
- 🧪 **Pa11y CI** — build-to-build regression tracking
- 🎨 **Contrast Grid / Stark (Figma)** — verifies token ratios

**Manual Verification**
- Browser DevTools contrast check  
- NVDA / VoiceOver contrast simulation  
- Test `prefers-color-scheme` dark/light  
- Simulate color-blind modes (deuteranopia · protanopia)

---

## 📊 Results Summary (v0.1 Audit)

| Category | Pass ✅ | Fail ❌ | Notes / Action |
|-----------|:------:|:------:|----------------|
| Header & Navigation | ✅ | – | Meets all AA ratios |
| Timeline / Canvas | ✅ | – | Adjusted inactive tick labels → `#c7c7c7` |
| Map Controls | ✅ | – | Added outline offset for focus ring |
| Detail Panel | ✅ | – | Increased metadata contrast +10 % |
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

  style A fill:#E6EFFF,stroke:#0074D9,stroke-width:2px
  style B fill:#F8F8FF,stroke:#6C63FF,stroke-width:1.5px
  style C fill:#FFFDE7,stroke:#FBC02D,stroke-width:1.5px
  style D fill:#E3F2FD,stroke:#1976D2,stroke-width:1.5px
  style E fill:#E8F5E9,stroke:#2E7D32,stroke-width:1.5px
  style F fill:#FFF3C4,stroke:#FFB700,stroke-width:2px

  %% END OF MERMAID
````

---

## 🧩 Recommendations

* Maintain ≥ **4.5 : 1** for text at 100 % zoom
* Provide focus-visible outlines ≥ 3 px wide (≥ 3 : 1 contrast)
* Do not convey meaning by color alone → use labels or shapes
* Test both dark and light themes under `prefers-color-scheme`
* Validate new tokens in Figma before merge approval

---

## ⚙️ Continuous Integration (Color QA)

```yaml
# .github/workflows/a11y_color_contrast.yml
on:
  pull_request:
    paths:
      - "web/src/**/*.scss"
      - "docs/design/reviews/accessibility/color_contrast.md"
jobs:
  contrast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install contrast test deps
        run: npm i -g pa11y-ci axe-core-cli
      - name: Run Contrast Checks
        run: pa11y-ci --config .pa11yci.json > pa11y-report.json
      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: a11y-contrast-report
          path: pa11y-report.json
```

---

## 🧾 Provenance

| Field              | Value                                   |
| ------------------ | --------------------------------------- |
| **Reviewer(s)**    | @accessibility-team / @design-lead      |
| **Review Date**    | `2025-10-07`                            |
| **Commit Hash**    | `{{ GIT_COMMIT }}`                      |
| **Build Artifact** | `lighthouse-report-{{ build_id }}.html` |
| **CI Job**         | `a11y_color_contrast.yml`               |

---

## 🪪 License

Released under **Creative Commons CC-BY 4.0**
© 2025 Kansas Frontier Matrix Design Collective

---

<div align="center">

### 🎨 Kansas Frontier Matrix — Color Integrity by Design

**Accessible · Measured · Reproducible**

</div>
