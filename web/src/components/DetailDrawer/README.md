---
title: "📂 Kansas Frontier Matrix — DetailDrawer Component Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/DetailDrawer/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-detaildrawer-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-detaildrawer"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (content-dependent)"
sensitivity_level: "Variable"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/DetailDrawer/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../schemas/json/web-components-detaildrawer-readme.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-detaildrawer-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-detaildrawer-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-detaildrawer-readme"
event_source_id: "ledger:web/src/components/DetailDrawer/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict safeguards"
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
classification: "Public with CARE/sovereignty exceptions"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review every release cycle"
sunset_policy: "Superseded on next drawer system update"
---

<div align="center">

# 📂 **Kansas Frontier Matrix — DetailDrawer Component Overview**  
`web/src/components/DetailDrawer/README.md`

**Purpose:**  
Document the **DetailDrawer component suite**, a core UI pattern used throughout the KFM Web Platform for  
displaying deep, contextual, governance-aware content in a slide-out drawer.  
DetailDrawer acts as an **ethical detail view**, delivering narrative, metadata, provenance, CARE labels,  
and interaction tools without navigating away from the current page.

</div>

---

# 📘 Overview

DetailDrawer components enable:

- Slide-out, accessible detail panels  
- Contextual metadata and provenance display  
- CARE/Sovereignty warnings and redaction notices  
- Interaction with Story Node v3 content  
- Dataset previews for STAC/DCAT items  
- Focus Mode narrative subviews  
- Accessible and keyboard-friendly navigation  
- Controlled transitions with reduced-motion support  
- Telemetry for drawer usage and metadata interactions  

This suite is used in:

- Dataset detail views  
- Story Node deep-dives  
- Governance drawers  
- Focus Mode supplemental detail  
- Layer information panels  

---

# 🧱 Directory Structure

~~~text
web/src/components/DetailDrawer/
├── DetailDrawer.tsx                # Main UI drawer container
├── DrawerHeader.tsx                # Title, entity type, CARE label, close button
├── DrawerSection.tsx               # Reusable styled section block
├── DrawerMetadata.tsx              # Metadata list + provenance chips
├── DrawerProvenance.tsx            # Full PROV-O provenance panel
├── DrawerCAREBlock.tsx             # CARE, sovereignty, and cultural warnings
├── DrawerFooter.tsx                # Actions, links, dataset downloads
└── DrawerA11yHelpers.tsx           # Screen-reader descriptions, keyboard scaffolding
~~~

---

# 🧩 Component Responsibilities

## 📂 **DetailDrawer.tsx**
The primary drawer container.

Responsibilities:

- Render slide-out panel with reduced-motion adherence  
- Manage open/close transitions  
- Provide ARIA roles (`dialog`, `complementary`)  
- Maintain focus trapping  
- Integrate GovernanceContext, A11yContext, FocusContext  

Telemetry:

- `"drawer:open"`  
- `"drawer:close"`  
- `"drawer:section-expand"`  

Governance:

- Must block rendering if CARE prohibits content  
- Must show warnings before sensitive content  

---

## 🏷️ **DrawerHeader.tsx**
Displays:

- Title  
- Entity type  
- CAREBadge  
- Close button  
- ProvenanceChip (for immediate lineage reference)  

Accessibility:

- `<header>` landmark  
- Clear labeling and keyboard operability  

---

## 📄 **DrawerSection.tsx**
Reusable content block with:

- Section heading  
- Semantic `<section>` region  
- Optional description block  

Must:

- Preserve heading order  
- Avoid speculative or unverified text  

---

## 📊 **DrawerMetadata.tsx**
Displays metadata fields:

- Rights-holder  
- License  
- Source  
- Dataset size/type  
- Spatial-temporal extents (generalized when needed)  

Governance:

- Must indicate fields that have been masked or redacted  
- Must label AI-generated metadata  

---

## 🧬 **DrawerProvenance.tsx**
Renders full provenance chain:

- PROV-O linked entities  
- SBOM + manifest references  
- Transformation history  

Must:

- Provide JSON-LD download link  
- Maintain CARE alignment  
- Avoid inventing lineage  

Telemetry:

- `"drawer:provenance-open"`  

---

## ⚠️ **DrawerCAREBlock.tsx**
Displays mandatory ethical notices:

- Sovereignty warnings  
- Cultural sensitivity disclaimers  
- Explanation of H3 masking  
- CARE classification details  

Must appear **before** any sensitive content.

---

## 🧭 **DrawerFooter.tsx**
Contains:

- Action buttons (e.g., open in Focus Mode, download metadata)  
- External links with provenance  
- Dataset-specific tools  

Governance:

- Disabled buttons for restricted datasets  
- Screen-reader descriptions for sensitive actions  

Telemetry:

- `"drawer:action"`  

---

## ♿ **DrawerA11yHelpers.tsx**
Provides:

- SR-only descriptions of complex sections  
- Keyboard control helpers  
- ARIA attributes for drawer focus lifecycle  
- Announcements for open/close events  

Required for WCAG 2.1 AA compliance.

---

# 🔐 Governance & FAIR+CARE Integration

DetailDrawer components MUST:

- Display CARE classification clearly  
- Warn about sovereignty or cultural protections  
- Mask disallowed coordinate or metadata fields  
- Annotate AI-generated text segments  
- Provide provenance at all times  
- Prevent any speculative inference or unverified historical claims  

Any violation → **CI BLOCKER**.

---

# ♿ Accessibility Requirements

All drawers MUST:

- Provide keyboard navigation  
- Maintain visual focus rings  
- Use ARIA roles (`dialog`, `complementary`)  
- Respect reduced-motion settings  
- Provide alt text and textual equivalents for non-text elements  
- Maintain correct heading hierarchy  

Accessibility failure → **PR blocked**.

---

# 📈 Telemetry Responsibilities

Must emit:

- `"drawer:open"`  
- `"drawer:close"`  
- `"drawer:section-expand"`  
- `"drawer:provenance-open"`  
- `"drawer:care-warning"`  
- `"drawer:action"`  

Telemetry:

- Must be non-PII  
- Must include governance context  
- Must follow KFM telemetry schema  
- Logged to `focus-telemetry.json`  

---

# 🧪 Testing Requirements

Tests must include:

- Unit rendering tests  
- A11y tests (ARIA, keyboard, contrast)  
- Governance rule enforcement  
- Provenance propagation tests  
- Masking/redaction visibility tests  
- Telemetry validation  
- Focus/TimeContext integration tests  

Test locations:

~~~text
tests/unit/web/components/DetailDrawer/**
tests/integration/web/components/DetailDrawer/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full DetailDrawer documentation; governance, A11y, provenance, telemetry integration |
| v10.3.2 | 2025-11-14 | Added CARE + provenance improvements |
| v10.3.1 | 2025-11-13 | Initial drawer overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4  

</div>
