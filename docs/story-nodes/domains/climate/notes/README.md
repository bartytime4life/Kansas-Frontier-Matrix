---
title: "🌦️ KFM v11.2.6 — Climate Story Node Notes (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/climate/notes/README.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Climate Systems Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active"
doc_kind: "Notes Directory README"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:storynodes:domains:climate:notes:index:v11.2.6"
semantic_document_id: "kfm-storynodes-climate-notes-index-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/climate/notes/README.md"
immutability_status: "version-pinned"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"
schema_ref: "../../../../../schemas/json/story-node.schema.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

intent: "kfm-climate-storynode-notes"
lifecycle_stage: "draft-pool"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental · Attribution-Sensitive"
classification: "Generalized / Internal-Prep"
sensitivity: "Draft climate narratives and review notes (evidence-bounded; attribution-safe)"
sensitivity_level: "Low/Moderate"
public_exposure_risk: "Low"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "12 months"
sunset_policy: "Archived once integrated into stable Story Node sets"

provenance_chain:
  - "docs/story-nodes/domains/climate/notes/README.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "timeline-generation"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "📘 Overview"
    - "🎯 Allowed Content"
    - "🚫 Not Allowed"
    - "📜 Workflow Integration"
    - "🧪 Validation Notes"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "metadata-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🌦️ **Climate Story Node — Notes (KFM v11.2.6)**  
### *Draft Climate Events · Backlog · Data Reviews & Provenance Notes*  

`docs/story-nodes/domains/climate/notes/README.md`

**Purpose**  
Provide a workspace for **draft climate Story Nodes**, **data provenance notes**, **model considerations**,  
and **backlog items** awaiting refinement, validation, and governance approval.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 📂 🌦️ climate/
            └── 📂 🗒️ notes/
                ├── 📄 README.md                 # This file (notes directory index)
                ├── 📄 backlog.md                # Candidate Story Nodes & work queue
                └── 📄 ethics-checklist.md       # Climate ethics & attribution checklist
~~~

**Layout rules (normative)**  
- ASCII connectors remain plain for readability.  
- Directories use `📂` and MAY include a semantic emoji in the folder name (`🌦️ climate/`, `🗒️ notes/`).  
- Notes stay **generalized and internal-prep**; promotion to examples or published nodes requires the full review path.

---

## 📘 Overview

The climate **notes** area is used for:

- initial, incomplete drafts of climate Story Nodes
- early-stage interpretation notes (pending dataset verification)
- regional anomaly descriptions (heatwaves, droughts, cold spells, wind episodes)
- preliminary attribution-risk flags (what must be phrased cautiously)
- model performance notes (HRRR, ERA5, GOES, GFS, CMIP-class outputs)
- provenance scaffolding (what must be cited, linked, and versioned)
- reviewer questions and uncertainty framing

Nothing in this directory is considered final until it:

1. validates against `story-node.schema.json`,  
2. meets scientific rigor and uncertainty requirements,  
3. passes the climate ethics & attribution checklist,  
4. has STAC/DCAT references and PROV-O lineage where applicable,  
5. is approved by the Climate Systems Board (and governance reviewers as required).

---

## 🎯 Allowed Content

✔ Draft storylines summarizing events (observations-first)  
✔ Region-wide anomaly descriptions (generalized geography; valid GeoJSON when included)  
✔ Dataset availability checks (what exists, time coverage, known gaps)  
✔ Uncertainty notes and “wording risk” flags  
✔ Spatial generalization decisions (counties/regions/watersheds; no sensitive infrastructure)  
✔ Model vs observation separation notes  
✔ Historical analog candidates (public-domain / publicly documented only)

---

## 🚫 Not Allowed

🚫 Personal data  
🚫 Overconfident climate-attribution statements (“caused by climate change”) without evidence and stated confidence  
🚫 Speculation presented as fact  
🚫 Fake precision (over-specific time windows or boundaries without data support)  
🚫 Proprietary/unpublished model configs or private run parameters  
🚫 Media/rasters without license/rights review  
🚫 Sensitive infrastructure details (site-level vulnerabilities, internal-only facilities, etc.)

---

## 📜 Workflow Integration

### Draft → Review → Story Node

1. Add or update a candidate in `backlog.md`.  
2. Capture supporting notes here (short, generalized, evidence-bounded).  
3. Validate datasets (NOAA, NWS, HRRR, GOES, ERA5, etc.) and record sources.  
4. Run the checklist in `ethics-checklist.md`.  
5. Convert to:
   - Markdown Story Node (if your domain allows MD nodes), or
   - JSON Story Node (schema-valid) for ingestion.
6. Move completed work to:
   - `docs/story-nodes/domains/climate/examples/` (curated examples), or
   - the main Story Node tree (published nodes), per governance.

---

## 🧪 Validation Notes

Draft notes here **do not** need to be schema-valid, but they MUST still:

- remain scientifically accurate (no unit confusion, no model/obs conflation)
- use careful language around attribution and causality
- keep geographies generalized and public-safe
- prefer ISO-8601 temporal references when stating time windows
- preserve a clear “what we saw” vs “what we infer” separation

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Upgraded to KFM-MDP v11.2.6; added structured metadata + emoji directory layout; clarified allowed/prohibited content. |
| v11.2.2 | 2025-11-30 | Initial governed climate notes directory.                               |
| v11.2.1 | 2025-11-29 | Added backlog + ethics checklist structure.                             |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) ·
[🌦️ Climate Domain](../README.md) ·
[🧪 Climate Examples](../examples/README.md) ·
[📏 Standards Index](../../../../standards/README.md) ·
[🛡 Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
