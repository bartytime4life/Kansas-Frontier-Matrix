<div align="center">

# 🧩 Kansas Frontier Matrix — Figma Input Components  
`docs/design/mockups/figma/components/inputs/`

**Mission:** Establish canonical, accessible, and reproducible **input components**  
for the **Kansas Frontier Matrix (KFM)** design system — ensuring perfect **UI parity**  
between **Figma prototypes** and **React implementation**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-yellow)](../../../../../LICENSE)

</div>

---

## 🗂️ Directory Layout

```

docs/design/mockups/figma/components/inputs/
├── README.md              → Design & implementation standards (this file)
├── examples.md            → Visual + React examples of each input type
├── tokens.json            → Input design tokens (colors, spacing, focus rings)
├── figma-refs.json        → Figma component IDs & metadata
├── accessibility.md       → WCAG + ARIA documentation
└── changelog.md           → Version & design update history

````

> 🧭 *This folder defines all **input-related UI elements** for the KFM design system —  
> bridging design (Figma) and development (React) with unified, versioned documentation.*

---

## 📘 Overview

This documentation specifies how **input components** (text fields, selects, sliders, etc.)  
are designed, built, and maintained in the Kansas Frontier Matrix system.  

Inputs appear in:
- **Search & filter panels** (timeline/map)  
- **Form dialogs** and **dataset editors**  
- **Configuration tools** in admin views  

All follow **Master Coder Protocol (MCP)** standards for:
- Documentation-first reproducibility  
- Accessibility-first UI (WCAG AA)  
- Token-driven design  
- Cross-platform parity  

---

## 🧭 Core Principles

- **Clarity first** — Labels are visible and persistent.  
- **Predictable states** — Each state (hover/focus/error) is visually distinct.  
- **Accessibility by default** — Every control meets or exceeds WCAG 2.1 AA.  
- **Composable** — Works seamlessly in different layouts (map sidebar, modal, form).  
- **Temporal + spatial awareness** — Inputs integrate with map/timeline filters.  

---

## 🎨 Design Tokens

| Token | Purpose | Example Use |
|:------|:---------|:-------------|
| `--color-fg` / `--color-border` | Foreground & borders | Field text / outline |
| `--color-bg` / `--color-surface` | Background layers | Field base & hover |
| `--color-focus` / `--shadow-focus` | Focus indication | Accessible outlines |
| `--radius-sm`, `--radius-md` | Corner rounding | Field, menu corners |
| `--space-1..4` | Spacing scale | Padding & gaps |
| `--font-sans`, `--font-size-sm..md` | Typography | Labels, input text |

> 🎨 Tokens are defined globally in `web/src/styles/tokens.css` and synchronized in Figma variables.  
> **Dark mode** variants are automatically applied via token aliases.

---

## ⚙️ Input Anatomy

Every input component follows this structure:

1. **Label** — visible, linked via `for` or `aria-labelledby`.  
2. **Field** — editable or interactive element.  
3. **Affordance** — optional icon, clear button, or spinner.  
4. **Helper / Status text** — hint, warning, or error message.  

```mermaid
flowchart TD
  A[Label] --> B[Field]
  B --> C{Affordance?}
  C -->|Yes| D[Icon / Clear / Spinner]
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
| **Width**   | `inline`, `fill`, `auto`                                                         |

> Compact density reduces padding by ~20% for map filter trays or dense UIs.

---

## 🧱 Figma Components

**Path:** `Figma → Components / Inputs`

| Component                          | Description               |
| :--------------------------------- | :------------------------ |
| `TextField`, `TextArea`            | Base text inputs          |
| `PasswordField`                    | Secure entry w/ toggle    |
| `SearchField`                      | Search w/ loupe & clear   |
| `NumberField`                      | Numeric + stepper         |
| `Select`, `Combobox`               | Dropdowns + autocomplete  |
| `DatePicker`, `DateRange`          | Temporal filters          |
| `Checkbox`, `Switch`, `RadioGroup` | Boolean + grouped inputs  |
| `Slider`, `RangeSlider`            | Continuous range controls |
| `FileDrop`                         | File uploads (drag/drop)  |
| `TagInput`                         | Tokenized multi-select    |

All Figma variants use auto-layout vertical stacking:
**Label → Field → Helper Text** (`gap: var(--space-1)`).

---

## 🧩 Usage Guidelines

| Type                   | Best Used For                            |
| :--------------------- | :--------------------------------------- |
| **TextField**          | Short text (e.g. search or label inputs) |
| **TextArea**           | Long notes, comments, or narratives      |
| **Select**             | Static, short lists                      |
| **Combobox**           | Searchable or async large lists          |
| **NumberField**        | Years, coordinates, numeric filters      |
| **DatePicker / Range** | Timeline or range filtering              |
| **TagInput**           | Multi-facet tagging (“Treaty”, “Flood”)  |

---

## ♿ Accessibility

* Every field has a **visible label** or `aria-labelledby`.
* Hints/errors linked by `aria-describedby`.
* **Keyboard Support**

  * Text: standard editing; `Esc` clears (if clear icon shown).
  * Combobox: `↑/↓` navigate, `Enter` select, `Esc` close.
  * Checkbox/Switch: `Space` toggles.
  * Slider: `←/→` adjust, `Shift+←/→` fine-tune, `Home/End` extremes.
* **Focus Ring** uses `--color-focus` + `--shadow-focus`, ≥3:1 contrast ratio.

---

## ✅ Validation Rules

* Validate on **blur** and **submit**; real-time for lightweight rules only.
* Error messages are short, specific, and override hints.
* Only one visible status at a time.
* Date and number rules:

  * Year: range `1541–present` (Kansas data coverage).
  * Ranges: enforce `start ≤ end`; hint “Leave blank for open-ended.”

---

## 🌐 Internationalization

* Fully supports **RTL** layout using logical CSS properties.
* Dates stored as ISO 8601; localized at render time.
* Strings tokenized for translation.
* Wrap labels; never truncate important text.

---

## ⚡ Performance

* Debounce interactive inputs (250–300 ms).
* Cancel async requests when input changes.
* Virtualize long lists (Combobox, Select).
* Avoid forced reflows on resize or focus changes.

---

## 💻 React Code Examples

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
      <input id="q" type="search" value={q} onChange={(e) => setQ(e.target.value)}
             className="kfm-input" aria-describedby="q-hint" />
      <div id="q-hint" className="kfm-hint">Try “flood 1951” or “Osage treaty”.</div>
    </div>
  );
}
```

### 📅 Year Range Input

```tsx
function YearRange({ onChange }: { onChange: (r: {from?: number, to?: number}) => void }) {
  const [years, set] = React.useState({ from: "", to: "" });
  const update = (k: "from" | "to") => (e: React.ChangeEvent<HTMLInputElement>) =>
    set({ ...years, [k]: e.target.value });
  React.useEffect(() => {
    const { from, to } = years;
    if (!to || Number(from) <= Number(to))
      onChange({ from: +from || undefined, to: +to || undefined });
  }, [years]);
  return (
    <fieldset className="kfm-field">
      <legend className="kfm-label">Year Range</legend>
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

| Category          | Criteria                                         |
| :---------------- | :----------------------------------------------- |
| **Accessibility** | Label visible, ARIA connected, keyboard operable |
| **Contrast**      | ≥4.5:1 text; ≥3:1 focus ring                     |
| **Validation**    | Error clarity + consistency                      |
| **Dark Mode**     | Tokens render properly                           |
| **Performance**   | Inputs debounced; async cancelled                |
| **i18n**          | RTL verified, localized strings work             |

---

<div align="center">

### ✨ Contributor Notes

When updating or creating a new input:

* Document variants and token usage in **`README.md`**.
* Add working samples to **`examples.md`**.
* Update **`figma-refs.json`** when Figma components change.
* Record all version changes in **`changelog.md`**.

</div>
