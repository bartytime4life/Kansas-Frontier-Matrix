<div align="center">

# 🧭 Kansas Frontier Matrix — Figma Navigation Components  
`docs/design/mockups/figma/components/navigation/`

**Mission:** Define, document, and maintain all **navigation-related Figma components**  
for the **Kansas Frontier Matrix (KFM)** — ensuring consistent, accessible, and scalable  
user flows across the web platform, mobile layouts, and embedded map/timeline interfaces.  

Navigation in KFM represents the **user’s compass** — guiding exploration through **time, terrain, and history**,  
anchored in design consistency and accessibility excellence.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-Figma%20Components-pink)](https://www.figma.com)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-yellow)](../../../../../LICENSE)

</div>

---

## 🗂️ Directory Layout

navigation/
│
├── README.md            → Overview & standards (this file)
├── examples.md          → Figma + React navigation component examples
├── tokens.json          → Navigation tokens (colors, sizes, spacing)
├── figma-refs.json      → Figma component IDs & version metadata
├── accessibility.md     → WCAG + ARIA usage documentation
└── changelog.md         → Version history & design updates

---

## 📘 Overview

The **Navigation System** serves as the **structural backbone** of the Kansas Frontier Matrix interface —  
from the global header and footer to contextual map/timeline controls.  

All navigation components are designed to be:  
- **Modular** — reusable across multiple layouts  
- **Token-driven** — visually consistent via shared design variables  
- **Accessible** — WCAG 2.1 AA compliant  
- **Reproducible** — version-controlled under Master Coder Protocol (MCP)  

---

## 🧭 Navigation Categories

| Category | Description | Example ID | React Equivalent |
|:----------|:-------------|:------------|:----------------|
| **Header** | Global top bar with logo, timeline, and search | `nav_header_v2.0` | `<Header />` |
| **Footer** | Page footer with credits, licenses, and version | `nav_footer_v1.4` | `<Footer />` |
| **Tabs** | Sectional navigation (Map / Timeline / Archives) | `nav_tabs_v1.2` | `<NavTabs />` |
| **Breadcrumbs** | Hierarchical navigation trail | `nav_breadcrumbs_v1.1` | `<Breadcrumbs />` |
| **Sidebar Menu** | Collapsible drawer with filters & datasets | `nav_sidebar_v1.3` | `<SidebarNav />` |
| **Floating Controls** | Map-level actions (zoom, compass, reset) | `nav_controls_v1.0` | `<MapControls />` |

---

## 🎨 Design Tokens

| Token | Purpose | Example Value |
|:-------|:---------|:--------------|
| `--nav-height-header` | Header height | `64px` |
| `--nav-height-footer` | Footer height | `48px` |
| `--nav-bg` | Navigation background | `var(--color-surface)` |
| `--nav-fg` | Text and icon color | `var(--color-fg)` |
| `--nav-hover-bg` | Hover state background | `var(--color-surface-alt)` |
| `--nav-accent` | Accent color for active states | `var(--color-accent)` |
| `--nav-radius` | Corner radius for tabs/buttons | `6px` |
| `--nav-gap` | Default spacing between elements | `12px` |
| `--nav-font` | Font style | `var(--font-sans)` |

> 💡 Tokens unify the visual rhythm between navigation, map, timeline, and input components.

---

## 🧱 Core Components

### 🧭 Header (`nav_header_v2.0`)

**Purpose:** Global site header featuring the Kansas Frontier Matrix logo,  
global search, and links to key modules (Map, Timeline, Archives).

| Property | Value |
|:-----------|:------|
| Height | `--nav-height-header` (`64px`) |
| Background | `--nav-bg` |
| Layout | Fixed top, sticky behavior |
| Interactive Elements | Logo, Search, Navigation Tabs, Menu Button |
| Accessibility | `<header role="banner">` + `aria-label="Main Header"` |
| Figma ID | `ic/navigation/header_v2.0` |
| React File | `/web/src/components/navigation/Header.tsx` |

---

### 🧭 Footer (`nav_footer_v1.4`)

**Purpose:** Displays attributions, data licenses, and project version.  

| Property | Value |
|:-----------|:------|
| Height | `--nav-height-footer` (`48px`) |
| Contrast | ≥ 4.5:1 text contrast ratio |
| Layout | Fixed bottom or static (context dependent) |
| Accessibility | `<footer role="contentinfo">` |
| Figma ID | `ic/navigation/footer_v1.4` |
| React File | `/web/src/components/navigation/Footer.tsx` |

---

### 🧭 Tab Navigation (`nav_tabs_v1.2`)

**Purpose:** Provides contextual mode switching (Map ↔ Timeline ↔ Archives).  
Styled for clarity with tokenized active, hover, and focus states.

| State | Visual |
|:-------|:--------|
| Default | Neutral text with underline hover |
| Active | Accent bottom border (`--nav-accent`) |
| Focus | Tokenized shadow focus ring |
| Disabled | Muted color with reduced opacity |

**ARIA Pattern:**  
```html
<nav role="tablist">
  <button role="tab" aria-selected="true" aria-controls="map">Map</button>
  <button role="tab" aria-selected="false" aria-controls="timeline">Timeline</button>
</nav>


⸻

🧭 Sidebar Menu (nav_sidebar_v1.3)

Purpose: Collapsible dataset/layer drawer with keyboard accessibility.

Feature	Description
Behavior	Expands/collapses via button toggle
Keyboard Support	Tab, Esc, and Shift+Tab navigation
ARIA	<aside aria-expanded="true" aria-label="Sidebar Navigation">
Figma ID	ic/navigation/sidebar_v1.3
React File	/web/src/components/navigation/Sidebar.tsx


⸻

🧭 Floating Map Controls (nav_controls_v1.0)

Purpose: Compact UI for spatial navigation — zoom, compass, and reset map state.

Feature	Description
Layout	Circular icon buttons with tokenized spacing
Keyboard Access	All controls tabbable (Tab, Enter)
Figma ID	ic/navigation/controls_v1.0
React File	/web/src/components/navigation/MapControls.tsx


⸻

♿ Accessibility Guidelines

Requirement	Description	Validation Tool
Keyboard Navigation	All tabs and menus navigable via keyboard	Manual / Playwright
Landmark Roles	Use <header>, <nav>, <footer> for structure	Axe DevTools
Focus Indicators	Focus ring visible, ≥ 3:1 contrast	Figma / Stark
Color Contrast	Text ≥ 4.5:1; icons ≥ 3:1	WebAIM Contrast Checker
ARIA Labels	Each region labeled via aria-label	Screen Reader Test

✅ All accessibility mappings are documented in accessibility.md.

⸻

💻 React Example — Global Header

import { IconSearch, IconMenu } from "@/icons";

export function Header() {
  return (
    <header className="kfm-header" role="banner" aria-label="Kansas Frontier Matrix Global Header">
      <div className="kfm-logo">KFM</div>

      <nav role="navigation" aria-label="Primary Navigation">
        <ul className="kfm-nav-links">
          <li><a href="/map" className="active">Map</a></li>
          <li><a href="/timeline">Timeline</a></li>
          <li><a href="/archives">Archives</a></li>
        </ul>
      </nav>

      <div className="kfm-actions">
        <button aria-label="Search"><IconSearch size="20" /></button>
        <button aria-label="Open Menu"><IconMenu size="20" /></button>
      </div>
    </header>
  );
}


⸻

🧩 Design–Development Mapping

Figma Component	React Component	Path	Description
nav_header_v2.0	<Header />	/web/src/components/navigation/Header.tsx	Sticky top bar
nav_footer_v1.4	<Footer />	/web/src/components/navigation/Footer.tsx	Footer attribution
nav_tabs_v1.2	<NavTabs />	/web/src/components/navigation/Tabs.tsx	Tab mode selector
nav_sidebar_v1.3	<SidebarNav />	/web/src/components/navigation/Sidebar.tsx	Dataset drawer
nav_controls_v1.0	<MapControls />	/web/src/components/navigation/MapControls.tsx	Floating map tools


⸻

🧾 Example Metadata (navigation.yml)

id: nav_header_v2.0
title: Global Header Navigation
category: navigation
version: v2.0
author: design.system.team
status: active
source_figma: https://www.figma.com/file/ABCDE12345/KFM-Component-Library?node-id=105%3A101
description: >
  Global header navigation bar with logo, search, and mode tabs.
accessibility:
  contrast_ratio: 5.0 : 1
  keyboard_focus: true
  reduced_motion: true
linked_docs:
  - ../../../../../ui-guidelines.md
  - ../../../../../style-guide.md
license: CC-BY-4.0


⸻

🧰 Related Files
	•	../README.md — Figma component index
	•	../../../../../ui-guidelines.md — Accessibility & usability standards
	•	../../../../../style-guide.md — Design tokens & color usage
	•	../../../../../interaction-patterns.md — Navigation & interaction patterns
	•	../../../../../reviews/ — Design review logs

⸻


<div align="center">


🧭 “Navigation is the map of experience —

design it like a compass that always points true.”
— Kansas Frontier Matrix Design System Team

</div>
