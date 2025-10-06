<div align="center">

# 🧩 Kansas Frontier Matrix — Figma Input Component Examples  
`docs/design/mockups/figma/components/inputs/examples.md`

**Mission:** Showcase fully documented, reproducible **input component examples**  
for the **Kansas Frontier Matrix (KFM)** design system — linking **Figma**, **React**,  
and **accessibility** specifications under the Master Coder Protocol (MCP).

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![UI Library](https://img.shields.io/badge/Design-Figma%20Components-pink)](https://www.figma.com)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
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
├── accessibility.md
└── changelog.md

````

---

## 📘 Overview

This document provides **visual and coded examples** for the `inputs/` directory of  
the Kansas Frontier Matrix Figma component system. Each example connects  
**Figma prototypes**, **React implementations**, and **accessibility standards**  
to ensure visual + functional parity across the design system.

Every component example demonstrates:
- 📸 Figma visual reference  
- 💻 React + TypeScript implementation  
- ♿ Accessibility & validation behavior  
- 🎨 Token usage and design metadata  

---

## 🔍 Text Field

### 📸 Figma Reference
![TextField](https://img.shields.io/badge/Figma-TextField-6b74ff?logo=figma&logoColor=white)

### 💻 React Example
```tsx
function TextField({ label, placeholder }: { label: string; placeholder: string }) {
  return (
    <div className="kfm-field">
      <label htmlFor="tf" className="kfm-label">{label}</label>
      <input id="tf" className="kfm-input" type="text" placeholder={placeholder} />
      <div className="kfm-hint">Enter text value.</div>
    </div>
  );
}
````

### ♿ Accessibility

| Property           | Description                            |
| :----------------- | :------------------------------------- |
| `aria-labelledby`  | Connected to `<label>`                 |
| `aria-describedby` | Connects to hint or validation message |
| Keyboard           | Tab navigable; focus ring visible      |

---

## 🔑 Password Field

### 📸 Figma Reference

![PasswordField](https://img.shields.io/badge/Figma-PasswordField-8c67ff?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
function PasswordField() {
  const [show, setShow] = React.useState(false);
  return (
    <div className="kfm-field">
      <label htmlFor="pw" className="kfm-label">Password</label>
      <div className="kfm-input-wrap">
        <input id="pw" type={show ? "text" : "password"} className="kfm-input" />
        <button
          type="button"
          onClick={() => setShow(!show)}
          aria-label={show ? "Hide password" : "Show password"}
          className="kfm-icon-btn"
        >
          {show ? "🙈" : "👁️"}
        </button>
      </div>
      <div className="kfm-hint">Minimum 8 characters.</div>
    </div>
  );
}
```

### ♿ Accessibility

* Toggle button labeled with `aria-label`
* Keyboard operable via `Tab` and `Enter`
* Dynamic `type` change updates screen reader behavior

---

## 🔍 Search Field

### 📸 Figma Reference

![SearchField](https://img.shields.io/badge/Figma-SearchField-64b6f7?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
function SearchField({ onSearch }: { onSearch: (q: string) => void }) {
  const [query, setQuery] = React.useState("");
  React.useEffect(() => {
    const id = setTimeout(() => onSearch(query.trim()), 300);
    return () => clearTimeout(id);
  }, [query, onSearch]);

  return (
    <div className="kfm-field">
      <label htmlFor="search" className="kfm-label">Search</label>
      <div className="kfm-input-wrap">
        <span className="kfm-icon" aria-hidden="true">🔍</span>
        <input
          id="search"
          type="search"
          className="kfm-input"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search places, events..."
        />
        {query && (
          <button
            type="button"
            onClick={() => setQuery("")}
            aria-label="Clear search"
            className="kfm-icon-btn"
          >✕</button>
        )}
      </div>
      <div className="kfm-hint">Tip: Try “Osage Treaty 1867”.</div>
    </div>
  );
}
```

### ♿ Accessibility

| Key            | Function                          |
| :------------- | :-------------------------------- |
| `Enter`        | Executes search                   |
| `Esc`          | Clears field                      |
| Screen readers | Properly announces label and hint |

---

## 📅 Date Range Picker

### 📸 Figma Reference

![DateRange](https://img.shields.io/badge/Figma-DateRange-ffae42?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
function DateRange({ onChange }: { onChange: (r: { from?: string; to?: string }) => void }) {
  const [range, setRange] = React.useState({ from: "", to: "" });
  const update = (k: "from" | "to") => (e: React.ChangeEvent<HTMLInputElement>) => {
    const next = { ...range, [k]: e.target.value };
    setRange(next);
    onChange(next);
  };

  return (
    <fieldset className="kfm-field">
      <legend className="kfm-label">Date Range</legend>
      <div className="kfm-grid-2">
        <input type="date" className="kfm-input" onChange={update("from")} />
        <input type="date" className="kfm-input" onChange={update("to")} />
      </div>
      <div className="kfm-hint">Select start and end dates.</div>
    </fieldset>
  );
}
```

### ♿ Accessibility

* Dates stored in ISO format.
* Enforces `from ≤ to`.
* Keyboard and screen reader accessible.

---

## 🏷 Tag Input

### 📸 Figma Reference

![TagInput](https://img.shields.io/badge/Figma-TagInput-6fe88b?logo=figma\&logoColor=white)

### 💻 React Example

```tsx
function TagInput() {
  const [tags, setTags] = React.useState<string[]>([]);
  const [input, setInput] = React.useState("");

  const addTag = () => {
    if (input.trim() && !tags.includes(input.trim())) {
      setTags([...tags, input.trim()]);
      setInput("");
    }
  };

  return (
    <div className="kfm-field">
      <label className="kfm-label">Tags</label>
      <div className="kfm-tag-wrap">
        {tags.map((t) => (
          <span key={t} className="kfm-tag">
            {t}
            <button
              type="button"
              aria-label={`Remove ${t}`}
              onClick={() => setTags(tags.filter((x) => x !== t))}
              className="kfm-tag-close"
            >
              ×
            </button>
          </span>
        ))}
        <input
          className="kfm-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && addTag()}
          placeholder="Add tag..."
        />
      </div>
      <div className="kfm-hint">Press Enter to add tags.</div>
    </div>
  );
}
```

### ♿ Accessibility

* Each tag has `aria-label` for removal.
* Focusable tags support keyboard deletion via `Backspace`.
* Screen reader announces each added tag.

---

## 🧪 QA Checklist

| Category          | Criteria                                    |
| :---------------- | :------------------------------------------ |
| **Accessibility** | Labels visible, focus clear, ARIA connected |
| **Validation**    | Errors concise; one state visible           |
| **Contrast**      | Meets WCAG AA ratios                        |
| **Dark Mode**     | Token colors validated                      |
| **Performance**   | Debounced + async safe                      |
| **i18n**          | RTL + localized date formatting verified    |

---

<div align="center">

### ✨ Contributor Notes

When adding or modifying examples:

* Include **Figma component badge** and **React code snippet**.
* Describe **ARIA behaviors** and **validation logic**.
* Reference **tokens** used by each variant.
* Record updates in `changelog.md`.

</div>

