---
title: "🎨 Textures (Landmark) — <landmark_slug>"
path: "web/assets/3d/landmarks/<landmark_slug>/textures/README.md"
version: "v1.0.0"
last_updated: "2026-01-15"
status: "active"
doc_kind: "README"
license: "CC-BY-4.0"

# KFM Markdown / governance profile
markdown_protocol_version: "KFM-MDP v11.2.6"
pipeline_contract_version: "TBD"

governance_ref: "docs/governance/"
ethics_ref: "docs/governance/"

fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

doc_uuid: "urn:kfm:doc:web:assets:3d:landmarks:<landmark_slug>:textures:readme:v1.0.0"
semantic_document_id: "kfm.web.assets.3d.landmarks.<landmark_slug>.textures.readme"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# 🎨 Textures for `<landmark_slug>` (Web 3D)

This folder contains **runtime-ready textures** for the `<landmark_slug>` landmark’s 3D assets (typically glTF/glb materials). These textures are optimized for **web rendering**, **repeatable builds**, and **provenance-first** auditing.

> [!IMPORTANT]
> Treat textures as **governed assets**: every file should be attributable (license + source), reproducible (conversion steps), and verifiable (checksums). This mirrors KFM’s broader “evidence-first” posture.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📘 Overview

### ✅ Purpose
Provide a canonical, per-landmark home for **PBR textures** used by the landmark’s 3D model(s) in the KFM web viewer(s).

### 🎯 Scope
| In Scope ✅ | Out of Scope ❌ |
|---|---|
| Runtime texture files (KTX2/WebP/PNG/JPG) | Authoring sources (PSD, .blend, raw scans) |
| Texture manifest + provenance metadata | High-poly sculpt sources / bake cages |
| Preview swatches (optional) | Engine-specific caches (three.js cache, etc.) |
| Naming + channel packing conventions | Non-landmark shared materials (use a shared folder, if/when defined) |

### 👥 Audience
- 🧑‍💻 Web/3D implementers (MapLibre/Cesium/Three)  
- 🧪 Pipeline + QA maintainers (asset validation, checksum gates)  
- 🧾 Historians/curators (attribution, licensing, provenance review)

### 📚 Definitions
- **PBR**: Physically-Based Rendering materials (baseColor/metal/rough/normal/etc.)
- **KTX2**: GPU-friendly texture container (commonly BasisU compressed)
- **ORM**: Packed texture convention: **O**cclusion (R), **R**oughness (G), **M**etallic (B)
- **sRGB vs Linear**: Color textures use **sRGB**; data textures use **linear**

---

## 🧭 Directory contract

Expected contents (examples):

```text
web/assets/3d/landmarks/<landmark_slug>/textures/
├─ 📄 README.md                          # 📘 Texture package notes: format expectations, color space, and sizing rules
├─ ✅🧾 textures.manifest.json            # Required (recommended): inventory + roles + resolution + colorSpace + checksums
├─ 🎨🧵 <landmark_slug>_basecolor.ktx2    # Base color/albedo (KTX2 preferred for web; typically sRGB)
├─ 🧭🧵 <landmark_slug>_normal.ktx2       # Normal map (KTX2; typically linear)
├─ 🧲🧵 <landmark_slug>_orm.ktx2          # Packed ORM (occlusion/roughness/metallic; linear; channel map documented)
├─ ✨🧵 <landmark_slug>_emissive.ktx2     # Optional emissive/glow map (sRGB if color; document intent in manifest)
├─ 🫥🖼️ <landmark_slug>_opacity.webp      # Optional opacity mask (if not embedded as alpha in basecolor)
└─ 🖼️ previews/                          # Optional UI previews/swatches (small, web-optimized)
   ├─ 🎨🖼️ material-swatch.webp           # Quick swatch preview (single material look)
   └─ 🧾🖼️ contact-sheet.webp             # Contact sheet preview (all texture channels at a glance)
```

> [!NOTE]
> If your renderer needs fallbacks, you may include `.webp`/`.png` alongside `.ktx2`, but keep **one canonical “preferred”** entry in the manifest.

---

## 🏷️ Naming conventions

### ✅ Landmark slug rules
- Lowercase
- `kebab-case` recommended (e.g., `monument-rock`, `state-capitol`)
- Stable over time (treat as an identifier)

### ✅ Texture file rules
Use:  
`<landmark_slug>_<map-type>.<ext>`

**Allowed map-type suffixes**
- `basecolor` (aka albedo)
- `normal` (tangent space, +Y/OpenGL)
- `orm` (packed occlusion/roughness/metallic)
- `roughness` / `metallic` (only if not using ORM)
- `ao` (only if not using ORM)
- `emissive`
- `height` / `displacement` (rare for web; use cautiously)

**Allowed extensions**
- `.ktx2` ✅ preferred (GPU-compressed delivery)
- `.webp` ✅ good fallback/preview
- `.png` ✅ lossless fallback
- `.jpg` ✅ last-resort for basecolor only (no alpha)

> [!WARNING]
> Avoid shipping authoring formats (`.psd`, `.tif`, `.exr`) in `web/assets/…`. Keep those in non-web working areas and derive web outputs deterministically.

---

## 🎛️ Color space & channel packing (PBR rules)

### Color space
| Map | Color space |
|---|---|
| basecolor, emissive | **sRGB** |
| normal, orm, roughness, metallic, ao, height | **Linear** |

### ORM packing (recommended)
- **R** = Ambient Occlusion  
- **G** = Roughness  
- **B** = Metallic  
- **A** = unused (leave 1.0 / omit)

This matches common glTF material workflows and reduces texture count.

### Normal map convention
- **Tangent-space**
- **+Y (OpenGL)**
- If you inherit a DirectX (-Y) normal map, you must invert the green channel during conversion.

---

## 📦 Texture budgets & performance guardrails

These are guardrails for web-first delivery (tune per landmark complexity):

- ✅ Prefer **power-of-two** dimensions (512/1024/2048/4096)
- ✅ Keep total unique texture memory per landmark reasonable (target: **≤ 32–64 MB GPU** after compression)
- ✅ Use mipmaps (either embedded in KTX2 or generated at build time)
- ✅ Avoid 8K textures unless there is a **proven, measured** need

> [!TIP]
> If a landmark needs multiple materials, consider **atlas packing** (basecolor/normal/orm) for fewer binds—*only if it remains maintainable and reproducible*.

---

## 🧾 Provenance, licensing, and attribution

### Required: a per-folder manifest
Create/maintain `textures.manifest.json` that captures:
- ✅ file list + roles
- ✅ sha256 checksums
- ✅ source attribution + license for each texture
- ✅ conversion lineage (inputs → tool/version → outputs)

Example (shape only; adapt to your schema):

```json
{
  "schema_version": "TBD",
  "landmark_slug": "<landmark_slug>",
  "textures": [
    {
      "id": "<landmark_slug>_basecolor",
      "role": "basecolor",
      "file": "<landmark_slug>_basecolor.ktx2",
      "color_space": "srgb",
      "sha256": "TBD",
      "source": {
        "title": "TBD (scan/photo/artist)",
        "creator": "TBD",
        "license": "TBD",
        "source_url": "TBD"
      },
      "derivation": {
        "inputs": ["TBD"],
        "toolchain": ["toktx/basisu/etc (TBD)"],
        "notes": "TBD"
      }
    }
  ]
}
```

> [!IMPORTANT]
> If the upstream source is restricted, sensitive, or unclear, **do not ship** the derived texture in `web/assets/…` until governance review is complete (license clarity is non-negotiable).

### Metadata hygiene
- Strip EXIF and embedded metadata that can leak device/GPS/etc.
- Prefer deterministic exports (same inputs → same outputs)

---

## 🔌 Integration notes (glTF / materials)

General guidance:
- Materials should reference textures **relative to the model file** or via your asset loader’s resolved base path.
- Prefer glTF 2.0 metallic-roughness workflow (baseColor + ORM + normal + emissive).

Recommended mapping:
- `baseColorTexture` → `<landmark_slug>_basecolor.*`
- `normalTexture` → `<landmark_slug>_normal.*`
- `metallicRoughnessTexture` → `<landmark_slug>_orm.*` (G/B used by glTF; AO often wired separately depending on engine)
- `occlusionTexture` → `<landmark_slug>_orm.*` (R)

> [!NOTE]
> Some engines treat AO separately; document any engine-specific wiring in the **landmark’s parent README** (`web/assets/3d/landmarks/<landmark_slug>/README.md`) to avoid duplicating policy here.

---

## ✅ PR checklist (fail-closed)

| Check | Requirement |
|---|---|
| 📁 Canonical placement | Textures live here (no duplicates elsewhere) |
| 🧾 Manifest updated | `textures.manifest.json` updated + valid |
| 🔒 License clarity | Each texture has a license + attribution |
| 🧪 Determinism | Conversion steps documented (tool/version) |
| 🧮 Integrity | sha256 present (or CI computes/validates) |
| ⚡ Performance | Resolutions + formats within budget |
| 🧼 Metadata | EXIF stripped; no sensitive payloads |

---

## 🔗 References (project guidance)

- KFM documentation guidance on provenance-first + FAIR/CARE posture:  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM-style YAML front-matter + governed Markdown practices:  [oai_citation:2‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
