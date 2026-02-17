# Map state

![scope](https://img.shields.io/badge/scope-map%20UI%20state-blue)
![ui](https://img.shields.io/badge/ui-React%20%2B%20TypeScript-3178C6)
![map](https://img.shields.io/badge/map-MapLibre-2E7D32)
![governance](https://img.shields.io/badge/governance-trust%20membrane%20%2B%20policy-6A1B9A)

This folder defines the **map-centric UI state contract** for the KFM web application.

It exists so that the following parts of the UI stay in sync via a **single source of truth**:

- **MapViewer** (MapLibre scene + camera)
- **TimelineSlider** (selected time / year)
- **StoryPanel** (current Story Node / scroll-linked narrative)
- **LayerControl** (active layer toggles + per-layer presentation)

---

## Non-negotiables

> 🧭 **Single source of truth**
>  
> One global store drives the map experience (viewport, selected time, active layers, current story focus).  
> Components read via selectors/hooks and update via actions/events.

> 🧱 **Trust membrane**
>  
> This folder must never directly access databases, object storage, or LLMs.  
> Data access happens through **governed API clients** (policy boundary), and this module only supplies
> *UI state* + *context* for those requests.

> 🧊 **Serializable state only**
>  
> Do **not** store live objects in the global store (e.g., MapLibre `Map`, `Popup`, `Marker`, DOM nodes).
> Keep those in component refs. Store only JSON-serializable primitives and small objects.

> ⚡ **Performance-aware**
>  
> Do not put large GeoJSON blobs or feature arrays in state. Store **IDs/refs** and keep geometry in tiles
> (preferred) or local component caches when needed.

> 🧾 **Governance-aware**
>  
> State should not become a bypass for sensitivity controls. If something is restricted, the backend will
> enforce it; the UI must handle “redacted/withheld/403” outcomes gracefully.

---

## Folder layout

> Update this section if your implementation differs (this is the *intended* thin-slice layout).

```text
web/src/components/map/state/
  README.md

  index.ts                    # public exports for this folder

  mapState.types.ts           # MapState + small value objects
  mapState.initial.ts         # initial state (defaults)
  mapState.selectors.ts       # selectors + derived state
  mapState.events.ts          # action/event names + payload typing (optional)

  mapState.slice.ts           # Redux Toolkit slice (if Redux)
  mapState.store.ts           # Context/Zustand-style store (if not Redux)
  mapState.thunks.ts          # async actions for API calls (optional)

  __tests__/
    mapState.selectors.test.ts
    mapState.reducer.test.ts
```

---

## State model

The table below is a **recommended** decomposition. It’s fine to merge/split slices as long as the
non‑negotiables above remain true.

| Slice | Example fields | Durable? | Who uses it | Notes |
|---|---|---:|---|---|
| `viewport` | `center`, `zoom`, `bearing`, `pitch`, `bounds` | ✅ | MapViewer, permalinks, Focus Mode context | Update at `moveend` (or throttled), not every frame. |
| `time` | `currentYear`, `range`, `mode` | ✅ | TimelineSlider, MapViewer filters, StoryPanel highlight | Prefer a single canonical `currentYear` for sync. |
| `layers` | `activeLayerIds`, `opacityById`, `basemapStyleId` | ✅ | LayerControl, MapViewer registry | Store IDs, not layer definitions. |
| `story` | `storyId`, `nodeId`, `stepIndex`, `scrollAnchor` | ✅ | StoryPanel, MapViewer (story framing) | Enables scroll linking + deep links. |
| `selection` | `selectedFeatureRef`, `selectedDatasetId` | ✅ | Map popups, Focus Mode context | Store refs (IDs), not full feature objects. |
| `interaction` | `hoverFeatureRef`, `isDragging`, `pointerLngLat` | ❌ | Map hover UI | Ephemeral → avoid global re-renders when possible. |
| `loading` | `sourceReadyById`, `mapIsIdle`, `lastError` | ❌ | Transition logic, UI spinners | Prefer derived “ready” selectors. |
| `transitions` | `transitionStyleId`, `targetStyleId`, `phase` | ❌ | Story node navigation | Drives “never show blank map” behavior. |

---

## Durable vs ephemeral state

This project distinguishes two broad classes of state:

- **Durable (sync/share-worthy):** state that should survive refreshes or be encoded into URLs (permalinks)  
  Examples: `currentYear`, `activeLayerIds`, `viewport`, `currentStoryNodeId`, `selectedFeatureRef`.

- **Ephemeral (session-only):** state that is high-frequency or window/session specific  
  Examples: hover, drag flags, “source is loading”, in-progress transition phases.

> ✅ Rule of thumb: if it changes many times per second, it’s probably *ephemeral* and should not live in
> the global store (or should be throttled and/or scoped to a small sub-store).

---

## Data flow

```mermaid
flowchart LR
  UI[Timeline / Story nav / Layer toggles] -->|dispatch events| Store[Map state store]
  Store -->|selectors| Map[MapViewer (MapLibre)]
  Store -->|selectors| Story[StoryPanel]
  Store -->|selectors| Layers[LayerControl]
  Map -->|map events (moveend, click)| Store
```

---

## Focus Mode context builder

The map state is also used to build **context** for governed API calls (example: Focus Mode).

### Recommended contract shape

```json
{
  "question": "How did this event affect Kansas farmers?",
  "context": {
    "area": "Kansas",
    "year": 1935,
    "activeLayers": ["kfm.layer.dust_bowl_drought"],
    "viewport": { "center": [-98.0, 38.5], "zoom": 5.8 }
  }
}
```

### Implementation guidance

- Provide a selector like `selectFocusModeContext(state)` that returns **only** JSON-serializable data.
- Keep it **small** (IDs + scalar context), since this will go over the network on every question.
- Never include raw geometry unless explicitly required and policy-allowed.

---

## Story Node transitions

Two UI patterns are expected for Focus/Story navigation:

### 1) Instant Story transitions via low-quality style

On Story Node change:

1. Apply `transitionStyleId` immediately (lightweight / reduced symbol density).
2. Wait for a reliable “ready” signal (sources loaded + map idle + UI idle).
3. Swap to the full `styleId`.

**State requirements:**
- Track `{ transitionStyleId, targetStyleId, phase }`
- Preserve camera + `currentYear` + `activeLayerIds` across the swap

### 2) Progressive layer reveal

Instead of mounting/unmounting heavy layers, keep them mounted but initially transparent, then fade in
opacity when sources are ready.

**State requirements:**
- Track source readiness (or derive it from MapLibre events)
- Ensure rapid navigation cancels in-flight tweens (cleanup)

---

## Implementation profiles

<details>
<summary><strong>Redux Toolkit profile</strong> (typical for large global state)</summary>

```ts
// Example only — adapt to actual file names.

dispatch(mapActions.setCurrentYear(1935));
dispatch(mapActions.toggleLayer("kfm.layer.dust_bowl_drought"));
dispatch(mapActions.setViewport({ center, zoom }));

const year = useAppSelector(selectCurrentYear);
const activeLayers = useAppSelector(selectActiveLayerIds);
```

Recommended conventions:

- Keep reducers pure and payloads serializable.
- Put API side effects in thunks/services, not in reducers.
- Prefer selectors for derived state (memoize if needed).

</details>

<details>
<summary><strong>Context / “store hook” profile</strong> (small-to-medium state)</summary>

```ts
// Example only — adapt to actual implementation.

const year = useMapStore(s => s.time.currentYear);
const setYear = useMapStore(s => s.actions.setCurrentYear);

setYear(1935);
```

Recommended conventions:

- Keep state slices shallow to avoid broad re-renders.
- Provide stable action references (avoid re-creating functions on every render).
- Use selectors to minimize subscriptions.

</details>

---

## Performance guidance

- Prefer **tile-backed** layers for anything large (vector tiles / PMTiles / server tiles).  
- Store **IDs/refs**, not objects:
  - ✅ `selectedFeatureRef: { layerId, featureId }`
  - ❌ `selectedFeature: GeoJSON.Feature`
- Throttle or defer high-frequency updates:
  - viewport → update on `moveend` rather than on every `move`
- Treat derived values as computed:
  - `selectIsMapReady(state)` instead of storing multiple redundant booleans

---

## Testing expectations

Minimum coverage for changes in this folder:

- **Unit tests:** reducers (or store mutators) and selectors
- **Integration tests:** MapViewer ↔ store binding (moveend/click/selection)
- **E2E tests (Playwright):**
  - story navigation never shows a blank map
  - timeline change updates both map filters and story highlight
  - layer toggles persist through story style swaps

---

## Change checklist

- [ ] New state is serializable
- [ ] Types updated (`mapState.types.ts`)
- [ ] Defaults updated (`mapState.initial.ts`)
- [ ] Selectors updated and covered by tests
- [ ] Focus Mode context selector updated (if applicable)
- [ ] Story transition logic updated (if applicable)
- [ ] Documentation updated (this README + any relevant Story Node manifest docs)

---

## Design references

- *KFM web frontend blueprint:* global store contains viewport, selected time/year, active layers, and story-in-view.
- *KFM Focus Mode / Story patterns:* transition styles + progressive layer reveal.
- *KFM governance invariants:* trust membrane (UI → governed APIs only), cite-or-abstain, policy enforcement.