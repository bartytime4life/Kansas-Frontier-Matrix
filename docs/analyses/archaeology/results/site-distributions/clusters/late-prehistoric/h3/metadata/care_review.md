---
title: "🛡️ Kansas Frontier Matrix: Late Prehistoric H3 CARE Review Log"
path: "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/metadata/care_review.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / FAIR+CARE Council & Tribal Partners"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/archaeology-late-prehistoric-h3-care-review-v1.json"
governance_ref: "../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "CARE Review"
intent: "archaeology-h3-care-log"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Governed / Cultural Sovereignty"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "Archaeology Working Group · FAIR+CARE Council"
risk_category: "Cultural Sensitivity Review"
redaction_required: true
provenance_chain:
  - "docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/metadata/care_review.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E30 Right"
  schema_org: "CreativeWork"
  prov_o: "prov:Activity"
json_schema_ref: "../../../../../../../../../../schemas/json/archaeology-late-prehistoric-h3-care-review.schema.json"
shape_schema_ref: "../../../../../../../../../../schemas/shacl/archaeology-late-prehistoric-h3-care-review-shape.ttl"
doc_uuid: "urn:kfm:doc:archaeology:care-review:late-prehistoric-h3-v11.0.0"
semantic_document_id: "kfm-care-review-late-prehistoric-h3"
event_source_id: "ledger:docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/metadata/care_review.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "cultural-interpretation-without-source"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Internal / CARE-Governed"
role: "archaeology-care-review-late-prehistoric-h3"
lifecycle_stage: "active"
ttl_policy: "Reviewed every 6 months"
sunset_policy: "Superseded upon next CARE review cycle"
---

<div align="center">

# 🛡️ **Late Prehistoric H3 Cluster CARE Review Log**  
`docs/analyses/archaeology/results/site-distributions/clusters/late-prehistoric/h3/metadata/care_review.md`

**Purpose:**  
Document the **CARE review process**, cultural sovereignty considerations, redaction decisions, and tribal governance approvals associated with the Late Prehistoric H3 generalizations.

![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This CARE review log documents:

- Cultural sensitivity assessments  
- Tribal consultation notes  
- Redaction and masking decisions  
- Sovereignty-based restrictions  
- Required H3 generalization levels  
- Any conditions placed on public release  

All Late Prehistoric H3 outputs **must** undergo CARE review before public display.

---

## 🧭 CARE Principles Applied

### **C1 — Collective Benefit**
- Data and visualizations must support heritage preservation, community education, and collaborative research.  
- No outputs should benefit external actors at the expense of descendant communities.

### **C2 — Authority to Control**
- Tribes determine whether specific clusters require redaction, masking, or suppression.  
- Any H3 cell intersecting restricted landscapes is automatically upgraded to a coarser generalization (r7 or above).  
- Certain areas may be withheld from public layers.

### **C3 — Responsibility**
- Analysts must document how uncertainty, survey biases, and cultural significance are handled in modeling.  
- Sensitive interpretations must be flagged for additional review.

### **C4 — Ethics**
- Cultural contexts must be represented fairly, without speculation or colonial framing.  
- No attribution of cultural meaning is allowed unless directly sourced from descendant community input or verified ethnographic records.

---

## 🔐 Cultural Sensitivity Review Notes

Below is the template reviewers must fill during each CARE cycle:

### **1. Cultural Landscape Intersections**
- Describe landscapes included in the clusters (e.g., river terraces, ceremonial landscapes).  
- Identify areas requiring masking or aggregation.

### **2. Tribal Partner Feedback**
- Summary of consultation outcomes  
- Requested redactions  
- Required disclaimers  
- Sensitivity comments  

### **3. Required Generalization Level**
- `r7` (public-safe default)  
- `r8` (use when landscapes are less sensitive)  
- `Collapsed Region` (for highly sensitive areas)

### **4. Restrictions on Public Use**
- Whether certain cells must be omitted  
- Whether distribution summaries require additional disclaimers  
- Additional governance notes for Focus Mode rendering

### **5. Narrative Restrictions**
- Forbidden narrative interpretations  
- Required contextual notes for Focus Mode  
- Additional CARE framing instructions

---

## 🧬 Provenance & Lineage Integration

CARE review decisions must be logged in:

- `transformations-log.csv`  
- STAC Item `care:sensitivity` fields  
- Neo4j provenance graph (`prov:Activity`)  
- Story Node annotations where relevant  

All actions must maintain **auditability** and **traceability** under KFM governance.

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary |
|--------:|------------|------------------------------------------|---------|
| v11.0.0 | 2025-11-17 | FAIR+CARE Council · Archaeology WG       | Initial CARE review log for Late Prehistoric H3 clusters. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
CARE Review Record · Internal Cultural Safety Governance  
FAIR+CARE Certified · MCP-DL v6.3 Compatible  

[Back to Metadata](../README.md) · [Back to H3 Directory](../../README.md)

</div>
