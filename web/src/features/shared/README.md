# 🧩 Shared UI & Utilities (`web/src/features/shared`)

![Scope](https://img.shields.io/badge/scope-shared%20feature%20toolbox-blue)
![UI](https://img.shields.io/badge/ui-React%20SPA-61DAFB?logo=react&logoColor=white)
![Maps](https://img.shields.io/badge/maps-MapLibre-1f6feb)
![Contract-first](https://img.shields.io/badge/data-access-contract--first-success)
![Accessibility](https://img.shields.io/badge/a11y-required-brightgreen)

> **Purpose:** This folder is the **cross-feature toolbox** for the KFM web UI—reusable components, hooks, utilities, and “guardrails” that multiple features depend on.  
> Think: 📦 **one home for shared building blocks** so every feature stays consistent, testable, and governable.

---

## 🗺️ Quick map of “where shared sits”

```mermaid
flowchart LR
  subgraph Backend (root/)
    Graph[(Neo4j Graph)]
    API[src/server<br/>(Contracted APIs)]
    Graph --> API
  end

  subgraph Frontend (web/)
    Shared[web/src/features/shared]
    Features[web/src/features/*]
    Shared --> Features
    Features --> API
  end

  Graph -. 🚫 direct access forbidden .-> Features
```

✅ **Features can depend on `shared/`.**  
✅ **UI talks to data through the API boundary.**  
🚫 **No feature (or shared module) should query the graph/database directly.**

---

## 🎯 Why this folder exists

- **Consistency** 🧭: shared UI patterns (layout, controls, map primitives, charts, tables) shouldn’t be re-implemented per feature.
- **Velocity** ⚡: build once, reuse everywhere.
- **Governance & trust** 🧾: shared is a natural place to enforce **evidence-first**, **provenance-aware**, and **sensitivity-safe** UI behaviors.
- **Performance** 🚀: centralized performance patterns (memoization helpers, lazy-loading wrappers, debounced inputs) prevent death-by-a-thousand-cuts.

---

## ✅ What *belongs* in `shared/`

### 🧱 Components
Reusable UI pieces that multiple features use, including (examples):

- 🗺️ Map primitives (wrappers + controls)
- 🧭 Layout primitives (panels, split views, responsive wrappers)
- 🧰 Form + filtering controls (search bars, toggles, selects)
- 📊 Data presentation (tables, empty states, legends)
- 🧾 Evidence UX (citation chips, provenance badges, “source panel” patterns)

### 🪝 Hooks
- `useBreakpoint`, `useDebounce`, `useLocalStorageState`
- `useQueryParamState` (deep linking / shareable URLs)
- `useAsync`, `useAbortController` wrappers

### 🔌 API client helpers (frontend side)
- Fetch wrappers, auth token helpers, request cancellation
- Normalizers / mappers (API DTO → UI view models)
- Caching helpers (if your project uses a cache library)

### 🧠 Types & schemas (frontend)
- Shared TypeScript types (or JS JSDoc types) used across features
- Common enums (sensitivity labels, layer kinds, time granularity, etc.)

### 🧯 UX + safety helpers
- Redaction helpers (mask coordinates / blur sensitive fields)
- “Classification banner” UI helpers
- Safe logging / telemetry wrappers

---

## 🚫 What does **NOT** belong in `shared/`

- Feature-specific business logic (belongs in that feature)
- One-off UI used by a single screen (keep it local)
- “Magic” data access paths:
  - 🚫 direct DB/graph calls  
  - 🚫 hidden local data dumps  
  - 🚫 bypassing the API boundary
- Project-wide bootstrapping (app initialization, routing config) — that belongs higher up in `web/src/`

> [!RULE]
> If a module has **domain meaning** (“LandTreatyTimeline”, “AquiferScenarioPlanner”), it’s not shared.  
> Shared is for **domain-agnostic primitives**.

---

## 🧬 KFM UI invariants this folder must protect

### 1) 🔌 Contract-first data access
All data shown in the UI must come from the **governed API layer** (not directly from the graph/database).

**In practice:**
- Prefer `shared/api/*` utilities that standardize:
  - base URL
  - auth headers
  - retries / timeouts
  - abort signals
  - error normalization

### 2) 🧾 Evidence-first UX
UI elements that communicate facts should be able to:
- display citations / sources
- show provenance badges or “derived from” context
- clearly label AI-generated summaries (when applicable)

> [!NOTE]
> If a component displays a “claim” (summary text, interpretation, ranking), it should accept structured evidence metadata (sources, confidence, lineage IDs) rather than free text.

### 3) 🛡️ Sovereignty + sensitivity propagation
Shared components must make it **easy** to do the right thing:
- consistent classification labels (Public / Restricted / Sensitive)
- redaction utilities and UI patterns (blur, generalize, hide)
- safe defaults (opt-in for risky detail)

### 4) 📱 Responsive + accessible by default
Shared is where we standardize:
- breakpoints
- keyboard navigation patterns
- semantic HTML + ARIA patterns for map controls and complex widgets

---

## 🗂️ Suggested folder layout (recommended)

> If your current structure differs, that’s fine—this is a *target shape* that scales.

```text
web/src/features/shared/
  README.md                  👈 you are here
  index.ts                   📦 shared public exports (barrel)

  components/                🧱 reusable UI
    layout/                  🧭 panels, split views, page frames
    map/                     🗺️ MapView wrappers, layer toggles, legend UI
    data/                    📊 tables, charts shells, empty/error states
    feedback/                💬 toasts, dialogs, loading spinners
    evidence/                🧾 citations, provenance badges, evidence drawers

  hooks/                     🪝 reusable hooks
  api/                       🔌 client helpers + typed adapters
  styles/                    🎨 tokens, mixins, shared CSS utilities
  utils/                     🛠️ pure helpers (formatting, geo math, etc.)
  types/                     🧠 shared types
  constants/                 🧷 breakpoints, labels, defaults
  testutils/                 🧪 render helpers, fixtures, mocks
```

---

## 📦 Public API rules (so shared doesn’t become a mess)

### ✅ Do
- Export stable modules from `web/src/features/shared/index.ts`
- Keep imports predictable:

```ts
// ✅ preferred
import { Panel, useBreakpoint } from "@/features/shared";
```

*(If your project doesn’t use path aliases, use relative imports consistently.)*

### 🚫 Don’t
- Deep-import internals from other features:

```ts
// 🚫 avoid: creates brittle coupling
import { computeWaterPolicy } from "@/features/water/utils/computeWaterPolicy";
```

> [!TIP]
> If multiple features need something, **promote** it into `shared/` and give it a clear name + test coverage.

---

## 🗺️ Shared map primitives (KFM-style)

Even if features implement specialized map behavior, shared should provide the *baseline plumbing*:

- `MapView` wrapper (map init + cleanup)
- common controls:
  - zoom/home
  - basemap switcher
  - layer toggles
  - legend container
- interaction helpers:
  - click/hover handlers with debouncing
  - “select feature” state wiring
- safety helpers:
  - coordinate generalization (when sensitive)
  - consistent popover/panel layout for map pick results

---

## 📊 Shared data presentation (charts / tables)

From the KFM UI architecture perspective, these are common cross-feature needs:

- `ChartPanel` shell (loading/error/empty patterns)
- `DataTable` shell (sorting/pagination/export affordances)
- standard formatting utilities:
  - numbers + units
  - dates and timeline labels
  - uncertainty ranges / confidence display

> [!NOTE]
> Keep “data meaning” out of shared.
> Shared provides the *shell* and *formatters*; features provide the *domain data*.

---

## 🚀 Performance guardrails (shared should help, not hurt)

Shared components should default to good performance patterns:

- ✅ memoize heavy render paths
- ✅ accept `className` and `style` to avoid wrapper churn
- ✅ support code-splitting for heavy optional modules (e.g., 3D or specialized renderers)
- ✅ avoid re-render cascades from global state (use selectors carefully)

---

## 🧪 Testing expectations

Shared modules are **high blast-radius**. Minimum expectations:

- ✅ deterministic unit tests for utilities
- ✅ component tests for UI primitives (render + interaction)
- ✅ a11y smoke checks where feasible
- ✅ story/fixture coverage for edge states:
  - empty
  - loading
  - error
  - restricted/sensitive data

---

## ➕ Adding something to `shared/` (Definition of Done ✅)

Before opening a PR, check:

- [ ] This is used (or will be used) by **2+ features** (or it enforces a hard invariant)
- [ ] Clear name, clear responsibility (no “misc”)
- [ ] Exported via `shared/index.ts` (or intentionally kept internal with a comment)
- [ ] No forbidden dependencies (no importing from sibling features)
- [ ] Handles loading/error/empty states if it touches async data
- [ ] Accessibility considerations done (keyboard + semantics)
- [ ] Sensitive-data handling considered (redaction/classification)
- [ ] Tests added/updated

---

## ❓FAQ

<details>
<summary><strong>When should I create a shared component vs keep it in a feature?</strong></summary>

- Keep it in a feature if it’s **domain-specific** or only used once.
- Promote to shared if it’s reused, or if it enforces a **system invariant** (e.g., evidence display, redaction, API error normalization).

</details>

<details>
<summary><strong>Can shared own global state?</strong></summary>

Shared can provide **state helpers** (reducers, stores, context providers), but avoid making shared the place where “everything global” lives.  
Prefer feature-owned state, and share only what’s truly cross-cutting (e.g., timeline selection, map viewport serialization).

</details>

<details>
<summary><strong>Where should Story Node / Focus Mode rendering helpers live?</strong></summary>

If multiple routes render governed narrative content, shared is the right place for:
- Markdown renderer wrappers
- citation/evidence UI primitives
- provenance + classification display helpers

The actual story content should remain governed elsewhere (not in `web/`).

</details>

---

## 🧭 Related docs (repo-level)

- 📘 `docs/MASTER_GUIDE_v13.md` (system invariants, directory layout, governance)
- 🔌 `src/server/` (API boundary — the frontend’s data contract)
- 🧾 `docs/reports/story_nodes/` (governed narrative content)

---