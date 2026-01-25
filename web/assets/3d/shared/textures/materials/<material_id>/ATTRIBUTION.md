---
doc_type: attribution
doc_version: "KFM-MDP_v11.2.6"
path: "web/assets/3d/shared/textures/materials/<material_id>/ATTRIBUTION.md"
material_id: "<material_id>"
material_name: "<human_readable_material_name>"
created_utc: "<YYYY-MM-DDTHH:MM:SSZ>"
last_updated_utc: "<YYYY-MM-DDTHH:MM:SSZ>"
status: "draft" # draft|review|approved
classification: "public" # public|internal|restricted
provenance:
  evidence_first: true
  no_mystery_assets: true
  source_of_truth: "this_file"
owners:
  maintainer: "<github_handle_or_team>"
  reviewer: "<github_handle_or_team>"
---

# 🧱 Material Attribution — `<material_id>`

<p align="center">
  <img alt="KFM" src="https://img.shields.io/badge/KFM-provenance--first-2b6cb0" />
  <img alt="Asset" src="https://img.shields.io/badge/asset-3D%20material%20textures-6b46c1" />
  <img alt="Compliance" src="https://img.shields.io/badge/compliance-FAIR%2BCARE%20aware-0ea5e9" />
  <img alt="Status" src="https://img.shields.io/badge/status-draft-f59e0b" />
</p>

> 🧭 **Rule:** Anything visible in the UI must be attributable and auditable.  
> No attribution → no promotion → no shipping. ✅

---

## ✨ What this covers

This file documents **where this material’s textures came from**, **their license terms**, and **how KFM is allowed to use/redistribute them**.

📍 **Asset location (this folder):**
- `web/assets/3d/shared/textures/materials/<material_id>/`

---

## 📦 Recommended folder contents (suggested, not required)

```text
📁 web/assets/3d/shared/textures/materials/<material_id>/
  ├─ 🧾 ATTRIBUTION.md                # this file ✅
  ├─ 📄 LICENSE.txt                   # if required by upstream
  ├─ 📄 NOTICE.txt                    # if required by upstream
  ├─ 🧷 source/                       # upstream receipts (optional but strongly recommended)
  │   ├─ source.json                  # machine-readable source record
  │   └─ checksums.sha256             # integrity checks
  ├─ 🖼️ preview/                      # thumbnails / swatches
  └─ 🧵 textures/                     # actual maps (albedo/normal/roughness/etc.)
```

---

## 🏷️ Required credit line (UI-safe)

Use this when rendering the material in UI tooltips / provenance panels:

**Credit (short):** `<Credit line (Author/Provider) — License>`  
**Source (URL):** `<canonical_source_url>`  
**License (SPDX):** `<SPDX expression, e.g., CC-BY-4.0 or CC0-1.0>`

> ✅ If multiple upstream sources exist, concatenate credits by priority (primary → secondary) and keep it short.

---

## 🧾 Source Record (must be filled)

### 1) Primary upstream source

| Field | Value |
|---|---|
| Upstream Provider / Site | `<provider_name>` |
| Upstream Asset Name / Pack | `<asset_name_or_pack>` |
| Upstream URL (canonical) | `<https://...>` |
| Author / Creator | `<name_or_org>` |
| License Name | `<license_name>` |
| License SPDX | `<SPDX>` |
| License URL | `<https://...>` |
| Attribution required? | `yes/no` |
| Redistribution allowed? | `yes/no/unknown` |
| Commercial use allowed? | `yes/no/unknown` |
| Modification allowed? | `yes/no/unknown` |
| Required notices | `<LICENSE.txt, NOTICE.txt, attribution text, etc.>` |
| Retrieved (UTC) | `<YYYY-MM-DDTHH:MM:SSZ>` |
| Retrieved by | `<github_handle_or_pipeline>` |

### 2) Secondary sources (if any)

> Add rows as needed. If **any** source conflicts with another, list the conflict and choose the **most restrictive** handling until resolved.

| Provider | URL | License (SPDX) | Notes |
|---|---|---|---|
| `<provider>` | `<https://...>` | `<SPDX>` | `<what this contributed>` |

---

## 🧵 Texture inventory + provenance (required for all maps)

> Fill one row **per file**. Keep filenames stable once published.

| File | Map Type | Origin | License (SPDX) | Modified? | Mod Summary | SHA-256 |
|---|---|---|---|---:|---|---|
| `textures/<file>` | `albedo` | `<provider>` | `<SPDX>` | `yes/no` | `<e.g., resized to 2K, converted to PNG>` | `<sha256>` |
| `textures/<file>` | `normal` | `<provider>` | `<SPDX>` | `yes/no` | `<...>` | `<sha256>` |
| `textures/<file>` | `roughness` | `<provider>` | `<SPDX>` | `yes/no` | `<...>` | `<sha256>` |
| `textures/<file>` | `metallic` | `<provider>` | `<SPDX>` | `yes/no` | `<...>` | `<sha256>` |
| `textures/<file>` | `ao` | `<provider>` | `<SPDX>` | `yes/no` | `<...>` | `<sha256>` |
| `textures/<file>` | `height/displacement` | `<provider>` | `<SPDX>` | `yes/no` | `<...>` | `<sha256>` |

### 🔁 Transformation notes (if modified)

Document all edits (even “minor”):
- 🧰 Tools used: `<tool + version>`
- 🧪 Steps: `<resize/denoise/convert/colorspace/channel-pack/etc.>`
- 🎯 Intent: `<performance, consistency, visual fidelity, etc.>`
- 📉 Lossy ops? `<yes/no>` (if yes, specify)

---

## ⚖️ License & compliance decision

### Allowed usage inside KFM
- ✅ In-repo distribution: `yes/no/conditional`
- ✅ Bundled in build artifacts (web): `yes/no/conditional`
- ✅ CDN hosting: `yes/no/conditional`
- ✅ Derivative works: `yes/no/conditional`
- ✅ Attribution display required in UI: `yes/no`  
  - If **yes**, specify where: `layer provenance panel / 3D viewer HUD / about page / credits modal`

### Required notices to ship
- [ ] `LICENSE.txt` present (if required)
- [ ] `NOTICE.txt` present (if required)
- [ ] Attribution string added to UI provenance surfaces (if required)
- [ ] All texture file hashes captured (SHA-256)
- [ ] Any restrictions documented (e.g., “no redistribution”, “editorial use only”)

---

## 🧭 UI integration notes (provenance-first)

When this material is used in:
- 🗺️ Map overlays / 3D scenes
- 🧊 GLB / 3D Tiles materials
- 🎞️ Story Nodes (images/video)
- 🤖 Focus Mode summaries that reference visuals

…it must remain traceable. Include:
- material_id: `<material_id>`
- attribution: **Credit (short)** + **Source URL** + **License**
- optional: a link to this file in any “Credits / Sources” UI panel

---

## 🔒 Sensitivity / restrictions (if any)

If any upstream terms limit distribution or contain restrictions:
- Restriction summary: `<text>`
- Enforcement plan: `<e.g., keep out of public builds, require auth, replace with CC0 alternative, etc.>`
- Review required by: `<team/council>` (if applicable)

---

## ✅ Review checklist (merge gate)

- [ ] Source URL is canonical and reachable
- [ ] License is explicitly stated and compatible with intended distribution
- [ ] Attribution requirements are satisfied (text + placement)
- [ ] Texture inventory is complete (no missing maps)
- [ ] Checksums recorded for every file
- [ ] Any modifications documented
- [ ] No “unknown” values remain in the compliance decision block

---

## 🗂️ Change log

| Date (UTC) | Change | Author |
|---|---|---|
| `<YYYY-MM-DD>` | `<created attribution record>` | `<handle>` |
| `<YYYY-MM-DD>` | `<updated licenses / added hashes / etc.>` | `<handle>` |

---

## 🧩 Attribution snippets (copy/paste)

### Markdown (docs / release notes)
> **Material `<material_id>`**: `<Author/Provider>` — `<License>` (Source: `<URL>`)

### UI tooltip (compact)
`<Author/Provider> • <License> • <URL>`

### UI credits modal (expanded)
`Material: <material_name> (<material_id>) — Textures by <Author/Provider>. Licensed under <License>. Source: <URL>. Modifications: <summary>.`

---

