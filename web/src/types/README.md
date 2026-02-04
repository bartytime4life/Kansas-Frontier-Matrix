# 🧩 `web/src/types` — Frontend Type System (KFM)

![TypeScript](https://img.shields.io/badge/TypeScript-%E2%9C%94%EF%B8%8F-informational)
![Contracts](https://img.shields.io/badge/API%20Contracts-%F0%9F%93%9C-blue)
![Geo](https://img.shields.io/badge/GeoJSON-%F0%9F%97%BA%EF%B8%8F-success)
![Provenance](https://img.shields.io/badge/Provenance-%F0%9F%A7%BE%20Evidence--First-critical)

> **Purpose:** This folder is the **single source of truth** for the **TypeScript types** used by the KFM web client.  
> It defines the **data contracts** we expect from the governed API layer (datasets, tiles, story nodes, AI answers + citations), plus the geo/time primitives the UI needs for mapping & timelines.

---

## 📌 Why this exists

KFM is an *evidence-first* mapping + knowledge platform: every map layer, chart, and AI answer should be traceable to sources (“map behind the map”).  
This folder ensures the **web UI stays honest** by making contracts explicit and reusable across the app.

✅ What good types buy us:
- **Fewer runtime surprises** (shape mismatches get caught at build time)
- **Stable API/UI integration** (especially for map tiles + catalog + story playback)
- **Citable AI UX** by modeling **citations and sources** as first-class structures
- **Cleaner components**: UI code renders data; types define what data *is*

---

## 🗂️ Suggested folder layout

> Your actual tree may differ — this README documents the **intended structure** and conventions.

```text
📁 web/src/types
├─ 📄 README.md
├─ 📄 index.ts                 # barrel exports (recommended)
├─ 📁 core
│  ├─ 📄 ids.ts                # branded IDs, enums, discriminators
│  ├─ 📄 time.ts               # TimeRange, ISO strings, timeline helpers
│  └─ 📄 errors.ts             # APIError, Result<T>, ProblemDetails
├─ 📁 geo
│  ├─ 📄 geojson.ts            # Feature, FeatureCollection, Geometry unions
│  ├─ 📄 bbox.ts               # BBox, LngLat, projections metadata
│  └─ 📄 tiles.ts              # tile template strings, tile formats
├─ 📁 catalog
│  ├─ 📄 dataset.ts            # Dataset metadata summary, assets, license, lineage
│  └─ 📄 search.ts             # search request/response payloads
├─ 📁 story
│  ├─ 📄 storyNode.ts          # story node schema (time, layers, citations, media)
│  └─ 📄 tags.ts               # story tags, categories
└─ 📁 ai
   ├─ 📄 focusMode.ts          # query/answer + citations map
   └─ 📄 provenance.ts         # audit payloads shown in “audit panel”
```

---

## 🧠 Type philosophy (rules we follow)

### 1) Types are contracts, not vibes ✍️
If the backend can return it, we must be able to **name it**, **type it**, and **version it** (when needed).

### 2) Prefer **domain types** over “anonymous blobs” 🧱
Avoid sprinkling `Record<string, any>` or “just JSON” throughout components.
Instead: define a type once → reuse everywhere.

### 3) Keep **boundary safety** in mind 🚧
TypeScript checks compile-time shapes. Real HTTP responses are `unknown`.
At API boundaries, prefer **runtime parsing/validation** (example patterns below).

### 4) Model provenance and citations explicitly 🧾
KFM’s UX depends on citations. If we don’t type citations, they’ll get “optional’d” into irrelevance.

---

## ✨ Naming & conventions

- **Types/Interfaces:** `PascalCase`  
  Example: `DatasetSummary`, `FocusModeAnswer`
- **Fields:** match the API payload shape (often `snake_case` in APIs; `camelCase` in UI)  
  - If API returns `snake_case`, keep it in **transport types** (e.g., `DatasetDTO`)  
  - Map to **UI-friendly types** (e.g., `Dataset`) in a dedicated mapper layer (`web/src/lib/mappers/*`)
- **Discriminated unions:** always include a discriminator like `kind` or `type`
- **IDs:** prefer branded types (`DatasetId`, `LayerId`) instead of plain `string`

---

## 🧱 Core primitives we expect in a mapping app

### 🌍 Geo primitives
```ts
export type LngLat = readonly [lng: number, lat: number];

export type BBox = readonly [
  minLng: number,
  minLat: number,
  maxLng: number,
  maxLat: number
];
```

### ⏳ Time primitives
```ts
export type ISODateString = string;      // "1935-04-12"
export type ISODateTimeString = string;  // "1935-04-12T10:15:00Z"

export interface TimeRange {
  start: ISODateString | ISODateTimeString;
  end: ISODateString | ISODateTimeString;
}
```

---

## 🗺️ Tiles & layers (web map contracts)

### Tile endpoints (conceptual)
We treat tile URLs as a *templated resource* the UI can render via MapLibre/Cesium.

```ts
export type TileFormat = "mvt" | "png" | "webp";

export interface TileTemplate {
  layer: string;             // layer id
  format: TileFormat;
  template: string;          // e.g. "/tiles/{layer}/{z}/{x}/{y}.pbf"
  attribution?: string;
}
```

### Layer definition (UI-friendly)
```ts
export type LayerKind = "vector" | "raster" | "story" | "analysis";

export interface MapLayer {
  id: string;
  kind: LayerKind;
  title: string;
  description?: string;
  time?: TimeRange;          // if time-enabled
  tile?: TileTemplate;       // if tile-backed
}
```

---

## 📚 Catalog & datasets (metadata-first)

Datasets should carry enough metadata for:
- discovery/search
- licensing & access decisions
- linking to assets (STAC-like)
- provenance display

```ts
export interface DatasetSummary {
  id: string;
  title: string;
  description?: string;
  license?: string;
  themes?: string[];
  spatial?: BBox;
  temporal?: TimeRange;
}
```

---

## 📖 Story nodes (narratives you can replay)

Story nodes should be able to:
- set map view (center/zoom)
- activate layers
- define time window
- include citations and media

```ts
export interface StoryNode {
  id: string;
  title: string;
  summary?: string;

  time?: TimeRange;
  center?: LngLat;
  zoom?: number;

  layers: string[]; // layer IDs
  citations?: CitationRef[];
  media?: StoryMedia[];
}
```

---

## 🤖 Focus Mode (AI) — typed citations or it didn’t happen

> **Rule:** if the AI claims something factual, it must carry citations that map back to sources.

```ts
export interface EvidenceSource {
  id: string;         // stable source id
  title: string;      // display name
  kind: "dataset" | "document" | "graph" | "story" | "other";
  uri?: string;       // optional deep-link (if safe to show)
  excerpt?: string;   // short snippet shown in audit panel
}

export interface CitationRef {
  marker: string;     // e.g. "[1]"
  sourceId: string;   // maps into `sources[]`
}

export interface FocusModeQuery {
  question: string;
  context?: {
    bbox?: BBox;
    time?: TimeRange;
    placeId?: string;
    activeLayerIds?: string[];
  };
}

export interface FocusModeAnswer {
  answer: string;               // markdown-safe text
  citations: CitationRef[];     // structured mapping
  sources: EvidenceSource[];    // displayable sources list
  model?: { id: string; promptVersion?: string };
}
```

---

## 🧪 Boundary pattern: parse `unknown` into safe types

When fetching from the API:
1. Treat response as `unknown`
2. Validate/parse
3. Only then pass into components

### Minimal pattern (without a library)
```ts
export type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: string };

export function isTimeRange(x: any): x is TimeRange {
  return x && typeof x.start === "string" && typeof x.end === "string";
}
```

> If we adopt a runtime schema library (ex: Zod), put schemas next to types (same file or `*.schema.ts`) and export both.

---

## ✅ “What goes where?” (quick guide)

### Put **here** ✅
- API transport shapes (`DTOs`)
- Domain models used across multiple features
- Geo/time primitives
- AI citations + provenance structures
- Error/result types shared across hooks and services

### Do **not** put here ❌
- React component props *that are only used once*
- Styling tokens / CSS types
- Business logic (belongs in `lib/`, `services/`, `hooks/`)
- Mock data (belongs in `__mocks__/` or `fixtures/`)

---

## 🧭 Checklist for adding a new API feature

When you add or change an endpoint that the web UI consumes:

- [ ] Add/Update `DTO` type(s) in `types/`
- [ ] Add/Update domain model type(s) (if the UI wants a different shape)
- [ ] Add/Update mapper in `lib/mappers/`
- [ ] Add/Update fetcher in `services/` (or `api/`)
- [ ] Add/Update Story/AI/Layer typings if affected
- [ ] Ensure citations remain typed for any AI-facing output 🧾

---

## 📎 References (project + standards mindset)

- Kansas Frontier Matrix — Comprehensive System Documentation  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Professional Web Design: Techniques and Templates (context for design discipline & structure)  [oai_citation:1‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- Learn to Code HTML & CSS (front-end fundamentals & separation of concerns)  [oai_citation:2‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- Node.js (server/runtime context often shared by web tooling & build pipelines)  [oai_citation:3‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  

---

## 🧩 TODO hooks (optional next steps)

- Add `index.ts` barrel exports for stable imports (`import { TimeRange } from "@/types"`)
- Decide on runtime validation strategy (**Zod** recommended) and colocate schemas
- Add `ApiProblemDetails` / `RFC7807`-style errors for consistent failure handling
- Consider generating types from **OpenAPI/GraphQL** and layering domain models on top
