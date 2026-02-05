# 🧾 Licenses & Attributions (Web Assets)

![Attributions Required](https://img.shields.io/badge/attributions-required-blue)
![No Unknown Licenses](https://img.shields.io/badge/unknown%20licenses-NO-red)
![SPDX Friendly](https://img.shields.io/badge/SPDX-friendly-brightgreen)

> [!IMPORTANT]
> **If an asset doesn’t have a license trail, it doesn’t ship.** 🚫  
> This folder is our “paper trail” for everything the web client shows or bundles that comes from elsewhere.

---

## 📍 Where am I?

You’re reading:

```text
web/src/assets/attributions/licenses/README.md
```

This folder is the **single source of truth** for:
- ✅ **License texts** (MIT/Apache/CC/etc)
- ✅ **NOTICE / attribution text** required by licenses or providers
- ✅ **Source/provenance** (where we got it, what it is, how we’re allowed to use it)

---

## 🎯 Why this exists (Kansas Frontier Matrix context)

Kansas Frontier Matrix (KFM) aggregates and visualizes many external **geospatial layers** and **open datasets** (state portals, federal sources, community archives). Many are *public domain* or require *simple attribution*, and some sources impose **strict restrictions** (e.g., Google Earth imagery).  

This directory ensures the web UI can:
- show required attribution in-app 🧭
- keep license texts close to shipped assets 📦
- pass audits / due diligence ✅

---

## ✅ Golden rules

- [ ] **No “mystery assets.”** If we can’t identify source + license → don’t commit it.
- [ ] **Keep original license texts verbatim.** Don’t “summarize” a license into a few bullets.
- [ ] **Attribution must be visible in the UI** if required (maps, baselayers, charts, images, datasets).
- [ ] **If redistribution is forbidden**, don’t commit the asset—store only attribution + a pointer.
- [ ] **Per-dataset licenses win.** If a source portal hosts mixed licenses, each dataset is handled individually.

> [!NOTE]
> This README is **process + structure**. The **actual license texts** live in sibling folders.

---

## 📂 Recommended folder layout 🗂️

```text
web/src/assets/attributions/
  licenses/
    README.md
    manifest.json               # optional: machine-readable index for UI
    _templates/
      NOTICE.template.md
      SOURCE.template.md
    <thing>/
      LICENSE.txt               # full legal text (if applicable)
      NOTICE.md                 # attribution text we must display
      SOURCE.md                 # what it is, where we got it, scope of use
      CHANGES.md                # optional: if we modified it (helps CC licenses)
```

### 🧩 Naming conventions
Prefer one of these:
- `npm--<package-name>/` (example: `npm--leaflet/`)
- `data--<provider>--<dataset>/`
- `media--<vendor>--<asset-name>/`
- `font--<family>/`

---

## 🧷 Optional: `manifest.json` (so the UI can render attributions)

If you want the app to display a consolidated **Attribution Drawer** or **Map Attribution Bar**, keep a small manifest here.

<details>
<summary><strong>Example manifest.json</strong> (click to expand)</summary>

```json
{
  "generatedBy": "humans (for now)",
  "items": [
    {
      "id": "data--dasc--kansas-gis",
      "type": "data",
      "name": "Kansas Data Access and Support Center (DASC)",
      "license": "Varies (often public domain / simple attribution)",
      "attribution": "Source: Kansas DASC (see dataset metadata for license notes).",
      "links": ["https://www.kansasgis.org/"],
      "whereShown": ["Map", "Dataset detail pages"]
    },
    {
      "id": "map--openstreetmap",
      "type": "map",
      "name": "OpenStreetMap",
      "license": "Provider-specific (verify tile provider terms)",
      "attribution": "© OpenStreetMap",
      "links": ["https://www.openstreetmap.org/copyright"],
      "whereShown": ["Map"]
    }
  ]
}
```
</details>

---

## 🗺️ Map + data source attribution defaults (KFM-aligned)

Even when data is public domain, we still **credit the source** (good practice, and often required by providers/portals).

### 🧭 Suggested “Attribution Bar” behavior
- Always visible on map views (small, non-intrusive)
- Click opens a drawer listing:
  - source name
  - license (or “varies, see dataset metadata”)
  - link to source portal / dataset page
  - change notes (if we modified derived products)

---

## 📚 Known sources & constraints (starter inventory)

> [!TIP]
> Treat this as a **starter list**. Add/adjust entries as you confirm what the web client is actually shipping/showing.

| Category | Source / Thing | License posture (summary) | Minimum UI credit |
|---|---|---|---|
| 🗺️ State GIS | Kansas DASC (state GIS hub) | Often public domain or simple attribution; per-dataset notes apply | “Source: Kansas DASC” (+ dataset link when possible) |
| 🌊 Hydrology | USGS NWIS (stream gauges / wells) | Public domain (U.S. government data) | “Source: USGS NWIS” (+ dataset link) |
| ⛈️ Severe weather | NOAA Storm Events Database | Public domain / open access | “Source: NOAA Storm Events Database” |
| 🏜️ Drought | U.S. Drought Monitor | Public domain (joint product) | “Source: U.S. Drought Monitor” |
| 🔥 Wildfires | Wildfire Perimeters (national + Kansas sources) | Public domain (per KFM notes) | “Source: NIFC / Kansas GIS Hub (as applicable)” |
| 🧩 Basemap | OpenStreetMap | Attribution required (tile/provider terms vary) | “© OpenStreetMap” |
| ⚠️ Restricted imagery | Google Earth imagery / 3D | **Not public domain**; subject to Google + third‑party licensing | Only use via allowed paths + obey attribution & usage rules |

---

## ⚠️ Special case: Google Earth content (do not “just use it”)

> [!WARNING]
> Google Earth imagery/data is **not public domain**, and Google sources imagery from third parties.  
> Screenshots, tiles, 3D meshes/textures, and derived extraction can violate terms unless done via approved methods.

**If you think you need Google Earth assets:**
1. Document the exact use (screenshot? tiles? video? 3D mesh?).
2. Confirm the allowed workflow (API/permissions).
3. Store **attribution + policy notes** in `licenses/google-earth/` (or similar).
4. Prefer open imagery alternatives when possible.

---

## 🪪 License patterns we commonly touch

### 🟦 Public Domain (common for U.S. government datasets)
- You can generally use/redistribute freely
- Still **attribute the source** (best practice + helps provenance)

### 🟩 CC BY 4.0 (Creative Commons Attribution 4.0)
If you use CC BY 4.0 content (text/images), you must:
- give appropriate credit
- link to the license
- indicate changes (if any)

> Put the exact attribution copy in `NOTICE.md`.

### 🟥 “All Rights Reserved” (books, stock icons, proprietary media)
If it’s not clearly licensed for reuse:
- **do not copy/paste** text/images into the app
- don’t commit stock media unless the project owns the license
- store only a pointer + internal note (if needed)

---

## ➕ How to add a new asset/source (checklist)

1. **Create a folder** under `licenses/`:
   - `media--vendor--asset/` or `data--provider--dataset/`
2. Add:
   - `SOURCE.md` (where it came from, URL, what it is)
   - `LICENSE.txt` (full text) **or** “license reference” if it cannot be redistributed
   - `NOTICE.md` (the exact UI attribution we will display)
3. If modified:
   - `CHANGES.md` (what we changed, date, who)
4. (Optional) update `manifest.json` so the UI can render it automatically.

---

## 🧪 Suggested automation (optional but 🔥)

- ✅ CI check that **every file in `web/src/assets/**` has a matching entry** in this folder
- ✅ CI check that `manifest.json` matches actual folders
- ✅ Dependency license reporting stays in the package manager layer (npm/pnpm/yarn), but **UI-facing assets** must also be documented here

---

## 🧩 Templates

You can copy these into `_templates/` (and then into each asset folder):

<details>
<summary><strong>NOTICE.md template</strong></summary>

```md
# Attribution Notice

**Name:**  
**Source URL:**  
**License:**  
**Required attribution text (exact):**  
**Where shown in UI:**  
**Notes / constraints:**
```

</details>

<details>
<summary><strong>SOURCE.md template</strong></summary>

```md
# Source & Provenance

## What is this?
(Short description)

## Where did we get it?
- URL:
- Retrieved on:
- Vendor/Author:

## How is it used?
- Local path(s):
- Runtime usage (UI surfaces):

## License summary
- License name / version:
- Obligations:
- Restrictions:
```

</details>

---

## 🧯 Not legal advice

This is an engineering compliance workflow document, not legal counsel. When a license is unclear, **stop and verify** before shipping.

---
