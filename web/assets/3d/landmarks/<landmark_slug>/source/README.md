---
title: "🧱 Landmark Source Assets — <landmark_slug>"
path: "web/assets/3d/landmarks/<landmark_slug>/source/README.md"
version: "v1.0.0"
last_updated: "2026-01-15"
status: "active"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
pipeline_contract_version: "TBD"

governance_ref: "TBD"
ethics_ref: "TBD"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:web:assets:3d:landmarks:<landmark_slug>:source:readme:v1.0.0"
commit_sha: "<fill-at-commit>"
doc_integrity_checksum: "sha256:<fill-after-render>"
---

# 🧱 `source/` — Raw & Upstream Landmark Materials

![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-2b6cb0)
![3D](https://img.shields.io/badge/3D-Assets-111827)
![Provenance](https://img.shields.io/badge/Provenance-First-065f46)

> [!IMPORTANT]
> This folder is the **ground truth “inbox”** for a landmark’s upstream assets (scans, photogrammetry projects, CAD, reference imagery, field notes).  
> Treat everything here as **immutable source-of-record**. Derivatives belong in sibling folders like `../models/` and `../textures/`.

---

## 🎯 Purpose

This directory holds the **highest-fidelity inputs** used to produce the landmark’s shipping assets (GLB, 3D Tiles, runtime textures). It exists to ensure:

- ✅ **Reproducibility** (rebuild the landmark artifact stack)
- ✅ **Auditability** (trace every vertex/texture back to origin)
- ✅ **Non-destructive workflows** (source stays pristine; outputs iterate)

---

## ✅ Scope

| ✅ In Scope (belongs here) | 🚫 Out of Scope (do NOT put here) |
|---|---|
| 📷 Raw photo sets (photogrammetry) | ✅ Final runtime assets (GLB/3D Tiles/textures) |
| 🧪 Scan data (LiDAR, point clouds, E57/LAZ/LAS) | 🧱 Minified web-ready textures (use `../textures/`) |
| 🧰 Project files (Metashape, RealityCapture, Blender, etc.) | 🗂️ General/shared materials (use `../../../shared/…`) |
| 🗺️ Georeferencing artifacts (GCPs, CRS notes, transforms) | 🔐 Secrets, private keys, credentials |
| 🧾 Field notes + capture reports | 🧍 PII / sensitive imagery (unless explicitly cleared) |
| 📄 Upstream licenses + receipts of permission | ❌ Anything without provenance metadata |

---

## 🧭 Quick Links

- 📦 Runtime outputs: `../models/` and `../textures/`
- 🪪 Licensing: `../licenses/README.md`
- 🧾 Citations & sources: `../citations/README.md`
- 🏷️ Attribution summary: `../attribution.md`

---

## 🗂️ Suggested Sub-Structure

> [!NOTE]
> Not every landmark needs every subfolder. Keep it **lean** but **consistent**.

```text
web/assets/3d/landmarks/<landmark_slug>/source/
├─ 📷 photos/                     # Raw image sets (photogrammetry)
│  ├─ session-YYYYMMDD_* /
│  └─ README.md (optional)
├─ 🧪 scans/
│  ├─ lidar/                      # LAS/LAZ/E57/etc
│  ├─ structured_light/
│  └─ terrestrial/
├─ 🧱 cad/
│  ├─ original/
│  └─ exports/
├─ 🧠 projects/
│  ├─ metashape/
│  ├─ realitycapture/
│  ├─ blender/
│  └─ other/
├─ 🧭 georef/
│  ├─ gcp/                        # Ground Control Points, residuals, reports
│  ├─ crs/                        # CRS notes + epsg references
│  └─ transforms/                 # local→world transforms, anchors, origins
├─ 🧾 docs/
│  ├─ capture_report.md
│  ├─ equipment.md
│  └─ qa_notes.md
├─ 🧬 manifests/
│  ├─ source.manifest.yaml        # REQUIRED (inventory + provenance)
│  └─ checksums.sha256            # REQUIRED (integrity)
└─ 🧰 scripts/                    # Optional: one-off helpers for this landmark
```

---

## 🧬 Provenance Contract (Non-Negotiable)

### 1) `manifests/source.manifest.yaml` (required)

Create a manifest that inventories **every** source artifact (even if it’s stored via LFS/DVC pointers). Suggested schema:

```yaml
landmark_slug: "<landmark_slug>"
source_bundle_id: "src_<landmark_slug>_YYYYMMDD_v01"
created_at: "YYYY-MM-DD"
created_by: "name_or_handle"

capture:
  method: "photogrammetry|lidar|cad|hybrid|other"
  equipment:
    camera_or_scanner: "make/model"
    lens: "n/a"
    settings: "iso/shutter/aperture or n/a"
  environment: "outdoor|indoor|mixed"
  notes: "short capture context"

spatial:
  crs:
    name: "WGS84 / local / state-plane / UTM / etc"
    epsg: "TBD"
  units: "meters"
  georeferencing:
    gcp_used: true
    gcp_file: "georef/gcp/<file>"
    accuracy_report: "georef/gcp/<report>"
  anchor:
    description: "how the model is positioned in-world"
    transform_file: "georef/transforms/<file>"

assets:
  - id: "photo_set_01"
    type: "photo_set"
    path: "photos/session-YYYYMMDD_*/"
    license_ref: "../licenses/README.md"
    citation_ref: "../citations/README.md"
    sha256: "TBD"
    notes: "overlap ~70%, 24mm equiv"
  - id: "scan_01"
    type: "point_cloud"
    path: "scans/lidar/<file>.laz"
    sha256: "TBD"
    notes: "registered in software X"
```

### 2) `manifests/checksums.sha256` (required)

- Store **sha256** for each file (or each archive / pointer target).
- Recompute after any intentional repackage (never silently).

---

## 🌍 Georeferencing & Coordinate Hygiene

> [!TIP]
> The “right” CRS is the one that’s **documented** and **repeatable**.

Minimum expectations:

- ✅ Record the **original CRS** (as-captured)
- ✅ Record the **target CRS** used for publishing (typically WGS84-based for web viewers)
- ✅ Keep the **transform** (matrix/anchor/origin) as a tracked file in `georef/transforms/`
- ✅ If you used GCPs, store:
  - residuals / RMS error
  - coordinate source (survey, public control, derived)

---

## 🧱 Asset Handling Rules

### ✅ Do
- ✅ Keep source files **unchanged** (append-only policy)
- ✅ Use versioned session folders (`session-YYYYMMDD_*`)
- ✅ Prefer **lossless** source textures (TIFF/EXR/PNG) in `source/`
- ✅ Document every tool and major step in `docs/qa_notes.md`
- ✅ Keep licenses + permissions adjacent and easy to audit

### 🚫 Don’t
- 🚫 Don’t “clean up” source by overwriting originals
- 🚫 Don’t put final optimized assets here
- 🚫 Don’t mix unrelated landmarks (one slug = one provenance chain)
- 🚫 Don’t store unlicensed content without a permission trail

---

## 🔁 Pipeline Overview (Source → Shipping)

```mermaid
flowchart LR
  A[📥 source/ (raw upstream)] --> B[🧪 processing (tools/pipeline)]
  B --> C[🧱 models/ (glb / tilesets)]
  B --> D[🖼️ textures/ (runtime-ready)]
  C --> E[🌐 web runtime]
  D --> E
  A --> F[🧾 citations + licenses]
  F --> E
```

---

## ✅ QA Checklist (Before Promoting to Runtime)

- [ ] `manifests/source.manifest.yaml` exists + filled
- [ ] `manifests/checksums.sha256` exists + matches
- [ ] License path is auditable (`../licenses/README.md`)
- [ ] Citations are complete (`../citations/README.md`)
- [ ] CRS + units documented
- [ ] Transform/anchor file present if georeferenced
- [ ] No PII / sensitive material accidentally included
- [ ] Any large binaries tracked appropriately (LFS/DVC/pointers as per repo policy)

---

## 🧩 Slug Rules (Reminder)

`<landmark_slug>` should be:

- lowercase
- hyphen-separated
- stable over time (renames break provenance chains)

Examples:
- `monument-rock`
- `old-capitol-building`
- `fort-larned-blockhouse`

---

## 📎 Notes

- This directory is intentionally **tool-agnostic**: it supports photogrammetry, LiDAR, CAD, hybrid workflows.
- If you must package raw inputs (e.g., for transfer), prefer **archives inside `source/`** with checksums and a manifest entry.

---
