# 📖 Story Components (Story Nodes + Scrollytelling)

![KFM](https://img.shields.io/badge/KFM-Interactive%20Documentary-4c1?style=flat-square)
![React](https://img.shields.io/badge/React-UI-61dafb?style=flat-square&logo=react&logoColor=000)
![TypeScript](https://img.shields.io/badge/TypeScript-typed-3178c6?style=flat-square&logo=typescript&logoColor=fff)
![Redux](https://img.shields.io/badge/State-Redux%20%2F%20Context-764abc?style=flat-square&logo=redux&logoColor=fff)
![Map](https://img.shields.io/badge/Map-MapLibre%20%2B%20Cesium-2ea44f?style=flat-square)
![UX](https://img.shields.io/badge/UX-Scroll--Linked%20Storytelling-orange?style=flat-square)

> 🧭 This folder powers KFM’s **Story Node viewer**: narrative content that **drives map + timeline state** for a “scrollytelling” / “interactive documentary” experience.

---

## ✨ What lives here

**Path:** `web/src/components/story/`

This directory contains the UI building blocks that:

- 📝 Render story content (usually Markdown → HTML)
- 🧷 Bind story “beats” (sections/segments) to **map state** (viewport, camera, layers)
- ⏱️ Bind story “beats” to **timeline state** (year / time range)
- 🔖 Surface **citations + media** (evidence-first storytelling)
- ♿ Keep the experience accessible, keyboard-friendly, and performant

> ⚠️ **Contract-first reminder:** the UI should treat stories as *content + contracts*, not ad-hoc blobs.

---

## 🧠 Core concepts (quick glossary)

- **Story Node**: a governed narrative unit that includes metadata + time/map context + citations/media.
- **Story Segment**: a chapter/section/paragraph that can trigger a map/timeline update.
- **Trigger**: the “binding” between narrative and visualization (year changes, layer toggles, fly-to, etc.).
- **Global Store**: shared state (Redux/Context) that keeps map, timeline, story, and charts synchronized.

---

## 🗂️ Where story content lives (repo-wide)

This UI folder is **not** the canonical home for narrative content. Story files live under the governed docs structure:

- 📚 `docs/reports/story_nodes/`
  - 🧪 `draft/` (work-in-progress)
  - ✅ `published/` (released, curated)
- 🧾 Template for authors: `docs/templates/TEMPLATE__STORY_NODE_V3.md`

> ✅ Keep the boundary clean: **content in `docs/…`** ➜ **API** ➜ **UI in `web/…`**.

---

## 🔁 Data flow (how Story drives Map + Timeline)

```mermaid
flowchart LR
  A[📚 Story Content<br/>docs/reports/story_nodes/] -->|published via API| B[🌐 API<br/>/api/v1/story + /graphql]
  B --> C[🧩 StoryPanel / Story Viewer]
  C -->|dispatch trigger| D[(🧠 Global Store)]
  D --> E[🗺️ MapViewer<br/>(MapLibre / Cesium)]
  D --> F[⏱️ TimelineSlider]
  D --> G[📊 Charts / Panels]
  C --> H[🔖 Citations + Media UI]
```

**Key idea:** Story components **do not** talk to databases or filesystem directly. They **consume API responses** and dispatch store updates.

---

## 🧩 Suggested component boundaries

> Your exact filenames may vary — this is the recommended mental model for keeping Story logic tidy ✅

- **`StoryPanel`**: container that loads a story, renders content, owns navigation + scroll-linking.
- **`StoryScroller`**: scroll-linked “observer” layer (Intersection Observer).
- **`StoryNav`**: Next/Prev, chapter list, progress indicator.
- **`StoryCitations`**: renders evidence links, dataset refs, provenance blocks.
- **`story.types`**: TypeScript types mirroring the Story Node contract.
- **`story.triggers`**: pure functions that turn “trigger data” into store actions.
- **`story.utils`**: parsing helpers, slug/id helpers, etc.

---

## 🌐 Backend contract touchpoints (UI expectations)

### REST (Story Nodes)
Typical interactions include:
- `GET /api/v1/story/:id` — fetch a story
- `GET /api/v1/story?...` — search/filter by bbox/time/tags
- `POST /api/v1/story` — create (contributors/auth required)

Your UI should assume a story payload can include:
- 🏷️ title + tags
- ⏳ time range
- 🗺️ map center / camera settings
- 🧱 layer list
- 🔖 citations
- 🖼️ media (images/audio/video embeds)

### GraphQL (Story Nodes)
GraphQL can be used when you want story nodes *in relationship context* (e.g., stories connected to datasets/places/events).

---

## 🧷 Scroll-linked storytelling (Intersection Observer)

KFM’s scrollytelling pattern can work like modern long-form web journalism:

- The story is a continuous page
- Certain “trigger points” update the map/timeline automatically as you scroll
- Triggers can be represented as:
  - hidden sentinel elements inside rendered HTML, **or**
  - segment metadata in story JSON

### Minimal trigger markup idea
```html
<div class="story-trigger"
     data-year="1934"
     data-map="drought_layer"></div>
```

### Recommended observer behavior
- ✅ Use `IntersectionObserver` with a **sane threshold** (ex: 0.5) so triggers fire when a segment is meaningfully in view
- ✅ Debounce/throttle expensive map transitions (fly-to, heavy layer toggles)
- ✅ Respect `prefers-reduced-motion` (avoid aggressive camera animations)

---

## 🧠 Store integration pattern (sync across the app)

The story system works best when **story triggers dispatch actions** and other systems react:

- `timeline/setCurrentYear(1934)`
- `map/setViewport({ center, zoom, pitch, bearing })`
- `layers/setActiveLayers([...])`
- `story/setActiveSegment(segmentId)`

**Why:** It ensures that map, timeline, story highlight, and any charts stay consistent.

---

## ♿ Accessibility & UX guardrails

- ⌨️ **Keyboard navigation**: Next/Prev controls must be reachable and obvious.
- 🧭 **Focus management**: when navigating segments, move focus to the heading (or a logical landmark).
- 🧑‍🦯 **Reduced motion**: if user requests reduced motion, prefer instant changes (or minimal pans).
- 🏷️ **Readable hierarchy**: headings, chapter markers, and citations should be scannable.

---

## ⚡ Performance notes (maps are heavy)

Map transitions can be expensive — scrollytelling is “easy to make cool” and “easy to make janky.”

Do:
- ✅ throttle rapid-fire triggers (scroll can generate lots of events)
- ✅ ignore repeated triggers for the same active segment
- ✅ lazy-load media (images/audio) per segment
- ✅ batch updates: set year + layers + viewport in a single “transaction” if your store supports it

Avoid:
- ❌ flying the camera on every small scroll movement
- ❌ toggling large raster layers repeatedly during fast scrolling

---

## 🧪 Testing checklist

A healthy Story component test suite usually covers:

- ✅ Parsing: triggers extracted from story content / metadata
- ✅ Trigger → action mapping: correct store actions dispatched for a segment
- ✅ Navigation: Next/Prev updates active segment + scroll position
- ✅ “No double-fire”: same segment doesn’t spam the store on minor scroll changes
- ✅ Reduced motion: respects user preferences
- ✅ Citations rendering: links + labels show correctly

---

## 🧯 Troubleshooting

**Map doesn’t update when I scroll**
- Check that triggers exist in the rendered DOM (or segment metadata).
- Ensure observer thresholds aren’t too strict (e.g., `threshold: 1` can be hard to hit).
- Confirm your trigger handler dispatches store actions and MapViewer subscribes correctly.

**Timeline moves but story highlight doesn’t**
- Story highlight usually depends on `story.activeSegmentId` and/or `timeline.currentYear`.
- Confirm you update both (or define a single source of truth).

**Layers don’t appear**
- Verify layer IDs in story payload match the backend’s published layer IDs.
- Confirm layer toggles go through the global layer manager (not direct MapLibre calls).

---

## 🛣️ Roadmap hooks (future-friendly)

- 🛰️ **3D flyover story mode** (Cesium camera waypoints + “Play Tour”)
- 🧰 **Authoring preview mode**: calibrate trigger points visually
- 🧾 **Provenance UI upgrades**: “why am I seeing this” + versioned story citations
- 📱 **Mobile fallback**: click-through steps if scroll linking feels cramped

---

## 🤝 Contributing (UI side)

When adding/adjusting Story UI behavior:

1. ✅ Keep logic **pure & testable** (trigger parsing + trigger-to-action mapping)
2. ✅ Keep map/timeline changes **store-driven**
3. ✅ Don’t hardcode content paths — UI consumes **API outputs**
4. ✅ Prefer small, composable components (StoryPanel + Scroller + Nav + Citations)
5. ✅ Update this README if you introduce a new pattern 🎯

---

### 📌 Quick links (repo-relative)
- 📚 Story content: `../../../../docs/reports/story_nodes/`
- 🧾 Story node template: `../../../../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- 🧠 Architecture / contracts: `../../../../docs/architecture/`
- 🌐 API docs (if present): `../../../../src/server/api/`
- 🧬 Schemas (Story Node schema should live here): `../../../../schemas/`

---