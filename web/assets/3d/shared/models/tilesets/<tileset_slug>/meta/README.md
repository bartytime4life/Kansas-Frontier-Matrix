# 🧱 Tileset Meta — `<tileset_slug>`

![KFM](https://img.shields.io/badge/KFM-Tileset%20Meta%20Contract-v1-informational)
![3D%20Tiles](https://img.shields.io/badge/Format-3D%20Tiles-blue)
![CesiumJS](https://img.shields.io/badge/Viewer-CesiumJS-0b7285)
![Evidence%20First](https://img.shields.io/badge/Principle-Evidence--First-success)
![Policy%20as%20Code](https://img.shields.io/badge/Governance-OPA%20%2B%20Conftest-important)

> 🧭 **What this folder is:** the **human + machine metadata** (“data contract”) for a single 3D Tiles tileset in the Kansas Frontier Matrix (KFM).  
> ✅ **If it isn’t documented here (and in STAC/DCAT/PROV), it doesn’t ship.** No mystery layers.

---

## ✨ TL;DR Contract Checklist

Before this tileset can appear in **KFM UI**, **Story Nodes**, or **Focus Mode**:

- [ ] `../tileset.json` exists and loads ✅
- [ ] `meta/tileset.meta.json` completed (KFM Tileset Meta v1) 🧾
- [ ] `meta/stac.item.json` completed (points to the tileset as an asset) 🛰️
- [ ] `meta/dcat.dataset.json` completed (license + publisher + access) 🏷️
- [ ] `meta/prov.bundle.jsonld` completed (inputs + processing trace) 🧬
- [ ] `meta/sensitivity.json` completed (classification + CARE/sovereignty flags) 🔒
- [ ] `meta/thumbnail.(png|jpg|webp)` created 🖼️
- [ ] If tileset is **too large for Git**: `meta/distribution.json` includes **OCI digest + signature expectations** 📦🔏
- [ ] Optional but recommended: `meta/evidence-manifest.(yml|json)` for Story/Facts reproducibility 🧾🧪

---

## 🧭 Quick Links

- **Tileset entrypoint:** `../tileset.json`
- **KFM contract:** `./tileset.meta.json`
- **STAC evidence:** `./stac.item.json`
- **DCAT evidence:** `./dcat.dataset.json`
- **PROV evidence:** `./prov.bundle.jsonld`
- **Sensitivity:** `./sensitivity.json`
- **Preview:** `./thumbnail.png` *(or .jpg/.webp)*
- **Optional UI hints:** `./ui.layer.json`
- **Optional styling:** `./style.cesium.json`
- **Optional evidence manifest:** `./evidence-manifest.yaml`

---

## 🗂️ Expected Directory Layout

> Keep **heavy binaries** out of `meta/`. Meta is for *contracts + evidence*, not payload.

```text
🌐 web/
└── 🧰 assets/
    └── 🧊 3d/
        └── 🤝 shared/
            └── 🧩 models/
                └── 🧱 tilesets/
                    └── 🏷️ <tileset_slug>/
                        ├── 🗺️ tileset.json                 ← 3D Tiles root (entrypoint)
                        ├── 📦 content/                     ← tile payloads (b3dm/i3dm/glb/...) OR externalized
                        └── 🧾 meta/
                            ├── 📄 README.md                ← 👈 📍 you are here ✅
                            ├── 🧾 tileset.meta.json         ← KFM Tileset Meta v1 (required)
                            ├── 🛰️ stac.item.json            ← STAC Item (required)
                            ├── 🏷️ dcat.dataset.json         ← DCAT Dataset (required)
                            ├── 🧬 prov.bundle.jsonld        ← PROV bundle (required)
                            ├── 🛡️ sensitivity.json          ← classification + CARE flags (required)
                            ├── 🖼️ thumbnail.png             ← preview image (required)
                            ├── 🌍 distribution.json          ← OCI / remote distribution pointer (optional)
                            ├── 🧾 evidence-manifest.yaml     ← reproducibility ledger (optional)
                            ├── 🧩 ui.layer.json              ← UI defaults (optional)
                            ├── 🎨 style.cesium.json          ← styling rules (optional)
                            ├── 🔐 checksums.txt              ← sha256 list (optional, recommended)
                            └── 📜 LICENSE.txt                ← only if different from repo license (optional)
```

---

## 🧩 How KFM Uses Tilesets

### 🌍 UI (2D ⇄ 3D)
- KFM is **2D-first** for layered exploration, but 3D is supported via **CesiumJS** when it adds value (terrain, structures, subsurface concepts, “wow” moments).  
- This tileset should be **opt-in**: only load when the user toggles 3D mode or enables the layer.

### 🤖 Focus Mode (AI + citations)
- Focus Mode is **evidence-first**. Metadata here enables:
  - auto-attribution ✅
  - traceable answers ✅
  - refusal when missing provenance ✅

### 📚 Story Nodes
- Story Nodes can “fly” into a scene (3D camera) and cite the same evidence triplet.
- If a Story Node uses this tileset, add an **evidence manifest** entry that pins the exact version/digest.

---

## 🧱 Naming & Identity Rules

### 🧾 `tileset_slug` conventions
Use **lowercase kebab-case**. Keep it stable. Prefer:
- place + feature + year/range  
  - `monument-rocks-photogrammetry-2024`
  - `flint-hills-terrain-1850-1900`
- if sensitive/controlled, avoid leaking specifics in the slug:
  - `restricted-site-01` ✅ *(with real name in restricted metadata)*

### 🆔 IDs should be stable + deterministic
Recommended pattern:
- `kfm.tileset.<tileset_slug>`
- version: SemVer for metadata contract (`1.2.0`) and/or a content digest for payload identity.

---

## 🧾 Required Metadata Files

### 1) `tileset.meta.json` (KFM Tileset Meta v1)
This is the **primary “data contract”** for the tileset.

**Minimum required fields (v1):**
- `schema`
- `id`, `slug`, `version`
- `title`, `description`
- `spatial.extent` *(bbox + z-range)*
- `crs.horizontal` + `crs.vertical` *(or explicit `unknown` + notes)*
- `license` + `attribution`
- `sensitivity.classification`
- `distribution.mode` *(local|oci|remote)*
- `provenance.refs` *(STAC/DCAT/PROV pointers)*

**Template (copy/paste and fill):**
```json
{
  "schema": "kfm.tileset-meta/v1",
  "id": "kfm.tileset.<tileset_slug>",
  "slug": "<tileset_slug>",
  "version": "0.1.0",
  "title": "<Human title>",
  "description": "<What it is + why it matters + what it is NOT>",
  "themes": ["terrain", "history", "structures"],
  "keywords": ["Kansas", "KFM", "3D Tiles"],

  "spatial": {
    "bbox_wgs84": [-102.0, 36.99, -94.6, 40.0],
    "z_range_m": [0, 300],
    "center_wgs84": [-98.0, 38.5]
  },

  "crs": {
    "horizontal": "EPSG:4326",
    "vertical": "UNKNOWN",
    "vertical_notes": "Specify ellipsoidal/orthometric + datum if known."
  },

  "units": {
    "z": "m"
  },

  "quality": {
    "positional_accuracy_m": null,
    "vertical_accuracy_m": null,
    "known_limitations": [
      "Example: Photogrammetry mesh is best-effort; vegetation is simplified."
    ]
  },

  "sensitivity": {
    "classification": "public",
    "care_labels": [],
    "sovereignty_notes": ""
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "url": "<license url if applicable>",
    "notes": ""
  },

  "attribution": {
    "publisher": "<Org/Project>",
    "creators": ["<Name/Team>"],
    "source_citation": "<Short source citation>",
    "acknowledgements": []
  },

  "distribution": {
    "mode": "local",
    "entrypoint": "../tileset.json",
    "oci": {
      "ref": null,
      "digest": null,
      "signature_required": true
    },
    "remote": {
      "url": null,
      "headers_required": false
    }
  },

  "provenance": {
    "refs": {
      "stac_item": "./stac.item.json",
      "dcat_dataset": "./dcat.dataset.json",
      "prov_bundle": "./prov.bundle.jsonld",
      "evidence_manifest": "./evidence-manifest.yaml"
    },
    "pipeline_run_id": null,
    "inputs": [
      {
        "name": "<input dataset name>",
        "uri": "<stable id or url>",
        "license": "<input license>",
        "notes": ""
      }
    ],
    "tools": [
      {
        "name": "<tool>",
        "version": "<x.y.z>",
        "notes": ""
      }
    ]
  },

  "ui": {
    "recommended_view": "3d",
    "default_visibility": false,
    "opacity": 1.0,
    "legend": {
      "label": "<legend label>",
      "notes": ""
    }
  }
}
```

---

### 2) `stac.item.json` (Evidence: “what + where + assets”)
**Purpose:** make the tileset discoverable as a geospatial asset with consistent extents + links.

Suggested STAC approach:
- STAC Item geometry = footprint (polygon) or bbox  
- Add an asset such as:
  - `assets.tileset` → `../tileset.json`

> ✅ Keep the STAC ID stable and align with `tileset.meta.json:id`.

---

### 3) `dcat.dataset.json` (Evidence: “who + license + governance”)
**Purpose:** dataset-level publishing metadata (publisher, access rights, license, update cadence).

> ✅ DCAT is where “Can we ship this?” becomes explicit.

---

### 4) `prov.bundle.jsonld` (Evidence: “how it was made”)
**Purpose:** declare lineage:
- inputs used
- transformation steps
- agents (authors/reviewers/build system)
- outputs produced

> ✅ If this tileset was generated in CI or via a pipeline run, include a stable run ID and hashes.

---

### 5) `sensitivity.json` (Ethics + safety)
**Purpose:** codify:
- classification (public/internal/restricted)
- sovereignty constraints
- redaction requirements (e.g., fuzzing, bounding generalization)
- distribution constraints (e.g., no public CDN)

Example:
```json
{
  "classification": "public",
  "care_labels": [],
  "constraints": {
    "no_public_release": false,
    "requires_location_fuzzing": false,
    "min_bbox_size_km": 0
  },
  "notes": ""
}
```

---

## 🔐 Governance Rules (Fail-Closed by Design)

### ✅ Required
- **License must exist** (repo policy / CI policy gates).
- **No secrets in repo** (scan + deny).
- **No “mystery layers”**: anything exposed must have STAC/DCAT/PROV.
- **No output may be less restricted than inputs** (sovereignty/classification).

### 🚫 Not allowed
- Publishing a tileset with unknown provenance.
- Copying restricted geometry into a public tileset without required generalization/redaction.
- Committing gigantic tile payloads to Git when OCI distribution is intended.

---

## 📦 Distribution Modes

### Mode A — `local` (small demo / safe to ship)
Use when payload is small enough to live in the repo + static hosting.

- `distribution.mode = "local"`
- `distribution.entrypoint = "../tileset.json"`

### Mode B — `oci` (recommended for large tilesets)
Use when tileset payload is too large for Git or needs verifiable supply-chain integrity.

- Store payload as an **OCI artifact**
- Pin by **digest**
- Require **signature verification**
- Keep only pointers + evidence in repo

`distribution.json` example:
```json
{
  "mode": "oci",
  "oci": {
    "ref": "oci://<registry>/<org>/kfm-tilesets/<tileset_slug>:<tag>",
    "digest": "sha256:<immutable_digest>",
    "signature_required": true
  }
}
```

### Mode C — `remote` (CDN/object storage)
Use when tileset is hosted on a controlled endpoint.

- Provide stable URL
- Document auth headers requirement if any
- Still require STAC/DCAT/PROV

---

## 🧪 QA & Validation Checklist (Make CI Happy)

### 🧾 Metadata QA
- [ ] IDs match across `tileset.meta.json`, STAC, DCAT, PROV
- [ ] License fields exist + are explicit
- [ ] Sensitivity classification exists
- [ ] CRS is declared (horizontal + vertical or “UNKNOWN + notes”)
- [ ] bbox + z-range match real payload

### 🧱 Payload QA
- [ ] `tileset.json` loads without console errors
- [ ] Bounding volume covers content (no “invisible” tiles)
- [ ] LOD behaves (no popping catastrophe / no overdraw meltdown)
- [ ] Feature picking works (if metadata is embedded)

### 🖼️ UI QA
- [ ] Thumbnail exists and is representative
- [ ] Default visibility is **off** unless explicitly needed
- [ ] Layer name/description are human-friendly

### 🔏 Integrity QA (if OCI)
- [ ] digest pinned
- [ ] signature required and verified by policy
- [ ] checksums recorded (recommended)

---

## 🎛️ Optional UI Hints

### `ui.layer.json` (optional)
Use to suggest reasonable defaults for layer cards, toggles, and performance flags.

```json
{
  "layer_id": "kfm.tileset.<tileset_slug>",
  "type": "cesium-3dtiles",
  "label": "<Human label>",
  "description": "<Short description>",
  "default_visibility": false,
  "performance": {
    "max_screen_space_error": 16,
    "prefer_least_loaded_tiles": true
  },
  "time": {
    "enabled": false,
    "range": null
  }
}
```

### `style.cesium.json` (optional)
Keep styling separate when possible to avoid mutating payload for cosmetic changes.

---

## ⏳ Time-Travel Readiness (4D-Friendly)

If this tileset represents a time slice (or evolving geometry):
- add `temporal` fields in `tileset.meta.json`
- ensure the **timeline** can switch between versions without breaking provenance
- prefer append-only: new version = new artifact, not silent replacement

Suggested block:
```json
{
  "temporal": {
    "mode": "snapshot",
    "start": "1850-01-01",
    "end": "1850-12-31",
    "time_zone": "America/Chicago"
  }
}
```

---

## 🧠 AI / Analytics Readiness (Optional but Powerful)

If you want AI + graph queries to reason about this tileset:
- embed stable feature IDs
- include semantic tags (building/road/river/formation/etc.)
- record uncertainty/accuracy in metadata (don’t pretend precision you don’t have)

---

## 🧾 Changelog (Append-Only)
- **0.1.0** — Initial import (contract + evidence + preview)

---

## 👥 Ownership & Review

- **Owner / Steward:** `<name or team>`
- **Reviewer(s):** `<name(s)>`
- **Contact:** `<email/handle>`
- **Last reviewed:** `<YYYY-MM-DD>`

---

## 📜 License & Attribution

- **License (SPDX):** `<SPDX>`
- **Publisher:** `<org>`
- **Attribution:** `<required credit line>`
- **Source(s):** `<human citation(s)>`

> ✅ If attribution requirements are non-negotiable, also encode them in DCAT and in UI layer card text.

---

