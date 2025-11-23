---
title: "📚 Kansas Frontier Matrix — Pipelines Case Studies Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/case-studies/README.md"
version: "v11.0.1"
last_updated: "2025-11-23"
review_cycle: "Annual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.1/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.1/manifest.zip"
telemetry_ref: "../../../schemas/telemetry/pipelines-case-studies-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v11.0"
markdown_protocol_version: "KFM-MDP v11.0"
status: "Active · Under Expansion"
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

This README documents the **case-studies** directory:

```text
docs/pipelines/case-studies/
│
├── README.md                         ← this file
├── ai/
│   └── README.md                     ← AI-specific pipeline case studies index
├── snorkel-ai-prefect.md             ← external case study (planned)
├── climate-policy-radar-prefect.md   ← external case study (planned)
└── _templates/
    └── case-study-template-v11.md    ← authoring template (planned)
```

You can safely add new case study files under `docs/pipelines/case-studies/` as long as they:

- Use KFM-MDP v11 formatting
- Include full YAML front-matter metadata
- Follow the structure defined in the template section below

---

## 📂 Current and Planned Case Studies

### 🤖 Snorkel AI — Migration to Prefect (Planned)

**File (planned):**  
`docs/pipelines/case-studies/snorkel-ai-prefect.md`

**Focus:**

- Migration from home-grown orchestration (Redis Queue + custom plumbing) to Prefect
- Executing thousands of workflows per day
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
`docs/pipelines/case-studies/climate-policy-radar-prefect.md`

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

## 🧱 Case Study Structure (Template)

All case studies in this directory should follow a consistent, v11-aligned structure.  
When you create a new file (for example, `my-pipeline-case-study.md`), structure it as follows:

1. **Title and Metadata**
   - YAML front-matter with:
     - `title`, `path`, `version`, `last_updated`, `review_cycle`
     - `sbom_ref`, `manifest_ref`, `telemetry_ref`, `telemetry_schema`
     - `governance_ref`, `license`, `mcp_version`, `markdown_protocol_version`, `status`, `doc_kind`

2. **Overview**
   - Short, non-technical summary
   - System or organization context
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
   - High-level DAG and orchestration model
   - Orchestration platform (for example, Prefect, LangGraph-based)
   - Where telemetry, lineage, SBOM, and SLSA are enforced
   - Multi-repo and multi-team boundaries (if relevant)

6. **Reliability & Governance Features**
   - Retries, backoff, idempotency
   - WAL, checkpointing, rollback strategies
   - FAIR+CARE checks, sensitivity filters, sovereignty labels
   - PROV-O and OpenLineage emissions and their usage in KFM

7. **Operational Results**
   - Qualitative and/or quantitative improvements:
     - throughput
     - failure rates
     - latency
     - reproducibility
     - auditability
   - Impact on developer workflows and governance reviews

8. **Lessons for KFM v11**
   - Concrete recommendations for:
     - KFM orchestration patterns
     - KFM telemetry and lineage contracts
     - Contributor ergonomics and templates
   - Anti-patterns and pitfalls to avoid in KFM pipelines

9. **Implementation Notes & Next Steps**
   - How this pattern will be reused, generalized, or codified into:
     - templates
     - shared libraries
     - governance rules
     - training materials

A shared template file will be maintained at:

```text
docs/pipelines/case-studies/_templates/case-study-template-v11.md
```

---

## 🔗 Related Pipeline Documentation

For deeper context and to align new case studies with the rest of the KFM pipeline stack, see:

- 🧬 **Reliable Pipelines Architecture & Operations Guide**  
  `docs/pipelines/reliable-pipelines.md`

- 🧠 **AI Pipelines & Autonomous Workers**  
  `docs/pipelines/ai/README.md` (planned)

- 📊 **Validation & Observability for Pipelines**  
  `docs/pipelines/validation-observability/README.md`

- 🧭 **KFM Repository Architecture Overview**  
  `ARCHITECTURE.md` (at the repository root; see also `docs/architecture/`)

When adding a new case study, ensure it:

- Links back to this index (`docs/pipelines/case-studies/README.md`)
- References relevant standards under `docs/standards/`
- References relevant pipeline guides under `docs/pipelines/`

---

## ✅ Contribution Checklist for New Case Studies

Before opening a PR with a new case study under `docs/pipelines/case-studies/`, verify:

1. **File & Path**
   - File is created under `docs/pipelines/case-studies/` (or a clearly defined subdirectory)
   - `path` in front-matter matches the actual file location

2. **Metadata**
   - Uses KFM-MDP v11-compliant YAML front-matter
   - `version` and `last_updated` are set and maintained
   - `sbom_ref`, `manifest_ref`, `telemetry_ref`, `telemetry_schema` use correct relative paths
   - `governance_ref` points to the appropriate governance standard

3. **Formatting**
   - Uses GitHub-safe fenced blocks (tilde fences recommended)
   - No nested fences that could break rendering
   - Emojis in headings follow KFM v11 style guidelines
   - No decorative separators outside of the standard section breaks

4. **Content Quality**
   - Includes all required sections (Overview, Legacy, Drivers, Target Architecture, Reliability & Governance, Lessons, Next Steps)
   - Uses clear, precise, and neutral language
   - Distinguishes clearly between **facts**, **assumptions**, and **recommendations**

5. **Governance & Ethics**
   - Describes how telemetry, lineage, and FAIR+CARE are implemented
   - Explicitly flags any handling of sensitive or Indigenous data and associated safeguards
   - Aligns with:
     - `docs/standards/faircare.md`
     - `docs/standards/security/checksum-sbom-provenance.md`
     - `docs/standards/security/slsa-attestation-standard.md`

6. **Cross-Links**
   - Adds this case study to any relevant indices (for example, this README)
   - Links to related pipeline specs and standards
   - References any associated audit or provenance documents under `docs/archives/provenance/`

---

[⬅ Back to Pipelines Docs](../README.md) · [📚 KFM Documentation Index](../../README.md) · [🧬 Reliable Pipelines Guide](../reliable-pipelines.md)
