---
title: "⚠️ KFM v11.2.2 — Dependency-Confusion Exception Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/exceptions.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Security Council · FAIR+CARE"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/security-v3.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
doc_kind: "Security · Exceptions"
ontology_protocol_version: "KFM-OP v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"
pipeline_contract_version: "KFM-PDC v11"
---

<div align="center">

# ⚠️ **Dependency-Confusion Exception Registry**  
`docs/security/supply-chain/dependency-confusion/policy/exceptions.md`

**Purpose:**  
Record and justify **Security Council–approved exceptions** to the KFM dependency-confusion  
defense policy.  
All exceptions must remain temporary, tightly scoped, and bound to explicit mitigation measures.  
This file is immutable except through governance-approved PRs.

</div>

---

## 📘 Overview

Under KFM v11.2.2, all dependency sources *must* be:

- Fully pinned (version + hash + registry)  
- SLSA-attested  
- SBOM-sealed  
- Namespace-clean  
- Mirror-isolated  

However, certain specialized cases (legacy libraries, third-party research modules, compatibility  
layers) may require controlled exceptions.

**No exception is granted automatically.**  
Each must be:

- Submitted as a Security Exception Request (SER)  
- Reviewed by Supply-Chain Security Council  
- Approved by majority vote  
- Time-bounded (expiration required)  
- Mitigated with additional controls  
- Logged in this file  

---

## 🧭 Exception Format (Required)

Each exception entry must include:

```yaml
id: EX-DC-XXXX
package: "registry/package-name"
justification: >
  Clear technical necessity, referencing reproducibility evidence and
  compatibility constraints.
risk_assessment:
  severity: low|medium|high
  likelihood: low|medium|high
  compensating_controls:
    - "hash pinning"
    - "SLSA override attestation"
    - "sandbox execution"
scope:
  allowed_versions:
    - "1.2.3"
    - "1.2.4"
  registries:
    - "https://internal-mirror.example"
expiration: "YYYY-MM-DD"
approved_by:
  - name: "Security Council Member"
    role: "Council"
date_approved: "YYYY-MM-DD"
```

---

## 📂 Current Approved Exceptions (v11.2.2)

> ⚠️ *This registry starts empty for v11.2.2. Add entries below this line only through Security Council governance PRs.*

_No active exceptions._

---

## 🔐 Exception Lifecycle Rules

### 1. ⏳ Mandatory Expiration
Each exception must define a specific expiration date (≤ 90 days).

### 2. 🔄 Renewal Requirements
Renewals require:

- Fresh SER  
- Updated justification  
- New risk assessment  
- Proof of attempted remediation  

### 3. 🛠️ Automatic Revocation
Exceptions are automatically revoked when:

- A secure alternative is available  
- The upstream package is patched  
- A name collision emerges  
- SBOM drift is detected  
- A mirror now supports the dependency  

### 4. 🧪 CI Enforcement
CI validates:

- Exception IDs  
- Hash-pin matches  
- Registry allow-list conformity  
- Namespace scan compatibility  

Any violation triggers merge-blocking.

---

## 🕰️ Version History

| Version | Date | Notes |
|--------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial creation of exception registry |

---

<div align="center">

🔐 [Supply-Chain Security](../../README.md) • 🛡️ [Dependency-Confusion Policy](./README.md) • 🧭 [Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

