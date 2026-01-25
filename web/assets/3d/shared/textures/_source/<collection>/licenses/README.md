# 🧾 Texture Licenses & Attribution (Collection: `<collection>`)  

[![Provenance First](https://img.shields.io/badge/provenance-first-1f6feb)](#-why-this-folder-exists)
[![Licenses Tracked](https://img.shields.io/badge/licenses-tracked-success)](#-minimum-requirements)
[![Fail-Closed](https://img.shields.io/badge/governance-fail--closed-critical)](#-rules-of-the-road)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-7f3fbf)](#-faircare--sensitive--restricted-assets)

> ✅ **Goal:** every texture used by KFM ships with **clear license + attribution + provenance** so the UI (and exports) can automatically credit sources and stay legally/ethically clean.

---

## 📦 Where you are (path)
```
web/assets/3d/shared/textures/_source/<collection>/licenses/README.md
```

This README is **per texture collection**. Duplicate it across collections and replace `<collection>` with the folder name (e.g., `pbr_terrain_pack_v1`).

---

## 🧠 Why this folder exists
KFM is **provenance-first**: no “mystery layers,” no “mystery assets.” Textures are *data assets* just like datasets and story media—so they must be traceable, citable, and properly licensed.

This folder exists so we can:
- 📌 satisfy attribution/license obligations **at commit time**
- 🧪 enable automated **policy/CI gates** (fail fast if missing license metadata)
- 🗺️ surface credits in the UI (Layer Info / Provenance panels / exports)
- 🧾 generate a **THIRD-PARTY NOTICES** block for builds/releases

---

## ✅ Minimum requirements
Each collection must include:

### 1) A license manifest (required)
Create **one** of the following (pick one convention and stick to it in the collection):

- `ATTRIBUTION.yml` ✅ *(recommended)*  
- `ATTRIBUTION.json`

### 2) Full license texts (required when the license demands it)
Place canonical license texts here:
```
licenses/
  LICENSE_TEXTS/
    CC-BY-4.0.txt
    CC0-1.0.txt
    MIT.txt
    ...
```

### 3) Source receipts / evidence (strongly recommended)
- `SOURCES.json` (URLs + retrieval dates + checksums)
- Optional: `RECEIPTS/` (screenshots, vendor invoices, emails, etc. — **no secrets**)

### 4) Optional but helpful
- `THIRD_PARTY_NOTICES.md` (generated summary for quick scanning)
- `MODIFICATIONS.md` (document edits: re-bakes, color grading, channel packing, etc.)

---

## 🚦 Rules of the road
### ✅ DO
- Use SPDX identifiers (e.g., `CC-BY-4.0`, `CC0-1.0`, `MIT`) in the manifest.
- Store the **exact required attribution line** (some licenses specify wording).
- Record **where** the texture came from (source URL) and **when** it was retrieved.
- Note any **modifications** (resized, compressed, re-baked normals, packed ORM, etc.).
- Prefer assets that are **redistributable** (so the repo can legally contain them).

### ❌ DON’T
- Don’t add “Google Image Search” textures (no provenance, no license clarity).
- Don’t commit assets with **non-redistributable** or **unclear** terms.
- Don’t omit attribution “because it’s just a texture.” (Textures are still copyrighted works.)
- Don’t paste license text that you don’t have rights to redistribute (store a link if required).

---

## 🗂️ Standard folder layout (suggested)
```
🧵 textures/
└── 🧪 _source/
    └── 🗂️ <collection>/
        ├── 🖼️ textures/
        │   └── ... .png | .jpg | .ktx2 | .webp
        └── 📜 licenses/
            ├── 📄 README.md               👈 📍 you are here
            ├── 🏷️ ATTRIBUTION.yml         (canonical credits + UI-safe attribution strings)
            ├── 🔗 SOURCES.json            (machine-readable upstream source registry: URLs, authors, hashes)
            ├── 📚 LICENSE_TEXTS/
            │   ├── 📄 CC-BY-4.0.txt
            │   └── 📄 ... (other license texts)
            ├── 🧾 RECEIPTS/               (optional evidence)
            │   ├── 🧾 invoice.pdf
            │   └── 🖼️ screenshot_terms.png
            ├── ✍️ MODIFICATIONS.md        (optional: what changed vs upstream, tools/steps, dates)
            └── 🧩 THIRD_PARTY_NOTICES.md  (optional / generated: compiled notices for distribution)
```

---

## 🧷 Attribution manifest schema (recommended)
Create `ATTRIBUTION.yml` like:

```yaml
collection:
  id: "<collection>"
  description: "Short description of this texture collection."
  owner: "KFM / Contributors / Vendor Name"
  intended_use: "e.g., terrain albedo/normal/roughness for Cesium/three.js materials"

assets:
  - id: "flint_hills_albedo_4k"
    files:
      - "../textures/flint_hills_albedo_4k.png"
      - "../textures/flint_hills_orm_4k.png"
      - "../textures/flint_hills_normal_4k.png"
    license:
      spdx: "CC-BY-4.0"
      license_text: "./LICENSE_TEXTS/CC-BY-4.0.txt"   # if required
      url: "https://creativecommons.org/licenses/by/4.0/"
    attribution:
      author: "Jane Doe"
      title: "Flint Hills PBR Set"
      source_url: "https://example.com/flint-hills-pack"
      required_credit_line: "Flint Hills PBR Set © Jane Doe, CC BY 4.0"
    provenance:
      retrieved_utc: "2026-01-25T00:00:00Z"
      checksum_sha256:
        flint_hills_albedo_4k.png: "<sha256>"
        flint_hills_orm_4k.png: "<sha256>"
        flint_hills_normal_4k.png: "<sha256>"
      modifications:
        - "Converted to KTX2 (BasisU) for web delivery"
        - "Packed AO/Roughness/Metallic into ORM"
      notes: "Any extra constraints, disclaimers, or usage guidance."

  - id: "procedural_noise_generated"
    files:
      - "../textures/noise_512.png"
    license:
      spdx: "CC0-1.0"
      license_text: "./LICENSE_TEXTS/CC0-1.0.txt"
      url: "https://creativecommons.org/publicdomain/zero/1.0/"
    attribution:
      author: "KFM Team"
      title: "Procedural Noise"
      source_url: "generated"
      required_credit_line: "Procedural Noise (generated by KFM) — CC0"
    provenance:
      retrieved_utc: "2026-01-25T00:00:00Z"
      checksum_sha256:
        noise_512.png: "<sha256>"
      modifications:
        - "Generated via script: tools/texture/gen_noise.ts"
```

> 🧠 **Tip:** If a texture comes from a pack, you can reference the pack as the “source” and still list per-file checksums.

---

## 🧾 SOURCES.json (evidence receipts)
Create `SOURCES.json` to store raw “where this came from” receipts:

```json
{
  "collection": "<collection>",
  "sources": [
    {
      "source_url": "https://example.com/flint-hills-pack",
      "retrieved_utc": "2026-01-25T00:00:00Z",
      "license_spdx": "CC-BY-4.0",
      "evidence": {
        "terms_screenshot": "./RECEIPTS/screenshot_terms.png",
        "invoice": "./RECEIPTS/invoice.pdf"
      }
    }
  ]
}
```

---

## 🧪 CI / Policy Gate expectations (what will fail builds)
Keep your mental model simple:

- 🚫 Missing `license.spdx` → **fail**
- 🚫 Missing `attribution.source_url` (or explicit `source_url: generated`) → **fail**
- 🚫 License not on allowed list → **fail** (unless governance approves)
- 🚫 Sensitive/restricted data without proper flags → **fail**

*(Exact rules live in policy-as-code, but this folder should make compliance easy.)*

---

## 🖼️ UI + Export integration (how credits show up)
Textures may appear:
- in 3D globe/terrain materials
- in story scenes / narrative media
- in exported snapshots (screens, reports, print)

So we design attribution to be **machine-readable**:
- UI can show “Layer Info” → license + source + provenance
- Provenance panels can aggregate all active assets
- Export can auto-append a credits footer (“Sources + processed by KFM”)

> 🔁 **Rule:** If it renders, it credits. If it credits, it must have a manifest entry.

---

## ⚖️ FAIR+CARE / sensitive / restricted assets
If any texture:
- contains restricted cultural patterns/symbols
- includes sensitive site imagery
- has usage restrictions beyond a standard license

…then add a `governance:` block per asset:

```yaml
governance:
  sensitivity: "restricted"  # public | internal | restricted
  care_labels: ["culturally_sensitive"]
  access_notes: "Requires approval by <group/role> before redistribution."
```

---

## ✅ “Add a texture” checklist (copy/paste)
- [ ] Put texture files under `../textures/` (or your collection’s convention)
- [ ] Add/Update `ATTRIBUTION.yml` entry (license, author, source URL, credit line)
- [ ] Add license text to `LICENSE_TEXTS/` **if required**
- [ ] Add/Update `SOURCES.json` with retrieval date + evidence
- [ ] Add checksums (sha256) for all shipped files
- [ ] Document modifications (optional but encouraged)
- [ ] Ensure the license allows redistribution in this repo (or store a pointer-only)

---

## 🧯 FAQ
### “Can I use a texture if I can’t find a license?”
**No.** Unknown license = not shippable.

### “What about paid assets?”
Only if the terms explicitly allow redistribution **in this repository**. Otherwise: store a **pointer-only** (no binary) and document retrieval + license terms clearly.

### “Do we need license texts for Creative Commons?”
Often yes for notices; safest approach: store canonical text in `LICENSE_TEXTS/` and include the `license.url`.

### “I generated this texture with AI—what license applies?”
That depends on the tool/provider. Record:
- generator/tool name + version
- provider terms (link)
- prompt seed/settings if relevant
…and mark `source_url: generated`.

---

## 🏁 Template footer
Maintainers: when this collection is “done,” consider generating:
- `THIRD_PARTY_NOTICES.md` from `ATTRIBUTION.yml`
- a build-time credits bundle for the UI (e.g., `licenses.bundle.json`)

❤️ Thanks for keeping KFM **auditable** and **respectful**.

