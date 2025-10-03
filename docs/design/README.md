<div align="center">

# 🎨 Kansas Frontier Matrix — Design Docs (`/docs/design/`)

**Mission:** Capture and organize all **design-oriented artifacts** —  
UI/UX flows, interaction patterns, visualization mockups, and cross-domain  
design decisions that shape the Kansas Frontier Matrix (KFM).  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)  
[![Design Standards](https://img.shields.io/badge/Design-Human%20Centered-orange)](README.md)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](README.md)  

</div>

---

## 🎯 Purpose

The `/docs/design/` directory is the **design hub** for Kansas Frontier Matrix.  
Where `/docs/architecture/` describes the *system structure*, this directory focuses on:  

- 📐 **UI/UX flows** — timeline, map, search, AI assistant.  
- 🖼️ **Visual design** — color tokens, typography, icons, layout standards.  
- 🗺️ **Interactive patterns** — map overlays, time slider behaviors, accessibility.  
- 📖 **Narrative design** — how oral histories, treaties, and data appear as stories.  
- 🤝 **Contributor guidance** — how to propose and review new design ideas.  

Design docs follow **Master Coder Protocol (MCP)**:  
- Always documented before implemented.  
- Include diagrams (Mermaid + static exports).  
- Reference accessibility, reproducibility, and storytelling impact.  

---

## 📚 Contents

```text
docs/design/
├── README.md                # Index (this file)
├── ui-guidelines.md          # UX principles, accessibility, responsive design
├── style-guide.md            # Visual design tokens (colors, typography, CSS rules)
├── interaction-patterns.md   # Timeline/map/legend/search behavior
├── storytelling.md           # Narrative design, oral histories, guided flows
├── mockups/                  # Wireframes, sketches, exported design images
├── diagrams/                 # Mermaid diagrams (UI flows, component states)
└── reviews/                  # Design review notes & ADR-style decisions


⸻

🗂️ Key Docs
	•	ui-guidelines.md → UX principles, accessibility, responsive layouts.
	•	style-guide.md → CSS tokens, typography, theming (light/dark modes).
	•	interaction-patterns.md → Map + timeline interaction flows.
	•	storytelling.md → Narrative UX, oral history integration.
	•	mockups/ → Wireframes (from Figma, Excalidraw, etc.).
	•	reviews/ → Past design discussions and decisions.

⸻

🧭 Usage
	1.	Contributors — Review existing design docs before proposing UI changes.
	2.	Developers — Use style and interaction docs to guide frontend code.
	3.	Researchers — Understand how design conveys historical complexity.
	4.	Reviewers — Record decisions in reviews/ with diagrams + rationale.

⸻

🔗 Related Docs
	•	Architecture Docs
	•	Web UI Docs
	•	Glossary

⸻


<div align="center">


🎨 Design is how history becomes experience.
Every UI element must serve clarity, accessibility, and storytelling.

</div>