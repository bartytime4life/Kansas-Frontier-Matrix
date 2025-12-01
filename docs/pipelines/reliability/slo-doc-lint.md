---
title: "🧪 KFM v11 — Doc-Lint SLO & Error-Budget Policy (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/reliability/slo-doc-lint.md"
version: "v11.2.3"
last_updated: "2025-12-01"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability + Docs Council"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x docs CI compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../releases/v11.2.3/reliability-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/reliability-doclint-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

classification: "Internal Documentation Reliability Standard"
sensitivity: "Low"
sensitivity_level: "None"
public_exposure_risk: "Low"
machine_extractable: true
immutability_status: "version-pinned"

jurisdiction: "Kansas / United States"
ttl_policy: "12 months"
sunset_policy: "Superseded by next doc-lint revision"

accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Aware · Documentation Integrity"
care_label_detail: "CARE-Level 1 — Documentation Stewardship"

header_profile: "standard"
footer_profile: "standard"

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-sequence-v1"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Reliability"
  documentation: "Governed Clarity · Deterministic Structure"
  reliability: "SLO-Driven · Provenance-Enforced"
  governance: "Accountable · Transparent · Ethical"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "heading-registry-check"
  - "footer-check"
  - "frontmatter-check"
  - "fence-closure-check"
  - "directory-layout-check"
  - "provenance-check"
  - "telemetry-schema-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"
  - "unverified-architectural-claims"
  - "narrative-fabrication"

heading_registry:
  approved_h2:
    - "🧭 Purpose & Scope"
    - "🧾 Directory Layout"
    - "🎯 SLO"
    - "🧮 Error Budget"
    - "🚦 Merge Gating"
    - "🔁 Auto-Remediation Playbook"
    - "📈 Telemetry"
    - "🧰 CI Wiring"
    - "✅ Compliance Gates"
    - "🔐 Governance"

metadata_profiles:
  - "FAIR+CARE"
  - "OpenTelemetry"
  - "PROV-O"
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "KFM-Governance-Metadata"

provenance_chain:
  - "docs/pipelines/reliability/slo-doc-lint.md@v11.2.2"
  - "docs/pipelines/reliability/slo-doc-lint.md@v11.0.0"
  - "docs/pipelines/reliability/patterns/README.md@v10.4.3"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

<div align="center">

# 🧪 Doc-Lint SLO & Error-Budget Policy  
Documentation Reliability ≥ 99% — Deterministic, Governed, FAIR+CARE-Aligned

</div>

---

## 🧭 Purpose & Scope

This policy defines the **documentation reliability standard** for the Kansas Frontier Matrix (KFM).  
It establishes:

- The **SLO** for clean, deterministic markdown builds  
- The **error-budget contract** governing failure tolerance  
- The **merge gating controls** activated as budget burns  
- Required **telemetry**, **CI wiring**, and **auto-remediation workflows**  
- The **directory structure** and governance expectations for doc reliability components  

Scope:

- Applies to **all Markdown** under `docs/**` and any `README.md` within `web/**`  
- Applies to **CI pipelines** responsible for linting, validating, and enforcing structure  
- Applies to **contributors and reviewers** involved in documentation changes  
- Governs SLO behavior for **v10.x → v11.x compatibility window**  

This is a **governed, enforceable reliability contract**.

---

## 🧾 Directory Layout

docs/pipelines/reliability/  
├── 📄 README.md  
│       Reliability overview + root specs  
├── 🎯 slo-error-budgets.md  
│       Global SLO thresholds and error-budget policy  
├── 🧪 slo-doc-lint.md  
│       This file — doc-lint SLO + error-budget contract  
│  
├── 🧰 ci/  
│   ├── 🧾 docs-lint-ruleset.yaml  
│   │       Rule config: fences, frontmatter, badges, footers, mermaid  
│   └── 📊 dashboards/  
│       └── 📈 reliability-docs.json  
│               SLO dashboards (OpenTelemetry views)  
│  
└── 📊 reports/  
    ├── 📉 weekly-pareto.md  
    │       Auto-generated failing-rule Pareto  
    └── 🗂️ rca/  
        └── 📝 2025-12-doclint-breach.md  
                RCA template for documentation SLO breaches  

---

## 🎯 SLO

- Target: **99%+ first-pass doc-lint success**  
- Window: **30 days**  
- Counted failures: any structure or formatting violation including:
  fence closure, footer, YAML correctness, badge block, directory layout, mermaid closure  

---

## 🧮 Error Budget

Budget: **1%** failure rate  
Formula:  

burn_rate = failed_doclint_prs / total_prs_with_docs_changes  

Exclusions: infra outages and upstream breakages requiring RCA + pin

---

## 🚦 Merge Gating

Burn ≥ 50%:  
Require additional Docs Council reviewer  

Burn ≥ 100% (breach):  
Block merges, require docs:lint green, enable mdfmt verification and quick lint, restrict auto-merge  

---

## 🔁 Auto-Remediation Playbook

Weekly Pareto analysis  
Auto-fix top failing rules  
Refresh templates  
Comment-bot education  
RCA during breach  

---

## 📈 Telemetry

Emit doclint pass/fail metrics  
Track SLO pass rate and burn rate  
Dashboard location:  
dash/reliability-docs.json  

Warn threshold: < 99.5%  
Critical threshold: < 99%  

---

## 🧰 CI Wiring

jobs: docs:lint, docs:lint:quick, docs:lint:auto-fix  
required_checks: docs:lint  
hooks: mdfmt, frontmatter-verify, footer-verify, fence-guard, mermaid-close-check  

---

## ✅ Compliance Gates

Markdown MUST pass:  
frontmatter schema  
fence closure  
mermaid closure  
directory layout validity  
footer triple-link  
badge block (governed READMEs)  

---

## 🔐 Governance

Docs Council: policy owner  
Reliability Engineering: SLO owner  
Infra Team: CI enforcement  

Changes require 2-week shadow trial before activation.

---

[📘 Docs Root](../../..) · [🧱 Reliability Index](../README.md) · [🛡 Governance](../../standards/governance/ROOT-GOVERNANCE.md)