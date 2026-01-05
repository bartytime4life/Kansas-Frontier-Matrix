# 🧠 `web/src/store` — Redux Store (Global UI State)

![KFM](https://img.shields.io/badge/KFM-v13-2ea44f?style=flat)
![State](https://img.shields.io/badge/state-Redux-764ABC?logo=redux&logoColor=white)
![UI](https://img.shields.io/badge/UI-React-61DAFB?logo=react&logoColor=000)
![Types](https://img.shields.io/badge/types-TypeScript-3178C6?logo=typescript&logoColor=white)
![Rules](https://img.shields.io/badge/rules-API%20Boundary%20%26%20Evidence--First-orange)

This folder contains the **global state layer** for the KFM web client.  
We use **Redux** to keep state transitions predictable, debuggable, and easy to reason about—especially for **timeline-driven map layers**, multi-panel UI, and shared “app state” that many components depend on.

> [!IMPORTANT]
> **KFM invariant:** the UI (including this store) **must never** talk to Neo4j directly.  
> All data access flows through the governed API layer (see `src/server/`). 🔒

---

## 🧭 Quick links

- 🧩 UI entrypoint: `web/src/App.*`
- 🌐 API calls: `web/src/services/` (typically `apiClient.*`)
- 🗺️ Feature modules: `web/src/features/` (map, timeline, story, etc.)
- 📚 System rules: `docs/MASTER_GUIDE_v13.md` (pipeline invariants + governance)

---

## 📦 What the store is for (and what it is *not*)

### ✅ Store **should** hold (global/shared state)
Typical “app-wide” state that multiple components need:

- 🗓️ **Time control:** `currentDate`, time range, playback speed, time step
- 🗺️ **Map session state:** viewport (lng/lat/zoom), selected feature(s), hovered id, active basemap
- 🧱 **Layer toggles:** which layers are visible, opacity, styling options
- 🧾 **Evidence context pointers:** selected dataset IDs, STAC item IDs, PROV bundle IDs
- 🧭 **Navigation:** current route view mode, sidebar tabs, panel layout
- 👤 **Auth/session flags:** logged-in status + user profile summary (never secrets)

### 🚫 Store **must not** hold
- ❌ **Secrets** (API keys, tokens, credentials). Prefer httpOnly cookies or platform auth.
- ❌ **Raw / huge datasets** (multi‑MB GeoJSON blobs, imagery buffers, large arrays).
- ❌ **Non-serializable objects** (MapLibre/Cesium map instances, DOM nodes, class instances).
- ❌ **Unsourced narrative claims** (Story content must be governed and evidence-linked).

> [!TIP]
> If it’s **local to one component** and doesn’t need deep-linking or cross-feature coordination,
> keep it as local React state (`useState`, `useReducer`) instead of Redux.

---

## 🧱 Folder layout (recommended conventions)

> Your repo may have slight naming differences—follow existing patterns in this codebase.  
> This layout is the **intended shape** for long-term maintainability.

```text
📁 web/
  📁 src/
    📁 store/
      📄 README.md                 ← you are here
      📄 index.ts                  ← store bootstrap (configureStore)
      📄 hooks.ts                  ← typed hooks (useAppDispatch/useAppSelector)
      📄 rootReducer.ts            ← reducer registry
      📁 slices/                   ← feature slices
        📄 timelineSlice.ts
        📄 mapSlice.ts
        📄 layersSlice.ts
        📄 uiSlice.ts
        📄 authSlice.ts
        📄 storySlice.ts
      📁 selectors/                ← optional: shared selectors
      📁 middleware/               ← optional: custom middleware
      📁 persistence/              ← optional: localStorage/sessionStorage helpers
      📁 __tests__/                ← reducer/thunk tests
```

---

## 🔁 Data flow (Redux + governed API)

```mermaid
flowchart LR
  UI[🧑‍💻 React UI] -->|dispatch(action)| Store[(🧠 Redux Store)]
  Store -->|selectors| UI

  UI -->|dispatch(thunk)| Thunk[⚙️ async thunk]
  Thunk -->|request| Client[🌐 web/src/services/apiClient]
  Client -->|HTTP| API[🛡️ src/server API]
  API -->|response (redacted + typed)| Thunk
  Thunk -->|dispatch(result)| Store
```

> [!NOTE]
> The **store is UI-stage** in the KFM pipeline:  
> **ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode**  
> The store must respect this ordering and only consume **API outputs**.

---

## 🧩 Slice design rules

### 1) Prefer “feature slices” 🧱
Group by product features (map, timeline, layers, story), not by UI widgets.

✅ **Good**
- `timelineSlice` owns `currentDate`, playback controls
- `layersSlice` owns active layer IDs, layer configs
- `storySlice` owns selected story node id, focus mode state

❌ **Avoid**
- `leftSidebarSlice`, `timelineWidgetSlice` (too component-shaped)

### 2) Keep state minimal + normalized 🧠
- Store identifiers and configuration, not huge payloads.
- Normalize lists by `id` when feasible.

### 3) State must be serializable 📦
- No MapLibre/Cesium instances in Redux.
- If you need to reference a runtime object, keep it in a module singleton or React ref.

### 4) Derive UI values via selectors 🎯
- Keep computed state out of reducers when possible.
- Use memoized selectors (e.g., `reselect`) for heavy derivations.

---

## 🧑‍💻 Quick start patterns

### Typed hooks (recommended)
```ts
// web/src/store/hooks.ts
import { useDispatch, useSelector } from "react-redux";
import type { RootState, AppDispatch } from "./index";

export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector = useSelector.withTypes<RootState>();
```

### Dispatching from a component
```tsx
import { useAppDispatch, useAppSelector } from "@/store/hooks";
import { setCurrentDate } from "@/store/slices/timelineSlice";

export function TimelineSlider() {
  const dispatch = useAppDispatch();
  const currentDate = useAppSelector((s) => s.timeline.currentDate);

  return (
    <input
      type="date"
      value={currentDate}
      onChange={(e) => dispatch(setCurrentDate(e.target.value))}
    />
  );
}
```

---

## 🧱 Adding a new slice (checklist)

> [!TIP]
> If a slice will influence map rendering, aim for **fast updates** and **minimal payload**.

### ✅ Steps
1. **Create slice** in `store/slices/<feature>Slice.ts`
2. **Export actions** + **default reducer**
3. **Register reducer** in `rootReducer.ts`
4. **Update store bootstrap** in `index.ts` (if needed)
5. Add **selectors** for common reads
6. Add **tests** for reducers and thunks

### Example slice template (Redux Toolkit style)
```ts
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

type TimelineState = {
  currentDate: string; // ISO date: YYYY-MM-DD
  playing: boolean;
};

const initialState: TimelineState = {
  currentDate: "1861-01-01",
  playing: false,
};

const timelineSlice = createSlice({
  name: "timeline",
  initialState,
  reducers: {
    setCurrentDate(state, action: PayloadAction<string>) {
      state.currentDate = action.payload;
    },
    setPlaying(state, action: PayloadAction<boolean>) {
      state.playing = action.payload;
    },
  },
});

export const { setCurrentDate, setPlaying } = timelineSlice.actions;
export default timelineSlice.reducer;
```

---

## 🌐 Async data: thunks, caching, and governance

### Rules of the road 🚦
- ✅ Thunks call `web/src/services/*` (API clients), **not** DB drivers
- ✅ API responses must include (or allow retrieval of) provenance pointers when relevant
- ✅ Preserve **classification/redaction** signals from the API in state/UI
- ❌ Don’t “invent” narrative content in client state

### Caching strategy (practical defaults)
- Cache **lightweight summaries** (IDs, counts, timestamps, flags).
- Prefer **request libraries** (e.g., RTK Query) for API response caching if adopted.
- Use explicit invalidation when `currentDate` changes (timeline-driven refresh).

> [!IMPORTANT]
> **Classification propagation:** derived views must never become less restricted than inputs.  
> If the API flags something as restricted/redacted, the store should carry that flag through UI rendering.

---

## 🔗 Deep linking: URL ↔ store state

The frontend supports deep links like “open the app at a specific time + place + layer set.”

✅ Keep these state fields URL-sync friendly:
- `currentDate`
- map viewport (`lng`, `lat`, `zoom`)
- active layers list
- selected story node / focus mode id

<details>
  <summary><strong>✨ Suggested URL shape (example)</strong></summary>

```text
/map?date=1861-01-01&z=7&lat=38.5&lng=-98.0&layers=treaties,railroads&focus=story_0123
```

</details>

---

## 🧪 Testing expectations

### What to test
- ✅ Reducers: “given state + action → expected state”
- ✅ Selectors: derived outputs, memoization behavior for heavy selectors
- ✅ Thunks: API success/failure, redaction flags, error state

### What to avoid
- ❌ Snapshot testing entire store state
- ❌ Coupling tests to MapLibre/Cesium runtime objects

---

## 🧯 Common gotchas

- **Re-render storms:** use memoized selectors and avoid selecting giant subtrees.
- **Non-serializable warnings:** don’t store Date objects, map instances, class instances.
- **Timeline invalidation:** when `currentDate` changes, make sure dependent caches refresh.
- **Race conditions:** cancel/ignore stale requests (especially during rapid slider scrubbing).

---

## ✅ Definition of “done” for store changes

- [ ] State change is explained in slice docstrings / comments
- [ ] Actions are serializable + reducers are pure
- [ ] Async work goes through `services/` → governed API
- [ ] New state supports deep linking if user-facing
- [ ] Tests updated/added for reducers and critical selectors
- [ ] No governance regressions (API boundary, provenance, classification)

---

## 📚 References (project docs)

- `docs/MASTER_GUIDE_v13.md` — pipeline invariants + governance
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — v13 structure & rationale
- `docs/reports/story_nodes/` — narrative content (not stored here)

---

### 🗺️ Store philosophy in one line
**Keep UI state predictable, provenance-respectful, and API-governed—so maps, timelines, and stories stay trustworthy.** ✅
