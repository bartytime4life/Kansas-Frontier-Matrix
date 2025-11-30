---
title: "🧹 KFM v11.2.2 — Pre-Commit Validation Rules for Dependency-Confusion Defense (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/checks/pre-commit-rules.md"
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
doc_kind: "Security · Pre-Commit-Rules"
---

<div align="center">

# 🧹 **Pre-Commit Validation Rules for Dependency-Confusion Defense**  
`docs/security/supply-chain/dependency-confusion/checks/pre-commit-rules.md`

**Purpose:**  
Provide the mandatory local developer-side pre-commit validation rules that *must* run before  
any commit is allowed into the KFM monorepo.  
These rules prevent dependency-confusion vulnerabilities from being introduced during  
development by ensuring pinning discipline, registry isolation, lockfile integrity, signature checks,  
and SBOM consistency **before code ever reaches CI**.

</div>

---

## 📘 Overview

Pre-commit validation is the **developer-side enforcement layer** of KFM’s supply-chain defense.  
It mirrors CI behavior with *local-only checks* that:

- Detect unpinned dependencies  
- Identify registry-misconfigurations  
- Flag namespace-collision hazards  
- Validate cryptographic signatures  
- Prevent SBOM drift from entering PRs  
- Ensure hermetic development environments  
- Block commits lacking provenance metadata  
- Trigger fallback logic in degraded developer environments  

Pre-commit rules are always active and cannot be bypassed.

Local compliance ensures deterministic development and reduces CI churn.

---

## 🛠️ Required Tools (KFM-DTK)

All checks use the **KFM Developer Toolkit (DTK)**:

```
pip install kfm-dtk
```

Provides the following commands:

- `kfm-ns-scan` – Namespace collision detection  
- `kfm-reg-audit` – Registry isolation validation  
- `kfm-lock-verify` – Pinning & lockfile integrity  
- `kfm-sbom-diff` – SBOM drift detection  
- `kfm-provenance-verify` – Signature enforcement  
- `kfm-fallback-test` – Local fallback simulation  

---

## 🧹 Mandatory Pre-Commit Rule Set

### 1. 🧩 Exact Pinning & Lockfile Integrity
Before commit:

- All dependencies MUST be fully pinned  
- Lockfiles must include registry + version + digest  
- Lockfile must match SBOM  
- No floating deps  
- No cross-registry substitutions  

Command:

```bash
kfm-lock-verify
```

Commit blocked if:

- Lockfile changed without SBOM regeneration  
- Dependencies lack hash integrity  
- Registry mismatch detected

---

### 2. 🔒 Registry Isolation Check
Ensures no accidental public-registry usage.

Checks for:

- pypi.org  
- registry.npmjs.org  
- crates.io  
- Maven Central  
- NuGet public endpoints  

Run:

```bash
kfm-reg-audit --strict
```

Commit blocked on *any external registry reference*.

---

### 3. 🛰️ Namespace Collision Pre-Scan
Searches all public registries for KFM-like names.

Run:

```bash
kfm-ns-scan .
```

Blocks commit when:

- Similar public package exists  
- Dangerous namespace patterns detected  
- Typosquatting variants found  

Warns developer to file a Security Block Declaration (SBD).

---

### 4. ✍️ Signature & Provenance Verification
Ensures developer environment has valid:

- GPG commit signing  
- Verified Cosign signatures (for local artifacts)  
- Matching provenance metadata for modified components  

Run:

```bash
kfm-provenance-verify --local
```

Commit blocked if:

- Any signature invalid  
- Any artifact unverifiable  
- SLSA metadata missing  

---

### 5. 🧬 Local SBOM Drift Check
Ensures no unapproved dependency modifications.

Run:

```bash
kfm-sbom-diff --local
```

Commit is **rejected** when:

- New dependency appears outside policy  
- Digest mismatch detected  
- Lockfiles changed without matching SBOM update  

---

### 6. 🧱 Hermetic Sandbox Validation
Ensures developer environments mimic CI hermeticity as closely as possible.

Checks:

- No outbound registry traffic  
- No auto-installer plugins  
- No implicit fallback to public registries  
- No dynamic version resolution  

Triggered via:

```bash
kfm-fallback-test --validate
```

---

### 7. 🧭 Governance Constraint Validation
Ensures:

- Any dependency requiring exception is listed in `exceptions.md`  
- Expired SERs prevent commit  
- All policy documents are schema-valid  
- Modified policy files include updated YAML headers  

Run automatically via:

```bash
kfm-governance-validate
```

---

## 🔧 Installing Pre-Commit Hook

Add to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: kfm-precommit
        name: KFM Dependency-Confusion Precommit
        entry: tools/kfm-dtk/hooks/kfm-precommit.sh
        language: system
        pass_filenames: false
```

Then activate:

```bash
pre-commit install
```

This ensures rules run automatically on every commit.

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 checks/
    ├── 📄 README.md                     # Automated checks index
    ├── 📄 ci-validation-rules.md        # CI validation rules
    ├── 📄 provenance-hooks.md           # Attestation/provenance hooks
    ├── 📄 registry-anomaly-detection.md # Registry anomaly detection logic
    ├── 📄 pre-commit-rules.md           # This file — developer-side enforcement rules
    └── 📄 local-scan-guidance.md        # Manual/local scan instructions
~~~

---

## 🕰️ Version History

| Version | Date | Notes |
|---------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial creation of Pre-Commit dependency-confusion ruleset |

---

<div align="center">

🧪 [Automated Checks](./README.md) • 🧬 [Provenance Hooks](./provenance-hooks.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

