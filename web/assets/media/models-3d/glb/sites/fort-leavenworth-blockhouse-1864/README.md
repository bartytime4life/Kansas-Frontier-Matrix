<!--
📍 Path: web/assets/media/models-3d/glb/sites/fort-leavenworth-blockhouse-1864/README.md
-->

# 🏰 Fort Leavenworth Blockhouse (1864) — 3D Site Model (GLB)

**Asset ID (stable slug):** `fort-leavenworth-blockhouse-1864`  
**Status:** 🚧 *Contract-first stub — fill metadata + sources before “official catalog” use.*

**Tags:** `glTF2` `GLB` `3D` `Site` `KFM` `Provenance-First`

---

<details>
<summary>🧭 Contents</summary>

- 📦 Folder layout
- 👀 Preview
- 🧾 Provenance & data contract
- 🗺️ Georeferencing & placement
- 🧩 Using the model in the web app
- ✅ Validation & performance gates
- 🪪 License & attribution
- 🧷 References

</details>

---

## 📦 Folder layout

> [!TIP]
> Keep this folder name as the stable identifier. Renames break references, caches, and provenance chains.

```text
🌐 web/
└── 🧱 assets/
    └── 🎞️ media/
        └── 🧊 models-3d/
            └── 📦 glb/
                └── 🗺️ sites/
                    └── 🏰 fort-leavenworth-blockhouse-1864/
                        ├── README.md
                        ├── model.glb                # ✅ primary GLB (recommended name)
                        ├── preview.webp             # 🖼️ thumbnail / poster frame (optional but recommended)
                        ├── metadata.json            # ✅ REQUIRED “data contract” (provenance + schema)
                        └── sources/                 # ✅ REQUIRED for provenance-first workflows
                            ├── citations.md          # human-readable citations (recommended)
                            └── ...                   # scans, photosets, references, etc.
```

> [!IMPORTANT]
> In KFM, anything that appears in the UI should be traceable via required metadata (a “data contract”), including **source, license, spatial/temporal extent, and processing steps**, enforced via validators/CI—no “mystery layers.” [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 👀 Preview

> Add a `preview.webp` (or `preview.png`) for quick browsing in UIs and PRs.

```md
![Preview](preview.webp)
```

*(If preview isn’t available yet, leave the file out and keep this section as-is.)*

---

## 🧾 Provenance & data contract

KFM’s design is **contract-first** + **provenance-first**: assets should be self-describing, auditable, and attributable via metadata and processing traces. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Required: `metadata.json` (template)

> [!NOTE]
> The goal is to support provenance + reuse: clearly document **what this model represents**, **how it was created**, and **what it can (and cannot) be used for**. This mirrors cultural heritage best practice where interpretive vs. reality-based models must be distinguished and accompanied by transparent reporting. [oai_citation:3‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2) [oai_citation:4‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

```json
{
  "id": "fort-leavenworth-blockhouse-1864",
  "type": "3d_model",
  "title": "Fort Leavenworth Blockhouse (1864)",
  "description": "3D model for KFM site visualization. Fill in whether this is a reality-based capture or an interpretive reconstruction, plus scope/limits.",
  "model": {
    "format": "glb",
    "units": "meters",
    "upAxis": "Y",
    "georeference": {
      "crs": "EPSG:4326",
      "anchor": {
        "lat": null,
        "lon": null,
        "elevation_m": null
      },
      "heading_deg": null,
      "scale": 1.0,
      "notes": "Describe how the model is aligned (e.g., doorway faces east) and what point is used as the anchor."
    },
    "stats": {
      "triangles": null,
      "materials": null,
      "textures": []
    },
    "files": {
      "glb": "model.glb",
      "preview": "preview.webp"
    },
    "checksums": {
      "sha256": {
        "model.glb": "TODO",
        "preview.webp": "TODO"
      }
    }
  },
  "temporal": {
    "subject_year": 1864,
    "subject_year_confidence": "TBD",
    "notes": "If the year is approximate or refers to a historical phase, document rationale + sources."
  },
  "provenance": {
    "model_kind": "TBD (reality-based | interpretive | hybrid)",
    "sources": [
      {
        "type": "photo_set | lidar | drawings | archival_photos | other",
        "title": "TODO",
        "creator": "TODO",
        "date": "TODO",
        "license": "TODO",
        "citation": "TODO (human-readable citation text)"
      }
    ],
    "processing": [
      {
        "step": 1,
        "tool": "TODO (e.g., Metashape/RealityCapture/Blender)",
        "version": "TODO",
        "input": "TODO",
        "output": "TODO",
        "notes": "Key settings (alignment, decimation target, texture baking, etc.)"
      }
    ]
  },
  "license": {
    "spdx": "TBD",
    "attribution": "TBD",
    "notes": "List all required credits (photography, scans, archives, modeler, etc.)."
  },
  "created": "YYYY-MM-DD",
  "updated": "YYYY-MM-DD"
}
```

### 🧠 Optional but recommended (KFM-aligned)

- **Publishable metadata formats:** If/when promoted into the formal catalog, consider emitting/deriving a **STAC Item** (spatial asset) plus provenance links (e.g., PROV-O), since KFM’s architecture calls out open standards for spatial assets/datasets/provenance. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Human-readable `sources/citations.md`:** One place for full citations + archive identifiers, plus a short “what changed” log.

---

## 🗺️ Georeferencing & placement

> [!IMPORTANT]
> Decide whether this model is:
> - **Reality-based** (photogrammetry / LiDAR capture), or
> - **Interpretive reconstruction** (hypothesis-driven),
> and document it explicitly. Both model types require transparency to remain trustworthy and reusable. [oai_citation:6‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2) [oai_citation:7‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

### Recommended georeference workflow (high-level)

If the model is meant to be placed in georeferenced 3D space, capture and store:

- **Anchor point** (lat/lon/elevation) + **heading** + **scale**
- **How alignment was achieved** (GCPs, surveyed points, reference geometry)

Field-oriented 3D GIS workflows often rely on measured control (e.g., RTK GPS + GCPs) to georeference 3D models and maintain spatial coherence across datasets. [oai_citation:8‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

---

## 🧩 Using the model in the web app

### Web asset path

```text
/assets/media/models-3d/glb/sites/fort-leavenworth-blockhouse-1864/model.glb
```

### Example loader snippet (Three.js)

```js
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

const loader = new GLTFLoader();
loader.load(
  "/assets/media/models-3d/glb/sites/fort-leavenworth-blockhouse-1864/model.glb",
  (gltf) => {
    const obj = gltf.scene;
    // Optional: obj.scale.setScalar(1);
    // Optional: obj.rotation.y = ...;
    scene.add(obj);
  }
);
```

> [!TIP]
> If you apply transforms (scale/rotation/offset), record them in `metadata.json → model.georeference` so the placement is auditable and reproducible.

---

## ✅ Validation & performance gates

### Validation (recommended)

- ✅ GLB loads in at least 2 viewers (e.g., your web viewer + Blender)
- ✅ No missing textures / broken materials
- ✅ Correct scale (human-scale sanity check)
- ✅ Normals look correct (no inverted faces)
- ✅ Pivot/origin strategy documented (anchor + heading)

### Performance budgets (recommended defaults)

- 🎯 **Triangles:** keep within your target device budget (mobile vs desktop)
- 🎯 **Textures:** avoid unnecessarily huge textures; prefer power-of-two sizes
- 🎯 **Materials:** minimize material count where possible

> [!NOTE]
> If you create LOD variants, use a consistent naming scheme and list them under `metadata.json → model.files`.

---

## 🪪 License & attribution

> [!IMPORTANT]
> Do not publish this asset into any “official” KFM catalog until licensing is explicit and compatible with intended use. KFM’s trust model expects clear provenance + attribution-ready metadata. [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Fill in:

- **License (SPDX):** `TBD`
- **Required attribution text:** `TBD`
- **Source archives / creators:** `TBD`

---

## 🧷 References

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation (project architecture + provenance rules)  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Archaeological 3D GIS (3D model transparency + interpretive vs reality-based distinction)  [oai_citation:12‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  [oai_citation:13‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
