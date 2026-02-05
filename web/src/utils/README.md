# `web/src/utils` 🧰✨

![TypeScript](https://img.shields.io/badge/TypeScript-ready-3178C6?logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-UI-61DAFB?logo=react&logoColor=black)
![MapLibre](https://img.shields.io/badge/MapLibre-maps-1E88E5)
![KFM](https://img.shields.io/badge/KFM-v13%20guardrails-222)
![Provenance](https://img.shields.io/badge/Provenance-first-0B3D91)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-enforced-4CAF50)

Small, sharp, dependency-light helpers for the **KFM Web UI** (React/TypeScript + map UI).  
This folder exists to keep shared logic **pure**, **deterministic**, and **governance-aware** ✅

> [!IMPORTANT]
> In KFM, the UI is *not* allowed to “wing it.” If a feature needs provenance, redaction, or contract checks,
> **do it once here** and reuse everywhere. 🧱

---

## 🧭 Quick Navigation

- [What belongs in `utils`](#-what-belongs-in-utils)
- [Non-negotiables](#-non-negotiables)
- [Suggested layout](#-suggested-layout)
- [Naming & export conventions](#-naming--export-conventions)
- [Recipes](#-recipes)
- [Adding a new util](#-adding-a-new-util)
- [Anti-patterns](#-anti-patterns)

---

## ✅ What belongs in `utils`

**Put it here if it’s:**

- 🧼 **Pure**: same input → same output (ideally no side effects)
- 🧩 **Reusable**: used by multiple components/features
- 🧠 **Type-safe**: strongly typed inputs/outputs (no `any`)
- 🧭 **Governance-aware**: provenance checks, sovereignty/redaction helpers, safe formatting
- ⚡ **Performance helpers**: `debounce`, memo helpers, stable IDs, lightweight caching primitives

**Common examples:**
- 🗺️ Geo helpers (bbox math, GeoJSON normalization, coordinate formatting)
- 🧭 Map helpers (consistent layer IDs, MapLibre style snippets, popup content formatting)
- 💾 Storage helpers (namespaced local/session storage)
- 🧾 Formatting helpers (dates, numbers, labels, slugs)
- 🔐 Sovereignty helpers (redaction/generalization, classification propagation UI rules)
- 🧪 Tiny testable validators (runtime guards, schema adapters)

---

## 🚫 Non-negotiables

These are **system rules** the UI must uphold. `utils/` is one of the best places to enforce them.

### 1) 🧱 API boundary stays intact
- UI utilities **must not** query Neo4j/PostGIS directly.
- Any “data access helper” in `utils/` must remain a **thin, typed wrapper** over the governed API layer.

✅ Good: `fetchDataset(id)` → calls backend `/api/...`  
❌ Bad: `runCypher(query)` in frontend, or any direct DB/graph call

---

### 2) 🧾 Provenance-first rendering
If the UI displays:
- a map overlay 🗺️  
- a chart 📈  
- a story excerpt 📖  
- a “fact” in Focus Mode 🧠  

…it must tie back to **cataloged evidence** (DCAT/STAC/PROV IDs or equivalent references).

**Rule of thumb:** *“No provenance → no render.”* 🛑

---

### 3) 🪶 Sovereignty & CARE protections (no leaks)
Utilities must make it easy to:
- generalize or blur sensitive locations 📍➡️🟦  
- avoid “side-channel” leaks (e.g., precise coordinates hidden in tooltips, logs, or debug output) 🕵️‍♂️🚫  
- keep derived UI outputs **at least as restricted** as their inputs 🔒

---

### 4) 🧪 Determinism over cleverness
Avoid hidden nondeterminism:
- no random IDs without stable seeds 🎲🚫
- don’t silently bake in `Date.now()` into outputs unless that’s explicitly the purpose ⏱️

---

## 🗂️ Suggested layout

Your exact contents may differ, but **aim toward** a structure like this for sanity + scale:

```text
web/src/utils/
├── 🧠 provenance/          # provenance refs, citation formatting, hard gates
├── 🔐 sovereignty/         # redaction/generalization + classification helpers
├── 🗺️ geo/                 # GeoJSON, bbox, coordinate conversions
├── 🧭 map/                 # MapLibre/Cesium helper builders (layer/source/popup)
├── 🧵 async/               # debounce/throttle, AbortController helpers
├── 💾 storage/             # localStorage/sessionStorage (namespaced)
├── 🧾 format/              # date/number/label formatting, slugs
├── 🧪 __tests__/           # pure util unit tests
└── 📄 index.ts             # barrel exports (⚠️ no side effects)
```

> [!TIP]
> Keep MapLibre/Cesium-specific helpers **behind** small adapters so the rest of the app isn’t tightly coupled.

---

## 🧩 Naming & export conventions

### File naming
- Prefer **one intent per file** (e.g., `debounce.ts`, `formatDate.ts`, `redactLocation.ts`)
- Group by domain when a category grows: `geo/`, `map/`, `provenance/`, `sovereignty/`

### Exports
- ✅ Prefer **named exports**
- ✅ Prefer a local `index.ts` barrel for ergonomics
- ❌ Avoid default exports (harder refactors, inconsistent imports)

### Dependency rules
- ✅ Browser-safe only (unless explicitly guarded)
- ✅ Keep dependencies light
- ❌ Don’t import React components/hooks into `utils/`

---

## 🧱 “Contracts-first” in the UI

If you consume API responses, prefer a lightweight runtime guard:

- ✅ parse/validate critical shapes at the boundary (especially for:
  - provenance references
  - classification tags
  - layer configuration
  - story node references)

> [!NOTE]
> If you see yourself writing the same “is this field present?” checks in 3 places, it belongs in `utils/`.

---

## 🧠 Provenance primitives (recommended)

A tiny shared type goes a long way:

```ts
export type ProvenanceRef = {
  dcatDatasetId?: string;   // dataset catalog id
  stacItemId?: string;      // spatial asset id
  provActivityId?: string;  // lineage/run id
  sourceUrl?: string;       // external canonical source (optional)
  license?: string;
  classification?: "public" | "restricted" | "sensitive";
};
```

### Hard gate helper (pattern)
```ts
export function requireProvenance(ref?: ProvenanceRef): ProvenanceRef {
  if (!ref) throw new Error("Missing provenance");
  if (!ref.dcatDatasetId && !ref.stacItemId && !ref.provActivityId) {
    throw new Error("Unlinked content: no catalog/prov identifiers");
  }
  return ref;
}
```

---

## 🧪 Recipes

### 1) Debounce user input (search, sliders, map hover)
```ts
export function debounce<T extends (...args: any[]) => void>(fn: T, waitMs = 250) {
  let t: ReturnType<typeof setTimeout> | undefined;

  return (...args: Parameters<T>) => {
    if (t) clearTimeout(t);
    t = setTimeout(() => fn(...args), waitMs);
  };
}
```

---

### 2) Safe, typed fetch wrapper (API boundary friendly)
```ts
export class ApiError extends Error {
  constructor(
    message: string,
    public status?: number,
    public details?: unknown
  ) {
    super(message);
    this.name = "ApiError";
  }
}

export async function apiGetJson<T>(url: string, init?: RequestInit): Promise<T> {
  const res = await fetch(url, {
    method: "GET",
    headers: { "Accept": "application/json" },
    ...init,
  });

  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new ApiError(`API request failed: ${url}`, res.status, text);
  }

  return (await res.json()) as T;
}
```

> [!TIP]
> Keep “what endpoint to call” in feature/services code. Keep “how to safely call endpoints” in `utils/`.

---

### 3) Layer legend that always carries provenance 🗺️🧾
When you build UI metadata for a map overlay, make provenance *mandatory*:

```ts
export type LayerLegend = {
  title: string;
  description?: string;
  swatches?: Array<{ label: string; value: string }>;
  provenance: ProvenanceRef; // ✅ required
};

export function buildLegend(input: Omit<LayerLegend, "provenance"> & { provenance?: ProvenanceRef }): LayerLegend {
  return {
    ...input,
    provenance: requireProvenance(input.provenance),
  };
}
```

---

### 4) Sovereignty-safe coordinate display 📍➡️🟦
```ts
export type LonLat = { lon: number; lat: number };

export function formatLonLat(
  pt: LonLat,
  classification: "public" | "restricted" | "sensitive" = "public"
): string {
  if (classification === "sensitive") {
    // ✅ intentionally coarse; do not leak precise coords in UI
    const lon = Math.round(pt.lon * 10) / 10;
    const lat = Math.round(pt.lat * 10) / 10;
    return `${lat.toFixed(1)}, ${lon.toFixed(1)} (generalized)`;
  }
  return `${pt.lat.toFixed(5)}, ${pt.lon.toFixed(5)}`;
}
```

> [!WARNING]
> If a location is sensitive, **do not** place the raw coordinates in DOM attributes, logs, tooltips, debug panels, or telemetry payloads.

---

## ➕ Adding a new util

### Checklist ✅
- [ ] Is it truly shared (used or soon-to-be used in ≥2 places)?
- [ ] Is it deterministic (or explicitly documented why not)?
- [ ] Is the TypeScript type signature clear and strict?
- [ ] Is it safe for browser execution (or guarded)?
- [ ] If it affects rendering of evidence/maps/stories: does it enforce provenance?
- [ ] If it touches locations/entities: does it respect sovereignty/classification?
- [ ] Add/extend unit tests in `__tests__/` (pure utils are easy wins 🧪)

### PR hygiene 🧼
- Add a short example snippet in this README **or** in the function JSDoc
- Avoid “misc.ts” dumping grounds 🙅

---

## 🧨 Anti-patterns

- ❌ A `utils` function that performs uncontrolled network calls to unknown hosts
- ❌ Hidden side effects (writes to storage, emits telemetry) without being obvious in name/docs
- ❌ UI “shortcut” helpers that bypass governance (no provenance, no redaction, no contract checks)
- ❌ Copy/paste formatting logic sprinkled across components
- ❌ “Just this once” coordinate display hacks (they will leak eventually)

---

## 🔗 Canonical references (repo-local)

From this folder, the canonical KFM docs are typically here:

- 📘 Master guide: `../../../docs/MASTER_GUIDE_v13.md`
- ⚖️ Governance: `../../../docs/governance/ROOT_GOVERNANCE.md`
- 🪶 Sovereignty: `../../../docs/governance/SOVEREIGNTY.md`
- 🌐 API boundary (server): `../../../src/server/`
- 📜 API docs: `../../../src/server/api/README.md`

> [!NOTE]
> If any of the links above are missing, that’s a repo hygiene issue worth fixing—these are “source of truth” artifacts.
