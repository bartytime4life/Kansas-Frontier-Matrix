---
title: "📉 NASA SMAP — QA-Derived Uncertainty Modifiers (ETL Stage 5 · Sovereignty-Safe · FAIR+CARE)"
path: "docs/data/satellites/smap/qa/uncertainty_modifiers/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public QA/Uncertainty Dataset Layer"
status: "Active / Enforced"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council Oversight"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low"
risk_category: "Medium"
redaction_required: true

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/smap-uncertainty-modifiers-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-uncertainty-modifiers-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-modifiers-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-modifiers"
event_source_id: "ledger:docs/data/satellites/smap/qa/uncertainty_modifiers/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next uncertainty schema update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📉 **NASA SMAP — QA-Derived Uncertainty Modifiers**  
`docs/data/satellites/smap/qa/uncertainty_modifiers/README.md`

**Purpose**  
Document the **uncertainty modifiers** computed from multiple QA sources (Radiometer, RFI,  
Retrieval SM/FT/VWC) during **ETL Stage 5**, producing pixel-level uncertainty scalars  
used in KFM’s environmental modeling, STAC metadata, Focus Mode v3, and Story Node v3.

</div>

---

## 📘 1. Overview

The **Uncertainty Modifiers Layer** synthesizes QA signals into per-pixel  
uncertainty adjustments:

- 📡 RFI contamination  
- ⚠️ radiometer anomalies  
- 🎚️ retrieval confidence (SM/FT/VWC)  
- 🌡️ freeze–thaw instability  
- 🌱 vegetation-water ambiguity  
- 🧊 snow/rain contamination behavior  
- 🛡 sovereignty uncertainty floors (H3-based rules)

These modifiers impact all downstream environmental reasoning.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/uncertainty_modifiers/
├── 📄 README.md                                # This file
│
├── 📉 qa_uncertainty_scale.tif                  # Pixel-level uncertainty multiplier
├── 📑 metadata.json                             # STAC/DCAT metadata for uncertainty layer
│
├── 🧪 tests/                                    # Uncertainty validation suite
│   ├── test_uncertainty_scaling.py
│   ├── test_metadata_integrity.py
│   ├── test_governance_preservation.py
│   └── fixtures/
│       ├── sample_uncertainty_scale.tif
│       ├── sample_metadata.json
│       ├── expected_uncertainty_output.json
│       └── schema_expected.json
~~~

---

## 🧩 3. Responsibilities of the Uncertainty Modifier Layer

### 1. 📡 Integrate RFI QA  
Pixels with strong RFI → larger multiplicative uncertainty.

### 2. ⚠️ Integrate Radiometer QA  
Instrument anomalies → localized uncertainty increases.

### 3. 🎚️ Integrate Retrieval QA  
Confidence:  
- low → high uncertainty  
- medium → moderate  
- high → minimal adjustment  

### 4. 🌡️ Integrate FT Ambiguity  
Ambiguous seasonal transitions increase uncertainty, especially near sovereign lands.

### 5. 🌱 Integrate VWC Ambiguity  
Dense-canopy instability → targeted uncertainty inflation.

### 6. 🛡 Sovereignty Rules (Critical)  
In H3-sensitive regions:

- enforce `"kfm:sovereignty_uncertainty_floor"`  
- uncertainty NEVER decreases  
- aggregated generalization rules applied  
- `"kfm:mask_required"` where needed  
- `"kfm:care_label"` always retained  

### 7. 🔗 Prepare Metadata for STAC Writer  
Metadata includes:

- uncertainty rationale  
- aggregated QA sources  
- care/sovereignty fields  
- lineage references  

---

## 🔐 4. Governance, FAIR+CARE & Sovereignty Rules

Uncertainty MUST:

- never reduce uncertainty in sovereign areas  
- preserve `"kfm:h3_sensitive"`  
- propagate `"kfm:care_label"` and `"kfm:care_label_reason"`  
- attach `"kfm:governance_notes"` for any masking/generalization  
- track sovereignty-aware transformations in PROV-O  

Failing to enforce sovereignty = **CI hard block**.

---

## 🧪 5. QA & Validation Requirements

CI validates:

- correct uncertainty scaling values  
- alignment with SMAP base rasters  
- correct integration of RFI + radiometer + retrieval QA  
- metadata correctness (temporal, spatial, STAC, DCAT)  
- governance compliance  
- no illegal precision in sovereign H3 zones  
- correct lineage structure  

---

## 🔁 6. Uncertainty Modifiers in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → retrieval QA (SM/FT/VWC)
 → uncertainty propagation (THIS LAYER)
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Improved uncertainty envelopes for soil-moisture anomalies.

### Climate  
More accurate FT/VWC anomaly modeling with sovereign-safe uncertainty floors.

### Archaeology  
Environmental uncertainty supports safer interpretation of cultural landscapes.

### Story Node v3  
Uncertainty modifiers influence narrative evidence weighting.

### Focus Mode v3  
Uncertainty-aware reasoning and contextual explanations.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Uncertainty Modifier README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-ready; CI-safe; emoji-rich.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📉 QA → Uncertainty Tests](./tests/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

