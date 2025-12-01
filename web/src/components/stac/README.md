---
title: "🗂️ Kansas Frontier Matrix — STAC/DCAT UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/web-stac-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-stac-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public / Dataset-sensitive"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-stac"
semantic_intent:
  - "dataset-browsing"
  - "stac-ui"
  - "dcat-ui"
  - "governance-aware-metadata"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Dataset-dependent"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/stac/README.md@v10.4.0"
  - "web/src/components/stac/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../schemas/json/web-components-stac-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-stac-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-stac-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-stac-readme-v11"
event_source_id: "ledger:web/src/components/stac/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict constraints"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "coordinate-hallucination"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 Governance & FAIR+CARE Enforcement"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — STAC/DCAT UI Components Overview**  
`web/src/components/stac/README.md`

**Purpose:**  
Define the UI components responsible for **STAC (SpatioTemporal Asset Catalog)** and **DCAT (Dataset Catalog v3)** browsing,  
previewing, metadata display, governance surfacing, and telemetry generation in the KFM Web Platform.  
These components must be **FAIR+CARE-governed**, fully **WCAG AA+–accessible**, and  
**geospatial-governance–aware**, especially where datasets carry sovereignty, license, or redaction constraints.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Dataset%20Sensitive-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

**STAC/DCAT UI components** are the primary dataset exploration surfaces for KFM:

- Display dataset-level metadata (title, description, providers, rights)  
- Preview spatial footprints (generalized when required by CARE or sovereignty rules)  
- Integrate temporal metadata with `TimeContext` and `TimelineView`  
- Support dataset browsing, filtering, sorting, and quick-detail views  
- Render provenance (PROV-O) and CARE metadata inline  
- Avoid showing restricted coordinates, internal IDs, or sensitive attributes  
- Sync with:
  - Focus Mode (dataset-focused narratives)  
  - MapView (DatasetFootprintLayer)  
  - Story Node v3 (asset references)  
- Emit telemetry for dataset exploration and sustainability metrics  
- Are fully accessible (WCAG 2.1 AA+) and ethics-aligned  

They sit “between” the STAC/DCAT pipelines and the user, translating machine-readable catalogs into governed, human-usable UI.

---

## 🗂️ Directory Structure

~~~text
web/src/components/stac/
│
├── 📦 DatasetCard.tsx            # High-level dataset summary card (STAC/DCAT)
├── 📚 DatasetList.tsx            # Paginated dataset collection viewer
├── 🗺️ ItemPreview.tsx            # Preview for STAC Item (footprint + core metadata)
├── 🏷️ AssetMetadata.tsx          # Detailed asset metadata: license, provenance, rights
├── 🗓️ ExtentPreview.tsx          # Spatial + temporal extent visualization (maps + bars)
├── 🔍 STACSearchBar.tsx          # Search/filter control (time, bbox, keywords)
└── 🔧 STACSortToolbar.tsx        # Sorting + filtering toolbar for STAC/DCAT views
~~~

Any new component in this directory MUST be documented here.

---

## 🧩 Component Responsibilities

### 📦 DatasetCard.tsx

**Role:**  
Primary card for representing a dataset (STAC Collection, STAC Item, or DCAT Dataset).

**Displays (as available):**

- Dataset title and description  
- Dataset type (STAC collection, STAC item, DCAT dataset)  
- Publisher / creator / provider  
- CAREBadge (classification)  
- Temporal coverage summary  
- LicenseTag  
- ProvenanceChip  

**Requirements:**

- Fully keyboard-focusable and screen-reader readable  
- No dataset logic (filtering/sorting) inside; purely presentational  

**Telemetry (via parent wiring):**

- `"stac:dataset-open"` when user opens dataset details  

---

### 📚 DatasetList.tsx

**Role:**  
Render collections of datasets, with navigation and filter integration.

**Responsibilities:**

- List dataset cards (DatasetCard) in paginated / infinite-scroll style  
- Surface CARE/sovereignty classification for each dataset  
- Integrate with:
  - STAC search/filtering logic (from stacService/stacPipeline)  
  - Sorting and filter state  

**Governance:**

- Restricted datasets must:
  - Indicate the restriction  
  - Not expose blocked fields (e.g., direct file URLs if disallowed)  
- Sovereignty-controlled datasets must surface sovereignty labels and notices through Governance UI components.

**Telemetry:**

- `"stac:list-scroll"` (if implemented)  
- `"stac:filter-change"` (via attached toolbar/search bar)  

---

### 🗺️ ItemPreview.tsx

**Role:**  
Compact preview for a STAC Item.

**Displays:**

- Generalized spatial footprint (for map preview)  
- Bounding box (if allowed to be shown)  
- Temporal range (aligned with OWL-Time / TimeContext)  
- Asset summary (e.g., count/primary asset type)  
- CARE and provenance summary snippets  

**Governance:**

- MUST generalize or hide footprints for sensitive datasets (e.g., sovereignty-controlled sites)  
- MUST NOT expose raw coordinates or full-resolution extents of sensitive assets  
- Must support hooking into MapView to highlight dataset footprints without leaking precision  

---

### 🏷️ AssetMetadata.tsx

**Role:**  
Detailed metadata view for individual assets (images, COGs, GeoTIFFs, vector layers, etc.).

**Displays (depending on metadata):**

- Asset title / description  
- Media type (MIME)  
- LicenseTag & rights-holder  
- ProvenanceTrail link or summary  
- Data quality indicators (if available)  

**Governance:**

- MUST label redacted or restricted fields (e.g., “URL hidden due to sovereignty policy”)  
- MUST NOT render raw asset URLs for sensitive datasets unless explicitly allowed by governance context  
- Should provide cues when an asset has been derived or generalized from original resolution  

---

### 🗓️ ExtentPreview.tsx

**Role:**  
Visual and textual summary of spatial + temporal footprint.

**Responsibilities:**

- Render:
  - Temporal interval bars (overall coverage)  
  - Coarse spatial preview (e.g., bounding region)  
- Provide textual equivalents:
  - “Coverage: 1850–1900, Great Plains region”  

**Governance:**

- MUST indicate when footprints or intervals are generalized for CARE/sovereignty reasons  
- MUST NOT show highly precise extents for sensitive data  

**Accessibility:**

- No color-only meaning for time ranges (use patterns, labels, icons)  
- SR-only hints describing coverage  

---

### 🔍 STACSearchBar.tsx

**Role:**  
Search and filtering input component.

**Responsibilities:**

- Accept:
  - Keyword input  
  - Temporal filters (date-range pickers or presets)  
  - Spatial filters (bbox or region selection)  
  - Optional dataset-type filters (e.g., Datasets vs. Collections)  
- Integrate with:
  - FormControls primitives (`TextInput`, `Select`, etc.)  
  - STAC search logic in parent container  

**Accessibility:**

- All controls keyboard-operable  
- Labels and descriptions for filters  
- Clear instructions for time and spatial fields  

**Telemetry:**

- `"stac:search"`  
- `"stac:filter-change"`  

---

### 🔧 STACSortToolbar.tsx

**Role:**  
Sorting and filter toolbar for dataset lists.

**Responsibilities:**

- Provide sorting controls:
  - Newest / oldest first  
  - Alphabetical  
  - Temporal width  
- Provide toggles or selects for:
  - CARE classification filters  
  - Rights-holder filters  
  - Dataset type filters  

**Governance:**

- Must clearly indicate when certain datasets are hidden due to governance constraints (if parent provides that info)  

**Telemetry:**

- `"stac:sort-change"`  

---

## 🔐 Governance & FAIR+CARE Enforcement

STAC/DCAT UI components are **dataset-sensitive** and MUST:

- Display CARE classifications clearly for each dataset (via governance components)  
- Warning surfaces:
  - Sovereignty notices  
  - Cultural sensitivity / sacred site warnings  
- Mask or generalize:
  - Spatial footprints for restricted datasets (no raw coordinates)  
  - Temporal precision if necessary (e.g., year-only vs. full timestamp)  
- Show provenance:
  - ProvenanceChip / ProvenanceTrail links  
  - clear association of dataset to its source/provider  

These components MUST NOT:

- Fabricate or guess dataset geography or time spans  
- Display asset URLs or internal IDs when governance flags disallow it  
- Show “example” coordinates for sensitive data (no placeholder-lies)  

All governance failures (e.g., leaking exact coordinates for a sovereignty-controlled dataset) are **CI-blocking**.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

All STAC/DCAT components MUST:

- Use semantic HTML and ARIA roles for lists, cards, and controls  
- Provide keyboard navigation for:
  - dataset list scrolling  
  - search and filter controls  
  - sort toolbar interactions  
- Maintain 4.5:1 contrast for text and visual encodings  
- Provide textual equivalents where:
  - spatial previews are shown (e.g., “Dataset covers southwestern Kansas”)  
  - temporal extents are visualized  

Respect `prefers-reduced-motion` for any animations (hover, highlight, or transitions).

Accessibility regressions MUST block merges.

---

## 📈 Telemetry Responsibilities

STAC/DCAT components MUST support emission (via parent) of:

- `"stac:dataset-open"`  
- `"stac:search"`  
- `"stac:filter-change"`  
- `"stac:sort-change"`  
- `"stac:list-scroll"` (if used)  
- `"stac:item-preview-open"`  
- `"stac:care-warning-shown"`  
- `"stac:provenance-expand"`  

Telemetry:

- MUST be non-PII  
- MUST match schemas in `telemetry_schema`  
- SHOULD include dataset IDs (where appropriate and safe) for analytics, but not raw secret tokens or URLs  
- MUST be tied to this component’s version for debugging changes across releases  

---

## 🧪 Testing Requirements

Tests MUST cover:

- **Unit tests**:
  - Rendering of each component with typical and edge-case props  
  - Behavior with different CARE/sovereignty flags  

- **Integration tests**:
  - STAC/DCAT lists integrated with search & sort  
  - ItemPreview with MapView and TimelineView  
  - Governance overlays and warnings  

- **Accessibility tests**:
  - Keyboard navigation across DatasetList, STACSearchBar, SortToolbar  
  - ARIA attributes on DatasetCard, search fields, sort controls  

- **Governance tests**:
  - Masking for sensitive datasets (no raw coordinates)  
  - Restricted dataset fields hidden or labeled  

- **Telemetry tests**:
  - Events emitted as expected on user interactions  

Test layout:

~~~text
tests/unit/web/components/stac/**
tests/integration/web/components/stac/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                                     |
|--------:|------------|---------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; telemetry v2, FAIR+CARE clarifications, A11y refinements, masking rules |
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 rewrite; governance, masking, A11y, temporal + spatial extent integration |
| v10.3.2 | 2025-11-14 | Improved dataset list + item preview behaviors                                              |
| v10.3.1 | 2025-11-13 | Initial STAC/DCAT component overview                                                        |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../README.md) •  
[Standards Index](../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · STAC/DCAT · GeoSPARQL · CIDOC-CRM · OWL-Time · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>