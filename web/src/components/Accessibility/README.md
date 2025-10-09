<div align="center">

# ♿ Kansas Frontier Matrix — Accessibility Components  
`web/src/components/Accessibility/`

**Keyboard Navigation · Screen Reader Support · Focus Management · Reduced Motion**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../../.github/workflows/ci.yml)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../../../docs/design/reviews/accessibility/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **Accessibility components** implement the **Kansas Frontier Matrix** project’s  
commitment to **universal design** and **inclusive interaction**, ensuring that  
all users — including those relying on assistive technologies — can explore the  
interactive map, timeline, and knowledge graph effectively.

These components apply **WCAG 2.1 AA** standards and integrate tightly with  
the `AccessibilityContext`, `ThemeContext`, and keyboard hooks.  
Their purpose is to manage focus, provide ARIA announcements, and respect  
user preferences for reduced motion or contrast modes.

> _Accessibility in KFM isn’t an afterthought — it’s baked into the core architecture, per MCP guidelines._

---

## 🧱 Directory Structure

```text
web/src/components/Accessibility/
├── FocusRing.tsx          # Visual focus indicator for keyboard navigation
├── SkipToContentLink.tsx  # "Skip to main content" anchor for screen readers
├── LiveRegion.tsx         # ARIA live region for announcements (AI/chat/timeline updates)
├── ReducedMotionProvider.tsx # Disables animations if user prefers reduced motion
├── HotkeyHints.tsx        # Overlay listing active keyboard shortcuts
├── styles.scss            # High-contrast & focus-state styling
└── __tests__/             # Unit tests for focus/ARIA behavior


⸻

♿ Key Accessibility Features

Component	Purpose	WCAG Alignment
FocusRing	Draws visible outlines around focused elements (keyboard nav).	2.4.7 Focus Visible
SkipToContentLink	Allows skipping repetitive UI to main content.	2.4.1 Bypass Blocks
LiveRegion	Announces timeline/map updates or AI responses to screen readers.	4.1.3 Status Messages
ReducedMotionProvider	Disables animations if prefers-reduced-motion is true.	2.3.3 Animation from Interactions
HotkeyHints	Displays accessible overlay of keyboard shortcuts.	2.1.1 Keyboard
styles.scss	Ensures color contrast ≥ 4.5:1 and visible focus styles.	1.4.3 Contrast (Minimum)


⸻

⚙️ Implementation Example — FocusRing

import React from "react";

export const FocusRing: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div className="focus-ring-wrapper">
    {children}
    <span className="focus-outline" aria-hidden="true" />
  </div>
);

// styles.scss
.focus-outline {
  outline: 2px solid var(--kfm-color-accent);
  outline-offset: 3px;
  transition: outline 0.1s ease;
}

Used globally in all interactive elements — buttons, timeline handles,
map markers, and text inputs.

⸻

🧩 Interaction Flow

flowchart TD
  K["Keyboard Input"] --> F["FocusRing\n(visible focus)"]
  F --> SR["Screen Reader\nARIA Live Region"]
  SR --> ANN["Announcements\n(e.g. 'Event loaded: Flood of 1951')"]
  PREF["User Prefs\n(prefers-reduced-motion)"] --> RM["ReducedMotionProvider"]
  RM --> APP["AppShell\ncontrols Framer Motion transitions"]
%% END OF MERMAID


⸻

🧠 Integration Notes
	•	Context Link: All components subscribe to AccessibilityContext
to detect motion preferences, focus mode, and screen-reader flags.
	•	Hotkeys: Registered in useKeyboardShortcuts() to trigger map/timeline actions.
	•	Reduced Motion: When enabled, suppresses Framer Motion animations and replaces
animated transitions with instant style updates.
	•	ARIA Roles: role="dialog", role="status", and aria-live="polite" used appropriately.
	•	Announcements: All live text changes are debounced to prevent “speech spam.”

⸻

🧪 Testing & Validation

Test Type	Description	Tools
Keyboard Nav	Verify focus cycles correctly through interactive components.	Cypress + axe-core
Screen Reader Output	Ensure ARIA live regions announce updates correctly.	NVDA / VoiceOver
Color Contrast	Validate color pairs exceed 4.5:1 ratio.	axe-core / Lighthouse
Reduced Motion	Confirm animations respect user system preferences.	Puppeteer automation
Hotkey Overlay	Verify hint panel opens via shortcut (? key).	Jest + RTL

Target coverage: ≥ 90% for accessibility hooks and components.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	AccessibilityContext, keyboard events, user system preferences
Outputs	Focus visuals, ARIA messages, hotkey overlays
Dependencies	React 18+, Framer Motion, axe-core, TailwindCSS
Integrity	Verified via CI: accessibility audits, Lighthouse tests, unit & e2e suites


⸻

🔗 Related Documentation
	•	Web Frontend Components
	•	Context — AccessibilityContext
	•	Design Accessibility Reviews
	•	Keyboard Focus Audit
	•	Screen Reader Audit

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — Developed under the Master Coder Protocol (MCP) for
transparency, inclusivity, and reproducible accessibility design.

“Accessibility isn’t a feature; it’s the frontier every user deserves to cross.”

