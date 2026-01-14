# 🧵 Web Workers (`web/src/workers`)

![KFM](https://img.shields.io/badge/KFM-web%20ui-0b7285)
![Workers](https://img.shields.io/badge/threads-web%20workers-1c7ed6)
![Contracts](https://img.shields.io/badge/contracts-typed%20messages-f08c00)
![Provenance](https://img.shields.io/badge/provenance-first-7048e8)

KFM’s web UI is **map + narrative + analytics**. This folder exists so we can keep the UI smooth ✅ while crunching heavier tasks (geospatial transforms, graph ops, stats, image prep, etc.) in parallel.

> [!IMPORTANT]
> This folder is for **browser-side** Workers (Web Workers / module workers).  
> It is **not** the same thing as **backend pipeline/background workers** (e.g., Celery/queue workers, ETL jobs).

---

## 🧭 Table of contents

- [🎯 What belongs here](#-what-belongs-here)
- [🧱 Non-negotiables](#-non-negotiables)
- [🗂️ Suggested folder layout](#️-suggested-folder-layout)
- [📦 Worker inventory](#-worker-inventory)
- [🧾 Message contracts](#-message-contracts)
- [⚡ Performance patterns](#-performance-patterns)
- [🔒 Security & governance](#-security--governance)
- [🧪 Testing & reproducibility](#-testing--reproducibility)
- [➕ Adding a new worker](#-adding-a-new-worker)
- [📚 Project reference shelf](#-project-reference-shelf)

---

## 🎯 What belongs here

Workers are for **CPU-heavy** or **batchy** work that would otherwise freeze the main thread (scroll/zoom/drag/typing).

### ✅ Great worker jobs
- 🗺️ **Geospatial**: simplify/clip/merge vectors, build spatial indexes, compute clusters, precompute layer summaries.
- 🧠 **Graph**: compute connectivity, centrality-ish metrics, clustering/layout prep (when it’s safe to do client-side).
- 📊 **Analytics**: histograms, binning, regressions, Bayesian updates, Monte Carlo sampling (for *interactive* exploration).
- 🛰️ **Raster / remote sensing prep**: lightweight post-processing for visualization (color maps, stats, tiling prep).
- 🎨 **Rendering prep**: precompute geometry buffers, normalize/quantize attributes, decode/resize imagery for textures.

### ❌ Not worker jobs
- 🧾 **Creating “new truth”** (anything that should become an official dataset/evidence artifact)  
  → that belongs in governed pipelines & catalogs.
- 🔑 **Secrets / credentials** (tokens, API keys, anything sensitive)
- 🧱 **DOM work** (Workers don’t have DOM access)
- 🗄️ **Direct database access** (the UI must use the governed API boundary)
- 🧨 **Anything that must be “correct-by-construction” without validation** (run it in pipelines + tests)

---

## 🧱 Non-negotiables

KFM is built around **contract-first + provenance-first** workflows. Workers live *inside* the UI layer, so they must follow the same rules.

> [!CAUTION]
> **Workers may accelerate the UI, but they must not “leapfrog” governance.**  
> No worker should create a result that bypasses catalogs / provenance / API rules.

### Rules of thumb (for worker authors)
- ✅ **Only compute on inputs you were handed** (typically data fetched via the API + already redacted/governed).
- ✅ **Always return provenance metadata** for derived results (at minimum: input dataset IDs + processing step name).
- ✅ **Propagate sensitivity/classification tags**: outputs cannot be “less restricted” than inputs.
- ✅ **Prefer determinism**: same input + same config ⇒ same output (especially for analysis/simulation).
- ✅ **Graceful fallback**: if Workers aren’t available (or memory is tight), degrade to main thread *or* server compute.

---

## 🗂️ Suggested folder layout

> This is a **recommended** structure. If your bundler/tooling differs, adapt as needed.

```text
📁 web/
└─ 📁 src/
   └─ 📁 workers/
      ├─ 📄 README.md                 # 👈 you are here
      ├─ 📄 index.ts                  # (recommended) worker registry / exports
      ├─ 📁 _shared/
      │  ├─ 📄 types.ts               # shared message + error types
      │  ├─ 📄 codec.ts               # (optional) structured-clone safe helpers
      │  └─ 📄 trace.ts               # (optional) telemetry helpers
      ├─ 📁 geo/
      │  ├─ 📄 geo.worker.ts          # worker entry
      │  ├─ 📄 geo.client.ts          # main-thread wrapper
      │  └─ 📄 geo.ops.ts             # pure functions (testable)
      ├─ 📁 graph/
      ├─ 📁 stats/
      └─ 📁 media/
```

---

## 📦 Worker inventory

Keep this table updated. It becomes our “map” of what runs off-thread.

| Worker | Purpose | Ops (examples) | Output type | Deterministic? | Provenance fields |
|---|---|---|---|---:|---|
| `geo` | map-layer prep | `simplify`, `cluster`, `bbox` | GeoJSON + indexes | ✅ | `inputs[]`, `step`, `params` |
| `graph` | network compute | `components`, `cluster` | adjacency + labels | ✅* | `inputs[]`, `step`, `params` |
| `stats` | analytics | `hist`, `regress`, `bayesUpdate` | series + summaries | ✅* | `inputs[]`, `step`, `params` |
| `media` | image/raster prep | `decode`, `downsample` | ImageData/ArrayBuffer | ✅ | `inputs[]`, `step`, `params` |

\* Deterministic **if** you pass an explicit seed + config and avoid “ambient randomness”.

---

## 🧾 Message contracts

### Goals
- 🧩 **Typed** (TypeScript-first)
- 🔁 **Versioned** (schema evolution without breaking older callers)
- 🧯 **Safe** (structured-clone compatible)
- 🧵 **Cancelable** (AbortController-like behavior)
- 📈 **Observable** (progress + telemetry)

### Recommended shape

```ts
// web/src/workers/_shared/types.ts

export type WorkerSchemaVersion = 1;

export type WorkerRequest<TOp extends string, TPayload> = {
  v: WorkerSchemaVersion;
  id: string;              // request id (uuid)
  op: TOp;                 // operation name, namespaced (e.g., "geo/simplify")
  payload: TPayload;       // structured-clone safe
  meta?: {
    traceId?: string;      // correlate UI ↔ worker ↔ API
    startedAt?: number;    // performance.now() at send time
    provenance?: {
      inputs: Array<{
        datasetId: string;     // DCAT/STAC logical id (or API dataset id)
        itemIds?: string[];    // optional STAC item ids
        licenseId?: string;    // optional: license/terms id
        classification?: "public" | "restricted" | "sensitive";
      }>;
      step: string;         // "geo/simplify@1", "stats/regress@2", etc.
      paramsHash?: string;  // stable hash of relevant params
    };
    abortKey?: string;      // optional cancellation key
  };
};

export type WorkerProgress = {
  pct?: number;          // 0..100
  message?: string;      // human-readable
  stage?: string;        // "parse" | "compute" | "serialize" | ...
};

export type WorkerResponse<TResult> =
  | {
      v: WorkerSchemaVersion;
      id: string;
      ok: true;
      result: TResult;
      meta?: { finishedAt?: number; durationMs?: number };
    }
  | {
      v: WorkerSchemaVersion;
      id: string;
      ok: false;
      error: { name: string; message: string; stack?: string; code?: string };
      meta?: { finishedAt?: number; durationMs?: number };
    };

export type WorkerEvent<TResult> =
  | { type: "progress"; id: string; progress: WorkerProgress }
  | { type: "result"; id: string; response: WorkerResponse<TResult> };
```

### Minimal main-thread wrapper

```ts
// web/src/workers/geo/geo.client.ts

export function createGeoWorker(): Worker {
  return new Worker(new URL("./geo.worker.ts", import.meta.url), { type: "module" });
}

export function callWorker<TOp extends string, TPayload, TResult>(
  worker: Worker,
  req: WorkerRequest<TOp, TPayload>,
  onProgress?: (p: WorkerProgress) => void
): Promise<TResult> {
  return new Promise((resolve, reject) => {
    const onMessage = (event: MessageEvent) => {
      const msg = event.data as WorkerEvent<TResult>;
      if (!msg || msg.id !== req.id) return;

      if (msg.type === "progress") {
        onProgress?.(msg.progress);
        return;
      }

      worker.removeEventListener("message", onMessage);

      const res = msg.response;
      if (res.ok) resolve(res.result);
      else reject(Object.assign(new Error(res.error.message), res.error));
    };

    worker.addEventListener("message", onMessage);
    worker.postMessage(req);
  });
}
```

### Worker-side skeleton

```ts
// web/src/workers/geo/geo.worker.ts

import type { WorkerEvent, WorkerRequest, WorkerResponse } from "../_shared/types";

type GeoOps = "geo/simplify" | "geo/bbox";

self.addEventListener("message", async (event: MessageEvent) => {
  const req = event.data as WorkerRequest<GeoOps, any>;

  const started = performance.now();
  const send = (msg: WorkerEvent<any>) => (self as any).postMessage(msg);

  try {
    send({ type: "progress", id: req.id, progress: { pct: 5, stage: "start" } });

    // TODO: validate req shape (zod/io-ts/custom)
    // TODO: run the op
    const result = await runGeoOp(req);

    const finished = performance.now();
    const response: WorkerResponse<typeof result> = {
      v: req.v,
      id: req.id,
      ok: true,
      result,
      meta: { finishedAt: finished, durationMs: finished - started },
    };

    send({ type: "result", id: req.id, response });
  } catch (err: any) {
    const finished = performance.now();
    const response: WorkerResponse<never> = {
      v: req.v,
      id: req.id,
      ok: false,
      error: { name: err?.name ?? "Error", message: String(err?.message ?? err), stack: err?.stack },
      meta: { finishedAt: finished, durationMs: finished - started },
    };

    send({ type: "result", id: req.id, response });
  }
});

async function runGeoOp(req: WorkerRequest<GeoOps, any>) {
  switch (req.op) {
    case "geo/bbox":
      return bbox(req.payload);
    case "geo/simplify":
      return simplify(req.payload);
    default:
      throw new Error(`Unknown op: ${req.op}`);
  }
}

function bbox(payload: any) {
  // TODO: implement
  return payload;
}

function simplify(payload: any) {
  // TODO: implement
  return payload;
}
```

---

## ⚡ Performance patterns

### 🧩 Chunk work (“morsel-style”) and stream progress
If an operation touches thousands/millions of elements, process in chunks and emit progress events. That keeps UI feedback alive and makes cancellation possible.

**Pattern:**
- split inputs into fixed-size chunks
- process chunk → post progress
- repeat → post final result

### 🧠 Minimize copies
Structured cloning can be expensive. Prefer:
- `ArrayBuffer` / typed arrays
- `Transferable` objects for large buffers
- compact data representations (e.g., quantized floats) when appropriate

### 🧊 Cache repeated comparisons
If we repeatedly compare or normalize similar payloads (e.g., style keys, label keys, feature props), add small caches keyed by stable hashes.

### 🛰️ Know when to delegate to server/cloud
Workers are great for interactive compute, but:
- heavy remote sensing analysis,
- large-scale time series extraction,
- or “official” reproducible outputs  
should run in governed pipelines / APIs (and potentially external compute like Earth Engine).

---

## 🔒 Security & governance

### Treat worker inputs as untrusted
Even if we “own” the UI, payloads often originate from:
- user uploads
- external APIs
- third-party datasets

**Rules:**
- validate message shapes (schemas)
- never `eval` or execute user-provided code
- avoid dynamic function construction
- fail closed (return typed errors)

### Don’t move secrets into workers
- keep auth tokens in one controlled place (usually main thread + API client)
- prefer a design where workers are **pure compute** on already-fetched/validated data

### Don’t bypass the API boundary
Workers should not be an alternate “backdoor” to raw databases/graphs. If data access is needed, the main thread should request it via the governed API and then hand it to the worker.

---

## 🧪 Testing & reproducibility

Workers are “mini scientific computing runtimes” inside the browser. Treat them like it:

- ✅ deterministic seeds for randomness
- ✅ snapshot tests for stable transforms
- ✅ property tests for invariants (e.g., bbox contains all points)
- ✅ numeric tolerance tests (floating point reality)
- ✅ regression tests for known tricky datasets

> [!TIP]
> If you ship an analysis feature in the UI, always include enough metadata to reproduce it elsewhere (inputs + config + version + seed).

---

## ➕ Adding a new worker

### Checklist ✅
- [ ] Create worker folder: `web/src/workers/<domain>/`
- [ ] Define ops + payload/result types in `_shared/types.ts` (or domain types)
- [ ] Implement worker entry (`*.worker.ts`) with:
  - [ ] validation
  - [ ] progress events
  - [ ] cancel support (if long-running)
  - [ ] provenance propagation
- [ ] Add a main-thread client wrapper (`*.client.ts`)
- [ ] Add unit tests for pure ops (prefer `*.ops.ts`)
- [ ] Update the [Worker inventory](#-worker-inventory) table
- [ ] Add docs (1–2 examples) for each new op

---

## 📚 Project reference shelf

These project files informed the patterns in this folder (performance, reproducibility, geospatial + graph workflows, UI resilience, security posture, and governance):

### 🛰️ Modeling, simulation, optimization
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` — reproducible modeling mindset; uncertainty-aware simulation patterns
- `Generalized Topology Optimization for Structural Design.pdf` — iterative optimization loops + convergence thinking
- `B-C programming Books.pdf` — performance profiling mindset; repeatable evaluation loops (algorithmic workloads)

### 📊 Statistics, experimentation, inference
- `Understanding Statistics & Experimental Design.pdf` — bias control, multiple testing discipline, rigorous evaluation
- `regression-analysis-with-python.pdf` — regression modeling mechanics for UI analytics
- `Regression analysis using Python - slides-linear-regression.pdf` — keep correlation ≠ causation straight in UI narratives
- `think-bayes-bayesian-statistics-in-python.pdf` — Bayesian updating for interactive “what-if” exploration
- `graphical-data-analysis-with-r.pdf` — exploratory plots + outlier awareness for quick UI summaries

### 🗺️ Geospatial, mapping, 3D GIS, remote sensing
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf` — map readability + visual hierarchy (precompute what you can)
- `python-geospatial-analysis-cookbook.pdf` — topology/routing/indexing concepts that show up in KFM workflows
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` — when to offload heavy compute
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` — mobile context constraints (latency, sensors, UX)
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf` — 3D GIS workflows and the cost of heavy spatial analysis

### 🌐 Web UI engineering + graphics
- `responsive-web-design-with-html5-and-css3.pdf` — offline-first mindset + graceful degradation
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` — geometry/attribute prep patterns for GPU
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` — decoding/encoding costs; choose formats intentionally

### 🗄️ Data systems, scalability, interoperability
- `Scalable Data Management for Future Hardware.pdf` — chunked parallelism + task pool mindset (“morsels”)
- `Database Performance at Scale.pdf` — concurrency realities; don’t block; measure
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` — performance fundamentals that translate to client caches/indexes
- `Data Spaces.pdf` — interoperability + metadata-first thinking

### 🧑‍⚖️ Ethics, law, human-centered design, security posture
- `Introduction to Digital Humanism.pdf` — human-centered tech + transparency pressure
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` — accountability + “black box” skepticism
- `Principles of Biological Autonomy - book_9780262381833.pdf` — systems thinking for distributed behavior
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` — security as defense; threat-aware posture
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` — security literacy; **use defensively**

### 📚 Language + platform reference compendiums
- `A programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

---

🧭 **Next maintenance step:** once worker files exist, add a short “Per-worker README” under each domain folder (`geo/`, `graph/`, etc.) documenting ops + payload schemas + examples.
