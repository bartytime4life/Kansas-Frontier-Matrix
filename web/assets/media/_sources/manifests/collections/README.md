# 🗂️ Collections Manifests (Web Media Sources)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-blue)
![Provenance](https://img.shields.io/badge/Provenance-First-brightgreen)
![Contract](https://img.shields.io/badge/Contract-First-orange)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-purple)
![Status](https://img.shields.io/badge/status-draft-yellow)

> 📍 **You are here:** `web/assets/media/_sources/manifests/collections/`  
> 🎯 **Purpose:** Define *curated groupings* of source media (PDFs, images, maps, videos, etc.) that the web app can browse, filter, and cite as **evidence**.

---

## ✨ What is a “Collection” in KFM?

A **collection manifest** is a small, versioned “index card” that groups related sources into a logical set:

- 📚 A reading list (e.g., “Modeling & Simulation”)
- 🗺️ A map pack (e.g., “Historic Kansas Plat Maps”)
- 🧾 Evidence bundle for a Story Node (e.g., “Bleeding Kansas – Primary Sources”)
- 🧰 A toolkit set (e.g., “WebGL + GIS Visualization References”)

Collections are meant to be:
- ✅ **Provenance-first** (every source can be traced back to where it came from)
- ✅ **Contract-first** (schemas are stable; breaking changes are explicit)
- ✅ **Web-friendly** (fast to load; metadata supports UI filters/search)

---

## 🧱 Recommended Folder Layout

```text
🗂️ web/assets/media/
  └─ 🗂️ _sources/
     ├─ 🗂️ files/                       # ✅ local source media (when allowed)
     │  ├─ 🗂️ books/
     │  ├─ 🗂️ maps/
     │  └─ 🗂️ imagery/
     └─ 🗂️ manifests/
        ├─ 🗂️ sources/                  # ✅ atomic “source manifests” (one per asset/logical doc)
        ├─ 🗂️ collections/              # 👈 this folder (groupings of sources)
        └─ 🗂️ schemas/                  # ✅ JSON Schema contracts + validators
           ├─ collection.schema.json
           └─ source.schema.json
```

> [!NOTE]
> Keep **binaries out of `manifests/`**. Manifests should remain small, diff-friendly, reviewable text.

---

## 📄 File Naming & Conventions

### ✅ Collection manifest filename
Use one of the following patterns:

- `kebab-case.collection.json` *(recommended for runtime consumption)*
- `kebab-case.collection.yml` *(allowed for authoring; ideally compiled → JSON during build)*

Examples:
- `modeling-simulation.collection.json`
- `geospatial-visualization.collection.yml`

### 🆔 Stable collection IDs
Use stable, human-readable IDs:
- ✅ `modeling-simulation`
- ✅ `library-modeling-simulation`
- ✅ `kfm-library.modeling-simulation` *(namespaced, if needed)*  
- ❌ `collection1`
- ❌ `newstuff-final-final`

> [!TIP]
> **Never reuse IDs** for different content. If the meaning changes, create a new ID and deprecate the old one.

---

## 🧬 Collection Manifest Contract (v1)

Collections should be **thin** and mostly reference **source manifests** by ID.

### ✅ Minimal required fields

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `schema_version` | string | ✅ | e.g. `"kfm.media.collection/v1"` |
| `id` | string | ✅ | Stable identifier (matches filename) |
| `title` | string | ✅ | Human-facing title |
| `description` | string | ✅ | What it is + why it exists |
| `sources` | string[] | ✅ | Array of **source IDs** (defined in `../sources/`) |

### ⭐ Strongly recommended fields

| Field | Type | Why it matters |
|---|---|---|
| `tags` | string[] | Filtering + search |
| `license_summary` | string | Quick UI-safe description (does not replace per-source license fields) |
| `extent` | object | Spatial/temporal discovery (and optional STAC export) |
| `ui` | object | Icons, ordering, featured state, etc. |
| `provenance` | object | Who curated it, when, and why |

---

## 🧾 Example Collection Manifest

> Example: `modeling-simulation.collection.yml`

```yaml
schema_version: "kfm.media.collection/v1"
id: "modeling-simulation"
title: "🛰️ Modeling & Simulation"
description: >
  Core references for scientific modeling, simulation design, regression workflows,
  and experimental rigor used across the Kansas Frontier Matrix project.

tags:
  - modeling
  - simulation
  - statistics
  - regression
  - research-methods

license_summary: >
  Mixed licensing. See each source manifest for redistribution and attribution rules.

# Optional, but encouraged (helps search + future STAC alignment)
extent:
  spatial:
    # Use bbox only if sources are truly spatially scoped; otherwise omit.
    bbox: [-102.05, 36.99, -94.59, 40.00] # Kansas-ish envelope (example only)
  temporal:
    start: "1800-01-01"
    end: "1900-12-31"

sources:
  # These should correspond to manifests in: ../sources/<id>.source.(json|yml)
  - "book.scientific-modeling-simulation-nasa-grade"
  - "book.understanding-statistics-experimental-design"
  - "book.regression-analysis-with-python"
  - "book.think-bayes"
  - "paper.kfm-technical-documentation"

ui:
  icon: "🛰️"
  order: 20
  featured: true
  # Optional: a visual cover for UI cards (reference an asset in a source manifest)
  cover_source_id: "book.scientific-modeling-simulation-nasa-grade"

provenance:
  curated_by: "KFM Contributors"
  created_at: "2026-01-18"
  updated_at: "2026-01-18"
  rationale: >
    Establishes a shared, citable baseline for modeling + inference decisions across pipelines
    and story-node analysis.
```

---

## 🔗 How `sources` Works

Collections should point to **source manifests**, not raw files.

### ✅ Source manifests live here
`web/assets/media/_sources/manifests/sources/`

Each source manifest should describe **one logical source**:
- a single PDF 📄
- a map scan 🗺️
- a photo / screenshot 🖼️
- a dataset landing page 🔗
- a “book within a bundle PDF” 📚 *(see below)*

> [!IMPORTANT]
> Keep licensing + attribution **per source**, not only at the collection level.

---

## 📦 Handling “Bundle PDFs” (Multi-Book Files)

Some project PDFs are *compiled bundles* (multiple books inside one file). Treat each embedded book as a **virtual source**:

✅ Create separate source manifests like:
- `bundle.or-programming-books:objective-c-notes`
- `bundle.or-programming-books:implementing-programming-languages`

And include **page ranges** in the source manifest so the UI can deep-link consistently.

> [!TIP]
> If the UI cannot deep-link to pages yet, still capture page ranges now—future you will thank you. 😄

---

## 🛡️ Safety, Rights & Governance

### ©️ Copyright & Redistribution
- ✅ Only commit files to `web/assets/media/_sources/files/` if you have rights to redistribute.
- ✅ If not redistributable, store **metadata + a stable URL** in a source manifest.
- ✅ Prefer public-domain / open-licensed sources when possible.

> [!WARNING]
> Do **not** “accidentally ship” copyrighted PDFs inside the web build.

### 🧭 Sensitive content & location safety
If a source reveals sensitive locations (e.g., archaeological sites):
- 🚫 avoid precise coordinates in web-exposed manifests
- ✅ generalize spatial extent (county-level, bounding envelope, etc.)
- ✅ add a sensitivity marker in the **source manifest** (and optionally collection)

---

## 🧪 Validation & CI Expectations

Collection manifests should be:
- ✅ **Schema validated** (JSON Schema)
- ✅ **Link validated** (no broken `source_id` references)
- ✅ **Linted** (format + ordering if enforced)
- ✅ **Security scanned** (if any build tooling touches external URLs)

> [!NOTE]
> If you add a new manifest or field, update the corresponding schema in `../schemas/` and keep changes versioned.

---

## 🧭 Relationship to Data Catalogs (Optional Alignment)

If a collection is truly spatiotemporal and publishable:
- It *may* map cleanly to a **STAC Collection** (and each source/asset to STAC Items)
- It *may* participate in the project-wide **DCAT/PROV** exports

This folder is **web-facing**, but the metadata should be compatible with the larger KFM catalog approach wherever practical.

---

## 🧑‍💻 Add a New Collection Checklist ✅

1. 🧾 Create/confirm each `source manifest` in `../sources/`
2. 🗂️ Add or reference the media asset (local file or external URL)
3. 🧩 Create the new `*.collection.(yml|json)` file in this folder
4. 🧪 Run the validator (schema + reference checks)
5. 📚 If it’s a library/reference source, add/update `docs/library/MANIFEST.yml`
6. 📝 Update any Story Node(s) / UI routes that should surface the collection

---

## 🧰 Suggested Starter Collections (Based on Current Project Sources)

These are **examples** you can implement as manifests:

- 🛰️ **Modeling & Simulation**
  - Scientific Modeling and Simulation (NASA-grade)
  - Regression Analysis (Python)
  - Understanding Statistics & Experimental Design
  - Think Bayes

- 🗺️ **GIS, Maps & Remote Sensing**
  - Making Maps (GIS design)
  - Python Geospatial Analysis Cookbook
  - Mobile Mapping
  - Cloud-Based Remote Sensing with Google Earth Engine

- 🌐 **Web + Visualization**
  - Responsive Web Design (HTML5/CSS3)
  - WebGL Programming Guide

- 🗄️ **Data & Databases**
  - Database Performance at Scale
  - Scalable Data Management for Future Hardware
  - PostgreSQL Notes for Professionals

---

## 🗓️ Changelog

- **2026-01-18** — Initial scaffold for collection manifests README ✨

---