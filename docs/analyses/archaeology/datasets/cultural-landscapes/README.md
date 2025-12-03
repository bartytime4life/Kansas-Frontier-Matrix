---
title: "🏞️ Kansas Frontier Matrix — Cultural Landscape Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/README.md"
description: "Governed cultural landscape datasets for KFM v11, representing generalized settlement regions, mobility corridors, interaction spheres, and resource areas under FAIR+CARE and sovereignty rules."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Tribal Sovereignty Review Board"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-cultural-landscapes-v11.2.3"
doc_kind: "Dataset Category"
intent: "archaeology-cultural-landscapes"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

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
sensitivity: "Cultural / Historical / Archaeological"
sensitivity_level: "Medium"
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

data_steward: "Archaeology Working Group · FAIR+CARE Council · Tribal Sovereignty Review Board"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🏞️ Kansas Frontier Matrix — Cultural Landscape Datasets (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/README.md`

**Purpose**  
Define and govern all **cultural landscape datasets** used in KFM v11, covering:

- Settlement systems and habitation regions  
- Mobility and movement corridors  
- Territorial and cultural extents (generalized)  
- Interaction spheres and influence zones  
- Resource-procurement landscapes (stone, clay, fauna, etc.)  

These datasets feed:

- **Story Node v3**  
- **Focus Mode v3**  
- **Cesium 3D reconstructions**  
- **MapLibre time-aware layers**  
- **Neo4j cultural-region graph models**

All cultural landscape datasets are **generalized, sovereignty-governed, and CARE-audited** before inclusion.

---

## 📘 Overview (v11)

Cultural landscapes in KFM represent **human–land relationships across time**, including:

- Ancient and protohistoric **mobility corridors**  
- Cultural-phase **settlement regions** and habitation surfaces  
- **Interaction spheres** (for example, Great Bend aspect, Pawnee spheres)  
- **Territorial boundaries** (generalized and sovereignty-governed)  
- **Resource procurement zones** (chert, clay, fauna, plant resources)  
- **Cultural landscapes** that are permitted for public-governed representation under sovereignty rules  

**v11 introduces:**

- Mandatory **H3 r7–r10 generalization** for spatial components  
- Cultural and sovereignty AI governance filters integrated into Focus Mode v3  
- Expanded CARE labels and consent flags at dataset and feature levels  
- PROV-O–enriched lineage bundles for all landscape layers  
- DCAT 3.0 / STAC 1.0 v11-compliant metadata for all public-governed layers  
- Dataset-level sustainability telemetry (energy Wh, carbon gCO₂e)  

Restricted, sacred, or sovereignty-governed features follow strict redaction and generalization rules and may be **excluded from public catalogs**.

---

## 🗂️ Directory Layout (v11)

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/
├── 📄 README.md                    # This file
├── 📂 regions/                     # Settlement regions, tribal/cultural areas (generalized)
├── 📂 routes/                      # Mobility corridors, seasonal pathways, travel routes
├── 📂 interaction-spheres/         # Cultural influence zones (e.g., Great Bend, Pawnee)
├── 📂 resource-areas/              # Procurement zones (stone, clay, fauna, other resources)
├── 📂 stac/                        # STAC Items/Collections (v11 spec, generalized)
├── 📂 metadata/                    # DCAT 3.0 + CARE metadata
└── 📂 provenance/                  # PROV-O lineage + sovereignty review logs
~~~

This layout is **normative** for cultural landscape datasets and their metadata/provenance.

---

## 🌄 Cultural Landscape Categories (v11)

| Category               | Description                                  | CARE Level | Sovereignty Required | Status       |
|------------------------|----------------------------------------------|------------|----------------------|--------------|
| Settlement Regions     | Phase-specific habitation surfaces           | C2         | Yes                  | Allowed (generalized) |
| Territorial Boundaries | Cultural / tribal extents                    | C3–C4      | Yes                  | Conditional  |
| Mobility Routes        | Trails, trade routes, seasonal pathways      | C1–C2      | Sometimes            | Allowed      |
| Interaction Spheres    | Material-culture influence zones             | C2         | Yes                  | Allowed      |
| Resource Areas         | Procurement zones (stone, clay, fauna, etc.) | C2         | Yes                  | Conditional  |
| Sacred Landscapes      | Ceremonial or mythic geographies             | C4         | Yes                  | Restricted / Not Public |

**v11 prohibits** in public-governed layers:

- Precise geometry for sacred landscapes  
- Non-consented tribal knowledge and restricted cultural stories  
- Burial grounds, funerary objects, ritual geographies  
- Unreviewed ethnographic testimonies used as spatial evidence  
- Any dataset lacking formal sovereignty sign-off  

---

## 📦 Required Metadata (v11)

Every cultural landscape dataset MUST be backed by:

### STAC 1.0 Item / Collection (v11)

Required STAC fields (for public-governed layers):

- `id`  
- `stac_version: "1.0.0"`  
- `type: "Feature"` (Items) or `"Collection"` (groupings)  
- `bbox` (H3-generalized extents only)  
- `geometry`:
  - `Polygon` or `MultiPolygon` only for regions / resource areas  
- Temporal fields:
  - `properties.start_datetime` and `properties.end_datetime` for time-bounded landscapes  
- CARE and sovereignty:
  - `properties.care:sensitivity`  
  - `properties.care:sovereignty`  
  - `properties.care:consent_status` (where applicable)  
- Projection:
  - `proj:*` CRS metadata where needed  
- KFM extensions:
  - `properties.kfm:culture_phase` (or equivalent KFM phase field)  
  - `properties.kfm:generalization` (for example, `"H3-r8"`)  
  - `properties.kfm:provenance` (path to PROV-O bundle)  
- Assets:
  - Primary `data` asset (GeoJSON/COG/vector tiles) with appropriate roles

### DCAT 3.0 Metadata

Each dataset must have a DCAT 3.0 metadata record in `metadata/`:

- Dataset title, description, license, temporal/spatial coverage  
- Distributions that align with STAC assets  

### CARE and Sovereignty Metadata

Must include:

- Sensitivity classification  
- Cultural notes and context  
- Sovereignty decision path (including tribe / council where appropriate)  
- Consent provenance and conditions  
- Reviewer identities (FAIR+CARE and tribal where applicable)

---

## 🧪 Data Preparation Requirements (v11)

All cultural landscape datasets must:

- Use generalized polygons:
  - H3-based vectorization or topological simplification at sufficient scale.  
- Remove or generalize non-public cultural information:
  - No direct depiction of sacred sites or restricted pathways.  
- Use controlled vocabularies for:
  - `culture_phase`  
  - `region_type` (for example, settlement_region, mobility_corridor, resource_area)  
  - `route_type` (for example, trade, seasonal, migration)  
  - `interaction_type` (for example, influence_sphere, alliance_zone)  
- Provide temporal information in **OWL-Time** compatible form (Collections and/or Items).  
- Include a **Tribal Review Unit (TRU)** or equivalent record in the provenance log where required.  
- Include dataset-level sustainability telemetry (energy Wh, carbon gCO₂e) as per the telemetry schema.

Datasets that cannot meet these criteria must be held in governed, non-public registries rather than this directory.

---

## 🛰 Integration Into KFM Systems (v11)

### Neo4j Knowledge Graph

Cultural landscapes are modeled as:

**Nodes**

- `CulturalRegion`  
- `Route`  
- `InteractionSphere`  
- `ResourceArea`  

**Relationships**

- `TRAVERSED_BY` (Route ↔ CulturalRegion or Route ↔ Group/node in other domains)  
- `OCCUPIED_DURING` (CulturalRegion ↔ CulturalPhase / TimeInterval)  
- `ASSOCIATED_WITH` (CulturalRegion ↔ ArtifactInventories, StoryNodes, other datasets)  
- `GENERALIZED_FROM` (Public region ↔ internal higher-resolution representation, where allowed)  
- `CULTURAL_CONTINUUM_WITH` (relationships between regions across time)

### Story Node v3

Cultural landscape datasets support:

- Cultural narratives focused on regions and routes rather than sites.  
- Region evolution sequences across phases.  
- Mobility and trade storylines that respect sovereignty and CARE constraints.  
- Time-aligned overlays of cultural regions and resource areas.

### Focus Mode v3

Focus Mode uses these layers for:

- Sovereignty-aware, sensitivity-aware explanations of cultural geography.  
- Bias monitoring and guardrails for landscape narratives.  
- Provenance chips that show how regions and corridors were derived and reviewed.  
- Consent-based redaction for specific user profiles or views.

### MapLibre + Cesium

- Polygon layers for regions and resource areas.  
- Time-enabled region evolution.  
- 3D cultural landscapes in Cesium.  
- Animated mobility routes visualizing generalized movement patterns.

---

## 📊 Dataset Index (Illustrative)

| Dataset                                   | Category            | CARE | Sovereignty | Status   | Notes                                            |
|-------------------------------------------|---------------------|------|------------|----------|--------------------------------------------------|
| `regions/great-bend-aspect-v3`           | Interaction Sphere  | C2   | Yes        | 🟢 Active | Generalized polygons; approved for public catalog. |
| `routes/ancient-prairie-corridor-v2`     | Mobility            | C1   | Partial    | 🟢 Active | Ethnohistoric + archaeological synthesis; generalized. |
| `resource-areas/flint-hills-chert-v2`    | Resource Area       | C2   | Yes        | 🟡 Review | Ecological + cultural sensitivity review needed. |
| `regions/pawnee-territory-v2`            | Territorial         | C3–C4| Yes        | 🔒 Hold   | Requires additional Tribal Sovereignty Board approval. |

The authoritative index is derived from STAC Collections, metadata, provenance, and manifests; the table above is illustrative.

---

## 🧠 Example STAC Item (v11 Cultural Region)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "great-bend-aspect-v3",
  "bbox": [-101.7, 37.1, -95.2, 40.4],
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      [
        [ /* generalized polygon coordinates */ ]
      ]
    ]
  },
  "properties": {
    "kfm:domain": "archaeology-cultural-landscapes",
    "kfm:culture_phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "care:sovereignty": "protected",
    "care:consent_status": "approved",
    "kfm:generalization": "H3-r8",
    "start_datetime": "1200-01-01T00:00:00Z",
    "end_datetime": "1450-01-01T00:00:00Z",
    "kfm:provenance": "provenance/great-bend-aspect-v3.json"
  },
  "assets": {
    "data": {
      "href": "https://example.org/cultural-landscapes/great_bend_aspect_v3.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
~~~

This example is descriptive; actual schemas and constraints are defined under `stac/schemas/` and associated docs.

---

## 🕰 Version History

| Version   | Date       | Summary                                                                 |
|-----------|------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Aligned with KFM v11.2.3; added energy/carbon telemetry refs; clarified Focus Mode v3 and sovereignty integration; minor layout updates. |
| v11.0.0   | 2025-11-24 | Sovereignty-governed v11 rebuild; H3 r7–r10 generalization; CARE v11 metadata; PROV-O enriched lineage; AI governance integration. |
| v10.4.0   | 2025-11-17 | v10 cultural landscape index and initial governance rules.             |
| v10.0.0   | 2025-11-10 | Initial dataset structure for cultural landscapes.                     |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Archaeology Datasets](../README.md)
