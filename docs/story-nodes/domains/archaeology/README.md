---
title: "🏺 KFM v11.2.2 — Archaeology Story Node Domain (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/archaeology/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:story-nodes:archaeology:v11.2.2"
semantic_document_id: "kfm-storynodes-archaeology-domain"
event_source_id: "ledger:story-nodes/archaeology"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/storynode-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/storynodes-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Domain Specification"
intent: "kfm-archaeology-storynode-domain"
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

# 🏺 **Archaeology Story Node Domain (KFM v11)**  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
### *Generalized, Ethical, FAIR+CARE-Aligned Archaeological Narratives*  

`docs/story-nodes/domains/archaeology/README.md`

**Purpose**  
Define how archaeology-related Story Nodes must be authored, structured, masked, validated,  
and linked into the KFM graph and Focus Mode v3.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/story-nodes/domains/archaeology/
├── 📄 README.md                               # Domain overview & authoring rules
├── 📁 templates/                               # Authoring templates (MD + JSON)
│   ├── 📝 story-node-archaeology.md            # Human-facing template
│   ├── 🧩 story-node-archaeology.json          # JSON skeleton (schema-aligned)
│   └── 🔗 relation-patterns.md                 # Common graph relation patterns
├── 📁 examples/                                # Curated example Story Nodes
│   ├── 🏞️ protohistoric-wichita-site.json      # Generalized Protohistoric example
│   ├── 🧲 fort-larned-geophysics.json          # Non-invasive survey example
│   └── 📂 ...                                   # Additional examples
├── 📘 glossary.md                              # Archaeology-specific terminology
└── 📁 notes/                                   # Drafts, ethics, backlog
    ├── 📑 backlog.md                           # Candidate Story Nodes
    └── ⚖️ ethics-checklist.md                  # Sovereignty & CARE checklist
~~~

---

## 📘 Overview

This domain defines the **rules, structures, and constraints** for creating archaeology Story Nodes in KFM v11.

Archaeology Story Nodes must integrate:

- **Generalized spatial footprints** (never publish sensitive coordinates)  
- **Time intervals** with proper precision  
- **CIDOC-CRM**, **GeoSPARQL**, and **OWL-Time** alignment  
- **FAIR+CARE** and **Indigenous Sovereignty** rules  
- **STAC / DCAT** links for validated assets  
- **PROV-O provenance** for all referenced data  

They must be compatible with:

- Focus Mode v3  
- The Story Node JSON schema  
- Neo4j graph insertion patterns  
- MapLibre/Cesium rendering constraints  

---

## 🧠 Story Node Requirements

Archaeology Story Nodes **must**:

### **1. Use generalized geometries**
- County shapes, watershed regions, H3 masks (res 6–7 recommended).  
- Never reveal precise unprotected site coordinates.  
- Burial/sacred contexts always require **maximum masking**.

### **2. Distinguish observation / interpretation**
- Observation (recorded features, materials, stratigraphy)  
- Interpretation (supported by evidence)  
- Avoid speculation unless flagged as uncertain  

### **3. Maintain correct spacetime modeling**
- `spacetime.geometry` → generalized GeoJSON  
- `spacetime.when` → start, end, precision, original_label  
- Multi-phase sites → multiple Story Nodes or part-of relations  

### **4. Link properly into the knowledge graph**
Use `relations[]` for:
- `about` → site, feature, or excavation event  
- `references` → documents, reports, datasets  
- `counterpoint` → later reinterpretations  

### **5. Respect sovereignty rules**
Required for ANY Indigenous-linked content:
- CARE compliance  
- Tribal consultation requirements  
- Mandatory CI sovereignty checks  

---

## 🧭 Focus Mode Integration

Focus Mode v3 will:

- Center on the **generalized** geometry  
- Expand the timeline to include:
  - occupation phases  
  - survey events  
  - excavation seasons  
  - publication/reinterpretation events  
- Load graph neighbors (2-hop)  
- Present only **data-grounded**, **ethically-safe** narratives  

Nothing invented, inferred, or guessed by AI may be shown.

---

## 📦 Metadata & Provenance Rules

### **IDs**
Format (public-safe):
- `arch-ks-{county-fips}-{slug}-{nn}`

No state site numbers unless already public.

### **Assets**
Allowed:
- generalized site diagrams  
- non-sensitive field photos  
- geophysics rasters (masked)  

Prohibited:
- burial locations  
- sacred features  
- unpublished coordinates  
- internal site forms  

### **Required provenance**
- document sources  
- dataset IDs  
- processing steps  
- authors, dates  
- clearance / rights information when required  

---

## 🧪 Validation

CI/CD enforces:

- Story Node schema validation  
- STAC/DCAT link checks  
- Markdown protocol  
- Geometry masking checks  
- Sovereignty/CARE automated linting  
- Neo4j graph pattern validation for relations  

All archaeology additions require **manual Indigenous-data reviewer approval**.

---

## ⚖ FAIR+CARE Compliance

This domain is **Medium-Risk**, requiring:

- Generalization of spatial detail  
- Extra masking for burial/sacred sites  
- No cultural attributions without evidence  
- Strict transparency of uncertainty  
- Respect for tribal knowledge control  
- Data only used in ways aligned with **CARE** and community expectations  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|--------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed release; finalized emoji directory layout & v11.2.2 compliance. |
| v11.2.1 | 2025-11-29 | Added templates, examples, glossary, ethics notes; aligned to Story Node v11 schema. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
