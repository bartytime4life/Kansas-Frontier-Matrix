<div align="center">

# 🧩 Kansas Frontier Matrix — Figma Input Components  
`docs/design/mockups/figma/components/inputs/README.md`

**Mission:** Define **canonical, accessible, and reproducible input components** for the  
**Kansas Frontier Matrix (KFM)** design system — ensuring **visual consistency**, **semantic accuracy**,  
and **UI–code parity** between **Figma prototypes** and **React implementation**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-yellow)](../../../../../LICENSE)

</div>

---

## 📘 Overview

This document provides **Figma + React design specifications** for all **input controls**  
used across the **Kansas Frontier Matrix** platform — including forms, filters, dialogs, and  
map/timeline query components. All elements follow **MCP (Master Coder Protocol)**  
standards for documentation-first reproducibility, semantic markup, and accessibility compliance.

---

## 🧭 Principles

- **Clarity first** — Labels are always visible; placeholders never replace labels.  
- **Predictable states** — Hover ≠ Focus; Error ≠ Warning.  
- **Accessible by default** — WCAG AA contrast, ARIA labels, keyboard support.  
- **Composable** — Inputs integrate into filters, dialogs, or story UIs seamlessly.  
- **Temporal & spatial awareness** — Optimized for time and geography filters (timeline/map).  

---

## 🎨 Design Tokens

| Token | Purpose | Examples |
|:------|:---------|:----------|
| `--color-fg`, `--color-danger`, `--color-focus` | Text / status colors | Label, error, focus ring |
| `--color-bg`, `--color-surface`, `--color-border` | Field + border layers | Input base & hover |
| `--radius-sm`, `--radius-md` | Corner radius | Field, dropdowns |
| `--space-1..4` | Vertical/horizontal spacing | Padding, gaps |
| `--font-sans`, `--font-size-sm..md` | Typography | Label, input text |
| `--shadow-focus` | Accessible ring | Focus/active outline |

> 🔁 **Dark Mode:** Tokens auto-swap via CSS custom properties.

---

## ⚙️ Anatomy

Each input contains:  
**Label → Field → Affordances (icons, clear buttons) → Hint/Error text**

```mermaid
flowchart LR
  A[Label] --> B[Field]
  B --> C{Affordance?}
  C -->|Yes| D[Icon/Clear/Spinner]
  B --> E[Hint or Error Text]
````

<!-- END OF MERMAID -->

---

## 🎛 States & Variants

| Category    | Options                                                                          |
| :---------- | :------------------------------------------------------------------------------- |
| **State**   | `rest`, `hover`, `focus`, `filled`, `disabled`, `readonly`, `invalid`, `success` |
| **Size**    | `sm`, `md`                                                                       |
| **Density** | `default`, `compact`                                                             |
| **Width**   | `inline`, `fill`, `max-chars`                                                    |

> Compact density reduces vertical padding by 20% for map filters or data trays.

---

## 🧱 Figma Library Components

Located in **`Figma → Components / Inputs`**

**Component Types**

* `TextField` / `TextArea`
* `PasswordField` (visibility toggle)
* `NumberField`
* `SearchField` (clearable)
* `Select` / `Combobox`
* `DatePicker` / `DateRange`
* `Checkbox` / `Switch` / `RadioGroup`
* `Slider` / `RangeSlider`
* `FileDrop` (drag-and-drop)
* `TagInput` (tokenized)

**Component Properties**

| Property                       | Options                                   |
| :----------------------------- | :---------------------------------------- |
| `State`                        | Rest / Hover / Focus / Invalid / Disabled |
| `Size`                         | sm / md                                   |
| `Label`                        | Shown / Hidden                            |
| `HelperText`                   | On / Off                                  |
| `LeadingIcon` / `TrailingIcon` | On / Off                                  |
| `Density`                      | Default / Compact                         |

Auto layout: vertical flow (label → field → helper/status) with `gap: var(--space-1)`.

---

## 🧩 Usage Guidelines

| Type                    | Use Case                                             |
| :---------------------- | :--------------------------------------------------- |
| **Text vs. TextArea**   | Short entry vs. narrative or comments                |
| **Select vs. Combobox** | Small finite list vs. searchable large dataset       |
| **Number**              | For years, coordinates, numeric filters              |
| **Date/Range**          | Timeline filters (ISO format; UTC alignment)         |
| **Search**              | Debounced (250–300 ms), returns contextual results   |
| **TagInput**            | Multi-tag filters (e.g., “Treaty”, “Flood”, “1860s”) |

---

## ♿ Accessibility

* All inputs require a **visible label** or **`aria-labelledby`**.
* Hints and errors use **`aria-describedby`**.
* Keyboard behaviors:

  * **Text fields**: Typing, `Esc` clears.
  * **Selects/Comboboxes**: `↑`/`↓` navigate, `Enter` select, `Esc` close.
  * **Checkbox/Switch**: `Space` toggles.
  * **Slider**: `←/→` adjust, `Shift+←/→` fine step, `Home/End` extremes.
* Focus rings use `--color-focus` + `--shadow-focus` (visible at 3:1 contrast).

---

## ✅ Validation Rules

* Validate on **blur** or **submit**; real-time validation for light constraints only.
* Errors replace hints and are concise and actionable.
* Numeric/date validation:

  * Year: range `1541–present` (Kansas dataset coverage).
  * Ranges: enforce `start ≤ end`; provide hint “Leave blank for open-ended.”

---

## 🌐 Internationalization

* RTL supported via logical CSS properties.
* ISO 8601 for storage, localized display for UI.
* Avoid hardcoded units; tokenized strings only.
* Wrap long labels, prefer text wrapping over truncation.

---

## ⚡ Performance

* All searches debounced (250–300 ms).
* Async requests cancel on new input.
* Virtualize long option lists in comboboxes.
* Avoid blocking main thread on filter changes.

---

## 💻 React Code Examples

> Implementation examples (TypeScript + React + Tailwind)

### 🔍 Search Field

```tsx
function SearchField({ onSearch }: { onSearch: (q: string) => void }) {
  const [q, setQ] = React.useState("");
  React.useEffect(() => {
    const id = setTimeout(() => onSearch(q.trim()), 300);
    return () => clearTimeout(id);
  }, [q, onSearch]);
  return (
    <div className="kfm-field">
      <label htmlFor="q" className="kfm-label">Search places, events, years</label>
      <input id="q" className="kfm-input" type="search" value={q}
             onChange={(e) => setQ(e.target.value)} aria-describedby="q-hint" />
      <div id="q-hint" className="kfm-hint">Try “flood 1951” or “Osage treaty”.</div>
    </div>
  );
}
```

### 📅 Year Range Filter

```tsx
function YearRange({ onChange }: { onChange: (r: {from?: number, to?: number}) => void }) {
  const [years, setYears] = React.useState({ from: "", to: "" });
  const update = (k: "from" | "to") => (e: React.ChangeEvent<HTMLInputElement>) =>
    setYears({ ...years, [k]: e.target.value });
  React.useEffect(() => {
    const { from, to } = years;
    if (Number(from) <= Number(to) || !to) onChange({ from: +from || undefined, to: +to || undefined });
  }, [years]);
  return (
    <fieldset className="kfm-field">
      <legend className="kfm-label">Year range</legend>
      <div className="kfm-grid-2">
        <input placeholder="From" onChange={update("from")} className="kfm-input" />
        <input placeholder="To" onChange={update("to")} className="kfm-input" />
      </div>
      <div className="kfm-hint">Range: 1541–present.</div>
    </fieldset>
  );
}
```

---

## 🧪 QA Checklist

| Category            | Criteria                                         |
| :------------------ | :----------------------------------------------- |
| **Accessibility**   | Labels, focus, keyboard, ARIA roles all verified |
| **Visual Contrast** | ≥ 4.5:1 text; ≥ 3:1 focus outline                |
| **Validation**      | Clear copy; errors override hints                |
| **Dark Mode**       | Tokens render correctly                          |
| **Performance**     | Debounced + virtualized                          |
| **i18n**            | RTL verified; localized date formatting          |

---

<div align="center">
