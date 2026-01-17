# 🏔️ 3D Terrain Assets (Cesium-ready)

![Path](https://img.shields.io/badge/path-web%2Fassets%2Fmaps%2F3d%2Fterrain-informational)
![Type](https://img.shields.io/badge/type-static%20web%20assets-blue)
![Usage](https://img.shields.io/badge/usage-Cesium%203D%20terrain-orange)
![Policy](https://img.shields.io/badge/policy-provenance--first-success)

This folder contains **packaged terrain datasets** (elevation surfaces) that can be served as **static web assets** for KFM’s **3D map mode** (Cesium-based). 🌎⛰️

> [!IMPORTANT]
> Keep this directory **lean**. If a terrain dataset is “big Kansas” (or bigger), it should be **streamed via a terrain/tile service** in production. This folder is best for **small AOIs, demo packs, and test fixtures**.

---

## 🎯 What lives here

✅ Good fits for `web/assets/maps/3d/terrain/`:

- **Small, clipped terrain packs** used for offline demos or local development 🧪  
- **Visual regression test fixtures** (known terrain used in snapshots) 📸  
- **Story-specific AOIs** where 3D context matters (e.g., a battlefield ridge line) 🧭  
- **Experiment packs** while iterating on pipeline/tooling (as long as provenance is recorded)

🚫 Avoid putting these here:

- Full-state / high-resolution “forever” terrain datasets (store + serve them properly)
- Anything without clear **source + license + processing notes** (no “mystery layers” 🕵️‍♂️)

---

## 🧩 How the app uses terrain

KFM’s front-end includes both **2D** and **3D** viewing modes:

- **2D**: MapLibre-based map viewing  
- **3D**: Cesium-based globe/terrain visualization  

Terrain packs in this directory are meant to be referenced by the **3D viewer** (see `web/viewers/`), typically by pointing Cesium’s terrain provider at a URL that resolves to a **terrain package root**.

---

## 📦 Recommended directory layout

```text
web/assets/maps/3d/terrain/
├─ README.md
├─ manifest.json              # 👈 registry of available terrain packs (recommended)
└─ kansas_dem_10m_demo/       # 👈 example pack folder (name yours similarly)
   ├─ layer.json              # Cesium terrain root metadata (common)
   ├─ attribution.md          # required: credits + license notes
   ├─ metadata.json           # optional: extra KFM-friendly metadata (see below)
   └─ 0/                      # tiles (LOD hierarchy)
      └─ 0/
         └─ 0.terrain
```

> [!TIP]
> Name packs with a stable, descriptive id:  
> `"<region>_<source>_<resolution>_<variant>"`  
> Example: `flint_hills_usgs_10m_v1`

---

## 🗺️ Supported terrain packaging

This folder is primarily intended for **Cesium-consumable terrain**:

- **Quantized-Mesh terrain** (recommended for Cesium terrain providers)
- **3D Tiles terrain-like meshes** (advanced / experimental; useful if you’re already in a 3D Tiles pipeline)
- **Heightmap terrain** (ok for dev/testing, not ideal for “real” production terrain)

---

## 🧾 `manifest.json` (recommended)

To keep the UI predictable and governance-friendly, add a `manifest.json` that lists available packs and their metadata.

### Minimal schema (suggested)

```json
[
  {
    "id": "flint_hills_usgs_10m_v1",
    "title": "Flint Hills DEM (10m) — Demo Pack",
    "type": "cesium-quantized-mesh",
    "status": "demo",
    "path": "/assets/maps/3d/terrain/flint_hills_usgs_10m_v1/",
    "bbox_wgs84": [-96.95, 38.25, -95.95, 39.05],
    "resolution_m": 10,
    "vertical_units": "meters",
    "license": "TBD",
    "attribution_file": "attribution.md",
    "source_notes": "Fill in: dataset source + link/identifier",
    "processing_notes": "Fill in: clip/reproject/tooling/parameters"
  }
]
```

> [!NOTE]
> If a terrain pack is meant to be “official”, link it to the **catalog/provenance artifacts** (STAC/DCAT/PROV) in your pipeline—not just a loose manifest.

---

## ➕ Add a new terrain pack (runbook)

### 1) Prepare the source DEM/DTM
- Confirm **spatial extent**, **resolution**, **vertical units/datum**, and **license**.
- If you derived the terrain from LiDAR/photogrammetry products, document the **method** and **interpolation** choices.

### 2) Clip to your AOI ✂️
- Clip to the smallest bounding box/polygon that supports the story/demo.
- Keep files small enough to load quickly in a browser.

### 3) Build a Cesium-friendly terrain package 🧰
- Convert the DEM into a terrain format your Cesium viewer expects (commonly quantized-mesh).
- Ensure the output contains a terrain root file (often `layer.json`) plus tile hierarchy.

### 4) Drop the pack into this directory 📥
- Create `web/assets/maps/3d/terrain/<terrain-pack-id>/`
- Add:
  - `attribution.md` ✅ (required)
  - `metadata.json` ✅ (optional but recommended)
  - terrain root (`layer.json` or equivalent) ✅

### 5) Register the pack 🔖
- Add an entry to `manifest.json` (or whatever registry your viewer uses).

### 6) Wire it into the viewer 🧭
- Update the 3D viewer configuration to point at the pack’s `path`.
- Validate:
  - correct LOD behavior (zoom in/out)
  - no visible seams/spikes
  - reasonable load times

---

## 🧠 Governance & provenance rules (don’t skip)

> [!WARNING]
> If it shows up in the UI, it must be explainable. No “mystery terrain.”

**Minimum requirement for every terrain pack in this folder:**
- ✅ Source (who/where it came from)
- ✅ License/usage rights
- ✅ Spatial extent + resolution
- ✅ Processing notes (how it was produced)
- ✅ Attribution text (`attribution.md`)

**Preferred (for anything beyond a quick demo):**
- ✅ A proper **catalog + provenance trail** (STAC/DCAT/PROV) created in the pipeline
- ✅ A stable dataset id you can reference from UI/story steps
- ✅ Reproducible tooling/parameters recorded somewhere (run logs, scripts, or pipeline config)

---

## 🚀 Performance tips

- Keep the AOI small (terrain tiles can grow fast 📈)
- Avoid bundling statewide/high-res terrain into the web build
- Prefer fewer LOD levels for demos
- Test on a mid-range laptop + typical browser cache settings

---

## 🐞 Troubleshooting

**Terrain is flat / not applying**
- Verify the viewer is actually pointing at the pack root URL.
- Check that root metadata (`layer.json` or equivalent) is reachable.

**404s on tiles**
- Confirm the folder structure matches what your terrain provider expects.
- Validate the `path` in `manifest.json` matches your static asset base path.

**Spikes / weird elevations**
- Check vertical units (meters vs feet) and any datum shifts.
- Confirm your DEM wasn’t accidentally scaled or clipped with nodata artifacts.

**Loads are slow**
- Reduce AOI size or LOD depth.
- Ensure the server sets cache headers for static tiles.

---

## 🔗 Related areas in the repo

- `web/viewers/` → map viewer implementations (2D + 3D) 🧭  
- `web/assets/maps/` → other map-related static assets 🗺️  
- `data/` + catalogs (STAC/DCAT/PROV) → authoritative data publication pipeline 📚  

---

## 📜 Attribution template (copy/paste)

Create `attribution.md` inside each pack:

```md
# Attribution

**Dataset:** <name>  
**Source:** <organization / portal / dataset id>  
**License:** <license + any restrictions>  
**Accessed:** <YYYY-MM-DD>  

## Processing
- <clip AOI>
- <reprojection>
- <terrain build tooling + versions>
- <parameters>
```