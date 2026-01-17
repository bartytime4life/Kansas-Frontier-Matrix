# 🌐 API Resources

![Layer](https://img.shields.io/badge/layer-adapter-blue)
![Contract First](https://img.shields.io/badge/contract--first-required-2ea44f)
![Provenance](https://img.shields.io/badge/provenance--first-required-2ea44f)
![TypeScript](https://img.shields.io/badge/typescript-strongly%20typed-3178c6)

📍 **Location:** `web/src/adapters/api/resources/`

This folder contains **resource modules** that wrap the **KFM server API** into small, typed, composable functions.

> [!IMPORTANT]
> In KFM, the **UI is not a data source**. The UI must **not** query databases, file systems, or third‑party services directly.  
> Every dataset, layer, graph query, download, and narrative fetch **funnels through the server API**.

---

## 🧭 Quick navigation

- [What belongs here](#-what-belongs-here)
- [How it fits in the architecture](#-how-it-fits-in-the-architecture)
- [Folder conventions](#-folder-conventions)
- [Resource module template](#-resource-module-template)
- [Adding a new resource](#-adding-a-new-resource)
- [Testing](#-testing)
- [Performance and large files](#-performance-and-large-files)
- [Common pitfalls](#-common-pitfalls)
- [Related docs](#-related-docs)

---

## ✅ What belongs here

**Put in this folder:**

- 📦 **Per-endpoint “resource” wrappers** (e.g., datasets, tiles, story nodes, search, graph queries).
- 🧾 **Request/response normalization** that is *transport-level* (e.g., parsing dates, handling pagination envelopes).
- 🧯 **API error mapping** into a consistent error shape your app can handle.
- 🔐 **Auth-aware request helpers** (headers, tokens) *only via the shared ApiClient*.

**Do not put in this folder:**

- 🧠 Business logic, derivations, or UI-centric aggregation (“join these two endpoints and compute X”).
- 🎨 React hooks/components.
- 🗄️ Direct reads of `data/`, STAC/DCAT/PROV files, Neo4j, PostGIS, S3, etc.
- 🌍 Third‑party calls (geocoders, Earth Engine, etc.). Those must be mediated by the server.

---

## 🏗️ How it fits in the architecture

KFM uses a **clean/hexagonal architecture** mindset where “adapters” translate between the app and the outside world.

```text
┌───────────────────────────────────────────────────────────┐
│ UI (React / Map / Timeline)                               │
│   calls                                                    │
│   ▼                                                       │
│ web/src/adapters/api/resources  ← YOU ARE HERE             │
│   calls                                                    │
│   ▼                                                       │
│ web/src/adapters/api/client (ApiClient / fetch wrapper)    │
│   calls                                                    │
│   ▼                                                       │
│ src/server (REST/GraphQL + contracts + governance gates)   │
└───────────────────────────────────────────────────────────┘
```

**The goal:** keep the “how we talk to the API” code isolated, testable, and easy to swap.

---

## 📁 Folder conventions

> [!NOTE]
> Exact filenames may vary by feature, but the pattern should stay consistent.

### Recommended structure

```text
web/src/adapters/api/
├── 🌐 client/                    # shared HTTP client wrapper (fetch/axios, retries, auth, etc.)
├── ✅ resources/                 # ✅ this folder: endpoint-focused modules
│   ├── 📄 README.md              # you are here 📌
│   ├── 🧩📄 index.ts               # re-export resources
│   ├── 🗂️📄 datasets.ts            # example: dataset catalog + metadata
│   ├── 🧱🗺️📄 tiles.ts              # example: tile endpoints / signed URLs
│   ├── 🕸️📄 graph.ts               # example: graph queries (read-only)
│   ├── 📚🧩📄 storyNodes.ts          # example: governed narrative content
│   └── ➕ …                        # other domain resources
├── 🧾 types/                     # generated or shared API types (OpenAPI/GraphQL)
└── 🛑 errors/                    # shared ApiError types, guards, mappers
```

### Naming rules

- **One file ≈ one server “area”**: keep modules small and obvious.
- Prefer **verbs that signal intent**:
  - Queries: `get…`, `list…`, `search…`
  - Commands: `create…`, `update…`, `delete…`, `submit…`
- Export **one resource object** per file (or a small set of related functions).

---

## 🧩 Resource module template

Use this as a *shape guideline* (adapt to your actual ApiClient signature):

```ts
// web/src/adapters/api/resources/datasets.ts

import type { ApiClient } from "../client";
import type {
  Dataset,
  DatasetId,
  ListDatasetsQuery,
  ListDatasetsResponse,
} from "../types";

export function createDatasetsResource(client: ApiClient) {
  return {
    // 🔎 Query: list datasets (catalog/discovery)
    list: (query: ListDatasetsQuery) =>
      client.request<ListDatasetsResponse>({
        method: "GET",
        path: "/api/datasets",
        query,
      }),

    // 🔎 Query: get one dataset (metadata + provenance)
    get: (id: DatasetId) =>
      client.request<Dataset>({
        method: "GET",
        path: `/api/datasets/${id}`,
      }),
  };
}
```

### Standard expectations for every resource

- ✅ **Typed input + typed output** (no `any`).
- ✅ **Abortable** (support `AbortSignal` if your client supports it).
- ✅ **Pagination-ready** for list/search endpoints.
- ✅ **Preserve provenance**: do *not* drop citations/metadata fields returned by the server.
- ✅ **Error normalization**: throw or return a consistent `ApiError` type.

---

## ➕ Adding a new resource

### Step-by-step flow

1. 🧾 **Start with the API contract**
   - Define/extend the endpoint contract in the server contracts area (OpenAPI/GraphQL).
2. 🛠️ **Implement the server endpoint**
   - Keep enforcement (redaction/classification/governance) on the server side.
3. 🧬 **Regenerate or update shared types**
   - Ensure the web adapter consumes the contract (generated TS types, shared schema, etc.).
4. 📦 **Add a resource module**
   - New file in `resources/` exporting a resource object or functions.
5. 🔁 **Export it from `resources/index.ts`**
   - Keep imports consistent for the rest of the app.
6. 🧪 **Write tests**
   - Mock the ApiClient and validate path/method/params and response typing.
7. 🧭 **Wire it into the UI layer**
   - Prefer calling resources from a service/hook layer, not directly in components.

### Definition of done checklist

- [ ] Contract updated first (and versioned if needed)
- [ ] Backwards compatibility preserved (or explicit version bump)
- [ ] Types updated and used (no duplicate DTO definitions)
- [ ] Resource has clear query/command naming
- [ ] Errors mapped consistently
- [ ] Tests cover success + failure
- [ ] Large payloads handled correctly (pagination, streaming, signed URLs)
- [ ] No provenance fields dropped

---

## 🧪 Testing

### Unit tests

Unit tests here should be **fast** and **network-free**:

- mock `client.request`
- assert correct `{ method, path, query, body }`
- validate error mapping behavior

### Contract confidence

Even if the server has contract tests, the web adapter should still:

- rely on generated/shared types
- avoid hand-written DTO drift

> [!TIP]
> If you ever feel tempted to “patch” a contract mismatch in the UI, it’s usually a sign the **contract needs updating** (or the server needs to support a compatibility shape).

---

## 🚀 Performance and large files

KFM serves a lot of **geo + media artifacts** (GeoJSON, tiles, GeoTIFF/COG, PDFs, vector tiles, etc.). Resource calls should:

- 📚 Support **pagination** for catalog queries and searches.
- 🧊 Respect **caching** strategies provided by the API (ETags / cache headers if exposed).
- 🧵 Prefer **URL-based downloads** for huge assets (signed URLs / redirects) instead of pulling binary blobs through the UI.
- 🗺️ Use **tile endpoints** for heavy map layers rather than fetching full-resolution rasters.

---

## ⚠️ Common pitfalls

- ❌ **Calling `fetch` directly inside React components**  
  ✅ Use the ApiClient + resources so behavior is consistent and testable.

- ❌ **Silently stripping metadata**  
  ✅ KFM treats provenance and citations as first-class; keep them through to the UI.

- ❌ **UI-driven “backdoor” access patterns**  
  ✅ The UI must respect redaction/classification rules and never attempt to bypass them.

- ❌ **Duplicating server types in the UI**  
  ✅ Consume the contract (generated or shared types), don’t reinvent it.

---

## 🔗 Related docs

- 📘 `docs/MASTER_GUIDE_v13.md` — canonical pipeline + contract-first rules
- 🧩 `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` — how to extend endpoints cleanly
- 🗄️ `src/server/` — server API implementation
- 📐 `src/server/contracts/` — API contracts (OpenAPI/GraphQL)

---

## 🧠 Suggested next improvements

<details>
  <summary><strong>Ideas to level this up</strong> ✨</summary>

- Add a **shared response envelope** (`data`, `meta`, `provenance`) to make UI rendering consistent.
- Add **typed error codes** and a central `isApiError` type-guard.
- Add **request tracing** via a `x-kfm-request-id` header (server ↔ client correlation).
- Add a small **mock server** or MSW setup for integration tests.

</details>
