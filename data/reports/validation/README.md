---
title: "✅ Kansas Frontier Matrix — Data Validation Reports (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/reports/validation/README.md"
version: "v11.0.0"
last_updated: "2025-11-19"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Governance Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-reports-validation-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "KFM-MDP v11.0"
status: "Active / Enforced"
doc_kind: "Data Validation Layer"
intent: "reports-validation"
fair_category: "F1-A1-I1-R1"
care_label: "C0 · Low-Sensitivity Data QA"
ontology_alignment:
  schema_org: "Report"
  prov_o: "prov:Entity"
  dcat: "dcat:Dataset"
story_node_refs: []
provenance_chain:
  - "data/reports/validation/README.md@v10.0.0"
metadata_profiles:
  - "FAIR+CARE"
  - "DCAT 3.0"
  - "PROV-O"
  - "ISO 19115"
doc_uuid: "urn:kfm:data:reports:validation:v11"
semantic_document_id: "kfm-data-validation-reports"
event_source_id: "ledger:data_validation_q4_2025"
immutability_status: "mutable"
doc_integrity_checksum: "<sri-or-sha256>"
ai_training_input: false
ai_training_output: false
ai_transform_permissions:
  - "summary"
  - "governance-digest"
  - "timeline-generation"
ai_transform_restrictions:
  - "no-content-alteration"
sensitivity_level: "Contextual"
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public"
lifecycle_stage: "active"
ttl_policy: "Permanent"
sunset_policy: "Annual Review"
---

# ✅ Kansas Frontier Matrix — Data Validation Reports

This directory defines the **Data Validation Layer** for the  
Kansas Frontier Matrix (KFM) v11.

It captures all **schema conformance, STAC validation, quality-assurance,  
and governance-aligned checks** that are applied to datasets and models  
during the KFM lifecycle.

The goals of this layer are to:

- Guarantee **structural and semantic correctness** of all data products  
- Enforce **FAIR+CARE**, **DCAT 3.0**, and **ISO 19115** metadata standards  
- Support **reproducible, auditable, and ethics-aware** data releases  
- Provide machine- and human-readable **validation artifacts** for governance

All validation artifacts in this directory are:

- Produced by **autonomous validation pipelines** under KFM’s QA framework  
- Recorded in **append-only PROV-O–aligned governance ledgers**  
- Linked to **STAC / DCAT** metadata and release manifests  
- Enriched with **telemetry v11** (energy, CO₂, coverage, runtime)

---

# 📁 1. Directory Layout (DL-C Compliant)

This directory contains the core validation artifacts for data and model QA:

    data/reports/validation/
    ├── README.md
    ├── stac_validation_report.json
    ├── schema_validation_summary.json
    ├── geojson_schema_validation.log
    ├── ai_validation_metrics.json
    └── validation_summary.md

Descriptions:

- `stac_validation_report.json`  
  - STAC 1.0 / 1.x compliance and metadata checks for all datasets.  

- `schema_validation_summary.json`  
  - Summary of schema, attribute, and structural validation results  
    (GeoJSON, CSV, GeoTIFF, JSON-LD, other metadata).  

- `geojson_schema_validation.log`  
  - Detailed geometry/CRS checks from GDAL/ogrinfo and related tools.  

- `ai_validation_metrics.json`  
  - Validation metrics for AI-related datasets and models  
    (accuracy, F1, drift indices, error distributions).  

- `validation_summary.md`  
  - Human-readable summary of validation outcomes per governance cycle.

---

# 🧭 2. Overview of the Validation Engine

The KFM **Data Validation Engine** is invoked at key lifecycle boundaries:

- After dataset ingestion into `data/raw/`  
- After ETL processing into `data/work/` and `data/processed/`  
- Before dataset promotion to `data/reports/` and `releases/`  
- On changes to STAC/DCAT metadata or governance schemas  
- Prior to FAIR+CARE environmental / ethics audits  

For each dataset or model under review, the engine:

- Validates all metadata against KFM’s JSON Schemas  
- Confirms spatial and temporal integrity (bounds, CRS, geometry validity)  
- Ensures alignment with **STAC 1.x**, **DCAT 3.0**, and **ISO 19115**  
- Evaluates AI-augmented or derived products for drift, consistency, and bias  
- Writes machine-readable reports into `data/reports/validation/`  
- Publishes summary outcomes for governance and Focus Mode v3

---

# 🧪 3. Validation Dimensions & Tools

The validation layer covers multiple dimensions:

## 3.1 Structural & Schema Validation

- Tools: `jsonschema`, custom KFM schema validators  
- Targets: JSON, JSON-LD, CSV, GeoJSON, GeoTIFF metadata  
- Checks:  
  - Required fields present  
  - Types and enumerations respected  
  - Controlled vocabularies and code lists  
  - Referenced resources resolvable (STAC / DCAT)  

## 3.2 Spatial & Temporal Integrity

- Tools: `GDAL`, `ogrinfo`, projection utilities  
- Checks:  
  - Coordinate Reference System (CRS) declared and valid  
  - Extent bounds within expected domain (e.g., Kansas spatial envelope)  
  - Geometry validity (no self-intersections, broken polygons, etc.)  
  - Temporal coverage matching declared metadata  

## 3.3 STAC / DCAT Conformance

- Tools: `stac-validator`, DCAT linters  
- Checks:  
  - STAC Item, Collection, and Catalog structure validity  
  - Conformance to KFM’s DCAT 3.0 profiles  
  - Presence of links to provenance, sustainability, and FAIR+CARE artifacts  

## 3.4 AI & Derived Data Validation

- Tools: KFM AI validation modules, drift monitors  
- Checks:  
  - Accuracy, F1, precision/recall, calibration metrics  
  - Distributional drift across versions or time slices  
  - Consistency between model outputs and declared semantics  
  - Flags for potential bias or unstable behavior  

## 3.5 FAIR+CARE Internal Checks

- Checks whether validated outputs:  
  - Have complete metadata for discovery and reuse  
  - Use open, documented, interoperable formats  
  - Embed or link to CARE / stewardship metadata where applicable  
  - Satisfy KFM’s governance and ethics rubrics  

---

# 🧩 4. Example Validation Record (Plaintext Representation)

Example excerpt from `stac_validation_report.json`  
for dataset `hazards_v11.0.0`:

    {
      "dataset_id": "hazards_v11.0.0",
      "status": "passed",
      "validator": "stac-validator 1.2.0",
      "stac_version": "1.0.0",
      "errors": [],
      "warnings": [
        "Optional field 'keywords' not provided; recommended for discoverability."
      ],
      "metadata_completeness": 0.98,
      "linked_items": [
        "data/stac/items/hazards_v11.0.0.json",
        "data/reports/audit/data_provenance_ledger.json"
      ],
      "telemetry": {
        "energy_wh": 0.7,
        "co2_g": 1.0,
        "runtime_seconds": 5
      }
    }

This structure is **JSON-LD–ready** and links the validation  
artifact to the canonical STAC item and governance ledger.

---

# 🔍 5. Governance & FAIR+CARE Integration

Validation outputs are first-class governance artifacts and are:

- Referenced by the **Data Provenance Ledger**  
  - `data/reports/audit/data_provenance_ledger.json`  

- Aggregated into FAIR scoring reports  
  - `data/reports/fair/data_fair_summary.json`  

- Used by **autonomous promotion/rollback** logic  
  - Only datasets with passing validation are eligible for release  
  - Failed validations create remediation tasks for QA and governance  

- Surfaced into Focus Mode v3 as integrity and confidence context  
  - Narrative and hydrologic reconstructions reference validation status  

This ensures that **every published dataset** is:

- Traceable to its validation and governance history  
- Ethically screened and environmentally aware (via FAIR+CARE + sustainability)  
- Reproducible under KFM’s **SLSA-aligned** QA practices

---

# ⚖️ 6. Retention & Lifecycle

Validation artifacts are retained as part of KFM’s long-term governance archive:

- Per-cycle validation reports: retained for at least 5 years  
- Release-linked validation outputs: retained for the full life of the dataset  
- Telemetry and error logs: rotated on a scheduled basis but digested into summary reports  

Lifecycle automation is handled by:

- `validation_retention.yml` — rotates detailed logs  
- `governance-ledger-sync.yml` — ensures all validation artifacts are reflected  
  in the audit ledgers and that links remain up to date

---

# 🕰️ 7. Version History

- v11.0.0 — KFM-MDP v11 migration; Story Node v3–aligned narrative/technical style; updated telemetry schema to `data-reports-validation-v11.json`; tightened DCAT/PROV-O mappings.  
- v10.0.0 — Telemetry v2 embedded in validation artifacts; streaming STAC awareness; unified error taxonomy; expanded cross-linking to FAIR+CARE.  
- v9.x — Initial validation layer for STAC and schema conformance, pre–v10 telemetry.

---

# ✅ Kansas Frontier Matrix — Data Validation Lineage Layer

Validation is the **gatekeeper of trust** in the Kansas Frontier Matrix.  
Every dataset, model, and narrative depends on this layer to ensure that  
its structure, semantics, ethics, and environmental footprint meet KFM’s  
governance standards before being promoted, cited, or used in analysis.

[⬅ Back to Reports Index](../README.md) · [⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)
