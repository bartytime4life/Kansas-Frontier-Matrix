---
title: "🏛️ Archaeology Site 3D Assets — <Site Name> (<site-slug>)"
path: "web/assets/3d/archaeology/sites/<site-slug>/README.md"
version: "v1.0.0"
last_updated: "2026-01-15"
status: "template"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
pipeline_contract_version: "TBD"

project: "Kansas Frontier Matrix (KFM)"
subsystem: "web/assets/3d/archaeology"
asset_scope: "site"
site_slug: "<site-slug>"
site_id: "TBD"

fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"          # set to "sensitive" if location/context is protected
classification: "open"         # set to "restricted" if access-controlled
jurisdiction: "US-KS"

governance_ref: "docs/governance/GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"

doc_uuid: "urn:kfm:doc:web:assets:3d:archaeology:sites:<site-slug>:readme:v1.0.0"
semantic_document_id: "kfm.web.assets.3d.archaeology.sites.<site-slug>.readme"
---

# 🏛️ Archaeology Site 3D Assets — <Site Name> (`<site-slug>`)

![KFM](https://img.shields.io/badge/KFM-3D%20Archaeology-blue)
![Assets](https://img.shields.io/badge/assets-web--ready%20exports-5c7cfa)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-governed-success)

> [!IMPORTANT]
> **This folder is for web-consumable 3D derivatives only** (optimized meshes/tiles + previews + lightweight metadata).  
> **Authoritative source data** (raw scans, original photogrammetry, field notes, full-res rasters) must live in the governed data system (`data/*`) and be linked here via **STAC/DCAT/PROV** references.

---

## 📌 At a glance

| Field | Value |
|---|---|
| Site name | `<Site Name>` |
| Site slug | `<site-slug>` |
| Site ID | `TBD` |
| Primary CRS | `TBD (EPSG:xxxx)` |
| Web viewer target | `glTF/GLB` and/or `3D Tiles` |
| Sensitivity | `public` (set to `sensitive` if protected) |
| License | `TBD` (prefer CC-BY / CC0 for derivatives where allowed) |

---

## 📘 Overview

### Purpose
Provide a **single, predictable home** for all **web-ready 3D archaeological assets** for this site (models, tilesets, previews, and the minimal metadata needed by the KFM web viewer).

### Scope

| ✅ In scope | ❌ Out of scope |
|---|---|
| Web-ready `.glb` / `.gltf` models, `3D Tiles` tilesets | Raw scans (E57), full-res photogrammetry projects, source LAS/LAZ archives |
| Preview images (thumb/hero) & UI-friendly metadata | Field notebooks, protected coordinates, sensitive context details |
| Provenance pointers to governed datasets (STAC/DCAT/PROV) | “Working files” or “just-in-case” exports (put those in `data/work/*`) |

### Audience
- 🧑‍💻 **Frontend / Visualization devs** (Map/3D viewer integration)
- 🧪 **Data + pipeline engineers** (export + provenance)
- 🏺 **Archaeology / heritage reviewers** (sensitivity + interpretive integrity)

### Definitions
- **Web-ready**: optimized for browser streaming (reasonable polygon budget, compressed textures, LODs/tiling where needed).
- **Derivative**: produced from source data via a pipeline; must be traceable.
- **Protected / sensitive site**: location or context details restricted to prevent harm (e.g., looting).

---

## 🧭 Sensitivity & protection policy

> [!WARNING]
> **Do not publish precise coordinates, access routes, or feature-level descriptions** for protected sites.  
> If this site is protected, update front-matter to `sensitivity: "sensitive"` and `classification: "restricted"`, and ensure metadata uses **redacted geometry** (e.g., generalized bounding boxes, blurred centroid, or region-only).

**Recommended defaults (until reviewed):**
- ✅ Keep metadata minimal (period, generalized area, public narrative links)
- ✅ Store exact geometry in governed layers under access control (`data/*` + policy gates)
- ✅ Add “public-safe” derivatives only (no “treasure-map” fidelity)

---

## 🗂️ Directory layout

```text
web/assets/3d/archaeology/sites/<site-slug>/
├─ README.md
├─ meta/
│  ├─ site.meta.json              # minimal site metadata (public-safe)
│  ├─ manifest.site.json          # asset inventory + checksums + transforms
│  ├─ stac.item.json              # pointer/bridge to canonical data item(s)
│  ├─ prov.json                   # provenance summary for these derivatives
│  └─ citations.md                # evidence-first references (short + actionable)
├─ previews/
│  ├─ hero.webp                   # wide banner (optional)
│  ├─ thumb.webp                  # UI thumbnail (required)
│  └─ preview.glb.png             # render snapshot (optional)
└─ models/
   ├─ glb/
   │  ├─ <site-slug>__site.glb     # primary model (preferred)
   │  ├─ <site-slug>__context.glb  # terrain/context shell (optional)
   │  └─ <site-slug>__finds.glb    # if allowed + non-sensitive (optional)
   └─ tileset/
      ├─ tileset.json             # Cesium 3D Tiles root (optional)
      └─ ...                      # tiles/ (b3dm/pnts/metadata)
```

---

## 🧱 Asset standards (web)

### Preferred formats ✅
- 🟦 **GLB (glTF 2.0 binary)** for most site models (`models/glb/*.glb`)
- 🧊 **3D Tiles** for large/streamed scenes (`models/tileset/tileset.json`)
- 🖼️ **WEBP** for previews (`previews/*.webp`)

### Mesh + texture guidance
- 🧩 Use **LOD** or tiling for heavy meshes (keep first paint fast)
- 🗜️ Prefer modern compression when possible:
  - mesh: Draco (glTF extension) or tiling
  - textures: KTX2/Basis (if your viewer pipeline supports it)
- 🧭 Ensure consistent units (**meters**) and document any transforms in `manifest.site.json`

---

## 🧾 Metadata contract

### `meta/site.meta.json` (minimal, public-safe)
**Required keys (recommended baseline):**
```json
{
  "site_slug": "<site-slug>",
  "site_name": "<Site Name>",
  "site_id": "TBD",
  "classification": "open",
  "sensitivity": "public",
  "jurisdiction": "US-KS",
  "time_range": {"start": "TBD", "end": "TBD"},
  "summary": "TBD (public-safe)",
  "public_geometry": {
    "type": "bbox",
    "value": ["TBD","TBD","TBD","TBD"],
    "note": "Redact/generalize if protected"
  },
  "links": {
    "story_nodes": [],
    "canonical_stac": "meta/stac.item.json"
  }
}
```

### `meta/manifest.site.json` (assets + checksums)
Track **what to load** and **how to place it**:
```json
{
  "site_slug": "<site-slug>",
  "assets": [
    {
      "role": "primary",
      "type": "model",
      "format": "glb",
      "uri": "models/glb/<site-slug>__site.glb",
      "sha256": "TBD",
      "lod": "TBD",
      "crs": "TBD",
      "transform": {
        "kind": "local_to_world",
        "value": "TBD (matrix or params)",
        "units": "meters"
      }
    }
  ]
}
```

---

## 🔗 Provenance (non-negotiable)

> [!NOTE]
> Every model here must be traceable to:
> - **source dataset(s)** (catalog IDs / STAC Item IDs)
> - **processing run** (pipeline run ID, commit SHA, parameters)
> - **quality gates** (checksums, validation notes)

**Minimum:** fill in `meta/stac.item.json` and `meta/prov.json`, and add at least one concrete citation in `meta/citations.md`.

---

## 🧪 QA checklist (Definition of Done)

- [ ] ✅ Front-matter filled (slug, classification, sensitivity, doc_uuid)
- [ ] ✅ `meta/site.meta.json` present and **public-safe**
- [ ] ✅ `meta/manifest.site.json` present with **sha256** for each asset
- [ ] ✅ `previews/thumb.webp` present (UI-required)
- [ ] ✅ Provenance pointers present (`stac.item.json`, `prov.json`)
- [ ] ✅ No protected coordinates or “how to loot this” detail
- [ ] ✅ Assets load in the web viewer without console errors
- [ ] ✅ File names follow conventions (`<site-slug>__<role>.<ext>`)

---

## 🧩 Common patterns

### Naming
- ✅ `<site-slug>__site.glb` = primary
- ✅ `<site-slug>__context.glb` = terrain/context shell
- ✅ `<site-slug>__<feature-group>.glb` = optional thematic layer (only if safe)

### Versioning
- If geometry meaningfully changes: bump **asset version** inside `manifest.site.json`
- If only compression/packaging changes: keep geometry version, bump **export revision**

---

## 📎 Related docs (expected in repo)

- 🧭 Governance: `docs/governance/GOVERNANCE.md`
- 🧑‍⚖️ Ethics & harm prevention: `docs/governance/ETHICS.md`
- 🧾 Provenance conventions: `docs/provenance/README.md`
- 🗺️ Viewer integration: `web/README.md` (or `web/docs/*`)

---

## 📝 Changelog

- **v1.0.0** — Template created for site-scoped 3D asset exports.
