---
title: "🧪 Kansas Frontier Matrix — Geospatial Test Fixtures Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/tests/fixtures/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-pipelines-geospatial-fixtures-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Fixtures Overview"
intent: "geospatial-fixtures"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed depending on dataset"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Low to moderate"
indigenous_rights_flag: "Conditional (if sovereignty data present)"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false
provenance_chain:
  - "web/src/pipelines/geospatial/tests/fixtures/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../../schemas/json/web-pipelines-geospatial-fixtures.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/web-pipelines-geospatial-fixtures-shape.ttl"
doc_uuid: "urn:kfm:doc:web-pipelines-geospatial-fixtures-v10.4.0"
semantic_document_id: "kfm-doc-web-pipelines-geospatial-fixtures"
event_source_id: "ledger:web/src/pipelines/geospatial/tests/fixtures/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden"
ai_transform_permissions:
  - "semantic-highlighting"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public / Test-only"
role: "fixtures-overview"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next fixture restructuring"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Geospatial Pipeline Fixtures Overview**  
`web/src/pipelines/geospatial/tests/fixtures/README.md`

**Purpose:**  
Document the **fixtures** used by the geospatial test suite — ensuring all spatial test data is synthetic,
non-sensitive, provenance-logged, CARE-compliant, and stable for deterministic testing of geospatial pipelines  
(loadFootprints, masking, CRS normalization, temporal filters, and spatial telemetry).

</div>

---

# 📘 Overview

Fixtures are the **ground truth** datasets used in KFM’s geospatial pipeline tests.  
They must be:

- **Deterministic**  
- **Fully synthetic or heavily generalized**  
- **Non-sensitive**  
- **FAIR+CARE-compliant**  
- **Version-pinned**  
- **Provenance-documented**  
- **Stable across releases**  

These fixtures simulate:

- STAC footprints  
- Story Node v3 geometry  
- Temporal ranges  
- Masking/redaction logic  
- CRS normalization cases  
- Timeline → Map → Focus Mode interactions  
- Telemetry emission triggers  

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/tests/fixtures/
├── README.md                         # This fixture documentation
│
├── footprints/                       # Synthetic and sanitized footprints
│   ├── stac_item.json                # Mock STAC item with bbox + geometry
│   ├── footprint.geojson             # Minimal GeoJSON polygon
│   └── multi_footprint.geojson       # MultiPolygon example
│
├── temporal/                         # Time-ranged spatial objects
│   ├── temporal_feature_1850_1900.geojson
│   ├── temporal_feature_1900_1950.geojson
│   └── fuzzy_temporal_case.geojson   # Start/end uncertainty
│
├── masking/                          # CARE + sovereignty redaction cases
│   ├── sensitive_site_input.geojson  # Synthetic sensitive location
│   ├── sensitive_site_h3_mask.json   # Expected H3 r7 output
│   └── blur_mask_example.geojson     # Alternative masking example
│
├── geometry/                         # CRS + topology fixtures
│   ├── epsg_3857.geojson             # Needs normalization to EPSG:4326
│   ├── topojson_example.json         # Simplification + conversion case
│   ├── invalid_geometry_case.geojson # Self-intersecting polygon (error case)
│   └── simplified.geojson            # Expected simplified output
│
└── storynodes/                       # Story Node v3 spatial fixtures
    ├── storynode_01.geojson          # Narrative-linked footprint
    ├── storynode_02.geojson          # Multi-temporal overlay
    └── storynode_cluster.json        # Grouped features for cluster tests
~~~

---

# 🔐 Provenance & CARE Requirements

Fixtures MUST:

- Be **synthetic**, **heavily simplified**, or **H3-generalized**  
- Never include real sensitive coordinates  
- Include metadata fields:
  - `"source": "synthetic-fixture"`  
  - `"license": "MIT"`  
  - `"provenance": "test-fixture-generated"`  
  - `"care_class": "Public / Synthetic"`  

If testing masking logic, the **input** may simulate cultural/sensitive geometry but MUST NOT be real.

All masking outputs must log:

- H3 resolution  
- Masking style (coarse hex, blur, centroid removal)  
- CARE justification  

---

# 🧩 Fixture Categories & Their Purposes

## 1. Footprint Fixtures
Used to test:

- STAC item parsing  
- GeoJSON geometry loading  
- CRS normalization  
- Bounding box filtering  
- Multipolygon handling  

## 2. Temporal Fixtures
Used to test:

- Timeline → geometry syncing  
- OWL-Time alignment  
- Fuzzy intervals  
- Combined map + temporal filtering  

## 3. Masking Fixtures
Used to test:

- CARE-compliant masking  
- Sovereignty boundaries  
- H3 generalization  
- Restricted coordinate handling  

## 4. Geometry Fixtures
Used to test:

- Invalid geometry rejection  
- CRS → EPSG:4326 workflows  
- TopoJSON conversion  
- Simplification behavior  

## 5. Story Node Fixtures
Used to test:

- Story Node v3 spatial associations  
- Geometry merging (`mergeLayersForMap.ts`)  
- Focus Mode → spatial highlight behavior  
- Temporal + spatial blending  

---

# 🧪 Testing Methodology Using Fixtures

### Each fixture must support tests in:

- `loadFootprints.test.ts`  
- `temporalFilters.test.ts`  
- `masking.test.ts`  
- `geometryTransform.test.ts`  
- `mergeLayers.test.ts`  
- `spatial_telemetry.test.ts`  

### Fixtures must validate:

- CRS correctness  
- Geometry integrity  
- CARE masking  
- Temporal range correctness  
- Schema validity (Story Node, STAC, telemetry)  

---

# 📈 Telemetry Expectations

Fixtures trigger deterministic telemetry events such as:

- `"spatial:pan"`  
- `"spatial:zoom"`  
- `"spatial:layer-toggle"`  
- `"spatial:masking-applied"`  
- `"storynode:geometry-hover"`  

All telemetry must:

- Be non-PII  
- Match defined schemas  
- Align with sustainability + governance goals  

---

# 🔒 Security & Privacy Notes

Fixtures **must not** contain:

- PII  
- Real cultural or sacred coordinates  
- Proprietary data  
- Licensed imagery or shapes from restricted datasets  

All geographical shapes must be:

- Synthetic or  
- Derived from real datasets but generalized past safe thresholds (H3 r7+).  

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full fixture documentation for geospatial testing aligned with KFM-MDP v10.4 |
| v10.3.2 | 2025-11-14 | Added masking and spatial telemetry fixtures |
| v10.3.1 | 2025-11-13 | Initial fixture setup |
---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Test Document · Version-Pinned  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  

</div>