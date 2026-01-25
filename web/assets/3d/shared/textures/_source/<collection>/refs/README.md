# 🧱 Texture Reference Pack — `<collection>` (refs)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-black)
![Provenance](https://img.shields.io/badge/Principle-Provenance--first-2ea44f)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-1f6feb)
![Runtime](https://img.shields.io/badge/Runtime-NOT%20shipped-lightgrey)

This folder contains **reference material** (📷 photos, 🗺️ scans, 🧾 citations/links, 🧪 lab notes) used to author **textures/materials** for KFM’s 3D web experience.

> [!IMPORTANT]
> **Refs are not runtime assets.**  
> They exist so that every texture/material can be **audited** for origin, license, and sensitivity.  
> In KFM terms: **no “mystery layers”** — even art assets must be traceable.

---

## 🧭 Quick navigation

- [🎯 What goes in `refs/`](#-what-goes-in-refs)
- [📁 Folder contract](#-folder-contract)
- [✅ Golden rules](#-golden-rules)
- [🧾 `refs.manifest.yml` (required)](#-refsmanifestyml-required)
- [🏷️ Naming conventions](#-naming-conventions)
- [⚖️ License + attribution requirements](#️-license--attribution-requirements)
- [🔒 Sensitivity + CARE checks](#-sensitivity--care-checks)
- [🤖 AI-assisted references](#-ai-assisted-references)
- [🧪 PR checklist](#-pr-checklist)
- [🔗 Related KFM docs](#-related-kfm-docs)

---

## 🎯 What goes in `refs/`

### ✅ Good examples
- 📷 **Source photos** of materials (stone, brick, wood, paper, cloth, metal, prairie ground cover, etc.)
- 🗺️ **Historic scan excerpts** or public-domain imagery used as a visual basis
- 🧾 **Citations** for external sources (URLs, book/page refs, archive IDs) — even if you **can’t** commit the bytes
- 🧪 **Notes** about how a texture was derived (e.g., “base color sampled from ref__..., normal sculpted from …”)
- 🧩 **Material studies** (vendor sheets, measurement notes, photogrammetry capture notes)

### ❌ Not allowed here
- 🚫 **Unlicensed / unknown-origin images** (if we can’t prove origin + rights, we don’t commit it)
- 🚫 **Runtime-ready texture outputs** (those belong outside `refs/`)
- 🚫 **Sensitive data leaks** (GPS EXIF, restricted imagery, private property details, sacred-site specifics, etc.)
- 🚫 **Gigantic binaries** committed “just because” (use artifact storage / LFS / registry + link, see below)

> [!TIP]
> If you **must** reference a restricted/copyrighted source:  
> ✅ store only a **pointer** (citation + access instructions) in `refs.manifest.yml`  
> ❌ do **not** commit the bytes.

---

## 📁 Folder contract

This folder is a **mini “data contract”** for visual sources.

### Required files 🧾
- 📄 `README.md` — you are here
- 🧾 `refs.manifest.yml` — **required** source/rights/sensitivity registry for every ref

### Recommended files 🧪
- 🔐 `checksums.sha256` — integrity hashes for any committed binaries
- 🖼️ `thumbs/` — optional small previews (only if license allows)
- 📝 `notes/` — capture logs, measurements, photogrammetry notes, etc.
- 🤖 `ai/` — prompts + settings if AI-assisted refs are involved (see [AI section](#-ai-assisted-references))

### Suggested layout 🗂️
```text
web/assets/3d/shared/textures/_source/<collection>/
└─ 📷 refs/
   ├─ 📄 README.md                      # 📘 What refs are stored here, licensing rules, and how to cite refs in asset.meta.yaml
   ├─ 🧾 refs.manifest.yml               # Inventory of reference files (ids, origin URLs, capture dates, license, usage notes)
   ├─ 🔐📄 checksums.sha256              # (recommended) Integrity hashes for refs + manifest (tamper detection)
   ├─ 🖼️ thumbs/                        # (optional) Tiny thumbnails for browsing refs quickly
   │  └─ 🖼️ ref__...__thumb.jpg          # Thumbnail for a reference (keep small; derived from the ref)
   ├─ 📝 notes/                         # (optional) Human notes about capture/conditions/material interpretation
   │  ├─ 📝📄 capture-log.md             # Capture log: camera/lighting/location (as allowed), constraints, anomalies
   │  └─ 🧱📝 material-notes.md          # Material notes: what to preserve, texture goals, pitfalls, intended usage
   └─ 🤖 ai/                            # (optional) AI assist artifacts (store hashes/notes; avoid raw prompts by default)
      ├─ 🧠📝 prompts.md                 # Prompts/instructions used (sanitize; prefer storing hashes in stricter setups)
      └─ 🏃 runs/
         └─ 🧾 2026-01-25__model__seed__notes.json  # Run notes: model id, seed, params, outputs refs (no sensitive content)
```

---

## ✅ Golden rules

1. **No mystery assets 🔍**  
   Every ref must have **traceable origin** (who/where/when/how) and **rights** (license + attribution).

2. **Provenance-first 🧬**  
   If a texture/material uses a ref, the ref must be registered in `refs.manifest.yml`.  
   (KFM’s philosophy: anything that reaches UI must be explainable, attributable, and reproducible.)

3. **Fail closed 🧱**  
   If license/sensitivity is unclear → treat it as **restricted** and keep it out of the repo until resolved.

4. **Immutable evidence mindset 🧾**  
   Don’t silently “edit a ref.” If you must modify, create a **new file** and record the relationship in the manifest.

5. **Keep it lean 🚚**  
   Refs should be *useful* and *auditable*, not a dumping ground. Large sources should be stored in an artifact system with pointers.

---

## 🧾 `refs.manifest.yml` (required)

This file is the **source-of-truth registry** for reference material.

> [!IMPORTANT]
> If you add a ref file and it’s not in `refs.manifest.yml`, it does not exist (as far as governance is concerned).

### Minimal schema (recommended)
```yaml
# refs.manifest.yml
collection:
  id: "<collection>"
  description: "Reference materials used to author textures/materials for <collection>."
  owner: "<team-or-handle>"
  last_reviewed: "YYYY-MM-DD"

defaults:
  sensitivity: "public"         # public | internal | restricted
  allowed_in_repo: true         # false => pointer-only (no bytes committed)
  credit_required: true

items:
  - id: "REF-0001"
    file: "ref__limestone__fieldphoto__2026-01-20__v01.jpg"   # omit if pointer-only
    kind: "photo"                                             # photo | scan | excerpt | vendor | link | ai
    title: "Kansas limestone reference photo"
    source:
      type: "original"                                        # original | archive | website | book | dataset | vendor
      citation: "Captured by <name> at <place>, <date>."
      url: ""                                                 # optional (keep empty if not applicable)
    rights:
      license: "CC-BY-4.0"                                     # SPDX-style or clear text
      attribution: "Photo © <name> (CC-BY 4.0)"
      proof: "Signed contributor agreement / contributor is author"
    sensitivity:
      level: "public"
      notes: "No GPS EXIF; no people; no restricted locations."
    integrity:
      sha256: "<sha256-hash-here>"
    usage_notes:
      - "Base color sampling for limestone material"
      - "Roughness derived from photo frequency content; normal sculpted manually"
    derived_outputs:
      - "../<downstream-path>/limestone_basecolor.ktx2"
      - "../<downstream-path>/limestone_normal.ktx2"

  - id: "REF-0002"
    kind: "link"
    title: "Archive scan used as stylistic inspiration (pointer-only)"
    source:
      type: "archive"
      citation: "<Archive name>, Collection <id>, Item <id>, page <n>."
      url: "<link-if-allowed>"
    rights:
      license: "All Rights Reserved"
      attribution: "<Archive required attribution text>"
      proof: "Redistribution not allowed; reference pointer only"
    sensitivity:
      level: "internal"
      notes: "Do not commit bytes. Keep access instructions here."
    allowed_in_repo: false
```

### Manifest rules 📌
- `id` must be **stable** (don’t renumber just because order changed).
- `rights.license` must be explicit — no “unknown”.
- If a ref is **pointer-only**, set `allowed_in_repo: false` and omit `file`.
- If a ref file is committed, include `integrity.sha256`.

---

## 🏷️ Naming conventions

Use filenames that are:
- ✅ human readable
- ✅ stable
- ✅ diff-friendly (avoid random strings as primary names)
- ✅ meaningful without opening the file

### Recommended pattern
`ref__<subject>__<source>__<yyyy-mm-dd|yyyy>__v<##>.<ext>`

Examples:
- `ref__prairie_soil__fieldphoto__2026-01-20__v01.jpg`
- `ref__brick_red__museum_scan__1890__v02.tif`
- `ref__weathered_wood__vendor_sheet__2024__v01.pdf`

### File types 📎
- Photos/scans: `.jpg` (high quality), `.png`, `.tif` (if necessary)
- Docs: `.pdf`, `.md`
- Avoid: proprietary formats unless there’s no alternative

> [!TIP]
> Keep ref images **high-quality**, but not absurdly huge.  
> If an image is enormous, consider committing only a licensed thumbnail + pointer to original storage.

---

## ⚖️ License + attribution requirements

KFM treats **license and provenance as first-class data** — same standard applies to art assets.

### Required for every reference ✅
- **License** (or explicit redistribution restriction)
- **Attribution string** (exact text needed for UI/credits/NOTICE)
- **Proof/notes** explaining why we can legally use/store it
- **Date accessed** for web/archive sources (recommended)

### Recommended license posture 🧠
- Prefer: **Public Domain / CC0 / CC-BY**
- Be cautious with: **NC / ND** (they often conflict with open distribution and remixing)
- Avoid committing: **unknown / scraped / ambiguous** assets

> [!WARNING]
> “Found on Google” is **not** a license.

---

## 🔒 Sensitivity + CARE checks

Even “just textures” can leak sensitive info (locations, people, sacred artifacts, private property).

### Before committing any photo/scan 📷
- [ ] **Check EXIF** (GPS coordinates, device IDs, timestamps, faces)
- [ ] Remove/avoid sensitive metadata **before** the file becomes part of the repo history
- [ ] Classify sensitivity in `refs.manifest.yml`
- [ ] If culturally sensitive: ensure proper **Authority to Control** and **Ethics** handling (CARE)

> [!IMPORTANT]
> If a ref relates to culturally sensitive material, restricted research, or sacred sites:  
> treat as **restricted by default** and follow governance review.

---

## 🤖 AI-assisted references

KFM allows AI assistance **only with transparency**.

If an AI system contributed to a ref (generation, enhancement, upscaling, inpainting, etc.):

✅ Do:
- Add an entry in `refs.manifest.yml` with `kind: "ai"`
- Store prompts/settings in `refs/ai/` (model, version, seed, tools, date, operator)
- Clearly mark usage notes: what is factual vs what is synthetic/interpretive

❌ Don’t:
- Hide AI origin
- Commit AI-generated imagery with unclear rights
- Use AI output as “evidence” without explicit labeling

Suggested `ai/` logging format:
```text
refs/ai/
  prompts.md
  runs/
    2026-01-25__model-gpt__tool-imagegen__seed-12345__notes.json
```

---

## 🧪 PR checklist

Before opening a PR that adds/changes refs:

- [ ] Added/updated **`refs.manifest.yml`**
- [ ] Included explicit **license + attribution**
- [ ] Included **sensitivity classification** + notes
- [ ] Added/updated **`checksums.sha256`** (for committed binaries)
- [ ] Verified no sensitive EXIF/GPS/PII is committed
- [ ] Kept file sizes reasonable (or used pointer-only + artifact storage)
- [ ] If AI-assisted: included **prompts + run metadata** and labeled the manifest entry
- [ ] PR description explains **why** the refs were added and what downstream texture(s) they support

---

## 🔗 Related KFM docs

These project docs define the system-wide rules this folder follows:

- 📘 `/docs/MASTER_GUIDE_v13.md` — overall contributor rules & contract-first mindset
- 🧾 `/api/scripts/policy/README.md` — policy gates (licenses, provenance completeness, sensitivity)
- ⚖️ `/docs/guides/governance/faircare-oversight.md` — FAIR + CARE oversight
- 🧠 `/docs/guides/pipelines/kfm-ai-pipeline-cookiecutter.md` — AI actions logged + PR-based governance
- 🗺️ `/docs/architecture/` — web mapping stack & constraints (2D/3D UI considerations)

---

## 📌 Notes for maintainers

- Keep `refs.manifest.yml` **reviewed** and **tight**.
- If something sensitive accidentally lands in Git history, treat it as a security/privacy incident: remove, rotate, document, and harden checks.
- Consider adding CI linting for:
  - manifest presence
  - missing licenses
  - missing sensitivity labels
  - missing checksums for binaries
  - oversized files in `refs/`

