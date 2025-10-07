<div align="center">

# 🧭 Kansas Frontier Matrix — UI Component Design Reviews  
`docs/design/reviews/ui_components/`

**Purpose:** Centralize peer-review records and audit templates for all **user-interface components**—from Figma mockups through React/MapLibre implementation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../)
[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](../accessibility/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY-4.0-lightgrey)](../../../LICENSE)

</div>

---

## 🎯 Objective

This directory tracks **UI component design reviews** to ensure each interactive element meets the project’s visual, behavioral, and accessibility standards.  
Every review documents the evolution of a component across design, implementation, and release.

UI components form the bridge between **data (knowledge graph)** and **interaction (map + timeline)**, so every change must preserve time–space–story alignment in the Kansas Frontier Matrix.

---

## 🧭 Directory Layout

```text
docs/design/reviews/ui_components/
├── README.md                    # This index
├── navigation.md                # Header, search, menus
├── timeline.md                  # Timeline slider, scrub, zoom
├── map_controls.md              # Map toolbar, layers, legend
├── ai_assistant.md              # AI drawer, prompt panel, chat UI
├── detail_panel.md              # Entity/event dossier panel
└── templates/                   # Forms for component-level review
    ├── component_review_template.md
    ├── figma_to_react_checklist.md
    └── accessibility_component_audit.md

Each markdown file documents:
	•	Design reference: Figma node ID / frame name
	•	Implementation reference: React component path (web/src/components/...)
	•	Review metadata: commit, reviewers, checklist, decisions

⸻

🪶 Review Criteria

Category	Requirement	Validation
Visual Consistency	Matches design tokens (--kfm-color-*, typography, spacing)	✅ Figma → React parity
Responsiveness	Adapts across ≥ 3 breakpoints	✅ Chrome DevTools audit
Accessibility	Meets WCAG 2.1 AA; proper ARIA roles	✅ Screen-reader test
Performance	≤ 16 ms paint for animation or transition	✅ Lighthouse/Profiler
Interaction Feedback	Clear hover/focus/active states	✅ Manual test
State Management	Uses React Context or props → stateless logic	✅ Code review
Documentation	README + comments updated	✅ Reviewer check
Versioning	Semantic version bump logged	✅ semver: in front-matter


⸻

🧩 Workflow
	1.	Open Review — copy templates/component_review_template.md.
	2.	Link Assets — reference Figma frame + React component path.
	3.	Assess — follow MCP checklist (clarity · consistency · compliance · reproducibility).
	4.	Record — document findings, screenshots, accessibility notes.
	5.	Approve / Merge — sign-off by ≥ 2 reviewers; commit message includes design-review: tag.
	6.	Archive — move closed reviews to /archive/ if superseded.

⸻

🧩 Example Diagram — UI Component Review Flow

flowchart TD
  A["Design Created\n(Figma Component)"] --> B["Implementation\n(React / MapLibre Component)"]
  B --> C["Internal Review\n(Design Team · Accessibility Audit)"]
  C --> D["Peer Review\n(PR · Reviewer Sign-off)"]
  D --> E["Approved & Merged\nVersion Bump + Tag"]
  E --> F["Archived\nin docs/design/reviews/ui_components/archive/"]
<!-- END OF MERMAID -->


⸻

🧰 Templates

Template	Description
component_review_template.md	Standard form for documenting each component’s audit
figma_to_react_checklist.md	Step-by-step Figma → implementation parity verification
accessibility_component_audit.md	WCAG/ARIA-focused component testing guide


⸻

🪪 Provenance & Licensing

All review artifacts are versioned alongside the source branch and retain provenance metadata (commit, mockup_version, reviewed_by).
Released under Creative Commons CC-BY 4.0 — attribution required when reusing review content.

© 2025 Kansas Frontier Matrix Design Collective


