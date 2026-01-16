---
title: "🧾 Landmark 3D Licenses & Attributions"
description: "Per-landmark license texts, attribution statements, and machine-readable manifests for 3D assets."
project: "Kansas Frontier Matrix (KFM)"
doc_type: "README"
kfm_mdp_version: "v11.2.6"
version: "v1.0.0"
status: "active"
last_updated: "2026-01-15"
canonical_path: "web/assets/3d/landmarks/<landmark_slug>/licenses/README.md"
semantic_document_id: "kfm:web.assets.3d.landmarks.licenses.readme"
doc_uuid: "2c5fd67e-0e8a-4ff2-8f06-0a266b1acb07"
license: "SEE-ROOT-LICENSE"
fair_category: "FAIR+CARE"
care_label: "C0: Public"
tags:
  - 3d
  - landmarks
  - licensing
  - attribution
  - provenance
---

<p align="center">
  <img alt="KFM-MDP" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-blue?style=for-the-badge" />
  <img alt="Provenance First" src="https://img.shields.io/badge/Provenance-First-important?style=for-the-badge" />
  <img alt="SPDX" src="https://img.shields.io/badge/SPDX-Labels-success?style=for-the-badge" />
  <img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-6f42c1?style=for-the-badge" />
</p>

# 🧾 Licenses & Attributions (Landmark 3D)

This folder is the **canonical, per-landmark home** for all **license texts, attribution statements, and source/provenance receipts** needed to legally ship *any* 3D assets under:

`web/assets/3d/landmarks/<landmark_slug>/`

> [!IMPORTANT]
> **Repo code** is licensed at the root (KFM uses **MIT** for software), but **3D assets are not automatically covered** by that license.  
> Treat every texture/model as a **data artifact** with its own terms.

---

## 🧭 What this folder is for

✅ Put these here:

- **Third-party license texts** (kept **verbatim**, as provided)
- **Attribution** content (human-readable + UI-ready snippets)
- **Source receipts** (URLs, archive links, retrieval dates, checksums)
- **Machine-readable license manifest** (for CI + UI “Credits / Licenses” panels)

🚫 Do **not** put these here:

- Textures / images (`../textures/`)
- Models / meshes (`../models/`)
- Any secrets, keys, paid download tokens, private emails, or restricted site docs
- “Assumed licensing” without evidence

---

## 🧱 Recommended layout

You can keep this minimal, but the following structure scales cleanly as assets grow:

```text
web/assets/3d/landmarks/<landmark_slug>/
├─ licenses/ 🧾
│  ├─ README.md
│  ├─ ATTRIBUTION.md                # human + UI friendly credits
│  ├─ THIRD_PARTY_NOTICES.md        # roll-up notices (optional)
│  ├─ manifest/
│  │  ├─ license-manifest.json      # machine-readable map: asset_id → license
│  │  └─ license-manifest.schema.json (optional)
│  ├─ sources/
│  │  ├─ <asset_id>.yml             # provenance + terms for each asset
│  │  └─ <asset_id>.notes.md        # optional narrative/legal notes
│  ├─ texts/
│  │  ├─ SPDX-CC-BY-4.0.txt
│  │  ├─ SPDX-CC-BY-SA-4.0.txt
│  │  ├─ SPDX-CC0-1.0.txt
│  │  └─ LICENSE-<vendor>-<date>.txt
│  └─ receipts/
│     ├─ <asset_id>.sha256
│     └─ <asset_id>.source-url.txt
├─ textures/ 🎨
└─ models/ 🧱
```

> [!NOTE]
> If this landmark uses **only one license** for the entire 3D bundle, you may collapse the structure to:
> `licenses/ATTRIBUTION.md`, `licenses/LICENSE.txt`, and `licenses/manifest/license-manifest.json`.

---

## 🏷️ Naming conventions

### Landmark slug
`<landmark_slug>` should be:
- lowercase
- kebab-case (`fort-leavenworth`, `monument-rocks`)
- ASCII only

### Asset IDs
Use a **stable** `asset_id` that can be referenced from manifests in `textures/` and `models/`.

Recommended pattern:
- `tx_<landmark>_<subject>_<variant>_<res>`
- `mdl_<landmark>_<subject>_<lod>`

Examples:
- `tx_monument-rocks_sandstone_albedo_4k`
- `mdl_fort-leavenworth_main-building_lod1`

### SPDX identifiers
Always record license identifiers using SPDX-style strings when possible:
- `CC-BY-4.0`, `CC-BY-SA-4.0`, `CC0-1.0`, `MIT`, `Apache-2.0`, etc.

If unknown, use:
- `LicenseRef-UNKNOWN` *(and open an issue before shipping)*

---

## 🧾 Minimal “add an asset” workflow

1. **Capture the source**
   - URL(s), author/organization, retrieval date/time, and any download page terms.
2. **Store the license text**
   - Put the exact license in `licenses/texts/…` (don’t rewrite it).
3. **Create a provenance record**
   - Add `licenses/sources/<asset_id>.yml`.
4. **Update attribution**
   - Add the credit line(s) to `licenses/ATTRIBUTION.md`.
5. **Update the manifest**
   - Add/update `licenses/manifest/license-manifest.json`.
6. **Verify**
   - Add checksum receipt(s) in `licenses/receipts/` and run validation.

---

## 📄 Suggested `sources/<asset_id>.yml` schema

```yaml
asset_id: "tx_monument-rocks_sandstone_albedo_4k"
asset_path:
  - "../textures/tx_monument-rocks_sandstone_albedo_4k.png"
source:
  name: "Example Texture Library"
  url: "https://example.com/textures/123"
  retrieved_at: "2026-01-15"
  archive_url: "https://web.archive.org/..."
creator:
  name: "Jane Doe"
  organization: "Example Co."
license:
  spdx: "CC-BY-4.0"
  license_url: "https://creativecommons.org/licenses/by/4.0/"
  attribution_required: true
  sharealike: false
modifications:
  - "cropped"
  - "color corrected"
  - "converted to PNG"
attribution_text: "© Jane Doe / Example Co. (CC-BY-4.0)"
notes: "Any extra constraints or clarifications."
```

---

## 🪪 Machine-readable manifest (for CI + UI)

`licenses/manifest/license-manifest.json` is intended to be **boring, strict, and greppable**.

Minimal shape:

```json
{
  "schema_version": "v1",
  "landmark_slug": "<landmark_slug>",
  "assets": [
    {
      "asset_id": "tx_monument-rocks_sandstone_albedo_4k",
      "path": "web/assets/3d/landmarks/<landmark_slug>/textures/tx_monument-rocks_sandstone_albedo_4k.png",
      "license_spdx": "CC-BY-4.0",
      "attribution_ref": "ATTRIBUTION.md#tx_monument-rocks_sandstone_albedo_4k"
    }
  ]
}
```

> [!TIP]
> Keep `asset_id` consistent across:
> - `textures/` or `models/` manifests  
> - `licenses/sources/<asset_id>.yml`  
> - `licenses/manifest/license-manifest.json`

---

## ✅ Validation rules (recommended)

Your CI/policy gates **should fail closed** if:

- An asset exists in `textures/` or `models/` but **has no license record**
- `license_spdx` is missing/unknown **without justification**
- `attribution_required=true` but `attribution_text` is missing
- License text is referenced but **not present** in `licenses/texts/`
- Provenance is missing `source.url` and `retrieved_at`

---

## 🧨 Common edge cases

<details>
  <summary><strong>🟣 Public Domain / US Government works</strong></summary>

- Record as `Public-Domain` (or `CC0-1.0` when you *explicitly* dedicate your *own* work).
- Still capture provenance: who issued it, where you got it, and any caveats.
</details>

<details>
  <summary><strong>🟠 Composite textures (multiple inputs)</strong></summary>

- Use a “parent” `asset_id` with `sources: [ ... ]` and list all upstream assets + licenses.
- If licenses conflict, **do not ship** until resolved.
</details>

<details>
  <summary><strong>🔴 Restricted cultural/heritage agreements</strong></summary>

- Some sites allow scanning but restrict redistribution.
- Mark `care_label`/sensitivity accordingly and store **only what you’re allowed** to publish.
</details>

---

## 🔗 Related docs

- 🎨 Textures: `../textures/README.md`
- 🧱 Models: `../models/README.md` *(if present)*
- 🧠 Landmark bundle overview: `../README.md` *(if present)*
- 🏛 Repo-wide license: `/<repo_root>/LICENSE` and `/<repo_root>/NOTICE` *(authoritative)*

---

## ⚖️ Disclaimer

This documentation is a **process guide**, not legal advice. When in doubt:
- prefer **public domain / permissive** sources,
- preserve evidence,
- and escalate uncertain licenses before publishing.
