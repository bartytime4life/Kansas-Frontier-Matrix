<!-- According to a document from 2026-01-17 (project docs snapshot used to draft this README). -->

# 🧊 GLB 3D Models (`.glb`)
**Path:** `web/assets/media/models-3d/glb/`

![Format](https://img.shields.io/badge/format-GLB%20%2F%20glTF%202.0-blue)
![Target](https://img.shields.io/badge/target-web%20(WebGL)-informational)
![Policy](https://img.shields.io/badge/policy-provenance--first-success)

This folder contains **glTF Binary** (`.glb`) assets intended for the KFM web experience—things like **3D terrain**, **sites/structures**, **artifacts**, and other spatial story elements.

> [!IMPORTANT]
> **No “mystery models.”** Every model must ship with clear provenance + licensing metadata (see **Model Contract** ✅).

---

## 📌 Table of Contents
- [🎯 What belongs here](#-what-belongs-here)
- [🗂️ Recommended folder layout](#️-recommended-folder-layout)
- [➕ Adding a new model](#-adding-a-new-model)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧾 Model contract (required)](#-model-contract-required)
- [🌍 Geospatial conventions](#-geospatial-conventions)
- [⚡ Performance & optimization](#-performance--optimization)
- [✅ Review checklist](#-review-checklist)
- [🔐 Sensitive locations & ethics](#-sensitive-locations--ethics)
- [📜 Licensing & attribution](#-licensing--attribution)
- [🧰 Troubleshooting](#-troubleshooting)

---

## 🎯 What belongs here

✅ **Good fits**
- Web-ready `.glb` models (PBR-friendly, reasonable polygon counts)
- Models intended for **interactive UI** (click/select/inspect)
- Models that can be **traceably sourced** (public domain, CC, licensed, or original work)

🚫 **Avoid**
- Unattributed downloads (unknown license)
- Unbounded mega-assets (huge scans) without LODs, simplification, or tiling
- Models that reveal sensitive locations at dangerous precision (see [Sensitive locations & ethics](#-sensitive-locations--ethics))

---

## 🗂️ Recommended folder layout

Keep each model **self-contained** in a folder so we can store metadata, previews, and licensing together.

```text
📁 web/assets/media/models-3d/glb/
├─ 📄 README.md
├─ 📄 manifest.json                # optional: registry for the web app
├─ 📁 terrain/
│  └─ 📁 kansas-statewide/
│     ├─ 🧊 model.lod0.glb
│     ├─ 🧊 model.lod1.glb
│     ├─ 🖼️ preview.webp
│     ├─ 🧾 model.contract.json
│     └─ 📜 LICENSE.md
├─ 📁 sites/
│  └─ 📁 fort-leavenworth-blockhouse-1864/
│     ├─ 🧊 model.lod0.glb
│     ├─ 🖼️ preview.webp
│     ├─ 🧾 model.contract.json
│     ├─ 📜 LICENSE.md
│     └─ 📝 notes.md               # optional: context, limitations, interpretive notes
└─ 📁 artifacts/
   └─ 📁 kansa-pottery-shard-a/
      ├─ 🧊 model.lod0.glb
      ├─ 🖼️ preview.webp
      ├─ 🧾 model.contract.json
      └─ 📜 LICENSE.md
```

> [!TIP]
> If you truly need a **single-file drop**, you can place the `.glb` at the top-level—**but still** include its `model.contract.json` + `LICENSE.md` in a same-named folder or a sidecar pattern.

---

## ➕ Adding a new model

1. **Create a folder** under the right domain (`terrain/`, `sites/`, `artifacts/`, etc.).
2. Export or place your model as:
   - `model.lod0.glb` (required)
   - `model.lod1.glb`, `model.lod2.glb` (optional but strongly recommended)
3. Add a **preview image**: `preview.webp`
4. Create `model.contract.json` (required)
5. Add `LICENSE.md` (required)
6. (Optional) Add `notes.md` if the model is interpretive, reconstructed, or has known limitations.
7. (Optional) Register it in `manifest.json` if the web app uses a manifest registry.

---

## 🏷️ Naming conventions

### Folder names
- ✅ `kebab-case`
- ✅ short, descriptive
- ✅ include approximate date if it matters (e.g., `...-1864`)
- ❌ no spaces, no emojis in folder names, avoid uppercase

Examples:
- `fort-leavenworth-blockhouse-1864`
- `kansas-statewide`
- `kansa-pottery-shard-a`

### File names
Use the standard set:
- `model.lod0.glb` (required)
- `model.lod1.glb` (optional)
- `preview.webp` (recommended)
- `model.contract.json` (required)
- `LICENSE.md` (required)

> [!NOTE]
> **LOD naming** is deliberate. It keeps the runtime simple: choose LOD by device/perf budget and load `model.lod?.glb`.

---

## 🧾 Model contract (required)

Each model needs a **contract file** that acts like a “data contract” / “model card”:
- tells us **what it is**
- tells us **where it came from**
- tells us **what license applies**
- tells us **how it was processed**
- tells the UI how to place/scale it

### ✅ Required fields (minimum)
- `schema_version`
- `id`
- `title`
- `description`
- `license`
- `provenance.source`
- `provenance.attribution`
- `files.lod0`
- `spatial.units`
- `spatial.up_axis`

### 📄 Template: `model.contract.json`

```json
{
  "schema_version": "kfm.model-contract.v1",
  "id": "sites/fort-leavenworth-blockhouse-1864",
  "title": "Fort Leavenworth Blockhouse (circa 1864)",
  "description": "A lightweight web-optimized reconstruction for educational visualization. See notes for uncertainty and assumptions.",
  "tags": ["kansas", "fort-leavenworth", "civil-war-era", "reconstruction"],

  "license": "CC-BY-4.0",

  "files": {
    "lod0": "model.lod0.glb",
    "lod1": "model.lod1.glb",
    "preview": "preview.webp",
    "notes": "notes.md"
  },

  "spatial": {
    "units": "m",
    "up_axis": "Y",

    "georeferenced": true,
    "crs": "EPSG:4326",

    "origin": { "lon": -94.9220, "lat": 39.3500, "alt_m": 230.0 },
    "frame": "ENU",

    "bbox_wgs84": [-94.9240, 39.3485, -94.9200, 39.3515],
    "approx_horizontal_accuracy_m": 15
  },

  "rendering": {
    "pbr": true,
    "double_sided": false,
    "preferred_lod": "lod1"
  },

  "provenance": {
    "source": {
      "type": "photogrammetry|lidar|archival|hand-modeled|procedural",
      "source_url": "https://example.org/source-or-archive-record",
      "creator": "Example Institution or Author",
      "issued": "2024-05-10"
    },
    "attribution": "Example Institution (CC-BY-4.0)",
    "processing_steps": [
      "Cleaned scan",
      "Retopology + decimation",
      "Baked textures",
      "Exported glTF 2.0 / GLB"
    ],
    "checksum": {
      "lod0_sha256": "REPLACE_ME",
      "lod1_sha256": "REPLACE_ME"
    }
  },

  "faircare": {
    "collective_benefit": "Education and preservation of Kansas history.",
    "authority_to_control": "Open",
    "responsibility": "KFM Maintainers",
    "ethics": "If culturally sensitive, see sensitivity fields and restrictions."
  },

  "sensitivity": {
    "classification": "public|restricted|sensitive",
    "notes": "If restricted, remove precise origin/bbox and publish generalized LOD only."
  }
}
```

> [!TIP]
> If `georeferenced=false`, omit `origin`, `bbox_wgs84`, and use a neutral scene origin. Still keep `units` + `up_axis`.

---

## 🌍 Geospatial conventions

To keep placement consistent across the web map + 3D viewer:

- **Units:** meters (`"units": "m"`)
- **Up-axis:** Y (`"up_axis": "Y"`)
- **Georeferencing (recommended):**
  - Store a **WGS84 origin** (`EPSG:4326`) in the contract
  - Model coordinates are interpreted as **local meters** in a declared frame (e.g., `"frame": "ENU"`)
  - Avoid huge world coordinates inside the mesh (floating point precision issues)

> [!WARNING]
> If you change `origin`, `frame`, `scale`, or `up_axis`, treat it as a **breaking change**—update the contract + regenerate derived placements.

---

## ⚡ Performance & optimization

Web performance matters. Prefer:
- ✅ multiple LODs (`lod0`/`lod1`/`lod2`)
- ✅ reasonable texture sizes (e.g., 1–2k for mid LODs)
- ✅ merged materials where possible
- ✅ clean topology (remove hidden faces, duplicates, stray vertices)

<details>
  <summary><strong>🧪 Suggested targets (adjust per scene)</strong></summary>

- **LOD0 (desktop/high):** best quality
- **LOD1 (default):** balanced
- **LOD2 (mobile/overview):** lightweight

Heuristics (not hard rules):
- Keep **LOD1** under ~5–15 MB when possible
- Keep **draw calls** low (merge meshes/materials thoughtfully)
- Prefer GPU-friendly textures; avoid many separate texture files

</details>

---

## ✅ Review checklist

Before merging a new model:

- [ ] `model.contract.json` present + filled
- [ ] `LICENSE.md` present + matches contract
- [ ] `preview.webp` present (and looks correct)
- [ ] LODs load correctly (if provided)
- [ ] Orientation is correct (no sideways/upside-down)
- [ ] Scale is correct (units are meters)
- [ ] Pivot/origin makes sense (no weird offset)
- [ ] No embedded sensitive info (or marked + generalized)
- [ ] Contract includes provenance and processing steps

---

## 🔐 Sensitive locations & ethics

Some models should **not** be fully public or should be published with **reduced precision** (e.g., sacred sites, endangered species habitat, fragile archaeological locations).

Recommended approaches:
- publish only a **generalized LOD**
- reduce `bbox` precision / omit exact `origin`
- mark contract `sensitivity.classification = "restricted"` or `"sensitive"`
- provide a safe explanation in `notes.md`

---

## 📜 Licensing & attribution

Every model must have:
- a clearly stated `license` in `model.contract.json`
- an accompanying `LICENSE.md` explaining:
  - license text or SPDX identifier
  - required attribution wording
  - any usage restrictions (commercial/non-commercial, share-alike, etc.)

> [!NOTE]
> If a model depends on a source with attribution requirements, ensure the UI can surface it. That’s why the contract includes `provenance.attribution`.

---

## 🧰 Troubleshooting

**Model is black / unlit**
- Check normals
- Confirm PBR materials are valid
- Ensure textures are present and referenced correctly

**Model is rotated wrong**
- Confirm `up_axis`
- Re-export with consistent axis settings and document it

**Model is huge / tiny**
- Confirm units in DCC tool (Blender/Maya/etc.)
- Ensure `"units": "m"` matches export scale

**Model is offset on the map**
- Confirm `origin` and `frame`
- Confirm the intended anchor point (center vs corner vs known landmark)

---

### 🧭 Philosophy (why this is strict)
This repository treats models as **first-class data assets**—meaning they must be auditable, attributable, and safe to reuse in research + education contexts. 🌾🗺️✨
