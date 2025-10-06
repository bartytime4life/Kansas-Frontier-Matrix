<div align="center">

# ♿ Kansas Frontier Matrix — Icon Accessibility Guide  
`docs/design/mockups/figma/components/icons/accessibility.md`

**Mission:** Guarantee all **icons** within the **Kansas Frontier Matrix (KFM)**  
meet or exceed **WCAG 2.1 AA** and **ARIA 1.2** accessibility standards — ensuring  
that visual and interactive icons are perceivable, operable, and understandable  
to every user, across Figma design, React implementation, and assistive technologies.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Accessibility](https://img.shields.io/badge/Compliance-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
[![Design System](https://img.shields.io/badge/Design-Figma%20Components-pink)](https://www.figma.com)
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
├── accessibility.md   ← Accessibility reference (this file)
└── changelog.md

````

---

## 📘 Overview

Icons are visual indicators of **actions, states, or concepts** in the KFM interface.  
They must be accessible to users of **screen readers, keyboard navigation,  
and high-contrast or non-visual environments**.

This document specifies how to implement, label, and test accessible icons  
across Figma and React, ensuring parity between design intent and live behavior.

---

## 🧭 Accessibility Principles

| Principle | Definition |
|:-----------|:------------|
| **Meaningful** | Every icon must communicate its purpose via text alternative. |
| **Visible** | Icons must maintain color contrast and visible focus when interactive. |
| **Operable** | Interactive icons must be usable with keyboard and screen reader. |
| **Consistent** | Same icon = same meaning, across UI contexts. |
| **Fallback-ready** | Icons convey meaning even if images or styles fail. |

> 🧱 *Icons are not decoration — they are information.*

---

## 🎨 Visual Design Requirements

| Element | Requirement |
|:----------|:--------------|
| **Contrast** | Icons must have ≥ 3:1 contrast ratio with background. |
| **Focus State** | Focus rings (`--shadow-focus`) must be visible and meet ≥ 3:1 ratio. |
| **Disabled Icons** | Appear muted but maintain ≥ 3:1 contrast. |
| **Color Tokens** | Use tokenized color variables (no hardcoded hex values). |
| **Scaling** | Icons must render crisply at all sizes (16–32 px). |

> 🎨 Figma and code both use the same token set defined in `icons/tokens.json`.

---

## 🧱 ARIA Patterns

### 1️⃣ Non-Decorative Icons (Informational or Interactive)
Used for icons that convey meaning or function.

```html
<svg role="img" aria-label="Filter data">
  <title>Filter data</title>
  <use href="#icon-filter" />
</svg>
````

| Attribute    | Purpose                               |
| :----------- | :------------------------------------ |
| `role="img"` | Identifies SVG as meaningful content  |
| `aria-label` | Describes function for assistive tech |
| `<title>`    | Provides human-readable label         |

---

### 2️⃣ Decorative Icons (Purely Visual)

Used when icons have no semantic meaning — they are visual embellishments only.

```html
<svg aria-hidden="true" focusable="false">
  <use href="#icon-chevron-right" />
</svg>
```

| Attribute            | Purpose                          |
| :------------------- | :------------------------------- |
| `aria-hidden="true"` | Excludes from accessibility tree |
| `focusable="false"`  | Removes icon from tab order      |

> ⚠️ *Never assign both `aria-label` and `aria-hidden` — choose one.*

---

### 3️⃣ Button or Link Icons

Icons that trigger actions must be enclosed in an interactive element.

```html
<button aria-label="Open Settings">
  <svg role="img" aria-hidden="false">
    <title>Open Settings</title>
    <use href="#icon-settings" />
  </svg>
</button>
```

**Rules:**

* Do **not** attach `onClick` to `<svg>` directly.
* Use `<button>` or `<a>` for semantics and keyboard accessibility.
* Maintain visible focus ring around parent container.

---

### 4️⃣ Icon-only Buttons (Common in KFM)

When the icon itself is the only visible element (e.g., close, filter, search).

| ARIA Property  | Requirement                              |
| :------------- | :--------------------------------------- |
| `aria-label`   | Must describe the button’s action        |
| `aria-pressed` | Use on toggle icons (true/false)         |
| `title`        | Optional, adds tooltip for sighted users |
| `tabindex="0"` | Ensures keyboard accessibility           |

Example:

```html
<button aria-label="Clear search" class="kfm-icon-btn">
  <svg role="img" aria-hidden="false">
    <title>Clear search</title>
    <use href="#icon-x" />
  </svg>
</button>
```

---

## 🧭 Keyboard Behavior

| Key               | Expected Action                   | Applies To             |
| :---------------- | :-------------------------------- | :--------------------- |
| `Tab`             | Moves focus between icons/buttons | All interactive icons  |
| `Enter` / `Space` | Activates action                  | IconButton, ToggleIcon |
| `Esc`             | Cancels or closes contextual menu | IconButton (menus)     |
| `Shift + Tab`     | Reverses navigation order         | All interactive icons  |

> 🧩 **No icon should trap focus** or require a mouse to activate.

---

## 🗣️ Screen Reader Announcements

| Icon Type     | Screen Reader Output                          |
| :------------ | :-------------------------------------------- |
| Informational | "Icon: [Label]"                               |
| Button Icon   | "Button: [Action]"                            |
| Toggle Icon   | "Toggle Button: [State]" (e.g., “on” / “off”) |
| Decorative    | *Not announced*                               |
| Linked Icon   | "Link: [Destination]"                         |

> 🔎 *Use meaningful verbs in ARIA labels:*
>
> * `Open map layers` (✅)
> * `Layers` (❌)

---

## 🌐 Localization & RTL

* All ARIA labels and `<title>` content must support translation.
* Do not hardcode direction-sensitive icons — use **mirrored variants** for RTL:

  * `arrow-left` ↔ `arrow-right`
  * `chevron-left` ↔ `chevron-right`
* Figma exports both directions as component variants.
* In React, direction is handled via CSS logical properties (`dir="rtl"`).

Example:

```tsx
<IconArrow direction={document.dir === "rtl" ? "right" : "left"} />
```

---

## 🔍 Testing Guidelines

| Area                    | Requirement                                 | Method                    |
| :---------------------- | :------------------------------------------ | :------------------------ |
| **Keyboard Navigation** | Icons reachable & operable with Tab / Enter | Manual test               |
| **Screen Reader**       | ARIA roles & labels announced correctly     | NVDA, VoiceOver           |
| **Contrast**            | ≥ 3:1 ratio verified                        | WebAIM Contrast Checker   |
| **Focus**               | Visible focus outline                       | Browser + tab test        |
| **ARIA Validation**     | No redundant/conflicting attributes         | axe DevTools              |
| **RTL**                 | Icons mirror correctly                      | Browser locale simulation |

---

## 🧪 QA Checklist

|  ✅  | Requirement                                          |
| :-: | :--------------------------------------------------- |
|  ☐  | Icons use standardized roles and labels              |
|  ☐  | Interactive icons are wrapped in `<button>` or `<a>` |
|  ☐  | Decorative icons are hidden from assistive tech      |
|  ☐  | Icons maintain color contrast and visible focus      |
|  ☐  | Tested with NVDA, VoiceOver, and keyboard-only input |
|  ☐  | RTL mirroring verified for directional icons         |
|  ☐  | ARIA attributes validated (no conflicts)             |

---

<div align="center">

### ✨ Contributor Notes

When adding or updating icons:

* Include appropriate `role` (`img`, `button`, `switch`, etc.).
* Define `aria-label` or `aria-hidden` clearly — **never omit both.**
* Validate focus and contrast manually before commit.
* Update this file and `changelog.md` for any accessibility-affecting change.

**Icons are communication. Accessibility ensures they speak to everyone.**

</div>
