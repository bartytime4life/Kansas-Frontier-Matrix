# 🪨 Monument Rocks — Selected Photos (Photogrammetry Sources) 📸

![asset](https://img.shields.io/badge/asset-source-blue)
![pipeline](https://img.shields.io/badge/pipeline-photogrammetry-8A2BE2)
![status](https://img.shields.io/badge/status-curated-success)
![provenance](https://img.shields.io/badge/provenance-required-critical)
![safety](https://img.shields.io/badge/sensitivity-policy%20gated-orange)

📁 **Path:** `web/assets/3d/shared/models/monument-rocks/sources/photos_selected/`  
🎯 **Purpose:** a curated (“golden”) subset of photos used to reconstruct the **Monument Rocks** 3D model for the KFM web experience (2D ⇄ 3D storytelling, “Kansas From Above” demo target).:contentReference[oaicite:0]{index=0}

---

## ✅ What belongs here

These photos are the **inputs** to the photogrammetry pipeline (Structure-from-Motion + Multi-View Stereo). They are *not* a general photo gallery.

**✅ Include**
- High-quality, high-overlap, sharp images suitable for photogrammetry
- Coverage from multiple angles + elevations (walk-around loops)
- Consistent exposure and focus (as much as possible)
- **Only** items that are intended to be referenced by manifests / provenance

**🚫 Don’t include**
- RAW camera files (`.CR2`, `.NEF`, `.ARW`) — store in the evidence store / artifact registry (see “Storage”)
- Random “nice shots” with low overlap
- Edited or filtered versions that change pixels (those are *derivatives*, not sources)
- Photos containing identifiable faces / license plates (unless explicitly approved + documented)

> [!IMPORTANT]
> **No silent changes.** This folder is treated like evidence input for a reproducible pipeline:
> - Don’t overwrite existing files.
> - Don’t “fix” images in-place.
> - Any change must be **additive**, with updated manifests + provenance.
>
> This follows KFM’s “immutability & trust boundaries” and deterministic pipeline philosophy.:contentReference[oaicite:1]{index=1}

---

## 🗂️ Folder map

```text
🪨 monument-rocks/
└─ 📁 sources/
   └─ 📁 photos_selected/        👈 you are here
      ├─ README.md
      ├─ (recommended) manifest.photos.json
      ├─ (recommended) manifest.sha256
      ├─ (recommended) exif.json
      └─ (recommended) LICENSES/ (or refs in DCAT/manifest)
```

> [!NOTE]
> The “recommended” files above can be generated automatically. The folder can still work without them, but KFM standards assume we can always trace, verify, and reproduce outputs.

---

## 🧠 Pipeline overview (how these photos become a web-ready model)

```mermaid
flowchart TD
  A[📸 Capture / Sources] --> B[🧹 Selection + QC]
  B --> C[🧾 Evidence manifests<br/>sha256 + EXIF + license + classification]
  C --> D[🧠 Photogrammetry (SfM/MVS)]
  D --> E[🧱 Mesh + UV + textures]
  E --> F[🚀 Web packaging<br/>glTF/GLB + 3D Tiles + optimized textures]
  F --> G[🗺️ KFM UI<br/>MapLibre 2D ⇄ Cesium 3D]
```

KFM’s front-end architecture explicitly supports a **MapLibre 2D viewer** and a **CesiumJS 3D viewer**, using **3D Tiles** for streaming 3D content (and optionally 3D landmark models).:contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

---

## 🧹 Selection criteria (what “selected” means)

| Category | Target | Why it matters |
|---|---|---|
| Overlap | ~70%+ forward + side overlap | Stable feature matching |
| Sharpness | No motion blur, consistent focus | Prevents noisy reconstructions |
| Exposure | Avoid blown highlights / crushed shadows | Better texture & feature tracking |
| Coverage | Full 360° coverage + varied elevations | Prevents holes / weak geometry |
| Motion | No moving people/vehicles dominating frame | SfM confusion + privacy |
| Repetition | Avoid near-duplicates | Wasteful compute; can destabilize matching |
| EXIF integrity | Preserve original EXIF when possible | Audit, camera modeling, QA |

> [!TIP]
> If you *must* include edited photos (color correction / de-noise), store them as **derivatives** elsewhere and keep the original “as received” photo bytes in the raw evidence boundary. This follows KFM’s “no manual edits to processed data” / deterministic pipeline expectations.:contentReference[oaicite:4]{index=4}

---

## 🧾 Metadata contract (KFM-style, but scoped to photos)

KFM’s metadata stack revolves around **STAC + DCAT + PROV** (the “catalog triplet”) for discoverability, licensing, and lineage tracking.:contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}

For *this folder*, we keep it practical:

### 1) `manifest.photos.json` (recommended)
A machine-readable inventory of selected images.

```json
{
  "dataset_id": "kfm:3d:monument-rocks:photos:selected",
  "collection": "monument-rocks",
  "classification": "public",
  "license_spdx": "CC-BY-4.0",
  "capture": {
    "location_hint": "Monument Rocks, Kansas",
    "crs": "EPSG:4326"
  },
  "photos": [
    {
      "file": "IMG_0001.JPG",
      "sha256": "…",
      "bytes": 12345678,
      "captured_at": "YYYY-MM-DDTHH:MM:SSZ",
      "camera": { "make": "…", "model": "…", "lens": "…" },
      "exif": { "focal_length_mm": 24.0, "f_number": 8.0, "iso": 100, "shutter_s": 0.004 },
      "gps": { "lat": 0.0, "lon": 0.0, "alt_m": 0.0 }
    }
  ]
}
```

> [!IMPORTANT]
> **CRS standard:** KFM serves web-facing geospatial coordinates in **WGS84 / EPSG:4326** and expects original CRS tracking in metadata when relevant.:contentReference[oaicite:7]{index=7}

### 2) `manifest.sha256` (recommended)
A plain hash list to keep changes auditable.

```bash
# stable ordering matters for review diffs
find . -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -print0 \
  | sort -z \
  | xargs -0 sha256sum > manifest.sha256
```

### 3) `exif.json` (recommended)
Extract EXIF (numeric) for QA and repro.

```bash
exiftool -json -n *.jpg > exif.json
```

---

## 🔒 Sensitivity, policy, and “no leaks”

KFM’s governance expectations include:
- **Sensitivity classification propagation** (outputs can’t be “less restricted” than inputs)
- Safeguards against leaking sensitive coordinates via UI or side channels:contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}

**For this folder:**
- If *any* photo set includes restricted capture context, set `classification` accordingly (e.g., `restricted`, `confidential`) and avoid publishing derivatives to public web assets.
- If EXIF includes GPS but the location should be generalized, store full coordinates in a protected evidence store and publish only generalized geometry in STAC/DCAT.

> [!CAUTION]
> **Don’t rely on “it’s just an image”** — EXIF can carry location/time/device identifiers. Treat metadata as part of the dataset.

---

## 🧑‍💻 How to contribute new photos (clean, reproducible path)

1) **Ingest originals** into the raw evidence boundary (recommended pattern)  
   - Raw bytes are immutable evidence; downstream folders contain derived/curated copies.:contentReference[oaicite:10]{index=10}

2) **Select** photos into this folder
   - Prefer copying *exact bytes* from raw → selected
   - Avoid any re-encoding

3) **Generate/update manifests**
   - `manifest.sha256`
   - `exif.json`
   - `manifest.photos.json` (or update it)

4) **Ensure policy gates will pass**
   - license present
   - classification present
   - provenance/manifest present (no “mystery photos”)

5) **Open PR**
   - Let CI verify hashes + manifests
   - Optional: allow an agent to propose fixes, but never auto-merge (human review required).:contentReference[oaicite:11]{index=11}

---

## 🧪 PR checklist (fast review)

- [ ] No files overwritten (additive only)
- [ ] `manifest.sha256` updated and matches files
- [ ] `manifest.photos.json` updated (license + classification included)
- [ ] No faces / plates / personal data visible
- [ ] Photos meet overlap + sharpness criteria
- [ ] Any georeferencing claims have backing metadata (EXIF, GCP log, etc.)
- [ ] If a derived model changes, there is a run/provenance note tying new outputs to this input set

---

## 📦 Storage notes (keep the repo usable)

KFM’s repo structure and workflow anticipate large datasets being referenced or managed carefully (e.g., raw data not necessarily stored directly in Git).:contentReference[oaicite:12]{index=12}

Recommended strategy:
- **Full-res originals** → evidence store (DVC remote / object storage / OCI registry)
- **This folder** → curated subset (either:
  - downsampled “build inputs”, or
  - pointers + manifests referencing external evidence bytes)
- **Web runtime artifacts** (GLB / 3D Tiles / textures) → publishable assets, ideally content-addressed

KFM also proposes an OCI-based artifact distribution pattern (ORAS + Cosign), which is a strong fit for shipping large model assets (and signing provenance).:contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}

---

## 🎭 Story + UI integration (why this matters)

KFM’s UI expects narratives and visual content to remain **traceable** (clickable citations/metadata), including inside stories.:contentReference[oaicite:15]{index=15}

That’s why this folder should always be representable as:
- a dataset (DCAT),
- a set of assets (STAC),
- and a lineage chain (PROV),
so a future “Kansas From Above — Monument Rocks” story can cite the exact source photos that produced the 3D model.:contentReference[oaicite:16]{index=16}

---

## 📚 Project standards & reference library (used to shape this README)

### Core KFM docs (governance + architecture)
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`:contentReference[oaicite:17]{index=17}
- `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`:contentReference[oaicite:18]{index=18}
- `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`:contentReference[oaicite:19]{index=19}
- `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`:contentReference[oaicite:20]{index=20}
- `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`:contentReference[oaicite:21]{index=21}
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`:contentReference[oaicite:22]{index=22}
- `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf` (immersive 3D storytelling inspirations):contentReference[oaicite:23]{index=23}
- `Additional Project Ideas.pdf` (policy gates, manifests, OCI artifacts):contentReference[oaicite:24]{index=24}

### Project reference portfolios (embedded libraries 📦)
> [!NOTE]
> The following PDFs are **portfolios** containing many attached reference docs (CV/AI, geospatial WebGL, pipelines, programming). They’re used as a knowledge base for implementation choices and future automation.

<details>
<summary>🧠 AI Concepts &amp; more.pdf (portfolio)</summary>

Selected relevant references inside:
- *Pattern Recognition and Machine Learning*
- *Deep Learning with Python*
- *Introduction to Machine Learning with Python*
- *AI Foundations of Computational Agents*

Use cases here: automated photo QC (blur detection, near-duplicate detection, subject filtering), and future “AI Data Steward” style intake automation.

</details>

<details>
<summary>🗺️ Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf (portfolio)</summary>

Selected relevant references inside:
- *webgl-programming-guide-interactive-3d-graphics-programming-with-webgl*
- *google-maps-javascript-api-cookbook*
- *geoprocessing-with-python*
- *python-geospatial-analysis-cookbook*
- *DesigningVirtualWorlds*
- *Archaeological 3D GIS*

Use cases here: WebGL constraints, 3D visualization patterns, geospatial processing that supports 3D context.

</details>

<details>
<summary>🧱 Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf (portfolio)</summary>

Selected relevant references inside:
- *The Data Engineering Cookbook*
- *Database Performance at Scale*
- *Comprehensive CI/CD Guide for Software and Data Projects*
- *Bayesian Methods for Hackers*

Use cases here: reproducible data pipelines, deterministic processing discipline, and scaling artifact handling.

</details>

<details>
<summary>🧰 Various programming langurages &amp; resources 1.pdf (portfolio)</summary>

Selected relevant references inside:
- *Git Notes for Professionals*
- *Bash Notes for Professionals*
- *Algorithms Notes for Professionals*
- *HTML5 Canvas Notes for Professionals*
- *Handbook Of Applied Cryptography*

Use cases here: automation scripting, build tooling, verification primitives (hashing/signing), and web rendering techniques.

</details>

---

## 🧩 Glossary

- **Raw photos**: immutable, “as received” camera exports (evidence boundary)
- **Selected photos**: curated subset (this folder) used to generate the model
- **Derived artifacts**: point clouds, meshes, textures, GLB, 3D Tiles (rebuildable outputs)
- **Run manifest**: a record of a pipeline run (inputs, outputs, tool versions, hashes) — aligns with KFM’s governance vocabulary:contentReference[oaicite:25]{index=25}

---

## ✅ Bottom line

This folder is a **high-trust input set** for producing a **high-trust 3D artifact**.  
Treat it like evidence: reproducible, hashable, policy-gated, and ready to be cited in Story Nodes.

