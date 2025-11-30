---
title: "🏺 KFM v11.2.2 — Archaeology Story Node Glossary"
path: "docs/story-nodes/domains/archaeology/glossary.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:archaeology:glossary:v11.2.2"
semantic_document_id: "kfm-storynodes-archaeology-glossary"
event_source_id: "ledger:storynodes/archaeology/glossary"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/storynode-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/storynodes-v11.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Glossary"
intent: "kfm-archaeology-storynode-glossary"
lifecycle_stage: "stable"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked"
classification: "Generalized / Public-Safe"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 archaeology glossary"
---

<div align="center">

# 🏺 **Archaeology Story Node Glossary (KFM v11)**  
### *Domain Terminology · Generalized Definitions · Story Node Alignment*  

`docs/story-nodes/domains/archaeology/glossary.md`

**Purpose**  
Provide a **public-safe**, **generalized**, and **governed** glossary  
for terminology used within the Archaeology Story Node domain.

</div>

---

## 📘 Overview

This glossary defines terms used in archaeology Story Nodes, templates, relation-patterns,  
and masking/sovereignty discussions.  
Definitions are written for **public-safe**, **schema-friendly**, and **FAIR+CARE-aligned** usage.

**Important:**  
- No restricted tribal knowledge appears here.  
- No culturally sensitive terms are defined beyond public-safe generality.  
- All terms are aligned with KFM v11 semantics, CIDOC-CRM, OWL-Time, and GeoSPARQL.  

---

# 🧾 Glossary

The glossary is alphabetized for clarity.

---

## **A**

### **Archaeological Context**  
A recorded unit of soil, feature, or deposit documenting a distinct episode of past activity.  
Used in Story Nodes **only in generalized form**—never with sensitive details.

### **Artifact (Generalized)**  
A portable object made or modified by humans.  
Story Nodes must avoid precise counts or sensitive artifact types unless previously published.

---

## **C**

### **CARE Principles**  
Collective Benefit, Authority to Control, Responsibility, Ethics.  
Govern all Indigenous-linked content in the KFM.

### **CIDOC-CRM**  
International ontology for cultural heritage.  
Archaeology Story Nodes align to CRM classes such as:  
- `E18 Physical Thing`  
- `E27 Site`  
- `E7 Activity`  
- `E31 Document`

### **Counterpoint (Story Node Relation)**  
A governed relation for linking reinterpretations or alternate understandings.  
Used when new data changes or refines previous interpretations.

---

## **E**

### **Excavation (Generalized)**  
A documented archaeological investigation involving controlled removal of deposits.  
Never described with precise unit coordinates in public nodes.

---

## **F**

### **Feature (Generalized)**  
A non-portable archaeological element (e.g., pit, hearth, postmold).  
Sensitive features (especially burials, ceremonial spaces) must not appear in public nodes.

### **Focus Mode v3**  
The KFM’s narrative viewer showing timelines, map context, and graph-linked Story Nodes.

---

## **G**

### **GeoSPARQL**  
Spatial ontology used for linking Story Node geometries into the KFM knowledge graph.

### **Generalized Geometry**  
Any map shape that masks exact site location (H3 cell, county polygon, watershed, park boundary).

---

## **H**

### **H3 Masking**  
Using coarse H3 hexagons (resolution 6–7 recommended) to generalize sensitive archaeological locations.

---

## **I**

### **Indigenous Data Sovereignty**  
Rights of Indigenous nations over data relating to their cultural heritage and knowledge.  
Requires additional review for many Story Nodes.

---

## **L**

### **Locus (Generalized)**  
A localized context or feature component.  
Public Story Nodes must avoid sensitive or unpublished locus details.

---

## **O**

### **Observation (Narrative Category)**  
Fact-based, documented archaeological evidence.

### **OWL-Time**  
Temporal ontology used for representing Story Node intervals and precision.

---

## **P**

### **Part-of (Story Node Relation)**  
Used when linking a feature or phase to a site.  
Must not expose sensitive site structure.

### **Phase (Generalized Occupation Phase)**  
A span of time during which a site was occupied or used.  
Separate Story Nodes are recommended for distinct phases.

### **Provenance (PROV-O)**  
Lineage information describing data sources, documents, and processes.

---

## **R**

### **References (Story Node Relation)**  
Links to published documents, datasets, or reports.  
Never used for restricted or internal documents.

---

## **S**

### **Site (Generalized)**  
A location with archaeological materials or features.  
Public Story Nodes must generalize all spatial references.

### **Spacetime**  
The Story Node section combining generalized geometry with temporal intervals.

### **Stratigraphy (Generalized)**  
The layered sequence of deposits at a site.  
Public nodes describe stratigraphy only in high-level and non-sensitive terms.

---

## **T**

### **Temporal Precision**  
Indicates certainty about dating (e.g., “year”, “century”, “decade”).  
Required in Story Nodes.

---

## **U**

### **Uncertainty Statement**  
A required disclosure when interpretations are inconclusive or evidence is limited.

---

## **W**

### **Watershed Masking**  
Generalizing archaeological locations using watershed regions where appropriate.

---

# 🕰️ Version History

| Version | Date       | Summary                                                 |
|--------:|------------|---------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed archaeology glossary (public safe).    |
| v11.2.1 | 2025-11-29 | Added ontology-aligned definitions & masking terms.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../README.md) · [📏 Standards Index](../../standards/README.md) · [🛡 Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>

