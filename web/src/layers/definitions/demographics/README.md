# 📊 Demographics — Layer Definitions (KFM Web)

![Domain](https://img.shields.io/badge/domain-demographics-0b7285)
![Frontend](https://img.shields.io/badge/web-react%20%2B%20typescript-2f9e44)
![Maps](https://img.shields.io/badge/maps-MapLibre%20GL%20JS-1c7ed6)
![Catalog](https://img.shields.io/badge/metadata-DCAT%20%2B%20STAC-845ef7)
![Governance](https://img.shields.io/badge/governance-CARE%20%2B%20FAIR-f03e3e)

> **Location:** `web/src/layers/definitions/demographics/`  
> **Purpose:** Define *how demographic datasets appear and behave* in the KFM map UI (legend, styling, provenance links, time behavior, tooltips, safe defaults).

---

## 🧭 What “Demographics” means in KFM

Demographics layers describe **people, households, and community conditions** over space and (often) time. In KFM, this typically includes:

- 👥 **Population** (counts, density, change)
- 🧒🧑🧓 **Age structure** (median age, cohorts, dependency ratios)
- 🏠 **Households & housing** (household size, housing units, tenure)
- 💼 **Economy** (income, poverty, employment)
- 🎓 **Education** (attainment)
- 🧭 **Mobility & settlement** (migration proxies, urban/rural patterns)
- 🕰️ **Historical census views** (territorial/state/federal snapshots where available)

> 🚫 **Non-goal:** this folder is not for raw data, ETL, or database schema definitions. It is for **front-end layer configuration** only.

---

## 🧩 How these definitions are used by the Web App

KFM’s front-end is a map-centric React app (TypeScript) that keeps key UI state in a global store (commonly Redux/Context patterns). Demographic layers must work cleanly with:

### ⏳ Timeline / “currentYear”
- When a user scrubs the timeline, the global store updates a `currentYear` (or equivalent).
- The **map and story panel stay in sync**: map filters time-aware layers; story highlights relevant sections.
- **Demographics layers must declare** how they respond to time changes (discrete year snapshots vs ranges).

✅ **Rule:** If the dataset is time-aware, the definition must encode **time compatibility** (e.g., available years, default year, or how to filter tiles/features).

### 🗺️ MapLibre rendering model
KFM uses MapLibre GL JS for 2D interactive mapping:
- **Vector tiles (MVT)** for large datasets (fast pan/zoom, server-side tiling)
- **GeoJSON overlays** for smaller datasets or ad-hoc queries
- Layer toggles and legends are driven by a **layer registry/config** model

✅ **Rule:** Choose the *lightest* client path: tiles for heavy layers, GeoJSON only when it’s small/filtered.

---

## 🔗 Provenance-first: data sources & metadata links

Every demographics layer must be traceable back to its dataset record:

### 📚 Dataset metadata
Demographics layers should link to dataset metadata from the backend catalog:
- Use dataset IDs that resolve through the catalog (DCAT summary + STAC assets).
- Surface **title, description, license, and lineage** in the layer info panel.

### 🧪 Data access patterns (frontend expectations)
Demographic layers generally consume data via:
- 🧊 **Tile endpoints** for map rendering (vector `.pbf` or raster `.png/.webp`)
- 🧾 **Dataset downloads / streaming** for small extents or tables
- 🔍 **Safe query endpoints** for advanced filtering (where permitted)

✅ **Rule:** The UI should never “invent” sources. If we can’t cite the dataset record, the layer isn’t ready.

---

## 🧱 Definition Contract (recommended shape)

Actual types may vary across the repo, but demographics definitions should follow a consistent contract.

### ✅ Minimum required fields
At minimum, each layer definition should include:

- `id` — stable and unique across all layers
- `title` — human-readable label for Layer Control
- `domain` / `category` — e.g., `demographics`
- `source` — how to fetch data (tile URL template or GeoJSON/query config)
- `style` — MapLibre layer spec(s): `paint`, `layout`, `filter`
- `legend` — how users interpret colors/symbols
- `provenance` — dataset/catalog references
- `time` — how to bind to `currentYear` (if applicable)
- `tooltips` / `popup` — safe fields for hover/click inspection

### 🧪 Example (TypeScript-ish pseudocode)
```ts
export const populationDensity: DemographicsLayerDefinition = {
  id: "demo.population_density",
  title: "Population Density",
  domain: "demographics",
  description: "People per sq. mile (normalized).",
  provenance: {
    datasetId: "census_population_density",
    // optionally: catalogUrl, license, attribution overrides
  },
  time: {
    mode: "discrete",                 // "none" | "discrete" | "range"
    availableYears: [1865, 1875, 1885, 1895, 1905, 1915, 1925],
    defaultYear: 1895,
    bindTo: "currentYear",            // how the UI state drives the layer
  },
  source: {
    kind: "vectorTile",               // "vectorTile" | "rasterTile" | "geojson" | "query"
    tiles: "/tiles/demo_pop_density/{z}/{x}/{y}.pbf",
    sourceLayer: "counties",          // MVT source-layer (if used)
  },
  style: {
    type: "fill",
    paint: {
      // no hard-coded colors here unless your project standard requires it;
      // prefer shared palettes + breaks utilities
    },
  },
  legend: {
    kind: "choropleth",
    unitLabel: "people / sq. mi.",
    // class breaks, labels, no-data behavior, etc.
  },
  popup: {
    titleField: "name",
    fields: [
      { label: "Year", field: "year" },
      { label: "Pop / sq. mi.", field: "pop_density" },
      { label: "Population (total)", field: "population" },
    ],
  },
};
```

---

## 🎨 Cartography & UX Rules for Demographics Layers

Demographics layers can mislead *fast* if the map design is sloppy. These rules keep interpretation honest.

### 1) Choropleth vs totals (⚠️ common pitfall)
- Choropleths are best for **rates/densities/normalized values**.
- Totals (raw counts) are often better shown via **graduated symbols** (or paired with a normalized choropleth).

✅ **Rule:** If you map a total as a fill choropleth, include an explicit warning in the layer description and provide an alternative when possible.

### 2) Legends must communicate reality (not vibes)
A good legend:
- Orders values intuitively (higher = more)
- Shows **class breaks** clearly
- Uses a **no-data** symbol that doesn’t look like “zero”
- Matches the layer’s real data distribution (avoid deceptive continuous ramps for discrete bins)

✅ **Rule:** Prefer **non-continuous binned legends** for classed choropleths unless the data are truly continuous and users benefit from interpolation.

### 3) Boundary dominance & readability
- Keep polygon boundaries present but not overpowering.
- Avoid pure white for “lowest class” if white is also used for “no data”.
- Default opacity should support stacking with other layers.

✅ **Rule:** Demographics layers should be stack-friendly: boundaries subtle, fills semi-transparent when overlap is expected.

### 4) Layer order matters
- “Fill” polygons (demographics) typically sit **below** boundary/label overlays.
- If a demographics fill layer is intended as context, ensure it doesn’t obscure points/lines needed for interpretation.

✅ **Rule:** Make the intended stacking order explicit (either via registry ordering or documented “recommended z-order”).

---

## 🧠 Ethics, CARE/FAIR, and “do no harm” display defaults

Demographics is **high-risk for misinterpretation and harm**, especially when mapped at small geographies or when describing Indigenous communities.

### ✅ Required guardrails
- **No PII ever.** No row-level people data in UI layers.
- Use **aggregation** (county/tract/region) appropriate to the metric.
- Consider **suppression/rounding** for small counts (re-identification risk).
- Avoid deficit-only narratives; provide context and limitations.

### 🪶 Indigenous Data Governance alignment
If a layer touches Indigenous populations, lands, or identities:
- Ensure the layer’s metadata reflects **authority, provenance, and permissions**
- Avoid reinforcing stereotypes through “deficit-only” framing
- Provide clear language about what the data can/cannot say
- Follow community governance where applicable (CARE-style expectations)

✅ **Rule:** “Demographics” layers must be as careful with **how** they tell a story as with **what** they show.

---

## 🧰 Adding a new demographics layer (Contributor Checklist)

### Step 0 — Confirm the dataset exists ✅
- Dataset has a stable `datasetId`
- Dataset metadata is in the catalog (DCAT/STAC)
- License/attribution is clear
- Time coverage is known (if applicable)

### Step 1 — Decide the delivery method 🚚
- Vector tiles for large polygon layers
- GeoJSON/query for bounded/small feature sets
- Raster only when necessary (e.g., pre-rendered density surfaces)

### Step 2 — Create the layer definition 🧩
- Create a new definition file (or extend `index.ts` registry export)
- Add: title, description, provenance, time behavior, style, legend, tooltip fields
- Use shared helpers for:
  - class breaks
  - palettes
  - number formatting
  - no-data rules

### Step 3 — Ensure timeline correctness ⏳
- If the dataset is a set of snapshots:
  - define `availableYears`
  - define mapping from `currentYear` → nearest supported year (if needed)
- If it is a range:
  - define `minYear`, `maxYear`, and filtering rules

### Step 4 — Validate safety & meaning 🧠
- Are we mapping a total with a choropleth? If yes, reconsider or justify.
- Are tooltips exposing sensitive/small-count values? If yes, suppress or aggregate.
- Does the layer description include limitations and context?

### Step 5 — UI polish ✅
- Layer name is short and scannable in the Layer Control
- Legend is readable and correctly labeled (units!)
- Popups show the *right* fields with friendly formatting
- Defaults don’t overwhelm the map

---

## 🧯 Common pitfalls & troubleshooting

### “My layer shows up but is blank”
- Wrong tile URL template (z/x/y mismatch)
- Wrong `sourceLayer` name (vector tiles)
- Filter excludes everything (year mismatch, missing property)
- Style paint references missing field names

### “The legend doesn’t match the map”
- Class breaks were computed on a different year/region than what is displayed
- The UI is using a continuous ramp while the map uses binned styling (or vice versa)

✅ **Rule:** Time-comparable layers should either:
- use **fixed breaks** across years (best for comparison), or
- clearly disclose that breaks are year-specific (best for within-year contrast)

### “Users are misreading the map”
- Totals choropleth problem
- No-data looks like zero
- Legend unit missing
- Too many layers are active by default

---

## 🔎 Recommended “Demographics layer” templates

### 🧾 Choropleth (normalized metric)
Use when:
- rate per 1,000 people
- density per sq mi
- percent of population

### 📍 Graduated symbol (totals)
Use when:
- total population
- total households
- raw counts

### 🧊 Time-snapshots
Use when:
- historical census years
- decennial comparisons
- discontinuous data

---

## 📚 Related docs (project-local)

- 📘 `src/server/api/README.md` — dataset, query, and tiles endpoints
- 🧱 `docs/standards/` — metadata profiles, governance expectations
- 🧭 `web/src/components/LayerControl` — layer toggling UI (if present)
- ⏳ `web/src/components/TimelineSlider` — time scrubber behavior (if present)

---

## 🧷 Glossary

- **DCAT**: Dataset catalog metadata standard (discovery + summary)
- **STAC**: Spatiotemporal Asset Catalog (assets + time/space indexing)
- **MVT / PBF**: Mapbox Vector Tiles format served as `.pbf`
- **CARE**: Collective benefit, Authority to control, Responsibility, Ethics (Indigenous data governance)
- **FAIR**: Findable, Accessible, Interoperable, Reusable (open data expectations)
- **No-data**: Not the same as zero; must be visually distinct