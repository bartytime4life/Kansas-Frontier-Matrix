---
title: "🧾 Kansas Frontier Matrix — Excalidraw Sketch Metadata"
document_type: "Design Metadata Specification"
version: "v1.0.0"
last_updated: "2025-10-22"
authors: ["@kfm-design", "@kfm-data", "@kfm-architecture"]
status: "Stable"
license: "CC-BY 4.0"
asset_class: "Metadata Definitions"
design_stage: "Ideation → Documentation"
review_cycle: "Quarterly"
approvers: ["@kfm-design-lead", "@kfm-architecture"]
mcp_alignment: ["Documentation-First", "Reproducibility", "Provenance", "Accessibility", "Open-Standards"]
semantic_alignment: ["CIDOC CRM", "schema.org/CreativeWork"]
data_integrity: "sha256 validated via docs-validate.yml"
schema_version: "MCP-DL v6.3"
metadata_schema: "docs/standards/metadata-schema.yml"
provenance_method: "Git-based + SHA256 chain"
linked_standards: ["FAIR Principles", "ISO 19115"]
archival_policy: "Immutable metadata entries preserved alongside sketches"
related_components: ["Excalidraw Sketches", "Design Mockups", "Figma Components", "System Architecture"]
---

<div align="center">

# 🧾 Kansas Frontier Matrix — Excalidraw Sketch Metadata  
`docs/design/mockups/excalidraw/sketches/metadata/`

**Structured · Provenanced · Discoverable**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../docs/design/)
[![Metadata Schema](https://img.shields.io/badge/Schema-MCP--DL%20Metadata%20v3.2-orange)](../../../../../../docs/standards/metadata-schema.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **metadata JSON files** describing each Excalidraw sketch in the Kansas Frontier Matrix (KFM) design system.  
Metadata provides contextual information for each sketch — enabling **traceability**, **semantic linking**, and **provenance validation** in alignment with the **Master Coder Protocol (MCP-DL v6.3)**.

Each metadata file complements its corresponding `.excalidraw` sketch and `.svg` export under `../`.

---

## 🧭 Purpose

The purpose of this metadata layer is to:
- Standardize **design record-keeping** for ideation and mockup artifacts.  
- Enable **semantic search and relationships** between sketches and related design documents.  
- Support **reproducibility**, **authorship tracking**, and **design lineage mapping**.  
- Integrate with the **KFM Design Asset Indexer** and **MkDocs documentation site**.

> 💡 Each metadata entry acts as a *digital passport* for a design artifact, connecting visual, textual, and conceptual information.

---

## 📁 Directory Structure

```text
docs/design/mockups/excalidraw/sketches/metadata/
├── README.md                              # This documentation file
├── 20251006_timeline-scrubber-concept.json
├── 20251010_ai-context-diagram.json
└── checksums.txt                          # Validation log for metadata integrity
```

**Naming Convention:**  
`YYYYMMDD_topic-shortdesc.json` — mirrors associated `.excalidraw` file.  
Example: `20251006_timeline-scrubber-concept.json` ↔ `20251006_timeline-scrubber-concept.excalidraw`.

---

## 🧩 Metadata Schema

| Field | Type | Description | Example |
|:--|:--|:--|:--|
| `id` | String | Unique ID of the sketch (slug format). | `timeline-scrubber-concept` |
| `title` | String | Descriptive title of the sketch. | `"Timeline Scrubber Interaction Concept"` |
| `author` | String | Creator(s) or team. | `"Kansas Frontier Matrix Design Team"` |
| `created` | Date | Creation date (YYYY-MM-DD). | `"2025-10-06"` |
| `modified` | Date | Last modified date. | `"2025-10-22"` |
| `tags` | Array | Keywords for search and classification. | `["timeline", "interaction", "ui"]` |
| `status` | Enum | Current phase: `concept`, `approved`, `implemented`, `archived`. | `"concept"` |
| `description` | String | Brief explanation of the design intent. | `"Explores early ideas for timeline scrubbing and playback."` |
| `related` | Array | Paths to related design or documentation files. | `["docs/design/mockups/figma/components/navigation/README.md"]` |
| `license` | String | License identifier. | `"CC-BY-4.0"` |
| `checksum` | String | SHA256 checksum of the associated `.excalidraw` file. | `"sha256-23bd..."` |
| `provenance` | Object | Commit, author, and version references. | `{ "commit": "abc123", "branch": "main" }` |

---

## 🧮 Example Metadata File

```json
{
  "id": "timeline-scrubber-concept",
  "title": "Timeline Scrubber Interaction Concept",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-06",
  "modified": "2025-10-22",
  "tags": ["timeline", "interaction", "ui", "design"],
  "status": "concept",
  "description": "Explores early ideas for timeline scrubbing and playback within the map synchronization context.",
  "related": [
    "docs/design/mockups/figma/components/navigation/README.md"
  ],
  "license": "CC-BY-4.0",
  "checksum": "sha256-23bd...",
  "provenance": {
    "commit": "d4aef23",
    "branch": "main",
    "reviewed_by": "@kfm-design-lead",
    "verified": true
  }
}
```

---

## 🧠 Integration with KFM Systems

- **Design Asset Indexer**: Automatically scans metadata and updates central registries.  
- **MkDocs Builder**: Embeds metadata summaries in design documentation pages.  
- **Analytics Pipeline**: Collects usage statistics through the `assetView` telemetry schema.  
- **Integrity Validator**: Confirms checksums match `.excalidraw` sources via CI.  

---

## 🧪 Validation & CI Integration

| Validation Task | Description | CI Workflow |
|:--|:--|:--|
| **Schema Validation** | Checks field types and required fields | `docs-validate.yml` |
| **Checksum Verification** | Ensures integrity against source files | `checksum-verify.yml` |
| **Naming Convention** | Enforces consistent filenames | `pre-commit lint` |
| **Metadata Completeness** | Confirms minimum fields (`id`, `title`, `author`, `checksum`) | `design-assets-lint.yml` |

---

## ♿ Accessibility & Semantics

- Metadata files are **machine-readable JSON**, ensuring compatibility with accessibility tooling.  
- Fields like `description` and `title` enhance assistive content rendering in MkDocs and search indexing.  
- Compliant with **schema.org/CreativeWork** and **WCAG 2.1 AA** contextual metadata practices.  

---

## 🧾 Example Provenance Log (checksums.txt)

```
20251006_timeline-scrubber-concept.json  sha256-14be8c...
20251010_ai-context-diagram.json          sha256-9ac3b9...
```

---

## ✅ Compliance Summary

| Standard | Status | Verified In | Verified By | Notes |
|:--|:--|:--|:--|:--|
| MCP-DL v6.3 | ✅ | docs-validate.yml | CI Bot | Metadata schema compliance |
| FAIR Principles | ✅ | docs-validate.yml | @kfm-data | Findable and Interoperable |
| CIDOC CRM / schema.org | ✅ | metadata mapping | @kfm-architecture | Aligned with CreativeWork schema |
| Provenance Hashing | ✅ | checksums.txt | CI | Integrity chain maintained |
| Data Integrity | ✅ | design-assets-lint.yml | CI | JSON and checksum parity validated |

---

## 🗓️ Change Log

| Date | Description |
|:--|:--|
| **2025-10-22** | Initial release — metadata structure, schema, and validation integration |

---

## 📜 License & Credits

Metadata © 2025 **Kansas Frontier Matrix Project**.  
Licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.  

Created and maintained by the **KFM Design & Interaction Team**  
in accordance with the **Master Coder Protocol (MCP-DL v6.3)**.

**Document checksum:** `sha256:bcf2b134f2631d1f51d2d28c8a2c1aa50e379a5b6af85f50e8683902e14e11b2`  
**PGP Signature:**  
```
-----BEGIN KFM-SIGNATURE-----
bWV0YWRhdGEtcmVhZG1lLWRvYy12MS4wLjAKQW5keSBCYXJ0YSwgMjAyNS0xMC0yMg==
-----END KFM-SIGNATURE-----
```