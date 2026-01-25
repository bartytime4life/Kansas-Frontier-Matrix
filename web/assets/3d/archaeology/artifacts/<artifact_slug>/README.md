<!-- According to a document from 2026-01-25, KFM treats “evidence artifacts” (including 3D models) as governed, provenance-first outputs that must be cataloged (STAC/DCAT/PROV) and policy-gated before they appear in the UI. -->

---
title: "🗿 Archaeology Artifact Pack — <artifact_slug>"
path: "web/assets/3d/archaeology/artifacts/<artifact_slug>/README.md"
version: "0.1.0"
last_updated: "2026-01-25"
status: "draft"
kfm:
  domain: archaeology
  entity_kind: artifact
  artifact_slug: "<artifact_slug>"
  artifact_id: "kfm:archaeology:artifact:<artifact_slug>"
  classification: "public|internal|restricted|embargoed"
  sensitivity:
    looting_risk: "low|medium|high"
    coordinates: "public|generalized|hidden"
    notes: ""
  evidence_triplet:
    stac_item: "data/stac/items/archaeology/artifacts/<artifact_slug>.json"
    dcat_dataset: "data/catalog/dcat/archaeology/artifacts/<artifact_slug>.jsonld"
    prov_bundle: "data/prov/archaeology/artifacts/<artifact_slug>.jsonld"
  ui:
    default_viewer: "cesium|threejs"
    default_camera: {}
---

# 🗿 Archaeology Artifact Pack — `<artifact_slug>`

![Status](https://img.shields.io/badge/status-draft-orange)
![Domain](https://img.shields.io/badge/domain-archaeology-7b3f00)
![3D](https://img.shields.io/badge/3D-glTF%2FGLB-0ea5e9)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE-3b82f6)
![Evidence](https://img.shields.io/badge/evidence-STAC%2FDCAT%2FPROV-10b981)

> [!IMPORTANT]
> This folder is **runtime web content**. If the artifact (or its exact findspot) is **restricted/sensitive**, **do not ship the 3D model here**. Keep the asset in governed storage and expose it through the API (e.g., signed URLs / access checks) instead.

---

## 👀 Quick preview

> Replace `thumbnail.webp` with your real preview image (or remove this section).

![Artifact preview](./thumbnail.webp)

---

## 🧾 Artifact at-a-glance

| Field | Value (fill in) |
|---|---|
| Display name | `TBD` |
| Short description | `TBD (1–2 sentences)` |
| Time/period | `TBD` |
| Culture/community | `TBD (use CARE-aware language)` |
| Material(s) | `TBD` |
| Dimensions | `TBD (units)` |
| Current repository / holding institution | `TBD` |
| Accession / catalog # | `TBD` |
| Classification | `public / internal / restricted / embargoed` |
| Location handling | `public / generalized / hidden` |
| Looting risk | `low / medium / high` |
| License | `TBD` |
| Primary citation(s) | `TBD` |

---

## 📦 What belongs in this folder

This directory lives at:

`web/assets/3d/archaeology/artifacts/<artifact_slug>/`

It should contain **web-optimized** 3D assets + a lightweight manifest so the platform can:

- Render the model (3D viewer) 🧱
- Show provenance + licensing + citations 🧾
- Enforce governance (classification / redaction) 🔒
- Link the artifact to KFM’s catalogs/graph/story nodes 🕸️📚

---

## 🗂️ Recommended folder layout

```text
📁 <artifact_slug>/
├─ 🧾 README.md
├─ 🧩 artifact.manifest.json
├─ 🖼️ thumbnail.webp
├─ 🧭 annotations.geojson              # optional hotspots (labels, callouts)
├─ 🔏 checksums.sha256                  # required (tamper-evidence)
├─ 📜 LICENSE.txt                       # or CREDITS.md (required if license demands)
└─ 🧱 model/
   ├─ 🧊 model.glb                      # primary runtime model (recommended)
   ├─ 🧊 model_lod1.glb                 # optional LOD
   ├─ 🧊 model_lod2.glb                 # optional LOD
   └─ 🎨 textures/                      # optional if not embedded in GLB
```

> [!TIP]
> If your model is too large for Git, use **DVC** for “large rasters or model files” (pointer files in Git, binaries in remote storage) or distribute via OCI/ORAS (see below). ✅

---

## 🧩 `artifact.manifest.json` contract

This manifest is the **UI-friendly** metadata glue that points to:

- Local runtime assets in this folder (GLB, thumbnails)
- The evidence triplet (STAC / DCAT / PROV)
- Governance labels (classification, sensitivity)
- Optional UI hints (camera start pose, annotations)

<details>
<summary>🧱 Minimal JSON example (template)</summary>

```json
{
  "artifact_id": "kfm:archaeology:artifact:<artifact_slug>",
  "slug": "<artifact_slug>",
  "title": "TBD",
  "summary": "TBD",
  "classification": "public",
  "sensitivity": {
    "looting_risk": "medium",
    "coordinates": "generalized",
    "notes": "Exact findspot withheld; geometry generalized."
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "TBD (institution / author / lab)",
    "source_url": "TBD"
  },

  "provenance": {
    "stac_item": "data/stac/items/archaeology/artifacts/<artifact_slug>.json",
    "dcat_dataset": "data/catalog/dcat/archaeology/artifacts/<artifact_slug>.jsonld",
    "prov_bundle": "data/prov/archaeology/artifacts/<artifact_slug>.jsonld"
  },

  "links": {
    "related_sites": [],
    "related_collections": [],
    "related_story_nodes": []
  },

  "assets": [
    {
      "role": "primary-3d",
      "href": "./model/model.glb",
      "media_type": "model/gltf-binary",
      "sha256": "TBD",
      "bytes": 0
    },
    {
      "role": "thumbnail",
      "href": "./thumbnail.webp",
      "media_type": "image/webp",
      "sha256": "TBD",
      "bytes": 0
    }
  ],

  "ui": {
    "viewer": "cesium",
    "default_camera": {
      "heading": 0,
      "pitch": -25,
      "range_m": 2.5
    }
  }
}
```
</details>

> [!NOTE]
> The manifest is **not** a replacement for STAC/DCAT/PROV. It’s the thin “frontend adapter” that references them.

---

## 🧬 Evidence-first publishing

KFM treats **every published dataset/evidence artifact** as an “evidence triplet”:

- **STAC** (assets + spatiotemporal metadata)
- **DCAT** (catalog discoverability + distributions)
- **PROV** (lineage: raw inputs → transformations → outputs)

This folder should **point to** those records (and CI/policy should enforce they exist).  

---

## 🕸️ Knowledge graph + ontology mapping

When ingested, the artifact should be represented in the graph as **metadata + relationships**, not as bulky binaries. Recommended link targets:

- Places (generalized if sensitive)
- Periods / events
- People/agents (researchers, institutions, digitization workflows)
- Related datasets / story nodes

If you’re mapping “artifact semantics,” CIDOC-CRM-style roles are a good fit (e.g., “man-made object,” “production event,” “findspot”), and spatial relations can use GeoSPARQL-style predicates.

---

## 🔒 Governance, safety, and looting risk

> [!WARNING]
> **Precise artifact locations** (or sensitive site coordinates) can enable looting. If in doubt: **generalize, hide, or omit** exact coordinates — and mark the artifact as restricted/generalized.

Practical patterns:

- Store **generalized geometry** (e.g., a coarse area or hex cell) instead of a point
- Gate details behind access control (API-level)
- Ensure outputs are **never less restricted** than their inputs (fail-closed governance)

---

## 🧱 3D asset guidelines

### Recommended formats ✅

- **GLB** (`model/gltf-binary`) for single-file delivery (easy caching, fewer requests)
- **glTF + external textures** if you need shared textures across LODs
- **3D Tiles** when you need streaming or many objects (Cesium-friendly)

### Web performance checklist ⚡

- Target a **runtime-optimized** mesh (decimation where acceptable)
- Prefer compressed textures (e.g., Web-friendly formats), but keep a high-fidelity source elsewhere
- Provide **LODs** if the artifact is heavy
- Include `checksums.sha256` for all shipped files

---

## 🗺️ Viewer integration (Cesium vs Three.js)

### Cesium (3D globe / 3D Tiles) 🌍
Use when the artifact is contextualized in a geospatial scene (terrain, 3D map mode, site context).

### Three.js (local 3D view) 🧪
Use when you want a “specimen viewer” independent of map context.

A classic minimal Three.js setup uses a `WebGLRenderer`, attaches it to the DOM, and adds interactive controls (e.g., Trackball controls).  

---

## 🧭 Optional: annotations (hotspots)

If you include `annotations.geojson`, keep it **UI-only** and **non-sensitive** (no exact findspot leaks). Suggested structure:

- `Point` features in *model space* or *viewer space* (document which)
- Properties:
  - `label`
  - `description`
  - `severity` (info/warn)
  - `media` (optional image/audio link via API)

---

## 📦 Distribution options for large models

Choose the smallest option that satisfies governance + performance:

1. **Git-tracked** (small public models) ✅  
2. **DVC-tracked** (large models) 🧳  
3. **OCI/ORAS + Cosign** (content-addressable, signed artifact bundles) 🔏📦  

If using OCI/ORAS, store the **digest** in DCAT distribution so the exact bytes can be fetched reproducibly.

---

## 🧩 Story node integration (optional but encouraged)

If this artifact appears in a narrative, link it from a Story Node (Markdown + JSON config). Story content is typically maintained in a structured directory (example: `web/story_nodes/` or `content/stories/`) and reviewed for references, formatting, and correctness.

---

## ✅ Definition of Done

- [ ] `artifact.manifest.json` filled in + validated
- [ ] `checksums.sha256` present (and hashes match)
- [ ] License + attribution included (and compatible)
- [ ] Sensitivity handled (coordinates generalized/hidden if needed)
- [ ] Evidence triplet exists (STAC/DCAT/PROV pointers resolve)
- [ ] UI can render the model (Cesium or Three.js) without console errors
- [ ] CI/policy gates pass (ordering, provenance-first, API boundary, etc.)

---

## 📚 Project docs used (quick links)

> These are the core project references that shaped this template.

- Kansas Frontier Matrix – Comprehensive UI System Overview :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM) :contentReference[oaicite:4]{index=4}
- Document Refinement Request - Kansas Frontier Matrix (KFM) :contentReference[oaicite:5]{index=5}
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation :contentReference[oaicite:6]{index=6}
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design :contentReference[oaicite:7]{index=7}
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖 :contentReference[oaicite:8]{index=8}
- Additional Project Ideas :contentReference[oaicite:9]{index=9}
- Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design :contentReference[oaicite:10]{index=10}
- KFM- python-geospatial-analysis-cookbook (Three.js / WebGL snippets) :contentReference[oaicite:11]{index=11}
- Data Mining Concepts & applictions (privacy & inference risk concepts) :contentReference[oaicite:12]{index=12}

---

<details>
<summary>📎 KFM doc traceability (internal citations)</summary>

- “Evidence triplet” requirement + where catalogs live. :contentReference[oaicite:13]{index=13}  
- Graph ingestion is driven from STAC/DCAT/PROV, uses governed ontology (CIDOC-CRM / GeoSPARQL), and forbids “mystery nodes.” :contentReference[oaicite:14]{index=14}  
- API boundary rule: UI must not bypass governed API paths. :contentReference[oaicite:15]{index=15}  
- “Artifacts must go through API; direct access/hard-coding in UI not allowed.” :contentReference[oaicite:16]{index=16}  
- STAC/DCAT/PROV alignment policy and CI validation expectations. :contentReference[oaicite:17]{index=17}  
- Cross-layer linkage expectations (STAC → data, DCAT → distribution, PROV end-to-end, graph references catalogs). :contentReference[oaicite:18]{index=18}  
- Sensitive archaeology locations can attract looters; show generalized area/hex instead of exact points. :contentReference[oaicite:19]{index=19}  
- Cesium-based 3D viewer + 3D Tiles for streaming 3D content. :contentReference[oaicite:20]{index=20}  
- Storage patterns: processed artifacts stored as files/object storage with checksums for integrity. :contentReference[oaicite:21]{index=21}:contentReference[oaicite:22]{index=22}  
- CI blocks merging when required metadata is missing/invalid (license/schema/validation). :contentReference[oaicite:23]{index=23}  
- Policy gates (schema, STAC/DCAT/PROV completeness, license, sensitivity, provenance; citations). :contentReference[oaicite:24]{index=24}  
- Policy as code with OPA/Rego + Conftest; governance checks are non-negotiable. :contentReference[oaicite:25]{index=25}  
- “Never output less restricted than sources” (fail-closed redaction). :contentReference[oaicite:26]{index=26}  
- DVC for large rasters/model files to avoid bloating Git. :contentReference[oaicite:27]{index=27}  
- OCI/ORAS + Cosign concept for content-addressable, signed artifact storage. :contentReference[oaicite:28]{index=28}  
- Offline pack idea for museums/field use (subset of data + story content). :contentReference[oaicite:29]{index=29}:contentReference[oaicite:30]{index=30}  
- 3D + AR exploration via CesiumJS/3D Tiles; new visualization modes still use cataloged, API-served data. :contentReference[oaicite:31]{index=31}:contentReference[oaicite:32]{index=32}  
- Example Three.js viewer primitives (WebGLRenderer + TrackballControls). :contentReference[oaicite:33]{index=33}  
- Story Nodes are Markdown + JSON; stored in a structured repo directory and reviewed for references/quality. :contentReference[oaicite:34]{index=34}  
- Privacy/inference risk: even outputs can disclose sensitive info; query auditing/inference control concepts. :contentReference[oaicite:35]{index=35}  
- QA + CI best practices: tests run on each commit/PR; pipeline must be green before merge. :contentReference[oaicite:36]{index=36}

</details>

