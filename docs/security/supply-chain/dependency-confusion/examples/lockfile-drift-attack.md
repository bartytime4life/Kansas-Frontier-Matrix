---
title: "🗂️ KFM v11.2.2 — Lockfile Drift Attack (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/lockfile-drift-attack.md"
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
  - "docs/security/supply-chain/dependency-confusion/examples/lockfile-drift-attack.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/lockfile-drift-attack.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:lockfile-drift-attack:v11.2.2"
semantic_document_id: "kfm-depconf-examples-lockfiledrift-v11.2.2"
event_source_id: "ledger:depconf.examples.lockfiledrift.v11.2.2"

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
    - "📘 Background"
    - "🗂️ Directory Layout"
    - "🧨 Example: Drift Introduced by a Malicious Commit"
    - "🧪 Simulated CI Detection Output"
    - "🚨 Why This Attack Works (in unprotected systems)"
    - "🛡️ How KFM v11.2.2 Prevents This Attack"
    - "🧭 Developer Guidance"
    - "🕰️ Version History"
---

<div align="center">

# 🗂️ **Lockfile Drift Attack Example**  
`docs/security/supply-chain/dependency-confusion/examples/lockfile-drift-attack.md`

**Purpose:**  
Show how **lockfile drift** enables dependency-confusion by desynchronizing  
the lockfile → dependency graph → mirror metadata → SBOM connection,  
allowing malicious versions or shadow dependencies to enter the system.

</div>

---

## 📘 Background

A lockfile drift attack occurs when:

- Lockfile content no longer matches the SBOM  
- Hash or registry mismatches appear silently  
- New rogue dependencies appear in the lockfile  
- Resolver ignores outdated lockfiles  
- Public registries override internal ones  
- Dependency graph integrity is lost  

Attackers frequently exploit drift windows to poison dependency graphs.

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
    ├── 📄 lockfile-drift-attack.md   # This file
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🧨 Example: Drift Introduced by a Malicious Commit

### 🔒 Expected Lockfile State
```yaml
kfm-math-tools:
  version: "2.4.1"
  registry: "https://kfm-pypi.internal/simple"
  hash: "sha256:4f0a81b9..."
```

### 💣 Malicious Modification
```yaml
kfm-math-tools:
  version: "99.0.0"
  registry: "https://pypi.org/simple"
  hash: "sha256:deadbeef..."
```

### ⚠️ Added Rogue Dependency
```yaml
kfm-math-tools-helper:
  version: "1.0.0"
  registry: "https://pypi.org/simple"
  hash: "sha256:aa11ccdd..."
```

This causes resolvers to:

- Pull malicious upstream versions  
- Pull dependencies NOT in SBOM  
- Break reproducibility and provenance  

---

## 🧪 Simulated CI Detection Output

```text
[lockfile-verify]     ERROR: lockfile does not match SBOM
[digest-check]        ERROR: hash mismatch for kfm-math-tools
[namespace-monitor]   WARNING: rogue dependency detected
[sbom-validate]       ERROR: SBOM missing entries for helper dependency
[registry-policy]     FAIL: public registry contacted
[policy]              FAIL: lockfile drift attack detected
```

---

## 🚨 Why This Attack Works (in unprotected systems)

- Lockfiles not validated  
- SBOM not enforced  
- Resolver ignores outdated lockfile entries  
- Public registry fallback allowed  
- No namespace monitoring  
- No provenance checks  

---

## 🛡️ How KFM v11.2.2 Prevents This Attack

### ✔ Lockfile Integrity Enforcement  
Lockfiles must match SBOM + provenance chain.

### ✔ SBOM Drift Detection  
Any inconsistency halts builds.

### ✔ Registry Isolation  
Public registries permanently blocked.

### ✔ Namespace Collision Detection  
Rogue dependencies flagged instantly.

### ✔ Provenance + Signature Enforcement  
Malicious versions cannot provide valid SLSA/Cosign bundles.

### ✔ Fallback Controls  
Drift triggers Tier 1 freeze mode.

### ✔ Pre-Commit Checks  
Developers catch drift before committing.

---

## 🧭 Developer Guidance

- Never manually edit lockfiles  
- Regenerate lockfile + SBOM together  
- Use only internal registries  
- Run local scans:
  ```bash
  kfm-lock-verify
  kfm-sbom-diff --local
  ```
- Treat drift warnings as *critical*  
- Roll back to sealed dependency snapshots  

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Full extended metadata upgrade & layout restructuring |

---

<div align="center">

📚 [Examples Index](./README.md) • 🏁 [Version Race Example](./namespace-collision-versionrace.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
