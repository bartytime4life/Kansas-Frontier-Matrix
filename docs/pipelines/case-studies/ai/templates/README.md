---
title: "🧩 KFM v11 — AI Case Study Templates Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/case-studies/ai/templates/README.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Annual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.1/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.1/pipelines-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-ai-case-studies-templates-v11.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active"
doc_kind: "Template Index"
semantic_document_id: "kfm-doc:pipelines-case-studies-ai-templates"
doc_uuid: "urn:kfm:pipelines:case-studies:ai:templates:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Integrated · Data-Quality"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
redaction_required: false
classification: "Public Document"
jurisdiction: "Kansas / United States"
risk_category: "Template / Documentation"
data_steward: "KFM FAIR+CARE Council"
ai_training_inclusion: true
ai_focusmode_usage: "Allowed"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculation"
  - "unverified assertions"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon template v12 release"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
---

<div align="center">

# 🧩 **AI Case Study Template Library**  
`docs/pipelines/case-studies/ai/templates/README.md`

**Authoring templates for creating fully compliant, governance-aligned  
AI pipeline case studies in the Kansas Frontier Matrix (KFM v11).**

</div>

---

# 📘 1. Purpose

This directory provides **standardized templates** for writing  
**AI-focused pipeline case studies** within the Kansas Frontier Matrix.

These templates ensure:

- Full **KFM-MDP v11** formatting compliance  
- Proper **YAML metadata front-matter**  
- Correct **FAIR+CARE governance reflection**  
- Clear structure for describing AI/ML workflows  
- Built-in sections for lineage, ethics, provenance, observability  
- Authoring consistency across all teams and domains  

All new AI pipeline case studies **must** begin from one of these templates.

---

# 🗂 2. Directory Layout (Local Only + Next Branch)

```text
docs/pipelines/case-studies/ai/templates/
│
├── README.md                         ← this file
└── case-study-ai-template-v11.md     ← primary authoring template (planned)
```

This directory focuses exclusively on **authoring guidance** and **template scaffolds**.

---

# 🧱 3. Template Purpose

Each template is designed to support:

- **AI pipeline narrative structure**
- **Model training/inference documentation**
- **Autonomous ML refresh workflows**
- **Explainability integration (SHAP/LIME/Focus Mode)**
- **Ethical review (FAIR+CARE)**
- **Provenance (PROV-O, SLSA v1.0, OpenLineage v2.5)**
- **Checksum/SBOM alignment**
- **Reproducibility expectations**
- **Graph-safe structuring (Neo4j + ontology alignment)**

These requirements guarantee every case study contributes directly to  
KFM’s cross-pipeline engineering and governance patterns.

---

# 🧩 4. Case Study Template (Summary of Required Structure)

The full template (in `case-study-ai-template-v11.md`) includes:

1. **Front-Matter**  
   Complete metadata block with versioning, provenance refs, ontology alignment.

2. **Overview**  
   Description of system, organizational context, pipeline goals.

3. **Legacy Approach**  
   Pain points, governance gaps, reproducibility or reliability issues.

4. **Migration Drivers / Change Motivation**  
   Technical + ethical reasons for redesign.

5. **Target Architecture**  
   - DAG structure  
   - Model stages (training → inference → explainability)    
   - Observability injection points  
   - Provenance boundaries  

6. **Reliability & Governance Pattern**  
   - WAL  
   - deterministic retry  
   - reproducibility contracts  
   - SLSA  
   - SBOM  
   - FAIR+CARE controls  

7. **Operational Outcomes**  
   Effectiveness, throughput, drift reduction, cost patterns.

8. **Lessons for KFM**  
   Direct mapping to KFM v11 pipeline architecture.

9. **Next Steps**  
   Opportunities for template expansion or pipeline unification.

---

# 🔗 5. Related Documents

- `docs/pipelines/case-studies/ai/README.md`  
- `docs/pipelines/case-studies/README.md`  
- `docs/pipelines/ai/README.md`  
- `docs/pipelines/reliable-pipelines.md`  
- `docs/pipelines/validation-observability/README.md`  
- `docs/standards/security/slsa-attestation-standard.md`  
- `docs/standards/security/sbom-standard.md`  
- `docs/standards/faircare.md`  

---

# 🕰 6. Version History

- **v11.0.0 (2025-11-23)** — Initial template index for AI pipeline case studies.

---

<div align="center">

**Kansas Frontier Matrix — AI Case Study Templates (v11)**  
*Consistent · Ethical · Reproducible · Governance-Aligned*

</div>

---

### 🔗 Footer  
[⬅ Back to AI Case Studies](../README.md) · [📚 Pipeline Case Studies](../../README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

