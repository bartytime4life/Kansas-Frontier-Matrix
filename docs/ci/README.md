---
title: "🧪 Kansas Frontier Matrix — CI Documentation Index"
path: "docs/ci/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Council · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles: []

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "ci-docs-index"
audience:
  - "Reliability Engineering"
  - "Data Engineering"
  - "Catalog + Provenance Engineering"
  - "Security / Supply Chain"
  - "Governance Reviewers"

scope:
  domain: "ci-cd"
  applies_to:
    - "docs/ci/**"
    - ".github/workflows/**"
    - "schemas/**"
    - "policies/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (no secrets; provenance-safe)"
sensitivity_level: "None"
public_exposure_risk: "Low"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Reliability Council · FAIR+CARE Council"

doc_uuid: "urn:kfm:doc:ci:index:v11.2.6"
semantic_document_id: "kfm-ci-index-v11.2.6"
event_source_id: "ledger:kfm:doc:ci:index:v11.2.6"
commit_sha: "<latest-commit-hash>"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../security/supply-chain/README.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "fabricating approvals"
  - "fabricating provenance or policy decisions"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — CI Documentation Index**
`docs/ci/README.md`

**Purpose**  
Provide a governed entry point for Kansas Frontier Matrix (KFM) **CI/CD standards, patterns, and runbooks**:
deterministic builds, validation gates, provenance emission, supply-chain controls, and policy enforcement.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/CI%2FCD-Governed-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

This directory contains CI documentation that supports:

- **Deterministic, replayable pipelines** (same inputs + same config ⇒ same outputs + checksums).
- **Validation gates** for contracts, catalogs, schemas, provenance, and governance requirements.
- **Provenance-first delivery** (OpenLineage + PROV-O) and evidence artifacts attached to PRs.
- **Supply-chain integrity** (SBOM, attestations, signature verification) for build outputs.
- **FAIR+CARE governance controls** (rights, sensitivity, and sovereignty-aware policy gates).

### Key documents

- **AI codegen preview + provenance gates**  
  `docs/ci/ai-codegen-preview/README.md`

If additional CI patterns or runbooks are introduced under `docs/ci/`, they MUST be linked from this index.

---

## 🗂 Directory Layout

~~~text
📁 docs/
└── 📁 ci/
    ├── 📄 README.md                               — This index (governed)
    └── 📁 ai-codegen-preview/
        └── 📄 README.md                           — AI codegen PR pattern: deterministic preview + provenance gates
~~~

Recommended adjacent roots (referenced by CI docs):

~~~text
📁 .github/
└── 📁 workflows/                                 — CI workflows (policy-gated, deterministic, reproducible)

📁 schemas/                                       — JSON schemas and SHACL shapes used in validation gates
📁 policies/                                      — OPA/Rego policies, GE suites, and governance gate rules
📁 releases/                                      — Release packets (SBOM, attestations, signatures, manifests)
📁 mcp/
└── 📁 runs/                                      — Run logs and config snapshots for reproducibility
~~~

---

## 🧭 Context

KFM CI is not only “tests and lint.” It is a governed control plane that ensures:

- **Contracts are enforced** at the repo boundary (KFM-PDC v11).
- **Catalog integrity is preserved** (STAC/DCAT validation and linkage checks).
- **Provenance is complete and machine-verifiable** (OpenLineage + PROV-O).
- **Sensitive and sovereignty-affected data stays protected** (policy gates and escalation requirements).
- **Build outputs are auditable** (SBOM, attestations, signatures, checksum manifests).

CI must treat artifacts as governed evidence, not just build byproducts.

---

## 🧱 Architecture

A typical governed CI flow is composed of:

- **Pre-merge checks**
  - formatting and repo hygiene
  - schema validation (JSON/SHACL where applicable)
  - unit and integration tests
  - policy evaluation (OPA/Rego)
- **Evidence emission**
  - build manifests and checksums
  - validation reports (STAC/DCAT/PROV)
  - telemetry snapshots (when enabled)
- **Governance gating**
  - required-review routing based on rights/sensitivity/sovereignty flags
  - merge blocked unless all required gates pass
  - steward override only with signed justification artifact (when allowed)

---

## 📦 Data & Metadata

CI and preview builds SHOULD emit machine-readable artifacts, including:

- **Build manifests**
  - artifact list + checksums (sha256)
  - pinned toolchain and dependency locks
- **Validation reports**
  - STAC validation report
  - DCAT SHACL report
  - PROV-O validation report
  - contract validation summary (KFM-PDC)
- **Supply-chain artifacts**
  - SBOM (SPDX)
  - SLSA provenance/attestation
  - signature verification report (when used)
- **Telemetry (optional, governed)**
  - runtime, energy/CO2e, reliability budget indicators

All artifacts intended to justify merge decisions MUST be linkable from the PR checks or stored in governed run logs.

---

## 🧪 Validation & CI/CD

Minimum CI expectations for governed changes:

- `markdown-lint` and `metadata-check` (KFM-MDP compliance)
- schema validation for any emitted JSON/JSON-LD
- contract validation for pipeline interfaces (KFM-PDC)
- provenance validation for lineage artifacts (KFM-PROV)
- supply-chain verification (SBOM + attestation policy, when artifacts are built)
- policy evaluation (OPA/Rego gates)
- secret-scan and PII-scan (non-negotiable)

Where CI introduces new checks, they MUST be documented under `docs/ci/` and added to this index.

---

## 🧠 Story Node & Focus Mode Integration

CI artifacts can be treated as evidence inputs for Story Nodes and Focus Mode when they are:

- provenance-linked (PROV-O or OpenLineage IDs present),
- immutable or version-pinned (checksums and commit hashes recorded),
- rights-aware (no restricted content leaked through logs or previews).

Focus Mode MAY summarize CI outcomes and link to artifacts, but MUST NOT invent approvals or policy decisions.

---

## ⚖ FAIR+CARE & Governance

CI gates MUST enforce:

- license and rights compatibility checks (where applicable),
- sovereignty policy constraints and escalation rules,
- prohibition of secrets, PII, or restricted locations in logs, artifacts, or previews,
- clear separation between:
  - **facts** (validator outputs, attestations),
  - **interpretation** (risk assessments),
  - **policy** (required approvals and blocks).

Governance overrides (if allowed) MUST be accompanied by signed justification and preserved provenance.

---

## 🕰 Version History

| Version | Date       | Notes |
|-------:|------------|------|
| v11.2.6 | 2025-12-13 | Initial governed CI documentation index. |

---

<div align="center">

🧪 **Kansas Frontier Matrix — CI Documentation Index**  
Deterministic Pipelines · Verifiable Lineage · Policy-Gated Merges

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[📘 Docs Root](../README.md) ·
[🤖 AI Codegen Preview Pattern](./ai-codegen-preview/README.md) ·
[🏛 Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🔐 Supply-Chain Security](../security/supply-chain/README.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

