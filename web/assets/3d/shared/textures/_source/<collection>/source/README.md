---
title: "🧵 KFM Texture Source Pack — <collection>"
doc_kind: "asset-readme"
scope: "web/assets/3d/shared/textures/_source/<collection>/source"
status: "active"
owner: "KFM Maintainers"
last_reviewed: "2026-01-25"
---

# 🧵 Texture Source Pack — `<collection>`

![Asset Tier](https://img.shields.io/badge/asset-tier%3A_source_of_truth-000000)
![Pipeline](https://img.shields.io/badge/pipeline-provenance--first-2b6cb0)
![Runtime](https://img.shields.io/badge/runtime-WebGL%20%7C%20Cesium%20%7C%203D%20Tiles-6b46c1)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-f59e0b)
![Policy](https://img.shields.io/badge/CI-policy_gates%20(OPA%2FConftest)-111827)

**This folder holds the highest-fidelity, *unmodified* source textures for the `<collection>` texture library.**  
These sources feed KFM’s 3D experiences (Cesium globe/terrain, 3D Tiles content, AR-ready scenes, and Story Node visuals), where transparency, attribution, and sensitivity rules are first-class features. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

---

## 🔎 Quick Nav

- [✅ What belongs here](#-what-belongs-here)
- [🗂️ Folder layout](#️-folder-layout)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧱 PBR map cheat-sheet](#-pbr-map-cheat-sheet)
- [🧾 Required metadata](#-required-metadata)
- [🚦 Policy & governance](#-policy--governance)
- [⚡ Performance rules](#-performance-rules)
- [🤖 AI-assisted helpers](#-ai-assisted-helpers)
- [✅ Definition of Done](#-definition-of-done)
- [📚 Design authority](#-design-authority)

---

## ✅ What belongs here

> [!IMPORTANT]
> **`source/` is immutable-by-convention.**  
> Never “clean up” or overwrite originals. If it changes, it’s a **new version**.

### Put **in** `source/` 📥
- Vendor downloads (original ZIPs, original TIFF/PNG/JPG sets)
- Scan outputs (raw scans, untrimmed exports)
- Photogrammetry outputs (raw/aligned texture atlases before optimization)
- High-res PBR sets (albedo/baseColor, normal, roughness, metallic, AO, height)
- Source rasters intended for *draping imagery* on terrain (when the texture set is used as a raster overlay in 3D) :contentReference[oaicite:2]{index=2}

### Keep **out of** `source/` 🚫
- Runtime-optimized textures (KTX2/BasisU, resized “game-ready”, web-delivery JPGs)
- Auto-generated mipmaps, atlases, baked maps
- Anything “experimental” that may be discarded (that belongs in `../work/`)

---

## 🗂️ Folder layout

This README lives at:

`web/assets/3d/shared/textures/_source/<collection>/source/README.md`

Recommended structure (create missing folders as needed):

```text
📁 web/assets/3d/shared/textures/
└─ 📁 _source/
   └─ 📁 <collection>/
      ├─ 📁 source/                      ✅ immutable originals (YOU ARE HERE)
      │  ├─ 📁 vYYYY-MM-DD_<origin>/      🔒 snapshot of exactly what we received
      │  ├─ 📄 checksums.sha256           🧾 integrity (hashes for every file)
      │  ├─ 📄 manifest.source.json       🧭 provenance + license + intent
      │  ├─ 📄 ATTRIBUTION.md             🏷️ human-readable credits (if required)
      │  └─ 📄 README.md                  📌 this file
      ├─ 📁 work/                         🧪 editable working files (PSD/BLEND/etc.)
      └─ 📁 exports/                      🚀 deterministic runtime outputs (web-ready)
```

> [!NOTE]
> If your runtime assets live outside `_source/`, keep `exports/` as a **build artifact staging area** and publish from there (copy/sync into the runtime folder used by the app).  
> This mirrors KFM’s broader “deterministic packaging + dual formats” philosophy. :contentReference[oaicite:3]{index=3}

---

## 🏷️ Naming conventions

KFM favors **discoverability + determinism** (treat data/assets like code). :contentReference[oaicite:4]{index=4}

### ✅ Recommended pattern
**Directory (texture set):**
```text
<material-name>__<variant>__v<major>
```

**Files (maps):**
```text
<material-name>__<variant>__<map>__<res>.<ext>
```

### ✅ Examples
```text
brick_red__clean__v1/
  brick_red__clean__albedo__4k.tif
  brick_red__clean__normal__4k.tif
  brick_red__clean__roughness__4k.tif
  brick_red__clean__ao__4k.tif
```

### ✅ Allowed `<map>` values (standardize!)
- `albedo` (or `basecolor`)
- `normal`
- `roughness`
- `metallic`
- `ao`
- `height` (or `displacement`)
- `emissive`
- `opacity` (or `alpha`)
- `orm` (packed Occlusion/Roughness/Metallic)

> [!TIP]
> If a texture set is used by **Story Nodes**, keep names stable so story configs and markdown references don’t churn. Story Nodes are designed as simple **Markdown + JSON** contributions. :contentReference[oaicite:5]{index=5}

---

## 🧱 PBR map cheat-sheet

| Map | Typical role | Color space | Notes |
|---|---:|---:|---|
| `albedo` / `basecolor` | surface color | **sRGB** | avoid baked lighting/shadows when possible |
| `normal` | micro-surface direction | **Linear** | tangent-space normal maps expected in most web pipelines |
| `roughness` | microsurface scatter | **Linear** | white = rough, black = smooth (common convention) |
| `metallic` | metalness | **Linear** | usually near 0 or 1 (few grays) |
| `ao` | ambient occlusion | **Linear** | sometimes packed into `orm` |
| `height` | displacement/parallax | **Linear** | use carefully on mobile/AR |
| `emissive` | glow/light | **sRGB** | ensure it’s intentional (night signage etc.) |

> [!NOTE]
> KFM’s 3D stack includes CesiumJS (globe/terrain, 3D Tiles streaming), which commonly renders **textured** terrain and **textured building models**. Keep map roles explicit so exports can be generated consistently. :contentReference[oaicite:6]{index=6}

---

## 🧾 Required metadata

KFM is built around **traceability**: users should always be able to see the “map behind the map” (and the *asset behind the asset*). :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8}

### Minimum required files (in `source/`)
- `manifest.source.json` 🧭 (machine-readable provenance)
- `checksums.sha256` 🔐 (integrity)
- `ATTRIBUTION.md` 🏷️ (human credits, when license requires)
- *(optional but recommended)* `LICENSE.txt` or `LICENSE.spdx` 📜 (if not already in manifest)

### `manifest.source.json` (template)
```json
{
  "id": "kfm.texture.<collection>.<material>.<variant>.v1",
  "type": "kfm.texture.source",
  "title": "<Human title>",
  "collection": "<collection>",
  "intent": [
    "cesium_3d_tiles",
    "terrain_drape",
    "story_nodes",
    "ar_ready"
  ],
  "provenance": {
    "source_name": "<vendor/archive/project>",
    "source_url": "<where we got it>",
    "retrieved_utc": "2026-01-25T00:00:00Z",
    "author_or_org": "<creator>",
    "notes": "Keep a short, factual description of acquisition and constraints."
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution_required": true,
    "restrictions": ["no-ai-training", "non-commercial-only"]
  },
  "classification": "public",
  "care": {
    "labels": [],
    "notes": ""
  },
  "files": [
    {
      "path": "v2026-01-25_vendor/original/brick_red__clean__albedo__4k.tif",
      "sha256": "<fill>",
      "role": "albedo",
      "colorspace": "sRGB"
    }
  ],
  "derivatives": {
    "exports_dir": "../exports/<material>__<variant>__v1/",
    "runtime_dir": "../../../<collection>/<material>__<variant>__v1/"
  }
}
```

> [!IMPORTANT]
> **No provenance → no publish.**  
> This mirrors KFM’s “provenance-first publishing” rule (policy gated in CI). :contentReference[oaicite:9]{index=9}

---

## 🚦 Policy & governance

KFM governance is **fail-closed**: if we’re missing license/provenance/classification details, the default is to block publication until resolved. :contentReference[oaicite:10]{index=10}

### What CI policy gates typically enforce ✅
- Every asset has a **license** and **attribution** info (where applicable) :contentReference[oaicite:11]{index=11}
- No obvious **secrets** committed (tokens/keys) :contentReference[oaicite:12]{index=12}
- **Classification propagates**: outputs cannot be *less restrictive* than inputs :contentReference[oaicite:13]{index=13}
- “Pipeline ordering”: you can’t ship a runtime artifact if you skipped required metadata stages :contentReference[oaicite:14]{index=14}

### Sensitivity & ethical display 🛡️
The UI is designed to surface sensitivity (locks/warnings) and to generalize restricted content when needed (e.g., coarse display instead of exact location). Even for textures, this matters when imagery encodes sensitive context. :contentReference[oaicite:15]{index=15}

---

## ⚡ Performance rules

KFM runs in the browser (React UI + WebGL) and supports 2D/3D switching, 3D Tiles streaming, and mobile/AR ambitions. Optimize early. :contentReference[oaicite:16]{index=16} :contentReference[oaicite:17]{index=17}

### “Web-ready” export guidelines (for `../exports/`)
- Prefer **power-of-two** sizes when possible (512, 1024, 2048, 4096)
- Always generate **mipmaps** for runtime textures
- Avoid unnecessary alpha channels (they cost memory/bandwidth)
- Reuse textures across models when possible (shared library = fewer downloads)
- If targeting Cesium/3D Tiles or glTF pipelines, consider **KTX2/BasisU** exports (GPU compressed)

> [!TIP]
> KFM’s broader architecture leans on **deterministic packaging** (reproducible outputs with hashes). That’s the mindset for texture exports too. :contentReference[oaicite:18]{index=18}

---

## 📦 Optional: “treat textures like artifacts” (OCI + signatures)

KFM proposes using **OCI registries as storage** (ORAS) and **Cosign signatures** for artifacts—bringing software supply-chain rigor to data/assets. This is especially valuable for large binaries (textures, tilesets, models). :contentReference[oaicite:19]{index=19} :contentReference[oaicite:20]{index=20}

### What that buys us 🎯
- Pull by immutable **digest** (content-addressable)
- Rollback to known-good versions
- Attach provenance (PROV) and SBOM-like attestations alongside binaries
- Verified origin (Cosign) before runtime use :contentReference[oaicite:21]{index=21}

---

## 🤖 AI-assisted helpers

KFM’s AI features are explicitly designed to be **explainable** and to keep citations/traceability in the loop. Apply the same discipline to asset workflows. :contentReference[oaicite:22]{index=22}

### Allowed (helpful) AI usage ✅
- Auto-tagging texture sets (material type, era/region relevance)
- Detecting seams, repetition artifacts, compression banding
- Suggesting map packing (ORM), resolution tiers, or dedup opportunities
- Drafting `manifest.source.json` *from provided evidence* (human review required)

### Not allowed (without explicit approval) 🚫
- Re-licensing, removing attribution requirements, or “guessing” the source
- Generating derivative textures that could violate the source license
- Publishing AI-generated textures without marking them as such

> [!IMPORTANT]
> If AI contributes to edits or derivative generation, record it in provenance (who/what/when/tool versions).  
> KFM policy explicitly applies equally to humans and agents. :contentReference[oaicite:23]{index=23}

---

## ✅ Definition of Done

Before a texture set is considered “ready to publish”:

- [ ] Original files are stored under a version folder `vYYYY-MM-DD_<origin>/` (no overwrites)
- [ ] `manifest.source.json` exists and includes **license + attribution + source URL + retrieved date**
- [ ] `checksums.sha256` exists and matches files
- [ ] Sensitivity/classification reviewed (and marked) 🔒 :contentReference[oaicite:24]{index=24}
- [ ] Runtime exports (if any) are generated deterministically into `../exports/`
- [ ] Story Node usage (if any) includes credits/citations in markdown/config :contentReference[oaicite:25]{index=25}
- [ ] CI policy gates pass (license/provenance/safety) :contentReference[oaicite:26]{index=26}

---

## 📚 Design authority

These project documents define the principles this README follows (pipeline rigor, provenance-first, 2D/3D/AR goals, policy gates, and UI transparency):

- **KFM — Comprehensive Technical Documentation** :contentReference[oaicite:27]{index=27}  
- **KFM — Comprehensive Architecture, Features, and Design** :contentReference[oaicite:28]{index=28}  
- **KFM — AI System Overview 🧭🤖** :contentReference[oaicite:29]{index=29}  
- **KFM — Comprehensive UI System Overview** :contentReference[oaicite:30]{index=30}  
- **KFM — Data Intake: Technical & Design Guide** :contentReference[oaicite:31]{index=31}  
- **Innovative Concepts to Evolve KFM** :contentReference[oaicite:32]{index=32}  
- **Latest Ideas & Future Proposals** :contentReference[oaicite:33]{index=33}  
- **Additional Project Ideas (Policy Gates, OCI artifacts, etc.)** :contentReference[oaicite:34]{index=34}  
- **Maps / Virtual Worlds / Geospatial WebGL Resource Pack** :contentReference[oaicite:35]{index=35}  
- **AI Concepts & more (resource pack)** :contentReference[oaicite:36]{index=36}  
- **Various programming languages & resources (resource pack)** :contentReference[oaicite:37]{index=37}  
- **Data Management / Architectures / Data Science (resource pack)** :contentReference[oaicite:38]{index=38}  

---

## 🧩 Collection setup (fill this in)

When you create a new `<collection>`, update these fields in the YAML front-matter:

- `title`: `🧵 KFM Texture Source Pack — <collection>`
- `owner`: team/person responsible for approvals
- `status`: `active | draft | deprecated`
- Optional: add collection intent keywords to `manifest.source.json`

> [!TIP]
> Keep collections small and purposeful (e.g., `terrain-drapes`, `pbr-materials`, `buildings-historic`, `ui-atlases`) so downstream pipelines and Story Nodes can reference them cleanly.

