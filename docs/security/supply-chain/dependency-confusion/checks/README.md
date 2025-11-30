---
title: "🧪 KFM v11.2.2 — Dependency-Confusion Automated Checks (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/checks/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Supply-Chain Security Council"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/security-v3.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
doc_kind: "Security · Automated-Checks"
---

<div align="center">

# 🧪 **Dependency-Confusion Automated Checks**  
`docs/security/supply-chain/dependency-confusion/checks/README.md`

**Purpose:**  
Define all automated checks executed by KFM-CI to detect, block, and escalate  
dependency-confusion threats across every part of the KFM supply chain.  
These checks are deterministic, reproducible, hermetic, and produce immutable security evidence  
for long-term forensics, governance, and attestation workflows.

</div>

---

## 📘 Overview

KFM v11.2.2 implements **ten** automated check families across:

- CI/CD (GitHub Actions)  
- Developer pre-commit hooks  
- Local scanning tools (KFM-DTK)  
- ETL pipelines  
- Registry mirroring subsystems  
- Release workflows  
- SBOM & provenance infrastructure  

Each automated check ensures:

- Namespace collision prevention  
- Registry-isolation enforcement  
- Deterministic dependency pinning  
- Provenance validation (SLSA ≥ 3)  
- SBOM drift detection  
- Lockfile & digest reproducibility  
- Hermetic sandbox enforcement  
- Fallback activation in degraded conditions  

These protections **cannot be bypassed**.

---

## 🧬 Automated Check Families

### 1. 🛰️ **Namespace Collision Monitor**
Workflow: `namespace-monitor.yml`  
Detects collisions, shadow packages, typo-squatting, and dangerous upstream publishes.  
Evidence: `policy/evidence/namespace-scan.json`

---

### 2. 🔒 **Registry Isolation Checker**
Workflow: `registry-policy-check.yml`  
Ensures strict allow-list usage, mirror integrity, and no external registry contact.  
Evidence: `policy/evidence/registry-audit.json`

---

### 3. 🧩 **Dependency Pinning Validator**
Workflow: `dependency-integrity.yml`  
Validates exact pinning: (version + registry + digest), lockfile consistency, no floating versions.

---

### 4. 📦 **SBOM Drift Detector**
Workflow: `sbom-validate.yml`  
Validates digests, dependency graph consistency, and detects unapproved upgrades.  
Evidence: `policy/evidence/sbom-diff.json`

---

### 5. ✍️ **Signature & Provenance Verification**
Workflow: `slsa-attestation-verify.yml`  
Validates Cosign, GPG, provenance bundles, SLSA metadata, and artifact signatures.  
Evidence: `policy/evidence/attestation-verify.json`

---

### 6. 🧱 **Hermetic Sandbox Enforcement**
Workflow: `hermetic-build-guard.yml`  
Ensures builds run inside sealed, zero-network sandboxes using only pinned dependencies.

---

### 7. 🧯 **Fallback-Control Trigger Engine**
Workflow: `fallback-activation.yml`  
Activates Tier 1 fallback controls when mirrors, SBOM validation, or provenance checks degrade.  
See: `../policy/fallback-controls.md`

---

### 8. 🕵️ **Registry Anomaly Detection**
Workflow: integrated into multiple scans  
Detects timing anomalies, digest drift, publisher-identity drift, TLS issues, metadata mismatches.  
See: `registry-anomaly-detection.md`

---

### 9. 🧬 **Provenance Hooks (Multi-Stage)**
Workflow: integrated  
Executes PF-Hook, FT-Hook, BT-Hook, AP-Hook, SA-Hook, SBOM-Hook, RS-Hook across build stages.  
See: `provenance-hooks.md`

---

### 10. 🧹 **Pre-Commit Developer Validation**
Executed before commit (mirrors CI on workstation).  
Ensures early detection of pinning drift, registry leaks, SBOM mismatches, signature failures.  
See: `pre-commit-rules.md`

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
    ├── 📄 README.md                     # This file — automated checks overview
    ├── 📄 ci-validation-rules.md
    ├── 📄 provenance-hooks.md
    ├── 📄 registry-anomaly-detection.md
    ├── 📄 pre-commit-rules.md
    └── 📄 local-scan-guidance.md
~~~

---

## 🕰️ Version History

| Version | Date       | Notes |
|--------|------------|-------|
| v11.2.2 | 2025-11-30 | Expanded to 10 check families, aligned with new check docs, updated directory tree |

---

<div align="center">

🛡️ [Policy Overview](../policy/README.md) • 🧬 [Provenance Hooks](./provenance-hooks.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
