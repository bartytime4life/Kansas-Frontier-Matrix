---
title: "🔍 KFM v11.2.2 — Local Scan Guidance for Dependency-Confusion Defense (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/checks/local-scan-guidance.md"
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
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
doc_kind: "Security · Local-Scan-Guidance"
---

<div align="center">

# 🔍 **Local Scan Guidance for Dependency-Confusion Defense**  
`docs/security/supply-chain/dependency-confusion/checks/local-scan-guidance.md`

**Purpose:**  
Provide step-by-step instructions for developers, security engineers, and CI maintainers to run  
manual/local dependency-confusion scans outside CI/CD.  
These checks replicate KFM-CI behavior locally to detect namespace collisions, pinning drift,  
signature failures, registry anomalies, and SBOM inconsistencies *before code is pushed*.

</div>

---

## 📘 Overview

While CI provides full enforcement, **local scanning empowers developers** to detect issues early.

Local scans allow you to:

- Validate dependency pinning  
- Detect registry-misconfiguration  
- Identify namespace collisions  
- Verify cryptographic signatures  
- Compare local dependency graphs against SBOM  
- Inspect potential typosquatting packages  
- Pre-run provenance hooks  
- Trigger fallback checks manually  

Local scans ensure development remains deterministic, compliant, and secure.

---

## 🧩 Local Scan Tooling Provided

KFM includes the following supported tools:

| Scan Type | Local Tool | Description |
|----------|------------|-------------|
| Namespace Collision | `kfm-ns-scan` | Scans public registries for KFM-like names |
| Registry Isolation | `kfm-reg-audit` | Validates registry URLs + TLS pinning |
| Pinning Integrity | `kfm-lock-verify` | Ensures lockfiles match SBOM & hash digests |
| SBOM Drift | `kfm-sbom-diff` | Compares current deps to last sealed SBOM |
| Provenance/Signatures | `kfm-provenance-verify` | Validates artifact & commit signatures |
| Fallback Mode | `kfm-fallback-test` | Simulates degraded mirror conditions |

These CLI tools run inside the KFM Developer Toolkit (KFM-DTK).

---

## 🔧 Installation (KFM Developer Toolkit)

Install via:

```bash
pip install kfm-dtk
```

Or from source:

```bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd tools/kfm-dtk
pip install -e .
```

> All local scans require Python ≥ 3.11.

---

## 🛰️ Running Local Namespace Scans

Detects public-package name collisions and suspicious variants.

```bash
kfm-ns-scan .
```

Flags:

- First-publish collisions  
- Typosquatting variants  
- Suspicious namespace permutations  
- Identical public names to internal packages  

Results saved to:

```
policy/evidence/namespace-scan.json
```

---

## 🔒 Checking Registry Isolation Locally

Validate that your environment uses **only** KFM-approved mirrors.

```bash
kfm-reg-audit --strict
```

Checks:

- No references to pypi.org / npmjs.org / crates.io  
- TLS pinning  
- Internal mirror whitelist  
- No fallback resolutions  

---

## 📦 Validating Dependency Pinning

```bash
kfm-lock-verify
```

This ensures:

- All deps are fully pinned  
- No floating versions  
- Lockfile matches SBOM  
- No cross-registry contamination  

---

## 🧬 Verifying SBOM Drift Locally

```bash
kfm-sbom-diff --local
```

Detects:

- Hash mismatches  
- Package additions/removals  
- Unapproved upgrades  
- Shadow artifacts  

---

## ✍️ Local Provenance & Signature Verification

```bash
kfm-provenance-verify --all
```

Validates:

- Cosign signatures  
- GPG signatures  
- Provenance metadata  
- SLSA attestations  

Unsigned components → ERROR + instructions to remediate.

---

## 🧯 Testing Fallback Activation

Simulates failing mirrors or metadata drift:

```bash
kfm-fallback-test
```

Triggers:

- Lockfile freeze  
- Local-only artifact mode  
- Registry quarantine simulation  

Use for debugging registry failures.

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 checks/
    ├── 📄 README.md                     # Automated checks index
    ├── 📄 ci-validation-rules.md        # CI validation rules
    ├── 📄 provenance-hooks.md           # Attestation/provenance hooks
    ├── 📄 registry-anomaly-detection.md # Registry anomaly detection rules
    ├── 📄 pre-commit-rules.md           # (optional) Developer-machine validation policies
    └── 📄 local-scan-guidance.md        # This file — manual/local scan guidance
~~~

---

## 🕰️ Version History

| Version | Date | Notes |
|---------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial creation of local/manual scan guidance |

---

<div align="center">

🧪 [Automated Checks](./README.md) • 🔒 [Registry Isolation](../policy/registry-isolation.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

