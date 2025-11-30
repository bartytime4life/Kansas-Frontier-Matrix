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
Document all automated KFM-CI checks that detect, prevent, block, and escalate  
dependency-confusion threats across the entire KFM supply-chain.  
These checks are deterministic, reproducible, and designed to protect all pipelines, registries,  
lockfiles, and artifacts from namespace shadowing or malicious upstream interference.

</div>

---

## 📘 Overview

The KFM dependency-confusion protections consist of **seven automated check families**,  
executed continuously across:

- CI/CD (GitHub Actions)  
- Developer pre-commit hooks  
- ETL & ingestion pipelines  
- Release workflows  
- Registry mirroring infrastructure  

Each automated check contributes to:

- Prevention of rogue package substitution  
- Early detection of namespace collisions  
- Enforcement of registry isolation  
- SLSA provenance verification  
- SBOM drift detection  
- Lockfile integrity and reproducibility  
- Evidence generation for long-term forensics  

These checks cannot be disabled or bypassed.

---

## 🧬 Automated Check Families

### 1. 🛰️ **Namespace Collision Monitor**
Workflow: `namespace-monitor.yml`

Monitors for:

- Public-package namespace collisions  
- Suspicious first-time publishes  
- Rogue shadow attempts  
- Registry typo-squatting patterns  
- High-risk namespace blocks

Produces evidence:  
`policy/evidence/namespace-scan.json`

---

### 2. 🔒 **Registry Isolation Checker**
Workflow: `registry-policy-check.yml`

Enforces:

- Strict allow-list  
- No outbound registry access  
- No implicit fallback to public registries  
- Mirror integrity verification  

Produces evidence:  
`policy/evidence/registry-audit.json`

---

### 3. 🧩 **Dependency Pinning Validator**
Workflow: `dependency-integrity.yml`

Ensures:

- Exact pinning (version + registry + hash)  
- Lockfile consistency  
- No floating or wildcard versioning  
- No unauthorized registry references  

Blocks on any drift.

---

### 4. 📦 **SBOM Drift Detector**
Workflow: `sbom-validate.yml`

Verifies:

- Artifact digests  
- SBOM inclusion  
- Consistency with pinned dependency graph  
- Mirror reproducibility  

Produces evidence:  
`policy/evidence/sbom-diff.json`

---

### 5. ✍️ **Signature & Provenance Verification**
Workflow: `slsa-attestation-verify.yml`

Validates:

- Cosign signatures  
- GPG signatures  
- SLSA v3+ provenance attestations  
- Artifact immutability  

Produces evidence:  
`policy/evidence/attestation-verify.json`  
(if enabled)

---

### 6. 🧱 **Hermetic Sandbox Enforcement**
Workflow: `hermetic-build-guard.yml`

Ensures builds:

- Have zero outbound network access  
- Resolve only from internal mirrors  
- Execute inside sealed sandboxes  
- Use sealed dependency snapshots  

Rejects any environment leakage.

---

### 7. 🧯 **Fallback-Control Trigger Engine**
Workflow: `fallback-activation.yml`

Triggered when:

- Mirrors fail  
- Namespace monitor degrades  
- SBOM drift cannot be resolved  
- Signature chain missing  

Automatically activates Tier 1 fallback controls  
(see: `policy/fallback-controls.md`).

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
    └── 📄 README.md     # This file — automated check documentation
~~~

---

## 🕰️ Version History

| Version | Date | Notes |
|--------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial creation of automated checks registry |

---

<div align="center">

🛡️ [Policy Overview](../policy/README.md) • 📏 [Rules](../policy/rules.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

