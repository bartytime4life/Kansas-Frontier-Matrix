---
title: "🗺️ Kansas Frontier Matrix — Geospatial Pipeline Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-pipelines-geospatial-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-pipelines-geospatial"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (Unless dataset requires masking)"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Dataset-dependent"
indigenous_rights_flag: "Conditional for sovereignty datasets"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false
provenance_chain:
  - "web/src/pipelines/geospatial/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../schemas/json/web-pipelines-geospatial-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-pipelines-geospatial-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-pipelines-geospatial-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-pipelines-geospatial-readme"
event_source_id: "ledger:web/src/pipelines/geospatial/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public (unless dataset declares CARE restrictions)"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next geospatial pipeline redesign"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Geospatial Pipeline Overview**  
`web/src/pipelines/geospatial/README.md`

**Purpose:**  
Describe the **geospatial orchestration pipelines** that power the map, spatial reasoning, footprints, temporal filtering,  
and governance-aware masking layers of the Kansas Frontier Matrix (KFM) Web Platform.  
These pipelines ensure that **all geospatial data entering the UI is validated, FAIR+CARE-compliant, provenance-aligned,  
and synchronized** with the timeline, Focus Mode, and Story Node v3 systems.

</div>

---

# 📘 Overview

The **Geospatial Pipeline** is responsible for:

- Loading, validating, and transforming geospatial datasets  
- Integrating STAC/DCAT dataset footprints  
- Synchronizing spatial data with **timeline ranges**  
- Applying H3-based masking for CARE & sovereignty constraints  
- Preparing geometry for **MapLibre**, **Cesium**, and **Focus Mode**  
- Performing temporal slicing of vector & raster layers  
- Preparing data for Story Node v3 overlays  
- Ensuring spatial data integrity (CRS, geometry validity)  
- Emitting telemetry for spatial interactions

This layer sits between:

- UI components (MapView, StoryNodeView, FocusPanel)  
- Services (`stacService.ts`, `apiClient.ts`, `governanceService.ts`)  
- Contexts (`TimeContext`, `FocusContext`)  

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/
├── loadFootprints.ts            # Load + schema-validate footprints (vector + raster)
├── applyTemporalFilters.ts      # Apply time-window filtering to spatial layers
├── maskSensitiveGeometry.ts     # CARE + sovereignty masking (H3)
├── geometryTransform.ts         # CRS normalization + TopoJSON/GeoJSON transforms
├── mergeLayersForMap.ts         # Merge STAC + vector + Story Node geometry for MapLibre
└── spatialTelemetry.ts          # Map + layer → telemetry (pan, zoom, feature interaction)
~~~

---

# 🧩 Geospatial Pipeline Stages

## 1. **Footprint Loading (`loadFootprints.ts`)**

Responsibilities:

- Load footprints from:
  - STAC Items & Collections  
  - Processed GeoJSON & TopoJSON  
  - Story Node v3 geometry bundles  
- Validate:
  - CRS  
  - Geometry validity  
  - Temporal extent  
  - License & provenance metadata  
- Normalize shapes for MapLibre & Cesium  

Guarantees:

- No malformed geometries enter the UI  
- All geometry is CRS-normalized before rendering  

---

## 2. **Temporal Filtering (`applyTemporalFilters.ts`)**

Responsibilities:

- Apply timeline window constraints to geospatial features  
- Filter:
  - Story Nodes  
  - STAC Items  
  - Event layers  
  - Archaeological or environmental layers  
- Align with **OWL-Time** semantics  
- Handle fuzzy temporal intervals

Guarantees:

- Only time-relevant features render  
- Timeline → Map → FocusMode always synchronized  

---

## 3. **CARE & Sovereignty Masking (`maskSensitiveGeometry.ts`)**

Responsibilities:

- H3 r7+ masking of cultural, sacred, or sovereignty-controlled sites  
- Spatial redaction depending on:
  - CARE classification  
  - Sovereignty domain  
  - Dataset governance metadata  
- Produce UI-friendly masking indicators (blur, coarse-grain hex cells)

Guarantees:

- No sensitive coordinates exposed  
- Ethical rendering preserved  
- Masking metadata is provided to the UI for proper labeling  

---

## 4. **Geometry Transforms (`geometryTransform.ts`)**

Responsibilities:

- CRS normalization → EPSG:4326  
- Optional local projection transforms  
- Conversion between:
  - GeoJSON ⇄ TopoJSON  
  - COG footprints → polygon approximations  
- Geometry simplification for performance  
- 2D & 3D geometry preparation for:
  - MapLibre  
  - Cesium  

Guarantees:

- Stable rendering  
- Predictable geometry performance  
- Accurate alignment with basemaps + terrain  

---

## 5. **Layer Merging (`mergeLayersForMap.ts`)**

Responsibilities:

- Combine inputs into a unified map data flow:
  - STAC footprints  
  - Story Node geometry  
  - Governance overlays  
  - Time-filtered vector layers  
  - Focus Mode highlights  
- Produce UI-ready map layers with metadata:
  - license  
  - provenance  
  - CARE flags  
  - temporal range  

Guarantees:

- Map reflects accurate, ethical, filtered view of all data  
- No mixing of incompatible geometries  
- Governance metadata retained  

---

## 6. **Spatial Telemetry (`spatialTelemetry.ts`)**

Tracks:

- Pan / zoom / rotate  
- Layer toggles  
- Footprint loading events  
- Story Node geometry interactions  
- Focus Mode spatial activity  
- Rendering performance (ms per frame; scene complexity)

Outputs written into:

`releases/<version>/focus-telemetry.json`

Guarantees:

- No PII  
- Aggregated usage metrics only  
- Used for sustainability + UX improvement  

---

# 🔧 Example Pipeline Flow (Conceptual)

~~~text
User Interacts with Map
       │
       ▼
loadFootprints.ts
       │
       ▼
applyTemporalFilters.ts
       │
       ▼
maskSensitiveGeometry.ts   (CARE enforcement)
       │
       ▼
geometryTransform.ts        (CRS + shape normalization)
       │
       ▼
mergeLayersForMap.ts        (Unified map pipeline)
       │
       ├──► MapLibre render
       └──► Cesium render
       │
       ▼
spatialTelemetry.ts         (Observability + audit)
~~~

---

# 🧪 Testing Requirements

Each pipeline must have:

- **Unit tests:** spatial math, CRS, geometry validation  
- **Integration tests:** MapLibre + Timeline + Focus sync  
- **Governance tests:** masking, sovereignty enforcement  
- **Schema tests:** STAC footprints, temporal ranges  
- **A11y tests:** accessible interaction  
- **Telemetry tests:** correct spatial telemetry emission  

Tests live under:

~~~text
tests/unit/web/pipelines/geospatial/**
tests/integration/web/pipelines/geospatial/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full geospatial pipeline documentation added; includes masking, STAC, temporal sync, telemetry |
| v10.3.2 | 2025-11-14 | Added spatial telemetry + governance enforcement |
| v10.3.1 | 2025-11-13 | Initial geospatial pipeline creation |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  

</div>