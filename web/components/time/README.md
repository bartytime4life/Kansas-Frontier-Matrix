# ⏳ Time UI — Timeline Slider, Playback, & Event Markers

![Status](https://img.shields.io/badge/status-draft-informational)
![UI](https://img.shields.io/badge/ui-timeline%20%2B%20events-blue)
![Stack](https://img.shields.io/badge/stack-React%20%2B%20TypeScript-3178C6?logo=typescript&logoColor=white)
![Map](https://img.shields.io/badge/map-MapLibre%20GL%20JS-3B82F6)
![A11y](https://img.shields.io/badge/a11y-WCAG%20%2B%20WAI--ARIA-0EA5E9)

> 🎛️ A first-class time navigator for the Kansas-Matrix web UI: **scrub through years/dates**, **animate changes**, and **surface key historical events**—while keeping map layers & stories in sync.

---

## 🧭 Why this exists

Time is a *core navigation axis* in the KFM/Kansas-Matrix experience. The Time component(s) in this folder provide:

- 🗓️ **Timeline slider** to scrub across years (or specific dates)
- 🗺️ **Binding** between a selected time value and **time-aware layers**
- 📍 **Event markers** (point or range events) that can open tooltips and/or trigger story content
- ⏯️ **Playback controls** for temporal “animation” / stepping through slices
- 🧾 **Provenance-friendly UI hooks** (events/layers can show what they are, where they came from)

> [!IMPORTANT]
> The timeline is intended to be the **source of truth** for *time-filtered layers*—if a layer declares temporal metadata, it should respond to timeline changes.

---

## 📦 What lives in `web/components/time/`

Typical building blocks (names may vary by implementation):

- `TimeProvider` / `TimeContext` 🧠  
  Global (or route-level) time state: selected value, bounds, play state, step size, etc.
- `useTime()` hook 🪝  
  Typed access to time state + actions (set time, set range, toggle play).
- `TimeSlider` 🎚️  
  The actual slider UI (scrub + keyboard control).
- `TimeControls` ⏯️  
  Play/pause, step forward/back, speed (optional).
- `TimelineEvents` 📍  
  Event markers overlay aligned to the slider scale.
- `time.utils.ts` 🧰  
  Parsing/formatting helpers (year/date), clamping, stepping, debouncing.

> [!TIP]
> If the rest of the app already has a global state store (Zustand/Redux/etc.), `TimeProvider` can be a thin wrapper that plugs into it—what matters is a **single authoritative time state**.

---

## ✨ Features (expected)

### 1) Timeline slider 🎚️
- Discrete stepping (e.g., by **year** or dataset-defined steps)
- Optional continuous mode (dates) with snap-to-ticks
- Supports:
  - drag / scrub
  - click-to-jump
  - keyboard left/right (step), home/end (min/max)

### 2) Playback (temporal animation) ⏯️
- Play/pause
- Step forward/back
- Optional speed multiplier
- Ends behavior:
  - stop at max
  - loop (optional)

### 3) Event markers & “temporal storytelling” 📍📚
- Events appear as:
  - **point events** (single date/year)
  - **range events** (start–end span, e.g., multi-year periods)
- Click or focus + enter triggers:
  - tooltip / popover
  - optional callback to open a Story Node

### 4) Layer time binding 🗺️
- A layer that declares temporal metadata should update when the time changes.
- Prefer a single “binder” at the map-view level that:
  - knows which layers are time-aware
  - applies map filters/styles efficiently (debounced while scrubbing)

---

## 🧱 Recommended public API

Expose a small, stable surface area from this folder (barrel exports help):

```ts
// web/components/time/index.ts (recommended)
export * from "./TimeProvider";
export * from "./useTime";
export * from "./TimeSlider";
export * from "./TimelineEvents";
export * from "./types";
```

### Types (suggested) 🧩

```ts
// web/components/time/types.ts
export type TimeGranularity = "year" | "date";

/**
 * Keep this *simple*: most historical layers can be driven by an integer year.
 * If you need full precision, use ISO date strings (UTC recommended).
 */
export type TimeValue = number | string; // 1900 OR "1951-07-10"

export interface TimeBounds<T extends TimeValue = TimeValue> {
  min: T;
  max: T;
  step?: number; // used when granularity === "year"
}

export interface TimeState<T extends TimeValue = TimeValue> extends TimeBounds<T> {
  granularity: TimeGranularity;
  value: T;
  isPlaying: boolean;
  speed?: number; // e.g., steps per second
}

export interface TimelineEvent {
  id: string;
  title: string;

  /** Use ISO for dates; use number for year-only events. */
  start: TimeValue;
  end?: TimeValue;

  description?: string;

  /** Optional: integrate with narrative/story mode */
  storyId?: string;

  /** Optional: provenance hooks */
  sources?: Array<{
    label: string;     // "Kansas Historical Society"
    citation?: string; // short citation key or internal reference
  }>;
}
```

---

## 🔌 Usage examples

### Example A — Basic timeline in a panel 🎛️

```tsx
import { TimeProvider, TimeSlider, TimelineEvents } from "@/web/components/time";

export function RightPanelTimeline() {
  return (
    <TimeProvider
      initial={{
        granularity: "year",
        min: 1850,
        max: 2020,
        value: 1900,
        isPlaying: false,
        step: 1,
      }}
    >
      <section aria-label="Time navigation" className="timePanel">
        <header className="timePanelHeader">
          <h2>🗓️ Timeline</h2>
        </header>

        <TimeSlider />

        <TimelineEvents
          events={[
            { id: "dustbowl", title: "Dust Bowl", start: 1931, end: 1939 },
            { id: "flood1951", title: "Great Flood", start: 1951 },
          ]}
        />
      </section>
    </TimeProvider>
  );
}
```

### Example B — MapLibre binding (time-aware layers) 🗺️

```tsx
import { useEffect } from "react";
import type maplibregl from "maplibre-gl";
import { useTime } from "@/web/components/time";

export function MapTimeBinder({ map }: { map: maplibregl.Map }) {
  const { state } = useTime();

  useEffect(() => {
    // Example: a layer whose features have a numeric `year` property.
    if (state.granularity === "year" && typeof state.value === "number") {
      map.setFilter("population-density", ["==", ["get", "year"], state.value]);
      map.setFilter("county-boundaries", ["<=", ["get", "year_start"], state.value]);
    }

    // If using ISO dates, normalize + compare consistently (UTC).
  }, [map, state.granularity, state.value]);

  return null;
}
```

> [!TIP]
> For performance: **debounce filter updates** during drag, and apply the final update on “commit” (pointer up / key up). Playback can update on a fixed tick.

### Example C — Clicking an event opens a Story Node 📚

```tsx
import { TimelineEvents } from "@/web/components/time";

export function TimelineWithStories({ openStory }: { openStory: (id: string) => void }) {
  return (
    <TimelineEvents
      events={[
        { id: "dustbowl", title: "Dust Bowl", start: 1931, end: 1939, storyId: "story-dustbowl" },
      ]}
      onEventSelect={(evt) => {
        if (evt.storyId) openStory(evt.storyId);
      }}
    />
  );
}
```

---

## 🧾 Data contracts

### ✅ Temporal layer metadata (recommended convention)
For a layer to be “time-aware,” it should declare *temporal intent* in metadata so the UI can bind it.

Example (illustrative):

```json
{
  "id": "population-density",
  "title": "Population Density",
  "temporal": {
    "granularity": "year",
    "values": [1890, 1900, 1910, 1920, 1930, 1940],
    "field": "year"
  }
}
```

Alternative (range-based features):

```json
{
  "id": "county-boundaries",
  "title": "County Boundaries (Historical)",
  "temporal": {
    "granularity": "year",
    "rangeFields": { "start": "year_start", "end": "year_end" }
  }
}
```

> [!IMPORTANT]
> Keep temporal metadata **explicit and machine-readable**. The slider can’t reliably “guess” time behavior.

### ✅ Timeline event catalog (recommended convention)
Events are best stored as JSON/YAML in a simple catalog that this component can consume.

```yaml
- id: dustbowl
  title: "Dust Bowl"
  start: 1931
  end: 1939
  description: "A prolonged period of severe dust storms affecting the Great Plains."
  sources:
    - label: "KFM Event Catalog"
      citation: "event:dustbowl"
```

---

## ♿ Accessibility checklist

Use semantic controls and ARIA only when needed:

- ✅ Slider uses `<input type="range">` *or* a well-tested slider component
- ✅ Provide a visible label (or `aria-label`) for screen readers
- ✅ Keyboard support:
  - Left/Right = step
  - Home/End = bounds
  - Space = play/pause (if focus is on play button)
- ✅ Provide `aria-valuetext` for human-friendly announcements (e.g., “Year 1900”)
- ✅ Focus rings are visible and not removed

> [!NOTE]
> Prefer semantic HTML first; ARIA is for filling gaps—not replacing good markup.

---

## ⚡ Performance notes

- 🧠 Precompute time-aware layers once (IDs + temporal rules)
- 🧵 Debounce expensive updates when scrubbing (map filter/style churn)
- 🎞️ Playback should tick at a stable cadence (e.g., `requestAnimationFrame` or interval)
- 🧊 Consider a “dragging” flag to reduce map work until commit

---

## 🧪 Testing ideas

- Unit tests:
  - clamping (min/max)
  - stepping logic
  - playback tick progression
- Component tests:
  - slider keyboard controls
  - event selection callbacks
- Map integration tests (smoke):
  - moving the slider changes filters for time-aware layers

---

## 🧰 Troubleshooting

**My layer doesn’t change with the slider**
- Confirm the layer declares temporal metadata (`temporal` block).
- Confirm the map binder applies the correct filter and the feature property types match (number vs string).

**Playback is choppy**
- Reduce update frequency while playing.
- Avoid recomputing event layouts on every tick; memoize by bounds + viewport.

**Events don’t line up with the slider**
- Ensure event `start/end` match the slider’s `granularity` (year vs date) and bounds.

---

## 🗺️ Next steps (common upgrades)

- 📏 Range selection (start–end window), not just a single instant
- 🧷 Snap-to-event and “jump to next/prev event”
- 🧠 “Smart” step lists per active layer set (union of available years)
- 🧾 Provenance UI: show sources for events/layers in tooltips
