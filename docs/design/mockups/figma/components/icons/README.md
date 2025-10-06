<div align="center">

# 🎨 Kansas Frontier Matrix — Figma Icon Components  
`docs/design/mockups/figma/components/icons/`

**Mission:** Define the **iconography system** for the **Kansas Frontier Matrix (KFM)**  
to ensure consistency, accessibility, and scalability across Figma and React.  

Icons act as universal signifiers in KFM — connecting **map tools, filters, actions,  
and narratives** with clear, meaningful, and minimal visual language.  

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-Figma%20Components-pink)](https://www.figma.com)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-yellow)](../../../../../LICENSE)

</div>

---

## 🗂️ Directory Layout

```

icons/
├── README.md              → Design standards and usage guidelines (this file)
├── examples.md            → Visual & React icon usage patterns
├── tokens.json            → Icon size, color, and stroke weight definitions
├── figma-refs.json        → Figma icon component IDs and version data
├── accessibility.md       → ARIA labeling and WCAG compliance for icons
└── changelog.md           → Update history for icon library and assets

````

---

## 📘 Overview

Icons in the Kansas Frontier Matrix design system are:  
- 🧭 **Functional** — convey meaning instantly, not decoration  
- 🧩 **Modular** — token-driven with scalable sizes and consistent geometry  
- ♿ **Accessible** — labeled for assistive tech and non-visual use  
- 🧱 **Reproducible** — unified naming between Figma and React libraries  

The **Figma Icon Library** is mirrored in the **React icon set**, allowing  
designers and developers to share one canonical source of truth.

---

## 🧭 Design Principles

| Principle | Description |
|:-----------|:-------------|
| **Clarity** | Icons should communicate their purpose instantly without ambiguity. |
| **Consistency** | Use a uniform grid, stroke weight, and corner radius across all icons. |
| **Scalability** | Icons must render clearly at `16px`, `20px`, `24px`, and `32px`. |
| **Accessibility** | Every interactive icon must have an accessible name (`aria-label`). |
| **Neutral Aesthetic** | Icons complement KFM’s visual hierarchy — clean, geometric, timeless. |

---

## 🎨 Icon Grid & Style Rules

| Property | Standard |
|:----------|:----------|
| **Canvas Size** | 24×24 px |
| **Grid System** | 2 px base grid |
| **Stroke Width** | 1.5 px (variable by weight) |
| **Corner Radius** | 2 px min |
| **Style Tokens** | Color + weight derived from `tokens.json` |
| **Color Variables** | `--color-fg`, `--color-fg-muted`, `--color-accent` |

> 🧩 *All icons adhere to Material Design-level optical balance but follow KFM’s geometry language.*

---

## 🧱 Categories

| Category | Examples | Usage |
|:----------|:----------|:------|
| **System** | `search`, `close`, `menu`, `settings`, `help` | Core UI controls |
| **Map & Geo** | `pin`, `layer`, `terrain`, `compass`, `zoom-in/out` | Map viewer + geographic controls |
| **Timeline & Data** | `calendar`, `clock`, `filter`, `graph`, `slider` | Temporal + data-driven UI |
| **Documentary** | `book`, `photo`, `map`, `paperclip`, `link` | Document & source visualization |
| **Navigation** | `arrow-left/right/up/down`, `chevron`, `home`, `route` | Motion + hierarchy controls |
| **Accessibility** | `eye`, `keyboard`, `speaker`, `contrast` | Accessibility UI states |

---

## 🧩 Naming Convention

| Layer | Format | Example |
|:-------|:---------|:----------|
| **Figma Component** | `ic/{category}/{name}` | `ic/system/search` |
| **React Component** | `Icon{Name}` | `IconSearch`, `IconFilter` |
| **File Name** | `icon-{name}.svg` | `icon-search.svg` |
| **Variable Alias** | `--icon-{name}` | `--icon-pin` |

> ⚙️ Example:  
> Figma → `ic/map/pin` → React → `<IconPin />` → Asset → `/icons/pin.svg`

---

## 🧩 Design Tokens (icons/tokens.json)

| Token | Description | Example Value |
|:-------|:-------------|:---------------|
| `--icon-size-sm` | Small interface icon (toolbars, badges) | `16px` |
| `--icon-size-md` | Default icon size | `20px` |
| `--icon-size-lg` | Large context icons | `24px` |
| `--icon-size-xl` | Hero or map icons | `32px` |
| `--icon-color-default` | Standard icon color | `#333333` |
| `--icon-color-accent` | Emphasized icon color | `#0057B7` |
| `--icon-stroke-weight` | Line width for vector paths | `1.5` |

---

## 🧠 Implementation Notes

### Figma
- Each icon exists as a **single component instance** (`ic/{category}/{name}`).
- Export format: `.SVG` with preserved layer names.
- Use Figma Variants for filled, outlined, and dual-tone styles.
- Maintain centralized token linkage to theme colors.

### React
- Icons are imported from `/web/src/icons/` and rendered as React components.
- Supports `size`, `color`, and `title` props for customization.
- Example:

```tsx
import { IconFilter, IconPin } from "@/icons";

function Toolbar() {
  return (
    <div className="kfm-toolbar">
      <IconFilter size="20" color="var(--icon-color-accent)" title="Filter layers" />
      <IconPin size="20" color="var(--icon-color-default)" title="Drop pin" />
    </div>
  );
}
````

---

## ♿ Accessibility Guidelines

| Requirement              | Description                                                              |
| :----------------------- | :----------------------------------------------------------------------- |
| **Non-Decorative Icons** | Must include `role="img"` and `aria-label` or `<title>`.                 |
| **Decorative Icons**     | Must include `aria-hidden="true"`.                                       |
| **Clickable Icons**      | Wrapped in `<button>` or `<a>`; never use raw `<svg>` for interactivity. |
| **Focus State**          | Must include visible ring (driven by `--shadow-focus`).                  |
| **Text Alternatives**    | Labels should convey same meaning as visual icon.                        |

Example:

```html
<button aria-label="Open settings">
  <svg role="img" aria-hidden="false">
    <title>Settings</title>
    <use href="#icon-settings" />
  </svg>
</button>
```

---

## 🧩 Example Usage Table

| Icon | React Component      | Purpose                        |
| :--- | :------------------- | :----------------------------- |
| 🔍   | `<IconSearch />`     | Global search and filters      |
| 🗺️  | `<IconMap />`        | Map navigation                 |
| 🕓   | `<IconClock />`      | Timeline or time range filter  |
| 📎   | `<IconAttachment />` | Linking sources or documents   |
| ⚙️   | `<IconSettings />`   | Preferences and tools menu     |
| 🧭   | `<IconCompass />`    | Directional navigation         |
| 🔈   | `<IconSpeaker />`    | Audio or oral history elements |

---

## 🧪 QA Checklist

| Category               | Validation Criteria                         |
| :--------------------- | :------------------------------------------ |
| **Design Tokens**      | Icon sizes + colors map to theme tokens     |
| **ARIA Compliance**    | All icons labeled or hidden correctly       |
| **Dark Mode**          | All icons adapt via `--icon-color-*` tokens |
| **Naming Consistency** | Figma → Code → File paths match             |
| **Performance**        | SVGs optimized (no unnecessary metadata)    |
| **Export Quality**     | Crisp at all standard sizes (16–32 px)      |

---

<div align="center">

### ✨ Contributor Notes

When adding or updating icons:

* Name icons using lowercase, dash-separated format.
* Ensure stroke widths and grid alignment follow standards.
* Update `figma-refs.json` with new component IDs.
* Record version and token changes in `changelog.md`.
* Test color and focus states in **light and dark themes**.

**Icons are the language of the interface — clarity first, ornamentation second.**

</div>

