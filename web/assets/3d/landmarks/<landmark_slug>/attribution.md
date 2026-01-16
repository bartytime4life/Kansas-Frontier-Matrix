---
kfm_md_protocol: "KFM-MDP"
kfm_md_protocol_version: "11.2.6"
doc_kind: "asset-attribution"
doc_uuid: "c96e7b6e-acde-4a2b-8a1c-4b9a7c5f2d22"
canonical_path: "web/assets/3d/landmarks/<landmark_slug>/attribution.md"
title: "🏛️ Landmark Attribution — <Landmark Name> (<landmark_slug>)"
status: "draft"
created: "2026-01-15"
updated: "2026-01-15"
audience:
  - maintainers
  - legal
  - contributors
  - ui
tags:
  - kfm
  - 3d
  - landmark
  - attribution
  - licensing
  - provenance
---

# 🏛️ Landmark Attribution — <Landmark Name> (`<landmark_slug>`)

![KFM](https://img.shields.io/badge/KFM-Frontier%20Matrix-1f6feb?style=flat-square)
![Asset](https://img.shields.io/badge/Asset-3D%20Landmark-7c3aed?style=flat-square)
![Purpose](https://img.shields.io/badge/Purpose-Attribution%20%26%20License%20Ledger-f97316?style=flat-square)

> ✅ **Goal:** a single, human-readable + machine-parsable place to capture *who made what*, *where it came from*, and *what license terms apply* for this landmark’s 3D bundle.

---

## 🧭 What this file covers

This attribution ledger applies to assets stored under:

📁 `web/assets/3d/landmarks/<landmark_slug>/`

Including (but not limited to):

- 🧱 **Models** (e.g., `.glb`, `.gltf`, `.obj`, `.fbx`)
- 🖼️ **Textures** (e.g., `.png`, `.jpg`, `.webp`, `.ktx2`)
- 🧪 **Derived/optimized** versions (decimation, baking, atlas generation, compression)
- 🧾 **License artifacts** stored in:
  - 📁 `web/assets/3d/landmarks/<landmark_slug>/licenses/`
  - 📁 `web/assets/3d/landmarks/<landmark_slug>/textures/` (texture-specific notes if needed)

---

## ⚡ Copy/paste attribution (UI-ready)

### 🏷️ Short form
> **<Landmark Name> 3D model** — © <Creator/Org> (<Year>). Source: <Repository/Archive/URL>. License: <SPDX/CC label>. Modifications: <Yes/No>.

### 🧾 Long form
> **<Landmark Name> 3D asset bundle** includes model geometry, textures, and derived render-optimized artifacts.  
> **Model:** © <Creator/Org> (<Year>), <Link>. License: <License>.  
> **Textures:** © <Creator/Org> (<Year>), <Link>. License: <License>.  
> **Processing/changes by KFM:** <Describe exact changes: retopo/decimation/bake/atlas/compress>, <Date>.  
> **Required attribution:** <Exact required attribution text from upstream license, if any>.

> 🧠 Tip: If the upstream requires *specific* wording, paste it verbatim in the “Required attribution” fields below.

---

## 🧾 Machine-readable attribution record (KFM-friendly)

> Keep this block updated; tooling can parse it later.

```yaml
landmark:
  slug: "<landmark_slug>"
  name: "<Landmark Name>"
  location:
    place_name: "<City/County/State>"
    centroid_wgs84: ["<lon>", "<lat>"] # optional
  kfm_ids:
    internal_asset_id: "<uuid-or-kfm-id>" # optional

bundle:
  combined_license_policy: "MOST_RESTRICTIVE_WINS"
  combined_license_result: "<computed (e.g., CC-BY-4.0)>"
  combined_attribution_required: true

components:
  - kind: "model"
    local_paths:
      - "web/assets/3d/landmarks/<landmark_slug>/<MODEL_FILE>"
    upstream:
      title: "<Upstream title>"
      author: "<Person/Org>"
      source_url: "<https://...>"
      source_date: "<YYYY-MM-DD or YYYY>"
      license:
        spdx_or_label: "<e.g., CC-BY-4.0 / CC0-1.0 / MIT / Proprietary>"
        license_url: "<https://...>"
        attribution_text_required: "<paste exact required wording or 'none'>"
      proof:
        evidence_path: "web/assets/3d/landmarks/<landmark_slug>/licenses/<FILE_OR_SCREENSHOT>"
        notes: "<what proves provenance?>"
    modifications:
      - date: "<YYYY-MM-DD>"
        by: "<name/org>"
        description: "<decimate / retopo / UVs / bake / convert / optimize>"
        outputs:
          - "<output file paths>"
        tools: ["<blender>", "<gltfpack>", "<meshoptimizer>", "<etc>"]

  - kind: "textures"
    local_paths:
      - "web/assets/3d/landmarks/<landmark_slug>/textures/<TEXTURE_FILE_OR_DIR>"
    upstream:
      title: "<Texture set name>"
      author: "<Person/Org>"
      source_url: "<https://...>"
      license:
        spdx_or_label: "<...>"
        license_url: "<...>"
        attribution_text_required: "<paste exact required wording or 'none'>"
    modifications:
      - date: "<YYYY-MM-DD>"
        by: "<name/org>"
        description: "<resize / compress / atlas / convert to KTX2>"
        outputs:
          - "<output file paths>"

  - kind: "reference"
    local_paths:
      - "web/assets/3d/landmarks/<landmark_slug>/licenses/<REFERENCE_DOC>"
    upstream:
      title: "<Photo/scan/map reference>"
      author: "<Person/Org>"
      source_url: "<https://...>"
      license:
        spdx_or_label: "<...>"
        attribution_text_required: "<...>"
```

---

## 📦 Component ledger (human-readable)

> Keep this table in sync with the YAML block above.

| Component | Local path(s) | Upstream source | Creator | License | Required attribution | Modified by KFM? |
|---|---|---|---|---|---|---|
| 🧱 Model | `<MODEL_FILE>` | `<URL>` | `<Creator>` | `<License>` | `<Required text / none>` | `<Yes/No>` |
| 🖼️ Textures | `textures/<...>` | `<URL>` | `<Creator>` | `<License>` | `<Required text / none>` | `<Yes/No>` |
| 📸 References | `licenses/<...>` | `<URL>` | `<Creator>` | `<License>` | `<Required text / none>` | `<Yes/No>` |

---

## 🔍 License resolution notes (how to interpret “combined”)

- 🧩 **Composite bundles inherit the most restrictive component terms.**
- 🧾 If *any* component requires attribution (e.g., CC-BY), the **bundle requires attribution**.
- 🚫 If *any* component is **Non-Commercial** or **No-Derivatives**, **downstream use must respect those constraints** unless you replace that component with a compatible one.
- 🧠 If you’re unsure: keep it conservative, and add a note in **“Open questions”** below.

---

## 🧷 Provenance checklist (fail-closed)

- [ ] Every component has an upstream URL or archival citation
- [ ] Every component’s license text (or authoritative link) is stored under `licenses/`
- [ ] Any required attribution wording is captured verbatim
- [ ] Modifications (if any) are documented with dates + tools
- [ ] If license is unclear, component is marked **TBD** and treated as **restricted** until resolved

---

## 🧯 Open questions / TODO (if any)

- ❓ `<What is unclear?>`
- 🧾 `<Need to confirm license for ...>`
- 🔄 `<Replace component with open alternative?>`

---

## 🔁 Maintenance workflow

When updating this landmark bundle:

1. 🧾 **Update** `components` (YAML block) and the table above  
2. 📎 **Add** any new license notices into `licenses/`  
3. ✅ **Revalidate** combined license result + attribution text  
4. 🧪 **Record** transforms/optimizations (what changed, why, how)  
5. 🧷 **Keep UI-safe copy text** current (Short + Long form)

---

## 📬 Contact (optional)

- Maintainer: `<name or team>`
- Reviewers: `<legal/data steward>`
- Issue link: `<GitHub issue or tracker>`
