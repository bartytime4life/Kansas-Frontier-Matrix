---
title: "📉📚 Kansas Frontier Matrix: Late Prehistoric H3 — Paleo-Seasonal Uncertainty Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/inputs/environmental_rasters/climate/seasonality/paleoseasonal/uncertainty/metadata/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-paleoseasonal-uncertainty-metadata-v1.json"
governance_ref: "../../../../../../../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Metadata"
intent: "archaeology-late-prehistoric-h3-paleoseasonal-uncertainty-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Uncertainty Metadata"
redaction_required: false
provenance_chain:
  - "docs/analyses/.../uncertainty/metadata/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
json_schema_ref: "../../../../../../../../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-paleoseasonal-uncertainty-metadata.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-paleoseasonal-uncertainty-metadata-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:paleoseasonal-uncertainty-metadata-late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-paleoseasonal-uncertainty-metadata"
event_source_id: "ledger:docs/.../uncertainty/metadata/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-uncertainty"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-late-prehistoric-h3-paleoseasonal-uncertainty-metadata"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next uncertainty metadata revision"
---

<div align="center">

# 📉📚 **Late Prehistoric H3 — Paleo-Seasonal Uncertainty Metadata Registry**  
`docs/analyses/.../uncertainty/metadata/README.md`

**Purpose:**  
Provide the **complete metadata schema and dataset-level descriptions** for uncertainty rasters associated with Late Prehistoric paleo-seasonal climate reconstructions.  
These metadata artifacts describe the uncertainty layers that accompany paleo-seasonal temps/precip rasters and ensure that they remain fully FAIR+CARE-governed, machine-validated, and narrative-safe for analysis and Focus Mode v3 use.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains metadata for all **uncertainty layers** used in Late Prehistoric H3 cluster workflows:

- Uncertainty rasters for reconstructed temperature  
- Uncertainty rasters for reconstructed precipitation  
- Combined uncertainty summary tables  
- Proxy disagreement indices  
- Calibration model variance logs  

These metadata files ensure:

- reproducibility  
- transparency  
- cultural governance  
- rigorous scientific interpretation  
- compliance with KFM-MDP v11 metadata structure  
- compatibility with DCAT / STAC / PROV-O / Story Node v3  

All uncertainty metadata must adhere to strict lineage rules and remain free of speculative environmental or cultural claims.

---

## 🗂️ Directory Layout

```text
docs/.../uncertainty/metadata/
├── README.md                                 # This file
├── holocene_temp_uncertainty_metadata.json   # STAC/DCAT metadata for temp uncertainty
├── holocene_precip_uncertainty_metadata.json # STAC/DCAT metadata for precip uncertainty
├── uncertainty_summary.jsonld                 # Combined JSON-LD metadata
└── validation_report.json                     # CI/CD validation output
````

---

## 🌡️ Temperature Uncertainty Metadata

**File:** `holocene_temp_uncertainty_metadata.json`

Includes:

* STAC Item fields (`stac_version`, `bbox`, `datetime`, etc.)
* DCAT dataset descriptors (`dct:title`, `dct:description`, `dcat:distribution`)
* Calibration model details
* Proxy source linkage
* CARE flags (`care:sensitivity = generalized`)
* Provenance chain (`prov:wasGeneratedBy`)
* KFM extensions for uncertainty quantification

---

## 🌧️ Precipitation Uncertainty Metadata

**File:** `holocene_precip_uncertainty_metadata.json`

Includes:

* rainfall reconstruction uncertainties
* proxy disagreement metrics
* confidence fields
* temporal spans (OWL-Time)
* citation blocks for proxy datasets
* GeoSPARQL geometries for generalized extents

---

## 📦 Combined Uncertainty Summary (`uncertainty_summary.jsonld`)

Contains:

* unified metadata
* multi-proxy consensus metrics
* global uncertainty scores
* environmental context notes (non-speculative)
* Story Node cross-links
* references to all individual metadata files

This serves as the **canonical uncertainty metadata bundle**.

---

## 🧪 Validation & CI/CD Integration

`validation_report.json` stores pipeline validation outputs:

* JSON Schema validation
* SHACL shape checks
* FAIR+CARE compliance checks
* Link integrity
* Required-field presence checks
* Accessibility metadata verification

Metadata must pass all checks before integration with:

* Focus Mode v3
* Story Node v3
* STAC discovery browser
* Knowledge Graph provenance layer

---

## 🧠 Focus Mode Integration Notes

Focus Mode uses uncertainty metadata to:

* qualify environmental interpretations
* annotate narrative elements with confidence levels
* reveal environmental model limitations
* prevent overinterpretation of paleo-seasonal climate signals

Example Focus Summary:

> **Focus Summary:**
> Uncertainty metadata indicates where paleo-seasonal reconstructions are highly reliable
> and where proxy disagreement or calibration limits reduce confidence.
> These notes help guide responsible archaeological interpretation and narrative framing.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                          |
| ------: | ---------- | ---------------------------------- | ---------------------------------------------------------------- |
| v11.0.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Initial metadata registry for paleo-seasonal uncertainty layers. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Uncertainty Metadata · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Uncertainty](../README.md) · [Back to Proxy Sources](../../sources/README.md)

</div>
