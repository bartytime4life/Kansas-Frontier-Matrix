---
title: "🔷 KFM v11.2.3 — Smoky Hill Cultural Drainage Region H3 Mosaics (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/data/h3/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 cultural-landscape-region data-contract (H3 layer)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-cultural-landscape-regions-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Region Data Subdirectory"
intent: "cultural-landscape-region-smoky-hill-h3"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🔷 **KFM — Smoky Hill Cultural Drainage Region · H3 Mosaics**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/data/h3/README.md`

**Purpose:**  
Define and govern the **public H3 mosaic layer** for the **Smoky Hill Cultural Drainage Region**.  
This directory holds **hexagonal H3 representations** of the Smoky Hill corridor that:

- Support sensitivity-aware and scale-aware visualizations  
- Power Focus Mode v2/v3 overlays and Story Node context chips  
- Back STAC Item assets for `"h3-only"` visibility policies  
- Remain **FAIR+CARE-compliant**, **sovereignty-safe**, and **site-safe**

All mosaics here are **derived** from more detailed internal sources and must never expose raw or high-precision data.

</div>

---

## 📘 Overview

The H3 GeoJSON files in this directory represent:

- A **primary H3 mosaic** at a governed resolution (e.g., `res=6`)  
- An optional **coarser mosaic** for ultra-generalized views (e.g., `res=5`)  

They are used when:

- CARE policies require `"h3-only"` representations instead of polygons  
- Wide-area or high-level views benefit from normalized hexagonal footprints along the Smoky Hill drainage corridor  

Authoritative data contract for the parent region data directory is defined at:

- `../README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/data/h3/
├── 📄 README.md                                   # This file (H3 layout & constraints)
├── 🔷 smoky-hill-region-h3-r6.v1.geojson          # Primary H3 mosaic @ res=6
└── 🔷 smoky-hill-region-h3-r5.v1.geojson          # Optional coarser mosaic @ res=5
~~~

**Naming contract:**

- `smoky-hill-region-h3-r<res>.v<semver>.geojson`  
  - Example: `smoky-hill-region-h3-r6.v1.geojson`  

All filenames must:

- Use lowercase, dash-separated slugs  
- Encode the **region slug**, H3 resolution, and semantic version

---

## 🔢 H3 Mosaic Schema & CRS Requirements

All `.geojson` files in this directory must:

- Be valid **GeoJSON** (a `FeatureCollection` is recommended)  
- Use **Polygon** or **MultiPolygon** geometries representing H3 cell boundaries  
- Use **EPSG:4326** (WGS84 lon/lat) coordinates  
- Avoid:

  - Geometry-less encodings (H3 strings with no polygons)  
  - Mixed geometry types (Points/Lines) in the same file  
  - Excessive cell density that implies backing site-level data

Recommended pattern:

- A `FeatureCollection` where each `Feature` corresponds to one H3 cell.  
- Geometry = H3 cell polygon, properties = H3 index and KFM-specific fields.

---

## 🧾 Required Properties (Per H3 Cell Feature)

Each H3 cell feature must include:

- `kfm:region_slug = "smoky-hill-region"`  
- `kfm:h3_resolution` — integer (e.g., `6` or `5`)  
- `kfm:version = "v1"` (or appropriate version)  
- Either:

  - `h3:index` — canonical H3 index string (preferred), or  
  - An equivalent property defined in the KFM H3 profile  

Optional convenience properties:

- `kfm:region_kind = "drainage"` (and optionally `"eco-cultural"`)  
- `kfm:cell_role` — if certain cells are flagged for special display or analysis purposes  

**Do not** embed:

- Site IDs, internal dataset IDs, or any sensitive attributes  
- Detailed upstream evidence references (those belong in provenance & metadata)

---

## 📊 File-Specific Contracts

### 1️⃣ `smoky-hill-region-h3-r6.v1.geojson` (Primary Mosaic)

Represents the **primary H3 mosaic** for the Smoky Hill region at `res=6`.

Requirements:

- Approximate the canonical region polygon from `../geojson/` at the specified resolution.  
- Cover the same conceptual drainage corridor and valley context used by the region dataset and STAC artifacts.  
- Align with `"polygon-generalized"` or `"h3-only"` visibility rules in CARE metadata.

Use for:

- Most H3-based overlays in Focus Mode.  
- Sensitivity-aware views where per-cell aggregation along the river corridor is sufficient.

---

### 2️⃣ `smoky-hill-region-h3-r5.v1.geojson` (Coarser Mosaic)

Represents a **coarser H3 mosaic** at `res=5`.

Requirements:

- True generalization of the `res=6` mosaic (no finer detail).  
- Suitable for very small-scale / wide-area maps (state / Plains overview).

Use for:

- Extremely zoomed-out representations where a small number of cells cover the Smoky Hill drainage.  
- Performance-sensitive contexts or where higher abstraction is preferred.

Any additional resolutions must follow this contract and be recorded in provenance.

---

## ⚖ CARE, Sovereignty & Sensitivity

H3 mosaics are a key tool for enforcing CARE and sovereignty protections in the Smoky Hill corridor:

They **must not**:

- Use H3 resolutions so fine that settlement distributions or sensitive riverine locales can be inferred.  
- Reconstruct confidential patterns when overlaid with other public data.  
- Represent contested or sovereign boundaries without explicit governance approval.

Effective precision must align with:

- `care:sensitivity` and `care:visibility_rules` in region metadata, STAC, and provenance.  
- Example: If `"h3-only"` is mandated for certain modes, only these mosaics — not polygons — should be used in map overlays for those modes.

Any change that increases spatial precision (e.g., adding `res=7` mosaics) is a **governance event** and may require **tribal/sovereign review** and updated provenance.

---

## 🧬 Provenance, STAC & Metadata Linkage

Each H3 mosaic file must be:

- Referenced by at least one STAC Item under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/items/`  
  via assets such as:

  - `assets.h3` with `href` pointing into `../data/h3/`.

- Covered by a canonical PROV-O provenance log under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `smoky-hill-region-v1.json`).

Provenance must document:

- The algorithms and parameters used to generate the H3 mosaics:
  - Polygon → H3 fill  
  - Clipping, filtering, and quality checks  
- The relationship between polygon generalizations and H3 mosaics.  
- Review activities and agents (FAIR+CARE, tribal).

Region metadata (e.g., `../metadata/dcat-smoky-hill-region-v1.jsonld`) must be consistent with:

- H3 resolutions used here.  
- CARE visibility rules referencing `"h3-only"` where appropriate.

---

## 🧪 Validation & CI/CD

H3 GeoJSON files in this directory are **CI-enforced**.

### Geometry & H3 Checks

- GeoJSON schema validation.  
- Polygon validity (no malformed cell polygons).  
- H3 integrity checks (as implemented in KFM tooling):
  - Valid `h3:index` strings.  
  - All cells at the declared `kfm:h3_resolution`.

### Cross-Link Checks

- Every file must:

  - Be referenced in at least one STAC Item as an asset.  
  - Be covered by a PROV-O provenance entity in the associated log.  

- STAC Items that reference H3 mosaics must pass:
  - STAC schema + KFM archaeology profile validation.  
  - CARE/sovereignty checks.

### Governance & CARE Checks

CI must **block**:

- Introduction of finer-than-allowed H3 resolutions without governance approval.  
- Changes where H3 coverage no longer reasonably matches the drainage-region polygon extent.  
- CARE inconsistencies between H3 assets and region metadata/provenance.

Indicative CI workflows:

- `artifact-stac-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml`  

---

## 🧭 Authoring & Update Workflow

When modifying H3 mosaics in this directory:

1. **Derive from internal sources**  
   - Generate mosaics from trusted internal geometries and analyses, **not** from public GeoJSON only.

2. **Generate or update mosaics**  
   - Use governed tools to fill and clip H3 cells.  
   - Record `h3_resolution`, fill rules, clipping logic, and filters for provenance.

3. **Update STAC & Metadata**  
   - Ensure STAC Items reference the correct H3 files and resolutions.  
   - Confirm CARE visibility rules reflect any new H3 assets.

4. **Update Provenance**  
   - Bump or append PROV-O logs documenting mosaic creation or changes.  
   - Ensure region provenance refs include the updated canonical provenance paths.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-smoky-hill-h3`) for geometry, H3, STAC, and CARE checks.

6. **Submit PR & Address Feedback**  
   - CI and governance reviewers confirm compliance before merge.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed H3 mosaic layout, naming, and CARE/provenance/CI requirements for Smoky Hill Cultural Drainage Region; aligned with region data, STAC, metadata, and provenance standards. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Smoky Hill Region Data](../README.md) · [⬅ Back to Smoky Hill Cultural Drainage Region](../../README.md) · [⬅ Back to Cultural Landscape Regions](../../../README.md)

</div>
