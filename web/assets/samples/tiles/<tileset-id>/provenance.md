---
id: "<tileset-id>"
title: "<Human-friendly tileset name>"
status: "sample" # sample | draft | governed | deprecated
artifact_type: "tileset" # tileset | style | sprite | glyphs | terrain | 3dtiles
kfm:
  stage: "ui_asset" # ui_asset | cataloged_asset | api_asset
  # If this is promoted beyond "samples", link the governed records here:
  stac_asset: "<path-or-id>"     # e.g., data/catalog/stac/<...>.json
  dcat_dataset: "<path-or-id>"   # e.g., data/catalog/dcat/<...>.json
  prov_record: "<path-or-id>"    # e.g., data/catalog/prov/<...>.json
  data_contract: "<path-or-id>"  # metadata JSON “data contract”
license: "<SPDX-ID-or-custom>"   # e.g., CC-BY-4.0 | ODbL-1.0 | Public-Domain | Proprietary (avoid if possible)
sensitivity: "public"            # public | restricted | internal
created: "2026-01-18"
last_updated: "2026-01-18"
owners:
  - "<name-or-team-handle>"
contacts:
  - "<email-or-issue-link>"
spatial:
  crs: "EPSG:3857"               # typical for XYZ/WebMercator tiles
  tiling_scheme: "XYZ"
  bounds_wgs84: ["<minLon>", "<minLat>", "<maxLon>", "<maxLat>"]
  center_wgs84: ["<lon>", "<lat>", "<zoom>"]
temporal:
  start: "<YYYY-MM-DD|YYYY|unknown>"
  end: "<YYYY-MM-DD|YYYY|present|unknown>"
tiles:
  kind: "<vector|raster|terrain>"
  storage: "<directory|mbtiles>"
  tile_format: "<pbf|mvt|png|webp|jpg|terrain-rgb>"
  minzoom: "<0>"
  maxzoom: "<14>"
  # Examples:
  # - directory: "tiles/{z}/{x}/{y}.pbf"
  # - mbtiles: "<tileset-id>.mbtiles"
  path_pattern: "<relative-path-pattern>"
integrity:
  # Fill these when you publish/rebuild (strongly recommended)
  artifact_sha256: "<sha256-of-mbtiles-or-tarball-or-root-manifest>"
  manifest: "<relative-path-to-manifest.json>" # optional: listing tiles + hashes
---

# 🧾 Provenance — `<tileset-id>`

![Status](https://img.shields.io/badge/status-sample-blue)
![Artifact](https://img.shields.io/badge/artifact-tileset-6f42c1)
![Provenance](https://img.shields.io/badge/provenance-required-success)
![License](https://img.shields.io/badge/license-TBD-lightgrey)
![Tiles](https://img.shields.io/badge/tiles-XYZ%20%2F%20EPSG%3A3857-informational)

Human-readable provenance + reproducibility notes for this **sample tileset** located at:

`web/assets/samples/tiles/<tileset-id>/`

> [!IMPORTANT]
> This tileset is intended for **demo / sample** usage. If it is referenced by governed UI flows (Story Nodes / Focus Mode / production layers), it should also be registered in the **catalogs** (STAC/DCAT) and have a **PROV lineage record** (see “Machine-readable records” below). ✅

---

## ✅ Quick facts

| Field | Value |
|---|---|
| Tileset ID | `<tileset-id>` |
| Title | `<Human-friendly tileset name>` |
| Kind | `<vector \| raster \| terrain>` |
| Storage | `<directory \| mbtiles>` |
| Tile format | `<pbf/mvt/png/webp/...>` |
| CRS + scheme | `EPSG:3857 (Web Mercator), XYZ` |
| Zoom range | `<minzoom> → <maxzoom>` |
| Bounds (WGS84) | `<minLon,minLat,maxLon,maxLat>` |
| Temporal coverage | `<start> → <end>` |
| Sensitivity | `public` |
| License | `<SPDX-ID-or-custom>` |
| Owners | `<name-or-team-handle>` |
| Last updated | `2026-01-18` |

---

## 📁 Folder layout

```text
📁 web/assets/samples/tiles/<tileset-id>/
├─ 🧾 provenance.md                 ← you are here
├─ 🗺️ tiles/                        ← (if directory storage) {z}/{x}/{y}.<ext>
│  └─ ... 
├─ 🧱 <tileset-id>.mbtiles           ← (if MBTiles storage)
├─ 🧭 tilejson.json                  ← (recommended) TileJSON for MapLibre
├─ 🎨 style.json                     ← (optional) MapLibre style referencing this tileset
├─ 🖼️ preview.png                    ← (optional) layer preview/screenshot
└─ 🧷 attribution.txt                ← (optional) short attribution string for UI
```

> [!TIP]
> If this tileset is shipped as a directory of tiles, consider adding a small **manifest** (hashes + counts) for integrity and cache-busting. 🧷

---

## 🧬 Machine-readable records

If this tileset is **only** a sample asset, you may keep these as `TBD`.  
If this tileset becomes **governed**, fill these in and ensure CI validates them. ✅

- **Data contract (metadata JSON):** `<kfm.data_contract>`
- **STAC asset record:** `<kfm.stac_asset>`
- **DCAT dataset/distribution:** `<kfm.dcat_dataset>`
- **PROV lineage record:** `<kfm.prov_record>`

---

## 🧾 Upstream sources

List **every** upstream dataset used to create this tileset. If you can’t fully identify a source, mark it as `TBD` and open an issue before this tileset is considered governed.

| Source ID | Publisher / Owner | Source title | Source URL | License | Retrieved | Checksum / ID | Notes |
|---|---|---|---|---|---|---|---|
| `<source-1>` | `<org>` | `<dataset title>` | `<url>` | `<license>` | `<date>` | `<sha256|doi|id>` | `<notes>` |
| `<source-2>` | `<org>` | `<dataset title>` | `<url>` | `<license>` | `<date>` | `<sha256|doi|id>` | `<notes>` |

### 📌 Attribution notes
- Required attribution text (for UI):  
  > `<publisher> — <dataset title> (<year>). License: <license>. Processed into tiles by KFM.`

- If multiple sources: include a short “credits list” that can be rendered in the UI.

---

## 🔁 Processing & lineage

### High-level lineage (human)

1. **Ingest** upstream source(s) → store immutable snapshot in `data/raw/…`
2. **Normalize** (schema cleanup, CRS normalization, attribute curation) → `data/processed/…`
3. **Tile** (generalize, simplify, encode to vector/raster tiles) → output here: `web/assets/samples/tiles/<tileset-id>/…`
4. **Validate** (metadata + schema + basic tile sanity checks) → produce/attach logs + hashes
5. **Publish** (sample asset) → used by the web viewer

### Lineage graph (Mermaid)

```mermaid
flowchart LR
  A[Upstream source(s)\n(raw external)] --> B[Raw snapshot\n(data/raw)]
  B --> C[Processed dataset\n(data/processed)]
  C --> D[Tile build activity\n(tile generator)]
  D --> E[Tileset artifact\n(web/assets/samples/tiles/<tileset-id>)]
  E --> F[Web viewer\n(MapLibre/Cesium)]
```

---

## 🧪 Validation & QA

### Required checks (recommended even for samples)

- [ ] **License verified** for each upstream source (including restrictions and attribution requirements)
- [ ] **Bounds & zoom sanity** checked (no accidental global bounds unless intended)
- [ ] **Schema sanity**: expected layer names/fields (vector) or bands/encoding (raster/terrain)
- [ ] **Tile integrity**: spot-check at least 3 zoom levels (min/mid/max) in the web viewer
- [ ] **Cache-busting**: version bump or hash update when tiles change
- [ ] **No “mystery layers”**: every feature can be traced to an upstream source row above

### Optional checks (nice-to-have)

- [ ] Automated tile lint (detect empty tiles, missing tiles at common z/x/y, invalid gzip, etc.)
- [ ] Visual regression snapshot for preview.png
- [ ] Performance note: approximate download size at typical view (z=8–12)

---

## 🧩 Web integration notes

### MapLibre / TileJSON

If you include `tilejson.json`, it should match how the web app loads this layer.

```json
{
  "tilejson": "3.0.0",
  "name": "<tileset-id>",
  "description": "<short description>",
  "version": "0.1.0",
  "scheme": "xyz",
  "tiles": ["./tiles/{z}/{x}/{y}.<ext>"],
  "minzoom": <minzoom>,
  "maxzoom": <maxzoom>,
  "bounds": [<minLon>, <minLat>, <maxLon>, <maxLat>]
}
```

> [!NOTE]
> Keep `tiles` relative for sample assets (so the demo can run from static hosting). If/when moved behind an API/tile server, update `tiles` to the served endpoint and bump version. 🚀

---

## ⚠️ Known limitations

Document anything that could mislead users:

- 🧭 **Generalization:** features simplified at low zoom → boundaries may not align at parcel-level
- 🕰️ **Temporal ambiguity:** upstream dataset may reflect mixed years or unknown capture date
- 🧱 **Attribute completeness:** some columns removed for size/privacy
- 🛰️ **Raster artifacts:** resampling seams or compression artifacts at some zooms
- 🧩 **Coverage gaps:** no-data areas or missing counties/tiles

---

## 🗓️ Change log

| Version | Date | What changed | Who | Notes |
|---|---|---|---|---|
| `0.1.0` | 2026-01-18 | Initial sample publish | `<name>` | `<notes>` |
| `0.1.1` | `<date>` | `<change>` | `<name>` | `<notes>` |

---

## ✅ Maintainer checklist (when rebuilding tiles)

- [ ] Update **created / last_updated**
- [ ] Update **upstream sources** (retrieved date + checksum / IDs)
- [ ] Record **tile build tool + version** used (tippecanoe/gdal/etc.) in “Processing”
- [ ] Update **integrity.artifact_sha256** (or manifest)
- [ ] Bump **version** in TileJSON/style (if present)
- [ ] Add/refresh **preview.png**
- [ ] If promoted to governed use: fill **STAC/DCAT/PROV + contract** links and ensure CI passes ✅
