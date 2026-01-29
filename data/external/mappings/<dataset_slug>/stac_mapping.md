# 🛰️ STAC Mapping — `<dataset_slug>`

![STAC](https://img.shields.io/badge/STAC-1.0%2B-2ea44f)
![Domain](https://img.shields.io/badge/Domain-external-6f42c1)
![Status](https://img.shields.io/badge/Status-draft-yellow)
![KFM](https://img.shields.io/badge/KFM-contract--first-blue)

> 🎯 **Goal:** Define *exactly* how the external dataset `<dataset_slug>` becomes a **STAC Collection + Item(s)** in KFM, with stable asset links into `data/**/processed/**` (or equivalent stable storage), and cross-links to DCAT + PROV so the whole pipeline stays traceable end‑to‑end.

---

## 🧩 Placeholder Legend

Replace these consistently:

- `<dataset_slug>` → stable kebab-case slug (e.g., `usgs-3dep-dem`, `kansas-county-boundaries-1880`)
- `<dataset_title>` → human title
- `<dataset_version>` → dataset version tag (e.g., `v1`, `2026-01`, `2025.12.0`)
- `<collection_id>` → recommended: `external-<dataset_slug>`
- `<item_id>` → derived from the itemization strategy (see below)
- `<license_id>` → SPDX when possible, else `proprietary`/`unknown` (plus explanation)
- `<source_org>` / `<source_url>` → upstream publisher + canonical landing page
- `<pipeline_name>` / `<pipeline_run_id>` / `<git_commit>` → provenance anchors

---

## 🧭 KFM Contract Context (Non‑Negotiables)

KFM expects the canonical sequence:

**Raw → Processed → Catalog (STAC/DCAT) + PROV → Database → API → UI** ✅

This file is the “mapping contract” that makes the **Catalog step** deterministic and auditable.

---

## 📦 Required Paths & Outputs

### 🗂️ Dataset staging (domain = `external`)
Use this standardized staging layout:

- 📁 `data/external/raw/<dataset_slug>/` *(immutable snapshots; read-only inputs)*
- 📁 `data/external/work/<dataset_slug>/` *(intermediate scratch artifacts; reproducible)*
- 📁 `data/external/processed/<dataset_slug>/` *(final curated outputs; ready for downstream use)*

### 🛰️ Canonical STAC outputs (repo-wide catalogs)
At publication time, write STAC to:

- 🧾 `data/stac/collections/<collection_id>.json`
- 🧾 `data/stac/items/<collection_id>/<item_id>.json` *(recommended foldering)*

> 🧠 Tip: Keeping items grouped by collection avoids “10k files in one folder” pain.

---

## 🧱 Dataset Identity Card

Fill this out first — it drives Collection metadata.

| Field | Value |
|---|---|
| Dataset slug | `<dataset_slug>` |
| Dataset title | `<dataset_title>` |
| Description | `<1–3 sentence description of what this dataset is and why we use it>` |
| Upstream publisher | `<source_org>` |
| Upstream landing page | `<source_url>` |
| Upstream download/API | `<download_url_or_api_endpoint>` |
| License | `<license_id>` + `<notes/constraints>` |
| Coverage (spatial) | `<Kansas-only | regional | national | global>` |
| Coverage (temporal) | `<start_date> → <end_date> (or “unknown”)` |
| Sensitivity | `public | restricted | sensitive` |
| Steward (KFM) | `<name/team>` |

---

## 🛰️ STAC Collection Mapping

### ✅ Collection ID + Files
- **Collection ID:** `<collection_id>` *(recommended: `external-<dataset_slug>`)*
- **Collection JSON:** `data/stac/collections/<collection_id>.json`

### 🧾 Collection fields (must define)
Minimum (plus KFM profile-required fields where applicable):

- `id`, `type`, `stac_version`
- `title`, `description`, `keywords`
- `license`
- `providers` (source + KFM roles)
- `extent.spatial.bbox` and `extent.temporal.interval`
- `links` (self/root/parent; plus optional `via` to upstream)
- `summaries` (optional, but great for discovery)

### 🧑‍🤝‍🧑 Providers (recommended pattern)
- Provider 1: upstream publisher (roles: `producer`, `licensor`)
- Provider 2: KFM (roles: `processor`, `host`)

---

## 🧩 Itemization Strategy

Pick **one** strategy and document it clearly (don’t mix unless justified).

- [ ] **A. One Item per processed deliverable file** *(default & safest)*  
- [ ] **B. One Item per tile (grid index)** *(imagery / rasters)*
- [ ] **C. One Item per time slice** *(time series)*
- [ ] **D. One Item per feature** *(rare; only when feature count is modest)*
- [ ] **E. Collection-only (no Items)** *(only if dataset is non-spatial AND has no assets worth itemizing — discouraged)*

✅ **Chosen strategy:** **A / B / C / D / E** → `<choose_one>`

---

## 🧾 STAC Item Mapping

### 🆔 Item ID template
Define a deterministic ID rule.

**Recommended templates:**

- **Strategy A (per file):**  
  `<dataset_slug>__<asset_basename>__<dataset_version>`
- **Strategy B (tile):**  
  `<dataset_slug>__tile-<grid_id>__<dataset_version>`
- **Strategy C (time slice):**  
  `<dataset_slug>__<yyyy-mm-dd>__<dataset_version>`
- **Strategy D (feature):**  
  `<dataset_slug>__fid-<source_primary_key>__<dataset_version>`

✅ **Item ID template used:**  
`<item_id_template_here>`

---

### 🗺️ Geometry & BBOX rules
Choose exactly how geometry is computed:

- **geometry strategy:** `from_asset | from_features | dataset_bbox | null`
- **bbox strategy:** `from_geometry | from_asset_metadata | dataset_bbox | null`

✅ **Chosen:**
- geometry: `<strategy>`
- bbox: `<strategy>`

**If non-spatial:** set `geometry: null`, `bbox: null`, and add a clear note in `properties["kfm:spatial_note"]`.

---

### ⏱️ Datetime rules
STAC Items should include temporal fields when meaningful.

Pick one:
- `datetime = dataset_publication_date`
- `datetime = asset_timestamp` *(from filename or metadata)*
- `datetime = start_datetime + end_datetime` *(interval datasets)*
- `datetime = null` *(only if truly unknown / not applicable)*

✅ **Chosen datetime rule:** `<rule>`

---

### 🧾 Required Item properties (KFM-friendly)
These are recommended properties that keep catalogs, provenance, and governance linked:

- `title` *(optional but helpful)*
- `description` *(optional but helpful)*
- `license` *(if asset-level differs, include on assets too)*
- `providers` *(if not inherited cleanly from collection; otherwise omit)*
- `kfm:dataset_slug` = `<dataset_slug>`
- `kfm:dataset_version` = `<dataset_version>`
- `kfm:source_org` = `<source_org>`
- `kfm:source_url` = `<source_url>`
- `kfm:pipeline_name` = `<pipeline_name>`
- `kfm:pipeline_run_id` = `<pipeline_run_id>`
- `kfm:git_commit` = `<git_commit>`
- `kfm:prov_bundle` = `data/prov/<prov_id>.json` *(or your canonical PROV path)*
- `kfm:sensitivity` = `public | restricted | sensitive`
- `kfm:uncertainty` *(optional: freeform or structured; depends on KFM profile)*

> 🧠 If you’re unsure what’s mandatory, align with `docs/standards/KFM_STAC_PROFILE.md` and validate against `schemas/stac/`.

---

## 📎 Asset Mapping

### 🎒 Asset rules (non-negotiable)
- Assets must point to **final processed outputs** in `data/**/processed/**` *or* a stable storage URI.
- Use stable, reproducible paths and attach checksums when possible.
- Every asset should have: `href`, `type` (media type), `roles`, and a human-readable `title`.

### 📋 Default asset set (edit as needed)

| Asset key | Roles | `href` (recommended) | Media type (`type`) | Notes |
|---|---|---|---|---|
| `data` | `["data"]` | `data/external/processed/<dataset_slug>/<path>` | `<mime>` | Primary deliverable (GeoJSON/GeoTIFF/Parquet/etc.) |
| `metadata` | `["metadata"]` | `data/external/processed/<dataset_slug>/metadata/<file>` | `application/json` | Any sidecar metadata (upstream JSON, parsed summary, etc.) |
| `license` | `["metadata"]` | `data/external/raw/<dataset_slug>/LICENSE.*` | `text/plain` | If license text is shipped locally |
| `thumbnail` | `["thumbnail"]` | `data/external/processed/<dataset_slug>/thumbs/<file>` | `image/png` | Optional preview for UI |
| `overview` | `["overview"]` | `data/external/processed/<dataset_slug>/overviews/<file>` | `image/tiff` | Optional COG/overview raster |

### 🧠 Media type quick picks (common)
- GeoJSON: `application/geo+json`
- JSON: `application/json`
- CSV: `text/csv`
- Parquet: `application/x-parquet`
- GeoTIFF/COG: `image/tiff; application=geotiff`
- PNG: `image/png`
- PDF: `application/pdf`

---

## 🔗 Cross-Layer Linkage (STAC ↔ DCAT ↔ PROV ↔ Graph)

### 🧾 DCAT linkage (required expectation)
- DCAT dataset entry should include distributions that reference:
  - the STAC Collection **and/or**
  - a representative STAC Item **and/or**
  - direct download links to processed assets

📌 Suggested DCAT file:
- `data/catalog/dcat/<dataset_slug>__<dataset_version>.jsonld`

### 🧬 PROV linkage (required expectation)
PROV must capture full lineage:
- raw inputs → work intermediates → processed outputs
- plus pipeline run identifiers (run ID, commit hash, config)

📌 Suggested PROV file:
- `data/prov/<dataset_slug>__<dataset_version>.prov.json`

### 🕸️ Graph linkage (strong recommendation)
Graph nodes should reference catalog IDs, not duplicate payloads:
- store `stac_item_id`, `stac_collection_id`, `doi/ark` if available
- fetch details at runtime from catalogs

---

## 🧪 Validation Checklist (CI-friendly)

Run these before considering the dataset “published” ✅

### ✅ 1) Structural checks
- [ ] Processed assets exist at the `href` paths
- [ ] No asset points to `data/**/raw/**` unless role is metadata/legal only
- [ ] IDs are deterministic and stable across re-runs

### ✅ 2) Schema + profile checks
- [ ] `data/stac/collections/<collection_id>.json` validates against `schemas/stac/`
- [ ] All Items validate against `schemas/stac/`
- [ ] KFM STAC profile fields are present (as required)

### ✅ 3) Cross-layer checks
- [ ] DCAT references STAC/distributions correctly
- [ ] PROV references raw→work→processed chain with run anchors
- [ ] Sensitivity/governance fields are set (no “unknown” unless justified)

---

## ⚖️ Governance, FAIR+CARE, and Sensitivity Notes

### 🔒 Sensitivity classification
Set and justify:

- **Sensitivity:** `public | restricted | sensitive`
- **Redaction needs:** `<yes/no + what rules>`
- **Sovereignty considerations:** `<yes/no + notes>`

> 🧭 If the dataset contains Indigenous knowledge, archeological site locations, or culturally sensitive material, default to *restricted* until reviewed.

---

## 🧰 Machine-Readable Mapping Spec (YAML)

> 🧪 Pipelines can parse this block as the authoritative mapping contract.

```yaml
kfm_stac_mapping_v1:
  dataset_slug: "<dataset_slug>"
  domain: "external"
  dataset_version: "<dataset_version>"

  stac:
    collection:
      id: "<collection_id>" # recommended: external-<dataset_slug>
      file: "data/stac/collections/<collection_id>.json"
      title: "<dataset_title>"
      description: "<dataset_description>"
      license: "<license_id>"
      keywords: ["<keyword1>", "<keyword2>"]
      providers:
        - name: "<source_org>"
          roles: ["producer", "licensor"]
          url: "<source_url>"
        - name: "Kansas Frontier Matrix (KFM)"
          roles: ["processor", "host"]
          url: "<kfm_project_url_or_repo>"
      extent:
        spatial:
          bbox:
            - [<west>, <south>, <east>, <north>]
        temporal:
          interval:
            - ["<start_datetime_or_null>", "<end_datetime_or_null>"]
      summaries:
        kfm:dataset_slug: ["<dataset_slug>"]
        kfm:dataset_version: ["<dataset_version>"]
        kfm:sensitivity: ["public|restricted|sensitive"]

    items:
      itemization_strategy: "<A|B|C|D|E>"
      file_dir: "data/stac/items/<collection_id>/"
      id_template: "<dataset_slug>__<token>__<dataset_version>"
      geometry_strategy: "<from_asset|from_features|dataset_bbox|null>"
      bbox_strategy: "<from_geometry|from_asset_metadata|dataset_bbox|null>"
      datetime_strategy: "<dataset_publication_date|asset_timestamp|interval|null>"

      properties:
        kfm:dataset_slug: "<dataset_slug>"
        kfm:dataset_version: "<dataset_version>"
        kfm:source_org: "<source_org>"
        kfm:source_url: "<source_url>"
        kfm:pipeline_name: "<pipeline_name>"
        kfm:pipeline_run_id: "<pipeline_run_id>"
        kfm:git_commit: "<git_commit>"
        kfm:prov_bundle_href: "data/prov/<dataset_slug>__<dataset_version>.prov.json"
        kfm:sensitivity: "<public|restricted|sensitive>"
        kfm:uncertainty: "<optional>"

    assets:
      - key: "data"
        roles: ["data"]
        href_template: "data/external/processed/<dataset_slug>/{relative_asset_path}"
        media_type: "<mime>"
        title: "<asset_title>"
        include_checksums: true
      - key: "metadata"
        roles: ["metadata"]
        href_template: "data/external/processed/<dataset_slug>/metadata/{relative_metadata_path}"
        media_type: "application/json"
        title: "<metadata_title>"
        include_checksums: true

  linkage:
    dcat_href: "data/catalog/dcat/<dataset_slug>__<dataset_version>.jsonld"
    prov_href: "data/prov/<dataset_slug>__<dataset_version>.prov.json"
    graph_reference_strategy: "store_stac_ids_only"
```

---

## 🧷 Example STAC Skeletons (Templates)

<details>
<summary><strong>📄 Collection JSON skeleton</strong> (click to expand)</summary>

```json
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "id": "<collection_id>",
  "title": "<dataset_title>",
  "description": "<dataset_description>",
  "license": "<license_id>",
  "keywords": ["<keyword1>", "<keyword2>"],
  "providers": [
    {
      "name": "<source_org>",
      "roles": ["producer", "licensor"],
      "url": "<source_url>"
    },
    {
      "name": "Kansas Frontier Matrix (KFM)",
      "roles": ["processor", "host"],
      "url": "<kfm_project_url_or_repo>"
    }
  ],
  "extent": {
    "spatial": { "bbox": [[<west>, <south>, <east>, <north>]] },
    "temporal": { "interval": [["<start_datetime_or_null>", "<end_datetime_or_null>"]] }
  },
  "links": [
    { "rel": "self", "href": "data/stac/collections/<collection_id>.json", "type": "application/json" }
  ],
  "summaries": {
    "kfm:dataset_slug": ["<dataset_slug>"],
    "kfm:dataset_version": ["<dataset_version>"],
    "kfm:sensitivity": ["public|restricted|sensitive"]
  }
}
```

</details>

<details>
<summary><strong>📄 Item JSON skeleton</strong> (click to expand)</summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "<item_id>",
  "collection": "<collection_id>",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "<datetime_or_null>",
    "kfm:dataset_slug": "<dataset_slug>",
    "kfm:dataset_version": "<dataset_version>",
    "kfm:source_org": "<source_org>",
    "kfm:source_url": "<source_url>",
    "kfm:pipeline_name": "<pipeline_name>",
    "kfm:pipeline_run_id": "<pipeline_run_id>",
    "kfm:git_commit": "<git_commit>",
    "kfm:prov_bundle_href": "data/prov/<dataset_slug>__<dataset_version>.prov.json",
    "kfm:sensitivity": "<public|restricted|sensitive>"
  },
  "assets": {
    "data": {
      "href": "data/external/processed/<dataset_slug>/<path_to_asset>",
      "type": "<mime>",
      "roles": ["data"],
      "title": "<asset_title>"
    },
    "metadata": {
      "href": "data/external/processed/<dataset_slug>/metadata/<metadata_file>",
      "type": "application/json",
      "roles": ["metadata"],
      "title": "<metadata_title>"
    }
  },
  "links": [
    { "rel": "collection", "href": "data/stac/collections/<collection_id>.json", "type": "application/json" }
  ]
}
```

</details>

---

## ✅ Definition of Done (for this mapping)

- [ ] Placeholders replaced with real dataset values
- [ ] Itemization strategy chosen and justified
- [ ] Asset table complete (keys, roles, hrefs, media types)
- [ ] YAML mapping spec updated and consistent with narrative
- [ ] Validation checklist is runnable + passes (locally/CI)
- [ ] Sensitivity + governance notes completed (FAIR+CARE aware)
- [ ] Ready to pair with `dcat_mapping.md` + `prov_mapping.md`

---

