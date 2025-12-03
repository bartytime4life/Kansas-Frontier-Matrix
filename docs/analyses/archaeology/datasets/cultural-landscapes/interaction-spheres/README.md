---
title: "🌀 Kansas Frontier Matrix — Cultural Landscape Interaction Spheres (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/README.md"
description: "Generalized cultural interaction-sphere datasets in KFM v11, representing regional material-culture connectivity and trade networks under FAIR+CARE and sovereignty governance."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Tribal Sovereignty Review Board"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-cultural-landscapes-interaction-spheres-v11.2.3"
doc_kind: "Dataset Subcategory"
intent: "archaeology-interaction-spheres"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-interaction-spheres-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-interaction-spheres-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🌀 Kansas Frontier Matrix — Cultural Landscape Interaction Spheres (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/README.md`

**Purpose**  
Define, document, and govern all **interaction sphere datasets** used in the Kansas Frontier Matrix (KFM) v11.

Interaction spheres represent **regional-scale cultural connectivity zones**, defined by:

- Shared material-culture traits  
- Overlapping trade, communication, or migration networks  
- Cross-regional interaction and contact patterns  
- Co-adaptation to similar environmental regimes  

These datasets feed:

- Cultural-phase and cultural-region mapping  
- Story Node v3 cultural network models  
- Focus Mode v3 interpretive overlays and explanations  
- MapLibre + Cesium landscape synthesis  
- AI-assisted movement and diffusion modeling  
- Neo4j knowledge-graph cultural-relationship linking  

All interaction spheres are **generalized**, **CARE-audited**, and **sovereignty-governed** before inclusion.

---

## 📘 Overview

Interaction spheres in KFM represent **broad cultural zones** rather than hard boundaries. They are derived from:

- Shared artifact styles and assemblage patterns  
- Technological traditions and subsistence parallels  
- Trade, exchange, and contact evidence (material and textual)  
- Ethnohistoric and archival sources (where permitted)  
- Aggregated artifact inventories and cultural landscape layers  

Examples include:

- **Great Bend Aspect** zones  
- **Central Plains Tradition** exchange regions  
- **Protohistoric Wichita interaction corridors**  
- **Northern Plains–Central Plains contact regions**

All geometries are **generalized polygons or H3 mosaics** to protect sensitive landscapes and respect sovereignty.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/
├── 📄 README.md                      # This file
├── 📂 great-bend-aspect/             # Generalized polygons & metadata for Great Bend aspect
├── 📂 central-plains-exchange/       # Multi-era interaction zones
├── 📂 protohistoric-wichita/         # Ethnohistoric/archaeological overlap regions
├── 📂 stac/                          # STAC Items & Collections for interaction spheres
├── 📂 metadata/                      # DCAT, CARE, and cultural notes
└── 📂 provenance/                    # PROV-O lineage & review logs (including tribal review)
~~~

This layout is **normative** for interaction-sphere datasets and their metadata/provenance.

---

## 🌀 Dataset Definition

| Component            | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Interaction Sphere** | A cultural region defined by shared material culture and interaction patterns |
| **Temporal Span**    | Typically multi-century; modeled using OWL-Time intervals                   |
| **Spatial Representation** | Generalized polygons or H3 mosaic surfaces (no site-level precision) |
| **Sources**          | Archaeological literature, aggregated artifact inventories, ethnohistoric sources (where governed) |
| **Cultural Sensitivity** | Tribal/sovereignty review strongly recommended; CARE metadata required |

Interaction spheres are **interpretive constructs** and must be documented as such; they should never be presented as rigid territorial claims.

---

## 🧭 Example Cultural Interaction Spheres

### Great Bend Aspect Interaction Sphere

- Temporal: Late Prehistoric / Protohistoric (AD 1300–1700).  
- Defined by: ceramic styles, lithic patterns, settlement morphology, and subsistence signatures.  
- Interpretive linkage: often associated with ancestors of protohistoric Wichita communities.  
- Environmental footprint: Central Plains plus southern Flint Hills, generalized to safe polygons.

### Central Plains Tradition Exchange Region

- A material-flow zone connecting Smoky Hill, Republican, and Platte drainages.  
- Shared architectural traits, pottery motifs, and faunal exploitation patterns.  
- Represents an **exchange sphere**, not a hard boundary.

### Protohistoric Wichita Corridor

- Interaction route linking southern Plains, Great Bend aspects, and early European trade networks.  
- High cultural sensitivity → **tribal/sovereignty review mandatory**.  
- Spatial representation must be highly generalized and carefully documented.

---

## 📦 Required Metadata (All Interaction Sphere Datasets)

Every interaction-sphere dataset must be backed by complete STAC, DCAT, CARE, and provenance metadata.

### STAC Item Requirements (v11)

Required fields (Item-level):

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id` (versioned, e.g., `"great-bend-aspect-v3"`)  
- `bbox` (generalized; derived from generalized geometry)  
- `geometry`:
  - `Polygon` or `MultiPolygon` only  
- `properties` must include:
  - `kfm:domain` (for example, `"archaeology-cultural-landscapes"`)  
  - `kfm:culture_phase` (or `kfm:phase` depending on extension)  
  - `kfm:generalization` (for example, `"H3-r8"`)  
  - `kfm:provenance` (provenance JSON path)  
  - `care:sensitivity` (`"generalized"` or `"restricted-generalized"`)  
  - `care:sovereignty` (for example, `"protected"`)  
  - `care:consent_status` (for example, `"approved"` or `"conditional"`)  

Assets:

- Primary `data` asset (GeoJSON/COG/vector tiles) with:
  - `href`, `type`, and `roles` including `"data"`.

Example STAC snippet (illustrative):

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "great-bend-aspect-v3",
  "bbox": [-101.8, 37.0, -95.3, 40.5],
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [[[ /* generalized coordinates */ ]]]
  },
  "properties": {
    "kfm:domain": "archaeology-cultural-landscapes",
    "kfm:culture_phase": "Late Prehistoric",
    "kfm:generalization": "H3-r8",
    "care:sensitivity": "generalized",
    "care:sovereignty": "protected",
    "care:consent_status": "approved",
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

---

## ⚖️ Cultural & Ethical Requirements (FAIR+CARE + Sovereignty)

Interaction-sphere datasets must:

- Avoid implying rigid or ahistorical boundaries; emphasize **fluidity and interpretive uncertainty**.  
- Use non-essentialist, non-colonial language (avoid “tribal territory” without explicit consent).  
- Provide cultural notes explaining interpretive limits and data sources.  
- Generalize or omit zones that intersect sacred or restricted landscapes unless explicit tribal authorization exists.  
- Never include sacred sites, ceremonial centers, or restricted geographies in identifiable form.  
- Receive Indigenous/tribal review for protohistoric, ethnohistoric, or high-sensitivity spheres.

Forbidden content in public-governed interaction-sphere layers:

- Exact outlines of sacred or ceremonial landscapes.  
- Precise territorial claims presented without tribal consent.  
- Raw archaeological site locations or clusterings that could reveal protected places.  
- Non-consented ethnographic accounts mapped directly into polygons.

---

## 📊 Dataset Index (Illustrative)

| Dataset                               | Category           | CARE | Sovereignty | Status   | Notes                                                    |
|---------------------------------------|--------------------|------|------------|----------|----------------------------------------------------------|
| `great-bend-aspect/v3`               | Great Bend Aspect  | C2   | Yes        | 🟢 Active | Generalized polygons; CARE and sovereignty review done.  |
| `central-plains-exchange/v2`         | Exchange Sphere    | C2   | Yes        | 🟢 Active | STAC + DCAT compliant; interpretive uncertainty noted.   |
| `protohistoric-wichita/v2`           | Protohistoric Corridor | C3–C4 | Yes    | 🟡 Review | Tribal consultation ongoing; higher generalization required. |

The canonical status, review dates, and flags are derived from metadata, provenance, and manifests; this table is descriptive.

---

## 🧪 Integration Into KFM Ecosystem

### Neo4j Knowledge Graph

Interaction-sphere datasets become:

**Nodes**

- `InteractionSphere`  
- `CulturePhase`  
- `CulturalRegion`  
- `MaterialPattern`  

**Relationships**

- `INTERACTED_WITH` (InteractionSphere ↔ other regions/groups)  
- `OVERLAPS` (InteractionSphere ↔ other landscape layers)  
- `ASSOCIATED_WITH` (InteractionSphere ↔ ArtifactInventories, StoryNodes)  
- `GENERALIZED_FROM` (public polygons ↔ internal higher-resolution representations)

### Focus Mode v3

Interaction-sphere layers support:

- Cultural network narratives and regional interaction explanations.  
- Time-aware overlays of interaction zones and material flows.  
- Sovereignty-aware, sensitivity-aware responses with provenance chips.  
- Guardrails that minimize overstatement of territorial certainty.

### Story Node v3

Interaction spheres enrich Story Nodes with:

- Cultural network context across phases.  
- Trade and migration sequence scaffolds.  
- Multi-region archaeological storylines built from generalized, governed regions.

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · FAIR+CARE Council · Tribal Sovereignty Review Board | Updated to KFM v11.2.3; aligned with cultural-landscapes v11; added sovereignty + telemetry integration details and Focus Mode v3 framing. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council       | Created interaction-spheres directory; added metadata, CARE, and STAC requirements. |
| v10.0.0   | 2025-11-10 | Cultural Landscape Team                  | Initial category structure for interaction spheres.                     |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscapes](../README.md)
