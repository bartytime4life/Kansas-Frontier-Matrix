<div align="center">

# ♿ Kansas Frontier Matrix — Input Accessibility Guide  
`docs/design/mockups/figma/components/inputs/accessibility.md`

**Mission:** Ensure every **input component** in the **Kansas Frontier Matrix (KFM)** design system  
is **accessible, perceivable, operable, understandable, and robust** in compliance with  
**WCAG 2.1 AA**, **ARIA 1.2**, and **Master Coder Protocol (MCP)** reproducibility standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Accessibility](https://img.shields.io/badge/Compliance-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-yellow)](../../../../../LICENSE)

</div>

---

## 🗂️ Directory Layout

```

inputs/
├── README.md
├── examples.md
├── tokens.json
├── figma-refs.json
├── accessibility.md   ← Accessibility reference (this file)
└── changelog.md

````

---

## 📘 Overview

This file defines **accessibility requirements and ARIA patterns**  
for all **input components** in the KFM design system.  

It serves as the baseline accessibility specification for both  
**Figma designers** and **React developers**, ensuring parity across  
prototypes, production, and assistive technologies.

The objective: **no user is excluded** — regardless of device, mode, or ability.  

---

## 🧭 Accessibility Philosophy

| Principle | Definition |
|:-----------|:------------|
| **Perceivable** | All information and components are visible, audible, and machine-readable. |
| **Operable** | Every interactive element is usable via keyboard, mouse, or touch. |
| **Understandable** | The purpose and status of each input is clear. |
| **Robust** | Inputs remain compatible with assistive technologies and evolving standards. |

> 🧱 *Accessibility is not a layer — it is a design foundation.*

---

## 🎨 General Input Rules

### Labels
- Every input **must have a visible label** or programmatic equivalent (`aria-labelledby`).
- Labels are **persistently visible** (never replaced by placeholders).
- Label–field association uses `for` attribute (`<label for="input-id">`).
- In Figma, label text should appear directly above or beside the field.

### Hints & Descriptions
- Use `aria-describedby` to associate hints or helper text with the field.
- Only **one ID** per field for hints; if multiple hints exist, combine them programmatically.

### Errors & Validation
- When a validation error occurs:
  - Add or swap `aria-describedby` to the error message ID.
  - Use `aria-invalid="true"` on the field.
  - Display error messages in red (`--color-danger`) with ≥ 4.5:1 contrast.

### Required Fields
- Use the `required` attribute in HTML and visually indicate with `*`.
- For screen readers, add `aria-required="true"` where necessary.

---

## 🎛 Keyboard Interaction

| Action | Behavior | Applies To |
|:--------|:-----------|:-----------|
| `Tab` | Moves to next focusable element | All inputs |
| `Shift + Tab` | Moves to previous element | All inputs |
| `Enter` | Submits or confirms input (varies by context) | Text, Search, Select |
| `Esc` | Cancels or clears input | Search, Combobox |
| `↑ / ↓` | Navigate list options | Select, Combobox, RadioGroup |
| `← / →` | Adjust value | Slider, RangeSlider |
| `Space` | Toggles binary state | Checkbox, Switch |
| `Home / End` | Jump to min/max value | Slider |
| `Alt + Down` | Opens dropdowns | Combobox / Select |
| `Shift` | Enables fine-grain adjustment | Slider |

> 🔑 **Focus ring** must always be visible (`--color-focus`, `--shadow-focus`).

---

## 🗣️ Screen Reader Patterns

### Standard Input (`<input type="text">`)
- Reads: **label**, field type (“edit text”), and **hint** (via `aria-describedby`).
- Announces “required” if applicable.
- Announces “invalid entry” if `aria-invalid="true"`.

### Password Field
- Reads: “Password, edit text.”
- Toggle visibility button must have `aria-label` describing action (“Show password” / “Hide password”).

### Search Field
- Announces “Search, edit text.”
- `role="searchbox"` is optional; browsers infer automatically for `<input type="search">`.

### TextArea
- Announces “Multiline edit.”
- Includes row/column information if provided.

### Select / Combobox
- Uses:
  - `role="combobox"`
  - `aria-expanded` = `true|false`
  - `aria-controls` → ID of dropdown list
  - `aria-activedescendant` → ID of highlighted option
- Options list uses:
  - `role="listbox"`
  - Each option uses `role="option"`

### Checkbox
- Uses:
  - `role="checkbox"`
  - `aria-checked` = `true|false|mixed`
- Labels explicitly reference input.

### RadioGroup
- Uses:
  - `role="radiogroup"`
  - Each radio has `role="radio"`
  - `aria-checked` = `true|false`
  - Keyboard navigation: `← / →` cycles options.

### Switch
- Uses:
  - `role="switch"`
  - `aria-checked` = `true|false`
  - Toggle via `Space`.

### Slider / RangeSlider
- Uses:
  - `role="slider"`
  - `aria-valuemin`, `aria-valuemax`, `aria-valuenow`
  - Updates values in real-time during keyboard input.

---

## 🎯 Focus Management

- The **focus indicator** must always be visible (`--shadow-focus` ring).
- Focus never moves automatically except:
  - When dropdowns open (`aria-expanded` = `true`), focus moves to listbox.
  - When closing menus, focus returns to originating field.
- Do **not** trap focus inside components (except modals).

> ⚡ Tip: Test focus order with `Tab` alone. It must always follow DOM order.

---

## 🧩 Accessible Color & Contrast

| Element | Minimum Contrast | Notes |
|:---------|:----------------:|:------|
| Text / Label | 4.5:1 | Required by WCAG AA |
| Icons | 3:1 | Relative to background |
| Focus Ring | 3:1 | Must remain visible |
| Error State | 4.5:1 | Red text vs background |
| Disabled Field | 3:1 | Must remain perceivable |

> ✅ Validate using [Contrast Checker](https://webaim.org/resources/contrastchecker/).

---

## 🌐 Localization & RTL Support

- **Bidirectional text:** Inputs must support `dir="rtl"` and `dir="ltr"`.  
- **Date inputs:** Localize format (e.g., `MM/DD/YYYY` → `DD.MM.YYYY`) via system locale.  
- **Screen reader language:** Set `lang` attribute at page root.  
- **Icons:** Automatically mirrored in RTL layouts.

---

## 🧱 Accessible Examples

### 1️⃣ Text Field Example
```html
<label for="name">Name</label>
<input id="name" type="text" aria-describedby="name-hint" required />
<span id="name-hint">Your full name as it appears in records.</span>
````

### 2️⃣ Checkbox Example

```html
<div role="group" aria-labelledby="consent-group">
  <span id="consent-group">Email Preferences</span>
  <label><input type="checkbox" aria-checked="true" /> Subscribe to newsletter</label>
</div>
```

### 3️⃣ Slider Example

```html
<label for="volume">Volume</label>
<input
  id="volume"
  type="range"
  min="0"
  max="100"
  value="60"
  aria-valuemin="0"
  aria-valuemax="100"
  aria-valuenow="60"
  aria-label="Volume level"
/>
```

---

## ✅ Testing Checklist

| Area                | Requirement                               | Tool / Method                 |
| :------------------ | :---------------------------------------- | :---------------------------- |
| **Keyboard**        | Fully navigable (Tab, Enter, Esc, Arrows) | Manual testing                |
| **Screen Reader**   | Reads labels, states, errors              | NVDA, VoiceOver               |
| **Contrast**        | Meets WCAG AA ratios                      | WebAIM, Figma contrast plugin |
| **Focus**           | Always visible and logical                | Tab navigation                |
| **ARIA Validation** | Attributes are valid, no conflicts        | axe DevTools, Lighthouse      |
| **RTL Support**     | All mirrored, labels remain aligned       | Browser locale simulation     |

---

<div align="center">

### ✨ Contributor Notes

When adding or editing input components:

* Include full **ARIA mapping** and **focus logic**.
* Verify color tokens meet contrast ratios.
* Test new variants with **keyboard + screen reader** before commit.
* Update this file and `changelog.md` with any accessibility change.

**Accessibility is not optional — it is KFM’s design baseline.**

</div>
