---
title: "🗺️ Kansas Frontier Matrix — Processed Spatial Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/spatial/metadata/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-spatial-metadata-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-spatial-metadata-readme"
event_source_id: "ledger:data/processed/spatial/metadata/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-spatial-processed-metadata-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Metadata Registry"
intent: "processed-spatial-metadata"
role: "spatial-domain"
category: "Data · Spatial · Metadata · Processed"

fair_category: "F1-A1-I1-R1"
care_label: "Low–Medium — some spatial datasets intersect sensitive areas"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
redaction_required: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low–Medium"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/data-spatial-processed-metadata-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/data-spatial-processed-metadata-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified geographic claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public Dataset"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next spatial-domain metadata update"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Processed Spatial Metadata**  
`data/processed/spatial/metadata/README.md`

Metadata governing:

- 🧭 Administrative and cadastral boundaries  
- 🗺️ Reference base maps (state, county, township, parcels)  
- 🌐 Road networks, hydrography, transportation features  
- 🛰️ Raster spatial layers (DEMs, hillshades, base imagery)  
- 📦 Vector tiles, COG rasters, and spatial index structures  
- 🧠 Focus Mode v3 spatial anchors & geometry context  
- 🌐 STAC/DCAT metadata for all spatial assets  

All metadata here is **FAIR+CARE-certified, governance-approved, provenance-linked, and schema-validated**.

</div>

---

## 1. 📘 Purpose

This directory contains **metadata for all processed spatial datasets**, ensuring:

- Reproducibility of boundary datasets, basemaps, vector layers, and COG rasters  
- Consistency between geometry sources: DASC, USGS, TIGER/Line, and KFM-derived composites  
- Ethical governance and sovereignty-aware handling of spatial features  
- Integration with Neo4j spatial layers & Focus Mode v3 geographic narratives  
- Compliance with STAC/DCAT, ISO 19115, and KFM-PDC v11  

Spatial metadata supports:

- Hazard overlays  
- Climate/hydrology alignment  
- Story Node v3 geospatial grounding  
- Temporal and spatial scope validation  

---

## 2. 🗂️ Directory Layout (Mobile-Safe)

```text
data/processed/spatial/metadata/
├── README.md                               ← this file
├── checksums.json                           ← SHA-256 checksums for spatial datasets
├── provenance.json                          ← PROV-O lineage tree
├── schema_validation.json                   ← Schema validation results
├── faircare_certification.json              ← FAIR+CARE certification record
└── metadata_manifest.json                   ← STAC/DCAT metadata catalog
```

---

## 3. 📑 Metadata Coverage

### **Dataset Identity**
Covers metadata for:

- Administrative boundaries (county, township, section)  
- Parcel boundaries when applicable (generalized)  
- Hydrologic boundaries (HUCs)  
- Transportation networks  
- Elevation models (DEM, hillshade, slope/aspect)  
- Spatial indexing artifacts (H3, quadkeys, tilesets)  

### **Schema Structure**
Metadata validation ensures:

- Correct geometry types (Polygon, MultiPolygon, LineString)  
- CRS normalization to **EPSG:4326**  
- Complete attribute coverage (GNIS IDs, county FIPS, etc.)  
- No invalid rings or self-intersection  
- Raster alignment to KFM spatial grid standards  

### **Ethical Flags**
Spatial datasets must respect:

- Indigenous sovereignty boundaries  
- Culturally sensitive areas (generalized to H3 or redacted)  
- CARE-compliant geospatial access rules  

### **Quality & Lineage Validation**
Checks include:

- Source agency traceability (USGS, DASC, Census TIGER/Line)  
- Geometry validation (topology, ring order, closure)  
- Spatial consistency across layers (boundary alignment, snapping)  

### **File Tracking**
Each dataset in the spatial domain has:

- Official SHA-256 checksum  
- Source pipeline reference  
- Associated lineage entities  
- Governance ledger path  

---

## 4. 🔗 PROV-O Lineage Overview

The lineage file (`provenance.json`) expresses:

### **Entities**
- Raw boundaries (county, township, section)  
- Raw raster layers (DEM/LiDAR-derived hillshade)  
- Road & hydrography layers (TIGER/Line, DASC)  
- Processed boundaries (generalized, clipped, dissolved)  
- Derived rapid-access spatial indices  

### **Activities**
- CRS normalization  
- Topology repair  
- Attribute cleansing & harmonization  
- Raster reprojection/resampling  
- Vector tiling & spatial indexing  

### **Agents**
- KFM Spatial Domain Stewards  
- KFM Data Council  
- Source agencies: USGS, Census Bureau, DASC  

---

## 5. ⚖️ FAIR+CARE Governance — Spatial Domain

### **FAIR**
- Transparent, open spatial layers  
- Clear provenance for every boundary, raster, and geometry  
- Reusable for hazards, hydrology, landcover, climate, etc.  
- Discoverable via STAC/DCAT catalogs  

### **CARE**
Spatial data may encode sensitive cultural landscapes.  
Thus metadata enforces:

- Indigenous boundary masking rules  
- Cultural-site generalization requirements  
- CARE-based risk evaluation  

Certification details recorded in:

```
faircare_certification.json
```

---

## 6. 🧪 Schema Validation Summary

`schema_validation.json` includes:

- Geometry validity (no null shapes, no broken polygons)  
- Attribute field validation (names, types, completeness)  
- Spatial consistency (boundary alignment, snapping)  
- Raster metadata checks (resolution, extent, compression)  
- KFM PDC v11 compliance  

---

## 7. 🧮 Checksums & Metadata Manifest

`checksums.json` includes SHA-256 digests for:

- All boundary datasets  
- All raster basemaps (DEM, hillshade, derived surfaces)  
- Transportation/hydrography layers  
- Spatial indexing assets  

`metadata_manifest.json` contains:

- STAC-aligned metadata index  
- DCAT Dataset + Distribution entries  
- Cross-references to:
  - Provenance (PROV-O)  
  - Schema validation  
  - FAIR+CARE certification  

---

## 8. 🖥️ Focus Mode Integration

Focus Mode v3 uses this metadata to:

- Anchor stories to reliable geospatial extents  
- Validate geographic scopes in region-based narratives  
- Provide proper spatial context for hazards/climate/hydrology  
- Respect sovereignty & culturally sensitive boundaries  

Spatial metadata ensures:

- No unintended leaks of sensitive coordinates  
- Accurate geometry-driven narrative reasoning  
- Valid bounding boxes & extents for backdrop rendering  

---

## 9. 🕰️ Version History

| Version | Date       | Summary                                                   |
|--------:|------------|-----------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial processed spatial metadata registry (preferred format) |
| v10.0.0 | 2025-11-10 | Preliminary spatial metadata added                         |

<div align="center">

**Kansas Frontier Matrix — Spatial Metadata Domain**  
🗺️ FAIR+CARE Certified · Integrity-Verified · Diamond⁹ Ω / Crown∞Ω  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Spatial](../README.md) · [Data Architecture](../../ARCHITECTURE.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>