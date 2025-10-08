<div align="center">

# 🔤 Kansas Frontier Matrix — Typography System  
`docs/design/mockups/typography/`

**Readable · Hierarchical · Accessible · Reproducible**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../docs/design/)  
[![Figma Source](https://img.shields.io/badge/Figma-Typography%20System-purple)](./figma-refs.json)  
[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](../../../../docs/design/reviews/accessibility/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **Typography System** defines how text is styled, scaled, and rendered throughout the  
**Kansas Frontier Matrix (KFM)** interface — ensuring clarity, accessibility, and brand consistency.  
Typography is foundational to the KFM design system and is applied across both **web UI**  
(React + MapLibre) and **documentation** (Markdown · PDF · STAC metadata).

### Goals

- Maintain consistent visual **hierarchy** across map, timeline, and panel UIs.  
- Guarantee **WCAG 2.1 AA accessibility** for all text sizes and contrasts.  
- Support **dual environments**: screen (CSS/HTML) and print (PDF/STAC exports).  
- Encode **semantic intent** — headings, labels, annotations — as design tokens.  

---

## 🧩 Type Hierarchy Overview

```mermaid
graph TD
  A["Display · h1–h2\nTitles & Section Headers"] --> B["Body · p, span\nNarrative Text"]
  B --> C["Meta · caption, label\nSecondary Information"]
  C --> D["Mono · code, data\nTechnical & Structured Text"]

  style A fill:#E6EFFF,stroke:#0074D9,stroke-width:2px
  style B fill:#E3F2FD,stroke:#1976D2,stroke-width:1.5px
  style C fill:#FFFDE7,stroke:#FBC02D,stroke-width:1.5px
  style D fill:#E8F5E9,stroke:#2E7D32,stroke-width:1.5px

  %% END OF MERMAID
````

Typography in KFM follows a **four-tier hierarchy**:

1. **Display Type** — Large contextual titles for sections and views.
2. **Body Type** — Primary content, paragraphs, and popups.
3. **Meta Type** — Labels, captions, hints, or units.
4. **Monospace Type** — Code, coordinates, or data elements.

---

## 🗂️ Directory Structure

```text
docs/design/mockups/typography/
├── README.md                 # This documentation
├── figma-refs.json           # Figma node references and style hashes
├── type-scale.json            # JSON of font sizes, line heights, and weights
├── text-styles.css            # CSS classes and custom properties
├── wireframes/                # Typography visualizations (Figma exports)
│   ├── type-hierarchy.png
│   ├── text-samples-dark.png
│   └── text-samples-light.png
└── thumbnails/
    └── typography-thumb.png
```

---

## 🧠 Font Stack & Tokens

| Variable                   | Description                | Example Value                 |
| -------------------------- | -------------------------- | ----------------------------- |
| `--kfm-font-display`       | Display / heading font     | `"Inter", sans-serif`         |
| `--kfm-font-body`          | Body and UI text font      | `"Inter", sans-serif`         |
| `--kfm-font-mono`          | Code / metadata text font  | `"JetBrains Mono", monospace` |
| `--kfm-font-size-base`     | Default base font size     | `16px`                        |
| `--kfm-line-height-base`   | Line height for paragraphs | `1.6`                         |
| `--kfm-font-weight-normal` | Regular weight             | `400`                         |
| `--kfm-font-weight-bold`   | Bold / emphasis weight     | `600`                         |
| `--kfm-font-weight-heavy`  | Display / heading weight   | `700`                         |

All typography tokens are defined in `text-styles.css`
and compiled into `web/src/styles/tokens.css` for front-end use.

---

## 📏 Type Scale (Responsive)

| Level       | Usage                        | Size (rem) | Line Height | Weight |
| ----------- | ---------------------------- | :--------: | :---------: | :----: |
| **h1**      | Page titles / major headings |    2.25    |     1.2     |   700  |
| **h2**      | Section titles               |    1.75    |     1.3     |   600  |
| **h3**      | Subheadings                  |    1.50    |     1.4     |   600  |
| **h4**      | Minor headings               |    1.25    |     1.5     |   500  |
| **body-lg** | Large paragraph text         |    1.125   |     1.6     |   400  |
| **body-md** | Standard paragraph           |    1.00    |     1.6     |   400  |
| **body-sm** | Compact UI text              |    0.875   |     1.5     |   400  |
| **caption** | Footnotes, meta text         |    0.75    |     1.4     |   400  |
| **mono**    | Code / data labels           |    0.875   |     1.4     |   500  |

---

## 🧩 Example CSS Implementation

```css
:root {
  --kfm-font-display: "Inter", sans-serif;
  --kfm-font-body: "Inter", sans-serif;
  --kfm-font-mono: "JetBrains Mono", monospace;
  --kfm-font-size-base: 16px;
  --kfm-line-height-base: 1.6;
}

h1, .kfm-h1 {
  font-family: var(--kfm-font-display);
  font-size: 2.25rem;
  font-weight: 700;
  line-height: 1.2;
}

p, .kfm-body {
  font-family: var(--kfm-font-body);
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.6;
}

.kfm-caption {
  font-family: var(--kfm-font-body);
  font-size: 0.75rem;
  color: var(--kfm-muted);
}

code, .kfm-mono {
  font-family: var(--kfm-font-mono);
  background: var(--kfm-bg-muted);
  border-radius: 4px;
  padding: 0.1rem 0.25rem;
}
```

---

## ♿ Accessibility Guidelines

| Guideline              | Description                        | Implementation                                |
| ---------------------- | ---------------------------------- | --------------------------------------------- |
| **Contrast**           | Text/background ratio ≥ 4.5 : 1    | Verified via Stark + Axe tools                |
| **Scalability**        | Text resizes to 200 % without loss | Use relative units (rem/em)                   |
| **Focus States**       | Visible focus around text inputs   | Use `outline-offset` + `box-shadow`           |
| **Semantic Hierarchy** | Logical h1 → h6 structure          | Validated in accessibility audits             |
| **Localization**       | Unicode-safe fonts + diacritics    | Tested in EN / FR / ES / KS historical glyphs |

---

## 🧾 Provenance & Integrity

| Asset                      | Figma Node           | Export Date | SHA256         |
| -------------------------- | -------------------- | ----------- | -------------- |
| **type-hierarchy.png**     | `figma://node/60:12` | 2025-09-30  | `sha256-cf12…` |
| **text-samples-dark.png**  | `figma://node/60:15` | 2025-09-30  | `sha256-fb9a…` |
| **text-samples-light.png** | `figma://node/60:17` | 2025-09-30  | `sha256-3b41…` |

All exported typography assets and token files are verified via CI checksums under MCP reproducibility protocols.

---

## ⚙️ Continuous Integration (Typography Validation)

```yaml
# .github/workflows/typography_validate.yml
on:
  pull_request:
    paths:
      - "docs/design/mockups/typography/**"
jobs:
  typography:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate Markdown formatting
        run: npx markdownlint-cli2 "docs/design/mockups/typography/**/*.md"
      - name: Validate CSS tokens
        run: npx stylelint "docs/design/mockups/typography/**/*.css"
      - name: Verify asset checksums
        run: sha256sum -c checksums.txt
```

---

## 📚 Related Documents

* 🎨 [Design Tokens & Color Palette](../color-tokens/)
* 🧭 [Panels & Detail Views](../panels/)
* 🧩 [Navigation Components](../figma/components/navigation/)
* 🧱 [Web UI Architecture](../../../reviews/architecture/web_ui_architecture_review.md)
* 🗂 [Markdown “Standard Kit”](../../../../docs/standards/markdown-kit.md)

---

## 🪪 License & Credits

Typography System © 2025 **Kansas Frontier Matrix Design & Interaction Team**
Released under **Creative Commons CC-BY 4.0 International**
Maintained under **Master Coder Protocol (MCP)** — documentation-first, auditable, reproducible.

---

<div align="center">

### 🔤 Kansas Frontier Matrix — Typography System

**Readable · Accessible · Consistent · Reproducible**

</div>
