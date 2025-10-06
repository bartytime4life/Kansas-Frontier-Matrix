<div align="center">

# 🧭 Kansas Frontier Matrix — Figma Navigation Components  
`docs/design/mockups/figma/components/navigation/`

**Mission:** Define, document, and maintain all **navigation-related Figma components**  
for the **Kansas Frontier Matrix (KFM)** — ensuring consistent, accessible, and scalable  
user flows across the web platform, mobile layouts, and embedded map/timeline interfaces.  

Navigation is how users move through time, terrain, and history within the KFM system —  
combining clarity of movement, temporal context, and narrative progression.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-Figma%20Components-pink)](https://www.figma.com)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-yellow)](../../../../../LICENSE)

</div>

---

## 🗂️ Directory Layout

navigation/
├── README.md              → Overview & standards (this file)
├── examples.md            → Figma + React navigation component examples
├── tokens.json            → Navigation tokens (sizes, colors, spacing)
├── figma-refs.json        → Figma component IDs & variant mappings
├── accessibility.md       → WCAG compliance & ARIA patterns
└── changelog.md           → Version history & updates

---

## 📘 Overview

The **Navigation System** provides the structural backbone of the Kansas Frontier Matrix interface —  
from the global header and footer to localized controls for map and timeline navigation.

Each navigation component in this directory:
- Is **modular**, **responsive**, and **Figma–React synchronized**.  
- Follows **Master Coder Protocol (MCP)** for reproducible design.  
- Meets **WCAG 2.1 AA** accessibility standards.  
- Uses shared **design tokens** for colors, spacing, and motion.

---

## 🧭 Navigation Categories

| Type | Description | Example ID | React Equivalent |
|:------|:-------------|:-------------|:----------------|
| **Header** | Global top bar with logo, search, and timeline link | `nav_header_v2.0` | `<Header />` |
| **Footer** | Site-wide footer with credits and metadata | `nav_footer_v1.4` | `<Footer />` |
| **Tabs** | Contextual navigation between sections (Map, Timeline, Archives) | `nav_tabs_v1.2` | `<NavTabs />` |
| **Breadcrumbs** | Hierarchical trail navigation for datasets | `nav_breadcrumbs_v1.1` | `<Breadcrumbs />` |
| **Sidebar Menu** | Collapsible drawer with layer and dataset navigation | `nav_sidebar_v1.3` | `<SidebarNav />` |
| **Floating Controls** | On-map contextual navigation (zoom, compass, reset) | `nav_controls_v1.0` | `<MapControls />` |

---

## 🧱 Design Tokens (navigation/tokens.json)

| Token | Purpose | Example Value |
|:-------|:---------|:---------------|
| `--nav-height-header` | Default header height | `64px` |
| `--nav-height-footer` | Default footer height | `48px` |
| `--nav-bg` | Background color | `var(--color-surface)` |
| `--nav-fg` | Foreground text/icon color | `var(--color-fg)` |
| `--nav-hover-bg` | Hover background | `var(--color-surface-alt)` |
| `--nav-accent` | Accent border or highlight | `var(--color-accent)` |
| `--nav-radius` | Border radius for tabs/links | `6px` |
| `--nav-gap` | Spacing between elements | `12px` |
| `--nav-font` | Typography style | `var(--font-sans)` |

> Tokens unify visual rhythm between navigation, inputs, and panels.

---

## 🧭 Header Component (`nav_header_v2.0`)

**Description:**  
The global site header anchors navigation, timeline access, and global search.

| Attribute | Specification |
|:-----------|:---------------|
| **Height** | `--nav-height-header` (`64px`) |
| **Background** | `--nav-bg` |
| **Interactive Elements** | Logo, search bar, menu button, profile or settings icon |
| **Accessibility** | Semantic `<header>` role, ARIA labeling for navigation landmarks |
| **Behavior** | Sticky on scroll, reduced height on mobile |
| **Figma Node** | `ic/navigation/header_v2.0` |
| **React Component** | `<Header />` (`web/src/components/navigation/Header.tsx`) |

---

## 🧭 Footer Component (`nav_footer_v1.4`)

**Description:**  
Provides context and attribution links (data sources, license, contributors).

| Attribute | Specification |
|:-----------|:---------------|
| **Height** | `--nav-height-footer` (`48px`) |
| **Content** | Attribution text, quick links, and version info |
| **Color Contrast** | ≥ 4.5:1 for all text and icons |
| **Accessibility** | `<footer>` semantic tag with `aria-label="Site Footer"` |
| **Responsive Layout** | Collapsible column view for small screens |

---

## 🧭 Tab Navigation (`nav_tabs_v1.2`)

**Description:**  
Allows switching between major app modes — Map, Timeline, Archives, or Data Layers.

**Figma Spec:** `components/navigation/tabs/nav_tabs_v1.2`  
**React Equivalent:** `<NavTabs />`  
**ARIA Pattern:** `role="tablist"` + `aria-selected` + `aria-controls`

| State | Visual |
|:-------|:--------|
| Default | Subtle bottom border accent |
| Hover | Surface-alt background |
| Active | Accent color underline |
| Focus | Tokenized shadow focus ring |

---

## 🧩 Sidebar Menu (`nav_sidebar_v1.3`)

**Description:**  
A collapsible drawer navigation for datasets, layers, and tools.

- Uses tokenized shadow and overlay for accessibility.  
- Accessible via keyboard (`Tab`, `Esc`, `Shift+Tab`).  
- Implements focus trapping and ARIA state:  
  ```html
  <aside aria-label="Sidebar Navigation" aria-expanded="true"></aside>


⸻

♿ Accessibility Guidelines

Criterion	Requirement	Validation
Keyboard Navigation	All menus & tabs accessible via Tab, Enter, Space.	Manual Test
Focus Management	Focus trap in modals/sidebars.	Playwright / Manual
Landmarks	Use <header>, <nav>, <footer> with descriptive labels.	Axe DevTools
Contrast	≥ 4.5:1 for text, ≥ 3:1 for icons.	Figma + Stark
Reduced Motion	Respect prefers-reduced-motion.	Browser Simulation

Accessibility metadata is defined in accessibility.md for full ARIA role mappings.

⸻

🧩 Example — Global Header (React Implementation)

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

🧩 Design-to-Development Mapping

Figma Component	React Component	File Path	Notes
nav_header_v2.0	<Header />	/web/src/components/navigation/Header.tsx	Fixed header w/ search
nav_footer_v1.4	<Footer />	/web/src/components/navigation/Footer.tsx	Includes credits + links
nav_tabs_v1.2	<NavTabs />	/web/src/components/navigation/Tabs.tsx	Tab navigation system
nav_sidebar_v1.3	<SidebarNav />	/web/src/components/navigation/Sidebar.tsx	Collapsible dataset drawer


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

🧩 Related Files
	•	../README.md — Figma component index
	•	../../../../../ui-guidelines.md — Accessibility standards
	•	../../../../../style-guide.md — Visual and motion tokens
	•	../../../../../interaction-patterns.md — Navigation behaviors
	•	../../../../../reviews/ — Design review logs

⸻


<div align="center">


🧭 “Navigation is the map of experience —

design it like a compass that always points true.”
— Kansas Frontier Matrix Design System Team

</div>

