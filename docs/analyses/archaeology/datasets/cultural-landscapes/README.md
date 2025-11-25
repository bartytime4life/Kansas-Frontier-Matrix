---
title: "🏞️ Kansas Frontier Matrix — Cultural Landscape Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Tribal Sovereignty Review Board"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_guid: "urn:kfm:doc:archaeology-cultural-landscapes-v11.0.0"
doc_kind: "Dataset Category"
intent: "archaeology-cultural-landscapes"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes"

sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-cultural-landscapes-v11.json"
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
sensitivity: "Cultural / Historical / Archaeological"
sensitivity_level: "Medium"
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

# 🏞️ **Kansas Frontier Matrix — Cultural Landscape Datasets (v11)**  
`docs/analyses/archaeology/datasets/cultural-landscapes/README.md`

**FAIR+CARE Certified · Sovereignty-Governed · Diamond⁹ Ω / Crown∞Ω**

**Purpose:**  
Define and govern all **cultural landscape datasets** used in KFM v11, covering:  
settlement systems, movement corridors, territorial extents, interaction spheres, and resource-procurement landscapes across Kansas.

These datasets feed directly into:  
**Story Node v3 · Focus Mode v3 · Cesium 3D Reconstructions · MapLibre time-aware layers · Neo4j cultural-region graph models**

</div>

---

# 📘 v11 Overview

Cultural landscapes in KFM represent **human–land relationships across time**, including:

- Ancient & protohistoric **mobility corridors**  
- Cultural-phase **settlement regions**  
- **Interaction spheres** (e.g., Great Bend aspect)  
- **Territorial boundaries** (generalized; sovereignty-governed)  
- **Resource procurement zones** (e.g., chert, clay, fauna)  
- **Sacred / cultural landscapes** (when permitted under sovereignty rules)  

**v11 introduces:**

- Mandatory **H3 r7–r10 generalization**  
- Cultural & sovereignty AI governance filters  
- Expanded CARE labels & consent flags  
- PROV-O enriched lineage bundles  
- DCAT 3.0 / STAC 1.0 v11-compliant metadata  
- Sustainability metrics per dataset (energy, carbon)

Restricted, sacred, or sovereignty-governed data must follow strict redaction rules.

---

# 🗂️ Directory Layout (v11)

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/
├── README.md                    # This file
├── regions/                     # Settlement regions, tribal/cultural areas (generalized)
├── routes/                      # Mobility corridors, seasonal pathways
├── interaction-spheres/         # Cultural influence zones (Great Bend, Pawnee, etc.)
├── resource-areas/              # Procurement zones (stone, clay, fauna)
├── stac/                        # STAC Items/Collections (v11 spec)
├── metadata/                    # DCAT 3.0 + CARE metadata
└── provenance/                  # PROV-O lineage + sovereignty review logs
~~~

---

# 🌄 Cultural Landscape Categories (v11)

| Category | Description | CARE Level | Sovereignty Required | Status |
|---------|-------------|------------|-----------------------|--------|
| **Settlement Regions** | Phase-specific habitation surfaces | C2 | Yes | Allowed (generalized) |
| **Territorial Boundaries** | Cultural/tribal extents | C3–C4 | Yes | Conditional |
| **Mobility Routes** | Trails, trade, conflict/peace routes | C1–C2 | Sometimes | Allowed |
| **Interaction Spheres** | Material-culture influence zones | C2 | Yes | Allowed |
| **Resource Areas** | Chert quarries, clay beds, hunting zones | C2 | Yes | Conditional |
| **Sacred Landscapes** | Ceremonial or mythic geographies | C4 | Yes | Restricted / Not Public |

**v11 Prohibits:**  
- Precise coordinates for sacred landscapes  
- Non-consented tribal knowledge  
- Burial grounds, funerary objects, or ritual geographies  
- Unreviewed ethnographic testimonies  
- Any dataset lacking sovereignty sign-off

---

# 📦 Required Metadata (v11 Hard Requirements)

Every dataset MUST include:

## ✔ STAC Item / Collection (v11)
Fields:

- `id`  
- `bbox` (H3 generalized)  
- `geometry` (polygon/multipolygon only)  
- `start_datetime` / `end_datetime`  
- `care:sensitivity`, `care:sovereignty`, `care:consent_status`  
- `proj:*` CRS metadata  
- `kfm:culture_phase`  
- `kfm:generalization`: `"H3-r7"` → `"H3-r10"`  
- `kfm:provenance`: PROV-O bundle link  
- Assets for GeoJSON, COG, vector tiles  

## ✔ DCAT 3.0 Metadata

## ✔ CARE v11 Metadata

Must include:

- Sensitivity class  
- Cultural notes  
- Sovereignty decision path  
- Consent provenance  
- Reviewer identity (tribal + FAIR+CARE)

---

# 🧪 Data Preparation Requirements (v11)

All datasets must:

- Use generalized polygons (H3 or topological simplification)  
- Strip all non-public cultural information  
- Use controlled vocabularies:
  - `culture_phase`
  - `region_type`
  - `route_type`
  - `interaction_type`  
- Provide temporal phases (OWL-Time compatible)  
- Include a TRU (Tribal Review Unit) record in provenance logs  
- Include dataset-level sustainability telemetry (Wh, gCO₂e)

---

# 🛰 Integration Into KFM Systems (v11)

## Neo4j Graph

Nodes:
- `CulturalRegion`, `Route`, `InteractionSphere`, `ResourceArea`

Relationships:
- `TRAVERSED_BY`
- `OCCUPIED_DURING`
- `ASSOCIATED_WITH`
- `GENERALIZED_FROM`
- `CULTURAL_CONTINUUM_WITH`

## Story Node v3
- Cultural narratives  
- Region evolution sequences  
- Mobility + trade storylines  
- Time-aligned cultural region overlays  

## Focus Mode v3
- Sovereignty-aware narrative filters  
- Cultural bias monitoring  
- Explainability and provenance chips  
- Consent-based redaction layers  

## Mapping (MapLibre + Cesium)
- Polygon layers  
- Time-enabled region evolution  
- 3D cultural landscapes  
- Animated movement routes  

---

# 📊 Dataset Index (v11)

| Dataset | Category | CARE | Sovereignty | Status | Notes |
|---|---|---|---|---|---|
| `regions/great-bend-aspect-v3` | Interaction Sphere | C2 | Yes | 🟢 Active | Generalized polygons |
| `routes/ancient-prairie-corridor-v2` | Mobility | C1 | Partial | 🟢 Active | Ethnohistoric + archaeological synthesis |
| `resource-areas/flint-hills-chert-v2` | Resource Area | C2 | Yes | 🟡 Review | Ecological sensitivity review needed |
| `regions/pawnee-territory-v2` | Territorial | C3–C4 | Yes | 🔒 Hold | Requires Tribal Sovereignty Board approval |

---

# 🧠 Example STAC Item (v11 Cultural Region)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "great-bend-aspect-v3",
  "bbox": [-101.7, 37.1, -95.2, 40.4],
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [[[ ... ]]]
  },
  "properties": {
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
      "href": "https://example.org/cl-v3/great_bend_aspect_v3.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
~~~

---

# 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| **v11.0.0** | 2025-11-24 | Sovereignty-governed v11 rebuild; H3 r7–r10 generalization; CARE v11 metadata; PROV-O enriched lineage; AI governance integration |
| v10.4.0 | 2025-11-17 | v10 cultural landscape index |
| v10.0.0 | 2025-11-10 | Initial dataset structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Archaeology Datasets](../README.md)

</div>