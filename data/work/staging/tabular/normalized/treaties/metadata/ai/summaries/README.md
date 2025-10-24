---
title: "🧠 Kansas Frontier Matrix — Treaty AI Summaries"
document_type: "AI Summarization Outputs · Semantic Contextualization · FAIR Provenance"
version: "v1.1.0"
last_updated: "2025-10-27"
status: "Production · FAIR+CARE+ISO Aligned"
maturity: "Stable"
license: ["MIT (scripts)", "CC-BY 4.0 (text summaries)"]
owners: ["@kfm-ai","@kfm-data","@kfm-ethics"]
reviewers: ["@kfm-architecture","@kfm-qa"]
tags: ["kfm","treaties","ai","summarization","nlp","graph","cidoc-crm","owl-time","prov-o","fair","care","mcp","neo4j","stac","focus-mode","hxi"]
alignment:
  - MCP-DL v6.4.3
  - FAIR / CARE
  - CIDOC CRM / OWL-Time / PROV-O
  - ISO 9001 / ISO 19115
  - WCAG 2.1 AA (content a11y metadata)
validation:
  ci_enforced: true
  summarization_quality: "ROUGE ≥ 0.85"
  factual_accuracy: "≥ 0.90 human-verified"
  checksum_verify: true
  provenance_chain: true
observability:
  endpoint: "https://metrics.kfm.ai/ai-treaty-summaries"
  dashboard: "https://metrics.kfm.ai/grafana/ai-treaty-summaries"
  metrics: ["summary_count","avg_length_tokens","rouge_score","factual_consistency_score","graph_link_rate","bias_flag_rate","rollback_events"]
preservation_policy:
  replication_targets: ["GitHub Releases","Zenodo DOI (major)"]
  checksum_algorithm: "SHA-256"
  retention: "permanent (summaries embedded in graph + exported in JSON-LD)"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/README.md"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Treaty AI Summaries (v1.1.0 · FAIR + CARE + ISO Aligned)**  
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
| Model Card | Datasheet + limitations for summarizer | `models/kfm_treaty_summary_v1/MODEL_CARD.md` |
| CIDOC CRM | Conceptual grounding (`E31 Document`) | `docs/standards/ontologies.md` |
| PROV-O | Tracks provenance (agent, activity, entity) | `provenance.jsonld` |
| Graph Linkage | Inserts summaries into Neo4j (`HAS_SUMMARY`) | `src/graph/upsert_summary.cql` |
| Focus Mode | Uses summaries as context chips | `.../graph/cypher/create_focus_edges.cql` |
| STAC | Catalogs exports | `data/stac/treaties/` |

---

## 🗂️ Directory Layout
```

summaries/
├── treaty_1851_fort_laramie_summary.json       # AI-generated summary + metadata
├── treaty_1867_medicine_lodge_summary.json     # Summary for Medicine Lodge Treaty
├── treaty_1868_little_arkansas_summary.json    # Additional treaty summary
├── golden_set/                                 # Human-authored gold refs for QA
│   ├── golden_medicine_lodge.md
│   └── rubric.yaml
├── prompts/                                    # Prompt templates & controls
│   ├── summarization_prompt.md
│   └── safety_instructions.md
├── model_metadata.yaml                         # Model config, parameters, dataset lineage
├── validation_report.json                      # ROUGE, factuality, bias audits
├── provenance.jsonld                           # PROV-O description of summary generation
└── README.md                                   # You are here

````

---

## 🔄 Workflow
```mermaid
flowchart TD
A["Input: Treaty Text + Entities (NER)"] --> B["AI Summarization Model · kfm_treaty_summary_v1"]
B --> C["Post-process: Fact Validation · Ethical Screening · A11y check"]
C --> D["Output JSON (summary + metadata · checksums)"]
D --> E["Neo4j Link (HAS_SUMMARY) · Focus chips"]
E --> F["FAIR Export: JSON-LD · STAC Item"]
````

### Command Example

```bash
python src/ai/nlp/summarizer.py \
  --input data/work/staging/tabular/normalized/treaties/raw/treaty_1867_medicine_lodge.txt \
  --output data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/treaty_1867_medicine_lodge_summary.json \
  --model models/kfm_treaty_summary_v1 --max_tokens 300 --temperature 0.2
```

---

## 🧾 Summary JSON Schema (local contract)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Treaty Summary",
  "type": "object",
  "required": ["id","model","created","linked_treaty","text","entities","metrics","provenance"],
  "properties": {
    "id": {"type": "string"},
    "model": {"type": "string"},
    "created": {"type": "string","format":"date-time"},
    "language": {"type":"string","enum":["en","es","fr"]},
    "linked_treaty": {"type":"string"},
    "text": {"type":"string","minLength": 60, "maxLength": 2500},
    "entities": {
      "type":"object",
      "properties":{
        "places":{"type":"array","items":{"type":"string"}},
        "people":{"type":"array","items":{"type":"string"}},
        "groups":{"type":"array","items":{"type":"string"}}
      }
    },
    "metrics": {
      "type":"object",
      "properties":{
        "rouge": {"type":"number","minimum":0,"maximum":1},
        "factual_accuracy": {"type":"number","minimum":0,"maximum":1},
        "bias_flags": {"type":"array","items":{"type":"string"}}
      }
    },
    "provenance": {
      "type":"object",
      "required": ["commit","ledger_tx","input_checksum"],
      "properties":{
        "commit":{"type":"string"},
        "ledger_tx":{"type":"string"},
        "input_checksum":{"type":"string"},
        "reviewed_by":{"type":"string"}
      }
    }
  }
}
```

---

## 🔗 Graph Linking (Cypher)

```cypher
// ensure Summary node & linkage
MERGE (t:Treaty {id:$treaty_id})
MERGE (s:Summary {id:$summary_id})
SET s.text = $text,
    s.model = $model,
    s.created = datetime($created),
    s.language = coalesce($language,'en'),
    s.rouge = $rouge,
    s.factual_accuracy = $factual_accuracy
MERGE (t)-[:HAS_SUMMARY]->(s);
```

---

## 🧱 STAC Item (example)

```yaml
type: Feature
stac_version: "1.0.0"
id: "summary_treaty_1867_medicine_lodge"
properties:
  datetime: "1867-10-21T00:00:00Z"
  kfm:entity: "Summary"
  kfm:linked_treaty: "treaty_1867_medicine_lodge"
  kfm:model: "kfm_treaty_summary_v1"
assets:
  json:
    href: "./treaty_1867_medicine_lodge_summary.json"
    type: "application/json"
    roles: ["metadata","description"]
```

---

## 🧑‍⚖️ Human-in-the-Loop (HITL) Review

**Reviewer rubric (golden_set/rubric.yaml):**

* Accuracy (0–5), Neutrality (0–5), Clarity (0–5), Respect/CARE (0–5), Evidence-linked (0–5)
  **Workflow**

1. AI draft →
2. Automatic checks (facts, bias scanners, entity alignment) →
3. Human review (rubric + edits) →
4. Approve → publish & link →
5. Log ledger TX + checksums

**Rollback**

* If *post-publication* issues found, create `supersedes` link and mark prior summary `deprecated:true` (never delete published text).

---

## 🧠 Prompt Template (prompts/summarization_prompt.md)

```
Instruction: Summarize the treaty neutrally and succinctly (150–280 words).  
Include: purpose, parties, geographic scope, date(s), key outcomes.  
Do not speculate. Cite places/people/groups as found in text.  
Style: respectful, non-judgmental, past tense.  
Output fields: text only.
Controls: temperature=0.2, max_tokens=300, stop=["\n\n###"].
```

**Safety addendum (prompts/safety_instructions.md)**

* Avoid stereotypes; flag ambiguous attributions; include uncertainty markers if sources conflict.

---

## 🧮 Observability Metrics

| Metric             | Target        | Current | Verified | Source                 |
| :----------------- | :------------ | :------ | :------- | :--------------------- |
| Avg Summary Length | 150–300 words | 212     | ✅        | CI                     |
| ROUGE Score        | ≥ 0.85        | 0.91    | ✅        | validation_report.json |
| Factual Accuracy   | ≥ 0.90        | 0.96    | ✅        | reviewer rubric        |
| Graph Link Rate    | 100%          | 100%    | ✅        | Neo4j                  |
| Bias Flag Rate     | 0% critical   | 0%      | ✅        | bias scanner           |
| Rollback Events    | 0             | 0       | ✅        | ledger audit           |

---

## 🔐 Security · Ethics · A11y

* **CARE**: culturally respectful phrasing; no sensitive personal data; consult tribal sources where possible.
* **A11y**: summaries tagged with language; reading level ~9–11th grade; alt-text where images are referenced in UIs.
* **Licensing**: summaries CC-BY 4.0; cite original sources when excerpted.

---

## 🧾 FAIR Metadata Summary

| Field        | Value                                     |
| :----------- | :---------------------------------------- |
| Dataset      | Treaty AI Summaries                       |
| Model        | `kfm_treaty_summary_v1`                   |
| Ontologies   | CIDOC CRM (`E31 Document`), PROV-O        |
| Checksum     | SHA-256 per file                          |
| License      | CC-BY 4.0                                 |
| Review Cycle | AI-generated → Human reviewed → Published |
| Provenance   | Linked to Neo4j and ledger receipts       |
| Retention    | Permanent (graph-linked nodes)            |

---

## 🧰 Make Targets & CI

```
make ai-summaries-generate        # batch generation
make ai-summaries-validate        # metrics + schema + bias checks
make ai-summaries-publish         # write to repo + link to graph + STAC update
make ai-summaries-rollback ID=... # create supersession record
```

CI jobs: `ai-summaries.yml` (generate/validate), `graph-link.yml` (link), `stac-publish.yml` (catalog).

---

## 🧱 Standards & Compliance

* ✅ **MCP-DL v6.4.3** — documentation-first, reproducible generation
* ✅ **FAIR + CARE** — ethical, accessible data publishing
* ✅ **CIDOC CRM / PROV-O / OWL-Time** semantic annotation
* ✅ **ISO 9001 / 19115** metadata completeness
* ✅ **AI Governance** — bias & hallucination audit, provenance ledger linking

---

## 📘 Related Documentation

* [AI Graph Cypher Scripts](../graph/cypher/README.md)
* [Graph Exports](../graph/exports/README.md)
* [Graph Snapshots](../graph/snapshots/README.md)
* [AI System Developer Guide](../../../../../../../../../docs/architecture/ai-system.md)
* [Ethics & AI Policy](../../../../../../../../../docs/standards/ai-ethics.md)
* [Focus Mode Design](../../../../../../../../../docs/design/focus-mode.md)

---

## 🕓 Version History

| Version    | Date       | Author  | Reviewer          | Notes                                                        |
| :--------- | :--------- | :------ | :---------------- | :----------------------------------------------------------- |
| **v1.1.0** | 2025-10-27 | @kfm-ai | @kfm-architecture | Added schema, prompts, HITL rubric, STAC item, rollback & CI |
| v1.0.0     | 2025-10-27 | @kfm-ai | @kfm-architecture | Initial AI summary pipeline (FAIR + CARE + provenance)       |

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
