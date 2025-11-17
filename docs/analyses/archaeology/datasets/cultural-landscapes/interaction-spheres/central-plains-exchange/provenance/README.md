---
title: "🔄🧬 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere Provenance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/provenance/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council (Tribal Review Not Required for This Sphere)"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-provenance-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Provenance Record Index"
intent: "cultural-landscape-interaction-sphere-central-plains-exchange-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant (Generalized)"
---

<div align="center">

# 🔄🧬 **Central Plains Exchange Interaction Sphere — Provenance Logs**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/provenance/README.md`

**Purpose:**  
Provide the authoritative **provenance index** for the **Central Plains Exchange Interaction Sphere** within the Kansas Frontier Matrix (KFM).  
These provenance records ensure complete transparency of:

- Dataset origins  
- GIS transformation and generalization  
- Cultural & ethical review  
- Methodological decisions  
- Data lineage (raw → generalized → processed)  
- FAIR+CARE governance compliance  

This dataset is *moderate sensitivity* (not protohistoric) and may be published after standard FAIR+CARE review.

</div>

---

# 📘 Overview

The provenance logs in this directory describe:

- Source data used to construct the interaction sphere  
- Generalization workflow (H3 + polygon simplification)  
- Archaeological interpretation basis  
- Paleoenvironmental & geomorphological context synthesis  
- Review by the FAIR+CARE Council  
- Model assumptions, bias limitations, uncertainty ranges  
- Dataset versioning and lineage  

These logs are formatted as **JSON-LD PROV-O documents**, enabling machine-readability and integration into ETL pipelines, Story Nodes, Focus Mode v2, and the KFM Knowledge Graph.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/provenance/
├── README.md                               # This file
└── central-plains-exchange-v1.json          # Provenance (PROV-O) for this dataset
~~~

---

# 🧩 Required PROV-O Components for This Sphere

### ✔ `@context`
Must include:
- `"prov"`  
- `"care"`  
- `"kfm"`  
- `"dct"` (for DCAT crosswalk)  
- `"crm"` (optional CIDOC-CRM mapping)

---

### ✔ `prov:Entity`

Must define:

| Entity | Description |
|---|---|
| `raw` | Original public-domain cultural/landscape sources |
| `generalized` | H3/Polygon generalized sphere geometry |
| `processed` | Validated, published KFM-ready dataset |

Optional:
- `interpretive` entity for archaeological synthesis models

---

### ✔ `prov:Activity`

Required activity categories:

| Activity | Description |
|---|---|
| `generalization` | H3-level derivation + simplification |
| `integration` | Combining archaeological, environmental, and ethnohistoric insights |
| `cleaning` | Metadata harmonization |
| `faircare_review` | Ethics and cultural review |
| `temporal_alignment` | Phase-to-interval mapping |

Each activity must include:

- `prov:type`  
- `prov:startTime`  
- `prov:endTime`  
- `kfm:steps` (array)  

---

### ✔ `prov:Agent`

Agents must document:

| Type | Requirement |
|---|---|
| Analyst | Archaeologist / GIS specialist |
| FAIR+CARE reviewer | Required |
| Source institution | PD archive or academic source |

This sphere **does not require tribal review**, unlike protohistoric datasets.

---

### ✔ Lineage Relations

All provenance logs must include:

- `prov:wasDerivedFrom`  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasAttributedTo`  

These express the raw → generalized → processed lineage.

---

# ⚖️ CARE Cultural Safety Requirements

Although this sphere is moderate sensitivity, CARE still applies:

- `care:sensitivity: "generalized"`  
- `care:review: "faircare"`  
- `care:notes` describing removed/restricted materials  
- `care:visibility_rules: "polygon-generalized"`  

Forbidden:

- `"restricted"` classification  
- Exact boundaries  
- Sacred or sensitive knowledge  
- Site coordinates  

Generalization methods described in provenance must align with:

- Spatial ethics  
- Sovereignty protections  
- Community expectations  

---

# 🧪 Example Provenance Snippet

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#",
    "dct": "http://purl.org/dc/terms/"
  },
  "prov:Entity": {
    "raw": {
      "prov:type": "Dataset",
      "prov:label": "Archaeological synthesis of CPT interaction networks",
      "kfm:source": "Public domain literature (multiple PD sources)"
    },
    "generalized": {
      "prov:type": "Dataset",
      "prov:label": "Generalized Interaction Sphere (H3 level 6)",
      "care:notes": "Geomorphology-based boundary adjustment + cultural safety review"
    },
    "processed": {
      "prov:type": "Dataset",
      "kfm:provenance_version": "v1",
      "prov:label": "Central Plains Exchange v1"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "Generalization",
      "prov:startTime": "2025-10-16T13:25:00Z",
      "prov:endTime": "2025-10-16T14:02:00Z",
      "kfm:steps": ["H3 indexing", "polygon simplification", "boundary smoothing"]
    },
    "faircare_review": {
      "prov:type": "Review",
      "prov:endTime": "2025-10-17T17:40:00Z",
      "kfm:steps": ["ethical language check", "sensitivity review"]
    }
  },
  "prov:Agent": {
    "analyst": { "prov:label": "A. Barta", "prov:type": "Person" },
    "faircare": { "prov:label": "FAIR+CARE Council", "prov:type": "Group" }
  },
  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "generalized", "prov:usedEntity": "raw" },
    { "prov:generatedEntity": "processed", "prov:usedEntity": "generalized" }
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Generalized to avoid revealing culturally meaningful landscapes."
}
~~~

---

# 🧠 Integration Into KFM Ecosystem

Provenance files empower:

### Knowledge Graph
Nodes:
- `InteractionSphere`
- `GeneralizedRegion`
- `CulturalPhase`
- `ProvenanceActivity`
- `CulturalSensitivityLevel`

Edges:
- `GENERALIZED_FROM`  
- `HAS_PROVENANCE`  
- `ASSOCIATED_WITH`  
- `OCCURRED_DURING`  
- `CARE_SENSITIVITY`

### Story Nodes
- Cultural exchange narratives  
- Multi-valley interaction stories  
- Cross-cultural diffusion arcs  

### Focus Mode v2
- Ethical sensitivity prompts  
- Provenance-chip overlays  
- Explainability messages  
- AI reasoning guardrails  

---

# 📊 Provenance Index

| Provenance File | Version | Sensitivity | Review | Status |
|---|---|---|---|---|
| `central-plains-exchange-v1.json` | v1 | generalized | FAIR+CARE | 🟢 Active |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Initial provenance log for Central Plains Exchange Interaction Sphere |
| v0.1 | 2025-11-10 | Landscape Provenance Team | Prototype lineage & generalization chain |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Central Plains Exchange Sphere](../README.md)

</div>