# 📸 Monument Rocks — `photos_raw` (Immutable Source Photos)

![Stage](https://img.shields.io/badge/stage-RAW%20%26%20IMMUTABLE-blue)
![Asset](https://img.shields.io/badge/asset-Monument%20Rocks-2ea44f)
![Pipeline](https://img.shields.io/badge/pipeline-evidence--first%20%2F%20PROV-purple)
![Output](https://img.shields.io/badge/output-glTF%20%2B%203D%20Tiles-orange)
![Viewer](https://img.shields.io/badge/viewer-CesiumJS-lightgrey)

**Folder:** `web/assets/3d/shared/models/monument-rocks/sources/photos_raw/`  
**Purpose:** Store the **original, unmodified** photo sources used to build the *Monument Rocks* 3D asset (photogrammetry ➜ mesh ➜ glTF ➜ Cesium 3D Tiles) for KFM’s 3D experiences 🧭🌾

---

## 🧭 Quick Nav

- ⬆️ Back to **Monument Rocks model root**: `../../README.md`
- ⬅️ Back to **sources/**: `../`
- ✅ Looking for the *web-consumable* output? You probably want `tileset.json`, `*.b3dm`, or `*.glb` in the **build/dist** folders (not in here).

---

> [!IMPORTANT]
> **This is a provenance anchor.** Treat everything in `photos_raw/` as **append-only + immutable**.
>
> ✅ Add new source photos  
> ❌ Do not overwrite, “touch up”, resize, rename, recompress, strip EXIF, or rotate-in-place  
>
> If edits are needed, do them in a **work/processed** stage and keep a **traceable link back** to these originals.

---

## 🎯 What belongs here

**✅ Yes (raw source material)**
- Camera originals (e.g., `JPG`, `JPEG`, `DNG`, `NEF`, `CR2`, `ARW`, etc.)
- Drone capture originals (where legally and ethically permissible)
- Any *source* photos that directly contributed to the mesh/texture bake

**❌ No (derived outputs)**
- Cropped/rotated/denoised/AI-enhanced versions  
- Downsampled “web preview” JPGs  
- Masks, depth maps, point clouds, meshes, textures, atlases  
- glTF / GLB / 3D Tiles outputs

> [!TIP]
> Put derived content in your model’s `work/` or `processed/` paths (or whichever KFM staging folders your pipeline uses). Keep `photos_raw/` pristine.

---

## 🧱 Directory Contract (expected layout)

We keep raw photos organized by **capture session**, plus lightweight “audit files” at the top level.

```text
📁 photos_raw/
├─ 📄 README.md                      # you are here 🙂
├─ 📄 checksums.sha256               # REQUIRED (top-level)
├─ 📄 photos.manifest.csv            # REQUIRED (top-level)
├─ 📁 sessions/                      # RECOMMENDED (capture-session grouping)
│  ├─ 📁 2025-07-14__drone-grid__v01/
│  │  ├─ 📄 capture_session.yml      # REQUIRED (per session)
│  │  ├─ 📄 sources.yml              # REQUIRED (per session)
│  │  ├─ 📄 notes.md                 # optional field notes
│  │  └─ 📷 DJI_0001.DNG / JPG / ...
│  └─ 📁 2025-07-14__handheld-orbits__v01/
│     ├─ 📄 capture_session.yml
│     ├─ 📄 sources.yml
│     └─ 📷 DSC_0001.NEF / JPG / ...
└─ 📁 _quarantine/                   # optional (suspect licensing/sensitivity)
```

---

## 🧾 Provenance & Governance Rules (KFM-standard)

### 1) Evidence-first publishing 🧠🔎
KFM treats *anything used in UI / story / AI* as needing **traceable evidence**. For this folder that means:

- Every capture session must have **who/when/where/how** metadata
- Every file must be represented in a manifest
- Every file must be covered by checksums

### 2) No “mystery files” 🚫👻
If a photo is in this folder but is not:
- in `photos.manifest.csv`, **and**
- in `checksums.sha256`, **and**
- covered by a session `capture_session.yml` + `sources.yml`

…it’s considered **not ingest-ready**.

### 3) Classification & sensitivity 🔐
Photos may contain:
- identifiable people / vehicles
- EXIF GPS data
- culturally sensitive context

If a capture session is **restricted**, it must be marked as such in metadata and **must not be shipped** in any public/offline pack. Derived/public versions must be redacted in a governed stage.

---

## 🏷️ Naming rules (don’t rename raw files)

> [!NOTE]
> **Default:** keep camera-native filenames exactly as captured.  
> We rely on **session folders + manifest rows** for stable identity.

If you *must* impose a canonical naming scheme (rare), do it via:
- a `renames.csv` mapping, **or**
- symlinks in `work/` stage (not in `photos_raw/`)

### ✅ Capture session folder naming
Use a stable, sortable pattern:

- `YYYY-MM-DD__<capture-type>__vNN/`

Examples:
- `2025-07-14__drone-grid__v01/`
- `2025-07-14__handheld-orbits__v01/`
- `2025-07-14__golden-hour-textures__v01/`

---

## 📄 Required audit files

### `photos.manifest.csv` (top-level) ✅
One row per file (minimum). Keep it boring and strict.

**Recommended columns**
- `relative_path` (from `photos_raw/`)
- `sha256` (optional if you keep in checksums file only)
- `session_id`
- `capture_utc` (best-effort)
- `camera_make`
- `camera_model`
- `lens`
- `focal_length_mm`
- `license`
- `classification`
- `notes`

Example row (CSV):
```csv
relative_path,session_id,capture_utc,camera_make,camera_model,lens,focal_length_mm,license,classification,notes
sessions/2025-07-14__handheld-orbits__v01/DSC_0001.NEF,2025-07-14__handheld-orbits__v01,2025-07-14T15:31:12Z,Nikon,D850,24-70mm,35,CC-BY-4.0,public,"orbit pass #1"
```

### `checksums.sha256` (top-level) ✅
A reproducibility guardrail.

Generate (example):
```bash
# from within photos_raw/
find sessions -type f \
  \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.dng' -o -iname '*.nef' -o -iname '*.cr2' -o -iname '*.arw' \) \
  -print0 | sort -z | xargs -0 sha256sum > checksums.sha256
```

Verify:
```bash
sha256sum -c checksums.sha256
```

---

## 🗂️ Per-session metadata (REQUIRED)

Each session folder must include:

- `capture_session.yml` — **how** the photos were captured  
- `sources.yml` — **who owns them, where they came from, what license applies**

### 📌 `capture_session.yml` template (copy/paste)
```yaml
id: "kfm:asset:3d:monument-rocks:photos_raw:2025-07-14__handheld-orbits__v01"
title: "Monument Rocks — handheld orbit captures (v01)"
classification: "public" # public | internal | restricted
capture:
  start_utc: "2025-07-14T15:30:00Z"
  end_utc: "2025-07-14T16:10:00Z"
  platform: "handheld" # handheld | drone | pole | other
  notes: "Overcast, low wind, soft shadows"
equipment:
  camera_make: "Nikon"
  camera_model: "D850"
  lens: "24-70mm"
  focal_length_mm: 35
  image_format: ["NEF"]
geospatial:
  crs: "EPSG:4326" # WGS84
  bbox_wgs84: [minLon, minLat, maxLon, maxLat] # best-effort
  gps_in_exif: true
quality:
  intended_overlap: "high"
  blur_screened: false
```

### 🧾 `sources.yml` template (copy/paste)
```yaml
license: "CC-BY-4.0"   # or project-specific license identifier
attribution: "Kansas Frontier Matrix contributors"
source_type: "first_party" # first_party | third_party | partner
provenance:
  captured_by:
    name: ""
    contact: ""
    affiliation: ""
  captured_on_site_permission: "public_land_assumed" # be explicit if permits exist
  notes: "If any 3rd-party media is included, document exact origin and terms."
```

---

## 🧪 3D Asset Pipeline Linkage (how these photos become the model)

KFM’s philosophy is **traceability from raw ➜ output ➜ UI/story**.

```mermaid
flowchart LR
  A[📸 photos_raw (immutable)] --> B[🧰 work/ (alignment, masks, cleanup)]
  B --> C[🧱 mesh + textures (processed)]
  C --> D[📦 glTF/GLB export]
  D --> E[🧊 Cesium 3D Tiles tileset]
  E --> F[🗺️ KFM Web UI (Cesium 3D mode)]
  F --> G[📖 Story Node: "Kansas From Above" demo]
  C --> H[🧾 STAC/DCAT/PROV (evidence triplet)]
  H --> F
```

> [!TIP]
> Even if the *files* live under `web/assets/…`, the **metadata truth** should still land in canonical KFM catalogs (STAC/DCAT/PROV) so the UI/AI can cite it cleanly.

---

## ✅ PR Checklist (for adding a new photo session)

- [ ] Create a new `sessions/YYYY-MM-DD__<type>__vNN/` folder
- [ ] Copy raw files in **without renaming**
- [ ] Add `capture_session.yml`
- [ ] Add `sources.yml` (license + attribution is non-negotiable)
- [ ] Update `photos.manifest.csv`
- [ ] Regenerate `checksums.sha256`
- [ ] Confirm classification (public/internal/restricted)
- [ ] (If used in UI/story) ensure STAC/DCAT/PROV references exist in the canonical KFM catalogs

---

## 🧯 Common pitfalls (avoid these)

- **Recompressing JPGs** “to save space” (breaks checksum + texture fidelity)
- **Stripping EXIF** unintentionally (removes time/location anchors)
- **Mixing sessions** in one folder (ruins capture reproducibility)
- **Missing license info** (blocks publishing and violates evidence-first rules)
- **Accidentally deploying raw photos** in production builds (privacy/EXIF leak risk)

---

## 🧰 Tooling notes (non-binding, but recommended)

- Photogrammetry: Meshroom / OpenDroneMap / RealityCapture (choose based on license + workflow)
- Cleanup + optimization: Blender, glTF transform tools, mesh simplification
- Delivery: **glTF** for portable web assets + **3D Tiles** for streaming in Cesium

> [!NOTE]
> The “best” tool is the one we can reproduce. If a tool is proprietary, document settings and export logs carefully so we can re-run or migrate later.

---

## 🧩 TODO (nice-to-have enhancements)

- 📌 Add an `ASSET_CARD.md` at the model root (model-card style metadata)
- 🧾 Add explicit STAC Item IDs for each session
- 🧪 Add a `qa_report.md` (blur detection %, coverage notes, known gaps)
- 🧊 Add a `tileset_build_log.json` in build outputs to link back to sessions + commits

