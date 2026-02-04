# 🧩 `web/public/config` — Public Runtime Config (KFM Web) 🌾🗺️

![Public](https://img.shields.io/badge/scope-public%20assets-brightgreen)
![Runtime Config](https://img.shields.io/badge/config-runtime%20(load%20at%20startup)-blue)
![API First](https://img.shields.io/badge/architecture-API%20first%20%7C%20governed-orange)
![Provenance](https://img.shields.io/badge/principle-provenance%20first-purple)

This folder contains **public, runtime-loadable configuration files** for the KFM web client (the map UI + timeline + Focus Mode panel). Because it lives under `public/`, **everything here is world-readable** and will be served as static files by your web server/CDN. ✅

> 🎯 Goal: let us deploy the same front-end build everywhere, while switching environments (local/dev/prod) by swapping **only** these JSON files.

---

## 📦 What belongs here

Use this folder for **non-secret** settings the browser must know at runtime, such as:

- 🌐 **API base URLs** (the UI must go through the governed API layer — not direct DB calls)
- 🧱 **GraphQL / REST paths** (e.g., `/graphql`, `/api/v1`)
- 🗺️ **Map defaults** (center, zoom, Kansas bounds, default basemap style URL)
- 🧩 **Layer catalogs** (what layers exist, IDs, tile endpoints, attribution, etc.)
- 🧪 **Feature flags** (enable/disable “3D”, “Focus Mode”, experimental UI bits)
- 🧾 **Attribution + citation metadata** (“map behind the map” 🔎)

KFM’s architecture is designed so clients consume data via **REST/GraphQL APIs** and map tiles, with governance gates (policy checks, provenance, licensing) enforced in the service layer. This config should reinforce that “truth path.”  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🚫 What must NOT go here

Because `public/` is public:

- ❌ API keys that grant privileges (Mapbox tokens, cloud keys, database creds, etc.)
- ❌ Any secrets, JWT signing keys, OAuth client secrets
- ❌ Internal hostnames / private network details you don’t want exposed
- ❌ Anything that bypasses governance (direct DB endpoints)

> 🔐 Rule of thumb: **If it would hurt to paste it into a public GitHub issue, it doesn’t belong here.**

---

## 🗂️ Suggested layout (recommended)

> If your project already has established filenames, keep them — this is a suggested structure that scales well.

```text
web/
└─ public/
   └─ config/
      ├─ README.md                👈 you are here
      ├─ app.json                 🌐 global app/runtime settings
      ├─ endpoints.json           🔌 API + tile endpoints (optional split)
      ├─ layers.json              🗺️ map layer catalog (UI toggles + tiles)
      ├─ basemaps.json            🧭 basemap styles/providers
      ├─ feature-flags.json       🧪 kill-switches & experiments
      ├─ ui.json                  🎛️ UI defaults (panels, timeline range)
      └─ version.json             🏷️ build + config version (cache busting)
```

---

## 🧠 How the app should load this config (pattern)

Typical pattern for React/SPA:

1. The app boots
2. It fetches one “root” config file (e.g., `/config/app.json`)
3. It validates shape (lightweight)
4. It stores the result in a global state/store/context
5. The map/timeline/features initialize from that state

<details>
  <summary>🧪 Example loader snippet (TypeScript-ish)</summary>

```ts
// Example only — adapt to your codebase.
export type RuntimeConfig = {
  env: "local" | "dev" | "prod";
  apiBaseUrl: string;        // e.g. https://kfm.example.com
  restBasePath: string;      // e.g. /api/v1
  graphqlPath: string;       // e.g. /graphql
  tilesPath: string;         // e.g. /tiles
  map: {
    defaultCenter: [number, number]; // [lng, lat]
    defaultZoom: number;
    bounds?: [[number, number], [number, number]];
    styleUrl?: string;
  };
  features?: Record<string, boolean>;
};

export async function loadRuntimeConfig(): Promise<RuntimeConfig> {
  const res = await fetch("/config/app.json", { cache: "no-store" });
  if (!res.ok) throw new Error(`Config fetch failed: ${res.status}`);
  const cfg = (await res.json()) as RuntimeConfig;

  // Minimal validation (do more if you can).
  if (!cfg.apiBaseUrl) throw new Error("Missing apiBaseUrl in /config/app.json");

  return cfg;
}
```
</details>

---

## 🌐 Endpoints: keep the UI on the governed “truth path”

KFM’s service layer exposes REST and GraphQL and standard documentation endpoints (OpenAPI/Swagger). The web client should be configured to talk only to these controlled entry points.  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

Common patterns you’ll likely encode in `app.json` / `endpoints.json`:

- ✅ REST base: `/api/v1/...`
- ✅ GraphQL: `/graphql`
- ✅ OpenAPI spec: `/openapi.json`
- ✅ Swagger UI: `/docs`
- ✅ Tiles:
  - Vector tiles: `/tiles/{layer}/{z}/{x}/{y}.pbf`
  - Raster tiles: `/tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`)

> 🗺️ This matters because the map UI (MapLibre / Cesium) is typically driven by **tile endpoints** and/or GeoJSON endpoints — all of which should remain governed and auditable.  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🗺️ Layer config: bake in provenance (“map behind the map”) 🔎

A layer entry should include:

- `id` (stable)
- `title` / `description`
- `type` (`vector-tile`, `raster-tile`, `geojson`, etc.)
- `endpoint` or `source` URL template
- `attribution`
- `license`
- `datasetId` (or catalog reference)
- optional: `temporal` range, tags, default visibility, styling hints

<details>
  <summary>🧾 Example <code>layers.json</code> (minimal)</summary>

```json
{
  "layers": [
    {
      "id": "historic_trails",
      "title": "Historic Trails",
      "type": "vector-tile",
      "tileUrl": "/tiles/historic_trails/{z}/{x}/{y}.pbf",
      "attribution": "KFM + upstream authoritative sources",
      "license": "See dataset metadata",
      "datasetId": "ks_historic_trails",
      "tags": ["history", "transport"],
      "defaultVisible": false
    }
  ]
}
```
</details>

> ✅ Tip: keep config **declarative**. The UI code should interpret this catalog, not hardcode per-layer behavior.

---

## 🧪 Feature flags (kill-switch friendly) 🚦

Feature flags are your “break glass” controls for UI experiments:

- `focusMode`: enable/disable AI panel visibility
- `cesium3d`: enable/disable 3D mode
- `timeline`: enable/disable timeline module
- `debugPanels`: enable/disable dev-only panels

Keep it simple:

```json
{
  "features": {
    "focusMode": true,
    "cesium3d": true,
    "timeline": true,
    "debugPanels": false
  }
}
```

KFM’s AI experience is designed around “No Source, No Answer” and provenance-first outputs; feature flags let you ship safely while tightening policy and UX.  [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## ♻️ Environment strategy (local/dev/prod)

### Option A — Swap files at deploy time (simple ✅)

- Commit `app.example.json`
- In CI/CD (or Docker/K8s), copy the right env file into place as `app.json`

Example:

```bash
cp web/public/config/app.prod.json web/public/config/app.json
```

### Option B — Mount config as a volume (best for Docker/K8s 🐳)

Mount `config/` to the container path where static files are served:

```text
/usr/share/nginx/html/config
```

This enables “same build, different config” with zero rebuilds.

---

## 🧊 Caching rules (important!)

Because these are static files, they can be cached aggressively.

### Recommended

- Serve `/config/*.json` with:
  - `Cache-Control: no-store` **or**
  - short TTL + revalidation (`max-age=60, must-revalidate`)
- Add a tiny `/config/version.json` and have the app read it first (or embed it in HTML)

Example `version.json`:

```json
{
  "build": "2026-02-04",
  "gitSha": "abcdef1",
  "configRev": "prod-17"
}
```

---

## ✅ Naming conventions (keep it tidy)

Borrowing standard web dev hygiene:

- Files: `kebab-case.json` (or consistent `snake_case.json`) — pick one and stick to it
- IDs: stable, lowercase, `_` or `-` separated (avoid spaces)
- Don’t rename IDs casually — treat them like API contracts

Good conventions reduce UI/UX complexity and prevent “mystery config drift.”  [oai_citation:4‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  [oai_citation:5‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

---

## 🧰 Troubleshooting quick hits

- **Config 404** → web server isn’t serving `public/config` (check build output + static root)
- **CORS errors** → your `apiBaseUrl` points cross-origin without proper CORS headers
- **Map blank** → basemap `styleUrl` unreachable or tiles endpoint mismatch
- **Changes not showing** → CDN cached old config (fix cache headers or bump `version.json`)

---

## 📚 References (project files)

- 🌾 Kansas Frontier Matrix — Comprehensive System Documentation  [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- 🧱 Professional Web Design: Techniques and Templates (naming/consistency best practices)  [oai_citation:7‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- 🎨 Learn to Code HTML & CSS (web fundamentals + practical patterns)  [oai_citation:8‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- ⚛️ Node.js / React tooling notes (build vs runtime config context)  [oai_citation:9‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  

---