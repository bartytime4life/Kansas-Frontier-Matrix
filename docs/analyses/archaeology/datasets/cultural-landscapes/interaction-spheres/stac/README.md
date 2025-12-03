---
title: "🗂️ Kansas Frontier Matrix — Interaction Sphere STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/README.md"
description: "STAC 1.0 catalog for KFM v11 interaction-sphere datasets, enabling governed discovery of generalized cultural connectivity zones under FAIR+CARE and sovereignty rules."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-interaction-spheres-stac-catalog-v11.2.3"
doc_kind: "STAC Catalog"
intent: "interaction-spheres-stac"
semantic_document_id: "kfm-doc-archaeology-interaction-spheres-stac-catalog-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-interaction-spheres-stac-catalog-v1.json"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🗂️ Kansas Frontier Matrix — Interaction Sphere STAC Catalog (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/README.md`

**Purpose**  
Provide the **authoritative STAC (SpatioTemporal Asset Catalog) index** for all **interaction sphere** datasets within the Kansas Frontier Matrix (KFM).

Interaction spheres model broad-scale patterns of:

- Cultural connectivity and shared material culture  
- Trade and exchange networks  
- Communication and migration pathways  
- Eco-cultural co-adaptation across regions  

This catalog ensures interaction-sphere datasets are:

- Machine-discoverable and queryable  
- FAIR+CARE and sovereignty aligned  
- STAC 1.0 compliant and schema-validated  
- Ontology-mapped to the KFM Knowledge Graph (CIDOC-CRM + GeoSPARQL + OWL-Time)  
- Ethically governed via CARE metadata and provenance  
- Fully integrated with Story Nodes and Focus Mode v3

---

## 📘 Overview

This STAC catalog directory provides:

- **STAC Collections** grouping interaction-sphere datasets by cultural domain  
- **STAC Items** describing individual interaction spheres  
- **Schemas** enforcing STAC + KFM + CARE rules  
- **Templates** for contributors authoring new Items/Collections  
- Crosswalks that keep **STAC ↔ DCAT ↔ PROV-O ↔ Graph** aligned  

Interaction spheres cataloged here include, for example:

- **Great Bend Aspect (v3)**  
- **Central Plains Exchange (v2)**  
- **Protohistoric Wichita corridor (v2, high sensitivity)**  
- Future expansions (for example, Caddoan borderlands, Plains–Apache exchanges)

All catalog entries correspond to **generalized** landscape layers; sensitive internals remain governed outside public STAC.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/
├── 📄 README.md                          # This file
├── 📂 collections/                       # STAC Collections for interaction spheres
│   ├── 📄 interaction-spheres.json       # Root collection for interaction spheres
│   ├── 📄 great-bend-aspect.json         # Great Bend Aspect collection
│   ├── 📄 central-plains-exchange.json   # Central Plains exchange collection
│   └── 📄 protohistoric-wichita.json     # Protohistoric Wichita corridor collection
├── 📂 items/                             # STAC Items (individual interaction spheres)
│   ├── 📄 great-bend-aspect-v3.json
│   ├── 📄 central-plains-exchange-v2.json
│   ├── 📄 protohistoric-wichita-v2.json
├── 📂 schemas/                           # STAC, KFM, CARE validation schemas
└── 📂 templates/                         # Contributor templates (Items + Collections)
~~~

This layout is **normative** for STAC catalog content in this sub-tree.

---

## 📚 Controlled Vocabularies (STAC Properties)

Interaction-sphere STAC Items and Collections should use the same vocabularies defined in the parent interaction-spheres README:

| Field                 | Allowed / Example Values                                       |
|-----------------------|----------------------------------------------------------------|
| `region_type`         | `interaction_sphere`, `exchange_zone`, `contact_region`        |
| `route_type`          | `trade`, `seasonal`, `migration`, `multimodal`, `other`        |
| `interaction_type`    | `influence_sphere`, `contact_zone`, `exchange_corridor`        |
| `care:consent_status` | `approved`, `conditional`, `not-approved`, `not-applicable`    |

These may appear as `properties.region_type`, `properties.kfm:region_type`, or in related KFM extension fields, depending on the extension schema.

---

## 🧭 STAC Collections (Required)

Each interaction sphere must belong to a **STAC Collection**, which defines the grouping context.

### Minimum Collection Requirements

Collections under `collections/` must include:

- STAC core:
  - `stac_version: "1.0.0"`  
  - `type: "Collection"`  
  - `id` (for example, `"interaction-spheres"`, `"great-bend-aspect"`)  
  - `description` (high-level cultural + temporal summary)  
  - `license` (for example, `"CC-BY-4.0"`)  
  - `extent.spatial` (generalized bbox)  
  - `extent.temporal` (OWL-Time compliant intervals)  

- KFM extensions:
  - `kfm:domain = "archaeology-cultural-landscapes"`  
  - `kfm:region_type` (for example, `interaction_sphere`, `exchange_zone`)  
  - `kfm:review_cycle` (for example, `"Biannual"`)  

- CARE fields:
  - `care:sensitivity` (for example, `"generalized"`, `"restricted-generalized"`)  
  - `care:sovereignty` (for example, `"protected"`)  
  - `care:notes` describing cultural-safety considerations  

Collections should also link (`links[]`) to their child Items and, where appropriate, to root or parent Collections.

---

## 📦 STAC Item Requirements

Each STAC Item describing an interaction sphere must meet these requirements:

### STAC Core

- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id` (stable, versioned; matches filename)  
- `bbox` (generalized bounding box)  
- `geometry`:
  - `Polygon` or `MultiPolygon` only  
  - Derived from generalized/H3-based geometries  
- `properties` (must include KFM + CARE extensions)  
- `assets`:
  - `data` asset with `href`, `type`, and `roles` including `"data"`

### KFM Interaction-Sphere Metadata (`kfm:*`)

Typical required fields (see extension schemas for exact constraints):

| Field                 | Description                                                  |
|-----------------------|--------------------------------------------------------------|
| `kfm:domain`          | Must be `"archaeology-cultural-landscapes"`                 |
| `kfm:culture_phase`   | Phase(s) defining the sphere (or `kfm:phase`)              |
| `kfm:region_type`     | One of the controlled `region_type` values                  |
| `kfm:generalization`  | Generalization level (for example, `"H3-r7"`, `"H3-r8"`)    |
| `kfm:provenance`      | Relative path to PROV-O lineage file                        |
| `kfm:review_cycle`    | For example, `"Biannual"`                                   |

Additional domain-specific fields (for example, `kfm:interaction_type`) may be enforced via schemas in `schemas/`.

### CARE Cultural-Safety Metadata (`care:*`)

| Field                   | Description / Rules                                      |
|-------------------------|----------------------------------------------------------|
| `care:sensitivity`      | `"general"`, `"generalized"`, or `"restricted-generalized"` (no `"restricted"` in public catalog) |
| `care:review`           | `"faircare"`, `"tribal"`, or `"none-required"`           |
| `care:notes`            | Required for `generalized` / `restricted-generalized`    |
| `care:visibility_rules` | For example, `"h3-only"` or `"no-exact-points"`          |
| `care:consent_status`   | `approved`, `conditional`, `not-approved`, `not-applicable` |

Items representing protohistoric or ethnohistoric interaction spheres typically require `care:review = "tribal"` and more cautious visibility rules.

### DCAT Crosswalk

Metadata in `metadata/` must map cleanly to STAC Item fields:

- `dct:title` ↔ STAC `id` or `description`  
- `dct:license` ↔ STAC `license`  
- `dct:temporal` ↔ STAC temporal properties or Collection `extent.temporal`  
- `dcat:distribution` ↔ STAC `assets.data.href`

### PROV-O Linkage

Each STAC Item must include:

- `kfm:provenance` → relative path to the corresponding PROV-O provenance JSON in `../provenance/`.

---

## 🌍 Spatial Requirements

- Use **generalized polygons** and/or **H3 mosaics (levels r5–r8)**; no site-level precision.  
- CRS must be **EPSG:4326** for STAC geometries and bboxes.  
- Geometry simplification is required for public release:
  - Remove fine-scale features that could imply specific sites or sacred places.  
- For highly sensitive spheres:
  - Visibility may be limited to `h3-only` (no explicit geometry in public STAC).

---

## 🕰 Temporal Requirements

- Use **OWL-Time–compatible** temporal ranges (for example, start and end datetimes).  
- Cultural-phase-based time windows should be consistent with:
  - Interaction-sphere metadata  
  - Associated Story Nodes and Focus Mode timelines.  
- Multi-era spheres must represent the full range of evidence coverage.

---

## ⚖️ Cultural, Ethical & Sovereignty Governance

Interaction spheres are culturally sensitive interpretive products. Therefore:

### Required

- FAIR+CARE governance review.  
- Tribal/sovereignty review for protohistoric and ethnohistoric interaction spheres.  
- Cultural framing that emphasizes interpretive limits and avoids colonial or essentialist language.  
- Documentation (via `care:notes` and provenance) of:
  - Generalization choices  
  - Ethical filtering and masking  
  - Review bodies and consent pathways  

### Forbidden

- `care:sensitivity = "restricted"` for public STAC Items in this catalog.  
- Exact cultural boundaries, especially where contested or unapproved.  
- Restricted ceremonial or oral-history content mapped directly to polygons.  
- Raw or site-precise spatial data tied to sacred or protected landscapes.

---

## 🧪 Validation Requirements

STAC Items and Collections must validate against:

1. `stac-item-schema.json` (Item structure and STAC core fields)  
2. `stac-collection-schema.json` (Collection structure)  
3. `kfm-archaeology-extension.json` (or cultural-landscapes extension)  
4. `care-sensitivity-extension.json` (CARE values and rules)  
5. `dcat-crosswalk.json` (DCAT ↔ STAC alignment)  
6. Provenance-link schemas (confirm `kfm:provenance` correctness)  
7. Spatial generalization checks (H3/generalization constraints)  

CI workflows include, for example:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`

Any failure blocks catalog updates and triggers governance review.

---

## 🧠 KFM Ecosystem Integration

### Knowledge Graph

From this catalog, ingestion creates:

**Nodes**

- `InteractionSphere`  
- `CulturalRegion`  
- `CulturePhase`  
- `MaterialPattern`  

**Edges**

- `GENERALIZED_FROM`  
- `ASSOCIATED_WITH` (to artifact inventories, Story Nodes, other layers)  
- `OCCURRED_DURING` (temporal links to phases)  
- `HAS_PROVENANCE`  
- `HAS_METADATA`  
- `HAS_CARE_SENSITIVITY`

### Story Node v3

- Interaction sphere STAC Items inform story networks and cross-regional narratives.  
- Provenance and CARE data control what is surfaced and how it is framed.

### Focus Mode v3

- Provides cultural overlay context and network-aware explanations.  
- Applies sovereignty and CARE filters based on metadata and STAC properties.  
- Uses provenance paths for explanation chips and user-facing audit trails.

---

## 🔗 Related Specifications

For full governance of interaction-sphere data, also see:

- `../README.md`  
  – Interaction spheres dataset overview (semantic and governance context).  
- `../metadata/README.md`  
  – DCAT + CARE metadata for interaction spheres.  
- `../provenance/README.md`  
  – PROV-O lineage & sovereignty review logs.  
- `../../stac/schemas/README.md`  
  – STAC schema definitions (Items, Collections, extensions).  

---

## 📊 Catalog Index (Illustrative)

| STAC Item                         | Collection                | Sensitivity            | Review        | Status   |
|----------------------------------|---------------------------|------------------------|---------------|----------|
| `great-bend-aspect-v3.json`     | `great-bend-aspect.json`  | generalized            | FAIR+CARE     | 🟢 Active |
| `central-plains-exchange-v2.json`| `central-plains-exchange.json` | generalized      | FAIR+CARE     | 🟢 Active |
| `protohistoric-wichita-v2.json`  | `protohistoric-wichita.json`   | restricted-generalized | Tribal + FAIR+CARE | 🟡 Review |

Authoritative status and review flags live in metadata, provenance, and manifests; the table above is descriptive.

---

## 🕰 Version History

| Version   | Date       | Author                                                   | Summary                                                                 |
|-----------|------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee | Updated to KFM v11.2.3; added controlled vocabularies, related-spec links, telemetry refs, and clarified sovereignty-aware validation. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council               | Created full STAC catalog system for interaction spheres including STAC/DCAT/CARE alignment. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                                  | Initial catalog scaffold.                                              |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Spheres](../README.md)
