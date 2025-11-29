---
title: "📦 NASA SMAP — Reprojection Test Fixtures (Synthetic EASE-Grid ↔ KFM CRS Inputs) · ETL Stage 2"
path: "docs/data/satellites/smap/transforms/reprojection/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · QA Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

classification: "Public Test Fixtures"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

test_category: "CRS Transform · BBox Normalization · Uncertainty Resampling · Governance Flags"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R3"
care_label: "CARE-A / CARE-B depending on mock geometry"
indigenous_rights_flag: true
sensitivity_level: "Low (fully synthetic)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems QA Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-reprojection-v11.schema.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-reprojection-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:reprojection:tests:fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-reprojection-tests-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/transforms/reprojection/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "18 months"
sunset_policy: "Superseded upon fixture-format update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Reprojection Test Fixtures (Synthetic Grid & Raster Inputs)**  
`docs/data/satellites/smap/transforms/reprojection/tests/fixtures/README.md`

**Purpose**  
Provide the **synthetic spatial data fixtures** used to test the SMAP  
**Reprojection Stage (EASE-Grid 2.0 → KFM CRS)**.  
These fixtures ensure ETL Stage 2 behaves consistently, ethically,  
and STAC/DCAT/JSON-LD/PROV-O compliant across all SMAP products  
(soil moisture · freeze–thaw · VWC · QA/RFI).

</div>

---

## 📘 1. Overview

These fixtures emulate NASA L3 geospatial grids and KFM CRS targets in a **tiny, deterministic form**.

They validate:

- CRS transforms  
- BBox normalization  
- Anti-meridian handling  
- Pixel-center vs pixel-edge alignment  
- Uncertainty resampling  
- Governance-flag propagation  
- STAC `proj:*` + `raster:*` metadata correctness  
- Spatial provenance consistency  

Fixtures are lightweight, synthetic, FAIR-safe, sovereignty-safe,  
and engineered for super-fast CI runs.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/reprojection/tests/fixtures/
├── 📄 README.md                           # This file
│
├── 🗺️ sample_ease_grid.json               # Synthetic EASE-Grid 2.0 grid definition
├── 🌐 sample_kfm_grid.json                # Synthetic KFM CRS grid definition
│
├── 🛰️ sample_raster_before.tif            # Tiny mock L3 raster before reprojection
├── 🛰️ sample_raster_after.tif             # Expected raster after reprojection
│
├── 📉 sample_uncertainty_before.tif       # Uncertainty before reprojection
├── 📉 sample_uncertainty_after.tif        # Uncertainty after reprojection
│
└── 🔧 schema_expected.json                # Expected structure used by regression tests
~~~

All fixtures are **synthetic**, **small**, and **schema-validated**.

---

## 🧩 3. Fixture Responsibilities

### 🗺️ `sample_ease_grid.json`
- Minimal EASE-Grid 2.0 definition  
- CRS metadata  
- Cell-center coordinates  
- Pixel orientation rules  
- Used to test:
  - reprojection core  
  - CRS integrity  
  - BBox alignment  

### 🌐 `sample_kfm_grid.json`
- KFM’s unified CRS (subset)  
- CRS transform parameters  
- Used to confirm:
  - correct EPSG  
  - correct proj4/WKT  
  - valid `proj:*` metadata for STAC  

### 🛰️ `sample_raster_before.tif`
- Synthetic brightness-temperature or similar SMAP-like grid  
- Tiny dimensions (e.g., 10×10)  
- Pixel values designed for deterministic mapping  

### 🛰️ `sample_raster_after.tif`
- Expected output after correct reprojection  
- Used to verify:
  - coordinate rounding  
  - interpolation mode  
  - pixel alignment  

### 📉 `sample_uncertainty_before.tif` & `sample_uncertainty_after.tif`
Validate:

- Correct uncertainty interpolation rules  
- No sharpening or bias  
- Preservation of uncertainty semantics  

### 🔧 `schema_expected.json`
Contains:

- Expected grid dimensions  
- Valid min/max bounds  
- Proper CRS identifiers  
- Expected reprojection parameters  
- Alignment tolerances  

Used by:
- `test_ease_projection.py`  
- `test_crs_integrity.py`  
- `test_uncertainty_interpolation.py`  

---

## 🔐 4. Governance & Sovereignty Requirements

Even synthetic fixtures must:

- Represent H3/CARE-sensitive zones in a **test-safe** way  
- Include sovereignty flags in metadata mocks  
- Use synthetic coordinates that DO NOT correspond to real protected areas  
- Validate `"kfm:h3_sensitive"` & `"kfm:mask_required"` propagation logic  
- Maintain sovereignty-invariant behavior across CRS transforms  

All test fixtures must pass:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. QA & Validation Expectations

Fixture validation ensures:

- CRS structure correctness  
- Pixel indexing alignment  
- No NaNs unless intentional (declared in schema)  
- Micro-level BBox correctness  
- Predictable interpolation behavior  

These errors would cause:

- failed STAC generation  
- misaligned hydrology/climate grids  
- incorrect Story Node v3 or Focus Mode v3 environmental overlays  

---

## 🔁 6. Integration in Full ETL Context

~~~text
decode
 → reprojection (this test suite)
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC Item/Collection construction
 → DCAT dataset registration
 → PROV-O lineage export
 → OpenLineage telemetry emission
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Reliably reprojected wetness & runoff layers.

### Climate  
Freeze-line and VWC anomaly layers.

### Archaeology  
Vegetation masking + landscape-state reconstructions.

### Story Node v3  
Accurate spatial anchors for historical/environmental narratives.

### Focus Mode v3  
Spatially coherent environmental context for entities & timelines.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full reprojection-fixtures README; emoji layout; governance/H3 rules; CRS-test alignment; CI-safe |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal fixture notes.                                                                     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Reprojection Tests](../README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

