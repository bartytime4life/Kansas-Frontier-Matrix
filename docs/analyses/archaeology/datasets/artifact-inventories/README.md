---
title: "🏺 Kansas Frontier Matrix — Artifact Inventories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed, sovereignty-aligned artifact inventory corpus for KFM v11, restricted to FAIR+CARE-compliant, provenance-rich, open-licensed materials."
path: "docs/analyses/archaeology/datasets/artifact-inventories/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Tribal Sovereignty Review Board"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventories-v11.2.3"
doc_kind: "Dataset Category"
intent: "archaeology-artifact-inventories"
semantic_document_id: "kfm-doc-archaeology-artifact-inventories-v11.2.3"
category: "Analyses · Archaeology · Artifact Inventories"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-artifact-inventories-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Archaeological / Heritage"
sensitivity_level: "High"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Archaeology & Heritage WG · Tribal Sovereignty Board"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Artifact Inventories (v11)**  
`docs/analyses/archaeology/datasets/artifact-inventories/README.md`

**FAIR+CARE Certified · Sovereignty-Aligned · Diamond⁹ Ω / Crown∞Ω**

**Purpose:**  
Define the **governed, ethically filtered, sovereignty-compliant artifact inventory corpus** included in KFM v11.  
Only **public-domain** and **open-license** artifact datasets are permitted.  
All provenance must be verifiable.  
All culturally sensitive materials must be **excluded**, **generalized**, or **sovereignty-gated**.

</div>

---

## 📘 v11 Overview

Artifact inventories support:

- Cultural landscape reconstructions  
- Chronological + occupation-phase modeling  
- Lithic & ceramic classification  
- AI-assisted Focus Mode v3 reasoning  
- Story Node v3 evidence linking  
- Settlement + trade network inference  
- H3-based spatial generalization for cultural safety  

**v11 expands:**

- CARE level definitions  
- Sovereignty governance  
- H3 r7–r10 spatial safety rules  
- AI explainability metadata  
- PROV-O enriched lineage  
- DCAT 3.0 compliance  
- STAC 1.0 Collection upgrades  

---

## 🗂️ Directory Layout (v11 · Normative)

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/
├── 📄 README.md                       # This file (dataset-category index)
├── 📂 inventories/                    # Cleaned, vetted, standardized inventories
├── 🗂️ stac/                           # STAC Items/Collections (v11 schema)
├── 🧾 metadata/                       # DCAT + CARE metadata, licensing, lineage
└── 🔗 provenance/                     # PROV-O bundles (entity → activity → agent)
~~~

This layout is **normative** for artifact-inventory datasets in the archaeology domain.

---

## 🧭 Artifact Inventory Categories (v11)

| Category                   | Description                             | CARE Level | Allowed | Notes                                                             |
|----------------------------|-----------------------------------------|------------|---------|-------------------------------------------------------------------|
| **Lithics**                | Chipped/ground stone, debitage         | C1–C2      | ✅      | Public-domain only; generalized findspots                         |
| **Ceramics**               | Sherds, vessels, motifs                | C2–C3      | ⚠️      | Decorations cannot expose restricted tribal knowledge             |
| **Faunal (PD)**            | Open-license zooarchaeology             | C1–C2      | ⚠️      | Sacred species removed or generalized                             |
| **Metal Artifacts**        | Contact-era metals, tools              | C1         | ✅      | Requires explicit provenance verification                         |
| **Protohistoric Items**    | Trade goods, contact artifacts         | C2–C4      | 🔒      | Tribal sovereignty review required before publication             |
| **Misc. Material Culture** | Beads, ornaments, tools                | C1–C3      | ⚠️      | Allowed only with PD/open documentation and sovereignty approval  |

**Strictly forbidden:**

- Human remains or funerary objects  
- Sacred/ceremonial items  
- Tribal-restricted belongings  
- Exact provenience for sensitive sites  
- Unprovenanced artifacts (any chain break)  

---

## 📦 Required Metadata (v11 Hard Requirements)

Every inventory must include **STAC**, **DCAT**, and **PROV-O** representations, plus KFM governance extensions.

### ✔ STAC Item (v11)

Required fields:

| Field                       | Description                                  |
|----------------------------|----------------------------------------------|
| `id`                       | Dataset unique ID                            |
| `bbox`                     | H3-generalized footprint                     |
| `properties.kfm:phase`     | Cultural/temporal phase                      |
| `properties.care:*`        | Sensitivity, sovereignty, consent            |
| `properties.kfm:generalization` | H3 level (e.g., `H3-r7`)               |
| `assets.data.href`         | PD/open dataset link                         |

---

### ✔ DCAT Dataset (v11)

| Field            | Description                                            |
|------------------|--------------------------------------------------------|
| `dct:title`      | Dataset title                                         |
| `dct:license`    | Must be PD, CC0, or CC-BY                             |
| `dcat:distribution[]` | Access paths and formats                        |
| `dct:temporal`   | Phase or occupation date range                        |
| `dct:spatial`    | Generalized footprint (aligned to STAC/H3)            |

---

### ✔ PROV-O Provenance (v11)

Must include:

- `prov:wasDerivedFrom` (source collections, archives, original catalogs)  
- `prov:wasGeneratedBy` (KFM ingestion + cleaning pipeline)  
- `prov:used` (classification standards, vocabularies, external references)  
- `prov:qualifiedAttribution` (analyst + reviewer, sovereignty board where applicable)  
- Full chain from **source → processing → validation → publication**  

All PROV-O bundles live under `provenance/` and must be **machine-parseable**.

---

## 🛡 Cultural & Sovereignty Safety (v11)

Artifact inventories must **not** expose:

- Restricted tribal heritage  
- Ritual objects or sacred motifs  
- Sensitive species or symbolic animals  
- Exact findspots or provenience  
- Contextual associations that imply sacred geography  

### Required Enforcement

- H3 r7–r10 spatial generalization (per sensitivity level)  
- CARE labels embedded in STAC, DCAT, and PROV-O metadata  
- Sovereignty rules checked via AI governance filters before publication  
- Redaction logs stored in `provenance/` with explicit `prov:invalidated` traces  
- Public datasets must be **PD-safe and sovereignty-approved**  

---

## 🧪 Data Preparation Requirements (v11)

Artifact inventory tables must:

- Use **UUIDs** for all artifact IDs  
- Provide controlled vocabularies for:  
  - `material`  
  - `artifact_type`  
  - `decoration`  
  - `phase`  
  - `culture`  
- Include fields such as:  
  - `temporal_bounds` (start, end, precision)  
  - `context_description` (generalized, non-sensitive)  
  - `collection_source` (museum/archive/field project)  
  - `license` and `rights_holder`  
- Strip all restricted fields, including:  
  - exact site names or codes  
  - detailed field notes  
  - researcher personal data  
  - unsafe media attachments or high-resolution imagery of sensitive items  

Data prep must be **deterministic** and reproducible with documented ETL steps.

---

## 🛰 Integration Into KFM (v11 Architecture)

### Neo4j Knowledge Graph (v11)

Nodes:

- `Artifact`, `ArtifactType`, `Material`, `Culture`  
- `OccupationPhase`, `GeneralizedSite`, `StoryNode`  

Relationships (ontology-aligned):

- `FOUND_AT` (→ `GeneralizedSite` / H3 region)  
- `BELONGS_TO` (collection, culture, or phase)  
- `ASSOCIATED_WITH` (Story Nodes, routes, contexts)  
- `DATED_TO` (occupation phase, temporal interval)  
- `HAS_MATERIAL` (material classification)  

### Focus Mode v3

- Uses artifact inventories to support **cautious cultural inferences**.  
- Every generated explanation is backed by:
  - tone audit  
  - cultural sensitivity audit  
  - sovereignty masking  
- Provenance chips link each summary line to **specific artifact evidence** and PROV-O bundles.

### Story Node v3

- Encodes:
  - material-culture evidence  
  - trade network reconstructions  
  - settlement phases  
  - interaction spheres  
- Story Nodes that reference artifact inventories must:
  - embed `semantic_document_id` for this README  
  - carry forward CARE, sovereignty, and H3 generalization flags  

### Map & 3D Layers

- H3-based artifact density maps  
- Material-typed choropleths (generalized)  
- Temporal sliders (OWL-Time-aligned intervals)  
- No single artifact or sensitive context is visually isolatable.

---

## 📊 Artifact Dataset Status Matrix (v11)

| Dataset                     | Category       | CARE Level | Sovereignty | Status   | Notes                             |
|----------------------------|----------------|------------|------------|----------|-----------------------------------|
| `lithics/flint-hills-v11`  | Lithics        | C1         | Yes        | 🟢 Active | PD dataset, H3 r7                 |
| `ceramics/prairie-v11`     | Ceramics       | C2         | Yes        | 🟢 Active | Decorations reviewed, motifs safe |
| `faunal/open-fauna-v11`    | Faunal         | C1         | No         | 🟡 Review | Sacred species filter in progress |
| `protohistoric/contact-v11`| Protohistoric  | C3–C4      | Yes        | 🔒 Hold   | Requires sovereignty signoff      |

This matrix is **illustrative**; canonical status lives in `metadata/` + registry.

---

## 🧠 Example v11 STAC Item

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

This shape MUST align with `telemetry_schema`, `energy_schema`, and `carbon_schema` for full KFM compliance.

---

## 🕰 Version History

| Version   | Date       | Summary                                                                                 |
|-----------|------------|-----------------------------------------------------------------------------------------|
| **v11.2.3** | 2025-12-02 | v11.2 alignment; telemetry/energy/carbon schema refs updated; sensitivity fields aligned; governance metadata expanded. |
| v11.0.0   | 2025-11-24 | Full v11 rebuild · sovereignty enforcement · H3 r7–r10 rules · cultural safety expansion · PROV-O upgrades. |
| v10.4.0   | 2025-11-17 | v10 archaeology dataset framework.                                                      |
| v10.0.0   | 2025-11-10 | Initial structure.                                                                      |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Archaeology Datasets](../README.md)

</div>