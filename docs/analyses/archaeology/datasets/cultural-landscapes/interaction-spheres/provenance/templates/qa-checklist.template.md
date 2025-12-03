---
title: "🧪 Kansas Frontier Matrix — Archaeology Provenance QA Checklist Template (Interaction Spheres) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/templates/qa-checklist.template.md"
description: "Standard QA checklist template for interaction-sphere provenance in KFM v11, covering quality control, FAIR+CARE, sovereignty, and spatial/temporal validity."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Archaeology Domain Leads · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-interaction-spheres-provenance-qa-template-v11.2.3"
doc_kind: "QA Checklist Template"
intent: "interaction-sphere-provenance-qa-template"
semantic_document_id: "kfm-doc-archaeology-interaction-spheres-provenance-qa-template-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Provenance · QA"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-interaction-spheres-provenance-qa-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-gco2e-v1.json"

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

data_steward: "Archaeology Domain Leads · Cultural Landscape Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/templates/qa-checklist.template.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🧪 Archaeology Provenance QA Checklist Template (Interaction Spheres)

> **Purpose**  
> This checklist ensures that all **interaction-sphere** datasets in KFM v11 meet **quality control**, **FAIR+CARE**, **sovereignty**, and **spatial/temporal validity** requirements **before merge and publication**.

This file is a **template**: copy, rename, and fill it per dataset (for example, into the dataset-specific `provenance/` directory).

---

## ✅ Dataset Identification

- [ ] Dataset ID matches STAC + DCAT naming conventions (ID = filename stem, versioned)  
- [ ] Title and description complete, neutral, and non-colonial  
- [ ] Spatial extent (bbox) valid and generalized  
- [ ] Temporal extent valid with explicit precision (year/decade/century)  
- [ ] Dataset version updated and consistent across:
  - STAC Item  
  - DCAT/metadata  
  - Provenance log  
- [ ] All provenance references present:
  - `dataset-provenance.yml`  
  - `sources-registry.csv`  
  - `transformations-log.csv`  
  - `story-links.json` (if used)  

---

## 📐 Geometry & Spatial QA

- [ ] All geometries valid (no self-intersections, empty geometries, invalid rings)  
- [ ] CRS set to **EPSG:4326** unless another CRS is explicitly documented  
- [ ] Topology rules checked (no unintended overlaps/slivers; expected adjacencies documented)  
- [ ] Sensitive locations generalized to H3-level region (or equivalent) where required  
- [ ] Interaction-sphere polygons are generalized (not site-level outlines)  
- [ ] MultiPolygons simplified with tolerance documented in `transformations-log.csv`  
- [ ] Any raster/tiling layers have correct `nodata` values and metadata  

---

## 🏛️ Attribute & Schema QA

- [ ] All required attributes present for this dataset’s schema (see relevant README + schemas)  
- [ ] Controlled vocabulary terms used where defined (`region_type`, `interaction_type`, etc.)  
- [ ] No personally identifiable information (PII) present  
- [ ] Cultural, tribal, or sensitive descriptive fields masked/removed or generalized appropriately  
- [ ] Attribute domains validated (numeric ranges, classification systems, enumerations)  
- [ ] Null/missing data handling documented (e.g., sentinel codes, empty strings)  

---

## 🧬 Provenance Completeness

- [ ] `dataset-provenance.yml` filled with:
  - dataset ID, title, description  
  - spatial and temporal extents  
  - license, rights, and CARE notes  
  - high-level lineage summary  
- [ ] `sources-registry.csv` populated with all input sources  
- [ ] `transformations-log.csv` updated for every ETL and modeling step  
- [ ] MCP experiment IDs referenced where applicable (for experiments/pipelines)  
- [ ] All agents (people, organizations, software/pipelines) identified  
- [ ] PROV-O relations (`used`, `wasGeneratedBy`, `wasDerivedFrom`, `wasAttributedTo`) implied or explicitly defined  
- [ ] Story Node / Focus Mode IDs linked in `story-links.json` where relevant  

---

## ⚖️ FAIR+CARE Compliance

### FAIR

- [ ] **Findable** — IDs stable; metadata present in STAC + DCAT; discoverable via catalog  
- [ ] **Accessible** — License and access constraints specified; access URIs working  
- [ ] **Interoperable** — Schema aligned with STAC / DCAT / GeoJSON; CRS declared; formats open  
- [ ] **Reusable** — Clear lineage, methods, and appropriate rights/consent information provided  

### CARE

- [ ] **Collective Benefit** — Dataset use aligns with benefit to communities, not only external researchers  
- [ ] **Authority to Control** — Permission and governance routes verified (especially for protohistoric/ethnohistoric data)  
- [ ] **Responsibility** — Culturally sensitive materials reviewed by appropriate bodies (FAIR+CARE, tribal)  
- [ ] **Ethics** — Redaction and generalization decisions documented; harms and risks considered and mitigated  

---

## 🔐 Sensitivity & Ethics Review

- [ ] Spatial generalization applied where required by sovereignty policy or CARE review  
- [ ] Sacred, burial, or restricted ceremonial areas have been treated according to tribal guidelines:
  - generalized, removed, or kept out of public-facing layers  
- [ ] All consultations recorded (tribal, community, institutional) with dates and outcomes  
- [ ] Data distribution level documented (public / restricted / internal) and matches repository placement  
- [ ] No reproduction of restricted map sheets, archives, or oral histories without explicit permission  
- [ ] Language used in descriptions and notes avoids colonial framing and essentialism  

---

## 🧑‍🔧 Technical Validation

- [ ] All provenance artifacts pass schema validation (where schemas exist)  
- [ ] CSV headers and required columns validated (`sources-registry`, `transformations-log`)  
- [ ] JSON (`story-links`, any PROV-O JSON) parses and matches schema  
- [ ] YAML (`dataset-provenance.yml`) is linted and conflict-free  
- [ ] No broken or stale relative paths (STAC ↔ metadata ↔ provenance ↔ inventories/tiles)  
- [ ] Linked STAC Item(s) validate via `stac` validation tooling  
- [ ] Geometry validated via QA tools (QGIS, Python QA scripts, or CI validator)  

---

## 🧰 Documentation Completeness

- [ ] Dataset-level README updated (within the dataset’s directory)  
- [ ] Changelog / version history updated if applicable  
- [ ] Version bump applied consistently across:
  - STAC, DCAT/metadata, provenance, and main datasets  
- [ ] All metadata files are in sync (`stac/`, `metadata/`, `provenance/`)  
- [ ] Inline notes in `transformations-log.csv` clear and sufficient for re-implementation  
- [ ] Any Story Node narrative references (IDs, labels) verified and still valid  

---

## 📝 Final Reviewer Notes

**Reviewer:**  
**Date:**  

**Decision:**  
- ☐ Approve  
- ☐ Minor Fixes Needed  
- ☐ Reject  

**Comments:**  
