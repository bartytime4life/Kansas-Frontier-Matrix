<div align="center">

# 🕰️ Kansas Frontier Matrix — TimelineView Component  
`web/src/components/TimelineView/`

**Temporal Navigation · Event Visualization · Time–Map Synchronization**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../../.github/workflows/ci.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../../../docs/design/reviews/accessibility/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **TimelineView Component** renders the interactive **chronological visualization**  
for the Kansas Frontier Matrix application. It enables users to explore Kansas’s history  
over time, synchronize the temporal range with the **MapView**, and interact with  
events from the underlying knowledge graph (people, places, treaties, disasters, etc.).

The timeline is implemented with **HTML5 Canvas** and **D3.js** for efficient rendering  
of hundreds of time-linked events. It connects to the **TimelineContext** for state  
management and dynamically filters map layers and entities by visible date range.

---

## 🧱 Directory Structure

```text
web/src/components/TimelineView/
├── TimelineView.tsx        # Main component rendering the timeline canvas
├── TimelineAxis.tsx        # D3-based axis and date ticks
├── EventMarkers.tsx        # Visual elements for events, hover effects
├── Tooltip.tsx             # Hover detail popups for events
├── styles.scss             # Timeline-specific layout and theme
└── __tests__/              # Jest + RTL tests for rendering and event selection


⸻

⚙️ Component Architecture

flowchart TD
  T["TimelineView\n(Canvas + D3)"] --> TC["TimelineContext\n(start, end, zoom)"]
  T --> API["FastAPI\nGET /events?start&end"]
  T --> MAP["MapView\n(syncs visible range)"]
  T --> DP["DetailPanel\nshows selected event"]
  T --> AI["AIAssistant\ncontext-aware queries"]
%% END OF MERMAID


⸻

🧩 Core Features

Feature	Description	Data Source
Time Navigation	Scroll, pan, and zoom to move across historical periods.	TimelineContext
Event Markers	Draws visual markers for historical events (color-coded by category).	/api/events
Hover Details	Displays tooltip with event name, date, and quick summary.	API / Graph data
Time–Map Sync	Adjusts map layers to match visible temporal range.	LayerContext / STAC
Temporal Filtering	Filters entities and datasets by year or interval.	Knowledge Graph
Keyboard Navigation	Arrow keys for scrolling; +/- for zoom.	AccessibilityContext
Performance Rendering	Uses HTML5 Canvas for high-FPS performance.	D3.js / Canvas API


⸻

💬 Example Implementation

import React, { useRef, useEffect } from "react";
import * as d3 from "d3";
import { useTimeline } from "../../context/TimelineContext";
import "./styles.scss";

export const TimelineView: React.FC = () => {
  const canvasRef = useRef(null);
  const { range, setRange, events } = useTimeline();

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Example: Draw events as colored dots
    events.forEach(event => {
      const x = d3.scaleTime()
        .domain([range.start, range.end])
        .range([0, canvas.width])(new Date(event.date));
      ctx.fillStyle = event.color || "#00b3b3";
      ctx.beginPath();
      ctx.arc(x, 40, 5, 0, 2 * Math.PI);
      ctx.fill();
    });
  }, [range, events]);

  return <canvas ref={canvasRef} className="timeline-canvas" width={800} height={100}></canvas>;
};


⸻

🧮 Data Flow

sequenceDiagram
  participant U as User
  participant T as TimelineView
  participant C as TimelineContext
  participant API as FastAPI
  participant M as MapView

  U->>T: Scrolls or drags timeline
  T->>C: setRange(newStart, newEnd)
  C->>API: GET /events?start&end
  API-->>C: Returns filtered events
  C-->>T: Updates event list
  T-->>M: Emits range for layer visibility sync
%% END OF MERMAID


⸻

🎨 Visual Design

Element	Description
Event Dots	Circles representing events; color-coded by category (e.g., treaties=blue, natural disasters=orange).
Axis	D3-rendered ticks for years/decades; dynamic labeling based on zoom level.
Timeline Range Shading	Highlights the active visible period with gradient overlay.
Tooltip	Appears on hover, displaying title, date, and summary.
Transitions	Smooth pan and zoom via Framer Motion easing curves.

Dark Mode: automatic inversion of background and tick colors via ThemeContext.

⸻

♿ Accessibility

Feature	Implementation
Keyboard Navigation	Arrow keys to pan; +/- for zoom; Enter to open event.
ARIA Roles	role="region" aria-label="Historical timeline of Kansas events".
Focus Ring	High-contrast outline for selected events.
Screen Reader Announcements	Event titles and years read on focus.
Reduced Motion	Disables smooth transitions if prefers-reduced-motion is active.


⸻

🧪 Testing

Test Case	Description	Tool
Event Rendering	Confirms events appear correctly and within range.	Jest + Canvas Mock
Range Update	Verifies range updates trigger new fetch calls.	React Testing Library
Hover/Tooltip	Ensures tooltip content matches hovered event.	Jest DOM
Keyboard Navigation	Simulates key input for accessibility.	Cypress
Accessibility Check	Validates ARIA and contrast compliance.	axe-core

Coverage target: ≥ 90% lines / branches.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	/api/events, TimelineContext, LayerContext
Outputs	Canvas rendering of historical events synchronized with MapView
Dependencies	React, D3.js, Framer Motion, TailwindCSS
Integrity	Validated via CI — functional, performance, and accessibility tests


⸻

🔗 Related Documentation
	•	MapView Component
	•	LayerControls Component
	•	Context — Timeline & Layer
	•	Web UI Architecture

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — developed under the Master Coder Protocol (MCP)
for reproducibility, accessibility, and scientifically traceable storytelling.

“The TimelineView connects memory to motion — Kansas history unfolding through time.”

