---
title: "🧪 Archaeology Provenance QA Checklist Template"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/templates/qa-checklist.template.md"
version: "v11.0.0"
last_updated: "2025-11-17"
review_cycle: "Annual / Archaeology Domain Leads"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-interaction-spheres-provenance-qa-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

# 🧪 Archaeology Provenance QA Checklist Template

> **Purpose:**  
> This checklist ensures that all archaeology interaction-sphere datasets meet **quality control**, **FAIR+CARE**, **ethical**, and **spatial/temporal validity** requirements before merge and publication.

---

## ✅ Dataset Identification

- [ ] Dataset ID matches STAC + DCAT naming conventions  
- [ ] Title and description complete  
- [ ] Spatial extent (bbox) valid  
- [ ] Temporal extent valid with explicit precision (year/decade/century)  
- [ ] Dataset version updated and consistent across files  
- [ ] All provenance references (sources, transformations, story links) present

---

## 📐 Geometry & Spatial QA

- [ ] All geometries valid (no self-intersections, empty geometries, etc.)  
- [ ] CRS set to EPSG:4326 unless documented otherwise  
- [ ] Topology rules adhered to (no overlaps, slivers, or invalid network connections)  
- [ ] Sensitive locations generalized to H3-level region (if required)  
- [ ] Multi-polygons simplified with tolerance documented in transformations log  
- [ ] Raster layers have correct nodata values  

---

## 🏛️ Attribute & Schema QA

- [ ] All required attributes present  
- [ ] Controlled vocabulary terms used where defined  
- [ ] No personally identifiable information (PII)  
- [ ] Cultural, tribal, or sensitive fields masked/removed appropriately  
- [ ] Attribute domains validated (numeric ranges, classification systems)  
- [ ] Null handling and missing data policy clearly stated

---

## 🧬 Provenance Completeness

- [ ] `dataset-provenance.yml` properly filled  
- [ ] `sources-registry.csv` populated with all required metadata  
- [ ] `transformations-log.csv` updated for every ETL & modeling step  
- [ ] MCP experiment IDs referenced where applicable  
- [ ] All agents (people/software) identified  
- [ ] PROV-O relations implied or explicitly defined  
- [ ] Story Node / Focus Mode IDs linked where relevant  

---

## ⚖️ FAIR+CARE Compliance

### FAIR
- [ ] Findability: IDs stable, dataset discoverable  
- [ ] Accessibility: license + rights specified  
- [ ] Interoperability: schema aligned with STAC / DCAT / GeoJSON  
- [ ] Reusability: clear lineage and methods provided  

### CARE
- [ ] **C**ollective benefit: dataset use aligns with community benefit  
- [ ] **A**uthority to control: permissions verified  
- [ ] **R**esponsibility: culturally sensitive materials reviewed  
- [ ] **E**thics: redaction/generalization decisions documented  

---

## 🔐 Sensitivity & Ethics Review

- [ ] Spatial generalization applied when required  
- [ ] Sacred, burial, or restricted sites handled per tribal guidelines  
- [ ] Consultations recorded (tribal, community, institutional)  
- [ ] Data distribution level documented (public/restricted/internal)  
- [ ] No reproduction of restricted map sheets or archives without permission  

---

## 🧑‍🔧 Technical Validation

- [ ] All files pass schema validation (`make validate-provenance`)  
- [ ] CSV headers validated  
- [ ] JSON parses and matches schema  
- [ ] YAML is linted and conflict-free  
- [ ] No broken relative paths  
- [ ] STAC item(s) valid via `stac-validator`  
- [ ] Geometry validated via QA tools (QGIS, Python validator, or CI script)

---

## 🧰 Documentation Completeness

- [ ] Readme for dataset updated  
- [ ] Changelog updated  
- [ ] Version bump applied correctly  
- [ ] All metadata files (STAC, DCAT, provenance) in sync  
- [ ] Inline notes in transformations log clear and complete  
- [ ] Any Story Node narrative references verified  

---

## 📝 Final Reviewer Notes

**Reviewer:**  
**Date:**  
**Decision:** ☐ Approve  ☐ Minor Fixes Needed  ☐ Reject  
**Comments:**  

