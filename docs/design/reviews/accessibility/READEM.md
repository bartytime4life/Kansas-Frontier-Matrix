<div align="center">

# ♿ Kansas Frontier Matrix — Accessibility Reviews  
`docs/design/reviews/accessibility/`

**Mission:** Guarantee full **WCAG 2.1 AA** and **Section 508** compliance across the web interface, timeline, map, and AI-assistant components.  
Accessibility is treated as a **core layer of reproducibility** under the Master Coder Protocol (MCP) — ensuring that every user, regardless of ability, can explore Kansas’s historical and spatial narratives.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)
[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#audit-checklists)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY-4.0-lightgrey)](../../../LICENSE)

</div>

---

## 🎯 Purpose

This directory documents **accessibility reviews** for all Kansas Frontier Matrix user-interface elements (React, MapLibre, Timeline Canvas, and AI panels).  
Each review validates compliance with standards and captures recommended improvements.  
Reports here complement the **UI Component Reviews** (`../ui_components/`) and are required before any major release or feature merge.

---

## 🧭 Directory Layout

```text
docs/design/reviews/accessibility/
├── README.md                          # This index
├── color_contrast.md                   # Palette + token compliance (WCAG ratios)
├── keyboard_focus.md                   # Keyboard navigation & tab order
├── screen_reader.md                    # ARIA roles, alt text, semantic structure
└── templates/                          # Review templates & checklists
    ├── accessibility_audit_template.md
    ├── wcag_checklist.md
    └── aria_roles_reference.md


⸻

🪶 Review Scope

Layer	Focus	Example Checks
Web UI	React DOM + MapLibre overlays	Focus order, heading hierarchy, landmarks
Timeline Canvas	Dynamic rendering	Keyboard access, color contrast of events
Map Controls	Buttons, legends, tooltips	ARIA labels, hit-area size, hover states
AI Assistant	Text areas, chat log	Live-region updates, focus trapping
Data Visualization	Map/timeline color scales	Perceptual contrast, pattern redundancy


⸻

✅ Audit Checklists

Each review uses standardized templates aligned to WCAG 2.1 AA and EN 301 549:

Category	Target	Pass / Fail / Notes
Perceivable	Text contrast ≥ 4.5 : 1, non-text ≥ 3 : 1	
Operable	All actions keyboard-accessible	
Understandable	Consistent navigation / labeling	
Robust	Valid semantic HTML, ARIA roles	
Cognitive	Motion & animation tolerances (prefers-reduced-motion)	


⸻

🧩 Accessibility Review Flow

flowchart TD
  A["Component Ready\n(Figma → React build)"] --> B["Run Automated Tests\n(Axe · Lighthouse · pa11y)"]
  B --> C["Manual Audit\nKeyboard · Screen Reader · Color"]
  C --> D["Record Findings\nTemplate + Checklist"]
  D --> E["Fix / Iterate\nDeveloper implements corrections"]
  E --> F["Verify & Approve\n2 Reviewers sign-off"]
  F --> G["Archive Report\nunder docs/design/reviews/accessibility/"]
<!-- END OF MERMAID -->


⸻

🧠 Tools & Methods
	•	Automated Testing: Axe Core CLI, Lighthouse CI, Pa11y, and Storybook a11y.
	•	Manual Audits: NVDA / VoiceOver screen-reader sessions, keyboard walkthroughs, color-contrast measurements (Contrast-Checker, Figma Plugin).
	•	Design Tokens: --kfm-color-*, --kfm-font-*, --kfm-spacing-* ensure consistent accessible theming.
	•	Reporting: All audits exported to Markdown using the accessibility_audit_template.md.

⸻

🧾 Provenance & Versioning

Each accessibility review includes:

review_id: "a11y_{{component}}_{{version}}"
component_path: "web/src/components/{{component}}"
reviewed_by: ["@auditor1", "@auditor2"]
date: "{{ ISO8601_DATE }}"
commit: "{{ GIT_COMMIT }}"
wcag_level: "AA"
status: "approved" # or "needs work"


⸻

🧰 Templates

File	Description
accessibility_audit_template.md	Full structured audit form (WCAG → criteria → evidence → resolution).
wcag_checklist.md	Quick reference list for manual verification.
aria_roles_reference.md	Standard ARIA roles, landmarks, and usage in KFM components.


⸻

🔒 Compliance Targets
	•	WCAG 2.1 AA baseline (with AAA aimed for text contrast).
	•	Section 508 (U.S. federal standard).
	•	WAI-ARIA 1.2 best practices.
	•	Verified using Lighthouse CI ≥ 90 Accessibility Score per component.

⸻

🪪 License

All accessibility reviews and templates are licensed under Creative Commons CC-BY 4.0.
© 2025 Kansas Frontier Matrix Design Collective.

⸻



