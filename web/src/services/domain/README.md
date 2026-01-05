# 🧩 Domain Services (Web)

![TypeScript](https://img.shields.io/badge/TypeScript-First-3178C6?logo=typescript&logoColor=white)
![Clean Architecture](https://img.shields.io/badge/Architecture-Clean%20Layers-0B7285)
![Testing](https://img.shields.io/badge/Tests-Jest%2FVitest-6E40C9)
![Maps](https://img.shields.io/badge/Maps-2D%2F3D%20Ready-2B8A3E)

> **Purpose:** This folder contains **domain-level services (aka “use cases”)** for the KFM web app.  
> They sit between **UI (React components/features)** and **infrastructure (API clients, storage, telemetry)** and provide **typed, testable, reusable workflows**.

---

## 🗺️ Where this fits in the KFM architecture

KFM follows a layered approach inspired by Clean Architecture:

- **🧠 Domain entities & rules** (core concepts: fields, layers, NDVI, scenarios, users)
- **⚙️ Use cases / application logic** (workflows: “load NDVI layer for date”, “fetch field timeseries”, “submit simulation”)
- **🔌 Interfaces / adapters** (ports: repositories, presenters, gateways)
- **🏗️ Infrastructure** (HTTP clients, caches, browser APIs, analytics SDKs, map engines)

In the **web app**, `web/src/services/domain` is where we implement the **use cases** as code:  
**small, focused flows** that orchestrate data access, caching, validation, and business rules—without leaking UI concerns into the core.

---

## ✅ What belongs here (and what doesn’t)

| ✅ Put it in `services/domain/` | 🚫 Keep it out of `services/domain/` |
|---|---|
| Use-case orchestration (compose multiple API calls, normalize results) | React components, hooks, JSX |
| DTO → Domain mapping (turn API payloads into typed models) | Direct `fetch()` / `axios` calls (use adapters/clients) |
| Domain validation / guardrails (e.g., date ranges, required params) | Browser-only side effects (`localStorage`, `window`, DOM) |
| Caching + request coalescing (avoid duplicate calls) | Redux reducers/slices (store should *call* domain, not live inside it) |
| Throttling policies for timeline scrubbing & map refresh | Styling, UI layout, UX copy |
| Typed errors & “result” objects | Secrets, tokens hardcoded, env wiring |

> 🔐 **Reminder:** Backend authorization is the source of truth. Domain services may *hide/disable* features based on user role claims for UX, but should not assume UI-only checks are security controls.

---

## 🧱 Suggested folder layout

> Your exact structure may differ—this is the recommended pattern for keeping things discoverable and scalable.

```text
📦 web/src/services/domain
├─ 📄 README.md
├─ 📄 index.ts
├─ 📁 _shared
│  ├─ 📄 types.ts              # shared domain types (Result, IDs, etc.)
│  ├─ 📄 errors.ts             # typed domain errors
│  ├─ 📄 guards.ts             # invariants + runtime validation helpers
│  ├─ 📄 mappers.ts            # DTO ⇄ Domain mapping helpers
│  └─ 📄 caching.ts            # in-memory cache helpers (TTL, LRU, de-dupe)
│
├─ 📁 auth
│  ├─ 📄 auth.service.ts
│  ├─ 📄 auth.ports.ts         # interfaces (AuthGateway, TokenStore)
│  └─ 📄 auth.types.ts
│
├─ 📁 layers
│  ├─ 📄 layerCatalog.service.ts
│  ├─ 📄 layerCatalog.ports.ts # LayerRepository, TileGateway, etc.
│  └─ 📄 layer.types.ts
│
├─ 📁 timeseries
│  ├─ 📄 fieldTimeseries.service.ts
│  ├─ 📄 timeseries.ports.ts
│  └─ 📄 timeseries.types.ts
│
├─ 📁 scenarios
│  ├─ 📄 scenarioRuns.service.ts
│  ├─ 📄 scenarios.ports.ts
│  └─ 📄 scenarios.types.ts
│
└─ 📁 __tests__
   ├─ 🧪 layerCatalog.service.test.ts
   └─ 🧪 fieldTimeseries.service.test.ts
```

---

## 🔩 Design rules (the “sharp edges”)

### 1) 🧼 Keep services small & single-purpose
A domain service should read like a **workflow**:
- validate inputs
- ask a port for data (repository/gateway)
- map/normalize
- return a typed result

If it grows beyond ~150–250 lines, split by sub-use-case.

### 2) 🔁 Prefer ports (interfaces) over imports
Domain services should depend on abstractions:

```ts
export interface LayerCatalogRepository {
  listAvailableLayers(): Promise<LayerMetaDto[]>;
  getLayerAvailability(layerId: string): Promise<{ dates: string[] }>;
}
```

Infrastructure implements these ports elsewhere (e.g., `services/api`, `services/http`, `services/storage`), then gets injected into the domain service.

### 3) 🧠 Domain services return domain models (not raw DTOs)
API payload shapes can change. Domain models should be stable and meaningful.

### 4) 🧯 Typed errors, not stringly-typed exceptions
Prefer domain errors your UI/store can handle predictably.

### 5) ⏱️ Timeline + maps need request discipline
The KFM UI has “scrubbing” behaviors (timeline slider, map overlays). Domain services should support:
- request throttling/debouncing at the boundary
- request de-duplication (“same request in-flight”)
- caching adjacent dates (prefetch strategy)

---

## 🔄 Data flow at runtime (UI → Domain → Infra)

```mermaid
flowchart LR
  UI[🖥️ React Feature / Component] --> Store[🧰 Store / Controller]
  Store --> UseCase[🧩 Domain Service (Use Case)]
  UseCase --> Port[🔌 Port Interface]
  Port --> Infra[🏗️ Infra Adapter (API Client / Cache / Storage)]
  Infra --> API[🌐 Backend API]
  API --> Infra --> UseCase --> Store --> UI
```

---

## 🧪 Example: A domain service (Layer Catalog)

### Domain types
```ts
// web/src/services/domain/layers/layer.types.ts
export type LayerId = string;

export interface LayerMeta {
  id: LayerId;
  name: string;
  kind: "raster" | "vector" | "timeseries";
  description?: string;
}

export interface LayerAvailability {
  id: LayerId;
  availableDates: string[]; // ISO date strings (YYYY-MM-DD)
}
```

### Port (interface)
```ts
// web/src/services/domain/layers/layerCatalog.ports.ts
import type { LayerId } from "./layer.types";

export interface LayerCatalogRepository {
  listLayers(): Promise<Array<{ id: string; name: string; kind: string; description?: string }>>;
  getAvailability(layerId: LayerId): Promise<{ dates: string[] }>;
}
```

### Service (use case)
```ts
// web/src/services/domain/layers/layerCatalog.service.ts
import type { LayerAvailability, LayerMeta, LayerId } from "./layer.types";
import type { LayerCatalogRepository } from "./layerCatalog.ports";

export class DomainError extends Error {
  constructor(public code: string, message: string) {
    super(message);
  }
}

export function createLayerCatalogService(deps: { repo: LayerCatalogRepository }) {
  return {
    async listLayerCatalog(): Promise<LayerMeta[]> {
      const raw = await deps.repo.listLayers();

      // DTO → Domain mapping (normalize kind)
      return raw.map((x) => ({
        id: x.id,
        name: x.name,
        kind: x.kind === "raster" || x.kind === "vector" || x.kind === "timeseries" ? x.kind : "vector",
        description: x.description,
      }));
    },

    async getLayerAvailability(layerId: LayerId): Promise<LayerAvailability> {
      if (!layerId?.trim()) throw new DomainError("INVALID_LAYER_ID", "layerId is required");

      const { dates } = await deps.repo.getAvailability(layerId);

      // Guard: keep only valid ISO-like dates
      const safeDates = (dates ?? []).filter((d) => /^\d{4}-\d{2}-\d{2}$/.test(d));

      return { id: layerId, availableDates: safeDates };
    },
  };
}
```

### Usage (store/controller)
```ts
// Pseudo example (Redux thunk, controller, or any caller)
// The caller wires infrastructure, then calls the domain.
import { createLayerCatalogService } from "@/services/domain/layers/layerCatalog.service";
import { layerCatalogRepo } from "@/services/api/layers/layerCatalogRepo"; // infra adapter

const layerDomain = createLayerCatalogService({ repo: layerCatalogRepo });

// Later...
const catalog = await layerDomain.listLayerCatalog();
```

---

## 🧠 Practical KFM domain use cases to expect here

These are examples of the kinds of “use cases” that belong in this folder:

- 🛰️ **Remote sensing layers**
  - list available NDVI layers by date
  - resolve raster tiles endpoint + metadata
  - request prefetch of adjacent dates for smooth timeline playback

- 🌦️ **Weather + climate**
  - get field-level weather summaries for selected time range
  - merge NOAA-like feeds with local sensor data (client-side normalization only)

- 🌱 **Fields & soil**
  - fetch field boundary + soil attributes
  - compute quick client-side derived stats (min/max/avg) for display

- 🤖 **Predictions**
  - request model inference result + uncertainty metadata
  - map backend responses into “explainable” domain objects for UI

- 🧪 **Scenarios / simulation runs**
  - submit scenario job
  - poll job status with backoff
  - hydrate final outputs into map layers + charts

---

## 🧰 Testing strategy

### Unit tests (preferred)
Domain services should be testable with **mock ports**:

```ts
import { createLayerCatalogService } from "../layers/layerCatalog.service";

test("maps repo DTOs into domain LayerMeta", async () => {
  const service = createLayerCatalogService({
    repo: {
      listLayers: async () => [{ id: "ndvi", name: "NDVI", kind: "raster" }],
      getAvailability: async () => ({ dates: ["2025-03-01"] }),
    },
  });

  const catalog = await service.listLayerCatalog();
  expect(catalog[0].kind).toBe("raster");
});
```

### Integration tests (optional)
Run against a dev API only outside unit test scope (CI can do this if configured).

---

## 🧭 Conventions & standards

- **TypeScript strict** ✅  
  Avoid `any`; model API responses as DTOs, and transform into domain types.
- **Naming**
  - `*.service.ts` → domain use case
  - `*.ports.ts` → interfaces/ports
  - `*.types.ts` → domain types
- **Exports**
  - `index.ts` should re-export public domain services (no deep import spelunking).
- **No UI imports**
  - Nothing in domain should import from `components/`, `features/`, `pages/`.

---

## 🧾 Checklist for adding a new domain service

- [ ] Create a folder under `services/domain/<subdomain>/`
- [ ] Define **ports** (`*.ports.ts`) first (what do we need from infra?)
- [ ] Define **types** (`*.types.ts`) (stable domain model)
- [ ] Implement service (`*.service.ts`) with small, focused functions
- [ ] Add tests with mocked ports ✅
- [ ] Export from `services/domain/index.ts`
- [ ] Add/refresh docs here (examples + edge cases)

---

## 🔍 FAQ

<details>
  <summary><strong>Why not call the API directly from components?</strong></summary>

Because it couples UI to infrastructure and spreads business rules everywhere.  
Domain services centralize workflows (validation, mapping, caching, throttling) so UI stays lean and consistent.

</details>

<details>
  <summary><strong>Where do DTO validators go (Zod, io-ts, custom guards)?</strong></summary>

Put validators at the boundary. If you use a runtime validator, keep it in `services/domain/_shared/guards.ts`  
or alongside the DTO mapper in the relevant subdomain. Domain types should remain stable.

</details>

<details>
  <summary><strong>Where should auth token handling live?</strong></summary>

Token storage and refresh mechanics are **infrastructure concerns**.  
Domain services may depend on a `TokenProvider` port, but should not touch `localStorage` directly.

</details>

---

## 🔗 Related docs

- 🧱 Architecture principles: Clean layers, dependency inversion, and use-case separation  
- 🗺️ Frontend concepts: React + state management + map/timeline performance considerations  
- 🔐 Security: JWT handling, role-based access, and request discipline  

> If you’re looking for the deeper “why”, start with the project’s master technical documentation (KFM Comprehensive Technical Documentation & Markdown Guide) and the frontend architecture sections.