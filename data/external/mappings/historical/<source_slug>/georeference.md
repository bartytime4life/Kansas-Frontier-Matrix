# 🧭 Georeferencing — `<source_slug>`

![status](https://img.shields.io/badge/status-draft-informational)
![artifact](https://img.shields.io/badge/artifact-COG%20%2B%20STAC%20%2B%20PROV-blue)
![pipeline](https://img.shields.io/badge/pipeline-Raw→Processed→Catalog%2FProv→DB→API→UI-success)

> [!IMPORTANT]
> **This file is the per-source “how + what we did” record** for georeferencing historical map scans tied to `<source_slug>`.  
> Keep it updated as you add/redo map sheets so the pipeline remains reproducible and provenance-linked.

---

## 🧾 What belongs here

This folder holds **external historical map inputs** and the working artifacts needed to produce **georeferenced outputs** that are ready to be cataloged and used downstream.

- ✅ Raw scanned imagery stays immutable (keep originals).
- ✅ Intermediates live in `work/`.
- ✅ Final outputs live in `processed/` *and/or* the repo’s canonical `data/processed/...` location.
- ✅ “Published” means: **data + STAC + DCAT + PROV** are all present and linked.

---

## 📁 Recommended layout

> [!TIP]
> Create only what you need now; the rest can land as you publish.

```text
📁 data/
└─ 📁 external/
   └─ 📁 mappings/
      └─ 🏛️ historical/
         └─ 📁 <source_slug>/                              🗺️ georeferencing package (per upstream source)
            ├─ 📝 georeference.md                           👈 you are here (workflow + conventions + QA bar)
            ├─ 📁 raw/                                      🔒 immutable scans (as-downloaded / never edit)
            │  ├─ 🖼️ <sheet_id>__orig.tif                    📦 original scan (TIFF)
            │  └─ 🖼️ <sheet_id>__orig.jpg                    📦 original scan (JPEG)
            ├─ 📁 work/                                     🧰 editable intermediates (projects, GCPs, crops)
            │  └─ 📁 <sheet_id>/                             🧷 per-sheet workspace
            │     ├─ 📁 qgis/                                🧰 QGIS georef projects
            │     │  ├─ 📄 <sheet_id>.qgz                    🗺️ project file
            │     │  └─ 📄 <sheet_id>.qgd                    🧭 georeferencer sidecar
            │     ├─ 📁 gcps/                                📍 ground control points (GCPs)
            │     │  ├─ 📄 <sheet_id>__gcps.csv              🧾 tabular GCPs (x/y + lon/lat + residuals)
            │     │  └─ 📄 <sheet_id>__gcps.points           📍 QGIS GCP points file
            │     └─ 📁 preproc/                             🧼 preprocessing outputs (crops, de-skew, contrast)
            │        └─ 🖼️ <sheet_id>__cropped.tif           ✂️ cropped/cleaned working raster
            ├─ 📁 processed/                                 ✅ georeferenced deliverables (downstream-ready)
            │  ├─ 🧊 <sheet_id>.cog.tif                       🚀 Cloud Optimized GeoTIFF (COG) + overviews
            │  └─ 🖼️ <sheet_id>__thumb.jpg                   👀 quick thumbnail for catalog/cards
            ├─ 📁 qa/                                        🔍 QA screenshots + checks
            │  └─ 🖼️ <sheet_id>__overlay_check.png           ✅ overlay sanity check (modern basemap alignment)
            └─ 📁 hashes/                                    ◻️ optional: checksums for auditability
               ├─ 🔐 raw__sha256.txt                          🔐 hashes for raw scans
               └─ 🔐 processed__sha256.txt                    🔐 hashes for processed deliverables
```

---

## 🔎 Source record

Fill this in *before* georeferencing (or as soon as you can).

| Field | Value |
|---|---|
| Source name | `<human_readable_source_name>` |
| Provider / archive | `<provider>` |
| Source URL(s) | `<url(s)>` |
| Accessed / downloaded | `YYYY-MM-DD` |
| Map publication year (or range) | `<YYYY or YYYY–YYYY>` |
| Map scale (if known) | `<e.g., 1:24,000>` |
| Stated projection / datum (if printed) | `<e.g., NAD27 / ...>` |
| Geographic coverage | `<short description>` |
| License / rights notes | `<public domain / CC / unknown / restricted>` |
| Notes | `<anything weird about the scan>` |

> [!NOTE]
> If the map is copyrighted or the license is unclear, treat redistribution as **restricted until verified**. You can still do internal georeferencing, but catalog/publish decisions must respect the rights status.

---

## 🎯 Deliverables

For each map sheet (`<sheet_id>`), aim to produce:

- **COG raster**: `<sheet_id>.cog.tif`
- (Optional) **thumbnail**: `<sheet_id>__thumb.jpg`
- **GCP export**: `<sheet_id>__gcps.csv` (pixel + world coords)
- **Georeferencer project**: QGIS `.qgz` + `.points`/GCP file
- **QA overlay screenshot**: `<sheet_id>__overlay_check.png`
- **Catalog + provenance** (canonical locations):
  - STAC Item (links to the COG)
  - DCAT dataset entry (discovery + license + distribution)
  - PROV bundle (inputs → steps → outputs)

---

## 🧭 Spatial reference policy

> [!WARNING]
> **Datums and ellipsoids matter.** If your reference layer and your historic map are effectively in different datums, they can appear “close but wrong.”

### Pick your working CRS (practical rule)

1. **If the historic map includes a graticule** (lat/long ticks) or clearly states its datum/projection:  
   - Use that information (record it in the log), then choose a target CRS that supports your intended use.
2. **If the map has no CRS info**:  
   - Choose a stable target CRS for KFM consumption (commonly WGS84 / EPSG:4326 for interchange) and document the choice.

### Always record:
- `target_crs` (EPSG code)
- `source_datum/projection` (if known)
- Any reprojection/transform steps taken

---

## 📌 GCP strategy

**Goal:** distribute control points so the warp is stable across the whole sheet.

✅ Prefer:
- road intersections that still exist
- courthouse squares / town centers
- bridge crossings that persisted
- rail junctions still visible
- section corners / survey grid intersections (when reliable)
- graticule intersections (best when printed clearly)

⚠️ Avoid:
- riverbanks/meanders (they move)
- shorelines (they shift)
- symbols with unclear centers
- decorative cartouches / borders

**Minimum suggested:**
- Small/local map: 8–12 well-spread GCPs  
- Larger/warped sheets: 15–30 GCPs (add more near edges/corners)

---

## 🛠️ Workflow

> [!TIP]
> Keep the “interactive” work (QGIS) **exportable** (GCP tables + parameters) so the pipeline can be rerun without guesswork.

### Option A — QGIS (interactive Georeferencer)

1. Put the original scan in `raw/` (immutable).
2. If you need to crop/deskew/levels-adjust, write outputs to `work/<sheet_id>/preproc/`.
3. Open **QGIS → Raster → Georeferencer**.
4. Set:
   - Target CRS: `<EPSG:xxxx>`
   - Transformation: `<Helmert / Polynomial 1/2/3 / TPS>` (pick appropriate)
   - Resampling: `<Nearest / Bilinear / Cubic>` (maps usually Bilinear/Cubic)
   - Output: `processed/<sheet_id>.tif` (or temp in `work/` then finalize)
5. Add GCPs and **save GCPs** to:  
   `work/<sheet_id>/gcps/<sheet_id>__gcps.points` (or equivalent)
6. Start georeferencing.
7. Export your GCP list to CSV:  
   `work/<sheet_id>/gcps/<sheet_id>__gcps.csv`
8. Convert final GeoTIFF to **COG** (see Option B recipe) → `processed/<sheet_id>.cog.tif`
9. Create `qa/<sheet_id>__overlay_check.png` (screenshot of overlay on reference basemap)

**Record in the per-sheet log (below):**
- transformation type + order
- resampling method
- number of GCPs
- RMS/residual summary (if available)

---

### Option B — GDAL (scriptable)

<details>
<summary><strong>📦 Minimal CLI recipe (template)</strong></summary>

```bash
# 0) (optional) compute hashes (audit trail)
sha256sum "raw/<sheet_id>__orig.tif" >> hashes/raw__sha256.txt

# 1) If you have GCPs, embed them (example placeholders)
# gdal_translate -of GTiff \
#   -gcp <px> <py> <x> <y> \
#   -gcp <px> <py> <x> <y> \
#   raw/<sheet_id>__orig.tif work/<sheet_id>/<sheet_id>__gcps_embedded.tif

# 2) Warp to target CRS (template)
# gdalwarp -t_srs EPSG:<xxxx> \
#   -r cubic \
#   -co COMPRESS=DEFLATE -co TILED=YES \
#   work/<sheet_id>/<sheet_id>__gcps_embedded.tif work/<sheet_id>/<sheet_id>__warped.tif

# 3) Convert to Cloud-Optimized GeoTIFF (COG)
# gdal_translate -of COG \
#   -co COMPRESS=DEFLATE \
#   -co LEVEL=9 \
#   work/<sheet_id>/<sheet_id>__warped.tif processed/<sheet_id>.cog.tif

sha256sum "processed/<sheet_id>.cog.tif" >> hashes/processed__sha256.txt
```

</details>

> [!NOTE]
> The CLI is here to make the workflow **repeatable**. Even if you georeference in QGIS, capture enough details (GCP export + parameters) so a script can reproduce the output.

---

### Option C — KFM automation hooks (if present)

If the repo includes automation like `georef_map.py` / `pack_kmz.py`, prefer using it once control points are known.

- Store the canonical GCP file in `work/<sheet_id>/gcps/`
- Run via Makefile/CLI (project standard)
- Log the command + config used in the per-sheet record

---

## ✅ QA & acceptance checklist

For each sheet:

- [ ] Overlay check against a modern reference layer looks reasonable (major rivers/roads/towns line up).
- [ ] GCPs are well-distributed (not clustered).
- [ ] Residuals are not dominated by one corner/edge.
- [ ] No obvious shear/rotation artifacts unless expected from the original.
- [ ] Output is a **COG** and loads quickly in typical GIS/web tooling.
- [ ] CRS is recorded correctly (and matches metadata).
- [ ] Rights/license notes are recorded.

> [!TIP]
> If you can’t get alignment “perfect,” record the **uncertainty** (e.g., “±250m expected due to poor scan + inconsistent symbols”).

---

## 📚 Metadata & provenance requirements

> [!IMPORTANT]
> Treat the georeferenced raster as a **first-class evidence artifact**: it must be stored, cataloged, and provenance-traced before use in the graph/UI.

### STAC (spatial + temporal indexing)
Include (at minimum):
- bbox + footprint geometry
- time range / publication year (or best estimate)
- source attribution + license
- links to the COG asset
- processing summary (e.g., “cropped + georeferenced using N control points”)

### DCAT (dataset discovery)
At minimum:
- title, description, license, keywords
- distributions that link to STAC and/or direct asset downloads

### PROV (lineage)
Must connect:
- raw scan(s) → intermediate work → processed COG(s)
- include:
  - agent (person/software)
  - timestamps
  - parameters/config
  - run id / commit hash (if available)

---

## 🗂️ Per-sheet log (fill this out)

> [!TIP]
> One row per georeferenced output (sheet/page).

| sheet_id | year | raw_input | target_crs | gcp_count | transform | resample | RMS / notes | output_cog | qa_artifact | stac_item | prov_bundle |
|---|---:|---|---|---:|---|---|---|---|---|---|---|
| `<sheet_id>` | `<YYYY>` | `raw/<...>` | `EPSG:<...>` | `<N>` | `<...>` | `<...>` | `<...>` | `processed/<...>.cog.tif` | `qa/<...>.png` | `<path-or-id>` | `<path-or-id>` |

---

## 🧩 GCP table template (CSV)

Save as: `work/<sheet_id>/gcps/<sheet_id>__gcps.csv`

```csv
gcp_id,pixel_x,pixel_y,world_x,world_y,world_z,notes
1,,,,,, "e.g., road intersection / graticule"
2,,,,,, 
3,,,,,, 
```

---

## 🔄 Change log

| Date | Who | Change |
|---|---|---|
| `YYYY-MM-DD` | `<name>` | created runbook |
| `YYYY-MM-DD` | `<name>` | added sheets `<sheet_id>, <sheet_id>` |

---

## 📎 References (project-local)

- `docs/MASTER_GUIDE_v13.md` (pipeline + catalog expectations)
- `docs/standards/` (STAC/DCAT/PROV profiles)
- `mcp/sops/georeference_map.md` (if present; canonical SOP)
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf`
- `Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `KFM- python-geospatial-analysis-cookbook-...pdf`

