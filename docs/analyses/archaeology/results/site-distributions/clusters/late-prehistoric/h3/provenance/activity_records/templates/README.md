---
title: "📜 Kansas Frontier Matrix: Late Prehistoric H3 Activity Record Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/templates/README.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / FAIR+CARE Council · Archaeology Working Group"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-activity-record-templates-v1.json"
governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Provenance Templates"
intent: "archaeology-late-prehistoric-h3-activity-record-templates"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Template / Provenance"
redaction_required: false
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/templates/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-activity-record-template.schema.json"
shape_schema_ref: "../../../../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-activity-record-template-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:templates:late-prehistoric-h3-activity-records-v11.0.0"
semantic_document_id: "kfm-arch-results-late-prehistoric-h3-activity-record-templates"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/templates/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "fabricated-lineage"
  - "unverified-inference"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public / Templates"
role: "archaeology-late-prehistoric-h3-activity-record-templates"
lifecycle_stage: "stable"
ttl_policy: "Review every 24 months"
sunset_policy: "Superseded upon next major provenance-template revision"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Late Prehistoric H3 Activity Record Templates**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/templates/README.md`

**Purpose:**  
Provide **standardized JSON-LD templates** for all PROV-O activity records associated with Late Prehistoric H3 generalization workflows.  
These templates guarantee consistent structure, governance compliance, semantic alignment, and deterministic lineage reproduction across KFM.

![Docs](https://img.shields.io/badge/Docs·MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains templates for:

- **Generalization activities** (H3 r7/r8)  
- **KDE smoothing operations**  
- **Spatial validation processes**  
- **CARE redaction activities**  
- **Public export packaging**  
- **Modeling transformations**  

Each template is:

- Structured using **JSON-LD**  
- Fully compliant with **PROV-O**, **CIDOC-CRM**, and **GeoSPARQL**  
- Aligned with **KFM provenance schema**  
- Reviewed and approved under **FAIR+CARE governance**  

These templates ensure that activity records:

- Follow a unified semantic pattern  
- Are machine-validated (JSON Schema + SHACL)  
- Can be ingested into **Neo4j provenance graphs**  
- Support complete reproducibility (WAL → Retry → Rollback → Lineage)

---

## 🗂️ Directory Layout

```text
docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/provenance/activity_records/templates/
├── README.md                               # This file
├── activity_record.template.jsonld          # Base template for any PROV-O Activity
├── generalization.template.jsonld           # H3 generalization workflow
├── kde_smoothing.template.jsonld            # KDE smoothing step
├── spatial_validation.template.jsonld       # Spatial autocorrelation / QC step
├── care_redaction.template.jsonld           # Tribal review + redaction template
└── export_packaging.template.jsonld         # Public-safe dataset packaging
````

---

## 📜 Template Design Principles

All templates must follow:

### 1️⃣ **PROV-O Core Structure**

Each JSON-LD activity record must include:

* `@id` — stable URN for the activity
* `@type`:

  * `"prov:Activity"`
  * additional KFM or CIDOC classes where relevant
* **Time stamps**:

  * `prov:startedAtTime`
  * `prov:endedAtTime`
* **Entities**:

  * `prov:used` (inputs)
  * `prov:generated` (outputs)
* **Agents**:

  * `prov:wasAssociatedWith` (human or software agents)

---

### 2️⃣ **CARE Metadata Embedding**

Every template must include fields for:

* `care:sensitivity`
* `care:redaction_level`
* `care:review_status`
* `care:sovereignty_notes`

These govern:

* masking
* aggregation
* suppression
* narrative constraints

---

### 3️⃣ **KFM Provenance Extensions**

Templates must include:

* `kfm:pipeline_version`
* `kfm:model_parameters`
* `kfm:confidence_estimates`
* `kfm:generalization_level`
* `kfm:validation_checks`
* `kfm:stac_references`
* `kfm:story_node_links`

These fields bind the activity record into:

* KFM pipelines
* STAC lineage
* Story Node v3
* Focus Mode v3

---

### 4️⃣ **Deterministic Reproducibility Encoding**

Templates must encode:

* random seeds
* code version
* parameter sets
* environmental variables
* configuration versions

These appear under:

```json
"kfm:reproducibility": {
  "seed": 12345,
  "env": "python3.11",
  "config_hash": "<sha256>"
}
```

---

### 5️⃣ **WAL → Retry → Rollback → Lineage Hooks**

All templates must contain WAL metadata:

```json
"kfm:wal": {
  "checkpoint": "activity_0004",
  "rollback_allowed": true
}
```

This ensures:

* traceability
* safety
* deterministic re-runs
* rollbacks when CARE changes occur

---

## 📝 Example Template (Excerpt)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://data.kfm.org/ns/care#",
    "kfm": "https://data.kfm.org/ns/kfm#"
  },
  "@id": "urn:kfm:activity:late-prehistoric-h3-generalization-template",
  "@type": ["prov:Activity", "kfm:H3Generalization"],
  "prov:startedAtTime": "<ISO8601>",
  "prov:endedAtTime": "<ISO8601>",
  "prov:used": [],
  "prov:generated": [],
  "prov:wasAssociatedWith": ["urn:kfm:agent:archaeology-wg"],
  "care:sensitivity": "generalized",
  "care:redaction_level": "r7",
  "kfm:pipeline_version": "v11.0.0",
  "kfm:generalization_level": "r7",
  "kfm:stac_references": [],
  "kfm:story_node_links": []
}
```

---

## 🧪 Validation Requirements

All completed activity records based on these templates must:

* Pass **JSON Schema** validation
* Pass **SHACL shape constraints**
* Contain **no missing required fields**
* Use **valid URNs**
* Use **ISO8601 timestamps**
* Include **complete CARE metadata**
* Include **complete lineage chain references**

Incomplete or malformed records will **fail CI/CD** and block merges.

---

## 🕰️ Version History

| Version | Date       | Author                             | Summary                                                                        |
| ------: | ---------- | ---------------------------------- | ------------------------------------------------------------------------------ |
| v11.0.0 | 2025-11-17 | FAIR+CARE Council · Archaeology WG | Initial template registry for Late Prehistoric H3 provenance activity records. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0
Provenance Template Registry · CARE-Governed · FAIR+CARE Certified
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[Back to Activity Records](../README.md) · [Back to Provenance](../../README.md)

</div>
