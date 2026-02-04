# 🧠 `web/src/state` — Frontend State (Global Store)

![React](https://img.shields.io/badge/React-UI-2ea44f)
![TypeScript](https://img.shields.io/badge/TypeScript-Typed%20State-3178c6)
![State](https://img.shields.io/badge/State-Global%20Store-6f42c1)
![Provenance](https://img.shields.io/badge/Provenance-First-ff7a18)

Welcome to the **state layer** for the Kansas Frontier Matrix (KFM) web UI ✅  
This folder exists so **disparate UI components stay in sync** (map ↔ timeline ↔ story ↔ charts ↔ Focus Mode).  
Example: when the user selects a new year on the timeline, the store updates `currentYear` and both the map and story panel react to it.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ✨ What this folder is responsible for

### ✅ Owns
- **App-wide UI state** that multiple components rely on:
  - 🗺️ Map view state (2D MapLibre / 3D Cesium toggle, active layers, params like year)
  - 🕰️ Timeline state (`currentYear`, playback/animation, range filters)
  - 📖 Story / scrollytelling state (active story/section, “mapState” choreography, narrative sync)
  - 🤖 Focus Mode state (conversation turns, citations, selected context like time/place)
- **Predictable updates** (actions → reducers → selectors/hooks) suitable for debugging and auditing (design docs lean toward Redux for scale/time‑travel style debugging). [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ❌ Does *not* own
- Component-local UI details (hover states, a single input field value, etc.)
- Direct DB access or filesystem access (**never** from UI)
- Hidden “magic” side effects in reducers

> 🔒 KFM principle: the **UI communicates exclusively through the backend API** (REST/GraphQL) and **never directly touches databases** — this is essential for governance and consistency.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 Mental model

```mermaid
flowchart LR
  U[🧑 User action] --> A[🎬 Dispatch action]
  A --> R[🧩 Reducer updates store]
  R --> S[🔎 Selectors / hooks]
  S --> V[🖥️ UI re-renders]
  V -->|if needed| E[🌐 API call (thunk/service)]
  E --> A2[🎬 Dispatch success/failure]
  A2 --> R
```

This matches the “keep components in sync” goal described in the KFM blueprint (timeline year → map filter + story highlight). [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🗂️ Suggested layout (guiding pattern)

> 📌 The exact filenames may differ, but the *roles* below should exist.

```text
📦 web/src/state/
├─ 🧠 store.ts                # store setup (middleware/devtools)
├─ 🧩 slices/                 # domain reducers (map/timeline/story/focus/etc.)
│  ├─ 🗺️ mapSlice.ts
│  ├─ 🕰️ timelineSlice.ts
│  ├─ 📖 storySlice.ts
│  ├─ 🤖 focusModeSlice.ts
│  └─ 🧰 uiSlice.ts
├─ 🔎 selectors/              # derived/memoized selectors
├─ 🧱 types.ts                # shared state types/interfaces
├─ 💾 persistence/            # localStorage/session persistence (prefs)
└─ 🧪 __tests__/              # reducer/selector tests
```

---

## 🧩 Core state domains (recommended)

### 🗺️ Map domain
KFM’s UI is map-centric and uses **MapLibre GL JS (2D)** and **CesiumJS (3D)** with a UI toggle between modes.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Store should typically track:
- `map.mode`: `"2d" | "3d"`
- `map.view`: `{ center, zoom, bearing, pitch }`
- `map.layers.active`: list of visible layers
- `map.layers.params`: per-layer params (example: year/opacity)
- `map.selection`: selected feature(s) by **ID**, not entire geometry blobs
- `map.draw`: drawn bbox/polygon (if enabling spatial queries)

> 🧠 Tip: keep **MapLibre/Cesium instances out of global state** (store only serializable view + flags).  
> This keeps time-travel debugging clean and prevents non-serializable state from leaking everywhere.

---

### 🕰️ Timeline domain
The blueprint explicitly calls out a timeline driving map filtering and narrative syncing (e.g., `currentYear`). [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Store should track:
- `timeline.currentYear`
- `timeline.range` (min/max)
- `timeline.playback`: `{ playing, speed }`
- `timeline.snap`: snapping rules (year/decade/event)

---

### 📖 Story domain (scrollytelling)
Stories can include a **JSON script** that maps narrative sections to **map actions** (center/zoom/layers/annotations + timeline year). The UI reads this JSON and triggers map changes as the user scrolls.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Store should track:
- `story.activeStoryId`
- `story.activeSectionId`
- `story.progress` (scroll position / section index)
- `story.script.mapState` (or computed “next map state”)
- `story.lockMap` (optional: when story drives map vs user drives map)

---

### 🤖 Focus Mode domain
Focus Mode is **strictly layered**: the UI **does not call the LLM directly**; it calls backend endpoints (e.g., `/focus-mode/query`) and the API layer orchestrates retrieval and model calls.  [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

Store should track:
- `focus.sessionId`
- `focus.messages[]` (user/assistant turns)
- `focus.streaming`: `{ active, partialText }`
- `focus.context`: `{ place?, time?, layers?, selection? }`
- `focus.citations[]` (normalized reference objects)

> 🔗 Evidence-first is a hard requirement: answers include citation markers and the UI renders them as clickable footnotes.  [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

### 🧰 UI shell domain
Examples:
- Left/right panels open/closed
- Active tool (inspect / draw / measure / annotate)
- Toasts / alerts
- Theme / accessibility mode

---

## 🌐 State ↔ API contract (don’t skip this)

KFM exposes API endpoints for:
- dataset metadata & catalog search
- constrained ad-hoc querying
- map tiles (`/tiles/{layer}/{z}/{x}/{y}.pbf` / raster variants)  
…and clients like MapLibre consume those tile URLs.  [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### ✅ Pattern to follow
- State stores **IDs + parameters**
- API/data layer fetches the real payload
- Reducers only update “what the UI needs”

### 🚫 Anti-pattern
- “Reducer calls `fetch()`”
- “Component bypasses API and loads data directly”
- “State stores raw megabytes of GeoJSON when tiles exist”

---

## 🧾 Provenance & governance in state (KFM flavor)

When you add *anything* that changes what the user can see (layers, story sections, selected entities), make sure the UI can still “show its work”:

- **Every map layer should link back to provenance/metadata** (DCAT/STAC) and display citations in the UI.  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- For user-interaction features (highlighting a location, selecting a feature), ensure **CARE** compliance (example given: hide precise coordinates if sensitive).  [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Testing expectations

- Reducers should be unit-testable (pure, deterministic)
- Selectors should be tested for derived correctness
- Story “mapState choreography” should be regression-tested (section → expected map view/layers/year)  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🛠️ “How do I add new state?” (fast checklist)

1. 🧱 Define types and initial state (keep it serializable)
2. 🧩 Add/extend the domain slice (map/timeline/story/focus/ui)
3. 🎬 Create actions that describe *user intent* (not implementation)
4. 🔎 Add selectors (prefer memoized derived reads)
5. 🔌 Wire UI via hooks/context
6. 🧪 Add tests for reducers/selectors
7. 🧾 Confirm provenance + citation UX if this affects displayed facts/layers  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🚦Quick “Do / Don’t” rules

### ✅ Do
- Keep shared state **small** and **serializable**
- Store references by **ID**, not whole blobs
- Use global state for cross-component coordination (timeline ↔ map ↔ story) [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Keep Focus Mode UI layered: UI → API → retrieval/LLM [oai_citation:15‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### ❌ Don’t
- Put MapLibre/Cesium instance objects in the store
- Make reducers async
- Skip provenance/citation wiring for new layers/features [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📚 Sources (design grounding)
- Global store keeps map/timeline/story in sync; Redux suggested for scale/time-travel patterns. [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Frontend stack: React/TypeScript + MapLibre (2D) + Cesium (3D), timeline, scrollytelling, global store, API-only access from UI. [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Story JSON scripts can drive section → mapState + timeline changes (“scrollytelling choreography”). [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Focus Mode UI is decoupled from model calls; it calls backend endpoints that orchestrate retrieval + generation. [oai_citation:20‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- API provides dataset/catalog endpoints and map tile endpoints consumable by map clients. [oai_citation:21‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Evidence-first: citations in responses and UI renders them as clickable footnotes. [oai_citation:22‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- UI changes/layers must tie back to provenance and respect CARE constraints (e.g., coordinate redaction if sensitive). [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)