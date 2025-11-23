---
title: "🤖 Kansas Frontier Matrix — AI Pipeline Case Studies Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/case-studies/ai/README.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Annual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.1/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.1/pipelines-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-ai-case-studies-v11.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Under Expansion"
doc_kind: "AI Pipeline Case Study Index"
semantic_document_id: "kfm-doc:pipelines-case-studies-ai"
doc_uuid: "urn:kfm:pipelines:case-studies:ai:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Integrated · Data-Quality"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
redaction_required: false
classification: "Public Document"
jurisdiction: "Kansas / United States"
risk_category: "Operational Reliability"
data_steward: "KFM FAIR+CARE Council"
ai_training_inclusion: true
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "model-card-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "unverified predictions"
  - "speculative narratives"
  - "hallucinated model lineage"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon template v12 release"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
---

<div align="center">

# 🤖 **Kansas Frontier Matrix — AI Pipeline Case Studies Index**  
`docs/pipelines/case-studies/ai/README.md`

**A curated sub-library of AI-specific pipeline case studies designed  
to illuminate ML orchestration, ethics, lineage, and reliability patterns  
directly applicable to KFM v11.**

</div>

---

# 📘 1. Purpose

This section contains **AI-focused case studies** that examine:

- migrations to Python-native workflow engines  
- model-training and inference DAG architectures  
- reproducibility (seed locking, deterministic outputs)  
- FAIR+CARE-aligned AI governance  
- explainability pipelines (SHAP/LIME, Focus Mode attribution)  
- AI-derived Story Node workflows  
- autonomous ML retraining cycles  
- Neo4j semantic enrichment and graph-safe AI patterns  

These case studies help all KFM contributors develop **ethical, reliable, reproducible, and observable AI pipelines**.

---

# 🗂 2. Directory Layout (KFM v11 Style)

```text
docs/
│
└── pipelines/
    │
    ├── case-studies/
    │   ├── README.md
    │   └── ai/
    │       └── README.md               ← you are here
    │
    ├── ai/
    │   └── README.md                   ← main AI pipelines spec
    │
    ├── reliable-pipelines.md
    ├── validation-observability/
    │   └── README.md
    │
    └── ...
```

This directory hosts only **AI-focused case studies**, not the pipelines themselves.

---

# 📚 3. Planned AI Case Studies

### 🔁 3.1 Autonomous ML Re-Training (Planned)
`docs/pipelines/case-studies/ai/autonomous-ml-refresh.md`

Focus:

- nightly model retraining  
- model drift detection  
- explainability snapshots  
- checksum + SBOM + SLSA model lineage  
- promotion gate rules for ML artifacts  

---

### 🧠 3.2 Focus Mode v3 — Semantic Reasoning Engine (Planned)
`docs/pipelines/case-studies/ai/focus-mode-v3-case-study.md`

Focus:

- multi-hop graph reasoning  
- episodic memory windows  
- domain-grounded semantic linking  
- CARE-restricted narrative safety  
- prompt-regime reproducibility  

---

### 📦 3.3 Embedding Pipelines & Vector Search (Planned)
`docs/pipelines/case-studies/ai/embeddings-case-study.md`

Focus:

- deterministic embedding generation  
- HNSW index reproducibility  
- embedding drift management  
- FAIR+CARE constraints on text corpora  
- provenance linking (OpenLineage → SBOM → checksums)

---

# 🧱 4. Case Study Template (Required for All AI Case Studies)

All new AI case studies MUST follow the v11 template:

1. **YAML Front Matter**  
   - version, last_updated, telemetry, governance, ontology mapping

2. **Overview**  
   - system, purpose, high-level architecture

3. **Legacy Architecture / Prior Approach**  
   - failures, scaling issues, ethical gaps

4. **Motivations for Change**  
   - operational, ethical, reproducibility, governance

5. **Target Architecture**  
   - DAG engine, model pipeline stages, explainability components

6. **Reliability & Governance Features**  
   - WAL, rollback, deterministic seeds  
   - FAIR+CARE rules  
   - SLSA provenance  
   - OpenLineage linking  
   - SBOM integration

7. **Operational Results**  
   - throughput, reproducibility, governance improvements

8. **Lessons for KFM v11**  
   - specific actionable recommendations  
   - patterns and anti-patterns

9. **Next Steps**  
   - how the case study informs new v11 templates & guardrails

This template will eventually live in:

```
docs/pipelines/case-studies/ai/_templates/case-study-template-v11.md
```

---

# 🔗 5. Related Documents

- `docs/pipelines/ai/README.md`  
- `docs/pipelines/reliable-pipelines.md`  
- `docs/pipelines/validation-observability/README.md`  
- `docs/standards/security/checksum-sbom-provenance.md`  
- `docs/standards/security/slsa-attestation-standard.md`  
- `docs/standards/faircare.md`  
- `docs/architecture/ai-system/README.md`

---

# 🕰 6. Version History

- **v11.0.0 (2025-11-23)** – Initial creation of the AI case study index.

---

<div align="center">

**Kansas Frontier Matrix — AI Pipeline Case Studies (v11)**  
*Ethical · Reproducible · Governed · Semantically Grounded*

</div>

---

### 🔗 Footer  
[⬅ Back to Case Studies Index](../README.md) · [🧠 AI Pipelines](../../ai/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

