# ⏱️ `time/` UI Components

![React](https://img.shields.io/badge/React-UI-61DAFB?logo=react&logoColor=000000)
![TypeScript](https://img.shields.io/badge/TypeScript-ready-3178C6?logo=typescript&logoColor=ffffff)
![A11y](https://img.shields.io/badge/A11y-WCAG%202.1%20AA-success)
![KFM](https://img.shields.io/badge/KFM-maps%20%2B%20timelines-7c3aed)

> Shared components + helpers for **displaying** 🗓️ and **selecting** ⏳ time across the KFM web experience (maps, timelines, story views).

---

## ✨ Why this exists

Time is a first-class axis in Kansas Frontier Matrix:
- **Timelines** drive historical/contextual exploration 📼
- **Time ranges** filter catalogs/datasets 🔎
- **“Last updated”** builds trust for near-real-time layers ♻️

This folder keeps all that temporal UX consistent, testable, and accessible.

---

## 🧭 What lives here

> [!TIP]
> If you’re not sure what’s exported, check `index.ts` in this folder.

Typical building blocks you’ll find here:

- **`<Timestamp />`** 🕰️  
  Renders a stable, readable timestamp (with optional timezone + tooltip).
- **`<TimeAgo />`** ⌛  
  Human-friendly relative time (e.g., “5 min ago”), with an absolute fallback.
- **`<TimeRange />` / `<TimeRangePicker />`** 🧱  
  Start/end (or open-ended) range selection for dataset and catalog filtering.
- **`<TimelineScrubber />`** 🎚️  
  Slider/scrubber for map+timeline overlays (including “Year: ####” labeling).

> If you don’t see a component you need, add it here instead of re-implementing time logic in feature folders.

---

## 📦 Suggested folder layout (example)

```text
📁 web/src/components/time/
├─ ⏱️ README.md
├─ index.ts
├─ 🕰️ Timestamp.tsx
├─ ⌛ TimeAgo.tsx
├─ 🧱 TimeRangePicker.tsx
├─ 🎚️ TimelineScrubber.tsx
└─ 🧪 __tests__/
   ├─ Timestamp.test.ts
   ├─ TimeAgo.test.ts
   └─ TimeRangePicker.test.ts
```

---

## 🚀 Usage examples

### 1) Display a dataset “Last Updated” (absolute + relative)

```tsx
import { Timestamp, TimeAgo } from "./time";

export function DatasetMeta({ updatedAtISO }: { updatedAtISO: string }) {
  return (
    <div>
      <div>
        <strong>Last updated:</strong>{" "}
        <Timestamp value={updatedAtISO} />
        {" · "}
        <TimeAgo value={updatedAtISO} />
      </div>
    </div>
  );
}
```

### 2) Build a time-range filter for catalog search

```tsx
import { useMemo, useState } from "react";
import { TimeRangePicker } from "./time";

export function CatalogFilters() {
  const [range, setRange] = useState<{ start?: string; end?: string }>({});

  const query = useMemo(() => {
    // 👇 Keep this as a *contract-driven* mapping.
    // The API supports time-range filtering; use the agreed query param names.
    const params = new URLSearchParams();
    if (range.start) params.set("time_start", range.start);
    if (range.end) params.set("time_end", range.end);
    return params.toString();
  }, [range]);

  return (
    <section>
      <h3>Filters</h3>
      <TimeRangePicker value={range} onChange={setRange} />

      <small style={{ opacity: 0.8 }}>
        Query preview: <code>{query || "(none)"}</code>
      </small>
    </section>
  );
}
```

> [!NOTE]
> Use **ISO 8601** strings (`YYYY-MM-DDTHH:mm:ssZ`) end-to-end. Avoid passing `Date` objects across boundaries unless you control timezone handling.

---

## 🎨 Timeline UX notes (KFM flavor)

When time drives a map overlay, make it feel “native” to the story:

- A **timeline overlay** can sit at the bottom of a map view 🗺️🎞️
- A subtle “film strip” motif can communicate historical sequences 📼 (but must not hide interactive targets)
- Always **label the current time** near the slider (tooltip or “Year: 1950”) to reduce user guesswork 🎯

---

## ✅ Formatting rules (do this every time)

### ✅ Store + transport
- Prefer **ISO 8601 UTC** (`...Z`) for API payloads, metadata, and persisted state.
- Treat “date-only” values as a **different type** than “timestamp” values (avoid accidental midnight conversions).

### ✅ Display
- Use semantic HTML: render timestamps as `<time dateTime="...">...</time>` 🧠
- Make timezone explicit when it matters:
  - Show `UTC` label for system timestamps
  - Show local timezone label (e.g. `America/Chicago`) when displaying user-local times

### ✅ Relative time
- Relative time (“3 hours ago”) must have an **absolute** fallback (tooltip, aria-label, or secondary text).

---

## ♿ Accessibility checklist

- ⌨️ **Keyboard support** for range pickers and scrubbing controls
- 🗣️ **Screen reader clarity**
  - `aria-label="Time range start"`
  - `aria-label="Time range end"`
  - For scrubbing: announce current value (e.g., `aria-valuetext="Year 1950"`)
- 🎚️ Sliders must expose:
  - `role="slider"`
  - `aria-valuemin`, `aria-valuemax`, `aria-valuenow`
- 🎯 Don’t rely on color alone to communicate “live/updated” state

---

## 🧪 Testing guidance

> [!TIP]
> Time-based UI breaks silently—test it like a contract.

- Freeze time with fake timers (or inject `now()` into helpers)
- Add regression tests for:
  - DST transitions 🌗
  - Leap day (Feb 29) 📆
  - End-exclusive vs end-inclusive ranges (be explicit!)
  - Empty/unknown times (render `—` or “Unknown” consistently)

---

## 🧯 Common pitfalls (avoid these)

- ❌ Formatting with local timezone when the data represents UTC
- ❌ Mixing “date-only” and “datetime” strings
- ❌ Scrubber updates causing excessive re-renders (debounce / requestAnimationFrame for drag)
- ❌ Relative time that never updates (or updates too frequently)
  - Use sensible intervals (e.g., 1 min) unless you truly need seconds

---

## 🤝 Contributing

### Add a new time component
- Keep formatting logic in **one place** (helper or shared formatter)
- Document props clearly (including accepted string formats)
- Include at least:
  - 1 story/example snippet 📎
  - 1 test file 🧪
  - A11y notes ♿

### PR checklist ✅
- [ ] Uses ISO 8601 consistently
- [ ] Works in `America/Chicago` and UTC
- [ ] Keyboard + screen reader verified
- [ ] Tests cover at least one tricky edge case

---

## 🔗 Related docs (project)

- 📚 API contracts for search + time range filtering (see `docs/architecture/` and server API docs)
- 🗺️ Map + timeline interaction patterns (see UX sketches / blueprint docs)
- 🧾 Provenance & metadata expectations (STAC/DCAT/PROV)

---

**Owner:** 🧑‍💻 Web UI / Design System  
**Scope:** 🔒 Presentation + input only (no direct DB access; always go through API contracts)