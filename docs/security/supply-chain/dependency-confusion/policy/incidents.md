---
title: "🚨 KFM v11.2.2 — Dependency-Confusion Incident Log (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/incidents.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Security Council"
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
doc_kind: "Security · Incident-Log"
ontology_protocol_version: "KFM-OP v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"
pipeline_contract_version: "KFM-PDC v11"
---

<div align="center">

# 🚨 **Dependency-Confusion Incident Log**  
`docs/security/supply-chain/dependency-confusion/policy/incidents.md`

**Purpose:**  
Serve as the **immutable forensic register** of all dependency-confusion–related incidents  
detected, blocked, or mitigated by KFM v11.2.2 security defenses.

All entries require Security Council approval and are permanently preserved for governance,  
audit, and long-term supply-chain analytics.

</div>

---

## 📘 Overview

This log captures confirmed or suspected dependency-confusion incidents across:

- Public registry namespace collisions  
- Rogue shadow packages  
- Malicious dependency injection attempts  
- Unauthorized registry resolution behavior  
- SBOM drift suggesting compromised dependencies  
- Attestation chain breakage (SLSA violations)  

Each entry MUST follow the required incident schema and MUST be accompanied by  
machine evidence stored under:

```
docs/security/supply-chain/dependency-confusion/policy/evidence/
```

---

## 🧭 Incident Entry Schema (Required)

Every incident MUST include the following fields:

```yaml
id: INC-DC-YYYY-NNNN
date_detected: "YYYY-MM-DD"
severity: low|medium|high|critical
status: "open" | "mitigated" | "false-positive" | "under-review"
vector: "namespace-collision" | "rogue-package" | "registry-leak" |
        "sbom-drift" | "attestation-failure" | "other"
description: >
  Clear factual description of the suspicious or malicious behavior.
evidence_refs:
  - "evidence/namespace-scan.json"
  - "evidence/sbom-diff.json"
affected_components:
  - "pipelines/batch/etl"
  - "web/frontend"
  - "graph/neo4j-loader"
root_cause: >
  Summary of confirmed cause (if known).
mitigation:
  actions:
    - "mirror lock activated"
    - "namespace quarantined"
    - "dependency pinned to hash"
  completed: true|false
follow_up_actions:
  - "SLSA chain verification"
  - "dependency replacement roadmap"
date_closed: "YYYY-MM-DD"
approved_by:
  - name: "Security Council Member"
    role: "Council"
```

---

## 📂 Current Incident Log (v11.2.2)

> 🚨 *This log is initially empty for v11.2.2. All new incidents must be added below this line via governance-approved PRs.*

_No recorded incidents._

---

## 🔐 Incident Lifecycle Requirements

### 1. 🕵️ Detection
All anomalies detected by namespace-monitor, SBOM-diff, SLSA attestation checks, or CI must be  
treated as potential incidents until proven otherwise.

### 2. 🧪 Investigation
Security Council conducts:

- Evidence collection  
- Risk assessment  
- Impact analysis  
- Threat attribution (if applicable)  

### 3. 🛡️ Mitigation
Mitigation actions must be:

- Immediate  
- Measurable  
- Reproducible  
- Recorded  
- Attached to evidence refs  

### 4. 🧾 Closure
Closed incidents require:

- Formal approval  
- Completed mitigation  
- Proven remediation  
- Updated SBOM & provenance  
- Linked documentation updates  

---

## 🕰️ Version History

| Version | Date | Notes |
|--------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial incident log created |

---

<div align="center">

🛡️ [Dependency-Confusion Policy](./README.md) • 📁 [Evidence Archive](./evidence/README.md) • 🧭 [Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

