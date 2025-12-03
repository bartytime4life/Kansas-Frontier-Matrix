---
title: "🌐 KFM v11.2.3 — Arkansas River Basin Region GeoJSON Geometries (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/data/geojson/README.md"
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
intent: "cultural-landscape-region-arkansas-river-basin-geojson"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🌐 **KFM — Arkansas River Basin Cultural Landscape Region · GeoJSON Geometries**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/data/geojson/README.md`

**Purpose:**  
Define and govern the **public GeoJSON geometry layer** for the **Arkansas River Basin Cultural Landscape Region**.  
This directory holds the **generalized polygon geometries** that:

- Power region-level STAC Items & Collections  
- Feed Neo4j graph loaders, ETL pipelines, and Focus Mode overlays  
- Drive MapLibre & Cesium basin-scale visualizations  
- Remain **FAIR+CARE-compliant**, **sovereignty-safe**, and **site-safe**

All geometries here are **derived** from more detailed internal sources and must never include raw or high-precision data.

</div>

---

## 📘 Overview

The GeoJSON files in this directory represent:

- The **primary Arkansas River Basin region boundary** (generalized polygon)  
- A **simplified outline** for small-scale / overview maps  
- An optional **mask geometry** for shading or clipping the basin interior  

They must:

- Use **EPSG:4326** (WGS84 lon/lat)  
- Be **topologically valid** and **generalized** (no site-level detail)  
- Align with the region spec (`../README.md`), region metadata, STAC, and provenance

Authoritative data contract for the parent region data directory lives at:

- `../README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/data/geojson/
├── 📄 README.md                                      # This file (GeoJSON layout & constraints)
├── 🌐 arkansas-river-basin-region.v1.geojson         # Primary generalized region polygon
├── 🌐 arkansas-river-basin-region.v1-simplified.geojson
│   # Extra-simplified outline for very small-scale / overview maps
└── 🌐 arkansas-river-basin-region.v1-mask.geojson    # Optional interior mask/clip polygon for rendering
~~~

**Naming contract:**

- `arkansas-river-basin-region.v<semver>.geojson` — primary region geometry per version  
- `arkansas-river-basin-region.v<semver>-simplified.geojson` — more aggressive simplification  
- `arkansas-river-basin-region.v<semver>-mask.geojson` — mask/clip geometry  

All filenames must:

- Use lowercase, dash-separated slugs  
- Encode the **region slug** (`arkansas-river-basin-region`) and **semantic version** (`v1`, `v2`, …)

---

## 🌍 GeoJSON Schema & CRS Requirements

All `.geojson` files in this directory must:

- Be valid **GeoJSON** (`Feature` or `FeatureCollection`)  
- Use **Polygon** or **MultiPolygon** geometries only  
- Use **EPSG:4326** (WGS84 lon/lat) coordinates  
- Avoid:

  - Multi-geometry mixes (e.g., Points + Polygons)  
  - Invalid polygons (self-intersections, bow-ties, etc.)  
  - Excessive vertex density that suggests hidden high-precision data

Recommended pattern:

- A single `FeatureCollection` with one `Feature` for the region polygon  
- Or a small set of features where justified (e.g., discontiguous sub-polygons)

---

## 🧾 Required Properties (Per Feature)

Each region feature in these files must include, at minimum:

- `kfm:region_slug = "arkansas-river-basin-region"`  
- `kfm:region_kind = "drainage"` (and optionally `"eco-cultural"`)  
- `kfm:version = "v1"` (or appropriate version)  

Optional convenience properties (canonical values live in STAC/metadata):

- `kfm:culture_phase` — summary of cultural phases (canonical in STAC).  
- `kfm:source_label` — short label for upstream synthesis (if helpful).  

**Do not** embed:

- Site IDs, sensitive labels, or direct references to confidential datasets.  
- Detailed attributes better handled in STAC, DCAT, or the graph.

---

## 🧮 File-Specific Contracts

### 1️⃣ `arkansas-river-basin-region.v1.geojson` (Primary)

- Represents the **canonical generalized polygon** for the region.  
- Must be:

  - The default geometry used in STAC Items.  
  - Sufficiently generalized to avoid site-level inference.  
  - In sync with STAC `bbox` and region metadata spatial descriptors.

Use for:

- Most map overlays at regional zoom levels.  
- Graph ingestion as the basin’s geometry.

### 2️⃣ `arkansas-river-basin-region.v1-simplified.geojson` (Simplified)

- More aggressively simplified geometry for:

  - Very small-scale maps (e.g., state overview, national scope).  
  - Situations where visual clarity matters more than geometric fidelity.

Constraints:

- Must remain a **generalization of** the primary polygon (never more detailed).  
- May drop small features or bends, but must preserve high-level basin form.  
- If referenced in STAC Items, changes require updated provenance.

### 3️⃣ `arkansas-river-basin-region.v1-mask.geojson` (Mask)

- Used as a **rendering or analysis mask**, for example:

  - Shading the basin interior.  
  - Clipping other layers to the basin region.

Constraints:

- Must not introduce more detailed boundaries than the primary polygon.  
- Can be a copy or buffered variant of the primary polygon, but always at the same abstraction level.  
- Any buffering or transformation must be documented in provenance.

---

## ⚖ CARE, Sovereignty & Sensitivity

All geometries here must respect CARE and sovereignty constraints for the Arkansas River Basin:

- **Forbidden** in this directory:

  - Geometries that allow recovery of precise site clusters or sacred/ceremonial areas.  
  - Encoded boundaries that are not approved for public representation.  
  - Nearly exact copies of internal confidential maps, even if nominally “generalized”.

- Effective precision must match:

  - `care:sensitivity` and `care:visibility_rules` in region metadata, STAC, and provenance.  
  - E.g., where `"h3-only"` is mandated, these polygon geometries may still exist here but **must not** be exposed in specific UIs.

Any change that tightens geometry around internal data **must** go through:

- FAIR+CARE review  
- Sovereignty/tribal review where applicable  
- Provenance updates documenting rationale and process

---

## 🧬 Provenance, STAC & Metadata Linkage

Each file in this directory must be:

- Referenced from at least one STAC Item in:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/stac/items/`
- Linked via `assets.data.href` (and/or related assets) in those Items.  
- Covered by a PROV-O provenance log under:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `arkansas-river-basin-region-v1.json`).

Provenance must record:

- The specific **output paths** for these files.  
- The **generalization algorithms** and parameters used.  
- Review activities and agents.

Region metadata JSON-LD must:

- Refer to these geometries indirectly via STAC and provenance links.  
- Stay in sync with versioning and region slug.

---

## 🧪 Validation & CI/CD

GeoJSON files in this directory are **CI-enforced**:

### Geometry & Schema Checks

- GeoJSON schema validation (proper Feature/FeatureCollection).  
- Topology checks (valid polygons, no self-intersections).  
- Coordinate sanity checks (within lat/lon bounds, no NaNs, etc.).

### Cross-Link Checks

- Every file must appear as an asset in at least one STAC Item.  
- STAC Items must pass:

  - STAC schema validation  
  - Region metadata cross-checks  
  - Provenance linkage validation  

### Governance & CARE Checks

- CARE fields in metadata/provenance must be compatible with the level of abstraction in these geometries.  
- CI must **block**:

  - Introduction of new geometries that appear more precise than allowed.  
  - Removal/renaming of files without corresponding STAC/provenance updates.  
  - Any regression flagged by FAIR+CARE or sovereignty audits.

---

## 🧭 Authoring & Update Workflow

When modifying files in this directory:

1. **Work from internal, non-public sources**  
   - Never treat these GeoJSON files as authoritative editing sources for raw data.

2. **Generate or update generalized geometries**  
   - Apply simplification, buffering, and clipping as appropriate.  
   - Record parameters for provenance (`kfm:steps`).

3. **Update STAC & Metadata**  
   - Ensure STAC Items reference the correct filenames and versions.  
   - Confirm region metadata still aligns with spatial coverage.

4. **Update Provenance**  
   - Bump or append provenance logs documenting geometry changes and reviews.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-arkansas-geojson`) to run geometry, STAC, and CARE checks.

6. **Submit PR & Address Feedback**  
   - CI and governance reviewers verify compliance before merge.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed GeoJSON layout, file naming, and CARE/provenance/CI requirements for Arkansas River Basin region polygons; aligned with region data, STAC, metadata, and provenance standards. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Arkansas River Basin Region Data](../README.md) · [⬅ Back to Arkansas River Basin Region](../../README.md) · [⬅ Back to Cultural Landscape Regions](../../..//README.md)

</div>
