# 🧩 API Hooks — `web/src/hooks/api`

![React](https://img.shields.io/badge/React-hooks-informational)
![TypeScript](https://img.shields.io/badge/TypeScript-typed-informational)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-informational)
![GraphQL](https://img.shields.io/badge/GraphQL-graph%20queries-informational)
![OPA](https://img.shields.io/badge/OPA-policy%20gates-informational)

> ✅ **Goal:** This folder is the **single, consistent way** the web UI talks to KFM backends (REST, GraphQL, tiles, and Focus Mode).
>
> ⚖️ **Constraint:** KFM is governed + provenance-first → **hooks must respect policy + evidence invariants** (no “quick fetch” shortcuts).

---

## 📌 What belongs here?

This directory contains **React hooks** that wrap network calls to KFM services, so that UI components can stay clean and predictable:

- 🔌 **REST hooks** (dataset/catalog/query endpoints)
- 🧬 **GraphQL hooks** (graph + cross-domain joins)
- 🗺️ **Map hooks** (tiles + geo payloads)
- 🧠 **Focus Mode hooks** (AI assistant requests + streaming responses)
- 🧰 **Shared plumbing** (client wrapper, types, runtime guards, error normalization)

---

## 🧭 The KFM “Truth Path” (why hooks exist)

KFM’s architecture has a non‑negotiable flow:

```
Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI
```

**Implication for this folder:**  
✅ UI components should **never** reach around the API boundary (no direct DB calls, no “talk to the model directly”).  
➡️ If the UI needs something, we add/adjust **an API endpoint** and then create/extend **a hook** here.

---

## 🗂️ Suggested folder map (pattern)

> Your exact filenames may evolve — the intent should not. 💡

```
📦 web/src/hooks/api
├─ 📄 README.md                      ← you are here
├─ 🧰 client/                        ← fetch wrapper + errors + auth helpers
│  ├─ apiClient.ts
│  ├─ errors.ts
│  ├─ headers.ts
│  └─ types.ts
├─ 🧾 catalog/                        ← dataset discovery/search
│  ├─ useCatalogSearch.ts
│  └─ useDataset.ts
├─ 🗺️ geo/                            ← geo payload helpers (bbox, geojson, etc.)
│  ├─ useDatasetGeoJSON.ts
│  └─ bbox.ts
├─ 🧬 graphql/                         ← GraphQL query hooks
│  ├─ useGraphQL.ts
│  └─ operations.ts
├─ 🧠 focus-mode/                      ← AI assistant hooks
│  ├─ useFocusModeQuery.ts
│  ├─ useFocusModeStream.ts
│  └─ citations.ts
└─ 🧪 __tests__/                       ← MSW fixtures + hook tests
```

---

## 🌐 API surfaces these hooks commonly call

KFM typically exposes several “front doors” that the UI can target:

### 1) REST (`/api/v1/*`)
Examples you’ll see referenced in the architecture docs:

- `GET /api/v1/datasets/{id}` → dataset metadata (DCAT-aligned)  
- `POST /api/v1/catalog/search` → search datasets (filters like bbox/time/keywords)  
- `GET /api/v1/datasets/{id}/data?format=geojson&bbox=...` → stream geo features  
- `POST /api/v1/query` → **safe** query interface (no direct DB access from UI)

### 2) GraphQL (`/graphql`)
Used when the UI needs **connected** knowledge (graph relationships + join-like queries).

### 3) Tiles (`/tiles/*`)
Vector/raster tile endpoints used for map rendering, e.g.:

- `/tiles/{layer}/{z}/{x}/{y}.pbf`
- `/tiles/{layer}/{z}/{x}/{y}.png`

### 4) Focus Mode (`/focus-mode/*`)
AI assistant endpoints, commonly:

- `POST /focus-mode/query` → ask a question (backend orchestrates retrieval + policy + citations)

> 🧠 Focus Mode is **evidence-first**: responses are expected to include citations that the UI can render as clickable footnotes.

---

## 🧪 Hook design rules (team-level conventions)

### ✅ 1) Hooks return UI-friendly state, not “raw fetch”
Prefer:

- `data`
- `error` (normalized)
- `isLoading` / `status`
- `refetch` / `mutate` (if using a query library)

Avoid:

- returning raw `Response`
- forcing components to parse JSON / map status codes

### ✅ 2) Always normalize errors (including policy denies)
KFM is “fail-closed” by design. Your hook should differentiate:

- 🌐 **network** failure (offline, DNS, timeout)
- 🔐 **auth** (401)
- ⛔ **policy denied** (403 / OPA deny)
- 🧾 **validation** (422)
- 💥 **server error** (5xx)

💡 Components shouldn’t guess what happened — hooks should make it obvious.

### ✅ 3) Prefer relative URLs behind the gateway
When the UI is served behind the same reverse proxy, prefer:

- `fetch("/api/v1/...")`
- `fetch("/graphql")`
- `fetch("/focus-mode/query")`

This keeps deployments consistent and reduces CORS drama.

### ✅ 4) Cancellation is not optional (maps + search + chat)
If a hook can be triggered frequently (typing, panning maps, timeline scrubbing), support cancellation:

- `AbortController`
- query-library cancellation primitives (if used)

### ✅ 5) Runtime guards for untrusted payloads
Even with TypeScript, API payloads are **untrusted input**. For critical flows, consider:

- schema guards (e.g., `zod` / custom validators)
- defensive parsing for Focus Mode citation maps

---

## 🔐 Auth & token handling (pragmatic guidance)

If KFM uses **cookie sessions**:  
✅ hooks should send credentials correctly and not re‑implement auth in components.

If KFM uses **bearer tokens**:  
⚠️ treat browser storage as hostile. Prefer:

- short‑lived tokens
- in‑memory storage where possible
- rotating sessions via backend

> 🔎 Don’t quietly “make it work” by stuffing long‑lived credentials into `localStorage`. If you must store something, document the tradeoff clearly in the hook and in UI.

---

## ⚖️ Governance & sensitive data behavior

KFM’s governance model can tag data with sensitivity and apply policy at request time.

**What hooks must do:**
- ✅ surface “denied” vs “not found” correctly (don’t mask governance decisions as missing data)
- ✅ expose any “safe fallback” messages from the API (especially Focus Mode)
- ✅ never attempt client-side workarounds for restricted data

### 🌿 Indigenous data considerations (CARE-aligned behavior)
Some datasets may be governed by community constraints (restricted access, takedown requests, warnings).

Hook responsibilities:
- don’t cache/share restricted responses in ways that bypass policy
- support “withdrawn”/“restricted” states gracefully
- pass through warning metadata so UI can present it respectfully

---

## 🧠 Focus Mode hooks (special rules)

Focus Mode is **not** “call an LLM from the browser.”

The backend orchestrator typically:
1) parses intent  
2) retrieves relevant graph/docs/data  
3) generates an answer with citations  
4) runs policy checks (OPA)  
5) returns answer + citation map (and logs provenance)

### ✅ UI expectations
Your Focus Mode hook(s) should support:
- streaming (if enabled) for responsiveness
- final structured payload:
  - `answer` (markdown-ish or plain text)
  - `citations` mapping (e.g., `[1] → source metadata`)
  - `policy` result (allowed / redacted / refused)
  - optional `trace` payloads (if user requested “show work”)

### Example hook shape (illustrative)
```ts
type FocusModeResponse = {
  answer: string;
  citations: Record<string, { title: string; url?: string; kind: "dataset" | "doc" | "graph" }>;
  policy: { allowed: boolean; redacted?: boolean; reason?: string };
};

export function useFocusModeQuery() {
  // return { ask, isLoading, error, lastResponse }
}
```

---

## 🚀 Adding a new API hook (checklist)

### 1) Confirm the API contract
- Endpoint exists (or create it in the API layer)
- Request/response types are defined (OpenAPI / GraphQL schema)
- Security + policy behavior is understood (what does 403 mean here?)

### 2) Create types first 🧱
- `Request` / `Response` types
- shared DTOs in a `types.ts` (domain folder)

### 3) Implement the hook 🪝
- call through the shared client wrapper
- normalize errors
- add cancellation support for high-frequency hooks

### 4) Add tests 🧪
- MSW mocks for success + failure + policy-deny cases
- regression tests for parsing/validation (especially Focus Mode)

### 5) Document it 📚
- add the hook to the “Hook Index” section below
- note any policy nuances or caching pitfalls

---

## 🧾 Hook Index (fill in as hooks land)

> Keep this list current so UI devs can find the right hook fast. ⚡

### Catalog / Datasets
- `useDataset(datasetId)`
- `useCatalogSearch(filters)`

### Geo / Tiles
- `useDatasetGeoJSON(datasetId, bbox)`
- `useTileUrl(layerId)` (builder helper)

### GraphQL
- `useGraphQL(query, variables)`

### Focus Mode
- `useFocusModeQuery()`
- `useFocusModeStream()` (if streaming supported)

---

## 🧯 Troubleshooting

<details>
  <summary><strong>😵 CORS errors in dev</strong></summary>

- Prefer running behind the dev proxy / reverse proxy when possible.
- If cross-origin is unavoidable, confirm backend CORS allowlist is configured for your dev origin.
</details>

<details>
  <summary><strong>🧩 “Works in Postman, fails in UI”</strong></summary>

- check cookies/credentials mode
- verify base URL (relative vs absolute)
- confirm headers (content-type, auth)
- confirm policy: UI user role may differ from your Postman token
</details>

<details>
  <summary><strong>🗺️ Tiles are blank / 404</strong></summary>

- confirm layer name matches backend config
- confirm tile format (pbf vs png)
- confirm gateway routing for `/tiles/*`
</details>

---

## 🔗 Related docs (recommended reading)
- 🏗️ Architecture & invariants: `../../../../docs/`
- ⚙️ Backend API layer: `../../../../api/`
- 🧠 Focus Mode / AI governance: `../../../../docs/architecture/ai/`
- 🧾 Catalog + provenance standards: `../../../../docs/standards/`

---

## ✅ “Good Hook” review mini-checklist

- [ ] Uses shared client wrapper (not ad-hoc `fetch`)
- [ ] Typed request/response
- [ ] Normalized error handling (incl. policy denies)
- [ ] Cancellation supported where needed
- [ ] Safe caching (doesn’t leak restricted payloads)
- [ ] Documented in the Hook Index
- [ ] Includes tests for success + denied + failure