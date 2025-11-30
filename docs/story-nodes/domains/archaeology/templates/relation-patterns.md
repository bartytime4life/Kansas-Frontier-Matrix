---
title: "🏺 KFM v11.2.2 — Archaeology Story Node Relation Patterns"
path: "docs/story-nodes/domains/archaeology/templates/relation-patterns.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:archaeology:relationpatterns:v11.2.2"
semantic_document_id: "kfm-storynodes-archaeology-relpatterns"
event_source_id: "ledger:storynodes/archaeology/templates/relationpatterns"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/storynode-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/storynodes-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Relation Pattern Guide"
intent: "kfm-archaeology-storynode-relpatterns"
lifecycle_stage: "stable"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked"
classification: "Generalized / Public-Safe"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by future v12 domain rewrite"
---

<div align="center">

# 🔗 **Archaeology Story Node — Relation Patterns (KFM v11)**  
### *Safe Graph Modeling for Sites, Features, Surveys, Excavations & Interpretations*  

`docs/story-nodes/domains/archaeology/templates/relation-patterns.md`

**Purpose**  
Provide **canonical, governed relation patterns** for archaeology Story Nodes  
to ensure safe, consistent, ontology-aligned graph connections across KFM.

</div>

---

## 📘 Overview

Archaeology Story Nodes rely heavily on structured relations to:

- link **sites**, **features**, **events**, **documents**, and **people**,  
- support **Focus Mode v3**,  
- preserve **provenance** (PROV-O),  
- maintain **CIDOC-CRM** alignment,  
- enforce **FAIR+CARE** and **sovereignty rules**.

All patterns below are **safe**, **public-ready**, and **approved** for the archaeology domain.

**Prohibited:**  
- any relation implying precise unpublished locations  
- any relation exposing burial/sacred features  
- any relation implying undocumented cultural affiliation  

---

## 🔗 Relation Pattern Library (KFM v11)

Each pattern includes:

- **Relation Type** (`rel`)  
- **Meaning**  
- **CIDOC-CRM / standards alignment**  
- **Usage Rules**  
- **Example Snippet**  

---

## 🧱 1. Primary Association

### **`rel: "about"`**  
**Meaning:** This Story Node is about a site, feature, or excavation/survey event.  
**CIDOC:** `E7 Activity`, `E18 Physical Thing`, `E27 Site`  
**Rules:**  
- Exactly **one** primary `about` target.  
- For multi-phase sites: use separate Story Nodes per phase.  
- Never use this to point at unpublished internal site numbers.

**Example:**
~~~json
{
  "rel": "about",
  "id": "place:arch-ks-165-lower-walnut-village"
}
~~~

---

## 📚 2. Documentation & Reference Links

### **`rel: "references"`**  
**Meaning:** The Story Node cites a document, dataset, or publication.  
**CIDOC:** `E31 Document`  
**Rules:**  
- Use for published reports, articles, accessible datasets.  
- Never reference restricted/internal forms.  
- Use STAC/DCAT hints when possible.

**Example:**
~~~json
{
  "rel": "references",
  "id": "doc:kshs-archaeology-report-1973"
}
~~~

---

## 🪶 3. Counter-Interpretations

### **`rel: "counterpoint"`**  
**Meaning:** This Story Node presents an updated or contested interpretation.  
**CIDOC:** `E13 Attribute Assignment`  
**Rules:**  
- Use only when reinterpretations are documented.  
- Do not “invent” counterpoints using AI.  
- Must include explanation in narrative.

**Example:**
~~~json
{
  "rel": "counterpoint",
  "id": "story:arch-ks-165-village-phase-1"
}
~~~

---

## 🧱 4. Part–Whole Structure (Sites, Features, Phases)

### **`rel: "part-of"`**  
**Meaning:** This node describes a sub-component (feature, locus, context, phase).  
**CIDOC:** `P46 is composed of`  
**Rules:**  
- Safe when detailing general site structure.  
- Must not expose burial/sacred feature details.  
- Mask spatial extents appropriately.

**Example:**
~~~json
{
  "rel": "part-of",
  "id": "place:arch-ks-089-river-bluff-site"
}
~~~

---

## 🏺 5. Event Participation (Surveys, Excavations)

### **`rel: "carried-out-by"`**  
**Meaning:** Links an event to a person/organization.  
**CIDOC:** `P14 carried out by`  
**Rules:**  
- Use only for documented survey/excavation events.  
- Use organization-level IDs unless public-facing individuals are appropriate.

**Example:**
~~~json
{
  "rel": "carried-out-by",
  "id": "org:kansas-anthropological-association"
}
~~~

---

### **`rel: "participated-in"`**  
**Meaning:** A person participated in an archaeological activity.  
**CIDOC:** `P11 had participant`  
**Rules:**  
- Use sparingly for public-safe contributors.  
- Omit volunteers unless public records already list them.

**Example:**
~~~json
{
  "rel": "participated-in",
  "id": "person:john-doe"
}
~~~

---

## 🌎 6. Place Relationships

### **`rel: "located-in"`**  
**Meaning:** General location relationship at coarse scale.  
**CIDOC:** `P89 falls within`  
**Rules:**  
- Only use for H3 cells, counties, watersheds, or published public parks.

**Example:**
~~~json
{
  "rel": "located-in",
  "id": "region:kansas-arkansas-river-basin"
}
~~~

---

## ⚖ 7. Sovereignty & Sensitive Information

### **`rel: "requires-review"`**  
**Meaning:** Marks a Story Node or linked asset requiring CARE / tribal review.  
**CIDOC:** `E30 Right`  
**Rules:**  
- Always include for Indigenous-linked or culturally sensitive material.  
- CI will block merge until reviewer approval.

**Example:**
~~~json
{
  "rel": "requires-review",
  "id": "policy:indigenous-data-sovereignty"
}
~~~

---

## 🧩 Valid Relation Matrix (Quick Reference)

~~~text
about             → site, feature, event  
references        → publications, datasets, reports  
counterpoint      → reinterpretations  
part-of           → features, contexts, phases  
carried-out-by    → organizations, documented people  
participated-in   → documented participants  
located-in        → regions, counties, H3 cells  
requires-review   → sovereignty/CARE policy nodes
~~~

---

## 🕰️ Version History

| Version | Date       | Summary                                                           |
|--------:|------------|-------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed relation-pattern library for archaeology Story Nodes. |
| v11.2.1 | 2025-11-29 | Added pattern scaffolding and CIDOC/GeoSPARQL mappings.             |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

