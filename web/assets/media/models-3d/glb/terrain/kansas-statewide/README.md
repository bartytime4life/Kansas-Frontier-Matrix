# Kansas Statewide Terrain (GLB) 🏞️🧱

![format](https://img.shields.io/badge/format-glTF%202.0%20%7C%20GLB-blue)
![scope](https://img.shields.io/badge/scope-Kansas%20%7C%20statewide-brightgreen)
![policy](https://img.shields.io/badge/policy-provenance--first-orange)
![runtime](https://img.shields.io/badge/runtime-web%2Fassets-lightgrey)

> 📁 **Location:** `web/assets/media/models-3d/glb/terrain/kansas-statewide/`  
> This directory contains the **Kansas statewide terrain surface** used by the KFM web UI for **3D context** (Cesium / three.js scenes, “Kansas From Above” story beats, etc.).

---

## 🧭 At-a-glance

| What | Where it lives | Source of truth |
|---|---:|---|
| 🧱 Runtime 3D mesh | This folder (`*.glb`) | **Data contract** (`terrain.contract.json`) |
| 🧾 Provenance + license + extent | `terrain.contract.json` | Contract validators / catalogs |
| 🧠 Story + UI references | Web UI / story nodes | Should point back to contract/citation |

> [!IMPORTANT]
> **No “mystery layers.”** Any terrain model in this folder must have a **matching data contract** describing **source + license + processing** before it’s considered “official” for KFM.

---

## ✨ Why this exists

KFM supports layered mapping over time and can expand into **3D terrain visualization**. A statewide terrain mesh provides the base physical context (relief, slopes, landform shape) to support:
- 🧭 **2D → 3D transitions** in stories (e.g., “Kansas From Above” scenes)
- 🛰️ **Draped overlays** (historic land cover, imagery, etc.) on a physical surface
- 🎯 **Region callouts** (Flint Hills, river valleys, watershed divides)

---

## 📦 What’s in here

**Target layout (recommended):**
```text
📁 kansas-statewide/
├─ 🧱 *.glb                       # Terrain mesh(es) (glTF 2.0 binary)
├─ 🖼️ thumbnail.(png|webp)         # Optional preview image
├─ 🧾 terrain.contract.json         # REQUIRED: provenance + license + extent + processing
└─ 📄 README.md
```

---

## 🗂️ Recommended naming (keep it boring ✅)

If you add LODs or variants, prefer a predictable pattern:
- `ks_statewide_terrain_lod0.glb`
- `ks_statewide_terrain_lod1.glb` (optional)
- `terrain.contract.json`
- `thumbnail.webp` (optional)

> [!TIP]
> “Statewide” meshes should stay lightweight. If you need detail, add a **regional/high-res** terrain asset (and blend or swap by zoom).

---

## 🎮 Using the terrain in the web client

### three.js (GLTFLoader) 🧩

```js
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

const loader = new GLTFLoader();

loader.load(
  '/assets/media/models-3d/glb/terrain/kansas-statewide/<terrain-file>.glb',
  (gltf) => {
    const terrain = gltf.scene;
    terrain.name = 'kansas-statewide-terrain';

    // Optional: keep terrain in a dedicated group/layer for toggling
    // terrain.layers.set(1);

    scene.add(terrain);
  }
);
```

### CesiumJS (Model primitive) 🌍

```js
const model = await Cesium.Model.fromGltfAsync({
  url: '/assets/media/models-3d/glb/terrain/kansas-statewide/<terrain-file>.glb',

  // Use the anchor in terrain.contract.json to build the modelMatrix:
  modelMatrix: Cesium.Transforms.eastNorthUpToFixedFrame(
    Cesium.Cartesian3.fromDegrees(anchorLon, anchorLat, anchorHeightMeters)
  ),

  scale: 1.0,
});

viewer.scene.primitives.add(model);
```

> [!NOTE]
> If you find yourself fighting file size or needing smooth zoom-based detail, consider moving the **source elevation** into a **streaming terrain format** (e.g., Cesium-friendly tiling) and keep this GLB for simple/static use.

---

## 🧭 Spatial reference, units & georeferencing

KFM’s web-facing spatial standard is **WGS84 (EPSG:4326)** for consistency across layers. If processing uses another CRS (State Plane, Lambert, etc.), the **original CRS must be recorded** and web alignment must be handled via reprojection or a known transform.

**Expectations for this terrain asset:**
- 📐 **Units:** meters (including vertical units)
- 🧭 **Extent metadata:** bbox stored in EPSG:4326 (minLon, minLat, maxLon, maxLat)
- 🧷 **Georeferencing:** store an **anchor** (lon/lat/height) + any transform rules needed by the viewer
- 🧾 **Original CRS:** captured in provenance metadata if different during processing

<details>
<summary>🧾 Minimal <code>terrain.contract.json</code> template (recommended)</summary>

```json
{
  "id": "terrain_kansas_statewide_glb",
  "title": "Kansas Statewide Terrain (GLB)",
  "description": "Statewide terrain surface used by the KFM 3D web UI.",
  "schema_version": "vX.Y.Z",
  "license": "SEE_SOURCE",
  "spatial": {
    "bbox": ["minLon", "minLat", "maxLon", "maxLat"],
    "crs": "EPSG:4326",
    "vertical_units": "meters",
    "vertical_datum": "REQUIRED_IF_KNOWN"
  },
  "provenance": {
    "source_name": "REQUIRED",
    "source_url": "REQUIRED",
    "creator": "REQUIRED",
    "issued": "YYYY-MM-DD",
    "processing_steps": [
      "Reprojected source elevation to EPSG:4326 for web alignment (or documented transform)",
      "Generated mesh from elevation surface",
      "Simplified/decimated for statewide performance",
      "Exported to GLB (glTF 2.0)"
    ]
  },
  "rendering": {
    "anchor": { "lon": "REQUIRED", "lat": "REQUIRED", "height_m": "REQUIRED" },
    "up_axis": "Y",
    "notes": "Viewer-specific transforms/scaling go here."
  },
  "faircare": {
    "collective_benefit": "RECOMMENDED",
    "authority_to_control": "RECOMMENDED",
    "responsibility": "RECOMMENDED",
    "ethics": "RECOMMENDED"
  }
}
```

</details>

> [!IMPORTANT]
> If the terrain is derived from LiDAR/DEM products (or services like statewide hillshade), **do not assume license terms** — capture them explicitly in the contract.

---

## 🏗️ Build/update pipeline (high-level)

KFM follows a **contract-first & evidence-first** approach: runtime artifacts (like this GLB) should be outputs of the pipeline — not files that bypass provenance/citation requirements.

**Conceptual flow:**
1. 🧪 **ETL / ingest:** obtain elevation source (DEM / LiDAR-derived products), record original CRS + license  
2. 🧾 **Catalog & lineage:** publish STAC/DCAT/PROV metadata (data contract + provenance)  
3. 🧱 **Derive artifact:** generate/export optimized mesh (GLB) for the web UI  
4. 🌐 **Serve & render:** expose via APIs/static assets, referenced by UI + stories  

---

## 🛠️ Troubleshooting

- **Terrain appears “flat”** → check vertical scaling (units must be meters) and ensure the mesh wasn’t normalized without recording the multiplier.
- **Terrain is offset / drifting** → verify `anchor` (lon/lat/height) and any viewer transform logic.
- **Terrain is upside-down** → confirm axis conventions and that transforms were applied/frozen before export.
- **Performance is poor** → decimate more, add LODs, compress, or switch to streaming terrain formats.

---

## ⚡ Performance & LOD tips

- 🧩 Prefer **tiling/LODs** for “zoom-in” experiences (statewide in LOD0, regions in LOD1+).
- 🗜️ Consider GLB compression (Draco / meshopt) where your runtime supports it.
- 🎛️ Keep materials simple; terrain reads well with lighting + hillshade-style shading.

---

## ✅ QA checklist (Definition of Done)

Before merging/using a new or updated statewide terrain GLB:

- [ ] 🧾 A `terrain.contract.json` exists and includes **source + license + processing steps**
- [ ] 🧭 Spatial extent is correct and expressed in **EPSG:4326** in metadata
- [ ] 📏 Vertical units are declared (meters) + vertical datum noted if known
- [ ] 🎮 Loads in target viewer(s) without flipping / scaling surprises
- [ ] ⚡ File size and triangle count are reasonable for web delivery
- [ ] 🧪 Regeneration steps are scripted/repeatable (pipeline-friendly)
- [ ] 🧠 Any story/UI usage can trace back to the contract (no orphan assets)

---

## 🔗 Related

- 🛰️ **Environmental & terrain layers**: DEM/LiDAR-derived products + hillshade/slope/aspect (see the contract for authoritative citations)
- 🌍 **3D roadmap**: Cesium-based streaming terrain / 3D Tiles for high-res experiences
- 🗺️ **2D UI**: MapLibre/Leaflet for layered historical mapping; 3D is opt-in for deeper context
