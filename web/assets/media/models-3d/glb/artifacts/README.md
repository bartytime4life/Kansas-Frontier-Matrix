# 🗿 Artifacts (3D Models) — `.glb` (glTF 2.0)

![format](https://img.shields.io/badge/format-GLB%20%28glTF%202.0%29-blue)
![web](https://img.shields.io/badge/target-web%20streaming-2ea44f)
![provenance](https://img.shields.io/badge/principle-provenance--first-7b3fe4)
![contract](https://img.shields.io/badge/principle-contract--first-ff8c00)
![status](https://img.shields.io/badge/folder-public%20asset%20directory-555)

> 📍 **Path:** `web/assets/media/models-3d/glb/artifacts/`  
> 🧠 **Purpose:** Web-ready **3D artifact models** for the KFM UI (fast to load, easy to cite, hard to “mystery-drop” into the app).

---

## ✨ What lives here?

This directory contains **production** 3D artifacts in **binary glTF** (`.glb`) format, plus the minimal supporting files needed for:

- 🧊 **Rendering** in the web client (GLB)
- 🖼️ **Previewing** in galleries (thumbnail / preview)
- 🧾 **Auditing** (metadata “data contract” + provenance + license)
- 🔗 **Linking** to the larger KFM knowledge graph / map layers / story nodes

> [!IMPORTANT]
> This is a **public** web asset folder. Don’t put raw scans, field notes, or anything sensitive here.
> Keep heavy source data and private context in the governed data/pipeline areas — ship *only* what the browser needs.

---

## 📦 Directory layout

### ✅ Recommended (per-artifact folder)

```text
📦 artifacts/
 ┣ 📁 <artifact-id>/
 ┃ ┣ 🧊 <artifact-id>.glb
 ┃ ┣ 🖼️ <artifact-id>.preview.webp
 ┃ ┣ 🧾 <artifact-id>.meta.json
 ┃ ┗ 📁 sources/
 ┃    ┗ 🔗 citations.md  (optional: human-readable bibliography)
 ┗ 📄 README.md
```

### Alternative (flat layout)

Use only if you **don’t** need per-asset previews or sidecars:

```text
📦 artifacts/
 ┣ 🧊 <artifact-id>.glb
 ┣ 🧾 <artifact-id>.meta.json
 ┣ 🖼️ <artifact-id>.preview.webp
 ┗ 📄 README.md
```

> [!TIP]
> If you’re unsure, start with the **per-artifact folder**. You’ll want it the moment you add previews, LODs, multiple derivatives, or richer provenance notes.

---

## 🏷️ Naming & versioning rules

### Artifact IDs (stable, never reused)
- ✅ `kebab-case`
- ✅ stable across renames
- ✅ **no spaces**
- ✅ no “final”, “new”, “fixed2”

**Examples**
- `arrowhead-flint-0012`
- `ceramic-shard-rim-0047`

### Files (deterministic)
Inside each artifact folder, use:

- `/<artifact-id>/<artifact-id>.glb`
- `/<artifact-id>/<artifact-id>.meta.json`
- `/<artifact-id>/<artifact-id>.preview.webp`

### Versions
Prefer **git history** + **metadata fields** (below) over filename version spam.

If you *must* version filenames (e.g., experimental parallel models), use:

- `<artifact-id>__v001.glb`
- `<artifact-id>__v002.glb`

…and keep `<artifact-id>.glb` as the “current” symlink/alias **only if your build system supports it**.

---

## 🧾 Required metadata (data contract)

Each artifact MUST ship with a sidecar JSON file:

`<artifact-id>.meta.json`

This is the **contract-first** guardrail that prevents “mystery assets” and enables auto-attribution.

### Minimum required fields

```text
id, title, summary, license, sources[], creators[], created_at,
provenance.processing_steps[], geometry.metrics, sensitivity
```

> [!NOTE]
> Your metadata is treated as a **first-class product** — not an afterthought.
> If we can’t explain *where the model came from* and *how it was produced*, it doesn’t ship.

### Example: `<artifact-id>.meta.json`

```json
{
  "id": "arrowhead-flint-0012",
  "title": "Flint Arrowhead (Type A)",
  "summary": "Reality-based mesh of a flint arrowhead. Optimized for web viewing and educational storytelling.",
  "tags": ["artifact", "lithic", "arrowhead"],
  "created_at": "2026-01-18",
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Example Institution / Collection",
    "notes": "Verify rights for redistribution + derivative works."
  },
  "creators": [
    {
      "name": "KFM Team",
      "role": "processing",
      "contact": "docs/contacts.md#kfm-team"
    }
  ],
  "sources": [
    {
      "type": "photogrammetry",
      "citation": "Field capture campaign (YYYY-MM-DD), camera + lens details, operator, collection ID.",
      "source_uri": "internal://kfm/archive/captures/arrowhead-flint-0012/",
      "access": "restricted"
    }
  ],
  "provenance": {
    "method": "image-based 3D modeling",
    "processing_steps": [
      "Aligned images + generated dense cloud",
      "Reconstructed mesh",
      "Cleaned mesh (holes, non-manifold edges)",
      "Decimated for web budget",
      "Baked textures",
      "Exported GLB (PBR, embedded textures)"
    ],
    "tools": [
      { "name": "Metashape", "version": "x.y" },
      { "name": "Blender", "version": "x.y" }
    ]
  },
  "geometry": {
    "units": "m",
    "orientation_hint": "upright, centered; pivot at base center",
    "metrics": {
      "triangles": 64210,
      "materials": 1,
      "textures": [
        { "type": "baseColor", "resolution": "2048x2048", "format": "jpg" }
      ],
      "glb_size_bytes": 4821930
    },
    "bounds": {
      "approx_size_m": { "x": 0.06, "y": 0.02, "z": 0.01 }
    }
  },
  "context": {
    "collection": "Kansas Frontier Matrix",
    "related_story_ids": ["story-lithics-overview"],
    "related_dataset_ids": ["catalog:artifacts:arrowheads"]
  },
  "sensitivity": {
    "level": "public",
    "notes": "No precise site coordinates embedded in public metadata."
  }
}
```

---

## 🔐 Sensitivity & cultural safety

Some artifact records can be sensitive (e.g., looting risk, sacred context, living community governance). Treat sensitivity as **part of the data contract**, not a UI feature.

**Rules**
- 🚫 Do **not** include exact find-site coordinates in public web metadata unless explicitly approved.
- 🧭 If location is needed, use **generalized** areas (region/county/hex grid) and note the policy in metadata.
- 🤝 If the artifact relates to Indigenous communities, ensure **Authority to Control** is respected and permissions are documented in the metadata notes.

> [!IMPORTANT]
> If you’re not sure whether something is sensitive: assume it is, mark it as restricted, and route through governance.

---

## 🧪 Definition of Done (DoD) for a new GLB artifact ✅

- [ ] 🧾 **Metadata contract complete** (`<artifact-id>.meta.json`)
- [ ] 🔗 **All claims trace to sources** (citations / collection IDs / capture notes)
- [ ] 🔁 **Processing steps are repeatable** (tools + versions + step list)
- [ ] ⚖️ **License verified** (SPDX ID + attribution text + any restrictions)
- [ ] 🔐 **Sensitivity assessed** (and generalized/redacted where needed)
- [ ] 📦 **Performance budgets met** (below)
- [ ] 🖼️ **Preview added** (`.webp`) and looks correct in UI
- [ ] ✅ Loads in the web viewer without missing textures/material warnings

---

## ⚡ Performance budgets (web-first)

These are **targets**, not commandments — but they’ll keep the site snappy:

### Default targets (good on mid-range mobile)
- **GLB size:** ≤ **8 MB**
- **Triangles:** ≤ **100k**
- **Textures:** 1–2 maps, ≤ **2K**
- **Materials:** 1–3

### If you exceed targets
Add justification in metadata under:

- `geometry.metrics.*`
- `provenance.processing_steps[]`
- `sensitivity.notes` (if constraints forced the choice)

> [!TIP]
> If you need extreme fidelity, consider shipping **multiple LODs** (and let the viewer pick), or splitting the artifact into logical components.

---

## 🔁 Suggested optimization pipeline (repeatable)

A practical “scan → ship” workflow:

1. 📸 **Capture**
   - Photogrammetry set or scan
2. 🧹 **Clean**
   - Remove background, fill holes, fix non-manifold edges
3. 🧬 **Simplify**
   - Decimate mesh for web budgets (preserve silhouette)
4. 🎨 **Bake**
   - Bake normals / AO if needed, consolidate materials
5. 🧊 **Export**
   - Export to **glTF 2.0 / GLB**, embed textures
6. 🗜️ **Compress**
   - Prefer modern texture compression (KTX2/Basis) when supported
   - Consider mesh compression (meshopt / Draco) depending on viewer tooling
7. ✅ **Validate**
   - Open locally in your target viewer
   - Confirm scale, pivot, material correctness
8. 🧾 **Document**
   - Fill metadata contract, including tool versions + processing steps

---

## 🧩 Linking artifacts to the rest of KFM

Artifacts become most valuable when they connect to:

- 🗺️ **Map layers** (where appropriate)
- 🧠 **Knowledge graph entities** (people, events, places, periods)
- 📚 **Story nodes** (narratives, exhibits, lessons)

**Recommended metadata link fields**
- `context.related_story_ids[]`
- `context.related_dataset_ids[]`
- (Optional) `context.knowledge_graph_refs[]` (IDs/URIs)

> [!NOTE]
> Keep “truth” about provenance in **metadata**, not hardcoded in the UI.
> The UI should *display* provenance, not *invent* it.

---

## 🖥️ Using an artifact in the web app

### URL convention (static asset)
When using the recommended folder layout:

```text
/assets/media/models-3d/glb/artifacts/<artifact-id>/<artifact-id>.glb
```

### Metadata lookup
```text
/assets/media/models-3d/glb/artifacts/<artifact-id>/<artifact-id>.meta.json
```

### Minimal embed example (viewer-agnostic)
```js
const artifactId = "arrowhead-flint-0012";
const modelUrl = `/assets/media/models-3d/glb/artifacts/${artifactId}/${artifactId}.glb`;
const metaUrl  = `/assets/media/models-3d/glb/artifacts/${artifactId}/${artifactId}.meta.json`;
```

> [!TIP]
> Treat GLB loading as “network content”: cache aggressively, preload previews first, and consider lazy-loading the heavy model until the user asks to view it.

---

## 🧯 Troubleshooting

<details>
  <summary><strong>Model looks huge / tiny</strong></summary>

- Confirm `geometry.units` in metadata.
- Ensure you didn’t export in centimeters while assuming meters.
- Prefer “baked transforms” (scale = 1) in the exported GLB.

</details>

<details>
  <summary><strong>Black / missing textures</strong></summary>

- Ensure textures are embedded (or correctly referenced if external).
- Confirm PBR maps are assigned correctly (baseColor vs metallicRoughness, etc.).
- Verify color space assumptions (sRGB vs linear) in your viewer.

</details>

<details>
  <summary><strong>GLB is too big</strong></summary>

- Reduce texture resolution first (often the biggest win).
- Decimate mesh with silhouette preservation.
- Consolidate materials and remove unused vertex attributes.

</details>

---

## 🤝 Contributing

1. Add the artifact folder + files
2. Ensure the metadata contract is complete
3. Validate that it loads + performs well
4. Open a PR with:
   - before/after size + triangle counts
   - screenshot/preview
   - citation + license notes

---

## 📚 Project context

This artifact pipeline follows the broader KFM approach: **contract-first**, **provenance-first**, and **human-centered transparency** — so that models are usable for research, education, and storytelling without becoming black-box media blobs.
