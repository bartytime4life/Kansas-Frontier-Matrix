---
title: "🌐 KFM v11.2.2 — Sandbox Network Leak (Hermeticity Violation Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/sandbox-network-leak.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
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

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"

ontology_alignment:
  cidoc: "E13 Attribute Assignment"
  schema_org: "TechArticle"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/examples/sandbox-network-leak.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/sandbox-network-leak.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:sandbox-network-leak:v11.2.2"
semantic_document_id: "kfm-depconf-examples-sandboxnetworkleak-v11.2.2"
event_source_id: "ledger:depconf.examples.sandboxnetworkleak.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🌐 **Sandbox Network Leak Example**  
`docs/security/supply-chain/dependency-confusion/examples/sandbox-network-leak.md`

**Purpose:**  
Demonstrate how outbound network leaks inside a CI or development sandbox  
enable silent dependency-confusion compromises by allowing accidental contact  
with public registries, auto-installers, or malicious update channels.  
This example supports KFM’s hermeticity enforcement and anomaly-detection models.

</div>

---

## 📘 Background

A sandbox network leak occurs when a supposedly isolated build or runtime environment  
unexpectedly permits outbound network traffic.  
This permits:

- resolver fallback to public registries  
- plugin auto-installation  
- dependency auto-upgrades  
- telemetry exfiltration  
- shadow-package injection  

Such leaks often arise from:

- misconfigured CI runners  
- incorrect container isolation  
- permissive network proxy settings  
- developer machines with mixed environments  
- tools like npm, pip, Gradle auto-installing plugins  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md
    ├── 📄 namespace-collision-firstpublish.md
    ├── 📄 namespace-collision-versionrace.md
    ├── 📄 typosquat-examples.md
    ├── 📄 registry-fallback.md
    ├── 📄 mirror-drift.md
    ├── 📄 sbom-drift-basic.json
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md    # This file
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🌐 Example Scenario

### 🏛 Expected Hermetic Sandbox Behavior
```
- Zero outbound network access
- No DNS resolution to public servers
- No plugin auto-installation
- Only internal mirrors reachable
```

### 💣 Misconfigured Sandbox Behavior
```
sandbox> curl https://pypi.org
200 OK
sandbox> ping registry.npmjs.org
64 bytes from 151.101.x.x ...
```

### 🚨 Real Attack Chain
1. Internal mirror becomes temporarily unavailable  
2. Resolver attempts fallback → public registry  
3. Finds malicious version  
4. Installs compromised artifact  
5. SBOM + provenance mismatch  

---

## 🧪 Simulated CI Detection Output

```text
[hermetic-build-guard] ERROR: outbound network contact detected to pypi.org
[registry-policy-check] FAIL: contact with public registry forbidden under KFM policy
[attestation-verify]  ERROR: missing SLSA provenance for installed dependency
[sbom-validate]       ERROR: dependency hash mismatch vs SBOM
[policy]              FAIL: sandbox-network-leak triggered — quarantine activated
```

---

## 🚨 Why This Attack Works in Unprotected Systems

- missing hermetic sandbox enforcement  
- unblocked outbound internet  
- resolver fallback allowed  
- floating dependency versions  
- no provenance verification  
- plugin auto-updates  

---

## 🛡️ How KFM v11.2.2 Prevents Network Leak Attacks

### ✔ Hermetic Sandbox Enforcement  
Force ZERO outbound traffic.

### ✔ Registry Isolation  
Public registries permanently blocked.

### ✔ Exact Pinning  
Resolver cannot auto-upgrade or fallback.

### ✔ SBOM Drift Enforcement  
All mismatches halt builds immediately.

### ✔ Provenance & Signature Enforcement  
Malicious public artifacts cannot satisfy signing requirements.

### ✔ Evidence-Based Quarantine  
CI stores evidence for forensic review.

### ✔ Developer Pre-Commit Safeguards  
Local sandbox leak checks prevent bad commits.

---

## 🧭 Developer Guidance

- Validate current environment:
  ```bash
  kfm-reg-audit --strict
  ```
- Disable plugin auto-installers  
- Ensure Dockerfile uses hermetic base images  
- Treat all network-leak warnings as **critical incidents**  
- Rebuild only from sealed dependency snapshots  

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Fully extended metadata and upgraded structure |

---

<div align="center">

📚 [Examples Index](./README.md) • ⛓️ [Registry Fallback](./registry-fallback.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
