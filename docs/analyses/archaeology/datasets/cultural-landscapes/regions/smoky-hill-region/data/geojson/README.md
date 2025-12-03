---
title: "🌐 KFM v11.2.3 — Smoky Hill Cultural Drainage Region GeoJSON Geometries (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/data/geojson/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 cultural-landscape-region data-contract (GeoJSON layer)"

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
intent: "cultural-landscape-region-smoky-hill-geojson"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🌐 **KFM — Smoky Hill Cultural Drainage Region · GeoJSON Geometries**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/data/geojson/README.md`

**Purpose:**  
Define and govern the **public GeoJSON geometry layer** for the **Smoky Hill Cultural Drainage Region**.  
This directory holds the **generalized drainage-region polygons** that:

- Power Smoky Hill region STAC Items & Collections  
- Feed Neo4j graph loaders, ETL pipelines, and Focus Mode overlays  
- Drive MapLibre & Cesium visualizations of the Smoky Hill corridor  
- Remain **FAIR+CARE-compliant**, **sovereignty-safe**, and **site-safe**

All geometries here are **derived** from more detailed internal sources and must never include raw or high-precision data.

</div>

---

## 📘 Overview

The GeoJSON files in this directory represent:

- The **primary Smoky Hill cultural drainage region boundary** (generalized polygon)  
- A **topology-safe simplified outline** for very small-scale / overview maps  
- (Optionally) a **mask geometry** for shading or clipping the drainage-region interior  

They must:

- Use **EPSG:4326** (WGS84 lon/lat)  
- Be **topologically valid** and **generalized** (no site-level detail)  
- Align with the region spec, metadata, STAC, and provenance:

  - Region spec: `../README.md`  
  - Region metadata: `../metadata/dcat-smoky-hill-region-v1.jsonld` (or equivalent)  
  - STAC: `../../stac/`  
  - Provenance: `../provenance/` and global `../../../../provenance/`

The authoritative data contract for the parent `data/` directory is defined at:

- `../README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/data/geojson/
├── 📄 README.md                               # This file (GeoJSON layout & constraints)
├── 🌐 smoky-hill-region.v1.geojson           # Primary generalized drainage-region polygon
└── 🌐 smoky-hill-region.v1-topology-simplified.geojson
    # Extra-simplified, topology-safe outline for very small-scale / overview maps
~~~

**Naming contract:**

- `smoky-hill-region.v<semver>.geojson`  
  - Primary region geometry per version (v1, v2, …).  
- `smoky-hill-region.v<semver>-topology-simplified.geojson`  
  - More aggressively simplified, topology-safe outline for overview maps.  
- If added later: `smoky-hill-region.v<semver>-mask.geojson`  
  - Mask/clip geometry for rendering.

All filenames must:

- Use lowercase, dash-separated slugs.  
- Encode the **region slug** (`smoky-hill-region`) and **semantic version** (`v1`, `v2`, …).

---

## 🌍 GeoJSON Schema & CRS Requirements

All `.geojson` files in this directory must:

- Be valid **GeoJSON** (`Feature` or `FeatureCollection`).  
- Use **Polygon** or **MultiPolygon** geometries only.  
- Use **EPSG:4326** (WGS84 lon/lat) coordinates.  
- Avoid:

  - Mixed geometry types in the same file (e.g., Points + Polygons).  
  - Invalid polygons (self-intersections, bow-ties, slivers).  
  - Excessive vertex density that implies hidden high-precision data or raw survey footprints.

Recommended pattern:

- A single `FeatureCollection` with one `Feature` for the main drainage-region polygon.  
- Or a small set of features where the drainage corridor is discontiguous.

---

## 🧾 Required Properties (Per Feature)

Each region feature in these files must include, at minimum:

- `kfm:region_slug = "smoky-hill-region"`  
- `kfm:region_kind = "drainage"` (and optionally `"eco-cultural"`)  
- `kfm:version = "v1"` (or the appropriate version tag)  

Optional convenience properties (canonical values live in STAC/metadata):

- `kfm:culture_phase` — summary of cultural phases (e.g., `["Woodland","Late Prehistoric","Protohistoric"]`)  
- `kfm:source_label` — short label for upstream synthesis (e.g., “hydrology + geomorphology + survey synthesis”)  

**Do not** embed:

- Site IDs or survey IDs.  
- Sensitive local place names or coordinates.  
- Any attributes better handled via provenance or internal-only datasets.

---

## 🧮 File-Specific Contracts

### 1️⃣ `smoky-hill-region.v1.geojson` (Primary)

Represents the **canonical generalized drainage-region polygon** for the Smoky Hill corridor.

Requirements:

- Default geometry used in STAC Items as the main polygon asset.  
- Sufficiently generalized to avoid site-level inference along the valley.  
- In sync with:

  - STAC `bbox` and spatial extent.  
  - Region metadata spatial descriptors (corridor, valley, drainage basin).  
  - Provenance descriptions of generalization steps.

Used for:

- Most region overlays at appropriate map zoom levels.  
- Graph ingestion as the Smoky Hill drainage-region geometry.

---

### 2️⃣ `smoky-hill-region.v1-topology-simplified.geojson` (Simplified)

More aggressively simplified, **topology-safe** geometry for **small-scale / overview** contexts.

Constraints:

- Must remain a **generalization of** the primary polygon (never more detailed).  
- May drop minor features or bends but must preserve the recognizable Smoky Hill drainage form.  
- If referenced in STAC Items, changes require:

  - Updated provenance documenting simplification.  
  - Consistency checks with metadata and CARE policies.

Used for:

- High-level Kansas / Plains overviews.  
- Low-detail basemaps where visual clarity and performance are prioritized.

---

### (Optional) `smoky-hill-region.v1-mask.geojson` (Mask)

If introduced, used as a **rendering or analysis mask**, for example:

- Shading the Smoky Hill corridor interior.  
- Clipping Story Node overlays or other datasets to the drainage-region envelope.

Constraints:

- Must not be more detailed than the primary polygon.  
- May be a copy of the primary polygon or a buffered/eroded variant at the same abstraction level.  
- Any buffering or transformation must be documented in PROV-O provenance.

---

## ⚖ CARE, Sovereignty & Sensitivity

All geometries here must respect CARE and sovereignty constraints, especially around:

- Settlement pattern inference along the Smoky Hill valley.  
- Culturally sensitive riverine locations.  
- Traditional land use and culturally important places.

**Forbidden** in this directory:

- Geometries that allow reverse-engineering of precise site clusters or sensitive locations.  
- Encoded boundaries that could be mistaken for sovereign, legal, or contested cultural claims without explicit approval.  
- Nearly exact copies of confidential drainage or settlement maps.

Effective precision must align with:

- `care:sensitivity` and `care:visibility_rules` in:

  - Region metadata (`../metadata/dcat-smoky-hill-region-v1.jsonld`, or equivalent).  
  - STAC Collections/Items (`../../stac/`).  
  - PROV-O logs (`../provenance/` and `../../../../provenance/`).

Examples:

- `"polygon-generalized"` → polygons may be shown at moderate/regional zooms.  
- `"h3-only"` → polygons may still exist here but clients **must** render only H3 mosaics for some modes.

Any change that tightens geometries around internal data is a **governance event** and may require **tribal/sovereign review**.

---

## 🧬 Provenance, STAC & Metadata Linkage

Each file in this directory must be:

- Referenced by at least one STAC Item under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/items/`  
  via assets such as `assets.data.href`.

- Covered by a canonical PROV-O provenance log under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `smoky-hill-region-v1.json`).

Provenance must record:

- The **output paths** for these files.  
- The **generalization algorithms** and parameters (simplification tolerance, clipping, buffers).  
- Review activities and agents (FAIR+CARE, tribal).

Region metadata JSON-LD must:

- Refer to these geometries indirectly via STAC and provenance.  
- Stay in sync with versioning and coverage.

---

## 🧪 Validation & CI/CD

GeoJSON files in this directory are **CI-enforced**:

### Geometry & Schema Checks

- GeoJSON schema validation.  
- Topology checks:

  - Valid polygons / multipolygons.  
  - No self-intersections or invalid rings.

- Coordinate sanity checks (within valid lat/lon ranges; no NaNs).

### Cross-Link Checks

- Every file must appear as an asset in at least one STAC Item.  
- Corresponding STAC Items must pass:

  - STAC schema validation.  
  - Region metadata cross-checks.  
  - Provenance linkage validation.

### Governance & CARE Checks

- CARE fields in metadata/provenance must be compatible with the level of abstraction in these geometries.  
- CI must **block**:

  - Introduction of geometries that are more precise than allowed.  
  - Removal/renaming of files without updating STAC and provenance.  
  - Any regression flagged by FAIR+CARE or sovereignty audits.

Indicative CI workflows:

- `artifact-stac-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml`  

---

## 🧭 Authoring & Update Workflow

When modifying files in this directory:

1. **Work from internal, non-public sources**  
   - Derive generalized outputs from internal hydrology, geomorphology, and archaeological data.  
   - Never treat these public GeoJSON files as authoritative raw data.

2. **Generate or update generalized geometries**  
   - Apply governed simplification, buffering, clipping, and quality checks.  
   - Capture all parameters for PROV-O (`kfm:steps`).

3. **Update STAC & Metadata**  
   - Ensure STAC Items reference correct filenames and versions.  
   - Confirm spatial coverage in metadata remains accurate and consistent.

4. **Update Provenance**  
   - Bump or append PROV-O provenance log version(s) for `smoky-hill-region`.  
   - Ensure CARE fields and governance notes reflect any changes.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-smoky-hill-geojson`) for geometry, STAC, and CARE checks.

6. **Submit PR & Address Feedback**  
   - CI and governance reviewers verify compliance before merge.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed GeoJSON layout, naming, and CARE/provenance/CI requirements for Smoky Hill Cultural Drainage Region polygons; aligned with region data, STAC, metadata, and provenance standards. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Smoky Hill Region Data](../README.md) · [⬅ Back to Smoky Hill Cultural Drainage Region](../../README.md) · [⬅ Back to Cultural Landscape Regions](../../../README.md)

</div>
