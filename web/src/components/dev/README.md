# 🧰 Dev Components (`web/src/components/dev`)

![scope: dev-only](https://img.shields.io/badge/scope-dev--only-orange)
![ui: react](https://img.shields.io/badge/ui-react-61DAFB)
![lang: typescript](https://img.shields.io/badge/lang-typescript-3178C6)
![kfm: governed](https://img.shields.io/badge/kfm-governed%20by%20policy-6E56CF)

> **What this folder is:** developer-only UI utilities for inspecting **state**, **maps**, **API calls**, **provenance**, and **Focus Mode** behavior.  
> **What this folder is NOT:** “admin tools”, “prod features”, or anything required for runtime.

---

## 🧭 Quick links

- ⬅️ Project overview: `../../../../README.md`
- 🧱 Architecture docs: `../../../../docs/`
- 🔌 API docs (local): `http://localhost:8000/docs` (Swagger UI) + `http://localhost:8000/graphql` (if enabled)
- 🧪 Tests: `../../../../tests/`
- ⚙️ Tooling / validators: `../../../../tools/`

---

## 🔭 Purpose

KFM’s UI is map + timeline + story + AI (Focus Mode). When we’re building and debugging that experience, we need **visibility**:

- 🧵 What global state is set right now (year, bbox, selected feature, active story node)?
- 🗺️ What MapLibre/Cesium layers are loaded (style, filters, tile URLs, render order)?
- 🔌 What API calls are being made (and what payloads come back)?
- 🧾 What provenance/citations are attached (especially for AI answers)?
- 🛡️ What policy decisions were applied (fail-closed behavior, RBAC gating)?

This folder keeps those “developer eyes” tools isolated so they’re easy to add/remove and **hard to accidentally ship**.

---

## ✅ Non‑negotiables (KFM rules that dev tools must obey)

> **Fail closed.** If something is missing (metadata, policy, auth), the tool should *not* “guess” or bypass guards.  
> **API boundary only.** Dev UI **must not** query PostGIS/Neo4j directly—ever.  
> **No sensitive leakage.** Don’t print tokens, private dataset content, or restricted coordinates into the DOM/console.

**Dev tools should help us verify governance, not weaken it.** 🧷

---

## 🧩 How this fits the KFM stack

```mermaid
flowchart LR
  UI[🖥️ React/TypeScript UI] -->|REST / GraphQL| API[🧠 API Layer\n(FastAPI + GraphQL)]
  API --> KG[(🕸️ Neo4j\nKnowledge Graph)]
  API --> GIS[(🗺️ PostGIS\nGeospatial DB)]
  API --> IDX[(🔎 Search/Index)]
  API -->|prompt + retrieved context| LLM[🤖 Ollama\nFocus Mode Engine]
  LLM --> API
  API --> UI
```

**Dev components live entirely in the UI** and should only “see” what a normal UI user would see, plus safe debug metadata.

---

## 🧪 What typically lives in `dev/`

Think of this directory as a “toolbelt”. 🧰

### 🗺️ Map debugging
- Pointer readout (lat/lng, zoom, bearing)
- Current style + layer order
- Active filters (time range, bbox, story context)
- Tile request inspection (vector/raster endpoint sanity)

### 🧵 State & timeline inspection
- Current timeline year/range
- Selected entities (feature IDs, story node IDs)
- Store snapshots (Redux/Context) + action logging (when enabled)

### 🔌 API exploration
- Quick “ping” / health checks
- Dataset metadata lookups
- Tile URL builders (copy/paste)
- GraphQL query scratchpad (dev only)

### 🤖 Focus Mode inspection
- Request payload preview (question + context)
- Response view:
  - citations / sources list
  - model version/tag (if returned)
  - policy decision metadata (allowed/denied + reason)
- “No Source, No Answer” sanity checks

### 🛡️ Policy & governance helpers
- Role / access boundary visualization
- “Why denied?” panels (safe to show—no secret policy internals)

---

## 🧱 Recommended folder layout

> Adapt as needed—this is the target shape so dev tooling stays consistent and discoverable.

```text
web/src/components/dev/
├─ 📄 README.md                      # you are here 🙂
├─ 🧩 DevToolsRoot.tsx               # single entry point for all dev tooling UI
├─ 🔐 DevToolsGate.tsx               # centralized gating (build + runtime)
├─ 🧾 DevToolsRegistry.ts            # list of available tools + ordering
│
├─ 🗺️ map/
│  ├─ MapInspector.tsx               # layer list, tiles, coords, style info
│  └─ MapDebugOverlay.tsx            # small HUD overlay
│
├─ 🧵 state/
│  ├─ StateViewer.tsx                # store snapshot (read-only)
│  └─ ActionLog.tsx                  # dev-only action stream
│
├─ 🔌 api/
│  ├─ ApiExplorer.tsx                # call safe endpoints, view responses
│  └─ TileUrlBuilder.tsx             # build /tiles/{layer}/{z}/{x}/{y}
│
├─ 🤖 focus-mode/
│  ├─ FocusModeInspector.tsx         # request/response + citations/policy view
│  └─ PromptPreview.tsx              # shows composed prompt parts (sanitized)
│
└─ 🧰 shared/
   ├─ useDevFlag.ts                  # flag hook (env + query param)
   ├─ SafeJsonViewer.tsx             # pretty-print with truncation & redaction
   └─ redact.ts                      # token/PII redaction helpers
```

---

## 🚦 Gating: how to ensure dev tools never ship accidentally

You want **two locks**:

1) **Build-time lock** (tree-shake away in prod builds)  
2) **Runtime lock** (even in staging/dev, only show when explicitly enabled)

### ✅ Build-time examples

#### Vite
```ts
export const DEV_BUILD = import.meta.env.DEV;
```

#### CRA / Webpack
```ts
export const DEV_BUILD = process.env.NODE_ENV !== "production";
```

### ✅ Runtime flag examples

> Pick one canonical flag for the project and stick to it.

- env flag: `VITE_KFM_DEVTOOLS=1` / `REACT_APP_KFM_DEVTOOLS=1`
- query param: `?devtools=1`
- localStorage: `kfm:devtools = "1"`

Example hook:

```ts
export function useDevToolsEnabled(): boolean {
  const devBuild =
    (typeof import.meta !== "undefined" && (import.meta as any).env?.DEV) ||
    process.env.NODE_ENV !== "production";

  const url = new URL(window.location.href);
  const qp = url.searchParams.get("devtools") === "1";

  const envFlag =
    ((import.meta as any).env?.VITE_KFM_DEVTOOLS ?? process.env.REACT_APP_KFM_DEVTOOLS) === "1";

  return Boolean(devBuild && (envFlag || qp));
}
```

---

## ➕ Adding a new dev tool (the “right way”)

1. **Create the tool component** under an appropriate subfolder (e.g., `map/`, `api/`, `focus-mode/`).
2. **Assume untrusted inputs** (API responses, URL params, copied JSON, etc.).
3. **Redact sensitive fields** by default (tokens, cookies, auth headers, user emails).
4. **Register the tool** in `DevToolsRegistry.ts`.
5. **Gate it** behind `DevToolsGate.tsx`.
6. **Keep imports one-way**:
   - ✅ app → dev (only through a gated entry point)
   - ❌ dev → app core (avoid circular/implicit inclusion)

> If you can import a dev tool from “regular UI” without a gate, it will eventually ship. 🚫

---

## 🧾 Debugging Focus Mode responsibly

Focus Mode is evidence-first. Dev tooling should make it easy to verify:

- the UI is calling the **API** (not an LLM directly)
- the response includes **citations**
- the response includes **policy decision metadata** (when available)
- the UI renders citations in a **clickable, auditable** way

### Suggested (safe) response shape to display

```ts
type FocusModeDebug = {
  answer: string;
  citations: Array<{
    id: string;
    title?: string;
    url?: string;
    datasetId?: string;
    excerpt?: string; // truncated
  }>;
  model?: { provider?: string; name?: string; tag?: string; version?: string };
  policy?: { allowed: boolean; reason?: string; policyVersion?: string };
  provenance?: { ledgerId?: string; timestamp?: string };
};
```

✅ Prefer **truncation** and **redaction** over raw dumps.

---

## 🔌 Useful local endpoints (common KFM dev workflow)

> Exact routes may evolve; these are the “usual suspects”.

- Swagger UI: `http://localhost:8000/docs`
- GraphQL: `http://localhost:8000/graphql` (if enabled)
- Dataset metadata: `/api/v1/datasets/{id}`
- Catalog search: `/api/v1/catalog/search`
- Vector tiles: `/tiles/{layer}/{z}/{x}/{y}.pbf`
- Raster tiles: `/tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`)

---

## 🧯 Troubleshooting (quick fixes)

- **Port conflicts** (common: 5432, 7474, 8000, 3000): stop the local service or remap ports in `docker-compose.yml`.
- **Web container not reflecting changes**: confirm volume mounts for `web/src` and rebuild if dependencies changed.
- **CORS / API base URL weirdness**: verify `.env` / `.env.local` and the UI’s configured API origin.
- **Slow map rendering**: disable heavy overlays and ensure you’re using tiles for large datasets (not full GeoJSON blobs).

---

## 🧼 Production hygiene checklist (before merging)

- [ ] Dev tools are **gated** (build + runtime)
- [ ] No dev-only imports leak into core UI paths
- [ ] Sensitive values are **redacted** in any viewer/logging
- [ ] No direct datastore access (API boundary respected)
- [ ] UI still works with dev tools removed/disabled
- [ ] “Fail closed” behavior preserved (no bypass toggles)

---

## 📌 Notes

<details>
  <summary><strong>Why keep dev tooling inside the repo?</strong> 🧠</summary>

- Repeatability: every dev sees the same diagnostics.
- Faster onboarding: “how do I inspect X?” becomes a button, not tribal knowledge.
- Governance verification: tools help confirm provenance/citations/policy behavior *in the UI where users experience it*.
</details>