<div align="center">

# 🧩 Kansas Frontier Matrix — Accessibility Templates  
`docs/design/reviews/accessibility/templates/`

**Purpose:** Provide standardized templates and checklists for all accessibility audits conducted under the Kansas Frontier Matrix (KFM) design system.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../)
[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](../README.md)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY-4.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🎯 Objective

This folder collects reusable **audit templates**, **checklists**, and **reference guides** for accessibility compliance.  
Each template follows **MCP reproducibility** principles: consistent metadata, measurable results, and clear traceability to commits and UI components.

---

## 📁 Directory Layout

```text
docs/design/reviews/accessibility/templates/
├── README.md                       # This index
├── accessibility_audit_template.md # Full a11y audit report form
├── wcag_checklist.md               # Criteria mapping (WCAG 2.1 AA)
└── aria_roles_reference.md         # Role + landmark usage guide


⸻

🧩 Template Overview

File	Purpose	Usage
accessibility_audit_template.md	Structured form to document per-component accessibility reviews.	Copy when starting a new audit.
wcag_checklist.md	Detailed success criteria for WCAG 2.1 AA mapped to KFM components.	Reference during testing.
aria_roles_reference.md	Quick reference for ARIA roles, landmarks, and states used in React/MapLibre.	Consult for code review validation.


⸻

🪶 Template Usage Flow

flowchart TD
  A["Start Audit\n(new component / feature)"] --> B["Duplicate Template\naccessibility_audit_template.md"]
  B --> C["Fill In Metadata\ncommit · reviewer · component"]
  C --> D["Run Automated Tests\nAxe · Lighthouse · Pa11y"]
  D --> E["Perform Manual Checks\nKeyboard · Screen Reader · Color"]
  E --> F["Record Results + Screenshots\nin Markdown"]
  F --> G["Submit Pull Request\nTag reviewers + attach report"]
  G --> H["Archive Approved Audit\nin /accessibility/"]
<!-- END OF MERMAID -->


⸻

🧠 Best Practices
	•	Always test both light and dark themes using the same checklist.
	•	Include screenshots and test environment details in every audit.
	•	Link directly to related component paths (e.g., web/src/components/Timeline/).
	•	Save final reports under the corresponding directory (docs/design/reviews/accessibility/).
	•	Mark results with standardized keys:

status: pass | fail | needs-review
wcag_level: "AA"
reviewer: "@handle"
commit: "{{ GIT_COMMIT }}"



⸻

🧾 Provenance & Compliance

Field	Description
Frameworks Tested	React 18, MapLibre GL, HTML5 Canvas
Standards Referenced	WCAG 2.1 AA, Section 508, WAI-ARIA 1.2
Automation Tools	Axe Core, Pa11y CI, Lighthouse, Storybook a11y
Version Control	Every audit template includes commit metadata
Audit Frequency	Per release or major UI update


⸻

🪪 License

All accessibility templates and documentation are released under Creative Commons CC-BY 4.0.
© 2025 Kansas Frontier Matrix Design Collective

⸻



