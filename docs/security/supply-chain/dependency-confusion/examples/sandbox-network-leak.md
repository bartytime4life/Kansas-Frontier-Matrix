---
title: "🌐 KFM v11.2.2 — Sandbox Network Leak (Hermeticity Violation Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/sandbox-network-leak.md"
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

# 🌐 **Sandbox Network Leak Example**  
`docs/security/supply-chain/dependency-confusion/examples/sandbox-network-leak.md`

**Purpose:**  
Demonstrate how a **network leak inside a CI or development sandbox** can cause silent  
dependency-confusion compromises by allowing outbound requests to public registries,  
plugin installers, or update services — all of which should be forbidden under KFM v11.2.2  
hermeticity guarantees.

</div>

---

## 📘 Background

A **sandbox network leak** happens when:

1. A build or test environment unexpectedly has outbound network access.  
2. A dependency resolver or auto-installer contacts a public registry.  
3. Public malicious versions replace internal pinned dependencies.  
4. Plugin auto-installers fetch vulnerable or outdated tooling.  
5. SBOM and provenance controls are bypassed in non-hermetic phases.  

Leaks occur due to:

- Misconfigured CI runners  
- Incorrect container sandboxing  
- Network proxy bypass  
- Auto-update plugins  
- “Smart” build tools resolving dependencies dynamically  
- Hidden transitive installation scripts  

This attack surfaces frequently in ecosystems like npm, pip, and Gradle.

---

## 🌐 Example Scenario

### 🏛 Expected (Hermetic) Sandbox Behavior
```
- Zero outbound network access
- Only internal mirrors allowed
- No DNS resolution to public servers
- No plugin auto-installation
```

### 💣 Vulnerable / Misconfigured Sandbox Behavior
The sandbox **incorrectly** allows outbound connections:

```
sandbox> ping pypi.org
64 bytes from 151.101.x.x...
sandbox> curl https://registry.npmjs.org/
{ "ok": false, ... }
```

### 🚨 Real Attack Example
During a pip install:

```
pip install kfm-geo-core --timeout 5
```

Internal mirror fails due to temporary outage:

```
ERROR: Timeout contacting https://kfm-pypi.internal/simple
```

Resolver silently falls back:

```
Trying https://pypi.org/simple
Found kfm-geo-core v97.0.0
Installing...
```

A malicious package is installed, bypassing all protections.

---

## 🧪 Simulated CI Detection Output

```text
[hermetic-build-guard] ERROR: Outbound network detected: pypi.org
[registry-policy-check] FAIL: Public registry contacted during sandboxed build.
[namespace-monitor]   WARNING: Public publish spike detected for "kfm-geo-core".
[attestation-verify]  ERROR: No valid SLSA provenance for installed dependency.
[sbom-validate]       ERROR: SBOM mismatch with expected dependency graph.
[policy]              FAIL: sandbox-network-leak detected — security quarantine activated.
```

Evidence recorded:

- `policy/evidence/registry-audit.json`
- `policy/evidence/namespace-scan.json`

---

## 🚨 Why This Attack Works (in unprotected systems)

- Sandbox not hermetic  
- Outbound network allowed  
- Resolver fallback enabled  
- No strict mirror isolation  
- Lockfiles ignored  
- No SBOM enforcement  
- No provenance validation  
- Plugin auto-installers allowed to fetch packages  

---

## 🛡️ How KFM v11.2.2 Prevents Network Leak Attacks

### ✔ Hermetic Sandbox Enforcement  
Sandbox receives ZERO outbound connectivity.

### ✔ Registry Isolation  
Even if network leak exists, registries outside KFM mirrors are blocked.

### ✔ Deterministic Pinning  
Resolver cannot fetch unexpected versions.

### ✔ SBOM Locking  
Drift triggers freeze mode.

### ✔ Provenance Enforcement  
Malicious public packages lack valid signatures/provenance.

### ✔ Evidence-Based Quarantine  
Any leak event → immediate build halt + quarantine.

### ✔ Pre-Commit Local Sandbox Test  
Developers can validate using:

```bash
kfm-fallback-test --validate
```

---

## 🧭 Developer Guidance

To avoid network leak vulnerabilities:

- Validate no outbound traffic:
  ```bash
  kfm-reg-audit --strict
  ```
- Disable all auto-installers/plugins.
- Audit Dockerfiles for unintended network dependencies.
- Ensure CI runner images enforce hermetic mode.
- Treat all leak detections as **critical security incidents**.

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
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md    # This file
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🕰️ Version History

| Version | Date       | Notes |
|---------|------------|--------|
| v11.2.2 | 2025-11-30 | Initial sandbox network leak example |

---

<div align="center">

📚 [Examples Index](./README.md) • ⛓️ [Registry Fallback](./registry-fallback.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

