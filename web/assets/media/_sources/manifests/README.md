# 🧾 Media Source Manifests (Web UI)  
> **Location:** `web/assets/media/_sources/manifests/`  
> **Purpose:** Provenance-first “data contracts” for every media asset the UI can ship, display, cite, or reference.

<p align="center">
  <img alt="Provenance First" src="https://img.shields.io/badge/Provenance-first-1f6feb" />
  <img alt="Contract First" src="https://img.shields.io/badge/Contracts-required-8250df" />
  <img alt="Evidence First" src="https://img.shields.io/badge/Evidence-first-0e8a16" />
  <img alt="Schema" src="https://img.shields.io/badge/Format-YAML%20%7C%20JSON-orange" />
</p>

---

## 🎯 What lives here?

This folder contains **manifest files** that describe **external media sources** used by the KFM web experience:

- 🗺️ archival map scans (images / PDFs)
- 🧑‍🏫 educational figures/graphics
- 🎥 short clips / audio
- 📄 reference PDFs (when licensed/allowed)

**Manifests are the source-of-truth metadata layer**: *before* a file becomes a “real” UI asset, it should be declared here with **origin, license, integrity hashes, and processing history**.

---

## ✅ Why manifests?

Manifests help KFM stay **auditable, mappable, and trustworthy**:

- 🔎 **Traceability** → every asset can point back to its origin
- 🧾 **Attribution** → UI can auto-render credit lines & citations
- ♻️ **Reproducible builds** → deterministic inputs + checksums
- 🚫 **No mystery assets** → nothing “just appears” in production
- 🧩 **Clean architecture-friendly** → UI reads contracts, not chaos

---

## 🗂️ Suggested folder layout

> Your repo may evolve—this is the *recommended* organization for this subtree.

```text
web/assets/media/_sources/
├─ 🧾 manifests/                         # 🧾 Source-of-truth inventories for media “sources” (what exists + where it came from)
│  ├─ 📄 README.md                       # 📘 How manifests are structured, required fields, and generation workflow
│  ├─ 📚 collections/                    # 📚 Curated collection manifests (group assets by theme/project/intake)
│  │  ├─ 🗺️ kansas-historical-maps.yml    # Collection: historical map sources (scans, providers, licensing notes)
│  │  ├─ 🎙️ oral-history-audio.yml        # Collection: oral-history recordings (consent, transcript expectations)
│  │  └─ ➕ …                             # Additional collection manifests
│  ├─ 🧪 schema/                         # 🧪 Validation contracts for the manifest format
│  │  └─ 📐🧾 media-source-manifest.schema.json # JSON Schema used by CI/validators (optional but recommended)
│  └─ ⚙️ _generated/                     # ⚙️ Machine-generated rollups (do not hand-edit)
│     ├─ 🧾🗂️ index.json                  # Fast lookup index (assetId → pointers/labels/tags) built from collections
│     └─ 🔐🧾 checksums.json              # Integrity map (file → sha256/size) for reproducibility + change detection
├─ 📥 raw/                               # 📥 As-received originals (masters/scans/recordings); keep immutable + well-labeled
└─ 🧱 derived/                           # 🧱 Derived intermediates (normalized/transcoded) used to produce served assets
```

### 🧠 Rule of thumb
- `raw/` holds **original** (or fetched) bits (when allowed)
- `derived/` holds **web-ready** outputs (resized images, webm/mp4 variants, optimized PDFs, etc.)
- `manifests/` holds the **contracts** tying everything together

---

## 🧩 Manifest format

You can author manifests in either:

- **YAML** ✅ (recommended for humans)
- **JSON** ✅ (recommended if directly fetched by the browser)

If you use YAML, consider a build step that generates JSON into `manifests/_generated/`.

---

## 🧱 Minimal schema (opinionated but practical)

Each manifest describes a **collection** and its **assets**.

### Top-level fields

| Field | Type | Required | Notes |
|------|------|----------|------|
| `manifest_version` | number | ✅ | Bump on breaking schema changes |
| `kind` | string | ✅ | e.g. `kfm.media.manifest` |
| `collection.id` | string | ✅ | Stable identifier (never reused) |
| `collection.title` | string | ✅ | Human title shown in UI |
| `collection.description` | string | ✅ | Why this collection exists |
| `collection.license` | object | ✅ | Collection-wide default (assets can override) |
| `assets[]` | array | ✅ | Individual media entries |
| `maintainers[]` | array | ✅ | Who to contact / review ownership |
| `created_at` | string (ISO) | ✅ | `YYYY-MM-DD` |
| `updated_at` | string (ISO) | ✅ | `YYYY-MM-DD` |

### Asset fields

| Field | Type | Required | Notes |
|------|------|----------|------|
| `id` | string | ✅ | Stable asset ID (don’t rename lightly) |
| `type` | string | ✅ | `image` / `video` / `audio` / `pdf` / `dataset` |
| `title` | string | ✅ | Display name |
| `description` | string | ✅ | What it is + why it matters |
| `origin` | object | ✅ | URLs, publisher/author, access date |
| `license` | object | ✅ | SPDX or explicit license name + URL |
| `files[]` | array | ✅ | Raw and derived file pointers + checksums |
| `processing[]` | array | ✅ | Steps applied to make derivatives |
| `attribution` | string | ✅ | UI-ready credit line |
| `tags[]` | array | 🟡 | Search & grouping |
| `spatial` | object | 🟡 | bbox/centroid/CRS if relevant |
| `temporal` | object | 🟡 | date range, event date, publication date |
| `sensitivity` | object | 🟡 | classification & handling rules |

🟡 = strongly recommended when applicable.

---

## 📄 Copy/paste template (YAML)

```yaml
manifest_version: 1
kind: kfm.media.manifest

collection:
  id: kfm.media.kansas-historical-maps.v1
  title: "Kansas Historical Maps (Selected)"
  description: >
    Curated historical map media used in the web UI for story nodes,
    side-panels, and citations.
  license:
    spdx: "CC-BY-4.0"
    name: "Creative Commons Attribution 4.0"
    url: "https://creativecommons.org/licenses/by/4.0/"

maintainers:
  - name: "KFM Maintainers"
    role: "review/merge"
    contact: "repo-owners"

created_at: "2026-01-17"
updated_at: "2026-01-17"

assets:
  - id: kfm.media.kansas-historical-maps.1885_state_map.v1
    type: image
    title: "Kansas State Map (1885)"
    description: >
      Scanned historical map used for timeline comparison and story annotations.
    origin:
      publisher: "Example Archive"
      url: "https://example.org/kansas-map-1885"
      accessed_at: "2026-01-10"
      source_id: "archive:KS-1885-001"
    license:
      spdx: "Public-Domain"
      name: "Public Domain"
      url: "https://creativecommons.org/publicdomain/mark/1.0/"
    attribution: "Example Archive — Kansas State Map (1885). Public Domain."
    tags: ["kansas", "map", "1885", "historical"]

    files:
      - role: raw
        path: "../raw/kansas-historical-maps/1885_state_map.tif"
        mime: "image/tiff"
        sha256: "REPLACE_ME"
      - role: derived
        path: "../derived/kansas-historical-maps/1885_state_map_2400w.webp"
        mime: "image/webp"
        sha256: "REPLACE_ME"

    processing:
      - step: "convert"
        tool: "imagemagick"
        notes: "Converted TIFF → WEBP for web delivery"
      - step: "resize"
        tool: "imagemagick"
        notes: "Generated 2400px max-width derivative"

    spatial:
      crs: "EPSG:4326"
      bbox: [-102.051, 36.993, -94.588, 40.003]

    sensitivity:
      classification: "public"
      notes: "No restrictions."
```

---

## ➕ Adding a new media source (checklist)

1. 🏷️ **Choose a stable ID**
   - Prefer predictable, versioned IDs:  
     `kfm.media.<collection>.<slug>.v<major>`

2. 🧾 **Document licensing**
   - If you can’t clearly state license/rights → **don’t ship it**

3. 📥 **Place the bits (when allowed)**
   - `../raw/...` for originals  
   - `../derived/...` for optimized UI-ready assets

4. 🔐 **Generate integrity hashes**
   - Include `sha256` for **every** file entry

5. 🧱 **Record processing**
   - Write every transformation step as `processing[]`
   - Keep it reproducible (tools + intent)

6. 🧪 **Validate**
   - Ensure it matches `schema/media-source-manifest.schema.json`
   - If CI exists: it should fail on missing fields / bad hashes

7. 🔎 **PR review**
   - Reviewers should check: source, license, and whether the UI needs it

---

## 🔒 Sensitivity & sovereignty

Some media may represent:
- culturally sensitive locations
- private individuals
- restricted Indigenous knowledge
- security-sensitive infrastructure

If an item is not fully public, set `sensitivity.classification` and ensure derivatives honor the rule:

> 🧷 **No output artifact may be less restricted than its inputs.**

---

## ⚡ Performance notes

- Keep manifests **small & readable**
- Split large collections into multiple files (e.g. by theme or era)
- Prefer **derived web formats** (webp/avif, optimized PDFs, streaming-friendly video)

---

## 🧭 Related (conceptual) pipeline

Even though this folder is under `web/`, manifests should remain compatible with KFM’s broader “contracts → governed outputs → UI” approach:

- 📥 Source declaration (manifests)
- 🧱 Processing (derived assets)
- 🧾 Attribution & citations (UI)

---

## 🧰 FAQ

### “Do we store raw media in git?”
**Only if** the license and size make sense. Otherwise:
- store raw elsewhere (e.g., DVC or object storage)
- keep the manifest + checksums in git
- generate derived assets during build/release

### “What if the source URL changes?”
Do **not** delete history. Update `origin`, bump `updated_at`, and consider bumping the asset’s `.v#` if meaningfully different.

### “How does the UI use this?”
Typically via a generated `index.json`:
- fast lookup by `asset.id`
- standardized attribution blocks
- stable references for story nodes

---

## 🧡 Conventions

- ✅ `kebab-case` for IDs and filenames
- ✅ ISO dates: `YYYY-MM-DD`
- ✅ Explicit license for every asset
- ✅ Every file has `sha256`
- ✅ Every transformation has a `processing[]` entry

---

## 🧾 TODOs (recommended next files)

- `schema/media-source-manifest.schema.json` 🧪 (validation)
- `_generated/index.json` ⚙️ (build output)
- `_generated/checksums.json` 🔐 (integrity map)

---
