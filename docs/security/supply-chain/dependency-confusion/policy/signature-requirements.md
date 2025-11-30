---
title: "✍️ KFM v11.2.2 — Cryptographic Signature Requirements (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/signature-requirements.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Supply-Chain Security Council"
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
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"

doc_kind: "Security · Signature-Policy"
intent: "cryptographic-signature-enforcement · provenance-integrity"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Integrity · Security"
classification: "Security · Supply Chain · Cryptographic Policy"
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
sunset_policy: "Superseded by next cryptographic-policy revision"

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
  - "docs/security/supply-chain/dependency-confusion/policy/signature-requirements.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/policy/signature-requirements.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/policy/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:policy:signature-requirements:v11.2.2"
semantic_document_id: "kfm-depconf-policy-signature-v11.2.2"
event_source_id: "ledger:depconf.policy.signature.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "diagram-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🔐 Allowed Signing Mechanisms"
    - "📏 Mandatory Signature Requirements"
    - "🕰️ Version History"
---

<div align="center">

# ✍️ **Cryptographic Signature Requirements**  
`docs/security/supply-chain/dependency-confusion/policy/signature-requirements.md`

**Purpose:**  
Define the mandatory rules for cryptographic signing, verification, and provenance validation  
of all artifacts, dependencies, and build outputs in KFM v11.2.2.  
These rules ensure integrity, authenticity, reproducibility, and protection against  
dependency-confusion and malicious injection across the entire supply chain.

</div>

---

## 📘 Overview

KFM mandates **universal cryptographic verification** for:

- Dependency artifacts (pip / npm / cargo / Maven / NuGet / gem / Go)  
- Build outputs  
- Container images  
- SBOMs  
- Provenance attestations (SLSA)  
- Lockfiles  
- Git commits and annotated tags  

No unsigned or unverifiable artifacts may enter any KFM environment, including:

- CI/CD  
- Developer workstations  
- ETL pipelines  
- Knowledge graph ingestion  
- Release packaging  

All signatures must be:

- Deterministic  
- Tamper-evident  
- Verifiable offline  
- Linked into PROV-O provenance graphs  

---

## 🗂️ Directory Layout

~~~text
📁 policy/
├── 📄 README.md                 # High-level dependency-confusion policy
├── 📄 rules.md                  # Enforcement rules
├── 📄 registry-isolation.md     # Registry isolation policy
├── 📄 signature-requirements.md # This file — cryptographic requirements
├── 📄 fallback-controls.md      # Degraded-mode & emergency controls
├── 📄 exceptions.md             # SER-approved exceptions
├── 📄 incidents.md              # Incident log
└── 📂 evidence/
    ├── 🛰️ namespace-scan.json
    ├── 🧬 sbom-diff.json
    ├── 🔐 registry-audit.json
    └── 🧾 attestation-verify.json
~~~

---

## 🔐 Allowed Signing Mechanisms

KFM permits only the following cryptographic systems:

### ✓ Sigstore / Cosign
Used for:

- Container images  
- Build artifacts  
- Dependency bundles  
- Provenance attestations  

### ✓ GPG (Ed25519, RSA-4096)
Used for:

- Git commits  
- Annotated tags  
- Release bundles  
- Secure manifest signing  

### ✓ SHA-256 / SHA-512 Checksums
Used for:

- Lockfiles  
- SBOM artifacts  
- Dependency digests  
- Mirror integrity verification  

### ✓ SLSA Provenance Signing
Required for:

- Automated build chains  
- Minimum **SLSA Level 3** provenance  

---

## 📏 Mandatory Signature Requirements

### 1. 🧩 All Dependencies Must Be Signed
Every dependency MUST have:

- Verifiable registry signatures  
- Matching SBOM checksums  
- SLSA provenance (where supported)  

Unsigned or unverifiable dependencies → **blocked + quarantined**.

---

### 2. 🧾 All Git Commits Must Be Signed
All KFM developers MUST sign:

- Commits  
- Tags  
- Release pointers  

Unsigned commits → **CI rejection**.

---

### 3. 🗃️ All Build Artifacts Must Be Signed
Artifacts (wheels, jars, node bundles, crates, gemsets, containers) MUST:

- Carry a Cosign signature  
- Include provenance metadata  
- Pass digest verification  

Artifacts lacking required metadata → **quarantined**.

---

### 4. 🧬 All SBOMs Must Be Signed
SBOMs MUST:

- Include checksum lists  
- Be signed by build infrastructure  
- Be verified prior to artifact ingestion  
- Match lockfile digests  

SBOM drift → triggers Tier 1 fallback (see `fallback-controls.md`).

---

### 5. 🧪 CI/CD Must Verify All Signatures
CI MUST:

- Run Cosign verification  
- Validate GPG signatures  
- Compare digests  
- Validate SLSA provenance  

Signature failure → **merge blocked + incident recorded**.

---

### 6. 🧱 Lockfiles Must Be Hash-Sealed
Each lockfile MUST:

- Contain SHA-256 digests for all dependencies  
- Be associated with signed commits  
- Maintain immutable provenance linkage  

Lockfile mismatch → **immediate build halt**.

---

### 7. 🛡️ Mirror Integrity Signatures Required
Mirror synchronization MUST:

- Validate TLS pinning  
- Verify artifact digests and signatures  
- Reject unverifiable or unsigned artifacts  

Unverifiable mirrors → **quarantined automatically**, triggering fallback Tier 1.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                     |
|----------|------------|-----------------------------------------------------------|
| v11.2.2  | 2025-11-30 | Extended metadata; directory layout moved up; v11.2.2 alignment |
| v11.2.1  | 2025-10-10 | Added mandatory commit-signing + lockfile hash sealing    |
| v11.2.0  | 2025-09-05 | Initial cryptographic signature policy                    |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 🔒 [Registry Isolation](./registry-isolation.md) • 🧭 [Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
