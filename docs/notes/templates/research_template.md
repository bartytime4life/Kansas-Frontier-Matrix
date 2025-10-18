<div align="center">

# 🔬 Kansas Frontier Matrix — **Research Note Template**  
`docs/notes/templates/research_template.md`

**Purpose:** Provide a formal structure for documenting **research findings, experiments, literature reviews, or data analyses** within the **Kansas Frontier Matrix (KFM)**.  
Every research note created from this template is **FAIR-aligned**, **MCP-DL v6.3–compliant**, and automatically ingested into the **Knowledge Graph** as a `prov:Entity`.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../standards/documentation.md)
[![Docs Validated](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../.github/workflows/policy-check.yml)
[![Knowledge Graph](https://img.shields.io/badge/Linked-Knowledge%20Graph-green)](../../architecture/knowledge-graph.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

```yaml
---
id: R-YYYY-NNN
title: "<Research Title>"
author: "@kfm-research"
date: 2025-10-18
status: draft                # draft | in-review | published | archived
category: "Ontology"         # Archaeology | Climate | Hydrology | Geospatial | NLP | AI/ML | Data Modeling
tags: ["research","analysis","ontology","mcp","provenance"]
linked_docs:
  - ../../standards/documentation.md
linked_datasets:
  - ../../data/stac/terrain/ks_1m_dem_2018_2020.json
linked_experiments:
  - ../../docs/experiments/example_experiment.md
linked_commits:
  - e9a45b2
linked_meetings:
  - ../../docs/notes/meetings.md#M-2025-010
summary: >
  Concise description of the research scope and its purpose within KFM.
  Used for AI indexing, search, and provenance records.
ai_assist:
  summarize: true
  embed_in_graph: true
  vector_model: "sentence-transformers/all-MiniLM-L6-v2"
period_context:
  id: "perio.do/mcp-research-phase-2025"
  label: "MCP Research Integration Phase"
license: "CC-BY 4.0"
---
```

---

## 🧭 Context

Describe **why this research was conducted**, what questions it addresses, and its relevance to the Kansas Frontier Matrix ecosystem.  
Include any previous work or legacy notes that this builds upon.

> Example:  
> “This research explores the alignment of archaeological field records with FAIR metadata schemas under MCP-DL v6.3.”

---

## 🧩 Objectives

Clearly outline the **goals or hypotheses**:
- What is being tested or evaluated?
- How does it support KFM’s reproducibility or data integrity standards?
- What are the expected outcomes?

---

## ⚙️ Methodology

Describe **data sources, workflows, and validation techniques** used.

| Component | Tool / Standard | Description |
| :-- | :-- | :-- |
| ETL | Python / GDAL / Pandas | Data processing scripts |
| Validation | JSON Schema / STAC | Metadata compliance |
| Analysis | Jupyter / R / AI model | Statistical or ML approach |
| Provenance | PROV-O / CIDOC CRM | Lineage and reproducibility tracking |

**Code Example:**
```python
import pandas as pd
df = pd.read_csv("data/processed/hydrology_flow.csv")
print(df.describe())
```

---

## 🧠 Results & Findings

Summarize **what was discovered or demonstrated**.
- Highlight quantitative or qualitative results.
- Provide summary tables or figures when appropriate.

| Metric | Result | Description |
| :-- | :-- | :-- |
| Correlation | 0.83 | DEM-derived flow accumulation vs. NHD baseline |
| Runtime | 2h 13m | Processing efficiency benchmark |
| Validation | ✅ 100% | Schema and checksum verification passed |

---

## 🧮 Analysis & Discussion

Interpret the findings:
- How do results support or contradict hypotheses?
- What implications arise for data architecture or ontology design?
- Note unresolved questions or potential next steps.

> Example:
> “The analysis confirms the feasibility of cross-linking CIDOC CRM and STAC entities for temporal event mapping.”

---

## 🔗 Related Work & Literature

| Reference | Description |
| :-- | :-- |
| `docs/architecture/data-architecture.md` | Reference architecture influencing the analysis |
| `docs/standards/metadata.md` | Schema and FAIR validation procedures |
| [CIDOC CRM v7.1](https://www.cidoc-crm.org/) | Core ontology for cultural and historical events |

---

## 🧾 Provenance (RDF/Turtle)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix crm:  <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix dc:   <http://purl.org/dc/terms/> .
@prefix kfm:  <https://kfm.org/id/> .

kfm:research/R-2025-001
    a prov:Entity, crm:E31_Document ;
    dc:title "Hydrology Flow Validation Study" ;
    prov:wasGeneratedBy kfm:activity/hydrology_validation_etl ;
    prov:used kfm:dataset/usgs_streamflow_ks_1900_2020 ;
    prov:wasAttributedTo kfm:agent/kfm-research ;
    dc:date "2025-10-18"^^xsd:date ;
    dc:description "Research note validating hydrological flow accumulation models under FAIR governance." .
```

---

## 📊 FAIR & MCP Compliance

| Principle | Implementation |
| :-- | :-- |
| **Findable** | Indexed via Neo4j graph and Zenodo export |
| **Accessible** | Open data and document access via GitHub |
| **Interoperable** | PROV-O, CIDOC CRM, and JSON Schema alignment |
| **Reusable** | CC-BY 4.0 license, detailed methods, validated results |

---

## ✅ Checklist Before Submission

| Validation | Requirement |
| :-- | :-- |
| ✅ YAML syntax passes `yamllint` |
| ✅ Schema passes `research.schema.json` |
| ✅ FAIR validation complete |
| ✅ Linked docs/datasets resolve correctly |
| ✅ No sensitive or restricted data included |
| ✅ Summary ≤ 3 sentences |
| ✅ Code snippets anonymized or reproducible |

---

## 🤖 Validation Commands

```bash
make docs-validate
pytest tools/tests/test_templates.py -k research
```

---

## 📎 Related Templates

| Template | Purpose |
| :-- | :-- |
| [`note_template.md`](note_template.md) | For general notes or hypotheses |
| [`idea_template.md`](idea_template.md) | For conceptual or early-stage ideas |
| [`archive_template.md`](archive_template.md) | For archiving research when superseded |

---

## 📅 Version History

| Version | Date | Author | Summary |
| :-- | :-- | :-- | :-- |
| v1.0.0 | 2025-10-18 | @kfm-docs | Initial research template with FAIR schema, provenance model, and validation workflow integration. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Experiment Logged. Every Result Proven.”*  
📍 `docs/notes/templates/research_template.md` · Maintained under MCP-DL v6.3 governance and FAIR research standards.

</div>
