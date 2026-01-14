# 🧪 Fixtures — Web UI (`web/data/fixtures/`)

![scope](https://img.shields.io/badge/scope-web%2Fdata%2Ffixtures-blue)
![use](https://img.shields.io/badge/use-dev%20%7C%20tests%20%7C%20demos-success)
![format](https://img.shields.io/badge/formats-JSON%20%7C%20GeoJSON%20%7C%20TopoJSON-informational)
![rule](https://img.shields.io/badge/rule-contract--first%20%26%20provenance--first-important)

Static, **small**, **sanitized**, and **versioned** sample payloads used to build & test the KFM web UI (maps, timelines, Story/Focus views) without requiring a full backend or large datasets.

> [!IMPORTANT]
> **Fixtures are not a data pipeline.** They must never become a “mystery source of truth.”  
> Treat fixtures as **UI stand-ins** for **already-defined contracts** (API + schemas) and **catalog outputs** (STAC/DCAT/PROV), not as “new data”.

---

## 🧭 What belongs here (and what doesn’t)

### ✅ Use fixtures for
- 🧑‍💻 **Local development** when the API isn’t running (offline / airplane mode).
- 🧪 **Unit / integration / visual regression tests** (deterministic inputs).
- 🎭 **Storybook / UI demos** (stable “known good” responses).
- 🗺️ **Map layer prototyping** with small GeoJSON/TopoJSON samples (simplified geometries).
- 🧩 **Contract validation** (fixtures act as examples that must match schemas).

### ❌ Don’t use fixtures for
- 🚫 Shipping “real data” around API governance rules.
- 🚫 Storing big files (COGs, tilesets, LiDAR, full-resolution boundaries, dumps).
- 🚫 Anything sensitive (PII, restricted locations, sovereignty-sensitive layers, keys/tokens).
- 🚫 Bypassing the API boundary in production code (“just read the JSON from fixtures”).

---

## 🥇 Golden rules (non-negotiable)

1. **Small by default** 📉  
   Keep fixtures *tiny*: ideal files are **KBs**, not **MBs**. Prefer simplified geometries & short lists.

2. **Match contracts** 🧾  
   A fixture must conform to the **current API/Schema contract** (or explicitly declare the contract version it targets).

3. **Provenance-aware** 🔎  
   If a fixture represents a dataset/layer/story, it should be traceable to a **catalog identity** (STAC/DCAT) and/or a known example contract.

4. **Deterministic** 🧊  
   No random values unless seeded and documented. Tests and screenshots must be repeatable.

5. **Sanitized & license-safe** 🛡️  
   Fixtures must be **public-shareable** and properly attributed in metadata when derived from real sources.

---

## 🗂️ Recommended layout

This folder can evolve, but aim for a clear separation between **API mocks**, **geospatial payloads**, and **metadata**:

```text
web/data/fixtures/
├── 📄 README.md
├── 📁 manifest/                       # “What’s here?” + versioning + provenance pointers
│   └── 📄 fixtures.manifest.json
├── 📁 api/                            # Mock API responses (contract-shaped)
│   ├── 📄 datasets__list.v1.json
│   ├── 📄 datasets__get__demo-layer.v1.json
│   ├── 📄 storynodes__list.v1.json
│   └── 📄 storynodes__get__demo-story.v1.json
├── 📁 geo/                            # GeoJSON / TopoJSON samples used by the map
│   ├── 📄 ks_counties_simplified.geojson
│   └── 📄 sample_points.geojson
├── 📁 catalogs/                       # Small “boundary artifacts” snapshots
│   ├── 📁 stac/
│   │   ├── 📁 collections/
│   │   └── 📁 items/
│   ├── 📁 dcat/
│   └── 📁 prov/
└── 📁 ui/                             # UI config presets used in demos/tests
    ├── 📄 layer_presets.json
    └── 📄 map_style_overrides.json
```

> [!NOTE]
> If your repo already has a different structure, **don’t churn it**—add a *small* `manifest/` and start converging gradually.

---

## 🏷️ Naming conventions

### API fixtures
Use names that communicate **endpoint intent** and **contract version**:

- `datasets__list.v1.json`
- `datasets__get__<dataset_id>.v1.json`
- `storynodes__get__<story_slug>.v1.json`

If you mock multiple variants (success/error/empty):
- `datasets__list.v1__empty.json`
- `datasets__get__demo-layer.v1__404.json`

### Geospatial fixtures
- Prefer: `snake_case`, descriptive, and stable.
- Include simplification hints: `*_simplified`, `*_sample`, `*_mini`.

Examples:
- `ks_counties_simplified.geojson`
- `railroads_1900_sample.geojson`

---

## 🧾 Fixture metadata (manifest pattern)

Add/maintain a manifest entry for every “meaningful” fixture (anything referenced by tests, demos, or UI presets).

Example: `manifest/fixtures.manifest.json`

```json
{
  "version": "0.1.0",
  "updated_at": "YYYY-MM-DD",
  "fixtures": [
    {
      "id": "datasets__list.v1",
      "type": "api",
      "path": "api/datasets__list.v1.json",
      "contract": {
        "kind": "openapi|jsonschema",
        "ref": "schemas/.../datasets.list.v1.schema.json",
        "version": "v1"
      },
      "provenance": {
        "derived_from": [
          "data/catalog/dcat/<dataset>.jsonld",
          "data/stac/collections/<collection>.json"
        ],
        "notes": "Snapshot taken from local API on commit <hash> and sanitized."
      },
      "license": "CC0-1.0|CC-BY-4.0|MIT|SEE_SOURCE",
      "contains_real_data": false
    }
  ]
}
```

> [!TIP]
> If it’s faster: start with `"contains_real_data": false` and only promote to true once license/provenance are explicitly recorded.

---

## 🗺️ GeoJSON guardrails (so MapLibre doesn’t cry)

When adding GeoJSON fixtures:

- **CRS:** assume **WGS84 / EPSG:4326** (lon/lat) unless your contract says otherwise.
- **Precision:** reduce coordinate precision (often ~5–6 decimals is plenty).
- **Simplify geometry:** use simplified boundaries (TopoJSON is great for polygons).
- **Keep properties lean:** avoid huge attribute blobs.

Minimal `FeatureCollection` example:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "demo-point-001",
      "geometry": { "type": "Point", "coordinates": [-96.5767, 39.1836] },
      "properties": { "label": "Demo point", "year": 1854 }
    }
  ]
}
```

---

## 🔌 How fixtures should plug into the UI

A healthy pattern is:

- ✅ **Production:** UI → API → governed data
- ✅ **Dev/Test:** UI → fixture loader (or mock service worker) → fixture JSON
- ❌ **Never:** UI → fixtures as a hidden production dependency

### Common approaches
- **Mock Service Worker (MSW):** intercept fetch calls and return `web/data/fixtures/api/*`.
- **Feature flag:** `USE_FIXTURES=true` toggles a fetch adapter.
- **Storybook-only imports:** components import fixtures only inside stories/tests.

> [!WARNING]
> If you import fixtures from production bundles, you may accidentally ship them.  
> Keep fixture imports behind test/dev entrypoints.

---

## ✅ Validation checklist (PR “Definition of Done”)

When adding/changing fixtures:

- [ ] 📦 Updated `manifest/fixtures.manifest.json`
- [ ] 🧾 Fixture conforms to the relevant **schema/contract**
- [ ] 🧊 Fixture is deterministic (stable ordering, stable IDs)
- [ ] 🧹 No secrets / tokens / personal data
- [ ] 🏷️ License + attribution recorded (or marked `SEE_SOURCE`)
- [ ] 🗺️ Geometries are simplified and reasonable in size
- [ ] 🧪 Tests/demos that use the fixture still pass

---

## 🛡️ Security & governance notes

- Assume fixtures are **public** once committed.
- Follow **classification propagation** thinking: if a source is restricted, your fixture **cannot** be less restricted.
- Prefer **synthetic** or **toy** data for UI behaviors (popups, legends, filters, time sliders).

---

## 🧩 Related docs you’ll probably want open

From repo root (approx paths):
- 📘 `docs/MASTER_GUIDE_v13.md` — canonical pipeline ordering & invariants
- 🧱 `schemas/` — JSON Schemas for UI/API/catalog artifacts
- 🔌 `src/server/` — API boundary (fixtures should mirror these contracts)
- 🗺️ `web/` — UI implementation (React + MapLibre; optional Cesium)

---

## 📚 Project reference library (why these fixture rules exist)

<details>
<summary><strong>Click to expand the “project files” map 🧭📦</strong></summary>

| Project file | How it informs fixtures (what to borrow) |
|---|---|
| **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf** | Architecture separation, provenance-first, contract-first, map UI expectations (MapLibre/Cesium), open geospatial formats |
| **MARKDOWN_GUIDE_v13.md.gdoc** | Canonical pipeline ordering, governance, “no bypassing” rules, and boundary artifact expectations |
| **python-geospatial-analysis-cookbook.pdf** | Practical patterns for generating/exporting GeoJSON and PostGIS-friendly shapes for small samples |
| **making-maps-a-visual-guide-to-map-design-for-gis.pdf** | Cartographic sanity checks (don’t overload layers, keep symbols/attributes readable in demos) |
| **Mobile Mapping_ Space, Cartography and the Digital...pdf** | Offline/low-bandwidth thinking → keep fixtures compact and intentional |
| **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** | Lightweight thumbnails/fixture imagery choices and tradeoffs |
| **webgl-programming-guide...webgl.pdf** | If/when fixtures include tiny 3D assets (glTF snippets, 3D tiles metadata) |
| **responsive-web-design-with-html5-and-css3.pdf** | Fixture-driven UI states across breakpoints (mobile-first demos) |
| **Database Performance at Scale.pdf** | Don’t “dump databases” into fixtures; simulate interfaces, not storage |
| **Scalable Data Management for Future Hardware.pdf** | Streaming mindset: prefer references/metadata over embedding heavy data |
| **Cloud-Based Remote Sensing with Google Earth Engine...pdf** | Remote sensing layers should be referenced as catalogs/tiles; fixtures should be tiny previews |
| **Scientific Modeling and Simulation (NASA-grade) ...pdf** | If you add simulation outputs as fixtures: include metadata, parameters, determinism notes |
| **Understanding Statistics & Experimental Design.pdf** | If fixtures include stats charts: include known distributions/expected results |
| **regression-analysis-with-python.pdf** / **slides-linear-regression.pdf** | Predictable “toy” datasets for chart + model UI testing |
| **think-bayes-bayesian-statistics-in-python.pdf** | Sample priors/posteriors for uncertainty UI elements (keep small + explicit) |
| **graphical-data-analysis-with-r.pdf** | Canonical plots & edge cases for visualization fixtures |
| **Spectral Geometry of Graphs.pdf** | If you ship graph fixtures: keep tiny subgraphs with known properties |
| **Data Spaces.pdf** | Interop mindset: fixtures should mimic portable, standards-aligned payloads |
| **Introduction to Digital Humanism.pdf** | Human-centered UI fixtures (avoid dark patterns, respect user trust) |
| **On the path to AI Law’s prophecies...pdf** | If fixtures touch AI outputs: label clearly, keep traceable, avoid deceptive authority |
| **ethical-hacking-and-countermeasures...pdf** / **Gray Hat Python...pdf** | Security posture: never store secrets, treat all fixture data as public |
| **PostgreSQL Notes for Professionals...pdf** | If fixtures represent SQL-ish data: stable IDs, consistent types, minimal rows |
| **Archaeological 3D GIS...pdf** | 3D/heritage data fixtures should be carefully scoped + provenance-aware |
| **Generalized Topology Optimization...pdf** | If including design/simulation fixtures: store parameters + simplified outputs |
| **A / B-C / D-E / F-H / I-L / M-N / O-R / S-T / U-X programming Books.pdf** | General implementation patterns (scripts, CI, testing) and language/tool reference for fixture tooling |

</details>

---

## ⬆️ Back to top

[↑](#-fixtures--web-ui-webdatafixtures)