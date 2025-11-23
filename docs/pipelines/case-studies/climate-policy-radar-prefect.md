---
title: "🌍 KFM v11 — Climate Policy Radar: Step Functions → Prefect Migration Case Study (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/case-studies/climate-policy-radar-prefect.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Annual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.1/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.1/pipelines-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-case-study-climate-policy-radar-v11.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active"
doc_kind: "Pipeline Case Study"
semantic_document_id: "kfm-doc:pipelines-case-study-climate-policy-radar-prefect"
doc_uuid: "urn:kfm:pipelines:case-studies:climate-policy-radar-prefect:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Integrated · Doc-Workflow"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
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
  - "hallucinated citations"
  - "speculative system behavior"
lifecycle_stage: "stable"
ttl_policy: "Review required every 18 months"
sunset_policy: "Superseded by next major pipeline migration standard"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Activity"
  geosparql: "geo:FeatureCollection"
---

<div align="center">

# 🌍 **Climate Policy Radar — Step Functions → Prefect Migration Case Study (KFM v11)**  
`docs/pipelines/case-studies/climate-policy-radar-prefect.md`

*A public, technology-focused case study highlighting best practices from  
AWS Step Functions → Prefect migrations, and how those lessons directly  
inform KFM v11 pipeline architecture.*

</div>

---

# 🔖 1. Overview

This case study summarizes **publicly known migration patterns** seen when organizations working  
with **large text corpora**, including Climate Policy Radar, transitioned from:

- **AWS Step Functions (JSON declarative workflows)**  
- **Lambda-based micro-tasks**  
- **Cron-scheduled jobs**

to a **Python-native orchestration framework such as Prefect**, which better supports:

- dynamic branching  
- modular workflow composition  
- developer ergonomics  
- metadata-rich observability  
- stateful long-running tasks  

This document extracts the **technical lessons** and explains how they influenced  
the **KFM v11 pipeline design**, especially in domains requiring:

- large document processing  
- policy/legislation ingestion  
- NLP-based metadata generation  
- autonomous refresh cycles  

No private or internal organizational details are included.

---

# 🕰️ 2. Legacy Architecture: AWS Step Functions + Lambda

Public technology reports and best practices note that Step Functions are powerful but have  
**inherent constraints** for complex, research-driven workflow ecosystems:

### 2.1 Pain Points in Legacy Stacks

#### ❌ 1. Limited developer expressiveness  
Workflows described entirely in JSON led to:

- verbose definitions  
- poor readability  
- difficult debugging  
- minimal IDE tooling

#### ❌ 2. Hard to handle long-running NLP tasks  
Climate-policy document ingestion can involve:

- expensive OCR  
- model-based classification  
- complex renormalization steps  
- multi-branch validations

Lambda’s **15-minute execution limit** restricts these workloads.

#### ❌ 3. Difficult to express dynamic branching  
Document pipelines naturally involve:

- conditionals  
- retries  
- recursive directory expansion  
- metadata-based branching  
- rate-limited external API calls

JSON-based Step Functions struggle to express these patterns cleanly.

#### ❌ 4. Poor local development ergonomics  
Engineers must:

- deploy to AWS for every test  
- mock infrastructure extensively  
- manage state machine JSON manually

---

# 🎯 3. Drivers Toward Prefect (Public Technology Motivations)

### 3.1 Python-native ecosystem  
- dynamic, code-first workflows  
- reusable task libraries  
- better readability + fewer lines  

### 3.2 Excellent observability  
- built-in UI  
- flow/task logs  
- distributed execution  

### 3.3 Parameterization and branching  
Dynamic workflows become trivial:

```python
if ".pdf" in doc.name:
    return process_pdf(doc)
else:
    return process_text(doc)
```

### 3.4 Long-running task support  
Perfect for:

- OCR  
- embedding generation  
- topic modeling  
- metadata extraction  
- multi-agent NLP pipelines  

### 3.5 Local-first development  
Prefect flows run:

- in notebooks  
- in scripts  
- in CI  
- in production infrastructure  

This greatly accelerates iteration.

---

# 🧱 4. Target Architecture (Publicly Observed Migration Pattern)

Below is a **model migration pattern** for organizations shifting from Step Functions  
to Prefect-based orchestration.

~~~mermaid
flowchart TD
  A[Raw Document Ingestion] --> B[Text Normalization]
  B --> C[OCR and PDF Processing]
  C --> D[Metadata Extraction]
  D --> E[NLP Model Inference]
  E --> F[Policy Classification]
  F --> G[Indexing and Search Update]
  G --> H[Observability + Telemetry]
  H --> I[Publish to API or Research Tools]
~~~

This general pattern mirrors many modern Python-native orchestrator migrations.

---

# 🔐 5. Reliability & Governance Features (Public Best Practices)

### 5.1 Retry + Backoff  
Prefect’s retry logic avoids unnecessary Lambda-style state resets.

### 5.2 Task-level caching  
Prevents repeated costly computations.

### 5.3 Parameterized flows  
Allows dynamic document sets and metadata-driven pipelines.

### 5.4 Structured logging & observability  
Research workflows benefit from:

- progress tracking  
- model-version tracing  
- reproducibility reports  

### 5.5 Hybrid execution  
Flows can run:

- on-prem  
- on clusters  
- in Kubernetes  
- on serverless targets  

Public reports show significant improvements in cost and flexibility.

---

# 📘 6. Lessons Applicable to KFM v11

The metadata-heavy workflow systems used by Climate Policy Radar and other organizations  
dealing with policy documents map closely to KFM’s needs for:

- ordinance datasets  
- legislative climate policy  
- environmental impact assessments  
- historical reports  
- multi-decade document collections  

### Key lessons applied to KFM:

## ✔ 1. Code-first workflows simplify complex ETL/AI tasks  
Python-native DAGs reduce friction for:

- hydrology scientists  
- climate-policy researchers  
- Story Node authors  
- FAIR+CARE governance reviewers  

## ✔ 2. Better observability improves governance & auditability  
Structured logs → easier FAIR+CARE reviews.  
Telemetry → allows operational risk scoring.

## ✔ 3. Dynamic branching is essential  
Environmental datasets, climate documents, and hazards archives  
rarely follow fixed shapes.

## ✔ 4. Model inference belongs *inside* the orchestrator  
Not as external, untracked services.  
This improves:

- OpenLineage provenance  
- SLSA attestations  
- drift monitoring  

## ✔ 5. Local-first development accelerates KFM domain experts  
A huge benefit for:

- hydrologists  
- climate researchers  
- historians  
- archivists  

---

# 🧭 7. Why KFM Adopted LangGraph v11 Instead of Prefect Directly

KFM v11 adopted **LangGraph**, not Prefect, because:

### ✔ It integrates natively with AI agents, multi-hop reasoning, and Focus Mode v3  
Prefect is world-class for ETL  
LangGraph is better for **agentic pipelines + semantic workflows**.

### ✔ LangGraph supports deterministic AI chain-of-thought with governance  
Essential for:

- Story Nodes  
- Focus Mode explainability  
- semantic safety rails  

### ✔ LangGraph nodes map cleanly to KFM validation layers  
Each node can enforce:

- structural  
- semantic  
- spatiotemporal  
- ethical  
- AI explainability  

### ✔ LangGraph DAGs can embed AI agents (Prefect cannot)  
AI-native control flows were mandatory for KFM.

### ✔ Still compatible with Prefect-like reliability patterns  
Retry, idempotency, WAL, backoff, observability — all replicated in KFM v11.

---

# 🚀 8. KFM Architecture Inspired by This Case Study

### Adopted:

- code-first orchestration  
- dynamic flow branching  
- long-running task support  
- telemetry-centric design  
- powerful local dev workflow  
- deterministic flow definitions  

### Extended by KFM:

- FAIR+CARE ethical gating  
- Indigenous sovereignty rules  
- Story Node v3 semantic engine  
- OPA-based publish gating  
- SLSA + SBOM + checksum registry  
- Neo4j semantic graph alignment  
- STAC/DCAT dataset promotion  

---

# 🧩 9. Appendix (Optional)

May include:

- public GitHub links to Step Functions → Prefect examples  
- performance improvements commonly reported  
- architecture comparisons (JSON vs Python-native DAGs)  

---

# 🕰 10. Version History

- **v11.0.0 (2025-11-23)** — Initial public-technology-focused case study release.

---

<div align="center">

**KFM v11 — Climate Policy Radar Migration Case Study**  
*Modern Orchestration · Improved Observability · FAIR+CARE-Aligned Governance*

</div>

---

### 🔗 Footer  
[⬅ Back to Case Studies](../README.md) · [📚 Pipelines Docs](../../README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

