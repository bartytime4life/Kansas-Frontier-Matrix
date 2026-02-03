# 📦 STAC Items — `data/stac/items/`

![STAC](https://img.shields.io/badge/STAC-Items-2ea44f)
![Catalog](https://img.shields.io/badge/Catalog-Boundary%20Artifact-blue)
![Provenance](https://img.shields.io/badge/Provenance-PROV%20linked-important)
![Format](https://img.shields.io/badge/Format-STAC%20Item%20(GeoJSON%20Feature)-informational)

Welcome to the **STAC Item** shelf for the Kansas Frontier Matrix (KFM) data catalog.  
Each file in this directory represents **one discoverable evidence artifact** (imagery scene, LiDAR tile, vector layer snapshot, document, derived analysis output, etc.) and is part of the project’s governed **truth path**:

> **Raw ➜ Work ➜ Processed ➜ Catalog (STAC/DCAT) ➜ PROV ➜ Runtime Stores ➜ API ➜ UI/AI**

---

## 🧭 What belongs here?

✅ **STAC Item JSON files** (one per asset “unit”) that:
- point to the **real data** (usually in `data/processed/**` or stable object storage),
- carry **spatiotemporal metadata** (geometry, bbox, datetime / interval),
- include **assets** with clear roles (data, thumbnail, metadata, etc.),
- link outward to **DCAT** and **PROV** counterparts (directly or indirectly),
- remain **traceable** (source attribution + reproducible lineage).

❌ Not allowed here:
- Raw source files (those go under `data/raw/**`)
- Intermediate work products (those go under `data/work/**`)
- “Mystery JSON” that doesn’t validate as a STAC Item
- Signed/expiring URLs, secrets, access tokens 🔒

---

## 🗂️ Expected sibling layout

```text
📁 data/
└── 📁 stac/
    ├── 📁 collections/   🗃️ STAC Collections (dataset-level metadata)
    └── 📁 items/         📦 STAC Items (this folder)
📁 data/
└── 📁 catalog/
    └── 📁 dcat/          🧾 DCAT Dataset entries (JSON-LD)
📁 data/
└── 📁 prov/              🧬 PROV bundles (lineage per dataset/run)
```

> [!NOTE]
> KFM treats STAC/DCAT/PROV as **boundary artifacts**: they are required before data is considered “published” into downstream systems (graph, API, UI). [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧱 How Items fit the KFM pipeline (why this matters)

KFM is **evidence-first**: maps, charts, and AI answers should always have a **“map behind the map”**.  
For remote sensing and other geospatial assets, the ingestion pipeline produces processed outputs and then emits a **STAC Item entry** into the catalog alongside provenance details. [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🧩 Cross-layer linkage rules (STAC ↔ DCAT ↔ PROV ↔ Graph)

KFM enforces these expectations:

- **STAC Items → Data**: every Item must point to the actual asset(s) in `data/processed/**` or equivalent stable storage. [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **DCAT → Distributions**: DCAT entries should link to STAC and/or direct download endpoints (discovery layer). [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **PROV end-to-end**: PROV must connect raw inputs → work steps → processed outputs, tied to a run/config/commit hash. [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Graph references catalogs**: graph nodes store *references* (e.g., STAC Item IDs), not bulky payloads. [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧾 STAC Item “minimum contract” ✅

At a minimum, every Item should include:

- `type`: `"Feature"`
- `stac_version`
- `id` (stable & unique)
- `geometry` + `bbox` (or `null` where policy allows for non-spatial artifacts)
- `properties`:
  - `datetime` **or** (`start_datetime` + `end_datetime`)
- `links` (at least `self`, plus `collection`/`parent`/`root` when available)
- `assets` (at least one)

> [!TIP]
> Treat the `id` as a long-lived identifier. **Do not** bake ephemeral paths into it.

---

## 🏷️ Naming conventions (recommended)

You can organize Items either **flat** or **by collection**. Pick one and stick to it.

### Option A — per-collection folders (recommended for scale)
```text
data/stac/items/<collection_id>/<item_id>.json
```

### Option B — flat (acceptable for small catalogs)
```text
data/stac/items/<collection_id>__<item_id>.json
```

**Recommended `item_id` patterns**:
- `sentinel-2a_2025-06-21_tile-15SWC`
- `usgs-3dep_2023_tile-14-6020_laz`
- `kars_ndvi_1935-07_statewide_v1`

---

## 🧰 Assets rules (do this, not that)

### ✅ Do
- Use **stable** `href` targets:
  - repo-relative paths (when data is versioned in-repo), **or**
  - object storage URLs that don’t expire (S3/HTTP with stable addressing)
- Give assets meaningful keys: `data`, `thumbnail`, `overview`, `metadata`, `qa`, etc.
- Set `type` (media type) when known (e.g., `image/tiff; application=geotiff; profile=cloud-optimized`)
- Add `roles` to communicate intent: `["data"]`, `["thumbnail"]`, `["overview"]`, `["metadata"]`

### ❌ Don’t
- Use signed URLs (`?X-Amz-Signature=...`)
- Point to `data/raw/**` (raw is not a published interface)
- Hide provenance inside a freeform paragraph only (link to PROV)

---

## 🧬 KFM-specific extensions (profile-driven)

KFM extends base standards with project-specific fields (e.g., provenance references, uncertainty indicators). All Items must conform to the project’s STAC profile and pass CI validation. [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> [!IMPORTANT]
> Use **namespaced** fields for custom properties, e.g. `kfm:*`  
> Examples: `kfm:provenance_ref`, `kfm:source`, `kfm:license_notes`, `kfm:uncertainty`

(Exact field names are defined by the KFM STAC profile and schemas.)

---

## 🧪 Validation (local + CI)

Before committing new/edited Items, validate them.

### ✅ JSON validity
- Must parse as JSON (no trailing commas, etc.)

### ✅ STAC validity (choose a validator)
**Python (pystac)**
```bash
python -m pip install pystac[validation]
python -c "import pystac; pystac.Item.from_file('data/stac/items/<...>.json').validate()"
```

**Node-based validators (optional)**
```bash
# example pattern (tooling may vary by repo)
npm install
npm run stac:validate
```

> [!NOTE]
> CI should validate Items against the KFM STAC profile (schemas + policy rules). [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧩 Template — starter STAC Item (copy/paste)

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [],
  "id": "example-item-id",
  "collection": "example-collection-id",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 39.99],
      [-94.60, 39.99],
      [-94.60, 37.00],
      [-102.05, 37.00],
      [-102.05, 39.99]
    ]]
  },
  "bbox": [-102.05, 37.00, -94.60, 39.99],
  "properties": {
    "datetime": "2025-06-21T00:00:00Z",
    "created": "2026-02-03T00:00:00Z",
    "updated": "2026-02-03T00:00:00Z",

    "kfm:source": "authoritative upstream name",
    "kfm:provenance_ref": "prov/<run-or-dataset-id>.json"
  },
  "links": [
    { "rel": "self", "href": "./example-item-id.json", "type": "application/json" },
    { "rel": "collection", "href": "../../stac/collections/example-collection-id.json", "type": "application/json" },

    { "rel": "describedby", "href": "../../catalog/dcat/example-dataset.jsonld", "type": "application/ld+json" }
  ],
  "assets": {
    "data": {
      "href": "../../processed/<domain>/example.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "title": "Primary data asset"
    },
    "thumbnail": {
      "href": "../../processed/<domain>/example_thumbnail.jpg",
      "type": "image/jpeg",
      "roles": ["thumbnail"],
      "title": "Quicklook thumbnail"
    },
    "metadata": {
      "href": "../../prov/<run-or-dataset-id>.json",
      "type": "application/json",
      "roles": ["metadata"],
      "title": "PROV lineage bundle"
    }
  }
}
```

> [!TIP]
> If you need an interval (not a single timestamp), prefer:
> - `properties.start_datetime`
> - `properties.end_datetime`
> and omit `properties.datetime`.

---

## 🧭 Common item patterns

<details>
<summary><strong>🛰️ Remote sensing scene (COG + tiles + quicklook)</strong></summary>

- `assets.data`: Cloud-Optimized GeoTIFF (COG)
- `assets.overview`: downsampled overview (optional)
- `assets.thumbnail`: JPG/PNG quicklook
- `assets.qa`: QA band, cloud mask, or metadata report (optional)

KFM’s pipeline commonly converts incoming scenes to COGs and publishes them with STAC Item metadata + provenance. [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

</details>

<details>
<summary><strong>🗺️ Vector layer snapshot (GeoJSON/GeoPackage/Parquet)</strong></summary>

- `assets.data`: GeoJSON / GeoPackage / Parquet
- include `properties.datetime` (or interval) that reflects the snapshot time
- if large, prefer Parquet + a clear `kfm:how_to_use` note in `properties`

</details>

<details>
<summary><strong>📜 Document artifact (PDF, scanned map, transcript)</strong></summary>

- `assets.data`: PDF (or image)
- `assets.text`: extracted text (if available)
- geometry/bbox may be Kansas-wide or specific to a place (depending on artifact)
- ensure PROV records OCR / extraction steps when applicable

</details>

---

## 🧯 Troubleshooting checklist

- [ ] Does the JSON parse?
- [ ] Does it validate as a STAC Item?
- [ ] Do `assets.*.href` targets exist (or resolve) and are they stable?
- [ ] Is the Item linked to the correct Collection?
- [ ] Is provenance discoverable (PROV link / reference present)?
- [ ] Are custom fields namespaced (e.g., `kfm:*`)?
- [ ] Any secrets / signed URLs accidentally included? 🔒

---

## 📚 References (project grounding)

- KFM system architecture & “truth path” (catalog as boundary artifact)  [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Markdown + repo layout + STAC/DCAT/PROV alignment policy  [oai_citation:10‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- Node-based tooling patterns (validators/scripts, if applicable)  [oai_citation:11‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
- Web/UI documentation conventions (for catalog-driven experiences)  [oai_citation:12‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  