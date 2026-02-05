# 🧪 Dev State Inspector (KFM) — `web/src/components/dev/state`

![React](https://img.shields.io/badge/React-%E2%9A%9B%EF%B8%8F-000000?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-%F0%9F%94%B7-000000?logo=typescript)
![State](https://img.shields.io/badge/State%20Debug-%F0%9F%A7%A0-000000)
![DevOnly](https://img.shields.io/badge/Dev%20Only-%F0%9F%94%92-000000)

A **developer-only** state explorer for the Kansas Frontier Matrix (KFM) web app.  
This panel exists to make debugging **map ↔ timeline ↔ story ↔ Focus Mode** synchronization *fast*, *repeatable*, and *safe*.

> ✅ **Design goal:** Show what the app *believes* is true right now (the store), not what we *hope* is true.  
> 🔒 **Safety goal:** Never leak sensitive/sovereign data while debugging.

---

## 📌 What this is

A small “inspector” UI that:

- 🧭 **Reads** the global app state (Redux/Context store)
- 🧩 **Organizes** it into human-friendly sections (Map, Timeline, Layers, Story, Focus Mode, API, Governance)
- 🧾 **Exports** a sanitized snapshot for bug reports (copy/download)
- 🧯 **Helps** detect state drift, race conditions, and broken invariants early

---

## 🚫 What this is NOT

- ❌ A production feature (should not ship in prod bundles)
- ❌ A backdoor into protected data
- ❌ A replacement for Redux DevTools (it complements it)
- ❌ A place to “fix state” by mutating it directly

> **Rule:** default behavior is **read-only** + **redacted**.

---

## 🗂️ Recommended folder layout (dev tooling)

```text
📁 web/
 └─ 📁 src/
    └─ 📁 components/
       └─ 📁 dev/
          └─ 📁 state/
             ├─ 📄 README.md  ✅ (you are here)
             ├─ 🧩 DevStatePanel.tsx
             ├─ 🧩 DevStateSection.tsx
             ├─ 🧰 adapters/
             │  ├─ reduxAdapter.ts
             │  └─ contextAdapter.ts
             ├─ 🧪 devState.redaction.test.ts
             └─ 🧪 DevStatePanel.test.tsx
```

If your filenames differ, that’s fine — the key idea is the **boundary**:  
**dev/state reads state, formats it, redacts it, and renders it.**

---

## 🧠 Core principles (KFM-aligned)

### 1) 🧱 Layering stays intact
The dev panel must not bypass the governed API boundary.

- ✅ It may display *request state* (last API call, status codes, payload sizes)
- ✅ It may show *IDs* for records (dataset IDs, node IDs) if allowed
- ❌ It must **not** query Neo4j/PostGIS directly from the browser
- ❌ It must **not** call the LLM service directly

### 2) 🔎 Provenance-first debugging
KFM operates with evidence-first + citation-aware flows. The state panel should make it easy to see:

- what user action happened
- what store changes resulted
- what sources (IDs) were involved
- what the UI is about to render (e.g., current filters)

### 3) 🔐 Sovereignty + classification propagation
Some data is restricted by design (e.g., precise sensitive locations). The panel must:

- default to redaction and generalization
- prevent “oops copy/paste leaks”
- allow opt-in sensitive viewing **only** via explicit dev flags (if ever)

---

## 🚀 Quickstart

### ✅ Mounting the panel (dev-only)

A common pattern is to mount it in `App.tsx` (or a DevToolbar) behind an environment flag.

```tsx
// App.tsx (example)
import { DevStatePanel } from "@/components/dev/state/DevStatePanel";

const DEV_STATE_ENABLED =
  (import.meta as any).env?.VITE_DEV_STATE === "1" ||
  (process.env as any).REACT_APP_DEV_STATE === "1" ||
  (process.env as any).NODE_ENV !== "production";

export function App() {
  return (
    <>
      {/* ...the actual app... */}
      {DEV_STATE_ENABLED ? <DevStatePanel /> : null}
    </>
  );
}
```

### 🧩 Suggested toggles

- `VITE_DEV_STATE=1` (Vite)
- `REACT_APP_DEV_STATE=1` (CRA)
- Optional: `?devState=1` query param override (handy for demos)

---

## 🧩 What the panel should show

Below is a “golden checklist” of sections that usually matter in KFM.

### 🗺️ Map
Show the minimum needed to debug rendering and interaction:

- viewport: `center`, `zoom`, `bearing`, `pitch`
- map mode: `2D | 3D`
- selected feature: `{id, layerId, propertiesPreview}`
- hovered feature: `{id, layerId}`
- active filters: bbox/time/topic filters (IDs, not full records)
- tile status: loading counts, last tile errors

✅ Debug questions this answers:
- “Why did the map jump?”
- “Why does a layer render at 1890 but not 1900?”
- “Why did clicking a feature select the wrong entity?”

---

### 🕰️ Timeline
- selected year / range
- playback state (playing, speed)
- snap settings (year stepping, clamp rules)
- current derived time window (if computed)

✅ Debug questions:
- “Why is story scroll not syncing to the year?”
- “Why does play mode skip years?”

---

### 🧅 Layers
- list of layers with:
  - enabled/disabled
  - opacity
  - styling preset
  - filter summary (IDs, tags, time)
- last style update timestamp (optional)

✅ Debug questions:
- “Why does toggling a layer do nothing?”
- “Why does opacity reset?”

---

### 📖 Story / Narrative
- active story ID / slug
- active section / anchor
- scroll-sync status (enabled, locked, driving component)
- selected citations (if story references sources)

✅ Debug questions:
- “Why does the story highlight the wrong section?”
- “Why does scroll jump when timeline changes?”

---

### 🔎 Search / Catalog
- query string
- applied search filters (time, bbox, tags)
- results summary (IDs only + counts)
- last request metadata (duration, status)

✅ Debug questions:
- “Why does search return empty?”
- “Why are results not updating after filter change?”

---

### 🤖 Focus Mode (AI Assistant UI)
Remember: UI stays decoupled from direct LLM calls.

Show:
- conversation/session ID
- message list metadata (role, length, timestamps)
- request state:
  - `idle | streaming | complete | error`
  - last backend endpoint called
- citation map summary:
  - citation tokens present
  - mapped record IDs available
- provenance/logging flags (if present)

✅ Debug questions:
- “Why did the answer get blocked?”
- “Why are citations present but not clickable?”
- “Why did the UI accept an answer without sources?” (it shouldn’t)

---

### 🔐 Governance / Safety
This section is key for KFM:

- classification tags present in UI state (`public|internal|sensitive|restricted`)
- redaction rules enabled (yes/no)
- coarse location mode enabled (yes/no)
- thresholds active (suppression rules for small counts)

✅ Debug questions:
- “Why is this point blurred/generalized?”
- “Why is this record hidden in the UI?”
- “Why is export missing fields?” (because it should be)

---

### 🌐 API / Network
- base URL
- last N calls summary:
  - endpoint
  - status
  - duration
  - payload size
- last error envelope (sanitized)

✅ Debug questions:
- “Is this a state bug or an API bug?”
- “Are we spamming the backend on every keystroke?”

---

## 🧼 Redaction & safe export

### ✅ Default rules
When exporting state snapshots:

- **Never export**
  - precise coordinates for sensitive layers
  - personal identifiers
  - any token/credential
  - raw documents/content blobs when not needed
- Prefer exporting:
  - **record IDs**
  - bounding boxes
  - aggregated stats
  - flags + derived values

### 🔒 Suggested implementation approach

Use a single redaction pipeline for:
- on-screen preview
- clipboard copy
- JSON download

```ts
// pseudo-code (shape intentionally generic)
export type RedactionRule = {
  path: string;            // dotpath or JSONPath-like selector
  mode: "mask" | "drop";   // how to handle it
  maskWith?: string;
};

export const DEFAULT_REDACTIONS: RedactionRule[] = [
  { path: "auth.token", mode: "drop" },
  { path: "focusMode.rawContext", mode: "drop" },
  { path: "map.selectedFeature.geometry.coordinates", mode: "mask", maskWith: "[REDACTED]" },
  { path: "governance.sensitive.*", mode: "drop" },
];
```

> 🔥 Treat “Copy state” as a potential data exfiltration vector. Redact first, always.

---

## ⚡ Performance notes

State inspectors can accidentally become performance problems if they re-render constantly.

Best practices:
- Render collapsed sections by default
- Throttle expensive stringify operations
- Avoid deep expansions unless requested
- Prefer preview summaries (counts + IDs) over full objects
- Keep “last actions” buffer capped (e.g., 50)

---

## 🧪 Testing expectations

At minimum, add tests for:

- ✅ redaction rules (mask/drop correctness)
- ✅ export snapshot stability (no non-deterministic values unless allowed)
- ✅ “dev-only” gating (panel does not mount in prod)
- ✅ large state handling (does not lock up UI)

Suggested test focus:
- Unit tests for the redaction engine (pure functions)
- UI tests for “copy/download” actions

---

## 🧯 Troubleshooting

### Panel doesn’t appear
- Confirm `VITE_DEV_STATE=1` or `REACT_APP_DEV_STATE=1`
- Confirm `NODE_ENV !== "production"`
- Confirm the panel is mounted in `App.tsx` (or equivalent)

### Panel makes the app slow
- Collapse sections by default
- Reduce render frequency (throttle)
- Stop rendering full GeoJSON blobs (IDs + counts only)

### “Copy snapshot” includes sensitive info
- Add the path to redactions
- Ensure export uses the *same redaction function* as the UI preview

---

## ✅ Contribution checklist

Before opening a PR:
- [ ] Dev panel mounts only in dev builds
- [ ] Export is redacted by default
- [ ] No direct DB or LLM calls from the UI
- [ ] No secrets or tokens ever displayed
- [ ] Tests added/updated for redaction + gating
- [ ] Sections remain small and human-readable (IDs + summaries win)

---

## 🔗 Related architecture docs (in-repo)
These docs explain why KFM’s UI state is designed the way it is:

- `docs/architecture/system_overview.md`
- `docs/architecture/ai/OLLAMA_INTEGRATION.md`
- `src/server/api/README.md`
- `docs/decisions/` (ADRs, if present)

---

## 🧭 Roadmap (nice-to-haves)
- 🧬 “Diff mode” between two snapshots
- 🧷 Bookmark a snapshot to LocalStorage (redacted)
- 🧰 Action log integration (last N actions)
- 🧭 “State invariants” warnings (e.g., timeline year out of bounds)
- 🧯 One-click “bug report bundle” export (snapshot + last API calls)

---

**Happy debugging. Keep it reproducible, keep it safe. 🧠🧯**
