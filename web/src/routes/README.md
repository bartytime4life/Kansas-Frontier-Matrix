# 🧭 `web/src/routes/` — KFM Route System

![React](https://img.shields.io/badge/React-SPA-61DAFB?style=flat-square&logo=react&logoColor=000)
![TypeScript](https://img.shields.io/badge/TypeScript-Strict-3178C6?style=flat-square&logo=typescript&logoColor=fff)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20Maps-2E7D32?style=flat-square)
![Cesium](https://img.shields.io/badge/Cesium-3D%20Globe-1E88E5?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-Governed%20API-009688?style=flat-square&logo=fastapi&logoColor=fff)

> **Purpose:** This folder contains the **page-level routes**, **nested layouts**, and **route-specific loading / error boundaries** for the Kansas Frontier Matrix (KFM) web UI.

KFM is explicitly designed to be **evidence-first** and **traceable** (“the map behind the map”)—so routes aren’t just navigation; they are **governance + reproducibility + permalinks** for maps, timelines, stories, and AI Focus Mode.  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧠 Quick Nav

- [Why routes matter in KFM](#-why-routes-matter-in-kfm)
- [What belongs here](#-what-belongs-here--what-doesnt)
- [Canonical route map](#-canonical-route-map)
- [URL state & permalinks](#-url-state--permalinks)
- [Data loading contract](#-data-loading-contract)
- [Adding a new route checklist](#-adding-a-new-route-checklist)
- [References](#-references)

---

## 🧬 Why routes matter in KFM

### ✅ The “Truth Path” (non‑negotiable)

KFM’s architecture enforces a strict pipeline:

**Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI**

…and **no component bypasses this truth path**. Concretely: **the web UI must not query databases directly**; it goes through the governed API.  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

This folder exists to keep that contract clear at the **UI boundary**.

### 🗺️ Where routes sit in the stack

KFM is a multi-tier system: ingestion → stores (PostGIS/Neo4j/search) → **FastAPI service layer** → UI (React) with MapLibre (2D) and Cesium (3D), plus “Focus Mode” AI tooling—guarded by governance gates (e.g., policy enforcement).  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

```mermaid
flowchart LR
  U[👤 User] --> R[🧭 Route / Page]
  R --> S[🧩 UI State (time/layers/selection)]
  R --> L[📦 Route Loader / Fetch]
  L --> API[🌐 FastAPI (Governed API)]
  API --> DB[(🗃️ PostGIS / Neo4j / Search)]
  API --> AI[🤖 Focus Mode Orchestrator]
  AI --> LLM[🧠 Ollama / LLM Runtime]
```

---

## 📦 What belongs here ✅ / What doesn’t ❌

### ✅ Belongs in `web/src/routes/`
- **Page shells** (layout, major panels, top-level composition)
- **Route guards** (auth-required pages, admin-only pages)
- **Route-level data loading** (query params → API calls → view models)
- **Error boundaries** and **loading states** for pages
- **Canonical URL definitions** (paths + required search params)
- **Permalink behavior** (deep-link map state, story position, filters)

### ❌ Does NOT belong in `web/src/routes/`
- Direct DB connections or “clever” side channels (**UI → DB is forbidden**)  [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Geospatial transformation pipelines (those live in ingestion/processing)
- Business logic duplicated from the API layer
- “Secret” state that can’t be represented in the URL (avoid non-shareable UX)

---

## 🗂️ Folder expectations (repo alignment)

The repository is organized with a top-level `web/` app alongside `docs/`, `src/`, `tools/`, etc.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

A typical shape for this folder (adjust to your router implementation):

```text
📁 web/
  📁 src/
    📁 routes/              👈 you are here
      📄 README.md
      📄 (root route / app shell)   # depends on router choice
      📁 map/
      📁 timeline/
      📁 stories/
      📁 datasets/
      📁 focus/
      📁 admin/
```

> ⚙️ Router note: KFM may be configured as a single-page map app or as multiple pages. If using React Router, routing may be defined in something like `web/src/App.tsx` with page components referenced from here.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 Canonical route map

> **Keep this table updated** whenever routes change. It’s the UI’s “navigation contract” for developers and designers.

| Route | Type | Primary job | URL State (minimum) | Backend/API touchpoints |
|---|---|---|---|---|
| `/` | 🏠 Landing | Default entry (often map-first) | `?view=` optional | tiles + catalog search |
| `/map` | 🗺️ Map Workspace | 2D/3D map, layers, selection | `bbox`, `time`, `layers`, `view=2d|3d` | map tiles endpoints (vector/raster) [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) |
| `/timeline` | ⏳ Time Navigator | Animate/step through time | `time`, `speed` | catalog search by time; story nodes |
| `/stories` | 📚 Index | Browse story modules | `q`, `tags` | story endpoints (REST/GraphQL) |
| `/stories/:storySlug` | 🧵 Story Player | Story + synchronized map/time | `section`, `time`, `bbox` | story nodes + related layers |
| `/datasets` | 🗃️ Catalog | Search datasets + metadata | `q`, `bbox`, `time` | `GET /api/v1/catalog/search` [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) |
| `/datasets/:datasetId` | 🧾 Dataset Detail | DCAT/STAC summary + assets | `tab` | `GET /api/v1/datasets/{id}` [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) |
| `/datasets/:datasetId/data` | 🧪 Data Preview | Sample/filtered data preview | `format`, `bbox`, filters | `GET /api/v1/datasets/{id}/data?...` [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) |
| `/focus` | 🎯 Focus Mode | Evidence-grounded Q&A | `thread`, `mode` | UI calls backend endpoint (e.g. `/focus-mode/query`) [oai_citation:10‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) |
| `/admin` | 🛡️ Governance | review gates, moderation | n/a | governed admin endpoints |
| `*` | 🚧 Not Found | helpful recovery | n/a | none |

### 🗺️ Map notes (2D & 3D)

KFM’s UI uses:
- **MapLibre GL JS** for 2D vector/raster layers, typically pulling tiles/GeoJSON from the API.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **CesiumJS** for optional 3D globe/terrain visualization.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

The prototype direction emphasizes MapLibre with a **timeline slider** for time-slice animation.  [oai_citation:13‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## 🔗 URL state & permalinks

> If a user can *see it*, they should be able to *bookmark it*. ✅

### Recommended “permalink spec” (map-centric)
Use **search params** as the canonical source of truth for shareable state:

- `view=2d|3d`
- `bbox=minLon,minLat,maxLon,maxLat`
- `time=YYYY` or `time=YYYY-MM-DD/YYYY-MM-DD`
- `layers=layerA,layerB,layerC`
- `opacity.layerA=0.6` (optional pattern)
- `selected=feature:<id>` or `selected=place:<id>`
- `story=:storySlug` + `section=:sectionId` (when story-synced)

**Rule of thumb:** local UI state is fine for ephemeral UI (open/closed panels), but map + time + selection should be URL-driven.

---

## 🌐 Data loading contract

### 1) Routes call the API, not the DB ✅
KFM explicitly routes all access through a governed API layer.  [oai_citation:14‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

Common endpoints referenced by the architecture docs:

- Dataset metadata: `GET /api/v1/datasets/{id}` [oai_citation:15‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Dataset search: `GET /api/v1/catalog/search` [oai_citation:16‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Dataset data stream: `GET /api/v1/datasets/{id}/data?format=...&bbox=...` [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Tiles (vector/raster):  
  - `GET /tiles/{layer}/{z}/{x}/{y}.pbf`  
  - `GET /tiles/{layer}/{z}/{x}/{y}.png` [oai_citation:18‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 2) Focus Mode is API-orchestrated ✅
The UI should **not** call the LLM runtime directly. Focus Mode is designed so the **front-end calls a backend endpoint** (e.g., `/focus-mode/query`) and the API orchestrates retrieval from knowledge stores + answer generation.  [oai_citation:19‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 3) REST + GraphQL (if enabled)
The backend is described as supporting REST and potentially GraphQL for flexible queries; keep route-level data access consistent and centralized via an `apiClient` (or equivalent) abstraction.  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧩 State management expectations

KFM’s UI is expected to synchronize map/time/story panels through shared state (a global store such as Redux is suggested in the docs).  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Route design rule:**  
If global state changes should be shareable/replayable → mirror it in the URL (and hydrate the store from the URL on navigation).

---

## 🧯 Error boundaries & “failure as UX”

Routes should be defensive and helpful:

- **404**: show recovery actions (back to map, search datasets, open stories index)
- **403**: show governance/policy explanation and where to request access
- **5xx**: show retry + diagnostics link (status page route if present)
- **Offline**: allow cached basemap + last-known state where feasible

---

## 🛡️ Guards & governance

Even though enforcement is server-side, routes should:
- hide admin-only navigation unless authorized
- avoid rendering “restricted dataset” views without access
- prefer optimistic UI that degrades gracefully (don’t leak details)

---

## 🧪 Adding a new route checklist

> The fastest way to keep KFM coherent is to treat every route like a mini‑product. ✨

- [ ] **Name & purpose**: choose a stable, human-friendly URL (`/stories/:storySlug`, `/datasets/:datasetId`)
- [ ] **Define URL state**: list required search params + defaults
- [ ] **Loader**: implement route-level data fetching via API client
- [ ] **Caching**: add prefetch hints for adjacent views (e.g., dataset detail → preview)
- [ ] **Error UX**: 404/403/empty states + retry
- [ ] **A11y**: page title, headings, focus management, keyboard nav
- [ ] **Telemetry**: route-view event + performance marks (optional)
- [ ] **Docs**: update the [Canonical route map](#-canonical-route-map)

---

## 📚 References

**Project architecture & governance context**
-  [oai_citation:22‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) Kansas Frontier Matrix Comprehensive System Documentation (evidence-first + truth path + API boundaries)  [oai_citation:23‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
-  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) KFM Comprehensive Technical Blueprint (UI stack, MapLibre/Cesium notes, routing mention)  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Repo / markdown standards**
-  [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) MARKDOWN_GUIDE_v13 (repo layout incl. `web/`)  [oai_citation:27‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**UI mapping direction**
-  [oai_citation:28‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H) Open-Source Geospatial Historical Mapping Hub Design (MapLibre + timeline slider concept)  [oai_citation:29‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
