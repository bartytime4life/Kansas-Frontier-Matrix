---
title: "🏺 Kansas Frontier Matrix — Archaeological Symbol Metadata Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/metadata/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Heritage Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/reports-visualization-focusmode-archsymbols-meta-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Archaeological Symbol Metadata — Focus Mode Legend System**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/metadata/README.md`

**Purpose:**  
Define the metadata structures, cultural governance fields, provenance rules, and FAIR+CARE validation requirements for **archaeological legend symbols** used in Focus Mode story node visualizations.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This metadata layer governs **all archaeological symbol assets** (SVG icons, controlled markers, protected heritage symbology) appearing in:

- Story Node map layers  
- 2D base/overlay maps  
- 3D Focus Mode scenes  
- Narrative-driven archaeological reconstructions  

All entries must follow:
- KFM v10 metadata schema  
- CARE-sensitive restrictions  
- WCAG accessibility labeling  
- FAIR+CARE governance pipelines  

---

## 🗂️ Directory Layout

```plaintext
metadata/
├── README.md                       # This file
├── field_definitions.md            # Required fields & schema rules
└── examples/
    ├── burial_mound_restricted.json
    ├── generalized_village_marker.json
    └── pottery_class_marker.json
```

---

## 🧩 Required Archaeological Symbol Metadata Fields

| Field | Description | Required | Example |
|-------|-------------|----------|---------|
| `id` | Unique symbol ID | ✅ | `"arch_symbol_village_generalized_v10"` |
| `title` | Human-readable symbol name | ✅ | `"Generalized Village Icon"` |
| `domain` | Always `"archaeology"` | ✅ | `"archaeology"` |
| `format` | Usually `"SVG"` | ✅ | `"SVG"` |
| `checksum_sha256` | Integrity hash of asset | ✅ | `"sha256-78afc1..."` |
| `care.status` | `approved` \| `restricted` | ⚠ Required for cultural items | `"restricted"` |
| `care.statement` | Cultural governance notes | ⚙️ | `"Spatial generalization ≥ 20 km"` |
| `care.reviewer` | FAIR+CARE Heritage Council reviewer | ⚙️ | `"KFM Heritage Board"` |
| `accessibility.title` | Required `<title>` label for screen readers | ✅ | `"Village (generalized)"` |
| `accessibility.desc` | Detailed `<desc>` for non-visual use | ⚙️ | `"Represents a generalized habitation site in Kansas."` |
| `updated` | ISO8601 timestamp | ✅ | `"2025-11-12T20:12:00Z"` |

---

## 🧠 CARE Governance Requirements

Sensitive archaeological symbols must include:
- Clear **care.status**  
- Distances for generalization  
- Notes on data sensitivity  
- Cultural steward reviewer name  
- Metadata stored in governance ledger  

Example CARE block:

```json
"care": {
  "status": "restricted",
  "statement": "Used only for masked sacred-area visualization.",
  "reviewer": "FAIR+CARE Heritage Council",
  "date_reviewed": "2025-11-12"
}
```

---

## 🧮 Provenance & Telemetry Integration

Every metadata file is linked to:
- Release **manifest.zip**  
- **SBOM SPDX** entry  
- **SHA-256** integrity checks  
- **focus-telemetry.json** for energy, carbon, and validation metrics  
- Governance Ledger entries for approval

Automated workflows:
- `faircare-validate.yml`  
- `stac-validate.yml` (when used in spatial layers)  
- `docs-lint.yml`  
- `telemetry-export.yml`  

---

## 📋 Example Metadata Record

```json
{
  "id": "arch_symbol_mound_protected_v10",
  "title": "Protected Mound (Generalized)",
  "domain": "archaeology",
  "format": "SVG",
  "checksum_sha256": "sha256-b92a1cf9d4e9aa...",
  "care": {
    "status": "restricted",
    "statement": "Culturally sensitive; generalized to >25 km radius.",
    "reviewer": "FAIR+CARE Heritage Board"
  },
  "accessibility": {
    "title": "Burial Mound (generalized)",
    "desc": "Represents a culturally sensitive burial mound shown only in generalized form."
  },
  "updated": "2025-11-12T20:12:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | FAIR+CARE Heritage Council | Initial metadata index for archaeological symbol governance and field definitions. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Master Coder Protocol v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Archaeological Symbols](../README.md)

</div>

