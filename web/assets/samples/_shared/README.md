<div align="center">

# ♻️ `_shared` — Shared Assets for Web Samples

**One place for sample styles, helpers, and tiny fixtures** so all demos look/behave consistently ✨

![Scope](https://img.shields.io/badge/scope-web%2Fassets%2Fsamples-blue)
![Intent](https://img.shields.io/badge/intent-demo%20%2B%20docs%20%2B%20fixtures-8a2be2)
![Guardrails](https://img.shields.io/badge/guardrails-provenance%E2%80%91first%20%7C%20contract%E2%80%91first-2ea44f)

</div>

---

## 🧭 What this folder is

This directory contains **shared** building blocks used by sample pages under:

```
web/
└─ 📁 assets/
   └─ 🧪 samples/
      ├─ ♻️ _shared/         # ← you are here 📌 Shared building blocks used by many samples (CSS/JS/data/licenses/schemas)
      ├─ 🧪 <sample-a>/      # Self-contained runnable sample A (index.html + app.js + README + local config)
      └─ 🧪 <sample-b>/      # Self-contained runnable sample B (index.html + app.js + README + local config)
```

Think of `_shared/` as the **sample kit**:
- 🎨 shared CSS (layout, spacing, typography, sample UI chrome)
- 🧠 shared JS/TS utilities (map bootstrap, URL state, layer toggles, timeline wiring)
- 🧩 tiny demo fixtures (small GeoJSON snippets, style presets, mock catalog responses)
- 🖼️ icons, placeholders, thumbnails for sample pages

> [!NOTE]
> The **main KFM UI** lives in `web/` and can include *precomputed JSON needed by the app* (e.g., document index / timeline configuration). Samples are allowed to reuse those patterns, but `_shared/` should remain **small**, **safe**, and **clearly “demo/fixture”** in nature. [oai_citation:0‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## ✅ What belongs here (and what does not)

### ✅ Belongs here
- **Reusable UI bits** for demos:
  - `sample-layout.css`, `panel.css`, `timeline.css`
- **Helper code** that *multiple* samples need:
  - `maplibre.bootstrap.ts`, `layerPanel.ts`, `timeline.ts`, `fetchJson.ts`
- **Tiny fixtures** that make samples work offline or in isolation:
  - small `*.geojson` (a handful of features)
  - minimal `*.json` config (layer list, timeline config, style presets)
- **Placeholder assets**
  - `logo.svg`, `pin.svg`, `thumbnail.png`

### ❌ Does *not* belong here
- 🚫 “Real” datasets or evidence artifacts (large rasters, full vectors, sensitive material)
- 🚫 Anything that should flow through **ETL → catalogs → API → UI**
- 🚫 Secrets, keys, tokens, credentials (ever)

> [!IMPORTANT]
> KFM’s governance model treats **evidence artifacts** as first-class datasets and disallows “sneaking” them into the UI via hard-coded files. Any artifact exposed in the UI must go through the governed API layer—**direct access / hard-coding is not allowed**. [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗂️ Suggested structure (convention, not law)

You may see variations, but this is the recommended layout:

```
web/assets/samples/_shared/
├── ♻️📄 README.md                 # this file
├── 🎨 css/
│   ├── 🎨📄 sample-base.css        # shared layout + resets for samples
│   ├── 🎨📄 sample-panels.css      # sidebar/panel styling
│   └── 🎨📄 sample-timeline.css    # timeline slider styling
├── 🧠 js/
│   ├── 🧠📄 map.bootstrap.js       # minimal “create map” helper
│   ├── 🧠📄 layer-panel.js         # toggle layers + opacity
│   ├── 🧠📄 timeline.js            # bind year/date → layer state
│   └── 🔗🧠📄 url-state.js         # sync UI ↔ query params
├── 🧩 data/
│   ├── 🧪 fixtures/                # tiny demo datasets (NOT authoritative)
│   ├── ⚙️ configs/                 # layer lists, demo timelines
│   └── 📐 schemas/                 # optional: sample JSON schema snippets
└── 🖼️ img/
    ├── 🧷 icons/
    └── 🧰 placeholders/
```

---

## 🧱 Design goals

Samples should:
- 🧩 be **copyable** (a sample folder can be duplicated and edited)
- ⚡ be **fast** (no huge assets, no heavy dependencies)
- 🧭 be **consistent** (same layout + interaction patterns)
- 🔎 demonstrate KFM principles: **provenance**, **metadata**, **temporal navigation**, and **“map behind the map”** transparency

KFM’s UI patterns often include a **timeline slider**, layer toggles, and contextual panels; samples should mirror those interaction ideas when relevant. [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🔌 How samples should reference `_shared`

Most samples live like:

```
web/assets/samples/<sample-name>/index.html
```

So references usually look like:

```html
<link rel="stylesheet" href="../_shared/css/sample-base.css" />
<script type="module" src="../_shared/js/map.bootstrap.js"></script>
```

> [!TIP]
> If your sample is nested deeper (e.g. `.../samples/foo/pages/bar.html`), adjust `../` accordingly.

---

## 🧠 Typical “shared helper” responsibilities

### 🗺️ Map bootstrap
Shared helpers should make it easy for samples to:
- initialize MapLibre / Leaflet quickly
- add a base layer
- register click/hover interactions
- wire up a layer panel

KFM’s web UI is map-centric and commonly uses open mapping libraries (e.g., MapLibre/Leaflet in design materials; MapLibre GL JS in the React SPA implementation). [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🕰️ Timeline wiring
Helpers can expose a tiny API like:

```js
setYear(1875)
setDate("1875-01-01")
getActiveLayers()
```

That aligns with KFM’s emphasis on temporal navigation via a timeline slider and time-aware layers. [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧩 Fixture data rules (very important)

Fixture data in `_shared/data/fixtures/` is allowed **only** for:
- demos
- unit-test-like sample pages
- UI prototyping
- screenshots/docs

### Fixture data MUST be:
- 📦 **small** (think KBs, not MBs)
- 🏷️ **clearly labeled** as *fixture/demo*
- 🧾 **licensed** (or self-created) with attribution notes
- 🔍 **non-sensitive** (no private parcel ownership data, no restricted Indigenous data, etc.)

### Fixture data MUST NOT:
- impersonate “official” KFM evidence
- bypass provenance, catalogs, or API rules

> [!IMPORTANT]
> KFM’s architecture is designed so the UI does **not** contain hidden data files and relies on governed APIs for access and enforcement. [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧾 Provenance & metadata expectations (even for demos)

KFM is **contract-first** and **provenance-first**:
- datasets are expected to have metadata contracts and traceable sources
- “mystery layers” are not allowed in the platform’s data model [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Even when you’re building a tiny sample, try to keep the spirit:
- include a `source.md` or `meta.json` next to fixtures when relevant
- link to the canonical standards when something graduates from “demo” to “real”

KFM’s standards emphasize STAC/DCAT/PROV alignment for datasets and derived artifacts, validated by CI in the project model. [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Adding a new shared asset: checklist

- [ ] Is this used by **2+ samples**? (If not, keep it inside the sample folder.)
- [ ] Is it **small** and **fast** to load?
- [ ] If it’s data: is it clearly labeled as **fixture/demo**?
- [ ] If it’s data: do we have **license/source notes**?
- [ ] Does it avoid bypassing KFM’s **API boundary** and provenance rules?
- [ ] Naming matches conventions (see below)

---

## 🏷️ Naming conventions

Keep names boring and searchable ✅

### Files
- `sample-*.css` for shared CSS
- `*.bootstrap.*` for setup helpers
- `timeline.*` for time navigation helpers
- `layer-panel.*` for layer toggles

### Data fixtures
Use a predictable shape:

```
<topic>__<type>__<version>.<ext>
```

Example:
- `railroads__lines__v1.geojson`
- `treaties__sites__v1.geojson`
- `timeline__kansas__v1.json`

---

## 🧰 Mini recipe: a “canonical” sample page

<details>
<summary><strong>📄 Click to expand example</strong></summary>

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>KFM Sample — Timeline + Layers</title>

    <link rel="stylesheet" href="../_shared/css/sample-base.css" />
    <link rel="stylesheet" href="../_shared/css/sample-panels.css" />
    <link rel="stylesheet" href="../_shared/css/sample-timeline.css" />
  </head>

  <body>
    <main class="sample-layout">
      <aside class="sample-panel">
        <h1>🧪 Sample</h1>
        <div id="layer-panel"></div>
        <div id="timeline"></div>
      </aside>

      <section class="sample-map">
        <div id="map"></div>
      </section>
    </main>

    <script type="module">
      import { createMap } from "../_shared/js/map.bootstrap.js";
      import { mountLayerPanel } from "../_shared/js/layer-panel.js";
      import { mountTimeline } from "../_shared/js/timeline.js";

      const map = await createMap({ container: "map" });

      mountLayerPanel(map, document.getElementById("layer-panel"));
      mountTimeline(map, document.getElementById("timeline"));
    </script>
  </body>
</html>
```

</details>

---

## 🧠 Relationship to the main KFM pipeline (why we’re strict)

KFM’s “non-negotiable ordering” is:

**ETL → catalogs (STAC/DCAT/PROV) → graph → API → UI → Story Nodes → Focus Mode** [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

This `_shared/` folder lives firmly on the **UI side** of that boundary.

So: use `_shared/` for **presentation**, **interaction**, and **tiny fixtures** — not for sneaking around governance.

---

## 🔎 Rationale sources (project docs)

- `web/` contains the frontend and may include precomputed JSON needed by the app (e.g., document index / timeline config). [oai_citation:12‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- KFM emphasizes provenance visibility (“map behind the map”) in the UI so users can see layer source/metadata. [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM is contract-first & provenance-first; datasets are expected to carry metadata contracts and not be “mystery layers.” [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- UI must not bypass governed APIs or hard-code exposed artifacts directly into the client. [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
