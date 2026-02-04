# 🪝 `web/src/hooks` — React Hooks for Kansas Frontier Matrix (KFM)

> **Goal:** keep UI components *clean, declarative, and evidence-first* by moving reusable logic (API calls, map lifecycle, timeline/story state, Focus Mode chat) into composable hooks.

---

## ✨ Design Philosophy (KFM-first)

KFM is built around a strict **“truth path”**: UI ➜ API ➜ governed stores (PostGIS/Neo4j/search) ➜ results.  
That means hooks in this folder should **never** “shortcut” governance by directly reaching into backends or model services.

### ✅ What that means for hooks
- 🌐 **UI talks to the API, not databases** (no direct PostGIS/Neo4j calls from the web layer).
- 🤖 **Focus Mode hooks call backend endpoints** (e.g. `/focus-mode/query`) — **the UI must not call the model runtime directly**.
- 🧾 **Evidence-first UX**: hooks that fetch analysis/answers should return enough metadata to render provenance/citations cleanly.
- 🛡️ **Fail closed mindset**: if policy denies, missing evidence, or auth fails, hooks should surface *safe* errors and avoid partial “guesses”.

<details>
<summary>📌 Why so strict?</summary>

KFM’s system design emphasizes provenance, policy gates, and auditable outputs. Hooks are a key place where accidental “side doors” can appear (direct fetches to internal services, bypassing auth headers, etc.). Keeping hooks aligned with the layered architecture makes the UI trustworthy and maintainable.

</details>

---

## 🧭 Hook Categories (recommended organization)

> The exact folders/files may evolve — **keep related hooks near each other** and avoid giant “misc” piles.

```text
web/src/hooks/
├── 🌐 api/              # data fetching hooks (REST/GraphQL)
├── 🗺️ map/              # MapLibre/Cesium lifecycle + layer helpers
├── 🕰️ timeline/         # year/time-range state + syncing
├── 📖 story/            # story nodes, narrative state
├── 🤖 focus-mode/       # AI assistant UX (question/answer + citations)
├── 🔐 auth/             # auth status, roles, capabilities, policy-aware UX
└── 🧰 utils/            # small reusable hooks (debounce, localStorage, etc.)
```

---

## 📏 Conventions & Standards

### 1) Naming ✅
- **Hook names must start with `use`**: `useFocusModeQuery`, `useTimelineYear`, `useMapLibreMap`
- File names should match hook names: `useFocusModeQuery.ts`

### 2) Export pattern ✅
Prefer **named exports** for hooks (easy refactors and grep):
```ts
export function useSomething() { /* ... */ }
```

Optional: maintain a small barrel export:
```ts
// web/src/hooks/index.ts
export * from "./focus-mode/useFocusModeQuery";
```

### 3) Return shape (be predictable) ✅
For async hooks, standardize on:
```ts
{
  data,
  error,
  isLoading,
  isSuccess,
  refetch,
}
```

### 4) Side effects & cleanup 🧹
If your hook creates **subscriptions, listeners, map instances, timers, or fetches**, it must:
- clean up on unmount
- cancel stale requests (AbortController)
- avoid infinite rerenders (stable deps)

---

## 🧠 Rules of Hooks (don’t fight React)

- 🚫 Don’t call hooks conditionally
- 🚫 Don’t call hooks inside loops
- ✅ Call hooks at the top-level of the hook/component
- ✅ Keep effects dependency arrays accurate

> If you need conditional behavior, keep the hook call unconditional and branch *inside* the hook logic.

---

## 🌐 API Hooks (KFM contract)

### Golden rule
**All network access should flow through the backend API layer.**  
Hooks should not “invent” alternate routes to data.

### Recommended structure
- A single API client wrapper (e.g., `web/src/services/api.ts`)
- Hooks call that wrapper and return clean state

#### ✅ Example: minimal fetch hook template
```ts
import { useEffect, useMemo, useState } from "react";

type AsyncState<T> = {
  data: T | null;
  error: Error | null;
  isLoading: boolean;
};

export function useApiGet<T>(url: string | null, deps: unknown[] = []): AsyncState<T> {
  const [state, setState] = useState<AsyncState<T>>({
    data: null,
    error: null,
    isLoading: Boolean(url),
  });

  const stableDeps = useMemo(() => deps, deps); // optional: keep deps stable if you really need it

  useEffect(() => {
    if (!url) return;

    const controller = new AbortController();
    setState(s => ({ ...s, isLoading: true, error: null }));

    fetch(url, { signal: controller.signal })
      .then(async r => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return (await r.json()) as T;
      })
      .then(data => setState({ data, error: null, isLoading: false }))
      .catch(err => {
        if (controller.signal.aborted) return;
        setState({ data: null, error: err, isLoading: false });
      });

    return () => controller.abort();
  }, [url, stableDeps]);

  return state;
}
```

---

## 🤖 Focus Mode Hooks (AI, but governed)

Focus Mode is designed so the **UI calls the backend**, and the backend orchestrates retrieval + generation + policy checks.  
Your hook should treat the backend response as *the source of truth*.

### Recommended hook responsibilities
- 🧾 Return:
  - `answerText`
  - `citations[]` (structured, so UI can render clickable provenance)
  - `policyStatus` / `blockedReason` when applicable
- 🧭 Accept:
  - `question`
  - optional “map context” (bbox, selected place, active layers, current year)
- 🧯 Handle:
  - policy denial
  - missing evidence (“No source, no answer” UX)
  - network cancellation and retries

#### ✅ Example response shape (suggested)
```ts
export type FocusCitation = {
  id: string;           // stable ID (dataset/doc/node)
  title: string;        // human label
  kind: "dataset" | "document" | "story" | "graph-node";
  url?: string;         // optional (prefer relative)
};

export type FocusModeResult = {
  answer: string;
  citations: FocusCitation[];
  blocked?: { reason: string };
};
```

#### ✅ Example hook signature (suggested)
```ts
export function useFocusModeQuery() {
  // returns: query(question, context) + state
}
```

---

## 🗺️ Map Hooks (MapLibre + Cesium lifecycle)

KFM’s front-end is map-centric: MapLibre (2D) and Cesium (3D). Hooks here should:
- initialize map/viewer exactly once
- expose imperative handles safely
- sync with global state (year/layers/selection)
- clean up **every** time (maps leak memory fast)

### Recommended patterns
- `useRef` for map instances
- `useEffect` for initialization and teardown
- Separate hooks:
  - `useMapLibreMap(containerRef, options)`
  - `useCesiumViewer(containerRef, options)`
  - `useMapLayers(map, activeLayers)`
  - `useMapSelection(map, selectedFeatureId)`

---

## 🕰️ Timeline + Story Hooks (sync across panels)

The UI commonly needs synchronized state:
- the timeline changes the year
- the map filters layers
- the story panel highlights narrative sections

Hooks should help components stay consistent:
- `useCurrentYear()`
- `useTimeRange()`
- `useActiveStory()`
- `useSelectedPlace()`

> If the project uses a global store (Redux/Zustand/etc.), hooks here should be thin wrappers (`useAppSelector`, `useAppDispatch`, `useCurrentYearSelector`).

---

## 🔐 Auth & Policy-Aware Hooks

KFM uses role-based access control + policy enforcement. The web UI should:
- detect auth state
- respond gracefully to 401/403
- hide or disable restricted UI affordances

Recommended hooks:
- `useAuthStatus()`
- `useUserRole()`
- `useCapabilities()` (derived from role + server hints)
- `usePolicyAwareFetch()` (optional wrapper)

---

## 🧰 Utility Hooks (small, reusable, boring = good)

Examples:
- `useDebounce(value, ms)`
- `useLocalStorage(key, initial)`
- `useEventListener(target, type, handler)`
- `usePrevious(value)`

> Keep these dependency-free and well-tested.

---

## 🧪 Testing Hooks

### Recommended toolkit
- ✅ `renderHook` (React Testing Library)
- ✅ MSW (mock fetch) for API hooks
- ✅ fake timers for debounce/interval hooks

### Testing checklist
- [ ] handles initial loading state correctly
- [ ] cancels on unmount (AbortController)
- [ ] does not update state after unmount
- [ ] handles 401/403 with clear error surfaces
- [ ] stable output shape (no surprise `undefined`s)

---

## ✅ “Add a New Hook” Checklist

- [ ] Hook name starts with `use`
- [ ] Has clear input/output types (TypeScript)
- [ ] Cleanup implemented (listeners, maps, timers, fetch)
- [ ] Doesn’t bypass API governance boundaries
- [ ] Returns structured data (esp. citations/provenance)
- [ ] Includes a usage example in JSDoc (or in this README if core)
- [ ] Has at least one test if non-trivial

---

## 📚 Project References (design grounding)

> These are the KFM project sources that inform the expectations of hooks in this folder:

- 🧭 KFM system architecture & AI integration notes:  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- 🛡️ Governance / policy-first posture:  [oai_citation:1‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- 🧩 Front-end patterns & React hooks reference material:  [oai_citation:2‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- 🧱 Additional project technical context:  [oai_citation:3‡ssoar-2022-zipp-Programming_Creativity_Semantics_and_Organisation.pdf](sediment://file_00000000cda071fdb35a0ccdeff2271c)  

---

## 🧯 Common Gotchas (save yourself hours)

- 🔁 **Infinite effects**: state updates inside `useEffect` + missing deps = render loops
- 🧊 **Stale closures**: callbacks capturing old state — prefer functional updates or stable refs
- ❌ **No cancellation**: stale fetch completes after route change and clobbers state
- 🗺️ **Map leaks**: missing `map.remove()` / viewer destroy on unmount = creeping memory use
- 🧾 **Unrenderable citations**: returning “raw strings” instead of structured provenance makes UI brittle

---

### 🏁 TL;DR
If components are the *storytellers*, hooks are the *field researchers* — collecting governed facts, keeping the map alive, and ensuring every “answer” is traceable. 🧭🗺️🧾
