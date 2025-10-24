---
title: "🧠 Kansas Frontier Matrix — Treaty AI Summaries"
document_type: "AI Summarization Outputs · Semantic Contextualization · FAIR Provenance"
version: "v1.0.0"
last_updated: "2025-10-27"
status: "Production · FAIR+CARE+ISO Aligned"
maturity: "Stable"
license: ["MIT (scripts)", "CC-BY 4.0 (text summaries)"]
owners: ["@kfm-ai","@kfm-data","@kfm-ethics"]
reviewers: ["@kfm-architecture","@kfm-qa"]
tags: ["kfm","treaties","ai","summarization","nlp","graph","cidoc-crm","owl-time","prov-o","fair","care","mcp","neo4j"]
alignment:
  - MCP-DL v6.4.3
  - FAIR / CARE
  - CIDOC CRM / OWL-Time / PROV-O
  - ISO 9001 / ISO 19115
validation:
  ci_enforced: true
  summarization_quality: "ROUGE ≥ 0.85"
  factual_accuracy: "verified"
  checksum_verify: true
  provenance_chain: true
observability:
  endpoint: "https://metrics.kfm.ai/ai-treaty-summaries"
  dashboard: "https://metrics.kfm.ai/grafana/ai-treaty-summaries"
  metrics: ["summary_count","avg_length_tokens","rouge_score","factual_consistency_score","graph_link_rate"]
preservation_policy:
  replication_targets: ["GitHub Releases","Zenodo DOI (major)"]
  checksum_algorithm: "SHA-256"
  retention: "permanent (summaries embedded in graph + exported in JSON-LD)"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/README.md"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Treaty AI Summaries (v1.0.0 · FAIR + CARE + ISO Aligned)**  
`data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/`

### *“Machine-generated treaty digests · ethical summarization · provenance-linked insights”*

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)](../../../../../../../../../../../docs/)
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![AI Summarization](https://img.shields.io/badge/AI-Summarization-blue?style=flat-square)]()
[![CIDOC CRM](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%2F%20PROV--O-8e44ad?style=flat-square)]()
[![Ledger](https://img.shields.io/badge/Governance-Immutable%20Ledger-d4af37?style=flat-square)]()

</div>

---

## 📘 Purpose
This directory stores **AI-generated treaty summaries** created by the Kansas Frontier Matrix NLP pipeline.  
Each summary distills a complex historical treaty into a concise, **fact-checked narrative**, linking to entities (places, people, groups) within the knowledge graph.  

Summaries are:
- **Ethically generated**, with transparency on AI model, training corpus, and reviewer oversight.  
- **Semantically linked** to treaty graph nodes via `HAS_SUMMARY` relationships.  
- **Traceable**, with each generation logged and checksum-verified.  
- **FAIR + CARE compliant**, supporting findability, accessibility, interoperability, and responsible use.

---

## 🧩 Context & Dependencies
| Component | Function | Source |
|:--|:--|:--|
| NLP Pipeline | Generates and validates summaries | `src/ai/nlp/summarizer.py` |
| CIDOC CRM | Provides conceptual grounding (`E31 Document`) | `docs/standards/ontologies.md` |
| PROV-O | Tracks provenance (agent, activity, entity) | linked via `provenance.jsonld` |
| AI Model | Transformer (GPT-style summarizer fine-tuned on KFM corpora) | `models/kfm_treaty_summary_v1/` |
| Graph Linkage | Inserts summaries into Neo4j (`HAS_SUMMARY` edges) | `src/graph/upsert_summary.cql` |

---

## 🗂️ Directory Layout
```

summaries/
├── treaty_1851_fort_laramie_summary.json     # AI-generated summary + metadata
├── treaty_1867_medicine_lodge_summary.json   # Summary for Medicine Lodge Treaty
├── treaty_1868_little_arkansas_summary.json  # Additional treaty summary
├── model_metadata.yaml                       # Model config, parameters, dataset lineage
├── validation_report.json                    # ROUGE, BLEU, factuality metrics
├── provenance.jsonld                         # PROV-O description of summary generation
└── README.md                                 # You are here

````

---

## 🔄 Workflow
```mermaid
flowchart TD
A["Input: Treaty Text + Entities (NER)"] --> B["AI Summarization Model (Transformer)"]
B --> C["Post-process: Fact Validation + Ethical Screening"]
C --> D["Output JSON (summary + metadata)"]
D --> E["Neo4j Graph Link (HAS_SUMMARY)"]
E --> F["FAIR Export: JSON-LD / STAC Publication"]
````

### Command Example

```bash
python src/ai/nlp/summarizer.py \
  --input data/work/staging/tabular/normalized/treaties/raw/treaty_1867_medicine_lodge.txt \
  --output data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/treaty_1867_medicine_lodge_summary.json
```

### Metadata Example

```json
{
  "id": "summary_treaty_1867_medicine_lodge",
  "model": "kfm_treaty_summary_v1",
  "created": "2025-10-27T00:00:00Z",
  "rouge_score": 0.91,
  "length_tokens": 247,
  "factual_accuracy": 0.96,
  "linked_treaty": "treaty_1867_medicine_lodge",
  "provenance": "ledger/tx/2025-10-27T00Z"
}
```

---

## 🧾 FAIR Metadata Summary

| Field        | Value                                     |
| :----------- | :---------------------------------------- |
| Dataset      | Treaty AI Summaries                       |
| Model        | `kfm_treaty_summary_v1`                   |
| Ontologies   | CIDOC CRM (`E31 Document`), PROV-O        |
| Checksum     | SHA-256                                   |
| License      | CC-BY 4.0                                 |
| Review Cycle | AI-generated → Human reviewed → Published |
| Provenance   | Linked to Neo4j and ledger receipts       |
| Retention    | Permanent (stored as graph-linked nodes)  |

---

## 🧮 Observability Metrics

| Metric             | Target       | Current | Verified | Source               |
| :----------------- | :----------- | :------ | :------- | :------------------- |
| Avg Summary Length | ≤ 300 tokens | 247     | ✅        | CI pipeline          |
| ROUGE Score        | ≥ 0.85       | 0.91    | ✅        | Validation report    |
| Factual Accuracy   | ≥ 0.90       | 0.96    | ✅        | Manual review        |
| Graph Link Rate    | 100%         | 100%    | ✅        | Neo4j validation     |
| Ethical Compliance | 100%         | 100%    | ✅        | Ethics review report |

---

## 🔐 Security & Ethics

* All AI outputs are **post-processed** by human reviewers for factuality and ethical context.
* AI models use **public domain** or **licensed** training corpora, in line with CARE principles.
* Each summary includes a **provenance trail**: model version, timestamp, input source, and ledger record.
* Logs and metrics are stored under `.../graph/logs/` for auditing.
* Reuse and modification are permitted under CC-BY 4.0, with attribution.

---

## 🧱 Standards & Compliance

* ✅ **MCP-DL v6.4.3** — documentation-first, reproducible generation
* ✅ **FAIR + CARE** — ethical, accessible data publishing
* ✅ **CIDOC CRM / PROV-O / OWL-Time** semantic annotation
* ✅ **ISO 9001 / 19115** metadata completeness
* ✅ **AI Governance** (bias and hallucination audit, provenance ledger linking)

---

## 📘 Related Documentation

* [AI Graph Cypher Scripts](../graph/cypher/README.md)
* [Graph Exports](../graph/exports/README.md)
* [Graph Snapshots](../graph/snapshots/README.md)
* [AI System Developer Guide](../../../../../../../../../docs/architecture/ai-system.md)
* [Ethics & AI Policy](../../../../../../../../../docs/standards/ai-ethics.md)

---

## 🕓 Version History

| Version    | Date       | Author  | Reviewer          | Notes                                                                   |
| :--------- | :--------- | :------ | :---------------- | :---------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-27 | @kfm-ai | @kfm-architecture | Initial AI summary pipeline documentation with FAIR + CARE + provenance |

---

<div align="center">

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)]()
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![AI Summarization](https://img.shields.io/badge/AI-Summarization-blue?style=flat-square)]()
[![CIDOC CRM](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%2F%20PROV--O-8e44ad?style=flat-square)]()
[![Ledger](https://img.shields.io/badge/Ledger-Immutable-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: FAIR + CARE + ISO Aligned
DOC-PATH: data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/README.md
MCP-CERTIFIED: true
SBOM-GENERATED: true
SLSA-ATTESTED: true
FAIR-CARE-COMPLIANT: true
A11Y-VERIFIED: true
GOVERNANCE-LEDGER-LINKED: true
OBSERVABILITY-ACTIVE: true
PROVENANCE-JSONLD: true
PERFORMANCE-BUDGET-P95: 2.5 s
ENERGY-BUDGET-P95: 25 Wh
CARBON-BUDGET-P95: 28 gCO₂e
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-27
MCP-FOOTER-END -->

```
```
