---
title: "🧬 KFM v11.2.2 — Provenance Hooks & Attestation Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/checks/provenance-hooks.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Supply-Chain Security Council"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/security-v3.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
doc_kind: "Security · Provenance"
---

<div align="center">

# 🧬 **Provenance Hooks & Attestation Rules**  
`docs/security/supply-chain/dependency-confusion/checks/provenance-hooks.md`

**Purpose:**  
Define the full set of provenance hooks, SLSA verification steps, and attestation requirements  
enforced by CI/CD to protect KFM from dependency-confusion, rogue artifact injection, SBOM drift,  
and upstream registry compromise.

These hooks provide cryptographic, reproducible, end-to-end assurance that every dependency  
and artifact originates from a trusted, verified, SLSA-compliant pipeline.

</div>

---

## 📘 Overview

KFM v11.2.2 implements a **multi-hook provenance verification architecture**, embedding security controls  
at all critical points of the software supply chain:

- Pre-fetch  
- Fetch/resolve  
- Build  
- Package  
- Sign  
- Publish  
- SBOM generate  
- Release seal  

Each hook is deterministic and tied to:

- SLSA-Level ≥ 3 provenance  
- Cosign signatures  
- GPG enforcement  
- Immutable evidence logs  
- FAIR+CARE provenance metadata  

Provenance hooks run in CI/CD, developer pre-commit layers, and ingestion pipelines.

---

## 🧬 Provenance Hook Categories

### 1. 🧩 Pre-Fetch Provenance Hook (PF-Hook)
Executed before dependency retrieval.

Validates:

- Manifest integrity  
- Registry allow-list compliance  
- SER exception boundaries  
- Lockfile digests  
- Provenance chain of prior build  

Blocks dependency resolution until all checks pass.

---

### 2. 📦 Fetch-Time Provenance Hook (FT-Hook)
Executed at the moment the dependency resolver contacts a registry or mirror.

Enforces:

- TLS certificate pinning  
- Cosign signature validation  
- Registry isolation  
- Digest pre-validation  
- Namespace blacklist/denylist enforcement  

Produces evidence:  
`policy/evidence/registry-audit.json`

---

### 3. 🏗️ Build-Time Provenance Hook (BT-Hook)
Executed during compilation/build.

Enforces:

- Hermetic sandboxing  
- Zero outbound network activity  
- Deterministic builds  
- No dependency drift  
- SLSA build provenance validation  

Produces evidence:  
`policy/evidence/attestation-verify.json`

---

### 4. 📦 Artifact-Packaging Provenance Hook (AP-Hook)
Executed during bundling of wheels, jars, crates, npm packs, gemsets, etc.

Checks:

- Artifact digests  
- Cosign signatures  
- Internal registry rewrite  
- SBOM inclusion for all dependencies  

Invalid signatures → **quarantine**.

---

### 5. ✍️ Signing & Attestation Hook (SA-Hook)
Executed after packaging.

Requires:

- Cosign signing of containers & artifacts  
- GPG signing of tags + commits  
- SLSA attestation generation  
- Provenance chain linkage to lockfiles & SBOMs  
- Timestamped verifiable signature bundle  

Failure → **build halt + incident stub**.

---

### 6. 🗃️ SBOM & Metadata Verification Hook (SBOM-Hook)
Executed after SBOM generation.

Checks:

- Digest matching between SBOM and actual artifacts  
- License metadata consistency  
- Provenance metadata correctness  
- No unapproved dependency additions  
- No digests missing or unverifiable  

Produces evidence:  
`policy/evidence/sbom-diff.json`

---

### 7. 🚀 Release Sealing Hook (RS-Hook)
Executed during final release build.

Enforces:

- SBOM freeze & seal  
- SLSA attestation freeze  
- Cosign signature seal  
- Provenance graph merge  
- Release manifest signing  
- Build metadata write-back to ledger  

Final output is an immutable, fully verifiable release bundle.

---

## 🧬 Provenance Evidence Outputs

Provenance hooks write to:

```
docs/security/supply-chain/dependency-confusion/policy/evidence/
```

Files include:

- 🛰️ `namespace-scan.json`  
- 🔐 `registry-audit.json`  
- 🧬 `sbom-diff.json`  
- 🧾 `attestation-verify.json`  
- 🗄️ `provenance-graph.json` (optional extensions)

All evidence must be:

- FAIR+CARE compliant  
- Timestamped  
- Immutable  
- Schema-validated  
- Linked by PROV-O lineage  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 checks/
    ├── 📄 README.md                    # Automated checks overview
    ├── 📄 ci-validation-rules.md       # CI validation rules
    ├── 📄 provenance-hooks.md          # This file — provenance/attestation hooks
    ├── 📄 pre-commit-rules.md          # (optional) Developer-machine hooks
    └── 📄 local-scan-guidance.md       # (optional) Manual scanning procedures
~~~

---

## 🕰️ Version History

| Version | Date | Notes |
|---------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial creation of provenance hooks & attestation rule set |

---

<div align="center">

🧪 [Automated Checks](./README.md) • ✍️ [Signature Requirements](../policy/signature-requirements.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

