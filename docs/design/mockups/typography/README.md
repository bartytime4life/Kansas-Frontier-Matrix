<div align="center">

# 🔤 Kansas Frontier Matrix — Typography System  
`docs/design/mockups/typography/`

**Readable · Hierarchical · Consistent Across UI**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Typography%20System-purple)](./figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **Typography System** defines how text is styled, scaled, and rendered throughout the Kansas Frontier Matrix (KFM) interface — ensuring clarity, accessibility, and brand consistency across all devices.  
Typography is a foundational layer of the design system, used in both the **web UI (React + MapLibre)** and **documentation (Markdown, PDF)** contexts.

The goals of this system are to:
- Maintain **consistent hierarchy** between map, timeline, and panel UIs  
- Guarantee **accessibility compliance (WCAG 2.1 AA)** for all text sizes and contrasts  
- Support **dual environments**: screen (HTML/CSS) and print (PDF/STAC metadata exports)  
- Encode **semantic intent** — headings, labels, annotations — as reusable design tokens  

---

## 🧩 Type Hierarchy Overview

```mermaid
graph TD
  A["Display · h1-h2\nTitles & Section Headers"] --> B["Body · p, span\nNarrative Text"]
  B --> C["Meta · caption, label\nSecondary Data"]
  C --> D["Mono · code, data\nTechnical Text"]

<!-- END OF MERMAID -->


Typography across KFM follows a four-tier hierarchy:
	1.	Display Type — Large contextual titles for sections and views
	2.	Body Type — Primary content, paragraphs, and popups
	3.	Meta Type — Labels, captions, and hints
	4.	Monospace Type — Code, coordinates, or structured data

⸻

📁 Directory Structure

docs/design/mockups/typography/
├── README.md                # This documentation
├── figma-refs.json          # Figma node references and style hashes
├── type-scale.json          # JSON of font sizes, line heights, and weights
├── text-styles.css          # CSS classes and custom properties
├── wireframes/              # Typography visualizations (Figma exports)
│   ├── type-hierarchy.png
│   ├── text-samples-dark.png
│   └── text-samples-light.png
└── thumbnails/              # Compressed previews for README display
    └── typography-thumb.png


⸻

🧠 Font Stack & Tokens

Variable	Description	Example Value
--kfm-font-display	Main heading font	"Inter", sans-serif
--kfm-font-body	Paragraph and UI text	"Inter", sans-serif
--kfm-font-mono	Technical/metadata text	"JetBrains Mono", monospace
--kfm-font-size-base	Default font size	16px
--kfm-line-height-base	Line height	1.6
--kfm-font-weight-normal	Normal weight	400
--kfm-font-weight-bold	Emphasis	600
--kfm-font-weight-heavy	Display weight	700

All font tokens are defined in the text-styles.css file and compiled into web/src/styles/tokens.css for the React frontend.

⸻

🧩 Type Scale (Responsive)

Level	Usage	Size (rem)	Line Height	Weight
h1	Page titles, major headings	2.25rem	1.2	700
h2	Section titles	1.75rem	1.3	600
h3	Subheadings	1.5rem	1.4	600
h4	Minor headings	1.25rem	1.5	500
body-lg	Large paragraph	1.125rem	1.6	400
body-md	Standard paragraph	1rem	1.6	400
body-sm	Compact UI text	0.875rem	1.5	400
caption	Footnotes, meta text	0.75rem	1.4	400
mono	Code/data labels	0.875rem	1.4	500


⸻

🧩 Example CSS Implementation

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


⸻

🧭 Accessibility Guidelines

Guideline	Description	Implementation
Contrast	Text-to-background ratio ≥ 4.5:1	Verified via Stark and Axe tools
Scalability	Text resizes up to 200% without loss of function	Relative units (rem/em) only
Focus State	Clearly visible focus ring around text inputs	outline-offset + box-shadow styles
Semantic Hierarchy	Headings in logical order (h1 → h6)	Validated via accessibility audit
Localization	Unicode-safe font stack with diacritics	Tested in English, French, Spanish


⸻

🧾 Provenance & Integrity

Asset	Figma Node	Exported	SHA256
type-hierarchy.png	figma://node/60:12	2025-09-30	sha256-cf12…
text-samples-dark.png	figma://node/60:15	2025-09-30	sha256-fb9a…
text-samples-light.png	figma://node/60:17	2025-09-30	sha256-3b41…

All exports and tokens validated through CI/CD under MCP reproducibility checks.

⸻

📚 Related Documents
	•	Design Tokens & Color Palette
	•	Panels & Detail Views
	•	Navigation Components
	•	Web UI Architecture
	•	Markdown “Standard Kit”

⸻

📜 License & Credits

Typography design © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Created by the KFM Design & Interaction Team, maintaining documentation-first principles for clarity, accessibility, and reproducibility across all Kansas Frontier Matrix UI and publishing contexts.

