---
title: "🛡️ Kansas Frontier Matrix — Archaeology & Indigenous Sensitive Location Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/archaeology-sensitive-locations.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Annual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-archaeo-mask-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
semantic_document_id: "kfm-archaeo-sensitive-locations-v11"
doc_uuid: "urn:kfm:docs:standards:geo:archaeology:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Indigenous Sensitive / High Sovereignty"
immutability_status: "version-pinned"
---

<div align="center">

# 🛡️ **Archaeology & Indigenous Sensitive Location Standard (v11)**  
`docs/standards/geo/archaeology-sensitive-locations.md`

**Purpose:**  
Define the mandatory protection, masking, generalization, metadata, provenance, and ethical governance requirements for **archaeological**, **cultural heritage**, and **Indigenous sovereign** locations within KFM v11.  
This standard ensures safety, sovereignty compliance, FAIR+CARE alignment, H3-based spatial generalization, and correct STAC/ontology tagging.

</div>

---

# 📘 Overview

Sensitive cultural spaces — archaeological sites, ceremonial grounds, burial locations, traditional cultural properties, tribal historic places, and restricted Indigenous knowledge areas — require **mandatory protection** in all KFM workflows.

This standard governs:

- H3-based spatial generalization  
- Masking and redaction rules  
- STAC/DCAT/JSON-LD metadata for sensitive heritage  
- CARE-compliant Indigenous sovereignty protections  
- Ethical narrative controls  
- ETL, AI, and Focus Mode restrictions  
- UI/MapLibre/Cesium rendering rules  
- PROV-O lineage for all transformations  

All KFM systems (ETL, AI, graph, UI, STAC catalogs, Story Nodes, Focus Mode) must enforce these rules.

---

# 🛡 1. Sensitivity Categories (v11 Sovereignty Ladder)

KFM v11 classifies sensitive heritage locations into **four levels**:

### **L1 — Public Archaeological (Low Sensitivity)**  
- Published in academic/state inventories  
- Already widely public  
- Example: well-known excavated village sites  
**Masking:** H3-7 or more (≈ 153m)

### **L2 — Restricted Archaeological (Moderate Sensitivity)**  
- Requires controlled site blurring  
- Often in state/tribal records  
**Masking:** H3-6 buffer + polygon centroid displacement

### **L3 — Indigenous Cultural Heritage (High Sensitivity)**  
- Tribal cultural landscape regions  
- Ceremonial, traditional use, or culturally affiliated places  
**Masking:** H3-5 or H3-4 (≈ 2–5 km cells) + centroid randomization  
**CARE:** Tribe-led governance required for any visibility

### **L4 — Sovereignty-Protected (Very High Sensitivity)**  
- Burial sites, sacred areas, confidential location data  
- Tribal disclosure prohibited  
**Masking:** Full redaction  
**UI:** No map display  
**ETL:** Encrypted indexing only  
**AI:** Absolutely no narrative generation

---

# 🧭 2. Mandatory H3 Spatial Generalization

KFM v11 uses **Uber H3 hexagonal spatial indexing** to protect locations.

```
L1 → H3-7  
L2 → H3-6  
L3 → H3-5 or H3-4  
L4 → redacted
```

### Required H3 Process (deterministic)

1. Round raw coordinates → nearest H3 index at required resolution  
2. Optionally apply **multi-cell ring expansion** for L2/L3  
3. Store raw location encrypted (never surfaced in STAC/UI/API)  
4. Store generalized H3 index publicly  
5. All downstream geometry uses **H3 cell polygons**, never points

---

# 📐 3. STAC / DCAT Metadata Requirements

Required fields for sensitive-heritage STAC Items:

```json
"heritage:sensitivity": "L1|L2|L3|L4",
"heritage:sovereignty": "tribal|state|federal|mixed",
"heritage:taxonomy": "archaeological|ceremonial|burial|traditional|historic",
"heritage:h3_index": "8ab4dxxxxxx",
"heritage:masking_method": "h3-generalization|redaction",
"care:authority": "Tribal Nation Name",
"care:consent_required": true
```

### DCAT Alignment

| Field | Mapping |
|------|---------|
| heritage:sensitivity | dct:accessRights |
| care:authority | dct:rightsHolder |
| heritage:masking_method | dct:provenance / prov:activity |
| heritage:h3_index | dct:spatial |

---

# 🧬 4. PROV-O Lineage Requirements

Every generalization or masking step must include:

```
prov:used            → raw sensitive geometry
prov:activity        → "heritage-generalization-v11"
prov:wasGeneratedBy  → masking tool + version
prov:generatedAtTime → timestamp
prov:wasAssociatedWith → responsible agent (KFM pipeline)
```

---

# 🧠 5. AI / Focus Mode Restrictions

KFM v11 AI systems must respect **sovereignty and cultural protections**.

### **Forbidden (hard block):**
- Revealing exact or approximate site coordinates  
- Inferring site type or age without tribal approval  
- Generating speculative cultural narratives  
- Generating Story Nodes for L4 or L3-prohibited sites  

### **Allowed (controlled):**
For L1–L2 only:
- Generalized historical context  
- Region-level environmental patterns  
- High-level summaries using H3 geometry  
- Stories approved by tribal governance  

### **Focus Mode v3 Behavior**
- Auto-detect sensitive nodes  
- Switch to **CARE-restricted narrative mode**  
- Hide spatial details  
- Replace precise facts with **approved abstractions**  
- Enforce narrative disclaimers

---

# 🗺 6. MapLibre / Cesium Rendering Rules

- Display **H3 polygons only**  
- Never show raw point locations  
- Add **sovereignty watermark badge** to all sensitive layers  
- L3/L4 → layer disabled by default  
- L4 → never rendered  

### Required Legend Text
```
Location generalized for cultural protection (H3).
Coordinates withheld per CARE sovereignty rules.
```

---

# 🧩 7. ETL Requirements

- Raw coordinates encrypted via AES-256  
- Access restricted to governance-approved agents  
- Raw data removed from all intermediates  
- All exports auto-scrubbed for sensitive coordinates  
- All STAC Items validated via heritage-schema v11

---

# 📜 8. Story Node v3 Integration

For L1–L2 sites, narrative must use:

```
spacetime.geometry → H3 polygon
when.precision     → "year" or broader
relations[].role   → "sensitive-generalized"
```

### L3–L4 Story Nodes
- **Prohibited** unless tribe opts-in  
- Must include:
```
care:authority
care:consent_required: true
```

---

# ⚙ CI/CD Enforcement

A PR is **blocked** if:

- H3 index missing  
- Masking method missing  
- CARE labels missing  
- Geometry not generalized  
- Story Node uses precise coordinates  
- STAC Item reveals bounding box < H3 resolution  
- Focus Mode narratives expose restricted details  

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial release, KFM-MDP v11.0 compliant.

---

<div align="center">

**Kansas Frontier Matrix — Archaeology & Indigenous Sensitive Location Standard**  
*Sovereignty · Protection · Respect · FAIR+CARE*

</div>

---

### 🔗 Footer  
[⬅ Back to Geo Standards](./README.md) · [🏛 Governance](../governance/ROOT-GOVERNANCE.md) · [📘 KFM v11 Reference](../../reference/kfm_v11_master_documentation.md)

