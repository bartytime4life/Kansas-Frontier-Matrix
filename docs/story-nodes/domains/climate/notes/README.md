---
title: "🌦️ KFM v11.2.2 — Climate Story Node Notes"
path: "docs/story-nodes/domains/climate/notes/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Continuous · Climate Systems Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:climate:notes:v11.2.2"
semantic_document_id: "kfm-storynodes-climate-notes"
event_source_id: "ledger:storynodes/climate/notes"
immutability_status: "version-pinned"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active"
doc_kind: "Notes Directory README"
intent: "kfm-climate-storynode-notes"
lifecycle_stage: "draft-pool"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental"
classification: "Generalized / Internal-Prep"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 months"
sunset_policy: "Archived once integrated into stable Story Node sets"
---

<div align="center">

# 🌦️ **Climate Story Node — Notes (KFM v11)**  
### *Draft Climate Events · Backlog · Data Reviews & Provenance Notes*  

`docs/story-nodes/domains/climate/notes/README.md`

**Purpose**  
Provide a workspace for **draft climate Story Nodes**,  
**data provenance notes**, **model considerations**,  
and **backlog items** awaiting refinement and validation.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/story-nodes/domains/climate/notes/
├── 📄 README.md                       # This file
├── 📑 backlog.md                      # Candidate Story Nodes & work queue
└── ⚖️ ethics-checklist.md             # Climate/AI ethics & attribution checklist
~~~

This directory holds **non-final** content that contributes to:

- climate event drafts  
- anomaly descriptions  
- model attribution notes  
- dataset review steps  
- Focus Mode preparation  
- scientific uncertainty framing  

---

## 📘 Overview

The climate notes area is used for:

- Initial, incomplete drafts of climate Story Nodes  
- Early-stage interpretation notes (pending dataset verification)  
- Long-term climate trend candidates  
- Regional anomaly descriptions (heatwaves, droughts, freeze events)  
- Preliminary climate attribution discussions  
- Model performance notes (HRRR, ERA5, GOES, GFS, CMIP6)  
- Environmental impact considerations  
- Questions for domain reviewers  

Nothing in this directory is considered final until it:

1. Validates against **story-node.schema.json**,  
2. Meets **scientific rigor & uncertainty** requirements,  
3. Passes environmental ethics review,  
4. Satisfies STAC/DCAT provenance completeness,  
5. Is approved by the Climate Systems Board.

---

## 🎯 Allowed Content

✔ Draft storylines summarizing events  
✔ Region-wide anomaly descriptions  
✔ Model comparison tables  
✔ Uncertainty notes  
✔ Spatial generalization decisions  
✔ Data quality checks for radar, satellite, reanalysis  
✔ Notes about historical analog events  

🚫 **Not allowed:**  
- Personal data  
- Overconfident climate-attribution claims  
- Speculation unsupported by datasets  
- Fake precision (temporal or spatial)  
- Unpublished proprietary model details  
- Media or rasters without license/rights review  

---

## 📜 Workflow Integration

### Draft → Review → Story Node

1. Add draft concept to **backlog.md**.  
2. Draft narrative & data notes in a working section.  
3. Validate datasets (NOAA, HRRR, GOES, ERA5, etc.).  
4. Run climate ethics checklist.  
5. Convert to:
   - Markdown Story Node (author template), or  
   - JSON Story Node (schema-valid).  
6. Move finished nodes to `examples/` or publish in the main Story Node directory.

---

## 🧪 Validation Notes

Draft notes here **do not** need to be schema-valid, but must still:

- adhere to masking/generalization of sensitive infrastructure  
- avoid unsupported attributions  
- remain scientifically accurate  
- match CF units/variable expectations  
- use ISO temporal references when possible  

---

## 🕰️ Version History

| Version | Date       | Summary                                                       |
|--------:|------------|---------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed climate notes directory.                     |
| v11.2.1 | 2025-11-29 | Added backlog + ethics checklist structure.                   |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

