---
title: "📚 KFM v11.2.2 — Dependency-Confusion Examples & Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/examples/README.md"
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
  cidoc: "E29 Design or Procedure"
  schema_org: "CollectionPage"
  prov_o: "prov:Collection"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/examples/README.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:index:v11.2.2"
semantic_document_id: "kfm-depconf-examples-index-v11.2.2"
event_source_id: "ledger:depconf.examples.index.v11.2.2"

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

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🎯 Example Categories"
    - "🕰️ Version History"
---

<div align="center">

# 📚 **Dependency-Confusion Examples & Patterns**  
`docs/security/supply-chain/dependency-confusion/examples/README.md`

**Purpose:**  
Serve as the authoritative index of all **dependency-confusion attack examples** used in  
KFM v11.2.2 for training, governance review, CI simulation, and automated reasoning models.  
This collection captures high-risk patterns (namespace collisions, typosquats, SBOM drift,  
signature failures, hermeticity violations) in a standardized, FAIR+CARE-aligned format.

</div>

---

## 📘 Overview

Dependency-confusion attacks exploit mismatches between:

- **Internal vs public package names**  
- **Version precedence rules**  
- **Resolver fallback behavior**  
- **Namespace ambiguity**  
- **Dynamic registry resolution**  
- **Missing provenance metadata**  

This directory includes:

- 🧨 Namespace collision examples  
- 🧿 Typosquatting patterns  
- 🔐 Registry fallback / mismatch cases  
- 🧬 SBOM & lockfile drift scenarios  
- ✍️ Signature & provenance failures  
- 🧱 Hermetic sandbox leak cases  

These examples are used by:

- KFM developers  
- Security Council auditors  
- Automated CI enforcement  
- Focus Mode v3 threat reasoning models  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md                       # This file — index of examples
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
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🎯 Example Categories

### 1. 🧨 Namespace Collision Examples  
- Collisions between internal and public packages  
- First-publish attacks  
- Version race exploitation  

Includes:  
`namespace-collision-basic.md`,  
`namespace-collision-firstpublish.md`,  
`namespace-collision-versionrace.md`

---

### 2. 🧿 Typosquatting Examples  
- Homoglyph attacks  
- Confusable characters  
- Prefix-suffix spoofing  
- Zero-width character tricks  

Example: `typosquat-examples.md`

---

### 3. 🔐 Registry-Resolution Failure Examples  
- Registry fallback  
- URL mismatch  
- TLS pinning failures  
- Mirror integrity drift  

Includes `registry-fallback.md`, `mirror-drift.md`

---

### 4. 🧬 SBOM & Lockfile Drift Examples  
- Dependency graph vs SBOM mismatch  
- Rogue dependencies  
- Drift introduced by commit tampering  

Includes:  
`sbom-drift-basic.json`,  
`lockfile-drift-attack.md`

---

### 5. ✍️ Signature & Provenance Failures  
- Invalid Cosign signatures  
- Missing SLSA provenance  
- Corrupted signing bundles  

Includes:  
`invalid-cosign.sig`,  
`missing-provenance.json`

---

### 6. 🧱 Hermetic Sandbox Violations  
- Network leaks  
- Plugin auto-installation  
- Fallback to public services  
- Failed sandbox enforcement  

Includes:  
`sandbox-network-leak.md`,  
`implicit-upgrade-attack.md`

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Full extended metadata upgrade; reorganized content and layout |

---

<div align="center">

🧪 [Automated Checks](../checks/README.md) • 🛡️ [Policy Overview](../policy/README.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
