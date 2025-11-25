---
title: "📍 Kansas Frontier Matrix — Site Gazetteer Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/site-gazetteers/README.md"
version: "v11.0.0"
last_updated: "2025-11-25"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_uuid: "urn:kfm:archaeology:site-gazetteers:v11.0.0"
semantic_document_id: "kfm-doc-arch-site-gazetteers"
doc_kind: "Dataset Category"
intent: "archaeology-site-gazetteers"
role: "dataset-governance"

sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-site-gazetteers-v4.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity_level: "Generalized"
public_exposure_risk: "Low"
indigenous_data_flag: true
cultural_sensitivity: "Moderate"
risk_category: "Low"
redaction_required: true

provenance_chain:
  - "docs/analyses/archaeology/datasets/site-gazetteers/README.md@v10.4.0"
  - "docs/analyses/archaeology/datasets/site-gazetteers/README.md@v10.0.0"

ontology_alignment:
  cidoc: "E53 Place"
  schema_org: "Place"
  owl_time: "TemporalEntity"
  prov_o: "prov:Collection"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/archaeology-site-gazetteers-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/archaeology-site-gazetteers-v11.shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next major archaeology datasets release"
---

<div align="center">

# 📍 **Kansas Frontier Matrix — Archaeological Site Gazetteers**  
`docs/analyses/archaeology/datasets/site-gazetteers/README.md`

**Purpose:**  
Provide a **FAIR+CARE-compliant**, sovereignty-respecting, and STAC/DCAT-aligned index of **generalized archaeological site gazetteers** used across the Kansas Frontier Matrix (KFM).  
These datasets supply the **spatial anchors** for Focus Mode v3, Story Node v3, cultural-phase modeling, and all archaeology-driven geospatial reasoning.

</div>

---

# 📘 Overview

Site Gazetteers represent **culturally safe**, **generalized**, and **governed** archaeological place references.  
They intentionally exclude sensitive details while preserving:

- Cultural-phase significance  
- Spatial reasoning capability (H3 generalization)  
- Temporal alignment (OWL-Time)  
- Provenance and licensing transparency  
- CARE + sovereignty compliance  
- Cross-domain compatibility (hydrology, ecology, paleoenvironment)

Forbidden in v11:

- Exact coordinates  
- Burial grounds  
- Ceremonial/sacred sites  
- Restricted tribal knowledge  
- Proprietary/confidential survey data  
- Any site lacking confirmed provenance or consent  
- Any dataset with non-CARE-compliant origins

The v11 version enforces **KFM Sovereignty Mode** + **Generalization Mode** (H3 r5–r7).

---

# 📦 Directory Structure (Stable v11 Format)

~~~~text
docs/analyses/archaeology/datasets/site-gazetteers/
├── README.md            # This file
├── gazetteers/          # Cleaned, generalized site lists (H3-only)
├── stac/                # STAC Items/Collections (v11 schema)
├── metadata/            # DCAT, CARE, sensitivity, temporal metadata
└── provenance/          # PROV-O lineage logs + processing history
~~~~

---

# 🧭 Dataset Classification (v11)

| Category | Description |
|---------|-------------|
| **Public-Domain Sites** | GNIS + public-domain archaeology entries (generalized required) |
| **Open Academic Gazetteers** | University datasets with PD/CC-BY licensing |
| **Tribal-Reviewed Generalized Sites** | High-level culturally safe boundaries; no specific coordinates |
| **Historic Register Sites** | National/State historic registers (already public) |
| **Cultural Phase Anchors** | Canonical archaeological sites tied to cultural periods (generalization mandatory) |

---

# 🧬 Metadata Requirements (v11)

## STAC 1.0 / KFM-STAC v11 Fields (Mandatory)

| Field | Description |
|-------|-------------|
| `id` | Gazetteer dataset ID |
| `bbox` | H3 generalized bounding region |
| `geometry` | MultiPoint / MultiPolygon of generalized cells |
| `kfm:site_type` | Cultural classification |
| `kfm:culture_phase` | Cultural/chronological period |
| `care:sensitivity` | `"generalized"` or `"restricted-generalized"` |
| `assets.gazetteer.href` | Link to CSV/GeoJSON site list |
| `kfm:provenance` | PROV-O reference file |

## DCAT 3.0 Requirements (Mandatory)

| Field | Required |
|-------|----------|
| `dct:title` | Name of dataset |
| `dct:license` | CC-BY or PD only |
| `dcat:distribution` | GeoJSON/CSV/H3 list |
| `dct:temporal` | OWL-Time interval or multi-period |

## CARE + Sovereignty Requirements

- All coordinates → **H3 grid only**  
- Restricted sites → **excluded or generalized**  
- Tribal-reviewed datasets → labeled with consent metadata  
- No colonial framing or decontextualized language  
- Cultural roles + risk context must be included  
- All datasets receive `care_label` + `sensitivity_level` tags  

---

# 🧪 Data Preparation (v11 Rules)

All site gazetteers must:

- Use schema fields:  
  `site_id`, `name`, `culture_phase`, `site_type`, `location_h3`, `confidence_level`, `sources`
- Include OWL-Time temporal fields  
- Include full PROV-O lineage  
- Strip all raw coordinates  
- Validate against:  
  - STAC v11 schema  
  - DCAT 3.0  
  - CIDOC-CRM (E53, E7, E27 mappings)  
  - CARE/Sovereignty rules  
- Pass FAIR+CARE Council review

Generalization thresholds:

- High sensitivity → H3 r7  
- Medium sensitivity → H3 r6  
- Low sensitivity → H3 r5  

---

# 🛰 Integration in KFM (Focus Mode · Story Nodes · Graph)

## Knowledge Graph (Neo4j)

Nodes:

- `Site`
- `CulturalPhase`
- `PlaceName`
- `LandscapeUnit`

Relationships:

- `LOCATED_AT` (H3 region)
- `BELONGS_TO`
- `ASSOCIATED_WITH`
- `MENTIONED_IN`

## Story Nodes v3

Gazetteers supply:

- Cultural anchors  
- Spatial grounding for narratives  
- Time-aligned cultural sequences  

## Focus Mode v3

Gazetteers provide:

- Spatial context  
- Cultural-phase relevance  
- Provenance chips  
- Sovereignty-aware tone filters  

---

# 📊 Dataset Index (v11)

| Dataset | Category | Location | Status | Review | Notes |
|--------|----------|----------|--------|--------|-------|
| `gnis/archaeology-gnis-v1` | Public-Domain | `gazetteers/` | 🟢 Active | 2025-11 | GNIS-linked, generalized |
| `academic/open-kansas-sites-v1` | Academic PD | `gazetteers/` | 🟢 Active | 2025-10 | Culture phases added |
| `tribal/generalized-list-v1` | Tribal-Reviewed | `gazetteers/` | 🟡 Needs Review | 2025-09 | Awaiting updated consent policy |
| `historic/registered-sites-v1` | Historic | `gazetteers/` | 🟢 Active | 2025-11 | Public register compliant |

---

# 🧠 Example STAC Item (v11 Format)

~~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-site-gazetteer-v1",
  "bbox": [-101.2, 37.4, -95.7, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ "H3-R7-GENERALIZED" ]]
  },
  "properties": {
    "kfm:site_type": "village",
    "kfm:culture_phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "kfm:provenance": "provenance/kfm-site-gazetteer-v1.json"
  },
  "assets": {
    "gazetteer": {
      "href": "https://example.com/gazetteers/kansas_generalized_sites_v1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
~~~~

---

# 🕰 Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v11.0.0 | 2025-11-25 | Archaeology WG · FAIR+CARE Council | Full regeneration under KFM-MDP v11; added sovereignty mode, H3 generalization tiers, enriched ontology links, telemetry v4, and stability-safe fencing |
| v10.4.0 | 2025-11-17 | Archaeology WG | Previous version (pre-v11 rules) |
| v10.0.0 | 2025-11-10 | Archaeology Dataset Team | Initial directory |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Datasets](../README.md)

</div>