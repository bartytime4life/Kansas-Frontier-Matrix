---
title: "❌ KFM v11.2.2 — Verification Failure Case (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/verification-failure-case.md"
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
  - "docs/security/supply-chain/dependency-confusion/examples/verification-failure-case.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/verification-failure-case.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:verification-failure-case:v11.2.2"
semantic_document_id: "kfm-depconf-verification-failure-case-v11.2.2"
event_source_id: "ledger:depconf.examples.verificationfailure.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"

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

# ❌ **Verification Failure Case**  
`docs/security/supply-chain/dependency-confusion/examples/verification-failure-case.md`

**Purpose:**  
Demonstrate a realistic **artifact verification failure** that indicates a dependency-confusion  
attack, provenance compromise, registry poisoning, or mirror drift.  
Used by KFM training, CI/CD simulation, and automated reasoning engines.

</div>

---

## 📘 Context

This example demonstrates what happens when:

- Digest ≠ SBOM  
- Cosign signature = INVALID  
- SLSA provenance = MISSING  
- Mirror metadata differs from baseline  

These are hallmark indicators of:

- Shadow-package injection  
- Registry poisoning  
- Man-in-the-middle replacement  
- Spoofed provenance  
- Build pipeline compromise  

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
    ├── 📄 sandbox-network-leak.md
    ├── 📄 implicit-upgrade-attack.md
    └── 📄 verification-failure-case.md   # This file
~~~

---

## ❌ Example Verification Failure

### 🔐 Artifact Under Test
```
package:         kfm-utils-core
version:         4.2.1
registry:        https://kfm-pypi.internal/simple
digest_sbom:     sha256:4af81c22f8b5...c316a1
digest_fetched:  sha256:b91c003bd7cc...f22181
cosign_signature: INVALID (key mismatch)
slsa_provenance: MISSING
```

### 🧪 Validation Output (Simulated)

```text
[attestation-verify] ERROR: SLSA provenance bundle missing.
[digest-check]      ERROR: Digest mismatch between SBOM and fetched artifact.
[cosign-verify]     ERROR: Cosign signature invalid — unknown public key.
[registry-audit]    WARNING: Artifact metadata differs from mirror baseline.
[policy]            FAIL: Artifact verification failure — quarantine required.
```

---

## 🚩 Why This Fails Verification

### 1. 🔑 Invalid Cosign Signature  
The artifact cannot be verified against trusted signing keys.

### 2. 🧬 Missing SLSA Provenance  
Every artifact must supply lineage.

### 3. 🧪 Digest Mismatch  
SBOM digest ≠ fetched artifact digest.

### 4. 🛰️ Registry Metadata Drift  
Mirror & authoritative metadata disagree.

---

## 🛑 Required KFM Response

1. **Block the build**  
2. Create incident stub in:  
   ```
   docs/security/supply-chain/dependency-confusion/policy/incidents.md
   ```
3. Quarantine package name  
4. Trigger mirror integrity diff-check  
5. Activate fallback Tier 1 (if drift persists)  
6. Require governance review  
7. Rebuild using sealed dependencies  

---

## 🧭 Developer Guidance

- Do NOT bypass verification errors  
- Rebuild SBOM locally using sealed dependencies  
- Validate GPG & Cosign trust stores  
- Ensure environment uses internal mirrors  
- Report anomalies immediately  

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Full extended v11.2.2 metadata; updated layout position |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧪 [Examples Overview](./README.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
