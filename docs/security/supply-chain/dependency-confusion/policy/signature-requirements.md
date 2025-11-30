---
title: "✍️ KFM v11.2.2 — Cryptographic Signature Requirements (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/signature-requirements.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Supply-Chain Security Council"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/security-v3.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"
doc_kind: "Security · Signature-Policy"
---

<div align="center">

# ✍️ **Cryptographic Signature Requirements**  
`docs/security/supply-chain/dependency-confusion/policy/signature-requirements.md`

**Purpose:**  
Define mandatory requirements for cryptographic signing, verification, and provenance validation  
of all artifacts, dependencies, and build outputs within KFM v11.2.2.  
These requirements ensure integrity, authenticity, reproducibility, and prevent dependency-confusion  
or malicious injection across the entire supply chain.

</div>

---

## 📘 Overview

KFM mandates **universal cryptographic verification** for:

- Dependency artifacts (pip/npm/cargo/maven/nuget/gem/go)
- Build outputs
- Container images
- SBOMs
- Provenance attestations (SLSA)
- Lockfiles
- Git commits and annotated tags

No unsigned or unverifiable artifacts may enter any KFM environment, including:

- CI/CD  
- Developer machines  
- ETL pipelines  
- Graph ingestion  
- Release packaging  

All signatures must be reproducible, tamper-evident, and verifiable offline.

---

## 🔐 Allowed Signing Mechanisms

KFM permits only the following cryptographic systems:

### ✓ Sigstore / Cosign
- For container images  
- For provenance attestations  
- For build artifacts  
- For dependency bundles  

### ✓ GPG (Ed25519, RSA-4096)
- For Git commits  
- For annotated tags  
- For release bundles  
- For secure manifest signing  

### ✓ SHA-256 / SHA-512 Checksums
- For lockfiles  
- For SBOM artifacts  
- For dependency digests  
- For mirror integrity checks  

### ✓ SLSA Provenance Signing
- For automated build chains  
- Requires Level ≥ 3  

---

## 📏 Mandatory Signature Requirements

### 1. 🧩 All Dependencies Must Be Signed  
Every dependency MUST include:

- Verified registry signature  
- SBOM checksum match  
- SLSA provenance signature (if supported by ecosystem)  

Unsigned deps → **blocked**.

---

### 2. 🧾 All Git Commits Must Be Signed (GPG or Sigstore)
All KFM developers must sign:

- Commits  
- Tags  
- Release references  

Unsigned commits → **rejected via CI**.

---

### 3. 🗃️ All Build Artifacts Must Be Signed
Artifacts (wheels, jars, node bundles, crates, gemsets, containers) must include:

- Cosign signature  
- Provenance metadata  
- Digest verification  

Artifacts lacking any required metadata → **quarantined**.

---

### 4. 🧬 All SBOMs Must Be Signed
SBOMs MUST:

- Include checksum lists  
- Be signed by build infrastructure  
- Be verified during artifact ingestion  
- Match lockfile digests  

SBOM drift → triggers fallback-controls Tier 1.

---

### 5. 🧪 CI/CD Must Verify All Signatures
CI enforcement includes:

- Cosign verify step  
- GPG signature checks  
- Digest comparison  
- SLSA provenance validation  

Signature failure → merge blocked + incident logged.

---

### 6. 🧱 Lockfiles Must Be Hash-Sealed
Each lockfile MUST include:

- SHA-256 digests for all dependencies  
- Cryptographically signed commit history  
- Immutable provenance linkage  

Lockfile mismatch → **immediate build halt**.

---

### 7. 🛡️ Mirror Integrity Signatures Required
Mirror actions MUST include:

- TLS pinning  
- Digest checks  
- Signature validation for mirrored artifacts  

Unverifiable mirrors → quarantined automatically.

---

## 🗂️ Directory Layout

~~~text
📁 policy/
├── 📄 README.md                 # High-level dependency-confusion policy
├── 📄 rules.md                  # Enforcement rules
├── 📄 registry-isolation.md     # Registry isolation policy
├── 📄 signature-requirements.md # This file — cryptographic requirements
├── 📄 exceptions.md             # SER-approved exceptions
├── 📄 incidents.md              # Incident register
└── 📂 evidence/
    ├── 🛰️ namespace-scan.json
    ├── 🧬 sbom-diff.json
    ├── 🔐 registry-audit.json
    └── 🧾 attestation-verify.json (optional)
~~~

---

## 🕰️ Version History

| Version | Date | Notes |
|--------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial cryptographic signature requirements created |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 🔒 [Registry Isolation](./registry-isolation.md) • 🧭 [Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

