---
title: "🧩 Tile 0 (Root) — <tileset-id>"
status: "draft"
version: "v0.1.0"
last_updated: "2026-01-17"
doc_kind: "Asset README"
asset_kind: "3d-tiles"
tileset_id: "<tileset-id>"
tile_id: "0"
path: "web/assets/maps/3d/tilesets/<tileset-id>/tiles/0/"
license: "See tileset-level licensing (data ≠ code)"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
provenance:
  source_dataset_id: "<catalog-id | stac-item-id | dcat-id>"
  generated_by: "<pipeline/tool>"
  generated_at: "<ISO-8601 UTC timestamp>"
  git_commit: "<commit-sha>"
doc_uuid: "urn:kfm:asset:3d-tiles:<tileset-id>:tile:0:readme:v0.1.0"
---

<p align="center">
  <img alt="KFM" src="https://img.shields.io/badge/KFM-3D%20Tileset-2ea44f?style=for-the-badge" />
  <img alt="Tile" src="https://img.shields.io/badge/tile-0-blue?style=for-the-badge" />
  <img alt="Classification" src="https://img.shields.io/badge/classification-open-brightgreen?style=for-the-badge" />
  <img alt="Status" src="https://img.shields.io/badge/status-draft-yellow?style=for-the-badge" />
</p>

# 🧩 Tile 0 (Root) — `<tileset-id>`

> [!IMPORTANT]
> This directory is a **public web asset** (served directly by the front-end).  
> ✅ Only publish **open/public** + **fully redacted** outputs here.  
> ❌ Never commit restricted locations, personal data, or culturally sensitive coordinates.

---

## 📍 You are here

`web/assets/maps/3d/tilesets/<tileset-id>/tiles/0/`

```text
📁 web/
  📁 assets/
    📁 maps/
      📁 3d/
        📁 tilesets/
          📁 <tileset-id>/
            📄 tileset.json
            📁 tiles/
              📁 0/        👈 this folder (root / LOD0)
              📁 1/
              📁 2/
              …
```

---

## 🧾 Quick facts (fill these in)

| Field | Value |
|---|---|
| Tileset ID | `<tileset-id>` |
| Tile ID | `0` |
| Role | Root / bootstrap tile (lowest LOD) |
| Content type | `<b3dm | pnts | i3dm | glb | external tileset>` |
| Coverage | `<bbox/region summary>` |
| Height units | `meters` (recommended) |
| CRS notes | `WGS84 alignment (source), georeferenced for 3D` |
| Source dataset | `<catalog-id>` |
| Last generated | `<generated_at>` |
| Generator | `<pipeline/tool + version>` |

---

## 🎯 Purpose

Tile `0` is the **entry point** for this tileset. It should:

- 🚀 Load quickly (first paint for the 3D view)
- 🧭 Cover the full extent of the tileset (coarse representation)
- 🧩 Refine into child tiles as the camera approaches / zooms in
- 🧾 Provide enough metadata hooks for provenance + governance

---

## 🧠 What “Tile 0” represents

In a typical 3D Tiles hierarchy, `tileset.json` points at a **root** tile that:
- Has the broadest bounding volume
- Has the highest geometric error (coarsest LOD)
- Exists primarily to **bootstrap** streaming + refinement

> [!NOTE]
> Some generators store the “root” as content in this folder; others make Tile `0` an **external tileset link**.  
> Either way: this folder documents the **logical root** for `<tileset-id>`.

---

## 📦 Expected contents

Minimum (recommended):
- ✅ A root content payload (example names below)
- ✅ A local metadata sidecar describing what’s inside

Common patterns:
- `0.b3dm` (batched 3D model)
- `0.pnts` (point cloud)
- `0.i3dm` (instanced models)
- `0.glb` / `0.gltf` (if your loader supports direct glTF at this level)

Recommended sidecars (choose what matches your pipeline):
- `tile.meta.json` — local tile facts (counts, bbox/region, CRS, generator, license)
- `SHA256SUMS` — integrity checks for the folder payload
- `preview.webp` — tiny thumbnail for docs/UI

Example **tile.meta.json** shape (suggested):
```json
{
  "tileset_id": "<tileset-id>",
  "tile_id": 0,
  "role": "root",
  "content_uri": "0.pnts",
  "stats": {
    "bytes": 1234567,
    "points": 987654,
    "triangles": null
  },
  "spatial": {
    "bbox_wgs84": [-102.05, 36.99, -94.59, 40.00],
    "vertical_units": "meters"
  },
  "provenance": {
    "source_dataset_id": "<catalog-id>",
    "generated_by": "<pipeline/tool>",
    "generated_at": "<ISO-8601 UTC>",
    "git_commit": "<commit-sha>"
  },
  "governance": {
    "care_label": "Public",
    "sensitivity": "public",
    "classification": "open",
    "redactions_applied": ["<none | generalized_coords | attribute_removed | ...>"]
  }
}
```

---

## 🛰️ How KFM uses this (runtime intent)

KFM’s front-end mapping stack is designed to support:
- 🗺️ **2D** interactive maps (e.g., MapLibre/Leaflet)
- 🌍 Optional **3D** visualization (e.g., CesiumJS)
- 🧱 Streaming 3D geospatial content via the **3D Tiles** standard

This folder exists so the web client can load `<tileset-id>` as a **3D layer** when the 3D view is enabled.

> [!TIP]
> Keep Tile `0` light. It’s the “first impression” tile that should appear fast, then refine.

---

## 🧾 Provenance & catalog linkage (evidence-first)

KFM’s ingestion philosophy expects:
- common spatial reference handling (reprojection tracked)
- metadata retained for traceability
- catalog-first thinking (dataset record before narrative)

**Do this for Tile `0`:**
- Link back to the dataset’s catalog record (STAC/DCAT-style ID)
- Record generator + timestamp + commit SHA
- Track original CRS + transforms in provenance (even if served as web-friendly output)

---

## 🧭 CRS, alignment, and units

Recommended conventions:
- 🌐 **WGS84 alignment** for web-facing geospatial consistency
- 🧱 3D tile payload uses the georeferencing approach required by your 3D Tiles pipeline
- 📏 Elevation/height units should be explicit (recommend: **meters**)

> [!NOTE]
> If your source data used a Kansas-specific projection (State Plane / Lambert), ensure the transform is captured in provenance, even if the output is “web standard”.

---

## 🔒 Governance: FAIR+CARE + redaction rules

This project treats governance metadata as **first-class**.

**Hard rules for anything served from `web/assets/…`:**
- ✅ Only publish content classified as `open/public`
- ✅ Apply redaction/generalization at every layer (data → metadata → API → UI)
- ❌ Never “loosen” restrictions downstream (no output less restricted than input)

If this tileset contains anything potentially sensitive (e.g., sacred sites, private landholder data, protected resources):
- Move it behind the API / authenticated delivery
- Generalize or remove precise coordinates
- Document the redaction in `tile.meta.json` + the dataset’s catalog record

---

## ✅ QA / Validation checklist (Tile 0)

### Visual + functional
- [ ] Loads in the 3D viewer without errors
- [ ] Correctly refines into child tiles (no “stuck” LOD)
- [ ] Bounding volume is sane (no huge offsets / wrong hemisphere)
- [ ] Z/height looks correct (no inverted terrain / massive vertical scaling)

### Provenance + governance
- [ ] `tile.meta.json` exists and includes `source_dataset_id`, `generated_by`, `generated_at`, `git_commit`
- [ ] Classification fields are present and correct (`open/public`)
- [ ] If redaction was required, it is documented (`redactions_applied` not empty)

### Integrity
- [ ] Checksums updated

```bash
# Linux
sha256sum * > SHA256SUMS

# macOS
shasum -a 256 * > SHA256SUMS
```

---

## ♻️ Regeneration notes (don’t hand-edit binaries)

> [!WARNING]
> Treat `.b3dm/.pnts/.i3dm` as **build artifacts**.  
> Regenerate via pipeline; do not edit by hand.

When regenerating:
1. Update `generated_at`, `git_commit`, and tool version
2. Recompute checksums
3. Confirm governance classification still matches source inputs
4. Smoke-test in the viewer (Tile `0` should still load first)

---

## 🔗 Nearby files

- `../../tileset.json` — tileset root manifest
- `../README.md` — tiles folder README (if present)
- `../../README.md` — tileset README (if present)

---

## 📚 Reference pointers (repo-root paths)

These are useful when documenting provenance/contracts in KFM:
- `docs/data/contracts/examples/README.md`
- `docs/governance/` (review gates, sensitivity rules, etc.)
- `data/catalog/` (STAC/DCAT-style dataset records, if present)
- `data/prov/` (PROV lineage, if present)

---
