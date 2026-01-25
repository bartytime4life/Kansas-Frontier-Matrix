<!--
📍 Path: web/assets/3d/shared/materials/library/<material_slug>/licenses/README.md
🎯 Purpose: A per-material “License & Provenance Pack” so KFM can ship 3D/PBR materials with full transparency.
-->

# 🧱 <material_name> — License & Provenance Pack

![Material](https://img.shields.io/badge/material-<material_slug>-2ea44f)
![SPDX](https://img.shields.io/badge/SPDX-<SPDX_ID>-informational)
![Redistribution](https://img.shields.io/badge/redistribution-<yes|no>-blue)
![Attribution](https://img.shields.io/badge/attribution-<required|not_required>-orange)

> [!IMPORTANT]
> **No “mystery materials.”** If this folder isn’t complete, the material **must not** ship in the app, offline packs, exports, or demos. ✅

---

## 🔎 Quick Summary

| Field | Value |
|---|---|
| **Material slug** | `<material_slug>` |
| **Display name** | `<material_name>` |
| **Material type** | `PBR (metal/rough)` \| `PBR (spec/gloss)` \| `Non‑PBR` |
| **Primary license (SPDX)** | `<SPDX_ID>` (example: `CC0-1.0`, `CC-BY-4.0`) |
| **Attribution required?** | `<Yes/No>` |
| **Redistribution allowed?** | `<Yes/No/Unclear>` |
| **Commercial use allowed?** | `<Yes/No/Unclear>` |
| **Share‑Alike / Copyleft?** | `<Yes/No>` |
| **Sensitive / restricted?** | `<None/Public/Restricted>` |
| **Imported on** | `<YYYY-MM-DD>` |
| **Last license audit** | `<YYYY-MM-DD>` |
| **Maintainer** | `@<github_handle>` |

---

## 📦 What belongs in `licenses/` (required unless noted)

✅ **Minimum shipping set:**

- [ ] `README.md` — this file  
- [ ] `LICENSE.txt` (or `LICENSE.md`) — **full upstream license text**  
- [ ] `ATTRIBUTION.md` — **copy/paste credit line(s)** (even if CC0; “not required” is still documented)  
- [ ] `SOURCES.yml` — machine‑readable provenance (URLs, author, retrieved_at, hashes)  
- [ ] `CHANGES.md` — any modifications we made (resize, crop, convert, generate maps, etc.)  
- [ ] `CHECKSUMS.sha256` — integrity hashes for *every shipped asset file* (textures + material definitions)

🟦 **Strongly recommended (when feasible):**

- [ ] `PROVENANCE.jsonld` — PROV‑O lineage (source → transforms → shipped artifacts)
- [ ] `SCREENSHOTS/` — upstream page screenshot + receipt PDF for “what we downloaded”  
- [ ] `NOTICES.md` — for multi-license edge cases (bundles, dual licensing, exceptions)

---

## 🗂 Folder Map

```text
📁 web/assets/3d/shared/materials/library/<material_slug>/
├─ 📁 textures/                         # actual PBR maps (or references to CDN/registry)
│  ├─ 🖼️ basecolor.<ext>
│  ├─ 🖼️ normal.<ext>
│  ├─ 🖼️ roughness.<ext>
│  ├─ 🖼️ metallic.<ext>
│  ├─ 🖼️ ao.<ext>
│  └─ 🖼️ height.<ext>                   # optional
├─ 📁 licenses/
│  ├─ 📄 README.md                      👈 you are here
│  ├─ 📄 LICENSE.txt
│  ├─ 📄 ATTRIBUTION.md
│  ├─ 📄 SOURCES.yml
│  ├─ 📄 CHANGES.md
│  └─ 📄 CHECKSUMS.sha256
└─ 📄 material.<json|glb|gltf|ts>        # material definition (engine-specific)
```

---

## 📜 License Declaration

### 1) Primary license

- **SPDX ID:** `<SPDX_ID>`
- **License URL:** `<https://…>`
- **Local copy:** [`LICENSE.txt`](./LICENSE.txt)

### 2) Human-readable obligations (fill these in)

- ✅ **Must include attribution?** `<Yes/No>`
- ✅ **Must mark changes?** `<Yes/No>`
- ✅ **Must include license text/notices with redistribution?** `<Yes/No>`
- ✅ **Share‑Alike / Copyleft?** `<Yes/No>`
- ✅ **Non‑Commercial restriction?** `<Yes/No>`
- ✅ **No‑Derivatives restriction?** `<Yes/No>`
- ⚠️ **Notes / exceptions / link to upstream terms:**  
  `<short explanation>`

> [!NOTE]
> This README is not legal advice. When the license is ambiguous or unusual, **treat as “Unclear”** and block shipping until reviewed.

---

## 🏷 Attribution

### 1) Copy/paste attribution (for UI credits, exports, Story Nodes, offline packs)

```text
<material_name> material textures by <Author/Studio> — <Source/Website> — Licensed under <SPDX_ID> (<license_url>).
Changes: <brief list or “none”>.
```

### 2) Where attribution must appear (KFM surfaces credits everywhere)

- 🧭 **In-app**: material/library viewer + “Layer/Asset Info” panel  
- 🧾 **Exports**: screenshots, share links, embed snippets, downloaded bundles  
- 🧳 **Offline packs**: included in the pack manifest/credits screen  
- 📚 **Story Nodes** (if used in a narrative): list in the Story’s evidence/credits block  

> [!TIP]
> If multiple materials are used in one rendered view, KFM should aggregate and display all credits (and respect the most restrictive terms).

---

## 🔗 Upstream Sources & Provenance

> [!IMPORTANT]
> “Source URL” alone is not provenance. Capture **when**, **what**, and **exactly which file** you got.

### Source table (add rows as needed)

| Source ID | Upstream Title | Author/Org | URL | Retrieved (UTC) | Upstream License | Notes |
|---|---|---|---|---|---|---|
| `upstream-01` | `<title>` | `<author>` | `<https://…>` | `<YYYY-MM-DDTHH:MM:SSZ>` | `<SPDX_ID>` | `<notes>` |

### Provenance requirements (minimum)

- **Stable URL(s)** + **archive link** (if available)
- **Retrieved timestamp**
- **Original filename(s)**
- **SHA256** of upstream files (before any conversion)
- **License snapshot** (copy of license terms *as of retrieval*)

---

## 🧪 Transformations & Derived Work

Document anything that changes the asset (even “small” changes can matter):

- [ ] Converted format (e.g., PNG → KTX2 / BasisU)
- [ ] Resized (e.g., 8k → 2k)
- [ ] Cropped / seam fixed / tiled
- [ ] Color space changes (sRGB vs linear)
- [ ] Generated maps (normal/roughness/AO) from base scan
- [ ] Denoised / sharpened / AI upscaling
- [ ] Channel packing (ORM, etc.)

### Recommended format for `CHANGES.md`

```text
- 2026-01-25: Imported upstream-01 files (sha256: …)
- 2026-01-25: Resized basecolor to 2048² for web performance
- 2026-01-25: Converted textures to .ktx2 using toktx (args: …)
- 2026-01-25: Generated normal map from height (tool: …)
```

> [!WARNING]
> If the upstream license is **NoDerivatives** (ND), *any* modification may be prohibited. Do not ship.

---

## 🧾 Asset Inventory & License Coverage

> [!NOTE]
> The goal is that every shipped file is covered, attributable, and integrity-checkable.

### Inventory template

| File | Kind | Source ID | License | Covered by Attribution? | SHA256 |
|---|---|---|---|---|---|
| `../textures/basecolor.<ext>` | basecolor | `upstream-01` | `<SPDX_ID>` | ✅ | `<sha256>` |
| `../textures/normal.<ext>` | normal | `generated` | `<SPDX_ID or derived>` | ✅ | `<sha256>` |
| `../material.<ext>` | material def | `internal` | `<Project license or note>` | ✅ | `<sha256>` |

---

## 🔐 Compliance Checklist (pre-merge)

- [ ] **License is identified** (SPDX + URL + local text)
- [ ] **Redistribution is allowed** for this repo + web delivery
- [ ] **Attribution requirements satisfied** (and ready to display in UI)
- [ ] **Changes documented** (CHANGES.md)
- [ ] **All files hashed** (CHECKSUMS.sha256)
- [ ] **Sensitive/restricted review** completed (if applicable)
- [ ] **No brand/trademark/logos** embedded (unless explicitly permitted)
- [ ] **Policy gates pass** (no missing license/provenance)

---

## 🧠 Sensitivity & Ethics (KFM-specific)

Even “just textures” can be sensitive if they come from protected cultural sites, restricted archives, or community-controlled sources.

- Sensitivity level: `<None/Public/Restricted>`
- Community/authority constraints (if any): `<text>`
- Redaction/generalization needed: `<text or “n/a”>`

---

## ♻ Versioning & Audit Trail

- **Material version:** `<semver>`
- **License audit log:**
  - `<YYYY-MM-DD>` — `<who>` — `<what changed / reviewed>`

> [!TIP]
> Keep license/provenance changes in the same PR as the asset change so reviewers can validate the whole chain.

---

## ❓ FAQ (quick answers)

**Q: What if there are multiple upstream sources?**  
A: Add each as a `Source ID`, list all files they contributed to, and ensure attribution covers all sources.

**Q: What if the license is unclear?**  
A: Mark `Redistribution allowed: Unclear` and **do not ship** until resolved.

**Q: Can we bundle this into the main project license?**  
A: No. Keep third‑party assets **separately licensed** and **explicitly documented** here.

---

✅ **Done right, this README makes the “material behind the material” as traceable as the “map behind the map.”**

