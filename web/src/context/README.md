<div align="center">

# 🧠 Kansas Frontier Matrix — Web Frontend Context  
`web/src/context/`

**Global App State · Map/Timeline Sync · Selection & Theming**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../.github/workflows/ci.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/src/context/` directory hosts **React Context providers** and **typed hooks** that coordinate
global state across the Kansas Frontier Matrix UI — keeping the **Map**, **Timeline**, **LayerControls**,
**DetailPanel**, and **AI Assistant** in sync.

Design goals:
- **Single source of truth** for cross-cutting state (timeline range, selected entity, active layers).
- **Deterministic updates** with minimal re-renders (memoized values/selectors).
- **Type-safe contracts** shared via `web/src/types/`.
- **MCP-aligned**: documented behaviors, predictable effects, and testable reducers.

---

## 🧱 Directory Structure

```text
web/src/context/
├── TimelineContext.tsx      # Global time window (start/end/zoom) + actions
├── MapContext.tsx           # Map instance refs, viewport, interactions
├── LayerContext.tsx         # Visible overlays, opacity, legends (STAC-driven)
├── SelectionContext.tsx     # Selected entity/event, multi-select, clipboard
├── ThemeContext.tsx         # Light/Dark theme + persistence
├── AIContext.tsx            # AI request state, responses, citations
├── AccessibilityContext.tsx # Focus ring, reduced motion, keyboard hints
└── index.ts                 # Re-exports all providers & hooks

Each context exports:
	•	A Provider (wraps children).
	•	A typed useXxx() hook.
	•	Actions / reducers (where appropriate).

⸻

🔗 Context Graph

flowchart TD
  TL["TimelineContext\n{start,end,zoom}"] --> MAP["MapContext\nviewport, mapRef"]
  TL --> LYR["LayerContext\nvisible, opacity"]
  SEL["SelectionContext\nentityId, type"] --> DP["DetailPanel"]
  MAP --> DP
  LYR --> MAP
  THEME["ThemeContext\nlight|dark"] --> APP["AppShell"]
  AI["AIContext\nrequest,status,answer"] --> AIP["AI Panel"]
  ACC["AccessibilityContext\nfocus,reducedMotion"] --> APP
<!-- END OF MERMAID -->


⸻

🧩 Usage Example

// App.tsx
import {
  TimelineProvider,
  MapProvider,
  LayerProvider,
  SelectionProvider,
  ThemeProvider,
  AIProvider,
  AccessibilityProvider,
} from "./context";

export function App() {
  return (
    <AccessibilityProvider>
      <ThemeProvider>
        <AIProvider>
          <TimelineProvider>
            <LayerProvider>
              <MapProvider>
                <SelectionProvider>
                  {/* AppShell: Header, MapView, TimelineView, Panels */}
                </SelectionProvider>
              </MapProvider>
            </LayerProvider>
          </TimelineProvider>
        </AIProvider>
      </ThemeProvider>
    </AccessibilityProvider>
  );
}

// Example component reading/writing context
import { useTimeline, useSelection } from "../context";

export function TimelineToolbar() {
  const { start, end, setRange, zoomIn, zoomOut } = useTimeline();
  const { selected, clearSelection } = useSelection();

  return (
    <div className="toolbar">
      <button onClick={() => zoomOut()}>−</button>
      <button onClick={() => zoomIn()}>+</button>
      <button onClick={() => setRange("1850-01-01", "1900-12-31")}>1850–1900</button>
      {selected && <button onClick={clearSelection}>Clear selection</button>}
      <span>{start} — {end}</span>
    </div>
  );
}


⸻

⚙️ Patterns & Contracts
	•	Providers compose, not collide: keep state domains independent; communicate via props or events.
	•	Selectors & memoization: export derived values (useMemo) to avoid unnecessary renders.
	•	Reducer-first critical flows: timeline and layers use reducers for explicit, testable transitions.
	•	Persistence: ThemeContext and user prefs saved via localStorage (namespaced keys).
	•	Interoperability: types (Event, Layer, AIResponse, TimelineRange) come from web/src/types/.

⸻

🧪 Testing
	•	Unit tests for each context reducer and hook under web/src/context/__tests__/.
	•	Use React Testing Library + Jest with render(<Provider>children</Provider>).
	•	Validate:
	•	Initial state contracts
	•	Action transitions (happy & edge paths)
	•	Memoized selectors (stable identity)
	•	A11y toggles (reducedMotion, focus ring) behavior

Coverage target: ≥ 85%.

⸻

🧠 Performance Notes
	•	Co-locate heavy state with the nearest component; lift to context only when shared.
	•	Memoize context values; export granular hooks (e.g., useLayerOpacity(id)) when useful.
	•	Avoid passing mutable objects in context; prefer immutable updates.
	•	For large maps, sync viewport via throttled dispatches (e.g., 60–120ms).

⸻

♿ Accessibility

AccessibilityContext centralizes:
	•	prefers-reduced-motion handling
	•	Focus outline mode (keyboard vs. mouse)
	•	Skip-to-content announcements
	•	Hotkey hints (surfaced to help overlays)

All contexts must respect these flags (e.g., animations disabled when reduced motion is on).

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	Typed models from ../types/, utilities from ../utils/, hooks from ../hooks/
Outputs	Context providers/hooks consumed by UI components
Dependencies	React 18+, TypeScript
Integrity	Linted (ESLint), typed (tsc --noEmit), tested in CI with coverage gates


⸻

🔗 Related Documentation
	•	Web Frontend Overview
	•	Hooks
	•	Types
	•	Web UI Architecture

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — built with MCP standards for reliability, clarity, and accessibility.

“Context is the campfire: every component gathers round to share the same light.”

