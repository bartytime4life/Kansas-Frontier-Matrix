# 🗺️ Map Preview Images (Thumbnails) — `web/assets/media/maps/previews/`

![role](https://img.shields.io/badge/role-thumbnails%20%26%20overviews-blue)
![formats](https://img.shields.io/badge/formats-webp%20%7C%20png%20%7C%20jpg-success)
![performance](https://img.shields.io/badge/perf-optimized%20assets-important)
![provenance](https://img.shields.io/badge/provenance-required-critical)

> [!NOTE]
> This folder contains **lightweight preview images** used by the **web map UI** (catalog cards, layer details panels, story cards).
> These images are **visual hints** for humans — **not** the authoritative geospatial datasets.

---

## 📦 Folder context (where this fits)

```text
web/ 🌐
└── assets/ 🧰
    └── media/ 🖼️
        └── maps/ 🗺️
            ├── previews/ 👈 you are here
            └── (tiles, full-res, legends, etc.)
```

> [!IMPORTANT]
> Treat everything in this directory as **public web content**. If it shouldn’t be public, it shouldn’t be here.

---

## ✅ What belongs in `previews/`

- 🧩 **Layer thumbnails** for dataset/layer cards (fast scan, instant recognition)
- 🗺️ **Overview images** (optional) for “big picture” previews
- 🧯 **Placeholder previews** for missing/restricted layers (consistent UX)
- 🧾 **Small legend snippets** (only if absolutely needed and readable at small sizes)

---

## 🚫 What does *not* belong here

- 🗄️ Full-resolution scans, GeoTIFFs/COGs, GeoJSON, shapefiles, tiles, etc.
- 🧪 Raw screenshots that haven’t been optimized (multi‑MB images)
- 🕵️ Anything with unclear licensing/provenance or missing attribution
- 🔒 Sensitive/restricted imagery (use placeholders instead)

---

## 🧭 Why previews matter (KFM principle alignment)

KFM is designed so that **anything shown in the UI should be traceable** (source + license + processing steps).  
Previews are part of the UI experience, so they should follow the same rule:

- ✅ preview exists **because** a dataset exists
- ✅ preview is **derived** from the dataset (or an explicitly licensed representative rendering)
- ✅ preview is **registered** in metadata so the UI can find it
- 🚫 no “mystery thumbnails” with unknown origin

---

## 📛 Naming conventions

Use stable, predictable names so the UI and metadata can reference them without guesswork.

### Recommended pattern ⭐

`<dataset-id-or-slug>__<role>.<ext>`

- `<dataset-id-or-slug>` → **must match** the catalog ID/slug used in metadata
- `<role>` → `thumb` | `overview` | `placeholder` | `legend`
- `<ext>` → `webp` (preferred) | `png` | `jpg`

**Examples**
- `kansas_territory_1854__thumb.webp`
- `usgs_topo_1920__overview.jpg`
- `_missing__placeholder.webp`
- `kansas_railroads_1890__legend.png`

### Optional: size suffix (only if you truly need multiple sizes)

`<dataset>__thumb@256.webp`  
`<dataset>__thumb@512.webp`

> [!TIP]
> If you introduce size variants, keep one as the “default” (`__thumb.webp`) and generate others only when needed.

---

## 📐 Image specs

These are **defaults** to keep things consistent and fast.

| Role | Target size | Aspect | Max file size | Preferred format | Notes |
|---|---:|---:|---:|---|---|
| `thumb` | 512×512 | 1:1 | ≤ 200 KB | WebP | primary UI thumbnail |
| `overview` | 1200×675 | 16:9 | ≤ 500 KB | WebP/JPG | optional hero/cover |
| `legend` | ≤ 512px wide | free | ≤ 150 KB | PNG/WebP | only if legible |
| `placeholder` | 512×512 | 1:1 | ≤ 100 KB | WebP | “missing/restricted” |

**General rules**
- ✅ Use **sRGB** color profile
- ✅ Prefer **WebP** for performance
- ✅ Use **PNG** only when you need crisp transparency (or alpha in WebP)
- ✅ Keep edges clean (avoid fuzzy resampling artifacts)

---

## 🎨 Visual consistency rules (so thumbnails look like one “system”)

- 🧭 **North-up** unless there’s a compelling reason not to.
- 🟦 Use a **consistent crop strategy**:
  - Kansas-wide when the layer is statewide
  - Representative AOI for local/municipal datasets
- 🧼 Avoid tiny labels/legends that become unreadable at small sizes.
- 🧩 For vector layers: prefer a neutral background + the layer styling used in the UI.
- 🕰️ For time-enabled datasets: choose a **representative time slice** and document it (in metadata notes).

---

## 🧾 Provenance, licensing, and attribution

> [!IMPORTANT]
> If the dataset’s license or provenance is unclear, **do not ship a preview**. Fix the metadata first.

**Rules of thumb**
- 🧷 A preview should be tied to a **cataloged dataset** (STAC / “data contract” style metadata).
- 🧾 Attribution must be derivable from metadata (source, license, processing notes).
- 🔒 Restricted datasets should use:
  - a **placeholder preview**, and
  - UI copy that explains why it’s restricted.

---

## 🔗 Registering previews in metadata (recommended)

If your dataset is represented as a STAC-like Item, add an asset entry (common roles: `thumbnail`, `overview`).

```json
{
  "assets": {
    "thumbnail": {
      "href": "web/assets/media/maps/previews/kansas_territory_1854__thumb.webp",
      "type": "image/webp",
      "roles": ["thumbnail"],
      "title": "Kansas Territory (1854) — preview thumbnail"
    },
    "overview": {
      "href": "web/assets/media/maps/previews/kansas_territory_1854__overview.webp",
      "type": "image/webp",
      "roles": ["overview"],
      "title": "Kansas Territory (1854) — overview preview"
    }
  }
}
```

> [!NOTE]
> The UI can use these references to show a dataset card + details panel that includes **description + metadata + preview**.

---

## 🛠️ Generating previews

Pick the simplest approach that keeps outputs reproducible.

<details>
<summary><strong>Option A — From a raster (COG/GeoTIFF) via GDAL</strong></summary>

```bash
# 1) (Optional) Warp to Web Mercator for consistent preview rendering
gdalwarp -t_srs EPSG:3857 -r bilinear -multi -wo NUM_THREADS=ALL_CPUS \
  input.tif /tmp/layer_3857.tif

# 2) Downscale to a thumbnail-friendly size
gdal_translate -of PNG -outsize 512 512 -r bilinear \
  /tmp/layer_3857.tif /tmp/preview.png

# 3) Convert to WebP (preferred)
cwebp -q 82 /tmp/preview.png \
  -o web/assets/media/maps/previews/<dataset-slug>__thumb.webp
```

</details>

<details>
<summary><strong>Option B — Screenshot from the web viewer (MapLibre styling)</strong></summary>

1. Load the layer in the viewer using the intended style rules.
2. Zoom to a representative extent (Kansas-wide or AOI).
3. Screenshot at **2× resolution**, then downscale + compress to the target size.

</details>

<details>
<summary><strong>Option C — Vector layers</strong></summary>

- Prefer rendering with the same style logic used in the UI.
- If you export from a GIS tool (e.g., QGIS), keep it simple:
  - neutral background
  - strong, readable geometry
  - minimal labels

</details>

---

## ✅ PR checklist (copy/paste into your PR)

- [ ] Filename matches convention (`<dataset>__thumb.webp`, etc.)
- [ ] File size is within budget (thumb ≤ 200 KB)
- [ ] Looks good at **~128px wide** (no illegible clutter)
- [ ] Preview is **registered in metadata** (STAC/data contract)
- [ ] License + attribution are clear (no “mystery layer”)
- [ ] Placeholder used for restricted/missing datasets

---

## 🧯 Troubleshooting

**My preview looks blurry**
- Export at **2×** and downscale, or increase the render resolution before compression.

**My preview has a weird color shift**
- Ensure the output is **sRGB**, and avoid embedded wide-gamut profiles.

**The UI can’t find my preview**
- Confirm the path in metadata exactly matches the file path (case-sensitive).
- Prefer lowercase filenames and consistent slugging.

---

## 🔗 Related jump points

- `web/` 🌐 — front-end app (Map UI + story UI + static assets)
- `data/` 🗄️ — authoritative datasets + pipelines + catalogs
- `docs/data/contracts/` 🧾 — metadata rules (source, license, processing, etc.)
