---
title: "📏 KFM v11.2.2 — Dependency-Confusion Enforcement Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/rules.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Supply-Chain Security Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/security-v3.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

doc_kind: "Security · Ruleset"
intent: "dependency-confusion-governance · enforcement-rules"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Protection of Critical Infrastructure"
classification: "Security · Supply Chain · Rules"
sensitivity: "Security-Sensitive (Non-personal)"
sensitivity_level: "High"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "High"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Annual review"
sunset_policy: "Superseded when v11.3 ruleset is published"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/policy/rules.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/policy/rules.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/policy/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:policy:rules:v11.2.2"
semantic_document_id: "kfm-depconf-policy-rules-v11.2.2"
event_source_id: "ledger:depconf.policy.rules.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "semantic-highlighting"
  - "timeline-generation"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "unverified-architectural-claims"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧱 Enforcement Rules (Required)"
    - "🧪 Validation & CI/CD Enforcement"
    - "🕰️ Version History"
---

<div align="center">

# 📏 **Dependency-Confusion Enforcement Rules**  
`docs/security/supply-chain/dependency-confusion/policy/rules.md`

**Purpose:**  
Define the *mandatory, non-negotiable enforcement rules* underpinning KFM’s dependency-confusion  
security posture. These rules are executed by KFM-CI, enforced via governance, and validated through  
SBOM lineage, SLSA attestations, and hermetic build constraints.

</div>

---

## 📘 Overview

These rules operationalize the KFM dependency-confusion defense model across all ecosystems:

- pip / poetry · npm · cargo · NuGet · Maven/Gradle · RubyGems · Go modules  
- Registry-isolation boundaries  
- SBOM/SLSA provenance enforcement  
- Deterministic resolver constraints  
- Namespace-collision scanning  
- Artifact validation & integrity-checking  
- Governance-backed exceptions  

All rules in this file are **mandatory, enforced, and CI-blocking**.

---

## 🗂️ Directory Layout

~~~text
📁 policy/
├── 📄 README.md               # High-level policy
├── 📄 rules.md                # This file — enforcement rules
├── 📄 registry-isolation.md   # Registry isolation requirements
├── 📄 signature-requirements.md
├── 📄 fallback-controls.md
├── 📄 exceptions.md
├── 📄 incidents.md
└── 📂 evidence/
    ├── 🛰️ namespace-scan.json
    ├── 🧬 sbom-diff.json
    ├── 🔐 registry-audit.json
    └── 🧾 attestation-verify.json
~~~

---

## 🧱 Enforcement Rules (Required)

### 1. 🧩 Deterministic Pinning
All dependencies MUST:

- Declare **exact versions**, **exact registries**, and **cryptographic hashes**  
- Use **lockfiles checked into version control**  
- Align fully with sealed SBOM artifact records  

**Prohibited:**  
- Wildcards (`*`, `>`, `<`, `^`, `~`)  
- Floating versions  
- Implicit registry URLs  

---

### 2. 🔒 Registry Isolation
Dependencies may only resolve from **KFM-governed internal mirrors**.

**Any contact** with a public registry (`pypi.org`, `npmjs.org`, `crates.io`, etc.)  
→ **immediate CI hard fail + incident stub**.

---

### 3. 🧬 SBOM & SLSA Enforcement
Builds MUST:

- Generate SBOMs  
- Validate digests via sealed SBOM  
- Enforce SLSA v3 provenance  
- Block mismatched or unprovenanced artifacts  

---

### 4. 🛰️ Namespace Collision Scanning
CI MUST detect:

- Public “first publish” conflicts  
- Shadow-version attacks  
- Version-race exploits  
- Typosquat or confusable namespace registrations  

Conflicts → quarantine + denylist entry.

---

### 5. 🧪 CI/CD Hermetic Sandbox
Builds MAY NOT:

- Access the public internet  
- Install dependencies outside pinned set  
- Modify lockfiles without governance approval  
- Resolve from fallback registries  

Sandboxing is mandatory across CI and pipeline execution.

---

### 6. 🧯 Immediate Quarantine Procedures
Upon identifying a suspicious dependency:

1. CI hard-fail  
2. Incident stub created in `incidents.md`  
3. Namespace quarantined  
4. Dependency list frozen  
5. Crisis rebuild from sealed artifacts  

---

### 7. 📝 Governance Exceptions (SER Required)
All exceptions MUST:

- Be logged in `exceptions.md`  
- Contain compensating controls  
- Have a ≤ 90-day expiration  
- Pass Security Council vote  

---

### 8. 📦 Lockfile Integrity
Lockfiles MUST:

- Include full registry URLs  
- Include exact package digests  
- Match SBOM entries  
- Remain immutable except via approved PRs  

Drift → **merge blocked**.

---

### 9. 🛡️ Artifact Validation
All artifacts MUST:

- Include provenance metadata  
- Match sealed SBOM digests  
- Validate Cosign/GPG signatures  
- Be reproducible and deterministic  

Failure → rejection + incident stub.

---

### 10. 📡 Telemetry & Evidence Logging
KFM logs all enforcement output to:

```
docs/security/supply-chain/dependency-confusion/policy/evidence/
```

Including:

- Namespace-scan logs  
- SBOM drift reports  
- Registry-audit logs  
- Signature and provenance checks  

All logs MUST be immutable and FAIR+CARE aligned.

---

## 🧪 Validation & CI/CD Enforcement

Enforced by workflows:

- `registry-policy-check.yml`
- `namespace-monitor.yml`
- `dependency-integrity.yml`
- `slsa-attestation-verify.yml`
- `sbom-validate.yml`
- `security-evidence-lint.yml`
- `governance-policy-check.yml`

Failures → **merge blocked on all protected branches**.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                  |
|----------|------------|--------------------------------------------------------|
| v11.2.2  | 2025-11-30 | Directory layout moved up; full extended metadata      |
| v11.2.1  | 2025-10-12 | Added typosquat detection + strict provenance linkage  |
| v11.2.0  | 2025-09-01 | Initial v11 enforcement framework                      |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 🗂️ [Evidence](./evidence/README.md) • 🧭 [Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
