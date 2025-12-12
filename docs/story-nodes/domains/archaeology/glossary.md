---
title: "🏺 KFM v11.2.6 — Archaeology Story Node Glossary"
path: "docs/story-nodes/domains/archaeology/glossary.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Glossary"
header_profile: "standard"
footer_profile: "standard"

intent: "kfm-archaeology-storynode-glossary"
lifecycle_stage: "stable"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:storynodes:archaeology:glossary:v11.2.6"
semantic_document_id: "kfm-storynodes-archaeology-glossary-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/archaeology/glossary.md"
immutability_status: "version-pinned"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/storynodes-v11.json"

schema_ref: "../../../../schemas/json/story-node.schema.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked (Public-Safe Glossary)"
classification: "Generalized / Public-Safe"
sensitivity: "Cultural heritage terminology (generalized)"
sensitivity_level: "Moderate"
public_exposure_risk: "Low (when generalization rules are followed)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Archaeology Domain Board + Indigenous Data Governance Board"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 archaeology glossary"

metadata_profiles:
  - "CIDOC-CRM (alignment)"
  - "GeoSPARQL (alignment)"
  - "OWL-Time (alignment)"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/archaeology/glossary.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🏺 **Archaeology Story Node Glossary (KFM v11.2.6)**  
### *Domain Terminology · Generalized Definitions · Story Node Alignment*  

`docs/story-nodes/domains/archaeology/glossary.md`

**Purpose**  
Provide a **public-safe**, **generalized**, and **governed** glossary  
for terminology used within the Archaeology Story Node domain.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Glossary-Governed-brightgreen" />
<img src="https://img.shields.io/badge/CARE-Sensitive-gold" />

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 🏺 archaeology/
            ├── 📄 README.md
            ├── 📄 glossary.md                      # This file
            ├── 📝 notes/
            │   ├── 📄 README.md
            │   ├── 📄 backlog.md
            │   └── ⚖️ ethics-checklist.md
            └── 🧩 templates/
                ├── 📄 README.md
                ├── 📝 story-node-archaeology.md
                ├── 🧩 story-node-archaeology.json
                └── 🔗 relation-patterns.md
~~~

---

## 📘 Overview

This glossary defines terms used in archaeology Story Nodes, templates, relation patterns,  
and masking/sovereignty discussions.

Definitions are written to be:

- **public-safe** (non-targetable, generalized)
- **schema-friendly** (usable in `story-node.schema.json` authored content)
- **FAIR+CARE-aligned** (sovereignty-aware terminology)

**Safety constraints (normative)**

- No restricted tribal knowledge appears here.
- No sensitive site-locating details appear here.
- Terms are generalized and aligned (where applicable) with:
  - CIDOC-CRM (cultural heritage)
  - OWL-Time (time intervals + precision)
  - GeoSPARQL (geometry semantics)
  - PROV-O (provenance framing)

---

## 🧾 Glossary

The glossary is alphabetized for clarity.

### A

**Archaeological Context**  
A recorded unit of deposit, feature, or observation documenting a distinct episode of past activity.  
In Story Nodes, contexts are described **only in generalized form** (no unit grids, no precise coordinates).

**Artifact (Generalized)**  
A portable object made, used, or modified by humans.  
Story Nodes MUST avoid precise counts or sensitive artifact types unless already published and non-sensitive.

---

### C

**CARE Principles**  
Collective Benefit, Authority to Control, Responsibility, Ethics.  
These principles govern Indigenous-linked and culturally sensitive archaeology content.

**CIDOC-CRM**  
An international ontology for cultural heritage. Archaeology Story Nodes commonly align to classes such as:  
- `E18 Physical Thing`  
- `E27 Site`  
- `E7 Activity`  
- `E31 Document`

**Counterpoint** *(Story Node relation)*  
A governed relation linking reinterpretations or alternate understandings.  
Used only when reinterpretations are documented and public-safe.

---

### E

**Excavation (Generalized)**  
A documented archaeological investigation involving controlled removal of deposits.  
Public Story Nodes MUST NOT include unit-level spatial details or internal form fields.

---

### F

**Feature (Generalized)**  
A non-portable archaeological element (e.g., pit, hearth, postmold) described at a coarse level.  
Sensitive features (burials, ceremonial spaces, sacred contexts) MUST NOT appear in public-safe nodes.

**Focus Mode v3**  
KFM’s narrative viewer that renders timelines, generalized map context, and graph-linked Story Nodes.

---

### G

**GeoSPARQL**  
A spatial ontology used to represent and relate geometries in the KFM knowledge graph.

**Generalized Geometry**  
Any spatial representation that masks exact site location (H3 cells, county polygons, watersheds, broad regions).  
Generalized geometries MUST be non-targetable.

---

### H

**H3 Masking**  
Using coarse H3 hexagons to generalize sensitive archaeological locations.  
Recommended practice is to use sufficiently coarse resolution to prevent reverse engineering.

---

### I

**Indigenous Data Sovereignty**  
Rights of Indigenous nations over data relating to their cultural heritage, lands, and knowledge.  
Many archaeology Story Nodes require consultation and additional review under sovereignty policy.

---

### L

**Locus (Generalized)**  
A localized context or feature component described without publishing sensitive detail.  
Public Story Nodes MUST avoid unpublished locus identifiers and precise spatial descriptors.

---

### M

**Masking Level**  
A declared generalization strength applied to geometry or assets (e.g., H3 resolution, county-level, watershed-level).  
Masking level MUST be consistent with the sensitivity of the content and stated in the Story Node.

---

### O

**Observation** *(Narrative category)*  
Fact-based, documented archaeological evidence (what is recorded or published).

**OWL-Time**  
A temporal ontology used for representing Story Node intervals and precision categories.

---

### P

**Part-of** *(Story Node relation)*  
Used to link a feature or phase node to a generalized parent site or landscape node.  
This relation MUST NOT be used to expose sensitive internal site structure.

**Phase (Generalized occupation phase)**  
A span of time during which a site or landscape was occupied or used.  
Separate Story Nodes are recommended for distinct phases (safer modeling + clearer timelines).

**Provenance (PROV-O)**  
Lineage information describing sources, documents, and processes that inform the Story Node.  
Provenance statements must remain public-safe and rights-aware.

---

### R

**References** *(Story Node relation)*  
Links to published documents, datasets, or reports.  
References MUST NOT point to restricted or internal-only documents.

---

### S

**Site (Generalized)**  
A location with archaeological materials or features.  
Public Story Nodes must generalize spatial references to prevent targeting.

**Spacetime**  
The Story Node component combining generalized geometry with temporal bounds and precision.

**Story Node**  
A governed narrative + metadata object that can be validated, indexed, and linked in the KFM graph.  
Story Nodes are authored to be evidence-led, provenance-aware, and safe for the declared classification.

**Stratigraphy (Generalized)**  
The layered sequence of deposits at a site.  
Public nodes describe stratigraphy only in high-level, non-sensitive terms.

---

### T

**Temporal Precision**  
A declared certainty level about dating (e.g., “year”, “decade”, “century”, “year-range”).  
Precision MUST match the actual dating method and available evidence.

---

### U

**Uncertainty Statement**  
A required disclosure when interpretations are inconclusive, evidence is limited, or records conflict.  
Uncertainty MUST be explicit and must not be replaced with speculation.

---

### W

**Watershed Masking**  
Generalizing archaeological locations using watershed regions when appropriate for sensitivity and scale.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Upgraded to KFM-MDP v11.2.6; corrected relative refs; added directory layout; normalized headings (single H1). |
| v11.2.2 | 2025-11-30 | Initial governed archaeology glossary (public-safe).                     |
| v11.2.1 | 2025-11-29 | Added ontology-aligned definitions & masking terms.                      |

---

<div align="center">

🏺 **Archaeology Glossary (v11.2.6)**  
Public-Safe Terminology · Ontology-Aligned · Governance-Ready

[🏺 Archaeology Domain](./README.md) ·
[🧩 Templates Index](./templates/README.md) ·
[🔗 Relation Patterns](./templates/relation-patterns.md) ·
[📝 Notes Index](./notes/README.md) ·
[⚖️ Ethics Checklist](./notes/ethics-checklist.md) ·
[📋 Backlog](./notes/backlog.md) ·
[📚 Story Nodes Root](../README.md) ·
[📘 Docs Root](../../README.md) ·
[📘 Markdown Protocol](../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[🛡 Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🧾 Story Node Schema](../../../schemas/json/story-node.schema.json)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>
