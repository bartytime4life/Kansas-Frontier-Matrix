<div align="center">

# 🧩 Kansas Frontier Matrix — **Notes Templates**  
`docs/notes/templates/README.md`

**Purpose:** Provide reusable **Markdown + YAML templates** for research notes, meeting records, brainstorming ideas, and backlog entries — ensuring every informal artifact in `/docs/notes/` is **structured, validated, searchable, MCP-DL v6.3–compliant**, and ready for ingestion into the **Kansas Frontier Matrix (KFM) Knowledge Graph**.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../standards/documentation.md)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../.github/workflows/policy-check.yml)
[![Site Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Site%20Build&logo=github)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

```yaml
---
title: "Kansas Frontier Matrix — Notes Templates"
document_type: "Templates"
version: "v2.1.0"
last_updated: "2025-10-18"
created: "2025-10-05"
owners: ["@kfm-docs","@kfm-architecture","@kfm-research","@kfm-governance","@kfm-security"]
status: "Stable"
maturity: "Production"
scope: "Docs/Notes/Templates"
license: "CC-BY 4.0"
semver_policy: "MAJOR.MINOR.PATCH"
tags: ["templates","notes","meetings","research","ideas","backlog","archive","provenance","governance","policy","a11y"]
audit_framework: "MCP-DL v6.3"
ci_required_checks:
  - docs-validate
  - site-build
  - policy-check
  - pre-commit
  - codeql
  - trivy
semantic_alignment:
  - PROV-O
  - CIDOC CRM
  - OWL-Time
  - SKOS
  - JSON Schema
  - ISO 8601
schema_index:
  note:        { file: "docs/schemas/note.schema.json",        version: "1.1.0" }
  idea:        { file: "docs/schemas/idea.schema.json",        version: "1.0.0" }
  backlog:     { file: "docs/schemas/backlog.schema.json",     version: "1.0.0" }
  meeting:     { file: "docs/schemas/meeting.schema.json",     version: "1.1.0" }
  research:    { file: "docs/schemas/research.schema.json",    version: "1.1.0" }
  archive:     { file: "docs/schemas/archive.schema.json",     version: "1.1.0" }
automation:
  - name: "Template Lint"
    schedule: "on-push"
    action: "tools/lint_templates.py"
  - name: "Template Sync → Graph"
    schedule: "0 6 * * MON"
    action: "tools/graph_ingest_notes.py"
ai_assist:
  summarize: false
  embed_in_graph: false
  classify: false
retention_policy:
  update_cycle: "Quarterly"
  archive_after: "18 months"
  purge_after: "48 months"
---
```

---

## 📚 Overview

These templates establish a **canonical format for informal documentation**—unifying research, collaboration, and creative work across the Kansas Frontier Matrix (KFM).  
Each template ensures your content can be parsed by machines, queried by humans, and preserved as part of **KFM’s long-term historical and technical provenance**.

Templates guarantee:

- 🧱 **Consistency** across all note types  
- 🔗 **Cross-linking** to datasets, code, and docs  
- 🧩 **YAML metadata** for traceable, auditable provenance  
- 🤖 **CI validation** & schema compliance  
- 🧠 **Knowledge Graph ingestion** using **PROV-O** and **CIDOC-CRM**

---

## 🗂️ Directory Layout

```text
docs/notes/templates/
├── README.md                    # (this file)
├── note_template.md             # General note / hypothesis
├── meeting_template.md          # Meeting & decision log
├── research_template.md         # Research summaries & reviews
├── backlog_template.md          # Task tracking / technical debt
├── archive_template.md          # Archiving & supersession record
└── idea_template.md             # Ideation / experimental concepts
```

---

## 🧭 Template Selection Flow

```mermaid
flowchart TD
    A["🧩 Need to document something?"] --> B["Is it exploratory or conceptual?"]
    B -->|Yes| C["Use idea_template.md"]
    B -->|No| D["Is it a research finding or literature review?"]
    D -->|Yes| E["Use research_template.md"]
    D -->|No| F["Is it a meeting, decision, or sprint note?"]
    F -->|Yes| G["Use meeting_template.md"]
    F -->|No| H["Is it a technical task or to-do?"]
    H -->|Yes| I["Use backlog_template.md"]
    H -->|No| J["Use note_template.md"]
    J --> K["Superseded? → archive_template.md"]
%% END OF MERMAID
```

---

## 🧩 Unified Metadata Reference

| Field | Applies To | Type | Description | Example |
| :-- | :-- | :-- | :-- | :-- |
| `id` | all | string | Unique identifier (`<prefix>-YYYY-NNN`) | `R-2025-001` |
| `title` | all | string | Document title | “Mapping Frontier Treaties” |
| `author` | all | string/array | Author or team handle | `@kfm-research` |
| `date` | note,research | date | ISO 8601 creation date | 2025-10-18 |
| `status` | all | enum | Lifecycle phase | `draft` |
| `priority` | backlog | enum | Task priority | `high` |
| `category` | research | enum | Research domain | `Ontology` |
| `type` | meeting | enum | Meeting classification | `governance` |
| `linked_docs` | all | array | Related docs | `docs/standards/...` |
| `linked_datasets` | research,note | array | STAC items / datasets | `data/stac/...` |
| `linked_commits` | all | array | Git SHAs | `["abc123"]` |
| `linked_ideas` | meeting,backlog | array | Ideas referenced | `I-2025-001` |
| `linked_backlog` | meeting,idea | array | Backlog items | `B-2025-004` |
| `linked_experiments` | research | array | Notebooks/experiments | `docs/experiments/...` |
| `summary` | all | string | Abstract for KG indexing | … |
| `ai_assist` | all | map | Summarization/embedding flags | `{ summarize: true }` |

---

## 📄 Template Catalog

```yaml
template_catalog:
  - id: T-001
    type: note
    file: "note_template.md"
    purpose: "General notes, ideas, and hypotheses."
  - id: T-002
    type: meeting
    file: "meeting_template.md"
    purpose: "Meeting documentation and decisions."
  - id: T-003
    type: research
    file: "research_template.md"
    purpose: "Scientific summaries and literature reviews."
  - id: T-004
    type: backlog
    file: "backlog_template.md"
    purpose: "Operational or technical tasks."
  - id: T-005
    type: idea
    file: "idea_template.md"
    purpose: "Brainstorming or innovation logs."
  - id: T-006
    type: archive
    file: "archive_template.md"
    purpose: "Record and preserve retired notes."
```

---

## 🧱 Core Template Components

1️⃣ **YAML Header** — defines metadata, links, and schema compliance  
2️⃣ **Markdown Body** — structured narrative content  
3️⃣ **CI Hooks** — validation (`yamllint`, `remark-lint`, `jsonschema`)  
4️⃣ **Graph Linkage** — PROV triples → Neo4j ingestion  

---

## 📘 Available Templates

Each template supports YAML schema validation, link checking, and graph ingestion.

- 🧩 **`note_template.md`** — General Notes & Hypotheses  
- 🗓️ **`meeting_template.md`** — Meetings & Decisions  
- 🔬 **`research_template.md`** — Research Summaries & Reviews  
- 🧱 **`backlog_template.md`** — Technical Tasks & Debt  
- 💡 **`idea_template.md`** — Conceptual & Exploratory Entries  
- 🗃️ **`archive_template.md`** — Closing or Superseding Notes

---

## 🔍 Linking Templates to the Knowledge Graph

**Example Triples**
```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dc:   <http://purl.org/dc/terms/> .
@prefix kfm:  <https://kfm.org/id/> .

kfm:note/N-2025-012
    a prov:Entity ;
    dc:title "LiDAR Pipeline Hypothesis" ;
    prov:wasAttributedTo kfm:agent/kfm-data ;
    prov:used kfm:dataset/ks_1m_dem_2018_2020 ;
    dc:date "2025-10-18"^^xsd:date .
```

**ER Graph Relationships**

```mermaid
erDiagram
    NOTE       ||--o{ DATASET : uses
    NOTE       ||--o{ DOCUMENT : references
    MEETING    ||--o{ DECISION : generates
    BACKLOG    ||--o{ ACTION   : tracks
    IDEA       ||--o{ NOTE     : inspires
    RESEARCH   ||--o{ DOCUMENT : cites
    ARCHIVE    ||--|| NOTE     : supersedes
%% END OF MERMAID
```

---

## 🧮 Metrics & Analytics

| Metric                | Source       | Target | Description                                  |
| :-------------------- | :----------- | :----- | :------------------------------------------- |
| Template usage (PRs)  | Git commits  | 100%   | Every informal doc uses a template           |
| Schema compliance     | CI results   | 100%   | Zero invalid YAML or missing fields          |
| Graph ingestion rate  | Neo4j        | ≥ 95%  | Notes successfully synced to the KG          |
| SKOS tag alignment    | Tag checker  | ≥ 98%  | Controlled vocabulary coverage (SKOS)        |

---

## ⚙️ Template Testing Framework

```bash
pytest tools/tests/test_templates.py
```

**Tests include**

- YAML loadability  
- Schema conformance  
- ISO 8601 date compliance  
- Tag vocabulary validation  
- Link resolution within repo

---

## 🧩 Automation & CLI Scaffolding

**CLI Tool**
```bash
python tools/new_note.py --type meeting --title "Ontology Sync" --author @kfm-docs
```

Generates a fully validated note with:

- Auto-incremented `id`  
- UTC `date`  
- Author from Git config  
- Correct schema + default links  

**Sample Output**
```bash
✔ Created docs/notes/meetings/M-2025-007.md
✔ Validated schema docs/schemas/meeting.schema.json
✔ Added to knowledge graph (Neo4j)
```

---

## 🔒 Security & Ethics

> Templates must **never** store credentials, raw PII, or restricted datasets.  
> Meeting recordings marked `internal` require ACL-managed links.  
> Sensitive coordinates or cultural data must follow Indigenous data sovereignty guidelines (see *Archaeology MCP Module*).  

---

## 🌐 Localization & Accessibility

Templates follow **WCAG 2.1 AA** and use plain technical English. For translated variants:

```yaml
language: en-US
alt_text: "Meeting notes template with accessible headings."
translation_available: ["es-ES","fr-FR"]
```

> Add translated templates under `docs/i18n/templates/` and reference in PR.

---

## 📊 Template Lifecycle & Roadmap

```mermaid
timeline
    title Template Evolution Roadmap
    2025-10 : v1.0 Initial Templates (YAML + CI)
    2026-01 : v1.3 Schema Unification + Validation Hooks
    2026-04 : v1.5 CLI Scaffolding
    2026-07 : v1.8 Domain Extensions (Climate, AI, Archaeology)
    2026-10 : v2.0 Full AI-driven Template Assistant
%% END OF MERMAID
```

---

## 🧠 Governance & Usage Guidelines

| Guideline             | Description                                         |
| :-------------------- | :-------------------------------------------------- |
| Template Consistency  | All informal docs must start from a template.       |
| Metadata Completeness | Missing YAML fields cause CI failure.               |
| Link Validity         | Internal links must resolve in-repo.                |
| Promotion & Archiving | Superseded notes archived; reproducible promoted.   |
| Provenance Enforcement| Each note links to a dataset, doc, or commit.       |

---

## 🤖 CI Validation Matrix

| Validation         | Tool / Path                    | Description                     |
| :----------------- | :----------------------------- | :------------------------------ |
| YAML syntax        | `yamllint`                     | Front-matter correctness        |
| Schema compliance  | `jsonschema`                   | Template-specific rules         |
| Link validation    | `remark-lint`                  | Internal link health            |
| Tag parsing        | `scripts/parse_tags.py`        | SKOS vocabulary sync            |
| Graph ingestion    | `tools/graph_ingest_notes.py`  | Adds entries to Neo4j           |
| Accessibility check| `scripts/check_a11y_headers.py`| Validates headings/contrast     |

**Run manually**
```bash
make docs-validate && make docs-lint
```

---

## 📎 Related Documentation

| File                                   | Description                                   |
| :------------------------------------- | :-------------------------------------------- |
| `docs/notes/README.md`                 | Notes workspace overview                      |
| `docs/notes/backlog.md`                | Operational backlog (tasks/actions)           |
| `docs/notes/ideas.md`                  | Idea repository for innovation                 |
| `docs/notes/research.md`               | Research ledger & findings                     |
| `docs/notes/meetings.md`               | Meetings & decisions log                       |
| `docs/standards/documentation.md`      | Documentation & writing standards              |
| `docs/standards/ontologies.md`         | CIDOC-CRM · PROV-O · OWL-Time · SKOS alignment |
| `docs/architecture/knowledge-graph.md` | Knowledge graph ingestion & linkage semantics  |

---

## 🚀 Future Roadmap

| Milestone | Target | Description                                       |
| :-------- | :----- | :------------------------------------------------ |
| v2.1      | Q1 2026| Interactive template editor in KFM web UI         |
| v2.2      | Q2 2026| Automated documentation scaffolding (GH Action)   |
| v2.3      | Q3 2026| Domain-specific extensions (Climate, AI, Arch.)   |
| v2.4      | Q4 2026| Template analytics dashboard (Grafana/Bloom)      |

---

## 📅 Version History

| Version | Date       | Author     | Summary                                                                 |
| :------ | :--------- | :--------- | :---------------------------------------------------------------------- |
| **v2.1.0** | 2025-10-18 | @kfm-docs  | Alignment with policy checks, added a11y script, expanded owners, and clarified testing. |
| v2.0.0  | 2025-10-18 | @kfm-docs  | Added schema catalog, CLI scaffolding, metadata index, AI readiness, accessibility, metrics. |
| v1.5.0  | 2025-10-17 | @kfm-docs  | ER/flow diagrams, unified schema integration, validation framework.     |
| v1.0.0  | 2025-10-05 | @kfm-docs  | Initial release with YAML metadata + CI integration.                    |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Idea Structured. Every Note Traceable.”*  
📍 `docs/notes/templates/README.md` · Maintained under MCP-DL v6.3 governance and CI validation.

</div>
