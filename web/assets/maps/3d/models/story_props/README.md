# 🧩 Story Props (3D Models)

![Asset Type](https://img.shields.io/badge/asset_type-story_props-3b82f6)
![Format](https://img.shields.io/badge/format-glTF%202.0%20(.glb)-blue)
![Viewer](https://img.shields.io/badge/viewer-CesiumJS%20(3D)-6f42c1)
![Policy](https://img.shields.io/badge/policy-provenance--first-important)

> “Story props” are small 3D models used to enhance **interactive narratives** in Kansas Frontier Matrix (KFM) when a story step switches the map into **3D mode** (Cesium). They are **not** full geospatial datasets—think: a landmark model 🪨, an artifact 🏺, a sign 🪧, a wagon 🛞, or a simple structure 🏠.

---

## 🎯 What belongs in `story_props/`

✅ **Use this folder** for:
- Lightweight/optimized 3D models that appear in a story step (fade in/out, click, hover, etc.)
- Narrative objects anchored to a point (lon/lat/height), optionally with a default orientation/scale
- “Wow-factor” moments in stories (e.g., reveal a landmark in 3D)

🚫 **Do not use this folder** for:
- Large 3D geospatial datasets (city-scale buildings, LiDAR point clouds, massive terrain meshes)
- Anything that needs streaming/tiling (use a **3D Tiles** tileset and reference by URL)
- Temporary / unlicensed / unknown-provenance assets

> [!IMPORTANT]
> KFM is **contract-first & provenance-first**. Treat every prop as an *asset with sources* — not “just a model file.”

---

## 🗺️ How props are used in KFM stories

KFM stories are typically authored as:
- **Markdown** narrative text (with images/citations), plus
- a **JSON** configuration that defines a step-by-step sequence (camera moves, layer toggles, overlays, etc.)

Story props are loaded when a step needs 3D context:
1. A story step switches to 3D (Cesium view).
2. The step references one or more props from this folder.
3. Props are positioned at WGS84 coordinates (lon/lat + optional height) and rendered with the story’s camera.

---

## 📁 Recommended folder layout

Keep each prop in its own folder so we can ship **model + preview + metadata** together.

```text
📁 web/assets/maps/3d/models/story_props/
├── 📄 README.md
├── 📁 monument_rocks/
│   ├── 📦 monument_rocks.glb
│   ├── 🖼️ monument_rocks.preview.webp
│   └── 🧾 monument_rocks.asset.json
├── 📁 prairie_wagon/
│   ├── 📦 prairie_wagon.glb
│   ├── 🖼️ prairie_wagon.preview.webp
│   └── 🧾 prairie_wagon.asset.json
└── 📁 ...
```

> [!NOTE]
> If your export requires external textures, keep them inside the same prop folder (e.g., `textures/`). Prefer `.glb` to avoid texture path issues.

---

## 📦 Supported formats

### ✅ Preferred
- **`.glb`** (binary glTF 2.0) — single file, web-friendly, fewer path issues

### ✅ Allowed (when needed)
- `.gltf` + `.bin` + textures (debugging or special pipelines)

### 🚫 Avoid
- `.fbx`, `.blend`, `.max` (authoring formats) — export runtime assets instead
- Raw scan meshes directly from photogrammetry (too heavy—optimize first)

---

## 🧾 Required metadata: the *Asset Contract* file

Every prop **must** include a sidecar metadata file:

```
<prop_id>.asset.json
```

This is how we prevent “mystery props” and keep UI assets traceable (license, source, processing, and how it should be placed).

### ✅ Minimum recommended fields

| Field | Why it exists |
|------:|---------------|
| `id` | Stable identifier (used in story configs) |
| `title`, `description` | Human-readable cataloging |
| `license` | Must be explicit (and compatible) |
| `source` | Where it came from (URL / archive / creator) |
| `attribution` | Credit text required by the license |
| `provenance[]` | How it was created/modified (tools + steps) |
| `assets.model.path` | Path to `.glb` / `.gltf` |
| `placement_defaults` | Default scale/orientation/height behavior |

### 🧩 Example `*.asset.json`

```json
{
  "type": "kfm.story_prop",
  "id": "monument_rocks",
  "title": "Monument Rocks (Chalk Pyramids)",
  "description": "Low-poly landmark prop used in 3D story steps.",
  "license": "CC BY 4.0",
  "source": {
    "name": "Kansas Geological Survey",
    "url": "https://example.com/source-page",
    "retrieved": "2026-01-17"
  },
  "attribution": "Kansas Geological Survey (CC BY 4.0)",
  "assets": {
    "model": {
      "path": "monument_rocks/monument_rocks.glb",
      "media_type": "model/gltf-binary"
    },
    "preview": {
      "path": "monument_rocks/monument_rocks.preview.webp",
      "media_type": "image/webp"
    }
  },
  "placement_defaults": {
    "crs": "EPSG:4326",
    "height_reference": "clampToGround",
    "scale": 1.0,
    "heading_pitch_roll_deg": { "heading": 0, "pitch": 0, "roll": 0 }
  },
  "provenance": [
    {
      "step": "Modeled and UV-unwrapped",
      "tool": "Blender",
      "by": "KFM Team",
      "when": "2026-01-17"
    },
    {
      "step": "Mesh decimation + export to GLB",
      "tool": "Blender",
      "when": "2026-01-17"
    }
  ],
  "tags": ["landmark", "geology", "kansas"]
}
```

> [!TIP]
> If you already have KFM-style dataset contracts, mirror that structure (source ➜ license ➜ processing ➜ outputs). Props are “assets,” not exceptions.

---

## 🧰 Performance budget & optimization guidelines

3D is **computationally heavier** than 2D layers—keep story props lightweight.

### Suggested targets (web-friendly)
- **File size:** ideally < **2–5 MB** per prop
- **Triangles:** keep it modest (optimize scans; avoid millions of tris)
- **Materials:** 1–2 materials if possible
- **Textures:** prefer **1K–2K**, avoid huge uncompressed PNG stacks

### Recommended optimization steps
- Remove hidden/internal geometry
- Merge meshes where sensible (reduce draw calls)
- Bake lighting if appropriate (storybook props often don’t need dynamic GI)
- Generate LODs if a prop appears at multiple zoom levels

<details>
  <summary><strong>🧪 Optional tooling ideas</strong> (click to expand)</summary>

- Validate: `gltf-validator`
- Optimize/compress: `gltf-transform` (mesh simplification / Draco / texture resizing)
- Texture compression: KTX2/BasisU (only if the runtime supports it)

</details>

---

## ➕ Adding a new prop (checklist)

1. **Create folder**: `story_props/<prop_id>/`
2. **Export model** to `.glb` (preferred) and place it in the prop folder
3. **Create preview** (`.webp` or `.png`)
4. **Write the asset contract**: `<prop_id>.asset.json`
5. **Reference it in a story step** (story JSON)
6. **Test in 3D** (Cesium view) and confirm:
   - placement (lon/lat/height)
   - scale/orientation
   - performance (no stutters)
   - attribution is visible where expected

---

## 🧷 Referencing a prop from a story step

Story config schemas may vary, but the pattern is consistent: a step includes a prop reference + placement.

```json
{
  "id": "step-02-monument-rocks",
  "mode": "3d",
  "camera": { "lon": -101.123, "lat": 38.876, "height_m": 2500 },
  "props": [
    {
      "id": "monument_rocks",
      "src": "/assets/maps/3d/models/story_props/monument_rocks/monument_rocks.glb",
      "position": { "lon": -101.123, "lat": 38.876, "height_m": 0 },
      "scale": 1.0,
      "heading_pitch_roll_deg": { "heading": 0, "pitch": 0, "roll": 0 }
    }
  ]
}
```

> [!NOTE]
> If the prop is *large* or you need many instances, consider hosting it as **3D Tiles** and referencing the tileset instead of committing huge binaries here.

---

## ✅ QA checklist before merging

| Check | Pass criteria |
|------|---------------|
| Loads in 3D viewer | No missing textures, no console errors |
| Correct scale | Looks plausible relative to terrain/buildings |
| Correct pivot/origin | Placement anchor behaves predictably |
| Performance | Doesn’t tank FPS on typical hardware |
| Metadata present | `*.asset.json` exists and includes license + source |
| Attribution | Credit text is available for UI display |

---

## 🪪 Licensing & attribution rules

- Do **not** add assets with unknown or incompatible licenses.
- Always include the license + source + required attribution in the asset contract.
- If you created the model in-house, still record provenance steps (tools, dates, authors).

> [!WARNING]
> If we can’t trace it, we can’t ship it. 🚫

---

## 🔗 Related KFM folders

- `web/viewers/` — map viewer logic (2D MapLibre + 3D Cesium)
- `web/story_nodes/` — story Markdown + step configuration JSON
- `web/assets/` — other static assets (icons, images, etc.)

---

## 🧭 Future improvements (nice-to-haves)

- Prop registry/index (`story_props.index.json`) for fast discovery & validation
- Automated CI checks:
  - ensure every prop has `*.asset.json`
  - enforce size/poly budgets
  - validate glTF structure
- Optional LOD + streaming strategy for “heavy” story scenes

---

🧠 **Mantra:** *No mystery layers → no mystery props.* ✅
