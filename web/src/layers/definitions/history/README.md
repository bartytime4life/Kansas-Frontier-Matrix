# 🏛️ History Layer Definitions (KFM)

![Domain](https://img.shields.io/badge/domain-history-1f6feb?style=flat-square)
![UI](https://img.shields.io/badge/UI-React%20%2B%20TypeScript-0b7285?style=flat-square)
![Maps](https://img.shields.io/badge/maps-MapLibre%20%2B%20Cesium-8250df?style=flat-square)
![Policy](https://img.shields.io/badge/FAIR%20%2B%20CARE-required-2da44e?style=flat-square)
![Provenance](https://img.shields.io/badge/provenance-first-f85149?style=flat-square)

Welcome to **`web/src/layers/definitions/history/`** 👋  
This folder is the **UI-facing registry/config layer** for **historical map overlays** (vector tiles, raster tiles, and small GeoJSON overlays) that the KFM web client can toggle, style, filter by time, and cite. This sits squarely in the **“(E) New UI layer or feature”** extension category: layers are added by extending the UI layer registry/config and **must tie back to provenance** and **respect CARE**, including coordinate hiding if sensitive.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> [!IMPORTANT]
> **`web/` is the single source of truth for the user-facing interface** (excluding narrative content), and it must not contain “hidden data files” or direct DB queries — it consumes the API and renders what the API returns.  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗺️ What counts as a “History” layer?

History layers are **time-indexed** or **era-representative** views of Kansas (and connected regions) that support over-time comparison, storytelling, and research. Common layer families include:

- 🗞️ **Archival & documentary-linked geography** (places/events referenced in texts)
- 🧭 **Settlements & infrastructure** (towns, forts, trading posts, trails, railroads)
- 🗺️ **Historical topographic maps** (e.g., georeferenced USGS scans, organized by year/scale)  [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- 📐 **Cadastral / land ownership / PLSS** + **treaty & reservation boundaries** (with date attributes)  [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- 🌾 **Land cover / hydrology over time** (river courses, wetlands, reservoirs, etc.)  [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

The front-end is designed to support **layer toggles by time period** and a **time slider** for moving through historical eras.  [oai_citation:5‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

---

## 🔌 How a history layer reaches the map (end-to-end)

KFM uses a layered architecture: **data → catalog/graph → API → UI**.  [oai_citation:6‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

```mermaid
flowchart LR
  A[(📁 data/<domain>/raw)] --> B[⚙️ src/pipelines/ ETL + validation]
  B --> C[(📦 STAC/DCAT/PROV catalogs)]
  B --> D[(🧱 Tiles: /tiles/{layer}/{z}/{x}/{y}.*)]
  C --> E[📚 API: /api/v1/datasets/{id} + /api/v1/catalog/search]
  D --> F[🌐 web/src/layers/definitions/history/]
  E --> F
  F --> G[🗺️ MapLibre (2D) + Cesium (3D)]
  G --> H[🧠 Focus Mode & Story Nodes: provenance-linked UX]
```

### 🧱 Tiles (the “big data” path)
The backend serves standardized map tiles for layers:

- Vector (MVT): `GET /tiles/{layer}/{z}/{x}/{y}.pbf`
- Raster: `GET /tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`)  [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

This allows multiple clients (web/3D/mobile) to consume the **same tile well**.  [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 📚 Dataset metadata (the “citation & UX truth” path)
The API exposes dataset metadata and discovery:

- `GET /api/v1/datasets/{id}` (DCAT summary + STAC assets)
- `GET /api/v1/catalog/search` (keyword/bbox/time-range search)
- `GET /api/v1/datasets/{id}/data?format=geojson&bbox=...` (stream features, filtered)  [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧭 Folder expectations & naming conventions

### 📁 Typical structure (example)
```text
web/src/layers/definitions/
└── 📁 history/
    ├── 📄 README.md                👈 you are here
    ├── 📄 index.ts                 (exports the history registry)
    ├── 📄 trails.layer.ts          (example: vector tile + time filter)
    ├── 📄 treaties.layer.ts        (example: polygons w/ date attributes)
    └── 📁 topo/
        ├── 📄 usgs_1880s.layer.ts  (example: raster tile era maps)
        └── 📄 usgs_1950s.layer.ts
```

### 🏷️ Stable IDs are non-negotiable
A layer ID should be:

- ✅ **stable across releases**
- ✅ aligned with the server’s tile name (`/tiles/{layer}/...`)
- ✅ URL/bookmark-safe (`snake_case` recommended)
- ✅ treated as an external contract (users + stories + saved views will reference it)

---

## 🧩 The layer definition contract (what every history layer must provide)

> [!NOTE]
> Exact types/interfaces will live in the `web/` codebase, but the UI *must* treat the registry config as a contract artifact (layer registry config is explicitly called out as part of UI “contracts”).  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### ✅ Minimum required fields (recommended)
Every history layer definition should have, at minimum:

- **Identity:** `id`, `title`, `description`, `tags`, `domain: "history"`
- **Data hookup:** `kind` (`vector-tile` | `raster-tile` | `geojson`), URL templates (relative to API base)
- **Temporal semantics:** how the layer responds to the timeline (`currentYear`, range, era bins)
- **Rendering:** MapLibre layer style(s), legend entries
- **Provenance:** dataset ID (DCAT/STAC), license, how to cite
- **Sensitivity:** `public|internal|sensitive` + redaction requirements

Why so heavy on metadata? Because dependable GIS practice requires metadata that includes **citation** and **temporal** information, and growing digital location data increases **locational privacy risk**.  [oai_citation:11‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

### 🧪 Example (TypeScript-ish pseudocode)
```ts
export const historicTrails: HistoryLayerDefinition = {
  id: "historic_trails",
  domain: "history",

  title: "Historic Trails",
  description: "Major historic trails and routes with approximate active years.",
  tags: ["transport", "trails", "overland"],

  // Data hookup
  kind: "vector-tile",
  tiles: {
    // Prefer the canonical /tiles endpoint pattern; keep base URL configurable.
    template: "/tiles/historic_trails/{z}/{x}/{y}.pbf",
    minzoom: 4,
    maxzoom: 14,
  },

  // Temporal behavior (timeline integration)
  temporal: {
    granularity: "year",
    // If features have a range, the UI can filter where:
    // start_year <= currentYear <= end_year
    startField: "start_year",
    endField: "end_year",
    // When data is uncertain, use null-safe rules + visual cues (see below).
    uncertaintyField: "date_confidence",
  },

  // MapLibre rendering
  maplibre: {
    sourceLayer: "historic_trails", // MVT layer name inside the tile
    layers: [
      {
        id: "historic_trails_line",
        type: "line",
        paint: {
          // dashed lines is a typical treatment for routes/trails
          "line-width": 2,
          "line-dasharray": [2, 2],
        },
      },
    ],
    legend: [
      { label: "Historic trail (approx.)", symbol: "line-dashed" },
    ],
  },

  // Provenance (must be shown in UI)
  provenance: {
    datasetId: "ks_historic_trails",
    // The UI should be able to fetch metadata via /api/v1/datasets/{id}
    datasetApiPath: "/api/v1/datasets/ks_historic_trails",
    citationText: "…", // short cite string shown in legend/info panel
    license: "…",
  },

  // Sensitivity & redaction requirements
  sensitivity: {
    level: "public", // public | internal | sensitive
    // Optional: rules the UI must enforce
    uiRedactions: {
      disableMaxZoom: false,
      roundCoordinates: false,
    },
  },
};
```

---

## 🕰️ Temporal behavior: how history layers must “move” with time

KFM’s UI state is designed to synchronize components: if the user changes a year on the timeline, a global store updates `currentYear`, and both the **map component** and narrative/UI components respond.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🧠 Two time models you’ll see in this folder
1. **Range-valid features** (most vector history layers)  
   Example: treaty boundary active 1854–1867 → show only within that range.

2. **Era/edition layers** (common for scanned maps / raster overlays)  
   Example: “USGS topo 1890s” is not a feature-by-feature range; it’s a layer representing an edition/period. The system organizes these layers by date/scale in metadata.  [oai_citation:13‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

### 🧩 Handling uncertainty (don’t lie with precision)
If your history layer has uncertain dates:
- Represent uncertainty explicitly (confidence flags / approximate year)
- Prefer UI cues (e.g., dashed outlines, dotted lines, “circa” labeling)

A key visualization caution: connecting points across time can imply certainty where none exists; missing/uncertain data should be made visible (e.g., dotted lines).  [oai_citation:14‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)

---

## 🧾 Provenance & citations (hard gate)

KFM’s design principles emphasize **“Provenance First”**: nothing enters without provenance; every record is tied to a source and traceable.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

When adding a **new UI layer**, the Master Guide explicitly requires:
- layers **tie back to provenance**
- overlays include an **info popup or legend that cites the data source (DCAT/STAC)**
- coordinate hiding when sensitive (CARE compliance)  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### ✅ What this means in practice (for history layers)
Your layer definition should ensure the UI can always show:

- **Source dataset title**
- **License / usage constraints**
- **How to cite**
- **Link back to dataset metadata** (`/api/v1/datasets/{id}`)  [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

> [!TIP]
> Treat provenance like a “UI feature,” not a compliance tax. It makes layers *trustworthy* and makes Focus Mode + Story Nodes safer to use.

---

## 🔒 Data sensitivity & governance (FAIR + CARE)

KFM supports **FAIR+CARE**, especially for Indigenous/sovereignty and sensitive-site concerns. Sensitive location data should be protected via:
- coordinate rounding
- generalization/aggregation
- access control
…and datasets can be tagged `public`, `internal`, or `sensitive`.  [oai_citation:18‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

Additionally, the UI contract explicitly requires:  
**UI must cause no data leakage** and must respect redaction rules (e.g., “no map zoom that bypasses them”), while maintaining accessibility and audit logs.  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧷 RBAC/OPA implications for layer definitions
The backend enforces access control with an RBAC model and OPA policy checks, using a **“fail closed”** philosophy (no access unless allowed).  [oai_citation:20‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

**Implication for this folder:**  
Your layer definitions should be ready for the API to:
- return **sanitized geometry**
- return **generalized tiles**
- hide attributes
- deny access entirely based on user role

…and the UI must handle these outcomes gracefully.

---

## 🧰 Adding a new History layer (meticulous runbook)

> [!IMPORTANT]
> Adding a layer is *usually* not just UI: it often touches **(A) data**, **(D) API**, and **(E) UI**. The Master Guide calls this out explicitly as a multi-touchpoint pattern.  [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 1) 📦 Data & metadata are ready
- [ ] Raw data lives under `data/<domain>/raw/` (read-only) and follows the domain layout pattern.  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] ETL is deterministic and logged (reproducible outputs for given inputs).  [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] STAC/DCAT/PROV records exist and validate (no dataset accepted without valid metadata).  [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Time coverage is represented (year/range/era) and is queryable.

### 2) 🧱 Tiles or GeoJSON are served by the API
- [ ] For large layers: vector tiles are available via `/tiles/{layer}/{z}/{x}/{y}.pbf`  [oai_citation:26‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- [ ] For rasters: `/tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`) exists  [oai_citation:27‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- [ ] For small layers: GeoJSON streaming endpoint exists (`/api/v1/datasets/{id}/data?...`)  [oai_citation:28‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 3) 🌐 Create the UI layer definition
- [ ] Create `*.layer.ts` in this folder (or a subfolder)  
- [ ] Export it from `history/index.ts` (or the local registry)
- [ ] Make sure `id` matches server layer naming
- [ ] Provide MapLibre layer styling + legend

MapLibre is the 2D engine; layers may be tile layers or GeoJSON overlays, and the map component styles them (e.g., “Historic Trails” dashed lines), with a legend/layer control showing symbology.  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 4) 🕰️ Integrate with timeline filtering
- [ ] Declare temporal fields or era bins
- [ ] Ensure the layer can respond to `currentYear` updates from global state  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Provide uncertainty visualization (don’t overclaim precision)

### 5) 🧾 Add provenance UX (legend/popup/info panel)
- [ ] Legend cites DCAT/STAC source
- [ ] Popup links to dataset metadata (`/api/v1/datasets/{id}`)  [oai_citation:31‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- [ ] License is visible in UI

### 6) 🔒 Sensitivity classification (and redaction plan)
- [ ] Tag sensitivity `public|internal|sensitive`  [oai_citation:32‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- [ ] If sensitive: document redaction + ensure UI can’t bypass it (zoom rules, attribute hiding, etc.)  [oai_citation:33‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] If sensitive: expect governance review triggers (contracts can’t be broken silently).  [oai_citation:34‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧠 Design notes: avoid clutter + protect privacy (especially for movement/paths)

If you’re rendering movement/flows (e.g., trails, migrations, shipments), heavy overlap can clutter the map. One approach is to show **abstracted trajectories**, aggregating time into intervals and places into larger regions.  [oai_citation:35‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)

For time-linked location histories, consider **resolution controls** + **time range filters** so users can explore at a safer, clearer scale.  [oai_citation:36‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)

These techniques often align nicely with CARE-driven privacy protection (less precise data by default) and with performance constraints.

---

## 🧯 Troubleshooting checklist

### “Layer toggles on, but nothing shows”
- ✅ Tile endpoint exists and is reachable (`/tiles/{layer}/...`)  [oai_citation:37‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- ✅ `sourceLayer` matches the MVT layer name inside the tile
- ✅ MapLibre style layer ID is unique
- ✅ `minzoom/maxzoom` matches expected visibility

### “Timeline changes but layer doesn’t update”
- ✅ Layer declares temporal semantics and uses the same year signal as the global store (`currentYear`)  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- ✅ Filters are applied to the correct layer IDs

### “Sensitive points are visible at high zoom”
- 🚨 This is a contract violation: UI must not allow zoom to bypass redactions.  [oai_citation:39‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Ensure the dataset is generalized upstream and/or max zoom is capped for that layer.

---

## 📚 References & project files

### 🧱 Core KFM docs (highly recommended)
- **KFM Comprehensive System Documentation** — API endpoints, tiles, and system patterns:  [oai_citation:40‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- **KFM Master Guide v13** (repo structure, contracts, extension points, governance):  [oai_citation:41‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

### 🗺️ History + mapping design
- **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design** — historical layer families + time slider UI concept:  [oai_citation:42‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
- **Making Maps: A Visual Guide to Map Design for GIS** — metadata, citation info, temporal info, and privacy cautions:  [oai_citation:43‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)  
- **Visualization of Time-Oriented Data** — temporal filtering/resolution and flow/movement abstraction patterns:  [oai_citation:44‡Visualization of Time-Oriented Data.pdf](sediment://file_000000001468722f929b8752236e5a72)  

### 🌐 Web/UI craft (for contributors working in `web/`)
- **Professional Web Design Techniques and Templates**:  [oai_citation:45‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- **Learn to Code HTML & CSS**:  [oai_citation:46‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- **Node.js + React + CSS + HTML**:  [oai_citation:47‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  

### ⚖️ Equity / ethics / reporting rigor (helps when mapping people & communities)
- **Indigenous Statistics** (data sovereignty-adjacent thinking):  [oai_citation:48‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)  
- **AI & ML in Health Care & Medical Sciences** (best-practice/checklist mindset for high-stakes claims):  [oai_citation:49‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)  

---

## ✅ Definition of done (for any new history layer PR)

- [ ] Layer renders correctly in 2D (MapLibre) and does not break 3D mode expectations (Cesium)
- [ ] Timeline behavior is correct (year/range/era)
- [ ] Provenance is visible in legend/popup and links to dataset metadata
- [ ] Sensitivity classification is set; redactions are enforced (UI cannot bypass)
- [ ] IDs are stable + documented
- [ ] Any contract/schema implications are updated & validated (contract-first mindset)  [oai_citation:50‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)