---
title: "🏺 Kansas Frontier Matrix — Artifact Inventories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Tribal Sovereignty Review Board"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_guid: "urn:kfm:doc:archaeology-artifact-inventories-v11.0.0"
doc_kind: "Dataset Category"
intent: "archaeology-artifact-inventories"
semantic_document_id: "kfm-doc-archaeology-artifact-inventories"

sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-artifact-inventories-v11.json"
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
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Archaeological / Heritage"
indigenous_data_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Governed Public"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Artifact Inventories (v11)**  
`docs/analyses/archaeology/datasets/artifact-inventories/README.md`

**FAIR+CARE Certified · Sovereignty-Aligned · Diamond⁹ Ω / Crown∞Ω**

**Purpose:**  
Define the full **governed, ethically filtered, sovereignty-compliant artifact inventory corpus** included in KFM v11.  
Only **public-domain** and **open-license** artifact datasets are permitted.  
All provenance must be verifiable.  
All culturally sensitive materials must be **excluded**, **generalized**, or **sovereignty-gated**.

</div>

---

# 📘 v11 Overview

Artifact inventories support:

- Cultural landscape reconstructions  
- Chronological + occupation-phase modeling  
- Lithic & ceramic classification  
- AI-assisted Focus Mode v3 reasoning  
- Story Node v3 evidence linking  
- Settlement + trade network inference  
- H3-based spatial generalization for cultural safety

**v11 expands**:

- CARE Level definitions  
- Sovereignty governance  
- H3 r7–r10 spatial safety rules  
- AI explainability metadata  
- PROV-O enriched lineage  
- DCAT 3.0 compliance  
- STAC 1.0 Collection upgrades  

---

# 🗂️ Directory Layout (v11)

```text
docs/analyses/archaeology/datasets/artifact-inventories/
├── README.md                       # This file
├── inventories/                    # Cleaned, vetted, standardized inventories
├── stac/                           # STAC Items/Collections (v11 schema)
├── metadata/                       # DCAT + CARE metadata, licensing, lineage
└── provenance/                     # PROV-O bundles (entity → activity → agent)
```

---

# 🧭 Artifact Inventory Categories (v11)

| Category | Description | CARE Level | Allowed | Notes |
|---------|-------------|------------|---------|-------|
| **Lithics** | Chipped/ground stone, debitage | C1–C2 | ✅ | Public-domain only |
| **Ceramics** | Sherds, vessels, motifs | C2–C3 | ⚠️ | Decorations cannot expose restricted tribal knowledge |
| **Faunal (PD)** | Open-license zooarchaeology | C1–C2 | ⚠️ | Sacred species removed or generalized |
| **Metal Artifacts** | Contact-era metals, tools | C1 | ✅ | Requires provenance verification |
| **Protohistoric Items** | Trade goods, contact artifacts | C2–C4 | 🔒 Review | Tribal sovereignty review required |
| **Misc. Material Culture** | Beads, ornaments, tools | C1–C3 | ⚠️ | Allowed only with PD documentation |

**Strictly forbidden:**  
- Human remains or funerary objects  
- Sacred/ceremonial items  
- Tribal-restricted belongings  
- Exact provenience for sensitive sites  
- Unprovenanced artifacts (any chain break)

---

# 📦 Required Metadata (v11 Hard Requirements)

Every inventory must include:

## ✔ STAC Item (v11)
Required fields:

| Field | Description |
|---|---|
| `id` | Dataset unique ID |
| `bbox` | H3 generalized footprint |
| `properties.kfm:phase` | Cultural/temporal phase |
| `properties.care:*` | Sensitivity, sovereignty, consent |
| `assets.data.href` | PD/open dataset link |

---

## ✔ DCAT Dataset (v11)
| Field | Description |
|---|---|
| `dct:title` | Dataset title |
| `dct:license` | Must be PD, CC0, or CC-BY |
| `dcat:distribution[]` | Access paths |
| `dct:temporal` | Phase or occupation date range |
| `dct:spatial` | Generalized footprint |

---

## ✔ PROV-O Provenance (v11)
Must include:

- `prov:wasDerivedFrom` (source)  
- `prov:wasGeneratedBy` (KFM ingestion pipeline)  
- `prov:used` (classification standards)  
- `prov:qualifiedAttribution` (analyst + reviewer)  
- Full chain from **source → processing → validation → publication**

---

# 🛡 Cultural & Sovereignty Safety (v11)

Artifact inventories must **not** expose:

- Restricted tribal heritage  
- Ritual objects or sacred motifs  
- Sensitive species or symbolic animals  
- Exact findspots or provenience  
- Contextual associations that imply sacred geography

### Required Enforcement
- H3 r7–r10 spatial generalization  
- CARE labels embedded in metadata  
- Sovereignty rules checked via AI Governance filters  
- Redaction logs stored in `provenance/`  
- Public datasets must be PD-safe  

---

# 🧪 Data Preparation Requirements (v11)

Artifact inventory tables must:

- Use **UUIDs** for all artifact IDs  
- Provide controlled vocabularies:  
  - `material`  
  - `artifact_type`  
  - `decoration`  
  - `phase`  
  - `culture`  
- Include:  
  - `temporal_bounds` (start, end, precision)  
  - `context_description` (generalized)  
  - `collection_source`  
- Strip all restricted fields:
  - site names  
  - field notes  
  - researcher personal data  
  - unsafe media attachments

---

# 🛰 Integration Into KFM (v11 Architecture)

## Neo4j Knowledge Graph (v11)
Nodes:
- `Artifact`, `ArtifactType`, `Material`, `Culture`,  
- `OccupationPhase`, `GeneralizedSite`, `StoryNode`.

Relationships:
- `FOUND_AT` (H3 region)  
- `BELONGS_TO`  
- `ASSOCIATED_WITH`  
- `DATED_TO`  
- `HAS_MATERIAL`  

## Focus Mode v3
- Uses artifact inventories to support cultural inferences  
- AI outputs undergo:  
  - tone audit  
  - cultural sensitivity audit  
  - sovereignty masking  
- Provenance chips link each summary line to artifact evidence

## Story Node v3
- Material-culture evidence  
- Trade network reconstructions  
- Settlement phases  
- Interaction spheres

## Map & 3D Layers
- Artifact density (H3)  
- Material-typed choropleths  
- Temporal sliders (OWL-Time)

---

# 📊 Artifact Dataset Status Matrix (v11)

| Dataset | Category | CARE Level | Sovereignty | Status | Notes |
|---|---|---|---|---|---|
| `lithics/flint-hills-v11` | Lithics | C1 | Yes | 🟢 Active | PD dataset, H3 r7 |
| `ceramics/prairie-v11` | Ceramics | C2 | Yes | 🟢 Active | Decorations reviewed |
| `faunal/open-fauna-v11` | Faunal | C1 | No | 🟡 Review | Sacred species filter |
| `protohistoric/contact-v11` | Protohistoric | C3–C4 | Yes | 🔒 Hold | Requires sovereignty signoff |

---

# 🧠 Example v11 STAC Item

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "artifact-inventory-flint-hills-lithics-v11",
  "bbox": [-101.3, 37.6, -95.3, 40.1],
  "properties": {
    "kfm:phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "care:sovereignty": "protected",
    "kfm:generalization": "H3-r7",
    "datetime": null
  },
  "assets": {
    "data": {
      "href": "https://example.org/artifacts/flint_hills_lithics_v11.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
~~~

---

# 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| **v11.0.0** | 2025-11-24 | Full v11 rebuild · sovereignty enforcement · H3 r7–r10 rules · cultural safety expansion · PROV-O upgrades |
| v10.4.0 | 2025-11-17 | v10 archaeology dataset framework |
| v10.0.0 | 2025-11-10 | Initial structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Archaeology Datasets](../README.md)

</div>