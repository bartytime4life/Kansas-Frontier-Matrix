# 🧩 UI 3D Models — `web/assets/media/models-3d/ui/`

![scope](https://img.shields.io/badge/scope-UI%203D%20assets-6f42c1)
![format](https://img.shields.io/badge/format-glTF%202.0%20%7C%20.glb-1f6feb)
![runtime](https://img.shields.io/badge/runtime-WebGL%20%7C%20Cesium%20%7C%20Browser-238636)
![policy](https://img.shields.io/badge/policy-provenance--first-critical-d73a49)

> [!NOTE]
> This folder is **only** for **small, reusable 3D assets that are part of the web UI** (gizmos, 3D icons, markers, mini widgets).  
> Large geospatial 3D content belongs in the **streaming geospatial pipeline** (e.g., 3D Tiles) — not here.

---

## 🎯 What goes in this folder?

✅ **Fits here (UI-scale 3D):**
- 🧭 Orientation widgets (compass ring, north arrow, axis gizmo)
- 📍 3D pins/markers used in UI overlays
- 🧰 Tool “gizmos” (selection handles, rulers, measurement widgets)
- 🧊 Small decorative/demo models used in **Story Nodes** or UI tutorials (when *lightweight*)

❌ **Does *not* fit here:**
- 🏔️ Terrain, LiDAR point clouds, city/building sets, “scene” content
- 🧱 Anything that should be **streamed/LOD’d** as geospatial 3D (use Cesium/3D Tiles pipeline)
- 🗃️ Raw scans / high-poly “source of truth” meshes (keep those in a source bucket, not UI runtime assets)

---

## 📁 Suggested folder layout

> [!TIP]
> Keep runtime assets **flat and predictable**. Add subfolders only when the set grows.

```text
web/assets/media/models-3d/ui/
├─ README.md
├─ _sources/                # 🧪 optional: .blend, high-poly, bake files (NOT referenced by runtime)
├─ gizmos/                  # 🧭 orientation + manipulation widgets
├─ markers/                 # 📍 pins, beacons, “selected” markers
├─ icons/                   # 🧊 3D iconography (low-poly, tiny textures)
└─ components/              # 🧩 composed UI models (multi-part)
```

---

## 🧱 Supported formats

### ✅ Preferred
- **`.glb` (glTF 2.0 binary)** — best for web delivery + loaders

### ⚠️ Allowed (sparingly)
- `.gltf` + `.bin` + external textures (only if required)
- Textures: `.ktx2` (preferred), `.png`, `.jpg`

### 🚫 Avoid
- `.fbx`, `.obj` (runtime) — keep as **source artifacts** only (in `_sources/`), if at all

---

## 🧾 Provenance-first rule (non‑negotiable) 🧬

> [!IMPORTANT]
> **Anything that shows up in the UI must be traceable.**  
> Every model in this folder must have **a sidecar metadata file** describing **source + license + processing**.

### 📄 Sidecar metadata file
For each model:
- `model-name.glb`
- `model-name.meta.json`

✅ Example:
- `compass-ring.glb`
- `compass-ring.meta.json`

<details>
  <summary><strong>📦 Minimal <code>.meta.json</code> template (copy/paste)</strong></summary>

```json
{
  "id": "ui/compass-ring",
  "name": "Compass Ring",
  "type": "ui-model",
  "description": "UI compass ring used in 3D orientation overlay.",
  "version": "1.0.0",

  "source": {
    "origin": "original | derived | third-party",
    "author": "YOUR_NAME_OR_TEAM",
    "source_url": "https://example.com/original/source",
    "license": "CC-BY-4.0 | CC0-1.0 | MIT | Proprietary",
    "attribution": "If required by license, put attribution text here."
  },

  "created": {
    "created_at": "YYYY-MM-DD",
    "tools": ["Blender 4.x", "gltf-transform", "ktx2"],
    "pipeline_notes": "Short human-readable description of edits + compression."
  },

  "runtime": {
    "units": "meters",
    "up_axis": "Y",
    "forward_axis": "Z",
    "intended_use": ["ui-overlay", "marker", "story-demo"],
    "budgets": {
      "triangles_max": 5000,
      "textures_max": 2,
      "max_texture_resolution": 1024
    }
  },

  "integrity": {
    "sha256": "OPTIONAL_BUT_RECOMMENDED",
    "notes": "Optional: how to reproduce/export."
  }
}
```
</details>

---

## 📐 Modeling standards (so assets behave predictably)

### 🧭 Orientation & axes
- **Up axis:** `+Y`  
- **Forward:** `+Z`  
- **Right:** `+X`

### 📏 Units & scale
- **1 unit = 1 meter** (glTF convention-friendly)
- UI models should be authored at **realistic scale** (so they can be reused in Cesium/3D contexts without “mystery scaling”)

### 🎯 Pivot/origin rules
- Put the pivot at the **interaction point**:
  - markers: pivot at **base-center**
  - gizmos: pivot at **center**
  - tool handles: pivot at **grab point**

---

## ⚡ Performance budgets (UI models)

> [!NOTE]
> Budgets are guidelines. If you exceed them, document why in `*.meta.json`.

| Asset type 🧩 | Triangle budget 🔻 | Textures 🖼️ | Max texture size 📐 | Target compressed size 📦 |
|---|---:|---:|---:|---:|
| 3D icon | ≤ 1,000 | ≤ 1 | 512² | ≤ 150 KB |
| Marker / pin | ≤ 3,000 | ≤ 2 | 1024² | ≤ 300 KB |
| Gizmo / widget | ≤ 5,000 | ≤ 2 | 1024² | ≤ 500 KB |
| “Special” UI model | ≤ 10,000 | ≤ 3 | 1024² | justify in meta |

**Default goals:**
- Prefer **single material** where possible
- Prefer **baked** shading over expensive geometry
- Use **compressed textures** (`.ktx2`) when possible

---

## 🛠️ Recommended export + optimization workflow

1) 🧱 **Author** in Blender (or preferred DCC)
2) 🎁 **Export** as **glTF 2.0 `.glb`**
3) 🧼 **Optimize**
   - remove unused nodes/materials
   - merge meshes if it reduces draw calls (without harming reuse)
   - simplify geometry if over budget
4) 🗜️ **Compress**
   - geometry compression where appropriate
   - texture compression (KTX2/Basis) where supported
5) ✅ **Validate**
   - loads with no warnings in your viewer
   - no missing textures
   - no external URL dependencies inside the glTF
6) 🧾 **Add `.meta.json`** and confirm license/attribution

---

## 🧪 Definition of Done (DoD) ✅

Before merging a UI model:

- [ ] ✅ Model is `.glb` (or documented exception)
- [ ] ✅ `*.meta.json` exists and includes **source + license**
- [ ] ✅ Pivot/origin correct (see 📐 Modeling standards)
- [ ] ✅ Triangle + texture budgets met (or justified)
- [ ] ✅ No external references (everything local)
- [ ] ✅ Tested in the target viewer(s) (2D/3D UI paths)
- [ ] ✅ If animated: respects reduced-motion UX (see ♿ below)

---

## ♿ Accessibility & UX guardrails

- Prefer **static** UI models unless animation adds real clarity
- If animated:
  - support a **reduced motion** mode (or keep animation subtle)
  - avoid rapid flashing / high-frequency motion

> [!TIP]
> Always provide a **2D fallback icon** for critical controls.

---

## 🔌 Usage notes (implementation-agnostic)

### 🧠 Loading strategy
- UI models should be **lazy-loaded** (only when needed)
- Cache models where reuse is common (gizmos/markers)
- Avoid blocking initial map render (load after map is interactive)

### 📍 Pathing convention
When referencing these assets in code, prefer **absolute-from-web-root** style paths (as your build system allows), e.g.:

```txt
/assets/media/models-3d/ui/gizmos/compass-ring.glb
```

---

## 🔒 Security & supply-chain basics

- Only accept assets from sources with **clear licensing**
- Don’t commit unreviewed third-party binaries
- Prefer a reproducible path: `_sources/` → export → optimize → validate → commit

---

## 🧭 “Where should I put this model?” decision helper

- **Is it part of UI chrome (small + reused)?** → ✅ `ui/`
- **Is it tied to a real place and needs streaming/LOD?** → 🚀 geospatial 3D pipeline (3D Tiles)
- **Is it a raw scan/high-poly master?** → 🧪 `_sources/` (or external source bucket), export only the optimized runtime model here

---

## ✨ Contribution vibe

This repo is a **living atlas** 🗺️ — UI assets should:
- be lightweight ⚡
- be trustworthy 🧾
- be reusable 🧩
- never become “mystery content” 🕵️‍♂️

💡 If in doubt: **document more, ship less.**
