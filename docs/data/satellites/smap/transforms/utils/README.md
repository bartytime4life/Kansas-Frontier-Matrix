---
title: "🧰 NASA SMAP — Shared ETL Utility Modules (Transforms Core Library)"
path: "docs/data/satellites/smap/transforms/utils/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council Oversight"
status: "Active / Enforced"

classification: "Public ETL Utility Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B (variable-dependent)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../schemas/json/transform-smap-utils-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/transform-smap-utils-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transforms-utils-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transforms-utils"
event_source_id: "ledger:docs/data/satellites/smap/transforms/utils/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon utilities-module overhaul"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧰 **NASA SMAP — Shared ETL Utilities**  
`docs/data/satellites/smap/transforms/utils/README.md`

**Purpose**  
Serve as the **central utility library** for all SMAP ETL stages.  
This module provides validated, deterministic, FAIR+CARE-aware helpers  
used by **decode**, **reprojection**, **calibration**, **QA/RFI**,  
**uncertainty**, **governance masking**, **provenance**, and **STAC writer**  
to ensure consistent behavior across the entire SMAP ingestion pipeline.

</div>

---

## 📘 1. Overview

The utilities in this directory provide:

- 🧮 Numerics, rescaling, unit conversions  
- 🗺️ Geospatial helpers (bbox, pixel ↔ geo transform, H3 alignment)  
- 📑 Metadata merge logic (governance, QA, uncertainty, STAC fields)  
- 🔒 Deterministic hashing and ID generation  
- 📂 File I/O wrappers (COG-safe, metadata-safe)  
- 🧾 JSON-LD & PROV-O helpers  
- 🔁 Array and structure normalization  
- 🧭 Sovereignty-aware clamping/generalization helpers  
- 🩺 Validation utilities for schema + SHACL  
- 🛠 Error-handling and ETL invariant enforcement  

All modules are **pure**, **side-effect free**, **testable**, and **consistent** across platforms.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/utils/
├── 📄 README.md                         # This file
│
├── 🧮 numeric.py                        # Numeric transforms, scaling, normalization
├── 🌐 geo_utils.py                      # CRS transforms, bbox ops, H3 helpers
├── 🧾 metadata_utils.py                 # STAC/DCAT metadata merging rules
├── 🔐 governance_utils.py               # CARE/H3/unmasking rules for metadata propagation
├── 📑 jsonld_utils.py                   # PROV-O JSON-LD helpers
├── 🪪 id_utils.py                       # Deterministic ID hashing, version tokens
├── 🔧 io_utils.py                       # Safe raster read/write + metadata sync
├── 🧬 array_utils.py                    # Deterministic array ops (unique, stable sort, merge)
│
└── 🧪 tests/
    ├── test_numeric.py
    ├── test_geo_utils.py
    ├── test_metadata_utils.py
    ├── test_governance_utils.py
    ├── test_jsonld_utils.py
    ├── test_id_utils.py
    ├── test_io_utils.py
    └── fixtures/
        ├── sample_raster.tif
        ├── sample_metadata.json
        ├── sample_h3_mask.json
        ├── sample_jsonld_stub.json
        └── schema_expected.json
~~~

---

## 🧩 3. Module Responsibilities

### 🧮 **numeric.py**
- deterministic math  
- uncertainty propagation helpers  
- clipping, scaling, interpolation  
- avoids floating-point nondeterminism  
- never reduces uncertainty in sensitive regions  

### 🌐 **geo_utils.py**
- bbox expansion/merge  
- reproject pixel → geo  
- H3 ↔ raster alignment  
- sovereignty-aware mask application  
- CRS inference and validation  

### 🧾 **metadata_utils.py**
- STAC property merging  
- DCAT field injection  
- QA/uncertainty metadata normalization  
- CARE/H3 metadata propagation  
- timeline/temporal normalization  

### 🔐 **governance_utils.py**
- apply `"kfm:mask_required"` logic  
- enforce `"kfm:sovereignty_uncertainty_floor"`  
- preserve CARE labels  
- ensure no sensitive coordinates leak  
- support generalization rules  

### 📑 **jsonld_utils.py**
- PROV-O node construction  
- Activity → Entity → Agent linking  
- JSON-LD context embedding  
- provenance flattening + compaction  

### 🪪 **id_utils.py**
- stable hash generation  
- STAC Item ID creation (sensor + timestamp + tile)  
- Agent/Activity ID creation  
- nondeterministic fields eliminated  

### 🔧 **io_utils.py**
- COG-safe read/write  
- metadata injection/validation  
- nodata and mask handling  
- coordinate reference checks  

### 🧬 **array_utils.py**
- stable sorting  
- merge, nest, unwrap  
- bitfield QA decoding utilities  
- deterministic graph-safe set ops  

---

## 🔐 4. Governance, FAIR+CARE, and Sovereignty Requirements

All utilities MUST:

- preserve `"kfm:care_label"`  
- propagate `"kfm:h3_sensitive"`  
- apply `"kfm:mask_required"` where appropriate  
- avoid introducing false precision  
- enforce sovereignty-aware uncertainty floors  
- avoid stripping governance metadata  
- avoid speculation or inferred values  

Governance enforced in CI via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation Requirements

Utilities are validated for:

- determinism  
- numeric stability  
- schema correctness  
- CRS correctness  
- governance propagation  
- JSON-LD/PROV conformance  
- STAC/DCAT metadata integrity  

Fixtures ensure repeatability and error detection.

---

## 🔁 6. Integrations in the SMAP ETL Chain

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer (final)
        ↑
 utilities used across ALL stages
~~~

Utilities serve as the **glue** that guarantees consistent behavior across ETL.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Reliable soil-moisture metadata, CRS, uncertainty behavior.

### Climate  
Stable FT/VWC metadata + governance-safe calculations.

### Archaeology  
Generalization + sovereignty-aware data handling.

### Story Node v3  
Consistent metadata & provenance blocks.

### Focus Mode v3  
Clean temporal, spatial, and governance semantics.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full utilities README; emoji-rich; governance/H3 aligned; STAC/DCAT/PROV compliant; CI-safe.             |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Utility Tests](./tests/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

