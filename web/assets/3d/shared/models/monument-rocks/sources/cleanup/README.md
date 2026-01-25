# 🪨 Monument Rocks — 3D Source Cleanup 🧼

![Stage](https://img.shields.io/badge/stage-cleanup-blue) ![Outputs](https://img.shields.io/badge/outputs-GLB%20%2B%203D%20Tiles-orange) ![Target](https://img.shields.io/badge/target-CesiumJS%20%7C%20WebGL-brightgreen) ![Standards](https://img.shields.io/badge/standards-STAC%20%7C%20DCAT%20%7C%20PROV-7b2cbf) ![Policy](https://img.shields.io/badge/policy-provenance--first%20%F0%9F%94%8D-lightgrey)

> [!IMPORTANT]
> This directory is the **cleanup workspace** for the Monument Rocks 3D asset(s).  
> **Raw sources stay immutable** ➜ **cleanup is reproducible** ➜ **dist is consumable** ✅

**Path:** `web/assets/3d/shared/models/monument-rocks/sources/cleanup/`

---

## 🧭 Quick Links

- 📥 Raw inputs: `../raw/` *(do not edit)*
- 🧼 You are here: `./`
- 📦 Runtime outputs (recommended): `../../dist/` *(or wherever the model root expects consumables)*
- 🧩 Model root: `../..`

---

## 🎯 Goals

- **Clean** geometry + materials so the model is stable and predictable in WebGL/Cesium.
- **Produce exports** that load fast (LOD + texture compression) and look good.
- **Preserve provenance** (licenses, sources, toolchain, decisions, checksums) so the asset is auditable and repeatable.
- **Support KFM 2D→3D storytelling** (e.g., “Kansas From Above”) and future AR/offline variants.

---

## 🗺️ Pipeline at a Glance

```mermaid
flowchart LR
  A[📥 sources/raw<br/>(immutable inputs)] --> B[🧼 sources/cleanup<br/>(this folder)]
  B --> C[📦 dist / runtime exports<br/>(GLB / 3D Tiles)]
  C --> D[🗺️ KFM UI<br/>(2D/3D toggle • stories • AR-ready)]
  B --> E[🧾 Provenance Pack<br/>(evidence • PROV • catalog metadata)]
  E --> D
```

---

## 📌 Golden Rules (Non‑Negotiable)

1. **Never** modify files inside `../raw/` (treat as read-only evidence) 🔒  
2. **Everything** in cleanup must be reproducible (document tools + versions + steps) 🧪  
3. **No output less restricted than input** (license + sensitivity must be respected) 🛡️  
4. **Optimize by LOD** (desktop/hero vs default web vs mobile/AR) 🪶  
5. **Geospatial anchor is data, not vibes** (record WGS84 anchor + orientation explicitly) 🧭  

---

## 🗂️ Recommended Folder Layout

> [!TIP]
> Keep this folder tidy by organizing work as **runs**, so each cleanup attempt has its own notes + metrics.

<details>
<summary>📁 Suggested structure (copy/adapt)</summary>

```text
cleanup/
  README.md

  runs/
    YYYY-MM-DD__short-desc/
      monument-rocks.cleanup.blend        # main working scene (non-destructive preferred)
      textures_work/                      # high-quality bake sources (PNG/TIF)
      exports_tmp/                        # optional quick exports for review (NOT final)
      notes.md                            # decisions, known issues, links, screenshots
      metrics.json                        # counts/sizes before vs after

  evidence/
    evidence-manifest.yml                 # sources + license + checksums (required for shipping)

  provenance/
    prov.jsonld                           # raw -> cleanup -> exports chain (required for shipping)

  georef/
    georef.wgs84.json                     # anchor + orientation (required for shipping)
```
</details>

### ✅ What Belongs Here

- Working scene files (e.g., `.blend`) 🧩  
- Retopo meshes / decimation setups 🕸️  
- Bake sources (albedo/normal/roughness/AO) 🎨  
- Cleanup logs + before/after metrics 📊  
- Provenance + evidence records 🧾  

### 🚫 What Does *Not* Belong Here

- Original raw drops (photos, point clouds, scan outputs) → **`../raw/`**  
- Final runtime bundles (GLB/3D Tiles served to users) → **`../../dist/`** *(or agreed runtime folder)*  
- Secrets, keys, tokens, private credentials → **never** 🚨  

---

## 🧰 Tooling (Recommended)

**Core**
- 🟦 **Blender** (cleanup, retopo, bake, export)

**Optional but highly recommended**
- ✅ glTF validator (catch spec/compat issues)
- 🗜️ glTF optimizers (mesh compression + texture pipeline)
- 🧊 Texture compression (KTX2/Basis) for web performance
- 🧹 CloudCompare / MeshLab for point clouds & mesh repair
- 🧳 Git LFS for large binaries (scene files, big textures)

> [!NOTE]
> Tool choices can evolve — but **document what you used** in `runs/*/notes.md` and `provenance/`.

---

## 🧼 Cleanup SOP

### 0) Start a New Cleanup Run 🏁

1. Create: `runs/YYYY-MM-DD__<short-desc>/`
2. In `notes.md`, write:
   - 🎯 Objective (what you’re fixing/improving)
   - 🧾 Source(s) used (reference `../raw/` identifiers)
   - 🧰 Tools + versions
   - ⚠️ Known constraints (license/sensitivity, missing data, etc.)
3. Copy *working* inputs into the run folder **only if needed** (prefer referencing raw by path + checksums).

---

### 1) Import & Normalize the Scene 🧭

**Checklist**
- [ ] Units are **meters** (scale sanity)
- [ ] Transforms are clean (**no negative scale**; apply transforms)
- [ ] Mesh normals are coherent (no “inside-out” shading)
- [ ] Object naming is consistent (`MR_*` prefix recommended)
- [ ] Origin/pivot is sensible (don’t “bake in” world placement by accident)

> [!TIP]
> Keep a “high/dirty” reference object hidden but present for comparison.

---

### 2) Geometry Hygiene 🧽

**Do**
- Remove floating junk geometry, scan spikes, micro-islands
- Fix non-manifold edges, internal faces, duplicate verts
- Resolve self-intersections that break decimation
- Recalculate normals, fix hard-edge artifacts
- Generate LODs (see below)

**Avoid**
- Over-decimating “hero silhouette” edges
- Destroying UV continuity right before baking
- Baking world-space details into geometry that should be textures

#### Suggested LOD Targets (Adjust as Needed)

| LOD | Intended Use | Triangle Budget (rule-of-thumb) | Notes |
|---:|---|---:|---|
| `lod0` | Hero / close-up | 150k–500k | Great for stills & close story stops |
| `lod1` | Default web | 30k–150k | KFM “most users” default |
| `lod2` | Mobile / AR / offline | 5k–30k | Must load quickly on weak devices |

> [!NOTE]
> Budgets depend on texture fidelity + silhouette needs. Log your before/after metrics.

---

### 3) UVs & Materials (PBR) 🎨

**Required**
- [ ] UVs are valid (no accidental overlaps unless intentional)
- [ ] Texel density is reasonable and consistent for the asset
- [ ] Materials follow PBR conventions (metal/rough pipeline)
- [ ] Texture naming is consistent

**Recommended**
- Use a single packed ORM texture when possible:
  - **R** = Occlusion  
  - **G** = Roughness  
  - **B** = Metallic  

<details>
<summary>🎛️ Recommended texture naming</summary>

```text
monument-rocks_baseColor.png
monument-rocks_normal.png
monument-rocks_orm.png         # occlusion/roughness/metallic packed
monument-rocks_emissive.png    # if needed
```
</details>

---

### 4) Georeferencing (WGS84 Anchor) 🧭🌎

KFM standardizes spatial alignment around **WGS84 (EPSG:4326)** at the “web truth” layer.  
For 3D assets, we keep the mesh in a clean local coordinate system **and** store a separate **anchor** that places it correctly in the world.

✅ Create: `georef/georef.wgs84.json`

<details>
<summary>📄 Template: <code>georef.wgs84.json</code></summary>

```json
{
  "crs": "EPSG:4326",
  "anchor": {
    "lat": 0,
    "lon": 0,
    "height_m": 0
  },
  "orientation": {
    "heading_deg": 0,
    "pitch_deg": 0,
    "roll_deg": 0
  },
  "scale": 1.0,
  "notes": "Replace lat/lon/height with a verified anchor (survey/GPS/authoritative source)."
}
```
</details>

> [!IMPORTANT]
> If you change the mesh origin/scale in cleanup, **update georef** and **record it in provenance**.

---

### 5) Export Targets 📦

| Export | When to use | Suggested Output Name |
|---|---|---|
| GLB `lod1` | Default web viewer | `monument-rocks_lod1.glb` |
| GLB `lod2` | Mobile/AR/offline pack | `monument-rocks_lod2.glb` |
| GLB `lod0` | Hero close-up (optional) | `monument-rocks_lod0.glb` |
| 3D Tiles | Cesium streaming / terrain scenes (optional) | `tileset/tileset.json` |

> [!TIP]
> If you’re targeting Cesium-first experiences, prefer **3D Tiles** for streaming + LOD management.  
> If you’re targeting lightweight WebGL, GLB is often the simplest.

---

### 6) Optimize & Validate ✅

**Validation**
- [ ] glTF/GLB loads cleanly (no missing textures)
- [ ] Validator passes (or issues documented + justified)
- [ ] Materials look correct in at least **two viewers** (e.g., local + Cesium/Three)

**Optimization**
- [ ] Use geometry compression when appropriate
- [ ] Compress textures for web (KTX2 recommended where supported)
- [ ] Keep runtime exports within size budgets for intended devices

<details>
<summary>🧪 Metrics template (store as <code>metrics.json</code>)</summary>

```json
{
  "before": { "triangles": 0, "textures_mb": 0, "glb_mb": 0 },
  "after":  { "triangles": 0, "textures_mb": 0, "glb_mb": 0 },
  "notes": "Record exact tool versions + settings in notes.md"
}
```
</details>

---

## ✅ Definition of Done (DoD)

A cleanup run can be considered “shippable” when:

- [ ] Raw sources remain untouched (`../raw/` unchanged)
- [ ] Clean working scene saved in `runs/.../`
- [ ] At least one runtime-ready export exists (usually `lod1`)
- [ ] Textures/materials are correct and consistent
- [ ] Georef anchor exists and matches the cleaned model
- [ ] Evidence + provenance are complete (see below)
- [ ] License and sensitivity are explicitly stated
- [ ] Review includes screenshots + metrics (before/after)

---

## 🧾 Evidence + Provenance Pack (Shipping Requirement)

KFM’s core promise is **traceability**. A 3D asset is *not* shippable unless we can answer:

- Where did this come from?  
- Under what license?  
- What changed during cleanup?  
- Which tools/settings produced the final export?

### Required files (recommended minimum)

- `evidence/evidence-manifest.yml` ✅
- `provenance/prov.jsonld` ✅
- `georef/georef.wgs84.json` ✅

<details>
<summary>📄 Template: <code>evidence-manifest.yml</code></summary>

```yaml
asset_id: kfm.3d.monument-rocks
title: "Monument Rocks (3D Model)"
sensitivity: public   # public | sensitive | restricted (project policy)
license: TBD          # MUST be resolved before shipping
sources:
  - id: raw-scan-01
    path: ../raw/<replace-me>
    type: photogrammetry|lidar|hand-model|other
    obtained_on: YYYY-MM-DD
    checksum_sha256: "<replace-me>"
    source_url: "<optional>"
    attribution: "<replace-me>"
    notes: "Any usage constraints, credit text, etc."
derivations:
  - run_id: MR-CLN-YYYYMMDD-01
    run_path: runs/YYYY-MM-DD__short-desc/
    outputs:
      - "../../dist/monument-rocks_lod1.glb"
    notes: "Summary of what changed + why"
```
</details>

<details>
<summary>📄 Template: <code>prov.jsonld</code> (minimal starter)</summary>

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "raw:scan01": { "prov:label": "Monument Rocks raw source scan (scan01)" },
    "clean:lod1": { "prov:label": "Monument Rocks GLB LOD1" }
  },
  "activity": {
    "act:cleanup": {
      "prov:label": "Cleanup + optimization",
      "prov:used": ["raw:scan01"],
      "prov:generated": ["clean:lod1"]
    }
  },
  "agent": {
    "agent:contributor": { "prov:type": "prov:Person", "prov:label": "Contributor (name/handle)" }
  }
}
```
</details>

> [!IMPORTANT]
> If **license is unknown**, treat the asset as **blocked** until resolved. 🚫

---

## 🔐 Sensitivity & Licensing

Even for public landmarks, we treat governance seriously:

- ✅ Assign a **sensitivity** label (`public`, `sensitive`, `restricted`)
- ✅ Ensure derived exports are **not less restricted** than the most restrictive input
- ✅ Include attribution/credits as required by the source license

---

## 🧩 Integration Contract (What the App Should Be Able to Rely On)

To keep the front-end simple, prefer a small manifest at the model root (recommended):

- `../.. / monument-rocks.asset.json` *(recommended name)*  
  - Declares default LOD, available exports, georef file, sensitivity, credits

<details>
<summary>📄 Template: <code>monument-rocks.asset.json</code></summary>

```json
{
  "id": "kfm.3d.monument-rocks",
  "title": "Monument Rocks",
  "sensitivity": "public",
  "georef": "sources/cleanup/georef/georef.wgs84.json",
  "defaults": {
    "runtime": "dist/monument-rocks_lod1.glb"
  },
  "lods": {
    "lod0": "dist/monument-rocks_lod0.glb",
    "lod1": "dist/monument-rocks_lod1.glb",
    "lod2": "dist/monument-rocks_lod2.glb"
  },
  "tileset": "dist/tileset/tileset.json",
  "credits": [
    { "text": "TBD", "url": "TBD" }
  ]
}
```
</details>

---

## 🧪 Cleanup Runs = Mini Experiments (MCP Style) 🧠🔬

> [!NOTE]
> Treat each cleanup run as an experiment: define the objective, document the method, record the result.

**Suggested run template (`runs/.../notes.md`)**
- Objective / hypothesis (e.g., “Reduce GLB to < 15MB while preserving silhouette”)
- Method (tools + settings + steps)
- Results (metrics table + screenshots)
- Conclusion (what worked, what didn’t, next steps)

---

## 🤝 PR / Review Checklist ✅

Before merging cleanup work that affects runtime exports:

- [ ] Evidence manifest complete (license + checksums)
- [ ] Provenance updated (inputs ➜ cleanup ➜ exports)
- [ ] Georef verified (WGS84 anchor present and correct)
- [ ] Validator checks passed (or issues documented)
- [ ] Before/after screenshots included
- [ ] Before/after metrics included
- [ ] No large binaries committed without Git LFS (if policy applies)

---

## 📚 Related KFM Docs (Recommended Reading)

- 📘 **Comprehensive Technical Documentation** (2D/3D integration, “Kansas From Above”, standards)
- 🧭 **AI System Overview** (offline packs, AR direction, 3D roadmap)
- 🧩 **Comprehensive UI System Overview** (3D/AR UX considerations + filtering)
- 📥 **Data Intake – Technical & Design Guide** (STAC/DCAT/PROV, evidence-first rules)
- 🚀 **Innovative Concepts** (hybrid 2D/3D storytelling, AR storyscapes, 4D digital twin ideas)
- 🧪 **Scientific Method / Master Coder Protocol** (reproducible workflows & documentation discipline)

---

## 🌄 Future Enhancements (Nice-to-Have)

- 🧊 **AR-specific variant** (super lightweight LOD2 + simplified materials)
- 🧳 **Offline pack bundle** (bundle model + minimal dependencies for field use)
- ⏳ **Time-state variants** (if future storytelling needs “then vs now” model states)
- 📦 **Artifact publishing** (optional OCI-based artifact storage + signatures, if adopted)

