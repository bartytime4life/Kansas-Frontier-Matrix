# 🗿 `models-3d/artifacts` — 3D Artifact Packages (Web)

![KFM](https://img.shields.io/badge/KFM-living%20atlas-2b7cff)
![Provenance](https://img.shields.io/badge/provenance-first-success)
![Contract](https://img.shields.io/badge/metadata-contract--first-informational)
![3D](https://img.shields.io/badge/3D-web%20ready-6f42c1)

Welcome to the **3D artifact** shelf for Kansas Frontier Matrix (KFM). This folder is for **web-ready 3D assets** (scans, reconstructions, interpretive models) that can be rendered in the UI and linked to the knowledge graph as *inspectable evidence*—not “mystery geometry.” KFM’s mission is to make Kansas’s spatial truth **searchable, mappable, auditable, and modelable**, and the same trust rules apply to 3D content.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✨ Core Principle (Non‑Negotiable)
### ✅ “No mystery layers” — even in 3D
Anything that appears in the UI must be traceable to sources and processing steps; citations + metadata are first-class.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
KFM enforces **contract-first + provenance-first** ingestion: metadata is required, and unsourced content is not allowed into the official catalog (“no mystery layers”).  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📦 What lives here?
This directory stores **artifact packages**: a model + preview media + metadata contracts + provenance.

Think of each artifact as a *small, self-describing bundle* that the frontend can load directly and the backend can reference safely.

---

## 🗂️ Expected Folder Layout
```text
web/assets/media/models-3d/artifacts/
  📁 <artifact-slug>/
    🧊 model.glb
    🖼️ preview.webp
    🧾 manifest.json
    🧬 provenance.json
    ⚖️ LICENSE.txt
    🧵 attribution.md            (optional but recommended)
    📁 textures/                 (optional; prefer embedded where feasible)
    📁 source/                   (optional; raw scans / working files, if allowed)
```

### Naming rules 🧼
- Folder names: `kebab-case` (e.g., `fort-leavenworth-cannonball`)
- Avoid spaces, parentheses, and “final_final_v7” 😄
- Version via metadata, not filenames (e.g., `manifest.json.version`)

---

## 🧾 Metadata & Provenance (How KFM “trusts” 3D)
KFM uses open standards for lineage and interchange (e.g., STAC / DCAT / PROV-O) to capture origin + processing formally.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
Every dataset is expected to carry a **metadata JSON “data contract”** including source, license, spatial/temporal extent, and processing steps.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

> **Rule of thumb:** if a future-you can’t answer “where did this come from and what did we do to it?” from the files in the package… it’s not ready to ship 🚫.

---

## ✅ Required Files (Minimum Viable Asset)
### 1) `model.glb`
- Preferred delivery format: **glTF 2.0 binary (`.glb`)** for web portability.
- Keep units consistent (meters recommended) and apply transforms before export.

### 2) `preview.webp`
- Used for galleries, search results, and quick UI loading.

### 3) `manifest.json`
“Frontend contract” for rendering and discovery.

**Example:**
```json
{
  "id": "fort-leavenworth-cannonball",
  "title": "Fort Leavenworth Cannonball (Scan)",
  "type": "artifact",
  "version": "1.0.0",
  "files": {
    "model": "model.glb",
    "preview": "preview.webp"
  },
  "tags": ["fort-leavenworth", "material-culture", "scan"],
  "renderHints": {
    "environment": "museum",
    "initialCamera": { "yaw": 20, "pitch": -15, "distance": 2.2 }
  },
  "spatial": {
    "units": "meters",
    "georeferencing": "none",
    "notes": "Object-space scan; linked to place via knowledge graph."
  }
}
```

### 4) `provenance.json`
“Evidence contract” for traceability (sources + transformations).  
This mirrors KFM’s provenance expectations where outputs can always be backed by cited sources.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Example:**
```json
{
  "entity": {
    "id": "fort-leavenworth-cannonball",
    "kind": "3d-model",
    "created": "2026-01-18"
  },
  "derivedFrom": [
    {
      "type": "photogrammetry",
      "source": "Field photo set (DSLR)",
      "sourceId": "kfm:source:photoset:12345",
      "license": "CC BY 4.0",
      "notes": "Original images captured on-site; see source catalog entry."
    }
  ],
  "processing": [
    { "step": "alignment", "tool": "Metashape", "version": "x.y", "notes": "Aligned + dense cloud" },
    { "step": "mesh_cleanup", "tool": "Blender", "version": "x.y", "notes": "Decimate + normals" },
    { "step": "export", "tool": "Blender", "notes": "Exported glTF 2.0 (.glb)" }
  ],
  "attribution": [
    { "name": "Contributor / Lab / Archive", "role": "creator" }
  ]
}
```

### 5) `LICENSE.txt`
KFM is intentionally strict about licensing to avoid downstream conflicts and keep collaboration safe.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🌍 Spatial Referencing (When applicable)
Some 3D assets are **georeferenced** (terrain meshes, site models, building shells). Others are **object-space** (museum artifacts).

3D workflows often include **scaling + georeferencing**, then exporting to a model format for GIS/web integration.  [oai_citation:8‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
Modern GIS workflows can import high-resolution 3D models into a georeferenced space.  [oai_citation:9‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

**Recommendation:**
- If **object-space**, store geospatial context in the **knowledge graph link** (place ↔ artifact) rather than baking global coordinates into the mesh.
- If **geo-space**, include a `spatial` block in `manifest.json` (CRS/anchor/bounds) and document the transform in `provenance.json`.

---

## 🧪 Validation Checklist (PR Gate Mental Model)
Before adding/merging an artifact package:

- [ ] Has `manifest.json` (loadable + correct relative paths)
- [ ] Has `provenance.json` with sources + processing steps (no black box)  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Has an explicit license (`LICENSE.txt`)  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] `preview.webp` present and representative
- [ ] Model loads in a standard glTF viewer (no missing textures)
- [ ] File sizes are reasonable for web (consider LODs if needed)

---

## 🧰 Suggested Pipeline (Scan → Web → KFM)
KFM’s ingestion philosophy is to normalize assets into standard formats with consistent spatial reference + metadata for traceability.  [oai_citation:12‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

A practical 3D content flow looks like:

1. 📸 **Capture / Acquire**
   - Photogrammetry produces accurate textured models and dense point clouds from photos, then can be scaled/georeferenced.  [oai_citation:13‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

2. 🧼 **Clean & Optimize**
   - Fix normals, remove noise, simplify mesh, bake textures.

3. 📦 **Export Web Asset**
   - Export **`.glb`** + generate `preview.webp`.

4. 🧾 **Attach Trust**
   - Fill `manifest.json`, `provenance.json`, and `LICENSE.txt`.

5. 🔗 **Link Into KFM**
   - Connect the artifact to Places/Events/Documents in the knowledge graph (so a user can move from *thing* → *where/when/why*). KFM’s knowledge graph is designed to interlink entities (places, events, documents, datasets) into an interconnected knowledge base.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🕸️ Why web packaging matters (3D as collaborative evidence)
3D Web GIS platforms enable storing/managing/displaying/analyzing 3D spatial info through the web, widening access and collaboration.  [oai_citation:15‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
This directory exists so the frontend can treat 3D artifacts as **first-class, queryable media**—with the same transparency expectations as map layers and datasets.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧩 FAQ
**Q: Can I drop a random `.fbx` here?**  
A: Please don’t. Convert to `.glb`, include preview + manifest + provenance + license.

**Q: Where do I put “raw scan stuff”?**  
A: If licensing allows, put it under `source/` inside the asset folder (or keep it in an archival bucket and reference it from `provenance.json`).

**Q: Do we need georeferencing for artifacts?**  
A: Not always. Many artifacts are object-space; link them to places/events via KFM entities instead. For site-scale models, georeferencing is recommended and should be documented in provenance.  [oai_citation:17‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

---

## ✅ TL;DR
A good artifact package is:
> **Renderable** 🧊 + **Previewable** 🖼️ + **Citable** 📚 + **Licensed** ⚖️ + **Auditable** 🔍  
…and therefore worthy of KFM’s “living atlas” promise.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
