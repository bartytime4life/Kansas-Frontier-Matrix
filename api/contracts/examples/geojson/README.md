# 🌍 GeoJSON Examples — KFM API Contracts

![GeoJSON](https://img.shields.io/badge/format-GeoJSON-2ea44f?logo=geojson&logoColor=white)
![Contract-First](https://img.shields.io/badge/principle-Contract--First-2563eb)
![Provenance-First](https://img.shields.io/badge/principle-Provenance--First-ec4899)
![Policy-Gated](https://img.shields.io/badge/security-Policy--Gated-f59e0b)
![Map UI Ready](https://img.shields.io/badge/ui-MapLibre%20%2B%20Cesium-111827)

> [!NOTE]
> According to a document from **January 24, 2026**, KFM is API-driven (REST + GraphQL), and every map visualization must stay *traceable to its sources* — “the map behind the map.” ✅  
> This folder makes that promise testable by providing **canonical GeoJSON payload examples** that match KFM’s response contracts.

---

## 📁 Where you are

```text
📁 api/
  📁 contracts/
    📁 examples/
      📁 geojson/
        📄 README.md   👈 you are here
        📄 *.json      (example GeoJSON payloads used for tests + docs)
```

---

## 🎯 Purpose of this folder

This directory is the **GeoJSON “examples pack”** for KFM’s **contract-first** API philosophy:

- ✅ Examples are used by **contract tests** (CI) and **developer docs**
- ✅ Examples illustrate how KFM layers are served to:
  - 🗺️ 2D map viewers (MapLibre)
  - 🌐 3D / AR-capable clients (Cesium / mobile “AR mode”)
  - 🤖 Focus Mode (AI assistant) — where map results must still include citations + provenance

> [!TIP]
> Treat every example in this folder as **production-shaped** payloads — even when the geometry/attributes are synthetic.

---

## 🧭 Why GeoJSON in KFM?

KFM uses GeoJSON as a **primary interchange format** for:
- Smaller/interactive vector layers & query results (good DX + easy client rendering)
- Exports / downloads and interoperability
- “Just-in-time” overlays (drawn AOIs, highlight features, story step callouts)

For performance at scale, KFM may serve **vector tiles** (MVT) or packaged artifacts (e.g., PMTiles) — but GeoJSON remains the go-to for:
- 🧪 contract examples
- 🔎 feature-level inspection
- 🧩 UI selection/highlight flows
- 🗂️ evidence/provenance traceability at the individual feature level

---

## ✅ KFM GeoJSON Profile

This section defines the **KFM GeoJSON Profile** used for API responses and examples in this folder.

### 1) Base GeoJSON rules (compatibility first) 🧱

All examples MUST:

- Use **`Feature`** or **`FeatureCollection`**
- Include `geometry` and `properties` for each feature
- Use `[longitude, latitude]` coordinate order
- Use WGS84 / web-friendly coordinates (no client-side CRS guessing)

> [!WARNING]
> Do **not** include precise geometry for sensitive layers unless it is explicitly a “restricted/private” example and demonstrates redaction (see “🔐 Redaction & sensitivity”).

---

### 2) KFM metadata requirements (provenance-first) 🧬

KFM extends GeoJSON using an opinionated metadata object at:

- `properties.kfm` (for Feature)
- optional `kfm` at FeatureCollection root (collection-level metadata)

#### ✅ Required fields for Feature examples

| Path | Type | Why it exists |
|---|---:|---|
| `properties.kfm.dataset_id` | `string` | Stable dataset identifier (catalog + graph linkage) |
| `properties.kfm.layer_id` | `string` | Map/UI layer identifier (“what the user toggled on”) |
| `properties.kfm.classification` | `string` | Data policy + access control (“public”, “restricted”, etc.) |
| `properties.kfm.provenance` | `object` | Links to STAC/DCAT/PROV backbone |
| `properties.kfm.attribution` | `object` | Source + license surfaced in UI & exports |
| `properties.kfm.links` | `array` | API/catalog pointers (self/about/download/etc.) |

> [!NOTE]
> KFM’s guiding rule: **if the UI can render it, the user can trace it**.  
> That’s why the contract expects explicit provenance + attribution in the payload.

---

### 3) Provenance triplet (STAC + DCAT + PROV) 🔗

KFM treats these as “load-bearing” provenance references:

- **STAC** → geospatial assets/items/collections
- **DCAT** → dataset metadata + distributions + access URLs
- **PROV** → lineage and transformations (“how it was made”)

Your GeoJSON payload should include pointers, e.g.:

- `properties.kfm.provenance.stac.collection`
- `properties.kfm.provenance.stac.item`
- `properties.kfm.provenance.dcat.dataset`
- `properties.kfm.provenance.dcat.distribution`
- `properties.kfm.provenance.prov.bundle`

> [!TIP]
> If you don’t have all three yet, **stub them** consistently in examples to keep the contract shape stable — then tighten gates later.

---

## ⏱️ Time & timeline compatibility

KFM treats time as a **first-class filter**: API + UI support time-range querying (ISO-8601).  
GeoJSON examples should demonstrate that by including at least one of:

- `properties.datetime` (instant)
- `properties.start_datetime` + `properties.end_datetime` (range)
- `properties.kfm.time` / `properties.kfm.time_range` (domain-specific)

Recommended formats:

- `YYYY-MM-DD`
- `YYYY-MM-DDTHH:MM:SSZ`
- Ranges as `start/end` (when used in query params)

---

## 🔐 Redaction & sensitivity

GeoJSON is powerful — and dangerous if it exposes protected locations.

KFM supports **tiered access + sensitivity-aware handling**. Your examples should show at least one pattern:

### Redaction patterns (choose one)

1) **Omit** restricted features entirely  
2) **Generalize** geometry (rounding, coarse cell, buffered polygon)  
3) **Mask** attributes (remove identifiers, truncate text fields)  
4) **Role-based** variants of the same endpoint

Recommended structure:

```json
{
  "kfm": {
    "classification": "restricted",
    "redaction": {
      "kind": "geometry_generalized",
      "precision_meters": 10000,
      "reason": "Sensitive site policy"
    }
  }
}
```

> [!WARNING]
> Never put real sacred sites / endangered locations / private addresses into contract examples.  
> Use synthetic coordinates and fake identifiers.

---

## 🧩 Common API patterns that yield GeoJSON

KFM’s API provides REST endpoints that return data **as GeoJSON** or return **links** to tiles.

### “Table query” pattern (simple + powerful)

A documented pattern uses a query endpoint like:

- `GET /api/v1/query?table=geo_counties`

Examples in this folder can model responses from that style of endpoint.

### “Dataset by ID” pattern

Examples may also model:

- `GET /api/datasets/{id}` returning either:
  - `FeatureCollection` (inline)
  - or a catalog-like JSON with GeoJSON/tile links

### “OGC-style” (future-compatible)

KFM can align with OGC API - Features semantics, e.g.:

- `/collections/{collectionId}/items` → GeoJSON FeatureCollection

> [!TIP]
> Even if the route structure evolves, the **payload contract** should stay stable — that’s why examples live in `api/contracts/`.

---

## 📦 Examples inventory (recommended filenames)

If you’re building out this folder, aim for a tight, useful set of examples:

| File | What it demonstrates | Emoji |
|---|---|---|
| `feature__point__realtime_sensor.public.json` | real-time point + attribution/provenance | 📍 |
| `feature__polygon__county_boundary.public.json` | polygons + stable IDs + bbox | 🧱 |
| `featurecollection__bbox_query__public.json` | bbox filter + pagination links | 🧭 |
| `featurecollection__time_filtered__public.json` | timeline-ready payload | ⏱️ |
| `feature__point__restricted_redacted.json` | redaction + classification | 🔐 |
| `featurecollection__mixed_geometry__debug.json` | QA/testing mixed geometries | 🧪 |

> [!NOTE]
> The names are suggestions — consistency matters more than perfection.  
> If you already have a naming standard elsewhere in `api/contracts/examples/`, match it.

---

## 🧾 Canonical payload examples

### ✅ Example 1: Feature (Point) with KFM metadata 📍

<details>
<summary><strong>Click to expand JSON</strong></summary>

```json
{
  "type": "Feature",
  "id": "kfm.feature:sensor.station_0001",
  "geometry": {
    "type": "Point",
    "coordinates": [-97.3301, 37.6872]
  },
  "properties": {
    "station_name": "Example River Gauge (Synthetic)",
    "value": 12.34,
    "units": "ft",
    "datetime": "2026-01-24T18:30:00Z",
    "kfm": {
      "dataset_id": "kfm.ks.hydro.river_gauges.v1",
      "layer_id": "realtime_river_gauges",
      "classification": "public",
      "provenance": {
        "stac": {
          "collection": "stac/collections/kfm.ks.hydro.river_gauges.v1.json",
          "item": "stac/items/kfm.ks.hydro.river_gauges.v1/station_0001.json"
        },
        "dcat": {
          "dataset": "dcat/datasets/kfm.ks.hydro.river_gauges.v1.json",
          "distribution": "dcat/distributions/kfm.ks.hydro.river_gauges.v1.geojson.json"
        },
        "prov": {
          "bundle": "prov/bundles/river_gauges_ingest_2026-01-24.json"
        }
      },
      "attribution": {
        "source": "Synthetic example (contract test)",
        "license": "N/A (example payload)"
      },
      "links": [
        {
          "rel": "self",
          "href": "/api/v1/query?table=realtime_river_gauges&where=station_id%3D%270001%27&format=geojson",
          "type": "application/geo+json"
        },
        {
          "rel": "about",
          "href": "/catalog/datasets/kfm.ks.hydro.river_gauges.v1"
        }
      ]
    }
  }
}
```

</details>

---

### ✅ Example 2: FeatureCollection (bbox + pagination + collection metadata) 🧭

<details>
<summary><strong>Click to expand JSON</strong></summary>

```json
{
  "type": "FeatureCollection",
  "bbox": [-102.05, 36.99, -94.60, 40.00],
  "features": [
    {
      "type": "Feature",
      "id": "kfm.feature:county.02045",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-99.00, 38.80],
            [-98.50, 38.80],
            [-98.50, 38.50],
            [-99.00, 38.50],
            [-99.00, 38.80]
          ]
        ]
      },
      "properties": {
        "name": "Example County (Synthetic)",
        "fips": "02045",
        "kfm": {
          "dataset_id": "kfm.ks.boundaries.counties.v1",
          "layer_id": "geo_counties",
          "classification": "public",
          "provenance": {
            "stac": { "collection": "stac/collections/kfm.ks.boundaries.counties.v1.json" },
            "dcat": { "dataset": "dcat/datasets/kfm.ks.boundaries.counties.v1.json" },
            "prov": { "bundle": "prov/bundles/counties_ingest_2026-01-24.json" }
          },
          "attribution": { "source": "Synthetic example (contract test)", "license": "N/A" },
          "links": [
            { "rel": "about", "href": "/catalog/datasets/kfm.ks.boundaries.counties.v1" }
          ]
        }
      }
    }
  ],
  "links": [
    {
      "rel": "self",
      "href": "/api/v1/query?table=geo_counties&bbox=-102.05,36.99,-94.60,40.00&limit=1&format=geojson",
      "type": "application/geo+json"
    },
    {
      "rel": "next",
      "href": "/api/v1/query?table=geo_counties&bbox=-102.05,36.99,-94.60,40.00&limit=1&cursor=eyJvZmZzZXQiOjF9&format=geojson",
      "type": "application/geo+json"
    }
  ],
  "kfm": {
    "layer_id": "geo_counties",
    "time_filter": null,
    "contract_version": "geojson-profile-v1"
  }
}
```

</details>

---

### ✅ Example 3: Restricted feature with generalized geometry 🔐

<details>
<summary><strong>Click to expand JSON</strong></summary>

```json
{
  "type": "Feature",
  "id": "kfm.feature:sensitive.site_0007",
  "geometry": {
    "type": "Point",
    "coordinates": [-98.00, 38.00]
  },
  "properties": {
    "label": "Sensitive location (example)",
    "kfm": {
      "dataset_id": "kfm.ks.sites.sensitive.v1",
      "layer_id": "sensitive_sites",
      "classification": "restricted",
      "redaction": {
        "kind": "geometry_generalized",
        "precision_meters": 10000,
        "reason": "Ethical access control / cultural protocol"
      },
      "provenance": {
        "dcat": { "dataset": "dcat/datasets/kfm.ks.sites.sensitive.v1.json" },
        "prov": { "bundle": "prov/bundles/sensitive_sites_ingest_2026-01-24.json" }
      },
      "attribution": {
        "source": "Withheld (restricted)",
        "license": "Restricted"
      },
      "links": [
        { "rel": "about", "href": "/catalog/datasets/kfm.ks.sites.sensitive.v1" }
      ]
    }
  }
}
```

</details>

---

## 🗺️ Consumer snippet (MapLibre) — rendering a GeoJSON layer

```js
// Minimal MapLibre example: add GeoJSON as a source + layer
map.addSource("kfm-layer", {
  type: "geojson",
  data: "/api/v1/query?table=geo_counties&bbox=-102.05,36.99,-94.60,40.00&format=geojson"
});

map.addLayer({
  id: "kfm-layer-fill",
  type: "fill",
  source: "kfm-layer",
  paint: {
    "fill-opacity": 0.35
  }
});
```

> [!TIP]
> Your UI popups can read `feature.properties.kfm.attribution` and `feature.properties.kfm.provenance` to show citations + “map behind the map”.

---

## 🧪 Validation & contract testing

Examples in this folder should be validated in CI (contract-first):

### Suggested validation pipeline

- ✅ JSON parses
- ✅ GeoJSON shape is correct (`Feature` / `FeatureCollection`)
- ✅ Required KFM fields exist (`properties.kfm.*`)
- ✅ Optional: geometry validity checks (no self-intersections, etc.)
- ✅ Optional: policy checks (license present, sensitivity honored)

### Add-a-new-example checklist ✅

- [ ] The payload uses `Feature` / `FeatureCollection`
- [ ] Every feature includes `properties.kfm.dataset_id`
- [ ] Every feature includes `properties.kfm.layer_id`
- [ ] Every feature includes `properties.kfm.classification`
- [ ] Every feature includes `properties.kfm.provenance` pointers (STAC/DCAT/PROV)
- [ ] Attribution is present (`properties.kfm.attribution.source`, `license`)
- [ ] Sensitive example uses explicit redaction (`properties.kfm.redaction`)
- [ ] Any time-aware example includes ISO-8601 fields (`datetime` or range)
- [ ] Add/update the “Examples inventory” table above

---

## 🚀 Performance note (when NOT to use GeoJSON)

GeoJSON is great… until it isn’t.

Prefer **vector tiles (MVT)** / **PMTiles** / **static artifacts** when:
- the layer is huge (roads, parcels, dense sensors)
- you need smooth pan/zoom performance
- you want caching/CDN delivery

GeoJSON examples still matter because:
- they define the feature-level semantics & metadata shape
- they document how the UI reads provenance + attribution
- they are perfect for “inspect this feature” workflows

---

## 📚 Related KFM design docs (project sources)

If you’re extending GeoJSON contracts, these docs explain the “why” behind the rules:

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** — API layout, REST/GraphQL, GeoJSON + tiles
- 🧭 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design** — timeline/time filters, MapLibre + Cesium
- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview** — provenance in UI, story nodes, AR/offline packs
- 📥 **Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide** — STAC/DCAT/PROV backbone + API boundary rule
- 🌟 **Kansas Frontier Matrix – Latest Ideas & Future Proposals** — PMTiles/GeoParquet tiling + scalable delivery
- 💡 **Innovative Concepts to Evolve KFM** — cultural protocols + sensitivity-aware geo-obfuscation + AR ideas
- 🧱 **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design** — MapLibre/Leaflet, GeoJSON layers, time slider
- 🧰 **Additional Project Ideas** — policy gates, schema drift checks, reproducible data ops patterns
- 📚 **AI Concepts & more** *(PDF portfolio)* — open in Acrobat for bundled references
- 🗃️ **Data Management…** *(PDF portfolio)* — open in Acrobat for bundled references
- 🧑‍💻 **Various programming languages & resources** *(PDF portfolio)* — open in Acrobat for bundled references
- 🗺️ **Maps / GoogleMaps / VirtualWorlds / WebGL…** *(PDF portfolio)* — open in Acrobat for bundled references

---

## 🧷 “Golden rules” (keep this short & strict)

1) ✅ **No provenance → not shippable**
2) ✅ **No attribution → not renderable**
3) ✅ **Sensitive data → must be redacted or omitted**
4) ✅ **Timeline layers → must include time fields**
5) ✅ **Examples → must stay deterministic + stable** (contracts depend on it)

---

<p align="center">
  <sub>🧠 Contract-first • 🧬 Provenance-first • 🗺️ Map-first • 🔐 Policy-gated</sub>
</p>
