---
title: "🛰️ KFM v11.2.2 — Dependency-Confusion Evidence Archive (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/evidence/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Security Council · FAIR+CARE"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/security-v3.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
doc_kind: "Evidence · Security"
ontology_protocol_version: "KFM-OP v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"
pipeline_contract_version: "KFM-PDC v11"
---

<div align="center">

# 🛰️ **Dependency-Confusion · Evidence Archive (KFM v11.2.2)**  
`docs/security/supply-chain/dependency-confusion/policy/evidence/README.md`

**Purpose:**  
Provide a consolidated, immutable evidence archive for all automated and manual findings  
related to dependency-confusion threat detection, namespace collisions, registry audit trails,  
SBOM drift logs, and SLSA attestation verification.  
This directory is a **forensic-grade** evidence vault, consumed by KFM-CI, Security Council,  
and long-term supply-chain analytics tooling.

</div>

---

## 📘 Overview

This directory stores **machine-readable security evidence** produced by:

- 🛰️ Namespace-scan automation (`namespace-monitor.yml`)  
- 🧬 SBOM drift detection (`sbom-diff-check.yml`)  
- 🔐 Registry-policy audits (`registry-audit.yml`)  
- 🗃️ SLSA proof-chain verification  
- 📦 Dependency-pin integrity checks  
- 🧪 Sandbox/hardening audit results  

All files in this folder are:

- **Immutable** (governance-protected; changes require Security Council approval)  
- **Schema-validated**  
- **Timestamped**  
- **Provenance-linked** (PROV-O lineage)  
- **Dependency-confusion–optimized** (focus: namespace collisions + shadowing attempts)  

The KFM v11 security model treats this directory as a root-of-truth for evidence trails.

---

## 📊 Evidence Types Stored Here

### 1. 🛰️ Namespace Scan Results (`namespace-scan.json`)
Contains:

- Discovered public-package collisions  
- Suspicious namespace registrations  
- Rogue shadow-package attempts  
- Registry timestamp deltas  
- Attacker-pattern detection (AI-assisted)  

### 2. 🧬 SBOM Drift Logs (`sbom-diff.json`)
Tracks:

- Hash deviations from last sealed build  
- Artifact inconsistencies  
- Unexpected version changes  
- Potential injection via build pipeline  
- Provenance mismatch events  

### 3. 🔐 Registry Audit Logs (`registry-audit.json`)
Documents:

- Registry allow-list & mirror integrity  
- Unauthorized outbound resolution attempts  
- Forbidden public-registry hits  
- SLSA-metadata compliance  

### 4. 🧩 Additional Machine Evidence
May include:

- `attestation-verify.json` — SLSA attestation chain results  
- `shadow-map.json` — Map of vulnerable namespace ranges  
- `pin-integrity.json` — Integrity snapshot of all locked dependencies  
- `alerts.json` — Aggregated CI security alerts  

---

## 🗂️ Directory Layout

~~~text
📁 evidence/
├── 🛰️ namespace-scan.json      # Automated namespace collision scan results
├── 🧬 sbom-diff.json            # SBOM drift log from secure builds
├── 🔐 registry-audit.json       # Registry validation & policy adherence
├── 🧾 attestation-verify.json   # Optional: SLSA v3+ attestation verification logs
├── 🗺️ shadow-map.json           # Optional: namespace vulnerability mapping
└── 📄 README.md                 # This documentation file
~~~

---

## 🧪 CI/CD Validation

This directory participates in the following workflows:

- `namespace-monitor.yml`  
- `sbom-validate.yml`  
- `slsa-attestation-verify.yml`  
- `security-evidence-lint.yml`  
- `governance-policy-check.yml`  

Failures in any evidence file:

1. Block merges  
2. Trigger Security Council review  
3. Generate a “Security Evidence Exception Record”  
4. Require updated forensic evidence  

---

## 🕰️ Version History

| Version | Date | Notes |
|---------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial release of v11.2.2-compliant evidence archive README |

---

<div align="center">

🔐 [Supply-Chain Security](../../../README.md) • 🛡️ [Dependency-Confusion Policy](../README.md) • 🧭 [Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

