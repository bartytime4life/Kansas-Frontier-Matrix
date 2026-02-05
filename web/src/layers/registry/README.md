# 🧩 Layer Registry

> **Purpose:** This folder is the **single source of truth** for what the KFM web map can render, how it’s styled, and how it stays compliant with the project’s **provenance + governance** guarantees.  
> The registry exists so “adding a layer” is **repeatable**, **auditable**, and **hard to do wrong**. ✅

---

## 🗺️ What “Layer Registry” means in KFM

KFM’s front-end is intentionally map‑centric (React + MapLibre for 2D, optional Cesium for 3D) and is designed to **consume governed data through the backend API**, not by reaching around it. The architecture explicitly preserves a “truth path” so every displayed fact remains traceable.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

This registry is where we declare:

- **Which** layers exist (IDs, titles, descriptions)
- **How** they load (vector tiles, raster tiles, GeoJSON overlays, 3D tiles/terrain)
- **How** they render (style rules, ordering, legend semantics)
- **How** they comply (provenance links, licensing, sensitivity controls, access expectations)

Map clients (MapLibre/OpenLayers/etc.) can consume KFM layers via **tile endpoints** (vector `.pbf` or raster `.png/.webp`), and the broader system goal is that multiple clients can “drink from the same well.”  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🔒 Non‑negotiables (KFM invariants)

### 1) The UI never bypasses governance
All access flows through the backend API and policy engine; the web UI does not “sneak” direct database access or embed hidden raw datasets.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 2) Every layer ties back to provenance (FAIR + CARE)
When you add a UI layer, it must link back to its provenance (typically via DCAT/STAC metadata surfaced in an info panel, legend, or layer details UI). This is a documented extension point: *“New UI layer → extend the layer registry/config → tie to provenance → comply with CARE (e.g., hide sensitive precision).”*  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) Validation gates are expected
KFM’s contribution model is built around automated checks that enforce invariants (metadata completeness, provenance integrity, security scans, etc.). Treat the registry the same way: missing provenance or broken linkage should fail fast.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 4) Accessibility + no leakage
The UI is an “internal contract” surface: it must remain accessible and must not leak sensitive data (including via map zoom/detail, filters, or UI affordances).  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ What belongs here (and what doesn’t)

### ✅ Belongs
- Layer definitions (metadata + rendering intent)
- Style declarations (MapLibre paint/layout fragments, symbol rules)
- Legend definitions (what the symbology means)
- Ordering rules (z‑order / draw order / grouping)
- Governance flags (sensitivity, access hints, redaction expectations)

### ❌ Does *not* belong
- Raw data files (GeoJSON dumps, CSVs, rasters, scans, etc.)
- Secrets, tokens, private URLs
- “Copy-pasted” symbology from copyrighted maps
- Anything that bypasses the API truth path

> 📌 Reminder: Map *representations* (symbology/layout choices) can be copyrighted even when the underlying facts are not. Be careful to create original styling and provide correct attribution/licensing.  [oai_citation:6‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

---

## 🧱 Layer entry model (recommended schema)

The exact TypeScript types may differ in this repo, but the **registry entry** should be able to express *at minimum* the following concepts.

| Field | Purpose | Notes |
|------|---------|------|
| `id` | Stable layer identifier | Prefer aligning with backend `{layer}` tile name and/or dataset ID patterns (e.g., `ks_hydrology_1880`).  [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) |
| `title` / `description` | Human-facing summary | Short, neutral, non-speculative |
| `kind` | Render type | `vector-tiles`, `raster-tiles`, `geojson`, `terrain`, `3d-tiles`, etc. (MapLibre supports tile layers + GeoJSON overlays).  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) |
| `source` | Where it loads from | Typically API tile endpoints (`/tiles/{layer}/{z}/{x}/{y}.pbf` or `.png/.webp`).  [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) |
| `style` | How it looks | MapLibre paint/layout; keep styles declarative |
| `legend` | What the symbols mean | Legend items must match actual rendering |
| `attribution` | Credit + license | Must be displayable in UI; avoid “hidden” attribution |
| `provenance` | Traceability hooks | Link to DCAT/STAC/PROV identifiers when possible (truth path).  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) |
| `minZoom` / `maxZoom` | Performance + intent | Prevent heavy layers at broad zooms |
| `defaultVisibility` | UX baseline | Defaults should be conservative for heavy/sensitive layers |
| `bbox` / `bounds` | Load limiting | Optional but recommended where known |
| `time` | Temporal filtering | If time-aware, declare supported time range/field |
| `sensitivity` | Safety & CARE | Drives redaction / generalization / access gates |
| `tags` / `group` | Discoverability | “Hydrology”, “Trails”, “Settlements”, etc. |

---

## 🧾 Minimum metadata you must be able to answer

Even if your code stores this differently, dependable GIS layers should be able to report **identification, quality, spatial organization, spatial reference, attribute/entity info, distribution/use policy, citation, temporal info, and contact**.  [oai_citation:11‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

That guidance maps cleanly to KFM’s broader catalog + provenance requirements (STAC/DCAT + PROV).  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 Layer kinds supported by KFM UI (conceptual)

### 🧩 MapLibre GL (2D)
KFM uses MapLibre for interactive 2D mapping; layers generally arrive as:
- **Tile layers** (vector `.pbf` or raster tiles) for large datasets  
- **GeoJSON overlays** for smaller datasets that can be transmitted as features directly  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> Example from project docs: toggling a layer like “Historic Trails” could request vector tiles via an API path and then style as dashed lines, etc.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🌐 CesiumJS (3D)
KFM can provide a 3D globe/terrain mode with Cesium, likely via a UI toggle. In 3D mode, the app can render imagery layers, terrain, and potentially 3D Tiles or glTF assets for reconstructions.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🛠️ Adding a new layer (repeatable checklist)

> If you only read one thing: follow this checklist and your PR should be painless. ✅

### 0) Confirm the “truth path” exists
- The dataset is ingested and published with catalog/provenance artifacts (STAC/DCAT + PROV).
- You are not shipping raw data into `web/`.

This aligns with the project’s staged pipeline model and its “traceability from raw to UI” promise.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 1) Confirm backend access (API contract)
At minimum you should be able to point to one of these:
- Dataset metadata (`GET /api/v1/datasets/{id}`)  [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Tiles (`GET /tiles/{layer}/{z}/{x}/{y}.pbf` or `.png/.webp`)  [oai_citation:18‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

> ⚠️ Note: some docs reference `/api/tiles/...` while others show `/tiles/...`. Treat these as *examples* and match the actual API base path used by the repo.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:20‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 2) Create the registry entry
- Choose a stable `id`
- Add title/description
- Declare `kind`, `source`, and zoom constraints
- Attach `attribution` + `license`
- Attach `provenance` pointers (DCAT/STAC identifiers or URLs stored elsewhere)

### 3) Add styling + legend
Use strong **figure–ground** discipline:
- Important features must read as figure
- Supporting context should recede
- Keep symbology consistent across layers and stories  [oai_citation:21‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

### 4) Wire into UI controls (if needed)
If the layer needs:
- A toggle
- Grouping
- Legend rendering
- Time slider interaction

…make sure it’s consistent with the app’s global state approach (timeline/year changes driving map + story updates).  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 5) Apply governance flags (especially for sensitive layers)
KFM explicitly supports FAIR + CARE governance. Certain precise locations may need to be generalized or hidden (rounding, aggregation to county, suppression rules, etc.).  [oai_citation:24‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

If the layer involves Indigenous communities/knowledge:
- Treat it as **Indigenous data**
- Ensure governance is integrated throughout the lifecycle
- Use metadata/labels to preserve provenance and authority (TK/BC labels are cited as mechanisms to assert authority where legislation is lacking)  [oai_citation:25‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)

### 6) Test (don’t skip)
Even old-school advice still holds: after changes, test in real browsers and viewport sizes so “it works on my machine” doesn’t ship.  [oai_citation:26‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)

Also test:
- Layer ordering (no accidental occlusion)
- Legend correctness
- Performance at min/max zooms
- Accessibility of toggles/controls (keyboard + screen reader expectations)

---

## 🕰️ Time-aware layers & scrollytelling hooks

KFM stories are time-driven: the UI includes a timeline slider and scrollytelling behaviors that update the map as the story progresses.  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

If a layer is time-aware, encode (somewhere in its entry):
- The time field or dimension it responds to
- Its valid time range
- Any “snap” rules (years only vs. date ranges)
- What happens outside the valid range (hide? clamp? show empty state?)

---

## 🧠 Sensitivity, privacy, and Indigenous Data Sovereignty

### Practical patterns KFM already anticipates
- Coordinate rounding / spatial aggregation for public views
- Suppression thresholds for small-n categories (avoid re-identification)
- Query auditing and limiting overly specific filters to prevent inference attacks  [oai_citation:28‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Registry responsibilities (your job when adding layers)
Add enough information so the UI can do the *right* thing by default:
- `sensitivity: "public" | "internal" | "sensitive" | ...`
- Default visibility **off** for sensitive layers
- Notes on generalization expectations (e.g., “county-level only”)
- UI copy for the layer info panel explaining restrictions

Indigenous Data Sovereignty and CARE emphasize balancing open data with protection of Indigenous rights and interests, including minimum expectations for data sharing and mechanisms to maintain provenance/authority.  [oai_citation:29‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)

---

## ♿ Accessibility & UI consistency (layer controls)

Layer toggles and legends are part of the “front door” to KFM knowledge. KFM documentation highlights usability/accessibility expectations for UI components.  [oai_citation:30‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)

**Implementation reminders:**
- Use semantic elements where possible (`nav`, `main`, etc.) to improve structure and accessibility.  [oai_citation:31‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)
- Make interactive controls keyboard reachable and clearly labeled
- Ensure legends are not color-only (shape/line pattern redundancy)

---

## 🧪 Validation & testing expectations (recommended)

Because the UI is an internal contract surface, consider adding (or maintaining) automated checks such as:

- ✅ Unique `id` validation (no duplicates)
- ✅ Required fields present (`title`, `kind`, `attribution`, provenance pointer)
- ✅ Zoom sanity checks (`minZoom <= maxZoom`)
- ✅ “Sensitive layer” rules (must not default to on, must have policy notes)
- ✅ Link validation for provenance pointers (where applicable)

This aligns with KFM’s CI gate philosophy and the UI contract expectations around accessibility and leakage prevention.  [oai_citation:32‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:33‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧯 Troubleshooting quick hits

<details>
<summary><strong>Layer toggle turns on but nothing draws</strong> 🫥</summary>

- Check `minZoom/maxZoom` (you might be outside the range)
- Confirm the tile endpoint returns data for the current viewport
- Confirm style filters match the tile layer source-layer / fields
- Confirm ordering (your layer may be drawing under a basemap fill)
</details>

<details>
<summary><strong>Tiles 404 / errors</strong> 🚫</summary>

- Verify the backend path pattern (docs show both `/tiles/{layer}/...` and `/api/tiles/...` as examples)  [oai_citation:34‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:35‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Verify the layer ID matches the backend `{layer}` name exactly
</details>

<details>
<summary><strong>Legend doesn’t match the map</strong> 🎭</summary>

- Ensure legend categories mirror real style rules (filters/thresholds)
- Confirm figure–ground intent: primary features should pop, context should recede  [oai_citation:36‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)
</details>

---

## 🧷 “Illustrative” TypeScript example

> ⚠️ This is **illustrative**, not authoritative. Use whatever types exist in this repo, but keep the same *conceptual fields*.

```ts
export type LayerKind =
  | "vector-tiles"
  | "raster-tiles"
  | "geojson"
  | "terrain"
  | "3d-tiles";

export interface LayerRegistryEntry {
  id: string;
  title: string;
  description?: string;

  kind: LayerKind;

  // Backend wiring
  datasetId?: string;          // e.g., "ks_hydrology_1880"
  tilePathTemplate?: string;   // e.g., "/tiles/{layer}/{z}/{x}/{y}.pbf"

  // Rendering intent
  minZoom?: number;
  maxZoom?: number;
  defaultVisibility?: boolean;

  // Governance + traceability
  attribution: { text: string; license?: string };
  provenance: {
    dcatId?: string;
    stacCollectionId?: string;
    provBundleId?: string;
  };

  sensitivity?: "public" | "internal" | "sensitive";
  tags?: string[];
  group?: string;
}
```

---

## 📚 Project sources used for this README

These are the primary internal docs/books consulted while writing this file:

- KFM architecture & truth path (UI ↔ API ↔ policy)  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- KFM API capabilities (datasets + tiles)  [oai_citation:38‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- UI extension points + layer registry requirement  [oai_citation:39‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- GIS metadata minimums + copyright considerations  [oai_citation:40‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)
- CARE / Indigenous data governance considerations  [oai_citation:41‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)

---

## 🔗 File citations (system links)

> These markers intentionally surface the underlying project files referenced by the assistant.

-  [oai_citation:42‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)
-  [oai_citation:43‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)
-  [oai_citation:44‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
-  [oai_citation:45‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)
-  [oai_citation:46‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)