<div align="center">

# 🤖 Kansas Frontier Matrix — **Review Log: AI/ML Model Validation**  
`docs/integration/reviews/logs/2025-10-06_ai-model-validation.md`

**Mission:** Record a complete, reproducible, and machine-readable **audit log** for an AI/ML model integrated into the  
**Kansas Frontier Matrix (KFM)** — validating training/data provenance, metrics, bias & ethics, security posture, ontology mapping,  
and end-to-end interoperability with the **graph · timeline · Focus Mode** per **MCP-DL v6.3**.

[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../../../.github/workflows/policy-check.yml)
[![Security · CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Security · Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../.github/workflows/trivy.yml)
[![Aligned · CIDOC · OWL-Time · PROV-O](https://img.shields.io/badge/Aligned-CIDOC%20CRM%20%7C%20OWL--Time%20%7C%20PROV--O-green)](../../../metadata-standards.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

```yaml
---
model: frontier_ner_v3
review_type: model
reviewers:
  - ai_engineer_x
  - ontology_specialist_y
status: approved
validation:
  metrics:
    precision: 0.92
    recall: 0.90
    f1: 0.91
  reproducibility: pass
  bias_audit: documented
  security_scan: pass
  documentation_card: present
  license: CC-BY-4.0
  hash: "ef34abcd1234ef34abcd1234ef34abcd1234ef34abcd1234ef34abcd1234ef34" # SHA-256 of model artifact
notes: |
  • Model: Named-Entity Recognition for historical Kansas corpora (treaties, newspapers, diaries).
  • Labels: {PERSON, ORG, GPE, DATE} + custom {TRIBE, TREATY, RIVER, PLACE}.
  • Training Data: Annotated treaty texts (Kappler), OCR'd historic newspapers (1850–1900), KHS documents.
    Dataset cards & licenses listed in `docs/model_card.md`.
  • Pipeline: `src/models/train_ner.py` (seed=42), preprocessing `src/etl/ner_preprocess.py`.
  • Container: `ghcr.io/bartytime4life/kfm-ner:v3.1.0` (reproducible; digest pinned in SBOM).
  • Evaluation: Held-out 10k sentences; macro-F1=0.91. Category F1 — TRIBE:0.89, PLACE:0.93, TREATY:0.92.
  • Interop: Output entities map to graph via `scripts/graph_ingest.py` (E74_Group, E31_Document, E53_Place, E52_Time-Span).
  • UI Integration: Focus Mode indexing enabled; confidences exported (H/M/L) to drive sidebar cues.
  • Security: CodeQL & Trivy clean for critical/high; actions & images pinned; SBOM attached.
  • Ethics: No PII used; cultural sensitivity cautions documented; usage limited to research/visualization.
commit: b4c5d6e
timestamp: 2025-10-06T14:22:00Z
linked_templates:
  - ../templates/model_review_template.md
  - ../checklist.md
---
````

---

## 🧩 Reviewer Notes

**AI Engineer X**

* Training environment locked via `environment.yml`; deterministic seed; reproducible container build hash recorded.
* Metrics exceed previous baseline (v3.0.2 F1=0.88 → v3.1.0 F1=0.91). Regression tests added to CI.

**Ontology Specialist Y**

* Verified mappings: “Kaw Nation” → `E74 Group`; “Treaty with the Kansa (1825)” → `E31 Document` + `E65 Creation`;
  cession interval → `E52 Time-Span`; signing place → `E53 Place`.
* Add SKOS concept for **Neutral Lands** (Cherokee) and map as controlled term; patch prepared.

### Actions

* ✅ Add SKOS term: `skos:Concept Neutral_Lands` and cross-link to `E53 Place`.
* ✅ Schedule data augmentation for under-represented tribes (3–5% F1 gap).
* ✅ Tag release `frontier_ner_v3` → v3.1.0; prepare v3.2.0 milestone for augmentation work.

---

## 📎 Supporting Artifacts

| Artifact           | Location                                      | Description                                      |
| :----------------- | :-------------------------------------------- | :----------------------------------------------- |
| **Model Card**     | `docs/model_card.md`                          | Intended use, data sources, ethics, limitations. |
| **SBOM (SPDX)**    | `logs/sbom_ner_v3.1.0.json`                   | Supply chain inventory for the model container.  |
| **CodeQL Report**  | `logs/codeql_scan_ner_v3_2025-10-06.sarif`    | Security static analysis output.                 |
| **Trivy SCA**      | `logs/trivy_sca_ner_v3.1.0.json`              | Dependency vulnerability scan.                   |
| **Training Log**   | `logs/train_log_ner_v3_2025-10-06.txt`        | Reproducibility evidence & metrics.              |
| **Eval Report**    | `logs/evaluate_ner_v3_2025-10-06.json`        | Per-label precision/recall/F1.                   |
| **Ontology Patch** | `logs/ontology_mapping_patch_ner_v3.1.0.diff` | Adds Neutral Lands concept + mapping.            |

---

## 🧮 Validation Summary

| Layer            | Tool / Method                    | Result           |
| :--------------- | :------------------------------- | :--------------- |
| Metrics          | `src/models/evaluate_ner.py`     | ✅ Pass (F1=0.91) |
| Reproducibility  | Docker digest + fixed seed       | ✅ Pass           |
| Bias & Fairness  | Bias audit section in model card | ✅ Documented     |
| Security         | CodeQL + Trivy SCA               | ✅ Pass           |
| Ontology Mapping | Graph ingest dry-run             | ✅ Pass           |
| Documentation    | `make docs-validate`             | ✅ Pass           |

---

## 🧠 Provenance & Semantic Record

| Ontology      | Class / Property      | Mapping                                              |
| :------------ | :-------------------- | :--------------------------------------------------- |
| **CIDOC CRM** | `E31 Document`        | Model card record                                    |
|               | `E39 Actor`           | “AI Engineer X”, “Ontology Specialist Y” (reviewers) |
|               | `E7 Activity`         | Training session v3.1.0                              |
| **OWL-Time**  | `time:Interval`       | 2025-10-01/2025-10-06 (training window)              |
| **PROV-O**    | `prov:wasDerivedFrom` | Treaty texts, KHS OCR, curated annotations           |
| **DCAT 2.0**  | `dcat:Dataset`        | Model artifact registration & metadata               |
| **STAC 1.0**  | `stac:item`           | Pointer to model card JSON (if exported)             |

---

## 🔐 Compliance & Governance

| Policy              | Check                                                          | Result |
| :------------------ | :------------------------------------------------------------- | :----- |
| **MCP-DL v6.3**     | Documentation-first; deterministic build; provenance present   | ✅      |
| **Open License**    | CC-BY-4.0 for model card/code; data licenses recorded          | ✅      |
| **Audit Record**    | This log indexed in `audit-index.json`                         | ✅      |
| **Ethics & Access** | No PII; cultural sensitivity handled; research-only usage note | ✅      |
| **Retention**       | Repo persistent + Zenodo/OSF replication pipeline              | ✅      |

---

## 🧮 Decision Summary

☑ **Approved** — model validated, documented, security-screened, and **Focus Mode**–ready.
Integration into the pipeline and graph is authorized (release v3.1.0). Next milestone v3.2.0 will target bias mitigation via data augmentation.

---

## 🔗 References

* `docs/model_card.md` — Model Card & ethics/bias notes
* `docs/architecture/ai-system.md` — KFM AI/ML architecture & pipelines
* `docs/integration/reviews/checklist.md` — Integration Board checklist
* `docs/standards/metadata.md` — STAC/DCAT/PROV schema fields
* `docs/standards/markdown_rules.md` — Markdown governance & style

---

<div align="center">

### 🤖 “Models write stories from data — reviews ensure those stories are faithful.”

**Kansas Frontier Matrix Review Council · MCP-DL v6.3**

</div>
