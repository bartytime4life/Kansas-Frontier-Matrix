---
title: "🌫️ KFM v11.2.2 — Mirror Drift Attack (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/mirror-drift.md"
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
  - "docs/security/supply-chain/dependency-confusion/examples/mirror-drift.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/examples/mirror-drift.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/examples/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:examples:mirror-drift:v11.2.2"
semantic_document_id: "kfm-depconf-examples-mirrordrift-v11.2.2"
event_source_id: "ledger:depconf.examples.mirrordrift.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "diagram-extraction"
  - "semantic-highlighting"
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
    - "🌫️ Example Scenario"
    - "🧪 Simulated CI Detection Output"
    - "🚨 Why This Attack Works (in unprotected systems)"
    - "🛡️ How KFM v11.2.2 Blocks This Attack"
    - "🧭 Developer Guidance"
    - "🕰️ Version History"
---

<div align="center">

# 🌫️ **Mirror Drift Attack Example**  
`docs/security/supply-chain/dependency-confusion/examples/mirror-drift.md`

**Purpose:**  
Show how *mirror drift*—inconsistency between internal mirror data and upstream registry data—  
can silently introduce dependency-confusion vulnerabilities, SBOM mismatches, and malicious artifacts.

</div>

---

## 📘 Background

A **mirror drift attack** occurs when:

1. Internal KFM mirror pulls corrupted or tampered upstream metadata.  
2. Upstream registry content changes unexpectedly or maliciously.  
3. Sync logic overwrites internal sealed metadata.  
4. Resolvers fetch altered packages believing them to be valid.  
5. Provenance & SBOM drift silently diverge.  

Mirror drift is one of the most dangerous supply-chain failure states.

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
    ├── 📄 mirror-drift.md              # This file
    ├── 📄 sbom-drift-basic.json
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🌫️ Example Scenario

### 🏛 Internal Mirror Expected State
```
package: kfm-analytics-core
version: 1.4.0
digest: sha256:6fd202aa...
provenance: VALID (SLSA v3+)
signature: cosign OK
```

### 💣 Upstream Tampered
```
package: kfm-analytics-core
version: 1.4.0
digest: sha256:a7dd900b...   # different!
provenance: MISSING
signature: INVALID
timestamp: 2025-11-29 02:15:10 UTC
```

### 🔁 Drift Window
During a sync:

- Attacker-published version overwrites internal mirror metadata  
- Internal SBOM becomes inconsistent  
- Resolver installs malicious artifact without warning  

---

## 🧪 Simulated CI Detection Output

```text
[mirror-integrity]    ERROR: digest mismatch detected for kfm-analytics-core
[namespace-monitor]   WARNING: suspicious upstream timestamp pattern
[sbom-validate]       ERROR: expected sha256:6fd202aa..., got sha256:a7dd900b...
[attestation-verify]  ERROR: missing or invalid SLSA provenance
[policy]              FAIL: mirror drift attack — mirror quarantined
```

Evidence produced in:

- `policy/evidence/registry-audit.json`
- `policy/evidence/sbom-diff.json`
- `policy/evidence/attestation-verify.json`

---

## 🚨 Why This Attack Works (in unprotected systems)

- Blind mirror sync  
- No provenance check before ingest  
- No digest equivalence enforcement  
- No SBOM locking  
- Misconfigured resolver trusts mirror  
- Lack of TLS pinning  
- No timestamp anomaly analysis  

---

## 🛡️ How KFM v11.2.2 Blocks This Attack

### ✔ TLS Pinning  
Mirror syncs must validate SAN and CA hierarchy.

### ✔ Digest Equivalence Enforcement  
SBOM ↔ upstream ↔ mirror digests must match.

### ✔ Provenance Validation  
Upstream assets without SLSA v3+ provenance are rejected.

### ✔ Mirror Drift Freeze Mode  
Mirror quarantined; sealed deps only.

### ✔ Evidence Logging  
Multi-file evidence chain ensures forensic traceability.

### ✔ CI Hard-Fail  
Drift → immediate pipeline shutdown.

### ✔ Namespace & Timestamp Monitoring  
Detects suspicious upstream activity.

---

## 🧭 Developer Guidance

- Never override drift warnings  
- Validate mirror integrity using:
  ```bash
  kfm-reg-audit --strict
  ```
- Compare sealed artifacts against SBOM  
- Roll back to last-known-good  
- Notify Security Council immediately  

---

## 🕰️ Version History

| Version  | Date       | Notes |
|----------|------------|--------|
| v11.2.2  | 2025-11-30 | Full extended metadata; layout moved; upgraded for v11.2.2 |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧩 [Lockfile Drift](./lockfile-drift-attack.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
