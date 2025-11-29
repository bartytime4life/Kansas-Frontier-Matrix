---
title: "🧪 NASA SMAP — Reprojection Stage Test Suite (EASE-Grid → KFM CRS) · ETL Stage 2"
path: "docs/data/satellites/smap/transforms/reprojection/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems QA · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

test_category: "ETL Stage 2 · Reprojection · CRS Integrity · BBox Validation"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"
provenance_profile: "KFM-PROV-O v11.2"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public ETL Test Documentation"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

fair_category: "F1-A1-I1-R3"
care_label: "CARE-A / CARE-B depending on spatial extent"
indigenous_rights_flag: true
sensitivity_level: "Low (synthetic test data)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems QA Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-reprojection-v11.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-reprojection-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:reprojection:tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-reprojection-tests"
event_source_id: "ledger:docs/data/satellites/smap/transforms/reprojection/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon modernization of reprojection test suite"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — Reprojection Test Suite (KFM ETL Stage 2)**  
`docs/data/satellites/smap/transforms/reprojection/tests/README.md`

**Purpose**  
Validate the correctness, reproducibility, governance alignment,  
and STAC/DCAT/JSON-LD/PROV-O compliance of the **Reprojection Stage**  
(EASE-Grid 2.0 → KFM CRS).  
These tests ensure spatial integrity before calibration, QA integration,  
uncertainty propagation, masking, and STAC/DCAT generation.

</div>

---

## 📘 1. Overview

This test suite ensures:

- Correct EASE-Grid 2.0 → KFM CRS reprojection  
- Proper handling of anti-meridian & bounding boxes  
- Preservation of geolocation accuracy  
- Stable raster alignment after reprojection  
- Consistency of uncertainty interpolation  
- Proper metadata propagation (`proj:*`, `raster:*`, `kfm:*`)  
- Proper CARE/H3 sensitivity propagation  
- Compatibility with KFM-STAC v11 projection extension  
- Structural readiness for STAC/DCAT/PROV-O generation  

All tests MUST pass before any SMAP dataset can be published into the KFM ecosystem.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/reprojection/tests/
├── 📄 README.md                               # This file
│
├── 🧪 test_ease_projection.py                 # EASE-Grid → KFM CRS reprojection integrity tests
├── 🧪 test_bbox_normalization.py              # Anti-meridian & bounds normalization tests
├── 🧪 test_crs_integrity.py                   # CRS metadata checks (EPSG, proj4, WKT, transform)
│
├── 🧪 test_uncertainty_interpolation.py       # Uncertainty resampling tests
├── 🧪 test_governance_flag_propagation.py     # CARE/H3 governance-flag propagation tests
│
└── 🔧 fixtures/                               # Synthetic test inputs & mock grids
    ├── sample_ease_grid.json
    ├── sample_kfm_grid.json
    ├── sample_raster_before.tif
    └── sample_raster_after.tif
~~~

All tests use **small synthetic fixtures** to guarantee determinism and FAST CI runtimes.

---

## 🧩 3. Required Test Domains

### ✔ CRS Integrity  
- Correct EPSG  
- proj4 / WKT consistency  
- Transform matrix correctness  

### ✔ Geometry Validity  
- No self-intersections  
- Valid polygon winding  
- BBox encloses geometry exactly  
- Anti-meridian safe  

### ✔ Reprojection Accuracy  
- Coordinate transformation correctness  
- Pixel-center / pixel-edge rules  
- Grid cell area sanity checks  

### ✔ Raster Alignment  
- Soil moisture  
- Freeze-thaw  
- Vegetation water  
- QA/RFI masks  
- After-reprojection alignment  

### ✔ Uncertainty Interpolation  
- No artificial reduction in uncertainty  
- Matching uncertainty semantics from NASA L2/L3  
- CRS-safe resampling  

### ✔ Governance Flag Propagation  
Ensures reprojection NEVER:

- Drops CARE labels  
- Drops sovereignty flags  
- Removes `"kfm:mask_required"`  
- Removes `"kfm:h3_sensitive"`  

These flags are **inputs** for the Masking Stage (ETL Stage 6).

---

## 🔐 4. Governance + FAIR+CARE Enforcement

All tests verify:

- Sovereignty context propagates across CRS boundaries  
- Grid transformations do not sharpen sensitive geographic detail  
- H3-sensitivity zones remain correctly marked  
- No introduced spatial bias or precision jump  
- CARE classification survives reprojection untouched  

Governance CI runs:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  

---

## 📊 5. Telemetry & QC Reporting

Each test run generates:

- OpenLineage events (per ETL step)  
- Telemetry entries in:
  `releases/<version>/data-telemetry.json`

Metrics include:

- Reprojection time  
- CRS conversion error statistics  
- Governance violations caught  
- Raster alignment error scores  
- Synthetic fixture correctness checks  

---

## 🔁 6. Integration in the Full ETL Chain

~~~text
decode
 → reprojection (this test suite)
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC Item/Collection creation
 → DCAT dataset registration
 → PROV-O lineage export
 → OpenLineage telemetry emission
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Reliable wetness + infiltration spatial layers.

### Climate  
Stable anomaly grids for drought, freeze-line, VWC.

### Archaeology  
Accurate vegetation masking + environmental overlays.

### Story Node v3  
Spatially-accurate event/landscape embeddings.

### Focus Mode v3  
CRS-correct environmental context generation.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                |
|--------:|------------|--------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full reprojection test-suite documentation; emoji directory; CRS/H3/CARE validation; CI-safe.         |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal placeholder.                                                                           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗺️ Reprojection Layer](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

