<div align="center">

# 🗃️ Kansas Frontier Matrix — Notes Archive

`docs/notes/archive/README.md`

**Purpose:** Define how archived notes are preserved, indexed, and referenced in the
**Kansas Frontier Matrix (KFM)** — ensuring that even superseded or deprecated materials
retain full **provenance, traceability, and version control** under the **Master Coder Protocol (MCP)**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../architecture/knowledge-graph.md)
[![Archive Integrity](https://img.shields.io/badge/Archive-Immutable-orange)](README.md)

</div>

---

## 📚 Overview

The `/docs/notes/archive/` directory acts as a **long-term, read-only vault** for
past discussions, drafts, and design notes that have been superseded, finalized, or
rendered obsolete.

Archiving ensures **no loss of institutional memory** while keeping the active
notes directory clean and focused on current work.

Every archived note remains:

* 🔒 **Immutable** — content is not deleted or rewritten
* 🧾 **Versioned** — file commit history preserved in Git
* 🔗 **Linked** — to successor documents, datasets, or issues
* 🧠 **Indexed** — as part of the MCP knowledge graph for provenance queries

---

## 🗂️ Directory Layout

```text
docs/notes/archive/
├── README.md                # (this file)
├── 2024/                    # Archive by year (preferred structure)
│   ├── 2024-07-22_old_terrain_pipeline_draft.md
│   └── 2024-08-14_climate_data_ideas.md
├── 2025/
│   ├── 2025-01-10_meeting_notes_v1.md
│   └── 2025-05-03_ontology_discussion.md
└── legacy/                  # Misc pre-MCP materials (optional)
```

> 📘 **Tip:** Organize archives by **year folder**, prefix filenames with
> `YYYY-MM-DD_` for consistent ordering and provenance parsing.

---

## 🧾 Archival Process

### Step-by-step MCP-aligned workflow

| Step                    | Action                                                         | Responsibility       |
| :---------------------- | :------------------------------------------------------------- | :------------------- |
| **1️⃣ Identify**        | Note becomes outdated, merged, or promoted to a formal doc.    | Author or Maintainer |
| **2️⃣ Move**            | Move note to `docs/notes/archive/<year>/`.                     | Maintainer           |
| **3️⃣ Prefix Rename**   | Add date prefix `YYYY-MM-DD_` to preserve chronology.          | Maintainer           |
| **4️⃣ Update Metadata** | Edit YAML header with `status: archived` and `archived_date:`. | Author               |
| **5️⃣ Link Successor**  | Add pointer to new doc or replacement note.                    | Author               |
| **6️⃣ Commit & Push**   | Commit change with message: `"Archive note: <title>"`.         | Maintainer           |
| **7️⃣ Validate**        | CI checks YAML and cross-links.                                | CI/CD Workflow       |

---

## 🧱 YAML Metadata for Archived Notes

Each archived note should include a final metadata header:

```yaml
---
title: "LiDAR Pipeline Draft — Superseded"
author: "Data Integration Team"
original_path: "docs/notes/ideas.md"
status: archived
archived_date: 2025-10-05
reason: superseded           # superseded | duplicate | merged | complete | reference
linked_successor:
  - ../../architecture/data-architecture.md
tags: ["archive","history","data"]
---
```

**Metadata Guidelines**

| Field              | Description                     | Example                               |
| :----------------- | :------------------------------ | :------------------------------------ |
| `title`            | Original note title             | “Ontology Discussion v1”              |
| `original_path`    | Where the note originally lived | `docs/notes/ideas.md`                 |
| `archived_date`    | ISO 8601 format                 | `2025-10-05`                          |
| `reason`           | Why it was archived             | `superseded`, `duplicate`, `complete` |
| `linked_successor` | Path(s) to replacement document | `../integration/new_etl_plan.md`      |

> CI will verify all archived notes contain `status: archived`
> and a valid `archived_date` before merge.

---

## 🔗 Linking to the Knowledge Graph

Archived notes are **retained as historical provenance entities**
in the KFM Knowledge Graph with their lineage and successor relationships.

**Example RDF snippet:**

```turtle
@prefix kfm: <https://kfm.org/id/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dc: <http://purl.org/dc/terms/> .

kfm:note/2024_terrain_pipeline_draft
    a prov:Entity ;
    dc:title "Terrain Pipeline Draft — 2024" ;
    prov:invalidatedAtTime "2025-10-05T00:00:00Z"^^xsd:dateTime ;
    prov:wasDerivedFrom kfm:note/ideas_terrain_pipeline ;
    prov:wasInformedBy kfm:doc/data_architecture ;
    dc:description "Archived draft replaced by formal data architecture documentation." .
```

---

## 🧩 Archival Rules

| Rule                       | Description                                                                |
| :------------------------- | :------------------------------------------------------------------------- |
| **No Deletion**            | Notes are archived, never removed.                                         |
| **Immutable Content**      | Once archived, only metadata may be appended (e.g., successor links).      |
| **Cross-Linking Required** | Each note must link to its successor or formal doc.                        |
| **Yearly Rollup**          | Archive directories are versioned yearly (e.g., `/2024/`, `/2025/`).       |
| **Legacy Migration**       | Any pre-MCP notes moved under `/legacy/` with tags `["legacy","pre-MCP"]`. |

---

## 🧰 Example Archived Note

```markdown
---
title: "Meeting Notes — Data Schema Discussion"
author: "Metadata Governance Team"
original_path: "docs/notes/meetings.md"
status: archived
archived_date: 2025-03-15
reason: superseded
linked_successor:
  - ../../standards/metadata.md
---

# 🗓️ Archived Meeting — Data Schema Discussion (March 2025)

This note summarized early discussions around STAC field naming.  
Superseded by finalized schema in `docs/standards/metadata.md`.

*Decision:* Adopted `properties.description` for dataset summaries.  
*Archived:* 2025-03-15 by @metadata-team
```

---

## 🧠 CI Integration & Validation

Archived notes are automatically validated during CI/CD builds.

| Validation Type      | Tool                               | Enforcement                        |
| :------------------- | :--------------------------------- | :--------------------------------- |
| **YAML Syntax**      | `yamllint`                         | Required                           |
| **Status Check**     | `scripts/check_archived_status.py` | Ensures `status: archived` present |
| **Date Validation**  | `dateutil`                         | Confirms valid ISO timestamp       |
| **Cross-Link Check** | `remark-lint`                      | Verifies successor paths exist     |
| **Graph Ingestion**  | `scripts/graph_ingest_notes.py`    | Updates provenance in Neo4j        |

Example command:

```bash
make docs-validate
```

---

## 🧾 Governance Guidelines

* The **Documentation Lead** or **Maintainer** approves archive entries.
* All archive additions are peer-reviewed before merge.
* Archived notes count as part of the KFM **knowledge graph provenance record**.
* Periodic audits ensure consistency and link accuracy.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                      |
| :---------------------- | :-------------------------------------------------- |
| **Documentation-first** | Archived notes retain full history and metadata.    |
| **Reproducibility**     | Git version history + metadata ensure auditability. |
| **Open Standards**      | Markdown + YAML + RDF/Turtle used for portability.  |
| **Provenance**          | Linked to successors & stored in Knowledge Graph.   |
| **Auditability**        | CI checks guarantee metadata and linkage validity.  |

---

## 📎 Related Documentation

| File                                   | Description                                        |
| :------------------------------------- | :------------------------------------------------- |
| `docs/notes/README.md`                 | Active note workspace overview.                    |
| `docs/notes/templates/README.md`       | Templates for creating notes and archival records. |
| `docs/standards/documentation.md`      | Documentation and formatting standards.            |
| `docs/architecture/knowledge-graph.md` | How notes integrate into semantic models.          |

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                                                   |
| :------ | :--------- | :--------------------- | :---------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-05 | KFM Documentation Team | Initial archive management guide with metadata schema, validation rules, and RDF linkage. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Nothing Lost. Everything Proven.”*
📍 [`docs/notes/archive/README.md`](.) · Official MCP-compliant guide for archiving notes and preserving historical context.

</div>
