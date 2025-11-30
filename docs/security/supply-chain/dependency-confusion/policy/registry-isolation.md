---
title: "🔒 KFM v11.2.2 — Registry Isolation Policy (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/registry-isolation.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Supply-Chain Security Council · FAIR+CARE"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

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

doc_kind: "Security · Registry-Isolation"
intent: "prevent-registry-hijack · enforce-resolver-determinism"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Protection of Critical Infrastructure"
classification: "Security · Supply Chain · Registry Isolation"
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
sunset_policy: "Superseded in v11.3 or next revision cycle"

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
  - "docs/security/supply-chain/dependency-confusion/policy/registry-isolation.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/policy/registry-isolation.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/policy/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:policy:registry-isolation:v11.2.2"
semantic_document_id: "kfm-depconf-policy-registryisolation-v11.2.2"
event_source_id: "ledger:depconf.policy.registryisolation.v11.2.2"

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
  - "unverified-architectural-claims"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🔐 Allowed Registries (Strict Allow-List)"
    - "🧱 Mandatory Isolation Rules"
    - "🧪 CI Enforcement"
    - "🕰️ Version History"
---

<div align="center">

# 🔒 **Registry Isolation Policy**  
`docs/security/supply-chain/dependency-confusion/policy/registry-isolation.md`

**Purpose:**  
Enforce strict internal-only registry resolution across *all* KFM ecosystems to block  
namespace shadowing, version-race hijacks, rogue upstream packages, and public-registry leakage.

</div>

---

## 📘 Overview

Registry isolation is the **first and most essential layer** of KFM supply-chain defense.  
The purpose: prevent the resolver from ever touching a public registry, even accidentally.

KFM v11.2.2 mandates:

- **Zero fallback**  
- **Zero public registry access**  
- **Internal mirrors only**  
- **Deterministic resolution**  
- **Full provenance validation**  

This prevents:

- Namespace collisions  
- Typosquat hijacks  
- Registry poisoning  
- Shadow-package injection  
- TLS downgrade or metadata drift attacks  

Registry isolation cannot be bypassed except by a formally approved SER.

---

## 🗂️ Directory Layout

~~~text
📁 policy/
├── 📄 README.md               # Top-level dependency-confusion policy
├── 📄 rules.md                # Enforcement rules
├── 📄 registry-isolation.md   # This file — strict registry isolation rules
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

## 🔐 Allowed Registries (Strict Allow-List)

### 🐍 Python (pip / poetry)
**Allowed:**  
- `https://kfm-pypi.internal/simple`

**Forbidden:**  
- `https://pypi.org/simple`  
- `https://test.pypi.org/simple`  
- All non-KFM domains

---

### 📦 NPM (JavaScript / TypeScript)
**Allowed:**  
- `https://npm.pkg.github.com/@kfm/*`

**Forbidden:**  
- `https://registry.npmjs.org/*`  
- Any unscoped access

---

### 🦀 Cargo (Rust)
**Allowed:**  
- `source = "kfm-internal"`

**Forbidden:**  
- crates.io  
- Any fallback source

---

### ☕ Maven / Gradle (Java)
**Allowed:**  
- `kfm-mirror`

**Forbidden:**  
- `central.maven.org`  
- `repo1.maven.org`  
- All public Sonatype endpoints

---

### 📦 NuGet (.NET)
**Allowed:**  
- `https://nuget.kfm.internal/v3/index.json`

**Forbidden:**  
- `https://api.nuget.org/v3/index.json`

---

### 💎 RubyGems
**Allowed:**  
- `https://gems.kfm.internal/`

**Forbidden:**  
- `https://rubygems.org/`

---

## 🧱 Mandatory Isolation Rules

### 1. 🌐 Outbound Registry Firewall
All CI/CD execution must occur in hermetic containers:

- No outbound internet  
- No public DNS  
- No fallback  
- No auto-installers contacting public registries  

---

### 2. 🧩 Explicit Registry Declaration
All manifests MUST include:

- Full registry URL  
- Exact version  
- Exact hash/digest  

Implicit sources → **merge blocked**.

---

### 3. 🛑 Public Registry Denylist
The denylist covers:

- All public registries  
- Known malicious mirrors  
- High-risk namespace patterns  

Violation →  
**CI hard fail → Incident stub → Council review**

---

### 4. 🛰️ Registry Integrity Verification
Daily mirror audit includes:

- TLS pinning validation  
- Digest comparison vs sealed SBOM  
- Metadata drift detection  
- SLSA provenance validation  

Mismatch → **mirror quarantine + Fallback Tier 1 freeze**

---

### 5. 🔍 Drift & Rollback Controls
If drift is detected:

- Mirror quarantined  
- Local sealed cache used  
- Namespace blocklist escalated  

---

## 🧪 CI Enforcement

Enforced by:

- `registry-policy-check.yml`  
- `namespace-monitor.yml`  
- `dependency-integrity.yml`  
- `slsa-attestation-verify.yml`  
- `sbom-validate.yml`  

All violations → **merge blocked**.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                |
|----------|------------|------------------------------------------------------|
| v11.2.2  | 2025-11-30 | Directory layout moved up; full extended metadata    |
| v11.2.1  | 2025-10-04 | Drift/rollback rules added                           |
| v11.2.0  | 2025-09-08 | Initial registry-isolation draft                     |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 📏 [Enforcement Rules](./rules.md) • 🧭 [Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
