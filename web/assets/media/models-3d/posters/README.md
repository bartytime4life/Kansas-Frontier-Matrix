---
title: "3D Model Posters"
path: "web/assets/media/models-3d/posters/README.md"
version: "v1.0.0"
last_updated: "2026-01-17"
status: "active"
doc_kind: "Asset README"
license: "CC-BY-4.0"
markdown_protocol_version: "1.0"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"
doc_uuid: "urn:kfm:doc:web:assets:models-3d:posters:readme:v1.0.0"
---

# 🖼️ 3D Model Posters

![web](https://img.shields.io/badge/web-assets-0b5fff) ![type](https://img.shields.io/badge/type-3D%20model%20posters-6f42c1) ![format](https://img.shields.io/badge/prefer-WebP%20%7C%20AVIF-1a7f37) ![principle](https://img.shields.io/badge/principle-provenance--first-critical)

Static **poster images** (a.k.a. previews) for our **3D model library**. These are the “first impression” visuals used in the web UI for things like galleries, search results, and loading placeholders.

> [!IMPORTANT]
> KFM runs **provenance-first** and **contract-first**: anything that shows up in the UI must be traceable back to cataloged sources and processing steps — no “mystery layers/assets.”  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📘 Overview

### 🎯 Purpose
- Give every `.glb/.gltf` a fast-loading **preview image** ✅
- Keep posters **web-optimized** (small, sharp, consistent) ⚡
- Preserve **traceability** (license + provenance metadata) 🔎

### 🧭 Scope

| ✅ In Scope | ❌ Out of Scope |
|---|---|
| Poster/preview images for 3D models | Source art files (`.psd`, `.blend`, raw renders) |
| File naming + format + size standards | Full model pipeline docs (belongs elsewhere) |
| Poster metadata sidecar (`.poster.json`) | 3D geometry optimization (decimation, Draco, etc.) |

### 👥 Audience
- 🧑‍💻 Frontend devs wiring the 3D gallery/viewer
- 🧑‍🎨 Contributors generating renders/previews
- 🧑‍⚖️ Reviewers checking license + attribution + provenance

### 🧩 Definitions
- **Poster** 🖼️: the “hero” preview image associated with a 3D model.
- **Thumbnail** 🔹: a smaller/cropped version used in grids (optional, but recommended).
- **Poster Contract** 🧾: sidecar metadata (JSON) that explains provenance, licensing, and what model the poster represents.

---

## 📂 Directory Layout

```text
web/
└─ 📁 assets/
   └─ 🎞️ media/
      └─ 🧊 models-3d/
         ├─ 🧊 models/                 # ✅ 3D runtime files (.glb/.gltf) actually served by the app
         └─ 🖼️ posters/                # 👈 you are here 📌 Poster/cover images for 3D assets (cards, loading states)
            ├─ 🖼️ <slug>.webp          # Primary poster image (web-optimized; consistent aspect ratio)
            ├─ 🧾 <slug>.poster.json   # Required sidecar: model refs, camera framing, license, provenance, alt text
            ├─ 🖼️ <slug>__thumb.webp   # Optional tiny thumbnail (fast lists / low-bandwidth)
            └─ 📄 README.md            # Rules: naming, target sizes, safe backgrounds, and required metadata fields
```

Why this lives under `web/`:
- The project is designed around **browser-first access** using standard web tech, keeping barriers low for collaborators and public users.  [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

---

## 🏷️ Naming Conventions

### ✅ Basename Mirroring (recommended)
**Poster filenames should mirror the model filename** (same slug, different extension):

- `models/<slug>.glb` ➜ `posters/<slug>.webp`
- `models/<slug>.gltf` ➜ `posters/<slug>.webp`

Example:
- `web/assets/media/models-3d/models/smoky-hill-1865.glb`
- `web/assets/media/models-3d/posters/smoky-hill-1865.webp`
- `web/assets/media/models-3d/posters/smoky-hill-1865.poster.json`

### 🔤 Slug rules
- ✅ `kebab-case`
- ✅ ASCII only (`a-z`, `0-9`, `-`, `_`)
- ✅ include time/version when the model represents a time slice: `kansas-terrain-1850`, `kansas-terrain-1900`
- ❌ no spaces, no “final_final2”, no ambiguous names like `model1`

> [!TIP]
> If your model naming includes an ID/version, keep it in the poster too — it makes catalog mapping deterministic and supports auditability.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧾 Poster Metadata Contract

KFM’s architecture treats metadata as first-class and enforces structured “contracts” for artifacts.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
Posters follow that same rule: **every poster should have a sidecar JSON**.

### ✅ Required Files Per Model
| File | Required | Purpose |
|---|---:|---|
| `<slug>.webp` | ✅ | Web poster image |
| `<slug>.poster.json` | ✅ | Provenance + license + linkage to the 3D model |
| `<slug>__thumb.webp` | ⭐ optional | Small grid-friendly thumbnail |

### 🧱 Minimum Contract Fields (poster JSON)
Your `<slug>.poster.json` MUST include:
- `id` — stable unique ID (URN-style preferred)
- `kind` — `"poster"`
- `for_model` — path or ID of the `.glb/.gltf`
- `title` — human-friendly name
- `license` — e.g. `CC-BY-4.0`, `CC0-1.0`, etc.
- `attribution` — plain text attribution string
- `sources[]` — list of upstream sources (datasets, archives, scans, etc.)
- `processing[]` — short steps describing how the poster was produced
- `created_at` — ISO timestamp
- `checksum_sha256` — integrity hash of the poster file
- `alt` — accessibility text for UI use

> [!NOTE]
> KFM documentation and pipelines emphasize **schema validation** and **link/reference validation** in CI. Treat poster metadata as schema-validated content, not “random JSON.”  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧪 Example `*.poster.json`
```json
{
  "id": "urn:kfm:asset:models-3d:poster:smoky-hill-1865:v1",
  "kind": "poster",
  "for_model": "../models/smoky-hill-1865.glb",
  "title": "Smoky Hill Terrain (1865)",
  "alt": "3D terrain model preview showing the Smoky Hill region with shaded relief.",
  "license": "CC-BY-4.0",
  "attribution": "Derived from public-domain elevation and historical references; compiled by KFM contributors.",
  "sources": [
    { "type": "dataset", "id": "urn:kfm:dataset:TBD", "note": "Replace with real dataset IDs/links." }
  ],
  "processing": [
    "Rendered from canonical camera preset (kfm_poster_cam_v1).",
    "Color-managed to sRGB and exported to WebP (quality=82)."
  ],
  "created_at": "2026-01-17T00:00:00Z",
  "checksum_sha256": "sha256:TBD"
}
```

---

## 🎛️ Render & Export Specs

### ✅ Preferred Formats
- **Primary:** `.webp` (best tradeoff: quality / size / browser support)
- **Allowed:** `.jpg` (fallback for photographic posters)
- **Use sparingly:** `.png` (only if transparency is required)

### 📐 Dimensions & Aspect
Pick ONE “default” poster aspect for consistency:
- **Recommended:** `16:9` (good for hero viewers) → e.g. `1600×900`
- **OR:** `1:1` (good for grid cards) → e.g. `1024×1024`

If your UI needs both:
- `posters/<slug>.webp` → hero poster (16:9)
- `posters/<slug>__thumb.webp` → thumbnail (square)

### ⚡ File Size Budgets
- Poster (hero): **≤ 400 KB** target
- Thumbnail: **≤ 120 KB** target

> [!TIP]
> The goal is instant UI feedback. If it “feels heavy,” it *is* heavy. Optimize harder 😄

### 🧭 Composition Guidelines (visual consistency)
- Keep the subject centered with ~5–8% safe margin
- Prefer neutral/consistent lighting & background
- Avoid baking text labels into posters when possible (UI should own text)
- If the model is geospatial/time-based, choose a camera angle that helps interpret shape/terrain

For archaeological / field-derived 3D work, **robust acquisition + validation routines** are key; posters should reflect the “validated” representation rather than an unverified draft render.  [oai_citation:5‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

---

## ✅ Quality Gates

### 🔍 Local Checklist (before PR)
- [ ] Poster exists: `posters/<slug>.webp`
- [ ] Naming mirrors model slug
- [ ] Poster looks correct in the web UI (no stretching/cropping surprises)
- [ ] File size is within budget
- [ ] Sidecar metadata exists: `posters/<slug>.poster.json`
- [ ] License + attribution are filled (no “TBD” in merged PRs)
- [ ] `alt` text is meaningful and concise

### 🤖 CI Expectations (how we keep trust)
KFM’s documentation and data governance emphasize:
- YAML front-matter checks and required sections ✅
- Link/reference validation ✅
- JSON schema validation ✅
- Sensitive/PII checks ✅  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Posters should align with the same philosophy**: validated metadata, no broken references, and no silent “mystery” content.

---

## 🔐 Sensitivity & Ethics

> [!WARNING]
> If a 3D model (or its exact location) is sensitive, **do not publish a revealing poster**.
> Use a generalized/obfuscated render, or omit the poster and mark the asset appropriately in metadata.

This matches the project’s broader approach to classification consistency and sensitive content scanning in governance workflows.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📚 References (Project Principles)

- **KFM contract-first + provenance-first rule** (no mystery assets; traceability; metadata as first-class)  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Repository structure + web-first accessibility** (why these assets sit under `web/`)  [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
- **Markdown + CI governance patterns** (front-matter checks, schema validation, link validation)  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **Markdown templates & governance-minded doc structure** (YAML front-matter + standard sections)  [oai_citation:11‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
- **3D field workflows + validation emphasis** (context for disciplined 3D representations)  [oai_citation:12‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
