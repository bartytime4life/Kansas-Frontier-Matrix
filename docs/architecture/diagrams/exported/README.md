<div align="center">

# 🖼️ **Kansas Frontier Matrix — Exported Diagram Assets (v2.0.0 · Tier-Ω+∞ Certified)**  
`docs/architecture/diagrams/exported/`

**Mission:** Curate and maintain all **rendered architecture diagrams** of the **Kansas Frontier Matrix (KFM)** — each diagram a **provenance-verified visual artifact**, exported from **Mermaid (`.mmd`)**, **Excalidraw**, or **vector sources** into reproducible, **open-standard formats** (SVG, PNG, PDF).  
Every exported diagram is a **validated, versioned artifact** aligned with **MCP-DL v6.3** documentation and CI/CD reproducibility policies.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../docs/)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../../../.github/workflows/stac-validate.yml)
[![SBOM & SLSA](https://img.shields.io/badge/Supply--Chain-SBOM%20%7C%20SLSA-green)](../../../../.github/workflows/slsa.yml)
[![Docs Validate](https://img.shields.io/badge/docs-validated-brightgreen)](../../../../.github/workflows/docs-validate.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Exported Diagram Assets"
document_type: "README"
version: "v2.0.0"
last_updated: "2025-11-16"
authors: ["@kfm-architecture","@kfm-docs","@kfm-design"]
status: "Stable"
maturity: "Production"
license: "CC-BY 4.0"
tags: ["diagrams","visualization","architecture","mcp","mermaid","svg","reproducibility","metadata"]
alignment:
  - MCP-DL v6.3
  - STAC 1.0
  - FAIR Principles
  - SLSA 3
  - ISO 19115-1 Metadata
validation:
  ci_workflows: ["site.yml","docs-validate.yml","policy-check.yml"]
  mermaid_end_marker: "<!-- END OF MERMAID -->"
preservation_policy:
  retention: "365d exports · 90d logs"
  checksum_algorithm: "SHA-256"
observability:
  metrics: ["diagram_build_latency_ms","mermaid_validation_errors","svg_size_kb","export_count"]
  endpoint: "https://metrics.kfm.ai/diagrams"
---
```

---

## 📚 Overview

The `docs/architecture/diagrams/exported/` directory is the **canonical visual documentation registry** for KFM.  
Each diagram is a **version-controlled, metadata-embedded artifact** used in reports, publications, and CI/CD documentation builds.  

Every export:
- ✅ **Preserves provenance** — metadata embedded at export time (`author`, `commit`, `timestamp`).
- 🔁 **Is reproducible** — deterministic rendering via CLI or CI workflows.
- 🧩 **Aligns with architecture docs** — one-to-one mapping with `.mmd` source files.
- 🌍 **Uses open formats** — SVG, PNG, and PDF only.
- 🔐 **Is validated** in the CI/CD build pipeline for integrity and accessibility.

---

## 🗂️ Directory Layout

```bash
docs/architecture/diagrams/exported/
├── README.md                        # (This file)
├── data_flow.png                    # ETL + validation pipeline visualization
├── web_ui_architecture.svg          # Web interface + MapLibre configuration
├── provenance_chain.svg             # Provenance chain + data lineage model
├── ci_cd_pipeline.png               # CI/CD automation and governance diagram
├── system_overview.png              # Full KFM system ecosystem diagram
├── knowledge_graph.svg              # Semantic + ontology architecture
└── _manifest.json                   # Generated metadata manifest for all exports
```

> Each exported diagram has a corresponding `.mmd` source in `docs/architecture/diagrams/`.  
> No manual edits to images are permitted — exports must originate from validated source files.

---

## 🧠 Export Workflow

### 🧩 CLI-Based Rendering (Mermaid CLI)

```bash
npx @mermaid-js/mermaid-cli -i system_overview.mmd -o exported/system_overview.png
```

### ⚙️ Makefile Target

```bash
make diagrams
```

**Automated Process:**

1. Validate Mermaid syntax and structure.
2. Render to `.png` + `.svg` via Mermaid CLI.
3. Embed metadata fields (commit, author, timestamp, version).
4. Store exports in `/exported/`.
5. Cross-validate against `_manifest.json` and CI logs.

---

## 🧩 File Metadata Schema

| Field | Description | Example |
|:------|:-------------|:--------|
| **title** | Diagram title or purpose | "Kansas Frontier Matrix — CI/CD Architecture" |
| **author** | Primary author or team | "@kfm-architecture" |
| **date_created** | UTC timestamp | `2025-11-16T18:21:00Z` |
| **source_file** | Relative path to `.mmd` file | `../system_overview.mmd` |
| **commit_hash** | SHA of repository state | `8b21c9d` |
| **format** | Output type | `SVG` |
| **license** | Usage rights | `CC-BY 4.0` |
| **checksum** | SHA-256 checksum of export | `4d3b2c...` |

---

## 🧮 Version Control & Provenance Policy

| Policy | Description |
|:--|:--|
| **One Source Rule** | Each exported diagram must have exactly one source `.mmd`. |
| **Deterministic Rendering** | Same commit → same export; no divergence allowed. |
| **Version Coupling** | Diagram updates tracked by SemVer + release tag. |
| **Open Format Enforcement** | Only `.svg`, `.png`, `.pdf` accepted (no proprietary formats). |
| **Integrity Validation** | Every file must pass SHA-256 and STAC-linked metadata check. |

---

## 🧰 CI/CD Integration

| Workflow | Function | Trigger |
|:--|:--|:--|
| **`site.yml`** | Builds documentation site, including diagrams. | On merge to `main` |
| **`docs-validate.yml`** | Validates frontmatter, metadata, and diagram syntax. | On PR |
| **`policy-check.yml`** | Ensures licensing, metadata completeness. | On PR |
| **`stac-validate.yml`** | Cross-validates STAC linkage metadata for diagrams. | On commit |

Validation artifacts are written to:  
`data/work/logs/diagrams/diagram_validation.log`

---

## 📊 Example Metadata Manifest

**File:** `_manifest.json`

```json
{
  "generated_at": "2025-11-16T18:25:00Z",
  "generator": "make diagrams-metadata",
  "diagrams": [
    {
      "file": "system_overview.png",
      "source": "../system_overview.mmd",
      "commit_hash": "b3d7f4a",
      "checksum": "97f2b8e...",
      "format": "PNG",
      "author": "@kfm-architecture"
    },
    {
      "file": "provenance_chain.svg",
      "source": "../provenance_chain.mmd",
      "commit_hash": "f01e7b9",
      "checksum": "3b19c7f...",
      "format": "SVG",
      "author": "@kfm-data"
    }
  ]
}
```

---

## 🧩 Integration Map

| Documentation File | Linked Diagram(s) | Purpose |
|:--|:--|:--|
| `architecture.md` | `system_overview.png`, `ci_cd_pipeline.png` | Full system layout |
| `data-architecture.md` | `data_flow.png`, `provenance_chain.svg` | Data lineage & validation |
| `web-ui-architecture.md` | `web_ui_architecture.svg` | Frontend visualization |
| `knowledge-graph.md` | `knowledge_graph.svg` | Ontology + graph schema |
| `ci-cd.md` | `ci_cd_pipeline.png` | Workflow governance |

---

## 🧭 Rendering Standards

| Requirement | Description |
|:--|:--|
| **Theme** | Accessible neutral palette, high-contrast text |
| **Font** | Sans-serif, consistent across diagrams |
| **Labels** | Plain-text labels, no embedded special characters |
| **Commit Convention** | `add(diagram): <name>` for exports |
| **Provenance Footer** | Must contain author + date metadata |

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
|:--|:--|
| **Documentation-first** | Every diagram has a readable `.mmd` source and metadata block. |
| **Reproducibility** | Deterministic exports from versioned sources. |
| **Open Standards** | SVG, PNG, PDF under CC-BY 4.0. |
| **Provenance** | Metadata + checksums link back to commit + author. |
| **Auditability** | CI workflows validate diagrams pre-merge. |

---

## 📎 Related Documentation

- `docs/architecture/diagrams/README.md` — Source architecture diagrams  
- `docs/architecture/architecture.md` — Full system overview  
- `.github/workflows/site.yml` — Diagram rendering and documentation build  
- `Makefile` — Diagram build and manifest generation commands  
- `docs/architecture/README.md` — Index of system, data, and web architectures  

---

## 🗓 Version History

| Version | Date | Summary |
|:--|:--|:--|
| **v2.0.0** | 2025-11-16 | Tier-Ω+∞: Added metadata manifest, observability metrics, policy validation, and STAC-linked provenance. |
| v1.0.0 | 2025-10-04 | Initial documentation for exported diagrams. |

---

<div align="center">

**Kansas Frontier Matrix — Exported Diagram Assets**  
*“Every Diagram Verified · Every Image Versioned · Every Pixel Provenant.”*

</div>