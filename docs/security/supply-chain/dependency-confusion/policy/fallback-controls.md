---
title: "🧯 KFM v11.2.2 — Dependency-Confusion Fallback Controls (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/fallback-controls.md"
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
ontology_protocol_version: "KFM-OP v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"
pipeline_contract_version: "KFM-PDC v11"
doc_kind: "Security · Fallback"
---

<div align="center">

# 🧯 **Dependency-Confusion — Fallback Controls**  
`docs/security/supply-chain/dependency-confusion/policy/fallback-controls.md`

**Purpose:**  
Define the *secondary and emergency controls* activated when primary dependency-confusion  
defenses fail, degrade, or become temporarily unavailable.  
Fallback controls ensure KFM supply-chain integrity remains intact even during partial outages,  
registry failures, mirror downtime, or anomaly escalations.

</div>

---

## 📘 Overview

KFM v11.2.2 implements a multilayered defense strategy:

**Primary Controls → Enforcement Rules (rules.md)**  
**Fallback Controls → This document**  
**Ultimate Safeguards → Emergency Supply-Chain Lockdown (ESCL)**

Fallback controls activate automatically in CI/CD, ETL environments, and local dev overlays  
when standard registry, SBOM, SLSA, or namespace-monitor protections enter **degraded mode**.

Fallback controls must be:

- Deterministic  
- Temporary  
- Logged in evidence trails  
- Automatically reverted after normal operation resumes  
- Fully FAIR+CARE compliant  

---

## 🧯 Tier 1 — Automated Fallback Controls (Immediate Activation)

These controls activate automatically when CI/CD detects:

- Mirror unreachable  
- Registry latency thresholds exceeded  
- SBOM/digest mismatch  
- Namespace-monitor failure  
- Attestation chain delay or missing metadata  

### 1. 🔐 Hard-Pinned Dependency Freezing
- Lockfiles become **read-only**  
- Only dependencies present in last-sealed SBOM are allowed  
- No updates permitted  
- “Freeze mode” is logged in evidence directory  

### 2. 🧱 Registry Circuit Breaker (Fail Closed)
If internal mirrors become unreachable:

- External registries remain blocked  
- Builds switch to **local artifact cache only**  
- All unrecognized packages are rejected  

### 3. 🧪 SBOM Drift Guard
If SBOM validation fails:

- All dependency-resolve actions are halted  
- Build runs only with previously validated dependency snapshots  

### 4. 🛰️ Namespace Monitor Fallback Mode
If namespace scanning service degrades:

- Previously known dangerous namespaces are preemptively blocked  
- Only allow-list names may be resolved  

---

## 🧯 Tier 2 — Semi-Manual Fallback Controls (Security-Council Trigger)

Triggered when automated controls require human oversight.

### 1. 🛑 Emergency Package Hold (EPH)
Security Council may freeze:

- Entire ecosystems (pip/npm/cargo)  
- Specific namespaces  
- Entire registries  

### 2. 📦 Manual Dependency Verification Queue
All dependency changes enter a manual-review pipeline for:

- Digest verification  
- Provenance signature checks  
- SLSA chain revalidation  
- Threat attribution  

### 3. 📘 Governance Override for Necessity Cases
When necessary for operational continuity:

- Temporary registry tunnels may be opened  
- But only with hashed, SLSA-attested artifacts  
- All overrides logged in exceptions.md  

---

## 🧯 Tier 3 — Emergency Supply-Chain Lockdown (ESCL)

ESCL is the **highest-level fallback**, activated only if:

- A confirmed dependency-compromise is detected  
- Malicious package infiltration is verified  
- Multiple namespaces are attacked simultaneously  
- Wide-scale registry poisoning occurs upstream  

### ESCL Actions:

- 🚫 All dependency resolution disabled  
- 🔒 Build system enters hermetic mode  
- 🗄️ Only sealed, internal artifacts permitted  
- 🧬 SBOM must match most recent known-good build  
- 🛰️ All outgoing network access blocked  
- 📁 All artifacts routed through quarantine filters  
- 🧯 Human sign-off required for every build  

### ESCL Exit Requirements:

- Full SLSA chain revalidation  
- All namespace threats remediated  
- Mirror integrity confirmed  
- SBOM and digest equivalence restored  

---

## 📂 Directory Layout

~~~text
📁 policy/
├── 📄 README.md             # High-level policy
├── 📄 rules.md              # Mandatory enforcement rules
├── 📄 exceptions.md         # Governance-approved exceptions
├── 📄 incidents.md          # Incident register
└── 📄 fallback-controls.md  # This file — emergency + fallback policies
~~~

---

## 🕰️ Version History

| Version | Date | Notes |
|--------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial release of fallback-control framework |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 📏 [Enforcement Rules](./rules.md) • 🧭 [Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

