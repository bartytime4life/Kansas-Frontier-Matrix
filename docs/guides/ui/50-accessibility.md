<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9b6e3b6d-8b6e-4a72-8c9c-43c56b5d9d7a
title: UI Accessibility
type: standard
version: v1
status: draft
owners: [kfm-ui, faircare-council]
created: 2026-03-04
updated: 2026-03-04
policy_label: public
related:
  - docs/guides/ui/README.md
  - docs/standards/governance/ROOT-GOVERNANCE.md
  - docs/standards/faircare/FAIRCARE-GUIDE.md
  - mcp/model_cards/climate_anomaly_net_v3.md
tags: [kfm, ui, accessibility, a11y, wcag]
notes:
  - "Accessibility requirements and implementation guidance for KFM Map Explorer, Story Mode, Focus Mode, and trust surfaces (Evidence Drawer, Policy Notice, Export)."
[/KFM_META_BLOCK_V2] -->

# UI Accessibility
One-line purpose: Ensure KFM’s UI is usable with keyboard and assistive technologies while preserving KFM’s governance UX (evidence-first, policy-visible, cite-or-abstain).

---

## Impact
- **Status:** Draft (intended to become “Active” when CI gates exist)
- **Owners:** `kfm-ui` (implementation) + `faircare-council` (review) *(TODO: confirm teams)*
- **Primary outcome:** Accessibility is treated as a **hard gate** for core trust surfaces (Evidence Drawer, Policy Notices, Exports), not optional polish.
- **Target audience:** UI engineers, designers, reviewers, QA

Badges (placeholders):

- ![Status](https://img.shields.io/badge/Status-Draft-lightgrey)
- ![A11y](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA%2B-blue)
- ![Governance](https://img.shields.io/badge/Governance-default--deny%20%2F%20fail--closed-orange)

Quick nav:

- [Scope](#scope)
- [KFM confirmed minimum requirements](#kfm-confirmed-minimum-requirements)
- [Targets and unknowns](#targets-and-unknowns)
- [Component guidance](#component-guidance)
- [Implementation patterns](#implementation-patterns)
- [Testing and gates](#testing-and-gates)
- [PR checklist](#pr-checklist)
- [Appendix](#appendix)

---

## Scope

### In scope
- **Web UI**: Map Explorer, Story Mode, Focus Mode, Catalog, Admin/Steward.
- **Trust surfaces**: Evidence Drawer, Policy Notice (why withheld), Data Version labels, “What changed?” panels.
- **Export outputs**: “downloadable report” / exports produced by the UI.

### Exclusions
- **Legal compliance determinations** (this doc is engineering guidance, not legal advice).
- **Non-web native apps** (unless explicitly added to KFM).
- **PDF/UA certification** as a formal guarantee (we can still design for tagged PDFs, but treat as a separate gate).

---

## Definitions and conventions

- **a11y**: Accessibility.
- **AT**: Assistive Technology (screen readers, speech input, switch devices).
- **WCAG**: Web Content Accessibility Guidelines (success criteria for conformance).
- **CONFIRMED / PROPOSED / UNKNOWN** labels:
  - **CONFIRMED** = explicitly stated in KFM docs or referenced standards already adopted by KFM artifacts.
  - **PROPOSED** = recommended practice we intend to enforce, pending governance sign-off.
  - **UNKNOWN** = decision not yet made; includes the smallest verification steps.

---

## KFM confirmed minimum requirements

These are the *minimum accessibility requirements* called out in KFM UI guidance.

- **CONFIRMED:** Keyboard navigable layer controls and Evidence Drawer; **visible focus states**.
- **CONFIRMED:** Text labels for policy badges and status indicators (no color-only meaning).
- **CONFIRMED:** ARIA labels for map controls.
- **CONFIRMED:** Safe Markdown rendering for narratives (CSP + sanitization to prevent XSS).
- **CONFIRMED:** Export outputs include citations and `audit_ref` in a readable format.

---

## Targets and unknowns

### Accessibility targets

| Target | Status | Notes |
|---|---|---|
| WCAG **2.1 AA+** as a baseline target | **CONFIRMED** | KFM artifacts already declare `accessibility_compliance: "WCAG 2.1 AA+"` in metadata. |
| WCAG **2.2 AA** as an upgrade target | **PROPOSED** | Adopt WCAG 2.2 AA for new UI work unless a compatibility constraint is documented. |
| Section 508 alignment (if applicable to deployments) | **PROPOSED** | Only enforce for deployments with that jurisdictional requirement. |
| Screen reader support baseline (NVDA + VoiceOver) | **PROPOSED** | Add JAWS only if required by user base / deployment. |

### Unknowns

| Unknown | Status | Smallest verification steps |
|---|---|---|
| Which WCAG version is the *project-wide* hard requirement (2.1 vs 2.2)? | **UNKNOWN** | 1) UI + Governance owners pick a baseline in an ADR. 2) Add CI gate text in this doc + workflow. |
| Are we generating exports as HTML, PDF, or both? | **UNKNOWN** | 1) Confirm export format(s). 2) If PDF: define tagging strategy (or document limitation). |
| Accessibility requirements for embedded 3D (Cesium) scenes | **UNKNOWN** | 1) Decide if 3D is “enhancement” vs “required.” 2) Define accessible alternative surface(s). |

---

## Component guidance

This section maps KFM UI components to accessibility expectations. Where possible, “MUST” items should become automated checks.

### App shell, navigation, and landmarks

- **PROPOSED:** Use semantic landmarks: `header`, `nav`, `main`, `footer`.
- **PROPOSED:** Provide a “Skip to main content” link as the first focusable element.
- **PROPOSED:** Preserve a logical tab order (DOM order should match visual order).

### Map Explorer

KFM Map Explorer includes map canvas + layer panel + time controls + inspection + Evidence Drawer.

- **CONFIRMED:** Layer controls must be keyboard navigable and have visible focus.
- **CONFIRMED:** Map controls must have ARIA labels.
- **PROPOSED:** Provide a non-map alternative to access the same information:
  - “Selected features list” (table or list) with keyboard navigation.
  - Feature details panel that is fully readable by screen reader.
- **PROPOSED:** Do not rely on color-only encoding for any “status” or “policy” badge.

### Timeline and time controls

- **PROPOSED:** Use native controls where possible (`<input type="range">`) with labeled min/max and current value.
- **PROPOSED:** Provide keyboard increments (arrow keys), page increments (PageUp/PageDown), and a “jump to start/end” (Home/End).

### Evidence Drawer

This is a trust surface and must be accessible by design.

- **CONFIRMED:** Evidence Drawer must be keyboard navigable and reachable from layers/features and story claims.
- **PROPOSED:** Treat Evidence Drawer as a modal dialog or a drawer with:
  - Focus trap while open
  - Escape key closes
  - Close button is reachable and labeled
  - Focus returns to the invoker on close
- **PROPOSED:** Evidence bundle IDs, dataset versions, licenses, freshness, and redaction notes must be readable as text (not only icons).

### Story Mode

Story Mode renders narrative Markdown with citations.

- **CONFIRMED:** Markdown rendering must be safe (sanitization + CSP).
- **PROPOSED:** Enforce heading order in stories (`h1` then `h2`, no skipping) to support screen-reader navigation.
- **PROPOSED:** All non-decorative images must have meaningful alt text.

### Focus Mode (chat + evidence-led Q&A)

- **PROPOSED:** Represent the conversation as a structured log (e.g., list of messages), not a visually-only container.
- **PROPOSED:** New assistant messages should be announced via an `aria-live` region (polite by default).
- **PROPOSED:** Inline citations must be:
  - Focusable
  - Have accessible names (“Open evidence bundle …”)
  - Open the Evidence Drawer in an accessible way (focus lands in the drawer)
- **CONFIRMED:** Exported Focus Mode answers must include citations and `audit_ref` in a readable format.

### Admin/Steward surfaces

- **PROPOSED:** Treat these as first-class a11y surfaces (they’re critical for governance work).
- **PROPOSED:** Tables must have headers; form inputs must have programmatic labels; errors must be announced.

---

## Implementation patterns

### Pattern: “Semantics first, ARIA second”
- **PROPOSED:** Prefer semantic HTML (button, link, input, details/summary) over `div` with roles.
- **PROPOSED:** Only add ARIA when native semantics can’t represent the interaction.

### Pattern: Visible focus (don’t remove outlines)
- **CONFIRMED (KFM):** Focus must be visible on keyboard navigation paths.
- **PROPOSED:** Provide a design token for focus ring and test it on dark/light basemaps.

### Pattern: Accessible “drawer/dialog” in React (near-runnable)
~~~tsx
import React, { useEffect, useRef } from "react";

type EvidenceDrawerProps = {
  open: boolean;
  title: string;
  onClose: () => void;
  children: React.ReactNode;
};

export function EvidenceDrawer({ open, title, onClose, children }: EvidenceDrawerProps) {
  const panelRef = useRef<HTMLDivElement | null>(null);
  const lastActiveRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (open) {
      lastActiveRef.current = document.activeElement as HTMLElement | null;
      // Move focus to the drawer container (or first focusable control inside it).
      panelRef.current?.focus();
    } else {
      // Restore focus to the element that opened the drawer.
      lastActiveRef.current?.focus();
    }
  }, [open]);

  useEffect(() => {
    if (!open) return;

    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
      // NOTE: Focus trapping typically uses a library (recommended) to avoid edge cases.
    };

    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [open, onClose]);

  if (!open) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-label={title}
      className="EvidenceDrawerOverlay"
    >
      <div
        ref={panelRef}
        tabIndex={-1}
        className="EvidenceDrawerPanel"
      >
        <header className="EvidenceDrawerHeader">
          <h2>{title}</h2>
          <button type="button" onClick={onClose} aria-label="Close evidence drawer">
            ✕
          </button>
        </header>

        <div className="EvidenceDrawerBody">{children}</div>
      </div>
    </div>
  );
}
~~~

### Pattern: Policy badge not color-only
- **CONFIRMED (KFM):** Policy badges and status indicators must have text labels (no color-only meaning).
- **PROPOSED:** Badge structure:
  - visible text (e.g., `Restricted`, `Generalized`, `Public`)
  - optional icon
  - optional tooltip (tooltip must be keyboard accessible)

### Pattern: Focus Mode live region for new messages
~~~tsx
export function ChatLog({ messages }: { messages: Array<{ id: string; role: "user" | "assistant"; text: string }> }) {
  return (
    <section aria-label="Focus Mode conversation">
      {/* Live region announces updates for screen reader users */}
      <div aria-live="polite" aria-atomic="false" className="sr-only">
        {messages.length ? messages[messages.length - 1].text : ""}
      </div>

      <ol>
        {messages.map((m) => (
          <li key={m.id} aria-label={m.role === "user" ? "User message" : "Assistant message"}>
            <p>{m.text}</p>
          </li>
        ))}
      </ol>
    </section>
  );
}
~~~

### Pattern: Safe Markdown rendering
- **CONFIRMED (KFM):** Markdown rendering must be safe (CSP + sanitization).
- **PROPOSED:** Enforce:
  - HTML disabled unless explicitly whitelisted
  - link `rel="noopener noreferrer"` where appropriate
  - image URL allowlist if needed
  - no scriptable content in narratives

---

## Testing and gates

### Accessibility test pipeline

~~~mermaid
flowchart LR
  D[Design review] --> L[Lint and typecheck]
  L --> A[Automated audit]
  A --> M[Manual tests]
  M --> P[Merge]
  M --> F[Fix issues]
  F --> L
~~~

### Automated checks

- **PROPOSED:** `eslint-plugin-jsx-a11y` (or equivalent) in CI.
- **PROPOSED:** `axe-core` (unit/integration) and `playwright-axe` (E2E) checks for critical pages:
  - Map Explorer
  - Story Mode reader
  - Focus Mode chat
  - Evidence Drawer open state
  - Export preview / export action surfaces
- **PROPOSED:** “No keyboard traps” check (manual + automated where possible).

### Manual checks (minimum)

- **PROPOSED:** Keyboard-only walkthrough:
  - Can you reach **every** control?
  - Can you operate map controls, layer toggles, time slider, citations, and drawer close?
  - Is focus always visible?
- **PROPOSED:** Screen reader smoke tests:
  - NVDA + Firefox (Windows)
  - VoiceOver + Safari (macOS)
- **PROPOSED:** Zoom and reflow:
  - 200% zoom (text legible, no loss of functionality)
- **PROPOSED:** Reduced motion:
  - With `prefers-reduced-motion`, animations are reduced or have alternatives.

---

## PR checklist

Use this as a merge gate checklist for UI work.

- [ ] **CONFIRMED:** Layer controls and Evidence Drawer are keyboard navigable; focus is visible.
- [ ] **CONFIRMED:** Policy/status meaning is not color-only; text labels exist.
- [ ] **CONFIRMED:** Map controls have ARIA labels.
- [ ] **CONFIRMED:** Story Markdown rendering is sanitized and CSP-compatible.
- [ ] **CONFIRMED:** Export outputs include citations and `audit_ref` in a readable format.
- [ ] **PROPOSED:** Automated a11y audits pass on changed routes/components.
- [ ] **PROPOSED:** Manual keyboard walkthrough completed for affected screens.
- [ ] **PROPOSED:** If new visualization assets added: contrast and alt-text requirements met.

---

## Appendix

<details>
<summary>Appendix A — Notes on maps and accessibility</summary>

- **PROPOSED:** A canvas/webgl map is rarely “readable” directly by a screen reader. Treat the map as an *interaction surface* and provide parallel accessible representations:
  - “Selected feature list” with details
  - A text-based summary of current view state (bbox name/region label, time window, active layers, policy labels)
  - Keyboard-operable controls for zoom/pan (or focusable map control buttons)
- **PROPOSED:** Ensure that **policy redactions/generalizations** apply equally to:
  - on-map rendering
  - feature detail panels
  - alt text and textual summaries
  - exports

</details>

<details>
<summary>Appendix B — Reference links</summary>

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WCAG overview: https://www.w3.org/WAI/standards-guidelines/wcag/
- ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- ARIA in HTML: https://www.w3.org/TR/html-aria/
- Section 508 overview: https://www.section508.gov/

</details>

[Back to top](#ui-accessibility)
