<div align="center">

# 🎨 Kansas Frontier Matrix — Figma Icon Component Examples  
`docs/design/mockups/figma/components/icons/examples.md`

**Mission:** Provide visual and coded examples for all **Figma icon components**  
in the **Kansas Frontier Matrix (KFM)** design system — ensuring consistent,  
accessible, and token-driven iconography between **Figma** and **React**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![Design System](https://img.shields.io/badge/Design-Figma%20Components-pink)](https://www.figma.com)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-yellow)](../../../../../LICENSE)

</div>

---

## 🗂️ Directory Layout

```

icons/
├── README.md
├── examples.md
├── tokens.json
├── figma-refs.json
├── accessibility.md
└── changelog.md

````

---

## 📘 Overview

This file demonstrates **how Figma icons map to React components**  
within the Kansas Frontier Matrix. Each example includes:
- 🖼️ Figma reference preview (for designers)  
- 💻 React/TypeScript example (for developers)  
- ♿ Accessibility and usage notes  
- 🎨 Token linkage (size, color, stroke)

Icons visually connect **map controls, datasets, story modes, and filters**,  
anchoring the user experience in consistent design language.

---

## 🔍 Icon Basics

Icons are vector-based and tokenized for consistency.  
Each can adapt to size, theme, or context through standardized properties.

| Property | Type | Description |
|:----------|:------|:-------------|
| `size` | string / number | Controls icon size (`sm`, `md`, `lg`, px value) |
| `color` | string | Inherits CSS token or explicit color value |
| `title` | string | Adds an accessible label or tooltip |
| `aria-hidden` | boolean | Hides decorative icons from assistive tech |

---

## ⚙️ Example 1 — Search Icon

### 🖼️ Figma Reference
![Search Icon](https://img.shields.io/badge/Figma-Search%20Icon-6B74FF?logo=figma&logoColor=white)

### 💻 React Example
```tsx
import { IconSearch } from "@/icons";

export function SearchButton() {
  return (
    <button className="kfm-btn-icon" aria-label="Search">
      <IconSearch size="20" color="var(--icon-color-default)" title="Search" />
    </button>
  );
}
````

### ♿ Accessibility

* `aria-label="Search"` ensures descriptive control naming.
* `title="Search"` offers tooltip and assistive label redundancy.
* Keyboard focus ring follows KFM focus token standards.

---

## 🧭 Example 2 — Map Pin Icon

### 🖼️ Figma Reference

![Pin Icon](https://img.shields.io/badge/Figma-Pin%20Icon-FF7F50?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
import { IconPin } from "@/icons";

export function MapMarker() {
  return (
    <div className="kfm-map-marker" role="img" aria-label="Pinned Location">
      <IconPin size="24" color="var(--icon-color-accent)" title="Pinned Location" />
    </div>
  );
}
```

### ♿ Accessibility

* Must include `role="img"` and accessible name.
* `color` variable adapts automatically between light and dark mode.

---

## 📅 Example 3 — Calendar Icon

### 🖼️ Figma Reference

![Calendar Icon](https://img.shields.io/badge/Figma-Calendar%20Icon-FEBE5D?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
import { IconCalendar } from "@/icons";

export function TimelineHeader() {
  return (
    <header className="kfm-timeline-header">
      <IconCalendar size="20" color="var(--icon-color-default)" title="Select Date Range" />
      <span>1854 — 1870</span>
    </header>
  );
}
```

### ♿ Accessibility

* Icon supports focusable keyboard outline when wrapped in interactive elements.
* Must never be the sole indicator of meaning — supplement with text.

---

## 🧮 Example 4 — Filter Icon

### 🖼️ Figma Reference

![Filter Icon](https://img.shields.io/badge/Figma-Filter%20Icon-00BFA6?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
import { IconFilter } from "@/icons";

export function FilterToggle({ active }: { active: boolean }) {
  return (
    <button
      className={`kfm-btn-icon ${active ? "is-active" : ""}`}
      aria-pressed={active}
      aria-label="Toggle Filters"
    >
      <IconFilter
        size="20"
        color={active ? "var(--icon-color-accent)" : "var(--icon-color-default)"}
        title="Toggle Filters"
      />
    </button>
  );
}
```

### ♿ Accessibility

| Behavior       | Description                          |
| :------------- | :----------------------------------- |
| `aria-pressed` | Communicates toggle state            |
| Keyboard       | `Enter` or `Space` toggles filter    |
| Color          | Accent color change reinforces state |

---

## 🗺️ Example 5 — Compass Icon (Directional)

### 🖼️ Figma Reference

![Compass Icon](https://img.shields.io/badge/Figma-Compass%20Icon-6895FF?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
import { IconCompass } from "@/icons";

export function MapOrientation() {
  return (
    <button
      className="kfm-btn-icon"
      aria-label="Reset map orientation"
      title="Reset map orientation"
    >
      <IconCompass size="24" color="var(--icon-color-default)" />
    </button>
  );
}
```

### ♿ Accessibility

* `aria-label` communicates purpose (“Reset map orientation”).
* Must include visible focus indicator on tab navigation.
* Avoid spinning animation unless explicitly user-triggered.

---

## 🧩 Example 6 — Layer Icon (Map Stack)

### 🖼️ Figma Reference

![Layer Icon](https://img.shields.io/badge/Figma-Layer%20Icon-FC79B3?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
import { IconLayers } from "@/icons";

export function LayerControl() {
  return (
    <div className="kfm-layer-control">
      <IconLayers size="20" color="var(--icon-color-default)" title="Layer Options" />
      <select aria-label="Select map layer" className="kfm-select">
        <option>Base</option>
        <option>Topographic</option>
        <option>Historic</option>
      </select>
    </div>
  );
}
```

### ♿ Accessibility

* `aria-label` on `<select>` clarifies function.
* Icon paired with text ensures meaning for all users.

---

## 🔊 Example 7 — Speaker / Audio Icon

### 🖼️ Figma Reference

![Speaker Icon](https://img.shields.io/badge/Figma-Speaker%20Icon-FF9F00?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
import { IconSpeaker } from "@/icons";

export function AudioNarrationToggle({ on, onToggle }: { on: boolean; onToggle: () => void }) {
  return (
    <button
      aria-pressed={on}
      onClick={onToggle}
      className={`kfm-btn-icon ${on ? "is-active" : ""}`}
      aria-label={on ? "Mute Narration" : "Play Narration"}
    >
      <IconSpeaker
        size="20"
        color={on ? "var(--icon-color-accent)" : "var(--icon-color-default)"}
        title={on ? "Mute Narration" : "Play Narration"}
      />
    </button>
  );
}
```

### ♿ Accessibility

* Uses `aria-pressed` to indicate toggle state.
* Text alternative matches action (Play vs Mute).
* Maintains consistent button width to prevent layout shift.

---

## 🧱 Example 8 — Settings Icon

### 🖼️ Figma Reference

![Settings Icon](https://img.shields.io/badge/Figma-Settings%20Icon-FFD166?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
import { IconSettings } from "@/icons";

export function SettingsMenu() {
  return (
    <button className="kfm-btn-icon" aria-haspopup="menu" aria-label="Open Settings">
      <IconSettings size="20" color="var(--icon-color-default)" title="Open Settings" />
    </button>
  );
}
```

### ♿ Accessibility

| Behavior               | Description                             |
| :--------------------- | :-------------------------------------- |
| `aria-haspopup="menu"` | Indicates button opens a settings menu  |
| Focus                  | Visual outline must meet contrast ratio |
| Tooltip                | Optional via `title` prop               |

---

## 🧪 QA Checklist

| Category          | Requirement                                           |
| :---------------- | :---------------------------------------------------- |
| **Accessibility** | Icons labeled or hidden (`aria-hidden`) appropriately |
| **Design Tokens** | Icon colors and sizes match theme tokens              |
| **Dark Mode**     | Colors switch dynamically (`--icon-color-accent`)     |
| **Performance**   | SVGs optimized and cached                             |
| **Consistency**   | Figma name ↔ React name parity verified               |
| **Scalability**   | Icons crisp at all supported resolutions              |

---

<div align="center">

### ✨ Contributor Notes

When creating new icon examples:

* Add **Figma badge** and visual reference.
* Provide **React + TypeScript implementation**.
* List **ARIA labels** and **interaction states**.
* Reference applicable **tokens** in `tokens.json`.
* Record updates in `changelog.md`.

**Icons are the universal language of KFM — clarity above all.**

</div>

