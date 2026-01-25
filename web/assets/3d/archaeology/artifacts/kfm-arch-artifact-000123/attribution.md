---
kfm:
  asset_id: "kfm-arch-artifact-000123"
  asset_path: "web/assets/3d/archaeology/artifacts/kfm-arch-artifact-000123/"
  asset_type: "3d_model"
  domain: "archaeology"
  status: "draft"
  created_utc: "2026-01-25"
  updated_utc: "2026-01-25"

  ui_contract:
    purpose: "Human-readable attribution + governance summary for the KFM UI (Layer/Asset Info panels) and exports."
    safe_for_public_display: true
    must_exist_for_publish: true

  standards:
    provenance_required: true
    stac_item: "./stac-item.json"        # REQUIRED (machine-readable)
    dcat_dataset: "./dcat-dataset.json"  # REQUIRED (machine-readable)
    prov_jsonld: "./prov.jsonld"         # REQUIRED (machine-readable)

  sensitivity:
    level: "sensitive_location"          # public | sensitive_location | confidential | embargoed
    public_location_precision: ">=10km"  # recommended obfuscation for public archaeology content
    reason: "Archaeological/cultural heritage locations can be exploited; public releases must avoid precise findspot/site coordinates."

  licensing:
    asset_license: "TBD"                 # e.g., CC-BY-4.0, CC0-1.0, custom, etc.
    textures_license: "TBD"
    metadata_license: "CC0-1.0 (recommended)"
    combined_output_rule: "Most restrictive license wins when composing layers/outputs."

  build_and_integrity:
    pipeline_run_id: "TBD"
    reproducible_pipeline: true
    checksums:
      glb_sha256: "TBD"
      textures_sha256: "TBD"
    attestations:
      sbom: "TBD"                        # e.g., ./sbom.spdx.json
      provenance_attestation: "TBD"      # e.g., ./provenance.intoto.jsonl
      signature: "TBD"                   # e.g., cosign bundle / sigstore log reference
---

# 🏺 Attribution & Governance — `kfm-arch-artifact-000123`

![Provenance](https://img.shields.io/badge/Provenance-Enforced-brightgreen)
![Standards](https://img.shields.io/badge/Standards-STAC%20%7C%20DCAT%20%7C%20PROV-blue)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-6f42c1)
![Sensitivity](https://img.shields.io/badge/Sensitivity-Location%20Redacted-yellow)
![3D](https://img.shields.io/badge/3D-glTF%202.0-0b5fff)

> ⚠️ **Archaeology safety note:** This asset is published with **location redaction/obfuscation** by default.  
> Do **not** use KFM outputs to locate, target, or disturb archaeological sites or cultural heritage materials.

---

## 📌 Quick Attribution (for UI overlays, exports, screenshots)

Use the **short** line when space is tight (e.g., a corner watermark). Use the **long** line for reports, publications, exhibits, and classroom materials.

```text
SHORT:
Kansas Frontier Matrix (KFM) — Archaeology 3D Artifact: kfm-arch-artifact-000123. See attribution.md for sources & license.
```

```text
LONG:
Kansas Frontier Matrix (KFM) — Archaeology 3D Artifact: kfm-arch-artifact-000123 (3D model + metadata). Provenance is tracked via STAC/DCAT/PROV. License/rights and upstream credits are documented in attribution.md and the linked catalog records. Sensitive-location handling applies.
```

✅ **If you remix/derive:** keep `artifact_id` unchanged and add a *new* derived asset ID; do not overwrite this attribution.

---

## 🧭 What this asset is

**Asset ID:** `kfm-arch-artifact-000123`  
**Type:** 3D archaeological object representation (web-ready model)  
**Intended uses:**  
- 🗺️ **KFM 2D/3D map contexts** (MapLibre + Cesium/3D viewers)  
- 📚 **Story Nodes / guided narratives** (2D→3D transitions, “stop” panels)  
- 🧑‍🏫 **Education & exhibits** (with explicit credits + licensing)  
- 📦 **Offline packs** (field/classroom use)  
- 🕶️ **AR-ready pipeline** (optional future packaging)

**Not intended for:** authentication of provenance/ownership, monetization without rights clearance, or precise site discovery.

---

## 🔐 Sensitivity, Ethics, and CARE controls

KFM follows **FAIR** (Findable, Accessible, Interoperable, Reusable) while honoring **CARE** (Collective Benefit, Authority to Control, Responsibility, Ethics) for cultural and sensitive data.

### Location policy (public release)
- ✅ Public-facing location is **generalized** (e.g., county / coarse grid / ~10km rounding).
- ✅ Any **precise findspot/site coordinates** must be:
  - withheld, **or**
  - gated behind authenticated roles **and** explicit approvals (community/authority),
  - and always recorded in provenance logs when accessed.

### Cultural protocols (when applicable)
If this artifact relates to Indigenous heritage or community-defined cultural protocols:
- Add **rights-holder contact** and **usage constraints** in the **Licensing & Rights** section.
- Add **access tier** requirements in **Access & Distribution** below.
- Add **context labels** (e.g., “restricted reproduction”, “community-only”) in the STAC/DCAT records.

---

## 📜 Licensing & Rights (MUST be completed before publish)

> Until this section is completed, treat the model as **All Rights Reserved** (internal use only).

### License matrix 🧾

| Component | File(s) | License | Rights holder | Notes |
|---|---|---:|---|---|
| 3D model geometry | `*.glb` / `*.gltf` | **TBD** | **TBD** | Include scan/reconstruction rights + permitted uses |
| Textures / materials | `textures/*` | **TBD** | **TBD** | Ensure texture sources are cleared (no unlicensed photos) |
| Metadata (this file) | `attribution.md` | CC0-1.0 (recommended) | KFM contributors | Safe-to-share descriptive metadata |
| Catalog metadata | `stac-item.json`, `dcat-dataset.json` | CC0-1.0 (recommended) | KFM contributors | Must include source/license fields |

### “Most restrictive wins” rule 🧠
If this asset is composed from multiple sources (e.g., external scans + third-party textures), the **output inherits the most restrictive license** among components. Document any downstream constraints here and in DCAT.

---

## 🧬 Provenance & Catalog pointers (STAC / DCAT / PROV)

KFM requires provenance for **every** published layer/asset. This file is the **human-readable summary**; the machine-readable truth is linked below.

- 🗂️ **STAC Item (asset-level metadata):** `./stac-item.json`
- 🏷️ **DCAT Dataset (dataset-level metadata):** `./dcat-dataset.json`
- 🧾 **W3C PROV (lineage & activities):** `./prov.jsonld`

<details>
<summary>🔍 What should be inside those files?</summary>

- **STAC**: geometry (generalized if sensitive), temporal range (if known), assets list (glb/gltf, textures, preview), roles, keywords, providers, license fields.
- **DCAT**: publisher, maintainer, access URL(s), license, keywords, spatial/temporal coverage, update cadence, contact point.
- **PROV**: capture → processing → export activities, who/what performed them, inputs/outputs, checksums, timestamps, tool versions.

</details>

---

## 🧱 Archaeology “SampleUnitSpec” (domain-pack concept)

This standardizes *what a “sample” is* so the system can scale archaeology workflows consistently.

| Field | Value |
|---|---|
| `sample_unit_spec.id` | `arch.artifact.single_object.v1` |
| `sample_unit_spec.unit` | `1 artifact object` |
| `sample_unit_spec.description` | One physical artifact represented as a single 3D model, with optional contextual metadata (generalized location, associated period/material classification). |
| `sample_unit_spec.capture_session` | See **Capture & Processing** below |
| `sample_unit_spec.constraints` | Scale must be real-world; units declared; orientation declared; sensitive coordinates never public by default |

---

## 🧪 Capture & Processing (3D pipeline summary)

> Goal: ensure this model is not a “pretty black box,” but a traceable research object.

### Capture (fill what you know)
| Field | Value |
|---|---|
| Capture method | TBD (photogrammetry / structured light / LiDAR / CT / manual reconstruction) |
| Capture date (UTC) | TBD |
| Capture operator | TBD |
| Capture device | TBD |
| Capture location | **REDACTED / GENERALIZED** (public) |
| Reference scale | TBD (scale bars / calipers / reference targets) |

### Processing (fill what you know)
| Step | Tooling | Output | Notes |
|---|---|---|---|
| Alignment / reconstruction | TBD | dense cloud / mesh | record tool + version |
| Mesh cleanup | TBD | cleaned mesh | document edits |
| Retopo / decimation | TBD | web mesh | include poly budget target |
| UV unwrap | TBD | UVs | note method |
| Texture bake | TBD | PBR textures | resolution(s) + color space |
| Export | TBD | glTF/GLB | specify glTF 2.0 compliance |

✅ **3D GIS / geospatial integration expectation:** If georeferencing applies, record CRS handling (original CRS, display CRS) and any transformations. Public outputs should align with web display norms (WGS84 for display) while preserving original CRS metadata in provenance.

---

## 🖥️ Rendering & Performance (web/AR ready)

| Property | Target / Expectation |
|---|---|
| Format | glTF 2.0 (`.glb` preferred for single-file delivery) |
| Units | meters (declare real-world scale) |
| Up axis | Y-up (declare if different) |
| Textures | power-of-two preferred; avoid uncompressed huge images |
| LOD strategy | optional (multi-res or decimated “preview” model) |
| Offline pack | include `preview/thumbnail.webp` + `preview/poster.webp` |

> 💡 If this will be used in a **Story Node**, keep a lightweight “preview” model for fast camera stops, and a full-res model behind an explicit “Load detail” action.

---

## 🧠 AI involvement (must be transparent)

KFM’s AI features are **evidence-based** and **human-in-the-loop**.

If AI was used for **any** of the following:
- automatic tagging (material/period/style),
- captioning,
- OCR/metadata extraction from field notes,
- similarity matching against collections,
- generating summaries for Story Nodes,

…then record it here with review status and links to provenance.

| AI task | Model/tool | Human reviewer | Review date | Notes |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | AI outputs must be labeled as AI-assisted; do not present as ground truth |

---

## 🛡️ Integrity, Security & Supply Chain (recommended)

For trust and reproducibility, attach or reference:

- 🔒 **Checksums** (SHA-256) for model + textures
- 🧾 **Provenance attestation** (CI/CD generated)
- 📦 **SBOM** for build toolchain (if bundled)
- ✍️ **Signature** for published artifacts (e.g., signed build outputs)

```text
glb_sha256:      TBD
textures_sha256: TBD
sbom:            TBD
signature:       TBD
```

---

## 🧾 How to cite (recommended template)

> Replace placeholders once licensing/rights are confirmed.

**Citation (APA-ish):**
```text
Kansas Frontier Matrix (KFM) contributors. (2026). Archaeology 3D Artifact: kfm-arch-artifact-000123 [3D model]. Kansas Frontier Matrix. (See STAC/DCAT/PROV metadata in the repository.)
```

**Citation (BibTeX template):**
```bibtex
@misc{kfm_arch_artifact_000123,
  title        = {Archaeology 3D Artifact: kfm-arch-artifact-000123},
  author       = {{Kansas Frontier Matrix (KFM) contributors}},
  year         = {2026},
  howpublished = {Kansas Frontier Matrix repository asset},
  note         = {Provenance tracked via STAC/DCAT/PROV; see attribution.md for licensing and sensitivity notes.}
}
```

---

## 🗂️ Expected sibling files (recommended layout)

```text
📦 web/assets/3d/archaeology/artifacts/kfm-arch-artifact-000123/
├─ 🧾 attribution.md            # this file (human-readable)
├─ 🗂️ stac-item.json           # machine-readable asset catalog entry
├─ 🧬 dcat-dataset.json         # machine-readable dataset catalog entry
├─ 🧾 prov.jsonld               # lineage + pipeline activity log
├─ 🧩 model.glb                 # primary 3D asset (preferred)
├─ 🖼️ textures/                 # PBR textures (if external)
│  ├─ baseColor.*
│  ├─ normal.*
│  ├─ metallicRoughness.*
│  └─ occlusion.*
└─ 🖼️ preview/
   ├─ thumbnail.webp
   └─ poster.webp
```

---

## ✅ Publish “Definition of Done” (artifact attribution)

### Required ✅
- [ ] `asset_license` filled (and compatible with upstream rights)
- [ ] rights holder(s) + credit(s) filled
- [ ] sensitivity level confirmed (`public` vs `sensitive_location` vs stricter)
- [ ] public location redaction verified
- [ ] STAC/DCAT/PROV files present and linked correctly
- [ ] model scale + units declared
- [ ] export is web-safe (performance check)

### Strongly recommended ⭐
- [ ] SHA-256 checksums recorded
- [ ] signature/attestation attached
- [ ] preview thumbnail/poster added
- [ ] AI assistance disclosure completed (if any)
- [ ] Story Node compatibility notes added (if used in narratives)

---

## 🧩 Maintainer Notes (why this file exists)

KFM’s UI and export tools are designed so that **every visible layer/asset carries attribution and provenance**. This file is the simplest, human-readable “receipt” that travels with the asset, while the catalog files (STAC/DCAT/PROV) provide full machine-readable traceability.

---

## 📚 Internal design references (for maintainers)

<details>
<summary>📖 Project docs that shaped this attribution format</summary>

- Kansas Frontier Matrix — UI System Overview (provenance surfaced everywhere; exports carry credits)  
- KFM — AI System Overview (evidence-based AI with citations; AR/offline direction)  
- KFM — Data Intake Guide (policy gates; catalog-first publishing; provenance-required data flows)  
- KFM — Comprehensive Architecture / Technical Documentation (FAIR/CARE, licensing, sensitivity, 2D/3D stack, WGS84 display norms)  
- KFM — Latest Ideas & Future Proposals (role-based access, FAIR/CARE enforcement by agents, supply-chain attestations)  
- Innovative Concepts to Evolve KFM (AR/hybrid storytelling; cultural protocols; sensitivity-aware handling)  
- Supporting research portfolios (AI, data engineering, maps/WebGL/3D GIS) — used to inform the 3D + ethics + governance checklist items.

</details>

