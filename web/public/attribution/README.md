# Attribution & Credits 🧾🗺️  
![Attribution Required](https://img.shields.io/badge/attribution-required-brightgreen) ![Provenance](https://img.shields.io/badge/provenance-PROV%20%7C%20STAC%20%7C%20DCAT-blue) ![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-purple) ![Default](https://img.shields.io/badge/default-fail--closed-red)

Welcome to **`web/public/attribution/`** — the public-facing “credits roll” for Kansas Frontier Matrix (KFM).  
This directory exists so every **map layer**, **chart**, **document snippet**, and **AI-assisted answer** can point back to a **real source + license** (“the map behind the map” 🧭).

> [!IMPORTANT]
> **If it shows up in the UI, it must be attributable.**  
> If it’s not attributable, it’s not publishable.

---

## Table of contents 🧭
- [What belongs in this folder](#what-belongs-in-this-folder-)
- [How attribution appears in the web app](#how-attribution-appears-in-the-web-app-)
- [Suggested folder layout](#suggested-folder-layout-)
- [Attribution “contract”](#attribution-contract-)
- [Attribution record templates](#attribution-record-templates-)
- [Adding / updating an attribution](#adding--updating-an-attribution-)
- [Sensitive data notes](#sensitive-data-notes-)
- [Initial source shortlist](#initial-source-shortlist-)
- [FAQ](#faq-)
- [References](#references-)

---

## What belongs in this folder 📦

### 1) Data sources 🛰️🌾
Anything that contributes **facts** or **geometry**:
- Vector layers (boundaries, roads, trails, parcels)
- Raster layers (imagery, elevation, hillshades, land cover)
- Time series & tables (climate, hydrology, census, agriculture)
- External APIs (stream gauges, catalog endpoints, etc.)

### 2) Basemaps & tiles 🧱🗺️
- Tile providers (XYZ/WMTS/PMTiles)
- Terrain/DEM providers
- Label datasets

> [!TIP]
> Basemap attribution often has **strict display rules** (logo placement, minimum font size, specific strings).  
> Capture the exact required string here so the UI can render it consistently.

### 3) Software & libraries ⚙️📚
- Open source packages used by the web app (and/or shared UI tooling)
- Map rendering libraries, visualization libraries, and UI frameworks
- Any third-party code copied into the repo (even small snippets)

### 4) Content assets 🎨🖼️
- Icons, fonts, photos, scanned maps, diagrams, screenshots used in the UI
- Storytelling content (if not authored 100% in-house)
- Embedded media (audio/video)

### 5) AI / Models / Derived outputs 🤖🧠
If the platform uses:
- A local or hosted model
- An embeddings model
- A classifier for remote sensing
- AI-assisted metadata generation

…then record:
- Model name + version
- Provider
- License
- Usage scope (what it does *and what it must not do*)
- Safety notes (if applicable)

---

## How attribution appears in the web app 🌐✨

This folder is designed to support **two kinds of attribution**:

1) **Human-readable** (for people)  
   - A clean, navigable attribution page (ex: `/attribution`)
   - Dataset “credits” on layer detail panels
   - Story footnotes / citations

2) **Machine-readable** (for systems)  
   - A single JSON file (or multiple chunked JSON files) the UI can load to render attribution dynamically
   - Optional per-dataset attribution fragments to keep merges conflict-free

> [!NOTE]
> The long-term goal is: **no hard-coded credits in UI components**.  
> The UI should render attribution from governed metadata.

---

## Suggested folder layout 🗂️

> This is a recommended structure — adjust to match the repo’s actual build system.

```text
📁 web/
  📁 public/
    📁 attribution/
      📄 README.md                      👈 you are here
      📄 attribution.index.json         (machine-readable index used by web UI)
      📄 NOTICE.md                      (optional: consolidated OSS notices)
      📁 data/                          (datasets + services)
        📄 ks_dasc_counties.md
        📄 usgs_nwis_streamgages.md
      📁 software/                      (OSS dependencies that require attribution)
        📄 maplibre.md
        📄 cesium.md
      📁 assets/                        (fonts/icons/images where license requires notice)
        📄 fonts.md
        📄 icons.md
      📁 models/                        (AI models / embeddings / classifiers)
        📄 llm_local_model.md
```

---

## Attribution “contract” 🤝✅

### Minimum bar (required) 🧾
Every attribution entry must have:

- **Title** (what is it?)
- **Publisher / Provider** (who made it?)
- **Source link** (where did it come from?)
- **License / terms** (what are we allowed to do?)
- **Attribution statement** (exact string required by provider, if any)
- **Date accessed** (or “last verified”)
- **Scope of use** (what part of KFM uses it?)

### Provenance linkage (strongly recommended) 🧬
If the dataset is part of KFM’s governed catalog, also include:

- **Catalog ID** (stable identifier)
- **STAC / DCAT references** (where applicable)
- **PROV reference** (how it was produced / transformed)
- **Processing notes** (human-readable summary of transformations)

> [!IMPORTANT]
> If a dataset has **no provenance metadata**, treat it as **not publishable**.

### “Fail-closed” rule 🔒
If **license**, **publisher**, or **classification** is missing, the pipeline/UI should treat the entry as **blocked** until fixed.

---

## Attribution record templates 🧩

### Dataset / API (Markdown) template 🛰️
Create a new file under `data/`:

```markdown
---
id: ks_dasc_example_layer
type: dataset
title: "Kansas Example Layer"
publisher: "Kansas Data Access and Support Center (DASC)"
source_url: "https://example.com/source"
license_name: "Public Domain / Terms Vary by Dataset"
license_url: "https://example.com/license"
required_attribution: "Source: Kansas DASC (accessed YYYY-MM-DD)"
date_accessed: "YYYY-MM-DD"
scope:
  - "Web basemap reference layer"
  - "Used in map overlays"
kfm:
  catalog_id: "ks_example_0001"
  stac: "stac/collections/ks_example.json"
  prov: "data/provenance/ks_example_0001.prov.json"
notes:
  - "Add any provider-specific display requirements."
  - "Describe transformations (clip, reproject, generalize, etc.)."
---
# Kansas Example Layer 🗺️
## Attribution ✅
**Required:** Source: Kansas DASC (accessed YYYY-MM-DD)

## License 📜
Summarize the license in plain language and link to the official terms.

## How KFM uses this 🧠
- What UI features depend on it?
- Is it cached, mirrored, or live-linked?

## Provenance 🧬
- Input(s)
- Processing steps
- Output(s)
- Known limitations / accuracy notes
```

### Open-source software template ⚙️
Create a new file under `software/`:

```markdown
---
id: maplibre_gl_js
type: software
name: "MapLibre GL JS"
homepage: "https://maplibre.org/"
license_name: "MIT"
license_url: "https://github.com/maplibre/maplibre-gl-js/blob/main/LICENSE.txt"
required_notice: "Include MIT license text in NOTICE.md (if required by distribution policy)"
scope:
  - "Web map rendering"
notes:
  - "Pin version in package manager lockfile."
---
# MapLibre GL JS 🗺️
## Why we use it
- Short summary

## License & Notice
- What must be displayed/retained?
```

### Fonts / icons / media template 🎨
Create a new file under `assets/`:

```markdown
---
id: icon_set_example
type: asset
name: "Example Icon Set"
source_url: "https://example.com/icons"
license_name: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
required_attribution: "Icons by Example Author (CC BY 4.0)"
scope:
  - "UI icons"
---
# Example Icon Set 🎨
## Required attribution ✅
Icons by Example Author (CC BY 4.0)

## Notes
- If modified, say what changed.
- If redistribution is restricted, document the rule.
```

---

## Adding / updating an attribution 🛠️

### Checklist ✅
- [ ] **Create or update** an attribution entry file (`data/`, `software/`, `assets/`, `models/`)
- [ ] Confirm **publisher** + **canonical source URL**
- [ ] Confirm **license name** + **license URL**
- [ ] Capture the **required attribution string** verbatim (if provided)
- [ ] Add **date accessed** (and optionally “last verified”)
- [ ] If applicable: link to **catalog ID / STAC / DCAT / PROV**
- [ ] If the source is **not redistributable**, document that clearly
- [ ] If changes were made (cleaning, clipping, generalizing), document them

### “Do not do this” ⛔
- Don’t paste copyrighted content “because it’s small”
- Don’t assume “government = public domain” (verify per dataset)
- Don’t ship a layer to the public UI without an attribution record

---

## Sensitive data notes 🧿

Some data may be sensitive even if it’s historically interesting or technically accessible:
- Precise cultural sites
- Locations of archeological resources
- Data that could identify individuals (directly or by inference)

Guidance:
- Prefer **aggregation** (county-level, tract-level, etc.)
- Consider **generalization** (coordinate rounding)
- Consider **suppression** (do not display small-n categories)
- Respect Indigenous data governance and labeling requirements

> [!IMPORTANT]
> Attribution ≠ permission.  
> Even with a source and license, sensitive data may need additional governance controls.

---

## Initial source shortlist 🗺️📚

This is a **starter list** of commonly-referenced sources in the KFM ecosystem.  
Treat it as **non-exhaustive** and **verify license terms per dataset**.

### Kansas / regional 🟦
- Kansas Data Access and Support Center (DASC) — foundational GIS layers  
- Kansas Geological Survey (KGS) — geology, water, maps, publications  
- Kansas Historical Society / Kansas Memory — digitized archives (photos, letters, maps)

### Federal / international 🌎
- USGS NWIS — hydrology and groundwater observations  
- NASA/USGS (Landsat) and ESA (Sentinel) — Earth observation imagery  
- NOAA archives — climate and weather records  
- Library of Congress (e.g., historical newspapers & collections)

### Land & treaties 🪶📜
- BLM General Land Office records — land patents and related land records  
- Indian Land Cessions / treaty-related spatial layers (verify terms + sensitivity handling)

---

## FAQ ❓

### Why not keep attribution only in the data catalog?
Because the web app needs a **public, human-readable** attribution surface — and some attributions apply to **UI assets** and **software**, not just datasets.

### Should we include full license text here?
Sometimes. If distribution policy requires it (common for OSS notices), put the full text into `NOTICE.md` and link to it from the specific entry.

### What about versioning?
If the repo includes `CITATION.cff`, treat attribution as **versioned**: cite the dataset/repo version used when publishing results.

---

## References 📚
- KFM governance & provenance docs (FAIR/CARE, provenance/audit trails, policy gates)
- KFM data catalog standards (STAC / DCAT / PROV)
- GIS metadata & copyright best practices