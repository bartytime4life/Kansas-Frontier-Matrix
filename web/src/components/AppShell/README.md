<div align="center">

# 🏗️ Kansas Frontier Matrix — AppShell Component  
`web/src/components/AppShell/`

**Core Layout · Global Providers · Responsive Container**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../../.github/workflows/ci.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **AppShell** component is the **root layout and orchestration layer** of the  
Kansas Frontier Matrix web application. It defines the application’s top-level structure,  
loading global contexts, managing responsive layout regions, and rendering  
the primary UI panels — **Header**, **MapView**, **TimelineView**, **LayerControls**,  
**DetailPanel**, and **AIAssistant**.

All components inside AppShell share the same **Context Providers**, ensuring consistent  
state between map, timeline, and AI panels.  

It’s the “hub” where Kansas’s data, history, and user interactions converge.

---

## 🧱 Directory Structure

```text
web/src/components/AppShell/
├── AppShell.tsx           # Main layout and routing logic
├── AppLayout.tsx          # Grid / flex layout definitions
├── LoadingScreen.tsx      # Initial app loading splash
├── ErrorBoundary.tsx      # Catches rendering or network errors
├── styles.scss            # Layout, grid, and theme styling
└── __tests__/             # Tests for layout, context loading, and rendering


⸻

🧩 Component Architecture

flowchart TD
  ROOT["AppShell\n(global entry)"]
  ROOT --> H["Header"]
  ROOT --> L["LayerControls"]
  ROOT --> M["MapView"]
  ROOT --> D["DetailPanel"]
  ROOT --> AI["AIAssistant"]
  ROOT --> T["TimelineView"]
  ROOT --> ACC["Accessibility Components"]
%% END OF MERMAID


⸻

🧠 Responsibilities

Responsibility	Description
Context Loading	Initializes all app-wide providers: Theme, Timeline, Map, Layer, AI, and Accessibility contexts.
Layout Grid	Defines the responsive layout and flex behavior for all panels (map, timeline, detail).
Routing & State	Handles top-level routing and persistent UI state (active panel, selected entity).
Error Handling	Wraps children with ErrorBoundary and shows user-friendly fallback UI.
Theming & Motion	Integrates Framer Motion transitions for smooth mounting/unmounting of panels.
Initialization	Displays LoadingScreen while fetching configuration and STAC metadata.


⸻

⚙️ Example Implementation

import React from "react";
import {
  ThemeProvider,
  TimelineProvider,
  LayerProvider,
  MapProvider,
  AIProvider,
  AccessibilityProvider,
} from "../../context";

import { Header } from "../Header";
import { MapView } from "../MapView";
import { TimelineView } from "../TimelineView";
import { LayerControls } from "../LayerControls";
import { DetailPanel } from "../DetailPanel";
import { AIAssistant } from "../AIAssistant";
import "./styles.scss";

export const AppShell: React.FC = () => {
  return (
    <AccessibilityProvider>
      <ThemeProvider>
        <AIProvider>
          <TimelineProvider>
            <LayerProvider>
              <MapProvider>
                <div className="app-shell">
                  <Header />
                  <main className="app-main">
                    <LayerControls />
                    <MapView />
                    <DetailPanel />
                    <AIAssistant />
                  </main>
                  <TimelineView />
                </div>
              </MapProvider>
            </LayerProvider>
          </TimelineProvider>
        </AIProvider>
      </ThemeProvider>
    </AccessibilityProvider>
  );
};


⸻

🧮 Layout Grid

flowchart TB
  H["Header (fixed top)"] --> MA["Main Area"]
  MA --> L["Left: Layer Controls"]
  MA --> M["Center: MapView"]
  MA --> D["Right: Detail Panel + AIAssistant"]
  MA --> TL["Bottom: Timeline (responsive)"]
%% END OF MERMAID

Grid behavior:
	•	Uses CSS Grid with responsive breakpoints defined in styles.scss.
	•	Panels auto-collapse on smaller screens; timeline becomes overlayed slider.
	•	Map always occupies central focus (min-width prioritized).

⸻

🎨 Styling & Theming
	•	Color and typography tokens imported from web/src/styles/variables.scss.
	•	Supports light/dark themes via ThemeContext.
	•	Framer Motion animates transitions between modes (fade, slide).
	•	Uses TailwindCSS utilities for flexible layout alignment.

⸻

🧪 Testing

Test Case	Description
Renders All Panels	Asserts Header, Map, Timeline, and AI Assistant load.
Context Availability	Ensures all providers deliver correct default values.
ErrorBoundary	Catches thrown component errors gracefully.
LoadingScreen	Displays until STAC catalog + API config are loaded.
Responsive Layout	Snapshot tests for desktop, tablet, mobile breakpoints.

Tools: Jest + React Testing Library + Cypress (for E2E).
Accessibility tested with axe-core (focus traps, ARIA labels, color contrast).

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	Contexts (Timeline, Map, AI, Layer, Accessibility), STAC catalog, API endpoints
Outputs	Fully rendered, interactive layout (HTML + React state tree)
Dependencies	React 18+, Framer Motion, TailwindCSS, TypeScript
Integrity	CI validates build integrity, accessibility score ≥ 95%, and 100% layout coverage


⸻

🔗 Related Documentation
	•	Web Frontend Components
	•	Context Providers
	•	Web UI Architecture
	•	Accessibility Design Guide

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — Built with the Master Coder Protocol (MCP)
for reproducible, accessible, and modular design.

“The AppShell is the frontier’s foundation — all stories, data, and design begin here.”

