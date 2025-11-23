---
title: "📚 Kansas Frontier Matrix — Pipelines Case Studies Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/case-studies/README.md"
version: "v11.0.3"
last_updated: "2025-11-23"
review_cycle: "Annual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.1/manifest.zip"
telemetry_ref: "../../../releases/v11.0.1/pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-case-studies-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Under Expansion"
doc_kind: "Pipelines Case Study Index"
semantic_document_id: "kfm-doc:pipelines-case-studies-index:v11"
doc_uuid: "urn:kfm:pipelines:case-studies:index:v11.0.3"
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
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon new protocol release"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Pipelines Case Studies Index**  
`docs/pipelines/case-studies/README.md`

**A unified, structured library of pipeline case studies documenting  
real-world ETL/AI workflows, engineering rationale, governance patterns,  
and FAIR+CARE ethics lessons for KFM v11.**

</div>

---

# 📘 1. Purpose & Scope

This directory contains **architectural case studies** used to guide the design of  
KFM v11 pipelines. These documents illustrate:

- How real organizations run scalable ETL/AI workflows  
- Why pipeline technologies (LangGraph, Prefect, Airflow, etc.) are chosen  
- How reliability, reproducibility, and compliance are enforced  
- How FAIR+CARE ethics shape engineering decisions  
- How these lessons directly inform Kansas Frontier Matrix workflows  

Case studies must help current and future contributors design pipelines that are:

- Reliable  
- Lineage-complete  
- Governance-aligned  
- FAIR+CARE compliant  
- Easy for domain experts to adapt  

---

# 🗂 2. Directory Layout (Aligned to KFM v11 Standards)

```text
docs/
│
└── pipelines/
    │
    ├── README.md
    ├── reliable-pipelines.md
    │
    ├── ai/
    │   └── README.md
    │
    ├── validation-observability/
    │   └── README.md
    │
    └── case-studies/
        ├── README.md                           ← you are here
        ├── snorkel-ai-prefect.md               ← planned
        ├── climate-policy-radar-prefect.md     ← planned
        └── _templates/
            └── case-study-template-v11.md      ← planned template
```

All case studies **must** appear under this directory and include valid  
`path:` metadata pointing to the exact file location.

---

# 📂 3. Case Studies (Current & Planned)

## 🤖 Snorkel AI — Migration to Prefect *(Planned)*

**Planned path:**  
`docs/pipelines/case-studies/snorkel-ai-prefect.md`

**Themes:**

- Migration from custom orchestration → Prefect  
- Running thousands of ML jobs/day  
- Removing home-grown queueing & retry plumbing  
- Lessons for KFM:
  - High-throughput ML ETL patterns  
  - Python-native DAG ergonomics  
  - Reliability & governance integration  
  - Mapping Snorkel patterns → LangGraph v11 + OpenLineage

---

## 🌍 Climate Policy Radar — Step Functions → Prefect *(Planned)*

**Planned path:**  
`docs/pipelines/case-studies/climate-policy-radar-prefect.md`

**Themes:**

- Migrating from AWS Step Functions + Lambdas  
- Processing 25k+ long-form climate-policy documents  
- Researcher-driven pipeline development  
- Lessons for KFM:
  - Document-centric processing patterns  
  - Conditional branching & long-running tasks  
  - Multi-repo workflow design for domain experts  

---

## 🧪 Internal KFM Case Studies (Recommended)

Future internal case studies should cover:

- 💧 **Hydrology**  
  - Autonomous streamflow reconstruction  
  - Multi-source fusion, anomaly smoothing, WSEL logic  
- 🌾 **Climate / Land Surface**  
  - Downscaling, NDVI/LC compositing  
- ⚠️ **Hazards**  
  - Wildfire + energy hazard ETL → AI modeling → Story Nodes  
- 🏛️ **Archaeology**  
  - Geophysics ETL, H3 generalization, sovereignty constraints  
- 🧠 **AI Governance**  
  - Focus Mode v3 pipelines, bias/drift detection, explainability chains  

All internal case studies must scrutinize:

- Retries, WAL, rollback  
- STAC/DCAT generation  
- OpenLineage evidence  
- SLSA provenance  
- FAIR+CARE ethics controls  
- Indigenous rights considerations  

---

# 🧱 4. Case Study Structure (v11 Template)

All case studies must follow this exact structure:

1. **YAML Front-Matter**
   - Full metadata: version, sbom_ref, manifest_ref, governance_ref, telemetry, etc.

2. **Overview**
   - Context, motivation, systems involved

3. **Legacy Architecture**
   - Prior workflow, pains, scaling issues, governance gaps

4. **Migration Drivers / Design Motivations**
   - Technical + ethical + operational reasons for change

5. **Target Architecture**
   - DAG engine, repos, runtime, observability  
   - Where lineage/provenance is enforced  
   - FAIR+CARE roles

6. **Reliability & Governance Features**
   - Retries, backoff, WAL, SLSA, SBOM, OpenLineage  
   - Data Contract v3 alignment  
   - Ethical safeguards

7. **Operational Results**
   - Throughput, latency, cost, auditability, reproducibility

8. **Lessons for KFM v11**
   - Clear, actionable guidance  
   - Anti-patterns to avoid  
   - Patterns to adopt KFM-wide

9. **Implementation Notes & Next Steps**
   - Where in KFM these lessons will be integrated  
   - Template or tooling recommendations

A future `_templates/case-study-template-v11.md` will provide a copy-ready skeleton.

---

# 🔗 5. Related Pipeline Documentation

Case studies must reference:

- `docs/pipelines/reliable-pipelines.md`  
- `docs/pipelines/validation-observability/README.md`  
- `docs/pipelines/ai/README.md`  
- Root `ARCHITECTURE.md`  
- Relevant standards under `docs/standards/`

---

# 🕰 6. Version History

- **v11.0.3 (2025-11-23)** — Upgraded to full directory-tree alignment, KFM-MDP v11 compliance.  
- **v11.0.2 (2025-11-23)** — Initial v11-compliant regeneration.  
- **v11.0.1** — Original metadata version.

---

<div align="center">

**Kansas Frontier Matrix — Pipelines Case Studies Index (v11)**  
*Architecture · Governance · FAIR+CARE Ethics · Reproducible Engineering*

</div>

---

### 🔗 Footer  
[⬅ Back to Pipelines Docs](../README.md) · [📚 Documentation Index](../../README.md) · [🧬 Reliable Pipelines Guide](../reliable-pipelines.md)
