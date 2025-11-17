---
title: "🧬 Kansas Frontier Matrix — Interaction Sphere Provenance Logs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review (when required)"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-interaction-spheres-provenance-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Provenance Index"
intent: "interaction-sphere-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant (Variable Sensitivity)"
---

<div align="center">

# 🧬 **Interaction Sphere Provenance Logs**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/README.md`

**Purpose:**  
Serve as the **authoritative provenance index** for all Interaction Sphere datasets within the Kansas Frontier Matrix (KFM).  
Provenance logs document:

- Cultural interpretations  
- GIS processing  
- Generalization & obfuscation  
- CARE/Tribal review workflows  
- Dataset lineage  
- Ethical decisions  
- Scientific + narrative assumptions  

Provenance is mandatory for **every** Interaction Sphere dataset and is essential for FAIR+CARE governance, transparency, reproducibility, and ethical AI interpretation.

</div>

---

# 📘 Overview

Interaction Spheres represent culturally significant, multi-era networks of:

- Exchange  
- Movement  
- Social co-presence  
- Settlement interconnectivity  
- Cultural diffusion  

Because these datasets involve **culturally sensitive** domains across multiple descendant communities, provenance logging must be:

- **Comprehensive**  
- **Machine-readable (PROV-O JSON-LD)**  
- **Ethically contextualized**  
- **FAIR+CARE reviewed**  
- **Generalization-aware**  
- **Properly versioned**

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/
├── README.md                                 # This file
├── great-bend-aspect-v2.json                 # Provenance for Great Bend Aspect Interaction Sphere
├── central-plains-exchange-v1.json           # Provenance for Central Plains Exchange Interaction Sphere
├── protohistoric-wichita-v1.json             # Provenance for Protohistoric Wichita (high-sensitivity)
└── templates/                                # Templates for creating new provenance records
~~~

---

# 🧩 Required PROV-O Components

All provenance logs MUST include:

### ✔ `@context`
With definitions for:
- `"prov"`
- `"care"`
- `"kfm"`
- `"dct"` (for crosswalk with DCAT)
- `"crm"` (optional; for CIDOC-CRM alignment)

---

### ✔ `prov:Entity`

Each provenance file must define:

| Entity | Notes |
|---|---|
| `raw` | Original open-data sources, generalized from literature/archaeology/ethnohistory |
| `generalized` | Spatially obfuscated version (H3 or simplified polygons) |
| `processed` | Final dataset used by KFM |

Optional:
- `interpretive` — When cultural synthesis requires model-based inference

---

### ✔ `prov:Activity`

Required activity types include:

| Activity | Description |
|---|---|
| `generalization` | H3 or polygon simplification process |
| `cleaning` | Attribute harmonization, CRS normalization |
| `integration` | Combining multi-source archaeological/literary evidence |
| `ethics_review` | FAIR+CARE + Tribal review steps |
| `modeling` | Environmental/diffusion modeling steps (if applicable) |

Each activity must include:
- `prov:startTime`
- `prov:endTime`
- `kfm:steps` (array of processing steps)
- `prov:type`

---

### ✔ `prov:Agent`

Agents must represent:

| Agent Type | Examples |
|---|---|
| Analyst | GIS specialist, archaeologist |
| FAIR+CARE Reviewer | Independent reviewers or KFM Council |
| Tribal Reviewer | Required for protohistoric or high-sensitivity spheres |
| Source Institution | KHS, PD archives, research teams |

---

### ✔ Lineage Relationships

All provenance files MUST include:

- `prov:wasDerivedFrom` — raw → generalized → processed  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasAttributedTo`  

These form the backbone of the reproducible data lineage.

---

# ⚖️ CARE Cultural Safety Requirements

Interaction Sphere datasets frequently intersect with restricted cultural knowledge.  
Therefore:

### Mandatory:
- `care:sensitivity: "generalized"` or `"restricted-generalized"`
- For protohistoric/wider-contact datasets: `care:review: "tribal"`
- `care:notes` describing ethical considerations  
- `care:visibility_rules`:  
  - `"h3-only"` for high sensitivity  
  - `"polygon-generalized"` for standard datasets

### Forbidden:
- `"restricted"` sensitivity level  
- Exact cultural boundaries  
- Publication of specific sacred or ceremonial sites  

---

# 🧪 Provenance Example (Excerpt)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },
  "prov:Entity": {
    "raw": {
      "prov:label": "Historical synthesis of CPT exchange patterns",
      "kfm:source": "Open archaeological synthesis (PD)"
    },
    "generalized": {
      "prov:label": "Generalized interaction sphere (H3-6)",
      "care:notes": "Boundaries generalized to protect cultural sovereignty."
    },
    "processed": {
      "prov:label": "Central Plains Exchange Sphere v1",
      "kfm:provenance_version": "v1"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "Generalization",
      "prov:startTime": "2025-10-15T10:22:00Z",
      "prov:endTime": "2025-10-15T10:47:00Z",
      "kfm:steps": ["H3 index derivation", "polygon simplification"]
    }
  },
  "prov:Agent": {
    "analyst": { "prov:label": "A. Barta" },
    "faircare": { "prov:label": "FAIR+CARE Council" }
  },
  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "generalized", "prov:usedEntity": "raw" },
    { "prov:generatedEntity": "processed", "prov:usedEntity": "generalized" }
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare"
}
~~~

---

# 🧠 Integration Into KFM

### Knowledge Graph
Provenance populates:

- `InteractionSphere` nodes  
- `GeneralizedRegion` nodes  
- `ProvenanceActivity` nodes  
- `ReviewEvent` nodes  

Relationships:
- `GENERALIZED_FROM`  
- `HAS_PROVENANCE`  
- `REVIEWED_BY`  
- `CARE_SENSITIVITY`  
- `ASSOCIATED_WITH`

### Story Nodes
Used for:

- Cultural narratives  
- Exchange/mobility story arcs  
- Ethical warnings  
- Time-depth explanations  

### Focus Mode v2
Provides:

- Provenance chips  
- Ethical sensitivity banners  
- Explanation-level transparency  

---

# 📊 Provenance Index

| Dataset | Version | Sensitivity | Review Type | Status |
|---|---|---|---|---|
| Great Bend Aspect | v2 | generalized | FAIR+CARE | 🟢 Active |
| Central Plains Exchange | v1 | generalized | FAIR+CARE | 🟢 Active |
| Protohistoric Wichita | v1 | restricted-generalized | Tribal Required | 🟡 Needs Review |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Fully defined Interaction Sphere provenance standards; added tribal review enforcement |
| v10.0.0 | 2025-11-10 | Landscape Provenance Team | Initial provenance directory structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Tribal Review Required (when applicable)  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Interaction Spheres](../README.md)

</div>