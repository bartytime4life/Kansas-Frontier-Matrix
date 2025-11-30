---
title: "🧨 KFM v11.2.2 — Namespace Collision (Basic Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-basic.md"
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
  - "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-basic.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-basic.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:namespace-collision-basic:v11.2.2"
semantic_document_id: "kfm-depconf-examples-basiccollision-v11.2.2"
event_source_id: "ledger:depconf.examples.namespacecollisionbasic.v11.2.2"

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

heading_registry:
  approved_h2:
    - "📘 Background"
    - "🗂️ Directory Layout"
    - "🧨 Example Scenario"
    - "🧪 Simulated CI Detection Output"
    - "🚨 Why This Attack Works (Without Protection)"
    - "🛡️ How KFM v11.2.2 Prevents Namespace Collisions"
    - "🧭 Developer Guidance"
    - "🕰️ Version History"
---

<div align="center">

# 🧨 **Namespace Collision — Basic Example**  
`docs/security/supply-chain/dependency-confusion/examples/namespace-collision-basic.md`

**Purpose:**  
Demonstrate how a simple namespace collision between internal and public registries  
can immediately trigger a dependency-confusion attack in misconfigured environments.  
This is the *fundamental pattern* underlying many dependency-confusion exploits.

</div>

---

## 📘 Background

A namespace collision occurs when:

- A **public package** uses the **same name** as a private KFM package  
- A resolver checks public registries first or falls back  
- Version precedence rules pick the attacker’s version  
- Registry scoping is incomplete or misconfigured  

This is the simplest and most widely exploited dependency-confusion mechanism.

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md       # This file
    ├── 📄 namespace-collision-firstpublish.md
    ├── 📄 namespace-collision-versionrace.md
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
name: kfm-data-core
version: 2.3.0
registry: https://kfm-pypi.internal/simple
```

### 💣 Public Package
```
name: kfm-data-core
version: 50.0.0
registry: https://pypi.org/simple
payload: attacker_payload.whl
uploaded: 2025-11-28
```

### 🤖 Vulnerable Resolver Path

1. Resolver queries **public registry first**  
2. Detects version `50.0.0` (higher)  
3. Prefers the public one  
4. Installs malicious artifact  

---

## 🧪 Simulated CI Detection Output

```text
[namespace-monitor]   ERROR: Public registry collision detected: "kfm-data-core"
[namespace-monitor]   Public version:   50.0.0
[namespace-monitor]   Internal version: 2.3.0
[policy]              FAIL: namespace collision — high severity
[evidence]            Updated namespace-scan.json
```

---

## 🚨 Why This Attack Works (Without Protection)

- No strict registry isolation  
- Public registry contact allowed  
- Version-precedence issues  
- No namespace-blocking  
- Floating version specifiers  
- Missing SBOM enforcement  
- No provenance validation  

---

## 🛡️ How KFM v11.2.2 Prevents Namespace Collisions

### ✔ Registry Isolation  
Public registries → **blocked** always.

### ✔ Namespace Scanning  
Detects name collisions instantly.

### ✔ Deterministic Pinning  
Version + registry + digest eliminate ambiguity.

### ✔ Provenance Enforcement  
Attackers cannot simulate KFM signatures/SLSA.

### ✔ SBOM Locking  
Ensures internal dependency alignment.

### ✔ Hermetic Sandbox Enforcement  
No unintended fallback behavior.

---

## 🧭 Developer Guidance

- Always install packages from KFM mirrors only  
- Never rely on implicit registry resolution  
- Run namespace scanning locally:
  ```bash
  kfm-ns-scan .
  ```
- Treat namespace collision alerts as critical  
- Validate registry configs for correctness  
- Avoid floating versions entirely  

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Full extended metadata + directory layout move |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [First-Publish Example](./namespace-collision-firstpublish.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
