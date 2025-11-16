---
title: "🗂️ Kansas Frontier Matrix — STAC/DCAT UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/stac/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-stac-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-stac"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Dataset-dependent"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/stac/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../schemas/json/web-components-stac-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-stac-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-stac-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-stac-readme"
event_source_id: "ledger:web/src/components/stac/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict constraints"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public / Dataset-sensitive"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next STAC/DCAT UI overhaul"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — STAC/DCAT UI Components Overview**  
`web/src/components/stac/README.md`

**Purpose:**  
Define the UI components responsible for **STAC (SpatioTemporal Asset Catalog)** and **DCAT (Dataset Catalog v3)** browsing,  
previewing, metadata display, governance surfacing, and telemetry generation in the KFM Web Platform.  
These components must be **FAIR+CARE-governed**, fully **WCAG AA–accessible**, and  
**geospatial-governance–aware**, especially where datasets carry sovereignty, license, or redaction constraints.

</div>

---

# 📘 Overview

STAC/DCAT components:

- Display dataset-level metadata  
- Preview spatial footprints (generalized when required)  
- Integrate temporal metadata with TimeContext  
- Support dataset browsing, filtering, and quick interactions  
- Render provenance + CARE metadata inline  
- Avoid showing restricted coordinates or sensitive detail  
- Sync with Focus Mode & Story Node v3 where applicable  
- Emit telemetry for dataset exploration and sustainability metrics  
- Are fully accessible and ethics-aligned  

These components interact with:

- `stacService.ts`  
- `dcatService.ts`  
- `stacPipeline.ts`  
- Governance + CARE context  
- Focus Mode v2.5 (dataset-based focus events)  
- MapContext for footprint previews  

---

# 🧱 Directory Structure

~~~text
web/src/components/stac/
├── DatasetCard.tsx               # High-level dataset summary card (STAC/DCAT)
├── DatasetList.tsx               # Paginated dataset collection viewer
├── ItemPreview.tsx               # Preview for STAC Item (footprint + metadata)
├── AssetMetadata.tsx             # Detailed metadata: license, provenance, rights
├── ExtentPreview.tsx             # Spatial + temporal extent visualization
├── STACSearchBar.tsx             # Search/filter control (time, bbox, keywords)
└── STACSortToolbar.tsx           # Sorting + filtering toolbar
~~~

---

# 🧩 Component Responsibilities

---

## 📦 **DatasetCard.tsx**

Displays high-level dataset metadata:

- Title, description  
- STAC/DCAT classification  
- Publisher/creator  
- CAREBadge  
- Temporal coverage  
- LicenseTag  
- ProvenanceChip  

Must:

- Support keyboard navigation  
- Use accessible headings  
- Emit telemetry: `"stac:dataset-open"`  

---

## 📚 **DatasetList.tsx**

Renders collections of datasets with:

- Pagination  
- Sorting controls  
- Filters (time, bbox, keyword)  
- CARE/sovereignty classification indicators  

Governance:

- Restricted datasets must display vulnerability warnings  
- Indigenous-governed datasets must show sovereignty banners  

Telemetry:

- `"stac:list-scroll"`  
- `"stac:filter-change"`  

---

## 🗺️ **ItemPreview.tsx**

Provides a mini-view of a STAC Item:

- Footprint preview (masked when sensitive)  
- COG asset summary  
- Bounding box  
- Temporal interval  
- CARE + provenance metadata  

Rules:

- MUST generalize footprints if dataset marks sensitive geometry  
- Must sync with MapContext when hovered or selected  
- Must not expose exact coordinates for restricted data  

---

## 🏷️ **AssetMetadata.tsx**

Displays:

- Asset-level metadata (image, COG, GeoTIFF, vector layer)  
- Rights-holder  
- LicenseTag  
- Provenance trail  
- Data quality indicators  

Care constraints:

- Must label redacted or restricted fields  
- Must prevent raw URLs from loading sensitive materials  

---

## 🗓️ **ExtentPreview.tsx**

Shows spatiotemporal extent:

- Time range (OWL-Time aligned)  
- Map footprint preview  
- Bounding box visualization  
- Temporal uncertainty blocks  

Accessibility:

- Must provide text equivalent for spatial previews  
- Must avoid color-only cues  

Governance:

- Must show when extent is generalized or masked  

---

## 🔍 **STACSearchBar.tsx**

Controls:

- Keyword search  
- Temporal filters  
- Spatial filters (bbox selection)  
- Dataset type filters  

Accessibility:

- Fully screen-reader operable  
- All controls keyboard accessible  
- High-contrast compliance  

Telemetry:

- `"stac:search"`  
- `"stac:filter-change"`  

---

## 🔧 **STACSortToolbar.tsx**

Provides:

- Sort-by (newest, oldest, alphabetical, temporal length)  
- CARE-label filtering  
- Rights-holder filtering  
- Dataset-type filtering  

Governance:

- Must clearly mark restrictions on dataset visibility  

Telemetry:

- `"stac:sort-change"`

---

# 🔐 Governance & FAIR+CARE Enforcement

STAC/DCAT components MUST:

- Display CARE classifications prominently  
- Warn when datasets have sovereignty restrictions  
- Hide blocked assets  
- Mask sensitive geometry with H3 r7+  
- Show provenance chips for all metadata  
- Provide context around AI-derived dataset summaries  
- Never misrepresent or speculate about dataset geography/history  

Governance violations → **CI-blocking error**.

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

All STAC components must:

- Use semantic HTML  
- Provide proper ARIA labeling  
- Respect reduced-motion  
- Use accessible color ramps  
- Provide textual equivalents for map previews  
- Ensure keyboard navigation works fully  

---

# 📈 Telemetry Responsibilities

Components must emit non-PII telemetry for:

- Dataset browsing  
- Item previews  
- Filtering/sorting changes  
- Spatial/temporal extent interactions  
- CARE warning displays  
- Provenance expansion events  

Stored in:

`releases/<version>/focus-telemetry.json`

---

# 🧪 Testing Requirements

Tests must cover:

- UI rendering  
- Accessibility flows  
- Governance rule enforcement  
- Telemetry accuracy  
- STAC schema validation  
- Masking + sovereignty behavior  
- Integration with MapContext + Timeline  

Test locations:

~~~text
tests/unit/web/components/stac/**
tests/integration/web/components/stac/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 rewrite; added governance, masking, A11y, temporal + spatial extent integration |
| v10.3.2 | 2025-11-14 | Improved dataset list + item preview behaviors |
| v10.3.1 | 2025-11-13 | Initial STAC/DCAT component overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>

