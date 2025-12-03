---
title: "🏺 Kansas Frontier Matrix — STAC Collection: Protohistoric Wichita Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/README.md"
description: "STAC 1.0 Collection + Item documentation for the Protohistoric Wichita interaction-sphere dataset in KFM v11, aligned with KFM, CARE, and sovereignty governance."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review Required"
content_stability: "stable"
status: "Active / Enforced (Tribal Review Required)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-protohistoric-wichita-stac-collection-v11.2.3"
doc_kind: "STAC Collection"
intent: "archaeology-interaction-spheres-protohistoric-wichita-stac"
semantic_document_id: "kfm-doc-archaeology-protohistoric-wichita-stac-collection-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/analyses-archaeology-interaction-spheres-stac-v1.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Historical / Archaeological"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/README.md@v10.4.1"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🏺 STAC Collection: Protohistoric Wichita Interaction Sphere (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/README.md`

**Purpose**  
Describe the **STAC 1.0 Collection and Items** for the **Protohistoric Wichita Interaction Sphere** within KFM v11.

This README focuses on:

- The **local STAC Collection** for this dataset.  
- The **STAC Item(s)** representing generalized interaction-sphere geometry.  
- How these STAC artifacts integrate with:
  - The **global interaction-sphere STAC catalog**.  
  - DCAT metadata and PROV-O provenance.  
  - CARE and sovereignty governance.

For cultural and historical context, see the parent dataset README:

- `../README.md`

---

## 📘 Overview

The Protohistoric Wichita interaction sphere is a **high-sensitivity cultural landscape** representing:

- Generalized zones of protohistoric Wichita interaction, exchange, and contact (ca. AD 1500–1700).  
- Synthesized from archaeological, ethnohistoric, and environmental evidence.  
- Governed under high-sensitivity CARE rules with **mandatory tribal review**.

This STAC folder provides:

- A **Collection** describing the overall dataset (`collection.json`).  
- One or more **Items** that represent generalized polygons at public-governed resolution.  
- Integration hooks for DCAT, provenance, and the global interaction-sphere STAC catalog.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/
├── 📄 README.md                       # This file
├── 📄 collection.json                 # STAC Collection: Protohistoric Wichita Interaction Sphere
└── 📂 items/
    └── 📄 protohistoric-wichita-v2.json  # STAC Item for this interaction sphere
~~~

IDs and filenames must be consistent across:

- `collection.json`  
- `items/protohistoric-wichita-v2.json`  
- `../metadata/protohistoric-wichita-v2.json`  
- `../provenance/protohistoric-wichita-v2.json`

---

## 📦 STAC Collection (`collection.json`)

The Collection provides the **top-level STAC descriptor** for this dataset.

### Required STAC Core Fields

- `stac_version: "1.0.0"`  
- `type: "Collection"`  
- `id`: for example, `"protohistoric-wichita-interaction-sphere"`  
- `description`: cultural scope and high-level summary  
- `license`: `"CC-BY-4.0"` (plus CARE/sovereignty conditions in metadata)  
- `extent`:
  - `extent.spatial.bbox` — generalized bounding box for the interaction sphere.  
  - `extent.temporal.interval` — OWL-Time–compatible `[start, end]` intervals (for example, `[["1500-01-01T00:00:00Z","1700-01-01T00:00:00Z"]]`).  

### KFM & CARE Fields (Collection-Level)

Typical properties (see global interaction-sphere schemas for exact constraints):

- `kfm:domain = "archaeology-cultural-landscapes"`  
- `kfm:region_type = "interaction_sphere"`  
- `kfm:review_cycle` (for example, `"Biannual"` or `"Quarterly"`)  
- `care:sensitivity` — `"restricted-generalized"` (expected for this dataset)  
- `care:review` — `"tribal"` plus FAIR+CARE where applicable  
- `care:sovereignty` — `"protected"`  
- `care:notes` — summary of high-level cultural safety decisions and conditions  

### Links

Collection `links[]` should include:

- `self` — reference to `collection.json`.  
- `root` or parent, if linking into the global interaction-sphere STAC catalog.  
- `item` — links to `items/protohistoric-wichita-v2.json`.  
- Optional links to documentation (dataset README, provenance README).

---

## 📦 STAC Item (`items/protohistoric-wichita-v2.json`)

The STAC Item represents the **generalized interaction-sphere geometry** and main assets.

### STAC Core Fields

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id: "protohistoric-wichita-v2"`  
- `bbox` — generalized bounding box (`[minLon, minLat, maxLon, maxLat]`).  
- `geometry`:
  - `type`: `"Polygon"` or `"MultiPolygon"`  
  - `coordinates`: highly generalized polygons only (H3-derived or similar).  

### KFM & CARE Properties

Required `properties` (summary; see schema docs for full list):

- `kfm:domain = "archaeology-cultural-landscapes"`  
- `kfm:region_type = "interaction_sphere"`  
- `kfm:culture_phase` / `kfm:phase` = `"Protohistoric-Wichita"` or equivalent canonical label(s)  
- `kfm:generalization` = for example, `"H3-r7"` or `"H3-r8"`  
- `kfm:provenance` = `"../provenance/protohistoric-wichita-v2.json"`  

CARE fields MUST reflect high sensitivity:

- `care:sensitivity = "restricted-generalized"`  
- `care:review = "tribal"` (plus FAIR+CARE, if recorded)  
- `care:sovereignty = "protected"`  
- `care:consent_status` — for example, `"conditional"` until full approval.  
- `care:notes` — summary of redaction and generalization decisions.  
- `care:visibility_rules = "h3-only"` for public-facing geometry, unless explicitly relaxed by sovereignty policy.

### Assets

At minimum:

- `assets.data`:
  - `href` → path or URL to generalized GeoJSON (for example, `"../protohistoric-wichita.geojson"` or a remote endpoint).  
  - `type` → `"application/geo+json"` or appropriate MIME type.  
  - `roles` → must include `"data"`.

Additional assets (for example, tilesets or PDF context maps) may be referenced as governed by CARE and sovereignty rules.

---

## 📚 Controlled Vocabularies (Local Use)

This STAC Collection/Item should align with global interaction-sphere vocabularies:

| Field                  | Allowed / Example Values                                       |
|------------------------|----------------------------------------------------------------|
| `kfm:region_type`      | `interaction_sphere`                                           |
| `kfm:interaction_type` | `influence_sphere`, `exchange_corridor`, `contact_zone`       |
| `care:consent_status`  | `approved`, `conditional`, `not-approved`, `not-applicable`    |

These are enforced or checked via schemas under:

- `../../stac/schemas/`

---

## 🧪 Validation & Governance

This Collection and its Item must pass:

- **STAC schemas**:
  - `stac-collection-schema.json` (for `collection.json`)  
  - `stac-item-schema.json` (for `protohistoric-wichita-v2.json`)  
- **KFM extensions**:
  - Cultural-landscape/interaction-sphere extension (`kfm:*`).  
- **CARE extensions**:
  - CARE cultural-safety schema (`care:*` fields).  
- **DCAT crosswalk**:
  - Alignment with `../metadata/protohistoric-wichita-v2.json`.  
- **Provenance crosswalk**:
  - Alignment with `../provenance/protohistoric-wichita-v2.json`.

CI workflows (for example `artifact-stac-validate.yml`, `metadata-validate.yml`, `faircare-audit.yml`) must all pass before changes are merged or released.

Any change to:

- Geometry,  
- Temporal coverage,  
- CARE or sovereignty metadata, or  
- Provenance linkage  

**must** be reflected consistently across STAC, metadata, provenance, and the dataset README, and be subject to **tribal review**.

---

## 🔗 Related Specifications

- `../README.md`  
  – Protohistoric Wichita interaction-sphere dataset overview and cultural context.  
- `../../stac/README.md`  
  – Interaction-sphere STAC catalog (Items + Collections overview).  
- `../../stac/items/README.md`  
  – STAC Item requirements for interaction spheres.  
- `../../stac/schemas/README.md`  
  – STAC schemas and extensions used by this Collection and Item.  
- `../metadata/README.md`  
  – DCAT + CARE metadata for this dataset.  
- `../provenance/README.md`  
  – Provenance index and requirements for Protohistoric Wichita.

---

## 🕰 Version History

| Version   | Date       | Author                                           | Summary                                                                 |
|-----------|------------|--------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisors | Aligned with KFM v11.2.3; updated front matter; clarified STAC Collection/Item fields, CARE/sovereignty expectations, and crosswalks. |
| v10.4.1   | 2025-11-17 | Lead Programmer · Archaeology WG                | v10.4.1 STAC documentation; expanded multi-layer Item set for v10.x context. |
| v10.4.0   | 2025-11-15 | Archaeology WG                                   | Initial Protohistoric Wichita STAC collection structure.               |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Protohistoric Wichita Dataset](../README.md)
