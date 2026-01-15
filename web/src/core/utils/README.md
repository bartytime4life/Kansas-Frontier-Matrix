# 🧰 Core Utilities (`web/src/core/utils`)

![Pipeline](https://img.shields.io/badge/pipeline-UI-0ea5e9?style=flat)
![TypeScript](https://img.shields.io/badge/language-TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![Contract-first](https://img.shields.io/badge/contract--first-✅-22c55e?style=flat)
![Evidence-first](https://img.shields.io/badge/evidence--first-✅-22c55e?style=flat)
![Provenance](https://img.shields.io/badge/provenance-always-a855f7?style=flat)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE-f97316?style=flat)

> [!NOTE]
> `core/utils` is the **shared toolbox** for the KFM Web UI: small, composable helpers that keep map/timeline/narrative features **deterministic**, **safe**, and **consistent**.

---

## 🔗 Quick links (repo-wide context)
- 📘 **Master Guide (v13)**: [`docs/MASTER_GUIDE_v13.md`](../../../../docs/MASTER_GUIDE_v13.md)
- 🧾 **Governance**: [`docs/governance/`](../../../../docs/governance/)
- 🧪 **Schemas / Contracts**: [`schemas/`](../../../../schemas/)
- 🛰️ **API layer (server)**: [`src/server/`](../../../../src/server/)
- 🌐 **Web app root**: [`web/`](../../../)

---

## 🧭 How this fits in the v13 pipeline
KFM’s canonical ordering is:

**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**

This folder supports the **UI stage** only (i.e., the browser app).

> [!IMPORTANT]
> **API Boundary Rule:** the UI must not query Neo4j (or any database) directly — it consumes **governed APIs** only.  
> If you think a “util” needs raw DB access, it belongs in `src/server/` (or earlier pipeline stages), not here.

---

## 🎯 What belongs in `core/utils`
✅ Put code here when it is:

- **Cross-cutting** (used by 2+ screens/features)
- **Small** (easy to understand in one sitting)
- **Low-dependency** (no heavyweight frameworks)
- **Deterministic** (same input → same output)
- **UI-stage safe** (cannot bypass redaction / classification / provenance constraints)

Common categories we expect to live here:

- 🧪 **Type guards & runtime validation** (safe parsing at boundaries)
- 🧱 **Assertions & invariants** (exhaustive checks, “should never happen”)
- 🧵 **Async helpers** (debounce/throttle, retry-with-backoff, AbortController glue)
- 🗺️ **Geo helpers** (bbox, lon/lat formatting, GeoJSON quirks)
- 🕰️ **Time helpers** (timeline range, year parsing, date formatting)
- 🧾 **Formatting** (numbers, units, citations labels, humanized text)
- 🔐 **Security utilities** (sanitization, safe URLs, escaping)
- ⚡ **Performance helpers** (memoization, stable keys, bounded micro-caches)
- 🧰 **General FP-ish helpers** (Result/Option patterns, immutable helpers)

---

## 🚫 What does NOT belong here
❌ Avoid putting these into `core/utils`:

- React components or hooks (`useSomething`) → `web/src/.../hooks` or `web/src/.../components`
- Feature/business logic → `web/src/features/<feature>/...`
- API endpoint definitions (server) → `src/server/`
- API client orchestration (browser) → `web/src/core/api/` (or equivalent)
- Map engine adapters (MapLibre/Cesium instances, layer lifecycle) → `web/src/core/map/` (or equivalent)
- Heavy computation (graph algorithms, optimization, large raster ops) → pipeline workers / server-side compute

> [!TIP]
> **Rule of thumb:** if the code “decides what something means,” it’s probably **domain logic** (not utils).  
> If the code “helps you do the same small thing in many places,” it’s probably a **util**.

---

## 🧱 Non‑negotiables
> [!WARNING]
> Utilities can accidentally become **policy bypasses**.  
> If a helper touches **visibility**, **filtering**, **search**, **export**, **sharing**, or **content rendering** — it must respect **classification + redaction + provenance** rules.

### ✅ Governance & safety checklist
- [ ] Input is validated (types **and** runtime when crossing boundaries)
- [ ] Output cannot “reveal more” than the input (no de-redaction, no unblurring)
- [ ] Works at any map zoom level (no “zoom to bypass” surprises)
- [ ] Telemetry/audit events are emitted where required (esp. redaction notices)
- [ ] Unit tests cover edge cases and malicious inputs
- [ ] No secret backdoors (no “temporary” debug flags that leak data)

---

## 📁 Suggested folder layout
> [!NOTE]
> We prefer “small files with one purpose” over a giant `utils.ts`.

<details>
<summary>📂 Suggested tree (adapt to what exists)</summary>

```text
📁 web/src/core/utils
├─ 📄 README.md
├─ 📄 index.ts                 # barrel exports (optional but encouraged)
├─ 📁 async/                   # debounce, throttle, retry, cancelation helpers
├─ 📁 browser/                 # localStorage, URL, clipboard (side-effecty, isolated)
├─ 📁 data/                    # parsing, schema validation, safe JSON utilities
├─ 📁 format/                  # dates, numbers, labels
├─ 📁 geo/                     # bbox, GeoJSON helpers, coordinate formatting
├─ 📁 security/                # sanitizers, escaping, safe URL helpers
└─ 📁 types/                   # Result/Option, type guards, assertions
```

</details>

---

## 🧩 Conventions
### Naming ✍️
- **`camelCase`** for functions
- **`PascalCase`** for types/classes
- Prefer **verbs**: `parseYear`, `formatCoordinate`, `assertNever`
- Put “unsafe” operations behind explicit names: `unsafeParseHtml`, `dangerouslySet...`

### Exports 📦
- Prefer **named exports** (better tree-shaking and refactors).
- If you maintain an `index.ts` barrel, keep it curated (don’t export internal-only helpers).

### Dependencies 🪶
- Default: **zero external deps**.
- If a dependency is justified, it must be:
  - widely used across the app,
  - small and stable,
  - documented (why it’s worth it),
  - and tested.

### Side effects ⚠️
- Pure functions belong at the top-level categories.
- Anything touching `window`, `document`, storage, clipboard, etc. should live in a clearly-labeled subfolder (e.g. `browser/`) or outside utils entirely.

---

## 🍱 Standard patterns (use them consistently)
### 1) Safe parsing (never trust the boundary) 🧪
```ts
// Prefer a "safe parse" helper that returns a Result-like shape.
// Example API: safeJsonParse(input): { ok: true; value } | { ok: false; error }

const parsed = safeJsonParse(input);

if (!parsed.ok) {
  // show a user-friendly error + optionally log telemetry
  return;
}

render(parsed.value);
```

### 2) Result / Option over “throw everywhere” 🧰
```ts
export type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

export const ok = <T>(value: T): Result<T, never> => ({ ok: true, value });
export const err = <E>(error: E): Result<never, E> => ({ ok: false, error });
```

### 3) Exhaustive checks (future-proof enums) 🧱
```ts
export function assertNever(x: never): never {
  throw new Error(`Unexpected value: ${String(x)}`);
}
```

### 4) Redaction-aware formatting (policy is code) 🔐
```ts
// Pseudocode: any display helper that might reveal sensitive info
// must respect classification/redaction signals from the API.

formatCoordinate(feature.geom, {
  classification: feature.classification,
  redaction: feature.redaction,
});
```

---

## 🗺️ Map + Timeline “glue”
KFM’s UI combines:
- 🗺️ **2D vector maps** (MapLibre)
- 🌍 **optional 3D globe/terrain** (Cesium)
- 🕰️ **a timeline slider** (historical navigation)
- 📖 **story steps** that synchronize layers + camera + time
- 🧠 **Focus Mode** (evidence-constrained Q&A)

Utilities in this folder should help with **small, repeatable** tasks like:
- normalizing camera state (lon/lat/zoom → canonical shape)
- clamping timeline values to valid ranges
- formatting “source” labels and citations in tooltips/side panels
- generating stable keys for layers/features (for caching + React lists)
- parsing/validating Story Node JSON configs and Markdown metadata safely

> [!IMPORTANT]
> Story Nodes are authored artifacts (Markdown + JSON config).  
> `core/utils` can help **validate and render safely**, but must **never** embed uncited narrative text.

---

## ⚡ Performance notes
- Prefer **precomputed** lookup maps over repeated `.find(...)` in render loops.
- Avoid allocating new objects in hot paths (especially map render + event handlers).
- Cache expensive computations with explicit keys (memoization) — but keep caches **bounded**.

---

## ✅ Adding a new util (PR checklist)
1. 📌 Pick the narrowest scope: can it be a pure function?
2. 🧪 Add unit tests for:
   - normal cases
   - weird edge cases
   - “hostile” input (`null`, `NaN`, gigantic arrays, pathological strings)
3. 🧾 Add a short doc comment + example usage.
4. 🔐 If it touches data visibility/export/search, confirm it respects classification/redaction.
5. 🧹 Run lint/format and keep exports tidy.

---

## 📚 Project reference library (why these matter here)
<details>
<summary>📖 Click to expand (all project docs/books that inform core/utils)</summary>

### 🏛️ KFM architecture, governance, and “how we build”
- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- 🧭 **MARKDOWN_GUIDE_v13.md.gdoc** (Master Guide v13)
- 🧱 **Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf**
- 🔎 **Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf**

### 🗺️ Mapping, GIS, geospatial analysis
- 🗺️ **making-maps-a-visual-guide-to-map-design-for-gis.pdf**
- 📱 **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf**
- 🧭 **python-geospatial-analysis-cookbook.pdf**
- 🛰️ **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf**
- 🏺 **Archaeological 3D GIS_26_01_12_17_53_09.pdf**

### 🌐 Web UI engineering + WebGL
- 🎛️ **responsive-web-design-with-html5-and-css3.pdf**
- 🧊 **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf**

### 🗄️ Data + scale + storage (performance mental models)
- 🧠 **Data Spaces.pdf**
- ⚡ **Database Performance at Scale.pdf**
- 🗃️ **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf**
- 🧵 **Scalable Data Management for Future Hardware.pdf**

### 📈 Statistics, modeling, simulation (UI display + analytics helpers)
- 📊 **Understanding Statistics & Experimental Design.pdf**
- 📉 **regression-analysis-with-python.pdf**
- 🧾 **Regression analysis using Python - slides-linear-regression.pdf**
- 🎲 **think-bayes-bayesian-statistics-in-python.pdf**
- 🚀 **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf**
- 🧠 **Spectral Geometry of Graphs.pdf**
- 🏗️ **Generalized Topology Optimization for Structural Design.pdf**
- 📉 **graphical-data-analysis-with-r.pdf**

### 🔐 Security + safety
- 🛡️ **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf**
- 🐍 **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf**
- 🧵 **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf**
- 🖼️ **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf**

### 🤝 Human-centered + legal/ethical context
- 🧑‍🤝‍🧑 **Introduction to Digital Humanism.pdf**
- ⚖️ **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf**
- 🧬 **Principles of Biological Autonomy - book_9780262381833.pdf**
- 🧠 **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf**

### 🧰 General programming references (compendiums)
- 📚 **A programming Books.pdf**
- 📚 **B-C programming Books.pdf**
- 📚 **D-E programming Books.pdf**
- 📚 **F-H programming Books.pdf**
- 📚 **I-L programming Books.pdf**
- 📚 **M-N programming Books.pdf**
- 📚 **O-R programming Books.pdf**
- 📚 **S-T programming Books.pdf**
- 📚 **U-X programming Books.pdf**

</details>

