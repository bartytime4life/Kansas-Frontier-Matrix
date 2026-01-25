---
title: "🧱 Material Notes — `<material_slug>`"
path: "web/assets/3d/shared/materials/library/<material_slug>/notes.md"
doc_kind: "material_notes"
status: "draft" # draft | review | approved | deprecated
version: "0.1.0"
last_updated: "2026-01-25"
owners:
  - "TBD (@handle)"
reviewers:
  - "TBD (@handle)"
material:
  slug: "<material_slug>"         # kebab-case
  display_name: "TBD"
  category: "TBD"                 # terrain|rock|soil|vegetation|wood|metal|masonry|water|ui|procedural|other
  workflow: "pbrMetallicRoughness"
  engines:
    - "cesiumjs"
    - "threejs"
    - "gltf/3d-tiles"
  tags:
    - "TBD"
governance:
  sensitivity: "TBD"              # public|restricted|sensitive
  rationale: "TBD"
  care_notes: "TBD"
license:
  spdx: "TBD"
  attribution: "TBD"
  upstream_source: "TBD"
provenance:
  evidence_manifest: "sources/evidence_manifest.yaml"  # optional but strongly recommended
  source_receipt: "sources/source_receipt.yaml"
  prov_jsonld: "sources/prov.jsonld"                   # optional but strongly recommended
  checksums: "sources/checksums.txt"
integrity:
  doc_uuid: "TBD"
  git_commit: "TBD"
  build_run_id: "TBD"              # pipeline/run manifest id (if available)
---

<!--
🧭 Template rules (keep this consistent across the repo):
- Do NOT delete front-matter keys; use "TBD" if unknown.
- This file is the canonical human-readable spec for the material pack.
- Align with KFM's evidence-first + governance-first approach (sources, provenance, and sensitivity are not optional in practice).:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}
-->

# 🧱 Material Notes — `<material_slug>`

![status](https://img.shields.io/badge/status-draft-yellow)
![pbr](https://img.shields.io/badge/PBR-metallic--roughness-blue)
![targets](https://img.shields.io/badge/targets-Cesium%20%7C%20Three%20%7C%20glTF-6f42c1)
![governance](https://img.shields.io/badge/governance-sensitivity%20tracked-orange)

> [!IMPORTANT]
> **KFM principle:** nothing is a “black box.” Materials are treated as publishable *evidence-backed assets* (license + provenance + sensitivity). This mirrors how KFM treats datasets and stories (catalog-driven, evidence-first, provenance-first publishing).:contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

---

## 🧭 Quick Nav
- [📘 Overview](#-overview)
- [📁 Directory Layout](#-directory-layout)
- [🎨 Material Specification](#-material-specification)
- [🧬 Provenance, Licensing, CARE/FAIR](#-provenance-licensing-carefair)
- [🧩 Integration Notes](#-integration-notes)
- [✅ QA Checklist](#-qa-checklist)
- [🗓️ Change Log](#️-change-log)
- [📚 Source Docs Used](#-source-docs-used)

---

## 📘 Overview

### 🎯 Purpose
Provide a **single source of truth** for this material pack:
- what it represents (visually + physically)
- what files exist and how they’re encoded
- how it should be used in **KFM’s 2D/3D UI + Story Nodes + (future) AR** contexts:contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}
- how to verify license/provenance/sensitivity before shipping to users:contentReference[oaicite:6]{index=6}

### 🧩 Scope
This file documents the **processed, web-ready** material package located at:

`web/assets/3d/shared/materials/library/<material_slug>/`

It should also **link back** to the upstream/raw sources and the pipeline run that produced this pack (when available).

### 👥 Audience
- 🎨 3D/Front-end implementers (CesiumJS / Three.js / glTF)
- 🧪 QA reviewers + maintainers (policy checks, performance)
- 🧾 Governance reviewers (license, sensitivity, CARE alignment)
- 🧭 Story/Content authors referencing the material in Story Nodes / Pulse Threads:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

### 🧾 Definitions
- **Material pack**: a versioned set of textures + a material contract (`material.json`) + provenance/receipt files.
- **Evidence manifest**: a concise YAML file that enumerates what sources + claims justify the asset (patterned after Story Node evidence manifests).:contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}
- **Sensitivity**: governance classification that may change how/if the material is exposed in UI (lock icons, gating, generalization).:contentReference[oaicite:11]{index=11}

### 🧱 Key Artifacts (expected)
- `material.json` (machine-readable contract)
- `maps/*.ktx2` (compressed GPU textures)
- `preview.png` (swatch / preview)
- `sources/*` (license + source receipt + checksums + optional PROV + optional evidence manifest)

### ✅ Definition of Done
- [ ] Front-matter is complete (no unknowns left except intentionally `TBD`)
- [ ] **License & attribution** recorded (SPDX + attribution text)
- [ ] **Provenance** includes a source receipt + checksums (and ideally PROV + evidence manifest)
- [ ] Material renders correctly in **Cesium** and/or **Three.js** test scenes
- [ ] Performance budget met (texture sizes, compression, mipmaps)
- [ ] Sensitivity classification correct + rationale included
- [ ] Passes policy-as-code checks (fail-closed) before merge/publish:contentReference[oaicite:12]{index=12}

---

## 📁 Directory Layout

> [!TIP]
> Keep this layout consistent; consumers should be able to load any material pack by slug.

```text
📁 web/assets/3d/shared/materials/library/<material_slug>/
├─ 📄 notes.md                          # ← you are here
├─ 📄 material.json                     # material contract (required)
├─ 🖼️ preview.png                       # swatch / preview (required)
├─ 🎞️ preview_turntable.mp4             # optional
├─ 📁 maps/                             # texture payloads (required)
│  ├─ basecolor.ktx2                    # sRGB
│  ├─ normal.ktx2                       # linear
│  ├─ orm.ktx2                          # linear (Occlusion/Roughness/Metallic packed)
│  ├─ emissive.ktx2                     # optional (sRGB)
│  └─ height.exr                        # optional (linear, for displacement workflows)
└─ 📁 sources/                          # governance + provenance (required)
   ├─ license.txt
   ├─ attribution.txt
   ├─ source_receipt.yaml
   ├─ checksums.txt
   ├─ prov.jsonld                       # recommended
   └─ evidence_manifest.yaml            # recommended
```

---

## 🎨 Material Specification

### 🧾 Identity
| Field | Value |
|---|---|
| Slug | `<material_slug>` |
| Display name | `TBD` |
| Category | `TBD` |
| Intended look | `TBD (photoreal / stylized / hybrid)` |
| Primary environment | `TBD (prairie / riverbank / masonry / metalwork / etc.)` |
| Temporal variants | `TBD (optional: 1850 / 1900 / 1950 / modern)` |

> [!NOTE]
> KFM is time-first (timeline slider + time-filtered exploration), so material variants **can** become a storytelling feature (e.g., “aged vs restored”).:contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}

### 🧠 PBR Workflow
**Workflow:** Metallic-Roughness (glTF compatible)

| Channel | Source | Encoding | Notes |
|---|---|---|---|
| Base Color | `maps/basecolor.ktx2` | sRGB | No baked lighting; neutral albedo |
| Normal | `maps/normal.ktx2` | Linear | Standard tangent-space |
| Occlusion | `maps/orm.ktx2 (R)` | Linear | Packed |
| Roughness | `maps/orm.ktx2 (G)` | Linear | Packed |
| Metallic | `maps/orm.ktx2 (B)` | Linear | Packed |
| Emissive | `maps/emissive.ktx2` | sRGB | Optional |
| Height | `maps/height.exr` | Linear | Optional displacement workflows |

### 📏 Scale, Tiling & UVs
- **Real-world scale:** `TBD (meters per texture repeat)`
- **UV conventions:** `TBD (UV0 primary, UV1 optional for AO)`
- **Tiling strategy:** `TBD (seamless / trim sheet / unique unwrap)`
- **Rotation constraints:** `TBD`

> [!WARNING]
> If the material represents a culturally sensitive pattern/texture or a specific heritage artifact surface, **do not publish as public** without governance review. Use sensitivity gating and/or abstraction. KFM’s UI and policies are designed to surface and enforce sensitivity classifications.:contentReference[oaicite:15]{index=15}:contentReference[oaicite:16]{index=16}

### 🖼️ Texture Budget (default guidance)
> Tune these per platform; keep the “why” documented.

- Desktop: basecolor/normal/orm up to `2048²` each (if needed)
- Mobile/offline pack: prefer `1024²` or `512²`
- Always generate mipmaps (avoid shimmer)
- Prefer KTX2 (BasisU) payloads for web GPU efficiency

### ⚙️ Material Contract (`material.json`) — Example
```json
{
  "slug": "<material_slug>",
  "name": "TBD",
  "category": "TBD",
  "workflow": "pbrMetallicRoughness",
  "textures": {
    "baseColor": "maps/basecolor.ktx2",
    "normal": "maps/normal.ktx2",
    "orm": "maps/orm.ktx2",
    "emissive": "maps/emissive.ktx2"
  },
  "params": {
    "baseColorFactor": [1, 1, 1, 1],
    "metallicFactor": 0.0,
    "roughnessFactor": 0.9,
    "normalScale": 1.0,
    "occlusionStrength": 1.0
  },
  "uv": {
    "repeat": [1, 1],
    "offset": [0, 0],
    "rotation": 0
  },
  "governance": {
    "sensitivity": "public",
    "licenseSpdx": "TBD",
    "attribution": "TBD"
  }
}
```

---

## 🧬 Provenance, Licensing, CARE/FAIR

### 📜 License (required)
- **SPDX:** `TBD`
- **Attribution statement:** `TBD`
- **Upstream source(s):** `TBD`
- **Usage constraints:** `TBD (commercial allowed? share-alike? attribution required?)`

> [!IMPORTANT]
> KFM treats licensing as a first-class requirement; policy gates can fail merges if license/provider info is missing. Make it explicit here and in receipts/manifests.:contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}

### 🧾 Source Receipt (`sources/source_receipt.yaml`) — Template
```yaml
material_slug: "<material_slug>"
retrieved_at: "TBD (ISO 8601)"
source_type: "TBD (scan|photo|procedural|library|photogrammetry)"
source_urls:
  - "TBD"
authors:
  - "TBD"
license:
  spdx: "TBD"
  link: "TBD"
notes: "TBD (what was done to create maps, what assumptions were made)"
```

### 🔏 Checksums (`sources/checksums.txt`)
- Include SHA-256 for every shipped file (maps, contract, preview).
- This supports auditability and “what exactly shipped?” questions.

### 🧾 Evidence Manifest (`sources/evidence_manifest.yaml`) — Recommended
Patterned after KFM story/pulse evidence manifests so **AI + users** can trace what supports the asset.

Why:
- KFM’s AI is designed to **always cite sources** and to refuse/flag uncertainty when sources are missing.:contentReference[oaicite:19]{index=19}
- KFM Pulse Threads and Story Nodes attach provenance + evidence manifests to keep narratives verifiable; the same pattern works for assets.:contentReference[oaicite:20]{index=20}

```yaml
id: "EM-<material_slug>-TBD"
claims:
  - id: "C1"
    statement: "Material represents <TBD> surface typical of <TBD region/time>."
    evidence:
      - kind: "photo_set"
        ref: "TBD"
      - kind: "document"
        ref: "TBD"
inputs:
  - id: "SRC-1"
    description: "Original scan/photos/procedural seed"
    uri: "TBD"
governance:
  sensitivity: "TBD"
  care_notes: "TBD"
```

### 🧠 CARE + FAIR (how this material aligns)
- **Findable/Interoperable**: consistent slug + contract + optional catalog/PROV links:contentReference[oaicite:21]{index=21}
- **Reusable**: license, attribution, checksums, and documented parameters
- **Authority to Control / Responsibility**: sensitivity classification and rationale must exist when cultural/heritage concerns apply:contentReference[oaicite:22]{index=22}:contentReference[oaicite:23]{index=23}

---

## 🧩 Integration Notes

### 🌍 KFM UI & User Trust Hooks
KFM’s UI emphasizes “the map behind the map” — users can inspect sources/metadata and see provenance cues rather than trusting a black-box visualization.:contentReference[oaicite:24]{index=24}

**Material UI expectations (recommended):**
- Show a **material swatch** (preview) wherever the material is selectable.
- Include a “Material Info” panel that mirrors Layer Info behavior:
  - license + attribution
  - provenance receipt link
  - sensitivity indicator (lock icon / warning)
- If used in a Story Node: cite the material in the story’s evidence manifest (or reference this pack’s evidence manifest).:contentReference[oaicite:25]{index=25}:contentReference[oaicite:26]{index=26}

### 🗺️ 2D/3D Mode
KFM uses MapLibre (2D) and CesiumJS (3D) with a smooth 2D/3D toggle, carrying map context and enabling 3D tiles/terrain visualization.:contentReference[oaicite:27]{index=27}:contentReference[oaicite:28]{index=28}

**Implications for materials:**
- Prefer **glTF-friendly** PBR settings so the same pack can be used for 3D Tiles / glTF models.
- Keep textures optimized for browser GPU constraints (mipmaps, compression).
- If a material is used for terrain storytelling (“imagery draped on terrain”), document tiling and scale assumptions explicitly.:contentReference[oaicite:29]{index=29}

### 🛰️ 3D Tiles / glTF
- If this material ships as part of a glTF model, ensure texture references align with `material.json`.
- If used by multiple models, prefer referencing this library path by slug rather than duplicating maps in each model folder.

### 📱 AR Readiness (future-facing)
KFM’s architecture anticipates AR clients as additional consumers of the same standardized services, enabling overlays on real landscapes.:contentReference[oaicite:30]{index=30}

**Material note:** if you expect AR use:
- include mobile-friendly texture variants (smaller sizes)
- ensure licensing allows redistribution on mobile clients
- avoid overly high-frequency detail that aliasing exaggerates in AR

### 🧠 Focus Mode / AI Explainability
Focus Mode is designed to:
- cite sources for every answer
- reflect user context (location/time/layers)
- surface explainability/audit cues:contentReference[oaicite:31]{index=31}

**Therefore, this notes.md should:**
- describe what the material represents (plain language)
- point to evidence/receipt/PROV so the AI can cite them
- clarify what is unknown or approximate (avoid accidental hallucinations)

---

## 🏗️ Pipeline + Governance (how this gets built safely)

### 🔁 Evidence-first build flow (recommended)
```mermaid
flowchart LR
  A[🧪 Raw sources (immutable)] --> B[🧼 Normalize & de-light]
  B --> C[🎛️ Generate PBR maps]
  C --> D[🧊 Compress to KTX2 + mipmaps]
  D --> E[🧾 Produce receipts + checksums + (optional) PROV + evidence manifest]
  E --> F[🛡️ Policy gates (fail-closed)]
  F --> G[📦 Publish to web/assets/3d/shared/materials/library/<slug>/]
  G --> H[🔎 Index for discovery (optional)]
```

> [!NOTE]
> This mirrors KFM’s catalog-driven + provenance-first approach where artifacts are not published/used until provenance exists, including for dynamic/rapid data flows.:contentReference[oaicite:32]{index=32}

### 🛡️ Policy gates (examples)
- require SPDX license + attribution text
- forbid unknown sensitivity
- require checksums for shipped files
- require no secrets embedded
- enforce naming conventions

This is consistent with KFM’s policy-as-code approach where CI rejects non-compliant changes (fail-closed).:contentReference[oaicite:33]{index=33}

### 📦 Optional: OCI Packaging for Material Packs
If/when KFM adopts OCI artifact storage for distributable assets:
- push the material pack as an OCI artifact (ORAS)
- sign with Cosign (keyless OIDC)
- attach PROV JSON-LD / SBoM / attestations as referrers:contentReference[oaicite:34]{index=34}:contentReference[oaicite:35]{index=35}

This enables offline packs, federation, and verifiable supply chain distribution.

---

## ✅ QA Checklist

### 👁️ Visual QA
- [ ] No baked shadows/lighting in basecolor (unless explicitly intended)
- [ ] Normal map orientation correct (no “inverted dents”)
- [ ] Roughness/metallic ranges make sense for the surface type
- [ ] No visible seams at intended tile scale
- [ ] Preview matches in-engine look (Cesium/Three test)

### 🚀 Performance QA
- [ ] Textures are KTX2 (or documented exception)
- [ ] Mipmaps present
- [ ] Texture sizes within budget for target platforms
- [ ] No unnecessary channels (pack where possible)

### 🧾 Governance QA
- [ ] SPDX license present
- [ ] Attribution present
- [ ] Source receipt complete
- [ ] Checksums complete
- [ ] Sensitivity classification set + rationale written
- [ ] (Recommended) Evidence manifest exists
- [ ] (Recommended) PROV exists or is linked

### 🤖 AI/UX QA
- [ ] Notes include plain-language description usable by Focus Mode
- [ ] Evidence/provenance links are present so answers can be cited:contentReference[oaicite:36]{index=36}

---

## 🗓️ Change Log

| Date | Version | Change | Author | Review |
|---|---:|---|---|---|
| 2026-01-25 | 0.1.0 | Initial template created | TBD | TBD |

---

## 📚 Source Docs Used

### ✅ KFM Core (Architecture / UI / AI / Data Intake)
- KFM Technical Documentation :contentReference[oaicite:37]{index=37}  
  (2D/3D stack, provenance transparency, Story Nodes):contentReference[oaicite:38]{index=38}:contentReference[oaicite:39]{index=39}
- KFM Architecture, Features, and Design :contentReference[oaicite:40]{index=40}  
  (2D↔3D toggle, AR readiness, tech stack context):contentReference[oaicite:41]{index=41}:contentReference[oaicite:42]{index=42}
- KFM UI System Overview :contentReference[oaicite:43]{index=43}  
  (sensitivity indicators, 3D tiles behavior, mode switching):contentReference[oaicite:44]{index=44}:contentReference[oaicite:45]{index=45}
- KFM AI System Overview :contentReference[oaicite:46]{index=46}  
  (always cites sources, explainability/audit cues):contentReference[oaicite:47]{index=47}
- KFM Data Intake — Technical & Design Guide :contentReference[oaicite:48]{index=48}  
  (STAC/DCAT/PROV linkage, evidence-first, provenance-first publishing):contentReference[oaicite:49]{index=49}:contentReference[oaicite:50]{index=50}

### 💡 KFM Expansion Ideas (Stories / Governance / Supply Chain)
- Additional Project Ideas (Pulse Threads, evidence manifests, policy gates, OCI artifacts) :contentReference[oaicite:51]{index=51}:contentReference[oaicite:52]{index=52}:contentReference[oaicite:53]{index=53}:contentReference[oaicite:54]{index=54}
- Innovative Concepts to Evolve KFM (4D digital twins, AR/hybrid storytelling) :contentReference[oaicite:55]{index=55}:contentReference[oaicite:56]{index=56}
- Latest Ideas & Future Proposals :contentReference[oaicite:57]{index=57} (used as planning context)

### 📚 Supporting Resource Portfolios (embedded libraries)
> These are reference libraries bundled as PDF portfolios; use them for deeper implementation research when needed.
- AI Concepts & more :contentReference[oaicite:58]{index=58}
- Maps / Google Maps / Virtual Worlds / Geo WebGL :contentReference[oaicite:59]{index=59}
- Various programming languages & resources :contentReference[oaicite:60]{index=60}
- Data Management / Architectures / Bayesian Methods :contentReference[oaicite:61]{index=61}

---

## 🧷 Appendix: “Fill Me In” Minimal Checklist (for fast authoring)
- [ ] Set `material.display_name`
- [ ] Set `license.spdx` + `license.attribution`
- [ ] Set `governance.sensitivity` + rationale
- [ ] Verify `material.json` paths exist
- [ ] Add `sources/source_receipt.yaml` + `sources/checksums.txt`
- [ ] Add `sources/evidence_manifest.yaml` (recommended)

