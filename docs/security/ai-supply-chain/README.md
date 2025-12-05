---
title: "🔐 KFM v11.2.4 — AI Supply-Chain Security Standards Index"
path: "docs/security/ai-supply-chain/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security & Supply-Chain Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x security-contract compatible"
status: "Active / Mandatory"

doc_kind: "Standards Index"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "security/ai-supply-chain"
  applies_to:
    - "ci-cd"
    - "github-actions"
    - "ai-agents"
    - "rag-systems"
    - "langgraph-workers"
    - "docs-automation"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-sha>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/security-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/security/ai-supply-chain-standards-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:security:ai-supply-chain-index-v11.2.4"
semantic_document_id: "kfm-doc-security-ai-supply-chain-index-v11.2.4"
event_source_id: "ledger:kfm:doc:security:ai-supply-chain-index"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🔐 KFM v11.2.4 — AI Supply-Chain Security Standards Index  
`docs/security/ai-supply-chain/README.md`

**Purpose:**  
Serve as the canonical index for all KFM AI supply-chain security standards — including prompt-injection defense, AI-agent constraints, CI/CD isolation, and telemetry — so every AI-assisted workflow in the repo is deterministic, auditable, and safe against attacker-controlled prompts.

</div>

---

## 📘 Overview

AI now participates in nearly every stage of KFM’s software and data supply chain:

- GitHub Actions workflows that use LLMs for code review and triage.  
- LangGraph/CLI agents that analyze diffs, configs, and logs.  
- Documentation and Story Node generators that consume repository content.  

This index:

- Defines the **documentation layout** for AI supply-chain security standards.  
- Explains how those standards plug into CI/CD, SBOM, provenance, and governance.  
- Points to the **Prompt-Injection Defense Standard** and related policy docs.  
- Establishes testing and telemetry expectations for all AI-assisted workflows.  

All AI-related security standards under `docs/security/ai-supply-chain/` **must**:

- Use KFM-MDP v11.2.4-compliant front matter and headings.  
- Declare scope and affected modules (CI, agents, docs pipelines, etc.).  
- Link back to this index and to the main Security index under `docs/security/README.md`.

---

## 🗂️ Directory Layout

```text
📂 docs/security/
└── 📂 ai-supply-chain/
    ├── 📄 README.md                                   # 🔐 AI Supply-Chain Security Standards Index (this file)
    └── 📂 prompt-injection-defense/                   # 🛡️ Prompt-Injection Defense Standard
        ├── 📄 README.md                               # 🛡️ Prompt-Injection Defense for CI/CD & AI Agents
        ├── 📂 policy/                                 # 📜 Normative policies & behavior constraints
        │   ├── 📄 boundaries.md                       # Prompt boundary & context isolation rules
        │   ├── 📄 agent-constraints.md                # Detailed AI agent behavior constraints
        │   └── 📄 ci-isolation.md                     # CI isolation & runner policies
        ├── 📂 patterns/                               # 🧪 Attack patterns & sanitization tests
        │   ├── 📂 detected-attacks/                   # Real / simulated attack write-ups
        │   └── 📂 sanitization-tests/                 # Test fixtures for sanitizer
        └── 📂 checklists/                             # ✅ Operational checklists
            ├── 📄 onboarding.md                       # New-repo AI-security onboarding
            └── 📄 audit.md                            # Periodic audit & review checklist
```

Author rules:

- New AI supply-chain standards must be added as subdirectories under `docs/security/ai-supply-chain/`, each with its own `README.md`.  
- Each new standard must clearly identify:
  - Affected CI workflows (`.github/workflows/*.yml`).  
  - Affected runtime modules (`src/security/...`, `src/ci/...`).  
  - Required telemetry and provenance hooks.

---

## 🧭 Context

This index sits in the broader KFM stack:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode → **AI-assisted CI/CD & governance loops**

AI supply-chain standards govern *how AI can participate* in:

- **CI/CD**: GitHub Actions, build/test/release jobs, automated triage.  
- **Security & compliance**: static analysis, SBOM checks, policy validation.  
- **Documentation & Story Nodes**: AI-generated docs, summaries, and geoethical overlays.  

Key design principles:

- **AI is an assistant, not an operator**: AI may propose but never directly execute.  
- **Untrusted text is always data**: PRs, issues, docs, and logs are non-executable inputs.  
- **Security-first composition**: any AI invocation must fit within a hardened, audited pipeline.  

The **Prompt-Injection Defense Standard** under this index is the first mandatory standard in this space and is considered normative for all new AI supply-chain work.

---

## 🧱 Architecture

From an architecture perspective, this index constrains:

- `.github/workflows/*` — CI, CD, and AI-assisted workflows.  
- `src/security/*` — reusable security modules (sanitizers, gates, classifiers).  
- `src/ci/*` or `src/tools/*` — helper scripts that integrate AI into pipelines.  

### 1. Module boundaries

Typical module layout influenced by this index:

- `src/security/prompt_sanitizer/`
  - Implements text sanitization and provenance labeling for untrusted inputs.  
- `src/security/ai_policy/`
  - Houses allowlists, intent classifiers, and AI agent constraints.  
- `src/ci/ai_review/`
  - Contains wrappers for AI review jobs invoked from workflows.  

Standards under this index must:

- Specify expected module paths and interfaces.  
- Avoid embedding AI logic directly in workflows — prefer reusable modules in `src/security/` or `src/ci/`.  
- Ensure that **all AI access to untrusted repo content** goes through these hardened modules.

### 2. Relationship to other security components

- **Supply-chain & SLSA standards**:
  - AI decisions must be included in provenance and SBOM flows.  
- **Geospatial & geoethical standards**:
  - Any AI handling geospatial or Story Node content must respect masking, access labels, and sovereignty rules.  

---

## 🧪 Validation & CI/CD

AI supply-chain standards are enforced via CI/CD. At minimum, repos that use AI must have workflows that:

- Validate that AI-related jobs:
  - Use **read-only permissions** and dedicated sandbox tokens.  
  - Route untrusted text through `src/security/prompt_sanitizer/`.  
  - Do **not** pipe AI output into `run:` steps or shells.  
- Run policy and patterns tests from:
  - `prompt-injection-defense/patterns/sanitization-tests/`.  
  - Any additional test suites added under this index.  
- Validate that telemetry events follow the `telemetry_schema` in front matter.

Recommended CI tasks:

- **Workflow linting** for AI-related anti-patterns.  
- **Red-team simulations** that inject known attacks into PRs/issues.  
- **Dependency checks** for AI/LLM SDKs and tools referenced by workflows.

Any new AI supply-chain standard must define:

- Required CI checks.  
- Example workflows.  
- Failure conditions that must block merges.

---

## 📦 Data & Metadata

AI supply-chain security is also a metadata and provenance problem.

### 1. Telemetry

This index references:

- `telemetry_ref`: aggregated security AI telemetry (per release).  
- `telemetry_schema`: schema describing:
  - AI invocation events.  
  - Prompt-sanitization stats.  
  - Blocked prompt-injection attempts.  
  - Energy/CO₂ estimates for AI jobs, where applicable.

Standards under this index must:

- Define the metrics they require (names, types, tags).  
- Keep cardinality under control (e.g., aggregate per workflow rather than per commit).  

### 2. Provenance

AI-related decisions must be part of the KFM PROV chain:

- Each AI job in CI should be representable as a `prov:Activity`.  
- Inputs (PR text, code, configs) and outputs (reviews, docs) should be `prov:Entity` records.  
- Agents (AI models, wrappers) should be `prov:Agent` entries, including model version and configuration.

Where appropriate, standards should specify:

- How AI interactions are recorded in SLSA attestations.  
- How policy versions (including this document’s `doc_uuid` and `version`) are attached to build provenance.

---

## ⚖ FAIR+CARE & Governance

AI in the supply chain is not just a technical risk; it is also a governance and ethical concern.

- **FAIR**
  - *Findable*: AI policies, workflows, and logs are discoverable for audits and incident response.  
  - *Accessible*: Security standards and telemetry are available (with appropriate access control) to maintainers and governance bodies.  
  - *Interoperable*: Uses open standards and schemas for telemetry and provenance.  
  - *Reusable*: Hardened AI workflow patterns can be ported across repos and projects.  

- **CARE**
  - *Collective Benefit*: Secures KFM contributors, communities, and downstream users from AI-mediated supply-chain compromise.  
  - *Authority to Control*: Governance bodies define allowed AI behaviors; AI cannot override or bypass them.  
  - *Responsibility*: Clear review cadences and incident-reporting expectations put accountability on maintainers and security teams.  
  - *Ethics*: AI is constrained to assist with safe, transparent tasks; it cannot silently change code, data, or narratives.

Governance expectations:

- Changes to AI supply-chain standards (including this index) require review by:
  - Security Engineering.  
  - MCP Council.  
  - FAIR+CARE Compliance, where behavior touches data governance.  

### 📚 Reference Standards & Resources (Footer)

- [FAIR Principles](https://www.go-fair.org/fair-principles/)  
- [CARE Principles for Indigenous Data Governance](https://www.gida-global.org/care)  
- [KFM Governance Framework](../../standards/governance/ROOT-GOVERNANCE.md)  
- [KFM Markdown Authoring Protocol — KFM-MDP v11.2.4](../../standards/kfm_markdown_protocol_v11.2.4.md)  
- [Prompt-Injection Defense Standard](./prompt-injection-defense/README.md)  
- [Security Index](../README.md)  

These references form the baseline **footer** for AI supply-chain security docs; reuse and extend as appropriate.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                                                     |
|--------:|------------|-------------------|-------------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Mandatory | Initial AI Supply-Chain Security Standards Index aligned with KFM-MDP v11.2.4 and CI/CD. |

Future revisions must:

- Add new AI supply-chain standards as subdirectories and link them here.  
- Update telemetry and provenance expectations when schemas evolve.  
- Keep this index synchronized with global security and governance standards.

---

<div align="center">

🔐 **KFM v11.2.4 — AI Supply-Chain Security Standards Index**  
Secure-by-Design · Governance-First · Auditable AI Workflows  

[📘 Docs Root](../../..) · [🔐 Security Index](../README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>