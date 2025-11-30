---
title: "⛓️ KFM v11.2.2 — Registry Fallback Attack (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/registry-fallback.md"
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
  - "docs/security/supply-chain/dependency-confusion/examples/registry-fallback.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/registry-fallback.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:registry-fallback:v11.2.2"
semantic_document_id: "kfm-depconf-examples-registryfallback-v11.2.2"
event_source_id: "ledger:depconf.examples.registryfallback.v11.2.2"

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

# ⛓️ **Registry Fallback Attack Example**  
`docs/security/supply-chain/dependency-confusion/examples/registry-fallback.md`

**Purpose:**  
Show how resolver fallback to public registries triggers silent dependency-confusion  
compromise even when internal mirrors exist, highlighting a common and dangerous  
real-world misconfiguration.

</div>

---

## 📘 Background

A **registry fallback attack** happens when:

1. The internal mirror fails (timeout, TLS error, 404).  
2. Resolver automatically contacts second/third registries.  
3. Public malicious package exists with the same name.  
4. Resolver silently installs malicious version.  
5. Lockfile + SBOM become invalid.  
6. Provenance metadata missing.  

This attack is especially common in:

- pip (Python)  
- npm (Node.js)  
- Maven/Gradle  
- Cargo  
- developer laptops with mixed configs  

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
    ├── 📄 registry-fallback.md        # This file
    ├── 📄 mirror-drift.md
    ├── 📄 sbom-drift-basic.json
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🔗 Example Scenario

### 🏛 Internal KFM Package
```
package: kfm-routing-core
version: 1.9.3
registry: https://kfm-pypi.internal/simple
hash: sha256:ee71bb12...
```

### 💣 Malicious Public Version
```
package: kfm-routing-core
version: 88.0.0
registry: https://pypi.org/simple
payload: credential exfiltration, remote shell
```

### ⚠️ Dangerous pip config
```
[global]
timeout = 2
extra-index-url = https://pypi.org/simple
```

### Resolver sequence
```
internal-mirror: timeout  
fallback → PyPI  
selects version 88.0.0  
installs malicious artifact  
no provenance  
SBOM mismatch  
```

---

## 🧪 Simulated CI Detection Output

```text
[registry-policy-check] FAIL: Outbound public registry contacted for "kfm-routing-core"
[namespace-monitor]    WARNING: public version outranks private version
[attestation-verify]   ERROR: invalid or missing SLSA provenance
[sbom-validate]        ERROR: SBOM mismatch vs installed dependency
[policy]               FAIL: registry fallback attack detected
```

Evidence stored in:

- `policy/evidence/registry-audit.json`
- `policy/evidence/namespace-scan.json`

---

## 🛡️ Why It Works in Unprotected Systems

- fallback behavior enabled  
- short timeouts  
- mixed registry configuration  
- missing SBOM alignment  
- no namespace scanning  
- no provenance validation  
- lockfile ignored  

---

## 🛡️ How KFM Prevents This Attack

### ✔ Registry Isolation  
Public registries permanently blocked.

### ✔ Hermetic Sandbox  
Outbound network → forbidden.

### ✔ Exact Version + Registry + Digest  
Removes version-precedence risk.

### ✔ SBOM Drift Enforcement  
Mismatch → build halted.

### ✔ Provenance Enforcement  
Attackers cannot forge SLSA & Cosign signing.

### ✔ Namespace Monitoring  
Detects high-version public publishes.

### ✔ Fallback Tier Activation  
Mirror failure triggers freeze mode, not fallback.

---

## 🧭 Developer Guidance

- Never use `extra-index-url` or public indexes  
- Run:
  ```bash
  kfm-reg-audit --strict
  ```
- Treat fallback warnings as critical  
- Ensure pre-commit policies block fallback-prone configs  
- Use sealed dependency snapshots  

---

## 🕰️ Version History

| Version | Date       | Notes |
|---------|------------|--------|
| v11.2.2 | 2025-11-30 | Full extended metadata + updated layout placement |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [Basic Collision](./namespace-collision-basic.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
