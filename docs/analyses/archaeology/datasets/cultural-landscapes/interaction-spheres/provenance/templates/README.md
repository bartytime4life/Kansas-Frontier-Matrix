---
title: "🏺 Kansas Frontier Matrix — Archaeology Provenance Templates (Interaction Spheres) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/templates/README.md"
description: "Template library for PROV-O + CARE provenance artifacts for KFM v11 interaction-sphere datasets, aligned with STAC, DCAT, and graph ingestion."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-interaction-spheres-provenance-templates-v11.2.3"
doc_kind: "Template Library"
intent: "interaction-sphere-provenance-templates"
semantic_document_id: "kfm-doc-archaeology-interaction-spheres-provenance-templates-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Provenance · Templates"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-interaction-spheres-provenance-templates-v1.json"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/templates/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🏺 Archaeology Provenance Templates (Interaction Spheres) — KFM v11

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/templates/README.md`

**Purpose**  
Define **standard, KFM-governed provenance templates** for archaeology **interaction-sphere datasets**  
(for example, Great Bend Aspect, Protohistoric Wichita, and related cultural landscapes).

These templates ensure every interaction-sphere dataset records:

- **Sources** (archives, repositories, field projects, literature)  
- **Transformations** (georeferencing, digitization, generalization, modeling)  
- **Review & governance** (FAIR+CARE, tribal/sovereignty review, redaction decisions)  
- **Lineage** from raw → generalized → processed  
- **Graph links** into Neo4j, Story Nodes, and Focus Mode v3

Templates are designed to be:

- **PROV-O JSON-LD compatible**  
- **CARE and sovereignty-aware**  
- **STAC / DCAT crosswalkable**  
- **Machine-validated in CI**  
- **Hydratable into the KFM knowledge graph**

---

## 📘 Overview

This directory provides **canonical provenance templates** for all archaeology interaction-sphere datasets under:

- `docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/**`

The templates:

- Capture **where data came from**.  
- Track **how they were processed and generalized**.  
- Record **who did what, when, and with which tools**.  
- Align with:
  - **PROV-O** (Entity / Activity / Agent)  
  - **STAC 1.0** (for `kfm:provenance` references)  
  - **DCAT 3.0** (for dataset-level provenance fields)  
  - **Story Node / Focus Mode v3** provenance chips and narrative context  

All interaction-sphere datasets MUST have provenance artifacts derived from these templates.

---

## 🗂 Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/templates/
├── 📄 README.md                          # This file
├── 📄 dataset-provenance.template.yml    # Dataset-level provenance summary (human + machine-readable)
├── 📄 sources-registry.template.csv      # Registry of all input sources
├── 📄 transformations-log.template.csv   # ETL and modeling step log
├── 📄 qa-checklist.template.md           # QA + FAIR+CARE review checklist
└── 📄 story-links.template.json          # Mapping from datasets to Story Nodes / Focus Mode entities
~~~

These templates mirror the **artifact-inventories provenance templates**, but are tuned to interaction-sphere and cultural-landscape use cases.

---

## 🧩 Template Types

### 1️⃣ Dataset-Level Provenance (YAML)

**File:** `dataset-provenance.template.yml`

Use this to describe a full interaction-sphere dataset, for example:

- `"Great Bend Aspect Interaction Sphere v3"`  
- `"Protohistoric Wichita Exchange Corridor v2"`

Key sections (to be adapted per dataset):

- `id` — stable dataset identifier (URN, UUID, or STAC/metadata ID).  
- `title`, `description` — human-readable label and abstract.  
- `collection` — STAC Collection ID (for example, `"great-bend-aspect"`).  
- `spatial_extent` — generalized bbox and region description.  
- `temporal_extent` — start/end ISO dates with precision notes (OWL-Time aligned).  
- `license`, `rights`, `access_constraints` — include CARE + sovereignty notes.  
- `lineage` — narrative summary of major processing stages.  
- `sources_ref` — links into `sources-registry.csv`.  
- `transformations_ref` — links into `transformations-log.csv`.  
- `care` and `sovereignty` — summary of sensitivity, review, and consent status.  
- `graph_links` — optional hints for Neo4j node/label creation.

### 2️⃣ Sources Registry (CSV)

**File:** `sources-registry.template.csv`

One row per **input source** used to build or update the interaction-sphere dataset.

Suggested columns:

- `source_id` — local identifier (`GBA_LIT_001`, `MAP_1894_01`, etc.).  
- `title` — source title (map name, article, report, dataset).  
- `creator` — person or organization.  
- `year` — publication or observation year.  
- `repository` — KHS, tribal archive, university, PD repository, etc.  
- `access_uri` — URL or catalog ID if available.  
- `license` — rights/usage conditions.  
- `sensitivity` — `public`, `restricted`, `generalize`.  
- `notes` — free-text context (for example, "used only as a coarse reference").

### 3️⃣ Transformations Log (CSV)

**File:** `transformations-log.template.csv`

Chronological log of ETL and modeling steps, keyed to scripts and MCP experiments.

Suggested columns:

- `step_id` — for example, `T001`, `T002`.  
- `activity_label` — `"Georectify 1894 topo map"`, `"H3 generalization"`.  
- `input_entities` — list of `source_id` or dataset IDs.  
- `output_entities` — IDs of resultant datasets/layers.  
- `script_or_tool` — Python module, QGIS algorithm, manual QGIS/QField, etc.  
- `experiment_id` — link to MCP experiment doc (for example, `EXP-INTSPHERE-2025-03`).  
- `run_date` — ISO date.  
- `operator` — analyst or team.  
- `qa_status` — `pending`, `approved`, `rejected`.  
- `notes` — free text description of caveats or special handling.

### 4️⃣ QA & FAIR+CARE Checklist (Markdown)

**File:** `qa-checklist.template.md`

A guided checklist for:

- Data quality (schema completeness, types, ranges, topological checks).  
- Spatial generalization (H3/generalization level, no precise sites).  
- CARE and sovereignty review:
  - Consent, community consultation, authority to control, and benefit sharing.  
- Narrative risk checks:
  - Avoiding harmful framing in Story Nodes and Focus Mode.  
- Licensing and rights confirmation.

This document is meant for human reviewers but can be inspected by CI for completion flags.

### 5️⃣ Story / Focus Links (JSON)

**File:** `story-links.template.json`

Maps interaction-sphere datasets to narrative and graph entities.

Typical content:

- Dataset-level entries:
  - `dataset_id` (aligned with STAC/metadata).  
  - `story_node_ids` relevant to the sphere.  
  - `focus_entity_ids` (for example, `CulturalRegion`, `CulturalPhase`, `InteractionSphere` node IDs).  
- Optionally:
  - Seed text or narrative labels for Focus Mode v3 to bootstrap explanations.  

This template enables tight coupling between data lineage and narrative surfaces.

---

## 🧬 Provenance Model & Standards

All templates share a common conceptual model:

- **Entity (PROV-O / CIDOC-CRM E73/E31)**  
  - Datasets, layers, derived surfaces, and key input documents.  

- **Activity (PROV-O / CIDOC-CRM E7/E65)**  
  - Georeferencing, digitization, classification, generalization, modeling, review.  

- **Agent (PROV-O / CIDOC-CRM E39)**  
  - People, teams, institutions, software/pipeline agents.  

- **Relations**  
  - `prov:used`, `prov:wasGeneratedBy`, `prov:wasDerivedFrom`, `prov:wasAttributedTo`.

Templates are compatible with:

- **STAC 1.0** — via `kfm:provenance` references in Items/Collections.  
- **DCAT 3.0** — via `dct:provenance` / related fields in metadata.  
- **CIDOC-CRM** — optional fields in YAML/JSON for advanced mapping.  
- **OWL-Time** — ISO datetimes with optional precision fields.  
- **GeoSPARQL** — geometry stored in GeoJSON, convertible to WKT for the graph.  
- **FAIR+CARE** — explicit fields for rights, sensitivity, and Indigenous data considerations.

---

## 🧪 Usage Workflow (Interaction Spheres)

1. **Copy templates** into your dataset-specific provenance folder  
   (for example, `cultural-landscapes/interaction-spheres/great-bend-aspect/provenance/`).

2. **Fill out `sources-registry.template.csv`**  
   - Register all input datasets, maps, reports, and services.

3. **Fill out `transformations-log.template.csv`**  
   - Log each ETL/modeling step and link to MCP experiment docs.

4. **Author `dataset-provenance.template.yml`**  
   - Summarize scope, temporal/spatial extent, key decisions, and lineage.

5. **Complete `qa-checklist.template.md`**  
   - Perform QA and CARE review; update QA status in the transformations log.

6. **Populate `story-links.template.json`** (recommended)  
   - Bind data outputs to Story Nodes and Focus Mode entities.

7. **Run validation**  
   - Use repository’s provenance/metadata validation tools (see CI section below).

8. **Rename and commit**  
   - Remove `.template` suffixes, set real IDs/paths, commit alongside STAC/metadata updates.

---

## ✅ Validation & CI

Provenance artifacts created from these templates are validated via:

- Schema checks (where JSON/YAML/CSV schemas are provided).  
- Internal consistency checks:
  - IDs between sources, transformations, and dataset-level provenance.  
- CARE and sovereignty checks (for example, ensuring governance flags exist where required).  

Validation is run by CI workflows, including (names may vary):

- `artifact-stac-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`  
- Any provenance-specific validation scripts defined under `docs/analyses/archaeology/validation/`.

Provenance omissions or invalid fields should block merges that modify interaction-sphere datasets.

---

## 🔗 Related Specifications

- `../README.md`  
  – Interaction Sphere provenance index and governance rules.  
- `../../stac/README.md`  
  – Interaction-sphere STAC catalog and `kfm:provenance` link usage.  
- `../../metadata/README.md`  
  – DCAT + CARE metadata standards.  
- `../../../../artifact-inventories/provenance/templates/README.md`  
  – Artifact-inventory provenance templates that inspired these patterns.

---

## 🕰 Version History

| Version   | Date       | Author                                             | Summary                                                                 |
|-----------|------------|----------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisory Review | Updated for KFM v11.2.3; aligned with interaction-sphere provenance index; added telemetry refs and clarified Focus Mode v3 usage. |
| v11.0.0   | 2025-11-17 | Lead Programmer (AI)                               | Initial creation of interaction-sphere provenance template README and template set. |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Sphere Provenance](../README.md)
