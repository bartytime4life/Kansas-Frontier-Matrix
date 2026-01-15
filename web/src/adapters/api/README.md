<div align="center">

# 🔌 API Adapters (`web/src/adapters/api`)  
**The Web UI’s single, governed “network boundary”** — typed clients, provenance-safe payloads, predictable errors ⚖️🧾

![Contract First](https://img.shields.io/badge/contract--first-required-1f6feb?style=flat)
![Evidence First](https://img.shields.io/badge/evidence--first-STAC%2FDCAT%2FPROV-3fb950?style=flat)
![TypeScript](https://img.shields.io/badge/TypeScript-ready-3178c6?style=flat)
![React](https://img.shields.io/badge/React-SPA-61dafb?style=flat)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20maps-000000?style=flat)
![Cesium](https://img.shields.io/badge/CesiumJS-3D%20globe-0b5fff?style=flat)

</div>

> [!IMPORTANT]
> **Everything the UI shows must be reachable through the API boundary** (contracts + redaction) — never via “side channels” or hidden data files. This folder exists to make that rule easy to follow. 🧭🛡️

---

## 🧩 What this folder is

This folder contains the **outbound adapters** the Web UI uses to call KFM backend APIs and convert responses into UI-ready data structures — while preserving **provenance (STAC/DCAT/PROV)** and enforcing **contract-first** behavior.  
It’s how we keep React components focused on **presentation + interaction**, not HTTP mechanics, caching rules, or error taxonomy. 🧠➡️🎛️

KFM’s architecture emphasizes isolating domain/service logic from infrastructure details via interfaces & adapters (ports/adapters). This folder is the **front-end equivalent**: a strict boundary between “UI intent” and “network reality.” 🧱🔌[^kfm_arch][^hexagonal][^layers]

---

## 🧭 Where this sits in the KFM pipeline

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode** 🧾🧩🛡️🗺️📚🔍[^pipeline]

This means:

- The UI is **not** allowed to bypass backend governance (contracts, redaction, classification).[^md_homes][^evidence_api]
- The UI should **surface provenance** for what it displays (the “map behind the map” concept).[^provenance_ui]

```mermaid
flowchart LR
  UI[🧑‍💻 React UI] --> AD[🔌 API Adapters<br/>web/src/adapters/api]
  AD -->|HTTP| API[🛡️ API boundary<br/>src/server]
  API --> S[🧠 Service layer]
  S --> D[📦 Domain]
  API --> CAT[🧾 STAC/DCAT/PROV catalogs]
  API --> G[🧩 Graph (Neo4j)]
  API --> DS[(🗄️ Data stores)]
  API --> AD
  AD --> UI
```

---

## ✅ What belongs here (and what doesn’t)

### ✅ Belongs here
- **A single HTTP client** (base URL, headers, auth injection, timeouts, retries, request IDs)
- **Resource-focused adapters** (catalog, features, graph, timelines, stories, downloads)
- **Runtime validation + normalization** (shape checking, decoding GeoJSON, paging tokens)
- **Caching + request coalescing** (avoid “thundering herd” on the same endpoint)
- **Provenance pass-through** (keep STAC/DCAT/PROV refs attached to responses)

### ❌ Does NOT belong here
- React components / hooks UI logic (belongs in UI layers)
- Business rules / “interpretation” logic (belongs server-side service layer or governed narratives)
- Direct database queries, hidden JSON files, or third-party API calls that bypass `src/server`[^md_homes]
- Any workaround that could leak sensitive data or bypass redaction[^redaction_ui]

---

## 🧱 Core design principles

### 1) Contract-first (always)
Backend contracts live in **`src/server/`** (OpenAPI, GraphQL, etc.). The UI’s job is to call those contracts — not invent its own parallel API surface.[^md_homes][^contract_tests]

**Rule of thumb:** If you can’t point to a server contract, you can’t ship a new adapter. ✅

### 2) Evidence-first / provenance-first
Every dataset and derived artifact is expected to have **STAC + DCAT + PROV** metadata, and PROV is explicitly required for transparency and reproducibility.[^stac_dcat_prov]  
On the UI side, adapters should make it easy for components to display:

- source attribution
- license/constraints
- processing lineage
- “confidence / uncertainty” flags (where available)

…and never drop those fields “because they’re annoying.” 🧾✨

### 3) Layer isolation (keep change cheap)
Layered architectures stay maintainable when responsibilities are isolated — presentation shouldn’t depend on persistence details, etc.[^layers][^isolation]

In practice: **React components call adapter functions**, not `fetch()` directly.

### 4) “One fact, one place”
The same principle shows up in performance/optimization literature: centralize the “truth” needed to operate efficiently and predictably. Apply it here by centralizing:
- base URL
- auth + headers
- error mapping
- retry policy
- caching strategy

(That’s why this folder exists. 🙂)

---

## 📁 Suggested directory layout

> [!NOTE]
> The exact filenames can vary — the important part is the separation: **client core** vs **resource adapters**.

```text
📁 web/src/adapters/api/
├─ 📄 README.md
├─ 📁 client/
│  ├─ 📄 httpClient.ts           # fetch wrapper: timeouts, headers, retries, trace IDs
│  ├─ 📄 errors.ts               # ApiError + error mapping
│  ├─ 📄 types.ts                # shared envelope + provenance types
│  └─ 📄 cache.ts                # TTL cache + in-flight promise cache
├─ 📁 resources/
│  ├─ 📄 catalog.ts              # STAC/DCAT discovery + dataset metadata
│  ├─ 📄 features.ts             # GeoJSON / OGC API Features-style queries
│  ├─ 📄 graph.ts                # entity graph queries (via backend)
│  ├─ 📄 stories.ts              # Story Nodes + Focus bundles
│  ├─ 📄 tiles.ts                # vector/3D tiles URLs + signed asset access
│  └─ 📄 downloads.ts            # export endpoints (CSV/GeoJSON/TIFF/etc.)
└─ 📄 index.ts                   # public exports
```

---

## 📦 Recommended request/response shape

### Response envelope (recommended)
KFM expects cross-layer linkage between catalogs/graph/UI — e.g., graph nodes reference catalog IDs rather than duplicating bulky data.[^catalog_linkage]  
To support that, treat “data” and “provenance” as first-class:

```ts
export type ApiEnvelope<T> = {
  data: T;

  // ✅ provenance / governance
  provenance?: {
    stac?: string[];  // STAC Item/Collection IDs
    dcat?: string[];  // DCAT dataset IDs
    prov?: string[];  // PROV bundle IDs
    citations?: Array<{ label: string; href?: string }>;
    licenses?: string[];
  };

  // ✅ operational context
  warnings?: Array<{ code: string; message: string }>;
  paging?: { next?: string; prev?: string; total?: number };

  // ✅ traceability
  requestId?: string;
};
```

### Error shape (recommended)
```ts
export type ApiError = {
  name: "ApiError";
  status: number;
  message: string;
  code?: string;
  requestId?: string;   // correlate logs across UI/server
  details?: unknown;    // safe-to-display, already redacted
};
```

---

## 🗺️ Geospatial + “big data” patterns (KFM-specific)

KFM’s UI stack is explicitly map-heavy: **React + TypeScript**, with **MapLibre GL JS** for 2D and **CesiumJS** for 3D, and an expectation that users can inspect provenance for visible layers/features.[^provenance_ui]

### 1) Prefer bounded queries (BBox, time window, filters)
KFM’s Integration Layer example calls out interfaces like `get_features_in_bounds(area)` — that’s the shape we want from frontend adapters too: ask for **what’s on screen**, not “give me Kansas.”[^kfm_arch]

### 2) Stream large raster data (COGs) + tile heavy layers
KFM’s design notes emphasize **Cloud-Optimized GeoTIFFs (COGs)** enabling partial reads via **HTTP range requests**, and optionally pre-generated tiles for performance.[^cogs]

Adapters should:
- request tiles/COG ranges via backend endpoints (signed URLs, range support)
- avoid downloading entire multi‑GB rasters
- expose a “tile URL template” or “asset URL” rather than the whole file

### 3) Standards-aware endpoints (OGC / STAC-ish)
KFM may support (or align toward) interoperability patterns like **OGC API - Features**, WMS/WFS, and STAC-like item endpoints.[^ogc]  
Adapters should keep these conventions obvious:
- `listCollections()`
- `listItems(collectionId, { bbox, datetime, limit })`
- `getItem(collectionId, itemId)`

---

## ⚡ Caching & request coalescing (don’t DDOS our own API)

### In-flight coalescing: cache the *promise*
When multiple components request the same resource, cache the **promise** so parallel calls share a single network request — and invalidate on error.[^promise_cache]

```ts
let cachedPromise: Promise<ApiEnvelope<any>> | null = null;

export function fetchOnce(fn: () => Promise<ApiEnvelope<any>>) {
  if (!cachedPromise) {
    cachedPromise = fn().catch((e) => {
      cachedPromise = null; // invalidate so next call can retry
      throw e;
    });
  }
  return cachedPromise;
}
```

### Windowed caching (TTL / eviction)
When caching expensive results, keep a bounded cache and evict when full — a common technique when intermediate results are reusable but memory isn’t infinite.[^cache_window]

---

## 📈 Telemetry + performance mindset

This folder is the best place to add:
- request IDs / correlation IDs
- simple timing metrics (start/end)
- lightweight retry/backoff counters
- cache hit rates

Why we care: user-facing apps usually need to protect latency at realistic throughput (P95/P99), not chase max throughput at any cost.[^benchmark]  
Also, workloads differ (read-heavy vs mixed vs batch-vs-realtime), and the client’s behavior (polling, infinite scroll, map pan/zoom storms) can *create* pathological patterns.[^workload_ratio]

> [!TIP]
> If you change adapter behavior (paging defaults, cache TTL, retry policy), treat it like a performance experiment: measure, compare, and document.

---

## 🔐 Security & governance guardrails

- **Respect redaction**: UI must not leak sensitive data or bypass redaction rules (e.g., “zoom in farther than allowed”).[^redaction_ui]
- **No direct artifact access**: evidence artifacts must be exposed via governed APIs; hard-coding artifacts or direct access is explicitly disallowed.[^evidence_api]
- **Audit friendliness**: track operations/lineage at the system level for audit and traceability — adapters should preserve IDs that make audits possible.[^lineage_audit]

---

## 🧰 Adding a new adapter (checklist)

> [!IMPORTANT]
> Build from the contract. If the endpoint isn’t in `src/server/contracts/`, start there. ✅[^md_homes][^contract_tests]

### Step-by-step
- [ ] 📜 **Define/extend the API contract** (OpenAPI/GraphQL) in `src/server/contracts/`
- [ ] 🛠️ Implement the backend endpoint (including redaction + classification)
- [ ] 🔌 Add a new function in `web/src/adapters/api/resources/<domain>.ts`
- [ ] 🧾 Ensure **provenance fields** are preserved (STAC/DCAT/PROV references)
- [ ] 🧪 Add tests (mocked fetch + contract fixtures)
- [ ] 🧭 Update docs (link to endpoint usage + UI behavior)

---

## 🧭 Example adapter pattern (geospatial routing)

A geospatial API style often looks like: `.../api/directions/<start>&<end>` with coordinates embedded in the path (or query).[^route_example]  
In KFM we usually prefer explicit query params (easier caching + observability), but either way the adapter should:

- validate coordinates
- normalize output to GeoJSON
- attach provenance/citations where available

```ts
export async function getDirections(params: {
  start: { x: number; y: number; floor?: number };
  end: { x: number; y: number; floor?: number };
}): Promise<ApiEnvelope<{ geojson: GeoJSON.FeatureCollection }>> {
  // build URL safely, call httpClient, validate response, return envelope
  throw new Error("Implement against src/server contract");
}
```

---

## 📚 Project reference shelf (all project files)

> [!NOTE]
> This is the shared “library” informing our implementation standards — performance, mapping, governance, stats, security, and ethics. (Listed here so contributors know what materials the project is grounded in.)

<details>
<summary><b>📖 Click to expand the full library list</b></summary>

### 🧱 Architecture, governance, and KFM blueprint
- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**  
- 📗 **MARKDOWN_GUIDE_v13.md.gdoc** (pipeline + contract-first + evidence-first)

### 🗺️ GIS, mapping, remote sensing, and visualization
- 🛰️ Cloud-Based Remote Sensing with Google Earth Engine — Fundamentals and Applications.pdf  
- 🗺️ making-maps-a-visual-guide-to-map-design-for-gis.pdf  
- 📍 Mobile Mapping: Space, Cartography and the Digital.pdf  
- 🧭 python-geospatial-analysis-cookbook.pdf  
- 🧱 Archaeological 3D GIS_26_01_12_17_53_09.pdf  
- 🎮 webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf  
- 🧩 compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf  

### ⚡ Performance, data systems, and databases
- 🗄️ Database Performance at Scale.pdf  
- 🧠 Scalable Data Management for Future Hardware.pdf  
- 🧱 Data Spaces.pdf  
- 🐘 PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf  

### 📊 Statistics, modeling, simulation, and ML literacy
- 📈 regression-analysis-with-python.pdf  
- 📊 Regression analysis using Python - slides-linear-regression.pdf  
- 🧪 Understanding Statistics & Experimental Design.pdf  
- 📉 graphical-data-analysis-with-r.pdf  
- 🎲 think-bayes-bayesian-statistics-in-python.pdf  
- 🚀 Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf  
- 🧬 Principles of Biological Autonomy.pdf  
- 🧮 Spectral Geometry of Graphs.pdf  
- 🏗️ Generalized Topology Optimization for Structural Design.pdf  
- 🤖 Deep Learning for Coders with fastai and PyTorch (file present in project assets)

### 🔐 Security and adversarial thinking
- 🛡️ ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf  
- 🕵️ Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf  

### ⚖️ Humanistic + legal/ethical context
- 🧠 Introduction to Digital Humanism.pdf  
- ⚖️ On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf  

### 📚 General programming references (multi-book compendiums)
- 📦 A programming Books.pdf  
- 📦 B-C programming Books.pdf  
- 📦 D-E programming Books.pdf  
- 📦 F-H programming Books.pdf  
- 📦 I-L programming Books.pdf  
- 📦 M-N programming Books.pdf  
- 📦 O-R programming Books.pdf  
- 📦 S-T programming Books.pdf  
- 📦 U-X programming Books.pdf  

</details>

---

## 🔎 Sources (grounding excerpts used in this README)

[^kfm_arch]: KFM describes a clean architecture with Domain, Service, Integration (interfaces/adapters), and Infrastructure layers; Integration includes interfaces like “get features in bounds” and decouples core logic from external systems.:contentReference[oaicite:0]{index=0}

[^hexagonal]: Data Spaces describes microservices as hexagonal architectures placing business logic at the center with inbound adapters and outbound adapters/controllers for external interactions.:contentReference[oaicite:1]{index=1}

[^layers]: Layered architecture benefits: separation of concerns and well-defined layer responsibilities help development, testing, and maintainability.:contentReference[oaicite:2]{index=2}

[^isolation]: Closed layers and “layers of isolation” reduce coupling and isolate change across the system.:contentReference[oaicite:3]{index=3}

[^md_homes]: Canonical subsystem homes: server API code + contracts live in `src/server/`, while the UI in `web/` relies on the API and contains no hidden data files or direct DB queries.:contentReference[oaicite:4]{index=4}

[^pipeline]: Canonical pipeline ordering (ETL → catalogs → graph → APIs → UI → narratives/focus); no stage bypasses earlier contracts/outputs.:contentReference[oaicite:5]{index=5}

[^stac_dcat_prov]: STAC/DCAT/PROV alignment policy: every dataset/evidence artifact must have STAC + DCAT + PROV, and PROV is emphasized for transparency/reproducibility.:contentReference[oaicite:6]{index=6}

[^catalog_linkage]: Cross-layer expectation: graph references catalog entries instead of duplicating data, enabling UI retrieval through catalogs/APIs.:contentReference[oaicite:7]{index=7}

[^evidence_api]: Evidence artifacts must be exposed through governed APIs; direct access or hard-coding in the UI is not allowed.:contentReference[oaicite:8]{index=8}

[^redaction_ui]: UI must not cause data leakage and must respect redaction rules and audit requirements.:contentReference[oaicite:9]{index=9}

[^provenance_ui]: KFM UI stack (React/TypeScript + MapLibre + Cesium) and the requirement to maintain provenance context for visible layers/features in the frontend.:contentReference[oaicite:10]{index=10}

[^cogs]: KFM remote sensing notes: Cloud-Optimized GeoTIFFs enable partial reads via HTTP range requests; heavy rasters can be pre-tiled for speed.:contentReference[oaicite:11]{index=11}

[^ogc]: KFM interoperability notes discuss OGC protocols and alignment toward OGC API - Features / STAC-like endpoint patterns.:contentReference[oaicite:12]{index=12}

[^promise_cache]: JavaScript guidance: caching the promise (not just the resolved result) can dedupe parallel requests; invalidate cached values on errors.:contentReference[oaicite:13]{index=13}

[^cache_window]: Scalable data management notes: caching results in a window and evicting when full can improve performance while controlling memory use.:contentReference[oaicite:14]{index=14}

[^workload_ratio]: Database performance framing: understanding read/write ratios and workload types is critical and commonly overlooked; poor fit becomes a major burden.:contentReference[oaicite:15]{index=15}

[^benchmark]: Benchmarking framing: decide whether you’re optimizing throughput or latency; user-facing systems often care about latency targets at a given throughput (P99/P99.99).:contentReference[oaicite:16]{index=16}

[^lineage_audit]: Data governance emphasis: tracking operations over data sources supports data lineage and a robust audit mechanism.:contentReference[oaicite:17]{index=17}

[^route_example]: Example of a directions API endpoint style with coordinates and sample request formatting.:contentReference[oaicite:18]{index=18}

[^contract_tests]: Contract expectations: APIs require specs + contract tests and compatibility guarantees; contract changes are tested against known inputs/outputs.:contentReference[oaicite:19]{index=19}


