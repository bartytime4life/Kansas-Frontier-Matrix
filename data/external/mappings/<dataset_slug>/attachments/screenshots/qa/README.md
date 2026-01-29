# 🧪 QA Screenshots — `<dataset_slug>` 📸

<p align="center">
  <img alt="QA Status" src="https://img.shields.io/badge/QA-pending-lightgrey">
  <img alt="Evidence" src="https://img.shields.io/badge/evidence-screenshots-blue">
  <img alt="Metadata" src="https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1">
  <img alt="Domain" src="https://img.shields.io/badge/domain-external-2ea44f">
</p>

> 🎯 **Purpose:** This folder stores **visual QA evidence** that the dataset mapping is *correct*, *reviewable*, and *safe to publish* (including metadata + provenance checks).  
> 🧷 Treat screenshots like “receipts” for review: each image should map to a specific check ✅

---

## 📍 You are here

```text
📦 data/
└── 🌐 external/
    └── 🗺️ mappings/
        └── 📁 <dataset_slug>/
            └── 📎 attachments/
                └── 📸 screenshots/
                    └── 🧪 qa/   👈 (this folder)
                        └── README.md
```

## 🔗 Quick links

- 📦 **Dataset mapping root:** `data/external/mappings/<dataset_slug>/` → [../../..](../../..)
- 📎 **Attachments root:** [../..](../..)
- 🌐 **External domain root:** [../../../../../README.md](../../../../../README.md)
- 📚 **KFM Master Guide (standards & governance):** [../../../../../../../docs/MASTER_GUIDE_v13.md](../../../../../../../docs/MASTER_GUIDE_v13.md)
- 🧾 **Standards (STAC/DCAT/PROV profiles):** [../../../../../../../docs/standards/](../../../../../../../docs/standards/)

---

## ✅ What belongs in `qa/`

Include screenshots that **prove** (not just “show”) one of these:

- 🧭 **Spatial sanity checks**
  - Extent is correct (bbox/footprint)
  - Alignment with basemap / known reference layers
  - Projection/CRS is what we claim
- 🧾 **Schema + attribute checks**
  - Field names/types match mapping
  - Null/missing values are understood
  - Category/value domains match docs
- 🧩 **Metadata + provenance checks**
  - STAC collection/item exists & validates
  - DCAT record exists (and matches dataset identity)
  - PROV chain is present (source → transform → publish)
- 🖥️ **UI / integration checks**
  - Dataset renders in the app/map UI
  - Legend + styling (if applicable) matches mapping docs

> 🔎 **Rule of thumb:** If a reviewer asks “how do we know?”, you should be able to point to a screenshot here (and/or a log elsewhere) that answers it.

---

## 🚫 What does **NOT** belong here

- ❌ Raw data exports (put those in `data/<domain>/raw/` or `work/`, not screenshots)
- ❌ Large binary dumps, full videos, or proprietary assets
- ❌ Sensitive material (PII, credentials, private tabs, personal bookmarks, etc.)

> 🔐 If you must show a sensitive UI for QA (rare): **redact/blur** before committing, or store securely outside repo and link in a restricted review channel.

---

## 📸 Minimal QA screenshot set

Use this as the “minimum viable evidence pack” (expand as needed):

- **QA-01** Source identity + timestamp (download page / catalog entry / archive item)
- **QA-02** CRS/projection evidence (layer properties showing EPSG / WKT)
- **QA-03** Spatial overlay (dataset layer over basemap/reference)
- **QA-04** Attribute/schema view (fields + sample rows or summary stats)
- **QA-05** STAC validation proof (item/collection view + validator output)
- **QA-06** DCAT proof (record view / JSON-LD snippet / registry page)
- **QA-07** PROV proof (activity/entity chain: source → transform → published artifact)
- **QA-08** UI render proof (frontend map/list view showing dataset correctly)

> 🧠 Not every dataset needs every screenshot type (e.g., no “UI render” if not published to UI yet), but you should **explicitly mark N/A** in the index below.

---

## 🏷️ File naming convention

**Goal:** predictable, sortable, greppable.

✅ Recommended:

```text
YYYY-MM-DD__<dataset_slug>__QA-<NN>__<topic>__v<rev>.png
```

Examples:

```text
2026-01-29__ks-county-boundaries__QA-03__overlay_alignment__v1.png
2026-01-29__ks-county-boundaries__QA-05__stac_validation__v2.png
```

Rules:

- Use `png` by default (crisp UI/text). Use `jpg` only when a photo-like image is huge.
- Keep names **lowercase** with `_` separators.
- Bump `v<rev>` when updating evidence (don’t overwrite unless necessary).

---

## 🧰 Capture settings (recommended)

- 🖥️ **Resolution:** 1920×1080 or higher  
- 🔍 **UI scale:** 100–125% (avoid tiny text)  
- 🧭 **Map screenshots:** include **scale bar** / **coordinates** if visible, and keep a recognizable reference (major cities/roads/river) in frame  
- 🧾 **Metadata screenshots:** include the **ID** in-frame (STAC Item ID, dataset slug, record URI, etc.)  
- 🧹 **Compression:** keep PRs friendly (consider `pngquant`/`oxipng` if you’re adding lots of PNGs)

---

## 🗂️ Screenshot index (fill this in)

> ✅ Add a row **per screenshot** you commit.  
> 📌 Keep this index updated so reviewers don’t have to guess what “image_12.png” means.

| QA ID | Screenshot | What it proves | Status | Notes |
|------:|------------|----------------|:------:|------|
| QA-01 | `YYYY-MM-DD__<dataset_slug>__QA-01__source_identity__v1.png` | Source page + dataset identity/date | ⬜ | |
| QA-02 | `YYYY-MM-DD__<dataset_slug>__QA-02__crs_properties__v1.png` | CRS/EPSG/WKT evidence | ⬜ | |
| QA-03 | `YYYY-MM-DD__<dataset_slug>__QA-03__overlay_alignment__v1.png` | Spatial alignment/extent | ⬜ | |
| QA-04 | `YYYY-MM-DD__<dataset_slug>__QA-04__schema_attributes__v1.png` | Fields/types/sample values | ⬜ | |
| QA-05 | `YYYY-MM-DD__<dataset_slug>__QA-05__stac_validation__v1.png` | STAC exists + validates | ⬜ | |
| QA-06 | `YYYY-MM-DD__<dataset_slug>__QA-06__dcat_record__v1.png` | DCAT exists + matches identity | ⬜ | |
| QA-07 | `YYYY-MM-DD__<dataset_slug>__QA-07__prov_chain__v1.png` | Provenance chain continuity | ⬜ | |
| QA-08 | `YYYY-MM-DD__<dataset_slug>__QA-08__ui_render__v1.png` | App/UI shows dataset correctly | ⬜/N/A | |

Legend (Status):
- ⬜ pending
- ✅ verified
- ⚠️ needs follow-up
- 🚫 blocked
- N/A not applicable

---

## 🧾 QA checklist (reviewer-friendly)

<details>
<summary><strong>🧭 Spatial QA</strong> (extent, CRS, alignment)</summary>

- [ ] Dataset extent (bbox/footprint) matches expected coverage
- [ ] Layer CRS is correct and documented (EPSG/WKT captured)
- [ ] Overlay alignment looks correct vs basemap/reference layers
- [ ] Geometry validity checked (self-intersections, empty geometries, etc.)
- [ ] If raster: nodata mask behaves as expected; pixel size/resolution matches docs
- [ ] If tiles/COGs: overviews present; no obvious resampling artifacts

</details>

<details>
<summary><strong>🧾 Schema & attributes QA</strong> (fields, values, nulls)</summary>

- [ ] Field names/types match mapping documentation
- [ ] Key fields have sane distributions (min/max/categories)
- [ ] Null values are expected (or explicitly explained)
- [ ] Units are correct (and labeled where relevant)
- [ ] If joins/lookups were used: cardinality is correct; no row explosion

</details>

<details>
<summary><strong>🧩 Metadata QA</strong> (STAC / DCAT / PROV)</summary>

- [ ] STAC collection/item exists and is valid (validator proof captured)
- [ ] STAC assets point to the correct artifacts (paths/URLs correct)
- [ ] DCAT record exists and matches dataset identity (title, publisher, temporal/spatial coverage)
- [ ] PROV chain exists: source → processing → published artifact
- [ ] IDs are consistent across STAC/DCAT/PROV (same dataset slug / identifiers)
- [ ] License is clearly documented and consistent across metadata

</details>

<details>
<summary><strong>🖥️ UI / integration QA</strong> (if published to app)</summary>

- [ ] Dataset appears in UI list/search
- [ ] Map layer renders without errors
- [ ] Styling/legend is correct (if applicable)
- [ ] Interaction works (hover/click/filters/time slider, as relevant)
- [ ] Performance is acceptable (no obvious slow tiles/blank areas)

</details>

<details>
<summary><strong>🗺️ Map artifact QA</strong> (scanned/historical/foreign maps — if applicable)</summary>

If you’re using scanned maps or third-party cartography as a primary source, capture marginal/context evidence:

- [ ] Map date(s) captured (survey/compilation preferred; note revisions)
- [ ] Publisher type noted (military/government/civilian)
- [ ] Map composition quality assessed (symbols/labels placement; clarity)
- [ ] Color/legend interpretation captured (legend screenshot or annotated notes)
- [ ] Any projection/grid quirks documented

</details>

<details>
<summary><strong>🔒 Governance & safety QA</strong></summary>

- [ ] No credentials/PII appear in screenshots
- [ ] Sensitive locations (if any) handled per governance policy (redaction/generalization)
- [ ] Licensing/copyright constraints respected (especially for scanned maps)
- [ ] Any access restrictions documented (what can/can’t be redistributed)

</details>

---

## 🧬 Evidence flow (how this folder fits the bigger system)

```mermaid
flowchart LR
  A[External Source 📎] --> B[Raw 📥]
  B --> C[Work / Transforms 🧪]
  C --> D[Processed ✅]
  D --> E[Metadata 🧾 STAC/DCAT/PROV]
  E --> F[Graph + UI 🌐]
  F --> G[QA Evidence 📸 (this folder)]
```

> 🧩 The goal is an **evidence-backed chain**: every published dataset should be traceable from UI → metadata → processed artifacts → source.

---

## ✅ Definition of Done (DoD)

This folder is “done” when:

- ✅ Screenshot index is filled out and matches committed files
- ✅ Minimum QA pack is complete **or** N/A is explicitly justified
- ✅ QA checklist items are checked off (or flagged ⚠️ with a follow-up issue)
- ✅ PR description links directly to the key screenshots (QA-03/05/07/08 are usually the fastest review)

---

## 📝 PR linking template (copy/paste)

```text
QA Evidence: data/external/mappings/<dataset_slug>/attachments/screenshots/qa/

Key screenshots:
- QA-03 overlay: <link to file>
- QA-05 STAC validation: <link to file>
- QA-07 PROV chain: <link to file>
- QA-08 UI render: <link to file>
```

---

## 📚 See also (project standards)

- 📘 KFM Master Guide: [../../../../../../../docs/MASTER_GUIDE_v13.md](../../../../../../../docs/MASTER_GUIDE_v13.md)
- 🧱 Standards folder: [../../../../../../../docs/standards/](../../../../../../../docs/standards/)
- 📦 External domain overview: [../../../../../README.md](../../../../../README.md)

---

### 🧠 Notes for future automation (optional)

If/when we automate QA evidence, this folder is a great target for:

- Auto-generating a `qa_index.md` from filenames
- Auto-validating required QA IDs exist for “publish-ready” datasets
- Rendering a “QA gallery” page in docs/site build

<!-- end -->
