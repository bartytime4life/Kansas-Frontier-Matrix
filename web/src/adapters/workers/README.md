# 🧵 Workers Adapters (`web/src/adapters/workers`)

![TypeScript](https://img.shields.io/badge/TypeScript-ready-3178C6?logo=typescript&logoColor=white)
![Web Workers](https://img.shields.io/badge/Web%20Workers-dedicated%20%26%20shared-0A66C2)
![Service Worker](https://img.shields.io/badge/Service%20Worker-offline%20%26%20cache-2E7D32)
![Architecture](https://img.shields.io/badge/Architecture-Ports%20%26%20Adapters-6A1B9A)
![KFM](https://img.shields.io/badge/KFM-contract--first%20%26%20provenance--first-111827)

> **Purpose:** Keep the UI buttery-smooth 🧈 by pushing expensive work off the main thread **without breaking** Kansas Frontier Matrix’s “contract-first + provenance-first” rules.  
> This folder is our browser-side “adapters boundary” for **Dedicated Web Workers**, **Shared Workers** (optional), and **Service Workers**.

---

<details>
<summary>📌 TL;DR</summary>

- ✅ **Use Dedicated Web Workers** for CPU-heavy transforms (GeoJSON operations, raster stats, graph computations, large JSON parsing).
- ✅ **Use Service Workers** for offline-first caching, request routing, and background sync-like behaviors.
- ✅ **Everything here is an adapter**: it hides browser quirks + gives the rest of the app a clean, typed interface.
- ✅ **Contract-first**: worker messages are versioned + validated.
- ✅ **Provenance-first**: results include lineage metadata so nothing “mysteriously appears” in UI.

Sources: KFM architecture + “no mystery layers” principles:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}.
</details>

---

## 🧭 Where this folder fits in the KFM repo

`web/` is the **UI frontend** (browser) and should not do direct database access; it communicates through the backend API as the gatekeeper (the browser is treated as an untrusted boundary):contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}.

This `workers/` directory lives under **adapters** because it’s the “outbound infrastructure boundary” between:
- **UI/business code** that wants “do X” (ports)
- **browser worker runtimes** that actually execute X (adapters)

This aligns with KFM’s layered / clean architecture approach (domain ↔ service ↔ integration ↔ infrastructure) where adapters decouple core logic from specific implementations:contentReference[oaicite:4]{index=4} and with “hexagonal / ports & adapters” concepts (inbound/outbound adapters):contentReference[oaicite:5]{index=5}.

---

## 🎯 Design goals

### 1) 🧊 Zero-jank UI
Any task that risks blocking the main thread (maps + timeline + story rendering, large parsing, geometry crunching) belongs here.

### 2) 📜 Contract-first (message schemas + versioning)
KFM is explicitly contract-first and provenance-first:contentReference[oaicite:6]{index=6}. In practice, that means:
- **Typed request/response envelopes**
- **Schema versioning + backward-compat strategy**
- **Fail-fast on incompatible versions**

### 3) 🧾 Provenance-first outputs (no “mystery layers”)
Anything visible in UI must remain traceable to sources and processing steps:contentReference[oaicite:7]{index=7}.

### 4) 🧱 Progressive enhancement, not “perfect parity”
We target **functional parity** across browsers/devices, not pixel-perfect parity, using a support matrix mindset:contentReference[oaicite:8]{index=8}.

### 5) 🔒 Respect trust boundaries
Frontend is **untrusted**; validate server-side and keep data access through API boundaries:contentReference[oaicite:9]{index=9}.

---

## 🧩 Worker types we support

### 🧵 Dedicated Web Worker (default)
- Runs in its own thread (per instantiation).
- Communicates via `postMessage` (message passing):contentReference[oaicite:10]{index=10}.
- Can be terminated via `worker.terminate()` (main thread) or `self.close()` (worker):contentReference[oaicite:11]{index=11}.

✅ Best for: compute-heavy tasks.

### 🤝 Shared Worker (optional)
- Shared across multiple tabs/contexts (when supported).
- Use when cross-tab reuse matters.

### 🌐 Service Worker (offline-first + request mediation)
- Event-driven background script and a programmable network proxy (intercepts fetch, caching, etc.):contentReference[oaicite:12]{index=12}.
- Scope is determined by its file location; registration can happen on page load:contentReference[oaicite:13]{index=13}.
- Not terminated via `terminate()`; lifecycle is managed by the browser:contentReference[oaicite:14]{index=14}.

✅ Best for: offline-first caching and resilient loading behavior:contentReference[oaicite:15]{index=15}.

---

## 🗂️ Suggested folder layout

> This repo may differ — treat this as the target structure for consistency.

```text
📁 web/src/adapters/workers/
├─ 📄 README.md  ✅ you are here
├─ 📄 index.ts
├─ 📄 types.ts                 # request/response envelopes + shared types
├─ 📄 workerClient.ts          # main-thread adapter (promise API over postMessage)
├─ 📄 workerRegistry.ts        # “one fact, one place” registry of workers/tasks
├─ 📁 dedicated/
│  ├─ 🧵 geo.worker.ts
│  ├─ 🧵 raster.worker.ts
│  └─ 🧵 graph.worker.ts
└─ 📁 service/
   ├─ 🌐 register.ts
   └─ 🌐 sw.ts                 # service worker entry (scope-aware)
```

“Single source of truth” thinking is encouraged (avoid duplicated protocol definitions):contentReference[oaicite:16]{index=16}.

---

## 📦 Public API (what UI code should use)

UI code should not juggle raw `postMessage` calls everywhere. The adapter should expose **a small, typed surface** that reads like a normal async client.

Example (pseudo-code):

```ts
import { workers } from "./workerRegistry";

// “command”
await workers.geo.run("geo.simplify", {
  featureCollection,
  tolerance: 2.5,
});

// “query”
const stats = await workers.raster.query("raster.zonalStats", {
  polygon,
  band: 1,
});
```

> Why “command vs query”? It’s a useful framing in hexagonal/microservice design: commands “do”, queries “ask”:contentReference[oaicite:17]{index=17}.  
> In practice, both are messages — but the semantics help you design idempotency, caching, and retries.

---

## 📨 Message contract (recommended)

### ✅ Envelope
Every message should have:
- `id` (correlation)
- `v` (protocol version)
- `type` (`command` | `query` | `progress` | `result` | `error` | `cancel`)
- `name` (task name)
- `payload` (validated)
- `meta` (trace + provenance hooks)

```ts
export type WorkerEnvelope<TName extends string, TPayload> = {
  id: string;
  v: number; // bump on breaking changes
  type: "command" | "query" | "cancel" | "progress" | "result" | "error";
  name: TName;
  payload?: TPayload;
  meta?: {
    traceId?: string;
    requestedAt?: number;
    // provenance hooks: “what inputs produced this output?”
    provenance?: {
      inputIds?: string[];
      algorithm?: string;
      algorithmVersion?: string;
    };
  };
};
```

### 🧾 Provenance rule
If a worker produces derived data that could influence UI claims, it must include lineage metadata so the UI can remain “no mystery layers”:contentReference[oaicite:18]{index=18} and remain aligned with KFM’s evidence & lineage emphasis:contentReference[oaicite:19]{index=19}.

---

## 🧬 KFM-specific use cases (why we care)

KFM’s story mode uses **Markdown narrative + JSON step config** and drives map interactions (MapLibre/Cesium calls, layer toggles, camera moves). Focus Mode AI is a panel that answers questions **with references**:contentReference[oaicite:20]{index=20}.

Workers are ideal for:
- 📍 Precomputing story-step diffs (layers on/off, camera transitions)
- 🗺️ Heavy GeoJSON transforms (simplify, dissolve, bbox, adjacency graphs)
- 🧠 Preparing embeddings / local ranking over *already retrieved* sources (never fabricate)
- 🧱 Generating/validating map layer metadata + style summaries
- 🧵 Parsing and indexing large Markdown/JSON story packs

Also: keep map conventions consistent — color scales & symbology matter for user trust:contentReference[oaicite:21]{index=21}.

---

## ⚡ Performance patterns (do these by default)

### 1) 🧠 Cache + reuse work (when safe)
Caching + query/result reuse can yield big speedups in data systems:contentReference[oaicite:22]{index=22}. In workers, this maps to:
- memoizing parsed JSON / decoded tiles
- caching topology/graph structures
- caching simplification results keyed by `(datasetId, params, algorithmVersion)`

### 2) 🧩 Batch, chunk, and pool (avoid “one giant job”)
Scalable systems often break work into tasks and distribute them via a pool:contentReference[oaicite:23]{index=23}. In browser workers:
- Chunk large arrays/features into slices
- Post incremental progress events
- Consider a **worker pool** for parallelizable tasks (but keep concurrency controlled)

### 3) 🚦 Concurrency is not infinite
Even in high-performance systems: no system supports unlimited concurrency; too much concurrency drives latency up:contentReference[oaicite:24]{index=24}.  
In practice:
- Keep a hard cap on simultaneous jobs per worker type.
- Prefer queueing over spawning unlimited workers.

### 4) 📊 Measure what matters (P95/P99)
Performance work needs clarity about latency vs throughput tradeoffs:contentReference[oaicite:25]{index=25}.  
Minimum metrics to capture per task:
- total time
- time in queue
- transfer time (message overhead)
- compute time

---

## 🌙 Offline-first & caching (Service Worker adapter)

Offline-first aims for apps that still load/work without a network connection:contentReference[oaicite:26]{index=26}. Service workers are the key browser primitive here (install/activate lifecycle, cache API):contentReference[oaicite:27]{index=27}.

**Rules for our implementation:**
- ✅ Cache only what we can safely store (respect governance + sensitivity)
- ✅ Version caches (e.g., `kfm-v3-assets`, `kfm-v3-tiles`)
- ✅ Prefer “stale-while-revalidate” where appropriate
- ✅ Provide a kill-switch (feature flag) if caching causes issues

Scope matters: the file path controls which requests the service worker can intercept:contentReference[oaicite:28]{index=28}.

---

## 🎮 3D + WebGL notes (for Cesium-ish paths)

Workers don’t render WebGL directly (usually), but they **can prepare data**: geometry buffers, tiling metadata, simplification, etc.

Two important reminders from the WebGL ecosystem:
- Browser differences often require compatibility helpers (e.g., wrapper utilities that hide vendor differences):contentReference[oaicite:29]{index=29} — this is literally what adapters are for.
- WebGL contexts can be lost and restored; apps should handle context lifecycle events (`webglcontextlost`, `webglcontextrestored`):contentReference[oaicite:30]{index=30}.

---

## 🛡️ Security & trust (non-negotiable)

- 🔒 **No direct DB access from the browser.** Frontend is untrusted; funnel through API gatekeeper and validate server-side:contentReference[oaicite:31]{index=31}.
- 🧼 Treat worker messages like untrusted input: validate shapes/types before running heavy operations.
- 🧾 If you generate derived data used in narrative, include provenance metadata (dataset IDs, algorithm version):contentReference[oaicite:32]{index=32}.
- 🤖 If worker-backed features support Focus Mode AI, ensure it stays advisory-only and shows citations/labels as required:contentReference[oaicite:33]{index=33}.

---

## 🧪 Testing strategy

### ✅ Unit tests (fast)
- Message validation
- Determinism of transforms (same input → same output)
- Error serialization/deserialization

### 🔁 Integration tests (worker boundary)
- Spin up the real worker entry
- Send `command/query` messages
- Assert results + `progress` events + cancellation behavior

### 🧯 Regression tests (performance)
- Snapshot P95/P99 timings for key tasks
- Catch “accidental O(N²)” changes early

---

## ➕ Adding a new worker (checklist)

1) 🧠 Decide if it’s **Dedicated** (compute) or **Service** (offline/network).
2) 🧾 Define a **task name**: `domain.action` (e.g., `geo.simplify`).
3) 📜 Add request/response types in `types.ts` (versioned).
4) 🧵 Implement the worker entry:
   - validate input
   - emit progress events for long tasks
   - include provenance metadata in outputs
5) 🧩 Register it in `workerRegistry.ts` (single source of truth):contentReference[oaicite:34]{index=34}.
6) 🧪 Add tests.
7) 📝 Update this README if it introduces a new pattern.

---

## 📚 Project reference shelf (why we have so many docs 😄)

<details>
<summary>📖 Library Index (useful when designing worker tasks)</summary>

### 🧭 Core project specs
- :contentReference[oaicite:35]{index=35} **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf** (architecture, provenance, security boundaries)
- :contentReference[oaicite:36]{index=36} **MARKDOWN_GUIDE_v13.md.gdoc** (repo structure + governance + pipeline framing)

### 🌐 Web, UI, and progressive enhancement
- :contentReference[oaicite:37]{index=37} **responsive-web-design-with-html5-and-css3.pdf**
- :contentReference[oaicite:38]{index=38} **I-L programming Books.pdf** (JS workers/service workers notes)
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** (image processing background)

### 🗺️ GIS, mapping, and remote sensing
- :contentReference[oaicite:39]{index=39} **python-geospatial-analysis-cookbook.pdf**
- **making-maps-a-visual-guide-to-map-design-for-gis.pdf**
- **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf**
- **Archaeological 3D GIS_26_01_12_17_53_09.pdf**
- **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf**

### 🎮 3D/graphics
- :contentReference[oaicite:40]{index=40} **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf**

### 🗄️ Data systems & performance
- :contentReference[oaicite:41]{index=41} **Scalable Data Management for Future Hardware.pdf**
- :contentReference[oaicite:42]{index=42} **Database Performance at Scale.pdf**
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf**

### 📈 Stats / ML / experimental design (useful for analytic workers)
- **Understanding Statistics & Experimental Design.pdf**
- **think-bayes-bayesian-statistics-in-python.pdf**
- **regression-analysis-with-python.pdf**
- **Regression analysis using Python - slides-linear-regression.pdf**
- **graphical-data-analysis-with-r.pdf**

### 🧠 Graphs, optimization, simulation (possible heavy compute candidates)
- **Spectral Geometry of Graphs.pdf**
- **Generalized Topology Optimization for Structural Design.pdf**
- **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf**
- **Principles of Biological Autonomy - book_9780262381833.pdf**

### ⚖️ Governance, ethics, security (guardrails)
- **Introduction to Digital Humanism.pdf**
- **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf**
- **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** (defensive security mindset)
- **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** (defensive awareness; do not implement offensive patterns)

### 📚 Programming bundles
- **A programming Books.pdf**
- **B-C programming Books.pdf**
- **D-E programming Books.pdf**
- **F-H programming Books.pdf**
- **I-L programming Books.pdf**
- **M-N programming Books.pdf**
- **O-R programming Books.pdf**
- **S-T programming Books.pdf**
- **U-X programming Books.pdf**

</details>

---

## 🔎 Footnotes (source anchors)

[^kfm-arch]: KFM layered/clean architecture + adapters decouple core from specific implementations:contentReference[oaicite:43]{index=43}.  
[^kfm-contract]: KFM “contract-first + provenance-first” and “no mystery layers” for UI outputs:contentReference[oaicite:44]{index=44}.  
[^kfm-trust]: Frontend treated as untrusted; funnel through API; validate server-side:contentReference[oaicite:45]{index=45}.  
[^repo-web]: `web/` is UI frontend; avoid direct DB access; rely on API boundaries:contentReference[oaicite:46]{index=46}.  
[^lineage]: Evidence + lineage emphasis for derived products and narrative traceability:contentReference[oaicite:47]{index=47}.  
[^workers-postmsg]: Workers communicate via `postMessage`; termination options exist for dedicated workers:contentReference[oaicite:48]{index=48}:contentReference[oaicite:49]{index=49}.  
[^sw-proxy]: Service worker behaves like a programmable network proxy and is event-driven:contentReference[oaicite:50]{index=50}; scope depends on file location:contentReference[oaicite:51]{index=51}.  
[^offline-first]: Offline-first framing and service worker relevance:contentReference[oaicite:52]{index=52}.  
[^perf-cache]: Caching and reuse can produce large speedups; apply analogous thinking to worker results and intermediates:contentReference[oaicite:53]{index=53}.  
[^perf-concurrency]: Concurrency limits and latency/throughput framing (useful for worker pool design and perf targets):contentReference[oaicite:54]{index=54}:contentReference[oaicite:55]{index=55}.  
[^hex]: Hexagonal/ports-and-adapters framing and command/query semantics:contentReference[oaicite:56]{index=56}:contentReference[oaicite:57]{index=57}.  
[^webgl-compat]: WebGL compatibility helpers hide browser differences (adapter mindset):contentReference[oaicite:58]{index=58} and context loss/restoration needs handling:contentReference[oaicite:59]{index=59}.  
[^kfm-story]: Story mode + focus panel architecture context:contentReference[oaicite:60]{index=60}.  
[^kfm-visuals]: Map design conventions (color scales, symbology) should remain consistent:contentReference[oaicite:61]{index=61}.  
[^focus-mode]: Focus Mode AI constraints: advisory-only, citations/labels for outputs:contentReference[oaicite:62]{index=62}.


