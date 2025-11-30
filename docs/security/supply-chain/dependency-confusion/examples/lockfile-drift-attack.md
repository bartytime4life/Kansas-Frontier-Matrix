---
title: "🗂️ KFM v11.2.2 — Lockfile Drift Attack (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/lockfile-drift-attack.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Security Council"
status: "Active · Educational Example"

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
doc_kind: "Security · Example"
---

<div align="center">

# 🗂️ **Lockfile Drift Attack Example**  
`docs/security/supply-chain/dependency-confusion/examples/lockfile-drift-attack.md`

**Purpose:**  
Demonstrate how **lockfile drift**—mismatches between lockfiles, SBOMs, and actual resolved  
artifacts—creates an opportunity for dependency-confusion attacks, shadow package injection,  
or execution of stale or malicious dependencies.  
This example is used for training developers and for automated CI/CD validation patterns.

</div>

---

## 📘 Background

A **lockfile drift attack** occurs when:

1. Lockfile contents **no longer match** the SBOM or dependency graph.
2. A resolver pulls updated or public versions inadvertently.
3. Hash, registry, or version mismatches go undetected.
4. Lockfiles are edited manually or by malicious actors.
5. A fallback or misconfigured environment silently ignores lockfile constraints.

Attackers exploit this by:

- Publishing a malicious version with the same name  
- Relying on resolver fallback to public registries  
- Exploiting missing or outdated hashes  
- Injecting new dependencies via subtle drift  
- Leveraging version precedence rules  

---

## 🧨 Example: Drift Introduced by a Malicious Commit

### 🔒 Expected Lockfile Entry
```yaml
kfm-math-tools:
  version: "2.4.1"
  registry: "https://kfm-pypi.internal/simple"
  hash: "sha256:4f0a81b9..."
```

### 💣 Malicious Modified Entry
```yaml
kfm-math-tools:
  version: "99.0.0"                # Attacker version
  registry: "https://pypi.org/simple"
  hash: "sha256:deadbeef..."       # Fake or attacker-generated digest
```

### ⚠️ Added Rogue Dependency
```yaml
kfm-math-tools-helper:
  version: "1.0.0"
  registry: "https://pypi.org/simple"
  hash: "sha256:aa11ccdd..."
```

This results in a resolver trying to fetch rogue dependencies that do not appear  
in the SBOM or internal registry inventory.

---

## 🧪 Simulated CI Detection Output

```text
[lockfile-verify]     ERROR: Lockfile does not match SBOM.
[digest-check]        ERROR: Hash mismatch on artifact for kfm-math-tools.
[namespace-monitor]   WARNING: Suspicious first-publish detected for helper package.
[sbom-validate]       ERROR: SBOM missing entries for rogue dependency.
[registry-policy]     FAIL: Public registry reference detected (pypi.org)
[policy]              FAIL: Lockfile drift attack detected.
```

Artifacts are immediately quarantined.

---

## 🚨 Why This Attack Works (in unprotected systems)

- Lockfiles not verified for hash or registry consistency  
- SBOM not integrated into CI/CD  
- Resolver ignores lockfile or partial lockfile entries  
- No namespace scanning  
- No checksum-based reproducibility requirements  
- No provenance metadata validation  

---

## 🛡️ How KFM v11.2.2 Prevents This Attack

### ✔ Lockfile Integrity Verification  
Every lockfile is validated for:

- Registry correctness  
- Version immutability  
- Hash reproducibility  
- SBOM alignment  
- Provenance linkage  

### ✔ SBOM Drift Checks  
Drift forces freeze mode:

- Dependency updates disabled  
- Only sealed dependencies allowed  
- Fallback Tier 1 activated if necessary  

### ✔ Registry Isolation Enforcement  
Public registries cannot be accessed under any circumstances.

### ✔ Namespace Collision Detection  
Rogue dependencies are immediately flagged.

### ✔ Provenance & Signature Requirements  
Malicious public packages cannot generate valid:

- Cosign signatures  
- SLSA provenance  
- Digest-matching SBOM entries  

### ✔ Pre-Commit Validation  
Developers caught before committing misaligned lockfiles.

---

## 🧭 Developer Guidance

To avoid lockfile drift:

- Never manually edit lockfiles  
- Regenerate lockfile + SBOM together  
- Use only KFM mirrors  
- Run pre-commit checks:
  ```bash
  kfm-lock-verify
  kfm-sbom-diff --local
  ```
- Report any drift warnings or namespace alerts  
- Treat lockfile drift as a critical security incident  

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
    ├── 📄 lockfile-drift-attack.md     # This file
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🕰️ Version History

| Version | Date       | Notes |
|---------|------------|--------|
| v11.2.2 | 2025-11-30 | Initial lockfile drift attack example |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [Version Race Example](./namespace-collision-versionrace.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

