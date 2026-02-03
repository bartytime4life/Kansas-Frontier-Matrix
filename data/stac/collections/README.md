# 🗺️ STAC Collections (KFM) — `data/stac/collections/`

![STAC](https://img.shields.io/badge/metadata-STAC-blue)
![Governed](https://img.shields.io/badge/policy-evidence--first-success)
![CI Validated](https://img.shields.io/badge/CI-schema%20validated-brightgreen)

Welcome to the **STAC Collections** folder for **Kansas Frontier Matrix (KFM)**. This directory holds **STAC Collection JSON** records used to index datasets and geospatial assets with consistent spatial/temporal metadata. 🧭

> In KFM, catalog artifacts are **boundary outputs**: data is not considered “published” until it has STAC + DCAT + PROV records generated and linked.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📦 What lives here?

- ✅ **STAC Collection JSON** files (one per dataset / logical asset group)
- ❌ No data files (those belong in `data/processed/**`)
- ❌ No item-level records (those belong in `data/stac/items/`)

KFM’s repo layout expects STAC collections in `data/stac/collections/` and STAC items in `data/stac/items/`.  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧠 Why Collections matter in KFM (the “truth path”)

KFM enforces a strict publishing pipeline: **Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI**, and “no dataset becomes public” without cataloging + provenance logging.  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

Collections are part of the **Catalog** layer:
- **STAC** = assets + spatiotemporal indexing  
- **DCAT** = dataset discovery and distributions  
- **PROV** = lineage (“how did we produce this?”)

KFM defines “Catalogs” as the combined metadata catalogs: **STAC for assets, DCAT for discovery, and PROV for lineage tracking**.  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ KFM minimum requirements (collection-level)

KFM requires STAC/DCAT/PROV alignment for every dataset (and “evidence artifact”).  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
Even non-spatial datasets typically still get a STAC Collection for consistency.  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

At minimum, your **Collection** should include:

### 1) Standard STAC fields
- `type`: `"Collection"`
- `stac_version`
- `id`
- `title`
- `description`
- `license`
- `extent` (spatial + temporal)
- `links` (including `root`, `self`, and relevant relations)

### 2) KFM cross-layer linkage expectations
- **Items → Data:** STAC Items must point to actual assets in `data/processed/**` (or stable equivalent).  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **DCAT → STAC/Distribution:** DCAT entries should distribute via STAC or direct resource links.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **PROV end-to-end:** PROV must connect raw ➜ work ➜ processed and identify the producing run/config.  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

> 🔒 Governance gate: if a dataset lacks provenance metadata, KFM treats it as **not publishable**.  [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧾 File naming & IDs (recommended)

Use **one file per collection**, named by the collection `id`:

```txt
data/stac/collections/
  ├── ks_<domain>_<dataset_slug>.json
  └── ...
```

Why this pattern?
- It matches how KFM references datasets in the API (example dataset id: `ks_hydrology_1880`).  [oai_citation:10‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- It encourages consistent linkage across STAC ↔ DCAT ↔ PROV (same `id` / cross-refs).

> If your domain needs custom metadata, extend the **KFM STAC/DCAT profiles** rather than inventing ad-hoc fields.  [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧩 Minimal Collection template (starter)

> This is a template; your exact fields may vary based on KFM profile requirements.

```json
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "id": "ks_hydrology_1880",
  "title": "Kansas Hydrology (1880) — Example",
  "description": "Short human-readable description of the dataset and what it represents.",
  "license": "proprietary-or-spdx-id",
  "extent": {
    "spatial": { "bbox": [[-102.051, 36.993, -94.588, 40.003]] },
    "temporal": { "interval": [["1880-01-01T00:00:00Z", "1880-12-31T23:59:59Z"]] }
  },
  "keywords": ["kansas", "hydrology", "historical"],
  "links": [
    { "rel": "self", "href": "./ks_hydrology_1880.json", "type": "application/json" },
    { "rel": "root", "href": "../catalog.json", "type": "application/json" }
  ]
}
```

---

## 🔁 “Publish a dataset” checklist (KFM)

When a dataset is ready to ship, ensure these **boundary artifacts** exist.  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

1) 🗃️ **Processed data**
- Stored in `data/processed/<domain>/...`  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

2) 🗂️ **STAC Collection**
- Write here: `data/stac/collections/<id>.json`  [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

3) 🧷 **STAC Items**
- Write to: `data/stac/items/` (each item points at the processed asset)  [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

4) 🧭 **DCAT dataset entry**
- Write to: `data/catalog/dcat/`  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

5) 🧬 **PROV lineage bundle**
- Write to: `data/prov/`  [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Must trace raw ➜ work ➜ processed, plus run/config identifiers.  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Validation (don’t skip 🚦)

KFM CI validates structured outputs against schemas:
- STAC Items/Collections, DCAT datasets, and PROV JSON-LD must validate against KFM profiles.  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- If metadata fails schema validation, **CI fails** until corrected (or a governed profile update occurs).  [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🌐 How Collections show up downstream (API & UI)

KFM’s API exposes dataset metadata (DCAT summary) and links to assets (including STAC items).  [oai_citation:21‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
This means your Collection/Items become the navigable, evidence-first doorway into the dataset.

---

## 🛡️ Governance notes (the “evidence-first” vibe)

- **Provenance is mandatory** for publishability.  [oai_citation:22‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- KFM treats “evidence artifacts” (including AI-derived layers) like first-class datasets: they must be cataloged and traced in PROV.  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Focus Mode follows “No Source, No Answer” (separate from STAC, but same philosophy): uncited answers are blocked.  [oai_citation:24‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🔗 Related (repo contracts & standards)

- `docs/standards/KFM_STAC_PROFILE.md` (project STAC profile; extensions & required fields)  [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- `docs/standards/KFM_DCAT_PROFILE.md` (project DCAT profile)  [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- `docs/standards/KFM_PROV_PROFILE.md` (project PROV profile)  [oai_citation:27‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- `schemas/` (JSON Schemas for STAC/DCAT/PROV validation)  [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧯 Common pitfalls (quick saves)

- **Collection exists but no Items** → nothing points to real assets (UI/API will feel empty).
- **Items point to `raw/` or `work/`** → violates the publish boundary (Items should point to stable outputs in `processed/`).  [oai_citation:29‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **Missing PROV** → dataset is not publishable.  [oai_citation:30‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- **Ad-hoc fields** → extend KFM profiles instead.  [oai_citation:31‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

---

_If you’re adding a new domain: keep data isolated by domain, and publish catalogs to the canonical locations (`data/stac/`, `data/catalog/dcat/`, `data/prov/`).  [oai_citation:32‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)_