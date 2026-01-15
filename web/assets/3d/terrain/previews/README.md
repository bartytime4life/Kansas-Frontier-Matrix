# 🌄 Terrain previews

![KFM](https://img.shields.io/badge/KFM-terrain%20previews-0b7285?style=flat)
![Web](https://img.shields.io/badge/web-static%20assets-1f6feb?style=flat)
![3D](https://img.shields.io/badge/3D-terrain%20%26%20globe-6f42c1?style=flat)
![Provenance](https://img.shields.io/badge/provenance-first%20class%20metadata-2da44e?style=flat)

Static, lightweight preview images for **terrain datasets** used by the KFM web UI (catalog cards, layer pickers, and any 3D terrain selection flows).

> [!IMPORTANT]
> KFM is **contract-first + provenance-first**: anything surfaced in the UI should be traceable back to a cataloged dataset and its processing lineage. Previews are “just images,” but they still must **map cleanly to a dataset ID** (no mystery thumbnails, no orphan assets). ✅

---

## 🧭 Folder context

```text
web/
└─ assets/
   └─ 3d/
      └─ terrain/
         └─ previews/   👈 you are here
```

---

## ✅ What belongs here

- 🖼️ **Preview images** for terrain datasets (optimized, small)
- 🧾 Optional **sidecar metadata** per preview (recommended) to keep generation reproducible + auditable
- 🧩 Optional shared placeholders (e.g., “preview not available”)

---

## 🚫 What does not belong here

- ❌ Raw DEMs, GeoTIFFs/COGs, quantized-mesh, or 3D Tiles payloads  
  (those should be streamed/served and referenced via the dataset catalog; this folder is for *UI thumbnails*)
- ❌ Unattributed screenshots or images with unclear origin/licensing
- ❌ “Temporary” debug captures that aren’t wired to a dataset ID

---

## 🏷️ Naming conventions

Use a predictable naming convention so the UI/tooling can resolve previews deterministically.

**Recommended pattern**

`<datasetId>__<variant>__<width>x<height>.<ext>`

**Examples**

- `kansas-lidar-dem__hillshade__640x360.webp`
- `kansas-lidar-dem__slope__512x512.png`
- `kansas-lidar-dem__coverage__640x360.webp`
- `kansas-lidar-dem__wireframe__640x360.webp`

### Dataset IDs

- ✅ Must match the dataset’s canonical identifier from the **data contract / catalog metadata**.
- ✅ Prefer **kebab-case**.
- ✅ Keep IDs stable over time (renames ripple everywhere).

> [!NOTE]
> If the project standardizes dataset IDs in a registry, treat that registry as the source of truth and mirror it here exactly.

---

## 🧾 Sidecar preview metadata

While the image itself is a static asset, KFM’s philosophy leans toward **reproducibility** and **traceability**. A sidecar file makes it easy to regenerate previews, audit rendering settings, and connect the thumbnail back to the catalog.

**Recommended sidecar name**

`<datasetId>__<variant>__<width>x<height>.preview.json`

### Minimal recommended fields

- `datasetId` (string)
- `variant` (string)
- `image` (string; filename or relative path)
- `bboxWgs84` (array `[minLon, minLat, maxLon, maxLat]`)
- `render` (object; shading mode, vertical exaggeration, etc.)
- `camera` (object; if captured from Cesium/3D viewer)
- `provenance` (object; pointers to dataset contract / STAC / processing notes)
- `license` (object; SPDX + attribution string)

<details>
<summary>📦 Example <code>.preview.json</code></summary>

```json
{
  "datasetId": "kansas-lidar-dem",
  "variant": "hillshade",
  "image": "kansas-lidar-dem__hillshade__640x360.webp",
  "bboxWgs84": [-102.051, 36.993, -94.588, 40.003],

  "render": {
    "mode": "hillshade",
    "verticalExaggeration": 1.0,
    "sunAzimuthDeg": 315,
    "sunAltitudeDeg": 45
  },

  "camera": {
    "engine": "cesium",
    "lonDeg": -98.5,
    "latDeg": 38.5,
    "heightMeters": 650000,
    "headingDeg": 0,
    "pitchDeg": -45,
    "rollDeg": 0
  },

  "provenance": {
    "dataContractRef": "data/contracts/terrain/kansas-lidar-dem.json",
    "stacRef": "data/catalog/terrain/kansas-lidar-dem/item.json",
    "generatedBy": {
      "tool": "manual-screenshot",
      "operator": "kfm-maintainer",
      "timestampUtc": "2026-01-15T00:00:00Z",
      "notes": "Captured in 3D viewer with consistent lighting + no UI chrome."
    }
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Derived from the referenced dataset sources (see data contract)."
  }
}
```

</details>

---

## 🎛️ Suggested preview variants

These are *recommendations* (not requirements) that map well to terrain/DEM-style layers.

| Variant 🧩 | Best for 🎯 | Notes |
|---|---|---|
| `hillshade` | Human-readable terrain shape | Works great even in grayscale |
| `slope` | Understanding steepness | Consistent legend helps a lot |
| `aspect` | Orientation analysis | Consider a standard color wheel |
| `color-relief` | “Marketing” / overview | Keep palette consistent across datasets |
| `coverage` | QA + completeness | Highlights missing tiles / edge gaps |
| `wireframe` | QA for mesh/LOD | Reveals triangulation + artifacts |

> [!TIP]
> Keep at least one preview variant that remains interpretable on small cards (often `hillshade`).

---

## 🧰 How to add or update a preview

1. **Confirm the dataset is cataloged** 🗂️  
   The dataset should already exist in the project’s catalog/contract system (with source + license + spatial extent).

2. **Capture/render the preview** 📸  
   - Use a consistent camera angle/zoom for comparable datasets.
   - Avoid UI chrome (no menus, cursors, or debug overlays).
   - Prefer a view that communicates the dataset’s “shape” quickly.

3. **Export in a web-friendly format** 🧼  
   - Prefer **WebP** for best size/quality (if supported by the build pipeline).
   - PNG is fine for crisp/flat graphics.
   - JPEG only when photographic texture is dominant.

4. **Optimize the file** 📦  
   Target small sizes so the catalog stays snappy:
   - ✅ Aim: **< 250 KB** each (lower is better)
   - ✅ Avoid huge dimensions that won’t be visible in UI

5. **Create/update the `.preview.json` sidecar** 🧾  
   Make sure `datasetId` matches the catalog ID exactly.

6. **Wire it to the catalog / layer registry** 🔗  
   Wherever the dataset “contract” or registry stores UI metadata, ensure it points to this preview file path.

7. **Sanity check in the UI** 👀  
   Verify:
   - correct image loads,
   - correct dataset mapping,
   - no broken paths,
   - no license surprises.

---

## ⚖️ Licensing and attribution

Previews can still trigger licensing obligations because they are derived from data products.

- ✅ Ensure the underlying dataset license allows redistribution of derived imagery (or that the project’s usage is compliant).
- ✅ Put attribution in the dataset’s metadata/contract (and optionally mirror it in the sidecar).
- ✅ If a dataset is restricted, consider a **generic placeholder** preview rather than a derived image.

---

## 🔎 Troubleshooting

- **Preview looks “flat”**  
  Increase hillshade contrast slightly or adjust sun altitude (keep consistent across datasets).

- **Preview doesn’t match the terrain in 3D view**  
  Make sure the capture is from the same dataset version and that vertical exaggeration wasn’t changed.

- **Colors differ between previews**  
  Standardize palettes/legends for `slope`, `aspect`, and `color-relief`.

---

## 📚 References

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design  [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- MARKDOWN_GUIDE_v13.md.gdoc  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
