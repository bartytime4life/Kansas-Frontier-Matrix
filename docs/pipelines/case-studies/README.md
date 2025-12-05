---
title: "📚 Kansas Frontier Matrix — Pipelines Case Studies Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/case-studies/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v11.0.1 → v11.2.4 narrative-compatible"
status: "Active · Under Expansion"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/pipelines-case-studies-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-case-studies-v11.2.4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

doc_kind: "Pipelines Case Study Index"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "pipelines/case-studies"
  applies_to:
    - "pipeline-case-studies"
    - "ai-pipeline-case-studies"
    - "orchestration-migrations"
    - "reliability-case-studies"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; examples only)"
classification: "Public"
jurisdiction: "Kansas / United States"
public_exposure_risk: "Low"
indigenous_rights_flag: false

doc_uuid: "urn:kfm:doc:pipelines:case-studies:index:v11.2.4"
semantic_document_id: "kfm-pipelines-case-studies-index-v11.2.4"
event_source_id: "ledger:docs/pipelines/case-studies/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 📚 Kansas Frontier Matrix — Pipelines Case Studies Index  
`docs/pipelines/case-studies/README.md`

**Purpose**  
Serve as the canonical **case studies hub** for KFM pipelines — capturing real-world and internal
examples of orchestration, reliability, lineage, and FAIR+CARE governance, and providing reusable
patterns for new workflows across the Kansas Frontier Matrix.

</div>

---

## 📘 Overview

This directory collects **v11-aligned pipeline case studies** that document:

- How complex ETL/AI workflows are orchestrated in practice  
- Why specific orchestration technologies and architectures were chosen  
- How reliability, lineage, and FAIR+CARE governance are enforced end-to-end  
- What lessons apply directly to the KFM pipeline stack (ETL, AI, Story Nodes, Focus Mode)  

Case studies here are intended to be:

- **Narrative + architectural**, not just code snippets  
- Focused on **workflow orchestration**, **reliability**, and **governance**  
- Explicit about **trade-offs**, **constraints**, and **lessons learned for KFM**  

### Scope

This index governs all case studies under `docs/pipelines/case-studies/`, including:

- External migrations (e.g., Step Functions → Prefect, home-grown orchestrators → Prefect/LangGraph)  
- Internal KFM pipeline redesigns and incident postmortems  
- Reliability and governance experiments (SLOs, backpressure, schema drift, auto-update patterns)  

### Audience

- Pipeline & reliability engineers  
- Data & AI architects  
- FAIR+CARE and governance reviewers  
- Focus Mode / Story Node designers who need concrete operational examples  

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/case-studies/
├── 📄 README.md                           # This file (pipelines case studies index)
├── 📂 ai/                                 # AI-specific pipeline case studies index
│   └── 📄 README.md
├── 📄 snorkel-ai-prefect.md               # External case study (planned)
├── 📄 climate-policy-radar-prefect.md     # External case study (planned)
└── 📂 _templates/
    └── 📄 case-study-template-v11.md      # Authoring template (planned)
~~~

Author rules:

- New case studies **must** live under `docs/pipelines/case-studies/` (or its subdirectories).  
- Each case study **must** have KFM-MDP–compliant front-matter and a single H1. [oai_citation:0‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
- Directory layouts **must** use fenced code blocks with `text` and the `├──` / `└──` tree glyphs.  

---

## 🧱 Architecture

This section defines **how case studies themselves are structured** so they are:

- Story-Node friendly  
- Graph-ingestible  
- Pipeline- and governance-compliant  

### Case Study Structure Template

All case studies should follow this v11-aligned outline:

1. **Title & Metadata (YAML front-matter)**  
   - `title`, `path`, `version`, `last_updated`  
   - `sbom_ref`, `manifest_ref`, `telemetry_ref`, `telemetry_schema`  
   - `governance_ref`, `license`, `mcp_version`, `markdown_protocol_version`, `status`, `doc_kind`  

2. **Overview**  
   - Short summary of the system or organization  
   - Why this case study matters to KFM  

3. **Legacy Architecture**  
   - What existed before migration or redesign  
   - Pain points: scalability, reliability, governance, developer experience  

4. **Migration Drivers / Design Motivations**  
   - Why change was necessary  
   - Constraints (cost, skills, time, compliance)  
   - Selection criteria for the new stack / orchestrator  

5. **Target Architecture**  
   - High-level DAG and orchestration model  
   - Where telemetry, lineage, SBOM, and SLSA are enforced  
   - Multi-repo and multi-team boundaries  

6. **Reliability & Governance Features**  
   - Retries, backoff, idempotency, WAL, checkpointing, rollback  
   - FAIR+CARE, sovereignty labels, sensitivity filters  
   - PROV-O and OpenLineage usage  

7. **Operational Results**  
   - Qualitative/quantitative improvements (throughput, failure rate, latency, reproducibility)  
   - Impact on developer velocity and governance reviews  

8. **Lessons for KFM v11**  
   - Concrete recommendations for KFM pipeline patterns  
   - Telemetry/lineage contract implications  
   - Anti-patterns and pitfalls to avoid  

9. **Implementation Notes & Next Steps**  
   - How the pattern will be reused, generalized, or turned into templates/SOPs  

A shared authoring template is maintained at:

~~~text
docs/pipelines/case-studies/_templates/case-study-template-v11.md
~~~

### Current and Planned Case Studies

**🤖 Snorkel AI — Migration to Prefect (Planned)**  
File (planned): `docs/pipelines/case-studies/snorkel-ai-prefect.md`  

Focus:

- Migration from home-grown orchestration (Redis Queue + custom plumbing) to Prefect  
- Operating thousands of workflows per day  
- Eliminating hand-rolled mechanisms for queues, retries, worker management, and basic telemetry  

KFM lessons:

- High-throughput autonomous refresh patterns  
- Elastic vs static worker pools  
- Python-native DAGs for complex ML workflows and LangGraph integration  

---

**🌍 Climate Policy Radar — From AWS Step Functions to Prefect (Planned)**  
File (planned): `docs/pipelines/case-studies/climate-policy-radar-prefect.md`  

Focus:

- Large-scale processing of ~25k+ climate-policy documents  
- Migration from Step Functions + Lambda + cron to Python-based Prefect flows  
- Multi-repo pipeline architecture owned by researchers and data scientists  

KFM lessons:

- How to empower domain experts (hydrology, climate, hazards, archaeology) to own flows  
- Why Python-native orchestration fits KFM’s multi-team structure  
- Patterns for large document-corpus processing (reports, PDFs, historical documents)  

---

## 🧭 Context

Case studies should be **deeply linked** into the rest of the KFM documentation so that:

- Governance reviewers can trace how standards are applied in real workflows.  
- Engineers can jump from case study → pipeline spec → standard → telemetry schema.  

Recommended cross-links for each case study:

- The root pipelines index: `docs/pipelines/README.md`  
- Relevant pipeline domains (e.g., `docs/pipelines/ai/README.md`, `docs/pipelines/atmo/README.md`)  
- Applicable standards (Markdown, governance, FAIR+CARE, OpenLineage)  
- Any associated provenance archives under `docs/archives/provenance/`  

---

## 🧪 Validation & CI/CD

Case studies are **documentation**, but they still participate in KFM’s CI/CD:

- **markdown-lint** — structural and style checks  
- **schema-lint** — validates YAML front-matter against doc schemas  
- **metadata-check** — ensures required references (SBOM, manifest, telemetry) are present  
- **footer-check** — verifies presence of governance links and version history  
- **provenance-check** — ensures case study versions align with `doc_uuid` and `semantic_document_id`  

Contribution checklist for new case studies:

1. **File & Path**  
   - Lives under `docs/pipelines/case-studies/` (or a subdirectory).  
   - `path` in front-matter matches the actual file location.  

2. **Metadata**  
   - Uses KFM-MDP v11.2.4-compliant front-matter.  
   - `version` and `last_updated` are set and maintained.  
   - `sbom_ref`, `manifest_ref`, `telemetry_ref`, `telemetry_schema` use correct relative paths.  
   - `governance_ref` points to the appropriate governance standard.  

3. **Formatting**  
   - Single H1, approved H2 headings, emojis aligned to KFM style. [oai_citation:1‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
   - Only tilde fences (`~~~`) inside this document to avoid nested-fence breaks.  
   - No decorative separators outside standard section breaks.  

4. **Content Quality**  
   - Includes all required conceptual sections (Overview, Legacy, Drivers, Target Architecture, Reliability & Governance, Lessons, Next Steps).  
   - Uses clear, precise, neutral language.  
   - Clearly distinguishes **facts**, **assumptions**, and **recommendations**.  

5. **Governance & Ethics**  
   - Describes how telemetry, lineage, and FAIR+CARE are implemented.  
   - Explicitly flags any handling of sensitive or Indigenous data and associated safeguards.  
   - References relevant standards (FAIR+CARE, security/SBOM, sovereignty where applicable).  

6. **Cross-Links**  
   - Links back to this index.  
   - Links to pipeline specs and standards used in the case study.  
   - References any associated audit or provenance documents.  

---

## ⚖ FAIR+CARE & Governance

Case studies are governance artifacts:

- They provide **evidence** of how FAIR+CARE, sovereignty, and reliability policies are applied.  
- They support **audits** by documenting real failures, migrations, and remediation patterns.  
- They guide future **pipeline reviews** by showing good and bad patterns in concrete contexts.  

Authors must:

- Avoid exposing sensitive or confidential operational data.  
- Use generalized or anonymized examples when describing incidents.  
- Clearly call out where Indigenous or culturally sensitive data would be involved and what protections are required.  

Governance reviewers may request:

- Additional detail on lineage, telemetry, or FAIR+CARE handling.  
- Follow-up documentation in standards or pipeline guides when a pattern should become canonical.  

---

## 🕰️ Version History

| Version  | Date       | Status                    | Summary                                                                 |
|---------:|------------|---------------------------|-------------------------------------------------------------------------|
| v11.2.4  | 2025-12-05 | Active · Under Expansion  | Upgraded to KFM-MDP v11.2.4; added governance footer, directory emojis, and CI alignment. |
| v11.0.1  | 2025-11-23 | Historical                | Initial pipelines case studies hub; established basic layout and goals. |

---

<div align="center">

📚 **Kansas Frontier Matrix — Pipelines Case Studies Index (v11.2.4)**  
Deterministic Pipelines · Evidence-Driven Governance · FAIR+CARE Case Narratives  

[⬅ Back to Pipelines Docs](../README.md) ·  
[📘 KFM Documentation Index](../../README.md) ·  
[⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>