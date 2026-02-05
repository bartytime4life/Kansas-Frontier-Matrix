# 🪝 `hooks/utils` — Shared Hook Utilities

> **Location:** `web/src/hooks/utils/`  
> **Purpose:** Small, reusable React hooks that are **domain-agnostic**, **safe**, and **boring** (in the best way) 😄

---

## 🎯 Why this folder exists

KFM’s web UI is map-heavy, data-driven, and governance-constrained. Utility hooks exist to:

- ✅ Reduce copy/paste patterns (abort controllers, event listeners, debouncing, stable callbacks, etc.)
- ✅ Prevent subtle React bugs (stale closures, missing cleanups, “setState on unmounted component”)
- ✅ Improve performance *by default* (avoid render storms during map/timeline interaction ⚡)
- ✅ Make it easier to keep KFM’s **pipeline + governance invariants** intact (see below 🧭)

---

## 🧭 KFM invariants utility hooks must not violate

Even “generic” hooks can accidentally bypass governance if they turn into a shadow data layer.

### ✅ Non-negotiables
- **API boundary stays sacred:** utility hooks must not embed “direct datastore” assumptions (Neo4j/PostGIS), and should remain API-consumer friendly.  
- **Provenance-first UX:** hooks that help display derived content must support provenance/metadata surfacing patterns (e.g., returning “displayable state” that can include source/lineage references).
- **Sovereignty + sensitivity safety:** hooks that affect map interactions should support location generalization/redaction workflows (don’t make it easier to leak precise coordinates).

> 🧠 Rule of thumb:  
> If a hook “knows about Kansas” (datasets, entities, story nodes, tiles, Focus Mode semantics), it probably **does not** belong in `hooks/utils`.

---

## 🧩 What goes in `hooks/utils` vs elsewhere

| ✅ Put it in `hooks/utils` | ❌ Don’t put it in `hooks/utils` |
|---|---|
| Small hooks with **no domain meaning** | Hooks that implement **KFM business rules** |
| Hooks that wrap **browser behaviors** (events, storage, media queries) | Hooks that call a specific endpoint like `/graphql` or `/api/v1/...` |
| Hooks that enforce **React correctness** (stable refs, safe effects) | Hooks that “know” graph entities, Story Nodes, layer registries |
| Hooks that help performance (debounce/throttle/raf scheduling) | Hooks that decide what is “sensitive” or “publishable” content |

### Suggested nearby homes 🗂️
If your hook is not a util, consider patterns like:
- `web/src/hooks/data/…` (query orchestration)
- `web/src/hooks/map/…` (MapLibre/3D interactions)
- `web/src/hooks/focus-mode/…` (Focus Mode orchestration)
- `web/src/hooks/story/…` (Story Node reading experience)

*(Exact folders may vary — keep the boundary principle even if names change.)*

---

## 🧱 Conventions

### Naming
- Hooks: `useXxxYyy.ts`
- One hook per file (preferred)
- If there’s a barrel file (`index.ts`), export only stable/public hooks.

### TypeScript
- Prefer explicit generics for “reusable data hooks”
- Return a **stable shape** (avoid returning new objects/functions every render unless intended)
- Prefer `readonly` arrays/tuples when appropriate

### Cleanup & safety
- Always remove event listeners in cleanup
- Always abort async work on unmount when possible
- Never assume `window` exists (SSR-safe patterns), unless the `web/` app is explicitly client-only

---

## ✅ Hook author checklist

When adding or modifying a utility hook:

- [ ] **No domain knowledge** (no KFM entity IDs, no dataset semantics)
- [ ] Uses **React hooks correctly** (top-level calls, dependency arrays)
- [ ] Includes **cleanup** for effects (listeners, timers, subscriptions)
- [ ] Handles **unmount safety** (abort async work / guard state updates)
- [ ] Avoids **render storms** (memoize outputs; debounce/throttle where needed)
- [ ] Documented below in **Inventory** (keep this README honest 📌)
- [ ] Has tests if behavior is non-trivial (timers, listeners, async)

---

## 📦 Inventory (keep updated)

> ⚠️ This table is intentionally “living documentation.”  
> Add a row when you add a new hook (or remove a row when deleting one).

| Hook | What it does | Common use | Footguns 🧨 |
|---|---|---|---|
| `useMountedRef` *(example)* | Ref that tracks mounted/unmounted | Async safety | Forgetting to check before setState |
| `useDebouncedValue` *(example)* | Debounce fast-changing values | Map move/zoom, search inputs | Debounce delay too high → sluggish UX |
| `useStableCallback` / `useEvent` *(example)* | Stable function identity + latest closure | Event handlers, subscriptions | Misusing can hide dependency issues |
| `useInterval` *(example)* | Interval with proper cleanup | Polling UI state | Over-polling; missing pause conditions |
| `useLocalStorage` *(example)* | Persist state to localStorage | UI preferences | SSR + JSON parsing failures |

> 🧩 If you’re unsure whether a hook belongs here:  
> put it in a feature folder first — promote to `utils` only once it’s used in **2+** distinct domains.

---

## 🧪 Recommended patterns (templates)

<details>
<summary><strong>🧷 Pattern: stable callback (avoid stale closures)</strong></summary>

```ts
import { useCallback, useRef } from "react";

/**
 * Keeps a stable function identity while always calling the latest implementation.
 * Great for event listeners + subscriptions.
 */
export function useStableCallback<TArgs extends unknown[], TResult>(
  fn: (...args: TArgs) => TResult
) {
  const ref = useRef(fn);
  ref.current = fn;

  return useCallback((...args: TArgs) => ref.current(...args), []);
}
```
</details>

<details>
<summary><strong>🧯 Pattern: abortable async effect</strong></summary>

```ts
import { useEffect } from "react";

export function useAbortableEffect(
  effect: (signal: AbortSignal) => void | (() => void),
  deps: readonly unknown[]
) {
  useEffect(() => {
    const controller = new AbortController();
    const cleanup = effect(controller.signal);

    return () => {
      controller.abort();
      if (typeof cleanup === "function") cleanup();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
}
```

✅ Helps prevent “setState after unmount” and cancels in-flight fetches.
</details>

<details>
<summary><strong>⏱️ Pattern: debounced value</strong></summary>

```ts
import { useEffect, useState } from "react";

export function useDebouncedValue<T>(value: T, delayMs: number) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const id = window.setTimeout(() => setDebounced(value), delayMs);
    return () => window.clearTimeout(id);
  }, [value, delayMs]);

  return debounced;
}
```

✅ Useful for map/timeline inputs and search boxes  
🧠 If SSR matters, guard access to `window`.
</details>

---

## ⚡ Performance notes for KFM’s UI

The KFM UI can receive **high-frequency signals** (map moves, hover events, timeline dragging). Utility hooks should help ensure:

- **Work is batched** (debounce/throttle/`requestAnimationFrame`)
- **Subscriptions don’t leak** (listeners cleaned up)
- **Derived values are memoized** (avoid recomputing geometry/transforms on every render)
- **State updates are intentional** (don’t set state on every pixel change)

> 🗺️ Map UX tip: prefer **debounced state** for data fetching, but **immediate state** for visual feedback (cursor, hover).

---

## 🔐 Safety notes (so we don’t accidentally create side-channels)

Utility hooks can unintentionally expose sensitive information if they:
- Serialize raw coordinates into URLs or storage
- Log raw responses/errors containing restricted details
- Encourage “quick hacks” like dumping entire objects into UI state

**Guideline:** prefer returning *minimal, display-safe shapes* and keep raw payload handling in governed layers.

---

## 🔗 Quick links (relative)

- 🏠 Project root: `../../../../README.md`
- 🧱 Server API docs: `../../../../src/server/api/README.md`
- 📚 Standards & governance: `../../../../docs/`
- 🗺️ Web app entry (if present): `../../README.md`

---

## 🧼 Maintenance

- Keep this README aligned with actual exports
- Promote hooks into `utils` only when they’re **truly general**
- Treat this folder as a **stability surface**: refactors should be cautious and well-tested 🧪

---