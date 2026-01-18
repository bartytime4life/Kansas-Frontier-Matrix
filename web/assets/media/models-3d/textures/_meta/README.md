---
title: "Textures Metadata (_meta)"
status: "active"
doc_kind: "Asset Standard"
last_updated: "2026-01-18"
path: "web/assets/media/models-3d/textures/_meta/README.md"
---

# 🧱 Textures Metadata (`_meta`) — KFM Web 3D Assets

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Scope](https://img.shields.io/badge/scope-web%2Fassets-blue)
![3D](https://img.shields.io/badge/render-WebGL%20%7C%20Cesium%20%7C%20MapLibre-purple)
![Provenance](https://img.shields.io/badge/provenance-required-orange)

> [!NOTE]
> This folder is the **source of truth for texture provenance + licensing metadata** used by the KFM web front-end (and any 3D viewers) to remain **auditable** and **creditable**.

KFM is built on **provenance-first** principles—every dataset (and by extension, every visual asset we ship) must be traceable to its **sources** and **processing steps**, with **citations and metadata treated as first-class data**. [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
This README applies those same rules to **3D textures** so the UI can always explain “where this came from” and “how it was made.” [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 Table of contents

- [📦 What lives in `_meta`](#-what-lives-in-_meta)
- [🔒 KFM invariants applied to textures](#-kfm-invariants-applied-to-textures)
- [🗂️ Folder layout](#️-folder-layout)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧪 PBR map types + color space rules](#-pbr-map-types--color-space-rules)
- [⚡ Performance budgets](#-performance-budgets)
- [🧾 Texture “data contract”](#-texture-data-contract)
- [✅ Add / update workflow](#-add--update-workflow)
- [📜 Licensing + attribution](#-licensing--attribution)
- [🔗 Project references](#-project-references)

---

## 📦 What lives in `_meta`

This directory is reserved for **metadata artifacts** that describe textures stored in sibling folders under:

`web/assets/media/models-3d/textures/`

Typical contents (some may be added over time):

- `README.md` (this file)
- `textures.manifest.json` ✅  
  A **runtime-friendly index** of texture packs (minimal fields) for the web app to list and load textures.
- `*.texture.json` ✅  
  One **metadata contract** per texture pack (full provenance + licensing + checksums).
- `licenses/` ✅  
  License texts or attribution bundles when required (e.g., CC-BY attribution text blocks).

> [!TIP]
> The KFM web client is a React-based front-end with dedicated viewer components (MapLibre GL JS + optional Cesium/3D mode). Keeping texture metadata in a predictable place supports UI inspection panels + credits overlays. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🔒 KFM invariants applied to textures

KFM uses a **contract-first** approach: “Every dataset has an associated metadata JSON (a ‘data contract’)… source, license, extent, processing steps… enforced via validators… no ‘mystery layers’.” [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

For textures, that means:

### ✅ Required (non-negotiable)

- **No texture pack without metadata.**  
  Every texture pack **MUST** have a `*.texture.json` contract. [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **No “mystery textures.”**  
  If a texture’s source/license is unknown → it does **not** belong in the official asset set. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Provenance-first.**  
  A texture’s metadata must explicitly capture: **sources → processing → outputs** so it remains traceable. [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Evidence-first UI.**  
  The UI should be able to display credits and provenance on-demand (like it does for data layers and Focus Mode). [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🧱 Governance alignment

KFM documentation recommends using structured metadata (like YAML front-matter) and enforcing provenance/citations as part of “governed documents.” [oai_citation:8‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
We follow the same spirit here: **assets are governed artifacts**.

---

## 🗂️ Folder layout

Example layout (illustrative):

```text
📁 web/assets/media/models-3d/textures/
├── 📁 terrain/
│   ├── ks_flint-hills_grass_2k_basecolor.webp
│   ├── ks_flint-hills_grass_2k_normal.png
│   └── ks_flint-hills_grass_2k_orm.webp
├── 📁 materials/
│   ├── ks_limestone_chiseled_2k_basecolor.webp
│   ├── ks_limestone_chiseled_2k_normal.png
│   └── ks_limestone_chiseled_2k_orm.webp
└── 📁 _meta/
    ├── README.md
    ├── textures.manifest.json
    ├── ks_flint-hills_grass.texture.json
    ├── ks_limestone_chiseled.texture.json
    └── 📁 licenses/
        └── ks_limestone_chiseled.LICENSE.txt
```

---

## 🏷️ Naming conventions

### 1) Texture pack slug

Use a **stable, human-readable slug** (snake_case):

- `ks_flint-hills_grass`
- `ks_limestone_chiseled`
- `ks_red-dirt_compacted`

> [!NOTE]
> Kansas-first slugs are encouraged because KFM is explicitly a “living atlas of Kansas.” [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 2) File naming pattern

**Pattern (recommended):**
```text
<slug>_<res>_<map>.<ext>
```

**Examples:**
- `ks_limestone_chiseled_2k_basecolor.webp`
- `ks_limestone_chiseled_2k_normal.png`
- `ks_limestone_chiseled_2k_orm.webp`

### 3) Resolution tokens

Use powers of two where possible:

- `512`, `1k`, `2k`, `4k` (preferred)
- Avoid oddball sizes unless justified

---

## 🧪 PBR map types + color space rules

KFM’s 3D stack includes 2D/3D viewers (MapLibre + Cesium mode). Textures must be predictable so they work across WebGL pipelines. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

| Map type | Suffix | Color space | Notes |
|---|---:|---|---|
| Base Color (Albedo) | `_basecolor` | **sRGB** | No baked lighting/shadows if possible |
| Normal | `_normal` | **Linear** | Tangent-space normal (most common) |
| ORM (Occlusion/Roughness/Metallic) | `_orm` | **Linear** | Packed channels: **R=AO, G=Roughness, B=Metallic** (glTF-friendly) |
| Roughness (single) | `_roughness` | **Linear** | Only if not using ORM |
| Metallic (single) | `_metallic` | **Linear** | Only if not using ORM |
| AO (single) | `_ao` | **Linear** | Only if not using ORM |
| Height/Displacement | `_height` | **Linear** | Prefer 16-bit PNG if needed (document it) |
| Emissive | `_emissive` | **sRGB** | Only when material truly emits light |

> [!WARNING]
> **Do not** store roughness/metallic/AO as sRGB. These are data maps and must be treated as **linear** inputs.

---

## ⚡ Performance budgets

Textures are the #1 driver of GPU memory usage in web 3D scenes. Keep assets efficient:

- ✅ Prefer `webp` for color/data maps when quality is acceptable
- ✅ Keep normals as PNG when artifacts matter
- ✅ Prefer `2k` for most materials; reserve `4k` for “hero” assets
- ✅ Avoid shipping duplicate near-identical variants unless needed

> [!TIP]
> If a texture pack is used in Cesium/3D Tiles scenes, assume a wider range of hardware (including laptops/tablets). Keep things lean.

---

## 🧾 Texture “data contract”

Each texture pack **MUST** have a metadata contract file:

```text
web/assets/media/models-3d/textures/_meta/<slug>.texture.json
```

Why: KFM requires metadata contracts and provenance records so any component can rely on self-described schema + provenance, and the system can automatically generate attribution/credits. [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Required fields (minimum)

```json
{
  "asset_kind": "texture",
  "asset_id": "urn:kfm:asset:texture:materials:ks_limestone_chiseled:v1",
  "slug": "ks_limestone_chiseled",
  "title": "Limestone (Chiseled)",
  "version": "1.0.0",
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Author Name — Source Name (CC-BY-4.0)"
  },
  "sources": [
    {
      "title": "Original capture / scan / library reference",
      "author": "Author or Organization",
      "license": "CC-BY-4.0",
      "retrieved_at": "2026-01-10",
      "url": "https://example.com/source"
    }
  ],
  "processing": {
    "steps": [
      {
        "tool": "tool-name",
        "version": "x.y.z",
        "notes": "What changed / what was generated"
      }
    ]
  },
  "textures": {
    "basecolor": { "path": "../materials/ks_limestone_chiseled_2k_basecolor.webp", "color_space": "sRGB" },
    "normal":    { "path": "../materials/ks_limestone_chiseled_2k_normal.png",      "color_space": "linear" },
    "orm":       { "path": "../materials/ks_limestone_chiseled_2k_orm.webp",        "color_space": "linear" }
  },
  "checksums": {
    "sha256": {
      "basecolor": "<sha256>",
      "normal": "<sha256>",
      "orm": "<sha256>"
    }
  },
  "tags": ["kansas", "limestone", "masonry"]
}
```

### 🌎 Optional fields (highly recommended)

- `spatial_extent`: bounding box or named region (when texture is place-derived)
- `temporal_extent`: capture date or historical applicability
- `sensitivity`: `{ "care_label": "...", "classification": "public|restricted", "notes": "..." }`
- `render_hints`: wrap modes, repeat scales, suggested roughness/metalness overrides
- `derivatives`: link to baked variants (e.g., `1k`, `2k`, `4k`) and GPU-compressed versions if produced

> [!NOTE]
> The broader KFM pipeline treats **derived products** as first-class evidence artifacts with provenance and validation gates. [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ Add / update workflow

1) **Add the texture files**  
   Place texture images under an appropriate subfolder (`terrain/`, `materials/`, etc.)

2) **Create / update the contract**  
   Add: `_meta/<slug>.texture.json`  
   Ensure it includes **license + sources + processing steps**. [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

3) **Update the manifest**  
   Add (or update) an entry in `_meta/textures.manifest.json` so the UI can discover it.

4) **Run validation** (locally if available)  
   CI is expected to enforce metadata contracts and reject “mystery” assets—consistent with KFM’s “no unsourced additions” guardrails. [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

5) **Open a PR with credits included**  
   Include any required attribution text and confirm the UI can display it.

---

## 📜 Licensing + attribution

KFM is explicit about transparency in licensing and attribution, and uses metadata to generate credits when needed. [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Rules of thumb

- Always store the **SPDX identifier** when possible (`MIT`, `CC-BY-4.0`, etc.)
- Always include **attribution text** if the license requires it
- If the source forbids redistribution → **do not commit** the texture
- Prefer open sources and community-contributed captures where provenance is clear

> [!TIP]
> If you’re unsure about a license, treat it as **restricted** until clarified.

---

## 🔗 Project references

These are the core project docs that shaped the governance model used here:

- 📘 KFM Technical Documentation (architecture, provenance-first, contract-first):  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
  Key excerpts used for this standard: provenance-first + “no mystery layers” + metadata contracts. [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

- 🧭 KFM v13 Master/Markdown Guide (pipeline invariants, evidence-first workflow):  [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
  Key invariant: strict pipeline ordering + provenance gating. [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

- ✍️ Markdown governance best practices (front-matter, citations as governance tools):  [oai_citation:23‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
  Used to justify structured doc metadata + evidence-first documentation style. [oai_citation:24‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
