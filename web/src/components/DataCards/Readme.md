---
title: "🗃️ Kansas Frontier Matrix — DataCards Component Suite Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/DataCards/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-datacards-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-datacards"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Dataset-dependent"
sensitivity_level: "Variable"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/DataCards/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../schemas/json/web-components-datacards-readme.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-datacards-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-datacards-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-datacards-readme"
event_source_id: "ledger:web/src/components/DataCards/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict guardrails"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "unverified historical claims"
  - "speculative dataset descriptions"
  - "hallucinated metadata"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public / Dataset-Sensitive"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next data-card system upgrade"
---

<div align="center">

# 🗃️ **Kansas Frontier Matrix — DataCards Component Suite Overview**  
`web/src/components/DataCards/README.md`

**Purpose:**  
Document the entire **DataCards UI component suite**, used across the Kansas Frontier Matrix Web Platform  
for presenting FAIR+CARE-governed dataset summaries, metadata, governance labels, spatial previews,  
temporal indicators, and provenance in compact, reusable card layouts.

DataCards power dataset browsing (STAC/DCAT), Story Node asset previews, and Focus Mode supplemental datasets.

</div>

---

# 📘 Overview

DataCards provide:

- Standardized card UI for datasets, assets, or metadata bundles  
- WCAG AA–compliant visual design  
- CARE-aware metadata display  
- Provenance chip integration  
- Spatial/temporal mini-previews  
- Interaction telemetry  
- No speculative, inferred, or fabricated metadata  
- Deterministic and schema-validated rendering  

They appear in:

- STAC/DCAT dataset lists  
- Story Node asset panels  
- Focus Mode related-datasets sections  
- DetailDrawer subviews  
- Map-adjacent resource listings  

---

# 🧱 Directory Structure

~~~text
web/src/components/DataCards/
├── DataCard.tsx                    # Universal dataset/narrative card
├── DataCardHeader.tsx              # Title, dataset type, CARE badge, provenance chip
├── DataCardMetadata.tsx            # List of key fields (publisher, license, time, bbox)
├── DataCardPreview.tsx             # Spatial/temporal mini-map/interval preview
├── DataCardFooter.tsx              # Actions: open, explore, preview in map
├── DataCardA11yHelpers.tsx         # Accessible descriptions + ARIA scaffolding
└── DataCardSkeleton.tsx            # Loading skeleton component (reduced-motion safe)
~~~

---

# 🧩 Component Responsibilities

## 🗃️ **DataCard.tsx**
The container that assembles all card sections.

Responsibilities:

- Provide consistent layout (padding, spacing, tokens)  
- Load governance + CARE labels  
- Render metadata fields safely  
- Trigger telemetry on interactions  
- Allow keyboard focus + screen-reader structure  

Governance:

- Must block rendering if dataset is sovereignty-controlled and redaction required  
- Must display masking/generalization notices  

Telemetry:

- `"datacard:open"`  
- `"datacard:hover"`  
- `"datacard:action"`  

---

## 🏷️ **DataCardHeader.tsx**
Displays:

- Dataset or asset title  
- CAREBadge  
- ProvenanceChip  
- Dataset classification  

A11y:

- `<header>` landmark  
- Clear labeling  
- High-contrast token use  

---

## 🧾 **DataCardMetadata.tsx**
Shows:

- Publisher  
- Rights-holder  
- License  
- Temporal extent  
- Spatial extent (generalized when sensitive)  
- Data type  

Governance rules:

- Sensitive metadata fields must show a redaction tooltip  
- Must indicate when fields are generalized  

---

## 🗺️ **DataCardPreview.tsx**
Renders optional previews:

- Mini spatial footprint (H3 r7+ compliant)  
- Temporal bar/interval preview  
- Coverage thumbnails  

Governance:

- MUST generalize coordinates  
- MUST display sovereignty notices  

A11y:

- Provide textual equivalents for spatial visualizations  

---

## 🦶 **DataCardFooter.tsx**
Contains common actions:

- View dataset  
- Open DetailDrawer  
- Open in MapView  
- View provenance  

Governance:

- Disable actions for restricted datasets  
- Display tooltips explaining restrictions  

Telemetry:

- `"datacard:action"`  

---

## ♿ **DataCardA11yHelpers.tsx**
Provides:

- ARIA labels  
- Screen-reader context blocks  
- Keyboard navigation scaffolding  
- Reduced-motion paths  

Mandatory for WCAG AA compliance.

---

## 🧱 **DataCardSkeleton.tsx**
Loading skeleton:

- Reduced-motion–adapted shimmer  
- High-contrast placeholders  
- Does not reveal sensitive shapes or content  

---

# 🔐 Governance & FAIR+CARE Integration

DataCards MUST:

- Respect sovereignty + CARE classifications  
- Mask/map-generalize geographic previews  
- Prevent exposure of restricted metadata  
- Display provenance metadata for each dataset  
- Label any AI-generated summary segments  
- Never speculate about dataset origins, meaning, or history  

Governance failures → **CI BLOCK**.

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

DataCards must:

- Use semantic HTML regions  
- Provide proper ARIA labeling  
- Not rely solely on color  
- Support full keyboard navigation  
- Maintain ≥ 4.5:1 color contrast  
- Respect reduced-motion preferences  

A11y violations block merges.

---

# 📈 Telemetry Responsibilities

DataCards emit:

- `"datacard:open"`  
- `"datacard:hover"`  
- `"datacard:action"`  
- `"datacard:care-warning"`  
- `"datacard:provenance-expand"`  

Telemetry must be:

- Non-PII  
- Schema-valid  
- CARE-aware  
- Stored in release bundles  

---

# 🧪 Testing Requirements

Must include:

- Unit tests (rendering, props, metadata behavior)  
- Integration tests (story + focus + STAC lists)  
- Governance enforcement checks  
- A11y keyboard + ARIA tests  
- Telemetry emission tests  
- Snapshot tests (optional)  

Locations:

~~~text
tests/unit/web/components/DataCards/**
tests/integration/web/components/DataCards/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full DataCards suite documentation; added governance, A11y, preview rules |
| v10.3.2 | 2025-11-14 | Improved metadata + CARE disclosure patterns |
| v10.3.1 | 2025-11-13 | Initial DataCards component overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>
