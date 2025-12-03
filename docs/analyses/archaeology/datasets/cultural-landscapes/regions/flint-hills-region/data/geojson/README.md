---
title: "🌐 KFM v11.2.3 — Flint Hills Eco-Cultural Region GeoJSON Geometries (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/data/geojson/README.md"
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
intent: "cultural-landscape-region-flint-hills-geojson"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🌐 **KFM — Flint Hills Eco-Cultural Landscape Region · GeoJSON Geometries**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/data/geojson/README.md`

**Purpose:**  
Define and govern the **public GeoJSON geometry layer** for the **Flint Hills Eco-Cultural Landscape Region**.  
This directory holds the **generalized eco-cultural polygons** that:

- Power Flint Hills region STAC Items & Collections  
- Feed Neo4j graph loaders, ETL pipelines, and Focus Mode overlays  
- Drive MapLibre & Cesium visualizations of the tallgrass / chert-rich band  
- Remain **FAIR+CARE-compliant**, **sovereignty-safe**, and **site-safe**

All geometries here are **derived** from more detailed internal sources and must never include raw or high-precision data.

</div>

---

## 📘 Overview

The GeoJSON files in this directory represent:

- The **primary Flint Hills eco-cultural region boundary** (generalized polygon)  
- A **simplified outline** for very small-scale / overview maps  
- An optional **mask geometry** for shading or clipping the eco-cultural band  

They must:

- Use **EPSG:4326** (WGS84 lon/lat)  
- Be **topologically valid** and **generalized** (no site-level detail; no quarry/site outlines)  
- Align with the region spec, region metadata, STAC, and provenance:

  - Region spec: `../README.md`  
  - Region metadata: `../metadata/dcat-flint-hills-region-v1.jsonld`  
  - STAC: `../../stac/`  
  - Provenance: `../../../provenance/` and global `../../../../provenance/`

The authoritative data contract for the parent `data/` directory is defined at:

- `../README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/data/geojson/
├── 📄 README.md                               # This file (GeoJSON layout & constraints)
├── 🌐 flint-hills-region.v1.geojson           # Primary generalized eco-cultural region polygon
├── 🌐 flint-hills-region.v1-simplified.geojson
│   # Extra-simplified outline for very small-scale / overview maps
└── 🌐 flint-hills-region.v1-mask.geojson      # Optional interior mask/clip polygon for rendering the eco-cultural band
~~~

**Naming contract:**

- `flint-hills-region.v<semver>.geojson` — primary region geometry per version  
- `flint-hills-region.v<semver>-simplified.geojson` — more aggressive simplification  
- `flint-hills-region.v<semver>-mask.geojson` — mask/clip geometry  

All filenames must:

- Use lowercase, dash-separated slugs  
- Encode the **region slug** (`flint-hills-region`) and **semantic version** (`v1`, `v2`, …)

---

## 🌍 GeoJSON Schema & CRS Requirements

All `.geojson` files in this directory must:

- Be valid **GeoJSON** (`Feature` or `FeatureCollection`)  
- Use **Polygon** or **MultiPolygon** geometries only  
- Use **EPSG:4326** (WGS84 lon/lat) coordinates  
- Avoid:

  - Mixed geometry types in the same file (e.g., Points + Polygons)  
  - Invalid polygons (self-intersections, bow-ties, slivers)  
  - Excessive vertex density that implies hidden high-precision data

Recommended pattern:

- A single `FeatureCollection` with one `Feature` for the region polygon  
- Or a small set of features where the eco-cultural band is discontiguous

---

## 🧾 Required Properties (Per Feature)

Each region feature in these files must include, at minimum:

- `kfm:region_slug = "flint-hills-region"`  
- `kfm:region_kind = "eco-cultural"`  
- `kfm:version = "v1"` (or the appropriate version tag)  

Optional convenience properties (canonical values live in STAC/metadata):

- `kfm:culture_phase` — summary of cultural phases (e.g., `["Woodland","Late Prehistoric","Protohistoric"]`)  
- `kfm:source_label` — short label for upstream synthesis (“eco-region + geology + survey synthesis”)  

**Do not** embed:

- Site IDs or survey IDs  
- Lithic quarry coordinates or names  
- Any sensitive label better handled via provenance or internal-only datasets

---

## 🧮 File-Specific Contracts

### 1️⃣ `flint-hills-region.v1.geojson` (Primary)

Represents the **canonical generalized eco-cultural polygon** for the Flint Hills region.

Requirements:

- Default geometry used in STAC Items as the main polygon asset.  
- Sufficiently generalized to avoid site-level inference or quarry exposure.  
- In sync with:
  - STAC `bbox` and spatial extent  
  - Region metadata spatial descriptors (eco-region names, general extent)  
  - Provenance descriptions of generalization steps

Used for:

- Most region overlays at appropriate map zoom levels.  
- Graph ingestion as the Flint Hills eco-cultural geometry.

---

### 2️⃣ `flint-hills-region.v1-simplified.geojson` (Simplified)

More aggressively simplified geometry for **small-scale / overview** contexts.

Constraints:

- Must remain a **generalization of** the primary polygon (never more detailed).  
- May drop minor features or bends but must preserve the high-level band form.  
- If referenced in STAC Items, changes require:
  - Updated provenance documenting simplification  
  - Consistency checks with metadata and CARE policies

Used for:

- High-level Kansas / Plains overviews  
- Low-detail basemaps where visual clarity is prioritized

---

### 3️⃣ `flint-hills-region.v1-mask.geojson` (Mask)

Used as a **rendering or analysis mask**, for example:

- Shading the eco-cultural band  
- Clipping other layers (e.g., climate, vegetation, Story Node overlays) to the Flint Hills extent

Constraints:

- Must not be more detailed than the primary polygon.  
- May be:
  - A copy of the primary polygon, or  
  - A buffered / eroded variant at the same abstraction level  
- Any buffering or transformation must be documented in PROV-O provenance.

---

## ⚖ CARE, Sovereignty & Sensitivity

All geometries here must respect CARE and sovereignty constraints, especially around:

- **Lithic provisioning zones** (chert-bearing formations)  
- **Settlement pattern inference** in the Flint Hills uplands and escarpments  
- **Traditional land use and culturally important places**

**Forbidden** in this directory:

- Geometries that allow reverse-engineering of precise quarry or site locations.  
- Encoded boundaries that could be mistaken for sovereign, legal, or contested cultural claims.  
- Nearly exact copies of confidential eco-cultural maps.

Effective precision must align with:

- `care:sensitivity` and `care:visibility_rules` in:
  - Region metadata (`../metadata/dcat-flint-hills-region-v1.jsonld`)  
  - STAC Collections/Items (`../../stac/`)  
  - PROV-O logs (`../../../provenance/` and `../../../../provenance/`)

Examples:

- `"polygon-generalized"` → these polygons may be shown at moderate/regional zooms.  
- `"h3-only"` → polygons may still exist here for internal use, but UIs must render only H3 mosaics.

Any change that tightens geometries around internal data is a **governance event** and may require **tribal/sovereign review**.

---

## 🧬 Provenance, STAC & Metadata Linkage

Each file in this directory must be:

- Referenced by at least one STAC Item under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/items/`  
  via assets such as `assets.data.href`.

- Covered by a canonical PROV-O provenance log under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `flint-hills-region-v1.json`).

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
  - Valid polygons / multipolygons  
  - No self-intersections or invalid rings  
- Coordinate sanity checks (no NaNs, within lat/lon ranges).

### Cross-Link Checks

- Every file must appear as an asset in at least one STAC Item.  
- Corresponding STAC Items must pass:
  - STAC schema validation  
  - Region metadata cross-checks  
  - Provenance linkage validation  

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
   - Derive generalized outputs from internal eco-cultural and archaeological data.  
   - Never treat these public GeoJSON files as authoritative raw data.

2. **Generate or update generalized geometries**  
   - Apply governed simplification, buffering, clipping, and quality checks.  
   - Capture all parameters for PROV-O (`kfm:steps`).

3. **Update STAC & Metadata**  
   - Ensure STAC Items reference correct filenames and versions.  
   - Confirm spatial coverage in metadata remains accurate and consistent.

4. **Update Provenance**  
   - Bump or append PROV-O provenance log version(s) for `flint-hills-region`.  
   - Ensure CARE fields and governance notes reflect any changes.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-flint-hills-geojson`) for geometry, STAC, and CARE checks.

6. **Submit PR & Address Feedback**  
   - CI and governance reviewers verify compliance before merge.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed GeoJSON layout, naming, and CARE/provenance/CI requirements for Flint Hills Eco-Cultural Region polygons; aligned with region data, STAC, metadata, and provenance standards. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Flint Hills Region Data](../README.md) · [⬅ Back to Flint Hills Eco-Cultural Region](../../README.md) · [⬅ Back to Cultural Landscape Regions](../../../README.md)

</div>
