<div align="center">

# 🪟 Kansas Frontier Matrix — Modals Component  
`web/src/components/Modals/`

**Dialogs · Popovers · Settings Panels · Accessibility-First Design**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../../.github/workflows/ci.yml)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../../../docs/design/reviews/accessibility/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **Modals Component Suite** provides reusable, accessible dialog interfaces across  
the **Kansas Frontier Matrix Web Application**. It includes modal implementations for  
application settings, keyboard shortcuts, “About” information, and help overlays.  

Built with **Framer Motion** for subtle animations and adhering to **WCAG 2.1 AA**,  
these components ensure seamless accessibility and predictable focus management.  

Each modal uses a consistent structure and can be controlled via context, keyboard  
shortcuts, or button triggers in the **Header** or **AI Assistant** panels.

---

## 🧱 Directory Structure

```text
web/src/components/Modals/
├── ModalContainer.tsx       # Core wrapper for modal logic (open/close, focus trap)
├── AboutModal.tsx           # Project information and metadata
├── SettingsModal.tsx        # User preferences (theme, motion, language)
├── HelpModal.tsx            # Keyboard shortcuts and user guide
├── AccessibilityModal.tsx   # A11y options (text size, color contrast)
├── styles.scss              # Theming, transitions, responsive layout
└── __tests__/               # Jest + RTL tests for modal accessibility and behavior


⸻

⚙️ Component Architecture

flowchart TD
  H["Header / Keyboard Shortcut"] --> M["ModalContainer"]
  M --> S1["AboutModal"]
  M --> S2["SettingsModal"]
  M --> S3["HelpModal"]
  M --> S4["AccessibilityModal"]
  M --> ACC["AccessibilityContext\n(focus trap, reduced motion)"]
%% END OF MERMAID


⸻

🧩 Key Features

Feature	Description	Standard
Accessible Dialogs	Uses ARIA role="dialog" and aria-modal="true" with keyboard traps.	WCAG 2.1 2.4.3 / 4.1.2
Framer Motion Animations	Smooth entrance/exit with reduced-motion detection.	2.3.3
Focus Management	Focus is auto-trapped inside modal and restored on close.	2.1.1
Keyboard Shortcuts	Press ? for Help, Ctrl+, for Settings, Shift+A for Accessibility.	Custom Hook
Dynamic Content	Each modal renders children passed as props with auto-sizing.	MCP UI modularity
Responsive Layout	Works on desktop and mobile with adaptive sizing and scroll-lock.	WCAG 1.4.10
Portal Rendering	Renders modals via React Portal to preserve DOM hierarchy.	WAI-ARIA best practice


⸻

💬 Example Implementation

import React, { useState } from "react";
import { ModalContainer } from "./ModalContainer";

export function AboutModal() {
  const [open, setOpen] = useState(false);

  return (
    <>
      <button onClick={() => setOpen(true)} aria-haspopup="dialog">
        About
      </button>
      <ModalContainer
        open={open}
        onClose={() => setOpen(false)}
        title="About Kansas Frontier Matrix"
      >
        <p>
          Kansas Frontier Matrix is an open-source, spatiotemporal knowledge hub
          connecting people, places, and events through time.
        </p>
      </ModalContainer>
    </>
  );
}


⸻

🧠 TypeScript Interfaces

export interface ModalProps {
  open: boolean;
  title?: string;
  children: React.ReactNode;
  onClose: () => void;
  ariaLabel?: string;
  width?: "sm" | "md" | "lg";
}


⸻

🎨 Styling & Motion
	•	Animations: Defined in styles.scss and powered by Framer Motion.
	•	fade-in and slide-up for entry.
	•	Reduced-motion users receive instant render (no transitions).
	•	Layout: Centered viewport overlay using CSS Grid.
	•	Backdrop: Semi-transparent with blur (backdrop-filter: blur(4px)).
	•	Colors: Adapt to theme (ThemeContext): light and dark palettes.

⸻

♿ Accessibility Implementation

Concern	Implementation
Focus Trap	Managed using AccessibilityContext and focus sentinel nodes.
Screen Readers	All modals use aria-labelledby and aria-describedby.
Escape Key	Closes the modal immediately and restores previous focus.
Reduced Motion	Animation disabled if prefers-reduced-motion detected.
Keyboard Shortcuts	Global listener for ?, Ctrl+,, and Shift+A.
Skip to Content	Press Alt+S focuses back to main content after modal close.

All accessibility features validated using axe-core and Lighthouse A11y audits.

⸻

🧪 Testing

Test Case	Description	Tools
Open/Close Logic	Ensures modals open and close with button and ESC key.	Jest + RTL
Focus Trap	Validates that focus stays within modal.	Cypress + axe-core
ARIA Compliance	Checks ARIA roles, labels, and hierarchy correctness.	axe-core
Reduced Motion	Confirms animations disabled when user preference set.	Jest mocks
Keyboard Shortcuts	Tests that global hotkeys trigger correct modal.	Jest DOM
Snapshot Testing	Captures consistent layout render per theme.	Jest Snapshot

Coverage goal: ≥ 90% lines / branches.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	AccessibilityContext, keyboard listeners, Framer Motion variants
Outputs	Portal-rendered dialogs with consistent theming and focus control
Dependencies	React 18+, Framer Motion, TailwindCSS, axe-core
Integrity	CI validates accessibility, stylelint, and ARIA test suite


⸻

🔗 Related Documentation
	•	Web Frontend Components Overview
	•	Accessibility Components
	•	Context — AccessibilityContext
	•	Web UI Architecture

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — developed in alignment with the Master Coder Protocol (MCP)
for inclusive, documented, and reproducible web architecture.

“Every dialog opens a door — the Modals framework ensures every user can walk through it.”

