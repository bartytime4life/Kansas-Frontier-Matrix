---
title: "🏁 KFM v11.2.2 — Namespace Collision: Version Race Attack (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-versionrace.md"
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
  - "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-versionrace.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-versionrace.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:namespace-collision-versionrace:v11.2.2"
semantic_document_id: "kfm-depconf-examples-versionrace-v11.2.2"
event_source_id: "ledger:depconf.examples.versionrace.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "timeline-generation"
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

# 🏁 **Namespace Collision — Version Race Attack**  
`docs/security/supply-chain/dependency-confusion/examples/namespace-collision-versionrace.md`

**Purpose:**  
Show how attackers exploit **version precedence** and **timing** to override internal libraries  
by publishing higher public versions immediately after legitimate KFM releases.  
This is a sophisticated variant of dependency-confusion attacks.

</div>

---

## 📘 Background

A **version race attack** occurs when:

- Internal packages exist and are valid  
- Attackers publish *the same name* publicly  
- Public versions are always **higher**  
- Resolver chooses highest version → attacker wins  
- Fallback registries + misconfiguration exacerbate this  
- Stale lockfiles or missing SBOM enforcement enable silent compromise  

This pattern occurs across all major ecosystems (npm, PyPI, Cargo, Maven).

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md
    ├── 📄 namespace-collision-firstpublish.md
    ├── 📄 namespace-collision-versionrace.md    # This file
    ├── 📄 typosquat-examples.md
    ├── 📄 registry-fallback.md
    ├── 📄 mirror-drift.md
    ├── 📄 sbom-drift-basic.json
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🧨 Example Scenario

### 🏛 Internal KFM Package
```
name: kfm-stats-core
version: 2.7.1
registry: https://kfm-pypi.internal/simple
```

### 💣 Attacker Version Race on PyPI
```
name: kfm-stats-core
public versions:
  3.0.0
  5.0.0
  7.1.1
  20.0.0
  81.0.0
```

Attacker publishes shortly after each KFM release to “stay ahead.”

---

### 🤖 Vulnerable Resolver Behavior

A misconfigured resolver compares:

- Internal: `2.7.1`  
- Public: `81.0.0`  

Result → selects malicious version.

---

## 🧪 Simulated CI Detection Output

```text
[namespace-monitor]   ERROR: Version-race detected for "kfm-stats-core"
[namespace-monitor]   Internal version: 2.7.1
[namespace-monitor]   Public highest:   81.0.0
[policy]              FAIL: version-race namespace collision attack
[evidence]            Updated namespace-scan.json
```

---

## 🚨 Why This Works in Unprotected Systems

- Resolver selects highest version number  
- Public registry fallback allowed  
- Stale lockfile  
- No namespace monitoring  
- No SBOM drift detection  
- No provenance/SLSA enforcement  
- No registry isolation  

---

## 🛡️ How KFM v11.2.2 Blocks Version-Race Attacks

### ✔ Registry Isolation  
Public registries **never allowed**.

### ✔ Exact Pinning  
Resolver forced to use specific registry + version + hash.

### ✔ Namespace Scanning  
Detects suspicious publish patterns & version spikes.

### ✔ SBOM Drift Enforcement  
Mismatch → CI freeze.

### ✔ Provenance & Signature Enforcement  
Attackers cannot produce valid Cosign + SLSA metadata.

### ✔ Quarantine  
Malicious name ranges permanently blocked.

### ✔ Developer Pre-Commit Checks  
Local environment warns early.

---

## 🧭 Developer Guidance

- Always use **pinned internal deps**  
- Treat sudden public version spikes as major incidents  
- Validate mirror config:
  ```bash
  kfm-reg-audit --strict
  ```
- Run namespace scans:
  ```bash
  kfm-ns-scan .
  ```
- Report anomalies immediately

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Full extended metadata & layout upgrade |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [Basic Collision](./namespace-collision-basic.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
