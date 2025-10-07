<div align="center">

# 🗣 Kansas Frontier Matrix — Accessibility Audit: Screen Reader  
`docs/design/reviews/accessibility/screen_reader.md`

**Goal:** Guarantee that every component of the Kansas Frontier Matrix web UI is fully perceivable and navigable  
via assistive technologies (NVDA, JAWS, VoiceOver, Orca). Accessibility is fundamental to the  
**Master Coder Protocol (MCP)** — *if it’s not accessible, it’s not reproducible.*

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#📊-summary-results)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../LICENSE)

</div>

---

## 🎯 Purpose

This audit validates the **semantic correctness**, **ARIA roles**, and **screen-reader readability**  
of the KFM interface across all major regions — **MapLibre**, **Timeline Canvas**, **AI Assistant**,  
and **Detail Panels** — ensuring all content has an accessible **name**, **role**, and **state**.

---

## 🧭 Scope

| Region | Description | Assistive Features Tested |
|---------|--------------|---------------------------|
| **Header & Navigation** | Branding, search, language toggle, help menu | ARIA landmarks (`role="banner"`, `nav`); skip links |
| **Timeline Canvas** | Chronological event visualization | Range input labeling + focus announcements |
| **Map View (MapLibre)** | Map overlays and markers | `aria-label`, `aria-describedby` on controls |
| **Layer Controls** | Toggles, legends, opacity sliders | Dynamic labels + live updates to `aria-pressed` |
| **AI Assistant Panel** | Chat input + responses | `aria-live="polite"` for replies; focus management |
| **Detail Panel** | Entity / event information | Heading hierarchy · `role="region"` for segmentation |

---

## 🧩 Checklist (WCAG 2.1 AA + ARIA 1.2)

| # | Requirement | Status | Notes |
|:--:|--------------|:-------:|-------|
| 1 | Landmarks (`header`, `nav`, `main`, `footer`) present | ✅ | Verified NVDA |
| 2 | Every interactive element has accessible name | ✅ | Buttons, toggles labeled |
| 3 | Dynamic updates via `aria-live` / `role="status"` | ✅ | AI Assistant + alerts |
| 4 | Logical heading hierarchy (`h1–h4`) | ✅ | Verified with VoiceOver rotor |
| 5 | Focused elements announce role + name | ✅ | Timeline + map controls |
| 6 | No duplicate / redundant announcements | ✅ | Nested label cleanup done |
| 7 | Modal focus trap preserves context | ⚙️ | Retest post React update |
| 8 | MapLibre controls visible in accessibility tree | ⚙️ | Pending upstream patch |
| 9 | Timeline Canvas accessible summary | ✅ | `aria-label="Kansas events timeline"` |
| 10 | SVG icons labeled or hidden (`aria-hidden`) | ✅ | Audit complete |

---

## 🧠 Tools & Environment

| Tool | Purpose | Result |
|------|----------|--------|
| NVDA 2023.3 (Windows) | Primary navigation audit | ✅ Pass |
| JAWS 2024 | Landmarks + forms test | ✅ Pass |
| VoiceOver (macOS 14) | Semantic region order | ✅ Pass |
| Chrome A11y Tree | DOM structure + labels | ✅ Pass |
| Axe Core CLI v4.10 | Automated ARIA check | ✅ Pass |
| Lighthouse CI | Accessibility ≥ 90 | ✅ Pass |

---

## 🗂️ Audit Steps

1. Launch site with screen-reader active (NVDA, JAWS, or VoiceOver).  
2. Verify **landmarks** and **regions** are announced in correct order.  
3. Tab through interactive items — ensure descriptive labels + visible focus.  
4. Trigger AI Assistant response → confirm `aria-live` announcements.  
5. Open Detail Panel → check heading hierarchy and labels.  
6. Switch map layers → confirm ARIA state changes.  
7. Document findings → retest post-correction.

---

## 📊 Summary Results

| Section | Status | Notes |
|----------|:------:|-------|
| Header & Navigation | ✅ | Landmarks correct; skip links visible |
| Map View | ⚙️ | Missing roles on zoom controls (PR open) |
| Timeline Canvas | ✅ | Focus + role announcements pass |
| Detail Panel | ✅ | Logical headings, regions confirmed |
| AI Assistant | ✅ | `aria-live="polite"` verified |
| Layer Controls | ✅ | Dynamic `aria-pressed` updates added |
| Global Skip Links | ✅ | Appears and functions correctly |

---

## 🧩 Screen-Reader Focus Flow

```mermaid
flowchart TD
  A["Header\nrole='banner'"] --> B["Navigation\nrole='navigation'"]
  B --> C["Main Content\nrole='main'"]
  C --> D["Timeline Canvas\naria-label='Kansas Events Timeline'"]
  D --> E["Map View\naria-label='Interactive Map of Kansas'"]
  E --> F["Detail Panel\nrole='region' aria-labelledby='entity-title'"]
  F --> G["AI Assistant Drawer\nrole='complementary'"]
  G --> H["Footer\nrole='contentinfo'"]

  style A fill:#E6EFFF,stroke:#0074D9,stroke-width:2px
  style B fill:#F8F8FF,stroke:#6C63FF,stroke-width:1.5px
  style C fill:#FFFDE7,stroke:#FBC02D,stroke-width:1.5px
  style D fill:#E3F2FD,stroke:#1976D2,stroke-width:1.5px
  style E fill:#E8F5E9,stroke:#2E7D32,stroke-width:1.5px
  style F fill:#FFF3C4,stroke:#FFB700,stroke-width:2px
  style G fill:#FFF9C4,stroke:#F57F17,stroke-width:1.5px
  style H fill:#F1F8E9,stroke:#43A047,stroke-width:1.5px

  %% END OF MERMAID
````

---

## 🧩 Recommendations

1. ✅ Add `aria-current="page"` to active nav items.
2. ✅ Apply `aria-describedby` for map markers referencing nearby text.
3. ⚙️ Add ARIA roles to MapLibre custom buttons (zoom / toggle).
4. ⚙️ Retest modal focus after React 18 upgrade.
5. 🧩 Integrate automated **screen-reader regression tests** via Pa11y + NVDA automation.

---

## ⚙️ Continuous Integration (Screen Reader QA)

```yaml
# .github/workflows/a11y_screen_reader.yml
on:
  pull_request:
    paths:
      - "web/src/components/**"
      - "docs/design/reviews/accessibility/screen_reader.md"
jobs:
  screenreader:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install a11y tools
        run: npm i -g axe-core-cli pa11y-ci
      - name: Run ARIA/role audit
        run: pa11y-ci --config .pa11yci.aria.json > aria-report.json
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: screenreader-audit-report
          path: aria-report.json
```

---

## 🧾 Provenance

| Field                  | Value                                                                           |
| ---------------------- | ------------------------------------------------------------------------------- |
| **Reviewer(s)**        | @accessibility-team · @design-lead                                              |
| **Review Date**        | `2025-10-07`                                                                    |
| **Components Audited** | Navigation v0.3.2 · Timeline v0.4.0 · Map Controls v0.5.1 · AI Assistant v0.3.0 |
| **Commit Hash**        | `{{ GIT_COMMIT }}`                                                              |
| **Result**             | ✅ AA Compliant (MapLibre patch pending)                                         |

---

## 🪪 License

Released under **Creative Commons CC-BY 4.0**
© 2025 Kansas Frontier Matrix Design Collective

---

<div align="center">

### 🗣 Kansas Frontier Matrix — Accessibility by Semantics

**Audible · Navigable · Reproducible**

</div>
