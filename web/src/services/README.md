# 🧰 `web/src/services` — UI Services Layer

![TypeScript](https://img.shields.io/badge/TypeScript-typed-informational?logo=typescript)
![React](https://img.shields.io/badge/React-client-blue?logo=react)
![API-First](https://img.shields.io/badge/API--First-contracts%20over%20coupling-success)
![Provenance](https://img.shields.io/badge/Provenance-first%20by%20design-purple)

> **One job:** this folder is the **network boundary** of the KFM web UI — the single home for **calling backend APIs**, **building tile URLs**, and **normalizing responses/errors**.  
> Keep components clean. Keep contracts explicit. Keep governance intact. 🧭

---

## 📌 What belongs here (and what doesn’t)

✅ **Belongs in `services/`**
- `fetch` / HTTP client wrappers (REST + GraphQL)
- “Domain service” modules (datasets, catalog search, tiles, Focus Mode, etc.)
- URL builders (e.g., vector tile templates)
- Request/response typing + error normalization (per endpoint)
- Cross-cutting concerns at the API edge (timeouts, abort signals, request IDs)

🚫 **Does NOT belong in `services/`**
- React components / JSX
- Global state (Redux slices, Zustand stores, etc.)
- React hooks (put those in `web/src/hooks/` — hooks can *use* services)
- Any direct DB logic (UI never talks to databases)
- Any direct LLM/AI calls (UI calls backend endpoints; backend orchestrates)

---

## 🧠 Mental model: “UI ↔ Services ↔ API”

```mermaid
flowchart LR
  UI[🖥️ React UI<br/>(components + hooks)] --> SVC[🧰 services/<br/>typed clients + helpers]
  SVC --> API[🧱 Backend API<br/>(FastAPI + GraphQL)]
  API --> DS[(🗄️ Datastores<br/>PostGIS / Neo4j / Search Index)]
  API --> AI[(🤖 Focus Mode<br/>LLM runtime behind API)]
```

**Rule of thumb:** If you see `fetch(...)` inside a component, it probably belongs here instead. 👀

---

## 🗂 Suggested layout

> Your repo may already have some of these names — this is the **intended shape** of the folder.

```text
📁 web/
  📁 src/
    📁 services/
      📄 README.md
      📄 apiClient.ts           # fetch wrapper (baseUrl, headers, errors)
      📄 graphqlClient.ts       # POST /graphql wrapper (typed requests)
      📄 tiles.ts               # tile URL builders + layer helpers
      📄 datasets.ts            # dataset metadata + dataset data endpoints
      📄 catalog.ts             # catalog search endpoints
      📄 query.ts               # ad-hoc query endpoint wrapper (if enabled)
      📄 focusMode.ts           # Focus Mode endpoint wrapper
      📄 index.ts               # barrel exports (optional)
```

<details>
<summary>✨ Why keep it centralized?</summary>

- **Governance & safety**: the UI stays decoupled; the API mediates validation + policy.
- **Consistency**: one error shape, one auth strategy, one retry/timeout approach.
- **Refactors don’t hurt**: if `/api/v1/...` changes, update one module, not 47 files.
</details>

---

## 🔑 Service design principles

### 1) 🔒 “Backend is the policy gate”
Services should assume the API enforces:
- provenance + citation requirements (especially for Focus Mode)
- access control / redaction rules
- validation and query safety

UI services should:
- surface **HTTP status**, **human-friendly message**, and **request correlation ID** (if returned)
- avoid inventing facts or falling back to “best guess” data

---

### 2) 🧾 Typed contracts (always)
Prefer exporting explicit types per endpoint.

```ts
// ✅ Good: each endpoint has a clear input/output surface
export type DatasetId = string;

export interface DatasetMeta {
  id: DatasetId;
  title: string;
  description?: string;
  updatedAt?: string;
  // ...
}
```

If you’re using a schema-driven setup (OpenAPI → types, GraphQL codegen, etc.), this folder is where those types get *consumed*.

---

### 3) 🧯 Normalize errors once
Every service function should throw (or return) a consistent error type.

**Recommended contract:**
- `ApiError.status` (HTTP status)
- `ApiError.code` (optional machine code)
- `ApiError.details` (optional structured payload)
- `ApiError.requestId` (if available)

```ts
export class ApiError extends Error {
  status: number;
  code?: string;
  details?: unknown;
  requestId?: string;

  constructor(message: string, init: Partial<ApiError>) {
    super(message);
    Object.assign(this, init);
  }
}
```

---

### 4) 🧵 Support AbortController (maps + search need it)
Maps and live search produce rapid request churn. Every call should accept an optional `AbortSignal`.

```ts
export type RequestOptions = {
  signal?: AbortSignal;
};

export async function searchCatalog(
  text: string,
  opts: RequestOptions = {}
) {
  // pass opts.signal through to fetch
}
```

---

## 🌐 Base API patterns

### ✅ Centralize base URL (don’t scatter it)
Pick **one** way to compute the API base URL and reuse it across the folder.

Example (Vite-style):
```ts
const API_BASE_URL =
  (import.meta as any).env?.VITE_API_BASE_URL ?? "";
```

If your project uses CRA/Next/etc., adapt accordingly — the key is **one source of truth**.

---

## 🧱 Common API surfaces used by the UI

> These are the typical backend capabilities the UI consumes (REST + GraphQL + tiles + Focus Mode).  
> Keep all of these calls inside `services/`.

### 🗃️ Datasets & Catalog
Typical patterns:
- `GET /api/v1/datasets/{id}` → dataset metadata
- `GET /api/v1/datasets/{id}/data` → dataset rows/features
- `GET /api/v1/catalog/search?text=...` → search datasets (and maybe stories)

**Service modules**
- `datasets.ts` → `getDatasetMeta(id)`, `getDatasetData(id, params)`
- `catalog.ts` → `searchCatalog(query, filters)`

---

### 🧠 Focus Mode (AI assistant)
**Important:** UI never calls the model directly. The UI hits a backend endpoint (commonly something like `POST /focus-mode/query`) and renders:
- the answer text
- the citations/footnotes payload (clickable in UI)
- optional structured provenance metadata

**Service module**
- `focusMode.ts` → `askFocusMode({ question, mapContext, selectedLayers, ... })`

Suggested response shape:
```ts
export interface FocusModeCitation {
  id: string;          // doc/story/dataset ref
  label?: string;      // short display label
  url?: string;        // optional deep link
}

export interface FocusModeResponse {
  answer: string;                 // may include markers like [1], [2]
  citations: FocusModeCitation[]; // render as clickable footnotes
  // optional: provenance, debug traces, etc.
}
```

---

### 🗺️ Tiles (MapLibre / Cesium)
Large layers should stream as tiles (vector/raster), while small overlays may use GeoJSON.

✅ Put **tile URL creation** in `tiles.ts` so that map components don’t hardcode paths.

```ts
export function vectorTileUrl(layer: string) {
  // Choose your routing convention:
  // - /tiles/{layer}/{z}/{x}/{y}.pbf
  // - /api/tiles/{layer}/{z}/{x}/{y}.pbf
  return `${API_BASE_URL}/api/tiles/${layer}/{z}/{x}/{y}.pbf`;
}
```

Then in the map layer code:
```ts
map.addSource("historic_trails", {
  type: "vector",
  tiles: [vectorTileUrl("historic_trails")],
});
```

---

### 🧬 GraphQL
If the UI uses GraphQL, keep the client in `graphqlClient.ts`.

```ts
export async function gql<TData, TVars>(
  query: string,
  variables?: TVars,
  opts: RequestOptions = {}
): Promise<TData> {
  return apiFetch<TData>("/graphql", {
    method: "POST",
    body: JSON.stringify({ query, variables }),
    signal: opts.signal,
  });
}
```

---

## 🧪 Testing strategy (quick + sane)

### ✅ Unit tests
- Mock `apiFetch` and assert:
  - path + method + body shape
  - response parsing
  - error normalization

### ✅ Integration-ish tests
- Use **MSW** (Mock Service Worker) to simulate the API at the network boundary.
- Validate:
  - abort behavior on rapid interactions (search, map pan/zoom)
  - focus mode citation rendering contract

---

## ✅ Checklist for adding a new service

- [ ] Create a new `services/<domain>.ts` file (or extend an existing domain module)
- [ ] Add **typed** input/output
- [ ] Use the shared `apiClient` wrapper (no raw `fetch`)
- [ ] Support `AbortSignal` where it matters
- [ ] Normalize errors (throw `ApiError`)
- [ ] Do not embed UI assumptions (keep it framework-agnostic)
- [ ] Export through `services/index.ts` (if you use barrel exports)

---

## 🧭 “If you remember nothing else…”

> **The UI is a map & narrative explorer. The API is the gatekeeper.  
> `services/` is the contract glue that keeps that separation clean.** 🔥

---
