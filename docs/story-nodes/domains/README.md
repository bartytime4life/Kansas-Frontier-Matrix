---
title: "🌐 Kansas Frontier Matrix — Domain Story Nodes Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/storynodes-domains-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Index"
intent: "story-nodes-domains-overview"
role: "domain-story-nodes-index"
category: "Story Nodes · Domain Narratives · Focus Mode v3"

classification: "Public Document"
sensitivity: "Mixed"
sensitivity_level: "Medium"
public_exposure_risk: "Low to Medium"
risk_category: "Content"
redaction_required: false
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed / Requires Review"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Article"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:Feature"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/README.md@v11.2.1"
  - "docs/story-nodes/domains/README.md@v11.0.0"
  - "docs/story-nodes/domains/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true

json_schema_ref: "../../../schemas/json/storynodes-domains-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/storynodes-domains-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "governance-override"
  - "content-alteration"
  - "speculative-additions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Domain Story Nodes Overview**  
`docs/story-nodes/domains/README.md`

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]() ·
[![Story Nodes v3](https://img.shields.io/badge/Story%20Nodes-v3-informational)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]() ·
[![WCAG AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-purple)]() ·
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

**Purpose**  
Serve as the **governed, ontology-aligned index** for all **Domain Story Nodes**.  
These Story Nodes narrate hydrology, climate, ecology, soil/terrain, hazards, archaeology, and historical processes within Kansas.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📂 story-nodes/
    ├── 📂 domains/
    │   ├── 📄 README.md                       # ← This file
    │   ├── 📂 history/                        # Historical & cultural narratives (strict governance)
    │   │   └── 📄 README.md
    │   ├── 📂 hydrology/                      # Rivers, basins, droughts, floods
    │   │   └── 📄 README.md
    │   ├── 📂 climate/                        # Climate anomalies, weather events, long-term patterns
    │   │   └── 📄 README.md
    │   ├── 📂 archaeology/                    # Archaeology & heritage (sovereignty-enforced)
    │   │   └── 📄 README.md
    │   ├── 📂 ecology/                        # Prairies, wetlands, species distributions
    │   │   └── 📄 README.md
    │   ├── 📂 soil/                           # Soil types, geomorphology, surface processes
    │   │   └── 📄 README.md
    │   └── 📂 hazards/                        # Tornadoes, wildfire, flood, extreme weather
            └── 📄 README.md
~~~

**Directory Rules**

- 📂 = directories only  
- 📄 = files only  
- No emojis inside ASCII connectors  
- Every child directory MUST maintain its own `README.md` and follow KFM-MDP v11.2.2  

---

## 📘 Overview of Domain Story Nodes

Domain Story Nodes describe **real-world environmental, hydrological, climatological, ecological, geological, hazard, archaeological, and historical phenomena** within Kansas.

They combine:

- Narrative text  
- Spatial footprints (generalized when required)  
- Temporal intervals (OWL-Time)  
- Dataset references (STAC/DCAT)  
- Event/place references (CIDOC-CRM, GeoSPARQL)  
- Governance metadata (CARE, sovereignty)  
- Provenance (PROV-O & OpenLineage)  

They are the primary way Focus Mode v3 explains **real physical processes and historical patterns** to users.

---

## 🧠 What Makes Domain Nodes Unique?

Domain Story Nodes must:

- Be fully **data-grounded** (no speculation).  
- Reference **real datasets**, **real events**, and **real places**.  
- Use H3 generalization for protected archaeological or cultural sites.  
- Include FAIR+CARE metadata and sovereignty flags.  
- Integrate with STAC/DCAT/ontology models.  
- Provide clear, structured narrative blocks Focus Mode can segment.

These nodes are **heavily governed**, especially in:

- Archaeology  
- Tribal/Indigenous cultural landscapes  
- Historical interpretations  

---

## 🌎 Domain Categories

### History
- Territorial changes and archival events.  
- Migration periods and social transformations.  
- Governed: sovereignty-sensitive, high CARE review.

### Hydrology
- Rivers, basins, floodplains, and drought episodes.  
- USGS gage–based timelines and water-balance stories.

### Climate
- Temperature and precipitation anomalies.  
- Severe storm events and climatological regimes (ENSO, PDO, etc.).

### Archaeology  *(most restricted domain)*
- Archaeological landscapes and cultural sites.  
- **No precise coordinates; mandatory H3 masking.**  
- Strong sovereignty and CARE oversight; only permitted, documented content.

### Ecology
- Prairie systems, wetlands, and habitat mosaics.  
- Species distribution narratives based on governed data.

### Soil & Terrain
- Soil classifications and geomorphologic units.  
- Terrain processes, erosion, and landscape evolution.

### Hazards
- Tornado tracks and severe convective storms.  
- Wildfires, floods, and compound hazard narratives.

---

## 📦 Data & Metadata Requirements

Each Domain Story Node MUST include:

- References to STAC collections/items for any datasets shown.  
- References to DCAT datasets for catalog-level descriptions.  
- Links to CIDOC-CRM events and places where applicable.  
- OWL-Time intervals or instants for temporal scope.  
- Governance metadata fields capturing CARE and sovereignty.  
- Provenance links to OpenLineage and other process logs.  

Nodes MUST validate against the Story Node v3 schema and any domain-specific constraints.

---

## ⚖ FAIR+CARE & Sovereignty

Domain Story Nodes cannot be authored without:

- CARE labels (`care_label`) and FAIR category (`fair_category`).  
- Explicit sovereignty protections and masking/generalization notes.  
- Clear provenance and licensing for referenced data.  
- Avoidance of speculative or sensational narratives, especially for archaeology and history.

**Archaeology nodes** are subject to the strictest rules in KFM:

- No direct coordinates.  
- No unauthorized cultural knowledge.  
- No publication without responsible review.

---

## 🧭 Role in Focus Mode

Domain Story Nodes allow Focus Mode v3 to:

- Produce map overlays with small narrative snippets.  
- Build time-based storylines of natural and cultural processes.  
- Link hydrology ↔ climate ↔ hazards ↔ ecology in one narrative path.  
- Provide data-backed, ethically governed explanations to end users.  

Focus Mode must only apply allowed AI transforms (`ai_transform_permissions`) and never modify node content directly.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                          |
|--------:|------------|--------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Rebuilt with badge row, strict emoji discipline, corrected directory layout, KFM-MDP v11.2.2 aligned. |
| v11.2.1 | 2025-11-27 | Split domain/system Story Node structure; clarified governance rules.                            |
| v11.0.0 | 2025-11-20 | Initial domain Story Nodes index and basic architecture.                                         |

---

<div align="center">

🌐 **Kansas Frontier Matrix — Domain Story Nodes (v11.2.2)**  
Real-World Narratives · Ontology-Linked · FAIR+CARE-Governed  

[⬅ Story Nodes Root](../README.md) · [🧠 System Nodes](../system/README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>

