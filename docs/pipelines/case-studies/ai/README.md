---
title: "🤖 Kansas Frontier Matrix — AI Pipeline Case Studies Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/case-studies/ai/README.md"
version: "v11.0.1"
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
doc_uuid: "urn:kfm:pipelines:case-studies:ai:index:v11.0.1"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Integrated · Data-Quality"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
redaction_required: false"
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
  - "speculative behavior"
  - "unverified historical claims"
  - "hallucinated lineage"
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

# 🤖 **AI Pipeline Case Studies Index (KFM v11)**  
`docs/pipelines/case-studies/ai/README.md`

**A focused library of AI-specific pipeline case studies documenting model workflows,  
autonomous ML patterns, explainability practices, lineage requirements, and  
FAIR+CARE-aligned governance lessons for KFM v11.**

</div>

---

# 📘 1. Purpose

This directory hosts **AI-related case studies** that demonstrate:

- AI/ML orchestration (training, inference, embeddings, explainability)
- Autonomous model refresh patterns
- Seed-locked reproducibility methods
- Ethical AI workflows (FAIR+CARE integrated)
- AI lineage (OpenLineage + SLSA + SBOM)
- Story Node and Focus Mode v3 AI behavior governance
- Integration with STAC, Neo4j, and WAL-based reliability

These examples serve as internal guidance for designing future **KFM v11 AI pipelines**.

---

# 🗂 2. Directory Layout (Focused on This Directory Only)

The layout below follows your requirement:  
**Show this directory and only the next branch beneath it.**

```text
docs/pipelines/case-studies/ai/
│
├── README.md                        ← this file
├── autonomous-ml-refresh.md         ← planned
├── focus-mode-v3-engine.md          ← planned
├── embeddings-vector-search.md       ← planned
└── _templates/
    └── case-study-ai-template-v11.md ← planned authoring template
```

---

# 📚 3. Planned AI Case Studies

## 🔁 Autonomous ML Re-Training (Planned)
`docs/pipelines/case-studies/ai/autonomous-ml-refresh.md`

Topics:
- nightly retraining  
- drift detection + rollback  
- SHAP/LIME explainability bundles  
- SLSA provenance + SBOM linkage  
- deterministic DAG execution  

---

## 🧠 Focus Mode v3 Semantic Engine (Planned)
`docs/pipelines/case-studies/ai/focus-mode-v3-engine.md`

Topics:
- multi-hop reasoning  
- Neo4j entity grounding  
- CARE-restricted narrative filtering  
- semantic windows, memory alignment  
- reproducibility constraints  

---

## 📦 Embedding Pipelines & Vector Search (Planned)
`docs/pipelines/case-studies/ai/embeddings-vector-search.md`

Topics:
- deterministic embeddings  
- HNSW reproducibility (index versioning)  
- dataset sensitivities  
- FAIR+CARE-safe text corpora  
- OpenLineage lineage chains for embeddings  

---

# 🧱 4. Required Case Study Structure (v11 Template)

All AI pipeline case studies MUST include:

1. **Front-Matter**  
   - complete metadata: version, sbom, manifest, telemetry, governance, ontology alignment

2. **Overview**  
   - short summary: pipeline purpose, domain context

3. **Legacy Architecture**  
   - previous system, limitations, ethics gaps

4. **Drivers for Redesign**  
   - operational, governance, reproducibility, FAIR+CARE

5. **Target Architecture**  
   - DAG engine (LangGraph / Prefect / other)  
   - training vs inference separation  
   - explainability pipeline  
   - provenance & lineage injection points  

6. **Reliability & Governance Design**  
   - WAL, rollback, idempotency, retries  
   - SLSA v1.0 attestations  
   - SBOM File entries  
   - FAIR+CARE masking rules  
   - Indigenous sovereignty protections (H3)  

7. **Performance & Operational Outcomes**  
   - throughput, scaling, cost, reproducibility  

8. **Lessons for KFM v11**  
   - specific, reusable insights  
   - patterns to adopt  
   - anti-patterns to avoid  

9. **Next Steps**  
   - how the pipeline pattern will integrate into future KFM DAGs  

---

# 🔗 5. Related Documents

- `docs/pipelines/ai/README.md`  
- `docs/pipelines/reliable-pipelines.md`  
- `docs/pipelines/validation-observability/README.md`  
- `docs/standards/security/slsa-attestation-standard.md`  
- `docs/standards/security/checksum-sbom-provenance.md`  
- `docs/standards/faircare.md`  
- `docs/architecture/ai-system/README.md`  

---

# 🕰 6. Version History

- **v11.0.1 (2025-11-23)** — Initial creation of AI case study index (KFM-MDP v11-aligned).

---

<div align="center">

**Kansas Frontier Matrix — AI Pipeline Case Studies (v11)**  
*Ethical · Reproducible · FAITHFUL · Semantically Grounded*

</div>

---

### 🔗 Footer  
[⬅ Back to Case Studies](../README.md) · [🧠 AI Pipelines](../../ai/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)
