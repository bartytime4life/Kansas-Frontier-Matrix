---
title: "📌 KFM v11.2.2 — Dependency Version Pinning Policy (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/version-pinning.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Supply-Chain Security Council · FAIR+CARE"
content_stability: "stable"
status: "Active · Enforced"

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
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"

doc_kind: "Security · Version-Pinning"
intent: "deterministic-dependency-resolution · supply-chain-hardening"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Protection of Critical Infrastructure"
classification: "Security · Dependency Integrity"
sensitivity: "Security-Sensitive (non-personal)"
sensitivity_level: "High"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "High"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next dependency-policy revision"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

metadata_profiles:
  - "FAIR+CARE"
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "PROV-O"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/policy/version-pinning.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/policy/version-pinning.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/policy/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:policy:version-pinning:v11.2.2"
semantic_document_id: "kfm-depconf-policy-versionpinning-v11.2.2"
event_source_id: "ledger:depconf.policy.versionpinning.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "timeline-generation"
  - "diagram-extraction"

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
    - "📌 Mandatory Version-Pinning Rules"
    - "🧪 CI Enforcement Requirements"
    - "🕰️ Version History"
---

<div align="center">

# 📌 **KFM v11.2.2 — Dependency Version Pinning Policy**  
`docs/security/supply-chain/dependency-confusion/policy/version-pinning.md`

**Purpose:**  
Ensure all KFM dependencies resolve deterministically, reproducibly, and securely —  
eliminating floating versions, mismatched resolution behavior, and all ambiguity exploited  
by dependency-confusion attackers.

</div>

---

## 📘 Overview

Version pinning is the backbone of KFM’s supply-chain integrity model.

KFM v11.2.2 requires all dependency versions to be:

- **Exact** (`"3.8.0"` NOT `^3.8`, `~3.8`, `>=3.8,<4.0`)  
- **Registry-scoped** (explicit URL, NOT resolver defaults)  
- **Digest-locked** (hash integrity required)  
- **SBOM-aligned** (verified against sealed SBOM entries)  
- **Provenance-validated** (SLSA ≥3 where supported)  

Any deviation breaks reproducibility and exposes the ecosystem to:

- First-publish hijacks  
- Version-race overrides  
- Typosquat escalations  
- Registry fallback attacks  
- Unsigned artifact injection  
- SBOM drift  

Version pinning is **non-optional**, **CI-enforced**, and **governance-audited**.

---

## 🗂️ Directory Layout

~~~text
📁 policy/
├── 📄 README.md                 # Top-level dependency-confusion policy
├── 📄 rules.md                  # Enforcement rules
├── 📄 registry-isolation.md     # Registry isolation requirements
├── 📄 signature-requirements.md # Cryptographic policy
├── 📄 fallback-controls.md      # Degraded-mode behaviors
├── 📄 version-pinning.md        # This file — version pinning policy
├── 📄 exceptions.md             # Governance-approved SER exceptions
├── 📄 incidents.md              # Incident register
└── 📂 evidence/
    ├── 🛰️ namespace-scan.json
    ├── 🧬 sbom-diff.json
    ├── 🔐 registry-audit.json
    └── 🧾 attestation-verify.json
~~~

---

## 📌 Mandatory Version-Pinning Rules

### 1. 🔒 Exact Version Locking
All dependencies MUST specify **exact semantic versions**:

- `"3.8.0"`  
- `"5.2.1"`  
- `"0.7.14"`  

❌ Floating forms prohibited:

- `^3.8.0`  
- `~3.8`  
- `>=3.8,<4.0`  
- `latest`  
- `*`  

### 2. 🌐 Registry-Scoped Pinning
Every dependency MUST include its **full registry URL**.

Examples:

- pip → `https://kfm-pypi.internal/simple`  
- npm → `https://npm.pkg.github.com/@kfm/*`  
- cargo → `source = "kfm-internal"`  

### 3. 🔑 Digest-Locked Artifacts
Each dependency MUST include:

- SHA-256 or SHA-512 integrity hash  
- Matching sealed SBOM digest  
- Verified registry signature  

Hash mismatch → **CI hard fail**.

### 4. 🧩 Lockfile Hardening
Lockfiles MUST:

- Include full registry URLs  
- Include hash digests  
- Be SBOM-verified  
- Be tied to signed commits  

Lockfile drift → **merge blocked**.

### 5. 🧬 SBOM Alignment
A dependency is valid ONLY if:

- SBOM digest matches  
- SBOM entry matches registry version + URL + hash  
- Provenance metadata is available  

Missing SBOM entries → **quarantine + incident stub**.

### 6. 🛰️ Provenance Validation (SLSA ≥3)
Where supported by tooling:

- Dependencies MUST include a SLSA provenance bundle  
- CI MUST verify the chain  

Missing provenance → **dependency rejected**.

### 7. 🧯 No Transitive Floating Dependencies
Transitive dependencies MUST also be pinned.  
Transient floating versions cause CI failure.

---

## 🧪 CI Enforcement Requirements

CI MUST validate:

- Exact-version pinning  
- Registry isolation (no public endpoints)  
- Hash integrity  
- SBOM consistency  
- Provenance metadata  
- Namespace-collision scanning  
- Lockfile immutability  
- No silent upgrades  

CI failing any rule → **merge blocked**.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                                   |
|----------|------------|-------------------------------------------------------------------------|
| v11.2.2  | 2025-11-30 | Full extended metadata; layout moved; rules aligned with v11.2.2        |
| v11.2.1  | 2025-10-12 | Added strict transitive-pinning requirement                              |
| v11.2.0  | 2025-09-04 | Initial draft                                                            |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 🔒 [Registry Isolation](./registry-isolation.md) • 🧭 [Governance](../../../../../standards)

