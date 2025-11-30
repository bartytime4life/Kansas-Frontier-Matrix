---
title: "🧪 KFM v11.2.2 — Dependency-Confusion Automated Checks (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/checks/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Supply-Chain Security Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/security-v3.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

doc_kind: "Security · Automated-Checks"
intent: "supply-chain-detection · automated-governance"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Infrastructure Protection"
classification: "Security · Automated Detection"
sensitivity: "Security-Sensitive (non-personal)"
sensitivity_level: "High"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "High"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Annual review"
sunset_policy: "Superseded when v11.3 automated checks are released"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/checks/README.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/checks/README.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:checks:index:v11.2.2"
semantic_document_id: "kfm-depconf-checks-index-v11.2.2"
event_source_id: "ledger:depconf.checks.index.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "timeline-generation"
  - "diagram-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "unverified-architectural-claims"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧬 Automated Check Families"
    - "🕰️ Version History"
---

<div align="center">

# 🧪 **Dependency-Confusion Automated Checks**  
`docs/security/supply-chain/dependency-confusion/checks/README.md`

**Purpose:**  
Document all automated CI, pre-commit, and local scanning checks that guard KFM’s  
supply-chain from dependency-confusion threats, namespace collisions, registry manipulation,  
SBOM drift, and provenance failures.

</div>

---

## 📘 Overview

KFM v11.2.2 implements **ten** automated check families across CI/CD, local scans,  
ETL pipelines, and release infrastructure. Each check enforces:

- Namespace collision detection  
- Registry isolation integrity  
- Deterministic pinning  
- Provenance + signature validity (SLSA ≥ 3)  
- SBOM alignment  
- Artifact/digest reproducibility  
- Hermetic sandbox compliance  
- Fallback activation on degraded conditions  

These protections **cannot** be bypassed or disabled.

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
├── 📁 policy/
│   ├── 📄 README.md
│   ├── 📄 rules.md
│   ├── 📄 registry-isolation.md
│   ├── 📄 signature-requirements.md
│   ├── 📄 fallback-controls.md
│   ├── 📄 exceptions.md
│   ├── 📄 incidents.md
│   └── 📂 evidence/
│       ├── 🛰️ namespace-scan.json
│       ├── 🧬 sbom-diff.json
│       ├── 🔐 registry-audit.json
│       └── 🧾 attestation-verify.json
└── 📁 checks/
    ├── 📄 README.md                 # This file
    ├── 📄 ci-validation-rules.md
    ├── 📄 provenance-hooks.md
    ├── 📄 registry-anomaly-detection.md
    ├── 📄 pre-commit-rules.md
    └── 📄 local-scan-guidance.md
~~~

---

## 🧬 Automated Check Families

### 1️⃣ 🛰️ Namespace Collision Monitor  
Workflow: `namespace-monitor.yml`  
Detects public/private naming conflicts, shadow packages, typo-squats, and suspicious upstream publishes.  
Produces: `policy/evidence/namespace-scan.json`

---

### 2️⃣ 🔒 Registry Isolation Checker  
Workflow: `registry-policy-check.yml`  
Ensures strict registry allow-listing and mirror integrity.  
Produces: `policy/evidence/registry-audit.json`

---

### 3️⃣ 🧩 Dependency Pinning Validator  
Workflow: `dependency-integrity.yml`  
Validates exact version + registry + digest pinning. Rejects floating versions.

---

### 4️⃣ 📦 SBOM Drift Detector  
Workflow: `sbom-validate.yml`  
Checks dependency graph equivalence, hash mismatches, and drift.  
Produces: `policy/evidence/sbom-diff.json`

---

### 5️⃣ ✍️ Signature & Provenance Verification  
Workflow: `slsa-attestation-verify.yml`  
Validates Cosign/GPG signatures and SLSA metadata.  
Produces: `policy/evidence/attestation-verify.json`

---

### 6️⃣ 🧱 Hermetic Sandbox Enforcement  
Workflow: `hermetic-build-guard.yml`  
Ensures zero-network, sealed-environment builds.

---

### 7️⃣ 🧯 Fallback-Control Trigger Engine  
Workflow: `fallback-activation.yml`  
Automatically activates fallback Tier 1 during registry/mirror degradation.  
See: `../policy/fallback-controls.md`

---

### 8️⃣ 🕵️ Registry Anomaly Detection  
Detects timing anomalies, digest drift, publisher identity changes, metadata inconsistencies.  
See: `registry-anomaly-detection.md`

---

### 9️⃣ 🧬 Multi-Stage Provenance Hooks  
PF-Hook → FT-Hook → BT-Hook → AP-Hook → SA-Hook → SBOM-Hook → RS-Hook  
See: `provenance-hooks.md`

---

### 🔟 🧹 Pre-Commit Developer Validation  
Local enforcement of lockfile integrity, registry isolation, SBOM/digest match, and signature validity.  
See: `pre-commit-rules.md`

---

## 🕰️ Version History

| Version  | Date       | Notes                                                          |
|----------|------------|----------------------------------------------------------------|
| v11.2.2  | 2025-11-30 | Directory layout moved up; fully extended metadata; updated for 10 check families |
| v11.2.1  | 2025-10-20 | Added registry anomaly detection + provenance hook expansion   |
| v11.2.0  | 2025-09-10 | Initial automated-checks framework                             |

---

<div align="center">

🛡️ [Policy Overview](../policy/README.md) • 🧬 [Provenance Hooks](./provenance-hooks.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
