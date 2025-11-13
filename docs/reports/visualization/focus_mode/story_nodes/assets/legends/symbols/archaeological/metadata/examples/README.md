---
title: "🏺 Kansas Frontier Matrix — Archaeological Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/metadata/examples/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Heritage Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/reports-visualization-focusmode-archsymbols-examples-v1.json"
governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Archaeological Symbol Metadata — Example Records**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/metadata/examples/README.md`

**Purpose:**  
Provide **validated example metadata records** for archaeological legend symbols used in Focus Mode story nodes, demonstrating correct FAIR+CARE governance, accessibility labeling, and provenance structure.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

These examples serve as **reference templates** for constructing symbol metadata files within:

```
focus_mode / story_nodes / assets / legends / symbols / archaeological / metadata/
```

All examples follow:
- Field rules in `field_definitions.md`
- CARE governance policies
- Accessibility labeling requirements
- SBOM + manifest linkage
- Telemetry compliance (v10.2 schema)

---

## 🗂️ Directory Layout

```plaintext
examples/
├── README.md                    # This file
├── village_generalized.json     # Example: generalized habitation symbol
├── mound_protected.json         # Example: restricted sacred mound symbol
└── pottery_marker.json          # Example: pottery/cultural layer symbol
```

---

## 🧪 Example 1 — Generalized Village Symbol

### JSON

```json
{
  "id": "arch_symbol_village_generalized_v10",
  "title": "Generalized Village Icon",
  "domain": "archaeology",
  "format": "SVG",
  "checksum_sha256": "sha256-12ab45f9c3ef...",
  "care": {
    "status": "approved",
    "statement": "Generalized to ensure no site-level precision.",
    "reviewer": "FAIR+CARE Heritage Council",
    "date_reviewed": "2025-11-12"
  },
  "accessibility": {
    "title": "Village (generalized)",
    "desc": "Represents a generalized habitation site, not tied to exact coordinates."
  },
  "updated": "2025-11-12T20:25:00Z"
}
```

---

## 🧪 Example 2 — Restricted Mound Symbol

### JSON

```json
{
  "id": "arch_symbol_mound_protected_v10",
  "title": "Protected Mound (Generalized)",
  "domain": "archaeology",
  "format": "SVG",
  "checksum_sha256": "sha256-78cf2b91ea77...",
  "care": {
    "status": "restricted",
    "statement": "Sensitive burial structure; symbol masks site within >25 km radius.",
    "reviewer": "FAIR+CARE Heritage Council",
    "date_reviewed": "2025-11-12",
    "notes": "Not for public un-generalized display."
  },
  "accessibility": {
    "title": "Burial Mound (generalized)",
    "desc": "Represents a sensitive burial mound shown only in generalized form."
  },
  "updated": "2025-11-12T20:26:00Z"
}
```

---

## 🧪 Example 3 — Pottery / Artifact Symbol

### JSON

```json
{
  "id": "arch_symbol_pottery_marker_v10",
  "title": "Artifact / Pottery Find Icon",
  "domain": "archaeology",
  "format": "SVG",
  "checksum_sha256": "sha256-ae83d79faf18...",
  "care": {
    "status": "approved",
    "statement": "Non-site-specific artifact type marker.",
    "reviewer": "FAIR+CARE Heritage Council",
    "date_reviewed": "2025-11-12"
  },
  "accessibility": {
    "title": "Pottery Artifact Marker",
    "desc": "Indicates the presence of a cultural artifact layer (non-sensitive)."
  },
  "updated": "2025-11-12T20:27:00Z"
}
```

---

## ⚖️ FAIR+CARE Validation Summary (Examples)

| Example | CARE Status | Sensitivity Level | Accessibility Complete | SBOM/Manifest Reference |
|---------|-------------|-------------------|------------------------|--------------------------|
| Village | approved | low | yes | v10.2 ✓ |
| Mound | restricted | high | yes | v10.2 ✓ |
| Pottery | approved | low | yes | v10.2 ✓ |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | FAIR+CARE Heritage Council | Initial examples library for archaeological symbol metadata. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Master Coder Protocol v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Metadata Index](../README.md)

</div>

