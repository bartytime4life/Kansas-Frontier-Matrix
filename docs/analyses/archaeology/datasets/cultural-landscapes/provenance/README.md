---
title: "🧬 Kansas Frontier Matrix — Cultural Landscape Provenance Logs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-provenance-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Provenance Logs"
intent: "cultural-landscape-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Cultural Landscape Provenance Logs**  
`docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`

**Purpose:**  
Define and govern the **provenance logging system** for all cultural landscape datasets within the Kansas Frontier Matrix (KFM).  
These logs capture **data origins**, **GIS transformations**, **ethical reviews**, **sensitivity generalization procedures**, and **FAIR+CARE governance requirements** for:

- Settlement regions  
- Interaction spheres  
- Resource procurement areas  
- Ancient mobility corridors  
- Generalized territorial/cultural boundaries  
- Any culturally significant environmental landscape layer  

Provenance files here ensure transparency, cultural safety, reproducibility, and explainability across KFM pipelines, Story Nodes, and Focus Mode v2.

</div>

---

# 📘 Overview

Every cultural landscape dataset must produce a corresponding **PROV-O JSON-LD provenance record** stored in this directory.  
These logs document:

- Original data sources  
- Spatial generalization methods (H3, simplification)  
- Data cleaning & processing steps  
- Ethical and cultural reviews  
- Analyst and reviewer attribution  
- Versioning and lineage  
- Uncertainty, bias, and interpretive assumptions  
- Alignment with STAC Items + metadata  

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/provenance/
├── README.md                                # This file
├── great-bend-aspect-v2.json                # Provenance: Great Bend Aspect sphere
├── central-plains-exchange-v1.json          # Provenance: Central Plains exchange zone
├── protohistoric-wichita-v1.json            # Provenance: Protohistoric Wichita region
└── templates/                               # Provenance templates for contributors
~~~

---

# 🧭 Required PROV-O Components (All Provenance Logs)

### ✔ `@context`
Must include:
- `"prov"`  
- `"care"`  
- `"kfm"`  
- CIDOC-CRM terms where appropriate

### ✔ Entities (`prov:Entity`)

Must define at least:

| Entity | Description |
|---|---|
| `raw` | Original dataset — raster/vector/geojson, literature-derived shapes |
| `generalized` | Spatially de-identified version (H3 or simplified polygon) |
| `processed` | Cleaned + validated landscape representation |

### ✔ Activities (`prov:Activity`)

Typical activities include:

- `generalization`  
- `feature_extraction`  
- `boundary_estimation`  
- `tribal_review`  
- `faircare_review`  
- `geoprocessing`  
- `time_model_alignment`  

### ✔ Agents (`prov:Agent`)

Agents must include:

| Agent Type | Example |
|---|---|
| Analyst | Individual researcher or GIS specialist |
| Reviewer | FAIR+CARE Council |
| Tribal Reviewer | Required for protohistoric/historic contexts |
| Source Institution | Archive, map survey, academic source |

### ✔ Relations

- `prov:wasDerivedFrom`  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasAttributedTo`

These relations must describe the full lineage chain from raw input → processed output.

---

# ⚖️ CARE Cultural Safety Requirements

All provenance logs for cultural landscapes must include:

| CARE Field | Purpose |
|---|---|---|
| `care:sensitivity` | `"generalized"` or `"restricted-generalized"` |
| `care:review` | `"faircare"` or `"tribal"` |
| `care:notes` | Describe cultural considerations |
| `care:visibility_rules` | `"h3-only"`, `"polygon-generalized"`, `"no-exact-boundaries"` |

**Forbidden content:**

- `"restricted"` (never allowed in public dataset provenance)  
- Exact depictions of ceremonial areas  
- Burial ground outlines  
- Sensitive ethnographic knowledge  

---

# 🧪 Example Provenance Snippet

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },
  "prov:Entity": {
    "raw": {
      "prov:label": "Initial landscape region from ethnohistoric mapping",
      "prov:type": "Dataset",
      "kfm:source": "Historical Atlas 1899"
    },
    "generalized": {
      "prov:label": "Generalized region (H3 level 6)",
      "prov:type": "Dataset",
      "care:notes": "Exact cultural boundaries removed."
    },
    "processed": {
      "prov:label": "Processed cultural landscape dataset v2",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v2"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "Generalization",
      "prov:startTime": "2025-10-14T13:22:00Z",
      "prov:endTime": "2025-10-14T14:05:00Z",
      "kfm:steps": ["H3 grid derivation", "polygon simplification"]
    },
    "review": {
      "prov:type": "Review",
      "prov:label": "FAIR+CARE ethics & tribal cultural review",
      "prov:endTime": "2025-10-15T17:40:00Z"
    }
  },
  "prov:Agent": {
    "analyst": { "prov:label": "A. Barta", "prov:type": "Person" },
    "faircare": { "prov:label": "FAIR+CARE Council", "prov:type": "Group" },
    "tribal": { "prov:label": "Tribal Heritage Office", "prov:type": "Group" }
  },
  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "generalized", "prov:usedEntity": "raw" },
    { "prov:generatedEntity": "processed", "prov:usedEntity": "generalized" }
  ],
  "care:sensitivity": "generalized",
  "care:review": "tribal",
  "care:notes": "Generalization required to protect culturally sensitive landscapes.",
  "care:visibility_rules": "polygon-generalized"
}
~~~

---

# 🧠 Integration Into the KFM Ecosystem

### **Knowledge Graph**

Nodes created:
- `LandscapeRegion`  
- `GeneralizedRegion`  
- `ProvenanceActivity`  
- `ReviewEvent`  
- `CulturalSensitivityLevel`

Edges:
- `GENERALIZED_FROM`  
- `PRODUCED_BY`  
- `REVIEWED_BY`  
- `HAS_SENSITIVITY`  
- `HAS_PROVENANCE`  

### **Story Nodes**
Provenance drives:
- Narrative transparency  
- Cultural attribution reasoning  
- Movement & interaction context stories  

### **Focus Mode v2**
Uses provenance for:
- Explainability overlays  
- Ethical flag injection  
- Provenance chips in UI panels  

---

# 🧪 Validation Requirements

Provenance logs must pass:

- PROV-O structural validation  
- CARE schema validation  
- KFM archaeology provenance rules  
- Metadata ↔ STAC ↔ provenance crosswalk  
- CI workflows:
  - `metadata-validate.yml`
  - `artifact-stac-validate.yml`
  - `faircare-audit.yml`

CI blocks ingestion if:

- Provenance missing  
- CARE sensitivity incorrect  
- No tribal review for protohistoric data  
- Spatial generalization not documented  

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Added complete provenance logging standard with CARE + PROV-O integration |
| v10.0.0 | 2025-11-10 | Landscape Provenance Team | Initial directory scaffolding |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Cultural Landscape Datasets](../README.md)

</div>