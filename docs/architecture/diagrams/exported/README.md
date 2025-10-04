<div align="center">

# 🖼️ Kansas Frontier Matrix — Exported Diagram Assets  
`docs/architecture/diagrams/exported/`

**Mission:** Maintain all **rendered architectural diagrams** — exported from their  
Mermaid (`.mmd`) or vector sources — in open formats such as **SVG**, **PNG**, and **PDF**,  
ensuring visual documentation is **consistent, reproducible, and version-controlled**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

The `docs/architecture/diagrams/exported/` directory contains **rendered visual outputs**  
that illustrate the **data, system, web, and CI/CD architectures** of the Kansas Frontier Matrix.

These diagrams are **compiled** from their Mermaid (`.mmd`) or source JSON specifications in  
`docs/architecture/diagrams/` and are referenced throughout documentation in:

- `docs/architecture/architecture.md`  
- `docs/architecture/data-architecture.md`  
- `docs/architecture/web-ui-architecture.md`  
- `docs/architecture/ci-cd.md`  
- `README.md` (repository root summary view)

Each diagram is an **artifact of record** — its metadata, creation date, and author information  
are embedded within its file or listed below.

---

## 🗂️ Directory Layout

```bash
docs/architecture/diagrams/exported/
├── README.md                        # This file (diagram metadata + policies)
├── data_flow.png                    # Data ingestion + ETL pipeline visualization
├── web_ui_architecture.svg          # Web interface & MapLibre system diagram
├── provenance_chain.svg             # Provenance model for datasets
├── ci_cd_pipeline.png               # Continuous integration + validation flow
├── system_overview.png              # Full-stack system architecture summary
└── knowledge_graph.svg              # Knowledge graph and semantic layer design
````

> **Note:**
> Each exported diagram directly corresponds to a `.mmd` source file in
> `docs/architecture/diagrams/` (one-to-one relationship).

---

## 🧠 Export Workflow

### CLI-Based Export (Mermaid CLI)

```bash
npx @mermaid-js/mermaid-cli -i data_flow.mmd -o exported/data_flow.png
```

### Makefile Target

```bash
make diagrams
```

**Process Summary:**

1. Validate Mermaid syntax (`.mmd` files).
2. Render to `.png` and `.svg` using Mermaid CLI.
3. Embed metadata (author, timestamp, commit hash).
4. Store outputs in `/exported/` for use in docs and site builds.
5. Reference them in corresponding `.md` architecture documents.

---

## 🧩 File Metadata Schema

All exported diagrams follow this embedded metadata convention (for SVG/PNG):

| Field            | Description                  | Example                  |
| :--------------- | :--------------------------- | :----------------------- |
| **title**        | Diagram name or purpose      | “KFM Data Flow Overview” |
| **author**       | Diagram creator              | “KFM Dev Team”           |
| **date_created** | Date of last export          | `2025-10-04`             |
| **source_file**  | Linked `.mmd` file           | `../data_flow.mmd`       |
| **commit_hash**  | Git commit ID at export time | `a93f0a2`                |
| **format**       | Output format                | `SVG`, `PNG`, or `PDF`   |
| **license**      | Usage license                | `CC-BY 4.0`              |

---

## 🧮 Version Control & Reproducibility

| Policy                   | Description                                                             |
| :----------------------- | :---------------------------------------------------------------------- |
| **One Source Rule**      | Every exported diagram must have a single authoritative `.mmd` source.  |
| **Deterministic Builds** | Re-exporting from the same `.mmd` and commit produces identical output. |
| **Version Tagging**      | Exports are tied to repository commits and release versions.            |
| **Open Formats Only**    | Only `.svg`, `.png`, `.pdf` are permitted for storage.                  |
| **No Binary Edits**      | Diagrams must not be altered outside the export process.                |

---

## 📊 Export Metadata Example

### `system_overview.svg` Metadata

```json
{
  "title": "Kansas Frontier Matrix — System Overview",
  "author": "KFM Documentation Team",
  "date_created": "2025-10-04",
  "source_file": "../system_overview.mmd",
  "commit_hash": "f5e84c9",
  "format": "SVG",
  "license": "CC-BY 4.0"
}
```

---

## 🧩 Integration with Documentation

| Documentation File       | Embedded Diagram(s)                         |
| :----------------------- | :------------------------------------------ |
| `architecture.md`        | `system_overview.png`, `ci_cd_pipeline.png` |
| `data-architecture.md`   | `data_flow.png`, `provenance_chain.svg`     |
| `web-ui-architecture.md` | `web_ui_architecture.svg`                   |
| `knowledge-graph.md`     | `knowledge_graph.svg`                       |
| `ci-cd.md`               | `ci_cd_pipeline.png`                        |

These exported images are automatically referenced in Markdown via
relative paths, ensuring **offline readability** and **site portability**.

---

## 🧰 Maintenance & Regeneration

| Command                  | Purpose                                                   |
| :----------------------- | :-------------------------------------------------------- |
| `make diagrams`          | Rebuilds all `.png`/`.svg` diagrams from Mermaid sources. |
| `make clean-diagrams`    | Removes all existing exports for full regeneration.       |
| `make diagrams-metadata` | Generates a JSON manifest with metadata for all diagrams. |

> **Manifest Output:** `docs/architecture/diagrams/exported/_manifest.json`
> Includes file names, last export time, commit hash, and corresponding `.mmd` sources.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                     |
| :---------------------- | :----------------------------------------------------------------- |
| **Documentation-first** | Each diagram has a corresponding `.mmd` source and metadata entry. |
| **Reproducibility**     | Exports deterministically generated from versioned Mermaid files.  |
| **Open Standards**      | SVG and PNG formats under CC-BY 4.0.                               |
| **Provenance**          | Embedded metadata links diagram to source and commit hash.         |
| **Auditability**        | Export process validated via `make diagrams` and CI/CD logs.       |

---

## 📎 Related Directories

| Path                          | Description                                                                 |
| :---------------------------- | :-------------------------------------------------------------------------- |
| `docs/architecture/diagrams/` | Source `.mmd` files for all architecture visuals.                           |
| `docs/architecture/`          | Architecture and system-level documentation.                                |
| `.github/workflows/site.yml`  | Workflow that rebuilds diagrams during site deployment.                     |
| `Makefile`                    | Contains automation commands for diagram rendering and metadata generation. |

---

## 📅 Version History

| Version | Date       | Summary                                                                              |
| :------ | :--------- | :----------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial documentation for exported architecture diagrams and visual asset standards. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Diagram Documented. Every Image Reproducible.”*
📍 [`docs/architecture/diagrams/exported/`](.) · Repository for all rendered architectural diagrams and visual assets.

</div>
