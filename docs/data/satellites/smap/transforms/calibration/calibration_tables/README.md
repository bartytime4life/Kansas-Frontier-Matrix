---
title: "🎚️ NASA SMAP — Calibration Tables (Radiometer Drift · Gain · Offset) · ETL Stage 3"
path: "docs/data/satellites/smap/transforms/calibration/calibration_tables/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Calibration Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
provenance_profile: "KFM-PROV-O v11.2"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public ETL Calibration Tables"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"

fair_category: "F1-A1-I1-R3"
care_label: "CARE-A / CARE-B (inherited from parent dataset)"
indigenous_rights_flag: false
sensitivity_level: "None (non-geospatial technical data)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · Calibration Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../../../schemas/json/transform-smap-calibration-tables-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/transform-smap-calibration-tables-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transform:calibration-tables-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-calibration-tables"
event_source_id: "ledger:docs/data/satellites/smap/transforms/calibration/calibration_tables/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon new calibration-cycle release"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🎚️ **NASA SMAP — Calibration Tables Library**  
`docs/data/satellites/smap/transforms/calibration/calibration_tables/README.md`

**Purpose**  
Provide the **versioned radiometer calibration tables** required during  
ETL **Stage 3 — Calibration**, which adjusts SMAP radiometer outputs  
(brightness temperature, soil moisture, FT, VWC, QA) for drift, gain, offsets,  
and mission-specific calibration cycles.

</div>

---

## 📘 1. Overview

The **calibration_tables/** directory contains all NASA-aligned calibrations:

- Radiometer **gain** adjustments  
- **Offset** corrections  
- **Long-term drift** coefficients  
- **Mode-specific** calibration parameters  
- **Versioned coefficient tables** for reproducible ETL  
- Calibration **epoch metadata**  
- Uncertainty propagation rules tied to calibration events  

These tables are referenced by:

- `apply_calibration.py`  
- Story Node v3 environmental provenance  
- Focus Mode v3 calibration transparency  
- STAC/DCAT generation  

Calibration is **never speculative**:  
every coefficient must trace back to a documented NASA source or vetted KFM correction.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/calibration/calibration_tables/
├── 📄 README.md                    # This file
│
├── 📚 table_v001.json             # Calibration epoch 001 (initial mission)
├── 📚 table_v002.json             # Calibration epoch 002
├── 📚 table_v003.json             # Calibration epoch 003
├── 📚 table_v004.json             # ...
│
└── 🗂️ history/                    # Historical tables + deprecated/diff logs
    ├── table_v000_legacy.json
    ├── diff_v001_v002.json
    └── diff_v002_v003.json
~~~

All calibration tables:

- Must specify `kfm:calibration_version`  
- Must define `coefficients` + `uncertainty model`  
- Must include provenance metadata linking back to NASA source products  

---

## 🧩 3. Calibration Table Specification (KFM-Cal v11)

Each table MUST contain:

### Required Fields  
- `calibration_version`  
- `nasa_product_version`  
- `valid_from` / `valid_to`  
- `coefficient_groups[]`:
  - `gain`  
  - `offset`  
  - `drift_per_year`  
  - `mode_specific[]`  

- `uncertainty_model`:
  - `radiometer_noise_floor`  
  - `propagation_rules`  
  - `bounds`  

- `provenance` (PROV-O):
  - `prov:used` (NASA tables, mission docs)  
  - `prov:wasGeneratedBy` (KFM calibration process)  
  - `prov:atLocation` (tool version, table file path)

### Optional Fields  
- `deprecated: true`  
- `notes`  

---

## 🔐 4. Governance & FAIR+CARE Compliance

Calibration tables:

- Do **not** contain geospatial data → **low sensitivity**  
- But calibration changes **affect interpretation** downstream  
- Therefore must disclose:
  - calibration epoch shifts  
  - uncertainty changes  
  - downstream impacts  
  - provenance trail  

Tables **must not** produce misleading environmental contrasts  
in Indigenous or culturally sensitive landscapes.

Downstream sovereignty masking rules ensure:

- Calibration does **not sharpen** sensitive features  
- Uncertainty is **never decreased** in protected areas  

---

## 🧪 5. QA, Validation & CI Enforcement

Calibration tables undergo:

- JSON Schema validation  
- SHACL constraint checks  
- Version continuity checks  
- Provenance chain validation  
- Consistency with SMAP decode metadata  
- Unit tests via:
  ```
  docs/data/satellites/smap/transforms/calibration/tests/
  ```

Failed validation → **CI hard fail**.

---

## 🔁 6. Place in Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration (this stage)
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC Item/Collection construction
 → DCAT metadata registration
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Reliable wetness/soil moisture thresholds  
- Stable flood modeling  

### Climate  
- VWC anomaly stability  
- Freeze-line consistency  

### Archaeology  
- Correct environmental backdrops for sites/events  

### Story Node v3  
- Accurate calibration-sensitive narrative context  

### Focus Mode v3  
- Transparency: “Which calibration epoch produced this value?”  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First full calibration-table README; emoji layout; PROV-O + STAC alignment; CI-safe; FAIR+CARE aligned. |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal calibration table index.                                                                 |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🎚️ Calibration Layer](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

