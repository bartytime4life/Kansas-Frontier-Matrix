---
title: "📐🛡️ KFM v11.2.4 — CRS & Geoprivacy Masking Integration Guide"
path: "docs/standards/geospatial/crs-topology/geoprivacy-masking/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Spatial Governance Board · Tribal Sovereignty Board"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x privacy-contract compatible"
status: "Active / Enforced"

doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "geospatial-crs-topology"
  applies_to:
    - "ingest"
    - "etl"
    - "analysis"
    - "geoprivacy-masking"
    - "stac"
    - "dcat"
    - "graph"
    - "tiling"
    - "api"
    - "frontend"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask & zoom-governance rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.4/geoprivacy-crs-topology-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/geoprivacy/v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

ttl_policy: "24 months"
sunset_policy: "Aligned with geoprivacy-masking & CRS/topology standards v11.2.4"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "GeoSPARQL 1.1"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/geospatial/geoprivacy-masking/README.md@v11.2.4"
  - "docs/standards/geospatial/crs-topology/README.md@v11.2.4"
  - "docs/standards/geospatial/geoprivacy-masking/examples/README.md@v11.2.4"

provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/geoprivacy-crs-topology-integration-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/geoprivacy-crs-topology-integration-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:crs-topology-geoprivacy-masking-v11.2.4"
semantic_document_id: "kfm-doc-crs-topology-geoprivacy-masking-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geospatial:crs-topology:geoprivacy-masking"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "📘 Overview"
    - "🧭 Context"
    - "🧱 Architecture"
    - "🗺️ Diagrams"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧪 Validation & CI/CD"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_crs_geoprivacy_rules_v10.4"
---

<div align="center">

# 📐🛡️ KFM v11.2.4 — CRS & Geoprivacy Masking Integration Guide  
CRS-Safe Donut Masking · Topology-Aware Privacy · GeoSPARQL / STAC / PROV-Aligned  

`docs/standards/geospatial/crs-topology/geoprivacy-masking/README.md`

**Purpose:**  
Define the **CRS and topology rules specific to geoprivacy masking** in the Kansas Frontier Matrix (KFM). This guide explains **where and how** the deterministic donut geomasking standard must run in CRS space, how masked geometries interact with topology cleaning and zoom governance, and how these operations are cataloged in STAC/DCAT, stored in Neo4j, and surfaced to Story Nodes and Focus Mode.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/
├── 📂 geoprivacy-masking/
│   └── 📄 README.md                           # 🛡 Geoprivacy & cultural-safety masking standard
├── 📂 tiling-resolution/
│   ├── 📄 README.md                           # 🧩 Tiling & zoom-level governance
│   └── 📄 examples.md                         # 📚 Tiling resolution examples
└── 📂 crs-topology/
    ├── 📄 README.md                           # 📐 CRS, geometry & topology governance standard
    └── 📂 geoprivacy-masking/
        └── 📄 README.md                       # 📐🛡 This guide: CRS/topology integration for masking
~~~

Related implementation and data locations (for reference):

~~~text
📂 src/pipelines/
├── 📂 ingest/
│   └── 📄 crs_normalization.py                # Detect & normalize source CRS → EPSG:4326
├── 📂 geometry/
│   ├── 📄 topology_cleaning.py                # Validity & topology fixes before/after masking
│   └── 📄 reprojection_ops.py                 # Shared reprojection utilities
└── 📂 masking/
    ├── 📄 donut_geomask.py                    # Deterministic donut geomasking implementation
    └── 📄 masking_runner.py                   # ETL step orchestrating CRS + masking

📂 tests/geoprivacy/
└── 📄 test_crs_topology_geoprivacy.py         # CI tests for CRS/topology compliance in masking
~~~

Author rules:

- This guide is **integration-focused** and does not redefine masking math or CRS policy; it **binds**:
  - 🛡 Geoprivacy Masking Standard  
  - 📐 CRS & Topology Standard  
  - 🧩 Tiling Resolution Standard  
- Any masking-related CRS or topology change must reference both:
  - `../README.md` (CRS/topology standard) and  
  - `../../geoprivacy-masking/README.md` (masking standard).

---

## 📘 Overview

The KFM geoprivacy standard defines *what* masking is allowed (deterministic donut geomasking, radii per label, sacred generalization).  
The CRS/topology standard defines *how* geometries must be stored, transformed, and validated (EPSG:4326 storage, Web Mercator display, topology rules).

This guide stitches them together:

- Masking must be performed in **CRS-safe ways**:
  - On appropriate ellipsoidal coordinates.  
  - With defined geodesic offset methods.  
  - Without producing topologically-invalid or out-of-bounds geometries.

- Topology must remain **clean after masking**:
  - Masked points and generalized regions must not violate topology constraints.  
  - H3 or polygon generalization for sacred data must still respect CRS and adjacency rules.

- Catalogs, graph, and tiles must **agree on CRS and privacy semantics**:
  - STAC/DCAT `kfm:*` fields must indicate both geoprivacy masking and CRS choices.  
  - Neo4j graph geometry and GeoSPARQL predicates must operate on consistent CRS.  
  - Tiling resolution and zoom-gating must respect both geoprivacy and CRS rules.

In short: this document is the **joint contract** between geoprivacy masking and CRS/topology governance.

---

## 🧭 Context

From the two parent standards:

- Geoprivacy:  
  - Masking is deterministic donut geomasking, driven by `kfm:sensitivity_label`.  
  - Sacred data uses large radii + H3 generalization.  
  - Raw coordinates never leave vault contexts.

- CRS & topology:  
  - Authoritative storage CRS is EPSG:4326 (WGS84, lon/lat).  
  - Web display CRS is EPSG:3857; tiles must be consistent.  
  - All geometries must be topologically valid and CRS-explicit.

This integration guide answers:

1. **Where to run masking in CRS space**  
   (e.g., in WGS84 geodesic domain before tiling).  
2. **How masking interacts with topology cleaning**  
   (before, after, and in what order).  
3. **How to keep Story Nodes and Focus Mode spatially honest**  
   (no implied precision beyond masked + generalized CRS).

---

## 🧱 Architecture

### 1. CRS order for masking ETL

The **normative sequence** for any dataset subject to geoprivacy masking:

1. **Source ingest & CRS detection**

   - Ingest in source CRS (e.g., EPSG:26914, state plane, etc.).  
   - Detect and validate source CRS; reject or quarantine if unknown.

2. **Reproject to EPSG:4326 (storage CRS)**

   - Use shared reprojection utilities (`reprojection_ops.py`).  
   - Log PROV: `prov:Activity = crs_reprojection`, `prov:used = source CRS`, `prov:generated = epsg4326 copy`.

3. **Topology cleaning (pre-masking)**

   - Run topology cleaning on EPSG:4326 geometries:  
     - Snap small slivers.  
     - Ensure validity.  
   - For point-based datasets, this may be minimal (dedupe, validate domain).

4. **Deterministic donut masking (EPSG:4326 geodesic domain)**

   - Run donut masking on EPSG:4326 coordinates:
     - Use geodesic offset on WGS84 ellipsoid.  
     - Use `r_min`, `r_max` per label from masking standard.  
   - Ensure offset uses **geodesic** calculations, not planar approximations.

5. **Topology/policy checks (post-masking)**

   - Confirm masked locations are:
     - Within allowed spatial domain (e.g., Kansas or configured region).  
     - Non-overlapping with forbidden polygons (if applicable).  
   - Confirm sacred generalization rules apply (H3/polygon generation).

6. **Optional reprojection for tiling**

   - If generating tiles, reproject masked/generalized geometries into display CRS (EPSG:3857).  
   - This step must not reintroduce raw coordinates; only masked outputs are used.

At no point are raw coordinates re-derived from masked data; reprojections only change CRS, not privacy semantics.

### 2. Geometry & topology constraints for masked outputs

**Point-based masking:**

- Masked points (public/community/sensitive) must:

  - Remain valid EPSG:4326 coordinates (within latitude/longitude bounds).  
  - Respect domain filters (within Kansas or configured bounding region).  
  - Not be snapped or cleaned in ways that reduce privacy (e.g., snapping to parcel corners).

- Topology cleaning **after** masking for points is limited to:

  - Removing exact duplicates if masking creates collisions.  
  - Optional small random selection if duplicates must be preserved as counts (documented carefully).

**Sacred regions (H3/polygons):**

- Geometry pipeline:

  1. Start from raw sacred points in EPSG:4326 (vault only).  
  2. Apply donut masking (EPSG:4326 geodesic).  
  3. Aggregate masked points into H3 cells or generalized polygons.  
  4. Clean and validate aggregated polygons per topology rules.  

- Sacred outputs must:

  - Be valid `Polygon` or `MultiPolygon` geometries in EPSG:4326.  
  - Have consistent ring orientation (CCW exterior, CW interior).  
  - Not leak original site locations (cells/polygons must be coarse enough; enforced in geoprivacy standard).

### 3. CRS and topology in Neo4j & GeoSPARQL

When masked geometries enter Neo4j:

- Node properties:

  - `geom`: Geometry in EPSG:4326 (masked or generalized).  
  - `crs`: `"EPSG:4326"`.  
  - `kfm:sensitivity_label`, `kfm:privacy_method`, `kfm:masking_run_id`.

- Graph relationships:

  - `:LOCATED_IN`, `:OVERLAPS_REGION`, etc. must be computed using GeoSPARQL predicates on **masked** geometries only.  
  - No graph operation may reference raw coordinates once masking is applied.

Topology invariants:

- A masked site `S` inside a county `C` must be:

  - `sfWithin(S_geom, C_geom)` true within tolerance.  
  - `(:Site)-[:LOCATED_IN]->(:County)` relationship consistent with masked geometry.

Any mismatch between geometry predicates and graph relationships is a **CI error**; CRS or topology integration must be fixed.

---

## 🗺️ Diagrams

### CRS & masking integration flow

~~~mermaid
flowchart LR
    A[Raw Geometry (various CRS)] --> B[CRS Normalization to EPSG:4326]
    B --> C[Topology Cleaning (pre-masking)]
    C --> D[Donut Masking (EPSG:4326 geodesic)]
    D --> E[Topology Checks (post-masking)]
    E --> F[H3/Polygon Generalization (for sacred)]
    F --> G[STAC/DCAT + Neo4j (masked CRS)]
    G --> H[Tiles & APIs (EPSG:3857)]
    H --> I[Story Nodes & Focus Mode]
~~~

---

## 📦 Data & Metadata

This guide refines how CRS & masking-related fields should appear together.

### 1. Masked feature properties (GeoJSON / STAC)

Minimum combined fields:

~~~json
{
  "kfm:privacy_method": "donut_geomask_v1",
  "kfm:sensitivity_label": "sensitive",
  "kfm:r_min_m": 1000,
  "kfm:r_max_m": 3000,
  "kfm:masking_run_id": "urn:kfm:etl-run:2025-12-06T00:00Z",
  "kfm:prov_ref": "prov/masking_run_2025-12-06.jsonld",
  "kfm:storage_crs": "EPSG:4326",
  "kfm:display_crs": "EPSG:3857",
  "kfm:source_crs": ["EPSG:26914"],
  "kfm:crs_transform_ref": "prov/crs_reprojection_run_2025-12-06.jsonld"
}
~~~

For sacred/generalized layers, add:

- `kfm:access_label`: `"tribal-only"` / `"restricted"` / `"withheld"`.  
- `kfm:sovereignty_label`: Tribal/community space.  
- `kfm:topology_clean_profile`: ID of topology rules used on generalized polygons.

### 2. Integration with H3 / grid systems

If H3 or similar indexing is used:

- `kfm:h3_resolution`: e.g., `8`.  
- `kfm:h3_crs`: `"EPSG:4326"` (H3 indexing is defined over WGS84).  

Vectorized H3 polygons must still:

- Conform to EPSG:4326 storage.  
- Pass topology validity checks.  

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For Items/Collections generated from masked geometries:

- CRS is implicitly WGS84 (GeoJSON) but KFM-specific CRS/masking fields provide explicit context.  
- Recommended `properties` snippet:

~~~json
{
  "kfm:privacy_method": "donut_geomask_v1",
  "kfm:sensitivity_label": "sacred",
  "kfm:storage_crs": "EPSG:4326",
  "kfm:display_crs": "EPSG:3857",
  "kfm:tiling_category": "sacred",
  "kfm:h3_resolution": 8
}
~~~

### DCAT

DCAT records for masked datasets should:

- Use `dct:spatial` referencing WGS84-conformant geometry.  
- Include `kfm:storage_crs`, `kfm:display_crs`, and `kfm:privacy_method` in custom extensions.  
- Reference both:

  - CRS/topology standard (`kfm-doc-crs-topology-v11.2.4`), and  
  - Geoprivacy masking standard (`kfm-doc-geoprivacy-masking-v11.2.4`).

### PROV

A single masking + CRS integration run may be represented as:

- `prov:Activity` with:

  - Inputs: raw dataset, source CRS.  
  - Outputs: masked EPSG:4326 geometries, optionally tiled EPSG:3857 services.

- `prov:Entity` for each geometry version:

  - `raw_epsg26914`, `clean_epsg4326`, `masked_epsg4326`, `generalized_h3_polygons`.

The `kfm:prov_ref` on features must point at bundles that record:

- CRS transform steps.  
- Masking steps.  
- Topology cleaning steps.  

---

## 🧪 Validation & CI/CD

This guide adds CRS/topology checks specific to masking. In addition to the tests defined in:

- `geoprivacy-masking` CI scenarios, and  
- `crs-topology` tests,

we require:

1. **Masking CRS tests**

   - Confirm masking is run on EPSG:4326 geometries (not on pre-normalization CRS).  
   - Assert all masked outputs have `kfm:storage_crs = "EPSG:4326"`.

2. **Geodesic offset correctness**

   - Unit tests verifying that donut masking uses geodesic offsets:
     - Distances on the ellipsoid match target `r_min_m`/`r_max_m` within tolerance.  
   - No planar-approximation shortcuts allowed for production runs.

3. **Topology validity of masked outputs**

   - For sacred generalized geometries, run `IsValid` checks and area sanity tests.  
   - For point-based masked data, confirm no coordinates fall outside allowed bounding regions.

4. **CRS + masking provenance consistency**

   - Check that each `kfm:masking_run_id` referenced in masked features has a PROV bundle which:
     - References the CRS reprojection activity.  
     - Records both CRS and masking steps in order.

These tests should live in `tests/geoprivacy/test_crs_topology_geoprivacy.py` and be wired into `kfm-ci`.

---

## 🧠 Story Node & Focus Mode Integration

CRS + geoprivacy integration affects how narratives talk about place and precision:

- Story Nodes should:

  - Reference masked or generalized geometries in EPSG:4326.  
  - Clearly indicate **scale** instead of implying exact coordinates (especially for sacred/sensitive data).  

- Focus Mode must:

  - Convert user interactions (clicks, extents) from Web Mercator to EPSG:4326 **without attempting to reverse masking**.  
  - Respect zoom-governance from tiling standard; it must not offer zoom options beyond allowed bands.

Example Story Node metadata:

~~~json
{
  "target_layer_id": "kansas_sacred_regions_v1",
  "target_standard": "kfm-doc-geoprivacy-masking-v11.2.4",
  "crs": "EPSG:4326",
  "narrative_scale": "county-sub-basin",
  "privacy_method": "donut_geomask_v1 + H3_R8"
}
~~~

Narratives should focus on **patterns and relationships**, not exact masked coordinates.

---

## ⚖ FAIR+CARE & Governance

CRS/topology + geoprivacy integration is central to FAIR+CARE:

- **FAIR**
  - *Findable*: CRS and masking metadata make spatial behavior searchable and auditable.  
  - *Accessible*: consistent CRS across masked datasets eases visualization and analysis.  
  - *Interoperable*: GeoSPARQL, STAC, DCAT, and PROV alignment enable tooling reuse.  
  - *Reusable*: clear CRS + masking contracts reduce misinterpretation of sensitive data.

- **CARE & sovereignty**
  - Correct CRS and topology are vital when representing Tribal boundaries, cultural landscapes, and sacred regions.  
  - Distorted or misaligned CRS can shift sacred sites on the map, undermining sovereignty and trust.  
  - This guide ensures geoprivacy masking respects both **spatial accuracy** (within allowable abstraction) and **sovereign control**.

Governance expectations:

- Any change to:

  - Where masking happens in CRS space,  
  - How sacred generalization interacts with CRS/topology, or  
  - The approved geodesic offset method,

  must be reviewed by:

  - FAIR+CARE Council, and  
  - Tribal Sovereignty Board (where applicable),

  and must update:

  - This guide,  
  - The Geoprivacy Masking Standard, and  
  - The CRS & Topology Standard.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                               |
|-----------:|------------|-------------------|---------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Initial CRS + geoprivacy masking integration guide; defines where masking runs in CRS space and topology constraints. |

Future updates should:

- Track changes to the geoprivacy masking or CRS/topology standards.  
- Add concrete CI snippets and schema examples as implementation matures.  
- Document any new grid systems (beyond H3) used for sacred or sensitive generalization.

---

<div align="center">

📐🛡️ **KFM v11.2.4 — CRS & Geoprivacy Masking Integration Guide**  
CRS-Safe Donut Masking · Clean Topology · FAIR+CARE Sovereignty  

[📘 Docs Root](../../../../..) · [📐 CRS & Topology Standard](../README.md) · [🛡 Geoprivacy Masking Standard](../../geoprivacy-masking/README.md) · [🧩 Tiling Resolution Standard](../../tiling-resolution/README.md) · [⚖ Governance](../../../governance/ROOT-GOVERNANCE.md)

</div>

