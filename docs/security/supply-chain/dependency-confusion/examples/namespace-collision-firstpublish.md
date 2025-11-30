---
title: "🧨 KFM v11.2.2 — Namespace Collision (First-Publish Attack Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-firstpublish.md"
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
  - "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-firstpublish.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-firstpublish.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:namespace-collision-firstpublish:v11.2.2"
semantic_document_id: "kfm-depconf-examples-firstpublish-v11.2.2"
event_source_id: "ledger:depconf.examples.firstpublish.v11.2.2"

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
    - "🚨 Why This Attack Works (Without KFM Protections)"
    - "🛡️ How KFM v11.2.2 Blocks This Attack"
    - "🧭 Developer Guidance"
    - "🕰️ Version History"
---

<div align="center">

# 🧨 **Namespace Collision — First-Publish Attack**  
`docs/security/supply-chain/dependency-confusion/examples/namespace-collision-firstpublish.md`

**Purpose:**  
Demonstrate the foundational *first-publish* dependency-confusion attack pattern,  
where a malicious actor publishes a public package **before** the internal one,  
tricking resolvers into selecting the wrong registry.

</div>

---

## 📘 Background

A first-publish attack occurs when:

1. KFM has a **private internal package** (e.g., `kfm-geo-core`).  
2. It does **not** exist on PyPI/NPM/etc.  
3. An attacker publishes a **public package with the same name**.  
4. Resolver attempts public registry first or uses version precedence → attacker wins.  

This is one of the oldest and most effective dependency-confusion tactics.

---

## 🗂️ Directory Layout  

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md
    ├── 📄 namespace-collision-firstpublish.md   # This file
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

### Internal KFM Package
```
name: kfm-geo-core
version: 3.8.0
registry: https://kfm-pypi.internal/simple
```

### Attacker First-Publish on PyPI
```
package:   kfm-geo-core
version:   99.0.0
registry:  https://pypi.org/simple
uploaded:  2025-11-04 02:13:05 UTC
payload:   malicious wheel (RAT loader)
```

### Why It's Effective

- Internal package has no public record  
- Public registry is trusted by misconfigured resolvers  
- Attacker uses inflated version (`99.0.0`)  
- Resolver incorrectly chooses the public one  

---

## 🧪 Simulated CI Detection Output

```text
[namespace-monitor]   WARNING: First-publish detected: "kfm-geo-core"
[namespace-monitor]   Internal version: 3.8.0
[namespace-monitor]   Public version:   99.0.0
[policy]              FAIL: namespace collision — quarantine name
[evidence]            Updated: namespace-scan.json
```

---

## 🚨 Why This Attack Works (Without KFM Protections)

- Resolver defaults to public-first registry lookup  
- Namespace shielding not enforced  
- No registry isolation  
- No SLSA provenance validation  
- Version precedence favors attacker  
- No SBOM enforcement  
- No fallback protections  

---

## 🛡️ How KFM v11.2.2 Blocks This Attack

### ✔ Registry Isolation  
Public registries → blocked.

### ✔ Namespace Monitoring  
First-publish attempts detected instantly.

### ✔ Exact Pinning  
Resolver cannot float to higher versions.

### ✔ SLSA + Cosign Validation  
Attacker cannot produce valid provenance.

### ✔ SBOM Drift Enforcement  
Mismatch halts builds.

### ✔ Fallback Tier  
Mirror failure never falls back to public registry.

### ✔ SBD Auto-Generation  
Security Block Declaration quarantines namespace.

---

## 🧭 Developer Guidance

- Never install packages not found in internal mirrors  
- Run namespace scan:
  ```bash
  kfm-ns-scan .
  ```
- Treat first-publish alerts as CRITICAL  
- Validate environment registry settings  
- Ensure no resolver fallback behavior  

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Full extended metadata upgrade; directory-layout repositioned |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [Basic Collision](./namespace-collision-basic.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
