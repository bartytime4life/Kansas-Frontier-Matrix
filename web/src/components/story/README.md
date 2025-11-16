---
title: "📖 Kansas Frontier Matrix — Story Node UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/story/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-story-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-story"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Variable (Story-dependent)"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/story/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document / E53 Place / E52 Time-Span"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../schemas/json/web-components-story-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-story-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-story-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-story-readme"
event_source_id: "ledger:web/src/components/story/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with constraints"
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
classification: "Public UI Components (with CARE exceptions)"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review every major release"
sunset_policy: "Superseded upon Story Node v4 upgrade"
---

<div align="center">

# 📖 **Kansas Frontier Matrix — Story Node UI Components Overview**  
`web/src/components/story/README.md`

**Purpose:**  
Describe the complete suite of **Story Node v3 UI components**, which render narrative units  
combining text, time, place, provenance, media, geospatial footprints, and governance metadata.  
Story Node components must be **ethically governed**, **WCAG-compliant**, and fully integrated  
with Focus Mode v2.5, Timeline, STAC data, and mapping pipelines.

</div>

---

# 📘 Overview

Story Node components:

- Render structured narratives  
- Display spatial footprints (generalized if restricted)  
- Integrate with Focus Mode and Timeline  
- Surface provenance metadata (source → rights-holder → transformation)  
- Show CARE labels and sovereignty warnings  
- Provide accessible, ethical UI for historical/cultural content  
- Annotate any AI-generated text  
- Sync with map highlight layers  
- Emit telemetry for narrative engagement  

These components must never:

- Invent historical claims  
- Show exact restricted coordinates  
- Collapse governance metadata  
- Display unmasked archaeological/sacred sites  

---

# 🧱 Directory Structure

~~~text
web/src/components/story/
├── StoryCard.tsx                   # Compact Story Node summary card
├── StoryDetail.tsx                 # Full narrative view with media + provenance
├── StoryMedia.tsx                  # Media carousel (images, scans, maps)
├── StoryMapPreview.tsx             # Mini-map with footprint (generalized as needed)
├── StoryRelations.tsx              # Related entities (places, events, docs)
├── StoryTimeline.tsx               # Optional temporal visualization block
├── StoryProvenance.tsx             # PROV-O aligned provenance information
└── StoryCareBlock.tsx              # CARE + sovereignty + ethics warning section
~~~

---

# 🧩 Component Responsibilities

## 📘 **StoryCard.tsx**
Displays:

- Title + short summary  
- CAREBadge  
- Time span  
- Location label (generalized when required)  
- ProvenanceChip  
- Click handler to open full Story Node  

Accessibility:

- Proper heading levels  
- Keyboard navigation  
- High-contrast tokens  

Telemetry:

- `"story:card-open"`  

---

## 📖 **StoryDetail.tsx**
Full, scrollable Story Node detail renderer.

Contains:

- Narrative sections (archival text + AI summaries clearly labeled)  
- Provenance trail  
- CARE + ethical notices  
- StoryMapPreview  
- StoryRelations  
- Media carousel  
- Temporal markers  

Governance Responsibilities:

- MUST label AI-generated narrative  
- MUST show provenance for all claims  
- MUST remove/blur sensitive content  

---

## 🖼️ **StoryMedia.tsx**
A media viewer for Story Node assets:

- Scans  
- Photos  
- Historical maps  
- Documents  

Rules:

- Metadata + rights-holder must be visible  
- Sensitive or sacred content must be masked or contextualized  
- Image zoom must respect reduced-motion  

---

## 🗺️ **StoryMapPreview.tsx**
Shows geospatial footprint:

- Uses generalized footprint for sensitive sites  
- Supports time-based fading  
- Syncs with Timeline + MapContext  
- Displays H3 masking when needed  

Governance:

- Must identify when location is masked  
- Prevent leakage of precise coordinates  

---

## 🔗 **StoryRelations.tsx**
Lists related entities:

- Places  
- Events  
- People  
- Datasets  
- Other Story Nodes  

Rules:

- Story Node → Entity link MUST match the knowledge graph (no inferences)  
- Sensitive entities must be flagged or masked  
- Relations must be keyboard-navigable and properly labeled  

---

## 🕰️ **StoryTimeline.tsx**
Optional mini-timeline for the node’s temporal span.

- OWL-Time aligned  
- Shows fuzzy dates clearly  
- High-contrast, reduced-motion compliant  

---

## 🧬 **StoryProvenance.tsx**
Renders the full provenance chain:

- Sources  
- Transformations  
- Rights-holder  
- Tools used  
- SBOM/manifests  
- CARE classification  

Must:

- Use PROV-O mapping  
- Provide downloadable JSON-LD block  

---

## ⚠️ **StoryCareBlock.tsx**
Contains mandatory ethical context:

- CARE label  
- Sovereignty warnings  
- Cultural sensitivity notes  
- Explanation of why masking is applied  
- Links to governance documents  

Displayed **before** any sensitive content.

---

# 🔐 Governance Expectations

All Story Node components must:

- Enforce CARE + sovereignty  
- Display provenance chips in all views  
- Block unsafe data displays  
- Correctly generalize/blur sensitive spatial data  
- Label AI content  
- Avoid speculative claims  
- Maintain ethical narrative framing  

Governance regressions → **CI hard fail**.

---

# ♿ Accessibility Requirements

Each Story Node component must:

- Use semantic HTML  
- Provide alt text for images  
- Support keyboard navigation  
- Maintain heading order  
- Respect reduced-motion settings  
- Provide screen-reader labels for temporal + spatial info  
- Ensure visible focus indicators  

WCAG 2.1 AA compliance is mandatory.

---

# 📈 Telemetry Responsibilities

Story Node components must emit:

- `"story:open"`  
- `"story:media-view"`  
- `"story:relation-click"`  
- `"story:timeline-hover"`  
- `"story:map-preview"`  
- `"story:care-warning-shown"`  
- `"story:provenance-expanded"`  

Telemetry must be:

- Non-PII  
- Schema-valid  
- CARE-aware  
- Included in the release bundle  
  (`releases/<version>/focus-telemetry.json`)

---

# 🧪 Testing Requirements

Each component must include:

- Unit tests (render, props, governance logic)  
- Integration tests (timeline/map sync)  
- A11y tests (ARIA, keyboard, contrast)  
- Governance tests (masking, provenance)  
- Telemetry tests  
- Story Node schema tests  

Test locations:

~~~text
tests/unit/web/components/story/**
tests/integration/web/components/story/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full Story Node v3 UI rewrite under KFM-MDP v10.4; added CARE, provenance, AI labeling rules |
| v10.3.2 | 2025-11-14 | Improved spatial previews + relations layout |
| v10.3.1 | 2025-11-13 | Initial Story Node component overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>

