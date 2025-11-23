---
title: "📚 Kansas Frontier Matrix — Pipelines Case Studies Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/case-studies/README.md"
version: "v11.0.1"
last_updated: "2025-11-23"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.1/manifest.zip"
telemetry_ref: "../../../releases/v11.0.1/pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-case-studies-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
status: "Active / Under Expansion"
doc_kind: "Pipelines Case Study Index"
---

# 📚 Kansas Frontier Matrix — Pipelines Case Studies Index

Welcome to the **KFM v11 pipelines case studies hub**. This directory collects real-world and internal case studies that document:

- How complex ETL/AI workflows are orchestrated
- Why specific orchestration technologies were chosen
- How reliability, lineage, and FAIR+CARE governance are enforced in practice
- What lessons apply directly to the Kansas Frontier Matrix (KFM) pipeline stack

Use this index to discover existing case studies and to add new ones in a consistent, v11-compliant way.

---

## 🎯 Purpose & Scope

This directory exists to:

- Document **end-to-end pipeline migrations and architectures** (internal and external)
- Capture **design rationales** behind KFM’s orchestration and reliability decisions
- Provide **reference patterns** for new pipelines (autonomous refresh, AI, ETL, Story Nodes)
- Support **FAIR+CARE and governance reviews** with concrete, example-driven evidence

Case studies here should be:

- Narrative and architectural (not just code snippets)
- Focused on **workflow orchestration**, **reliability**, and **governance**
- Explicit about **trade-offs** and **lessons learned for KFM**

---

## 🏗️ Directory Layout

This README describes the directory:

- `docs/pipelines/case-studies/README.md`

Planned and example layout:

- `docs/`
  - `pipelines/`
    - `README.md`
    - `reliable-pipelines.md`
    - `ai/`
      - `README.md`
    - `validation-observability/`
      - `README.md`
    - `case-studies/`
      - `README.md`                          ← you are here
      - `snorkel-ai-prefect.md`             ← external case study (planned)
      - `climate-policy-radar-prefect.md`   ← external case study (planned)
      - `_templates/`
        - `case-study-template-v11.md`      ← authoring template (planned)

You can safely add new case study files under `docs/pipelines/case-studies/` as long as they:

- Use KFM-MDP v11 formatting
- Include full YAML front-matter metadata
- Follow the structure defined in the template section below

---

## 📂 Current and Planned Case Studies

### 🤖 Snorkel AI — Migration to Prefect (Planned)

**File (planned):**  
- `docs/pipelines/case-studies/snorkel-ai-prefect.md`

**Focus:**

- Migration from home-grown orchestration (Redis Queue + custom plumbing) to Prefect
- Executing **thousands of workflows per day**
- Eliminating hand-rolled mechanisms for:
  - queueing
  - retries
  - worker management
  - basic telemetry
- Lessons for KFM:
  - High-throughput autonomous refresh patterns
  - Elastic workers vs static worker pools
  - Python-native DAGs for complex ML workflows

This case study should explicitly map Snorkel’s experience to:

- KFM’s **AI/ETL pipelines**
- **LangGraph DAG patterns**
- OpenLineage and PROV-O integration for KFM v11

---

### 🌍 Climate Policy Radar — From AWS Step Functions to Prefect (Planned)

**File (planned):**  
- `docs/pipelines/case-studies/climate-policy-radar-prefect.md`

**Focus:**

- Large-scale processing of ~25k+ climate-policy documents
- Migration from:
  - AWS Step Functions (JSON state machines)
  - Lambda functions
  - Cron jobs
- To:
  - Python-based Prefect flows
  - Multi-repository pipeline architecture
- Key themes:
  - Enabling researchers and data scientists to own workflows
  - Handling long-running, multi-stage document pipelines
  - Flexible branching, conditionals, and runtime parameters

Lessons for KFM:

- How to structure KFM’s pipelines so **domain experts** (hydrology, climate, hazards, archaeology) can author and evolve flows
- Why Python-native orchestration fits KFM’s **multi-repo, multi-team** structure
- Patterns for processing **large, document-like corpora** (e.g., reports, PDFs, historical documents)

---

### 🧪 Future Case Studies (Internal KFM)

Recommended internal KFM-focused case studies to add here:

- 💧 **Hydrology:**  
  - Autonomous streamflow reconstruction pipeline (AI-based gap filling, anomaly smoothing, multi-source fusion)
- 🌾 **Climate & Land Surface:**  
  - Climate downscaling and NDVI/landcover compositing pipelines
- ⚠️ **Hazards:**  
  - Wildfire and energy hazard ETL → AI hazard modeling → Story Node narratives
- 🏛️ **Heritage & Archaeology:**  
  - Geophysics ETL (magnetometry, GPR, resistivity) and H3 spatial generalization standard in action
- 🧠 **AI Governance:**  
  - Focus Mode v3, Story Node v3 pipelines with bias/drift detection and FAIR+CARE audits

Each internal case study should follow the same template structure and emphasize:

- Reliability (retries, rollbacks, WAL, promotion gates)
- Provenance (PROV-O, OpenLineage, ISO 19115 lineage)
- Ethics and governance (FAIR+CARE, Indigenous data sovereignty, sensitivity handling)

---

## 🧱 Case Study Structure (Template)

All case studies in this directory should follow a consistent, v11-aligned structure.  
When you create a new file (e.g., `my-pipeline-case-study.md`), structure it like:

1. **Title and Metadata**
   - YAML front-matter with:
     - `title`, `path`, `version`, `last_updated`, `review_cycle`
     - `sbom_ref`, `manifest_ref`, `telemetry_ref`, `telemetry_schema`
     - `governance_ref`, `license`, `mcp_version`, `markdown_protocol_version`, `status`, `doc_kind`

2. **Overview**
   - Short, non-technical summary
   - What system or organization this is about
   - Why this case study matters to KFM

3. **Legacy Architecture**
   - What existed before migration or redesign
   - Key pain points:
     - scalability
     - reliability
     - governance
     - developer experience

4. **Migration Drivers / Design Motivations**
   - Why change was necessary
   - Constraints (cost, skills, time, compliance)
   - Selection criteria for the new orchestration/architecture

5. **Target Architecture**
   - High-level DAG description
   - Orchestration platform (e.g., Prefect, LangGraph-based)
   - Where telemetry, lineage, and contracts are enforced
   - Multi-repo and multi-team boundaries (if relevant)

6. **Reliability & Governance Features**
   - Retries, backoff, idempotency
   - WAL, checkpointing, rollback paths
   - FAIR+CARE checks, sensitivity filters, sovereignty labels
   - PROV-O and OpenLineage emissions and how they integrate with KFM

7. **Operational Results**
   - Throughput improvements (qualitative or quantitative)
   - Failure rates before vs after (if available)
   - Developer workflow and iteration speed
   - Governance and audit improvements

8. **Lessons for KFM v11**
   - Concrete recommendations for:
     - KFM orchestration patterns
     - KFM telemetry/lineage contracts
     - Contributor ergonomics and templates
   - Any anti-patterns we should avoid in KFM

9. **Implementation Notes & Next Steps**
   - How this pattern will be reused, generalized, or codified into:
     - templates
     - libraries
     - governance requirements

A shared `_templates/case-study-template-v11.md` file should eventually contain a ready-to-copy skeleton matching this structure.

---

## 🔗 Related Pipeline Documentation

For deeper context and to align new case studies with the rest of the KFM pipeline stack, see:

- 🧬 **Reliable Pipelines Architecture & Operations Guide**  
  - `docs/pipelines/reliable-pipelines.md`

- 🧠 **AI Pipelines & Autonomous Workers**  
  - `docs/pipelines/ai/README.md` (planned)

- 📊 **Validation & Observability for Pipelines**  
  - `docs/pipelines/validation-observability/README.md` (planned)

- 🧭 **KFM Repository Architecture Overview**  
  - `ARCHITECTURE.md` (at repository root, name may vary)

When adding a new case study, cross-link it back to:

- This index (`docs/pipelines/case-studies/README.md`)
- The most relevant pipeline standard/guides under `docs/pipelines/`
- Any domain-specific standards under `docs/standards/`

---

## ✅ Contribution Checklist for New Case Studies

Before opening a PR with a new case study under `docs/pipelines/case-studies/`, verify:

1. 📄 **File & Path**
   - File is under `docs/pipelines/case-studies/`
   - Path in YAML front-matter matches the actual file location

2. 🧾 **Metadata**
   - KFM-MDP v11-compatible YAML front-matter present
   - `version` and `last_updated` set correctly
   - `sbom_ref`, `manifest_ref`, `telemetry_ref`, `telemetry_schema` use correct relative paths
   - `governance_ref` points to the appropriate governance document

3. 🎨 **Formatting**
   - Emojis on headings per v11 style
   - Uses GitHub-safe fenced blocks (if present, tildes are recommended)
   - No nested fences that could break rendering
   - No decorative separators beyond what KFM-MDP v11 allows

4. 🔍 **Content Quality**
   - Includes all major sections from the template:
     - Overview
     - Legacy architecture
     - Migration drivers
     - Target architecture
     - Reliability & governance features
     - Lessons for KFM
   - Uses clear language and is understandable by both engineers and domain experts

5. 🧬 **Governance & Provenance**
   - Mentions how telemetry, lineage, and FAIR+CARE are handled
   - Explicit about any sensitive data patterns, mitigation, or generalization (e.g., H3 usage)
   - If applicable, notes how Story Nodes and Focus Mode integrate

6. 🔗 **Cross-Links**
   - Links back to this README
   - Links to relevant standards and pipeline guides
   - Adds itself to any index/TOC sections where appropriate

---

[⬅️ Back to Pipelines Docs](../README.md) · [📚 KFM Documentation Index](../../README.md) · [🧬 Reliable Pipelines Guide](../reliable-pipelines.md)
